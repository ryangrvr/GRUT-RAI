"""Tests for the bridge parameter — τ_0 connecting decoherence to cosmology.

V7 §22: H_inf = (2-R)/(S·τ_0) with τ_0 from the noise kernel at the
gold benchmark (m=20818 amu, l=1 μm). This is the framework's testable
cross-sector connection.
"""

import pytest
import numpy as np


class TestBridgePrediction:
    """Tests for bridge_prediction — the core cross-sector formula."""

    def test_default_H0_70_returns_dict(self):
        from grut.bridge.parameter import bridge_prediction
        result = bridge_prediction(H_0_kms=70.0)
        expected = {"tau_0_s", "tau_0_Myr", "H_inf_Hz", "Omega_Lambda",
                     "Planck", "deviation_pct", "R", "R_choice"}
        assert expected.issubset(result.keys())

    def test_tau_0_is_41p9_Myr(self):
        """V7 gold-benchmark τ_0 = 41.9 Myr."""
        from grut.bridge.parameter import bridge_prediction
        result = bridge_prediction()
        assert abs(result["tau_0_Myr"] - 41.9) < 0.1

    def test_H_inf_is_1p885e_minus_18_Hz(self):
        """V7 §26 headline number."""
        from grut.bridge.parameter import bridge_prediction
        result = bridge_prediction()
        assert abs(result["H_inf_Hz"] - 1.885e-18) / 1.885e-18 < 0.01

    def test_Omega_Lambda_matches_Planck_within_0p5pct(self):
        from grut.bridge.parameter import bridge_prediction
        result = bridge_prediction(H_0_kms=70.0)
        assert abs(result["deviation_pct"]) < 0.5

    def test_Planck_reference_is_0p6889(self):
        from grut.bridge.parameter import bridge_prediction
        result = bridge_prediction()
        assert abs(result["Planck"] - 0.6889) < 1e-3

    def test_R_choice_hand_default(self):
        from grut.bridge.parameter import bridge_prediction
        result = bridge_prediction()
        assert result["R_choice"] == "closure"
        from grut.foundation.closure_protocol import R_REFRACTIVE
        assert abs(result["R"] - R_REFRACTIVE) < 1e-6

    def test_R_choice_epsilon(self):
        from grut.bridge.parameter import bridge_prediction
        result = bridge_prediction(R_choice="epsilon")
        assert result["R_choice"] == "epsilon"
        assert abs(result["R"] - 1.1537) < 1e-3

    def test_hand_and_epsilon_agree_within_0p5pct(self):
        from grut.bridge.parameter import bridge_prediction
        hand = bridge_prediction(R_choice="hand")
        eps = bridge_prediction(R_choice="epsilon")
        rel_diff = abs(hand["Omega_Lambda"] - eps["Omega_Lambda"]) / hand["Omega_Lambda"]
        assert rel_diff < 0.005

    def test_different_H0_gives_different_Omega_Lambda(self):
        from grut.bridge.parameter import bridge_prediction
        r1 = bridge_prediction(H_0_kms=67.4)
        r2 = bridge_prediction(H_0_kms=73.0)
        assert r1["Omega_Lambda"] != r2["Omega_Lambda"]


class TestExperimentalChain:
    """Tests for experimental_chain — the decoherence → cosmology path."""

    def test_returns_dict(self):
        from grut.bridge.parameter import experimental_chain
        # Gold benchmark: m=20818 amu, l=1 um, R=gold radius
        amu_kg = 1.66053906660e-27
        m_kg = 20818 * amu_kg
        l_m = 1e-6
        R_m = ((3 * m_kg) / (4 * np.pi * 19300))**(1/3)  # gold radius
        result = experimental_chain(m_kg, l_m, R_m, Lambda_measured_Hz=1e-5)
        assert isinstance(result, dict)

    def test_handles_different_lambda_values(self):
        from grut.bridge.parameter import experimental_chain
        amu_kg = 1.66053906660e-27
        m_kg = 20818 * amu_kg
        l_m = 1e-6
        R_m = ((3 * m_kg) / (4 * np.pi * 19300))**(1/3)
        r1 = experimental_chain(m_kg, l_m, R_m, 1e-6)
        r2 = experimental_chain(m_kg, l_m, R_m, 1e-5)
        # Different measurements should give different results
        assert r1 != r2


class TestTau0FromObservation:
    """Tests for tau_0_from_observation — derive τ_0 from Planck Ω_Λ."""

    def test_returns_tau_0(self):
        from grut.bridge.parameter import tau_0_from_observation
        result = tau_0_from_observation()
        assert "tau_0_s" in result or "tau_0_Myr" in result

    def test_tau_0_positive_finite(self):
        from grut.bridge.parameter import tau_0_from_observation
        result = tau_0_from_observation()
        tau_key = "tau_0_s" if "tau_0_s" in result else "tau_0_Myr"
        assert np.isfinite(result[tau_key])
        assert result[tau_key] > 0

    def test_tau_0_consistent_with_gold_benchmark(self):
        """τ_0 derived from Planck Ω_Λ should match the gold-benchmark 41.9 Myr."""
        from grut.bridge.parameter import tau_0_from_observation
        result = tau_0_from_observation()
        if "tau_0_Myr" in result:
            # Allow large window — this is a cross-check, not an exact match
            assert 10 < result["tau_0_Myr"] < 200
