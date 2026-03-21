"""Tests for Phase VII — Testing EOS / Potential Closure from beta_Q.

~120 tests across 15 classes covering all dataclasses, builders,
public API, master analysis, nonclaims, and serialization.
"""

from __future__ import annotations

import json
import math
import pytest

from grut.barrier_eos_potential import (
    # Constants
    ALPHA_VAC,
    BETA_Q,
    EPSILON_Q,
    R_EQ_OVER_R_S,
    C_ENDPOINT,
    LEVEL_EXACT,
    LEVEL_CONSTITUTIVE_DERIVED,
    LEVEL_CONSTITUTIVE_LAPSE_PROMOTION_OBSTRUCTED,
    ROUTE_A,
    ROUTE_B,
    ROUTE_C,
    ROUTE_D,
    TPHI_STATUS_PHASE_VI,
    TPHI_STATUS_PHASE_VII,
    SCOPE_STATEMENT,
    # Enum
    ClosureClassification,
    # Dataclasses
    EOSAdmissibilityTest,
    ConditionalMappingStep,
    ConditionalMappingSequence,
    AnisotropyAnalysis,
    CandidateScalarPotential,
    DegeneracyReductionAssessment,
    NECCompatibilityCheck,
    LapseImpactAssessment,
    Phase6Reconfirmation,
    StatusLadderUpdate,
    EOSPotentialResult,
    # Builders
    build_eos_admissibility_test,
    build_conditional_mapping_sequence,
    build_anisotropy_analysis,
    build_candidate_scalar_potential,
    build_degeneracy_reduction_assessment,
    build_nec_compatibility_check,
    build_lapse_impact_assessment,
    build_phase6_reconfirmation,
    build_status_ladder_update,
    # Public API
    test_eos_admissibility_from_beta,
    assess_conditional_eos_from_beta,
    assess_degeneracy_reduction,
    assess_lapse_impact,
    # Master
    compute_eos_potential_analysis,
    # Serialization
    eos_potential_result_to_dict,
)


# ================================================================
# Module-scoped fixtures
# ================================================================

@pytest.fixture(scope="module")
def eos_admissibility():
    return build_eos_admissibility_test()


@pytest.fixture(scope="module")
def conditional_sequence():
    return build_conditional_mapping_sequence()


@pytest.fixture(scope="module")
def anisotropy():
    return build_anisotropy_analysis()


@pytest.fixture(scope="module")
def candidate_potential():
    return build_candidate_scalar_potential()


@pytest.fixture(scope="module")
def degeneracy():
    return build_degeneracy_reduction_assessment()


@pytest.fixture(scope="module")
def nec_check():
    return build_nec_compatibility_check()


@pytest.fixture(scope="module")
def lapse_impact():
    return build_lapse_impact_assessment()


@pytest.fixture(scope="module")
def phase6_reconfirm():
    return build_phase6_reconfirmation()


@pytest.fixture(scope="module")
def status_ladder():
    return build_status_ladder_update()


@pytest.fixture(scope="module")
def master_result():
    return compute_eos_potential_analysis()


# ================================================================
# 1. TestConstants (~8 tests)
# ================================================================

class TestConstants:
    """Verify constant parity with canonical values."""

    def test_alpha_vac(self):
        assert abs(ALPHA_VAC - 1.0 / 3.0) < 1e-15

    def test_beta_q(self):
        assert abs(BETA_Q - 2.0) < 1e-15

    def test_epsilon_q(self):
        assert abs(EPSILON_Q - ALPHA_VAC ** 2) < 1e-15

    def test_r_eq_over_r_s(self):
        assert abs(R_EQ_OVER_R_S - ALPHA_VAC) < 1e-15

    def test_c_endpoint(self):
        assert abs(C_ENDPOINT - 1.0 / R_EQ_OVER_R_S) < 1e-15

    def test_scope_statement_nonempty(self):
        assert len(SCOPE_STATEMENT) > 50

    def test_closure_enum_has_six_values(self):
        assert len(ClosureClassification) == 6

    def test_closure_enum_values(self):
        expected = {
            "not_admissible",
            "admissible_but_nonunique",
            "partially_closing",
            "fully_closing",
            "incompatible_with_phase_v",
            "unresolved",
        }
        actual = {c.value for c in ClosureClassification}
        assert actual == expected


# ================================================================
# 2. TestEOSAdmissibility (~10 tests)
# ================================================================

class TestEOSAdmissibility:
    """Test that beta_Q is assessed as NOT an EOS exponent."""

    def test_beta_q_not_eos_exponent(self, eos_admissibility):
        assert eos_admissibility.beta_Q_is_eos_exponent is False

    def test_beta_q_is_stiffness_exponent(self, eos_admissibility):
        assert eos_admissibility.beta_Q_is_stiffness_exponent is True

    def test_requires_isotropy(self, eos_admissibility):
        assert eos_admissibility.requires_isotropy is True

    def test_requires_perfect_fluid(self, eos_admissibility):
        assert eos_admissibility.requires_perfect_fluid is True

    def test_collapse_anisotropic(self, eos_admissibility):
        assert eos_admissibility.anisotropy_required_for_collapse is True

    def test_single_w_insufficient(self, eos_admissibility):
        assert eos_admissibility.single_w_sufficient is False

    def test_single_w_sufficient_for_cosmo(self, eos_admissibility):
        assert eos_admissibility.single_w_sufficient_for_cosmo is True

    def test_conditional_mapping_exists(self, eos_admissibility):
        assert eos_admissibility.conditional_mapping_exists is True

    def test_omega_0_sq_exact(self, eos_admissibility):
        assert eos_admissibility.omega_0_sq_exact is True

    def test_assumptions_at_least_4(self, eos_admissibility):
        assert len(eos_admissibility.assumptions_for_mapping) >= 4

    def test_classification_admissible_but_nonunique(self, eos_admissibility):
        assert (
            eos_admissibility.classification
            == ClosureClassification.ADMISSIBLE_BUT_NONUNIQUE.value
        )


# ================================================================
# 3. TestConditionalSequence (~12 tests)
# ================================================================

class TestConditionalSequence:
    """Test the beta_Q -> omega_0 -> m^2 -> V -> w mapping-and-block."""

    def test_five_steps(self, conditional_sequence):
        assert conditional_sequence.n_steps == 5
        assert len(conditional_sequence.steps) == 5

    def test_two_exact_observations(self, conditional_sequence):
        assert conditional_sequence.n_exact_observations == 2

    def test_three_conditional_forward(self, conditional_sequence):
        assert conditional_sequence.n_conditional_forward == 3

    def test_step_1_exact_and_not_route_specific(self, conditional_sequence):
        s1 = conditional_sequence.steps[0]
        assert s1.step_number == 1
        assert s1.is_exact is True
        assert s1.is_route_specific is False
        assert s1.is_terminal_block is False

    def test_step_2_conditional_route_a(self, conditional_sequence):
        s2 = conditional_sequence.steps[1]
        assert s2.step_number == 2
        assert s2.is_exact is False
        assert s2.is_route_specific is True
        assert s2.route_if_specific == ROUTE_A

    def test_step_3_conditional_route_a(self, conditional_sequence):
        s3 = conditional_sequence.steps[2]
        assert s3.step_number == 3
        assert s3.is_exact is False
        assert s3.is_route_specific is True

    def test_step_4_conditional(self, conditional_sequence):
        s4 = conditional_sequence.steps[3]
        assert s4.step_number == 4
        assert s4.is_exact is False
        assert s4.is_terminal_block is False

    def test_step_5_terminal_anisotropy_block(self, conditional_sequence):
        s5 = conditional_sequence.steps[4]
        assert s5.step_number == 5
        assert s5.is_exact is True
        assert s5.is_terminal_block is True

    def test_has_terminal_anisotropy_block(self, conditional_sequence):
        assert conditional_sequence.has_terminal_anisotropy_block is True

    def test_sequence_not_fully_exact(self, conditional_sequence):
        assert conditional_sequence.sequence_is_fully_exact is False

    def test_first_non_exact_step_is_2(self, conditional_sequence):
        assert conditional_sequence.first_non_exact_step == 2

    def test_conditionality_flags(self, conditional_sequence):
        assert conditional_sequence.is_conditional is True
        assert conditional_sequence.requires_route_a is True
        assert conditional_sequence.requires_isotropy is True
        assert conditional_sequence.valid_for_collapse is False
        assert conditional_sequence.unique is False


# ================================================================
# 4. TestAnisotropy (~8 tests)
# ================================================================

class TestAnisotropy:
    """Verify barrier sector anisotropy analysis."""

    def test_cosmo_isotropic(self, anisotropy):
        assert anisotropy.cosmo_sector_isotropic is True

    def test_cosmo_single_w_sufficient(self, anisotropy):
        assert anisotropy.cosmo_single_w_sufficient is True

    def test_collapse_anisotropic(self, anisotropy):
        assert anisotropy.collapse_sector_anisotropic is True

    def test_collapse_needs_wr_and_wperp(self, anisotropy):
        assert anisotropy.collapse_needs_wr_and_wperp is True

    def test_single_w_insufficient_for_collapse(self, anisotropy):
        assert anisotropy.single_w_insufficient_for_collapse is True

    def test_cosmo_tphi_form_mentions_perfect_fluid(self, anisotropy):
        assert "perfect fluid" in anisotropy.cosmo_tphi_form.lower() or \
               "isotropic" in anisotropy.cosmo_tphi_form.lower()

    def test_collapse_tphi_form_mentions_anisotropic(self, anisotropy):
        assert "anisotropic" in anisotropy.collapse_tphi_form.lower()

    def test_collapse_tphi_form_mentions_p_r_p_t(self, anisotropy):
        assert "p_r" in anisotropy.collapse_tphi_form


# ================================================================
# 5. TestCandidatePotential (~10 tests)
# ================================================================

class TestCandidatePotential:
    """Verify candidate V(Phi) = Phi^2 / (2 tau^2)."""

    def test_phi_squared_form(self, candidate_potential):
        assert "Phi^2" in candidate_potential.form

    def test_not_unique(self, candidate_potential):
        assert candidate_potential.is_unique is False

    def test_route_specific_a(self, candidate_potential):
        assert candidate_potential.is_route_specific is True
        assert candidate_potential.route == ROUTE_A

    def test_not_from_beta_q_alone(self, candidate_potential):
        assert candidate_potential.not_from_beta_Q_alone is True

    def test_additional_identifications_listed(self, candidate_potential):
        assert len(candidate_potential.additional_identifications) >= 3

    def test_free_functions_before_2(self, candidate_potential):
        assert candidate_potential.n_free_before == 2

    def test_free_functions_after_1(self, candidate_potential):
        assert candidate_potential.n_free_after == 1

    def test_w_at_equilibrium_minus_1(self, candidate_potential):
        assert abs(candidate_potential.w_at_equilibrium - (-1.0)) < 1e-15

    def test_w_at_equilibrium_scope_explicit(self, candidate_potential):
        scope = candidate_potential.w_at_equilibrium_scope
        assert "isotropic" in scope.lower()
        assert "Route A" in scope

    def test_rho_plus_p_zero(self, candidate_potential):
        assert abs(candidate_potential.rho_plus_p_at_equilibrium) < 1e-15


# ================================================================
# 6. TestOtherPotentials (~4 tests)
# ================================================================

class TestOtherPotentials:
    """Verify alternative V(Phi) forms are listed."""

    def test_at_least_3_alternatives(self, candidate_potential):
        assert len(candidate_potential.other_admissible_V_forms) >= 3

    def test_includes_phi4(self, candidate_potential):
        forms = candidate_potential.other_admissible_V_forms
        assert any("Phi^4" in f or "quartic" in f for f in forms)

    def test_nonclaims_mention_nonuniqueness(self, candidate_potential):
        assert any(
            "NOT unique" in n or "not unique" in n.lower()
            for n in candidate_potential.nonclaims
        )

    def test_includes_non_polynomial(self, candidate_potential):
        forms = candidate_potential.other_admissible_V_forms
        assert any("non-polynomial" in f.lower() or "exp" in f for f in forms)


# ================================================================
# 7. TestDegeneracyReduction (~10 tests)
# ================================================================

class TestDegeneracyReduction:
    """Verify degeneracy reduction assessment."""

    def test_reduces_route_a(self, degeneracy):
        assert degeneracy.reduces_route_a is True

    def test_does_not_reduce_route_b(self, degeneracy):
        assert degeneracy.reduces_route_b is False

    def test_does_not_reduce_route_c(self, degeneracy):
        assert degeneracy.reduces_route_c is False

    def test_not_fully_breaks(self, degeneracy):
        assert degeneracy.fully_breaks_degeneracy is False

    def test_source_degeneracy_not_broken(self, degeneracy):
        assert degeneracy.source_degeneracy_broken is False

    def test_classification_partially_closing(self, degeneracy):
        assert (
            degeneracy.closure_classification
            == ClosureClassification.PARTIALLY_CLOSING.value
        )

    def test_closure_enum(self, degeneracy):
        assert degeneracy.closure_enum == ClosureClassification.PARTIALLY_CLOSING

    def test_route_a_free_before_2(self, degeneracy):
        assert degeneracy.route_a_free_before == 2

    def test_route_a_free_after_1(self, degeneracy):
        assert degeneracy.route_a_free_after == 1

    def test_source_degeneracy_reason_nonempty(self, degeneracy):
        assert len(degeneracy.source_degeneracy_reason) > 20


# ================================================================
# 8. TestNECCompatibility (~8 tests)
# ================================================================

class TestNECCompatibility:
    """NEC check for isotropic Route A candidate closure."""

    def test_w_minus_1(self, nec_check):
        assert abs(nec_check.w_at_equilibrium - (-1.0)) < 1e-15

    def test_rho_plus_p_zero(self, nec_check):
        assert abs(nec_check.rho_plus_p_at_equilibrium) < 1e-15

    def test_nec_marginal(self, nec_check):
        assert nec_check.nec_marginal_at_equilibrium is True

    def test_no_conflict(self, nec_check):
        assert nec_check.no_conflict is True

    def test_candidate_compatible_with_nec(self, nec_check):
        assert nec_check.candidate_v_compatible_with_nec is True

    def test_phase_v_nec_is_constitutive(self, nec_check):
        assert nec_check.phase_v_nec_is_constitutive is True

    def test_scope_is_isotropic_route_a_only(self, nec_check):
        assert nec_check.scope_is_isotropic_route_a_only is True

    def test_not_full_collapse_nec_analysis(self, nec_check):
        assert nec_check.not_full_collapse_nec_analysis is True


# ================================================================
# 9. TestLapseImpact (~6 tests)
# ================================================================

class TestLapseImpact:
    """Lapse obstruction unchanged by EOS/potential closure."""

    def test_no_improvement(self, lapse_impact):
        assert lapse_impact.improves_lapse_determination is False

    def test_obstruction_not_lifted(self, lapse_impact):
        assert lapse_impact.obstruction_lifted is False

    def test_phase_v_obstruction_unchanged(self, lapse_impact):
        assert lapse_impact.phase_v_obstruction_unchanged is True

    def test_tphi_still_constitutive(self, lapse_impact):
        assert lapse_impact.tphi_still_constitutive is True

    def test_specific_v_does_not_resolve(self, lapse_impact):
        assert lapse_impact.specific_v_does_not_resolve_metric is True

    def test_reason_nonempty(self, lapse_impact):
        assert len(lapse_impact.reason_no_improvement) > 30


# ================================================================
# 10. TestPhase6Reconfirmation (~6 tests)
# ================================================================

class TestPhase6Reconfirmation:
    """All Phase VI results survive Phase VII."""

    def test_source_degeneracy_preserved(self, phase6_reconfirm):
        assert phase6_reconfirm.source_degeneracy_preserved is True

    def test_tphi_underdetermination_preserved(self, phase6_reconfirm):
        assert phase6_reconfirm.tphi_underdetermination_preserved is True

    def test_route_assessment_preserved(self, phase6_reconfirm):
        assert phase6_reconfirm.route_assessment_preserved is True

    def test_status_ladder_preserved(self, phase6_reconfirm):
        assert phase6_reconfirm.status_ladder_preserved is True

    def test_phase5_results_preserved(self, phase6_reconfirm):
        assert phase6_reconfirm.phase5_results_preserved is True

    def test_all_preserved(self, phase6_reconfirm):
        assert phase6_reconfirm.all_preserved is True


# ================================================================
# 11. TestStatusLadder (~8 tests)
# ================================================================

class TestStatusLadder:
    """Status ladder: all levels unchanged."""

    def test_level_1_unchanged(self, status_ladder):
        assert status_ladder.level_1_changed is False
        assert status_ladder.level_1_before == LEVEL_EXACT
        assert status_ladder.level_1_after == LEVEL_EXACT

    def test_level_2_unchanged(self, status_ladder):
        assert status_ladder.level_2_changed is False
        assert status_ladder.level_2_before == LEVEL_CONSTITUTIVE_DERIVED
        assert status_ladder.level_2_after == LEVEL_CONSTITUTIVE_DERIVED

    def test_level_3_unchanged(self, status_ladder):
        assert status_ladder.level_3_changed is False
        assert (
            status_ladder.level_3_before
            == LEVEL_CONSTITUTIVE_LAPSE_PROMOTION_OBSTRUCTED
        )

    def test_tphi_unchanged(self, status_ladder):
        assert status_ladder.tphi_changed is False
        assert status_ladder.tphi_before == TPHI_STATUS_PHASE_VI
        assert status_ladder.tphi_after == TPHI_STATUS_PHASE_VII

    def test_tphi_vi_equals_vii(self, status_ladder):
        assert TPHI_STATUS_PHASE_VI == TPHI_STATUS_PHASE_VII

    def test_no_level_weakened(self, status_ladder):
        assert status_ladder.no_level_weakened is True

    def test_eos_closure_status(self, status_ladder):
        assert (
            status_ladder.eos_closure_status
            == ClosureClassification.ADMISSIBLE_BUT_NONUNIQUE.value
        )

    def test_degeneracy_status(self, status_ladder):
        assert (
            status_ladder.degeneracy_status
            == ClosureClassification.PARTIALLY_CLOSING.value
        )


# ================================================================
# 12. TestMasterResult (~15 tests)
# ================================================================

class TestMasterResult:
    """Master EOSPotentialResult: all components present and valid."""

    def test_valid(self, master_result):
        assert master_result.valid is True

    def test_eos_admissibility_present(self, master_result):
        assert master_result.eos_admissibility is not None

    def test_conditional_sequence_present(self, master_result):
        assert master_result.conditional_sequence is not None

    def test_anisotropy_present(self, master_result):
        assert master_result.anisotropy is not None

    def test_candidate_potential_present(self, master_result):
        assert master_result.candidate_potential is not None

    def test_degeneracy_assessment_present(self, master_result):
        assert master_result.degeneracy_assessment is not None

    def test_nec_compatibility_present(self, master_result):
        assert master_result.nec_compatibility is not None

    def test_lapse_impact_present(self, master_result):
        assert master_result.lapse_impact is not None

    def test_phase6_reconfirmation_present(self, master_result):
        assert master_result.phase6_reconfirmation is not None

    def test_status_ladder_present(self, master_result):
        assert master_result.status_ladder is not None

    def test_at_least_15_nonclaims(self, master_result):
        assert len(master_result.nonclaims) >= 15

    def test_closure_classification(self, master_result):
        assert (
            master_result.closure_classification
            == ClosureClassification.ADMISSIBLE_BUT_NONUNIQUE.value
        )

    def test_closure_enum(self, master_result):
        assert (
            master_result.closure_enum
            == ClosureClassification.ADMISSIBLE_BUT_NONUNIQUE
        )

    def test_diagnostics_populated(self, master_result):
        d = master_result.diagnostics
        assert d["beta_Q_is_eos_exponent"] is False
        assert d["beta_Q_is_stiffness_exponent"] is True
        assert d["conditional_mapping_exists"] is True
        assert d["has_terminal_anisotropy_block"] is True
        assert d["fully_breaks_degeneracy"] is False
        assert d["improves_lapse"] is False
        assert d["phase6_preserved"] is True

    def test_remaining_obstructions_nonempty(self, master_result):
        assert len(master_result.remaining_obstructions) >= 3

    def test_approx_status_nonempty(self, master_result):
        assert len(master_result.approx_status) > 50


# ================================================================
# 13. TestPublicAPI (~5 tests)
# ================================================================

class TestPublicAPI:
    """Verify all 5 public API functions return correct types."""

    def test_test_eos_admissibility_from_beta(self):
        result = test_eos_admissibility_from_beta()
        assert isinstance(result, EOSAdmissibilityTest)
        assert result.beta_Q_is_eos_exponent is False

    def test_assess_conditional_eos_from_beta(self):
        result = assess_conditional_eos_from_beta()
        assert isinstance(result, ConditionalMappingSequence)
        assert result.is_conditional is True
        assert result.requires_route_a is True
        assert result.valid_for_collapse is False

    def test_build_candidate_scalar_potential_public(self):
        result = build_candidate_scalar_potential()
        assert isinstance(result, CandidateScalarPotential)
        assert result.not_from_beta_Q_alone is True

    def test_assess_degeneracy_reduction(self):
        result = assess_degeneracy_reduction()
        assert isinstance(result, DegeneracyReductionAssessment)
        assert result.fully_breaks_degeneracy is False

    def test_assess_lapse_impact(self):
        result = assess_lapse_impact()
        assert isinstance(result, LapseImpactAssessment)
        assert result.improves_lapse_determination is False


# ================================================================
# 14. TestNonclaims (~6 tests)
# ================================================================

class TestNonclaims:
    """Nonclaims guardrails: key claims explicitly disclaimed."""

    def test_mentions_not_eos(self, master_result):
        ncs = master_result.nonclaims
        assert any(
            "NOT" in n and ("derive" in n.lower() or "equation of state" in n.lower())
            for n in ncs
        )

    def test_mentions_anisotropy(self, master_result):
        ncs = master_result.nonclaims
        assert any("anisotropic" in n.lower() for n in ncs)

    def test_mentions_route_specificity(self, master_result):
        ncs = master_result.nonclaims
        assert any(
            "Route A" in n or "route A" in n or "Route B" in n
            for n in ncs
        )

    def test_mentions_v_not_unique(self, master_result):
        ncs = master_result.nonclaims
        assert any("NOT unique" in n or "not unique" in n.lower() for n in ncs)

    def test_mentions_lapse_persists(self, master_result):
        ncs = master_result.nonclaims
        assert any(
            "lapse" in n.lower() and "persist" in n.lower()
            for n in ncs
        )

    def test_mentions_no_observational_predictions_changed(self, master_result):
        ncs = master_result.nonclaims
        assert any(
            "No observational" in n or "no observational" in n
            for n in ncs
        )


# ================================================================
# 15. TestSerialization (~7 tests)
# ================================================================

class TestSerialization:
    """Serialization roundtrip and structure."""

    def test_dict_is_dict(self, master_result):
        d = eos_potential_result_to_dict(master_result)
        assert isinstance(d, dict)

    def test_dict_valid(self, master_result):
        d = eos_potential_result_to_dict(master_result)
        assert d["valid"] is True

    def test_json_roundtrip(self, master_result):
        d = eos_potential_result_to_dict(master_result)
        s = json.dumps(d)
        d2 = json.loads(s)
        assert d2["valid"] is True

    def test_sequence_steps_in_dict(self, master_result):
        d = eos_potential_result_to_dict(master_result)
        steps = d["conditional_sequence"]["steps"]
        assert len(steps) == 5
        assert steps[0]["is_exact"] is True
        assert steps[4]["is_terminal_block"] is True

    def test_scope_in_dict(self, master_result):
        d = eos_potential_result_to_dict(master_result)
        # Scope captured via approx_status
        assert d["closure_classification"] == "admissible_but_nonunique"

    def test_nec_scope_in_dict(self, master_result):
        d = eos_potential_result_to_dict(master_result)
        nc = d["nec_compatibility"]
        assert nc["scope_is_isotropic_route_a_only"] is True
        assert nc["not_full_collapse_nec_analysis"] is True

    def test_diagnostics_in_dict(self, master_result):
        d = eos_potential_result_to_dict(master_result)
        diag = d["diagnostics"]
        assert diag["n_nonclaims"] >= 15
        assert diag["nec_scope_isotropic_route_a_only"] is True
        assert diag["not_from_beta_Q_alone"] is True
