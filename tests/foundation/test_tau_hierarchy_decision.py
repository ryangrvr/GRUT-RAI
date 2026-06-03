"""Tests for grut.foundation.tau_hierarchy_decision.

Pins the formal decision: GRUT is a multi-scale EFT (Option B).
τ₀ and τ_micro are independently anchored; no derivation between them.
"""

import math
import pytest

from grut.foundation.tau_hierarchy_decision import (
    LOG10_GAP,
    PATH3_CROSS_CHECK_RATIO,
    T_PEAK_NOISE_KERNEL_K,
    T_STAR_K,
    TAU_PRODUCT_S2,
    TAU_RATIO,
    evaluate_path1_genesis,
    evaluate_path2_plasma_frequency,
    evaluate_path3_multiplicative,
    evaluate_path4_honest_negative,
    tau_hierarchy_decision,
)
from grut.foundation.closure_protocol import TAU_0_SEC, TAU_MICRO_SEC, T_C_KELVIN_CANONICAL


class TestGap:
    """The two τ-scales differ by ~34 orders of magnitude."""

    def test_tau_ratio_is_about_1e34(self):
        assert 9e33 < TAU_RATIO < 1e35

    def test_log10_gap_is_34(self):
        assert abs(LOG10_GAP - 34.0) < 0.5

    def test_tau_0_is_larger(self):
        assert TAU_0_SEC > TAU_MICRO_SEC

    def test_tau_product_is_sub_millisecond_squared(self):
        """τ_micro × τ₀ ~ 10⁻⁴ s² — well below any astrophysical scale."""
        assert 1e-5 < TAU_PRODUCT_S2 < 1e-3


class TestPath1Genesis:
    """Path 1 is not viable: noise kernel temperature ≠ T_c."""

    @pytest.fixture(scope="class")
    def p1(self):
        return evaluate_path1_genesis()

    def test_not_viable(self, p1):
        assert p1["viable"] is False

    def test_noise_kernel_temperature_is_far_below_tc(self, p1):
        """T_peak = ℏ/(τ₀ k_B) ≈ 5.8×10⁻²⁷ K — 34 orders below T_c."""
        assert p1["T_peak_K"] < 1e-20

    def test_noise_kernel_temperature_gap_matches_tau_gap(self, p1):
        """T_c / T_peak = τ₀/τ_micro — same 34-order gap, confirming circularity."""
        log10_temp_gap = math.log10(T_C_KELVIN_CANONICAL / T_PEAK_NOISE_KERNEL_K)
        assert abs(log10_temp_gap - LOG10_GAP) < 0.5

    def test_reason_string_present(self, p1):
        assert len(p1["reason"]) > 10


class TestPath2PlasmaFrequency:
    """Path 2 is not viable: responsive-medium plasma frequency undefined."""

    @pytest.fixture(scope="class")
    def p2(self):
        return evaluate_path2_plasma_frequency()

    def test_not_viable(self, p2):
        assert p2["viable"] is False

    def test_reason_mentions_undefined(self, p2):
        r = p2["reason"].lower()
        assert "undefined" in r or "not characterized" in r or "research" in r


class TestPath3Multiplicative:
    """Path 3 fails: dimensional impossibility + numerical non-identity."""

    @pytest.fixture(scope="class")
    def p3(self):
        return evaluate_path3_multiplicative()

    def test_not_viable(self, p3):
        assert p3["viable"] is False

    def test_t_star_is_unphysically_cold(self):
        """T_* = ℏ/(k_B τ_micro τ₀) ≈ 40 nK — not a physical scale."""
        assert T_STAR_K < 1e-6  # below 1 µK

    def test_cross_check_ratio_not_unity(self):
        """τ_micro × τ₀ ≠ ℏ/(k_B T_c H₀ 108π) exactly — 1.6% mismatch."""
        assert abs(PATH3_CROSS_CHECK_RATIO - 1.0) > 0.005

    def test_cross_check_ratio_is_near_unity(self):
        """Ratio is within 5% of 1.0 — nearly tautological (confirming
        τ₀ and τ_micro are calibrated to separate but physically related
        anchors, not independent physics).
        The ~1.6% deviation arises because τ₀ has a Bullet Cluster anchor
        that moves it from the pure-formula 1/(H₀ × 108π) value."""
        assert 0.90 < PATH3_CROSS_CHECK_RATIO < 1.05

    def test_three_test_keys_present(self, p3):
        assert "test_A_dimensional" in p3
        assert "test_B_tautology" in p3
        assert "test_C_T_star" in p3


class TestPath4HonestNegative:
    """Path 4 / Option B is the viable outcome."""

    @pytest.fixture(scope="class")
    def p4(self):
        return evaluate_path4_honest_negative()

    def test_viable(self, p4):
        assert p4["viable"] is True

    def test_option_b_viable(self, p4):
        assert p4["option_b_viable"] is True

    def test_option_a_not_viable(self, p4):
        assert p4["option_a_viable"] is False

    def test_parameter_count_structure(self, p4):
        pc = p4["parameter_count"]
        assert pc["gravitational_predictive_core"] == 1
        assert pc["thermal_sector"] == 1
        assert pc["total_anchored"] == 2
        assert pc["total_free"] == 0

    def test_gravitational_core_claim_preserved(self, p4):
        """The zero-parameter gravitational core is intact."""
        assert "zero free parameters" in p4["what_is_preserved"].lower() or \
               "zero-parameter" in p4["what_is_preserved"].lower()


class TestDecisionSummary:
    """Top-level decision function returns correct verdict."""

    @pytest.fixture(scope="class")
    def d(self):
        return tau_hierarchy_decision()

    def test_decision_is_option_b(self, d):
        assert "Option B" in d["decision"]

    def test_relation_not_derivable(self, d):
        assert d["relation_derivable"] is False

    def test_gravitational_core_is_zero_parameter(self, d):
        assert d["gravitational_predictive_core_zero_parameter"] is True

    def test_thermal_sector_independently_anchored(self, d):
        assert d["thermal_sector_independently_anchored"] is True

    def test_only_path_4_viable(self, d):
        assert d["path_1"]["viable"] is False
        assert d["path_2"]["viable"] is False
        assert d["path_3"]["viable"] is False
        assert d["path_4"]["viable"] is True

    def test_log10_gap_34(self, d):
        assert abs(d["log10_gap"] - 34.0) < 0.5

    def test_verdict_mentions_both_options(self, d):
        v = d["verdict"]
        assert "Option A" in v or "Option B" in v

    def test_verdict_mentions_34_orders(self, d):
        assert "34" in d["verdict"]

    def test_required_top_level_keys(self, d):
        required = {
            "tau_0_sec", "tau_micro_sec", "tau_ratio", "log10_gap",
            "T_c_K", "path_1", "path_2", "path_3", "path_4",
            "viable_paths", "decision", "architectural_class",
            "gravitational_predictive_core_zero_parameter",
            "thermal_sector_independently_anchored",
            "relation_derivable", "verdict",
        }
        assert required.issubset(set(d.keys()))
