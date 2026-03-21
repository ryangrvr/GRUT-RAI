"""Tests — Phase D5: Source-Coupled Defect Dynamics.

60 tests across 11 classes.
"""

import math
import json
import pytest

from grut.source_coupled_defect import (
    # Constants
    ALPHA_VAC, R_S, M_EXT, R_EQ, TAU_CANONICAL, A_CRIT,
    COMP_B_COEFF, ETA_TARGET, ETA_SQUARED, LAMBDA_DEFAULT,
    GAMMA_DEFAULT, GAMMA_SCAN_VALUES, SOURCE_AMPLITUDE,
    COMP_A_TARGET, N_COUPLING_TYPES, KRETSCHNER_COEFF, MASS_COEFF,
    # Assumptions / nonclaims
    SOURCE_COUPLED_ASSUMPTIONS, SOURCE_COUPLED_NONCLAIMS,
    # Dataclasses
    SourceCoupledDefectParams, NormalizationMap,
    # Functions
    build_normalization_map,
    define_source_couplings,
    construct_sourced_lagrangian,
    derive_sourced_radial_ode,
    solve_sourced_bvp,
    extract_sourced_energy,
    assess_component_A_recovery,
    assess_component_B_preservation,
    scan_gamma,
    inventory_pathologies,
    classify_source_coupled,
    compute_source_coupled_defect,
    source_coupled_defect_result_to_dict,
)


@pytest.fixture(scope="module")
def params():
    return SourceCoupledDefectParams()


@pytest.fixture(scope="module")
def result():
    return compute_source_coupled_defect()


# ================================================================
# Section 1: Constants (5 tests)
# ================================================================

class TestConstants:
    def test_n_coupling_types(self):
        assert N_COUPLING_TYPES == 2

    def test_gamma_default(self):
        assert GAMMA_DEFAULT == 1.0

    def test_source_amplitude(self):
        assert SOURCE_AMPLITUDE == M_EXT

    def test_comp_a_target(self):
        assert COMP_A_TARGET > 1.0

    def test_eta_squared(self):
        assert abs(ETA_SQUARED - 1.0 / (8.0 * math.pi)) < 1e-10


# ================================================================
# Section 2: Normalization Map (6 tests)
# ================================================================

class TestNormalizationMap:
    def test_exists(self, result):
        assert result.normalization is not None

    def test_r_star(self, result):
        assert result.normalization.r_star == 1.0

    def test_x_star(self, result):
        assert abs(result.normalization.X_star - 0.5) < 1e-10

    def test_eta_value(self, result):
        assert abs(result.normalization.eta_value - ETA_TARGET) < 1e-10

    def test_source_nondim(self, result):
        assert "1/r_tilde^2" in result.normalization.source_nondim_formula

    def test_nondim_map_has_lambda_bar(self, result):
        assert "Lambda_bar" in result.normalization.nondim_map


# ================================================================
# Section 3: Source-Coupling Choices (5 tests)
# ================================================================

class TestSourceCouplingChoices:
    def test_exists(self, result):
        assert result.couplings is not None

    def test_two_couplings(self, result):
        assert len(result.couplings) == 2

    def test_quadratic_first(self, result):
        assert result.couplings[0].coupling_type == "quadratic"

    def test_quadratic_preserves_symmetry(self, result):
        assert result.couplings[0].symmetry_preserved

    def test_linear_breaks_symmetry(self, result):
        assert not result.couplings[1].symmetry_preserved


# ================================================================
# Section 4: Sourced Lagrangian (5 tests)
# ================================================================

class TestSourcedLagrangian:
    def test_exists(self, result):
        assert result.lagrangian is not None

    def test_four_terms(self, result):
        assert result.lagrangian.n_terms == 4

    def test_coupling_type(self, result):
        assert result.lagrangian.coupling_type == "quadratic"

    def test_source_formula(self, result):
        assert "/r^2" in result.lagrangian.source_formula

    def test_has_source_coupling_term(self, result):
        names = [t.name for t in result.lagrangian.terms]
        assert "source_coupling" in names


# ================================================================
# Section 5: Sourced Radial ODE (6 tests)
# ================================================================

class TestSourcedRadialODE:
    def test_exists(self, result):
        assert result.radial_equation is not None

    def test_source_sign_derived(self, result):
        assert result.radial_equation.source_term_sign == "-1"

    def test_sign_derivation_documented(self, result):
        deriv = result.radial_equation.sign_derivation
        assert "L_int" in deriv or "Euler" in deriv

    def test_full_ode_has_gamma(self, result):
        assert "gamma" in result.radial_equation.full_ode

    def test_unsourced_matches_d4(self, result):
        assert "lam*eta^2*f*(f^2-1)" in result.radial_equation.unsourced_ode

    def test_source_term_nonempty(self, result):
        assert len(result.radial_equation.source_term_formula) > 5


# ================================================================
# Section 6: BVP Convergence (5 tests)
# ================================================================

class TestBVPConvergence:
    def test_exists(self, result):
        assert result.baseline_bvp is not None

    def test_converged(self, result):
        assert result.baseline_bvp.converged

    def test_f_at_rmax(self, result):
        assert abs(result.baseline_bvp.f_at_rmax - 1.0) < 0.05

    def test_no_overshoot(self, result):
        assert result.baseline_bvp.f_max <= 1.05

    def test_residual_finite(self, result):
        assert math.isfinite(result.baseline_bvp.max_residual)


# ================================================================
# Section 7: Component A Recovery (6 tests)
# ================================================================

class TestComponentARecovery:
    def test_exists(self, result):
        assert result.comp_a_result is not None

    def test_shape_target(self, result):
        assert result.comp_a_result.shape_exponent_target == -4.0

    def test_shape_measured_negative(self, result):
        assert result.comp_a_result.shape_exponent_measured < 0

    def test_ratio_positive(self, result):
        assert result.comp_a_result.coeff_ratio > 0

    def test_ratio_insufficient(self, result):
        assert result.comp_a_result.coeff_ratio < 0.1

    def test_classification_honest(self, result):
        cl = result.comp_a_result.classification
        assert "insufficient" in cl or "partial" in cl


# ================================================================
# Section 8: Component B Preservation (6 tests)
# ================================================================

class TestComponentBPreservation:
    def test_exists(self, result):
        assert result.comp_b_result is not None

    def test_exponent_target(self, result):
        assert result.comp_b_result.exponent_target == -2.0

    def test_exponent_negative(self, result):
        assert result.comp_b_result.exponent_measured < 0

    def test_no_overshoot(self, result):
        assert not result.comp_b_result.f_overshoot

    def test_oscillation_free(self, result):
        assert result.comp_b_result.oscillation_free

    def test_classification_preserved(self, result):
        assert "preserved" in result.comp_b_result.classification


# ================================================================
# Section 9: Gamma Scan (6 tests)
# ================================================================

class TestGammaScan:
    def test_exists(self, result):
        assert result.gamma_scan is not None

    def test_nine_scanned(self, result):
        assert result.gamma_scan.n_scanned == 9

    def test_all_converged(self, result):
        assert result.gamma_scan.n_converged == 9

    def test_gamma_zero_baseline(self, result):
        assert result.gamma_scan.entries[0].gamma == 0.0

    def test_baseline_ratio_near_d4(self, result):
        assert abs(result.gamma_scan.entries[0].comp_A_ratio - 0.0035) < 0.002

    def test_best_ratio_ge_baseline(self, result):
        assert result.gamma_scan.best_ratio >= result.gamma_scan.entries[0].comp_A_ratio


# ================================================================
# Section 10: Pathologies & Classification (5 tests)
# ================================================================

class TestPathologiesClassification:
    def test_inventory_exists(self, result):
        assert result.pathology_inventory is not None

    def test_no_critical(self, result):
        assert result.pathology_inventory.n_critical == 0

    def test_at_least_one_documented(self, result):
        assert result.pathology_inventory.n_pathologies >= 1

    def test_classification_exists(self, result):
        assert result.classification is not None

    def test_phase_lock_has_d5(self, result):
        assert "source_coupled_D5" in result.classification.phase_lock_update


# ================================================================
# Section 11: Nonclaims & Serialization (5 tests)
# ================================================================

class TestNonclaimsSerialization:
    def test_ten_nonclaims(self, result):
        assert len(result.nonclaims) == 10

    def test_ten_assumptions(self, result):
        assert len(result.assumptions) == 10

    def test_serialization_valid(self, result):
        d = source_coupled_defect_result_to_dict(result)
        js = json.dumps(d, indent=2, default=str)
        assert len(js) > 100

    def test_serialization_has_normalization(self, result):
        d = source_coupled_defect_result_to_dict(result)
        assert "normalization" in d

    def test_serialization_has_classification(self, result):
        d = source_coupled_defect_result_to_dict(result)
        assert len(d["classification"]["classification"]) > 0
