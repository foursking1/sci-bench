# bonjean_2002

## Metadata

| Field | Value |
|-------|-------|
| Paper ID | bonjean_2002 |
| Score | 0.8128 |
| Weighted Score | 0.5636 |
| Reproduction Mode | full |
| Evidence Completeness | 100.00% |
| Confidence | 0.63 |

## Bottleneck Analysis

### 实验做错了 (8 rules)

- **R03**: value=9.43 target=8.0 tolerance=0.800000
- **R04**: value=3.61 target=3.0 tolerance=0.300000
- **R12**: value=0.63 target=0.76 tolerance=0.050000
- **R13**: value=0.5 target=0.64 tolerance=0.050000
- **R14**: value=0.5 target=0.62 tolerance=0.050000
- **R15**: value=-0.124 target=0.11 tolerance=0.030000
- **R21**: value=0.84 target=0.67 tolerance=0.050000
- **R24**: value=0.66 target=0.61 tolerance=0.050000

### 实验未执行 (1 rules)

- **R19**: evaluated pass_condition: 56.8 >= 64.0 -> False

## Claim Status

| Claim | Status | Rules Passed |
|-------|--------|-------------|
| C01 | PASS | 1/1 |
| C02 | PASS | 1/1 |
| C03 | PARTIAL | 1/3 |
| C04 | PASS | 1/1 |
| C05 | PASS | 2/2 |
| C06 | PASS | 1/1 |
| C07 | PASS | 1/1 |
| C08 | PARTIAL | 4/8 |
| C09 | PARTIAL | 4/7 |
| C10 | PASS | 1/1 |

## Failed Rules Detail

| Rule ID | Claims | Failure Reason |
|---------|--------|----------------|
| R03 | C03 | value=9.43 target=8.0 tolerance=0.800000 |
| R04 | C03 | value=3.61 target=3.0 tolerance=0.300000 |
| R12 | C08 | value=0.63 target=0.76 tolerance=0.050000 |
| R13 | C08 | value=0.5 target=0.64 tolerance=0.050000 |
| R14 | C08 | value=0.5 target=0.62 tolerance=0.050000 |
| R15 | C08 | value=-0.124 target=0.11 tolerance=0.030000 |
| R19 | C09 | evaluated pass_condition: 56.8 >= 64.0 -> False |
| R21 | C09 | value=0.84 target=0.67 tolerance=0.050000 |
| R24 | C09 | value=0.66 target=0.61 tolerance=0.050000 |

## Summary

综合评分 **0.8128**。
共 10 个声明：7 个完全支持，3 个部分支持，0 个未支持。
共 26 条验证规则，17 条通过，9 条失败。

**主要瓶颈**: 实验做错了

## Improvement Suggestions

- **数值精度校准**: 8条规则因数值不匹配失败，需检查复现实验配置、超参数、数据预处理是否与原文一致
- **补全实验**: 1条规则因实验未执行失败，需检查实验调度逻辑，确保所有配置组合跑完
