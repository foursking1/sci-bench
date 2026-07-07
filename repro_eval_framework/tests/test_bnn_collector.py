from pathlib import Path

import pytest

from repro_eval.collectors.bnn_rds import BnnRdsCollector
from repro_eval.config import load_config
from repro_eval.discovery import discover_files
from repro_eval.pipeline import load_truth


def test_bnn_rds_collector_extracts_expected_metrics():
    root = Path.cwd()
    if not (root / "new_reproduce/2604.04673v1/data/raw/radial_risk_matrix.rds").exists():
        pytest.skip("2604.04673v1 RDS fixture is not available")

    config = load_config(
        Path(),
        {
            "paper_id": "2604.04673v1",
            "repo_root": ".",
            "reproduce_dir": "new_reproduce/2604.04673v1",
            "truth": "truth/2604.04673v1.md",
            "output_dir": "artifacts_v2_framework/test_2604.04673v1",
        },
    )
    truth = load_truth(config)
    result = BnnRdsCollector().collect(config, truth, discover_files(config.reproduce_dir))
    assert result.metrics["task_metrics"]["P08"]["risk"]["MLE"] == 5.0
    assert result.metrics["task_metrics"]["P20"]["risk"]["Horseshoe_k100_max"] > 130.0

