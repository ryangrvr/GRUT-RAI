"""Tests — Phase D9: Self-Consistent Coupled Profile Integration.

60 tests across 11 classes.
"""

import json
import pytest

from grut.self_consistent_coupling import (
    compute_self_consistent,
    self_consistent_result_to_dict,
    define_coupled_solver,
    solve_self_consistent,
    assess_profile_deformation,
    inject_self_consistent_metric,
    scan_lambda_self_consistent,
    scan_portal_strength,
    classify_self_consistent,
    SelfConsistentParams,
    SelfConsistentResult,
    CLASSIFICATION_OPTIONS,
    G_PORTAL_SCAN_VALUES,
    LAMBDA_SCAN_VALUES,
    SELF_CONSISTENT_ASSUMPTIONS,
    SELF_CONSISTENT_NONCLAIMS,
)


@pytest.fixture(scope="module")
def params():
    return SelfConsistentParams()


@pytest.fixture(scope="module")
def result(params):
    return compute_self_consistent(params)


# ================================================================
# TestConstants (5 tests)
# ================================================================

class TestConstants:
    def test_g_portal_scan_size(self):
        assert len(G_PORTAL_SCAN_VALUES) == 4

    def test_lambda_scan_size(self):
        assert len(LAMBDA_SCAN_VALUES) == 6

    def test_classification_options(self):
        assert len(CLASSIFICATION_OPTIONS) == 5

    def test_default_relaxation(self):
        p = SelfConsistentParams()
        assert abs(p.relaxation_factor - 0.5) < 1e-10

    def test_default_g_portal(self):
        p = SelfConsistentParams()
        assert abs(p.g_portal - 1.0) < 1e-10


# ================================================================
# TestSolverDefinition (5 tests)
# ================================================================

class TestSolverDefinition:
    def test_exists(self, result):
        assert result.solver_definition is not None

    def test_proxy_closure(self, result):
        assert "proxy" in result.solver_definition.proxy_closure_statement.lower()

    def test_sign_analysis(self, result):
        assert "positive" in result.solver_definition.sign_analysis.lower()

    def test_relaxation_scheme(self, result):
        assert "omega" in result.solver_definition.under_relaxation_scheme.lower()

    def test_modified_ode(self, result):
        assert "g_portal" in result.solver_definition.modified_ode


# ================================================================
# TestSelfConsistentSolution (7 tests)
# ================================================================

class TestSelfConsistentSolution:
    def test_exists(self, result):
        assert result.profile_solution is not None

    def test_converged(self, result):
        assert result.profile_solution.converged

    def test_iterations_positive(self, result):
        assert result.profile_solution.n_iterations > 0

    def test_residual_below_tol(self, result, params):
        assert result.profile_solution.final_residual < params.convergence_tol

    def test_sigma_defect_positive(self, result):
        assert result.profile_solution.sigma_defect_at_Req > 0

    def test_a_eff_amplified(self, result, params):
        assert result.profile_solution.A_eff_at_Req > params.scalar_A

    def test_history_populated(self, result):
        assert len(result.profile_solution.convergence_history) > 0


# ================================================================
# TestProfileDeformation (6 tests)
# ================================================================

class TestProfileDeformation:
    def test_exists(self, result):
        assert result.deformation is not None

    def test_shift_max_nonneg(self, result):
        assert result.deformation.f_shift_max >= 0

    def test_shift_rms_nonneg(self, result):
        assert result.deformation.f_shift_rms >= 0

    def test_crossover_frozen_positive(self, result):
        assert result.deformation.crossover_radius_frozen > 0

    def test_classification_valid(self, result):
        assert result.deformation.deformation_classification in [
            "negligible", "moderate", "significant", "large"
        ]

    def test_sigma_shift_finite(self, result):
        assert abs(result.deformation.sigma_defect_shift) < 100


# ================================================================
# TestMetricInjection (6 tests)
# ================================================================

class TestMetricInjection:
    def test_exists(self, result):
        assert result.metric_result is not None

    def test_f_min_finite(self, result):
        assert abs(result.metric_result.f_min) < 1000

    def test_f_at_req_finite(self, result):
        assert abs(result.metric_result.f_at_Req) < 1000

    def test_budget_exists(self, result):
        assert len(result.metric_result.budget) > 0

    def test_metric_shift_finite(self, result):
        assert abs(result.metric_result.metric_shift_from_d7) < 100

    def test_metric_positive_is_bool(self, result):
        assert isinstance(result.metric_result.metric_positive, bool)


# ================================================================
# TestLambdaScan (6 tests)
# ================================================================

class TestLambdaScan:
    def test_exists(self, result):
        assert result.lambda_scan is not None

    def test_six_scanned(self, result):
        assert result.lambda_scan.n_scanned == 6

    def test_all_converged(self, result):
        assert result.lambda_scan.n_converged == 6

    def test_d7_viable(self, result):
        assert result.lambda_scan.n_positive_d7 >= 4

    def test_sc_viable_positive(self, result):
        assert result.lambda_scan.n_positive_sc > 0

    def test_threshold_valid(self, result):
        assert result.lambda_scan.threshold_shift in [
            "unchanged", "lower", "higher", "destroyed", "shifted"
        ]


# ================================================================
# TestPortalScan (5 tests)
# ================================================================

class TestPortalScan:
    def test_exists(self, result):
        assert result.portal_scan is not None

    def test_four_scanned(self, result):
        assert result.portal_scan.n_scanned == 4

    def test_g0_exists(self, result):
        entries = result.portal_scan.entries
        assert any(abs(e.g_portal) < 1e-10 for e in entries)

    def test_g0_positive(self, result):
        e0 = [e for e in result.portal_scan.entries if abs(e.g_portal) < 1e-10][0]
        assert e0.metric_positive

    def test_sensitivity_valid(self, result):
        assert result.portal_scan.sensitivity_assessment in [
            "insensitive", "mild_sensitivity",
            "moderate_sensitivity", "high_sensitivity"
        ]


# ================================================================
# TestClassification (6 tests)
# ================================================================

class TestClassification:
    def test_exists(self, result):
        assert result.classification is not None

    def test_valid_string(self, result):
        assert result.classification.classification in CLASSIFICATION_OPTIONS

    def test_phase_lock_d9(self, result):
        assert "self_consistent_D9" in result.classification.phase_lock_update

    def test_phase_lock_d8(self, result):
        assert "coupled_action_D8" in result.classification.phase_lock_update

    def test_proxy_flagged(self, result):
        assert result.classification.proxy_closure_used is True

    def test_deformation_level(self, result):
        assert result.classification.deformation_level in [
            "negligible", "moderate", "significant", "large"
        ]


# ================================================================
# TestD7Recovery (5 tests)
# ================================================================

class TestD7Recovery:
    def test_frozen_exists(self, result):
        assert result.frozen_solution is not None

    def test_frozen_g0(self, result):
        assert abs(result.frozen_solution.g_portal) < 1e-10

    def test_frozen_zero_iterations(self, result):
        assert result.frozen_solution.n_iterations == 0

    def test_frozen_converged(self, result):
        assert result.frozen_solution.converged

    def test_frozen_in_portal_scan(self, result):
        e0 = [e for e in result.portal_scan.entries if abs(e.g_portal) < 1e-10][0]
        assert e0.converged


# ================================================================
# TestNonclaimsSerialization (4 tests)
# ================================================================

class TestNonclaimsSerialization:
    def test_ten_nonclaims(self, result):
        assert len(result.nonclaims) == 10

    def test_ten_assumptions(self, result):
        assert len(result.assumptions) == 10

    def test_serialization_valid(self, result):
        d = self_consistent_result_to_dict(result)
        s = json.dumps(d)
        assert s is not None

    def test_serialization_has_classification(self, result):
        d = self_consistent_result_to_dict(result)
        assert "classification" in d


# ================================================================
# TestPhysicsConsistency (5 tests)
# ================================================================

class TestPhysicsConsistency:
    def test_portal_stabilizing(self, result):
        # SC sigma_defect should differ from frozen
        assert abs(result.deformation.sigma_defect_shift) > 0

    def test_metric_close_to_d7(self, result):
        mr = result.metric_result
        assert abs(mr.f_min - mr.f_d7_at_Req) / max(abs(mr.f_d7_at_Req), 0.01) < 0.5

    def test_rescue_preserved(self, result):
        assert result.lambda_scan.rescue_preserved

    def test_no_nan_history(self, result):
        for x in result.profile_solution.convergence_history:
            if isinstance(x, float):
                assert x == x  # NaN check

    def test_relaxation_valid(self, result):
        assert 0 < result.profile_solution.relaxation_used <= 1.0
