"""Tests for DM branch discriminator — 5 tests selecting between Route 1 and Route 2."""

import numpy as np


def test_self_consistency_route2_shifts():
    """Route 2 self-consistent g_dark shifts significantly from naive value."""
    from grut_solver.sectors.dark_matter.branch_discriminator import anomaly_self_consistency
    r = anomaly_self_consistency()
    shift = abs(r["route_2"]["fractional_shift"])
    assert shift > 0.1, f"Expected >10% shift, got {100*shift:.1f}%"


def test_route1_stability():
    """Route 1 has stable Higgs eigenvalue (|λ_J| < 1)."""
    from grut_solver.sectors.dark_matter.branch_discriminator import fixed_point_stability
    r = fixed_point_stability()
    assert r["route_1"]["stable_higgs"]
    assert r["route_1"]["stability_margin_higgs"] > 0


def test_route2_stability_fails():
    """Route 2 Higgs eigenvalue is outside [-1, 1] (unstable)."""
    from grut_solver.sectors.dark_matter.branch_discriminator import fixed_point_stability
    r = fixed_point_stability()
    assert not r["route_2"]["stable_higgs"]


def test_naturalness_prefers_route1():
    """Route 1 lambda is more natural (closer to O(1))."""
    from grut_solver.sectors.dark_matter.branch_discriminator import naturalness_test
    r = naturalness_test()
    assert r["route_1"]["combined_score"] > r["route_2"]["combined_score"]


def test_anomaly_budget_route1_perturbative():
    """Route 1 dark sector is a perturbative correction to C_FINAL (<10%)."""
    from grut_solver.sectors.dark_matter.branch_discriminator import anomaly_budget
    r = anomaly_budget()
    assert r["route_1"]["perturbative"]


def test_anomaly_budget_route2_nonperturbative():
    """Route 2 dark sector is NOT perturbative (>10% of C_FINAL)."""
    from grut_solver.sectors.dark_matter.branch_discriminator import anomaly_budget
    r = anomaly_budget()
    assert not r["route_2"]["perturbative"]


def test_baryonic_route1_preserves_cosmology():
    """Route 1 preserves H_inf to within 15%."""
    from grut_solver.sectors.dark_matter.branch_discriminator import baryonic_consistency
    r = baryonic_consistency()
    assert abs(r["route_1"]["H_inf_shift_pct"]) < 15


def test_overall_verdict():
    """Overall verdict selects Route 1."""
    from grut_solver.sectors.dark_matter.branch_discriminator import full_branch_discrimination
    r = full_branch_discrimination()
    assert r["overall_preferred"] == "Route 1"
    assert r["tally"]["route_1"] >= 4
