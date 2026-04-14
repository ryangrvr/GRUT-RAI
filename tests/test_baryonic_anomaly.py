"""
Tests for baryonic anomaly computation — R_B and eta_B.

Tests the two-route computation of the baryonic anomaly ratio
and the assembled baryon asymmetry.
"""

import numpy as np
import pytest


def test_abj_coefficient():
    """ABJ anomaly coefficient = N_gen/(16π²) to high precision."""
    from grut_solver.sectors.baryogenesis.baryonic_anomaly import abj_anomaly_coefficient
    k_b = abj_anomaly_coefficient()
    expected = 3.0 / (16.0 * np.pi**2)
    assert abs(k_b - expected) / expected < 1e-14


def test_baryonic_field_content():
    """SM baryonic field content: 36 quark Weyl, B²-weighted = 4."""
    from grut_solver.sectors.baryogenesis.baryonic_anomaly import sm_baryonic_field_content
    fc = sm_baryonic_field_content()
    assert fc["n_quark_weyl"] == 36
    assert fc["n_lepton_weyl"] == 9
    assert fc["n_total_weyl"] == 45
    assert abs(fc["b2_quarks"] - 4.0) < 1e-10
    assert abs(fc["f_fermion"] - 4.0 / 45.0) < 1e-10


def test_c_b_final_in_range():
    """C_B_final from scaling is in reasonable range [10⁻⁶, 10⁻³]."""
    from grut_solver.sectors.baryogenesis.baryonic_anomaly import c_b_final_scaling
    r1 = c_b_final_scaling()
    assert 1e-6 < abs(r1["c_b_final"]) < 1e-3


def test_r_b_positive_both_routes():
    """R_B is positive and finite for both routes."""
    from grut_solver.sectors.baryogenesis.baryonic_anomaly import (
        c_b_final_scaling, r_baryonic_route2,
    )
    r1 = c_b_final_scaling()
    r2 = r_baryonic_route2()
    assert r1["r_b"] > 0
    assert np.isfinite(r1["r_b"])
    assert r2["r_b"] > 0
    assert np.isfinite(r2["r_b"])


def test_sphaleron_rate():
    """Sphaleron rate matches expected order: κ α_W⁵ T⁴ at T_EW."""
    from grut_solver.sectors.baryogenesis.baryonic_anomaly import (
        sphaleron_rate, T_EW, ALPHA_W_MZ, KAPPA_SPHALERON,
    )
    gamma = sphaleron_rate(T_EW)
    # Expected order: 25 × (0.034 × 160)⁴ ~ 25 × 5.4⁴ ~ 25 × 850 ~ 2e4 GeV⁴
    assert gamma > 0
    assert 1e2 < gamma < 1e8  # reasonable range


def test_jarlskog():
    """Jarlskog invariant is 3.18e-5."""
    from grut_solver.sectors.baryogenesis.baryonic_anomaly import jarlskog_invariant
    j = jarlskog_invariant()
    assert abs(j["J_CP"] - 3.18e-5) / 3.18e-5 < 0.01


def test_k_neq_physical_range():
    """Nonequilibrium factor K_neq is in physical range [10⁻⁴, 1]."""
    from grut_solver.sectors.baryogenesis.baryonic_anomaly import k_neq_constitutive
    kn = k_neq_constitutive()
    assert 1e-4 < kn["k_neq"] < 1.0


def test_eta_computed_positive():
    """eta_B is computed and positive for both routes."""
    from grut_solver.sectors.baryogenesis.baryonic_anomaly import both_routes_comparison
    comp = both_routes_comparison()
    assert comp["route_1"]["eta_predicted"] > 0
    assert comp["route_2"]["eta_predicted"] > 0


def test_inverse_constraint():
    """Inverse constraint gives (2-R_B)/S_B ~ 10⁻⁵ from observation."""
    from grut_solver.sectors.baryogenesis.baryonic_anomaly import eta_from_observation_constraint
    inv = eta_from_observation_constraint()
    ratio = inv["required_ratio"]
    # Should be O(10⁻⁵) to O(10⁻³) depending on K_neq
    assert 1e-8 < abs(ratio) < 1e-1


def test_full_analysis_runs():
    """Full baryonic anomaly analysis runs without error."""
    from grut_solver.sectors.baryogenesis.baryonic_anomaly import full_baryonic_anomaly_analysis
    result = full_baryonic_anomaly_analysis()
    assert result["status"].startswith("COMPUTED")
    assert len(result["derived"]) >= 4
    assert len(result["results"]) >= 4
    assert len(result["honest_negatives"]) >= 3
    # Check summary values are finite
    for key in ["r_b_route1", "r_b_route2", "eta_route1", "eta_route2"]:
        assert np.isfinite(result["summary"][key])
