==============================================================================
El Gordo sensitivity analysis — does observation uncertainty close
                                  the factor-3.5 outlier?
==============================================================================

Parameter combinations swept: 80
  v_initial range:   2000 - 3500 km/s
  t_since range:     70 - 300 Myr
  dec_ratio range:   0.5 - 0.85

GRUT predicted offset:
  Min (most aggressive params):  42.9 kpc
  Canonical (v=2500/t=110/d=0.638): 70.4 kpc
  Max (most favorable params):   130.5 kpc

Observed offset published range:  120 - 600 kpc
Prediction range overlaps obs range: True

Closure scenarios:
Scenario                                                       canon    best
------------------------------------------------------------------------------
  Canonical (v=2500, t=110, dec=0.638), obs=250 kpc            0.281   0.522
  Lower observed bound (120 kpc, individual subclump centroids)   0.586   1.088
  Mid-low observed (150 kpc)                                   0.469   0.870
  Jee 2014 NW clump (600 kpc)                                  0.117   0.218

Verify:
  [PASS] sweep_covers_at_least_60_combinations
  [PASS] canonical_prediction_around_70_kpc
  [PASS] max_prediction_above_120_kpc
  [PASS] prediction_range_overlaps_obs_range
  [PASS] consistent_at_lower_obs_bound
  [PASS] best_case_within_factor_1p5_of_obs_lower_bound
