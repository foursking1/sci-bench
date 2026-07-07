#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path


def main() -> None:
    framework_dir = Path(__file__).resolve().parent
    sys.path.insert(0, str(framework_dir))

    from repro_eval.cli import main as cli_main

    argv = sys.argv[1:]
    if not argv or argv[0] not in {"evaluate", "batch"}:
        argv = ["evaluate", *argv]
    cli_main(argv)


if __name__ == "__main__":
    main()
