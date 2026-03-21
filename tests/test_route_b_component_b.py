"""Unit tests for Route B Component B test (grut/route_b_component_b.py).

Tests that pre-projection Route B cannot provide clean physical 1/r^2
support through any computed channel.  The g_- / doubled-metric sector
remains uncomputed and is the key unresolved residue.
12 test classes, ~70 tests.
"""

from __future__ import annotations

import math
import numpy as np
import pytest

from grut.route_b_component_b import (
    compute_route_b_component_b_assessment,
    route_b_result_to_dict,
    analyze_post_projection_equivalence,
    analyze_phi_minus_sector,
    analyze_g_minus_sector,
    analyze_dissipative_kernel,
    build_candidate_carrier_catalog,
    build_obstruction_catalog,
    assess_component_b_support,
    make_radial_grid,
    RouteBParams,
    ALPHA_VAC,
    R_S,
    M_EXT,
    R_EQ,
    TAU_CANONICAL,
    A_CRIT,
    EPSILON_RC_COEFF,
    COMP_B_COEFF,
    RHO_EQ_COEFF,
    PHI_GOLDEN,
    NONCLAIMS,
    ROUTE_B_ASSUMPTIONS,
)


# ================================================================
# Module-scoped fixtures
# ================================================================

@pytest.fixture(scope="module")
def params():
    return RouteBParams(n_r=500)


@pytest.fixture(scope="module")
def master_result(params):
    return compute_route_b_component_b_assessment(params)


@pytest.fixture(scope="module")
def post_proj(params):
    return analyze_post_projection_equivalence(params)


@pytest.fixture(scope="module")
def phi_minus(params):
    return analyze_phi_minus_sector(params)


@pytest.fixture(scope="module")
def g_minus(params):
    return analyze_g_minus_sector(params)


@pytest.fixture(scope="module")
def diss_kernel(params):
    return analyze_dissipative_kernel(params)


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

    def test_A_crit(self):
        assert abs(A_CRIT - 1.062) < 1e-6

    def test_phi_golden(self):
        assert abs(PHI_GOLDEN - (1.0 + math.sqrt(5.0)) / 2.0) < 1e-10


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


class TestPostProjectionEquivalence:
    """Verify post-projection Route B = Route C = pure 1/r^4."""

    def test_identical_to_route_c(self, post_proj):
        assert post_proj.identical_to_route_c is True

    def test_epsilon_coeff_matches_route_c(self, post_proj):
        route_c_coeff = A_CRIT ** 2 * M_EXT ** 2 / (2.0 * TAU_CANONICAL ** 2)
        assert abs(post_proj.epsilon_RC_coeff - route_c_coeff) / route_c_coeff < 1e-6

    def test_ratio_at_R_eq_overcovering(self, post_proj):
        assert post_proj.ratio_at_R_eq > 1.0

    def test_ratio_at_r1_undercovering(self, post_proj):
        assert post_proj.ratio_at_r1 < 1.0

    def test_not_provides_component_B(self, post_proj):
        assert post_proj.provides_component_B is False

    def test_shape_mismatch_exists(self, post_proj):
        assert len(post_proj.shape_mismatch) > 50

    def test_has_notes(self, post_proj):
        assert len(post_proj.notes) >= 3

    def test_epsilon_is_pure_1r4(self, post_proj):
        """epsilon * r^4 should be constant."""
        valid = post_proj.epsilon_min > 0
        product = post_proj.epsilon_post_proj[valid] * post_proj.r[valid] ** 4
        assert np.std(product) / np.mean(product) < 1e-10


class TestPhiMinusSector:
    """Verify Phi_- (ghost / difference) sector analysis."""

    def test_simple_growth_rate(self, phi_minus):
        expected = 1.0 / TAU_CANONICAL
        assert abs(phi_minus.simple_growth_rate - expected) / expected < 1e-6

    def test_full_kg_growth_rate(self, phi_minus):
        expected = PHI_GOLDEN / TAU_CANONICAL
        assert abs(phi_minus.full_kg_growth_rate - expected) / expected < 1e-6

    def test_decay_rate(self, phi_minus):
        expected = 1.0 / (PHI_GOLDEN * TAU_CANONICAL)
        assert abs(phi_minus.full_kg_decay_rate - expected) / expected < 1e-6

    def test_kinetic_sign_wrong(self, phi_minus):
        assert phi_minus.kinetic_sign == -1

    def test_is_ghost(self, phi_minus):
        assert phi_minus.is_ghost is True

    def test_not_geometric(self, phi_minus):
        assert phi_minus.spatial_profile_geometric is False

    def test_not_provides_component_B(self, phi_minus):
        assert phi_minus.provides_component_B is False


class TestGMinusSector:
    """Verify g_- (metric-difference) sector analysis."""

    def test_wrong_sign_eh(self, g_minus):
        assert g_minus.wrong_sign_eh is True

    def test_consistent_truncation(self, g_minus):
        assert g_minus.consistent_truncation is True

    def test_energy_density_not_computed(self, g_minus):
        assert g_minus.energy_density_computed is False

    def test_status_uncomputed_and_projection_sensitive(self, g_minus):
        assert g_minus.status == "uncomputed_and_projection_sensitive"

    def test_is_key_unresolved(self, g_minus):
        assert g_minus.is_key_unresolved_channel is True


class TestDissipativeKernel:
    """Verify S_diss dissipative kernel analysis."""

    def test_s_diss_zero_at_physical_limit(self, diss_kernel):
        assert abs(diss_kernel.s_diss_at_physical_limit) < 1e-15

    def test_vanishes_in_physical_limit(self, diss_kernel):
        assert diss_kernel.vanishes_in_physical_limit is True

    def test_pre_projection_ghost_coupled(self, diss_kernel):
        assert diss_kernel.pre_projection_ghost_coupled is True

    def test_not_provides_component_B(self, diss_kernel):
        assert diss_kernel.provides_component_B is False

    def test_has_notes(self, diss_kernel):
        assert len(diss_kernel.notes) >= 3


class TestCandidateCarrierCatalog:
    """Verify candidate carrier catalog."""

    def test_n_carriers(self, params):
        cc = build_candidate_carrier_catalog(params)
        assert cc.n_carriers == 5

    def test_n_physical(self, params):
        cc = build_candidate_carrier_catalog(params)
        assert cc.n_physical == 0

    def test_n_uncomputed(self, params):
        cc = build_candidate_carrier_catalog(params)
        assert cc.n_uncomputed == 2

    def test_n_projected_observable(self, params):
        cc = build_candidate_carrier_catalog(params)
        assert cc.n_projected_observable == 1

    def test_n_computed_sector(self, params):
        cc = build_candidate_carrier_catalog(params)
        assert cc.n_computed_sector == 2

    def test_n_formal_variation_channel(self, params):
        cc = build_candidate_carrier_catalog(params)
        assert cc.n_formal_variation_channel == 2

    def test_carrier_4_projection_sensitive(self, params):
        cc = build_candidate_carrier_catalog(params)
        assert cc.carriers[3].projection_status == "projection_sensitive"


class TestObstructionCatalog:
    """Verify obstruction catalog."""

    def test_n_obstructions(self):
        oc = build_obstruction_catalog()
        assert oc.n_obstructions == 5

    def test_n_high_severity(self):
        oc = build_obstruction_catalog()
        assert oc.n_high_severity == 3

    def test_n_medium_severity(self):
        oc = build_obstruction_catalog()
        assert oc.n_medium_severity == 2

    def test_obstruction_1_structural(self):
        oc = build_obstruction_catalog()
        assert oc.obstructions[0].obstruction_type == "structural"

    def test_obstruction_5_gap(self):
        oc = build_obstruction_catalog()
        assert oc.obstructions[4].obstruction_type == "gap"


class TestComponentBAssessment:
    """Verify aggregate Component B assessment."""

    def test_post_projection_not_sufficient(self, params):
        a = assess_component_b_support(params)
        assert a.post_projection_sufficient is False

    def test_computed_preproj_not_sufficient(self, params):
        a = assess_component_b_support(params)
        assert a.computed_preprojection_sufficient is False

    def test_uncomputed_sector_remains(self, params):
        a = assess_component_b_support(params)
        assert a.uncomputed_sector_remains is True

    def test_not_general_no_go(self, params):
        a = assess_component_b_support(params)
        assert a.is_general_no_go is False

    def test_classification_string(self, params):
        a = assess_component_b_support(params)
        assert a.classification_string == (
            "route_b_post_projection_insufficient__preprojection_unresolved"
        )

    def test_has_notes(self, params):
        a = assess_component_b_support(params)
        assert len(a.notes) >= 5


class TestNonclaims:
    """Verify nonclaims and assumptions."""

    def test_nonclaim_count(self, master_result):
        assert len(master_result.nonclaims) == 10

    def test_assumption_count(self, master_result):
        assert len(master_result.assumptions) == 6

    def test_g_minus_mentioned_in_nonclaims(self, master_result):
        assert any("g_- sector" in nc for nc in master_result.nonclaims)

    def test_ctp_mentioned_in_nonclaims(self, master_result):
        assert any("CTP boundary" in nc for nc in master_result.nonclaims)


class TestClassification:
    """Verify classification and ranking."""

    def test_classification_string(self, master_result):
        cl = master_result.classification
        assert cl.classification == (
            "route_b_post_projection_insufficient__preprojection_unresolved"
        )

    def test_post_projection_insufficient(self, master_result):
        cl = master_result.classification
        assert cl.post_projection_status == "insufficient"

    def test_g_minus_unresolved(self, master_result):
        cl = master_result.classification
        assert cl.g_minus_status == "unresolved"

    def test_is_provisional(self, master_result):
        cl = master_result.classification
        assert cl.is_provisional is True

    def test_not_general_no_go(self, master_result):
        cl = master_result.classification
        assert cl.is_general_no_go is False

    def test_uncomputed_sector_remains(self, master_result):
        cl = master_result.classification
        assert cl.uncomputed_sector_remains is True


class TestSerialization:
    """Verify serialization to dict."""

    def test_valid(self, master_result):
        d = route_b_result_to_dict(master_result)
        assert d["valid"] is True

    def test_has_classification(self, master_result):
        d = route_b_result_to_dict(master_result)
        assert "classification" in d

    def test_classification_string(self, master_result):
        d = route_b_result_to_dict(master_result)
        assert d["classification"]["classification"] == (
            "route_b_post_projection_insufficient__preprojection_unresolved"
        )

    def test_has_nonclaims(self, master_result):
        d = route_b_result_to_dict(master_result)
        assert len(d["nonclaims"]) == 10
