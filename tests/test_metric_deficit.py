"""Tests for Phase 6C — Global Metric Positivity Deficit and Minimal Closure.

~90 tests covering:
  TestConstants (9)
  TestRadialGrid (4)
  TestDeficitProfile (8)
  TestMinimalSource (10)
  TestKineticDeficit (7)
  TestAnisotropyInsufficiency (5)
  TestAdditiveSource (6)
  TestTwoParamScan (10)
  TestMonotonicProfileGap (7)
  TestPhase6BComparison (6)
  TestNonclaims (4)
  TestSerialization (5)
"""

from __future__ import annotations

import math
import pytest
import numpy as np

from grut.metric_deficit import (
    DeficitParams,
    DeficitProfile,
    MinimalSourceResult,
    KineticDeficitProfile,
    AnisotropyInsufficiency,
    AdditiveSourceResult,
    TwoParamScanResult,
    MonotonicProfileGap,
    Phase6BComparison,
    ClosureClassification,
    MetricDeficitResult,
    make_radial_grid,
    compute_static_mass,
    compute_equilibrium_density,
    compute_deficit_profile,
    compute_minimal_source,
    compute_kinetic_deficit,
    assess_anisotropy_insufficiency,
    compute_additive_source,
    scan_two_parameter,
    assess_monotonic_profile_insufficiency,
    build_phase6b_comparison,
    classify_closure,
    compute_metric_deficit_analysis,
    metric_deficit_result_to_dict,
    ALPHA_VAC,
    BETA_Q,
    R_S,
    M_EXT,
    R_EQ,
    C_COMPACTNESS,
    TAU_CANONICAL,
    A_EFF_CONSTITUTIVE,
    A_SCHW,
    MASS_COEFF,
    PHASE6_F_AT_REQ,
    PHASE6B_A_CRIT_NATURAL,
    NONCLAIMS,
    MINIMAL_SOURCE_ASSUMPTIONS,
)


# ================================================================
# Module-scoped fixtures
# ================================================================

@pytest.fixture(scope="module")
def params():
    return DeficitParams(n_r=500, n_A=30, n_B=30)


@pytest.fixture(scope="module")
def r_arr(params):
    return make_radial_grid(params)


@pytest.fixture(scope="module")
def deficit(params):
    return compute_deficit_profile(params)


@pytest.fixture(scope="module")
def minimal_source(deficit, params):
    return compute_minimal_source(deficit, params)


@pytest.fixture(scope="module")
def master_result(params):
    return compute_metric_deficit_analysis(params)


# ================================================================
# TestConstants (9)
# ================================================================

class TestConstants:
    def test_alpha_vac(self):
        assert abs(ALPHA_VAC - 1.0 / 3.0) < 1e-10

    def test_M_ext(self):
        assert abs(M_EXT - 0.5) < 1e-10

    def test_R_eq(self):
        assert abs(R_EQ - 1.0 / 3.0) < 1e-10

    def test_tau_canonical(self):
        assert abs(TAU_CANONICAL - math.sqrt(1.5)) < 1e-10

    def test_compactness(self):
        assert abs(C_COMPACTNESS - 3.0) < 1e-10

    def test_A_schw(self):
        assert abs(A_SCHW - (-2.0)) < 1e-10

    def test_mass_coeff(self):
        expected = 2.0 * math.pi * M_EXT ** 2 / TAU_CANONICAL ** 2
        assert abs(MASS_COEFF - expected) < 1e-10

    def test_phase6_f_ref(self):
        assert abs(PHASE6_F_AT_REQ - (-17.71)) < 0.01

    def test_phase6b_a_crit(self):
        assert abs(PHASE6B_A_CRIT_NATURAL - 1.062) < 0.001


# ================================================================
# TestRadialGrid (4)
# ================================================================

class TestRadialGrid:
    def test_grid_length(self, params, r_arr):
        assert len(r_arr) == params.n_r

    def test_grid_starts_at_R_ext(self, params, r_arr):
        assert abs(r_arr[0] - params.R_ext) < 1e-10

    def test_grid_decreasing(self, r_arr):
        assert np.all(np.diff(r_arr) < 0)

    def test_grid_covers_R_eq(self, params, r_arr):
        assert r_arr[-1] < params.R_eq < r_arr[0]


# ================================================================
# TestDeficitProfile (8)
# ================================================================

class TestDeficitProfile:
    def test_delta_at_R_eq(self, deficit):
        assert abs(deficit.delta_at_R_eq - 2.951) < 0.05

    def test_m_at_R_eq(self, deficit):
        assert abs(deficit.m_at_R_eq - 3.118) < 0.05

    def test_f_at_R_eq(self, deficit):
        assert abs(deficit.f_at_R_eq - (-17.71)) / 17.71 < 0.02

    def test_delta_positive_fraction(self, deficit):
        assert 0.7 < deficit.fraction_r_with_delta_positive < 0.95

    def test_delta_at_R_ext_negative(self, deficit):
        assert deficit.delta[0] < 0

    def test_delta_at_R_min_positive(self, deficit):
        assert deficit.delta[-1] > 0

    def test_delta_max_positive(self, deficit):
        assert deficit.delta_max > 0

    def test_rho_eq_negative(self, deficit):
        assert np.all(deficit.rho_eq < 0)


# ================================================================
# TestMinimalSource (10)
# ================================================================

class TestMinimalSource:
    def test_epsilon_equals_sum(self, minimal_source):
        np.testing.assert_allclose(
            minimal_source.epsilon_min,
            minimal_source.component_A + minimal_source.component_B,
            atol=1e-12,
        )

    def test_component_A_is_abs_rho_eq(self, deficit, minimal_source):
        mask = deficit.delta > 0
        np.testing.assert_allclose(
            minimal_source.component_A[mask],
            np.abs(deficit.rho_eq[mask]),
            rtol=1e-10,
        )

    def test_component_B_formula(self, deficit, minimal_source):
        mask = deficit.delta > 0
        expected = 1.0 / (8.0 * math.pi * deficit.r[mask] ** 2)
        np.testing.assert_allclose(
            minimal_source.component_B[mask], expected, rtol=1e-10,
        )

    def test_epsilon_zero_outside_deficit(self, deficit, minimal_source):
        mask = deficit.delta <= 0
        np.testing.assert_allclose(
            minimal_source.epsilon_min[mask], 0.0, atol=1e-15,
        )

    def test_sigma_at_R_eq_matches_delta(self, minimal_source):
        assert abs(minimal_source.Sigma_at_R_eq - minimal_source.delta_at_R_eq) / minimal_source.delta_at_R_eq < 0.01

    def test_f_corrected_near_zero(self, minimal_source):
        assert minimal_source.f_corrected_min > -0.1

    def test_verification_passes(self, minimal_source):
        assert minimal_source.verification_passes

    def test_ratio_B_A_at_R_eq(self, minimal_source):
        assert abs(minimal_source.ratio_B_over_A_at_R_eq - 0.053) < 0.01

    def test_ratio_B_A_at_r1(self, minimal_source):
        assert abs(minimal_source.ratio_B_over_A_at_r1 - 0.48) < 0.05

    def test_four_assumptions(self, minimal_source):
        assert len(minimal_source.assumptions) == 4


# ================================================================
# TestKineticDeficit (7)
# ================================================================

class TestKineticDeficit:
    def test_phi_dot_formula(self, deficit, minimal_source, params):
        kd = compute_kinetic_deficit(minimal_source, params)
        mask = deficit.delta > 0
        np.testing.assert_allclose(
            kd.Phi_dot_deficit[mask],
            np.sqrt(2.0 * minimal_source.epsilon_min[mask]),
            rtol=1e-10,
        )

    def test_phi_dot_positive(self, minimal_source, params):
        kd = compute_kinetic_deficit(minimal_source, params)
        assert kd.Phi_dot_at_R_eq > 0

    def test_ratio_to_natural(self, minimal_source, params):
        kd = compute_kinetic_deficit(minimal_source, params)
        assert abs(kd.ratio_to_natural_at_R_eq - 1.0) < 0.15

    def test_monotonic_inward(self, minimal_source, params):
        kd = compute_kinetic_deficit(minimal_source, params)
        assert kd.is_monotonic_inward

    def test_not_achievable(self, minimal_source, params):
        kd = compute_kinetic_deficit(minimal_source, params)
        assert not kd.achievable_within_grut

    def test_phi_dot_max(self, minimal_source, params):
        kd = compute_kinetic_deficit(minimal_source, params)
        assert kd.Phi_dot_max >= kd.Phi_dot_at_R_eq

    def test_has_notes(self, minimal_source, params):
        kd = compute_kinetic_deficit(minimal_source, params)
        assert len(kd.notes) >= 3


# ================================================================
# TestAnisotropyInsufficiency (5)
# ================================================================

class TestAnisotropyInsufficiency:
    def test_vanishes_at_f_zero(self, params):
        ai = assess_anisotropy_insufficiency(params)
        assert ai.vanishes_at_f_zero

    def test_insufficient(self, params):
        ai = assess_anisotropy_insufficiency(params)
        assert ai.insufficient

    def test_formula(self, params):
        ai = assess_anisotropy_insufficiency(params)
        assert ai.p_r_minus_p_perp_formula == "f * (Phi')^2"

    def test_mechanism_present(self, params):
        ai = assess_anisotropy_insufficiency(params)
        assert len(ai.mechanism) > 50

    def test_self_quenching_mentioned(self, params):
        ai = assess_anisotropy_insufficiency(params)
        assert "quench" in ai.mechanism.lower() or "vanish" in ai.mechanism.lower()


# ================================================================
# TestAdditiveSource (6)
# ================================================================

class TestAdditiveSource:
    def test_works_by_construction(self, minimal_source, params):
        addsrc = compute_additive_source(minimal_source, params)
        assert addsrc.works_by_construction

    def test_requires_beyond_grut(self, minimal_source, params):
        addsrc = compute_additive_source(minimal_source, params)
        assert addsrc.requires_beyond_grut

    def test_rho_extra_equals_epsilon_min(self, minimal_source, params):
        addsrc = compute_additive_source(minimal_source, params)
        np.testing.assert_allclose(
            addsrc.rho_extra, minimal_source.epsilon_min, rtol=1e-10,
        )

    def test_f_corrected_matches(self, minimal_source, params):
        addsrc = compute_additive_source(minimal_source, params)
        np.testing.assert_allclose(
            addsrc.f_corrected, minimal_source.f_corrected, rtol=1e-10,
        )

    def test_f_corrected_min(self, minimal_source, params):
        addsrc = compute_additive_source(minimal_source, params)
        assert addsrc.f_corrected_min > -0.1

    def test_has_notes(self, minimal_source, params):
        addsrc = compute_additive_source(minimal_source, params)
        assert len(addsrc.notes) >= 2


# ================================================================
# TestTwoParamScan (10)
# ================================================================

class TestTwoParamScan:
    def test_contour_exists(self, params):
        tp = scan_two_parameter(params)
        assert tp.contour_exists

    def test_A_crit_at_B0_positive(self, params):
        tp = scan_two_parameter(params)
        assert tp.A_crit_at_B0 > 0

    def test_recovers_phase6b(self, params):
        tp = scan_two_parameter(params)
        assert tp.recovers_phase6b

    def test_B_crit_at_A0_positive(self, params):
        tp = scan_two_parameter(params)
        assert tp.B_crit_at_A0 > 0

    def test_contour_points(self, params):
        tp = scan_two_parameter(params)
        assert len(tp.threshold_contour_A) > 5

    def test_A_decreases_with_B(self, params):
        tp = scan_two_parameter(params)
        if len(tp.threshold_contour_A) > 2:
            assert tp.threshold_contour_A[-1] < tp.threshold_contour_A[0]

    def test_grid_shape(self, params):
        tp = scan_two_parameter(params)
        assert tp.f_min_grid.shape == (params.n_A + 1, params.n_B + 1)

    def test_f_min_at_origin_negative(self, params):
        tp = scan_two_parameter(params)
        assert tp.f_min_grid[0, 0] < 0  # no correction → f < 0

    def test_f_min_at_large_A_positive(self, params):
        tp = scan_two_parameter(params)
        assert tp.f_min_grid[-1, -1] > 0  # large correction → f > 0

    def test_A_crit_matches_expected(self, params):
        tp = scan_two_parameter(params)
        rho_eq_coeff = params.M ** 2 / (2.0 * params.tau ** 2)
        expected = PHASE6B_A_CRIT_NATURAL ** 2 * rho_eq_coeff
        assert abs(tp.A_crit_at_B0 - expected) / expected < 0.10

    def test_normalization_mapping(self, params):
        """Lock: A_coeff = A_amplitude^2 * M^2/(2*tau^2) for Phase 6B recovery."""
        tp = scan_two_parameter(params)
        rho_eq_coeff = params.M ** 2 / (2.0 * params.tau ** 2)
        expected = PHASE6B_A_CRIT_NATURAL ** 2 * rho_eq_coeff
        assert abs(tp.A_crit_at_B0 - expected) / expected < 0.05


# ================================================================
# TestMonotonicProfileGap (7)
# ================================================================

class TestMonotonicProfileGap:
    def test_four_profiles(self, minimal_source, params):
        mg = assess_monotonic_profile_insufficiency(minimal_source, params)
        assert len(mg.tested_profiles) == 4

    def test_includes_natural(self, minimal_source, params):
        mg = assess_monotonic_profile_insufficiency(minimal_source, params)
        assert "1/r^4" in mg.tested_profiles

    def test_gap_positive(self, minimal_source, params):
        mg = assess_monotonic_profile_insufficiency(minimal_source, params)
        assert mg.gap_fraction > 0

    def test_gap_at_intermediate_r(self, minimal_source, params):
        mg = assess_monotonic_profile_insufficiency(minimal_source, params)
        assert mg.r_at_max_gap > R_EQ

    def test_not_general_no_go(self, minimal_source, params):
        mg = assess_monotonic_profile_insufficiency(minimal_source, params)
        assert not mg.is_general_no_go

    def test_statement_present(self, minimal_source, params):
        mg = assess_monotonic_profile_insufficiency(minimal_source, params)
        assert len(mg.insufficiency_statement) > 50

    def test_has_notes(self, minimal_source, params):
        mg = assess_monotonic_profile_insufficiency(minimal_source, params)
        assert len(mg.notes) >= 3


# ================================================================
# TestPhase6BComparison (6)
# ================================================================

class TestPhase6BComparison:
    def test_A_crit_value(self, master_result):
        p6b = master_result.phase6b_comparison
        assert abs(p6b.A_crit_natural - 1.062) < 0.001

    def test_exceeds_unity(self, master_result):
        p6b = master_result.phase6b_comparison
        assert p6b.A_crit_exceeds_unity

    def test_excess_fraction(self, master_result):
        p6b = master_result.phase6b_comparison
        assert abs(p6b.excess_fraction - 0.062) < 0.01

    def test_component_A(self, master_result):
        p6b = master_result.phase6b_comparison
        assert p6b.natural_provides_component_A

    def test_not_component_B(self, master_result):
        p6b = master_result.phase6b_comparison
        assert not p6b.natural_provides_component_B

    def test_explanation(self, master_result):
        p6b = master_result.phase6b_comparison
        assert len(p6b.overshoot_explanation) > 50


# ================================================================
# TestNonclaims (4)
# ================================================================

class TestNonclaims:
    def test_count(self):
        assert len(NONCLAIMS) == 14

    def test_saturation_mentioned(self):
        text = " ".join(NONCLAIMS).lower()
        assert "saturation" in text or "f = 0" in text

    def test_no_go_disclaimed(self):
        text = " ".join(NONCLAIMS).lower()
        assert "not a general no-go" in text

    def test_assumptions_count(self):
        assert len(MINIMAL_SOURCE_ASSUMPTIONS) == 4


# ================================================================
# TestSerialization (5)
# ================================================================

class TestSerialization:
    def test_valid(self, master_result):
        d = metric_deficit_result_to_dict(master_result)
        assert d["valid"] is True

    def test_has_classification(self, master_result):
        d = metric_deficit_result_to_dict(master_result)
        assert "closure_classification" in d

    def test_classification_string(self, master_result):
        d = metric_deficit_result_to_dict(master_result)
        assert d["closure_classification"]["classification"] == \
            "current_closure_insufficient__minimal_additive_source_identified"

    def test_has_assumptions(self, master_result):
        d = metric_deficit_result_to_dict(master_result)
        assert len(d.get("assumptions", [])) == 4

    def test_has_nonclaims(self, master_result):
        d = metric_deficit_result_to_dict(master_result)
        assert len(d.get("nonclaims", [])) == 14
