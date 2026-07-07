from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class EvalConfig:
    paper_id: str
    reproduce_dir: Path
    truth: Path
    output_dir: Path
    repo_root: Path
    run_asserts: bool = True
    preserve_sources: bool = True
    agent: dict[str, Any] = field(default_factory=dict)


@dataclass
class DiscoveredFile:
    path: str
    kind: str
    size_kb: float


@dataclass
class EvidenceEntry:
    rule_id: str
    evidence_status: str
    extracted_value: Any
    source_file: str
    mapping_confidence: float
    notes: str


@dataclass
class CollectorResult:
    metrics: dict[str, Any] = field(default_factory=dict)
    evidence: list[EvidenceEntry] = field(default_factory=list)
    copied_figures: dict[str, Path] = field(default_factory=dict)
    notes: list[str] = field(default_factory=list)
