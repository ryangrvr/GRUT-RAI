"""Tests — Phase D2: Numerical Monopole Integration.

57 tests across 10 classes.
"""

import math
import json
import pytest
import numpy as np

from grut.numerical_monopole import (
    # Constants
    ALPHA_VAC, R_S, M_EXT, R_EQ, TAU_CANONICAL, A_CRIT, A_CRIT_SQUARED,
    COMP_B_COEFF, ETA_MATCH, ETA_MATCH_SQUARED, MASS_COEFF, R_EXT,
    LAMBDA_SCAN_VALUES, PHASE6_F_AT_REQ, KEY_RADII,
    # Assumptions / nonclaims
    MONOPOLE_ASSUMPTIONS, MONOPOLE_NONCLAIMS,
    # Dataclasses
    NumericalMonopoleParams,
    # Functions
    compute_core_series,
    solve_hedgehog_bvp,
    extract_defect_energy,
    inject_into_metric,
    run_both_coupling_cases,
    scan_lambda,
    check_compatibility,
    classify_numerical_monopole,
    compute_numerical_monopole,
    numerical_monopole_result_to_dict,
)


@pytest.fixture(scope="module")
def params():
    return NumericalMonopoleParams()


@pytest.fixture(scope="module")
def result():
    return compute_numerical_monopole()


# ================================================================
# Section 1: Constants (6 tests)
# ================================================================

class TestConstants:
    def test_eta_match(self):
        assert abs(ETA_MATCH - 1.0 / math.sqrt(8.0 * math.pi)) < 1e-10

    def test_eta_squared_is_comp_b(self):
        assert abs(ETA_MATCH_SQUARED - COMP_B_COEFF) < 1e-10

    def test_mass_coeff(self):
        expected = 2.0 * math.pi * M_EXT ** 2 / TAU_CANONICAL ** 2
        assert abs(MASS_COEFF - expected) < 1e-8

    def test_R_ext(self):
        assert abs(R_EXT - 2.0 * R_S) < 1e-10

    def test_lambda_scan_count(self):
        assert len(LAMBDA_SCAN_VALUES) == 6

    def test_phase6_baseline(self):
        """Verify Phase 6 f(R_eq) ~ -17.71 from mass profile."""
        m_req = M_EXT + MASS_COEFF * (1.0 / R_EQ - 1.0 / R_EXT)
        f_req = 1.0 - 2.0 * m_req / R_EQ
        assert abs(f_req - PHASE6_F_AT_REQ) < 0.01


# ================================================================
# Section 2: Core Series Expansion (5 tests)
# ================================================================

class TestCoreSeries:
    def test_core_series_exists(self, result):
        assert result.core_series is not None

    def test_c1_positive(self, result):
        assert result.core_series.c1_estimate > 0

    def test_c3_negative(self, result):
        assert result.core_series.c3_value < 0

    def test_c3_formula(self, result):
        assert "lam * eta^2 * c1 / 10" in result.core_series.c3_formula

    def test_series_at_rmin_small(self, result):
        assert 0 < result.core_series.series_at_rmin < 0.1


# ================================================================
# Section 3: BVP Solver (6 tests)
# ================================================================

class TestBVPSolver:
    def test_bvp_exists(self, result):
        assert result.bvp_solution is not None

    def test_bvp_converged(self, result):
        assert result.bvp_solution.converged

    def test_max_residual_small(self, result):
        assert result.bvp_solution.max_residual < 1e-4

    def test_c1_effective_positive(self, result):
        assert result.bvp_solution.c1_effective > 0

    def test_f_at_rmax(self, result):
        assert abs(result.bvp_solution.f_at_rmax - 1.0) < 1e-4

    def test_f_at_rmin_near_zero(self, result):
        assert abs(result.bvp_solution.f_solution[0]) < 0.02


# ================================================================
# Section 4: Energy Decomposition (6 tests)
# ================================================================

class TestEnergyDecomposition:
    def test_energy_exists(self, result):
        assert result.energy_profile is not None

    def test_core_peak_positive(self, result):
        assert result.energy_profile.core_peak > 0

    def test_integrated_mass_positive(self, result):
        assert result.energy_profile.integrated_mass > 0

    def test_radial_kinetic_nonneg(self, result):
        assert np.all(result.energy_profile.radial_kinetic >= 0)

    def test_angular_gradient_nonneg(self, result):
        assert np.all(result.energy_profile.angular_gradient >= 0)

    def test_potential_nonneg(self, result):
        assert np.all(result.energy_profile.potential_term >= 0)


# ================================================================
# Section 5: Tail Verification (6 tests)
# ================================================================

class TestTailVerification:
    def test_tail_exponent_range(self, result):
        """Tail exponent should be between -2.5 and -1.0."""
        exp = result.energy_profile.tail_exponent
        assert -2.5 < exp < -1.0

    def test_tail_coefficient_approx(self, result):
        """Tail coefficient should approximate eta^2."""
        coeff = result.energy_profile.tail_coefficient
        assert abs(coeff - ETA_MATCH_SQUARED) / ETA_MATCH_SQUARED < 0.15

    def test_high_lambda_tail(self, result):
        """At lambda=200, tail should be within 0.05 of -2.0."""
        high = [e for e in result.lambda_scan.entries if e.lam == 200.0]
        assert len(high) == 1
        assert abs(high[0].tail_exponent - (-2.0)) < 0.05

    def test_core_peak_increases_with_lambda(self, result):
        entries = result.lambda_scan.entries
        peaks = [e.core_peak for e in entries]
        assert all(peaks[i] <= peaks[i + 1] + 1e-6
                   for i in range(len(peaks) - 1))

    def test_tail_exponent_monotonic(self, result):
        """Tail exponent should decrease toward -2 as lambda increases."""
        exponents = [e.tail_exponent for e in result.lambda_scan.entries]
        assert all(exponents[i] >= exponents[i + 1]
                   for i in range(len(exponents) - 1))

    def test_tail_exponent_approaches_minus_2(self, result):
        """Highest lambda tail exponent should be closer to -2 than lowest."""
        entries = result.lambda_scan.entries
        assert abs(entries[-1].tail_exponent - (-2.0)) < \
               abs(entries[0].tail_exponent - (-2.0))


# ================================================================
# Section 6: Metric Injection (7 tests)
# ================================================================

class TestMetricInjection:
    def test_injection_A_exists(self, result):
        assert result.injection_A is not None

    def test_injection_B_exists(self, result):
        assert result.injection_B is not None

    def test_case_A_mode(self, result):
        assert result.injection_A.coupling_mode == "case_A"

    def test_case_B_mode(self, result):
        assert result.injection_B.coupling_mode == "case_B"

    def test_case_A_scalar_amplitude(self, result):
        assert abs(result.injection_A.scalar_amplitude - A_CRIT) < 0.01

    def test_case_B_scalar_amplitude(self, result):
        assert abs(result.injection_B.scalar_amplitude - 1.0) < 0.01

    def test_defect_fraction_valid(self, result):
        """Defect fraction at R_eq should be in (0, 1)."""
        frac_key = f"r={R_EQ:.4f}"
        frac = result.injection_A.defect_fraction.get(frac_key, -1.0)
        assert 0 < frac < 1


# ================================================================
# Section 7: Lambda Scan (6 tests)
# ================================================================

class TestLambdaScan:
    def test_scan_exists(self, result):
        assert result.lambda_scan is not None

    def test_scan_count(self, result):
        assert result.lambda_scan.n_scanned == 6

    def test_all_converged(self, result):
        assert result.lambda_scan.n_converged == 6

    def test_case_A_at_least_as_good(self, result):
        """Case A should have at least as many positive as Case B."""
        assert result.lambda_scan.n_positive_A >= result.lambda_scan.n_positive_B

    def test_at_least_one_positive_A(self, result):
        assert result.lambda_scan.n_positive_A >= 1

    def test_defect_fraction_increases(self, result):
        """Defect fraction at R_eq should increase with lambda."""
        fracs = [e.defect_sigma_fraction_at_Req
                 for e in result.lambda_scan.entries]
        assert all(fracs[i] <= fracs[i + 1] + 1e-6
                   for i in range(len(fracs) - 1))


# ================================================================
# Section 8: Compatibility (5 tests)
# ================================================================

class TestCompatibility:
    def test_compatibility_exists(self, result):
        assert result.compatibility is not None

    def test_component_A_intact(self, result):
        assert result.compatibility.component_A_intact

    def test_coupling_additive(self, result):
        assert result.compatibility.coupling_is_additive

    def test_locked_results_preserved(self, result):
        assert result.compatibility.locked_results_preserved

    def test_defect_shape_reasonable(self, result):
        """Defect tail should be at least roughly 1/r^2 shaped."""
        exp = result.energy_profile.tail_exponent
        assert abs(exp - (-2.0)) < 0.5


# ================================================================
# Section 9: Classification (6 tests)
# ================================================================

class TestClassification:
    def test_classification_exists(self, result):
        assert result.classification is not None

    def test_classification_nonempty(self, result):
        assert len(result.classification.classification) > 0

    def test_phase_status_nonempty(self, result):
        assert len(result.classification.phase_status) > 0

    def test_summary_nonempty(self, result):
        assert len(result.classification.summary) > 10

    def test_phase_lock_has_d2(self, result):
        assert "defect_D2" in result.classification.phase_lock_update

    def test_result_valid(self, result):
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
        d = numerical_monopole_result_to_dict(result)
        js = json.dumps(d, indent=2, default=str)
        assert len(js) > 100

    def test_serialization_classification(self, result):
        d = numerical_monopole_result_to_dict(result)
        assert len(d["classification"]["classification"]) > 0

    def test_serialization_lambda_scan(self, result):
        d = numerical_monopole_result_to_dict(result)
        assert d["lambda_scan"]["n_scanned"] == 6
