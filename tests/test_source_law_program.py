"""Tests — Source-Law Program I (Loophole 5: X != M/r^2).

57 tests across 10 classes.  Mirrors the benchmark structure.
"""

import math
import json
import pytest
import numpy as np

from grut.source_law_program import (
    # Constants
    ALPHA_VAC, R_S, M_EXT, R_EQ, TAU_CANONICAL, A_CRIT,
    RHO_EQ_COEFF, EPSILON_RC_COEFF, COMP_B_COEFF, PHI_GOLDEN,
    N_SOURCE_FAMILIES, COMPONENT_B_TARGET_EXPONENT, LOCKED_EXPONENT,
    DIAGNOSTIC_B_COEFF,
    # Assumptions / nonclaims
    SOURCE_LAW_ASSUMPTIONS, SOURCE_LAW_NONCLAIMS,
    # Dataclasses
    SourceLawParams,
    # Functions
    define_target,
    build_source_family_specs,
    run_diagnostic_toy_probe,
    compute_family_shape,
    build_source_family_taxonomy,
    rank_candidates,
    assess_grut_nativeness,
    classify_source_law,
    compute_source_law_assessment,
    source_law_result_to_dict,
    make_radial_grid,
    _fit_spatial_exponent,
    _compute_epsilon_from_source,
)


@pytest.fixture(scope="module")
def params():
    return SourceLawParams()


@pytest.fixture(scope="module")
def result():
    return compute_source_law_assessment()


# ================================================================
# Section 1: Constants (5 tests)
# ================================================================

class TestConstants:
    def test_alpha_vac(self):
        assert abs(ALPHA_VAC - 1.0 / 3.0) < 1e-10

    def test_m_ext(self):
        assert abs(M_EXT - 0.5) < 1e-10

    def test_tau_canonical(self):
        assert abs(TAU_CANONICAL - math.sqrt(1.5)) < 1e-10

    def test_comp_b_coeff(self):
        assert abs(COMP_B_COEFF - 1.0 / (8.0 * math.pi)) < 1e-10

    def test_n_source_families(self):
        assert N_SOURCE_FAMILIES == 5


# ================================================================
# Section 2: Target Definition (5 tests)
# ================================================================

class TestTargetDefinition:
    def test_target_exists(self, result):
        assert result.target is not None

    def test_target_epsilon_exponent(self, result):
        assert result.target.target_epsilon_exponent == -2.0

    def test_required_source_exponent(self, result):
        assert result.target.required_source_exponent == -1.0

    def test_standard_source_exponent(self, result):
        assert result.target.standard_source_exponent == -2.0

    def test_standard_epsilon_exponent(self, result):
        assert result.target.standard_epsilon_exponent == -4.0


# ================================================================
# Section 3: Diagnostic Toy Probe (7 tests)
# ================================================================

class TestDiagnosticToyProbe:
    def test_probe_exists(self, result):
        assert result.diagnostic_probe is not None

    def test_B_value(self, result):
        assert abs(result.diagnostic_probe.B_value - DIAGNOSTIC_B_COEFF) < 1e-10

    def test_component_A_coeff(self, result):
        expected = A_CRIT ** 2 / (2.0 * TAU_CANONICAL ** 2) * M_EXT ** 2
        assert abs(result.diagnostic_probe.component_A_coeff - expected) / expected < 1e-4

    def test_component_B_coeff(self, result):
        expected = A_CRIT ** 2 / (2.0 * TAU_CANONICAL ** 2) * DIAGNOSTIC_B_COEFF ** 2
        assert abs(result.diagnostic_probe.component_B_coeff - expected) / expected < 1e-4

    def test_cross_term_coeff(self, result):
        expected = A_CRIT ** 2 / (2.0 * TAU_CANONICAL ** 2) * 2.0 * M_EXT * DIAGNOSTIC_B_COEFF
        assert abs(result.diagnostic_probe.cross_term_coeff - expected) / expected < 1e-4

    def test_inner_exponent_near_minus_4(self, result):
        dp = result.diagnostic_probe
        assert abs(dp.fitted_exponent_inner - (-4.0)) < abs(dp.fitted_exponent_inner - (-2.0))

    def test_probe_confirms_mechanism(self, result):
        assert result.diagnostic_probe.probe_confirms_mechanism


# ================================================================
# Section 4: Family 1 — Local Algebraic (6 tests)
# ================================================================

class TestFamily1Algebraic:
    def test_family_name(self, result):
        assert result.taxonomy.shape_results[0].family_name == "local_algebraic"

    def test_p1_epsilon_exponent(self, result):
        sub = result.taxonomy.shape_results[0].sub_exponents
        assert abs(sub["p=1.00_epsilon"] - (-4.0)) < 0.01

    def test_p05_epsilon_exponent(self, result):
        sub = result.taxonomy.shape_results[0].sub_exponents
        assert abs(sub["p=0.50_epsilon"] - (-2.0)) < 0.01

    def test_p075_epsilon_exponent(self, result):
        sub = result.taxonomy.shape_results[0].sub_exponents
        assert abs(sub["p=0.75_epsilon"] - (-3.0)) < 0.01

    def test_p025_epsilon_exponent(self, result):
        sub = result.taxonomy.shape_results[0].sub_exponents
        assert abs(sub["p=0.25_epsilon"] - (-1.0)) < 0.01

    def test_best_power_is_05(self, result):
        assert result.taxonomy.shape_results[0].algebraic_power_used == 0.5


# ================================================================
# Section 5: Family 2 — Gradient/Derivative (5 tests)
# ================================================================

class TestFamily2Gradient:
    def test_family_name(self, result):
        assert result.taxonomy.shape_results[1].family_name == "gradient_derivative"

    def test_cannot_produce_1_over_r(self, result):
        assert not result.taxonomy.shape_results[1].can_produce_1_over_r

    def test_d_dr_exponent(self, result):
        sub = result.taxonomy.shape_results[1].sub_exponents
        assert abs(sub["d/dr_exponent"] - (-3.0)) < 0.01

    def test_d2_dr2_exponent(self, result):
        sub = result.taxonomy.shape_results[1].sub_exponents
        assert abs(sub["d2/dr2_exponent"] - (-4.0)) < 0.01

    def test_epsilon_steeper_than_target(self, result):
        assert result.taxonomy.shape_results[1].epsilon_exponent < -2.0


# ================================================================
# Section 6: Family 3 — Cumulative/Integral (6 tests)
# ================================================================

class TestFamily3Integral:
    def test_family_name(self, result):
        assert result.taxonomy.shape_results[2].family_name == "cumulative_integral"

    def test_cannot_produce_pure_1_over_r(self, result):
        assert not result.taxonomy.shape_results[2].can_produce_1_over_r

    def test_one_over_r_coeff_positive(self, result):
        sub = result.taxonomy.shape_results[2].sub_exponents
        assert sub["one_over_r_coeff"] > 0

    def test_constant_offset_positive(self, result):
        sub = result.taxonomy.shape_results[2].sub_exponents
        assert sub["constant_offset"] > 0

    def test_epsilon_shallower_than_target(self, result):
        assert result.taxonomy.shape_results[2].epsilon_exponent > -2.0

    def test_constant_offset_value(self, result, params):
        sub = result.taxonomy.shape_results[2].sub_exponents
        expected = params.integral_lambda * params.M / params.integral_r_min
        assert abs(sub["constant_offset"] - expected) / expected < 1e-4


# ================================================================
# Section 7: Family 4 — Defect/Topological (6 tests)
# ================================================================

class TestFamily4Defect:
    def test_family_name(self, result):
        assert result.taxonomy.shape_results[3].family_name == "defect_topological"

    def test_can_produce_1_over_r(self, result):
        assert result.taxonomy.shape_results[3].can_produce_1_over_r

    def test_Q_only_epsilon_exponent(self, result):
        sub = result.taxonomy.shape_results[3].sub_exponents
        assert abs(sub["Q_only_epsilon_exponent"] - (-2.0)) < 0.01

    def test_comp_B_from_Q(self, result, params):
        sub = result.taxonomy.shape_results[3].sub_exponents
        prefactor = A_CRIT ** 2 / (2.0 * TAU_CANONICAL ** 2)
        expected = prefactor * params.defect_Q ** 2
        assert abs(sub["comp_B_from_Q"] - expected) / expected < 1e-4

    def test_full_epsilon_between_minus4_and_minus2(self, result):
        exp = result.taxonomy.shape_results[3].epsilon_exponent
        assert -4.0 < exp < -2.0

    def test_full_source_between_minus2_and_minus1(self, result):
        exp = result.taxonomy.shape_results[3].source_exponent
        assert -2.0 < exp < -1.0


# ================================================================
# Section 8: Family 5 — Processing-Invariant (5 tests)
# ================================================================

class TestFamily5Processing:
    def test_family_name(self, result):
        assert result.taxonomy.shape_results[4].family_name == "processing_lag_invariant"

    def test_cannot_produce_1_over_r(self, result):
        assert not result.taxonomy.shape_results[4].can_produce_1_over_r

    def test_source_exponent_standard(self, result):
        assert abs(result.taxonomy.shape_results[4].source_exponent - (-2.0)) < 0.01

    def test_epsilon_exponent_standard(self, result):
        assert abs(result.taxonomy.shape_results[4].epsilon_exponent - (-4.0)) < 0.01

    def test_deviation_is_2(self, result):
        assert abs(result.taxonomy.shape_results[4].deviation_from_target - 2.0) < 0.01


# ================================================================
# Section 9: Candidate Ranking & GRUT-Nativeness (6 tests)
# ================================================================

class TestRankingNativeness:
    def test_ranking_exists(self, result):
        assert result.ranking is not None

    def test_top_candidate(self, result):
        assert result.ranking.top_candidate_name == "local_algebraic"

    def test_no_grut_native_viable(self, result):
        assert not result.ranking.any_grut_native_viable

    def test_nativeness_exists(self, result):
        assert result.nativeness is not None

    def test_zero_grut_native_viable(self, result):
        assert result.nativeness.n_grut_native_viable == 0

    def test_two_non_native_viable(self, result):
        assert result.nativeness.n_non_native_viable == 2


# ================================================================
# Section 10: Final Classification & Nonclaims (6 tests)
# ================================================================

class TestClassificationNonclaims:
    def test_classification_exists(self, result):
        assert result.classification is not None

    def test_loophole_5_partially_viable(self, result):
        assert result.classification.loophole_5_status == "partially_viable"

    def test_classification_string(self, result):
        assert result.classification.classification == (
            "source_law_loophole_5_partially_viable__no_grut_native_mechanism"
        )

    def test_two_viable_families(self, result):
        assert result.classification.n_viable_families == 2

    def test_ten_nonclaims(self, result):
        assert len(result.nonclaims) == 10

    def test_ten_assumptions(self, result):
        assert len(result.assumptions) == 10
