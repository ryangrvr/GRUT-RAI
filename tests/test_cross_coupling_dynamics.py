"""Tests — Phase D7: Cross-Coupling Dynamics and Back-Reaction Test.

60 tests across 11 classes.
"""

import math
import json
import pytest

from grut.cross_coupling_dynamics import (
    # Constants
    ALPHA_BR_SCAN, BETA_XR_SCAN, LAMBDA_SCAN_VALUES,
    N_INTERACTION_CHANNELS, UNIT_BENCHMARK,
    MASS_COEFF, RHO_EQ_COEFF, R_EQ, R_EXT, M_EXT, ETA_SQUARED,
    # Assumptions / nonclaims
    CROSS_COUPLING_ASSUMPTIONS, CROSS_COUPLING_NONCLAIMS,
    # Dataclasses
    CrossCouplingParams,
    # Functions
    define_coupled_model,
    compute_coupled_sectors,
    assess_back_reaction,
    inject_coupled_metric,
    scan_coupling_strength,
    scan_lambda_coupled,
    classify_cross_coupling,
    compute_cross_coupling,
    cross_coupling_result_to_dict,
)


@pytest.fixture(scope="module")
def params():
    return CrossCouplingParams()


@pytest.fixture(scope="module")
def result():
    return compute_cross_coupling()


# ================================================================
# Section 1: Constants (5 tests)
# ================================================================

class TestConstants:
    def test_n_channels(self):
        assert N_INTERACTION_CHANNELS == 2

    def test_alpha_br_scan_length(self):
        assert len(ALPHA_BR_SCAN) == 5

    def test_beta_xr_scan_length(self):
        assert len(BETA_XR_SCAN) == 5

    def test_unit_benchmark(self):
        assert UNIT_BENCHMARK == (1.0, 1.0)

    def test_mass_coeff(self):
        assert abs(MASS_COEFF - math.pi / 3.0) < 1e-10


# ================================================================
# Section 2: Model Definition (5 tests)
# ================================================================

class TestModelDefinition:
    def test_exists(self, result):
        assert result.model_definition is not None

    def test_two_channels(self, result):
        assert result.model_definition.n_channels == 2

    def test_d6_recovery(self, result):
        assert "0" in result.model_definition.d6_recovery_condition

    def test_unit_benchmark_documented(self, result):
        assert result.model_definition.unit_benchmark == (1.0, 1.0)

    def test_channel_names(self, result):
        names = [ch.name for ch in result.model_definition.channels]
        assert "gravitational_back_reaction" in names
        assert "source_amplification" in names


# ================================================================
# Section 3: Coupled Sectors (7 tests)
# ================================================================

class TestCoupledSectors:
    def test_exists(self, result):
        assert result.coupled_sectors is not None

    def test_defect_sigma_positive(self, result):
        assert result.coupled_sectors.sigma_defect_at_Req > 0

    def test_A_eff_gt_A0(self, result):
        assert result.coupled_sectors.A_eff_at_Req > result.params.scalar_A

    def test_sigma_macro_coupled_gt_uncoupled(self, result):
        cs = result.coupled_sectors
        assert cs.sigma_macro_coupled_at_Req > cs.sigma_macro_d6_at_Req

    def test_sigma_total_positive(self, result):
        assert float(result.coupled_sectors.sigma_total[0]) > 0

    def test_d6_recovery(self, result):
        # At alpha=0, beta=0 from coupling scan
        for e in result.coupling_scan.entries:
            if abs(e.alpha_BR) < 1e-10 and abs(e.beta_XR) < 1e-10:
                assert e.metric_positive
                return
        pytest.fail("No (0,0) entry found")

    def test_grid_400_points(self, result):
        assert len(result.coupled_sectors.r_grid) == 400


# ================================================================
# Section 4: Back-Reaction (6 tests)
# ================================================================

class TestBackReaction:
    def test_exists(self, result):
        assert result.back_reaction is not None

    def test_delta_increase_positive(self, result):
        assert result.back_reaction.delta_increase_at_Req > 0

    def test_amplification_factor_gt_one(self, result):
        assert result.back_reaction.amplification_factor > 1.0

    def test_net_classification_string(self, result):
        assert result.back_reaction.net_classification in [
            "constructive", "destructive", "neutral"
        ]

    def test_sigma_macro_increase_positive(self, result):
        assert result.back_reaction.sigma_macro_increase_at_Req > 0

    def test_net_shift_finite(self, result):
        assert math.isfinite(result.back_reaction.net_metric_shift_at_Req)


# ================================================================
# Section 5: Metric Injection (6 tests)
# ================================================================

class TestMetricInjection:
    def test_exists(self, result):
        assert result.metric_injection is not None

    def test_f_min_finite(self, result):
        assert math.isfinite(result.metric_injection.f_min)

    def test_f_at_Req_finite(self, result):
        assert math.isfinite(result.metric_injection.f_at_Req)

    def test_budget_at_Req(self, result):
        assert f"r={R_EQ:.4f}" in result.metric_injection.budget

    def test_metric_shift_reported(self, result):
        assert math.isfinite(result.metric_injection.metric_shift)

    def test_d6_reference_positive(self, result):
        assert result.metric_injection.f_d6_at_Req > 0


# ================================================================
# Section 6: Coupling Strength Scan (7 tests)
# ================================================================

class TestCouplingStrengthScan:
    def test_exists(self, result):
        assert result.coupling_scan is not None

    def test_25_entries(self, result):
        assert result.coupling_scan.n_scanned == 25

    def test_d6_limit_positive(self, result):
        for e in result.coupling_scan.entries:
            if abs(e.alpha_BR) < 1e-10 and abs(e.beta_XR) < 1e-10:
                assert e.metric_positive
                return
        pytest.fail("No (0,0) entry")

    def test_unit_benchmark_reported(self, result):
        assert result.coupling_scan.unit_benchmark_entry is not None

    def test_unit_benchmark_fmin_finite(self, result):
        assert math.isfinite(result.coupling_scan.unit_benchmark_f_min)

    def test_n_positive_ge_one(self, result):
        assert result.coupling_scan.n_positive >= 1

    def test_pure_amplification_exists(self, result):
        assert result.coupling_scan.pure_amplification is not None


# ================================================================
# Section 7: Lambda Scan (6 tests)
# ================================================================

class TestLambdaScan:
    def test_exists(self, result):
        assert result.lambda_scan is not None

    def test_six_scanned(self, result):
        assert result.lambda_scan.n_scanned == 6

    def test_all_converged(self, result):
        assert result.lambda_scan.n_converged == 6

    def test_d6_positivity_preserved(self, result):
        assert result.lambda_scan.n_positive_d6 >= 4

    def test_coupled_positive_exists(self, result):
        assert result.lambda_scan.n_positive_coupled > 0

    def test_best_lambda_in_scan(self, result):
        assert result.lambda_scan.best_lambda_coupled in LAMBDA_SCAN_VALUES


# ================================================================
# Section 8: Classification (6 tests)
# ================================================================

class TestClassification:
    def test_exists(self, result):
        assert result.classification is not None

    def test_classification_string(self, result):
        assert result.classification.classification in [
            "fully_coupled_viable",
            "viability_window_shifted_but_survives",
            "partially_viable_under_coupling",
            "destroyed_by_back_reaction",
            "unresolved_coupled_artifacts",
        ]

    def test_phase_lock_has_d7(self, result):
        assert "cross_coupling_D7" in result.classification.phase_lock_update

    def test_d6_pessimistic_bool(self, result):
        assert isinstance(result.classification.d6_additive_pessimistic, bool)

    def test_viable_windows_lists(self, result):
        assert isinstance(result.classification.viable_lambda_window_coupled, list)

    def test_threshold_shift_string(self, result):
        assert result.classification.threshold_shift in [
            "unchanged", "lower", "higher", "shifted", "destroyed"
        ]


# ================================================================
# Section 9: D6 Recovery (4 tests)
# ================================================================

class TestD6Recovery:
    def test_zero_coupling_matches_d6(self, result):
        for e in result.coupling_scan.entries:
            if abs(e.alpha_BR) < 1e-10 and abs(e.beta_XR) < 1e-10:
                assert abs(e.f_min - 0.498) < 0.05
                return
        pytest.fail("No (0,0) entry")

    def test_alpha_only_destructive(self, result):
        sc = result.coupling_scan
        if sc.pure_backreaction:
            d6 = None
            for e in sc.entries:
                if abs(e.alpha_BR) < 1e-10 and abs(e.beta_XR) < 1e-10:
                    d6 = e
                    break
            assert sc.pure_backreaction.f_min <= d6.f_min + 0.01

    def test_beta_only_constructive(self, result):
        sc = result.coupling_scan
        if sc.pure_amplification:
            d6 = None
            for e in sc.entries:
                if abs(e.alpha_BR) < 1e-10 and abs(e.beta_XR) < 1e-10:
                    d6 = e
                    break
            assert sc.pure_amplification.f_min >= d6.f_min - 0.01

    def test_unit_benchmark_vs_d6(self, result):
        assert math.isfinite(result.coupling_scan.unit_benchmark_f_min)


# ================================================================
# Section 10: Nonclaims & Serialization (3 tests)
# ================================================================

class TestNonclaimsSerialization:
    def test_ten_nonclaims(self, result):
        assert len(result.nonclaims) == 10

    def test_ten_assumptions(self, result):
        assert len(result.assumptions) == 10

    def test_serialization_valid(self, result):
        d = cross_coupling_result_to_dict(result)
        js = json.dumps(d, indent=2, default=str)
        assert len(js) > 100


# ================================================================
# Section 11: Physics Consistency (5 tests)
# ================================================================

class TestPhysicsConsistency:
    def test_alpha_br_1_beta_0_eliminates_defect(self, result):
        sc = result.coupling_scan
        if sc.pure_backreaction:
            assert sc.pure_backreaction.f_min < 0

    def test_A_eff_unity_at_Rext(self, result):
        A_eff_end = float(result.coupled_sectors.A_eff[-1])
        assert abs(A_eff_end - result.params.scalar_A) < 0.1

    def test_sigma_macro_coupled_analytic_at_beta_0(self, result):
        # At beta=0, sigma_macro should match D6 analytic
        for e in result.coupling_scan.entries:
            if abs(e.alpha_BR) < 1e-10 and abs(e.beta_XR) < 1e-10:
                assert abs(e.f_min - 0.498) < 0.05
                return

    def test_no_nan_in_profiles(self, result):
        mi = result.metric_injection
        assert all(math.isfinite(float(x)) for x in mi.f_coupled)

    def test_d6_entry_neutral(self, result):
        for e in result.coupling_scan.entries:
            if abs(e.alpha_BR) < 1e-10 and abs(e.beta_XR) < 1e-10:
                assert e.net_classification == "neutral"
                return
