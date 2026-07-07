# Reproduction Evaluation Framework

This directory contains a small evaluation framework that wraps the existing
truth/assertion system into a single command.

## Quick Start

From the repository root:

```bash
PYTHONPATH=repro_eval_framework python -m repro_eval evaluate \
  --config repro_eval_framework/evals/2604.04673v1.yaml
```

Or use the wrapper script:

```bash
python repro_eval_framework/run_eval.py \
  --config repro_eval_framework/evals/2604.04673v1.yaml
```

The command writes a complete artifact bundle to:

```text
artifacts_v2_framework/2604.04673v1/
  metrics.json
  manifest.json
  collect_report.json
  extraction_spec.json
  run.log
  score_report.json
  evaluation_report.md
  figures/
  source_files/
```

## Batch Dataset

The framework includes a local dataset manifest:

```text
repro_eval_framework/dataset/manifest.yaml
```

All current `truth/*.md` files have been copied into:

```text
repro_eval_framework/truth/
```

Run one paper from the manifest:

```bash
python repro_eval_framework/run_eval.py batch \
  --manifest repro_eval_framework/dataset/manifest.yaml \
  --paper-id 2604.04673v1 \
  --no-agent
```

Run the first N papers:

```bash
python repro_eval_framework/run_eval.py batch \
  --manifest repro_eval_framework/dataset/manifest.yaml \
  --limit 3
```

Run one paper with Claude agent enabled:

```bash
python repro_eval_framework/run_eval.py batch \
  --manifest repro_eval_framework/dataset/manifest.yaml \
  --paper-id 2604.04681v1 \
  --agent-timeout 1800
```

Use `--no-agent` for deterministic-only smoke tests.

Batch outputs are written to:

```text
artifacts_v2_framework_batch/
  summary.json
  summary.csv
  summary.md
  <paper_id>/
```

Agent-backed scores can vary across runs because the extraction agent makes
semantic judgment calls. Each run stores the full prompt and structured output
under `<paper_id>/agent/` for review.

## Current Evaluation Set

The framework now carries a local copy of all root-level truth specs:

```text
repro_eval_framework/truth/
```

Current truth count: 24 files.

The runnable dataset is defined by:

```text
repro_eval_framework/dataset/manifest.yaml
```

The manifest currently includes the papers that have both a truth file and a
`new_reproduce/<paper_id>/` directory in this workspace. Current runnable count:
13 papers.

The latest framework evaluation results are summarized in:

```text
result/最新结果.md
```

Latest verified results, updated on 2026-07-07:

| Paper | Score | Weighted | Confidence | Anti-cheat | Pass | Failed Rules | Notes |
|---|---:|---:|---:|---|---:|---|---|
| `2604.04673v1` | 0.9082 | 0.8957 | 0.7409 | pass | 20/22 | R06,R10 | RDS + figures; deterministic collector first, agent fills gaps |
| `2604.04681v1` | 0.4958 | 0.4640 | 0.7400 | pass | 14/30 | R03,R04,R05,R06,R07,R08,R09,R13,R14,R15,R22,R23,R27,R28,R29,R30 | CSV/JSON tables; Claude agent collector |
| `2604.04930v1` | 0.5230 | 0.5150 | 0.7591 | pass | 12/22 | R01,R03,R05,R06,R10,R11,R16,R17,R21,R22 | figures/JSON/logs; Claude agent collector |
| `2604.04858v1` | 0.4694 | 0.5187 | 0.6201 | pass | 17/34 | R01,R02,R03,R04,R05,R09,R10,R11,R12,R13,R14,R19,R20,R21,R22,R23,R33 | FairLogue CSV/JSON/reports; latest real Claude agent run |

Result artifacts:

- Three-paper batch results:
  `artifacts_v2_framework_batch/summary.md`
- Latest real-agent result for `2604.04858v1`:
  `artifacts_v2_framework/2604.04858v1/evaluation_report.md`
- Stable replay result for `2604.04858v1`:
  `artifacts_v2_framework/2604.04858v1_replay/evaluation_report.md`
  with score `0.4001`; use this as a regression-test reference, not the latest
  live-agent score.

Notes:

- Agent-backed scores may vary between runs because Claude performs semantic
  evidence extraction.
- Deterministic collectors take precedence over agent output; agents fill
  missing evidence instead of overwriting exact measurements.
- Every agent-backed run stores `prompt.md`, `raw_response.txt`,
  `parsed_response.json`, and `stderr.txt` under the paper's `agent/` folder.

## Design

The framework makes the evaluated reproduction directory explicit. It does not
infer the target from the current working directory, which avoids accidentally
evaluating an older sibling directory.

The pipeline is:

```text
load truth.md
-> discover files in reproduce_dir
-> run collectors
-> build standardized artifacts
-> run assertions
-> repair known pass_condition alias issue
-> write JSON and Markdown reports
```

## Collectors

Collectors are deterministic where possible:

- `BnnRdsCollector` detects the BNN risk reproduction outputs and extracts
  numeric metrics directly from `.rds` files with `Rscript`.
- `FigureCollector` standardizes reproduced figure names into `figures/` so
  figure assertions can find them consistently.
- `AgentCollector` is the general fallback. It can run a real Claude Code
  agent (`provider: claude_cli`) or replay a saved artifact bundle for
  deterministic testing (`provider: replay`).

The intended production path is deterministic collectors first, then the agent
collector fills any semantic extraction gaps.

## Configuration

Example:

```yaml
paper_id: 2604.04673v1
repo_root: .
reproduce_dir: new_reproduce/2604.04673v1
truth: repro_eval_framework/truth/2604.04673v1.md
output_dir: artifacts_v2_framework/2604.04673v1
run_asserts: true
preserve_sources: true
```

Agent-enabled example:

```yaml
agent:
  enabled: true
  provider: claude_cli
  command: claude
  timeout: 1800
  permission_mode: bypassPermissions
```

You can override the timeout from the command line:

```bash
python repro_eval_framework/run_eval.py \
  --config repro_eval_framework/evals/2604.04681v1.claude.yaml \
  --agent-timeout 1800
```

For regression testing without calling an external model:

```yaml
agent:
  enabled: true
  provider: replay
  replay_artifacts: artifacts_v2/2604.04681v1
```

Agent traces are written under:

```text
<output_dir>/agent/
  prompt.md
  raw_response.txt
  stderr.txt
  parsed_response.json
```

You can also run without a YAML file:

```bash
PYTHONPATH=repro_eval_framework python -m repro_eval evaluate \
  --paper-id 2604.04673v1 \
  --reproduce-dir new_reproduce/2604.04673v1 \
  --truth repro_eval_framework/truth/2604.04673v1.md \
  --output-dir artifacts_v2_framework/2604.04673v1
```

## Tests

```bash
PYTHONPATH=repro_eval_framework pytest -q repro_eval_framework/tests
```

## Notes

The legacy assertion runner currently mishandles a rule written as
`pass_condition = actual > target`; it knows `target_value`, but not the alias
`target`. The framework repairs this after running the legacy assertions and
then recomputes claim and paper scores.
