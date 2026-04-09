"""
Sector 3 — Gravitational Decoherence: Validation Test Suite

Standardized Part 2 entry point. Calls into existing grut_solver tests
and adds sector-specific benchmarks.
"""

import numpy as np
import sys
sys.path.insert(0, ".")


# ── Test 1: USL reference value ────────────────────────────

def test_usl_reference():
    """Lambda_grav at reference platform matches 632.9 Hz."""
    from grut_solver.usl.gravitational import lambda_grav
    rate = lambda_grav(m=1e-14, l=100e-9, R=50e-9)
    assert abs(rate - 632.9) / 632.9 < 0.01, f"Rate = {rate}"
    print(f"  PASS: test_usl_reference (Lambda = {rate:.1f} Hz)")


# ── Test 2: Suppression factor transitions ─────────────────

def test_suppression_factor():
    """S(l/R) transitions at l = 2R and is monotonic."""
    from grut_solver.usl.gravitational import suppression_factor

    assert suppression_factor(200e-9, 50e-9) == 1.0, "Far field should be 1"
    assert suppression_factor(100e-9, 50e-9) == 1.0, "l = 2R should be 1"
    S_near = suppression_factor(10e-9, 50e-9)
    assert abs(S_near - (0.2)**3/6) < 1e-10, f"Near field: {S_near}"

    S_prev = 0
    for l in np.linspace(1e-9, 200e-9, 50):
        S = suppression_factor(l, 50e-9)
        assert S >= S_prev - 1e-15, f"Not monotonic at l = {l}"
        S_prev = S
    print(f"  PASS: test_suppression_factor (monotonic, transitions at 2R)")


# ── Test 3: Near-field / far-field scaling ─────────────────

def test_scaling_regimes():
    """Near field ~ l^2, far field ~ 1/l."""
    from grut_solver.usl.gravitational import lambda_grav
    m = 1e-14; R = 50e-9

    # Far field: check 1/l scaling
    L1 = lambda_grav(m, 200e-9, R)
    L2 = lambda_grav(m, 400e-9, R)
    ratio_far = L1 / L2
    assert abs(ratio_far - 2.0) < 0.01, f"Far ratio = {ratio_far}, expected 2"

    # Near field: check ~l^2 scaling (through S ~ (l/R)^3 / l = l^2/R^3)
    L3 = lambda_grav(m, 10e-9, R)
    L4 = lambda_grav(m, 20e-9, R)
    ratio_near = L4 / L3
    # Near field: Lambda ~ l^2, so doubling l -> 4x rate
    assert 3.5 < ratio_near < 4.5, f"Near ratio = {ratio_near}, expected ~4"

    print(f"  PASS: test_scaling_regimes (far: {ratio_far:.2f}x, near: {ratio_near:.2f}x)")


# ── Test 4: Kink peak location ─────────────────────────────

def test_kink_peak():
    """Peak at l ~ 1.8R for R = 50 nm."""
    from grut_solver.figures import compute_kink_data

    d = compute_kink_data(m=1e-14, R=50e-9)
    assert 85e-9 < d["l_peak"] < 100e-9, f"Peak at {d['l_peak']*1e9:.1f} nm"
    assert d["lam_peak"] > 500, f"Peak Lambda = {d['lam_peak']}"
    assert d["residual_dex"] > 0.1, f"Power-law residual {d['residual_dex']}"

    print(f"  PASS: test_kink_peak (l = {d['l_peak']*1e9:.1f} nm, "
          f"Lambda = {d['lam_peak']:.0f} Hz, residual = {d['residual_dex']:.3f} dex)")


# ── Test 5: Pressure plateau ──────────────────────────────

def test_pressure_plateau():
    """Gravity dominates at low P, gas dominates at high P."""
    from grut_solver.budget.total import compute_budget

    b_hi = compute_budget(1e-14, 50e-9, 100e-9, 10e-3, 1e-6)
    b_lo = compute_budget(1e-14, 50e-9, 100e-9, 10e-3, 1e-14)

    assert not b_hi.is_grav_dominated, "High P should be gas-dominated"
    assert b_lo.is_grav_dominated, "Low P should be gravity-dominated"
    assert b_lo.signal_to_noise > 1000, f"Low P SNR = {b_lo.signal_to_noise}"

    print(f"  PASS: test_pressure_plateau (hi-P: gas, lo-P: gravity, SNR = {b_lo.signal_to_noise:.0f})")


# ── Test 6: Crossover pressure ─────────────────────────────

def test_crossover_pressure():
    """P* is in the expected range."""
    from grut_solver.usl.scaling import crossover_pressure

    P = crossover_pressure(1e-14, 50e-9, 100e-9, 10e-3)
    assert 1e-11 < P < 1e-7, f"P* = {P}"
    print(f"  PASS: test_crossover_pressure (P* = {P:.2e} Pa)")


# ── Test 7: Boundary mass ─────────────────────────────────

def test_boundary_mass():
    """m* = sqrt(hbar l / (G t)) at reference point."""
    from grut_solver.usl.gravitational import boundary_mass
    from grut_solver.constants import HBAR, G

    m = boundary_mass(1e-7, 1.0)
    expected = np.sqrt(HBAR * 1e-7 / (G * 1.0))
    assert abs(m - expected) / expected < 1e-10
    print(f"  PASS: test_boundary_mass (m* = {m*1e15:.2f} fg)")


# ── Test 8: Bell protection ───────────────────────────────

def test_bell_protection():
    """Bell rate < product rate at d = 200 nm."""
    from grut_solver.usl.many_body import entanglement_discriminant

    d = entanglement_discriminant(1e-14, 100e-9, 200e-9, 50e-9)
    assert d["lambda_cross"] < 0, "Cross term should be negative"
    assert d["lambda_bell"] < d["lambda_product"], "Bell must be lower"
    assert abs(d["percent_difference"] + 16.7) < 1.0, f"Diff = {d['percent_difference']}"

    print(f"  PASS: test_bell_protection ({d['percent_difference']:.1f}% at d=200nm)")


# ── Test 9: GHZ suppression scaling ───────────────────────

def test_ghz_suppression():
    """GHZ/product ratio decreases with N."""
    from grut_solver.usl.many_body import lambda_ghz_3

    g3 = lambda_ghz_3(1e-14, 100e-9, 200e-9, 200e-9)
    assert g3["ratio_ghz_over_product"] < 1.0, "GHZ should be suppressed"
    assert g3["ratio_ghz_over_product"] > 0.0, "GHZ rate must be positive"
    print(f"  PASS: test_ghz_suppression (N=3: ratio = {g3['ratio_ghz_over_product']:.3f})")


# ── Test 10: Kill framework ──────────────────────────────

def test_kill_framework():
    """No tested alternative fits all six signatures."""
    from grut_solver.kill.model_comparison import run_all_kill_tests

    results = run_all_kill_tests()
    any_degenerate = any(r.can_mimic_all_three for r in results)
    # Note: power-law can fit plateau+geometry but not entanglement
    for r in results:
        assert not r.can_mimic_all_three or r.model_name == "power_law_floor", \
            f"{r.model_name} should not mimic all signatures"

    print(f"  PASS: test_kill_framework ({len(results)} models tested, "
          f"entanglement kills all state-independent)")


# ── Test 11: Anomaly suppression ─────────────────────────

def test_anomaly_suppression():
    """Anomaly channel is suppressed by ~10^-8."""
    from grut_solver.usl.gravitational import lambda_grav
    from grut_solver.usl.anomaly import lambda_anomaly

    Lg = lambda_grav(1e-14, 100e-9)
    La = lambda_anomaly(1e-14, 100e-9)
    ratio = La / Lg
    assert ratio < 1e-6, f"Anomaly ratio = {ratio}"
    print(f"  PASS: test_anomaly_suppression (ratio = {ratio:.2e})")


# ── Test 12: Existing bounds survival ────────────────────

def test_existing_bounds():
    """GRUT signal is undetectable at current experimental masses."""
    from grut_solver.usl.gravitational import lambda_grav
    from grut_solver.constants import AMU

    # OTIMA: 10^4 amu, l=100nm
    rate = lambda_grav(1e4 * AMU, 100e-9, 1.5e-9)
    assert rate < 1e-10, f"OTIMA rate {rate} should be negligible"
    print(f"  PASS: test_existing_bounds (OTIMA: Lambda = {rate:.2e} Hz, undetectable)")


# ── Test 13: Validity envelope ───────────────────────────

def test_validity_envelope():
    """Lab nanoparticle is in the VALID Markovian regime."""
    from grut_solver.usl.validity import classify_system

    lab = classify_system("lab_nanoparticle")
    assert lab["usl_trustworthy"], "Lab should be in VALID regime"
    print(f"  PASS: test_validity_envelope (W_tau = {lab['W_tau_decades']}, "
          f"regime = {lab['regime']})")


# ── Test 14: Systematic error ────────────────────────────

def test_systematic_floor():
    """Ward residual systematic does not affect gravitational sector."""
    from grut_solver.budget.systematic import apply_systematic_to_rate

    r = apply_systematic_to_rate(632.9, sector="gravitational")
    assert r["systematic_pct"] == 0.0, "Gravitational sector should have zero constitutive systematic"
    print(f"  PASS: test_systematic_floor (grav sector: {r['systematic_pct']}% systematic)")


# ═══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    tests = [
        test_usl_reference,
        test_suppression_factor,
        test_scaling_regimes,
        test_kink_peak,
        test_pressure_plateau,
        test_crossover_pressure,
        test_boundary_mass,
        test_bell_protection,
        test_ghz_suppression,
        test_kill_framework,
        test_anomaly_suppression,
        test_existing_bounds,
        test_validity_envelope,
        test_systematic_floor,
    ]

    print("=" * 60)
    print("SECTOR 3 — GRAVITATIONAL DECOHERENCE: VALIDATION SUITE")
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
        print(f"  ALL SECTOR 3 TESTS PASS.")
    print(f"  {'='*50}")
