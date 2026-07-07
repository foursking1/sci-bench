from __future__ import annotations

import json
import shutil
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .schema import CollectorResult, DiscoveredFile, EvalConfig, EvidenceEntry


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def deep_merge(dst: dict[str, Any], src: dict[str, Any]) -> dict[str, Any]:
    for key, value in src.items():
        if isinstance(value, dict) and isinstance(dst.get(key), dict):
            deep_merge(dst[key], value)
        else:
            dst[key] = value
    return dst


def deep_merge_missing(dst: dict[str, Any], src: dict[str, Any]) -> dict[str, Any]:
    """Merge src into dst without overwriting existing leaf values.

    Collectors run from most deterministic to most semantic. Later collectors
    should fill gaps, not replace earlier exact measurements.
    """
    for key, value in src.items():
        if key not in dst:
            dst[key] = value
        elif isinstance(value, dict) and isinstance(dst.get(key), dict):
            deep_merge_missing(dst[key], value)
    return dst


def build_extraction_spec(truth_spec: Any) -> list[dict[str, Any]]:
    spec: list[dict[str, Any]] = []
    for rule in truth_spec.rules:
        entry = {
            "rule_id": rule.rule_id,
            "type": rule.type,
            "description": rule.description,
            "confidence_weight": rule.confidence_weight,
        }
        if rule.target_path:
            entry["target_path"] = rule.target_path
        if rule.comparison:
            entry["comparison"] = rule.comparison
        if rule.type == "figure":
            entry["fuzzy_match"] = rule.fuzzy_match
            entry["judge_threshold"] = rule.judge_threshold
        spec.append(entry)
    return spec


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def build_artifacts(
    config: EvalConfig,
    truth_spec: Any,
    discovered: list[DiscoveredFile],
    collector_results: list[CollectorResult],
) -> dict[str, Path]:
    config.output_dir.mkdir(parents=True, exist_ok=True)

    metrics: dict[str, Any] = {
        "paper_id": config.paper_id,
        "run_status": "success",
        "primary_claims_tested": [claim.get("id", "") for claim in truth_spec.claims if claim.get("id")],
    }
    evidence_by_rule: dict[str, EvidenceEntry] = {}
    notes: list[str] = []

    for result in collector_results:
        deep_merge_missing(metrics, result.metrics)
        notes.extend(result.notes)
        for entry in result.evidence:
            existing = evidence_by_rule.get(entry.rule_id)
            if existing and existing.evidence_status == "evidence_found":
                continue
            evidence_by_rule[entry.rule_id] = entry

    # If an agent provides a scalar value for a rule with target_path, store it
    # under the exact truth path. This mirrors the legacy collect_agent builder
    # and prevents agents from needing to know every nested metrics convention.
    rules_by_id = {rule.rule_id: rule for rule in truth_spec.rules}
    for entry in evidence_by_rule.values():
        rule = rules_by_id.get(entry.rule_id)
        if not rule or not rule.target_path or entry.extracted_value is None:
            continue
        if isinstance(entry.extracted_value, (dict, list)):
            continue
        if not has_dotted(metrics, rule.target_path):
            set_dotted(metrics, rule.target_path, entry.extracted_value)

    all_evidence = []
    for rule in truth_spec.rules:
        entry = evidence_by_rule.get(
            rule.rule_id,
            EvidenceEntry(rule.rule_id, "no_evidence", None, "", 0.0, "No collector produced evidence for this rule."),
        )
        all_evidence.append(asdict(entry))

    manifest = {
        "paper_id": config.paper_id,
        "run_status": "success" if all(e["evidence_status"] == "evidence_found" for e in all_evidence) else "partial",
        "steps_completed": sorted({part for e in all_evidence for part in Path(e.get("source_file") or "").parts if part.startswith("P")}),
        "summary": f"Extracted {sum(e['evidence_status'] == 'evidence_found' for e in all_evidence)}/{len(all_evidence)} verification rules",
        "generated_at_utc": now_utc(),
        "artifacts": {
            "metrics": "artifacts/metrics.json",
            "log": "artifacts/run.log",
            "figures": "artifacts/figures/",
        },
        "collector_notes": notes,
    }
    collect_report = {
        "paper_id": config.paper_id,
        "evaluated_at_utc": now_utc(),
        "truth_md": str(config.truth.relative_to(config.repo_root) if config.truth.is_relative_to(config.repo_root) else config.truth),
        "rules_evaluated": all_evidence,
        "summary": {
            "total_rules": len(all_evidence),
            "evidence_found": sum(e["evidence_status"] == "evidence_found" for e in all_evidence),
            "no_evidence": sum(e["evidence_status"] == "no_evidence" for e in all_evidence),
            "extract_failed": sum(e["evidence_status"] == "extract_failed" for e in all_evidence),
            "mean_mapping_confidence": round(
                sum(e["mapping_confidence"] for e in all_evidence if e["mapping_confidence"] > 0)
                / max(1, sum(1 for e in all_evidence if e["mapping_confidence"] > 0)),
                2,
            ),
        },
    }
    run_log = "\n".join(
        [
            f"repro_eval_framework run for paper {config.paper_id}",
            f"timestamp: {now_utc()}",
            f"truth_md: {config.truth}",
            f"source_dir: {config.reproduce_dir}",
            f"rules_count: {len(truth_spec.rules)}",
            "",
            *[
                f"[{'FOUND' if e['evidence_status'] == 'evidence_found' else 'MISSING'}] {e['rule_id']}: {e['notes']}"
                for e in all_evidence
            ],
            "",
            f"Summary: {collect_report['summary']['evidence_found']}/{len(all_evidence)} rules have evidence",
            "EXPORT_SUCCESS",
            "",
        ]
    )

    write_json(config.output_dir / "metrics.json", metrics)
    write_json(config.output_dir / "manifest.json", manifest)
    write_json(config.output_dir / "collect_report.json", collect_report)
    write_json(config.output_dir / "extraction_spec.json", build_extraction_spec(truth_spec))
    (config.output_dir / "run.log").write_text(run_log, encoding="utf-8")

    if config.preserve_sources:
        preserve_sources(config, discovered)

    return {
        "metrics": config.output_dir / "metrics.json",
        "manifest": config.output_dir / "manifest.json",
        "collect_report": config.output_dir / "collect_report.json",
        "run_log": config.output_dir / "run.log",
    }


def preserve_sources(config: EvalConfig, discovered: list[DiscoveredFile]) -> None:
    root = config.output_dir / "source_files"
    if root.exists():
        shutil.rmtree(root)
    for item in discovered:
        source = config.reproduce_dir / item.path
        if not source.is_file():
            continue
        target = root / item.path
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def set_dotted(payload: dict[str, Any], dotted_path: str, value: Any) -> None:
    cur = payload
    parts = dotted_path.split(".")
    for part in parts[:-1]:
        cur = cur.setdefault(part, {})
    cur[parts[-1]] = value


def has_dotted(payload: dict[str, Any], dotted_path: str) -> bool:
    cur: Any = payload
    for part in dotted_path.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return False
        cur = cur[part]
    return True
