from __future__ import annotations

import json
import re
import shutil
import subprocess
from dataclasses import asdict
from pathlib import Path
from typing import Any

from ..artifacts import build_extraction_spec, deep_merge
from ..schema import CollectorResult, DiscoveredFile, EvalConfig, EvidenceEntry
from .base import Collector


class AgentCollector(Collector):
    """Agent-based evidence collector.

    The collector is intentionally backend-driven:
    - provider=claude_cli runs a real Claude Code print-mode agent.
    - provider=replay loads a saved metrics/collect_report bundle, useful for
      deterministic regression tests of the framework.
    """

    name = "agent"

    def collect(self, config: EvalConfig, truth_spec: Any, discovered: list[DiscoveredFile]) -> CollectorResult:
        agent_cfg = config.agent or {}
        if not agent_cfg.get("enabled", False):
            return CollectorResult(notes=["agent: disabled"])

        provider = agent_cfg.get("provider", "claude_cli")
        trace_dir = config.output_dir / "agent"
        if trace_dir.exists():
            shutil.rmtree(trace_dir)
        trace_dir.mkdir(parents=True, exist_ok=True)

        if provider == "replay":
            return self._collect_replay(config, truth_spec, trace_dir)
        if provider == "claude_cli":
            return self._collect_claude_cli(config, truth_spec, discovered, trace_dir)

        return CollectorResult(notes=[f"agent: unknown provider {provider!r}"])

    def _collect_replay(self, config: EvalConfig, truth_spec: Any, trace_dir: Path) -> CollectorResult:
        replay_dir = Path(config.agent.get("replay_artifacts", ""))
        if not replay_dir.is_absolute():
            replay_dir = config.repo_root / replay_dir
        metrics_path = replay_dir / "metrics.json"
        collect_path = replay_dir / "collect_report.json"
        if not metrics_path.exists() or not collect_path.exists():
            return CollectorResult(notes=[f"agent replay: missing {metrics_path} or {collect_path}"])

        metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
        collect_report = json.loads(collect_path.read_text(encoding="utf-8"))
        (trace_dir / "provider.txt").write_text("replay\n", encoding="utf-8")
        (trace_dir / "parsed_response.json").write_text(
            json.dumps({"metrics_patch": metrics, "rules_evaluated": collect_report.get("rules_evaluated", [])}, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

        evidence = [
            EvidenceEntry(
                rule_id=item.get("rule_id", ""),
                evidence_status=item.get("evidence_status", "no_evidence"),
                extracted_value=item.get("extracted_value"),
                source_file=item.get("source_file") or "",
                mapping_confidence=float(item.get("mapping_confidence") or 0.0),
                notes=item.get("notes") or "replayed agent evidence",
            )
            for item in collect_report.get("rules_evaluated", [])
        ]
        return CollectorResult(metrics=metrics, evidence=evidence, notes=[f"agent replay: loaded {replay_dir}"])

    def _collect_claude_cli(
        self,
        config: EvalConfig,
        truth_spec: Any,
        discovered: list[DiscoveredFile],
        trace_dir: Path,
    ) -> CollectorResult:
        prompt = self._build_prompt(config, truth_spec, discovered)
        prompt_path = trace_dir / "prompt.md"
        prompt_path.write_text(prompt, encoding="utf-8")

        timeout = int(config.agent.get("timeout", 600))
        command = str(config.agent.get("command", "claude"))
        args = [
            command,
            "-p",
            "--output-format",
            "json",
            "--no-session-persistence",
            "--permission-mode",
            str(config.agent.get("permission_mode", "bypassPermissions")),
            "--append-system-prompt",
            "Your final response must be a JSON object matching the provided JSON schema. Do not summarize. Do not write the answer to a file. Do not use markdown fences.",
            "--json-schema",
            json.dumps(agent_json_schema()),
            f"Read this prompt file and complete the extraction task: {prompt_path}",
        ]
        try:
            proc = subprocess.run(
                args,
                cwd=config.reproduce_dir,
                text=True,
                capture_output=True,
                timeout=timeout,
                check=False,
            )
        except subprocess.TimeoutExpired as exc:
            (trace_dir / "stderr.txt").write_text(f"timeout after {timeout}s\n{exc}", encoding="utf-8")
            return CollectorResult(notes=[f"agent claude_cli: timed out after {timeout}s"])
        except FileNotFoundError:
            (trace_dir / "stderr.txt").write_text(f"command not found: {command}\n", encoding="utf-8")
            return CollectorResult(notes=[f"agent claude_cli: command not found {command!r}"])

        (trace_dir / "raw_response.txt").write_text(proc.stdout or "", encoding="utf-8")
        (trace_dir / "stderr.txt").write_text(proc.stderr or "", encoding="utf-8")
        if proc.returncode != 0:
            return CollectorResult(notes=[f"agent claude_cli: failed rc={proc.returncode}"])

        parsed = parse_agent_response(proc.stdout)
        if parsed is None:
            parsed = self._load_agent_written_payload(config, proc.stdout, trace_dir)
        if parsed is None:
            return CollectorResult(notes=["agent claude_cli: response was not parseable JSON"])
        (trace_dir / "parsed_response.json").write_text(json.dumps(parsed, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        result = collector_result_from_agent_payload(parsed)
        self._validate_sources(config, result)
        return result

    def _build_prompt(self, config: EvalConfig, truth_spec: Any, discovered: list[DiscoveredFile]) -> str:
        discovered_payload = [asdict(item) for item in discovered]
        extraction_spec = build_extraction_spec(truth_spec)
        return f"""You are an evidence extraction agent for a scientific reproduction.

Evaluate this reproduction directory:
{config.reproduce_dir}

Do not use truth.md or claims.md as evidence. They contain target expectations.
Use only reproduction outputs such as results, reports, logs, figures, code, and generated data.

Discovered files:
```json
{json.dumps(discovered_payload, indent=2, ensure_ascii=False)}
```

Extraction spec:
```json
{json.dumps(extraction_spec, indent=2, ensure_ascii=False)}
```

Return ONLY valid JSON with this shape:
```json
{{
  "metrics_patch": {{"task_metrics": {{}}}},
  "rules_evaluated": [
    {{
      "rule_id": "R01",
      "evidence_status": "evidence_found",
      "extracted_value": 1.23,
      "source_file": "results/example.json",
      "mapping_confidence": 0.9,
      "notes": "short explanation"
    }}
  ]
}}
```

Rules:
- Fill metrics_patch with the dotted paths needed by target_path and comparison rules.
- Use the exact dotted paths shown in `target_path` and `comparison`.
- For comparison rules, create one metric value for each dotted path referenced by the expression.
- If a rule has no evidence, set evidence_status to no_evidence and explain why.
- source_file must be a real path relative to the reproduction directory.
- Do not write the answer to a file.
- Do not summarize your findings in prose.
- Your final answer must be the JSON object itself, matching the schema exactly.
- Do not include markdown fences in your final answer.
"""

    def _validate_sources(self, config: EvalConfig, result: CollectorResult) -> None:
        for entry in result.evidence:
            if entry.evidence_status != "evidence_found":
                continue
            if not entry.source_file:
                entry.evidence_status = "no_evidence"
                entry.mapping_confidence = 0.0
                entry.notes = "agent evidence rejected: missing source_file"
                continue
            source_name = Path(entry.source_file).name.lower()
            if source_name in {"truth.md", "claims.md"}:
                entry.evidence_status = "no_evidence"
                entry.mapping_confidence = 0.0
                entry.notes = f"agent evidence rejected: {entry.source_file} is not experimental output"
                continue
            if not (config.reproduce_dir / entry.source_file).is_file():
                entry.evidence_status = "no_evidence"
                entry.mapping_confidence = 0.0
                entry.notes = f"agent evidence rejected: source_file does not exist: {entry.source_file}"

    def _load_agent_written_payload(self, config: EvalConfig, stdout: str, trace_dir: Path) -> dict[str, Any] | None:
        candidates: list[Path] = []
        for match in re.finditer(r"`([^`]+\.json)`", stdout):
            candidates.append(config.reproduce_dir / match.group(1))
        candidates.extend(
            [
                config.reproduce_dir / "extraction_result.json",
                config.reproduce_dir / "agent_result.json",
                trace_dir / "extraction_result.json",
            ]
        )
        for candidate in candidates:
            if not candidate.is_file():
                continue
            try:
                parsed = json.loads(candidate.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                continue
            (trace_dir / "agent_written_file.txt").write_text(str(candidate) + "\n", encoding="utf-8")
            return parsed if isinstance(parsed, dict) else {"metrics_patch": {}, "rules_evaluated": parsed}
        return None


def parse_agent_response(text: str) -> dict[str, Any] | None:
    raw = text.strip()
    if "```" in raw:
        match = re.search(r"```(?:json)?\s*(.*?)\s*```", raw, re.DOTALL)
        if match:
            raw = match.group(1).strip()
    start_candidates = [idx for idx in [raw.find("{"), raw.find("[")] if idx >= 0]
    if start_candidates:
        raw = raw[min(start_candidates):]
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError:
        return None
    if isinstance(parsed, list):
        return {"metrics_patch": {}, "rules_evaluated": parsed}
    if isinstance(parsed, dict):
        if isinstance(parsed.get("structured_output"), dict):
            return parsed["structured_output"]
        if "rules_evaluated" in parsed or "metrics_patch" in parsed:
            return parsed
        for key in ("extraction", "results", "data", "evidence"):
            if isinstance(parsed.get(key), list):
                return {"metrics_patch": parsed.get("metrics_patch", {}), "rules_evaluated": parsed[key]}
    return None


def collector_result_from_agent_payload(payload: dict[str, Any]) -> CollectorResult:
    metrics: dict[str, Any] = {}
    deep_merge(metrics, payload.get("metrics_patch") or {})
    evidence = [
        EvidenceEntry(
            rule_id=item.get("rule_id", ""),
            evidence_status=item.get("evidence_status", "no_evidence"),
            extracted_value=item.get("extracted_value"),
            source_file=item.get("source_file") or "",
            mapping_confidence=float(item.get("mapping_confidence") or 0.0),
            notes=item.get("notes") or "",
        )
        for item in payload.get("rules_evaluated", [])
    ]
    return CollectorResult(metrics=metrics, evidence=evidence, notes=["agent: extracted evidence"])


def agent_json_schema() -> dict[str, Any]:
    return {
        "type": "object",
        "properties": {
            "metrics_patch": {"type": "object"},
            "rules_evaluated": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "rule_id": {"type": "string"},
                        "evidence_status": {"type": "string", "enum": ["evidence_found", "no_evidence", "extract_failed"]},
                        "extracted_value": {},
                        "source_file": {"type": "string"},
                        "mapping_confidence": {"type": "number"},
                        "notes": {"type": "string"},
                    },
                    "required": ["rule_id", "evidence_status", "extracted_value", "source_file", "mapping_confidence", "notes"],
                },
            },
        },
        "required": ["metrics_patch", "rules_evaluated"],
    }
