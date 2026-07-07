from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from .schema import EvalConfig


def _resolve(base: Path, value: str | Path) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    return (base / path).resolve()


def load_config(path: Path, cli_overrides: dict[str, Any] | None = None) -> EvalConfig:
    cli_overrides = cli_overrides or {}
    data: dict[str, Any] = {}
    if path and path.is_file():
        with path.open(encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}

    merged = {**data, **{k: v for k, v in cli_overrides.items() if v is not None}}
    repo_root = _resolve(Path.cwd(), merged.get("repo_root", "."))

    missing = [k for k in ("paper_id", "reproduce_dir", "truth", "output_dir") if not merged.get(k)]
    if missing:
        raise ValueError(f"missing required config fields: {', '.join(missing)}")

    return EvalConfig(
        paper_id=str(merged["paper_id"]),
        reproduce_dir=_resolve(repo_root, merged["reproduce_dir"]),
        truth=_resolve(repo_root, merged["truth"]),
        output_dir=_resolve(repo_root, merged["output_dir"]),
        repo_root=repo_root,
        run_asserts=bool(merged.get("run_asserts", True)),
        preserve_sources=bool(merged.get("preserve_sources", True)),
        agent=dict(merged.get("agent") or {}),
    )


def build_config_from_args(args: Any) -> EvalConfig:
    overrides = {
        "paper_id": args.paper_id,
        "reproduce_dir": args.reproduce_dir,
        "truth": args.truth,
        "output_dir": args.output_dir,
        "repo_root": args.repo_root,
        "run_asserts": not args.no_asserts,
    }
    if args.config:
        config = load_config(Path(args.config), overrides)
        if args.agent_timeout is not None:
            config.agent["timeout"] = args.agent_timeout
        return config

    overrides["repo_root"] = args.repo_root or "."
    config = load_config(Path(), overrides)
    if args.agent_timeout is not None:
        config.agent["timeout"] = args.agent_timeout
    return config
