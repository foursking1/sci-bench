# Truth: Processing seismic ambient noise data to obtain reliable broad-band surface wave dispersion measurements

## Metadata

| Field | Value |
|-------|-------|
| paper_id | bensen_2007 |
| title | Processing seismic ambient noise data to obtain reliable broad-band surface wave dispersion measurements |
| venue | Geophysical Journal International (2007), 169, 1239-1260 |
| reproduction_type | full |

---

## Claims

| ID | Text | Evidence Type |
|----|------|---------------|
| C01 | Broad-band symmetric-component cross-correlation from 12-months of data between ANMO and HRV shows clear Rayleigh wave signals across six passbands (7-150s, 7-25s, 20-50s, 33-67s, 50-100s, 70-150s) | figure |
| C02 | Comparison of five time-domain normalization methods shows that one-bit, running-absolute-mean, and water-level methods produce high SNR waveforms, while raw, clipped, and event detection methods produce noisy results | figure |
| C03 | Tuning temporal normalization weights to the earthquake band (15-50s) reduces spurious precursory arrivals in cross-correlations between NZ stations CRLZ and HIZ | figure |
| C04 | Spectral whitening flattens the amplitude spectrum at station HRV, removing microseism peaks and the 26s Gulf of Guinea signal | figure |
| C05 | Spectral whitening removes the 26s monochromatic noise peak from ANMO-CCM cross-correlations, producing results similar to a 26s notch filter | figure |
| C06 | Cross-correlations with spectral whitening between CCM and SSPA produce broader-band signals than those without whitening | figure |
| C07 | Rayleigh wave signal emerges with increasing stacking length (1 < 3 < 12 < 24 months) for ANMO-DWPF, and spectral SNR increases with stacking length | trend |
| C08 | Power law fit SNR = A*t^(1/n) with exponent n varying from ~2.55 at 10s to ~3.4 at 50s and ~2.66 at 100s | numeric |
| C09 | Automated FTAN on 12-month ANMO-COR produces group speed curve consistent with Shapiro & Ritzwoller (2002) 3-D model | figure |
| C10 | Cross-correlations between PFO and five stations show waveform agreement with Oct 31 2001 earthquake records | figure |
| C11 | Spatial cluster of 10 SoCal stations shows group and phase speed curves that agree with each other and with 3-D model | figure |
| C12 | 10 of 12 three-month stacks of CCM-DWPF yield consistent group velocity measurements | numeric |
| C13 | Linear inverse relationship between standard deviation of group speed and spectral SNR for >200 stations | trend |
| C14 | Ambient noise misfit (std=12.6s) is tighter than earthquake misfit (std=22.7s) at 16s across Europe | numeric |

---

## Verification Rules

### R01 — Six-passband cross-correlation figure
| Field | Value |
|-------|-------|
| rule_id | R01 |
| claim_ids | C01 |
| type | compare |
| description | Compare generated ANMO-HRV six-passband cross-correlation figure against reference |
| reference_path | figures/fig01.png |
| confidence_weight | 0.4 |

### R02 — Normalization method comparison figure
| Field | Value |
|-------|-------|
| rule_id | R02 |
| claim_ids | C02 |
| type | compare |
| description | Compare generated normalization method comparison figure against reference |
| reference_path | figures/fig02.png |
| confidence_weight | 0.4 |

### R03 — Normalization SNR ordering trend
| Field | Value |
|-------|-------|
| rule_id | R03 |
| claim_ids | C02 |
| type | trend |
| description | Verify SNR ordering: running-absolute-mean, one-bit, and water-level methods produce higher SNR than raw, clipped, and event-detection methods |
| comparison | task_metrics.P04.normalization_snr.running_absolute_mean > task_metrics.P04.normalization_snr.raw AND task_metrics.P04.normalization_snr.one_bit > task_metrics.P04.normalization_snr.raw AND task_metrics.P04.normalization_snr.water_level > task_metrics.P04.normalization_snr.raw AND task_metrics.P04.normalization_snr.running_absolute_mean > task_metrics.P04.normalization_snr.clipped AND task_metrics.P04.normalization_snr.running_absolute_mean > task_metrics.P04.normalization_snr.event_detection |
| confidence_weight | 0.7 |

### R04 — Earthquake-band tuning comparison figure
| Field | Value |
|-------|-------|
| rule_id | R04 |
| claim_ids | C03 |
| type | compare |
| description | Compare generated earthquake-band tuning comparison figure against reference |
| reference_path | figures/fig03.png |
| confidence_weight | 0.4 |

### R05 — Spectral whitening spectrum figure
| Field | Value |
|-------|-------|
| rule_id | R05 |
| claim_ids | C04 |
| type | compare |
| description | Compare generated spectral whitening spectrum figure against reference |
| reference_path | figures/fig04.png |
| confidence_weight | 0.4 |

### R06 — 26s noise removal comparison figure
| Field | Value |
|-------|-------|
| rule_id | R06 |
| claim_ids | C05 |
| type | compare |
| description | Compare generated 26s noise removal comparison figure against reference |
| reference_path | figures/fig05.png |
| confidence_weight | 0.4 |

### R07 — Broader-band cross-correlation figure
| Field | Value |
|-------|-------|
| rule_id | R07 |
| claim_ids | C06 |
| type | compare |
| description | Compare generated broader-band cross-correlation figure against reference |
| reference_path | figures/fig06.png |
| confidence_weight | 0.3 |

### R08 — SNR emergence with stacking length figure
| Field | Value |
|-------|-------|
| rule_id | R08 |
| claim_ids | C07 |
| type | compare |
| description | Compare generated SNR emergence with stacking length figure against reference |
| reference_path | figures/fig07.png |
| confidence_weight | 0.4 |

### R09 — SNR increases with stacking length trend
| Field | Value |
|-------|-------|
| rule_id | R09 |
| claim_ids | C07 |
| type | trend |
| description | Verify spectral SNR increases monotonically with stacking length: 1 month < 3 months < 12 months < 24 months |
| comparison | task_metrics.P08.snr_1month < task_metrics.P08.snr_3month AND task_metrics.P08.snr_3month < task_metrics.P08.snr_12month AND task_metrics.P08.snr_12month < task_metrics.P08.snr_24month |
| confidence_weight | 0.7 |

### R10 — Power law exponent at 10s
| Field | Value |
|-------|-------|
| rule_id | R10 |
| claim_ids | C08 |
| type | numeric |
| description | Power law exponent n at 10s period should be approximately 2.55 |
| target_path | task_metrics.P09.power_law.n_10s |
| target_value | 2.55 |
| tolerance_abs | 0.25 |
| tolerance_pct | 10.0 |
| confidence_weight | 1.0 |

### R11 — Power law exponent at 25s
| Field | Value |
|-------|-------|
| rule_id | R11 |
| claim_ids | C08 |
| type | numeric |
| description | Power law exponent n at 25s period should be approximately 2.88 |
| target_path | task_metrics.P09.power_law.n_25s |
| target_value | 2.88 |
| tolerance_abs | 0.29 |
| tolerance_pct | 10.0 |
| confidence_weight | 1.0 |

### R12 — Power law exponent at 50s
| Field | Value |
|-------|-------|
| rule_id | R12 |
| claim_ids | C08 |
| type | numeric |
| description | Power law exponent n at 50s period should be approximately 3.4 (maximum value) |
| target_path | task_metrics.P09.power_law.n_50s |
| target_value | 3.4 |
| tolerance_abs | 0.34 |
| tolerance_pct | 10.0 |
| confidence_weight | 1.0 |

### R13 — Power law exponent at 100s
| Field | Value |
|-------|-------|
| rule_id | R13 |
| claim_ids | C08 |
| type | numeric |
| description | Power law exponent n at 100s period should be approximately 2.66 |
| target_path | task_metrics.P09.power_law.n_100s |
| target_value | 2.66 |
| tolerance_abs | 0.27 |
| tolerance_pct | 10.0 |
| confidence_weight | 1.0 |

### R14 — Power law exponent ordering trend
| Field | Value |
|-------|-------|
| rule_id | R14 |
| claim_ids | C08 |
| type | trend |
| description | Verify power law exponent n ordering: n(10s) < n(25s) < n(50s) and n(50s) > n(100s), with maximum at 50s |
| comparison | task_metrics.P09.power_law.n_10s < task_metrics.P09.power_law.n_25s AND task_metrics.P09.power_law.n_25s < task_metrics.P09.power_law.n_50s AND task_metrics.P09.power_law.n_50s > task_metrics.P09.power_law.n_100s |
| confidence_weight | 0.7 |

### R15 — FTAN dispersion measurement figure
| Field | Value |
|-------|-------|
| rule_id | R15 |
| claim_ids | C09 |
| type | compare |
| description | Compare generated FTAN dispersion measurement figure against reference |
| reference_path | figures/fig08.png |
| confidence_weight | 0.4 |

### R16 — Earthquake waveform comparison figure
| Field | Value |
|-------|-------|
| rule_id | R16 |
| claim_ids | C10 |
| type | compare |
| description | Compare generated earthquake waveform comparison figure against reference |
| reference_path | figures/fig09.png |
| confidence_weight | 0.4 |

### R17 — Spatial cluster analysis figure
| Field | Value |
|-------|-------|
| rule_id | R17 |
| claim_ids | C11 |
| type | compare |
| description | Compare generated spatial cluster analysis figure against reference |
| reference_path | figures/fig10.png |
| confidence_weight | 0.4 |

### R18 — Temporal variability figure
| Field | Value |
|-------|-------|
| rule_id | R18 |
| claim_ids | C12 |
| type | compare |
| description | Compare generated temporal variability figure against reference |
| reference_path | figures/fig11.png |
| confidence_weight | 0.4 |

### R19 — Temporal variability numeric check
| Field | Value |
|-------|-------|
| rule_id | R19 |
| claim_ids | C12 |
| type | numeric |
| description | At least 10 of 12 three-month stacks should yield acceptable group velocity measurements (SNR > 10 threshold) |
| target_path | task_metrics.P12.temporal_variability.qualifying_stacks |
| target_value | 10 |
| tolerance_abs | 1 |
| tolerance_pct | 0 |
| confidence_weight | 0.7 |

### R20 — SNR proxy curve trend
| Field | Value |
|-------|-------|
| rule_id | R20 |
| claim_ids | C13 |
| type | compare |
| description | Compare generated SNR proxy curve scatter plot against reference |
| reference_path | figures/fig12.png |
| confidence_weight | 0.3 |

### R21 — SNR proxy inverse trend
| Field | Value |
|-------|-------|
| rule_id | R21 |
| claim_ids | C13 |
| type | trend |
| description | Verify that binned standard deviation decreases as spectral SNR increases (inverse relationship) |
| comparison | task_metrics.P12.proxy_curve.std_low_snr > task_metrics.P12.proxy_curve.std_mid_snr AND task_metrics.P12.proxy_curve.std_mid_snr > task_metrics.P12.proxy_curve.std_high_snr |
| confidence_weight | 0.7 |

### R22 — Ambient noise misfit numeric
| Field | Value |
|-------|-------|
| rule_id | R22 |
| claim_ids | C14 |
| type | numeric |
| description | Ambient noise misfit standard deviation at 16s period across Europe should be approximately 12.6s |
| target_path | task_metrics.P16.misfit.ambient_noise_std |
| target_value | 12.6 |
| tolerance_abs | 1.3 |
| tolerance_pct | 10.0 |
| confidence_weight | 1.0 |

### R23 — Earthquake misfit numeric
| Field | Value |
|-------|-------|
| rule_id | R23 |
| claim_ids | C14 |
| type | numeric |
| description | Earthquake misfit standard deviation at 16s period across Europe should be approximately 22.7s |
| target_path | task_metrics.P16.misfit.earthquake_std |
| target_value | 22.7 |
| tolerance_abs | 2.3 |
| tolerance_pct | 10.0 |
| confidence_weight | 1.0 |

### R24 — Misfit comparison trend
| Field | Value |
|-------|-------|
| rule_id | R24 |
| claim_ids | C14 |
| type | trend |
| description | Ambient noise misfit std dev should be approximately half the earthquake misfit std dev (ratio ~0.55) |
| comparison | task_metrics.P16.misfit.ambient_noise_std < task_metrics.P16.misfit.earthquake_std |
| confidence_weight | 0.7 |

### R25 — Misfit histogram figure
| Field | Value |
|-------|-------|
| rule_id | R25 |
| claim_ids | C14 |
| type | compare |
| description | Compare generated misfit histogram figure against reference |
| reference_path | figures/fig13.png |
| confidence_weight | 0.4 |
