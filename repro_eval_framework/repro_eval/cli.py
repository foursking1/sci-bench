from __future__ import annotations

import argparse
import json

from .config import build_config_from_args
from .batch import run_batch
from .pipeline import evaluate


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run a reproducibility evaluation pipeline.")
    sub = parser.add_subparsers(dest="command", required=True)

    ev = sub.add_parser("evaluate", help="Collect evidence, run assertions, and write reports.")
    ev.add_argument("--config", help="YAML config path.")
    ev.add_argument("--paper-id")
    ev.add_argument("--reproduce-dir")
    ev.add_argument("--truth")
    ev.add_argument("--output-dir")
    ev.add_argument("--repo-root", default=".")
    ev.add_argument("--agent-timeout", type=int, help="Override agent backend timeout in seconds.")
    ev.add_argument("--no-asserts", action="store_true", help="Only collect artifacts; skip assertion scoring.")
    ev.add_argument("--json", action="store_true", help="Print the full pipeline result as JSON.")

    batch = sub.add_parser("batch", help="Evaluate papers listed in a dataset manifest.")
    batch.add_argument("--manifest", default="repro_eval_framework/dataset/manifest.yaml")
    batch.add_argument("--paper-id", action="append", help="Only run a selected paper id. Repeatable.")
    batch.add_argument("--limit", type=int, help="Run at most N papers.")
    batch.add_argument("--no-agent", action="store_true", help="Disable agent collectors for this batch run.")
    batch.add_argument("--agent-timeout", type=int, help="Override agent timeout in seconds.")
    batch.add_argument("--json", action="store_true", help="Print the batch result as JSON.")
    return parser


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "evaluate":
        config = build_config_from_args(args)
        result = evaluate(config)
        if args.json:
            print(json.dumps(result, indent=2, ensure_ascii=False))
            return
        report = result.get("score_report") or {}
        print(f"Artifacts: {result['output_dir']}")
        if report:
            print(f"Paper score: {report.get('paper_score')} (weighted: {report.get('paper_score_weighted')})")
            print(f"Confidence: {report.get('confidence')}")
            print(f"Markdown report: {result['markdown_report']}")
    elif args.command == "batch":
        result = run_batch(
            __import__("pathlib").Path(args.manifest),
            paper_ids=set(args.paper_id) if args.paper_id else None,
            limit=args.limit,
            no_agent=args.no_agent,
            agent_timeout=args.agent_timeout,
        )
        if args.json:
            print(json.dumps(result, indent=2, ensure_ascii=False))
            return
        print(f"Batch results: {result['summary_md']}")
        for row in result["results"]:
            print(
                f"{row['paper_id']}: {row['status']} "
                f"score={row['paper_score']} weighted={row['paper_score_weighted']}"
            )
