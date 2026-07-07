# wong_2020

## Metadata

| Field | Value |
|-------|-------|
| Paper ID | wong_2020 |
| Score | 0.5226 |
| Weighted Score | 0.2645 |
| Reproduction Mode | full |
| Evidence Completeness | 100.00% |
| Confidence | 0.70 |

## Bottleneck Analysis

### 实验做错了 (15 rules)

- **R01**: value=0.662 target=0.85 tolerance=0.085000
- **R02**: value=14.29 target=12.34 tolerance=1.234000
- **R03**: value=0.417 target=0.72 tolerance=0.072000
- **R04**: value=15.57 target=19.17 tolerance=1.917000
- **R05**: value=11494.48 target=14910.0 tolerance=1491.000000
- **R06**: value=1.74 target=0.7 tolerance=0.070000
- **R08**: value=10.91 target=16.31 tolerance=1.631000
- **R09**: value=0.77 target=0.99 tolerance=0.099000
- **R10**: value=1.97 target=-1.4 tolerance=0.140000
- **R11**: value=0.622 target=0.8 tolerance=0.080000
- **R12**: value=0.535 target=0.33 tolerance=0.033000
- **R14**: value=2.8 target=6.43 tolerance=0.643000
- **R16**: value=788.47 target=1464.0 tolerance=146.400000
- **R17**: value=191.92 target=440.0 tolerance=44.000000
- **R21**: value=1.0 target=0.0 tolerance=0.000000

## Claim Status

| Claim | Status | Rules Passed |
|-------|--------|-------------|
| C01 | FAIL | 0/4 |
| C02 | PARTIAL | 1/4 |
| C03 | PARTIAL | 1/6 |
| C04 | PASS | 1/1 |
| C05 | PARTIAL | 1/3 |
| C06 | PASS | 1/1 |
| C07 | PASS | 1/1 |
| C08 | PARTIAL | 1/2 |

## Failed Rules Detail

| Rule ID | Claims | Failure Reason |
|---------|--------|----------------|
| R01 | C01 | value=0.662 target=0.85 tolerance=0.085000 |
| R02 | C01 | value=14.29 target=12.34 tolerance=1.234000 |
| R03 | C01 | value=0.417 target=0.72 tolerance=0.072000 |
| R04 | C01 | value=15.57 target=19.17 tolerance=1.917000 |
| R05 | C02 | value=11494.48 target=14910.0 tolerance=1491.000000 |
| R06 | C02 | value=1.74 target=0.7 tolerance=0.070000 |
| R08 | C02 | value=10.91 target=16.31 tolerance=1.631000 |
| R09 | C03 | value=0.77 target=0.99 tolerance=0.099000 |
| R10 | C03 | value=1.97 target=-1.4 tolerance=0.140000 |
| R11 | C03 | value=0.622 target=0.8 tolerance=0.080000 |
| R12 | C03 | value=0.535 target=0.33 tolerance=0.033000 |
| R14 | C03 | value=2.8 target=6.43 tolerance=0.643000 |
| R16 | C05 | value=788.47 target=1464.0 tolerance=146.400000 |
| R17 | C05 | value=191.92 target=440.0 tolerance=44.000000 |
| R21 | C08 | value=1.0 target=0.0 tolerance=0.000000 |

## Summary

综合评分 **0.5226**。
共 8 个声明：3 个完全支持，4 个部分支持，1 个未支持。
共 22 条验证规则，7 条通过，15 条失败。

**主要瓶颈**: 实验做错了

## Improvement Suggestions

- **数值精度校准**: 15条规则因数值不匹配失败，需检查复现实验配置、超参数、数据预处理是否与原文一致
