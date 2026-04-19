"""Tests for the baryogenesis sector — V7 §31 predictions.

Route 1: eta_B = 6.57e-10 (+7.7% vs observed 6.1e-10)
All three Sakharov conditions structural: B violation, CP asymmetry, non-eq.
"""

import pytest
import numpy as np


class TestEtaB:
    """Tests for compute_eta_b — the baryon asymmetry prediction."""

    def test_route_1_returns_expected_keys(self):
        from grut.derived.baryogenesis.eta import compute_eta_b
        result = compute_eta_b(route=1)
        expected = {"eta_B", "eta_observed", "deviation_pct",
                     "R_B", "S_B", "J_CP", "K_neq", "route", "status"}
        assert expected.issubset(result.keys())

    def test_route_1_eta_close_to_observed(self):
        """V7: eta_B = 6.57e-10, observed = 6.1e-10, deviation ~8%."""
        from grut.derived.baryogenesis.eta import compute_eta_b
        result = compute_eta_b(route=1)
        # V7 claims +7.7% deviation
        assert abs(result["deviation_pct"]) < 10.0

    def test_route_1_eta_positive(self):
        from grut.derived.baryogenesis.eta import compute_eta_b
        result = compute_eta_b(route=1)
        assert result["eta_B"] > 0

    def test_observed_eta_is_6p1e_minus_10(self):
        """Observed baryon asymmetry: 6.1e-10."""
        from grut.derived.baryogenesis.eta import compute_eta_b
        result = compute_eta_b(route=1)
        assert abs(result["eta_observed"] - 6.1e-10) / 6.1e-10 < 0.1

    def test_route_2_runs(self):
        from grut.derived.baryogenesis.eta import compute_eta_b
        result = compute_eta_b(route=2)
        assert "eta_B" in result

    def test_route_2_overshoots(self):
        """V7: Route 2 overshoots observed eta (hence Route 1 preferred)."""
        from grut.derived.baryogenesis.eta import compute_eta_b
        result = compute_eta_b(route=2)
        # Route 2 gives ~1.3e-9, ~2.2x observed
        assert result["eta_B"] > 1e-9

    def test_J_CP_is_SM_value(self):
        """Jarlskog invariant J_CP ≈ 3.18e-5 from SM."""
        from grut.derived.baryogenesis.eta import compute_eta_b
        result = compute_eta_b(route=1)
        assert abs(result["J_CP"] - 3.18e-5) / 3.18e-5 < 0.1


class TestGrutVsObservation:
    """Tests for the full observational crosscheck."""

    def test_returns_both_routes_and_measurements(self):
        from grut.derived.baryogenesis.crosscheck import grut_vs_observation
        result = grut_vs_observation()
        assert "grut_route1" in result
        assert "grut_route2" in result
        assert "measurements" in result

    def test_future_discrimination_runs(self):
        from grut.derived.baryogenesis.crosscheck import future_discrimination
        result = future_discrimination()
        assert isinstance(result, (dict, list))

    def test_parameter_sensitivity_runs(self):
        from grut.derived.baryogenesis.crosscheck import parameter_sensitivity
        result = parameter_sensitivity()
        assert isinstance(result, (dict, list))

    def test_model_comparison_runs(self):
        from grut.derived.baryogenesis.crosscheck import model_comparison
        result = model_comparison()
        assert isinstance(result, (dict, list))

    def test_lithium_problem_flagged(self):
        """V7 Track VIII honest negative: lithium-7 tension (+15%)."""
        from grut.derived.baryogenesis.crosscheck import lithium_problem
        result = lithium_problem()
        assert isinstance(result, dict)

    def test_full_crosscheck_runs(self):
        from grut.derived.baryogenesis.crosscheck import full_baryogenesis_crosscheck
        result = full_baryogenesis_crosscheck()
        assert isinstance(result, dict)
