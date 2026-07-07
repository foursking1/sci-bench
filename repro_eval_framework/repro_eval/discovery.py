from __future__ import annotations

import os
from pathlib import Path

from .schema import DiscoveredFile


SKIP_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules",
    ".cache",
    ".omc",
    "artifacts",
}


def file_kind(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".json":
        return "json"
    if suffix in {".csv", ".tsv"}:
        return "table"
    if suffix in {".txt", ".log", ".md"}:
        return "text"
    if suffix in {".png", ".jpg", ".jpeg", ".svg", ".pdf"}:
        return "figure"
    if suffix in {".py", ".r", ".sh"}:
        return "code"
    if suffix == ".rds":
        return "rds"
    return "unknown"


def discover_files(reproduce_dir: Path) -> list[DiscoveredFile]:
    files: list[DiscoveredFile] = []
    for root, dirs, names in os.walk(reproduce_dir):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        root_path = Path(root)
        for name in names:
            path = root_path / name
            if not path.is_file():
                continue
            rel = path.relative_to(reproduce_dir).as_posix()
            if any(part in SKIP_DIRS for part in Path(rel).parts):
                continue
            files.append(
                DiscoveredFile(
                    path=rel,
                    kind=file_kind(path),
                    size_kb=round(path.stat().st_size / 1024, 1),
                )
            )
    return sorted(files, key=lambda item: item.path)

