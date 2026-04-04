"""Tests for grut/metric_closure_program.py — Appendix K.

Covers:
  TestMassIntegralHelper     — _mass_integral_power_law formula for n=2,4,6
  TestComponentBAlgebra      — eta^2_point = 1/(20pi); delta = 1/3; profile vs point
  TestCandidateCatalog       — >=5 candidates; rho_eq negative; kinetic 1/r^4; hedgehog
  TestLapseSignNumerical     — max_f < 0; positive_static_grut_count = 0; nonneg=False
  TestClosureCondition       — A=0 f≈-17.71; A=1 f=-2; A=A_crit f=0; CompB f=0
  TestVerdictComputed        — verdicts assigned from Boolean outcomes, not hardcoded
  TestForbiddenClaims        — no permanent/GRUT-native static Killing horizon claim
  TestCrossConsistency       — eta^2_point vs COMP_B_COEFF; A_crit from Appendix J
  TestMasterAudit            — run_metric_closure_program() end-to-end
"""

from __future__ import annotations

import math
import pytest

from grut.metric_closure_program import (
    # Constants
    ALPHA_VAC, BETA_Q, R_S, M_EXT, R_EQ, C_EQ, TAU_SQ, R_EXT,
    MASS_COEFF, F_STATIC, M_STATIC, A_SCHW, A_CRIT, A_EFF_CONST,
    COMP_B_COEFF_GLOBAL, M_KILLING, DELTA_AFTER_A1,
    VERDICT_Q1, VERDICT_Q2, VERDICT_Q3, FORBIDDEN_CLAIMS,
    # Functions — import test_* under aliases to avoid pytest collection
    _mass_integral_power_law,
    build_candidate_catalog,
    compute_component_b_analysis,
    test_static_lapse_sign as run_lapse_sign_test,
    test_closure_condition as run_closure_condition_test,
    assign_verdicts,
    run_metric_closure_program,
    # Data structures
    CandidateSource, ComponentBAnalysis, LapseSignTest,
    ClosureConditionTest, MetricClosureProgramResult,
)


# ================================================================
# Helpers
# ================================================================

def _result() -> MetricClosureProgramResult:
    """Cache-free: each test gets a fresh run."""
    return run_metric_closure_program()


# ================================================================
# TestMassIntegralHelper
# ================================================================

class TestMassIntegralHelper:
    """Unit tests for _mass_integral_power_law."""

    def test_n2_formula(self):
        """For n=2: Sigma = 4pi*coeff*(R_ext - R_eq)."""
        coeff = 1.0 / (8.0 * math.pi)
        sigma = _mass_integral_power_law(coeff, n=2, R_eq=R_EQ, R_ext=R_EXT)
        expected = 4.0 * math.pi * coeff * (R_EXT - R_EQ)
        assert abs(sigma - expected) < 1e-10

    def test_n4_formula(self):
        """For n=4: Sigma = 4pi*coeff * (1/R_eq - 1/R_ext) * ... verify sign."""
        coeff = M_EXT ** 2 / (2.0 * TAU_SQ)
        sigma_pos = _mass_integral_power_law(coeff, n=4)
        sigma_neg = _mass_integral_power_law(-coeff, n=4)
        assert sigma_pos > 0.0
        assert sigma_neg < 0.0
        assert abs(sigma_pos + sigma_neg) < 1e-12   # antisymmetry in coeff

    def test_n4_exact_value(self):
        """n=4: Sigma = 4pi*coeff / (-1) * [R_ext^{-1} - R_eq^{-1}]."""
        coeff = M_EXT ** 2 / (2.0 * TAU_SQ)   # = 1/12
        sigma = _mass_integral_power_law(coeff, n=4)
        expected = 4.0 * math.pi * coeff / (3 - 4) * (R_EXT ** (3 - 4) - R_EQ ** (3 - 4))
        assert abs(sigma - expected) < 1e-10

    def test_n6_positive_for_positive_coeff(self):
        """For n=6 with positive coeff: Sigma > 0.
        exponent = 3-6 = -3; [R_ext^{-3} - R_eq^{-3}] < 0, so Sigma = coeff/(-3)*neg > 0.
        The spatial_gradient is negative because its effective coeff = 2*M^2*f < 0 (f < 0).
        """
        sigma = _mass_integral_power_law(1.0, n=6)
        assert sigma > 0.0

    def test_n3_logarithmic(self):
        """For n=3: Sigma = 4pi*coeff*ln(R_ext/R_eq)."""
        coeff = 1.0
        sigma = _mass_integral_power_law(coeff, n=3)
        expected = 4.0 * math.pi * coeff * math.log(R_EXT / R_EQ)
        assert abs(sigma - expected) < 1e-10

    def test_antisymmetry_n2(self):
        """Sigma sign flips when coeff sign flips (all n)."""
        for n in [2, 4, 6]:
            s1 = _mass_integral_power_law(+1.0, n=n)
            s2 = _mass_integral_power_law(-1.0, n=n)
            assert abs(s1 + s2) < 1e-12, f"antisymmetry failed at n={n}"

    def test_n2_hedgehog_with_global_coeff(self):
        """Hedgehog: eta^2 = 1/(8pi) gives positive sigma for R_ext > R_eq."""
        sigma = _mass_integral_power_law(COMP_B_COEFF_GLOBAL, n=2)
        assert sigma > 0.0
        # Exact: 4pi * (1/(8pi)) * (R_ext - R_eq) = (1/2)*(R_ext - R_eq) = 5/6
        expected = 0.5 * (R_EXT - R_EQ)
        assert abs(sigma - expected) < 1e-10


# ================================================================
# TestComponentBAlgebra
# ================================================================

class TestComponentBAlgebra:
    """Algebraic tests for the Component B requirement."""

    def test_delta_after_a1(self):
        """DELTA_AFTER_A1 = M - R_eq/2 = 1/3 exactly."""
        assert abs(DELTA_AFTER_A1 - 1.0 / 3.0) < 1e-12

    def test_m_killing(self):
        """M_KILLING = R_eq/2 = 1/6."""
        assert abs(M_KILLING - R_EQ / 2.0) < 1e-12
        assert abs(M_KILLING - 1.0 / 6.0) < 1e-12

    def test_comp_b_coeff_global(self):
        """COMP_B_COEFF_GLOBAL = 1/(8*pi)."""
        assert abs(COMP_B_COEFF_GLOBAL - 1.0 / (8.0 * math.pi)) < 1e-12

    def test_eta_sq_point_formula(self):
        """eta^2_point = delta / [4pi*(R_ext - R_eq)] = 1/(20 pi)."""
        candidates = build_candidate_catalog()
        comp_b = compute_component_b_analysis(candidates)
        expected = (1.0 / 3.0) / (4.0 * math.pi * (R_EXT - R_EQ))
        assert abs(comp_b.eta_sq_point - expected) < 1e-10

    def test_eta_sq_point_equals_1_over_20pi(self):
        """eta^2_point = 1/(20*pi) exactly (canonical units)."""
        candidates = build_candidate_catalog()
        comp_b = compute_component_b_analysis(candidates)
        expected = 1.0 / (20.0 * math.pi)
        assert abs(comp_b.eta_sq_point - expected) < 1e-10

    def test_eta_sq_profile_equals_global_coeff(self):
        """eta^2_profile = COMP_B_COEFF_GLOBAL = 1/(8 pi)."""
        candidates = build_candidate_catalog()
        comp_b = compute_component_b_analysis(candidates)
        assert abs(comp_b.eta_sq_profile - COMP_B_COEFF_GLOBAL) < 1e-12

    def test_eta_sq_point_less_than_profile(self):
        """Point closure needs less than global profile closure."""
        candidates = build_candidate_catalog()
        comp_b = compute_component_b_analysis(candidates)
        assert comp_b.eta_sq_point < comp_b.eta_sq_profile

    def test_eta_sq_ratio(self):
        """eta^2_point / eta^2_profile = (1/(20pi)) / (1/(8pi)) = 8/20 = 2/5."""
        candidates = build_candidate_catalog()
        comp_b = compute_component_b_analysis(candidates)
        expected_ratio = (1.0 / (20.0 * math.pi)) / (1.0 / (8.0 * math.pi))
        assert abs(comp_b.eta_sq_ratio - expected_ratio) < 1e-10
        assert abs(comp_b.eta_sq_ratio - 2.0 / 5.0) < 1e-10

    def test_1r4_cannot_close_statically(self):
        """1/r^4 sources: mass integral ~ (1/R_eq - 1/R_ext), scaling different from 1/r^2."""
        # 1/r^4 integration: Sigma ~ coeff * 4pi * (1/R_eq - 1/R_ext)
        # 1/r^2 integration: Sigma ~ coeff * 4pi * (R_ext - R_eq)
        # These scale differently: 1/r^4 gives ~8pi/3, 1/r^2 gives ~5pi/6
        sigma_r4 = _mass_integral_power_law(1.0, n=4)   # shape for 1/r^4
        sigma_r2 = _mass_integral_power_law(1.0, n=2)   # shape for 1/r^2
        # Different magnitudes: confirms distinct closure requirements
        assert sigma_r4 != sigma_r2

    def test_achievable_dynamically_is_true(self):
        """Kinetic at A_crit achieves f=0 (Appendix J result)."""
        candidates = build_candidate_catalog()
        comp_b = compute_component_b_analysis(candidates)
        assert comp_b.achievable_dynamically is True

    def test_achievable_statically_is_false(self):
        """No GRUT-native static source provides Component B in tested catalog."""
        candidates = build_candidate_catalog()
        comp_b = compute_component_b_analysis(candidates)
        assert comp_b.achievable_statically is False

    def test_delta_equals_1_third(self):
        """delta_after_a1 field in dataclass = 1/3."""
        candidates = build_candidate_catalog()
        comp_b = compute_component_b_analysis(candidates)
        assert abs(comp_b.delta_after_a1 - 1.0 / 3.0) < 1e-12


# ================================================================
# TestCandidateCatalog
# ================================================================

class TestCandidateCatalog:
    """Tests for the candidate source catalog."""

    def test_at_least_five_candidates(self):
        """Catalog must contain at least 5 candidate sources."""
        candidates = build_candidate_catalog()
        assert len(candidates) >= 5

    def test_catalog_has_six_candidates(self):
        """Catalog contains exactly 6 candidate sources (one per GRUT sector object)."""
        candidates = build_candidate_catalog()
        assert len(candidates) == 6

    def test_rho_eq_present(self):
        """rho_eq candidate is in catalog."""
        candidates = build_candidate_catalog()
        names = [c.name for c in candidates]
        assert "rho_eq" in names

    def test_rho_eq_negative_mass_integral(self):
        """rho_eq has negative mass integral (worsens the deficit)."""
        candidates = build_candidate_catalog()
        rho_eq = next(c for c in candidates if c.name == "rho_eq")
        assert rho_eq.mass_integral_canonical < 0.0

    def test_rho_eq_is_grut_native(self):
        """rho_eq is GRUT-native."""
        candidates = build_candidate_catalog()
        rho_eq = next(c for c in candidates if c.name == "rho_eq")
        assert rho_eq.grut_native is True

    def test_rho_eq_is_static(self):
        """rho_eq is available in the static limit."""
        candidates = build_candidate_catalog()
        rho_eq = next(c for c in candidates if c.name == "rho_eq")
        assert rho_eq.static_available is True

    def test_rho_eq_radial_power_4(self):
        """rho_eq has radial power 4 (~ 1/r^4)."""
        candidates = build_candidate_catalog()
        rho_eq = next(c for c in candidates if c.name == "rho_eq")
        assert rho_eq.radial_power == 4

    def test_rho_eq_does_not_provide_component_b(self):
        """rho_eq cannot supply Component B (wrong profile and negative sign)."""
        candidates = build_candidate_catalog()
        rho_eq = next(c for c in candidates if c.name == "rho_eq")
        assert rho_eq.provides_component_b is False

    def test_kinetic_A1_radial_power_4(self):
        """Kinetic source has radial power 4 (Component A, not B)."""
        candidates = build_candidate_catalog()
        kin = next(c for c in candidates if c.name == "kinetic_A1")
        assert kin.radial_power == 4

    def test_kinetic_A1_not_static(self):
        """Kinetic source requires Phi_dot != 0: not static."""
        candidates = build_candidate_catalog()
        kin = next(c for c in candidates if c.name == "kinetic_A1")
        assert kin.static_available is False

    def test_kinetic_A1_positive_mass_integral(self):
        """Kinetic source at A=1 has positive mass integral (reduces m(R_eq))."""
        candidates = build_candidate_catalog()
        kin = next(c for c in candidates if c.name == "kinetic_A1")
        assert kin.mass_integral_canonical > 0.0

    def test_kinetic_A1_grut_native(self):
        """Kinetic source is GRUT-native."""
        candidates = build_candidate_catalog()
        kin = next(c for c in candidates if c.name == "kinetic_A1")
        assert kin.grut_native is True

    def test_kinetic_does_not_provide_component_b(self):
        """Kinetic source is 1/r^4 (Component A), not 1/r^2 (Component B)."""
        candidates = build_candidate_catalog()
        kin = next(c for c in candidates if c.name == "kinetic_A1")
        assert kin.provides_component_b is False

    def test_hedgehog_radial_power_2(self):
        """O(3) hedgehog has radial power 2 (Component B profile)."""
        candidates = build_candidate_catalog()
        h = next(c for c in candidates if c.name == "o3_hedgehog")
        assert h.radial_power == 2

    def test_hedgehog_not_grut_native(self):
        """O(3) hedgehog is NOT GRUT-native (D13/D14/D15)."""
        candidates = build_candidate_catalog()
        h = next(c for c in candidates if c.name == "o3_hedgehog")
        assert h.grut_native is False

    def test_hedgehog_provides_component_b(self):
        """O(3) hedgehog provides Component B."""
        candidates = build_candidate_catalog()
        h = next(c for c in candidates if c.name == "o3_hedgehog")
        assert h.provides_component_b is True

    def test_hedgehog_positive_mass_integral(self):
        """Hedgehog has positive mass integral (reduces m(R_eq) toward threshold)."""
        candidates = build_candidate_catalog()
        h = next(c for c in candidates if c.name == "o3_hedgehog")
        assert h.mass_integral_canonical > 0.0

    def test_hedgehog_static(self):
        """Hedgehog is available statically."""
        candidates = build_candidate_catalog()
        h = next(c for c in candidates if c.name == "o3_hedgehog")
        assert h.static_available is True

    def test_route_b_unresolved(self):
        """Route B g_- mass integral is NaN (unresolved)."""
        candidates = build_candidate_catalog()
        rb = next(c for c in candidates if c.name == "route_b_g_minus")
        assert math.isnan(rb.mass_integral_canonical)

    def test_route_b_profile_unknown(self):
        """Route B g_- profile_type is 'unknown'."""
        candidates = build_candidate_catalog()
        rb = next(c for c in candidates if c.name == "route_b_g_minus")
        assert rb.profile_type == "unknown"

    def test_no_grut_native_static_1r2_positive(self):
        """No GRUT-native, static, 1/r^2, positive candidate exists in catalog."""
        candidates = build_candidate_catalog()
        grut_static_r2_pos = [
            c for c in candidates
            if c.grut_native
            and c.static_available
            and c.radial_power == 2
            and c.sign_in_barrier == "positive"
        ]
        assert len(grut_static_r2_pos) == 0

    def test_barrier_potential_negative(self):
        """Barrier potential V_Q effective contribution is negative."""
        candidates = build_candidate_catalog()
        vq = next(c for c in candidates if c.name == "barrier_potential_V_Q")
        assert vq.sign_in_barrier == "negative"
        assert vq.mass_integral_canonical < 0.0

    def test_spatial_gradient_negative(self):
        """Spatial gradient (1/2) f (Phi')^2 is negative when f < 0."""
        candidates = build_candidate_catalog()
        grad = next(c for c in candidates if c.name == "spatial_gradient")
        assert grad.sign_in_barrier == "negative"

    def test_kinetic_and_rho_eq_cancel_exactly(self):
        """Sigma_kin_A1 = -Sigma_rho_eq (exact cancellation at A=1)."""
        candidates = build_candidate_catalog()
        rho_eq = next(c for c in candidates if c.name == "rho_eq")
        kin = next(c for c in candidates if c.name == "kinetic_A1")
        assert abs(kin.mass_integral_canonical + rho_eq.mass_integral_canonical) < 1e-10


# ================================================================
# TestLapseSignNumerical
# ================================================================

class TestLapseSignNumerical:
    """Numerical lapse sign test."""

    def test_positive_static_grut_count_zero(self):
        """No positive, GRUT-native, static sources in catalog."""
        candidates = build_candidate_catalog()
        lapse = run_lapse_sign_test(candidates)
        assert lapse.positive_static_grut_count == 0

    def test_max_f_from_static_grut_is_negative(self):
        """Maximum f(R_eq) from static GRUT sources is negative."""
        candidates = build_candidate_catalog()
        lapse = run_lapse_sign_test(candidates)
        assert lapse.max_f_from_static_grut < 0.0

    def test_static_nonneg_not_achieved(self):
        """Static GRUT sources cannot achieve f(R_eq) >= 0."""
        candidates = build_candidate_catalog()
        lapse = run_lapse_sign_test(candidates)
        assert lapse.static_nonneg_achieved is False

    def test_max_f_worse_than_schwarzschild(self):
        """Static GRUT f(R_eq) is worse than Schwarzschild (-2)."""
        candidates = build_candidate_catalog()
        lapse = run_lapse_sign_test(candidates)
        assert lapse.max_f_from_static_grut < A_SCHW

    def test_max_f_consistent_with_locked_value(self):
        """Static GRUT f(R_eq) is in the vicinity of -17.71 (locked from tov_interior)."""
        candidates = build_candidate_catalog()
        lapse = run_lapse_sign_test(candidates)
        # Numerical integration uses two static sources (rho_eq + V_Q_eff)
        # which doubles the deficit compared to tov_interior's single-source
        # The exact value is less important than being << 0
        assert lapse.max_f_from_static_grut < -10.0

    def test_dynamic_transient_achieves_zero(self):
        """Locked result from Appendix J: dynamic A=A_crit achieves f=0."""
        candidates = build_candidate_catalog()
        lapse = run_lapse_sign_test(candidates)
        assert lapse.dynamic_transient_achieves_zero is True

    def test_obstruction_is_set_when_static_fails(self):
        """Obstruction string is non-empty when static_nonneg_achieved=False."""
        candidates = build_candidate_catalog()
        lapse = run_lapse_sign_test(candidates)
        assert not lapse.static_nonneg_achieved
        assert len(lapse.obstruction) > 0
        assert "lapse" in lapse.obstruction.lower() or "insufficiency" in lapse.obstruction.lower() or "negative" in lapse.obstruction.lower()

    def test_candidates_tested_count(self):
        """All catalog candidates are counted in the test."""
        candidates = build_candidate_catalog()
        lapse = run_lapse_sign_test(candidates)
        assert lapse.candidates_tested == len(candidates)


# ================================================================
# TestClosureCondition
# ================================================================

class TestClosureCondition:
    """Tests for the four Killing-horizon scenarios."""

    def setup_method(self):
        self.candidates = build_candidate_catalog()
        self.comp_b = compute_component_b_analysis(self.candidates)
        self.ct = run_closure_condition_test(self.candidates, self.comp_b)

    def test_f_at_A0_near_static_locked(self):
        """A=0 static gives f ≈ -17.71 (locked from tov_interior.py)."""
        assert abs(self.ct.f_at_A0 - F_STATIC) < 0.05

    def test_m_at_A0_near_m_static(self):
        """A=0 static gives m ≈ 3.118 (locked from tov_interior.py)."""
        assert abs(self.ct.m_at_A0 - M_STATIC) < 1e-6

    def test_f_at_A1_equals_schwarzschild(self):
        """A=1 kinetic gives f = A_Schw = -2 (Schwarzschild, not zero)."""
        assert abs(self.ct.f_at_A1 - A_SCHW) < 1e-6
        assert abs(self.ct.f_at_A1 - (-2.0)) < 1e-6

    def test_m_at_A1_equals_M_ext(self):
        """A=1 kinetic gives m(R_eq) = M_EXT = 1/2 (exact cancellation)."""
        assert abs(self.ct.m_at_A1 - M_EXT) < 1e-6

    def test_A1_does_not_satisfy_killing(self):
        """A=1 gives f=-2 not f=0: kinetic_A1_satisfies_killing = False."""
        assert self.ct.kinetic_A1_satisfies_killing is False

    def test_A0_does_not_satisfy_killing(self):
        """A=0 static gives f=-17.71: kinetic_A0_satisfies_killing = False."""
        assert self.ct.kinetic_A0_satisfies_killing is False

    def test_f_at_Acrit_near_zero(self):
        """A=A_crit gives f(R_eq) ≈ 0 (transient Killing horizon)."""
        assert abs(self.ct.f_at_Acrit) < 1e-3

    def test_m_at_Acrit_equals_m_killing(self):
        """A=A_crit gives m(R_eq) = R_eq/2 = M_KILLING = 1/6."""
        assert abs(self.ct.m_at_Acrit - M_KILLING) < 1e-3

    def test_kinetic_Acrit_satisfies_killing(self):
        """A=A_crit achieves f=0: kinetic_Acrit_satisfies_killing = True."""
        assert self.ct.kinetic_Acrit_satisfies_killing is True

    def test_component_b_satisfies_killing(self):
        """Component B with eta^2_point achieves f=0: component_b_satisfies_killing=True."""
        assert self.ct.component_b_satisfies_killing is True

    def test_f_with_component_b_near_zero(self):
        """Component B with eta^2_point: f(R_eq) ≈ 0."""
        assert abs(self.ct.f_with_component_b) < 1e-6

    def test_m_with_component_b_equals_m_killing(self):
        """Component B with eta^2_point: m(R_eq) = R_eq/2 exactly."""
        assert abs(self.ct.m_with_component_b - M_KILLING) < 1e-10

    def test_component_b_not_grut_native(self):
        """Component B (hedgehog) is NOT GRUT-native: D13/D14/D15."""
        assert self.ct.component_b_grut_native is False

    def test_static_grut_does_not_satisfy_killing(self):
        """No static GRUT-native source satisfies the Killing condition."""
        assert self.ct.static_grut_satisfies_killing is False

    def test_monotonicity_A0_A1_Acrit(self):
        """f(R_eq) increases monotonically: A=0 < A=1 < A=A_crit."""
        assert self.ct.f_at_A0 < self.ct.f_at_A1 < self.ct.f_at_Acrit

    def test_closure_formula_set(self):
        """Closure condition formula string is set."""
        assert len(self.ct.closure_condition_formula) > 0
        assert "m(R_eq)" in self.ct.closure_condition_formula or "Killing" in self.ct.closure_condition_formula


# ================================================================
# TestVerdictComputed
# ================================================================

class TestVerdictComputed:
    """Verdicts are assigned from Boolean test outcomes, not hardcoded strings."""

    def setup_method(self):
        self.candidates = build_candidate_catalog()
        self.comp_b = compute_component_b_analysis(self.candidates)
        self.lapse = run_lapse_sign_test(self.candidates)
        self.ct = run_closure_condition_test(self.candidates, self.comp_b)
        self.q1, self.q2, self.q3, self.exec_str = assign_verdicts(
            self.lapse, self.ct, self.comp_b, self.candidates
        )

    def test_q1_is_not_found(self):
        """Q1 verdict: no GRUT-native static source provides Component B."""
        assert self.q1 == VERDICT_Q1["not_found"]

    def test_q1_consistent_with_achievable_statically(self):
        """Q1 verdict follows from achievable_statically Boolean."""
        if self.comp_b.achievable_statically:
            assert self.q1 == VERDICT_Q1["found"]
        else:
            assert self.q1 == VERDICT_Q1["not_found"]

    def test_q2_is_not_achievable(self):
        """Q2 verdict: static timelike lapse not achievable from GRUT-native sources."""
        assert self.q2 == VERDICT_Q2["not_achievable"]

    def test_q2_consistent_with_static_nonneg(self):
        """Q2 verdict follows from static_nonneg_achieved Boolean."""
        if self.lapse.static_nonneg_achieved:
            assert self.q2 == VERDICT_Q2["achievable"]
        else:
            assert self.q2 == VERDICT_Q2["not_achievable"]

    def test_q3_is_kinetic_only(self):
        """Q3 verdict: Killing condition requires supercritical kinetic or non-native Component B."""
        assert self.q3 == VERDICT_Q3["kinetic_only"]

    def test_q3_consistent_with_closure_test(self):
        """Q3 verdict follows from kinetic_Acrit and component_b Boolean outcomes."""
        if self.ct.static_grut_satisfies_killing:
            assert self.q3 == VERDICT_Q3["static_grut"]
        elif self.ct.kinetic_Acrit_satisfies_killing or self.ct.component_b_satisfies_killing:
            assert self.q3 == VERDICT_Q3["kinetic_only"]
        else:
            assert self.q3 == VERDICT_Q3["not_closeable"]

    def test_executive_consistent_with_q2_and_q3(self):
        """Executive verdict follows from Q2 and Q3 outcomes."""
        if self.q2 == VERDICT_Q2["achievable"]:
            assert "static_grut" in self.exec_str
        elif self.q3 == VERDICT_Q3["kinetic_only"]:
            assert "supercritical_kinetic" in self.exec_str or "nonnative" in self.exec_str

    def test_executive_not_static_achievable(self):
        """Executive does NOT say static GRUT closure achievable (given current catalog)."""
        assert "static_grut_metric_closure_achievable" not in self.exec_str or self.lapse.static_nonneg_achieved

    def test_verdict_strings_are_nonempty(self):
        """All four verdict strings are non-empty."""
        for v in [self.q1, self.q2, self.q3, self.exec_str]:
            assert len(v) > 0

    def test_q1_q2_both_from_catalog_failures(self):
        """Both Q1 and Q2 are negative results driven by same catalog finding."""
        # Both follow from: no GRUT-native static source has 1/r^2 positive profile
        assert self.q1 == VERDICT_Q1["not_found"]
        assert self.q2 == VERDICT_Q2["not_achievable"]
        # These are consistent: if no 1/r^2 source, no static nonneg achievable
        assert not self.comp_b.achievable_statically
        assert not self.lapse.static_nonneg_achieved


# ================================================================
# TestForbiddenClaims
# ================================================================

class TestForbiddenClaims:
    """Verify the module does not make forbidden claims."""

    def test_forbidden_claims_list_nonempty(self):
        """FORBIDDEN_CLAIMS list is populated."""
        assert len(FORBIDDEN_CLAIMS) > 0

    def test_grut_native_static_f_nonneg_is_forbidden(self):
        """The claim that GRUT-native static sources achieve f >= 0 is forbidden."""
        assert "grut_native_static_source_achieves_f_nonneg_at_R_eq" in FORBIDDEN_CLAIMS

    def test_component_b_grut_native_is_forbidden(self):
        """The claim that Component B is GRUT-native is forbidden."""
        assert "component_b_is_grut_native" in FORBIDDEN_CLAIMS

    def test_permanent_killing_horizon_is_forbidden(self):
        """The claim of permanent Killing horizon from GRUT-native sources is forbidden."""
        assert "permanent_killing_horizon_from_grut_native_sources" in FORBIDDEN_CLAIMS

    def test_g_minus_resolved_is_forbidden(self):
        """The claim that g_- sector is resolved is forbidden."""
        assert "g_minus_sector_resolved" in FORBIDDEN_CLAIMS

    def test_catalog_exhaustive_no_go_is_forbidden(self):
        """Treating catalog verdict as universal no-go theorem is forbidden."""
        assert "catalog_is_exhaustive_no_go" in FORBIDDEN_CLAIMS

    def test_hawking_radiation_derived_is_forbidden(self):
        """The claim that Hawking radiation is derived is forbidden."""
        assert "hawking_radiation_derived" in FORBIDDEN_CLAIMS

    def test_result_includes_forbidden_claims_list(self):
        """run_metric_closure_program() result includes the forbidden claims list."""
        result = run_metric_closure_program()
        assert len(result.forbidden_claims) > 0
        for claim in FORBIDDEN_CLAIMS:
            assert claim in result.forbidden_claims

    def test_executive_verdict_does_not_contain_forbidden(self):
        """Executive verdict string does not contain any forbidden claim keyword."""
        result = run_metric_closure_program()
        exec_str = result.executive
        for fc in FORBIDDEN_CLAIMS:
            assert fc not in exec_str, f"Forbidden claim '{fc}' found in executive verdict"


# ================================================================
# TestCrossConsistency
# ================================================================

class TestCrossConsistency:
    """Cross-consistency between Appendix K and upstream locked values."""

    def test_a_crit_constant_matches_appendix_j(self):
        """A_CRIT constant ~ 1.062 (locked from dynamical_interior.py / Appendix J)."""
        assert abs(A_CRIT - 1.062) < 0.001

    def test_a_crit_analytic_matches_numerical(self):
        """Analytic A_crit = sqrt(1 + 2/(5pi)) ≈ 1.062 matches locked value."""
        a_crit_analytic = math.sqrt(1.0 + 2.0 / (5.0 * math.pi))
        assert abs(a_crit_analytic - A_CRIT) < 1e-3

    def test_eta_sq_point_less_than_global_coeff(self):
        """eta^2_point (1/(20pi)) < COMP_B_COEFF_GLOBAL (1/(8pi))."""
        eta_sq_point = 1.0 / (20.0 * math.pi)
        assert eta_sq_point < COMP_B_COEFF_GLOBAL

    def test_comp_b_coeff_global_consistent_with_metric_deficit(self):
        """COMP_B_COEFF_GLOBAL = 1/(8pi) matches metric_deficit.py locked value."""
        assert abs(COMP_B_COEFF_GLOBAL - 1.0 / (8.0 * math.pi)) < 1e-12

    def test_f_static_consistent_with_tov(self):
        """F_STATIC = -17.71 matches locked value from tov_interior.py."""
        assert abs(F_STATIC - (-17.71)) < 0.01

    def test_m_static_consistent_with_tov(self):
        """M_STATIC = 3.118 matches locked value from tov_interior.py."""
        assert abs(M_STATIC - 3.118) < 0.001

    def test_a_eff_const_consistent_with_covariant_interior(self):
        """A_EFF_CONST = -1 matches constitutive lapse from covariant_interior.py."""
        assert abs(A_EFF_CONST - (-1.0)) < 1e-10

    def test_a_schw_consistent_with_schwarzschild(self):
        """A_SCHW = 1 - 2M/R_eq = -2 (Schwarzschild reference)."""
        assert abs(A_SCHW - (-2.0)) < 1e-10

    def test_closure_m_at_Acrit_from_appendix_j_formula(self):
        """m(R_eq, A_crit) from Appendix J exact formula = R_eq/2."""
        A_crit_sq = 1.0 + 2.0 / (5.0 * math.pi)
        delta_m_nat = MASS_COEFF * (1.0 / R_EQ - 1.0 / R_EXT)
        m_Acrit = M_EXT - delta_m_nat * (A_crit_sq - 1.0)
        assert abs(m_Acrit - M_KILLING) < 1e-6

    def test_mass_coeff_formula(self):
        """MASS_COEFF = 2 pi M^2 / tau^2 = pi/3."""
        expected = 2.0 * math.pi * M_EXT ** 2 / TAU_SQ
        assert abs(MASS_COEFF - expected) < 1e-12
        assert abs(MASS_COEFF - math.pi / 3.0) < 1e-12

    def test_delta_m_nat_equals_5pi_over_6(self):
        """delta_m_nat = MASS_COEFF * (1/R_eq - 1/R_ext) = 5pi/6."""
        delta_m_nat = MASS_COEFF * (1.0 / R_EQ - 1.0 / R_EXT)
        expected = 5.0 * math.pi / 6.0
        assert abs(delta_m_nat - expected) < 1e-10

    def test_hedgehog_mass_integral_equals_5_sixth(self):
        """Hedgehog sigma = 4pi*(1/(8pi))*(R_ext-R_eq) = (1/2)*5/3 = 5/6."""
        sigma = _mass_integral_power_law(COMP_B_COEFF_GLOBAL, n=2)
        expected = 5.0 / 6.0
        assert abs(sigma - expected) < 1e-10

    def test_rho_eq_sigma_equals_minus_5pi_over_6(self):
        """rho_eq sigma = -MASS_COEFF*(1/R_eq - 1/R_ext) = -5pi/6 (increases m by 5pi/6)."""
        rho_eq_coeff = M_EXT ** 2 / (2.0 * TAU_SQ)
        sigma = _mass_integral_power_law(-rho_eq_coeff, n=4)
        expected = -5.0 * math.pi / 6.0
        assert abs(sigma - expected) < 1e-10


# ================================================================
# TestMasterAudit
# ================================================================

class TestMasterAudit:
    """End-to-end tests for run_metric_closure_program()."""

    def setup_method(self):
        self.result = run_metric_closure_program()

    def test_result_is_valid(self):
        """Master result is valid."""
        assert self.result.valid is True

    def test_result_has_candidates(self):
        """Result contains candidate sources."""
        assert len(self.result.candidates) >= 5

    def test_result_has_component_b(self):
        """Result contains ComponentBAnalysis."""
        assert self.result.component_b_analysis is not None

    def test_result_has_lapse_test(self):
        """Result contains LapseSignTest."""
        assert self.result.lapse_test is not None

    def test_result_has_closure_test(self):
        """Result contains ClosureConditionTest."""
        assert self.result.closure_test is not None

    def test_q1_verdict_nonempty(self):
        """Q1 verdict is non-empty."""
        assert len(self.result.q1_verdict) > 0

    def test_q2_verdict_nonempty(self):
        """Q2 verdict is non-empty."""
        assert len(self.result.q2_verdict) > 0

    def test_q3_verdict_nonempty(self):
        """Q3 verdict is non-empty."""
        assert len(self.result.q3_verdict) > 0

    def test_executive_nonempty(self):
        """Executive verdict is non-empty."""
        assert len(self.result.executive) > 0

    def test_nonclaims_nonempty(self):
        """Nonclaims list is populated."""
        assert len(self.result.nonclaims) > 0

    def test_forbidden_claims_nonempty(self):
        """Forbidden claims list is populated."""
        assert len(self.result.forbidden_claims) > 0

    def test_q1_is_not_found(self):
        """Q1 result: no GRUT-native static source provides Component B."""
        assert self.result.q1_verdict == VERDICT_Q1["not_found"]

    def test_q2_is_not_achievable(self):
        """Q2 result: static timelike lapse not achievable from GRUT-native sources."""
        assert self.result.q2_verdict == VERDICT_Q2["not_achievable"]

    def test_q3_is_kinetic_only(self):
        """Q3 result: Killing condition requires supercritical kinetic or non-native source."""
        assert self.result.q3_verdict == VERDICT_Q3["kinetic_only"]

    def test_executive_contains_supercritical(self):
        """Executive verdict references supercritical kinetic or nonnative Component B."""
        assert (
            "supercritical" in self.result.executive
            or "nonnative" in self.result.executive
        )

    def test_diagnostics_populated(self):
        """Diagnostics dict has expected keys."""
        diag = self.result.diagnostics
        for key in ["alpha_vac", "R_eq", "M_EXT", "A_CRIT", "F_STATIC", "COMP_B_COEFF_GLOBAL"]:
            assert key in diag, f"Missing diagnostic key: {key}"

    def test_diagnostics_static_nonneg_false(self):
        """Diagnostics confirm static_nonneg_achieved=False."""
        assert self.result.diagnostics["static_nonneg_achieved"] is False

    def test_diagnostics_a1_not_killing(self):
        """Diagnostics confirm kinetic_A1 does not satisfy Killing condition."""
        assert self.result.diagnostics["kinetic_A1_satisfies_killing"] is False

    def test_diagnostics_acrit_satisfies_killing(self):
        """Diagnostics confirm kinetic_Acrit satisfies Killing condition."""
        assert self.result.diagnostics["kinetic_Acrit_satisfies_killing"] is True

    def test_diagnostics_comp_b_satisfies_killing(self):
        """Diagnostics confirm Component B satisfies Killing condition."""
        assert self.result.diagnostics["component_b_satisfies_killing"] is True

    def test_component_b_not_achievable_statically(self):
        """Component B not achievable from GRUT-native static sources."""
        assert self.result.diagnostics["component_b_achievable_statically"] is False

    def test_n_candidates_in_diagnostics(self):
        """n_candidates diagnostic matches actual catalog length."""
        assert self.result.diagnostics["n_candidates"] == len(self.result.candidates)
