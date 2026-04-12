"""Tests for Sector 9: Solitonic Dark Matter."""
import sys; sys.path.insert(0, ".")
import numpy as np


def test_fixed_points():
    from grut_solver.sectors.dark_matter.soliton_dark_matter import find_fixed_points
    fp = find_fixed_points()
    assert fp["n_stable"] == 2
    assert fp["n_unstable"] == 1
    print(f"  PASS: {fp['n_stable']} stable + {fp['n_unstable']} unstable fixed points")

def test_domain_wall_bps():
    from grut_solver.sectors.dark_matter.soliton_dark_matter import domain_wall_analytical
    x = np.linspace(-10, 10, 500)
    w = domain_wall_analytical(x)
    ratio = w["total_energy"] / w["sigma_analytical"]
    assert abs(ratio - 1.0) < 0.02
    print(f"  PASS: BPS bound matched to {abs(ratio-1)*100:.1f}%")

def test_wall_connects_minima():
    from grut_solver.sectors.dark_matter.soliton_dark_matter import domain_wall_analytical
    x = np.linspace(-20, 20, 1000)
    w = domain_wall_analytical(x)
    assert abs(w["z"][0] - (-1.0)) < 0.01
    assert abs(w["z"][-1] - 1.0) < 0.01
    print(f"  PASS: wall connects z={w['z'][0]:.3f} to z={w['z'][-1]:.3f}")

def test_energy_positive_finite():
    from grut_solver.sectors.dark_matter.soliton_dark_matter import domain_wall_analytical
    x = np.linspace(-10, 10, 500)
    w = domain_wall_analytical(x)
    assert w["total_energy"] > 0
    assert np.isfinite(w["total_energy"])
    print(f"  PASS: energy = {w['total_energy']:.4f} (positive, finite)")

def test_soliton_width():
    from grut_solver.sectors.dark_matter.soliton_dark_matter import domain_wall_analytical, soliton_radius
    x = np.linspace(-10, 10, 500)
    w = domain_wall_analytical(x)
    r = soliton_radius(w)
    assert r > 0
    assert r < 20
    print(f"  PASS: soliton width = {r:.2f}")

def test_topological_stability():
    from grut_solver.sectors.dark_matter.soliton_dark_matter import soliton_stability
    s = soliton_stability()
    assert s["stable"]
    assert s["topological_charge"] == 1
    print(f"  PASS: topological charge = {s['topological_charge']}, stable = {s['stable']}")

def test_constitutive_survival():
    from grut_solver.sectors.dark_matter.soliton_dark_matter import soliton_time_evolution
    ev = soliton_time_evolution(noise_amp=0.05, n_steps=2000)
    assert ev["survived"]
    assert ev["charge_preserved"]
    print(f"  PASS: survived {ev['n_steps']} steps, E_ratio={ev['energy_ratio']:.3f}")

def test_physical_mass_finite():
    from grut_solver.sectors.dark_matter.soliton_dark_matter import soliton_physical_mass
    p = soliton_physical_mass(1.0, 100.0)
    assert np.isfinite(p["M_GeV"])
    assert p["M_GeV"] > 0
    print(f"  PASS: M = {p['M_GeV']:.2e} GeV (superheavy range)")

def test_numerical_solver():
    from grut_solver.sectors.dark_matter.soliton_dark_matter import domain_wall_numerical
    w = domain_wall_numerical(L=10, N=200)
    assert w["total_energy"] > 0
    assert np.isfinite(w["total_energy"])
    print(f"  PASS: numerical solver energy = {w['total_energy']:.4f}")

def test_parameter_scan_runs():
    from grut_solver.sectors.dark_matter.soliton_dark_matter import parameter_scan
    s = parameter_scan(n_lam=5, n_v=5)
    assert s["n_total"] == 25
    print(f"  PASS: scan {s['n_viable']}/{s['n_total']} viable (superheavy mass range)")


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
    print(f"DM Solitons: {passed} passed, {failed} failed, {passed+failed} total")
