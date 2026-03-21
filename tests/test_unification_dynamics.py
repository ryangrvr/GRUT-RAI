"""Tests — Phase D4: Embedded Triplet Unification Dynamics.

55 tests across 10 classes.
"""

import math
import json
import pytest

from grut.unification_dynamics import (
    # Constants
    ALPHA_VAC, R_S, M_EXT, R_EQ, TAU_CANONICAL, A_CRIT,
    COMP_B_COEFF, ETA_TARGET, ETA_SQUARED, LAMBDA_DEFAULT,
    XI_CONFORMAL, XI_DEFAULT, XI_SCAN_VALUES,
    MU0_SQUARED_DEFAULT, KRETSCHNER_COEFF,
    N_CURVATURE_INVARIANTS, N_LAGRANGIAN_TERMS, N_MODE_SECTORS,
    # Assumptions / nonclaims
    DYNAMICS_ASSUMPTIONS, DYNAMICS_NONCLAIMS,
    # Dataclasses
    UnificationDynamicsParams,
    # Functions
    construct_lagrangian,
    apply_embedding_ansatz,
    decompose_modes,
    derive_radial_mode_equation,
    assess_component_A_recovery,
    assess_component_B_preservation,
    assess_trigger_regime,
    inventory_artifacts,
    classify_dynamics,
    compute_unification_dynamics,
    unification_dynamics_result_to_dict,
)


@pytest.fixture(scope="module")
def params():
    return UnificationDynamicsParams()


@pytest.fixture(scope="module")
def result():
    return compute_unification_dynamics()


# ================================================================
# Section 1: Constants (5 tests)
# ================================================================

class TestConstants:
    def test_n_lagrangian_terms(self):
        assert N_LAGRANGIAN_TERMS == 4

    def test_n_mode_sectors(self):
        assert N_MODE_SECTORS == 4

    def test_n_curvature_invariants(self):
        assert N_CURVATURE_INVARIANTS == 3

    def test_eta_squared(self):
        assert abs(ETA_SQUARED - 1.0 / (8.0 * math.pi)) < 1e-10

    def test_mu0_squared_negative(self):
        assert MU0_SQUARED_DEFAULT < 0


# ================================================================
# Section 2: Lagrangian Construction (5 tests)
# ================================================================

class TestLagrangianConstruction:
    def test_lagrangian_exists(self, result):
        assert result.lagrangian is not None

    def test_four_terms(self, result):
        assert result.lagrangian.n_terms == 4

    def test_broken_phase(self, result):
        assert result.lagrangian.broken_phase

    def test_vev_matches(self, result):
        assert abs(result.lagrangian.vev_squared - ETA_SQUARED) < 0.01

    def test_effective_mass_formula(self, result):
        assert "m_eff" in result.lagrangian.effective_mass_formula


# ================================================================
# Section 3: Embedding Ansatz (5 tests)
# ================================================================

class TestEmbeddingAnsatz:
    def test_ansatz_exists(self, result):
        assert result.ansatz is not None

    def test_hedgehog_formula(self, result):
        assert "eta" in result.ansatz.ansatz_formula
        assert "f(r)" in result.ansatz.ansatz_formula

    def test_radial_mode(self, result):
        assert "eta" in result.ansatz.radial_mode_formula

    def test_boundary_origin(self, result):
        assert result.ansatz.boundary_f_origin == 0.0

    def test_boundary_infty(self, result):
        assert result.ansatz.boundary_f_infty == 1.0


# ================================================================
# Section 4: Mode Decomposition (6 tests)
# ================================================================

class TestModeDecomposition:
    def test_decomposition_exists(self, result):
        assert result.decomposition is not None

    def test_bvp_converged(self, result):
        assert result.decomposition.bvp_converged

    def test_four_sectors(self, result):
        assert result.decomposition.n_sectors == 4

    def test_radial_kinetic_present(self, result):
        names = [s.name for s in result.decomposition.sectors]
        assert "radial_kinetic" in names

    def test_angular_gradient_present(self, result):
        names = [s.name for s in result.decomposition.sectors]
        assert "angular_gradient" in names

    def test_potential_decays_steeply(self, result):
        assert result.decomposition.potential_exponent < -5.0


# ================================================================
# Section 5: Radial Mode Equation (6 tests)
# ================================================================

class TestRadialModeEquation:
    def test_exists(self, result):
        assert result.radial_equation is not None

    def test_eom_formula(self, result):
        assert len(result.radial_equation.eom_formula) > 10

    def test_scalar_memory_formula(self, result):
        assert len(result.radial_equation.scalar_memory_formula) > 10

    def test_radial_is_static(self, result):
        assert result.radial_equation.radial_is_static

    def test_scalar_memory_is_dynamic(self, result):
        assert result.radial_equation.scalar_memory_is_dynamic

    def test_curvature_coupling(self, result):
        assert result.radial_equation.eom_has_curvature_coupling


# ================================================================
# Section 6: Component A Recovery (6 tests)
# ================================================================

class TestComponentARecovery:
    def test_exists(self, result):
        assert result.comp_a_assessment is not None

    def test_shape_target(self, result):
        assert result.comp_a_assessment.shape_exponent_target == -4.0

    def test_shape_measured_negative(self, result):
        assert result.comp_a_assessment.shape_exponent_measured < 0

    def test_mechanisms_not_identical(self, result):
        # Honest: topology-driven != source-driven
        assert not result.comp_a_assessment.mechanisms_identical

    def test_classification_nonempty(self, result):
        assert len(result.comp_a_assessment.classification) > 0

    def test_all_three_false(self, result):
        # Mechanism always differs, so all_three_pass must be False
        assert not result.comp_a_assessment.all_three_pass


# ================================================================
# Section 7: Component B Preservation (5 tests)
# ================================================================

class TestComponentBPreservation:
    def test_exists(self, result):
        assert result.comp_b_assessment is not None

    def test_target(self, result):
        assert result.comp_b_assessment.angular_tail_exponent_target == -2.0

    def test_measured_negative(self, result):
        assert result.comp_b_assessment.angular_tail_exponent_measured < 0

    def test_angular_match(self, result):
        assert result.comp_b_assessment.angular_match

    def test_classification_preserved(self, result):
        assert result.comp_b_assessment.classification in (
            "preserved", "preserved_with_corrections"
        )


# ================================================================
# Section 8: Trigger Regime (6 tests)
# ================================================================

class TestTriggerRegime:
    def test_exists(self, result):
        assert result.trigger_assessment is not None

    def test_three_invariants(self, result):
        assert result.trigger_assessment.n_invariants == 3

    def test_top_ranked_nonempty(self, result):
        assert len(result.trigger_assessment.top_ranked_name) > 0

    def test_top_score_above_half(self, result):
        assert result.trigger_assessment.top_ranked_score > 0.5

    def test_kretschner_present(self, result):
        names = [inv.name for inv in result.trigger_assessment.invariants]
        assert "kretschner_sqrt" in names

    def test_classification_nonempty(self, result):
        assert len(result.trigger_assessment.classification) > 0


# ================================================================
# Section 9: Artifact Inventory & Classification (6 tests)
# ================================================================

class TestArtifactsClassification:
    def test_inventory_exists(self, result):
        assert result.artifact_inventory is not None

    def test_at_least_five(self, result):
        assert result.artifact_inventory.n_artifacts >= 5

    def test_at_least_one_major(self, result):
        assert result.artifact_inventory.n_major >= 1

    def test_all_have_descriptions(self, result):
        for a in result.artifact_inventory.artifacts:
            assert len(a.description) > 10

    def test_classification_exists(self, result):
        assert result.classification is not None

    def test_phase_lock_has_d4(self, result):
        assert "unification_D4" in result.classification.phase_lock_update


# ================================================================
# Section 10: Nonclaims & Serialization (5 tests)
# ================================================================

class TestNonclaimsSerialization:
    def test_ten_nonclaims(self, result):
        assert len(result.nonclaims) == 10

    def test_ten_assumptions(self, result):
        assert len(result.assumptions) == 10

    def test_serialization_valid(self, result):
        d = unification_dynamics_result_to_dict(result)
        js = json.dumps(d, indent=2, default=str)
        assert len(js) > 100

    def test_serialization_classification(self, result):
        d = unification_dynamics_result_to_dict(result)
        assert len(d["classification"]["classification"]) > 0

    def test_serialization_trigger(self, result):
        d = unification_dynamics_result_to_dict(result)
        assert d["trigger"]["n_invariants"] == 3
