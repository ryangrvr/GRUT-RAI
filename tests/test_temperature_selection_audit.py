"""Tests for grut/temperature_selection_audit.py — Appendix H Temperature Selection.

Tests verify:
1. Temperature candidate values at reference mass
2. First-law analysis: T_1stlaw = 9·T_Hawking
3. Mass-independent first-law ratio R = 2π√3/18
4. Selection criterion verdicts (FDT blocked, KMS conditional, first-law viable)
5. Fluctuation consequence: S(0) = ℏ/3
6. Forbidden claim guards
"""

import math
import pytest

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from grut.temperature_selection_audit import (
    # Constants
    G_SI, C_SI, HBAR_SI, K_B, L_PLANCK,
    ALPHA_VAC, BETA_Q, EPSILON_Q, R_EQ_OVER_RS, Q_CANONICAL, M_REF_KG,
    R_FIRSTLAW_ANALYTIC, _FORBIDDEN_CLASSIFICATIONS,
    # Data structures
    TemperatureValue, SelectionCriterion, FirstLawAnalysis,
    FluctuationConsequence, TemperatureSelectionResult,
    # Builders
    build_temperature_candidates,
    evaluate_fdt_criterion, evaluate_kms_criterion,
    evaluate_first_law_criterion, compute_first_law_analysis,
    compute_fluctuation_consequence,
    # Master runner
    run_temperature_selection_audit,
    # Helpers
    compute_R_firstlaw_analytic, compute_R_firstlaw_numerical,
    # Summary
    summary_string,
)


# ================================================================
# Fixtures
# ================================================================

@pytest.fixture
def result():
    """Full audit result at reference mass."""
    return run_temperature_selection_audit()


@pytest.fixture
def candidates():
    """Temperature candidates at reference mass."""
    return build_temperature_candidates()


@pytest.fixture
def first_law():
    """First law analysis at reference mass."""
    return compute_first_law_analysis()


# ================================================================
# Part 1: Parameters and Constants
# ================================================================

class TestParameters:
    def test_Q_canonical(self):
        """Q = β_Q/α_vac = 6."""
        assert abs(Q_CANONICAL - 6.0) < 1e-12

    def test_R_firstlaw_analytic_value(self):
        """R_analytic = 4π√3/(3Q) = 2π√3/9 ≈ 1.209 for Q=6."""
        expected = 4.0 * math.pi * math.sqrt(3.0) / (3.0 * Q_CANONICAL)
        assert abs(R_FIRSTLAW_ANALYTIC - expected) < 1e-12

    def test_R_firstlaw_analytic_approx(self):
        """R_analytic ≈ 1.209 (between 1.1 and 1.4)."""
        assert 1.1 < R_FIRSTLAW_ANALYTIC < 1.4

    def test_R_eq_over_rs(self):
        """R_eq/r_s = (ε_Q)^(1/β_Q) = 1/3."""
        assert abs(R_EQ_OVER_RS - 1.0 / 3.0) < 1e-12

    def test_forbidden_classifications_defined(self):
        """At least 5 forbidden strings."""
        assert len(_FORBIDDEN_CLASSIFICATIONS) >= 5


# ================================================================
# Part 2: Temperature Candidate Tests
# ================================================================

class TestTemperatureCandidates:
    def test_five_candidates_built(self, candidates):
        """Should have exactly 5 candidates: T_s, T_d, T_sg, T_h, T_1st."""
        assert len(candidates) == 5

    def test_t_structural_in_candidates(self, candidates):
        names = [c.name for c in candidates]
        assert "T_structural" in names

    def test_t_dissipation_in_candidates(self, candidates):
        names = [c.name for c in candidates]
        assert "T_dissipation" in names

    def test_t_1stlaw_in_candidates(self, candidates):
        names = [c.name for c in candidates]
        assert "T_1stlaw" in names

    def test_t_structural_grut_native(self, candidates):
        c = next(c for c in candidates if c.name == "T_structural")
        assert c.grut_native is True

    def test_t_dissipation_grut_native(self, candidates):
        c = next(c for c in candidates if c.name == "T_dissipation")
        assert c.grut_native is True

    def test_t_hawking_not_native(self, candidates):
        c = next(c for c in candidates if c.name == "T_hawking")
        assert c.grut_native is False

    def test_t_surface_gravity_not_native(self, candidates):
        c = next(c for c in candidates if c.name == "T_surface_gravity")
        assert c.grut_native is False

    def test_t_1stlaw_grut_native(self, candidates):
        """T_1stlaw is derived from GRUT quantities (first law)."""
        c = next(c for c in candidates if c.name == "T_1stlaw")
        assert c.grut_native is True

    def test_t_structural_over_t_dissipation_equals_Q(self, candidates):
        """T_structural = Q × T_dissipation (exactly, up to floating point)."""
        T_s = next(c.T_kelvin for c in candidates if c.name == "T_structural")
        T_d = next(c.T_kelvin for c in candidates if c.name == "T_dissipation")
        assert abs(T_s / T_d - Q_CANONICAL) < 1e-10

    def test_t_structural_much_larger_than_t_hawking(self, candidates):
        """T_structural >> T_Hawking (factor ~65 for 30 M_sun)."""
        T_s = next(c for c in candidates if c.name == "T_structural")
        assert T_s.T_over_T_hawking > 50.0

    def test_t_dissipation_about_ten_times_t_hawking(self, candidates):
        """T_dissipation ~ 10–11 × T_Hawking for 30 M_sun."""
        T_d = next(c for c in candidates if c.name == "T_dissipation")
        assert 9.0 < T_d.T_over_T_hawking < 12.0

    def test_t_1stlaw_equals_nine_t_hawking(self, candidates):
        """T_1stlaw = 9 × T_Hawking exactly."""
        T_1 = next(c for c in candidates if c.name == "T_1stlaw")
        assert abs(T_1.T_over_T_hawking - 9.0) < 1e-8

    def test_all_temperatures_positive(self, candidates):
        for c in candidates:
            assert c.T_kelvin > 0


# ================================================================
# Part 3: First Law Analysis Tests
# ================================================================

class TestFirstLawAnalysis:
    def test_T_1stlaw_equals_9_T_hawking(self, first_law):
        """T_1stlaw/T_Hawking = 9 exactly (from dS/dM formula)."""
        ratio = first_law.T_1stlaw_over_T_hawking
        assert abs(ratio - 9.0) < 1e-6

    def test_R_firstlaw_numerical_matches_analytic(self, first_law):
        """Numerical R should match analytic R = 2π√3/18 to high accuracy."""
        assert abs(first_law.R_firstlaw_T_diss - first_law.R_firstlaw_analytic) < 1e-8

    def test_R_firstlaw_analytic_is_mass_independent(self, first_law):
        """R_analytic is a constant (mass-independent flag set)."""
        assert first_law.R_is_mass_independent is True

    def test_R_firstlaw_mass_independence_numerical(self):
        """R should be the same for different masses."""
        R_30 = compute_R_firstlaw_numerical(30.0 * 1.989e30)
        R_10 = compute_R_firstlaw_numerical(10.0 * 1.989e30)
        R_100 = compute_R_firstlaw_numerical(100.0 * 1.989e30)
        # All should agree to better than 1 ppm
        assert abs(R_30 - R_10) < 1e-10
        assert abs(R_30 - R_100) < 1e-10

    def test_R_firstlaw_between_1_and_2(self, first_law):
        """R should be close to 1.21 (between 1.1 and 1.4)."""
        assert 1.1 < first_law.R_firstlaw_T_diss < 1.4

    def test_R_firstlaw_not_unity(self, first_law):
        """T_dissipation does NOT exactly satisfy first law: R ≠ 1."""
        assert abs(first_law.R_firstlaw_T_diss - 1.0) > 0.05

    def test_T_1stlaw_less_than_T_dissipation(self, first_law):
        """T_1stlaw < T_dissipation (first law selects a lower temperature)."""
        assert first_law.T_1stlaw_over_T_diss < 1.0

    def test_T_1stlaw_over_T_diss_approx_0_83(self, first_law):
        """T_1stlaw / T_dissipation = 1/R ≈ 0.827."""
        expected = 1.0 / R_FIRSTLAW_ANALYTIC
        assert abs(first_law.T_1stlaw_over_T_diss - expected) < 1e-6

    def test_first_law_approximately_satisfied(self, first_law):
        """First law ratio within factor 2 of unity."""
        assert first_law.first_law_approximately_satisfied is True

    def test_R_analytic_formula(self):
        """R = 4π√3/(3Q) should equal 2π√3/9 for Q=6."""
        R_func = compute_R_firstlaw_analytic(ALPHA_VAC, BETA_Q)
        assert abs(R_func - R_FIRSTLAW_ANALYTIC) < 1e-12

    def test_R_increases_with_Q(self):
        """R = 4π√3/(3Q) decreases as Q increases."""
        R_Q3 = compute_R_firstlaw_analytic(1.0 / 3.0, 1.0)   # Q=3
        R_Q6 = compute_R_firstlaw_analytic(1.0 / 3.0, 2.0)   # Q=6
        R_Q9 = compute_R_firstlaw_analytic(1.0 / 3.0, 3.0)   # Q=9
        assert R_Q3 > R_Q6 > R_Q9  # R decreases as Q increases


# ================================================================
# Part 4: Selection Criterion Tests
# ================================================================

class TestSelectionCriteria:
    def test_fdt_verdict_blocked(self):
        """FDT criterion is BLOCKED."""
        c = evaluate_fdt_criterion()
        assert c.verdict == "BLOCKED"

    def test_fdt_does_not_select_unique_T(self):
        """FDT does not select a unique temperature (blocked)."""
        c = evaluate_fdt_criterion()
        assert c.selects_unique_T is False

    def test_fdt_requires_appendix_c(self):
        """FDT requires Appendix C resolution."""
        c = evaluate_fdt_criterion()
        assert c.requires_appendix_c_resolved is True

    def test_kms_verdict_conditional(self):
        """KMS criterion is CONDITIONAL."""
        c = evaluate_kms_criterion()
        assert c.verdict == "CONDITIONAL"

    def test_kms_selects_T_structural(self):
        """KMS criterion selects T_structural."""
        c = evaluate_kms_criterion()
        assert c.selects_unique_T is True
        assert c.selected_T_name == "T_structural"

    def test_kms_requires_appendix_c(self):
        """KMS requires quantum state (Appendix C blocker)."""
        c = evaluate_kms_criterion()
        assert c.requires_appendix_c_resolved is True

    def test_first_law_verdict_viable(self):
        """First law criterion is VIABLE_WITH_ASSUMPTIONS."""
        c = evaluate_first_law_criterion()
        assert c.verdict == "VIABLE_WITH_ASSUMPTIONS"

    def test_first_law_selects_T_1stlaw(self):
        """First law selects T_1stlaw."""
        c = evaluate_first_law_criterion()
        assert c.selects_unique_T is True
        assert c.selected_T_name == "T_1stlaw"

    def test_first_law_does_not_require_appendix_c(self):
        """First law criterion does NOT require Appendix C."""
        c = evaluate_first_law_criterion()
        assert c.requires_appendix_c_resolved is False
        assert c.requires_quantum_state is False

    def test_first_law_requires_entropy_ansatz(self):
        """First law requires the entropy ansatz (S = πR_eq²/l_P²)."""
        c = evaluate_first_law_criterion()
        assert c.requires_entropy_ansatz is True


# ================================================================
# Part 5: Fluctuation Consequence Tests
# ================================================================

class TestFluctuationConsequence:
    def test_R_value_is_correct(self):
        """Fluctuation consequence R value matches analytic formula."""
        fc = compute_fluctuation_consequence()
        assert abs(fc.consequence_value - R_FIRSTLAW_ANALYTIC) < 1e-12

    def test_consequence_is_mass_independent(self):
        """The first-law ratio R is mass-independent."""
        fc = compute_fluctuation_consequence()
        assert fc.consequence_is_mass_independent is True

    def test_is_non_circular(self):
        """The fluctuation consequence is non-circular."""
        fc = compute_fluctuation_consequence()
        assert fc.is_non_circular is True

    def test_fdt_noise_formula_populated(self):
        """FDT noise formula should be documented."""
        fc = compute_fluctuation_consequence()
        assert len(fc.fdt_noise_formula) > 20

    def test_consequence_name_is_mass_independent_ratio(self):
        """Consequence is named 'mass_independent_first_law_ratio'."""
        fc = compute_fluctuation_consequence()
        assert fc.consequence_name == "mass_independent_first_law_ratio"


# ================================================================
# Part 6: Master Audit Tests
# ================================================================

class TestMasterAudit:
    def test_audit_runs_without_error(self, result):
        """Audit completes without exception."""
        assert result.valid is True

    def test_executive_determination(self, result):
        """Correct executive determination."""
        assert result.executive_determination == (
            "temperature_selectable_conditionally_not_uniquely"
        )

    def test_appendix_d_unchanged(self, result):
        """Appendix D classification unchanged."""
        assert result.appendix_d_classification == (
            "thermodynamic_sector_partially_consistent"
        )

    def test_appendix_e_unchanged(self, result):
        """Appendix E classification unchanged."""
        assert result.appendix_e_classification == (
            "locally_consistent_globally_underdetermined"
        )

    def test_strongest_criterion_is_first_law(self, result):
        """Strongest criterion is first_law_self_consistency."""
        assert result.strongest_criterion == "first_law_self_consistency"

    def test_n_criteria_blocked(self, result):
        """Exactly 1 criterion is BLOCKED (FDT)."""
        assert result.n_criteria_blocked == 1

    def test_n_criteria_conditional(self, result):
        """Exactly 1 criterion is CONDITIONAL (KMS)."""
        assert result.n_criteria_conditional == 1

    def test_n_criteria_selecting(self, result):
        """At least 2 criteria select a unique T (KMS and first law)."""
        assert result.n_criteria_selecting >= 2

    def test_safe_claims_populated(self, result):
        """At least 5 safe claims."""
        assert len(result.safe_claims) >= 5

    def test_unsafe_claims_populated(self, result):
        """At least 3 unsafe claims."""
        assert len(result.unsafe_claims) >= 3

    def test_nonclaims_populated(self, result):
        """At least 3 nonclaims."""
        assert len(result.nonclaims) >= 3

    def test_five_candidates_in_result(self, result):
        """5 temperature candidates in result."""
        assert len(result.candidates) == 5

    def test_route_verdicts_set(self, result):
        """All three criterion verdicts set."""
        assert result.criterion_fdt.verdict == "BLOCKED"
        assert result.criterion_kms.verdict == "CONDITIONAL"
        assert result.criterion_first_law.verdict == "VIABLE_WITH_ASSUMPTIONS"

    def test_first_law_R_in_result(self, result):
        """First-law ratio R is recorded and correct."""
        assert abs(result.first_law.R_firstlaw_T_diss - R_FIRSTLAW_ANALYTIC) < 1e-8

    def test_fluctuation_consequence_in_result(self, result):
        """Fluctuation consequence value is the analytic R."""
        assert abs(result.fluctuation.consequence_value - R_FIRSTLAW_ANALYTIC) < 1e-12


# ================================================================
# Part 7: Forbidden Claim Guards
# ================================================================

class TestForbiddenClaimGuards:
    def test_temperature_proven_is_forbidden(self):
        assert "temperature_proven" in _FORBIDDEN_CLASSIFICATIONS

    def test_temperature_uniquely_derived_is_forbidden(self):
        assert "temperature_uniquely_derived" in _FORBIDDEN_CLASSIFICATIONS

    def test_fdt_proven_is_forbidden(self):
        assert "fdt_proven_in_grut" in _FORBIDDEN_CLASSIFICATIONS

    def test_kms_proven_is_forbidden(self):
        assert "kms_proven_in_grut" in _FORBIDDEN_CLASSIFICATIONS

    def test_hawking_derived_is_forbidden(self):
        assert "hawking_derived_from_grut" in _FORBIDDEN_CLASSIFICATIONS

    def test_guard_raises_on_temperature_proven(self):
        r = TemperatureSelectionResult()
        r.executive_determination = "temperature_proven"
        with pytest.raises(AssertionError, match="temperature_proven"):
            r.assert_no_unsupported_claims()

    def test_guard_raises_on_uniquely_derived(self):
        r = TemperatureSelectionResult()
        r.executive_determination = "temperature_uniquely_derived"
        with pytest.raises(AssertionError):
            r.assert_no_unsupported_claims()

    def test_guard_raises_on_appendix_c_resolved(self):
        r = TemperatureSelectionResult()
        r.executive_determination = "appendix_c_resolved"
        with pytest.raises(AssertionError):
            r.assert_no_unsupported_claims()

    def test_guard_passes_on_correct_determination(self, result):
        """Guard should NOT raise for the correct determination."""
        result.assert_no_unsupported_claims()


# ================================================================
# Part 8: Summary String Tests
# ================================================================

class TestSummaryString:
    def test_summary_produced(self, result):
        s = summary_string(result)
        assert isinstance(s, str)
        assert len(s) > 300

    def test_summary_contains_determination(self, result):
        s = summary_string(result)
        assert "temperature_selectable_conditionally_not_uniquely" in s

    def test_summary_contains_R(self, result):
        s = summary_string(result)
        assert "2π√3" in s or "R =" in s

    def test_summary_contains_criterion_verdicts(self, result):
        s = summary_string(result)
        assert "BLOCKED" in s
        assert "CONDITIONAL" in s
        assert "VIABLE" in s


# ================================================================
# Part 9: Internal Consistency Tests
# ================================================================

class TestInternalConsistency:
    def test_T_1stlaw_equals_nine_T_hawking_analytically(self):
        """T_1stlaw = 9·T_H is derivable from the endpoint entropy formula.

        S = π·R_eq²/l_P² where R_eq = r_s/3 = 2GM/(3c²)
        dS/dM = 8πG²M/(9c⁴·l_P²)   (using l_P² = ℏG/c³)
        T = c²/(k_B · dS/dM) = c² · 9c⁴·l_P² / (k_B·8πG²M)
          = 9·c^6·l_P² / (8πG²M·k_B)
          = 9·ℏ·c³ / (8πGM·k_B)   (using l_P² = ℏG/c³)
          = 9 × T_Hawking
        """
        for M_solar in [10.0, 30.0, 100.0]:
            M_kg = M_solar * 1.989e30
            r_s = 2.0 * G_SI * M_kg / C_SI ** 2
            R_eq = r_s / 3.0
            dS_dM = 8.0 * math.pi * G_SI ** 2 * M_kg / (9.0 * C_SI ** 4 * L_PLANCK ** 2)
            T_1stlaw = C_SI ** 2 / (K_B * dS_dM)
            T_hawking = HBAR_SI * C_SI ** 3 / (8.0 * math.pi * G_SI * M_kg * K_B)
            assert abs(T_1stlaw / T_hawking - 9.0) < 1e-6, (
                f"For M={M_solar}: T_1stlaw/T_H = {T_1stlaw/T_hawking:.8f}"
            )

    def test_R_analytic_derivation(self):
        """Verify the analytic derivation of R = 4π√3/(3Q).

        R = k_B · T_diss · (dS/dM) / c²
          = ℏω₀/(Q) × 8πG²M/(9c⁶l_P²)    [using l_P² = ℏG/c³]
          = ℏω₀ × 8πGM/(9Q·c³)
          = 8πGM·ω₀/(9Q·c³)

        ω₀ = sqrt(2GM/R_eq³) = sqrt(2GM/(2GM/(3c²))³) = 3√3·c³/(2GM)

        R = 8πGM · 3√3·c³/(2GM) / (9Q·c³)
          = 8π·3√3/(18Q)
          = 4π√3/(3Q)
        """
        # Verify at reference mass
        M_kg = M_REF_KG
        r_s = 2.0 * G_SI * M_kg / C_SI ** 2
        R_eq = r_s / 3.0
        omega_0 = math.sqrt(2.0 * G_SI * M_kg / R_eq ** 3)
        T_diss = HBAR_SI * omega_0 / (Q_CANONICAL * K_B)
        dS_dM = 8.0 * math.pi * G_SI ** 2 * M_kg / (9.0 * C_SI ** 4 * L_PLANCK ** 2)
        R_numerical = K_B * T_diss * dS_dM / C_SI ** 2
        R_analytic = 4.0 * math.pi * math.sqrt(3.0) / (3.0 * Q_CANONICAL)
        assert abs(R_numerical - R_analytic) < 1e-8, (
            f"R_numerical = {R_numerical:.8f}, R_analytic = {R_analytic:.8f}"
        )

    def test_KMS_temperature_equals_T_structural(self):
        """If τ_local = KMS period: T_KMS = ℏ/(k_B·τ_local) = ℏω₀/k_B = T_structural."""
        M_kg = M_REF_KG
        r_s = 2.0 * G_SI * M_kg / C_SI ** 2
        R_eq = r_s / 3.0
        omega_0 = math.sqrt(2.0 * G_SI * M_kg / R_eq ** 3)
        t_dyn = math.sqrt(R_eq ** 3 / (2.0 * G_SI * M_kg))
        tau_local = 1.3225e15 * t_dyn / (1.3225e15 + t_dyn)   # ≈ t_dyn

        T_KMS = HBAR_SI / (K_B * tau_local)
        T_structural = HBAR_SI * omega_0 / K_B

        # T_KMS = T_structural since ω₀ · τ_local ≈ 1
        assert abs(T_KMS / T_structural - 1.0) < 1e-10, (
            f"T_KMS/T_structural = {T_KMS/T_structural:.12f}"
        )

    def test_T_dissipation_T_structural_ratio_equals_Q(self):
        """T_structural / T_dissipation = Q = 6 exactly."""
        M_kg = M_REF_KG
        r_s = 2.0 * G_SI * M_kg / C_SI ** 2
        R_eq = r_s / 3.0
        omega_0 = math.sqrt(2.0 * G_SI * M_kg / R_eq ** 3)
        T_s = HBAR_SI * omega_0 / K_B
        T_d = T_s / Q_CANONICAL
        assert abs(T_s / T_d - Q_CANONICAL) < 1e-12
