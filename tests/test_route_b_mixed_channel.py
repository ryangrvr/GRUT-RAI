"""Unit tests for Route B mixed g_+ * g_- channel (grut/route_b_mixed_channel.py).

Tests that the mixed cross-coupling channel is insufficient for Component B
within the tested perturbative Galley framework.
10 test classes, ~55 tests.
"""

from __future__ import annotations

import math
import pytest

from grut.route_b_mixed_channel import (
    compute_route_b_mixed_channel_assessment,
    route_b_mixed_result_to_dict,
    define_mixed_channel,
    derive_mixed_quadratic_structure,
    analyze_induced_source,
    assess_shape_compatibility,
    assess_mixed_projection_sensitivity,
    assess_mixed_physical_admissibility,
    classify_mixed_channel,
    make_radial_grid,
    RouteBMixedParams,
    ALPHA_VAC,
    R_S,
    M_EXT,
    R_EQ,
    TAU_CANONICAL,
    A_CRIT,
    PHI_GOLDEN,
    CTP_ANTISYMMETRY_ORDER,
    N_IC_PROFILES,
    COMPONENT_B_SCALING,
    NONCLAIMS,
    MIXED_ASSUMPTIONS,
)


# ================================================================
# Module-scoped fixtures
# ================================================================

@pytest.fixture(scope="module")
def params():
    return RouteBMixedParams(n_r=500)


@pytest.fixture(scope="module")
def master_result(params):
    return compute_route_b_mixed_channel_assessment(params)


@pytest.fixture(scope="module")
def defn_result(params):
    return define_mixed_channel(params)


@pytest.fixture(scope="module")
def quad_result(params):
    return derive_mixed_quadratic_structure(params)


@pytest.fixture(scope="module")
def source_result(params):
    return analyze_induced_source(params)


@pytest.fixture(scope="module")
def shape_result(params):
    return assess_shape_compatibility(params)


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

    def test_component_b_scaling(self):
        assert COMPONENT_B_SCALING == -2.0


class TestMixedChannelDefinition:
    """Verify the mixed channel definition."""

    def test_object_name(self, defn_result):
        assert defn_result.object_name == "delta^2_S_EH(h_+, h_-)"

    def test_is_bilinear(self, defn_result):
        assert defn_result.is_bilinear is True

    def test_is_self_adjoint(self, defn_result):
        assert defn_result.is_self_adjoint is True

    def test_is_only_surviving_quadratic(self, defn_result):
        assert defn_result.is_only_surviving_quadratic is True

    def test_diagonal_absent(self, defn_result):
        assert defn_result.diagonal_h_minus_squared_absent is True


class TestMixedQuadraticStructure:
    """Verify the surviving mixed quadratic structure derivation."""

    def test_mixed_term_survives(self, quad_result):
        assert quad_result.mixed_term_survives is True

    def test_analytical_coefficient(self, quad_result):
        assert quad_result.analytical_coefficient == 2.0

    def test_numerical_verification_passed(self, quad_result):
        assert quad_result.numerical_verification_passed is True

    def test_numerical_residual_small(self, quad_result):
        assert quad_result.numerical_verification_max_residual < 1e-4

    def test_is_self_adjoint(self, quad_result):
        assert quad_result.is_self_adjoint is True

    def test_has_notes(self, quad_result):
        assert len(quad_result.notes) >= 5

    def test_coefficient_exact(self, quad_result):
        assert abs(quad_result.analytical_coefficient - 2.0) < 1e-15


class TestInducedSourceAnalysis:
    """Verify the induced source / source chain analysis."""

    def test_source_chain_identified(self, source_result):
        assert source_result.source_chain_identified is True

    def test_h_minus_eom(self, source_result):
        assert source_result.h_minus_eom_is_linearized_einstein is True

    def test_source_is_t_tilde(self, source_result):
        assert source_result.source_is_t_tilde_phi_minus is True

    def test_t_tilde_bilinear(self, source_result):
        assert source_result.t_tilde_is_bilinear_in_phi_eq_phi_minus is True

    def test_is_ghost_sourced(self, source_result):
        assert source_result.is_ghost_sourced is True

    def test_is_ic_dependent(self, source_result):
        assert source_result.is_ic_dependent is True

    def test_profiles_differ(self, source_result):
        assert source_result.profiles_differ is True


class TestShapeCompatibility:
    """Verify shape compatibility with Component B."""

    def test_is_ic_dependent(self, shape_result):
        assert shape_result.is_ic_dependent is True

    def test_does_not_match_component_b(self, shape_result):
        assert shape_result.matches_component_b is False

    def test_radial_profiles_differ(self, shape_result):
        assert shape_result.radial_profiles_differ is True

    def test_profile_1_not_component_b(self, shape_result):
        assert abs(shape_result.profile_1_best_fit_exponent - COMPONENT_B_SCALING) > 0.5

    def test_profile_2_not_component_b(self, shape_result):
        assert abs(shape_result.profile_2_best_fit_exponent - COMPONENT_B_SCALING) > 0.5

    def test_profiles_differ_numerically(self, shape_result):
        diff = abs(shape_result.profile_1_best_fit_exponent -
                   shape_result.profile_2_best_fit_exponent)
        assert diff > 0.3

    def test_has_structural_argument(self, shape_result):
        assert len(shape_result.structural_argument) > 50


class TestProjectionSensitivity:
    """Verify projection and CTP boundary sensitivity."""

    def test_does_not_survive_physical_limit(self, params):
        pr = assess_mixed_projection_sensitivity(params)
        assert pr.survives_physical_limit is False

    def test_does_not_survive_ctp_boundary(self, params):
        pr = assess_mixed_projection_sensitivity(params)
        assert pr.survives_ctp_boundary is False

    def test_is_pre_projection_only(self, params):
        pr = assess_mixed_projection_sensitivity(params)
        assert pr.is_pre_projection_only is True

    def test_has_physical_limit_argument(self, params):
        pr = assess_mixed_projection_sensitivity(params)
        assert len(pr.physical_limit_argument) > 20

    def test_has_ctp_boundary_argument(self, params):
        pr = assess_mixed_projection_sensitivity(params)
        assert len(pr.ctp_boundary_argument) > 20


class TestPhysicalAdmissibility:
    """Verify physical admissibility assessment."""

    def test_not_admissible(self, params):
        ad = assess_mixed_physical_admissibility(params)
        assert ad.is_physically_admissible is False

    def test_four_pathologies(self, params):
        ad = assess_mixed_physical_admissibility(params)
        assert ad.n_pathology_channels == 4

    def test_jointly_disqualifying(self, params):
        ad = assess_mixed_physical_admissibility(params)
        assert ad.jointly_disqualifying is True

    def test_ic_dependent_pathology(self, params):
        ad = assess_mixed_physical_admissibility(params)
        assert ad.pathology_ic_dependent is True

    def test_ghost_sourced_pathology(self, params):
        ad = assess_mixed_physical_admissibility(params)
        assert ad.pathology_ghost_sourced is True

    def test_ctp_and_projection_killed(self, params):
        ad = assess_mixed_physical_admissibility(params)
        assert ad.pathology_ctp_killed is True
        assert ad.pathology_projection_killed is True


class TestClassification:
    """Verify classification and Route B status."""

    def test_classification_string(self, master_result):
        cl = master_result.classification
        assert cl.classification == (
            "mixed_channel_insufficient_within_tested_galley_framework"
        )

    def test_route_b_channels_closed(self, master_result):
        cl = master_result.classification
        assert cl.route_b_classical_channels_closed is True

    def test_all_tested_channels_classified(self, master_result):
        cl = master_result.classification
        assert cl.all_tested_channels_classified is True

    def test_framework_scope(self, master_result):
        cl = master_result.classification
        assert cl.framework_scope == "perturbative_galley_ctp_framework"

    def test_post_projection_insufficient(self, master_result):
        cl = master_result.classification
        assert cl.post_projection_status == "insufficient"

    def test_gminus_diagonal_absent(self, master_result):
        cl = master_result.classification
        assert cl.gminus_diagonal_status == "absent"

    def test_gminus_mixed_insufficient(self, master_result):
        cl = master_result.classification
        assert cl.gminus_mixed_status == "insufficient_within_tested_framework"


class TestNonclaims:
    """Verify nonclaims and assumptions."""

    def test_nonclaim_count(self, master_result):
        assert len(master_result.nonclaims) == 10

    def test_assumption_count(self, master_result):
        assert len(master_result.assumptions) == 10

    def test_nonclaims_mention_tested_residue(self, master_result):
        assert any("tested classical Route B residue" in nc
                    for nc in master_result.nonclaims)

    def test_nonclaims_mention_eom(self, master_result):
        assert any("EOM-level argument" in nc
                    for nc in master_result.nonclaims)


class TestSerialization:
    """Verify serialization to dict."""

    def test_valid(self, master_result):
        d = route_b_mixed_result_to_dict(master_result)
        assert d["valid"] is True

    def test_has_classification(self, master_result):
        d = route_b_mixed_result_to_dict(master_result)
        assert "classification" in d

    def test_classification_string(self, master_result):
        d = route_b_mixed_result_to_dict(master_result)
        assert d["classification"]["classification"] == (
            "mixed_channel_insufficient_within_tested_galley_framework"
        )

    def test_has_nonclaims(self, master_result):
        d = route_b_mixed_result_to_dict(master_result)
        assert len(d["nonclaims"]) == 10
