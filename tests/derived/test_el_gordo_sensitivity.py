"""Tests for grut.derived.cluster.el_gordo_sensitivity — does El Gordo's
factor-3.5 outlier survive parameter and observational uncertainty?

The original cluster_merger_scaling_law tagged El Gordo as an outlier
based on (canonical params, 250 kpc observed offset). This module
sweeps the published parameter ranges and shows the prediction range
overlaps with the lower part of the observation range — the factor
3.5 was specific to one parameter point, not a robust deviation.
"""

import math

import pytest

from grut.derived.cluster.el_gordo_sensitivity import (
    CANONICAL_OBSERVED_KPC,
    DEC_RATIO_RANGE,
    OBSERVED_OFFSET_RANGE_KPC,
    T_SINCE_RANGE_MYR,
    V_INITIAL_RANGE_KM_S,
    ClosureScenario,
    ElGordoPrediction,
    SensitivityReport,
    best_case_match,
    closure_scenarios,
    parameter_sweep,
    predict_at_params,
    sensitivity_report,
    verify,
)


class TestParameterRanges:
    def test_v_initial_range_published(self):
        """v_initial 2000-3500 km/s spans Menanteau 2012 - Jee 2014."""
        assert min(V_INITIAL_RANGE_KM_S) <= 2000
        assert max(V_INITIAL_RANGE_KM_S) >= 3500

    def test_t_since_range_published(self):
        """t_since 70-300 Myr spans the dynamical-model uncertainty."""
        assert min(T_SINCE_RANGE_MYR) <= 100
        assert max(T_SINCE_RANGE_MYR) >= 250

    def test_dec_ratio_range_published(self):
        """dec_ratio 0.5-0.85 reflects mass-ratio uncertainty."""
        assert min(DEC_RATIO_RANGE) <= 0.55
        assert max(DEC_RATIO_RANGE) >= 0.80

    def test_observed_range_spans_published_methodologies(self):
        """120-600 kpc covers individual centroids to Jee NW clump."""
        assert min(OBSERVED_OFFSET_RANGE_KPC) <= 150
        assert max(OBSERVED_OFFSET_RANGE_KPC) >= 500


class TestParameterSweep:
    def test_sweep_size_at_least_60(self):
        sweep = parameter_sweep()
        assert len(sweep) >= 60  # 4×5×4 = 80 combinations

    def test_each_prediction_positive(self):
        for p in parameter_sweep():
            assert p.predicted_kpc > 0

    def test_canonical_marked(self):
        sweep = parameter_sweep()
        canonical = [p for p in sweep if p.is_canonical]
        assert len(canonical) == 1
        c = canonical[0]
        assert abs(c.v_initial - 2500) < 1e-6
        assert abs(c.t_since - 110) < 1e-6

    def test_canonical_prediction_around_70_kpc(self):
        sweep = parameter_sweep()
        canonical = next(p for p in sweep if p.is_canonical)
        assert 65 < canonical.predicted_kpc < 80

    def test_predict_at_params_function(self):
        """The standalone function should agree with sweep entries."""
        p = predict_at_params(2500, 110, 0.638)
        assert p.is_canonical
        assert 65 < p.predicted_kpc < 80


class TestSensitivityReport:
    def test_min_prediction_above_30_kpc(self):
        rep = sensitivity_report()
        assert rep.min_prediction_kpc > 30

    def test_max_prediction_above_120_kpc(self):
        """At the most favorable parameters, prediction should be at
        least at the lower end of the observed range."""
        rep = sensitivity_report()
        assert rep.max_prediction_kpc > 120

    def test_max_prediction_around_130_kpc(self):
        rep = sensitivity_report()
        assert 120 < rep.max_prediction_kpc < 145

    def test_prediction_range_overlaps_observation_range(self):
        """The KEY result: prediction range ∩ observation range ≠ ∅."""
        rep = sensitivity_report()
        assert rep.overlaps_with_obs_range

    def test_consistent_at_lower_observed_bound(self):
        """At lower obs bound (120 kpc), max prediction within factor 1.5."""
        rep = sensitivity_report()
        assert rep.consistent_at_obs_lower_bound


class TestClosureScenarios:
    def test_four_scenarios_present(self):
        scenarios = closure_scenarios()
        assert len(scenarios) == 4

    def test_canonical_scenario_shows_outlier_with_250(self):
        """The canonical (v=2500/t=110/d=0.638, obs=250) scenario is
        what gave the factor-3.5 outlier flag."""
        scenarios = closure_scenarios()
        canonical = scenarios[0]
        assert canonical.canonical_ratio < 0.4
        assert "outlier" in canonical.interpretation.lower() or \
               "below" in canonical.interpretation.lower()

    def test_lower_bound_scenario_consistent(self):
        """At 120 kpc observed, best-case ratio ~1.09 — fully consistent."""
        scenarios = closure_scenarios()
        lower = scenarios[1]
        assert lower.observed_offset_assumed_kpc == 120
        assert 0.95 < lower.best_case_ratio < 1.20

    def test_mid_low_scenario_matches_other_clusters(self):
        """At 150 kpc observed, best-case ratio ~0.87 — same as the
        other three normal-regime mergers."""
        scenarios = closure_scenarios()
        mid = scenarios[2]
        assert mid.observed_offset_assumed_kpc == 150
        assert 0.80 < mid.best_case_ratio < 0.95

    def test_upper_bound_scenario_remains_problematic(self):
        """At 600 kpc observed (Jee NW clump), even best-case fails."""
        scenarios = closure_scenarios()
        upper = scenarios[3]
        assert upper.observed_offset_assumed_kpc == 600
        assert upper.best_case_ratio < 0.30


class TestBestCaseMatch:
    def test_best_case_returns_max_prediction(self):
        best, _ = best_case_match()
        sweep = parameter_sweep()
        assert best.predicted_kpc == max(p.predicted_kpc for p in sweep)

    def test_best_case_uses_favorable_parameters(self):
        """High v_initial + short t_since + high dec_ratio."""
        best, _ = best_case_match()
        # Should prefer extremes
        assert best.v_initial >= 3000
        assert best.dec_ratio >= 0.75


class TestVerifyHarness:
    def test_all_pass(self):
        checks = verify()
        failed = [k for k, v in checks.items() if not v]
        assert not failed, f"El Gordo sensitivity failures: {failed}"

    def test_returns_six_legs(self):
        assert len(verify()) == 6


class TestHonestFraming:
    """The module's framing should weaken (not strengthen) the
    'El Gordo is a problem' claim — the data permits multiple readings."""

    def test_module_doc_acknowledges_uncertainty(self):
        from grut.derived.cluster import el_gordo_sensitivity
        doc = el_gordo_sensitivity.__doc__ or ""
        assert "uncertainty" in doc.lower() or "uncertain" in doc.lower()

    def test_module_doc_notes_methodology_dependence(self):
        from grut.derived.cluster import el_gordo_sensitivity
        doc = el_gordo_sensitivity.__doc__ or ""
        assert "methodology" in doc.lower() or "reconstruction" in doc.lower()

    def test_module_doc_states_factor_3p5_was_specific_point(self):
        from grut.derived.cluster import el_gordo_sensitivity
        doc = el_gordo_sensitivity.__doc__ or ""
        assert "specific" in doc.lower() or "depend" in doc.lower()


class TestConsistencyAtLowObs:
    """Direct test: at the lower obs range, framework is consistent."""

    def test_at_120_kpc_best_ratio_around_1(self):
        """If observation is 120 kpc, best-case ratio ≈ 1.09."""
        scenarios = closure_scenarios()
        for s in scenarios:
            if s.observed_offset_assumed_kpc == 120:
                assert 1.0 < s.best_case_ratio < 1.2
                return
        pytest.fail("120 kpc scenario not in closure_scenarios")

    def test_at_150_kpc_best_ratio_matches_other_clusters(self):
        """If observation is 150 kpc, best-case ratio ≈ 0.87 — exactly
        the same ratio as Bullet, MACS, and within ~10% of Abell."""
        scenarios = closure_scenarios()
        for s in scenarios:
            if s.observed_offset_assumed_kpc == 150:
                # Bullet/MACS/Abell ratios are 0.79-0.88
                assert 0.75 < s.best_case_ratio < 0.95
                return
        pytest.fail("150 kpc scenario not in closure_scenarios")
