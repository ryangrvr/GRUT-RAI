"""Tests for Sector 9: Gauged Dark Matter (U(1)_dark)."""
import sys; sys.path.insert(0, ".")
import numpy as np


def test_route_1_lambda_natural():
    from grut_solver.sectors.dark_matter.gauge_dark_matter import route_1_rg_running
    r = route_1_rg_running()
    assert 0.01 < r["lambda"] < 10, f"lambda = {r['lambda']} not natural"
    print(f"  PASS: Route 1 lambda = {r['lambda']:.4f} (natural)")

def test_route_2_lambda_natural():
    from grut_solver.sectors.dark_matter.gauge_dark_matter import route_2_anomaly_extraction
    r = route_2_anomaly_extraction()
    assert 0.01 < r["lambda"] < 10, f"lambda = {r['lambda']} not natural"
    print(f"  PASS: Route 2 lambda = {r['lambda']:.4f} (natural)")

def test_route_1_bullet_ok():
    from grut_solver.sectors.dark_matter.gauge_dark_matter import route_1_rg_running
    r = route_1_rg_running()
    assert r["bullet_ok"], f"sigma/m = {r['sigma_over_m']}"
    print(f"  PASS: Route 1 sigma/m = {r['sigma_over_m']:.4e} (Bullet OK)")

def test_route_2_bullet_ok():
    from grut_solver.sectors.dark_matter.gauge_dark_matter import route_2_anomaly_extraction
    r = route_2_anomaly_extraction()
    assert r["bullet_ok"], f"sigma/m = {r['sigma_over_m']}"
    print(f"  PASS: Route 2 sigma/m = {r['sigma_over_m']:.4e} (Bullet OK)")

def test_s_k_at_boundary():
    from grut_solver.sectors.dark_matter.gauge_dark_matter import route_1_rg_running
    r = route_1_rg_running()
    assert abs(r["S_K"] - 1.0) < 0.01, f"S_K = {r['S_K']}"
    print(f"  PASS: S_K = {r['S_K']:.4f}")

def test_mass_superheavy():
    from grut_solver.sectors.dark_matter.gauge_dark_matter import both_routes
    r = both_routes()
    m_low, m_high = r["mass_range_GeV"]
    assert m_low > 1e6, f"M_low = {m_low}"
    assert m_high < 1e12, f"M_high = {m_high}"
    print(f"  PASS: M range = {m_low:.1e} - {m_high:.1e} GeV")

def test_dark_photon_mass():
    from grut_solver.sectors.dark_matter.gauge_dark_matter import route_1_rg_running
    r = route_1_rg_running()
    assert r["dark_photon_mass_MeV"] > 0
    assert r["dark_photon_mass_MeV"] < 10000  # below 10 GeV
    print(f"  PASS: dark photon m_A = {r['dark_photon_mass_MeV']:.0f} MeV")

def test_both_viable():
    from grut_solver.sectors.dark_matter.gauge_dark_matter import both_routes
    r = both_routes()
    assert r["both_viable"]
    assert r["both_natural_lambda"]
    print(f"  PASS: both routes viable and natural")


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    passed = failed = 0
    for t in tests:
        try:
            t()
            passed += 1
        except Exception as e:
            print(f"  FAIL: {t.__name__}: {e}")
            failed += 1
    print(f"\n{'='*60}")
    print(f"Gauged DM: {passed} passed, {failed} failed, {passed+failed} total")
