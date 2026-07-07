# Sci Bench

This repository contains a lightweight reproduction-evaluation framework and
the current truth/evaluation collection extracted from the local paper
reproduction workspace.

## Contents

- `repro_eval_framework/`: runnable evaluation framework.
- `repro_eval_framework/truth/`: 24 bundled truth specification files.
- `repro_eval_framework/dataset/manifest.yaml`: current runnable paper
  manifest.
- `result/最新结果.md`: latest evaluation-set result summary.

## Quick Start

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run tests:

```bash
PYTHONPATH=repro_eval_framework pytest -q repro_eval_framework/tests
```

Run one evaluation from a config:

```bash
python repro_eval_framework/run_eval.py \
  --config repro_eval_framework/evals/2604.04673v1.yaml
```

Run a batch evaluation from the manifest:

```bash
python repro_eval_framework/run_eval.py batch \
  --manifest repro_eval_framework/dataset/manifest.yaml \
  --limit 3
```

For details, see `repro_eval_framework/README.md`.

