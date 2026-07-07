# Dataset Manifest

This dataset folder defines the local evaluation set used by
`repro_eval_framework`.

## Truth Files

All current root-level `truth/*.md` files have been copied into:

```text
repro_eval_framework/truth/
```

Current count: 24 truth files.

## Manifest Coverage

`manifest.yaml` includes papers that currently have both:

- `repro_eval_framework/truth/<paper_id>.md`
- `new_reproduce/<paper_id>/`

Current count: 12 runnable papers.

## Smoke Test

The framework has been smoke-tested on three different reproduction shapes:

| Paper | Shape | Score | Weighted |
|---|---|---:|---:|
| 2604.04673v1 | RDS + figures + deterministic collector | 0.9082 | 0.8957 |
| 2604.04681v1 | CSV/JSON + Claude agent collector | 0.4958 | 0.4640 |
| 2604.04930v1 | Figures/JSON/logs + Claude agent collector | 0.5230 | 0.5150 |

Latest batch summary is written to:

```text
artifacts_v2_framework_batch/summary.md
```
