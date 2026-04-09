"""
Sector 1 — Quantum Mechanics Recovery: Validation Test Suite

Every test reports: quantity, expected, measured, error metric, pass/fail.
"""

import numpy as np
import sys
sys.path.insert(0, ".")


# ── Test 1: Constitutive parameter sanity ──────────────────────

def test_constitutive_params():
    """Constitutive parameters are dimensionally consistent."""
    from grut_solver.sectors.qm.constitutive_qm import constitutive_params
    from grut_solver.constants import HBAR

    p = constitutive_params(m=1.0)
    assert p["tau_I"] == HBAR / 2, f"tau_I mismatch: {p['tau_I']}"
    assert abs(p["hbar_check"] - HBAR) < 1e-50, "hbar = 2 tau_I check failed"
    assert p["c_2"] > 0, "c_2 must be positive (stability)"
    assert p["c_0"] == 1.0, "c_0 must be 1 (constitutive fixed point)"
    # m = tau_I^2 / c_2
    m_back = p["tau_I"]**2 / p["c_2"]
    assert abs(m_back - 1.0) < 1e-30, f"Mass roundtrip: {m_back}"

    print(f"  PASS: test_constitutive_params (tau_I = {p['tau_I']:.3e})")


# ── Test 2: Schrodinger recovery residual ──────────────────────

def test_schrodinger_recovery():
    """Constitutive RHS matches Schrodinger RHS to machine precision."""
    from grut_solver.sectors.qm.schrodinger_recovery import schrodinger_recovery_test

    r = schrodinger_recovery_test(N_steps=200)
    assert r["max_deviation"] < 1e-12, f"Deviation {r['max_deviation']} > 1e-12"
    assert abs(r["norm_constitutive"] - 1.0) < 1e-10, f"Norm drift: {r['norm_constitutive']}"
    assert r["status"] == "PASS"

    print(f"  PASS: test_schrodinger_recovery (max_dev = {r['max_deviation']:.2e})")


# ── Test 3: Continuity equation residual ───────────────────────

def test_continuity_residual():
    """d_t rho + d_x j = 0 to finite-difference accuracy."""
    from grut_solver.sectors.qm.schrodinger_recovery import rhs_constitutive, rk4_step
    from grut_solver.sectors.qm.continuity import continuity_residual

    hbar = 1.0; tau_I = 0.5; m = 1.0; c_2 = tau_I**2/m
    Nx = 256; L = 20.0; dx = L/Nx; dt = 0.001
    x = np.linspace(-L/2, L/2, Nx, endpoint=False)
    V = 0.5 * x**2

    z = np.exp(-x**2/4) * np.exp(3j*x)
    z = z.astype(complex)
    z /= np.sqrt(np.sum(np.abs(z)**2)*dx)

    # Evolve a few steps to get non-trivial state
    for _ in range(100):
        z = rk4_step(z, rhs_constitutive, dt, V, c_2, tau_I, dx)
    z_next = rk4_step(z, rhs_constitutive, dt, V, c_2, tau_I, dx)

    r = continuity_residual(z, z_next, dt, hbar, m, dx)
    assert r["relative_violation"] < 0.1, f"Continuity violation: {r['relative_violation']}"
    assert r["status"] == "PASS"

    print(f"  PASS: test_continuity_residual (relative = {r['relative_violation']:.4f})")


# ── Test 4: KG NR limit consistency ────────────────────────────

def test_kg_nr_limit():
    """Klein-Gordon NR limit matches Schrodinger dispersion."""
    from grut_solver.sectors.qm.relativistic_extensions import kg_nr_limit_test

    r = kg_nr_limit_test(M=5.0, k=0.5)
    assert r["relative_diff"] < 1e-3, f"KG NR error: {r['relative_diff']}"
    assert r["status"] == "PASS"

    print(f"  PASS: test_kg_nr_limit (rel_diff = {r['relative_diff']:.2e})")


# ── Test 5: Dirac norm conservation and group velocity ─────────

def test_dirac_benchmark():
    """1+1D Dirac: norm conserved, v_g matches k/omega."""
    from grut_solver.sectors.qm.relativistic_extensions import dirac_1d_benchmark

    r = dirac_1d_benchmark(M=1.0, k=2.0, N_steps=400)
    assert r["norm_delta"] < 1e-8, f"Dirac norm delta: {r['norm_delta']}"
    assert r["vg_error"] < 0.05, f"Dirac v_g error: {r['vg_error']}"

    print(f"  PASS: test_dirac_benchmark (norm_delta = {r['norm_delta']:.2e}, "
          f"vg_err = {r['vg_error']:.3f})")


# ── Test 6: Born transparency (linear) ────────────────────────

def test_born_linear():
    """Linear constitutive law: Z_0/Z_1 = 1 exactly."""
    from grut_solver.sectors.qm.born_transparency import born_transparency_linear

    r = born_transparency_linear()
    assert r["Z_ratio"] == 1.0
    assert r["born_correction"] == 0.0
    assert r["status"] == "PASS"

    print(f"  PASS: test_born_linear (Z_ratio = {r['Z_ratio']})")


# ── Test 7: Born transparency (bistable) ──────────────────────

def test_born_bistable():
    """Bistable constitutive law: Born correction small."""
    from grut_solver.sectors.qm.born_transparency import born_transparency_bistable

    r = born_transparency_bistable()
    assert r["born_correction"] < 0.01, f"Correction: {r['born_correction']}"
    assert r["status"] == "PASS"

    print(f"  PASS: test_born_bistable (correction = {r['born_correction']:.6f})")


# ── Test 8: tau_R instability (structural) ─────────────────────

def test_tau_R_instability():
    """Naive tau_R > 0 produces growth (all eigenvalues positive)."""
    from grut_solver.sectors.qm.ctp_lindblad import naive_tau_R_instability

    r = naive_tau_R_instability()
    assert r["all_positive"], "Eigenvalues should all be positive"
    assert r["growth_rate_at_tau_R_0_1"] > 0, "Growth rate should be positive"

    print(f"  PASS: test_tau_R_instability (growth = {r['growth_rate_at_tau_R_0_1']:.4f})")


# ── Test 9: Lindblad thermalization ────────────────────────────

def test_lindblad_thermalization():
    """Lindblad dynamics produces correct Boltzmann populations."""
    from grut_solver.sectors.qm.ctp_lindblad import lindblad_thermalization_test

    r = lindblad_thermalization_test(T=2.0, gamma=0.1)
    assert r["max_population_error"] < 1e-4, f"Pop error: {r['max_population_error']}"
    assert abs(r["trace"] - 1.0) < 1e-6, f"Trace: {r['trace']}"
    assert r["status"] == "PASS"

    print(f"  PASS: test_lindblad_thermalization (max_err = {r['max_population_error']:.2e})")


# ── Test 10: Ehrenfest trajectory ──────────────────────────────

def test_ehrenfest():
    """Wavepacket <x>(t) follows classical trajectory."""
    from grut_solver.sectors.qm.classical_limit import ehrenfest_test

    r = ehrenfest_test(x0=2.0, sigma=0.5, N_steps=1000)
    assert r["relative_error"] < 0.01, f"Ehrenfest error: {r['relative_error']}"
    assert r["status"] == "PASS"

    print(f"  PASS: test_ehrenfest (rel_error = {r['relative_error']:.4f})")


# ── Test 11: Group velocity = classical velocity ───────────────

def test_group_velocity():
    """v_group = p/m for free particle."""
    from grut_solver.sectors.qm.classical_limit import group_velocity_test

    r = group_velocity_test(k=5.0, m=1.0)
    assert r["match"], f"v_group = {r['v_group']}, v_class = {r['v_classical']}"
    assert r["status"] == "PASS"

    print(f"  PASS: test_group_velocity (v_g = {r['v_group']:.4f} = p/m)")


# ── Test 12: Norm conservation across all tau_I values ─────────

def test_norm_conservation_universality():
    """Norm = 1 is preserved for various tau_I (c_2) values."""
    from grut_solver.sectors.qm.schrodinger_recovery import rhs_constitutive, rk4_step

    Nx = 128; L = 20.0; dx = L/Nx; dt = 0.002; N_steps = 200
    x = np.linspace(-L/2, L/2, Nx, endpoint=False)
    V = np.zeros(Nx)
    z0 = np.exp(-x**2/4).astype(complex)
    z0 /= np.sqrt(np.sum(np.abs(z0)**2)*dx)

    for tau_I in [0.1, 0.25, 0.5, 1.0, 2.0]:
        c_2 = tau_I**2 / 1.0  # m = 1
        z = z0.copy()
        for _ in range(N_steps):
            z = rk4_step(z, rhs_constitutive, dt, V, c_2, tau_I, dx)
        norm = float(np.sum(np.abs(z)**2)*dx)
        assert abs(norm - 1.0) < 1e-8, f"Norm = {norm} at tau_I = {tau_I}"

    print(f"  PASS: test_norm_conservation_universality (5 tau_I values)")


# ═══════════════════════════════════════════════════════════════
# RUNNER
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    tests = [
        test_constitutive_params,
        test_schrodinger_recovery,
        test_continuity_residual,
        test_kg_nr_limit,
        test_dirac_benchmark,
        test_born_linear,
        test_born_bistable,
        test_tau_R_instability,
        test_lindblad_thermalization,
        test_ehrenfest,
        test_group_velocity,
        test_norm_conservation_universality,
    ]

    print("=" * 60)
    print("SECTOR 1 — QM RECOVERY: VALIDATION SUITE")
    print("=" * 60)

    passed = failed = 0
    for t in tests:
        try:
            t()
            passed += 1
        except Exception as e:
            print(f"  FAIL: {t.__name__}: {e}")
            failed += 1

    print()
    print(f"  {'='*50}")
    print(f"  {passed} PASSED, {failed} FAILED out of {len(tests)}")
    if failed == 0:
        print(f"  ALL SECTOR 1 TESTS PASS.")
    print(f"  {'='*50}")
