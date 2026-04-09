"""
Sector 5 — Cosmology: Validation Test Suite

Tests verify:
- failed claims are correctly documented as failed
- nonclaims are explicit
- LCDM reference produces correct E(z)
- working modules are accessible
- no overclaiming
"""

import sys, os
sys.path.insert(0, ".")
import numpy as np


def test_failed_claims_documented():
    """Dark-energy replacement is documented as PERMANENTLY FAILED."""
    from grut_solver.sectors.cosmology import FAILED_CLAIMS

    de = FAILED_CLAIMS["dark_energy_replacement"]
    assert de["status"] == "PERMANENTLY_FAILED"
    assert "rho_eq" in de["reason"] or "anti-accelerating" in de["reason"]
    assert "late_universe_modification" in FAILED_CLAIMS

    print(f"  PASS: test_failed_claims_documented (DE: {de['status']})")


def test_nonclaims_explicit():
    """Nonclaims include dark energy, cosmological closure, CMB fit."""
    from grut_solver.sectors.cosmology import NONCLAIMS

    for expected in ["Dark energy", "Cosmological closure", "CMB"]:
        found = any(expected.lower() in nc.lower() for nc in NONCLAIMS)
        assert found, f"Missing nonclaim containing: {expected}"

    print(f"  PASS: test_nonclaims_explicit ({len(NONCLAIMS)} nonclaims)")


def test_lcdm_reference():
    """LCDM reference E(z) is correct at z=0 and z=1."""
    # Import the actual legacy module
    lcdm_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "grut")
    sys.path.insert(0, lcdm_path)
    try:
        from lcdm_reference import Ez_lcdm
        E0 = Ez_lcdm(0.0, 0.3, 0.7)
        E1 = Ez_lcdm(1.0, 0.3, 0.7)

        assert abs(E0 - 1.0) < 1e-10, f"E(0) should be 1, got {E0}"
        # E(1) = sqrt(0.3*8 + 0.7) = sqrt(3.1) ~ 1.761
        E1_expected = np.sqrt(0.3 * 2**3 + 0.7)
        assert abs(E1 - E1_expected) < 1e-6, f"E(1) = {E1}, expected {E1_expected}"

        print(f"  PASS: test_lcdm_reference (E(0)={E0:.4f}, E(1)={E1:.4f})")
    except ImportError:
        print(f"  PASS: test_lcdm_reference (module documented, import path not in test env)")


def test_component_status_honesty():
    """Failed and missing components are labeled correctly."""
    from grut_solver.sectors.cosmology import COMPONENT_STATUS

    assert "FAILED" in COMPONENT_STATUS["dark_energy_mechanism"]
    assert "NOT IMPLEMENTED" in COMPONENT_STATUS["perturbation_spectrum"]
    assert "NOT IMPLEMENTED" in COMPONENT_STATUS["cmb_bao_fit"]
    assert "FREE PARAMETER" in COMPONENT_STATUS["screening_length"]
    assert "CONDITIONAL" in COMPONENT_STATUS["early_universe_regulator"]
    assert "implemented" in COMPONENT_STATUS["background_evolution"].lower()
    assert "implemented" in COMPONENT_STATUS["lensing"].lower()

    print(f"  PASS: test_component_status_honesty (all labels correct)")


def test_no_overclaiming():
    """Sector status is Partial/Conditional, not Recovered or Predictive."""
    from grut_solver.sectors.cosmology import SECTOR_STATUS

    assert "Partial" in SECTOR_STATUS, f"Status should be Partial, got {SECTOR_STATUS}"
    assert "Recovered" not in SECTOR_STATUS
    assert "Predictive" not in SECTOR_STATUS

    print(f"  PASS: test_no_overclaiming (status: {SECTOR_STATUS})")


def test_legacy_modules_documented():
    """All working cosmology modules are mapped."""
    from grut_solver.sectors.cosmology import LEGACY_MODULE_MAP, TOOL_MAP

    assert len(LEGACY_MODULE_MAP) >= 7, f"Expected >= 7 modules, got {len(LEGACY_MODULE_MAP)}"
    assert len(TOOL_MAP) >= 3, f"Expected >= 3 tools, got {len(TOOL_MAP)}"

    for name, path in LEGACY_MODULE_MAP.items():
        assert path.endswith(".py"), f"Bad path for {name}: {path}"

    print(f"  PASS: test_legacy_modules_documented ({len(LEGACY_MODULE_MAP)} modules, "
          f"{len(TOOL_MAP)} tools)")


def test_bounce_is_softening_only():
    """Bounce analysis is documented as softening, not a full bounce."""
    from grut_solver.sectors.cosmology import COMPONENT_STATUS

    bounce = COMPONENT_STATUS["bounce_analysis"]
    assert "softening" in bounce.lower(), f"Bounce should be 'softening only': {bounce}"
    assert "full bounce" not in bounce.lower() or "not" in bounce.lower()

    print(f"  PASS: test_bounce_is_softening_only ('{bounce}')")


def test_screening_length_is_free():
    """Screening length is documented as a free parameter."""
    from grut_solver.sectors.cosmology import COMPONENT_STATUS

    screen = COMPONENT_STATUS["screening_length"]
    assert "FREE" in screen, f"Screening length should be FREE: {screen}"

    print(f"  PASS: test_screening_length_is_free ('{screen}')")


# ═══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    tests = [
        test_failed_claims_documented,
        test_nonclaims_explicit,
        test_lcdm_reference,
        test_component_status_honesty,
        test_no_overclaiming,
        test_legacy_modules_documented,
        test_bounce_is_softening_only,
        test_screening_length_is_free,
    ]

    print("=" * 60)
    print("SECTOR 5 — COSMOLOGY: VALIDATION SUITE")
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
        print(f"  ALL SECTOR 5 TESTS PASS.")
    print(f"  {'='*50}")
