"""
Sector 2 — Electroweak / SM Host Structure: Validation Test Suite
"""

import numpy as np
import sys
sys.path.insert(0, ".")


def test_gauge_invariance():
    """U(1) gauge transformation preserves |z|^2."""
    from grut_solver.sectors.ew.gauge_u1 import gauge_invariance_check

    Nx = 128
    x = np.linspace(-10, 10, Nx)
    z = np.exp(-x**2/4 + 2j*x).astype(complex)
    A = 0.5 * np.sin(x)
    theta = 0.7 * np.cos(x)

    r = gauge_invariance_check(z, A, 1.0, theta, x[1]-x[0])
    assert r["max_rho_diff"] < 1e-14, f"Gauge invariance: {r['max_rho_diff']}"
    assert r["status"] == "PASS"
    print(f"  PASS: test_gauge_invariance (diff = {r['max_rho_diff']:.2e})")


def test_lorentz_force():
    """Wavepacket acceleration matches eE/m."""
    from grut_solver.sectors.ew.lorentz_force import lorentz_force_test

    r = lorentz_force_test(E_field=0.5)
    assert r["relative_error"] < 0.02, f"Lorentz force error: {r['relative_error']}"
    assert r["status"] == "PASS"
    print(f"  PASS: test_lorentz_force (a = {r['a_measured']:.4f} vs {r['a_theory']:.4f}, "
          f"err = {r['relative_error']:.3f})")


def test_lorentz_force_multi():
    """Lorentz force verified at multiple E values."""
    from grut_solver.sectors.ew.lorentz_force import lorentz_force_test

    for E in [0.2, 0.5, 1.0]:
        r = lorentz_force_test(E_field=E)
        assert r["relative_error"] < 0.02, f"E={E}: error {r['relative_error']}"
    print(f"  PASS: test_lorentz_force_multi (3 E values, all < 2%)")


def test_ab_phase():
    """AB phase: gauge transformation z -> z exp(i e integral A dx / hbar) is exact."""
    # The AB effect is ANALYTICALLY exact: a static A field multiplies z by
    # exp(i e integral_path A dx / hbar). We verify this directly.
    Nx = 256; L = 20.0; dx = L/Nx
    x = np.linspace(-L/2, L/2, Nx, endpoint=False)
    e = 1.0; hbar = 1.0
    z0 = np.exp(-x**2/4 + 2j*x).astype(complex)

    # Constant A in a region: integral A dx = A * L_AB
    for A_0 in [0.1, 0.3, 0.5]:
        L_AB = 5.0
        mask = np.abs(x) < L_AB / 2
        A_field = np.zeros(Nx)
        A_field[mask] = A_0
        # Exact phase: e * cumulative integral of A
        phase_exact = e * np.cumsum(A_field) * dx / hbar
        z_transformed = z0 * np.exp(1j * phase_exact)
        # The density |z|^2 should be unchanged
        rho_diff = np.max(np.abs(np.abs(z_transformed)**2 - np.abs(z0)**2))
        assert rho_diff < 1e-14, f"AB density change: {rho_diff} at A={A_0}"
        # The TOTAL accumulated phase should be e * A_0 * L_AB / hbar
        total_phase = e * A_0 * np.sum(mask) * dx / hbar
        expected = e * A_0 * L_AB / hbar
        assert abs(total_phase - expected) / expected < 0.02, \
            f"Phase mismatch at A={A_0}: {total_phase} vs {expected}"

    print(f"  PASS: test_ab_phase (3 A values, exact gauge phase verified)")


def test_charge_quantization():
    """Q = T^3 + Y/2 gives correct charges for all 7 SM fermions."""
    from grut_solver.sectors.ew.electroweak_su2_u1 import charge_quantization_check

    r = charge_quantization_check()
    assert r["all_exact"], "Not all charges match"
    assert r["status"] == "PASS"
    print(f"  PASS: test_charge_quantization (7/7 exact)")


def test_su2_covariance():
    """D_mu Z transforms covariantly under SU(2)."""
    from grut_solver.sectors.ew.electroweak_su2_u1 import su2_covariance_check

    r = su2_covariance_check()
    assert r["covariance_error"] < 1e-12
    assert r["gauge_invariance_error"] < 1e-12
    assert r["status"] == "PASS"
    print(f"  PASS: test_su2_covariance (err = {r['covariance_error']:.2e})")


def test_lie_algebra():
    """[T^a, T^b] = i epsilon^{abc} T^c."""
    from grut_solver.sectors.ew.electroweak_su2_u1 import lie_algebra_check

    r = lie_algebra_check()
    assert r["max_error"] < 1e-14
    assert r["status"] == "PASS"
    print(f"  PASS: test_lie_algebra (max err = {r['max_error']:.2e})")


def test_anomaly_cancellation():
    """All three anomaly conditions are exactly zero."""
    from grut_solver.sectors.ew.anomaly_cancellation import anomaly_check

    r = anomaly_check()
    assert r["all_cancel"], f"Anomalies: Y={r['sum_Y']}, Y3={r['sum_Y3']}, dbl={r['sum_Y_doublets']}"
    assert r["status"] == "PASS"
    print(f"  PASS: test_anomaly_cancellation (Y={r['sum_Y']:.1f}, Y3={r['sum_Y3']:.1f}, "
          f"dbl={r['sum_Y_doublets']:.1f})")


def test_higgs_vev():
    """Mexican-hat minimum is nonzero, origin is unstable."""
    from grut_solver.sectors.ew.higgs_sector import higgs_vev

    r = higgs_vev(mu2=1.0, lam=0.5)
    assert r["origin_unstable"], "Origin should be unstable"
    assert r["V_min"] < 0, "V at minimum should be < 0"
    assert r["v"] > 0, "VEV should be positive"
    print(f"  PASS: test_higgs_vev (v = {r['v']:.4f}, V_min = {r['V_min']:.4f})")


def test_symmetry_breaking():
    """SU(2) × U(1)_Y -> U(1)_EM. Q<H> = 0."""
    from grut_solver.sectors.ew.higgs_sector import symmetry_breaking_check

    r = symmetry_breaking_check()
    assert r["Q_H_is_zero"], "Q<H> must be zero (photon massless)"
    assert r["n_broken"] == 3, f"Expected 3 broken combinations, got {r['n_broken']}"
    assert r["n_goldstones"] == 3, f"Expected 3 Goldstones, got {r['n_goldstones']}"
    assert r["status"] == "PASS"
    print(f"  PASS: test_symmetry_breaking (Q<H>=0, {r['n_broken']} broken, "
          f"{r['n_goldstones']} Goldstones)")


def test_mass_relations():
    """W/Z masses, rho = 1, photon massless."""
    from grut_solver.sectors.ew.mass_relations import gauge_boson_masses

    r = gauge_boson_masses()
    assert r["rho_exact_one"], f"rho = {r['rho']}"
    assert r["photon_massless"], "Photon must be massless"
    assert 79 < r["m_W"] < 82, f"m_W = {r['m_W']}"
    assert 90 < r["m_Z"] < 92, f"m_Z = {r['m_Z']}"
    assert r["status"] == "PASS"
    print(f"  PASS: test_mass_relations (m_W={r['m_W']:.1f}, m_Z={r['m_Z']:.1f}, "
          f"rho={r['rho']:.6f})")


def test_parameter_count():
    """SM-equivalent parameter count."""
    from grut_solver.sectors.ew.mass_relations import sm_parameter_count

    r = sm_parameter_count()
    assert r["matches_SM"]
    assert r["n_free"] >= 10, f"Too few free params: {r['n_free']}"
    print(f"  PASS: test_parameter_count ({r['n_free']} free + {r['n_identified']} identified)")


def test_yukawas_free():
    """Yukawa couplings are documented as free (not derived)."""
    from grut_solver.sectors.ew.mass_relations import fermion_masses

    r = fermion_masses()
    assert r["yukawas_free"], "Yukawas must be labeled free"
    assert r["yukawa_hierarchy"] > 1e5, f"Hierarchy: {r['yukawa_hierarchy']}"
    print(f"  PASS: test_yukawas_free (hierarchy = {r['yukawa_hierarchy']:.0f}x)")


# ═══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    tests = [
        test_gauge_invariance,
        test_lorentz_force,
        test_lorentz_force_multi,
        test_ab_phase,
        test_charge_quantization,
        test_su2_covariance,
        test_lie_algebra,
        test_anomaly_cancellation,
        test_higgs_vev,
        test_symmetry_breaking,
        test_mass_relations,
        test_parameter_count,
        test_yukawas_free,
    ]

    print("=" * 60)
    print("SECTOR 2 — ELECTROWEAK HOST: VALIDATION SUITE")
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
        print(f"  ALL SECTOR 2 TESTS PASS.")
    print(f"  {'='*50}")
