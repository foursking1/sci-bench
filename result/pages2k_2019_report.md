# pages2k_2019

## Metadata

| Field | Value |
|-------|-------|
| Paper ID | pages2k_2019 |
| Score | 0.8857 |
| Weighted Score | 0.8361 |
| Reproduction Mode | full |
| Evidence Completeness | 100.00% |
| Confidence | 0.72 |

## Bottleneck Analysis

### 实验未执行 (1 rules)

- **R04**: evaluated pass_condition: 95.89 >= 98.9 - 1.0 -> False

### 实验做错了 (1 rules)

- **R03**: value=1.178 target=1.01 tolerance=0.151500

## Claim Status

| Claim | Status | Rules Passed |
|-------|--------|-------------|
| C01 | PASS | 2/2 |
| C02 | PASS | 1/1 |
| C03 | PARTIAL | 1/3 |
| C04 | PASS | 4/4 |
| C05 | PASS | 2/2 |
| C06 | PASS | 3/3 |
| C07 | PASS | 2/2 |

## Failed Rules Detail

| Rule ID | Claims | Failure Reason |
|---------|--------|----------------|
| R03 | C03 | value=1.178 target=1.01 tolerance=0.151500 |
| R04 | C03 | evaluated pass_condition: 95.89 >= 98.9 - 1.0 -> False |

## Summary

综合评分 **0.8857**。
共 7 个声明：6 个完全支持，1 个部分支持，0 个未支持。
共 17 条验证规则，15 条通过，2 条失败。

**主要瓶颈**: 实验未执行

## Improvement Suggestions

- **数值精度校准**: 1条规则因数值不匹配失败，需检查复现实验配置、超参数、数据预处理是否与原文一致
- **补全实验**: 1条规则因实验未执行失败，需检查实验调度逻辑，确保所有配置组合跑完
