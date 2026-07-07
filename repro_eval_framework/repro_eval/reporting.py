from __future__ import annotations

from pathlib import Path
from typing import Any

from .schema import EvalConfig


def write_markdown_report(config: EvalConfig, score_report: dict[str, Any] | None) -> Path:
    path = config.output_dir / "evaluation_report.md"
    if not score_report:
        path.write_text("# Evaluation Report\n\nAssertions were not run.\n", encoding="utf-8")
        return path

    failing = [rule for rule in score_report.get("rules", []) if not rule.get("passed")]
    lines = [
        f"# Evaluation Report: {config.paper_id}",
        "",
        "## Summary",
        "",
        f"- Paper score: `{score_report.get('paper_score')}`",
        f"- Weighted score: `{score_report.get('paper_score_weighted')}`",
        f"- Confidence: `{score_report.get('confidence')}`",
        f"- Evidence completeness: `{score_report.get('evidence_completeness')}`",
        f"- Anti-cheat: `{score_report.get('anti_cheat', {}).get('anti_cheat_overall', 'unknown')}`",
        "",
        "## Claims",
        "",
    ]
    for cid, claim in score_report.get("claims", {}).items():
        lines.append(
            f"- `{cid}`: {claim.get('status')} score={claim.get('score')} "
            f"passed={claim.get('rules_passed')}/{claim.get('rules_total')}"
        )
    lines.extend(["", "## Failing Rules", ""])
    if failing:
        for rule in failing:
            lines.append(f"- `{rule['rule_id']}` ({','.join(rule.get('claim_ids', []))}): {rule.get('detail')}")
    else:
        lines.append("- None")
    lines.extend(
        [
            "",
            "## Artifacts",
            "",
            "- `metrics.json`",
            "- `collect_report.json`",
            "- `manifest.json`",
            "- `score_report.json`",
            "- `figures/`",
            "- `source_files/`",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")
    return path

