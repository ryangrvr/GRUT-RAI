"""Tests for grut/first_law_gap_audit.py — Appendix I.

Coverage targets
----------------
  TestConstants                 — canonical parameter values and R_GAP
  TestBarrierPotentialNumerical — compute_barrier_potential_at_Req for several masses
  TestBarrierPotentialSimplified— compute_barrier_potential_simplified agrees with full
  TestExactRatio                — compute_V_Q_exact_ratio analytic formula
  TestMassIndependence          — V_Q/c² constant across masses
  TestEntropyRevision           — required entropy ratio, effective radius ratio
  TestTemperatureRevision       — T_1stlaw/T_diss = 1/R, magnitudes, relation to T_H
  TestGapClosureParameters      — Q and α needed for R = 1
  TestOptionBuilders            — build_* functions produce correct verdicts
  TestMasterAudit               — run_first_law_gap_audit() executive determination
  TestForbiddenClaimGuards      — assert_no_unsupported_claims raises on forbidden strings
  TestInheritedClassifications  — Appendix D, E, H unchanged
  TestSummaryString             — summary_string runs and contains key tokens
"""

import math
import pytest

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from grut.first_law_gap_audit import (
    # constants
    G_SI,
    C_SI,
    HBAR_SI,
    K_B,
    L_PLANCK,
    ALPHA_VAC,
    BETA_Q,
    EPSILON_Q,
    R_EQ_OVER_RS,
    Q_CANONICAL,
    M_SUN_KG,
    M_REF_KG,
    R_GAP,
    _FORBIDDEN_CLASSIFICATIONS,
    # data structures
    BarrierWorkAnalysis,
    EntropyRevisionAnalysis,
    TemperatureRevisionAnalysis,
    GapStructureAnalysis,
    FirstLawGapResult,
    # helpers
    compute_barrier_potential_at_Req,
    compute_barrier_potential_simplified,
    verify_V_Q_mass_independence,
    compute_V_Q_exact_ratio,
    compute_required_entropy_ratio,
    compute_effective_radius_ratio,
    compute_T_1stlaw_over_T_diss,
    compute_R_gap_for_exact_R_one,
    compute_alpha_needed_for_R_one,
    # builders
    build_barrier_work_analysis,
    build_entropy_revision_analysis,
    build_temperature_revision_analysis,
    build_gap_structure,
    # master
    run_first_law_gap_audit,
    summary_string,
)


# ================================================================
# TestConstants
# ================================================================

class TestConstants:
    """Canonical GRUT parameter values."""

    def test_alpha_vac(self):
        assert abs(ALPHA_VAC - 1.0 / 3.0) < 1e-15

    def test_beta_Q(self):
        assert BETA_Q == 2.0

    def test_epsilon_Q(self):
        expected = (1.0 / 3.0) ** 2
        assert abs(EPSILON_Q - expected) < 1e-15

    def test_R_eq_over_rs(self):
        """R_eq/r_s = ε_Q^(1/β_Q) = (1/9)^(1/2) = 1/3."""
        assert abs(R_EQ_OVER_RS - 1.0 / 3.0) < 1e-14

    def test_Q_canonical(self):
        """Q = β_Q/α_vac = 2/(1/3) = 6."""
        assert abs(Q_CANONICAL - 6.0) < 1e-14

    def test_R_gap_formula(self):
        """R_GAP = 4π√3/(3Q) = 2π√3/9."""
        expected = 4.0 * math.pi * math.sqrt(3.0) / (3.0 * Q_CANONICAL)
        assert abs(R_GAP - expected) < 1e-14

    def test_R_gap_value(self):
        """R_GAP ≈ 1.209 (not equal to 1)."""
        assert 1.20 < R_GAP < 1.22
        assert R_GAP != 1.0

    def test_R_gap_alt_formula(self):
        """R_GAP = 2π√3/9."""
        expected = 2.0 * math.pi * math.sqrt(3.0) / 9.0
        assert abs(R_GAP - expected) < 1e-14

    def test_M_ref(self):
        assert abs(M_REF_KG - 30.0 * M_SUN_KG) < 1e20

    def test_planck_length(self):
        expected = math.sqrt(HBAR_SI * G_SI / C_SI ** 3)
        assert abs(L_PLANCK - expected) < 1e-50

    def test_forbidden_classifications_non_empty(self):
        assert len(_FORBIDDEN_CLASSIFICATIONS) >= 6

    def test_gap_closed_is_forbidden(self):
        assert "gap_closed" in _FORBIDDEN_CLASSIFICATIONS

    def test_first_law_proven_is_forbidden(self):
        assert "first_law_proven" in _FORBIDDEN_CLASSIFICATIONS

    def test_temperature_proven_is_forbidden(self):
        assert "temperature_proven" in _FORBIDDEN_CLASSIFICATIONS


# ================================================================
# TestBarrierPotentialNumerical
# ================================================================

class TestBarrierPotentialNumerical:
    """V_Q(R_eq)/c² should equal -0.5 for any mass (full formula)."""

    def _check(self, M_solar, tol=1e-10):
        M_kg = M_solar * M_SUN_KG
        v = compute_barrier_potential_at_Req(M_kg)
        assert abs(v - (-0.5)) < tol, (
            f"V_Q/c² = {v} for {M_solar} M_sun (expected -0.5)"
        )

    def test_10_solar(self):
        self._check(10.0)

    def test_30_solar(self):
        self._check(30.0)

    def test_100_solar(self):
        self._check(100.0)

    def test_1e6_solar(self):
        self._check(1e6)

    def test_1_solar(self):
        self._check(1.0)

    def test_negative(self):
        """V_Q must be negative."""
        v = compute_barrier_potential_at_Req(M_REF_KG)
        assert v < 0.0

    def test_sign_exact(self):
        v = compute_barrier_potential_at_Req(M_REF_KG)
        assert abs(v + 0.5) < 1e-10


# ================================================================
# TestBarrierPotentialSimplified
# ================================================================

class TestBarrierPotentialSimplified:
    """compute_barrier_potential_simplified must agree with full formula."""

    def test_agreement_30_solar(self):
        M_kg = M_REF_KG
        v_full = compute_barrier_potential_at_Req(M_kg)
        v_simp = compute_barrier_potential_simplified(M_kg)
        assert abs(v_full - v_simp) < 1e-12

    def test_agreement_10_solar(self):
        M_kg = 10.0 * M_SUN_KG
        v_full = compute_barrier_potential_at_Req(M_kg)
        v_simp = compute_barrier_potential_simplified(M_kg)
        assert abs(v_full - v_simp) < 1e-12

    def test_both_return_neg_half(self):
        v = compute_barrier_potential_simplified(M_REF_KG)
        assert abs(v + 0.5) < 1e-10


# ================================================================
# TestExactRatio
# ================================================================

class TestExactRatio:
    """compute_V_Q_exact_ratio — analytic formula only."""

    def test_canonical_returns_neg_half(self):
        v = compute_V_Q_exact_ratio(BETA_Q, EPSILON_Q)
        assert abs(v + 0.5) < 1e-14

    def test_formula_derivation(self):
        """
        V_Q/c² = -1/(2*(1+β_Q)*ε_Q^(1/β_Q))
        = -1/(2 * 3 * (1/3)) = -1/2
        """
        beta = BETA_Q     # 2
        eps = EPSILON_Q   # 1/9
        R_eq_over_rs = eps ** (1.0 / beta)  # 1/3
        expected = -1.0 / (2.0 * (1.0 + beta) * R_eq_over_rs)
        assert abs(expected + 0.5) < 1e-14

    def test_no_mass_dependence(self):
        """Exact ratio has no mass dependence by construction."""
        v = compute_V_Q_exact_ratio()
        assert isinstance(v, float)
        assert v == compute_V_Q_exact_ratio(BETA_Q, EPSILON_Q)

    def test_agrees_with_numerical(self):
        v_exact = compute_V_Q_exact_ratio()
        v_num = compute_barrier_potential_at_Req(M_REF_KG)
        assert abs(v_exact - v_num) < 1e-10


# ================================================================
# TestMassIndependence
# ================================================================

class TestMassIndependence:
    """V_Q(R_eq)/c² is exactly mass-independent."""

    def test_verify_across_masses(self):
        results = verify_V_Q_mass_independence([10.0, 30.0, 100.0, 1e6])
        values = list(results.values())
        for v in values:
            assert abs(v + 0.5) < 1e-10

    def test_spread_is_tiny(self):
        results = verify_V_Q_mass_independence([1.0, 10.0, 100.0, 1e4, 1e8])
        values = list(results.values())
        spread = max(values) - min(values)
        assert spread < 1e-10

    def test_dV_dM_zero(self):
        """Finite-difference approximation of dV/dM should be ~0."""
        M1 = 30.0 * M_SUN_KG
        M2 = 31.0 * M_SUN_KG
        v1 = compute_barrier_potential_at_Req(M1)
        v2 = compute_barrier_potential_at_Req(M2)
        # V_Q/c² is constant, so (v2-v1)/(M2-M1)*c² ≈ 0
        dV_dM = (v2 - v1) / (M2 - M1) * C_SI ** 2
        assert abs(dV_dM) < 1e-10   # essentially machine zero


# ================================================================
# TestEntropyRevision
# ================================================================

class TestEntropyRevision:
    """Option (a): required entropy ratio to close the gap."""

    def test_required_entropy_ratio(self):
        """S_correct/S_eq = 1/R."""
        ratio = compute_required_entropy_ratio(R_GAP)
        assert abs(ratio - 1.0 / R_GAP) < 1e-14

    def test_required_entropy_ratio_lt_one(self):
        """S_correct < S_eq (entropy must decrease to close gap)."""
        ratio = compute_required_entropy_ratio(R_GAP)
        assert ratio < 1.0

    def test_required_entropy_ratio_value(self):
        """≈ 0.827."""
        ratio = compute_required_entropy_ratio(R_GAP)
        assert 0.82 < ratio < 0.84

    def test_effective_radius_ratio(self):
        """R_eff/R_eq = 1/√R."""
        ratio = compute_effective_radius_ratio(R_GAP)
        assert abs(ratio - 1.0 / math.sqrt(R_GAP)) < 1e-14

    def test_effective_radius_ratio_lt_one(self):
        ratio = compute_effective_radius_ratio(R_GAP)
        assert ratio < 1.0

    def test_effective_radius_ratio_value(self):
        """≈ 0.909."""
        ratio = compute_effective_radius_ratio(R_GAP)
        assert 0.90 < ratio < 0.92

    def test_s_ratio_r_eff_ratio_relation(self):
        """S_correct/S_eq = (R_eff/R_eq)^2."""
        s_ratio = compute_required_entropy_ratio()
        r_ratio = compute_effective_radius_ratio()
        assert abs(s_ratio - r_ratio ** 2) < 1e-14

    def test_consistent_with_r_gap(self):
        """R_gap × (S_correct/S_eq) = 1."""
        s_ratio = compute_required_entropy_ratio()
        assert abs(R_GAP * s_ratio - 1.0) < 1e-14


# ================================================================
# TestTemperatureRevision
# ================================================================

class TestTemperatureRevision:
    """Option (b): T_1stlaw/T_diss = 1/R."""

    def test_T_1stlaw_over_T_diss(self):
        ratio = compute_T_1stlaw_over_T_diss(R_GAP)
        assert abs(ratio - 1.0 / R_GAP) < 1e-14

    def test_T_1stlaw_lt_T_diss(self):
        """T_1stlaw < T_diss (T_1stlaw is colder)."""
        ratio = compute_T_1stlaw_over_T_diss(R_GAP)
        assert ratio < 1.0

    def test_T_1stlaw_ratio_value(self):
        """≈ 0.827."""
        ratio = compute_T_1stlaw_over_T_diss()
        assert 0.82 < ratio < 0.84

    def test_T_1stlaw_equals_9_T_hawking(self):
        """T_1stlaw = 9·T_Hawking (exact, derived in Appendix H)."""
        M_kg = M_REF_KG
        T_hawk = HBAR_SI * C_SI ** 3 / (8.0 * math.pi * G_SI * M_kg * K_B)
        T_1stlaw = 9.0 * T_hawk

        # T_diss = ℏω₀/(Q·k_B)
        r_s = 2.0 * G_SI * M_kg / C_SI ** 2
        R_eq = r_s * R_EQ_OVER_RS
        omega_0 = math.sqrt(BETA_Q * G_SI * M_kg / R_eq ** 3)
        T_diss = HBAR_SI * omega_0 / (Q_CANONICAL * K_B)

        expected_ratio = T_1stlaw / T_diss
        computed_ratio = compute_T_1stlaw_over_T_diss()
        assert abs(computed_ratio - expected_ratio) < 1e-10

    def test_T_ratio_equals_entropy_ratio(self):
        """T_1stlaw/T_diss = S_correct/S_eq (both equal 1/R)."""
        t_ratio = compute_T_1stlaw_over_T_diss()
        s_ratio = compute_required_entropy_ratio()
        assert abs(t_ratio - s_ratio) < 1e-14


# ================================================================
# TestGapClosureParameters
# ================================================================

class TestGapClosureParameters:
    """Parameters needed to close the gap exactly."""

    def test_Q_for_R_one(self):
        """Q_needed = 4π√3/3 ≈ 7.26."""
        Q_needed = compute_R_gap_for_exact_R_one()
        expected = 4.0 * math.pi * math.sqrt(3.0) / 3.0
        assert abs(Q_needed - expected) < 1e-14

    def test_Q_for_R_one_value(self):
        Q_needed = compute_R_gap_for_exact_R_one()
        assert 7.2 < Q_needed < 7.4

    def test_Q_for_R_one_gt_current(self):
        """Q_needed > Q_canonical = 6."""
        Q_needed = compute_R_gap_for_exact_R_one()
        assert Q_needed > Q_CANONICAL

    def test_alpha_needed(self):
        """α_vac_needed = β_Q/Q_needed ≈ 0.276."""
        alpha_needed = compute_alpha_needed_for_R_one()
        Q_needed = compute_R_gap_for_exact_R_one()
        assert abs(alpha_needed - BETA_Q / Q_needed) < 1e-14

    def test_alpha_needed_lt_current(self):
        """α_vac_needed < α_vac = 1/3."""
        alpha_needed = compute_alpha_needed_for_R_one()
        assert alpha_needed < ALPHA_VAC

    def test_alpha_needed_value(self):
        """≈ 0.276."""
        alpha_needed = compute_alpha_needed_for_R_one()
        assert 0.27 < alpha_needed < 0.29

    def test_check_R_one_with_Q_needed(self):
        """With Q_needed, R should equal 1."""
        Q_needed = compute_R_gap_for_exact_R_one()
        R_check = 4.0 * math.pi * math.sqrt(3.0) / (3.0 * Q_needed)
        assert abs(R_check - 1.0) < 1e-14

    def test_current_params_give_R_gap(self):
        """With current parameters, R = R_GAP (not 1)."""
        R_check = 4.0 * math.pi * math.sqrt(3.0) / (3.0 * Q_CANONICAL)
        assert abs(R_check - R_GAP) < 1e-14


# ================================================================
# TestOptionBuilders
# ================================================================

class TestOptionBuilders:
    """build_* functions return correct verdicts and values."""

    def test_barrier_work_verdict(self):
        bwa = build_barrier_work_analysis()
        assert bwa.verdict == "CLOSED"

    def test_barrier_work_V_Q(self):
        bwa = build_barrier_work_analysis()
        assert abs(bwa.V_Q_value_over_c_sq + 0.5) < 1e-10

    def test_barrier_work_zero_delta(self):
        bwa = build_barrier_work_analysis()
        assert bwa.delta_V_Q_over_delta_M == 0.0

    def test_barrier_work_M_independent(self):
        bwa = build_barrier_work_analysis()
        assert bwa.is_M_independent is True

    def test_barrier_work_contributions_zero(self):
        bwa = build_barrier_work_analysis()
        assert bwa.barrier_work_contribution == "ZERO"
        assert bwa.memory_work_contribution == "ZERO"

    def test_entropy_revision_verdict(self):
        era = build_entropy_revision_analysis()
        assert era.verdict == "STRUCTURALLY_POSSIBLE_NO_GRUT_MOTIVATION"

    def test_entropy_revision_ratio(self):
        era = build_entropy_revision_analysis()
        assert abs(era.S_required_over_S_current - 1.0 / R_GAP) < 1e-14

    def test_entropy_revision_r_eff(self):
        era = build_entropy_revision_analysis()
        assert abs(era.R_eff_over_R_eq - 1.0 / math.sqrt(R_GAP)) < 1e-14

    def test_entropy_revision_no_grut_motivation(self):
        era = build_entropy_revision_analysis()
        assert era.grut_native_motivation is False

    def test_entropy_revision_same_mass_scaling(self):
        era = build_entropy_revision_analysis()
        assert "M^2" in era.S_current_mass_scaling
        assert "M^2" in era.S_required_mass_scaling

    def test_entropy_revision_no_scaling_change(self):
        era = build_entropy_revision_analysis()
        assert era.mass_scaling_change_needed is False

    def test_temperature_revision_verdict(self):
        tra = build_temperature_revision_analysis()
        assert tra.verdict == "VIABLE_NO_NEW_GRUT_STRUCTURE"

    def test_temperature_revision_ratio(self):
        tra = build_temperature_revision_analysis()
        assert abs(tra.T_1stlaw_over_T_diss - 1.0 / R_GAP) < 1e-14

    def test_temperature_revision_not_grut_native(self):
        tra = build_temperature_revision_analysis()
        assert tra.T_1stlaw_grut_native is False

    def test_gap_structure_R_gap(self):
        gs = build_gap_structure()
        assert abs(gs.R_gap - R_GAP) < 1e-14

    def test_gap_structure_depends_on_Q(self):
        gs = build_gap_structure()
        assert any("Q" in dep for dep in gs.R_gap_depends_on)

    def test_gap_structure_M_independent(self):
        gs = build_gap_structure()
        assert any("Mass" in ind for ind in gs.R_gap_independent_of)


# ================================================================
# TestMasterAudit
# ================================================================

class TestMasterAudit:
    """run_first_law_gap_audit() executive determination and structure."""

    @pytest.fixture(scope="class")
    def result(self):
        return run_first_law_gap_audit()

    def test_valid(self, result):
        assert result.valid is True

    def test_executive_determination(self, result):
        assert result.executive_determination == "gap_structural_no_external_free_parameter"

    def test_option_c_closed(self, result):
        assert result.option_c_work.verdict == "CLOSED"

    def test_option_a_structurally_possible(self, result):
        assert "STRUCTURALLY_POSSIBLE" in result.option_a_entropy.verdict

    def test_option_b_viable(self, result):
        assert "VIABLE" in result.option_b_temperature.verdict

    def test_R_gap_correct(self, result):
        assert abs(result.R_gap - R_GAP) < 1e-14

    def test_R_gap_mass_independent(self, result):
        assert result.R_gap_mass_independent is True

    def test_safe_claims_non_empty(self, result):
        assert len(result.safe_claims) >= 4

    def test_unsafe_claims_non_empty(self, result):
        assert len(result.unsafe_claims) >= 2

    def test_nonclaims_non_empty(self, result):
        assert len(result.nonclaims) >= 3

    def test_safe_claim_V_Q(self, result):
        """Safe claims include V_Q = -c²/2."""
        combined = " ".join(result.safe_claims)
        assert "V_Q" in combined or "barrier" in combined.lower()

    def test_safe_claim_barrier_zero_work(self, result):
        combined = " ".join(result.safe_claims)
        assert "zero" in combined.lower() or "0" in combined

    def test_safe_claim_option_c_eliminated(self, result):
        combined = " ".join(result.safe_claims)
        assert "eliminated" in combined.lower() or "(c)" in combined

    def test_inherited_appendix_d(self, result):
        assert result.appendix_d_classification == "thermodynamic_sector_partially_consistent"

    def test_inherited_appendix_e(self, result):
        assert result.appendix_e_classification == "locally_consistent_globally_underdetermined"

    def test_inherited_appendix_h(self, result):
        assert result.appendix_h_classification == "temperature_selectable_conditionally_not_uniquely"

    def test_different_mass_same_exec(self):
        result1 = run_first_law_gap_audit(10.0 * M_SUN_KG)
        result2 = run_first_law_gap_audit(100.0 * M_SUN_KG)
        assert result1.executive_determination == result2.executive_determination

    def test_different_mass_same_R_gap(self):
        result1 = run_first_law_gap_audit(10.0 * M_SUN_KG)
        result2 = run_first_law_gap_audit(100.0 * M_SUN_KG)
        assert abs(result1.R_gap - result2.R_gap) < 1e-14

    def test_option_c_V_Q_mass_independent(self):
        r1 = run_first_law_gap_audit(10.0 * M_SUN_KG)
        r2 = run_first_law_gap_audit(1e6 * M_SUN_KG)
        assert abs(r1.option_c_work.V_Q_value_over_c_sq -
                   r2.option_c_work.V_Q_value_over_c_sq) < 1e-10

    def test_no_nonclaim_about_closing_gap(self, result):
        combined = " ".join(result.nonclaims)
        assert "does NOT close" in combined

    def test_determination_explains_all_three(self, result):
        exp = result.determination_explanation
        assert "CLOSED" in exp
        assert "STRUCTURALLY_POSSIBLE" in exp or "entropy" in exp.lower()
        assert "VIABLE" in exp or "T_1stlaw" in exp


# ================================================================
# TestForbiddenClaimGuards
# ================================================================

class TestForbiddenClaimGuards:
    """assert_no_unsupported_claims raises on every forbidden string."""

    def _check_forbidden(self, forbidden_str):
        result = FirstLawGapResult(
            executive_determination=forbidden_str,
            valid=True,
        )
        with pytest.raises(AssertionError):
            result.assert_no_unsupported_claims()

    def test_gap_closed_raises(self):
        self._check_forbidden("gap_closed")

    def test_first_law_proven_raises(self):
        self._check_forbidden("first_law_proven")

    def test_work_term_found_raises(self):
        self._check_forbidden("work_term_found")

    def test_entropy_derived_raises(self):
        self._check_forbidden("entropy_derived")

    def test_temperature_proven_raises(self):
        self._check_forbidden("temperature_proven")

    def test_appendix_c_resolved_raises(self):
        self._check_forbidden("appendix_c_resolved")

    def test_safe_exec_does_not_raise(self):
        result = run_first_law_gap_audit()
        # Should not raise
        result.assert_no_unsupported_claims()

    def test_all_forbidden_in_set(self):
        for f in _FORBIDDEN_CLASSIFICATIONS:
            self._check_forbidden(f)


# ================================================================
# TestInheritedClassifications
# ================================================================

class TestInheritedClassifications:
    """Appendix D, E, H classifications must not change."""

    def test_appendix_d_exact(self):
        result = run_first_law_gap_audit()
        assert result.appendix_d_classification == "thermodynamic_sector_partially_consistent"

    def test_appendix_e_exact(self):
        result = run_first_law_gap_audit()
        assert result.appendix_e_classification == "locally_consistent_globally_underdetermined"

    def test_appendix_h_exact(self):
        result = run_first_law_gap_audit()
        assert result.appendix_h_classification == "temperature_selectable_conditionally_not_uniquely"

    def test_all_three_distinct(self):
        result = run_first_law_gap_audit()
        classifications = {
            result.appendix_d_classification,
            result.appendix_e_classification,
            result.appendix_h_classification,
        }
        assert len(classifications) == 3   # all distinct

    def test_none_contain_gap_closed(self):
        result = run_first_law_gap_audit()
        for cls in [
            result.appendix_d_classification,
            result.appendix_e_classification,
            result.appendix_h_classification,
        ]:
            assert "gap_closed" not in cls


# ================================================================
# TestSummaryString
# ================================================================

class TestSummaryString:
    """summary_string runs without error and contains key tokens."""

    @pytest.fixture(scope="class")
    def s(self):
        result = run_first_law_gap_audit()
        return summary_string(result)

    def test_runs(self, s):
        assert isinstance(s, str)
        assert len(s) > 100

    def test_contains_R_gap_value(self, s):
        assert "1.20" in s

    def test_contains_option_c_verdict(self, s):
        assert "CLOSED" in s

    def test_contains_option_a_verdict(self, s):
        assert "STRUCTURALLY_POSSIBLE" in s or "entropy" in s.lower()

    def test_contains_option_b_verdict(self, s):
        assert "VIABLE" in s

    def test_contains_executive(self, s):
        assert "gap_structural" in s

    def test_contains_V_Q_value(self, s):
        assert "-0.5" in s

    def test_contains_appendix_d(self, s):
        assert "thermodynamic_sector_partially_consistent" in s

    def test_contains_appendix_e(self, s):
        assert "locally_consistent_globally_underdetermined" in s

    def test_contains_appendix_h(self, s):
        assert "temperature_selectable_conditionally_not_uniquely" in s

    def test_alpha_vac_shown(self, s):
        """Summary shows α_vac needed for R=1 vs current."""
        assert "0.276" in s or "0.27" in s

    def test_contains_T_1stlaw_ratio(self, s):
        assert "0.82" in s or "1/R" in s

    def test_contains_S_ratio(self, s):
        assert "0.82" in s or "1/R" in s


# ================================================================
# TestCrossConsistency
# ================================================================

class TestCrossConsistency:
    """Consistency relations across the audit."""

    def test_R_gap_equals_T_diss_over_T_1stlaw(self):
        """R_GAP = T_diss/T_1stlaw = 1/(T_1stlaw/T_diss)."""
        t_ratio = compute_T_1stlaw_over_T_diss()  # = 1/R
        assert abs(1.0 / t_ratio - R_GAP) < 1e-14

    def test_R_gap_equals_S_eq_over_S_correct(self):
        """R_GAP = S_eq/S_correct = 1/(S_correct/S_eq)."""
        s_ratio = compute_required_entropy_ratio()  # = 1/R
        assert abs(1.0 / s_ratio - R_GAP) < 1e-14

    def test_T_ratio_S_ratio_equal(self):
        """T_1stlaw/T_diss == S_correct/S_eq."""
        t_ratio = compute_T_1stlaw_over_T_diss()
        s_ratio = compute_required_entropy_ratio()
        assert abs(t_ratio - s_ratio) < 1e-14

    def test_V_Q_proof_consistency(self):
        """
        Algebraic proof: ε_Q · (r_s/R_eq)^β_Q = 1 at equilibrium.
        This is the key step that makes V_Q M-independent.
        """
        # ε_Q = (1/3)^2, R_eq = r_s/3  → r_s/R_eq = 3
        factor = EPSILON_Q * (1.0 / R_EQ_OVER_RS) ** BETA_Q
        assert abs(factor - 1.0) < 1e-14

    def test_R_gap_independent_of_M(self):
        """Numeric cross-check: T_diss·dS/dM/c² does not vary with M."""
        def compute_R_numeric(M_kg):
            r_s = 2.0 * G_SI * M_kg / C_SI ** 2
            R_eq = r_s * R_EQ_OVER_RS
            omega_0 = math.sqrt(BETA_Q * G_SI * M_kg / R_eq ** 3)
            T_diss = HBAR_SI * omega_0 / (Q_CANONICAL * K_B)
            dS_dM = 8.0 * math.pi * G_SI ** 2 * M_kg / (
                9.0 * C_SI ** 4 * L_PLANCK ** 2
            )
            return K_B * T_diss * dS_dM / C_SI ** 2

        R1 = compute_R_numeric(10.0 * M_SUN_KG)
        R2 = compute_R_numeric(30.0 * M_SUN_KG)
        R3 = compute_R_numeric(100.0 * M_SUN_KG)

        assert abs(R1 - R_GAP) < 1e-10
        assert abs(R2 - R_GAP) < 1e-10
        assert abs(R3 - R_GAP) < 1e-10
        assert abs(R1 - R2) < 1e-10
        assert abs(R2 - R3) < 1e-10

    def test_gap_formula_parametric(self):
        """R = 4π√3/(3Q) = 4π√3/(3*β_Q/α_vac)."""
        Q = BETA_Q / ALPHA_VAC
        R_check = 4.0 * math.pi * math.sqrt(3.0) / (3.0 * Q)
        assert abs(R_check - R_GAP) < 1e-14

    def test_exact_ratio_agrees_with_numerical_multiple_masses(self):
        v_exact = compute_V_Q_exact_ratio()
        for M_solar in [5.0, 50.0, 500.0, 5000.0]:
            M_kg = M_solar * M_SUN_KG
            v_num = compute_barrier_potential_at_Req(M_kg)
            assert abs(v_num - v_exact) < 1e-10
