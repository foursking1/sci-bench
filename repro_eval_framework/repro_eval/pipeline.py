from __future__ import annotations

import sys
from typing import Any

from .artifacts import build_artifacts
from .assertions import run_assertions
from .collectors import DEFAULT_COLLECTORS
from .discovery import discover_files
from .reporting import write_markdown_report
from .schema import EvalConfig


def load_truth(config: EvalConfig) -> Any:
    tools_dir = config.repo_root / "tools"
    if str(tools_dir) not in sys.path:
        sys.path.insert(0, str(tools_dir))
    from truth_parser import parse_truth

    return parse_truth(config.truth)


def evaluate(config: EvalConfig) -> dict[str, Any]:
    if not config.reproduce_dir.is_dir():
        raise FileNotFoundError(f"reproduce_dir does not exist: {config.reproduce_dir}")
    if not config.truth.is_file():
        raise FileNotFoundError(f"truth file does not exist: {config.truth}")

    truth_spec = load_truth(config)
    discovered = discover_files(config.reproduce_dir)
    collector_results = [collector.collect(config, truth_spec, discovered) for collector in DEFAULT_COLLECTORS]
    build_artifacts(config, truth_spec, discovered, collector_results)

    score_report = None
    if config.run_asserts:
        score_report = run_assertions(config, truth_spec)
    report_path = write_markdown_report(config, score_report)

    return {
        "paper_id": config.paper_id,
        "output_dir": str(config.output_dir),
        "discovered_files": len(discovered),
        "score_report": score_report,
        "markdown_report": str(report_path),
    }

