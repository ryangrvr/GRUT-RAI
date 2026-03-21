"""Tests for grut.barrier_action_sector — Covariant Barrier Action Sector.

Targeted tests for the Equilibrium Source Degeneracy Theorem, admissibility
conditions, route assessments (A-D), route comparison, T^Phi
underdetermination analysis, admissible T^Phi constraints, minimal missing
input, status ladder update, Phase V reconfirmation, master result, and
serialization.

~120 tests across 15 test classes.
"""

from __future__ import annotations

import json
import math

import pytest

from grut.barrier_action_sector import (
    compute_barrier_action_analysis,
    barrier_action_result_to_dict,
    build_admissibility_analysis,
    build_route_assessment_A,
    build_route_assessment_B,
    build_route_assessment_C,
    build_route_assessment_D,
    build_route_comparison,
    build_equilibrium_source_degeneracy_proof,
    build_tphi_underdetermination_analysis,
    build_admissible_tphi_constraints,
    build_minimal_missing_input,
    build_status_ladder_update,
    build_phase5_reconfirmation,
    ALPHA_VAC,
    BETA_Q,
    EPSILON_Q,
    R_EQ_OVER_R_S,
    C_ENDPOINT,
    N_ADMISSIBILITY_CONDITIONS,
    ROUTE_A,
    ROUTE_B,
    ROUTE_C,
    ROUTE_D,
    TPHI_STATUS_PHASE_V,
    TPHI_STATUS_PHASE_VI,
    LEVEL_EXACT,
    LEVEL_CONSTITUTIVE_DERIVED,
    LEVEL_CONSTITUTIVE_LAPSE_PROMOTION_OBSTRUCTED,
    SCOPE_STATEMENT,
)


# ================================================================
# Module-scoped fixtures
# ================================================================

@pytest.fixture(scope="module")
def admissibility():
    """Admissibility conditions."""
    return build_admissibility_analysis()


@pytest.fixture(scope="module")
def route_a():
    return build_route_assessment_A()


@pytest.fixture(scope="module")
def route_b():
    return build_route_assessment_B()


@pytest.fixture(scope="module")
def route_c():
    return build_route_assessment_C()


@pytest.fixture(scope="module")
def route_d():
    return build_route_assessment_D()


@pytest.fixture(scope="module")
def route_comparison():
    routes = [
        build_route_assessment_A(),
        build_route_assessment_B(),
        build_route_assessment_C(),
        build_route_assessment_D(),
    ]
    return build_route_comparison(routes)


@pytest.fixture(scope="module")
def source_degeneracy():
    return build_equilibrium_source_degeneracy_proof()


@pytest.fixture(scope="module")
def tphi_underdetermination():
    return build_tphi_underdetermination_analysis()


@pytest.fixture(scope="module")
def tphi_constraints():
    return build_admissible_tphi_constraints()


@pytest.fixture(scope="module")
def minimal_missing():
    return build_minimal_missing_input()


@pytest.fixture(scope="module")
def status_ladder():
    return build_status_ladder_update()


@pytest.fixture(scope="module")
def phase5_reconfirmation():
    return build_phase5_reconfirmation()


@pytest.fixture(scope="module")
def master_result():
    return compute_barrier_action_analysis()


# ================================================================
# 1. TestConstants (~6 tests)
# ================================================================

class TestConstants:
    """Verify self-contained constants match canonical values."""

    def test_alpha_vac(self):
        assert abs(ALPHA_VAC - 1.0 / 3.0) < 1e-15

    def test_beta_q(self):
        assert abs(BETA_Q - 2.0) < 1e-15

    def test_epsilon_q(self):
        assert abs(EPSILON_Q - ALPHA_VAC ** 2) < 1e-15
        assert abs(EPSILON_Q - 1.0 / 9.0) < 1e-15

    def test_r_eq_over_r_s(self):
        assert abs(R_EQ_OVER_R_S - ALPHA_VAC) < 1e-15

    def test_c_endpoint(self):
        assert abs(C_ENDPOINT - 3.0) < 1e-15

    def test_n_admissibility_conditions(self):
        assert N_ADMISSIBILITY_CONDITIONS == 6

    def test_scope_statement_nonempty(self):
        assert len(SCOPE_STATEMENT) > 50


# ================================================================
# 2. TestAdmissibilityConditions (~8 tests)
# ================================================================

class TestAdmissibilityConditions:
    """Test the 6 admissibility conditions."""

    def test_n_conditions(self, admissibility):
        assert admissibility.n_conditions == 6

    def test_conditions_count(self, admissibility):
        assert len(admissibility.conditions) == 6

    def test_all_have_label(self, admissibility):
        for c in admissibility.conditions:
            assert len(c.label) > 0

    def test_all_have_description(self, admissibility):
        for c in admissibility.conditions:
            assert len(c.description) > 10

    def test_all_have_required_by(self, admissibility):
        for c in admissibility.conditions:
            assert len(c.required_by) > 0

    def test_includes_general_covariance(self, admissibility):
        labels = [c.label for c in admissibility.conditions]
        assert "general_covariance" in labels

    def test_includes_combined_conservation(self, admissibility):
        labels = [c.label for c in admissibility.conditions]
        assert "combined_conservation" in labels

    def test_includes_equilibrium_compatibility(self, admissibility):
        labels = [c.label for c in admissibility.conditions]
        assert "equilibrium_compatibility" in labels


# ================================================================
# 3. TestRouteA (~8 tests)
# ================================================================

class TestRouteA:
    """Route A: Klein-Gordon overdamped."""

    def test_action_based(self, route_a):
        assert route_a.action_based is True

    def test_covariant(self, route_a):
        assert route_a.covariant is True

    def test_constitutive_limit_not_exact(self, route_a):
        """Route A is approximate (overdamped limit), not exact."""
        assert route_a.reproduces_constitutive_limit is True
        assert route_a.constitutive_limit_exact is False

    def test_gravity_coupling_resolved(self, route_a):
        """Formal minimal coupling exists."""
        assert route_a.gravity_coupling_resolved is True

    def test_not_uniquely_determined(self, route_a):
        assert route_a.uniquely_determined_by_grut is False

    def test_requires_extra_postulate(self, route_a):
        assert route_a.requires_extra_postulate is True

    def test_T_phi_derivable(self, route_a):
        assert route_a.T_phi_derivable is True

    def test_at_least_two_free_functions(self, route_a):
        assert route_a.n_free_functions >= 2
        assert len(route_a.free_functions) >= 2


# ================================================================
# 4. TestRouteB (~8 tests)
# ================================================================

class TestRouteB:
    """Route B: Galley doubled-field."""

    def test_action_based(self, route_b):
        assert route_b.action_based is True

    def test_covariant(self, route_b):
        assert route_b.covariant is True

    def test_constitutive_limit_exact(self, route_b):
        """Route B produces first-order ODE exactly."""
        assert route_b.reproduces_constitutive_limit is True
        assert route_b.constitutive_limit_exact is True

    def test_gravity_coupling_not_resolved(self, route_b):
        """Gravity coupling has NOT been implemented."""
        assert route_b.gravity_coupling_resolved is False

    def test_not_uniquely_determined(self, route_b):
        assert route_b.uniquely_determined_by_grut is False

    def test_requires_extra_postulate(self, route_b):
        assert route_b.requires_extra_postulate is True

    def test_T_phi_derivable(self, route_b):
        assert route_b.T_phi_derivable is True

    def test_route_label(self, route_b):
        assert route_b.route_label == ROUTE_B


# ================================================================
# 5. TestRouteC (~6 tests)
# ================================================================

class TestRouteC:
    """Route C: nonlocal retarded kernel."""

    def test_action_based(self, route_c):
        assert route_c.action_based is True

    def test_covariant(self, route_c):
        assert route_c.covariant is True

    def test_T_phi_derivable(self, route_c):
        assert route_c.T_phi_derivable is True

    def test_at_least_one_free_function(self, route_c):
        assert route_c.n_free_functions >= 1

    def test_not_uniquely_determined(self, route_c):
        assert route_c.uniquely_determined_by_grut is False

    def test_requires_extra_postulate(self, route_c):
        assert route_c.requires_extra_postulate is True


# ================================================================
# 6. TestRouteD (~6 tests)
# ================================================================

class TestRouteD:
    """Route D: auxiliary-field (non-action closure)."""

    def test_not_action_based(self, route_d):
        """Route D is a non-action closure route."""
        assert route_d.action_based is False

    def test_covariant(self, route_d):
        assert route_d.covariant is True

    def test_T_phi_not_derivable(self, route_d):
        """T^Phi is NOT variationally derivable under Route D."""
        assert route_d.T_phi_derivable is False

    def test_no_free_functions(self, route_d):
        assert route_d.n_free_functions == 0

    def test_does_not_require_extra_postulate(self, route_d):
        assert route_d.requires_extra_postulate is False

    def test_notes_mention_non_action(self, route_d):
        """Route D notes should say it is a non-action route."""
        assert any("non-action" in n for n in route_d.notes)


# ================================================================
# 7. TestRouteComparison (~8 tests)
# ================================================================

class TestRouteComparison:
    """Cross-route comparison."""

    def test_n_routes(self, route_comparison):
        assert route_comparison.n_routes == 4

    def test_routes_list_length(self, route_comparison):
        assert len(route_comparison.routes) == 4

    def test_any_fully_determined_false(self, route_comparison):
        assert route_comparison.any_fully_determined is False

    def test_best_action_candidate_nonempty(self, route_comparison):
        assert len(route_comparison.best_action_candidate) > 0

    def test_best_candidate_is_route_b(self, route_comparison):
        assert route_comparison.best_action_candidate == ROUTE_B

    def test_best_candidate_has_limitations(self, route_comparison):
        assert len(route_comparison.best_candidate_limitations) > 20

    def test_all_action_routes_require_extra(self, route_comparison):
        assert route_comparison.all_action_routes_require_extra is True

    def test_notes_nonempty(self, route_comparison):
        assert len(route_comparison.notes) >= 2


# ================================================================
# 8. TestSourceDegeneracy (~15 tests)
# ================================================================

class TestSourceDegeneracy:
    """Equilibrium Source Degeneracy Theorem — central result."""

    def test_source_at_eq_zero(self, source_degeneracy):
        assert abs(source_degeneracy.source_at_eq) < 1e-15

    def test_source_vanishes(self, source_degeneracy):
        assert source_degeneracy.source_vanishes is True

    def test_self_healing_input(self, source_degeneracy):
        assert source_degeneracy.self_healing_input is True

    def test_equilibrium_ode_trivial(self, source_degeneracy):
        assert source_degeneracy.equilibrium_ode_reduces_to_trivial is True

    def test_no_dynamical_discrimination(self, source_degeneracy):
        assert source_degeneracy.no_dynamical_discrimination is True

    def test_not_identifiable_from_equilibrium(self, source_degeneracy):
        assert source_degeneracy.action_not_identifiable_from_equilibrium is True

    def test_does_NOT_claim_identical_stress_energy(self, source_degeneracy):
        """Critical guardrail: theorem does NOT claim identical stress-energy."""
        assert source_degeneracy.does_NOT_claim_identical_stress_energy is True

    def test_six_proof_steps(self, source_degeneracy):
        assert len(source_degeneracy.proof_steps) == 6

    def test_first_step_mentions_equilibrium(self, source_degeneracy):
        assert "equilibrium" in source_degeneracy.proof_steps[0].lower()

    def test_last_step_contains_qed(self, source_degeneracy):
        assert "QED" in source_degeneracy.proof_steps[-1]

    def test_theorem_status_proven(self, source_degeneracy):
        assert source_degeneracy.theorem_status == "proven"

    def test_scope_statement(self, source_degeneracy):
        assert source_degeneracy.scope_statement == SCOPE_STATEMENT

    def test_uses_self_healing_from_phase_iv(self, source_degeneracy):
        assert source_degeneracy.uses_self_healing_from_phase_iv is True

    def test_uses_constitutive_ode_from_phase_iii(self, source_degeneracy):
        assert source_degeneracy.uses_constitutive_ode_from_phase_iii is True

    def test_notes_mention_non_identifiability(self, source_degeneracy):
        assert any(
            "non-identifiability" in n for n in source_degeneracy.notes
        )


# ================================================================
# 9. TestTPhiUnderdetermination (~8 tests)
# ================================================================

class TestTPhiUnderdetermination:
    """Level B: structural T^Phi underdetermination."""

    def test_level_A_supports(self, tphi_underdetermination):
        assert tphi_underdetermination.level_A_supports is True

    def test_level_A_does_not_prove_level_B(self, tphi_underdetermination):
        """Critical: A supports B but does NOT prove B."""
        assert tphi_underdetermination.level_A_proves_level_B is False

    def test_additional_inputs_needed(self, tphi_underdetermination):
        assert len(tphi_underdetermination.additional_inputs_needed) >= 3

    def test_independent_structural_reasons(self, tphi_underdetermination):
        assert len(tphi_underdetermination.independent_structural_reasons) >= 2

    def test_mentions_no_local_lagrangian(self, tphi_underdetermination):
        reasons = tphi_underdetermination.independent_structural_reasons
        assert any("no local" in r.lower() for r in reasons)

    def test_mentions_free_functions(self, tphi_underdetermination):
        reasons = tphi_underdetermination.independent_structural_reasons
        assert any("free functions" in r for r in reasons)

    def test_notes_classification_grade(self, tphi_underdetermination):
        assert any(
            "classification-grade" in n
            for n in tphi_underdetermination.notes
        )

    def test_notes_A_does_not_prove_B(self, tphi_underdetermination):
        assert any(
            "does not prove" in n for n in tphi_underdetermination.notes
        )


# ================================================================
# 10. TestTPhiConstraints (~8 tests)
# ================================================================

class TestTPhiConstraints:
    """Admissible T^Phi constraints."""

    def test_combined_conservation(self, tphi_constraints):
        assert tphi_constraints.combined_conservation is True

    def test_spherical_symmetry(self, tphi_constraints):
        assert tphi_constraints.spherical_symmetry is True

    def test_max_3_components(self, tphi_constraints):
        assert tphi_constraints.max_independent_components == 3

    def test_nec_violation_indicated(self, tphi_constraints):
        assert tphi_constraints.nec_violation_indicated is True

    def test_nec_derivation_level_constitutive(self, tphi_constraints):
        assert tphi_constraints.nec_derivation_level == "constitutive"

    def test_equilibrium_energy_is_matching_condition(self, tphi_constraints):
        """Equilibrium energy is a matching condition, NOT derived result."""
        assert tphi_constraints.equilibrium_energy_is_matching_condition is True

    def test_n_constraints(self, tphi_constraints):
        assert tphi_constraints.n_constraints == 5

    def test_constraints_list_length(self, tphi_constraints):
        assert len(tphi_constraints.constraints_list) == 5


# ================================================================
# 11. TestMinimalMissing (~8 tests)
# ================================================================

class TestMinimalMissing:
    """Minimal missing input analysis."""

    def test_n_candidates(self, minimal_missing):
        assert minimal_missing.n_candidates == 4

    def test_candidates_length(self, minimal_missing):
        assert len(minimal_missing.candidates) == 4

    def test_from_existing_grut_false(self, minimal_missing):
        assert minimal_missing.from_existing_grut is False

    def test_any_one_may_reduce_degeneracy(self, minimal_missing):
        assert minimal_missing.any_one_may_reduce_degeneracy is True

    def test_sufficiency_not_guaranteed(self, minimal_missing):
        """Sufficiency of a single input not guaranteed generically."""
        assert minimal_missing.sufficiency_not_guaranteed_generically is True

    def test_full_tphi_likely_needs_multiple(self, minimal_missing):
        assert minimal_missing.full_tphi_likely_needs_multiple is True

    def test_mentions_potential(self, minimal_missing):
        assert any("V(Phi)" in c for c in minimal_missing.candidates)

    def test_mentions_off_equilibrium(self, minimal_missing):
        assert any(
            "off-equilibrium" in c.lower() or "Off-equilibrium" in c
            for c in minimal_missing.candidates
        )


# ================================================================
# 12. TestPhase5Reconfirmation (~6 tests)
# ================================================================

class TestPhase5Reconfirmation:
    """All Phase V results preserved."""

    def test_all_preserved(self, phase5_reconfirmation):
        assert phase5_reconfirmation.all_preserved is True

    def test_insufficiency_preserved(self, phase5_reconfirmation):
        assert phase5_reconfirmation.insufficiency_theorem_preserved is True

    def test_effective_nec_preserved(self, phase5_reconfirmation):
        assert phase5_reconfirmation.effective_nec_preserved is True

    def test_lapse_direction_preserved(self, phase5_reconfirmation):
        assert phase5_reconfirmation.lapse_direction_preserved is True

    def test_proxy_classification_preserved(self, phase5_reconfirmation):
        assert phase5_reconfirmation.proxy_classification_preserved is True

    def test_self_healing_preserved(self, phase5_reconfirmation):
        assert phase5_reconfirmation.self_healing_preserved is True


# ================================================================
# 13. TestStatusLadder (~8 tests)
# ================================================================

class TestStatusLadder:
    """Status ladder update: Phase V → Phase VI."""

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
        assert (
            status_ladder.level_3_after
            == LEVEL_CONSTITUTIVE_LAPSE_PROMOTION_OBSTRUCTED
        )

    def test_tphi_sharpened(self, status_ladder):
        assert status_ladder.tphi_sharpened is True

    def test_tphi_before(self, status_ladder):
        assert status_ladder.tphi_before == TPHI_STATUS_PHASE_V

    def test_tphi_after(self, status_ladder):
        assert status_ladder.tphi_after == TPHI_STATUS_PHASE_VI

    def test_no_level_weakened(self, status_ladder):
        assert status_ladder.no_level_weakened is True

    def test_sharpening_reason_nonempty(self, status_ladder):
        assert len(status_ladder.tphi_sharpening_reason) > 20


# ================================================================
# 14. TestMasterResult (~15 tests)
# ================================================================

class TestMasterResult:
    """Master BarrierActionResult."""

    def test_valid(self, master_result):
        assert master_result.valid is True

    def test_action_derived_false(self, master_result):
        assert master_result.action_derived is False

    def test_action_partially_constrained(self, master_result):
        assert master_result.action_partially_constrained is True

    def test_source_degeneracy_proven(self, master_result):
        assert master_result.source_degeneracy_proven is True

    def test_tphi_underdetermination_established(self, master_result):
        assert master_result.tphi_underdetermination_established is True

    def test_self_healing_used_as_input(self, master_result):
        assert master_result.self_healing_used_as_input is True

    def test_has_admissibility(self, master_result):
        assert master_result.admissibility is not None
        assert master_result.admissibility.n_conditions == 6

    def test_has_all_routes(self, master_result):
        assert master_result.route_A is not None
        assert master_result.route_B is not None
        assert master_result.route_C is not None
        assert master_result.route_D is not None

    def test_has_route_comparison(self, master_result):
        assert master_result.route_comparison is not None
        assert master_result.route_comparison.n_routes == 4

    def test_has_source_degeneracy(self, master_result):
        assert master_result.source_degeneracy is not None
        assert master_result.source_degeneracy.theorem_status == "proven"

    def test_has_tphi_underdetermination(self, master_result):
        assert master_result.tphi_underdetermination is not None

    def test_has_tphi_constraints(self, master_result):
        assert master_result.tphi_constraints is not None

    def test_has_minimal_missing(self, master_result):
        assert master_result.minimal_missing is not None

    def test_nonclaims_at_least_12(self, master_result):
        assert len(master_result.nonclaims) >= 12

    def test_nonclaim_0_guardrail(self, master_result):
        """First nonclaim: does NOT derive a covariant action."""
        assert "does NOT derive" in master_result.nonclaims[0]

    def test_nonclaim_1_stress_energy(self, master_result):
        """Second nonclaim: does NOT claim identical stress-energy."""
        assert (
            "does NOT claim" in master_result.nonclaims[1]
            and "stress-energy" in master_result.nonclaims[1]
        )

    def test_remaining_obstructions_nonempty(self, master_result):
        assert len(master_result.remaining_obstructions) >= 2

    def test_diagnostics(self, master_result):
        d = master_result.diagnostics
        assert d["n_admissibility_conditions"] == 6
        assert d["n_routes"] == 4
        assert d["any_fully_determined"] is False
        assert d["source_degeneracy_proven"] is True
        assert d["level_A_proves_level_B"] is False
        assert d["tphi_sharpened"] is True
        assert d["phase5_preserved"] is True

    def test_approx_status_nonempty(self, master_result):
        assert len(master_result.approx_status) > 50


# ================================================================
# 15. TestSerialization (~7 tests)
# ================================================================

class TestSerialization:
    """JSON serialization and round-trip."""

    def test_dict_is_dict(self, master_result):
        d = barrier_action_result_to_dict(master_result)
        assert isinstance(d, dict)

    def test_dict_valid(self, master_result):
        d = barrier_action_result_to_dict(master_result)
        assert d["valid"] is True

    def test_json_roundtrip(self, master_result):
        d = barrier_action_result_to_dict(master_result)
        s = json.dumps(d)
        d2 = json.loads(s)
        assert d2["valid"] is True

    def test_scope_in_dict(self, master_result):
        d = barrier_action_result_to_dict(master_result)
        assert (
            d["source_degeneracy"]["scope_statement"] == SCOPE_STATEMENT
        )

    def test_source_degeneracy_proven_in_dict(self, master_result):
        d = barrier_action_result_to_dict(master_result)
        assert d["source_degeneracy_proven"] is True

    def test_action_derived_false_in_dict(self, master_result):
        d = barrier_action_result_to_dict(master_result)
        assert d["action_derived"] is False

    def test_nonclaims_in_dict(self, master_result):
        d = barrier_action_result_to_dict(master_result)
        assert len(d["nonclaims"]) >= 12
