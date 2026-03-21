"""Tests — Phase D6: Companion Architecture and Dual-Sector Metric Integration.

60 tests across 11 classes.
"""

import math
import json
import pytest

from grut.companion_architecture import (
    # Constants
    ALPHA_VAC, R_S, M_EXT, R_EQ, TAU_CANONICAL, A_CRIT,
    COMP_B_COEFF, ETA_TARGET, ETA_SQUARED, LAMBDA_DEFAULT,
    MASS_COEFF, RHO_EQ_COEFF, R_EXT, KRETSCHNER_COEFF,
    XI_DEFAULT, N_SECTORS, N_CROSS_TERMS,
    LAMBDA_SCAN_VALUES,
    # Assumptions / nonclaims
    COMPANION_ASSUMPTIONS, COMPANION_NONCLAIMS,
    # Dataclasses
    CompanionParams,
    # Functions
    define_architecture,
    verify_trigger_regime,
    construct_macro_sector,
    construct_defect_sector,
    decompose_dual_sector,
    analyze_sector_dominance,
    inject_companion_metric,
    scan_lambda_companion,
    inventory_cross_terms,
    classify_companion,
    compute_companion_architecture,
    companion_architecture_result_to_dict,
)


@pytest.fixture(scope="module")
def params():
    return CompanionParams()


@pytest.fixture(scope="module")
def result():
    return compute_companion_architecture()


# ================================================================
# Section 1: Constants (5 tests)
# ================================================================

class TestConstants:
    def test_n_sectors(self):
        assert N_SECTORS == 2

    def test_n_cross_terms(self):
        assert N_CROSS_TERMS == 4

    def test_a_crit(self):
        assert A_CRIT == 1.062

    def test_xi_default(self):
        assert XI_DEFAULT == 1.0

    def test_eta_squared(self):
        assert abs(ETA_SQUARED - 1.0 / (8.0 * math.pi)) < 1e-10


# ================================================================
# Section 2: Architecture Definition (5 tests)
# ================================================================

class TestArchitectureDefinition:
    def test_exists(self, result):
        assert result.architecture is not None

    def test_two_sectors(self, result):
        assert result.architecture.n_sectors == 2

    def test_additive_rule(self, result):
        assert "additive" in result.architecture.combination_rule.lower()

    def test_cross_terms_inventoried(self, result):
        assert "inventoried" in result.architecture.cross_term_treatment

    def test_sector_names(self, result):
        names = result.architecture.sector_names
        assert "macro_scalar_memory" in names
        assert "defect_hedgehog" in names


# ================================================================
# Section 3: Trigger Regime (7 tests)
# ================================================================

class TestTriggerRegime:
    def test_exists(self, result):
        assert result.trigger_regime is not None

    def test_sqrt_K_Req_positive(self, result):
        assert result.trigger_regime.sqrt_K_at_Req > 0

    def test_sqrt_K_Rext_positive(self, result):
        assert result.trigger_regime.sqrt_K_at_Rext > 0

    def test_core_dominates(self, result):
        assert result.trigger_regime.core_to_exterior_ratio > 10

    def test_K_crit_positive(self, result):
        assert result.trigger_regime.K_crit > 0

    def test_activation_radius_positive(self, result):
        assert result.trigger_regime.activation_radius > 0

    def test_active_at_Req(self, result):
        assert result.trigger_regime.active_at_Req


# ================================================================
# Section 4: Macro Sector (6 tests)
# ================================================================

class TestMacroSector:
    def test_baseline_exists(self, result):
        assert result.macro_baseline is not None

    def test_critical_exists(self, result):
        assert result.macro_critical is not None

    def test_baseline_label(self, result):
        assert result.macro_baseline.label == "baseline_A1"

    def test_critical_label(self, result):
        assert result.macro_critical.label == "critical_Acrit"

    def test_sigma_baseline_positive(self, result):
        assert result.macro_baseline.sigma_at_Req > 0

    def test_sigma_critical_gt_baseline(self, result):
        assert result.macro_critical.sigma_at_Req > result.macro_baseline.sigma_at_Req


# ================================================================
# Section 5: Defect Sector (6 tests)
# ================================================================

class TestDefectSector:
    def test_exists(self, result):
        assert result.defect_sector is not None

    def test_bvp_converged(self, result):
        assert result.defect_sector.bvp_converged

    def test_sigma_positive(self, result):
        assert result.defect_sector.sigma_at_Req > 0

    def test_tail_exponent_negative(self, result):
        assert result.defect_sector.tail_exponent < 0

    def test_tail_coefficient_positive(self, result):
        assert result.defect_sector.tail_coefficient > 0

    def test_interior_grid_400(self, result):
        assert len(result.defect_sector.r_interior) == 400


# ================================================================
# Section 6: Dual-Sector Decomposition (6 tests)
# ================================================================

class TestDualSectorDecomposition:
    def test_A1_exists(self, result):
        assert result.decomposition_A1 is not None

    def test_Acrit_exists(self, result):
        assert result.decomposition_Acrit is not None

    def test_A1_ratio_positive(self, result):
        assert result.decomposition_A1.epsilon_ratio_mean > 0

    def test_Acrit_ratio_ge_A1(self, result):
        assert (result.decomposition_Acrit.epsilon_ratio_mean
                >= result.decomposition_A1.epsilon_ratio_mean)

    def test_sigma_total_A1_positive(self, result):
        assert float(result.decomposition_A1.sigma_total[0]) > 0

    def test_sigma_total_Acrit_ge_A1(self, result):
        assert (float(result.decomposition_Acrit.sigma_total[0])
                >= float(result.decomposition_A1.sigma_total[0]))


# ================================================================
# Section 7: Sector Dominance (5 tests)
# ================================================================

class TestSectorDominance:
    def test_exists(self, result):
        assert result.dominance is not None

    def test_crossover_gt_Req(self, result):
        assert result.dominance.crossover_radius > R_EQ

    def test_crossover_reasonable(self, result):
        assert result.dominance.crossover_radius < R_EXT + 1.0

    def test_macro_dominates_inner(self, result):
        assert result.dominance.macro_dominates_inner

    def test_ratio_Req_gt_one(self, result):
        assert result.dominance.ratio_at_Req > 1.0


# ================================================================
# Section 8: Metric Injection (6 tests)
# ================================================================

class TestMetricInjection:
    def test_A1_exists(self, result):
        assert result.metric_A1 is not None

    def test_Acrit_exists(self, result):
        assert result.metric_Acrit is not None

    def test_fmin_A1_finite(self, result):
        assert math.isfinite(result.metric_A1.f_min)

    def test_fmin_Acrit_ge_A1(self, result):
        assert result.metric_Acrit.f_min >= result.metric_A1.f_min - 1e-10

    def test_budget_at_Req(self, result):
        assert f"r={R_EQ:.4f}" in result.metric_A1.budget

    def test_budget_has_delta(self, result):
        key = f"r={R_EQ:.4f}"
        assert "delta" in result.metric_A1.budget.get(key, {})


# ================================================================
# Section 9: Lambda Scan (6 tests)
# ================================================================

class TestLambdaScan:
    def test_exists(self, result):
        assert result.lambda_scan is not None

    def test_six_scanned(self, result):
        assert result.lambda_scan.n_scanned == 6

    def test_all_converged(self, result):
        assert result.lambda_scan.n_converged == 6

    def test_Acrit_ge_A1_positive(self, result):
        assert (result.lambda_scan.n_positive_Acrit
                >= result.lambda_scan.n_positive_A1)

    def test_best_lambda_A1_in_scan(self, result):
        assert result.lambda_scan.best_lambda_A1 in LAMBDA_SCAN_VALUES

    def test_best_lambda_Acrit_in_scan(self, result):
        assert result.lambda_scan.best_lambda_Acrit in LAMBDA_SCAN_VALUES


# ================================================================
# Section 10: Cross-Terms & Classification (5 tests)
# ================================================================

class TestCrossTermsClassification:
    def test_cross_terms_exists(self, result):
        assert result.cross_terms is not None

    def test_four_cross_terms(self, result):
        assert result.cross_terms.n_cross_terms == 4

    def test_additive_not_justified(self, result):
        assert not result.cross_terms.additive_approximation_justified

    def test_classification_exists(self, result):
        assert result.classification is not None

    def test_phase_lock_has_d6(self, result):
        assert "companion_D6" in result.classification.phase_lock_update


# ================================================================
# Section 11: Nonclaims & Serialization (3 tests)
# ================================================================

class TestNonclaimsSerialization:
    def test_ten_nonclaims(self, result):
        assert len(result.nonclaims) == 10

    def test_ten_assumptions(self, result):
        assert len(result.assumptions) == 10

    def test_serialization_valid(self, result):
        d = companion_architecture_result_to_dict(result)
        js = json.dumps(d, indent=2, default=str)
        assert len(js) > 100
