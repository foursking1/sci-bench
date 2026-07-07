from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any

from ..schema import CollectorResult, DiscoveredFile, EvalConfig, EvidenceEntry
from .base import Collector


class FigureCollector(Collector):
    name = "figures"

    STANDARD_NAMES = {
        "R17": ("Fig1_reproduced.png", "radial_risk_p5.png", "Figure 1 radial risk plot at p=5."),
        "R18": ("Fig2_reproduced.png", "radial_risk_p50.png", "Figure 2 radial risk plot at p=50."),
        "R19": ("Fig3_reproduced.png", "radial_risk_p100.png", "Figure 3 radial risk plot at p=100."),
        "R20": ("Fig4_reproduced.png", "sparsity_risk_p5.png", "Figure 4 sparsity risk plot at p=5."),
        "R21": ("Fig5_reproduced.png", "sparsity_risk_p50.png", "Figure 5 sparsity risk plot at p=50."),
        "R22": ("Fig6_reproduced.png", "sparsity_risk_p100.png", "Figure 6 sparsity risk plot at p=100."),
    }

    def collect(self, config: EvalConfig, truth_spec: Any, discovered: list[DiscoveredFile]) -> CollectorResult:
        figures_dir = config.output_dir / "figures"
        figures_dir.mkdir(parents=True, exist_ok=True)
        evidence: list[EvidenceEntry] = []
        copied: dict[str, Path] = {}

        for rule_id, (source_name, target_name, note) in self.STANDARD_NAMES.items():
            source = config.reproduce_dir / "figures" / source_name
            if not source.exists():
                evidence.append(EvidenceEntry(rule_id, "no_evidence", None, "", 0.0, f"missing expected figure {source_name}"))
                continue
            target = figures_dir / target_name
            shutil.copy2(source, target)
            copied[target_name] = target
            evidence.append(
                EvidenceEntry(
                    rule_id=rule_id,
                    evidence_status="evidence_found",
                    extracted_value=4.0,
                    source_file=f"figures/{source_name}",
                    mapping_confidence=0.9,
                    notes=f"{note} File exists and was standardized as figures/{target_name}.",
                )
            )

        return CollectorResult(evidence=evidence, copied_figures=copied, notes=[f"{self.name}: standardized {len(copied)} figures"])

