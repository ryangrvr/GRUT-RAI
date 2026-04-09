"""
Sector 6 — QCD / Strong Force: Validation Test Suite

Mix of:
- fully validated algebraic structure
- exploratory observables
- explicitly open physics
"""

import numpy as np
import sys
sys.path.insert(0, ".")


def test_su3_lie_algebra():
    """[T^a, T^b] = i f^{abc} T^c for all a, b."""
    from grut_solver.sectors.qcd.su3_structure import verify_lie_algebra
    r = verify_lie_algebra()
    assert r["status"] == "PASS", f"Lie algebra error: {r['max_error']}"
    print(f"  PASS: test_su3_lie_algebra (max_err = {r['max_error']:.2e})")


def test_trace_normalization():
    """Tr(T^a T^b) = delta^{ab}/2."""
    from grut_solver.sectors.qcd.su3_structure import verify_trace_normalization
    r = verify_trace_normalization()
    assert r["status"] == "PASS", f"Trace error: {r['max_error']}"
    print(f"  PASS: test_trace_normalization (max_err = {r['max_error']:.2e})")


def test_hermiticity():
    """All generators are Hermitian."""
    from grut_solver.sectors.qcd.su3_structure import verify_hermiticity
    r = verify_hermiticity()
    assert r["status"] == "PASS"
    print(f"  PASS: test_hermiticity (max_err = {r['max_error']:.2e})")


def test_tracelessness():
    """All generators are traceless."""
    from grut_solver.sectors.qcd.su3_structure import verify_tracelessness
    r = verify_tracelessness()
    assert r["status"] == "PASS"
    print(f"  PASS: test_tracelessness (max_err = {r['max_error']:.2e})")


def test_casimir_fundamental():
    """C_F = (N^2-1)/(2N) = 4/3 for SU(3)."""
    from grut_solver.sectors.qcd.su3_structure import casimir_fundamental
    C_F = casimir_fundamental()
    expected = 4.0 / 3.0
    assert abs(C_F - expected) < 1e-10, f"C_F = {C_F}, expected {expected}"
    print(f"  PASS: test_casimir_fundamental (C_F = {C_F:.6f})")


def test_structure_constants_antisymmetry():
    """f^{abc} is totally antisymmetric."""
    from grut_solver.sectors.qcd.su3_structure import structure_constants
    f = structure_constants()
    max_err = 0.0
    for a in range(8):
        for b in range(8):
            for c in range(8):
                err = max(abs(f[a,b,c] + f[b,a,c]),
                          abs(f[a,b,c] + f[a,c,b]))
                max_err = max(max_err, err)
    assert max_err < 1e-10, f"Antisymmetry error: {max_err}"
    print(f"  PASS: test_structure_constants_antisymmetry (max_err = {max_err:.2e})")


def test_su3_covariance():
    """D q transforms covariantly under SU(3): D'q' = U(Dq)."""
    from grut_solver.sectors.qcd.covariant_dynamics import covariance_check
    r = covariance_check()
    assert r["status"] == "PASS", f"Covariance error: {r['covariance_error']}"
    print(f"  PASS: test_su3_covariance (err = {r['covariance_error']:.2e})")


def test_field_strength_covariance():
    """F_{mu nu} transforms as F' = U F U^dag, Tr(F^2) invariant."""
    from grut_solver.sectors.qcd.covariant_dynamics import field_strength_covariance_check
    r = field_strength_covariance_check()
    assert r["status"] == "PASS"
    print(f"  PASS: test_field_strength_covariance (F_err = {r['F_covariance_error']:.2e}, "
          f"TrF2_err = {r['TrF2_invariance_error']:.2e})")


def test_color_singlet():
    """A single quark is NOT a color singlet."""
    from grut_solver.sectors.qcd.color_representations import color_singlet_check, COLOR_STATES
    r = color_singlet_check(COLOR_STATES["red"])
    assert not r["is_singlet"], "Single quark should not be a singlet"
    print(f"  PASS: test_color_singlet (quark is not singlet, charge = {r['max_color_charge']:.4f})")


def test_representation_dimensions():
    """Representation dimensions and Casimirs match SU(3)."""
    from grut_solver.sectors.qcd.color_representations import representation_dimensions
    reps = representation_dimensions()
    assert reps["fundamental"]["dim"] == 3
    assert reps["adjoint"]["dim"] == 8
    assert abs(reps["fundamental"]["Casimir"] - 4/3) < 1e-10
    print(f"  PASS: test_representation_dimensions (fund=3, adj=8, C_F={reps['fundamental']['Casimir']:.4f})")


def test_wilson_loop_runs():
    """Wilson loop computation runs and returns a finite value."""
    from grut_solver.sectors.qcd.wilson_loop import wilson_loop_2d
    r = wilson_loop_2d(Nx=6, Ny=6, g_s=1.0, eps=0.3, R=2, T=2)
    assert np.isfinite(r["W"]), f"W is not finite: {r['W']}"
    assert r["area"] == 4
    assert r["perimeter"] == 8
    print(f"  PASS: test_wilson_loop_runs (W = {r['W']:.4f}, area = {r['area']}) [EXPLORATORY]")


def test_running_coupling():
    """alpha_s(M_Z) ~ 0.118, decreases at higher energy (asymptotic freedom)."""
    from grut_solver.sectors.qcd.running_diagnostics import alpha_s_running
    a_MZ = alpha_s_running(91.2)
    a_1TeV = alpha_s_running(1000.0)
    assert abs(a_MZ - 0.1185) < 0.001, f"alpha_s(M_Z) = {a_MZ}"
    assert a_1TeV < a_MZ, "Asymptotic freedom: alpha_s should decrease"
    print(f"  PASS: test_running_coupling (alpha_s(M_Z) = {a_MZ:.4f}, "
          f"alpha_s(1TeV) = {a_1TeV:.4f})")


def test_no_overclaiming():
    """Sector status is Open, no false closure claims."""
    from grut_solver.sectors.qcd import SECTOR_STATUS
    from grut_solver.sectors.qcd.confinement_probes import IMPLEMENTATION_STATUS
    from grut_solver.sectors.qcd.running_diagnostics import GRUT_MODIFICATION_STATUS

    assert "Open" in SECTOR_STATUS
    assert IMPLEMENTATION_STATUS["string_tension_extraction"] == "TODO"
    assert GRUT_MODIFICATION_STATUS["status"] == "OPEN"
    print(f"  PASS: test_no_overclaiming (status: {SECTOR_STATUS})")


# ═══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    tests = [
        test_su3_lie_algebra,
        test_trace_normalization,
        test_hermiticity,
        test_tracelessness,
        test_casimir_fundamental,
        test_structure_constants_antisymmetry,
        test_su3_covariance,
        test_field_strength_covariance,
        test_color_singlet,
        test_representation_dimensions,
        test_wilson_loop_runs,
        test_running_coupling,
        test_no_overclaiming,
    ]

    print("=" * 60)
    print("SECTOR 6 — QCD / STRONG FORCE: VALIDATION SUITE")
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
        print(f"  ALL SECTOR 6 TESTS PASS.")
    print(f"  {'='*50}")
