"""Unit tests for Route B g_- energy density (grut/route_b_gminus_energy.py).

Tests that the standalone diagonal quadratic g_- action is absent by CTP
antisymmetry, and that the mixed g_+ * g_- channel remains unresolved.
11 test classes, ~56 tests.
"""

from __future__ import annotations

import math
import pytest

from grut.route_b_gminus_energy import (
    compute_route_b_gminus_energy_assessment,
    route_b_gminus_result_to_dict,
    derive_ctp_antisymmetry,
    analyze_quadratic_gminus_action,
    evaluate_energy_definitions,
    analyze_mixed_channel_residue,
    assess_component_b_compatibility,
    assess_projection_sensitivity,
    assess_physical_admissibility,
    classify_gminus_energy,
    make_radial_grid,
    RouteBGMinusParams,
    ALPHA_VAC,
    R_S,
    M_EXT,
    R_EQ,
    TAU_CANONICAL,
    A_CRIT,
    PHI_GOLDEN,
    CTP_ANTISYMMETRY_ORDER,
    NONCLAIMS,
    GMINUS_ASSUMPTIONS,
)


# ================================================================
# Module-scoped fixtures
# ================================================================

@pytest.fixture(scope="module")
def params():
    return RouteBGMinusParams(n_r=500)


@pytest.fixture(scope="module")
def master_result(params):
    return compute_route_b_gminus_energy_assessment(params)


@pytest.fixture(scope="module")
def ctp_result(params):
    return derive_ctp_antisymmetry(params)


@pytest.fixture(scope="module")
def quad_result(params):
    return analyze_quadratic_gminus_action(params)


@pytest.fixture(scope="module")
def energy_result(params):
    return evaluate_energy_definitions(params)


@pytest.fixture(scope="module")
def mixed_result(params):
    return analyze_mixed_channel_residue(params)


# ================================================================
# Test Classes
# ================================================================

class TestConstants:
    """Verify module-level constants."""

    def test_alpha_vac(self):
        assert abs(ALPHA_VAC - 1.0 / 3.0) < 1e-10

    def test_M_ext(self):
        assert abs(M_EXT - 0.5) < 1e-10

    def test_tau_canonical(self):
        assert abs(TAU_CANONICAL - math.sqrt(1.5)) < 1e-10

    def test_phi_golden(self):
        assert abs(PHI_GOLDEN - (1.0 + math.sqrt(5.0)) / 2.0) < 1e-10

    def test_ctp_antisymmetry_order(self):
        assert CTP_ANTISYMMETRY_ORDER == 2


class TestCTPAntisymmetryDerivation:
    """Verify the CTP antisymmetry derivation."""

    def test_even_orders_killed(self, ctp_result):
        assert 0 in ctp_result.even_orders_killed
        assert 2 in ctp_result.even_orders_killed
        assert 4 in ctp_result.even_orders_killed

    def test_odd_orders_survive(self, ctp_result):
        assert 1 in ctp_result.odd_orders_survive
        assert 3 in ctp_result.odd_orders_survive

    def test_diagonal_quadratic_coefficient_zero(self, ctp_result):
        assert ctp_result.diagonal_quadratic_coefficient == 0.0

    def test_copy_1_coefficient(self, ctp_result):
        assert abs(ctp_result.copy_1_quadratic_coefficient - 1.0 / 8.0) < 1e-15

    def test_copy_2_coefficient(self, ctp_result):
        assert abs(ctp_result.copy_2_quadratic_coefficient - 1.0 / 8.0) < 1e-15

    def test_cancellation_exact(self, ctp_result):
        assert ctp_result.cancellation_exact is True

    def test_numerical_verification(self, ctp_result):
        assert ctp_result.numerical_verification_passed is True


class TestQuadraticGMinusAction:
    """Verify the quadratic action analysis."""

    def test_diagonal_action_zero(self, quad_result):
        assert quad_result.diagonal_quadratic_action_zero is True

    def test_cross_coupling_exists(self, quad_result):
        assert quad_result.cross_coupling_exists is True

    def test_cross_coupling_vanishes_in_phys_limit(self, quad_result):
        assert quad_result.cross_coupling_vanishes_in_physical_limit is True

    def test_cross_coupling_linear_in_gminus(self, quad_result):
        assert quad_result.cross_coupling_linear_in_gminus is True

    def test_net_diagonal_sign_zero(self, quad_result):
        assert quad_result.net_diagonal_sign == 0

    def test_upgrade_flag(self, quad_result):
        assert quad_result.upgrade_from_wrong_sign_to_absent is True


class TestEnergyDefinitions:
    """Verify the four energy definition results for standalone diagonal sector."""

    def test_quadratic_eh_zero(self, energy_result):
        assert energy_result.quadratic_eh_result == "zero"

    def test_canonical_hamiltonian_zero(self, energy_result):
        assert energy_result.canonical_hamiltonian_result == "zero"

    def test_isaacson_zero(self, energy_result):
        assert energy_result.isaacson_result == "zero"

    def test_perturbation_theory_na(self, energy_result):
        assert energy_result.perturbation_theory_result == "not_applicable"

    def test_no_nonzero_definitions(self, energy_result):
        assert energy_result.n_definitions_giving_nonzero == 0

    def test_consensus_absent(self, energy_result):
        assert energy_result.standalone_diagonal_consensus == "energy_structurally_absent"


class TestMixedChannelResidue:
    """Verify the mixed g_+ * g_- channel analysis."""

    def test_cross_coupling_exists(self, mixed_result):
        assert mixed_result.cross_coupling_exists is True

    def test_linear_in_gminus(self, mixed_result):
        assert mixed_result.linear_in_gminus is True

    def test_vanishes_in_physical_limit(self, mixed_result):
        assert mixed_result.vanishes_in_physical_limit is True

    def test_is_remaining_residue(self, mixed_result):
        assert mixed_result.is_remaining_route_b_residue is True

    def test_effective_energy_not_computed(self, mixed_result):
        assert mixed_result.effective_energy_computed is False


class TestComponentBCompatibility:
    """Verify Component B compatibility assessment."""

    def test_standalone_diagonal_not_compatible(self, params):
        co = assess_component_b_compatibility(params)
        assert co.standalone_diagonal_compatible is False

    def test_mixed_channel_undetermined(self, params):
        co = assess_component_b_compatibility(params)
        assert co.mixed_channel_compatible == "undetermined"

    def test_computed_compatible_false(self, params):
        co = assess_component_b_compatibility(params)
        assert co.computed_compatible is False

    def test_overall_status(self, params):
        co = assess_component_b_compatibility(params)
        assert co.overall_status == "unresolved_but_narrowed"

    def test_has_notes(self, params):
        co = assess_component_b_compatibility(params)
        assert len(co.notes) >= 3


class TestProjectionSensitivity:
    """Verify projection sensitivity assessment."""

    def test_standalone_diagonal_moot(self, params):
        pr = assess_projection_sensitivity(params)
        assert pr.standalone_diagonal_projection == "moot"

    def test_mixed_channel_pre_projection_only(self, params):
        pr = assess_projection_sensitivity(params)
        assert pr.mixed_channel_projection == "pre_projection_only"

    def test_mixed_boundary_undetermined(self, params):
        pr = assess_projection_sensitivity(params)
        assert pr.mixed_channel_boundary_sensitive == "undetermined"

    def test_has_notes(self, params):
        pr = assess_projection_sensitivity(params)
        assert len(pr.notes) >= 3


class TestPhysicalAdmissibility:
    """Verify physical admissibility assessment."""

    def test_standalone_not_applicable(self, params):
        ad = assess_physical_admissibility(params)
        assert ad.standalone_diagonal_admissible == "not_applicable"

    def test_mixed_undetermined(self, params):
        ad = assess_physical_admissibility(params)
        assert ad.mixed_channel_admissible == "undetermined"

    def test_energy_does_not_exist(self, params):
        ad = assess_physical_admissibility(params)
        assert ad.energy_exists is False

    def test_has_notes(self, params):
        ad = assess_physical_admissibility(params)
        assert len(ad.notes) >= 3


class TestClassification:
    """Verify classification and ranking."""

    def test_classification_string(self, master_result):
        cl = master_result.classification
        assert cl.classification == (
            "gminus_diagonal_quadratic_energy_absent__"
            "mixed_channel_unresolved"
        )

    def test_not_full_no_go(self, master_result):
        cl = master_result.classification
        assert cl.is_full_route_b_no_go is False

    def test_standalone_diagonal_closed(self, master_result):
        cl = master_result.classification
        assert cl.standalone_diagonal_closed is True

    def test_mixed_channel_unresolved(self, master_result):
        cl = master_result.classification
        assert cl.mixed_channel_unresolved is True

    def test_residue_reduced(self, master_result):
        cl = master_result.classification
        assert cl.residue_reduced is True

    def test_is_provisional(self, master_result):
        cl = master_result.classification
        assert cl.is_provisional is True


class TestNonclaims:
    """Verify nonclaims and assumptions."""

    def test_nonclaim_count(self, master_result):
        assert len(master_result.nonclaims) == 10

    def test_assumption_count(self, master_result):
        assert len(master_result.assumptions) == 8

    def test_mixed_mentioned_in_nonclaims(self, master_result):
        assert any("mixed g_+ * g_-" in nc for nc in master_result.nonclaims)

    def test_ctp_antisymmetry_mentioned_in_nonclaims(self, master_result):
        assert any("CTP antisymmetry" in nc for nc in master_result.nonclaims)


class TestSerialization:
    """Verify serialization to dict."""

    def test_valid(self, master_result):
        d = route_b_gminus_result_to_dict(master_result)
        assert d["valid"] is True

    def test_has_classification(self, master_result):
        d = route_b_gminus_result_to_dict(master_result)
        assert "classification" in d

    def test_classification_string(self, master_result):
        d = route_b_gminus_result_to_dict(master_result)
        assert d["classification"]["classification"] == (
            "gminus_diagonal_quadratic_energy_absent__"
            "mixed_channel_unresolved"
        )

    def test_has_nonclaims(self, master_result):
        d = route_b_gminus_result_to_dict(master_result)
        assert len(d["nonclaims"]) == 10
