"""
Sector 4 — Gravity: Validation Test Suite

This is a PARTIAL sector. Tests verify:
- locked numerical results are correctly recorded
- status classifications are honest
- Sector 3 link is functional
- negative results are documented
- no overclaiming
"""

import sys
sys.path.insert(0, ".")


def test_locked_results_recorded():
    """Locked numerical results from the gravity program are documented."""
    from grut_solver.sectors.gravity import LOCKED_RESULTS

    assert LOCKED_RESULTS["f_R_eq_static"] == -17.71, "f must be -17.71 (LOCKED)"
    assert LOCKED_RESULTS["f_R_eq_static"] < 0, "f is NEGATIVE (worsens interior)"
    assert LOCKED_RESULTS["m_R_eq_static"] > 0, "mass must be positive"
    assert LOCKED_RESULTS["singularity_routes_tested"] == 10
    assert LOCKED_RESULTS["singularity_routes_succeeded"] == 0, "No routes succeeded"
    assert LOCKED_RESULTS["weak_field_correction"] < 1e-10, "Weak field is silent"

    print(f"  PASS: test_locked_results_recorded (f = {LOCKED_RESULTS['f_R_eq_static']}, "
          f"routes: 0/{LOCKED_RESULTS['singularity_routes_tested']} succeeded)")


def test_gravity_identity():
    """Gravity identity is honest: matter within GR, not emergent gravity."""
    from grut_solver.sectors.gravity import GRAVITY_IDENTITY

    assert "Einstein" in GRAVITY_IDENTITY or "standard" in GRAVITY_IDENTITY.lower()
    assert "emergent" not in GRAVITY_IDENTITY.lower()
    assert "derive" not in GRAVITY_IDENTITY.lower()

    print(f"  PASS: test_gravity_identity ('{GRAVITY_IDENTITY}')")


def test_component_status_honesty():
    """All failed/open components are labeled correctly."""
    from grut_solver.sectors.gravity import COMPONENT_STATUS

    assert "FAILED" in COMPONENT_STATUS["singularity_resolution"]
    assert "OPEN" in COMPONENT_STATUS["graviton"]
    assert "OPEN" in COMPONENT_STATUS["full_backreaction"]
    assert "OPEN" in COMPONENT_STATUS["uv_completion"]
    assert "demonstrated" in COMPONENT_STATUS["semiclassical_coupling"]
    assert "negative" in COMPONENT_STATUS["static_tov_interior"].lower()
    assert "transient" in COMPONENT_STATUS["dynamic_interior"].lower()

    print(f"  PASS: test_component_status_honesty (failures and opens correctly labeled)")


def test_sector_3_link():
    """Sector 3 (gravitational decoherence) is accessible from Sector 4."""
    from grut_solver.sectors.gravity import SECTOR_3_LINK
    from grut_solver.sectors.gravity_decoherence import lambda_grav

    # The link works: we can compute a decoherence rate from Sector 4's pointer
    rate = lambda_grav(m=1e-14, l=100e-9, R=50e-9)
    assert rate > 600, f"Sector 3 rate = {rate}"

    print(f"  PASS: test_sector_3_link (Lambda = {rate:.1f} Hz from Sector 3)")


def test_no_overclaiming():
    """The sector does not claim things it hasn't achieved."""
    from grut_solver.sectors.gravity import SECTOR_STATUS, COMPONENT_STATUS

    assert "Partial" in SECTOR_STATUS, f"Status should contain 'Partial', got {SECTOR_STATUS}"

    # These must NOT say "demonstrated" or "validated"
    for key in ["graviton", "full_backreaction", "uv_completion"]:
        assert "demonstrated" not in COMPONENT_STATUS[key].lower(), \
            f"{key} should not be 'demonstrated'"
        assert "validated" not in COMPONENT_STATUS[key].lower(), \
            f"{key} should not be 'validated'"

    print(f"  PASS: test_no_overclaiming (no false closure claims)")


def test_static_tov_worsens():
    """The static TOV result is correctly negative (f < 0)."""
    from grut_solver.sectors.gravity import LOCKED_RESULTS

    f = LOCKED_RESULTS["f_R_eq_static"]
    A_schw = LOCKED_RESULTS["A_Schw_reference"]

    assert f < 0, f"f should be < 0, got {f}"
    assert f < A_schw, f"f = {f} should be worse than Schwarzschild {A_schw}"

    print(f"  PASS: test_static_tov_worsens (f = {f} < A_Schw = {A_schw})")


def test_weak_field_silent():
    """Weak-field correction is observationally silent."""
    from grut_solver.sectors.gravity import LOCKED_RESULTS

    delta = LOCKED_RESULTS["weak_field_correction"]
    assert delta < 1e-10, f"Weak field should be silent, got {delta}"

    print(f"  PASS: test_weak_field_silent (delta ~ {delta:.0e})")


def test_legacy_modules_documented():
    """Legacy gravity modules are documented in the interface."""
    from grut_solver.sectors.gravity import LEGACY_MODULE_MAP

    expected_keys = ["TOV interior", "Dynamical collapse", "Metric deficit"]
    for key in expected_keys:
        assert key in LEGACY_MODULE_MAP, f"Missing: {key}"
        path = LEGACY_MODULE_MAP[key]
        assert path.endswith(".py"), f"Path should be .py: {path}"

    print(f"  PASS: test_legacy_modules_documented ({len(LEGACY_MODULE_MAP)} modules mapped)")


# ═══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    tests = [
        test_locked_results_recorded,
        test_gravity_identity,
        test_component_status_honesty,
        test_sector_3_link,
        test_no_overclaiming,
        test_static_tov_worsens,
        test_weak_field_silent,
        test_legacy_modules_documented,
    ]

    print("=" * 60)
    print("SECTOR 4 — GRAVITY: VALIDATION SUITE")
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
        print(f"  ALL SECTOR 4 TESTS PASS.")
    print(f"  {'='*50}")
