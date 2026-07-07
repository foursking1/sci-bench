# Truth: Diagnostic Model and Analysis of the Surface Currents in the Tropical Pacific Ocean

## Metadata

| Field | Value |
|-------|-------|
| paper_id | bonjean_2002 |
| title | Diagnostic Model and Analysis of the Surface Currents in the Tropical Pacific Ocean |
| venue | Journal of Physical Oceanography, Volume 32, October 2002 (pp. 2938-2954) |
| reproduction_type | full |

---

## Claims

| ID | Text | Evidence Type |
|----|------|---------------|
| C01 | Optimal depth-scale parameter H = 70 m determined by minimizing momentum balance residuals and STDD | numeric |
| C02 | Equatorial momentum balance shows wind stress and pressure gradient compensation | figure |
| C03 | Mean diagnostic velocity agrees with drifter field; STDD = 8 cm/s (zonal), 3 cm/s (meridional) | numeric |
| C04 | Diagnostic velocity from GCM fields is nearly identical to GCM velocity | figure |
| C05 | Diagnostic model reproduces SEC two-branch structure with reduced westward bias vs LMLN | trend |
| C06 | Seasonal cycle shows SEC reversal and NECC variations | figure |
| C07 | De-meaned seasonal fluctuations agree with DRCM in Hovmoller diagrams | figure |
| C08 | TAO time series correlations 0.66, 0.76, 0.64, 0.62; reduced mean bias | numeric |
| C09 | EOF analysis yields explained variance >64%, Gaussian e-folding ~3.1 deg, PC-TAO correlations | numeric |
| C10 | ENSO velocity anomalies show current reversal and eastward flow | figure |

---

## Verification Rules

### R01 - Optimal H Parameter
| Field | Value |
|-------|-------|
| rule_id | R01 |
| claim_ids | C01 |
| type | numeric |
| description | Optimal depth-scale parameter H should be approximately 70 m, determined by minimizing both momentum balance residuals and STDD |
| target_path | task_metrics.P06.optimal_H |
| target_value | 70 |
| tolerance_abs | 5 |
| confidence_weight | 1.0 |

### R02 - Momentum Balance Figure
| Field | Value |
|-------|-------|
| rule_id | R02 |
| claim_ids | C02 |
| type | compare |
| description | Compare generated equatorial momentum balance figure against reference |
| reference_path | figures/fig02.png |
| confidence_weight | 0.4 |

### R03 - STDD Zonal
| Field | Value |
|-------|-------|
| rule_id | R03 |
| claim_ids | C03 |
| type | numeric |
| description | Standard deviation of difference between modeled and drifter zonal velocity should be 8 cm/s |
| target_path | task_metrics.P09.stdd_zonal |
| target_value | 8.0 |
| tolerance_pct | 10.0 |
| confidence_weight | 1.0 |

### R04 - STDD Meridional
| Field | Value |
|-------|-------|
| rule_id | R04 |
| claim_ids | C03 |
| type | numeric |
| description | Standard deviation of difference between modeled and drifter meridional velocity should be 3 cm/s |
| target_path | task_metrics.P09.stdd_meridional |
| target_value | 3.0 |
| tolerance_pct | 10.0 |
| confidence_weight | 1.0 |

### R05 - Mean Velocity Drifter Comparison Figure
| Field | Value |
|-------|-------|
| rule_id | R05 |
| claim_ids | C03 |
| type | compare |
| description | Compare generated mean velocity vector map against reference |
| reference_path | figures/fig03.png |
| confidence_weight | 0.4 |

### R06 - GCM Velocity Comparison Figure
| Field | Value |
|-------|-------|
| rule_id | R06 |
| claim_ids | C04 |
| type | compare |
| description | Compare generated GCM velocity comparison figure against reference |
| reference_path | figures/fig04.png |
| confidence_weight | 0.4 |

### R07 - SEC Two-Branch Structure
| Field | Value |
|-------|-------|
| rule_id | R07 |
| claim_ids | C05 |
| type | trend |
| description | Diagnostic model SEC two-branch structure in meridional profiles (140W-100W): diagnostic model should better match drifter profiles than LMLN, showing equatorial minimum splitting the SEC into northern and southern branches |
| comparison | task_metrics.P13.diagnostic_vs_drifter.mse < task_metrics.P13.lmln_vs_drifter.mse |
| confidence_weight | 0.7 |

### R08 - Meridional Profile Comparison Figure
| Field | Value |
|-------|-------|
| rule_id | R08 |
| claim_ids | C05 |
| type | compare |
| description | Compare generated meridional profile comparison figure against reference |
| reference_path | figures/repro/fig04_meridional_profiles.png |
| confidence_weight | 0.4 |

### R09 - Seasonal Cycle Figure
| Field | Value |
|-------|-------|
| rule_id | R09 |
| claim_ids | C06 |
| type | compare |
| description | Compare generated seasonal cycle velocity vector maps against reference |
| reference_path | figures/repro/fig05_seasonal_cycle.png |
| confidence_weight | 0.4 |

### R10 - Hovmoller Diagrams Figure
| Field | Value |
|-------|-------|
| rule_id | R10 |
| claim_ids | C07 |
| type | compare |
| description | Compare generated Hovmoller diagram figure against reference |
| reference_path | figures/repro/fig06_hovmoller_seasonal.png |
| confidence_weight | 0.4 |

### R11 - TAO Correlation Coefficients
| Field | Value |
|-------|-------|
| rule_id | R11 |
| claim_ids | C08 |
| type | numeric |
| description | Correlation between model and TAO zonal velocity at 165E should be approximately 0.66 |
| target_path | task_metrics.P15.per_station.165E_0N.u.c |
| target_value | 0.66 |
| tolerance_abs | 0.05 |
| confidence_weight | 0.7 |

### R12 - TAO Correlation at 170W
| Field | Value |
|-------|-------|
| rule_id | R12 |
| claim_ids | C08 |
| type | numeric |
| description | Correlation between model and TAO zonal velocity at 170W should be approximately 0.76 |
| target_path | task_metrics.P15.per_station.170W_0N.u.c |
| target_value | 0.76 |
| tolerance_abs | 0.05 |
| confidence_weight | 0.7 |

### R13 - TAO Correlation at 140W
| Field | Value |
|-------|-------|
| rule_id | R13 |
| claim_ids | C08 |
| type | numeric |
| description | Correlation between model and TAO zonal velocity at 140W should be approximately 0.64 |
| target_path | task_metrics.P15.per_station.140W_0N.u.c |
| target_value | 0.64 |
| tolerance_abs | 0.05 |
| confidence_weight | 0.7 |

### R14 - TAO Correlation at 110W
| Field | Value |
|-------|-------|
| rule_id | R14 |
| claim_ids | C08 |
| type | numeric |
| description | Correlation between model and TAO zonal velocity at 110W should be approximately 0.62 |
| target_path | task_metrics.P15.per_station.110W_0N.u.c |
| target_value | 0.62 |
| tolerance_abs | 0.05 |
| confidence_weight | 0.7 |

### R15 - Mean Bias at 140W
| Field | Value |
|-------|-------|
| rule_id | R15 |
| claim_ids | C08 |
| type | numeric |
| description | Mean bias (u_bar - u_TAO) at 140W should be approximately 0.11 m/s, substantially lower than LMLN value of 0.43 m/s |
| target_path | task_metrics.P15.per_station.140W_0N.u.mean_bias |
| target_value | 0.11 |
| tolerance_abs | 0.03 |
| confidence_weight | 0.7 |

### R16 - Mean Bias at 110W
| Field | Value |
|-------|-------|
| rule_id | R16 |
| claim_ids | C08 |
| type | numeric |
| description | Mean bias (u_bar - u_TAO) at 110W should be approximately 0.01 m/s, substantially lower than LMLN value of 0.30 m/s |
| target_path | task_metrics.P15.per_station.110W_0N.u.mean_bias |
| target_value | 0.01 |
| tolerance_abs | 0.03 |
| confidence_weight | 0.7 |

### R17 - Bias Improvement Over LMLN
| Field | Value |
|-------|-------|
| rule_id | R17 |
| claim_ids | C08 |
| type | trend |
| description | Diagnostic model mean bias at 140W and 110W should be substantially lower than LMLN bias values (0.43 and 0.30 m/s respectively) |
| comparison | task_metrics.P15.per_station.140W_0N.u.mean_bias < task_metrics.P15.lmln_bias.140W_0N && task_metrics.P15.per_station.110W_0N.u.mean_bias < task_metrics.P15.lmln_bias.110W_0N |
| confidence_weight | 0.7 |

### R18 - TAO Time Series Figure
| Field | Value |
|-------|-------|
| rule_id | R18 |
| claim_ids | C08 |
| type | compare |
| description | Compare generated TAO time series figure against reference |
| reference_path | figures/fig7_tao_timeseries.png |
| confidence_weight | 0.3 |

### R19 - EOF Explained Variance
| Field | Value |
|-------|-------|
| rule_id | R19 |
| claim_ids | C09 |
| type | numeric |
| description | First-mode EOF explained variance should exceed 64% at all four longitudes |
| target_path | task_metrics.P16.eof.explained_variance_first_mode |
| target_value | 64.0 |
| tolerance_pct | 0 |
| tolerance_abs | 5.0 |
| pass_condition | actual >= 64.0 |
| confidence_weight | 1.0 |

### R20 - EOF Gaussian E-folding Scale
| Field | Value |
|-------|-------|
| rule_id | R20 |
| claim_ids | C09 |
| type | numeric |
| description | EOF meridional profile Gaussian fit e-folding scale lambda should be approximately 3.1 degrees on average |
| target_path | task_metrics.P16.eof.gaussian_fit.lambda_mean |
| target_value | 3.1 |
| tolerance_abs | 0.5 |
| confidence_weight | 0.7 |

### R21 - EOF PC-TAO Correlation at 165E
| Field | Value |
|-------|-------|
| rule_id | R21 |
| claim_ids | C09 |
| type | numeric |
| description | Correlation between EOF first-mode PC and TAO zonal current at 165E should be approximately 0.67 |
| target_path | task_metrics.P16.eof.pc_tao_correlation.165E |
| target_value | 0.67 |
| tolerance_abs | 0.05 |
| confidence_weight | 0.7 |

### R22 - EOF PC-TAO Correlation at 170W
| Field | Value |
|-------|-------|
| rule_id | R22 |
| claim_ids | C09 |
| type | numeric |
| description | Correlation between EOF first-mode PC and TAO zonal current at 170W should be approximately 0.77 |
| target_path | task_metrics.P16.eof.pc_tao_correlation.170W |
| target_value | 0.77 |
| tolerance_abs | 0.05 |
| confidence_weight | 0.7 |

### R23 - EOF PC-TAO Correlation at 140W
| Field | Value |
|-------|-------|
| rule_id | R23 |
| claim_ids | C09 |
| type | numeric |
| description | Correlation between EOF first-mode PC and TAO zonal current at 140W should be approximately 0.66 |
| target_path | task_metrics.P16.eof.pc_tao_correlation.140W |
| target_value | 0.66 |
| tolerance_abs | 0.05 |
| confidence_weight | 0.7 |

### R24 - EOF PC-TAO Correlation at 110W
| Field | Value |
|-------|-------|
| rule_id | R24 |
| claim_ids | C09 |
| type | numeric |
| description | Correlation between EOF first-mode PC and TAO zonal current at 110W should be approximately 0.61 |
| target_path | task_metrics.P16.eof.pc_tao_correlation.110W |
| target_value | 0.61 |
| tolerance_abs | 0.05 |
| confidence_weight | 0.7 |

### R25 - EOF Analysis Figure
| Field | Value |
|-------|-------|
| rule_id | R25 |
| claim_ids | C09 |
| type | compare |
| description | Compare generated EOF analysis figure against reference |
| reference_path | figures/fig8_eof.png |
| confidence_weight | 0.3 |

### R26 - ENSO Anomaly Figure
| Field | Value |
|-------|-------|
| rule_id | R26 |
| claim_ids | C10 |
| type | compare |
| description | Compare generated ENSO anomaly figure against reference |
| reference_path | figures/repro/fig09_enso_anomalies.png |
| confidence_weight | 0.4 |
