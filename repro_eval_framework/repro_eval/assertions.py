from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

from .artifacts import write_json
from .schema import EvalConfig


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def get_by_path(payload: Any, dotted: str) -> Any:
    cur = payload
    for part in dotted.split("."):
        if isinstance(cur, dict):
            cur = cur[part]
        elif isinstance(cur, list):
            cur = cur[int(part)]
        else:
            raise KeyError(dotted)
    return cur


def run_assertions(config: EvalConfig, truth_spec: Any) -> dict[str, Any]:
    tools_dir = config.repo_root / "tools"
    if str(tools_dir) not in sys.path:
        sys.path.insert(0, str(tools_dir))
    from run_asserts import run_truth_mode

    result = run_truth_mode(config.truth, config.output_dir, config.reproduce_dir, None)
    report = result[0] if isinstance(result, tuple) else result
    report = repair_pass_conditions(report, config, truth_spec)
    output = config.output_dir / "score_report.json"
    write_json(output, report)
    return report


def repair_pass_conditions(report: dict[str, Any], config: EvalConfig, truth_spec: Any) -> dict[str, Any]:
    """Correct failed numeric rules whose truth.md pass_condition is evaluable.

    The legacy runner replaces target_value but not a bare variable named
    target. This makes rules such as `actual > target` fall back to equality.
    The framework evaluates those rules explicitly and then recomputes scores.
    """
    metrics = load_json(config.output_dir / "metrics.json")
    context = dict(metrics)
    context["metrics"] = metrics

    rules_by_id = {rule.rule_id: rule for rule in truth_spec.rules}
    changed = False
    for result in report.get("rules", []):
        if result.get("passed"):
            continue
        rule = rules_by_id.get(result.get("rule_id"))
        if not rule or not rule.pass_condition or not rule.target_path:
            continue
        try:
            actual = get_by_path(context, rule.target_path)
        except Exception:
            continue
        if not isinstance(actual, (int, float)):
            continue
        passed = evaluate_condition(
            rule.pass_condition,
            actual=float(actual),
            target=rule.target_value,
            tolerance_abs=rule.tolerance_abs,
            tolerance_pct=rule.tolerance_pct,
        )
        if passed:
            result["passed"] = True
            result["score_awarded"] = result["score_possible"]
            result["detail"] = f"pass_condition repaired by framework: actual={actual} condition={rule.pass_condition}"
            changed = True

    if changed:
        recompute_scores(report, truth_spec)
    return report


def evaluate_condition(condition: str, *, actual: float, target: float | None, tolerance_abs: float, tolerance_pct: float) -> bool:
    expr = condition
    replacements = {
        "actual": actual,
        "target_value": target,
        "target": target,
        "tolerance_abs": tolerance_abs,
        "tolerance_pct": tolerance_pct,
    }
    for name, value in replacements.items():
        expr = re.sub(rf"\b{name}\b", repr(value), expr)
    if expr == condition and re.match(r"\s*[<>!=]=?", condition):
        expr = f"{actual} {condition}"
    return bool(eval(expr, {"__builtins__": {"abs": abs, "min": min, "max": max}}, {}))


def recompute_scores(report: dict[str, Any], truth_spec: Any) -> None:
    claim_ids = [claim.get("id", "") for claim in truth_spec.claims if claim.get("id")]
    claims: dict[str, Any] = {}
    for cid in claim_ids:
        rules = [r for r in report["rules"] if cid in r.get("claim_ids", [])]
        if not rules:
            claims[cid] = {
                "score": 0.0,
                "status": "not_tested",
                "rules_passed": 0,
                "rules_total": 0,
                "total_weight": 0.0,
                "failing_rules": [],
            }
            continue
        possible = sum(float(r["score_possible"]) for r in rules)
        awarded = sum(float(r["score_awarded"]) for r in rules)
        score = awarded / possible if possible else 0.0
        failing = [r["rule_id"] for r in rules if not r["passed"]]
        claims[cid] = {
            "score": round(score, 4),
            "status": "supported" if score == 1.0 and not failing else ("partially_supported" if score > 0 else "unsupported"),
            "rules_passed": sum(1 for r in rules if r["passed"]),
            "rules_total": len(rules),
            "total_weight": round(possible, 2),
            "failing_rules": failing,
        }
    scored = [v for v in claims.values() if v["status"] != "not_tested"]
    report["claims"] = claims
    report["paper_score"] = round(sum(v["score"] for v in scored) / len(scored), 4) if scored else 0.0
    total_weight = sum(v["total_weight"] for v in scored)
    report["paper_score_weighted"] = round(
        sum(v["score"] * v["total_weight"] for v in scored) / total_weight,
        4,
    ) if total_weight else 0.0
