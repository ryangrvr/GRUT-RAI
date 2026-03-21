"""Tests — Phase D1: Defect-Sector Admissibility.

57 tests across 10 classes.
"""

import math
import json
import pytest
import numpy as np

from grut.defect_admissibility import (
    # Constants
    ALPHA_VAC, R_S, M_EXT, R_EQ, TAU_CANONICAL, A_CRIT,
    COMP_B_COEFF, ETA_TARGET, MU_DEFAULT, LAMBDA_DEFAULT,
    N_FIELD_CANDIDATES, COMPONENT_B_TARGET_EXPONENT, DELTA_CORE,
    # Assumptions / nonclaims
    DEFECT_ASSUMPTIONS, DEFECT_NONCLAIMS,
    # Dataclasses
    DefectAdmissibilityParams,
    # Functions
    assess_field_content,
    define_ssb_potential,
    define_hedgehog_ansatz,
    derive_hedgehog_ode,
    decompose_energy,
    prove_asymptotic_tail,
    build_compatibility_inventory,
    classify_defect_admissibility,
    compute_defect_admissibility,
    defect_admissibility_result_to_dict,
    _analytic_f,
    _analytic_f_prime,
    _fit_spatial_exponent,
)


@pytest.fixture(scope="module")
def params():
    return DefectAdmissibilityParams()


@pytest.fixture(scope="module")
def result():
    return compute_defect_admissibility()


# ================================================================
# Section 1: Constants (5 tests)
# ================================================================

class TestConstants:
    def test_eta_target(self):
        assert abs(ETA_TARGET - 1.0 / math.sqrt(8.0 * math.pi)) < 1e-10

    def test_eta_squared_is_comp_b(self):
        assert abs(ETA_TARGET ** 2 - COMP_B_COEFF) < 1e-10

    def test_lambda_default(self):
        assert abs(LAMBDA_DEFAULT - MU_DEFAULT ** 2 / ETA_TARGET ** 2) < 1e-6

    def test_comp_b_coeff(self):
        assert abs(COMP_B_COEFF - 1.0 / (8.0 * math.pi)) < 1e-10

    def test_n_field_candidates(self):
        assert N_FIELD_CANDIDATES == 3


# ================================================================
# Section 2: Field Content Assessment (6 tests)
# ================================================================

class TestFieldContent:
    def test_field_content_exists(self, result):
        assert result.field_content is not None

    def test_three_candidates(self, result):
        assert result.field_content.n_candidates == 3

    def test_real_scalar_no_monopole(self, result):
        assert not result.field_content.candidates[0].supports_monopole

    def test_complex_scalar_no_monopole(self, result):
        assert not result.field_content.candidates[1].supports_monopole

    def test_O3_supports_monopole(self, result):
        assert result.field_content.candidates[2].supports_monopole

    def test_selected_O3(self, result):
        assert result.field_content.selected_name == "O3_triplet"


# ================================================================
# Section 3: SSB Potential (5 tests)
# ================================================================

class TestSSBPotential:
    def test_potential_exists(self, result):
        assert result.potential is not None

    def test_eta_relation(self, result):
        p = result.potential
        assert abs(p.eta - p.mu / math.sqrt(p.lam)) < 1e-8

    def test_eta_squared_matches(self, result):
        assert abs(result.potential.eta_squared - COMP_B_COEFF) / COMP_B_COEFF < 1e-4

    def test_vacuum_manifold(self, result):
        assert "S^2" in result.potential.vacuum_manifold

    def test_potential_at_minimum(self, result):
        p = result.potential
        expected = -p.mu ** 4 / (4.0 * p.lam)
        assert abs(p.potential_at_minimum - expected) < 1e-8


# ================================================================
# Section 4: Hedgehog Ansatz (5 tests)
# ================================================================

class TestHedgehogAnsatz:
    def test_ansatz_exists(self, result):
        assert result.ansatz is not None

    def test_three_components(self, result):
        assert result.ansatz.n_components == 3

    def test_bc_origin(self, result):
        assert result.ansatz.boundary_conditions["f(0)"] == 0.0

    def test_bc_infinity(self, result):
        assert result.ansatz.boundary_conditions["f(infinity)"] == 1.0

    def test_gradient_squared(self, result):
        assert "f'" in result.ansatz.gradient_squared

    # -- Analytic profile tests --

    def test_analytic_f_at_zero(self):
        """f(0) = 0 for the analytic profile."""
        r = np.array([0.001])
        f = _analytic_f(r, DELTA_CORE)
        assert f[0] < 0.01

    def test_analytic_f_at_infinity(self):
        """f(inf) -> 1 for the analytic profile."""
        r = np.array([1000.0])
        f = _analytic_f(r, DELTA_CORE)
        assert abs(f[0] - 1.0) < 1e-6


# ================================================================
# Section 5: ODE Structure (6 tests)
# ================================================================

class TestODEStructure:
    def test_ode_exists(self, result):
        assert result.ode is not None

    def test_ode_formula(self, result):
        assert "f''" in result.ode.ode_formula

    def test_coeff_f_prime(self, result):
        assert result.ode.coefficient_f_prime == "2/r"

    def test_coeff_f(self, result):
        assert result.ode.coefficient_f == "-2/r^2"

    def test_bc_origin(self, result):
        assert result.ode.bc_origin == 0.0

    def test_bc_infinity(self, result):
        assert result.ode.bc_infinity == 1.0


# ================================================================
# Section 6: Energy Decomposition (6 tests)
# ================================================================

class TestEnergyDecomposition:
    def test_energy_exists(self, result):
        assert result.energy is not None

    def test_angular_dominates_at_large_r(self, result):
        assert result.energy.angular_fraction_at_large_r > 0.99

    def test_tail_exponent_near_minus_2(self, result):
        assert abs(result.energy.tail_exponent - (-2.0)) < 0.05

    def test_radial_kinetic_nonneg(self, result):
        assert np.all(result.energy.radial_kinetic >= 0)

    def test_angular_gradient_nonneg(self, result):
        assert np.all(result.energy.angular_gradient >= 0)

    def test_potential_nonneg(self, result):
        assert np.all(result.energy.potential_term >= 0)


# ================================================================
# Section 7: Asymptotic Tail (7 tests)
# ================================================================

class TestAsymptoticTail:
    def test_tail_exists(self, result):
        assert result.tail_proof is not None

    def test_shape_compatible(self, result):
        assert result.tail_proof.shape_compatible

    def test_coefficient_match(self, result):
        assert result.tail_proof.coefficient_match

    def test_exponent_deviation(self, result):
        assert result.tail_proof.exponent_deviation < 0.05

    def test_ratio_match(self, result):
        assert result.tail_proof.ratio_match

    def test_surviving_coefficient(self, result):
        assert abs(result.tail_proof.surviving_coefficient - ETA_TARGET ** 2) / ETA_TARGET ** 2 < 1e-4

    def test_target_coefficient(self, result):
        assert abs(result.tail_proof.target_coefficient - COMP_B_COEFF) / COMP_B_COEFF < 1e-4


# ================================================================
# Section 8: Compatibility Inventory (6 tests)
# ================================================================

class TestCompatibilityInventory:
    def test_inventory_exists(self, result):
        assert result.compatibility is not None

    def test_six_questions(self, result):
        assert result.compatibility.n_questions == 6

    def test_four_high(self, result):
        assert result.compatibility.n_high_severity == 4

    def test_two_medium(self, result):
        assert result.compatibility.n_medium_severity == 2

    def test_scalar_memory_relation(self, result):
        cats = [q.category for q in result.compatibility.questions]
        assert "scalar_memory_relation" in cats

    def test_all_deferred_d2(self, result):
        assert all(q.deferred_to == "Phase D2" for q in result.compatibility.questions)


# ================================================================
# Section 9: Classification (6 tests)
# ================================================================

class TestClassification:
    def test_classification_exists(self, result):
        assert result.classification is not None

    def test_classification_string(self, result):
        assert result.classification.classification == "provisional_candidate_extension_formulated"

    def test_phase_status(self, result):
        assert result.classification.phase_status == "formulated"

    def test_shape_compatible(self, result):
        assert result.classification.shape_compatible

    def test_phase_lock_has_d1(self, result):
        assert "defect_sector_D1" in result.classification.phase_lock_update

    def test_valid(self, result):
        assert result.valid


# ================================================================
# Section 10: Nonclaims & Serialization (5 tests)
# ================================================================

class TestNonclaimsSerialization:
    def test_ten_nonclaims(self, result):
        assert len(result.nonclaims) == 10

    def test_ten_assumptions(self, result):
        assert len(result.assumptions) == 10

    def test_serialization_valid(self, result):
        d = defect_admissibility_result_to_dict(result)
        js = json.dumps(d, indent=2, default=str)
        assert len(js) > 100

    def test_serialization_classification(self, result):
        d = defect_admissibility_result_to_dict(result)
        assert d["classification"]["classification"] == "provisional_candidate_extension_formulated"

    def test_serialization_tail_proof(self, result):
        d = defect_admissibility_result_to_dict(result)
        assert d["tail_proof"]["shape_compatible"]
