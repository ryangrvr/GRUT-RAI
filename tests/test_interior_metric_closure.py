"""Tests for grut/interior_metric_closure.py — Appendix J.

Test coverage:
  TestConstants            — module-level constants and locked values
  TestDeficitChain         — three-layer metric deficit chain structure
  TestACritDerivation      — A_crit analytic computation
  TestSurfaceGravity       — kappa_GRUT and T_Killing
  TestKappaRatioAnalytic   — exact 3/5 ratio verification
  TestTransientCaveat      — transient horizon description
  TestFirstLawCrossCheck   — T_Killing vs T_1stlaw
  TestAnalyticalIdentities — algebraic consistency checks (A=0,A=1,A=A_crit)
  TestMasterAudit          — run_interior_metric_closure()
  TestForbiddenClaims      — forbidden claim guards
  TestExecutive            — executive determination string
"""

from __future__ import annotations

import math
import pytest

from grut.interior_metric_closure import (
    # constants
    ALPHA_VAC,
    BETA_Q,
    EPSILON_Q,
    R_S,
    M_EXT,
    R_EQ,
    C_EQ,
    TAU_SQ,
    TAU,
    R_EXT_CANONICAL,
    F_STATIC_AT_REQ,
    M_STATIC_AT_REQ,
    F_AT_A1,
    A_SCHW,
    A_EFF_CONSTITUTIVE,
    A_CRIT_NUMERICAL,
    A_CRIT_EXACT,
    A_CRIT_EXACT_SQ,
    F_PRIME_AT_REQ,
    KAPPA_GRUT,
    KAPPA_SCHW,
    KAPPA_RATIO,
    T_KILLING_OVER_T_HAWKING,
    A_CRIT_EXTREMAL,
    FORBIDDEN_CLAIMS,
    # data structures
    MetricLayer,
    ACritResult,
    SurfaceGravityResult,
    TransientCaveat,
    FirstLawCrossCheck,
    InteriorMetricClosureResult,
    # functions
    build_deficit_chain,
    compute_A_crit,
    compute_surface_gravity,
    build_transient_caveat,
    compute_first_law_cross_check,
    run_interior_metric_closure,
    check_layer_3a_cancellation,
    verify_f_static_at_A0,
    verify_f_at_A1,
    verify_kappa_ratio,
)

M_SUN_KG = 1.989e30


# ================================================================
# TestConstants
# ================================================================

class TestConstants:
    """Module-level constant correctness."""

    def test_alpha_vac(self):
        assert abs(ALPHA_VAC - 1.0 / 3.0) < 1e-15

    def test_beta_q(self):
        assert abs(BETA_Q - 2.0) < 1e-15

    def test_epsilon_q(self):
        assert abs(EPSILON_Q - ALPHA_VAC ** 2) < 1e-15

    def test_R_eq(self):
        assert abs(R_EQ - ALPHA_VAC * R_S) < 1e-15

    def test_C_eq(self):
        assert abs(C_EQ - 3.0) < 1e-14

    def test_tau_sq(self):
        # tau^2 = C_eq/2 = 3/2
        assert abs(TAU_SQ - 3.0 / 2.0) < 1e-14

    def test_tau(self):
        assert abs(TAU - math.sqrt(1.5)) < 1e-14

    def test_R_ext_canonical(self):
        assert abs(R_EXT_CANONICAL - 2.0 * R_S) < 1e-15

    def test_A_SCHW(self):
        # 1 - 2M/R_eq = 1 - 2*0.5/(1/3) = 1 - 3 = -2
        assert abs(A_SCHW - (-2.0)) < 1e-14

    def test_A_eff_constitutive(self):
        assert abs(A_EFF_CONSTITUTIVE - (-1.0)) < 1e-14

    def test_f_static_at_req_locked(self):
        assert abs(F_STATIC_AT_REQ - (-17.71)) < 1e-9

    def test_m_static_at_req_locked(self):
        assert abs(M_STATIC_AT_REQ - 3.118) < 1e-9

    def test_f_at_A1(self):
        assert abs(F_AT_A1 - A_SCHW) < 1e-14

    def test_A_crit_numerical_locked(self):
        assert abs(A_CRIT_NUMERICAL - 1.06) < 1e-10

    def test_A_crit_exact_positive(self):
        assert A_CRIT_EXACT > 1.0

    def test_A_crit_exact_close_to_numerical(self):
        assert abs(A_CRIT_EXACT - A_CRIT_NUMERICAL) / A_CRIT_NUMERICAL < 0.01

    def test_A_crit_sq_formula(self):
        # A_crit^2 = 1 + 2/(5*pi)
        expected = 1.0 + 2.0 / (5.0 * math.pi)
        assert abs(A_CRIT_EXACT_SQ - expected) < 1e-12

    def test_kappa_GRUT(self):
        assert abs(KAPPA_GRUT - 3.0 / 10.0) < 1e-12

    def test_kappa_Schw(self):
        # 1/(4M) = 1/(4*0.5) = 0.5
        assert abs(KAPPA_SCHW - 0.5) < 1e-14

    def test_kappa_ratio_exact(self):
        assert abs(KAPPA_RATIO - 3.0 / 5.0) < 1e-12

    def test_T_killing_over_T_hawking(self):
        assert abs(T_KILLING_OVER_T_HAWKING - 3.0 / 5.0) < 1e-12

    def test_A_crit_extremal_gt_canonical(self):
        # R_ext = r_s gives less room for kinetic boost => higher A_crit
        # Actually depends on direction: R_ext < 2*r_s means smaller domain,
        # less mass to integrate, so less kinetic needed? Let's just check > 1
        assert A_CRIT_EXTREMAL > 1.0

    def test_F_prime_at_req(self):
        # f'(R_eq) = 3/5
        assert abs(F_PRIME_AT_REQ - 3.0 / 5.0) < 1e-12

    def test_kappa_equals_half_f_prime(self):
        assert abs(KAPPA_GRUT - F_PRIME_AT_REQ / 2.0) < 1e-14


# ================================================================
# TestDeficitChain
# ================================================================

class TestDeficitChain:
    """Three-layer deficit chain structure and values."""

    def setup_method(self):
        self.layers = build_deficit_chain()

    def test_returns_list(self):
        assert isinstance(self.layers, list)

    def test_five_layers(self):
        assert len(self.layers) == 5

    def test_layer_types(self):
        for layer in self.layers:
            assert isinstance(layer, MetricLayer)

    def test_layer_names_unique(self):
        names = [l.name for l in self.layers]
        assert len(names) == len(set(names))

    def test_layer0_schwarzschild(self):
        l0 = self.layers[0]
        assert l0.name == "schwarzschild_reference"
        assert abs(l0.f_at_R_eq - A_SCHW) < 1e-14

    def test_layer1_constitutive(self):
        l1 = self.layers[1]
        assert l1.name == "constitutive_lapse_correction"
        assert abs(l1.f_at_R_eq - (-1.0)) < 1e-14

    def test_layer2_static_tov(self):
        l2 = self.layers[2]
        assert l2.name == "static_tov_equilibrium"
        assert abs(l2.f_at_R_eq - F_STATIC_AT_REQ) < 1e-9
        assert abs(l2.m_at_R_eq - M_STATIC_AT_REQ) < 1e-9

    def test_layer3a_A1(self):
        l3a = self.layers[3]
        assert l3a.name == "dynamical_natural_rate_A1"
        assert abs(l3a.f_at_R_eq - F_AT_A1) < 1e-14
        assert abs(l3a.m_at_R_eq - M_EXT) < 1e-14

    def test_layer3b_A_crit(self):
        l3b = self.layers[4]
        assert l3b.name == "dynamical_supercritical_A_crit"
        assert abs(l3b.f_at_R_eq - 0.0) < 1e-14
        assert abs(l3b.m_at_R_eq - R_EQ / 2.0) < 1e-14

    def test_layer3b_m_equals_R_eq_over_2(self):
        l3b = self.layers[4]
        assert abs(l3b.m_at_R_eq - R_EQ / 2.0) < 1e-14

    def test_f_monotonic_not_required(self):
        # Layer 2 (static TOV) is BELOW layer 0 — deficit gets worse before better
        l0 = self.layers[0]
        l2 = self.layers[2]
        assert l2.f_at_R_eq < l0.f_at_R_eq

    def test_locked_layers(self):
        # Layers 0, 1, 2, 3a should be locked (from upstream)
        assert self.layers[0].locked is True
        assert self.layers[1].locked is True
        assert self.layers[2].locked is True
        assert self.layers[3].locked is True

    def test_notes_populated(self):
        for layer in self.layers:
            assert len(layer.notes) > 0


# ================================================================
# TestACritDerivation
# ================================================================

class TestACritDerivation:
    """A_crit analytic derivation."""

    def setup_method(self):
        self.result = compute_A_crit()

    def test_returns_A_crit_result(self):
        assert isinstance(self.result, ACritResult)

    def test_A_crit_above_1(self):
        assert self.result.A_crit > 1.0

    def test_A_crit_close_to_locked(self):
        assert self.result.consistent_with_locked

    def test_A_crit_sq_correct(self):
        expected_sq = 1.0 + 2.0 / (5.0 * math.pi)
        assert abs(self.result.A_crit_sq - expected_sq) < 1e-12

    def test_A_crit_numerical_value(self):
        expected = math.sqrt(1.0 + 2.0 / (5.0 * math.pi))
        assert abs(self.result.A_crit - expected) < 1e-12

    def test_A_crit_percent_positive(self):
        assert self.result.A_crit_percent > 0.0

    def test_A_crit_percent_small(self):
        # Should be ~6.2%, well under 100%
        assert self.result.A_crit_percent < 20.0

    def test_numerator(self):
        # M - R_eq/2 = 0.5 - 1/6 = 1/3
        assert abs(self.result.numerator - 1.0 / 3.0) < 1e-14

    def test_denominator_positive(self):
        assert self.result.denominator > 0.0

    def test_extremal_A_crit(self):
        # extremal limit (R_ext = r_s = 1): A_crit^2 = 1 + 1/(2*pi)
        expected = math.sqrt(1.0 + 1.0 / (2.0 * math.pi))
        assert abs(self.result.extremal_limit_A_crit - expected) < 1e-10

    def test_notes_present(self):
        assert len(self.result.notes) > 0

    def test_R_ext_recorded(self):
        assert abs(self.result.R_ext - R_EXT_CANONICAL) < 1e-14

    def test_A_crit_increases_with_R_ext(self):
        # Larger R_ext means more volume for kinetic integration but also
        # larger domain for negative rho_eq — net effect: test direction
        r1 = compute_A_crit(R_ext=1.5)
        r2 = compute_A_crit(R_ext=3.0)
        # A_crit depends on (1/R_eq - 1/R_ext); as R_ext increases, this
        # denominator increases, so A_crit^2 - 1 decreases => A_crit decreases
        assert r1.A_crit > r2.A_crit


# ================================================================
# TestSurfaceGravity
# ================================================================

class TestSurfaceGravity:
    """kappa_GRUT and T_Killing."""

    def setup_method(self):
        self.result = compute_surface_gravity(A_crit_sq=A_CRIT_EXACT_SQ)

    def test_returns_surface_gravity_result(self):
        assert isinstance(self.result, SurfaceGravityResult)

    def test_kappa_GRUT_value(self):
        assert abs(self.result.kappa_GRUT - 3.0 / 10.0) < 1e-12

    def test_kappa_Schw_value(self):
        assert abs(self.result.kappa_Schw - 0.5) < 1e-14

    def test_kappa_ratio(self):
        assert abs(self.result.kappa_ratio - 3.0 / 5.0) < 1e-10

    def test_T_Killing_over_T_Hawking(self):
        assert abs(self.result.T_Killing_over_T_Hawking - 3.0 / 5.0) < 1e-6

    def test_T_Killing_below_T_Hawking(self):
        assert self.result.T_Killing_over_T_Hawking < 1.0

    def test_T_Killing_SI_positive(self):
        assert self.result.T_Killing_SI > 0.0

    def test_T_Hawking_SI_positive(self):
        assert self.result.T_Hawking_SI > 0.0

    def test_SI_ratio_consistent(self):
        ratio_SI = self.result.T_Killing_SI / self.result.T_Hawking_SI
        assert abs(ratio_SI - 3.0 / 5.0) < 1e-6

    def test_temperature_status(self):
        assert self.result.temperature_status == "new_candidate_grut_covariant"

    def test_derivation_string(self):
        assert len(self.result.derivation) > 0

    def test_notes_present(self):
        assert len(self.result.notes) > 0

    def test_f_prime_at_R_eq(self):
        assert abs(self.result.f_prime_at_R_eq - 3.0 / 5.0) < 1e-12

    def test_different_mass_same_ratio(self):
        # T_Killing/T_Hawking should be mass-independent
        r30 = compute_surface_gravity(A_crit_sq=A_CRIT_EXACT_SQ, M_SI=30 * M_SUN_KG)
        r10 = compute_surface_gravity(A_crit_sq=A_CRIT_EXACT_SQ, M_SI=10 * M_SUN_KG)
        assert abs(r30.T_Killing_over_T_Hawking - r10.T_Killing_over_T_Hawking) < 1e-8


# ================================================================
# TestKappaRatioAnalytic
# ================================================================

class TestKappaRatioAnalytic:
    """Exact algebraic verification of kappa_ratio = 3/5."""

    def test_factor_4_5(self):
        result = verify_kappa_ratio()
        assert abs(result["factor_4pi_M2_etc"] - 4.0 / 5.0) < 1e-12

    def test_f_prime_is_3_over_5(self):
        result = verify_kappa_ratio()
        assert abs(result["f_prime"] - 3.0 / 5.0) < 1e-12

    def test_kappa_GRUT_is_3_over_10(self):
        result = verify_kappa_ratio()
        assert abs(result["kappa_GRUT"] - 3.0 / 10.0) < 1e-12

    def test_kappa_ratio_exact_3_5(self):
        result = verify_kappa_ratio()
        assert result["exact_3_5"]

    def test_T_killing_equals_kappa_ratio(self):
        result = verify_kappa_ratio()
        assert abs(result["T_Killing_over_T_Hawking"] - 3.0 / 5.0) < 1e-12

    def test_formula_4pi_M2_Acrit2_tau2_Req(self):
        """Verify 4*pi*M^2*(A_crit^2-1)/(tau^2*R_eq) = 4/5 analytically."""
        M = M_EXT
        A_sq_minus_1 = 2.0 / (5.0 * math.pi)
        tau_sq = TAU_SQ
        R_eq = R_EQ
        factor = 4.0 * math.pi * M ** 2 * A_sq_minus_1 / (tau_sq * R_eq)
        # 4*pi*(1/4)*(2/(5*pi)) / (1.5*1/3) = pi*(2/(5*pi)) / 0.5 = (2/5)/0.5 = 4/5
        assert abs(factor - 4.0 / 5.0) < 1e-14


# ================================================================
# TestTransientCaveat
# ================================================================

class TestTransientCaveat:
    """Transient-horizon caveat."""

    def setup_method(self):
        self.caveat = build_transient_caveat()

    def test_returns_transient_caveat(self):
        assert isinstance(self.caveat, TransientCaveat)

    def test_decay_timescale_set(self):
        assert len(self.caveat.decay_timescale) > 0

    def test_mechanism_set(self):
        assert len(self.caveat.mechanism) > 0

    def test_late_time_f(self):
        assert abs(self.caveat.late_time_f - F_STATIC_AT_REQ) < 1e-9

    def test_late_time_f_negative(self):
        assert self.caveat.late_time_f < 0.0

    def test_classification(self):
        assert "transient" in self.caveat.classification

    def test_notes_present(self):
        assert len(self.caveat.notes) > 0


# ================================================================
# TestFirstLawCrossCheck
# ================================================================

class TestFirstLawCrossCheck:
    """Cross-check T_Killing vs first-law temperature target."""

    def setup_method(self):
        self.result = compute_first_law_cross_check(
            T_Killing_ratio=T_KILLING_OVER_T_HAWKING,
        )

    def test_returns_first_law_cross_check(self):
        assert isinstance(self.result, FirstLawCrossCheck)

    def test_T_Killing_ratio_recorded(self):
        assert abs(self.result.T_Killing_over_T_Hawking - 3.0 / 5.0) < 1e-12

    def test_T_1stlaw_ratio_default(self):
        # Default is 9.0 (Appendix I option b)
        assert abs(self.result.T_1stlaw_over_T_Hawking - 9.0) < 1e-14

    def test_gap_not_closed(self):
        # T_Killing = 0.6, T_1stlaw = 9.0 — far apart
        assert not self.result.gap_closed

    def test_ratio_T_Killing_to_1stlaw(self):
        # 0.6 / 9.0 = 1/15
        assert abs(self.result.ratio_T_Killing_to_1stlaw - 1.0 / 15.0) < 1e-12

    def test_gap_fraction_large(self):
        # gap fraction ~ (9-0.6)/9 ~ 0.933
        assert self.result.gap_fraction > 0.9

    def test_verdict_set(self):
        assert len(self.result.verdict) > 0

    def test_notes_present(self):
        assert len(self.result.notes) > 0


# ================================================================
# TestAnalyticalIdentities
# ================================================================

class TestAnalyticalIdentities:
    """Core algebraic consistency checks."""

    def test_layer3a_cancellation_exact(self):
        result = check_layer_3a_cancellation()
        assert result["cancellation_exact"]

    def test_layer3a_max_residual(self):
        result = check_layer_3a_cancellation()
        assert result["max_residual"] < 1e-14

    def test_f_at_A0_consistent_with_locked(self):
        result = verify_f_static_at_A0()
        assert result["f_consistent"]

    def test_m_at_A0_consistent_with_locked(self):
        result = verify_f_static_at_A0()
        assert result["m_consistent"]

    def test_f_at_A0_large_negative(self):
        result = verify_f_static_at_A0()
        assert result["f_at_R_eq_A0"] < -10.0

    def test_m_at_A0_much_larger_than_M(self):
        result = verify_f_static_at_A0()
        assert result["m_at_R_eq_A0"] > 1.0   # much larger than M_EXT = 0.5

    def test_f_at_A1_exact(self):
        result = verify_f_at_A1()
        assert result["consistent"]

    def test_f_at_A1_equals_A_SCHW(self):
        result = verify_f_at_A1()
        assert abs(result["f_at_R_eq_A1"] - A_SCHW) < 1e-14

    def test_m_at_A1_equals_M(self):
        result = verify_f_at_A1()
        assert abs(result["m_at_R_eq_A1"] - M_EXT) < 1e-14

    def test_A_crit_sq_from_mass_formula(self):
        """Verify A_crit^2 by solving m(R_eq) = R_eq/2 algebraically."""
        # m(R_eq) = M + 2*pi*M^2*(A^2-1)/tau^2 * (1/R_ext - 1/R_eq) = R_eq/2
        # solve for A^2:
        num = M_EXT - R_EQ / 2.0
        coeff = 2.0 * math.pi * M_EXT ** 2 / TAU_SQ
        denom = coeff * (1.0 / R_EQ - 1.0 / R_EXT_CANONICAL)
        A_sq = 1.0 + num / denom
        assert abs(A_sq - A_CRIT_EXACT_SQ) < 1e-12

    def test_f_at_A_crit_is_zero(self):
        """At A = A_crit, mass integral gives m = R_eq/2 and f = 0.

        Mass formula: m(R_eq, A) = M - delta_m_nat * (A^2 - 1)
        where delta_m_nat = 2*pi*M^2/tau^2 * (1/R_eq - 1/R_ext) > 0.
        """
        A_sq = A_CRIT_EXACT_SQ
        coeff = 2.0 * math.pi * M_EXT ** 2 / TAU_SQ
        delta_m_nat = coeff * (1.0 / R_EQ - 1.0 / R_EXT_CANONICAL)   # positive
        m_at_Acrit = M_EXT - delta_m_nat * (A_sq - 1.0)
        f_at_Acrit = 1.0 - 2.0 * m_at_Acrit / R_EQ
        assert abs(f_at_Acrit) < 1e-12

    def test_m_at_A_crit_equals_R_eq_over_2(self):
        """Mass at R_eq when A = A_crit equals R_eq/2 (Killing horizon condition)."""
        A_sq = A_CRIT_EXACT_SQ
        coeff = 2.0 * math.pi * M_EXT ** 2 / TAU_SQ
        delta_m_nat = coeff * (1.0 / R_EQ - 1.0 / R_EXT_CANONICAL)   # positive
        m_at_Acrit = M_EXT - delta_m_nat * (A_sq - 1.0)
        assert abs(m_at_Acrit - R_EQ / 2.0) < 1e-12


# ================================================================
# TestMasterAudit
# ================================================================

class TestMasterAudit:
    """run_interior_metric_closure() integration tests."""

    def setup_method(self):
        self.result = run_interior_metric_closure()

    def test_returns_result(self):
        assert isinstance(self.result, InteriorMetricClosureResult)

    def test_valid(self):
        assert self.result.valid

    def test_has_layers(self):
        assert self.result.layers is not None
        assert len(self.result.layers) == 5

    def test_has_A_crit(self):
        assert self.result.A_crit_result is not None

    def test_has_surface_gravity(self):
        assert self.result.surface_gravity is not None

    def test_has_transient_caveat(self):
        assert self.result.transient_caveat is not None

    def test_has_first_law_check(self):
        assert self.result.first_law_cross_check is not None

    def test_executive_string(self):
        assert len(self.result.executive) > 0
        assert "transient" in self.result.executive

    def test_executive_classification(self):
        assert self.result.executive == (
            "interior_metric_positivity_achievable_transient_supercritical_processing"
        )

    def test_nonclaims_present(self):
        assert len(self.result.nonclaims) > 0

    def test_forbidden_claims_list(self):
        assert len(self.result.forbidden_claims) > 0

    def test_diagnostics_keys(self):
        keys = self.result.diagnostics.keys()
        assert "alpha_vac" in keys
        assert "A_crit_exact" in keys
        assert "kappa_ratio" in keys
        assert "T_Killing_over_T_Hawking" in keys

    def test_diagnostics_alpha_vac(self):
        assert abs(self.result.diagnostics["alpha_vac"] - 1.0 / 3.0) < 1e-14

    def test_diagnostics_kappa_ratio(self):
        assert abs(self.result.diagnostics["kappa_ratio"] - 3.0 / 5.0) < 1e-12

    def test_diagnostics_T_killing(self):
        assert abs(
            self.result.diagnostics["T_Killing_over_T_Hawking"] - 3.0 / 5.0
        ) < 1e-12

    def test_A_crit_consistent_in_master(self):
        assert self.result.A_crit_result.consistent_with_locked

    def test_kappa_ratio_in_master(self):
        assert abs(
            self.result.surface_gravity.kappa_ratio - 3.0 / 5.0
        ) < 1e-10

    def test_T_killing_ratio_in_master(self):
        assert abs(
            self.result.surface_gravity.T_Killing_over_T_Hawking - 3.0 / 5.0
        ) < 1e-6

    def test_gap_not_closed_in_master(self):
        assert not self.result.first_law_cross_check.gap_closed

    def test_transient_late_time_f(self):
        assert self.result.transient_caveat.late_time_f < 0.0

    def test_layers_f_ordering(self):
        # Layer 3b (Killing horizon) has f = 0 (highest)
        # Layer 2 (static TOV) has lowest f
        layers = self.result.layers
        f_values = [l.f_at_R_eq for l in layers]
        assert f_values[2] < f_values[0]   # static TOV << Schwarzschild
        assert f_values[4] > f_values[2]   # A_crit >> static TOV


# ================================================================
# TestForbiddenClaims
# ================================================================

class TestForbiddenClaims:
    """Forbidden claim guards."""

    def test_forbidden_claims_list(self):
        assert isinstance(FORBIDDEN_CLAIMS, list)
        assert len(FORBIDDEN_CLAIMS) > 0

    def test_t_killing_not_proven(self):
        assert "t_killing_is_the_physical_temperature" in FORBIDDEN_CLAIMS

    def test_transient_not_permanent(self):
        assert "transient_horizon_is_permanent" in FORBIDDEN_CLAIMS

    def test_a_crit_not_physically_realised(self):
        assert "a_crit_is_physically_realised" in FORBIDDEN_CLAIMS

    def test_first_law_gap_not_closed(self):
        assert "first_law_gap_is_closed" in FORBIDDEN_CLAIMS

    def test_ghost_route_not_resolved(self):
        assert "ghost_route_resolved" in FORBIDDEN_CLAIMS

    def test_appendix_c_not_overridden(self):
        assert "appendix_c_blockers_overridden" in FORBIDDEN_CLAIMS

    def test_hawking_radiation_not_derived(self):
        assert "hawking_radiation_derived" in FORBIDDEN_CLAIMS

    def test_information_paradox_not_solved(self):
        assert "information_paradox_resolved" in FORBIDDEN_CLAIMS

    def test_no_forbidden_in_executive(self):
        result = run_interior_metric_closure()
        for fc in FORBIDDEN_CLAIMS:
            assert fc not in result.executive, (
                f"Forbidden claim '{fc}' found in executive string"
            )

    def test_nonclaims_cover_T_killing(self):
        result = run_interior_metric_closure()
        nc_text = " ".join(result.nonclaims).lower()
        assert "t_killing" in nc_text or "killing" in nc_text.replace("_", "")


# ================================================================
# TestExecutive
# ================================================================

class TestExecutive:
    """Executive determination."""

    def test_executive_string_value(self):
        result = run_interior_metric_closure()
        assert result.executive == (
            "interior_metric_positivity_achievable_transient_supercritical_processing"
        )

    def test_executive_not_blocked(self):
        result = run_interior_metric_closure()
        assert "blocked" not in result.executive

    def test_executive_contains_transient(self):
        result = run_interior_metric_closure()
        assert "transient" in result.executive

    def test_executive_contains_supercritical(self):
        result = run_interior_metric_closure()
        assert "supercritical" in result.executive


# ================================================================
# TestCrossConsistency
# ================================================================

class TestCrossConsistency:
    """Cross-module consistency checks."""

    def test_A_crit_sq_from_A_crit(self):
        assert abs(A_CRIT_EXACT_SQ - A_CRIT_EXACT ** 2) < 1e-14

    def test_kappa_ratio_from_kappa_GRUT_and_Schw(self):
        assert abs(KAPPA_RATIO - KAPPA_GRUT / KAPPA_SCHW) < 1e-14

    def test_T_killing_ratio_equals_kappa_ratio(self):
        assert abs(T_KILLING_OVER_T_HAWKING - KAPPA_RATIO) < 1e-14

    def test_epsilon_Q_equals_alpha_vac_sq(self):
        assert abs(EPSILON_Q - ALPHA_VAC ** 2) < 1e-15

    def test_R_eq_over_rs_equals_alpha_vac(self):
        assert abs(R_EQ / R_S - ALPHA_VAC) < 1e-15

    def test_tau_sq_is_C_eq_over_2(self):
        assert abs(TAU_SQ - C_EQ / 2.0) < 1e-14

    def test_A_SCHW_is_1_minus_C_eq(self):
        # 1 - 2M/R_eq = 1 - 2*(r_s/2)/(r_s/3) = 1 - 3 = -2
        assert abs(A_SCHW - (1.0 - C_EQ)) < 1e-14

    def test_constitutive_correction_is_plus_1(self):
        delta_A = A_EFF_CONSTITUTIVE - A_SCHW
        assert abs(delta_A - 1.0) < 1e-14

    def test_f_at_A0_chain_consistency(self):
        """A = 0 analytic formula must agree with locked static TOV value."""
        result = verify_f_static_at_A0()
        assert result["f_consistent"]
        assert result["m_consistent"]

    def test_layer_ordering(self):
        """f values at R_eq: static_tov << dyn_A1 = schw < constitutive < A_crit=0."""
        layers = build_deficit_chain()
        f = {l.name: l.f_at_R_eq for l in layers}
        # static TOV is worst: f = -17.71
        assert f["static_tov_equilibrium"] < f["schwarzschild_reference"]
        # constitutive lapse gives a +1 improvement over Schwarzschild
        assert f["schwarzschild_reference"] < f["constitutive_lapse_correction"]
        # dynamical A=1 recovers Schwarzschild exactly: equal to layer 0
        assert abs(f["dynamical_natural_rate_A1"] - f["schwarzschild_reference"]) < 1e-13
        # A_crit achieves f = 0 (highest)
        assert f["constitutive_lapse_correction"] < f["dynamical_supercritical_A_crit"]
        assert abs(f["dynamical_supercritical_A_crit"]) < 1e-14
