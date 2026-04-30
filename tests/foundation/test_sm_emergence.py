"""Tests for grut.foundation.sm_emergence — five-constraint consistency
check that promotes sm_emergence from anchored to computed.

The five CTP-derived constraints (V7 §15-§16):
  C1 gauge structure
  C2 anomaly cancellation
  C3 three generations
  C4 hierarchical mass ratios
  C5 constitutive consistency

These tests verify the SM as encoded in the framework satisfies all
five — necessary for the uniqueness claim, which itself remains
anchored in V7 prose beyond the present scope.
"""

from fractions import Fraction
import pytest

from grut.foundation.sm_emergence import (
    all_constraints,
    constraint_c1_gauge_structure,
    constraint_c2_anomaly_cancellation,
    constraint_c3_three_generations,
    constraint_c4_koide_K_two_thirds,
    constraint_c5_constitutive_consistency,
    summary_report,
    verify,
)


class TestConstraintC1GaugeStructure:
    def test_passes(self):
        r = constraint_c1_gauge_structure()
        assert r["passes"]

    def test_total_gauge_bosons_is_12(self):
        r = constraint_c1_gauge_structure()
        assert r["observed"] == 12
        assert r["expected"] == 12

    def test_decomposition_matches_8_3_1(self):
        r = constraint_c1_gauge_structure()
        assert "SU(3)" in r["detail"]
        assert "SU(2)" in r["detail"]
        assert "U(1)" in r["detail"]


class TestConstraintC2AnomalyCancellation:
    def test_passes(self):
        r = constraint_c2_anomaly_cancellation()
        assert r["passes"]

    def test_sum_Y_squared_is_10(self):
        r = constraint_c2_anomaly_cancellation()
        assert r["sum_Y_squared"] == 10

    def test_beta_U1_is_20_over_3(self):
        r = constraint_c2_anomaly_cancellation()
        assert r["beta_U1"] == "20/3"


class TestConstraintC3ThreeGenerations:
    def test_passes(self):
        r = constraint_c3_three_generations()
        assert r["passes"]

    def test_15_per_generation(self):
        r = constraint_c3_three_generations()
        assert r["fermions_per_gen"] == 15

    def test_3_generations(self):
        r = constraint_c3_three_generations()
        assert r["n_generations"] == 3

    def test_total_45(self):
        r = constraint_c3_three_generations()
        assert r["total_observed"] == 45


class TestConstraintC4KoideTwoThirds:
    def test_passes(self):
        r = constraint_c4_koide_K_two_thirds()
        assert r["passes"]

    def test_K_within_target_band(self):
        r = constraint_c4_koide_K_two_thirds()
        assert abs(r["K_observed"] - 2.0 / 3.0) / (2.0 / 3.0) < 0.01

    def test_deviation_is_tiny(self):
        r = constraint_c4_koide_K_two_thirds()
        assert r["deviation_pct"] < 0.01


class TestConstraintC5ConstitutiveConsistency:
    def test_passes(self):
        r = constraint_c5_constitutive_consistency()
        assert r["passes"]

    def test_a_duff_is_1991_over_2(self):
        r = constraint_c5_constitutive_consistency()
        assert r["a_duff"] == "1991/2"

    def test_c_ks_is_849(self):
        r = constraint_c5_constitutive_consistency()
        assert r["c_ks"] == "849"


class TestAggregation:
    def test_all_five_pass(self):
        v = verify()
        assert v["all_five_pass"]

    def test_each_constraint_passes(self):
        v = verify()
        for key, val in v.items():
            assert val, f"{key} failed"

    def test_all_constraints_returns_five_reports(self):
        reports = all_constraints()
        assert len(reports) == 5

    def test_each_constraint_has_passes_field(self):
        for r in all_constraints():
            assert "passes" in r
            assert isinstance(r["passes"], bool)

    def test_summary_report_says_all_pass(self):
        s = summary_report()
        assert s["all_pass"] is True

    def test_summary_describes_uniqueness_caveat(self):
        s = summary_report()
        # Make sure the summary surfaces the necessary-not-sufficient framing
        assert "uniqueness" in s["claim_status"].lower() or \
               "UNIQUENESS" in s["claim_status"]
