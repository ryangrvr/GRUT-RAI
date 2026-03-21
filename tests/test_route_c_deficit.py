"""Unit tests for Route C deficit assessment (grut/route_c_deficit.py).

Tests that the Markov-reduced Route C pathway cannot generate the missing
1/r^2 support identified in Phase 6C.  12 test classes, ~75 tests.
"""

from __future__ import annotations

import math
import numpy as np
import pytest

from grut.route_c_deficit import (
    compute_route_c_deficit_assessment,
    route_c_result_to_dict,
    compute_route_c_energy_profile,
    evaluate_chain_1_markov_kinetic,
    evaluate_chain_2_self_healing,
    evaluate_chain_3_candidate_potential,
    evaluate_chain_4_spatial_gradient,
    assess_insufficiency,
    compute_lapse_correction_at_equilibrium,
    analyze_potential_sector,
    analyze_spatial_gradient,
    catalog_loopholes,
    build_provisional_candidate_ranking,
    make_radial_grid,
    RouteCParams,
    ALPHA_VAC,
    R_S,
    M_EXT,
    R_EQ,
    TAU_CANONICAL,
    A_CRIT,
    EPSILON_RC_COEFF,
    COMP_B_COEFF,
    RHO_EQ_COEFF,
    PHASE6B_A_CRIT_NATURAL,
    NONCLAIMS,
    ROUTE_C_ASSUMPTIONS,
)


# ================================================================
# Module-scoped fixtures
# ================================================================

@pytest.fixture(scope="module")
def params():
    return RouteCParams(n_r=500)


@pytest.fixture(scope="module")
def master_result(params):
    return compute_route_c_deficit_assessment(params)


@pytest.fixture(scope="module")
def energy_profile(params):
    return compute_route_c_energy_profile(params)


# ================================================================
# Test Classes
# ================================================================

class TestConstants:
    """Verify module-level constants."""

    def test_alpha_vac(self):
        assert abs(ALPHA_VAC - 1.0 / 3.0) < 1e-10

    def test_M_ext(self):
        assert abs(M_EXT - 0.5) < 1e-10

    def test_R_eq(self):
        assert abs(R_EQ - R_S / 3.0) < 1e-10

    def test_tau_canonical(self):
        assert abs(TAU_CANONICAL - math.sqrt(1.5)) < 1e-10

    def test_A_crit(self):
        assert abs(A_CRIT - 1.062) < 1e-6

    def test_epsilon_rc_coeff(self):
        expected = A_CRIT ** 2 * M_EXT ** 2 / (2.0 * TAU_CANONICAL ** 2)
        assert abs(EPSILON_RC_COEFF - expected) < 1e-10

    def test_comp_b_coeff(self):
        expected = 1.0 / (8.0 * math.pi)
        assert abs(COMP_B_COEFF - expected) < 1e-10


class TestRadialGrid:
    """Verify grid construction."""

    def test_grid_length(self, params):
        r = make_radial_grid(params)
        assert len(r) == params.n_r

    def test_grid_starts_at_R_ext(self, params):
        r = make_radial_grid(params)
        assert abs(r[0] - params.R_ext) < 1e-6

    def test_grid_decreasing(self, params):
        r = make_radial_grid(params)
        assert all(r[i] > r[i + 1] for i in range(len(r) - 1))

    def test_grid_covers_R_eq(self, params):
        r = make_radial_grid(params)
        assert r[-1] < params.R_eq < r[0]


class TestRouteCEnergyProfile:
    """Verify Route C energy density vs epsilon_min comparison."""

    def test_epsilon_rc_is_pure_1r4(self, energy_profile):
        """epsilon_RC * r^4 should be constant."""
        ep = energy_profile
        valid = ep.epsilon_min > 0
        product = ep.epsilon_RC[valid] * ep.r[valid] ** 4
        assert np.std(product) / np.mean(product) < 1e-10

    def test_epsilon_rc_coeff_matches(self, energy_profile):
        assert abs(energy_profile.epsilon_RC_coeff - EPSILON_RC_COEFF) / EPSILON_RC_COEFF < 1e-6

    def test_epsilon_min_decomposition(self, energy_profile):
        """epsilon_min = Component A + Component B where nonzero."""
        ep = energy_profile
        valid = ep.epsilon_min > 0
        diff = np.abs(ep.epsilon_min[valid] - ep.component_A[valid] - ep.component_B[valid])
        assert np.max(diff) < 1e-12

    def test_deficit_ratio_at_R_eq_overcovering(self, energy_profile):
        """Ratio > 1 at R_eq means overcovering."""
        assert energy_profile.ratio_at_R_eq > 1.0

    def test_deficit_ratio_at_r1_undercovering(self, energy_profile):
        """Ratio < 1 at r=1 means undercovering."""
        assert energy_profile.ratio_at_r1 < 1.0

    def test_covers_component_A(self, energy_profile):
        assert energy_profile.covers_component_A is True

    def test_not_covers_component_B(self, energy_profile):
        assert energy_profile.covers_component_B is False

    def test_ratio_min_below_one(self, energy_profile):
        assert energy_profile.ratio_min < 1.0

    def test_integrated_shortfall_positive(self, energy_profile):
        assert energy_profile.integrated_shortfall > 0

    def test_has_notes(self, energy_profile):
        assert len(energy_profile.notes) >= 3


class TestChain1MarkovKinetic:
    """Verify Chain 1: Markov kinetic scaling."""

    def test_scaling_1r4(self, params):
        c = evaluate_chain_1_markov_kinetic(params)
        assert c.scaling_law == "1/r^4"

    def test_not_provides_1r2(self, params):
        c = evaluate_chain_1_markov_kinetic(params)
        assert c.provides_1r2 is False

    def test_is_formal(self, params):
        c = evaluate_chain_1_markov_kinetic(params)
        assert c.is_formal is True

    def test_premise_mentions_markov(self, params):
        c = evaluate_chain_1_markov_kinetic(params)
        assert "Markov" in c.premise

    def test_conclusion_mentions_1r4(self, params):
        c = evaluate_chain_1_markov_kinetic(params)
        assert "1/r^4" in c.conclusion


class TestChain2SelfHealing:
    """Verify Chain 2: Self-healing lapse correction."""

    def test_scaling_zero(self, params):
        c = evaluate_chain_2_self_healing(params)
        assert c.scaling_law == "0"

    def test_not_provides_1r2(self, params):
        c = evaluate_chain_2_self_healing(params)
        assert c.provides_1r2 is False

    def test_source_vanishes(self, params):
        lc = compute_lapse_correction_at_equilibrium(params)
        assert abs(lc.source_X_minus_Phi) < 1e-10

    def test_delta_phi_zero(self, params):
        lc = compute_lapse_correction_at_equilibrium(params)
        assert abs(lc.delta_Phi_lapse) < 1e-10

    def test_self_healing_holds(self, params):
        lc = compute_lapse_correction_at_equilibrium(params)
        assert lc.self_healing_holds is True

    def test_has_notes(self, params):
        lc = compute_lapse_correction_at_equilibrium(params)
        assert len(lc.notes) >= 3


class TestChain3CandidatePotential:
    """Verify Chain 3: Candidate potential sector."""

    def test_scaling_1r4(self, params):
        c = evaluate_chain_3_candidate_potential(params)
        assert c.scaling_law == "1/r^4"

    def test_not_provides_1r2(self, params):
        c = evaluate_chain_3_candidate_potential(params)
        assert c.provides_1r2 is False

    def test_V_at_R_eq_positive(self, params):
        ps = analyze_potential_sector(params)
        assert ps.V_at_R_eq > 0

    def test_not_intrinsic_route_c(self, params):
        ps = analyze_potential_sector(params)
        assert ps.is_intrinsic_route_c is False

    def test_premise_mentions_inherited(self, params):
        c = evaluate_chain_3_candidate_potential(params)
        assert "inherited" in c.premise.lower() or "candidate" in c.premise.lower()


class TestChain4SpatialGradient:
    """Verify Chain 4: Spatial gradient scaling."""

    def test_scaling_1r6(self, params):
        c = evaluate_chain_4_spatial_gradient(params)
        assert c.scaling_law == "1/r^6"

    def test_not_provides_1r2(self, params):
        c = evaluate_chain_4_spatial_gradient(params)
        assert c.provides_1r2 is False

    def test_gradient_sq_positive(self, params):
        sg = analyze_spatial_gradient(params)
        assert sg.gradient_sq_at_R_eq > 0

    def test_evaluated_in_reduced_background(self, params):
        sg = analyze_spatial_gradient(params)
        assert sg.evaluated_in_reduced_background is True

    def test_steeper_than_1r4(self, params):
        """1/r^6 decays faster than 1/r^4 at large r."""
        sg = analyze_spatial_gradient(params)
        assert "1/r^6" in sg.gradient_sq_scaling


class TestInsufficiencyAssessment:
    """Verify aggregate insufficiency assessment."""

    def test_n_chains(self, params):
        ia = assess_insufficiency(params)
        assert ia.n_chains == 4

    def test_all_consistent(self, params):
        ia = assess_insufficiency(params)
        assert ia.all_chains_consistent is True

    def test_none_provide_1r2(self, params):
        ia = assess_insufficiency(params)
        assert ia.any_chain_provides_1r2 is False

    def test_overall_insufficient(self, params):
        ia = assess_insufficiency(params)
        assert ia.overall_insufficient is True

    def test_classification_string(self, params):
        ia = assess_insufficiency(params)
        assert ia.classification_string == "route_c_insufficient_within_markov_reduction"

    def test_not_general_no_go(self, params):
        ia = assess_insufficiency(params)
        assert ia.is_general_no_go is False

    def test_has_notes(self, params):
        ia = assess_insufficiency(params)
        assert len(ia.notes) >= 3


class TestLoopholeCatalog:
    """Verify loophole catalog."""

    def test_n_loopholes(self):
        lpc = catalog_loopholes()
        assert lpc.n_loopholes == 5

    def test_high_severity_count(self):
        lpc = catalog_loopholes()
        assert lpc.n_high_severity == 2

    def test_beyond_markov_exists(self):
        lpc = catalog_loopholes()
        n = sum(1 for lp in lpc.loopholes if lp.requires_beyond_markov)
        assert n >= 1

    def test_kernel_loophole_name(self):
        lpc = catalog_loopholes()
        assert "kernel" in lpc.loopholes[0].name.lower()

    def test_source_loophole_name(self):
        lpc = catalog_loopholes()
        assert "source" in lpc.loopholes[4].name.lower()

    def test_none_tested(self):
        lpc = catalog_loopholes()
        assert lpc.any_tested is False


class TestProvisionalRanking:
    """Verify provisional candidate ranking update."""

    def test_route_c_status(self):
        pr = build_provisional_candidate_ranking()
        assert pr.route_c_status == "insufficient_within_markov_reduction"

    def test_route_c_downgraded(self):
        pr = build_provisional_candidate_ranking()
        assert pr.route_c_downgraded is True

    def test_route_b_provisional(self):
        pr = build_provisional_candidate_ranking()
        assert pr.route_b_status == "provisional"

    def test_route_b_ghost(self):
        pr = build_provisional_candidate_ranking()
        assert "ghost" in pr.route_b_obstruction.lower() or "Ghost" in pr.route_b_obstruction

    def test_previous_status(self):
        pr = build_provisional_candidate_ranking()
        assert "plausibility" in pr.route_c_previous_status

    def test_is_provisional(self):
        pr = build_provisional_candidate_ranking()
        assert pr.is_provisional is True


class TestNonclaims:
    """Verify nonclaims and assumptions."""

    def test_nonclaim_count(self, master_result):
        assert len(master_result.nonclaims) == 10

    def test_not_general_no_go_mentioned(self, master_result):
        assert any("NOT a general no-go" in nc for nc in master_result.nonclaims)

    def test_exponential_kernel_mentioned(self, master_result):
        assert any("exponential kernel" in nc for nc in master_result.nonclaims)

    def test_assumption_count(self, master_result):
        assert len(master_result.assumptions) == 5


class TestSerialization:
    """Verify serialization to dict."""

    def test_valid(self, master_result):
        d = route_c_result_to_dict(master_result)
        assert d["valid"] is True

    def test_has_classification(self, master_result):
        d = route_c_result_to_dict(master_result)
        assert "classification" in d

    def test_classification_string(self, master_result):
        d = route_c_result_to_dict(master_result)
        assert d["classification"]["classification"] == "route_c_insufficient_within_markov_reduction"

    def test_has_nonclaims(self, master_result):
        d = route_c_result_to_dict(master_result)
        assert len(d["nonclaims"]) == 10

    def test_has_assumptions(self, master_result):
        d = route_c_result_to_dict(master_result)
        assert len(d["assumptions"]) == 5
