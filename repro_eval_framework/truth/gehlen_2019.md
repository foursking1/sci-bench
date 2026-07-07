# Truth: A framework for assessing climate change impacts on shared fisheries resources and dependent coastal communities

## Metadata

| Field | Value |
|-------|-------|
| paper_id | gehlen_2019 |
| title | A framework for assessing climate change impacts on shared fisheries resources and dependent coastal communities |
| venue | Frontiers in Marine Science, 2019 (doi: 10.3389/fmars.2019.00579) |
| reproduction_type | full |

---

## Claims

| ID | Text | Evidence Type |
|----|------|---------------|
| C01 | GAM-based habitat suitability model produces correct current and projected (BNAM, CM2.6) spatial maps across the Scotian Shelf and Gulf of Maine | compare |
| C02 | Percent change in suitable habitat per LFA: CM2.6 projects consistently higher gains than BNAM; LFA 33 more than doubles under CM2.6; no net loss for any LFA | numeric + trend |
| C03 | LVI scores per LFA range from 2 to 2.5; LFA 41 scores 2.5 (BNAM) / 2 (CM2.6); none experience net loss | numeric |
| C04 | CIVI sub-index scores per LFA: ESI increases west to east, ISI similar across LFAs, SESI varies widely | numeric + trend |
| C05 | Integrated assessment: LFA 34 high SESI (dependent on fishing), LFA 27 more diverse SESI distribution | compare |
| C06 | BNAM and CM2.6 bottom temperature projections show similar spatial patterns but different magnitudes | trend |

---

## Verification Rules

### R01 - Habitat Suitability Maps (Figure 3)
| Field | Value |
|-------|-------|
| rule_id | R01 |
| claim_ids | C01 |
| type | compare |
| description | Compare generated current and projected habitat suitability maps against reference. Should show 4-panel spatial map: reference map with LFAs, current prediction (highest in Bay of Fundy/Browns Bank, 0-0.92 scale), BNAM projection (expansion to northeast), CM2.6 projection (similar but more intense) |
| reference_path | figures/fig03.png |
| confidence_weight | 0.5 |

### R02 - Habitat Suitability Scale
| Field | Value |
|-------|-------|
| rule_id | R02 |
| claim_ids | C01 |
| type | numeric |
| description | Habitat suitability scale must be 0-1 continuous, where 0 = low likelihood, 1 = high likelihood |
| target_path | task_metrics.P01.habitat_suitability_scale.max |
| target_value | 1.0 |
| tolerance_abs | 0.01 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.5 |

### R03 - Bootstrap Iterations
| Field | Value |
|-------|-------|
| rule_id | R03 |
| claim_ids | C01 |
| type | numeric |
| description | Number of bootstrap iterations should be exactly 100 |
| target_path | task_metrics.P01.n_bootstrap_iterations |
| target_value | 100 |
| tolerance_abs | 0 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.5 |

### R04 - Bootstrap Data Fraction
| Field | Value |
|-------|-------|
| rule_id | R04 |
| claim_ids | C01 |
| type | numeric |
| description | Bootstrap should use 85% of data per iteration |
| target_path | task_metrics.P01.bootstrap_data_fraction |
| target_value | 0.85 |
| tolerance_abs | 0.01 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.5 |

### R05 - Maximum Suitability Value
| Field | Value |
|-------|-------|
| rule_id | R05 |
| claim_ids | C01 |
| type | numeric |
| description | Maximum suitability value should be approximately 0.92 |
| target_path | task_metrics.P01.max_suitability_value |
| target_value | 0.92 |
| tolerance_abs | 0.05 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.5 |

### R06 - Habitat Change Maps (Figure 4)
| Field | Value |
|-------|-------|
| rule_id | R06 |
| claim_ids | C02 |
| type | compare |
| description | Compare generated spatial change in habitat suitability maps against reference. Should show 5-panel figure: percent change maps for CM2.6 and BNAM (red=gain up to 168%, blue=loss up to -168%), absolute change maps, and boxplots of median suitability per LFA |
| reference_path | figures/fig04.png |
| confidence_weight | 0.5 |

### R07 - Percent Change Boxplots (Figure 5)
| Field | Value |
|-------|-------|
| rule_id | R07 |
| claim_ids | C02 |
| type | compare |
| description | Compare generated percent change in suitable habitat boxplots against reference. Should show two panels: BNAM and CM2.6 percent gain/loss per LFA, with CM2.6 consistently higher |
| reference_path | figures/fig05.png |
| confidence_weight | 0.5 |

### R08 - Suitability Threshold
| Field | Value |
|-------|-------|
| rule_id | R08 |
| claim_ids | C02 |
| type | numeric |
| description | Habitat suitability threshold for "suitable" should be >0.3 |
| target_path | task_metrics.P02.suitability_threshold |
| target_value | 0.3 |
| tolerance_abs | 0.01 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.7 |

### R09 - CM2.6 Higher Gains Than BNAM (LFA 33)
| Field | Value |
|-------|-------|
| rule_id | R09 |
| claim_ids | C02 |
| type | trend |
| description | For LFA 33, percent habitat gain under CM2.6 should be substantially higher than under BNAM (CM2.6 more than doubles ~130-200%, BNAM almost doubles ~80-100%) |
| comparison | task_metrics.P02.percent_gain.LFA33.CM26 > task_metrics.P02.percent_gain.LFA33.BNAM |
| confidence_weight | 1.0 |

### R10 - No Net Loss for Any LFA
| Field | Value |
|-------|-------|
| rule_id | R10 |
| claim_ids | C02 |
| type | trend |
| description | None of the LFAs should experience net loss of suitable habitat; median percent change should be positive for all LFAs under both scenarios |
| comparison | task_metrics.P02.median_percent_gain_all_LFAs > 0 |
| confidence_weight | 1.0 |

### R11 - LFA 35 Decrease Under Warming
| Field | Value |
|-------|-------|
| rule_id | R11 |
| claim_ids | C02 |
| type | trend |
| description | LFA 35 (Bay of Fundy) should show a decrease in suitability despite starting at high level, suggesting waters warm beyond optimal by mid-century |
| comparison | task_metrics.P02.suitability_change.LFA35 < 0 |
| confidence_weight | 0.7 |

### R12 - CM2.6 Consistently Higher Than BNAM
| Field | Value |
|-------|-------|
| rule_id | R12 |
| claim_ids | C02 |
| type | trend |
| description | CM2.6 projected habitat gains should be consistently higher than BNAM gains across all LFAs |
| comparison | task_metrics.P02.total_gain.CM26 > task_metrics.P02.total_gain.BNAM |
| confidence_weight | 1.0 |

### R13 - LVI by CIVI Boxplots (Figure 6)
| Field | Value |
|-------|-------|
| rule_id | R13 |
| claim_ids | C03 |
| type | compare |
| description | Compare generated vulnerability sub-index boxplots against reference. Should show boxplots of ESI, ISI, SESI per LFA (38, 36, 35, 34, 33, 32, 31B, 31A, 27) with LVI background shading. ESI increases west to east, ISI moderate ~3, SESI varies widely |
| reference_path | figures/fig06.png |
| confidence_weight | 0.5 |

### R14 - LVI Score Range
| Field | Value |
|-------|-------|
| rule_id | R14 |
| claim_ids | C03 |
| type | numeric |
| description | LVI scores across all LFAs should range from 2 to 2.5 |
| target_path | task_metrics.P03.lvi_score.range_max |
| target_value | 2.5 |
| tolerance_abs | 0.25 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.7 |

### R15 - LFA 33 LVI Score
| Field | Value |
|-------|-------|
| rule_id | R15 |
| claim_ids | C03 |
| type | numeric |
| description | LFA 33 LVI score should be 2 (lowest) |
| target_path | task_metrics.P03.lvi_score.LFA33 |
| target_value | 2.0 |
| tolerance_abs | 0.25 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.7 |

### R16 - LFA 34 LVI Score
| Field | Value |
|-------|-------|
| rule_id | R16 |
| claim_ids | C03 |
| type | numeric |
| description | LFA 34 LVI score should be 2 (lowest) |
| target_path | task_metrics.P03.lvi_score.LFA34 |
| target_value | 2.0 |
| tolerance_abs | 0.25 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.7 |

### R17 - LFA 38 LVI Score
| Field | Value |
|-------|-------|
| rule_id | R17 |
| claim_ids | C03 |
| type | numeric |
| description | LFA 38 LVI score should be 2 (lowest) |
| target_path | task_metrics.P03.lvi_score.LFA38 |
| target_value | 2.0 |
| tolerance_abs | 0.25 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.7 |

### R18 - LFA 35 LVI Score
| Field | Value |
|-------|-------|
| rule_id | R18 |
| claim_ids | C03 |
| type | numeric |
| description | LFA 35 LVI score should be 2.5 (highest) |
| target_path | task_metrics.P03.lvi_score.LFA35 |
| target_value | 2.5 |
| tolerance_abs | 0.25 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.7 |

### R19 - LFA 36 LVI Score
| Field | Value |
|-------|-------|
| rule_id | R19 |
| claim_ids | C03 |
| type | numeric |
| description | LFA 36 LVI score should be 2.5 (highest) |
| target_path | task_metrics.P03.lvi_score.LFA36 |
| target_value | 2.5 |
| tolerance_abs | 0.25 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.7 |

### R20 - LFA 41 LVI Score (BNAM)
| Field | Value |
|-------|-------|
| rule_id | R20 |
| claim_ids | C03 |
| type | numeric |
| description | LFA 41 LVI score under BNAM scenario should be 2.5 |
| target_path | task_metrics.P03.lvi_score.LFA41.BNAM |
| target_value | 2.5 |
| tolerance_abs | 0.25 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.7 |

### R21 - LFA 41 LVI Score (CM2.6)
| Field | Value |
|-------|-------|
| rule_id | R21 |
| claim_ids | C03 |
| type | numeric |
| description | LFA 41 LVI score under CM2.6 scenario should be 2 |
| target_path | task_metrics.P03.lvi_score.LFA41.CM26 |
| target_value | 2.0 |
| tolerance_abs | 0.25 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.7 |

### R22 - ESI West-to-East Increase
| Field | Value |
|-------|-------|
| rule_id | R22 |
| claim_ids | C04 |
| type | trend |
| description | ESI should increase from western LFAs (Bay of Fundy area, e.g., LFA 38) to eastern LFAs (e.g., LFA 27) |
| comparison | task_metrics.P04.esi_median.LFA38 < task_metrics.P04.esi_median.LFA36 < task_metrics.P04.esi_median.LFA27 |
| confidence_weight | 1.0 |

### R23 - ISI Similar Across LFAs
| Field | Value |
|-------|-------|
| rule_id | R23 |
| claim_ids | C04 |
| type | numeric |
| description | ISI median should be approximately 3 (moderate) across all LFAs, with similar values |
| target_path | task_metrics.P04.isi_median.overall |
| target_value | 3.0 |
| tolerance_abs | 0.5 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.5 |

### R24 - SESI Least Dependent LFA
| Field | Value |
|-------|-------|
| rule_id | R24 |
| claim_ids | C04 |
| type | trend |
| description | LFA 32 should have the lowest SESI (least dependent on fisheries) |
| comparison | task_metrics.P04.sesi_median.LFA32 < task_metrics.P04.sesi_median.LFA34 and task_metrics.P04.sesi_median.LFA32 < task_metrics.P04.sesi_median.LFA31B and task_metrics.P04.sesi_median.LFA32 < task_metrics.P04.sesi_median.LFA38 |
| confidence_weight | 0.7 |

### R25 - SESI Most Dependent LFAs
| Field | Value |
|-------|-------|
| rule_id | R25 |
| claim_ids | C04 |
| type | trend |
| description | LFAs 31B, 34, and 38 should have the highest SESI (most dependent on fisheries) |
| comparison | task_metrics.P04.sesi_median.LFA31B > 3 and task_metrics.P04.sesi_median.LFA34 > 3 and task_metrics.P04.sesi_median.LFA38 > 3 |
| confidence_weight | 0.7 |

### R26 - SESI Variation
| Field | Value |
|-------|-------|
| rule_id | R26 |
| claim_ids | C04 |
| type | numeric |
| description | SESI should vary widely across region, with medians ranging from approximately 2 to 4.5 |
| target_path | task_metrics.P04.sesi_median.range |
| target_value | 2.5 |
| tolerance_abs | 1.0 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.5 |

### R27 - Score Scale
| Field | Value |
|-------|-------|
| rule_id | R27 |
| claim_ids | C04 |
| type | numeric |
| description | All sub-index scores should be on a 1-5 scale (1 = least vulnerable, 5 = most vulnerable) |
| target_path | task_metrics.P04.score_scale.min |
| target_value | 1.0 |
| tolerance_abs | 0.01 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.3 |

### R28 - Sub-index Aggregation Method
| Field | Value |
|-------|-------|
| rule_id | R28 |
| claim_ids | C04 |
| type | exists |
| description | Sub-index aggregation should use geometric mean |
| target_path | task_metrics.P04.aggregation_method |
| target_value | geometric_mean |
| scope | json |
| confidence_weight | 0.5 |

### R29 - Integrated Assessment Distributions (Figure 7)
| Field | Value |
|-------|-------|
| rule_id | R29 |
| claim_ids | C05 |
| type | compare |
| description | Compare generated vulnerability sub-index distribution plots against reference. Should show three-panel density/histogram figure for ESI, ISI, SESI comparing LFA 27 (blue), LFA 34 (yellow), and All LFAs (gray). LFA 34 SESI should be right-skewed (concentrated at 4-5); LFA 27 SESI more evenly distributed |
| reference_path | figures/fig07.png |
| confidence_weight | 0.5 |

### R30 - SESI Variables and SVD (Figure 8)
| Field | Value |
|-------|-------|
| rule_id | R30 |
| claim_ids | C05 |
| type | compare |
| description | Compare generated SESI variable distributions and Species Value Diversity against reference. Should show four-panel stacked bar chart: % Income from Fishing (LFA 34 concentrated at 5, LFA 27 split between 1 and 4), Population, Quantity Landed per Vessel, and Species Value Diversity (both LFA 27 and 34 concentrated at 4-5) |
| reference_path | figures/fig08.png |
| confidence_weight | 0.5 |

### R31 - LFA 34 SESI Distribution
| Field | Value |
|-------|-------|
| rule_id | R31 |
| claim_ids | C05 |
| type | trend |
| description | LFA 34 SESI distribution should be highly right-skewed, with most SCH scores at 4-5 (high dependence on fishing) |
| comparison | task_metrics.P05.sesi_lfa34_mode > task_metrics.P05.sesi_lfa27_mode |
| confidence_weight | 0.7 |

### R32 - LFA 27 SESI Distribution
| Field | Value |
|-------|-------|
| rule_id | R32 |
| claim_ids | C05 |
| type | trend |
| description | LFA 27 SESI distribution should be relatively flat with equivalent numbers of low, medium, and high vulnerability |
| comparison | task_metrics.P05.sesi_lfa27_std > task_metrics.P05.sesi_lfa34_std |
| confidence_weight | 0.5 |

### R33 - LFA 34 LVI Very Low
| Field | Value |
|-------|-------|
| rule_id | R33 |
| claim_ids | C05 |
| type | numeric |
| description | LFA 34 LVI should be very low (2) |
| target_path | task_metrics.P05.lvi_lfa34 |
| target_value | 2.0 |
| tolerance_abs | 0.25 |
| tolerance_pct | 0.0 |
| confidence_weight | 0.7 |

### R34 - SVD High Scores for LFAs 27 and 34
| Field | Value |
|-------|-------|
| rule_id | R34 |
| claim_ids | C05 |
| type | trend |
| description | Species Value Diversity for both LFAs 27 and 34 should show high scores (4-5), indicating high dependence on a few species |
| comparison | task_metrics.P05.svd_lfa27_mode is not None and task_metrics.P05.svd_lfa27_mode > 3 and task_metrics.P05.svd_lfa34_mode is not None and task_metrics.P05.svd_lfa34_mode > 3 |
| confidence_weight | 0.5 |

### R35 - BNAM and CM2.6 Spatial Pattern Similarity
| Field | Value |
|-------|-------|
| rule_id | R35 |
| claim_ids | C06 |
| type | trend |
| description | BNAM and CM2.6 bottom temperature projections should show similar spatial patterns (high correlation in spatial fields) |
| comparison | task_metrics.P06.spatial_correlation_BNAM_CM26 > 0.5 |
| confidence_weight | 1.0 |

### R36 - CM2.6 Larger Magnitude Than BNAM
| Field | Value |
|-------|-------|
| rule_id | R36 |
| claim_ids | C06 |
| type | trend |
| description | CM2.6 should predict larger temperature changes than BNAM (greater magnitude of bottom temperature change) |
| comparison | task_metrics.P06.mean_temp_change.CM26 > task_metrics.P06.mean_temp_change.BNAM |
| confidence_weight | 1.0 |
