"""Phase D11 -- Exact Two-Field Closure Tests.

60 tests across 11 classes, following the D9 test pattern.
Module-scoped fixture computes the full D11 result once.
"""

import math
import pytest
import numpy as np

from grut.exact_two_field_closure import (
    # Constants
    ALPHA_VAC, R_S, M_EXT, R_EQ, R_EXT, TAU_CANONICAL, A_CRIT,
    LAMBDA_DEFAULT, ETA_TARGET, XI_DEFAULT, RHO_EQ_COEFF, MASS_COEFF,
    MAX_ITERATIONS_DEFAULT, CONVERGENCE_TOL_DEFAULT,
    RELAXATION_FACTOR_DEFAULT, G_PORTAL_DEFAULT,
    G_PORTAL_SCAN_VALUES, LAMBDA_SCAN_VALUES,
    CLASSIFICATION_OPTIONS, D9_PROXY_ASSESSMENT_OPTIONS,
    EXACT_TWO_FIELD_ASSUMPTIONS, EXACT_TWO_FIELD_NONCLAIMS,
    # Dataclasses
    ExactTwoFieldParams, CoupledFieldEquations,
    ExactTwoFieldSolution, D9ComparisonResult, ExactMetricResult,
    ExactLambdaScanEntry, ExactLambdaScanResult,
    ExactPortalScanEntry, ExactPortalScanResult,
    D9RetrospectiveAssessment, ExactTwoFieldClassification,
    ExactTwoFieldResult,
    # Functions
    document_field_equations, solve_exact_two_field,
    compare_to_d9, inject_exact_metric,
    scan_lambda_exact, scan_portal_exact,
    assess_d9_retrospective, classify_exact_two_field,
    compute_exact_two_field, exact_two_field_result_to_dict,
)


# ================================================================
# Module-scoped fixture: compute once, reuse across all tests
# ================================================================

@pytest.fixture(scope="module")
def d11_result():
    """Compute the full D11 result once for all tests."""
    return compute_exact_two_field()


@pytest.fixture(scope="module")
def d11_params():
    """Default D11 parameters."""
    return ExactTwoFieldParams()


# ================================================================
# 1. TestConstants (5 tests)
# ================================================================

class TestConstants:
    """Verify inherited and D11-specific constants."""

    def test_r_eq(self):
        assert abs(R_EQ - 1.0 / 3.0) < 1e-12

    def test_tau_canonical(self):
        assert abs(TAU_CANONICAL - math.sqrt(1.5)) < 1e-12

    def test_rho_eq_coeff(self):
        expected = M_EXT ** 2 / (2 * TAU_CANONICAL ** 2)
        assert abs(RHO_EQ_COEFF - expected) < 1e-12

    def test_eta_target(self):
        expected = 1.0 / math.sqrt(8 * math.pi)
        assert abs(ETA_TARGET - expected) < 1e-12

    def test_lambda_default(self):
        assert abs(LAMBDA_DEFAULT - 8 * math.pi) < 1e-10


# ================================================================
# 2. TestFieldEquations (5 tests)
# ================================================================

class TestFieldEquations:
    """Verify field equations documentation (Level 0)."""

    def test_macro_equation_content(self, d11_result):
        fe = d11_result.field_equations
        assert "Phi" in fe.macro_equation
        assert "tau" in fe.macro_equation

    def test_defect_equation_content(self, d11_result):
        fe = d11_result.field_equations
        assert "f" in fe.defect_equation
        assert "lam" in fe.defect_equation

    def test_portal_sign_positive(self, d11_result):
        fe = d11_result.field_equations
        assert "positive" in fe.portal_sign_verification.lower()

    def test_source_status_fixed(self, d11_result):
        fe = d11_result.field_equations
        assert "FIXED" in fe.source_status

    def test_energy_density_convention(self, d11_result):
        fe = d11_result.field_equations
        assert "Phi" in fe.energy_density_convention


# ================================================================
# 3. TestExactSolution (6 tests)
# ================================================================

class TestExactSolution:
    """Verify the exact coupled BVP solution (Level 1)."""

    def test_converged(self, d11_result):
        assert d11_result.exact_solution.converged

    def test_method_is_string(self, d11_result):
        assert isinstance(d11_result.exact_solution.method, str)
        assert len(d11_result.exact_solution.method) > 0

    def test_r_grid_domain(self, d11_result):
        rg = d11_result.exact_solution.r_grid
        assert abs(rg[0] - R_EQ) < 0.01
        assert abs(rg[-1] - R_EXT) < 0.01

    def test_phi_positive(self, d11_result):
        assert np.all(d11_result.exact_solution.phi > 0)

    def test_f_defect_range(self, d11_result):
        f = d11_result.exact_solution.f_defect
        assert np.min(f) >= -0.01
        assert np.max(f) <= 1.01

    def test_epsilon_macro_positive(self, d11_result):
        assert np.all(d11_result.exact_solution.epsilon_macro > 0)


# ================================================================
# 4. TestLaplacianEnhancement (6 tests)
# ================================================================

class TestLaplacianEnhancement:
    """Verify the D8 Laplacian enhancement of Phi over M/r^2."""

    def test_phi_exceeds_uncoupled_at_Req(self, d11_result):
        es = d11_result.exact_solution
        idx = np.argmin(np.abs(es.r_grid - R_EQ))
        assert es.phi[idx] > M_EXT / R_EQ ** 2

    def test_phi_enhancement_ratio_lower_bound(self, d11_result):
        es = d11_result.exact_solution
        idx = np.argmin(np.abs(es.r_grid - R_EQ))
        ratio = es.phi[idx] / (M_EXT / R_EQ ** 2)
        assert ratio > 10

    def test_phi_enhancement_ratio_upper_bound(self, d11_result):
        es = d11_result.exact_solution
        idx = np.argmin(np.abs(es.r_grid - R_EQ))
        ratio = es.phi[idx] / (M_EXT / R_EQ ** 2)
        assert ratio < 100

    def test_eps_macro_much_larger_than_d9(self, d11_result):
        es = d11_result.exact_solution
        idx = np.argmin(np.abs(es.r_grid - R_EQ))
        eps_d9 = RHO_EQ_COEFF / R_EQ ** 4
        assert es.epsilon_macro[idx] / eps_d9 > 100

    def test_sigma_macro_dominates_sigma_defect(self, d11_result):
        es = d11_result.exact_solution
        assert es.sigma_macro_at_Req > 100 * es.sigma_defect_at_Req

    def test_phi_enhanced_at_rext(self, d11_result):
        es = d11_result.exact_solution
        idx = np.argmin(np.abs(es.r_grid - R_EXT))
        assert es.phi[idx] > M_EXT / R_EXT ** 2


# ================================================================
# 5. TestD9Comparison (6 tests)
# ================================================================

class TestD9Comparison:
    """Verify the D9 proxy comparison (Level 2)."""

    def test_both_metrics_positive(self, d11_result):
        dc = d11_result.d9_comparison
        assert dc.metric_positive_d11
        assert dc.metric_positive_d9

    def test_f_min_d11_positive(self, d11_result):
        assert d11_result.d9_comparison.f_min_d11 > 0

    def test_f_min_d9_positive(self, d11_result):
        assert d11_result.d9_comparison.f_min_d9 > 0

    def test_phi_deviation_large(self, d11_result):
        # The D8 Laplacian makes Phi very different from M/r^2
        assert d11_result.d9_comparison.phi_vs_proxy_max_deviation > 50

    def test_proxy_assessment_valid(self, d11_result):
        assert d11_result.d9_comparison.d9_proxy_assessment in D9_PROXY_ASSESSMENT_OPTIONS

    def test_proxy_quality_score_range(self, d11_result):
        score = d11_result.d9_comparison.proxy_quality_score
        assert 0.0 <= score <= 1.0


# ================================================================
# 6. TestMetricInjection (5 tests)
# ================================================================

class TestMetricInjection:
    """Verify metric injection from exact fields (Level 3)."""

    def test_metric_positive(self, d11_result):
        assert d11_result.metric_result.metric_positive

    def test_f_min_positive(self, d11_result):
        assert d11_result.metric_result.f_min > 0

    def test_f_min_at_boundary(self, d11_result):
        """Metric minimum is at R_EXT due to Laplacian enhancement."""
        assert abs(d11_result.metric_result.f_min_radius - R_EXT) < 0.1

    def test_f_at_Req_large(self, d11_result):
        """Interior metric is very large due to enhanced sigma_macro."""
        assert d11_result.metric_result.f_at_Req > 100

    def test_budget_nonempty(self, d11_result):
        assert len(d11_result.metric_result.budget) > 0


# ================================================================
# 7. TestLambdaScan (6 tests)
# ================================================================

class TestLambdaScan:
    """Verify lambda scan under exact closure (Level 4)."""

    def test_scanned_6_values(self, d11_result):
        assert d11_result.lambda_scan.n_scanned == 6

    def test_most_converged(self, d11_result):
        assert d11_result.lambda_scan.n_converged >= 5

    def test_all_positive_d11(self, d11_result):
        assert d11_result.lambda_scan.n_positive_d11 == 6

    def test_all_positive_d9(self, d11_result):
        assert d11_result.lambda_scan.n_positive_d9 == 6

    def test_viability_comparison_same(self, d11_result):
        assert d11_result.lambda_scan.viability_comparison == "same"

    def test_viable_windows_agree(self, d11_result):
        ls = d11_result.lambda_scan
        assert set(ls.viable_d11) == set(ls.viable_d9)


# ================================================================
# 8. TestPortalScan (6 tests)
# ================================================================

class TestPortalScan:
    """Verify portal coupling scan (Level 5)."""

    def test_scanned_5_values(self, d11_result):
        assert d11_result.portal_scan.n_scanned == 5

    def test_gp_zero_not_viable(self, d11_result):
        e0 = d11_result.portal_scan.entries[0]
        assert e0.g_portal == 0.0
        assert not e0.metric_positive

    def test_gp_01_viable(self, d11_result):
        e1 = d11_result.portal_scan.entries[1]
        assert abs(e1.g_portal - 0.1) < 1e-6
        assert e1.metric_positive

    def test_gp_10_viable(self, d11_result):
        e3 = d11_result.portal_scan.entries[3]
        assert abs(e3.g_portal - 1.0) < 1e-6
        assert e3.metric_positive

    def test_n_positive_at_least_4(self, d11_result):
        assert d11_result.portal_scan.n_positive >= 4

    def test_sensitivity_assessment_valid(self, d11_result):
        valid = {"mild_sensitivity", "moderate_sensitivity",
                 "significant_sensitivity", "destructive"}
        assert d11_result.portal_scan.sensitivity_assessment in valid


# ================================================================
# 9. TestRetrospective (5 tests)
# ================================================================

class TestRetrospective:
    """Verify D9 retrospective assessment (Level 6a)."""

    def test_assessment_valid(self, d11_result):
        assert d11_result.d9_retrospective.assessment in D9_PROXY_ASSESSMENT_OPTIONS

    def test_viability_agreement(self, d11_result):
        assert d11_result.d9_retrospective.viability_agreement

    def test_max_metric_discrepancy_bounded(self, d11_result):
        assert d11_result.d9_retrospective.max_metric_discrepancy < 0.2

    def test_parameter_window_identical(self, d11_result):
        assert d11_result.d9_retrospective.parameter_window_agreement == "identical"

    def test_summary_nonempty(self, d11_result):
        assert len(d11_result.d9_retrospective.summary) > 10


# ================================================================
# 10. TestClassification (6 tests)
# ================================================================

class TestClassification:
    """Verify final D11 classification (Level 6b)."""

    def test_classification_valid(self, d11_result):
        assert d11_result.classification.classification in CLASSIFICATION_OPTIONS

    def test_classification_supports_d9(self, d11_result):
        assert d11_result.classification.classification in {
            "exact_closure_achieved",
            "exact_closure_strongly_supports_d9",
        }

    def test_d9_viability_confirmed(self, d11_result):
        assert d11_result.classification.d9_viability_confirmed

    def test_exact_viability_across_lambda(self, d11_result):
        assert d11_result.classification.exact_viability_across_lambda

    def test_phase_lock_has_d11(self, d11_result):
        assert "exact_two_field_D11" in d11_result.classification.phase_lock_update

    def test_d9_assessment_valid(self, d11_result):
        assert d11_result.classification.d9_assessment in D9_PROXY_ASSESSMENT_OPTIONS


# ================================================================
# 11. TestNonclaimsSerialization (4 tests)
# ================================================================

class TestNonclaimsSerialization:
    """Verify nonclaims, assumptions, and serialization."""

    def test_assumptions_count(self, d11_result):
        assert len(d11_result.assumptions) == 10

    def test_nonclaims_count(self, d11_result):
        assert len(d11_result.nonclaims) == 10

    def test_serialization_valid(self, d11_result):
        d = exact_two_field_result_to_dict(d11_result)
        assert d["valid"] is True
        assert d["phase"] == "D11"

    def test_serialization_has_classification(self, d11_result):
        d = exact_two_field_result_to_dict(d11_result)
        assert "classification" in d
        assert d["classification"]["classification"] in CLASSIFICATION_OPTIONS
