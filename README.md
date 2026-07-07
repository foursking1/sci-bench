# Sci Bench

Sci Bench 是一个面向论文复现结果的自动评测项目。它把人工编写的
truth/assertion 规格、复现目录中的输出文件、确定性采集器和 Claude agent
语义采集器组合起来，形成一个可以用命令行批量运行的评测流程。

这个仓库当前不是论文复现代码合集，而是评测框架和评测集合本身。复现代码与
运行产物通常放在外部工作区的 `new_reproduce/<paper_id>/` 目录下，再由本仓库
中的评测框架读取和打分。

## 项目作用

这个项目主要解决三个问题：

- 把分散的 `truth/*.md` 评测规格收敛成一个可复用的本地数据集。
- 用统一脚本采集复现证据、生成 artifacts、执行 assertions，并输出分数报告。
- 对难以规则化抽取的证据，引入 Claude CLI agent 做语义级 evidence collection。

评测的目标不是判断论文真假，而是判断某个复现目录是否支撑 truth 文件中声明的
关键结果。每篇论文会得到普通分数、加权分数、置信度、anti-cheat 状态、通过规则数
和失败规则列表。

## 仓库组成

```text
.
├── README.md
├── requirements.txt
├── repro_eval_framework/
│   ├── README.md
│   ├── run_eval.py
│   ├── dataset/
│   │   └── manifest.yaml
│   ├── evals/
│   ├── repro_eval/
│   │   ├── artifacts.py
│   │   ├── assertions.py
│   │   ├── batch.py
│   │   ├── collectors/
│   │   ├── config.py
│   │   ├── discovery.py
│   │   ├── pipeline.py
│   │   └── reporting.py
│   ├── tests/
│   └── truth/
└── result/
    └── 最新结果.md
```

核心目录说明：

- `repro_eval_framework/`: 评测框架主体，可以单篇评测，也可以按 manifest 批量评测。
- `repro_eval_framework/truth/`: 当前内置的 24 个 truth 规格文件。
- `repro_eval_framework/dataset/manifest.yaml`: 当前可运行评测集合，记录 paper id、复现目录和 truth 路径。
- `repro_eval_framework/evals/`: 单篇评测配置示例，包括 deterministic、Claude agent 和 replay 模式。
- `repro_eval_framework/repro_eval/collectors/`: 证据采集器，包括确定性 collector 和 agent collector。
- `result/`: 当前评测集合的结果文档，最新汇总见 `result/最新结果.md`。

## 评测流程

一次评测大致执行以下步骤：

```text
读取 truth 规格
-> 扫描 reproduce_dir 中的复现输出
-> 运行 deterministic collectors
-> 必要时运行 Claude agent collector
-> 标准化写入 artifacts
-> 执行 assertion rules
-> 修复已知 pass_condition alias 兼容问题
-> 输出 JSON 与 Markdown 报告
```

默认输出目录示例：

```text
artifacts_v2_framework/<paper_id>/
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

agent 运行时还会写入：

```text
artifacts_v2_framework/<paper_id>/agent/
  prompt.md
  raw_response.txt
  parsed_response.json
  stderr.txt
```

## 当前评测集合

当前仓库内置：

- truth 文件数：24
- manifest 可运行论文数：13
- 最新已验证论文数：4

最新结果汇总在：

```text
result/最新结果.md
```

当前已验证结果：

| Paper | Score | Weighted | Confidence | Anti-cheat | Pass |
|---|---:|---:|---:|---|---:|
| `2604.04673v1` | 0.9082 | 0.8957 | 0.7409 | pass | 20/22 |
| `2604.04681v1` | 0.4958 | 0.4640 | 0.7400 | pass | 14/30 |
| `2604.04930v1` | 0.5230 | 0.5150 | 0.7591 | pass | 12/22 |
| `2604.04858v1` | 0.4694 | 0.5187 | 0.6201 | pass | 17/34 |

完整失败规则和备注见 `result/最新结果.md`。

## 环境要求

基础依赖：

```bash
python -m pip install -r requirements.txt
```

如果要使用真实 Claude agent 采集证据，还需要本机可调用 `claude` CLI，并且已经完成
认证。agent 相关参数在 YAML 配置或 batch 命令中设置，例如：

```yaml
agent:
  enabled: true
  provider: claude_cli
  command: claude
  timeout: 1800
  permission_mode: bypassPermissions
```

## 快速开始

运行测试：

```bash
PYTHONPATH=repro_eval_framework pytest -q repro_eval_framework/tests
```

运行单篇评测：

```bash
python repro_eval_framework/run_eval.py \
  --config repro_eval_framework/evals/2604.04673v1.yaml
```

运行 manifest 中的一篇：

```bash
python repro_eval_framework/run_eval.py batch \
  --manifest repro_eval_framework/dataset/manifest.yaml \
  --paper-id 2604.04673v1
```

运行 manifest 中前 3 篇：

```bash
python repro_eval_framework/run_eval.py batch \
  --manifest repro_eval_framework/dataset/manifest.yaml \
  --limit 3
```

只做 deterministic smoke test，不调用 agent：

```bash
python repro_eval_framework/run_eval.py batch \
  --manifest repro_eval_framework/dataset/manifest.yaml \
  --paper-id 2604.04673v1 \
  --no-agent
```

增加 agent 超时时间：

```bash
python repro_eval_framework/run_eval.py batch \
  --manifest repro_eval_framework/dataset/manifest.yaml \
  --paper-id 2604.04858v1 \
  --agent-timeout 1800
```

## 输入与外部数据

本仓库提交的是评测框架和 truth 集合，不包含大型复现工作区、虚拟环境或运行 artifacts。
manifest 中的 `reproduce_dir` 默认指向：

```text
new_reproduce/<paper_id>
```

使用时需要把对应复现目录放在仓库根目录下，或修改 config/manifest 里的
`reproduce_dir` 指向实际路径。

## 结果解读

评测报告中的主要字段：

- `Score`: 规则层面的总体支持程度。
- `Weighted`: 按 claim/rule 权重计算后的分数。
- `Confidence`: 证据完整性和采集可靠性的综合置信度。
- `Anti-cheat`: 是否通过基础反作弊检查。
- `Pass`: 通过规则数和总规则数。
- `Failed Rules`: 未通过的 assertion rule id。

Claude agent 参与的结果可能存在小幅波动。确定性 collector 会优先写入精确数值，
agent 主要用于补齐表格、日志、报告文本等语义证据。

## 更多文档

- 框架细节：`repro_eval_framework/README.md`
- 数据集说明：`repro_eval_framework/dataset/README.md`
- 最新结果：`result/最新结果.md`
