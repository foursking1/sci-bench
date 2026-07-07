from pathlib import Path

from repro_eval.batch import iter_paper_configs


def test_manifest_can_select_single_paper_without_agent():
    configs = iter_paper_configs(
        Path("repro_eval_framework/dataset/manifest.yaml"),
        paper_ids={"2604.04673v1"},
        no_agent=True,
    )
    assert len(configs) == 1
    assert configs[0].paper_id == "2604.04673v1"
    assert configs[0].truth.name == "2604.04673v1.md"
    assert configs[0].agent["enabled"] is False
