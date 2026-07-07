# Truth: Consistent multidecadal variability in global temperature reconstructions and simulations over the Common Era

## Metadata

| Field | Value |
|-------|-------|
| paper_id | pages2k_2019 |
| title | Consistent multidecadal variability in global temperature reconstructions and simulations over the Common Era |
| venue | Nature Geoscience, 2019 (doi: 10.1038/s41561-019-0400-0) |
| reproduction_type | full |

---

## Claims

| ID | Text | Evidence Type |
|----|------|---------------|
| C01 | Seven reconstruction methods produce coherent 2000-year GMST reconstructions with correct cooling rates, warmest period fraction, and reference period | numeric |
| C02 | Bandpass-filtered (30-200 yr) GMST shows tighter agreement across methods with correct anomaly range and coherent warm/cold periods | figure |
| C03 | Model/data variance ratios close to 1 (median 1.01) and significant correlations (>98.9%) for all 7 methods | numeric |
| C04 | D&A scaling factors: volcanic ~1, solar not detectable, GHG significant (1300-1800 CE) | numeric + trend |
| C05 | Unforced variability from D&A residuals consistent with control simulation variability | numeric |
| C06 | 51-yr running trends: 79% largest in 20th century, instrumental after 1948 exceeds 99th percentile | numeric |
| C07 | Trend probability after 1850 exceeds AR-noise and random baselines for timescales >20 yr | trend |

---

## Verification Rules

### R01 - Pre-industrial Cooling Rate (Lower-res Proxies)
| Field | Value |
|-------|-------|
| rule_id | R01 |
| claim_ids | C01 |
| type | numeric |
| description | Median pre-industrial cooling rate for methods with lower-than-annual resolution proxies should be approximately -0.23 degC/kyr |
| target_path | task_metrics.P05.cooling_rate_lower_res.median |
| target_value | -0.23 |
| tolerance_abs | 0.08 |
| tolerance_pct | 0.0 |
| confidence_weight | 1.0 |

### R02 - Pre-industrial Cooling Rate (Other Methods)
| Field | Value |
|-------|-------|
| rule_id | R02 |
| claim_ids | C01 |
| type | numeric |
| description | Median pre-industrial cooling rate for methods with annual resolution proxies should be approximately -0.09 degC/kyr |
| target_path | task_metrics.P05.cooling_rate_other.median |
| target_value | -0.09 |
| tolerance_abs | 0.09 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.7 |

### R03 - Warmest 10-year Period Fraction
| Field | Value |
|-------|-------|
| rule_id | R03 |
| claim_ids | C01 |
| type | numeric |
| description | Fraction of ensemble members with warmest 10-year period in the second half of the 20th century should be approximately 94% |
| target_path | task_metrics.P05.warmest_10yr_fraction |
| target_value | 0.94 |
| tolerance_abs | 0.05 |
| tolerance_pct | 0.0 |
| confidence_weight | 1.0 |

### R04 - Temperature Difference at 1600 CE
| Field | Value |
|-------|-------|
| rule_id | R04 |
| claim_ids | C01 |
| type | numeric |
| description | Temperature difference between warmest method (DA) and coldest method (BHM) at approximately 1600 CE should be approximately 0.5 degC |
| target_path | task_metrics.P05.da_bhm_diff_1600ce |
| target_value | 0.5 |
| tolerance_abs | 0.1 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.5 |

### R05 - Anomaly Reference Period
| Field | Value |
|-------|-------|
| rule_id | R05 |
| claim_ids | C01 |
| type | exists |
| description | Anomaly reference period must be 1961-1990 CE |
| target_path | task_metrics.P05.anomaly_reference_period |
| target_value | 1961-1990 |
| scope | json |
| confidence_weight | 0.7 |

### R06 - Bandpass-filtered GMST Figure (Figure 1b)
| Field | Value |
|-------|-------|
| rule_id | R06 |
| claim_ids | C02 |
| type | figure |
| description | Figure 1b: 30-200 yr bandpass-filtered GMST reconstruction ensemble medians for 7 methods over the Common Era. Should show coherent multidecadal variability with narrower spread than unfiltered, anomaly range approximately -0.2 to +0.2 degC, and identifiable warm (~1000, ~1100, ~1200 CE) and cold (~1320, ~1420, ~1560, ~1780 CE) periods |
| target_path | results/figure1b.png |
| judge_prompt | Does this figure show 30-200 year bandpass-filtered global mean surface temperature reconstructions over the Common Era? The figure should display 7 method ensemble medians as colored lines over 1-2000 CE, with a y-axis range of approximately -0.2 to +0.2 degC (temperature anomaly from 1961-1990 baseline). The spread among methods should appear narrower than typical unfiltered reconstructions. Look for coherent oscillations with warm periods around 1000, 1100, 1200 CE and cold periods around 1320, 1420, 1560, 1780 CE. |
| judge_rubric | 5=clear 7-line bandpass-filtered GMST plot with -0.2 to +0.2 degC y-axis, coherent oscillations across methods, narrow spread; 4=bandpass-filtered temperature reconstruction with correct features but missing one detail; 3=temperature time series with multidecadal variability visible but unclear if bandpass-filtered or 7 methods; 2=time series present but wrong format (e.g., unfiltered or wrong y-axis range); 1=no relevant temperature reconstruction; 0=completely unrelated figure |
| judge_threshold | 3.0 |
| confidence_weight | 0.5 |

### R07 - CPS Variance Ratio
| Field | Value |
|-------|-------|
| rule_id | R07 |
| claim_ids | C03 |
| type | numeric |
| description | CPS method variance ratio median (model/data) should be approximately 0.96 |
| target_path | task_metrics.P08.variance_ratio.CPS.median |
| target_value | 0.96 |
| tolerance_abs | 0.05 |
| tolerance_pct | 0.0 |
| confidence_weight | 1.0 |

### R08 - PCR Variance Ratio
| Field | Value |
|-------|-------|
| rule_id | R08 |
| claim_ids | C03 |
| type | numeric |
| description | PCR method variance ratio median should be approximately 1.01 |
| target_path | task_metrics.P08.variance_ratio.PCR.median |
| target_value | 1.01 |
| tolerance_abs | 0.05 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.7 |

### R09 - OIE Variance Ratio
| Field | Value |
|-------|-------|
| rule_id | R09 |
| claim_ids | C03 |
| type | numeric |
| description | OIE method variance ratio median should be approximately 1.13 |
| target_path | task_metrics.P08.variance_ratio.OIE.median |
| target_value | 1.13 |
| tolerance_abs | 0.05 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.7 |

### R10 - M08 Variance Ratio
| Field | Value |
|-------|-------|
| rule_id | R10 |
| claim_ids | C03 |
| type | numeric |
| description | M08 method variance ratio median should be approximately 1.01 |
| target_path | task_metrics.P08.variance_ratio.M08.median |
| target_value | 1.01 |
| tolerance_abs | 0.05 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.7 |

### R11 - PAI Variance Ratio
| Field | Value |
|-------|-------|
| rule_id | R11 |
| claim_ids | C03 |
| type | numeric |
| description | PAI method variance ratio median should be approximately 0.63 |
| target_path | task_metrics.P08.variance_ratio.PAI.median |
| target_value | 0.63 |
| tolerance_abs | 0.05 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.7 |

### R12 - BHM Variance Ratio
| Field | Value |
|-------|-------|
| rule_id | R12 |
| claim_ids | C03 |
| type | numeric |
| description | BHM method variance ratio median should be approximately 1.12 |
| target_path | task_metrics.P08.variance_ratio.BHM.median |
| target_value | 1.12 |
| tolerance_abs | 0.05 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.7 |

### R13 - DA Variance Ratio
| Field | Value |
|-------|-------|
| rule_id | R13 |
| claim_ids | C03 |
| type | numeric |
| description | DA method variance ratio median should be approximately 1.15 |
| target_path | task_metrics.P08.variance_ratio.DA.median |
| target_value | 1.15 |
| tolerance_abs | 0.05 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.7 |

### R14 - Overall Median Variance Ratio
| Field | Value |
|-------|-------|
| rule_id | R14 |
| claim_ids | C03 |
| type | numeric |
| description | Overall median variance ratio across all 7 methods should be approximately 1.01 |
| target_path | task_metrics.P08.overall_median_variance_ratio |
| target_value | 1.01 |
| tolerance_abs | 0.05 |
| tolerance_pct | 0.0 |
| confidence_weight | 1.0 |

### R15 - CPS Correlation Median
| Field | Value |
|-------|-------|
| rule_id | R15 |
| claim_ids | C03 |
| type | numeric |
| description | CPS method model-data correlation median should be approximately 0.64 |
| target_path | task_metrics.P08.correlation.CPS.median |
| target_value | 0.64 |
| tolerance_abs | 0.03 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.7 |

### R16 - PCR Correlation Median
| Field | Value |
|-------|-------|
| rule_id | R16 |
| claim_ids | C03 |
| type | numeric |
| description | PCR method model-data correlation median should be approximately 0.60 |
| target_path | task_metrics.P08.correlation.PCR.median |
| target_value | 0.6 |
| tolerance_abs | 0.03 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.7 |

### R17 - OIE Correlation Median
| Field | Value |
|-------|-------|
| rule_id | R17 |
| claim_ids | C03 |
| type | numeric |
| description | OIE method model-data correlation median should be approximately 0.61 |
| target_path | task_metrics.P08.correlation.OIE.median |
| target_value | 0.61 |
| tolerance_abs | 0.03 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.7 |

### R18 - M08 Correlation Median
| Field | Value |
|-------|-------|
| rule_id | R18 |
| claim_ids | C03 |
| type | numeric |
| description | M08 method model-data correlation median should be approximately 0.65 |
| target_path | task_metrics.P08.correlation.M08.median |
| target_value | 0.65 |
| tolerance_abs | 0.03 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.7 |

### R19 - PAI Correlation Median
| Field | Value |
|-------|-------|
| rule_id | R19 |
| claim_ids | C03 |
| type | numeric |
| description | PAI method model-data correlation median should be approximately 0.63 |
| target_path | task_metrics.P08.correlation.PAI.median |
| target_value | 0.63 |
| tolerance_abs | 0.03 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.7 |

### R20 - BHM Correlation Median
| Field | Value |
|-------|-------|
| rule_id | R20 |
| claim_ids | C03 |
| type | numeric |
| description | BHM method model-data correlation median should be approximately 0.53 |
| target_path | task_metrics.P08.correlation.BHM.median |
| target_value | 0.53 |
| tolerance_abs | 0.03 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.7 |

### R21 - DA Correlation Median
| Field | Value |
|-------|-------|
| rule_id | R21 |
| claim_ids | C03 |
| type | numeric |
| description | DA method model-data correlation median should be approximately 0.62 |
| target_path | task_metrics.P08.correlation.DA.median |
| target_value | 0.62 |
| tolerance_abs | 0.03 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.7 |

### R22 - AR(1) Noise Exceedance
| Field | Value |
|-------|-------|
| rule_id | R22 |
| claim_ids | C03 |
| type | trend |
| description | All 7 methods must have more than 95% of ensemble members with model-data correlation exceeding AR(1) noise threshold; the minimum across methods should be above 95% |
| comparison | task_metrics.P08.ar1_exceedance.min > 0.95 |
| confidence_weight | 1.0 |

### R23 - Total Forcing Scaling Factor
| Field | Value |
|-------|-------|
| rule_id | R23 |
| claim_ids | C04 |
| type | numeric |
| description | Total forcing median D&A scaling factor should be approximately 0.89 |
| target_path | task_metrics.P10.total_forcing_scaling.median |
| target_value | 0.89 |
| tolerance_abs | 0.1 |
| tolerance_pct | 0.0 |
| confidence_weight | 1.0 |

### R24 - Volcanic Scaling Factor Detectability
| Field | Value |
|-------|-------|
| rule_id | R24 |
| claim_ids | C04 |
| type | trend |
| description | Volcanic forcing scaling factor 90% confidence interval should encompass 1 (lower bound < 1 < upper bound) |
| comparison | task_metrics.P10.volcanic_scaling.ci_90_lower < 1 and task_metrics.P10.volcanic_scaling.ci_90_upper > 1 |
| confidence_weight | 1.0 |

### R25 - Solar Forcing Non-detectability
| Field | Value |
|-------|-------|
| rule_id | R25 |
| claim_ids | C04 |
| type | trend |
| description | Solar forcing scaling factor 90% confidence interval should include zero (not significantly different from zero) |
| comparison | task_metrics.P10.solar_scaling.ci_90_lower < 0 and task_metrics.P10.solar_scaling.ci_90_upper > 0 |
| confidence_weight | 1.0 |

### R26 - GHG Forcing Significance
| Field | Value |
|-------|-------|
| rule_id | R26 |
| claim_ids | C04 |
| type | trend |
| description | GHG forcing scaling factor 90% confidence interval should exclude zero (significantly different from zero) |
| comparison | task_metrics.P10.ghg_scaling.ci_90_lower > 0 |
| confidence_weight | 1.0 |

### R27 - D&A Residuals Within Control Range
| Field | Value |
|-------|-------|
| rule_id | R27 |
| claim_ids | C05 |
| type | numeric |
| description | Percentage of D&A residual-based unforced variability estimates within the 5%-95% range of control run estimates should be approximately 99% |
| target_path | task_metrics.P11.da_residuals_within_control_pct |
| target_value | 0.99 |
| tolerance_abs | 0.04 |
| tolerance_pct | 0.0 |
| confidence_weight | 1.0 |

### R28 - D&A Residual Amplitude Range
| Field | Value |
|-------|-------|
| rule_id | R28 |
| claim_ids | C05 |
| type | numeric |
| description | D&A residual amplitude should be in the range of approximately 0.02 to 0.07 degC |
| target_path | task_metrics.P11.da_residual_amplitude.upper |
| target_value | 0.045 |
| tolerance_abs | 0.025 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.5 |

### R29 - D&A Estimate Count
| Field | Value |
|-------|-------|
| rule_id | R29 |
| claim_ids | C05 |
| type | numeric |
| description | Number of D&A estimates should be exactly 7000 |
| target_path | task_metrics.P11.n_da_estimates |
| target_value | 7000 |
| tolerance_abs | 0 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.3 |

### R30 - Control Run Estimate Count
| Field | Value |
|-------|-------|
| rule_id | R30 |
| claim_ids | C05 |
| type | numeric |
| description | Number of control run estimates should be exactly 43 |
| target_path | task_metrics.P11.n_control_estimates |
| target_value | 43 |
| tolerance_abs | 0 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.3 |

### R31 - Fraction with Largest Trend in 20th Century
| Field | Value |
|-------|-------|
| rule_id | R31 |
| claim_ids | C06 |
| type | numeric |
| description | Fraction of ensemble members with largest 51-year trend in the 20th century should be approximately 79% |
| target_path | task_metrics.P12.largest_trend_20th_century_pct |
| target_value | 0.79 |
| tolerance_abs | 0.03 |
| tolerance_pct | 0.0 |
| confidence_weight | 1.0 |

### R32 - Trend Window Length
| Field | Value |
|-------|-------|
| rule_id | R32 |
| claim_ids | C06 |
| type | numeric |
| description | Trend window length should be exactly 51 years |
| target_path | task_metrics.P12.trend_window |
| target_value | 51 |
| tolerance_abs | 0 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.5 |

### R33 - Total Ensemble Members
| Field | Value |
|-------|-------|
| rule_id | R33 |
| claim_ids | C06 |
| type | numeric |
| description | Total number of ensemble members should be exactly 7000 (7 methods x 1000) |
| target_path | task_metrics.P12.total_ensemble_members |
| target_value | 7000 |
| tolerance_abs | 0 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.3 |

### R34 - Running Trends Figure (Figure 4a)
| Field | Value |
|-------|-------|
| rule_id | R34 |
| claim_ids | C06 |
| type | figure |
| description | Figure 4a: 51-year running linear GMST trends over the Common Era. Should show reconstruction ensemble percentiles, instrumental data overlay, EBM volcanic response (cooling spikes at major eruptions), and pre-industrial percentile thresholds. Two distinct warming periods in the 20th century should be visible (early 20th century and post-1970s) |
| target_path | results/figure4a.png |
| judge_prompt | Does this figure show 51-year running trends of global mean surface temperature over the Common Era (1-2000 CE)? The figure should display ensemble percentile shading (e.g., 5-95%, 25-75%), instrumental data as a line overlay, and distinct cooling spikes corresponding to major volcanic eruptions. Two warming periods in the 20th century should be visible: early 20th century and post-1970s. The y-axis should show trend units (degC per 51 years). Look for pre-industrial percentile threshold lines and EBM volcanic response curves. |
| judge_rubric | 5=clear 51-yr running trend plot over Common Era with ensemble shading, instrumental data overlay, volcanic cooling spikes, and two 20th-century warming periods visible; 4=running trend plot with most features but missing one element (e.g., no instrumental overlay or no EBM); 3=temperature trend time series but unclear if 51-yr running or missing key features; 2=time series present but wrong type (e.g., not running trends or wrong window); 1=has temperature data but not a trend plot; 0=completely unrelated figure |
| judge_threshold | 3.0 |
| confidence_weight | 0.4 |

### R35 - Trend Probability vs Length (Figure 4b)
| Field | Value |
|-------|-------|
| rule_id | R35 |
| claim_ids | C07 |
| type | figure |
| description | Figure 4b: Ensemble probability that the largest trend occurs after 1850 CE as a function of trend length (10-150 yr). Should show three curves: real reconstructions, AR-noise proxy reconstructions, and random numbers. Reconstructions should clearly exceed AR-noise and random baselines for trend lengths longer than approximately 20 years |
| target_path | results/figure4b.png |
| judge_prompt | Does this figure show the probability of the largest trend occurring after 1850 CE as a function of trend length (approximately 10-150 years on x-axis)? There should be three distinct curves: real reconstructions (highest probability), AR-noise proxy reconstructions (intermediate), and random numbers (lowest). The reconstruction curve should be clearly above the AR-noise curve for trend lengths greater than about 20 years. The y-axis should show probability (0 to 1 or 0% to 100%). The random number baseline should decrease with increasing trend length. |
| judge_rubric | 5=clear probability vs trend length plot with three distinct curves (reconstructions > AR-noise > random), reconstruction curve clearly above AR-noise after ~20 yr, probability y-axis; 4=probability vs trend length with three curves but one is hard to distinguish or missing label; 3=probability vs trend length with at least two curves showing separation; 2=has probability plot but wrong variables or only one curve; 1=has a plot but not probability vs trend length; 0=completely unrelated figure |
| judge_threshold | 3.0 |
| confidence_weight | 0.5 |

### R36 - Reconstructions Exceed AR-noise for Long Trends
| Field | Value |
|-------|-------|
| rule_id | R36 |
| claim_ids | C07 |
| type | trend |
| description | For trend lengths longer than approximately 20 years, the reconstruction probability of largest post-1850 trend should consistently exceed the AR-noise proxy probability |
| comparison | task_metrics.P13.recon_prob_51yr > task_metrics.P13.arnoise_prob_51yr |
| confidence_weight | 1.0 |

### R37 - Reconstructions Exceed Random Baseline
| Field | Value |
|-------|-------|
| rule_id | R37 |
| claim_ids | C07 |
| type | trend |
| description | For trend lengths longer than approximately 20 years, the reconstruction probability of largest post-1850 trend should consistently exceed the random number baseline probability |
| comparison | task_metrics.P13.recon_prob_51yr > task_metrics.P13.random_prob_51yr |
| confidence_weight | 0.7 |
