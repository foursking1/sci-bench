from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

import yaml

from .config import load_config
from .pipeline import evaluate


def load_manifest(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as f:
        manifest = yaml.safe_load(f) or {}
    if "papers" not in manifest or not isinstance(manifest["papers"], list):
        raise ValueError("manifest must contain a papers list")
    return manifest


def iter_paper_configs(
    manifest_path: Path,
    *,
    paper_ids: set[str] | None = None,
    limit: int | None = None,
    no_agent: bool = False,
    agent_timeout: int | None = None,
) -> list[Any]:
    manifest = load_manifest(manifest_path)
    base = manifest_path.parent.parent if manifest_path.parent.name == "dataset" else Path.cwd()
    defaults = dict(manifest.get("defaults") or {})
    papers = manifest["papers"]
    selected = []

    for paper in papers:
        paper_id = str(paper.get("paper_id", ""))
        if paper_ids and paper_id not in paper_ids:
            continue
        merged = merge_dicts(defaults, paper)
        output_root = Path(merged.pop("output_root", "artifacts_v2_framework_batch"))
        if not output_root.is_absolute():
            output_root = Path.cwd() / output_root
        merged.setdefault("output_dir", str(output_root / paper_id))
        merged.setdefault("repo_root", ".")
        if no_agent:
            merged["agent"] = {"enabled": False}
        elif agent_timeout is not None:
            merged.setdefault("agent", {})
            merged["agent"]["timeout"] = agent_timeout
        selected.append(load_config(Path(), merged))
        if limit is not None and len(selected) >= limit:
            break
    return selected


def merge_dicts(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    result = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = merge_dicts(result[key], value)
        else:
            result[key] = value
    return result


def run_batch(
    manifest_path: Path,
    *,
    paper_ids: set[str] | None = None,
    limit: int | None = None,
    no_agent: bool = False,
    agent_timeout: int | None = None,
) -> dict[str, Any]:
    configs = iter_paper_configs(
        manifest_path,
        paper_ids=paper_ids,
        limit=limit,
        no_agent=no_agent,
        agent_timeout=agent_timeout,
    )
    results = []
    for config in configs:
        try:
            result = evaluate(config)
            score = result.get("score_report") or {}
            results.append(
                {
                    "paper_id": config.paper_id,
                    "status": "ok",
                    "output_dir": str(config.output_dir),
                    "paper_score": score.get("paper_score"),
                    "paper_score_weighted": score.get("paper_score_weighted"),
                    "confidence": score.get("confidence"),
                    "anti_cheat": (score.get("anti_cheat") or {}).get("anti_cheat_overall"),
                    "failed_rules": ",".join(rule["rule_id"] for rule in score.get("rules", []) if not rule.get("passed")),
                    "error": "",
                }
            )
        except Exception as exc:
            results.append(
                {
                    "paper_id": config.paper_id,
                    "status": "error",
                    "output_dir": str(config.output_dir),
                    "paper_score": None,
                    "paper_score_weighted": None,
                    "confidence": None,
                    "anti_cheat": None,
                    "failed_rules": "",
                    "error": str(exc),
                }
            )

    output_root = Path.cwd() / "artifacts_v2_framework_batch"
    if configs:
        output_root = configs[0].output_dir.parent
    output_root.mkdir(parents=True, exist_ok=True)
    summary_json = output_root / "summary.json"
    summary_csv = output_root / "summary.csv"
    summary_md = output_root / "summary.md"

    payload = {"manifest": str(manifest_path), "count": len(results), "results": results}
    summary_json.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_summary_csv(summary_csv, results)
    write_summary_md(summary_md, results)
    return {"summary_json": str(summary_json), "summary_csv": str(summary_csv), "summary_md": str(summary_md), "results": results}


def write_summary_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = ["paper_id", "status", "paper_score", "paper_score_weighted", "confidence", "anti_cheat", "failed_rules", "output_dir", "error"]
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def write_summary_md(path: Path, rows: list[dict[str, Any]]) -> None:
    lines = [
        "# Batch Evaluation Summary",
        "",
        "| Paper | Status | Score | Weighted | Confidence | Anti-cheat | Failed Rules |",
        "|---|---:|---:|---:|---:|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row.get('paper_id')} | {row.get('status')} | {row.get('paper_score')} | "
            f"{row.get('paper_score_weighted')} | {row.get('confidence')} | {row.get('anti_cheat')} | "
            f"{row.get('failed_rules') or row.get('error') or ''} |"
        )
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")
