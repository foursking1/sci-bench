# 08_tapley_2004

## Metadata

| Field | Value |
|-------|-------|
| Paper ID | 08_tapley_2004 |
| Score | 0.8812 |
| Weighted Score | 0.7273 |
| Reproduction Mode | full |
| Evidence Completeness | 100.00% |
| Confidence | 0.82 |

## Bottleneck Analysis

### 实验做错了 (6 rules)

- **R02**: value=1.6526 target=3.0 tolerance=0.300000
- **R03**: value=0.5922 target=0.9 tolerance=0.100000
- **R04**: value=-5.8576 target=-6.4 tolerance=0.500000
- **R08**: value=2.2543 target=3.2 tolerance=0.320000
- **R10**: value=-4.7377 target=-4.0 tolerance=0.400000
- **R13**: value=11.3691 target=14.0 tolerance=1.000000

## Claim Status

| Claim | Status | Rules Passed |
|-------|--------|-------------|
| C01 | PARTIAL | 7/12 |
| C02 | PARTIAL | 2/3 |
| C03 | PASS | 1/1 |
| C04 | PASS | 2/2 |
| C05 | PASS | 3/3 |
| C06 | PASS | 2/2 |
| C07 | PASS | 1/1 |

## Failed Rules Detail

| Rule ID | Claims | Failure Reason |
|---------|--------|----------------|
| R02 | C01 | value=1.6526 target=3.0 tolerance=0.300000 |
| R03 | C01 | value=0.5922 target=0.9 tolerance=0.100000 |
| R04 | C01 | value=-5.8576 target=-6.4 tolerance=0.500000 |
| R08 | C01 | value=2.2543 target=3.2 tolerance=0.320000 |
| R10 | C01 | value=-4.7377 target=-4.0 tolerance=0.400000 |
| R13 | C02 | value=11.3691 target=14.0 tolerance=1.000000 |

## Summary

综合评分 **0.8812**。
共 7 个声明：5 个完全支持，2 个部分支持，0 个未支持。
共 24 条验证规则，18 条通过，6 条失败。

**主要瓶颈**: 实验做错了

## Improvement Suggestions

- **数值精度校准**: 6条规则因数值不匹配失败，需检查复现实验配置、超参数、数据预处理是否与原文一致
