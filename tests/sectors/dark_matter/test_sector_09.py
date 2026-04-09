"""Sector 9 — Dark Matter: Validation"""
import sys; sys.path.insert(0, ".")

def test_criteria_defined():
    from grut_solver.sectors.dark_matter.candidate_criteria import VIABILITY_CRITERIA
    assert len(VIABILITY_CRITERIA) >= 5
    print(f"  PASS: test_criteria_defined ({len(VIABILITY_CRITERIA)} criteria)")

def test_stability_check():
    from grut_solver.sectors.dark_matter.stability_checks import is_stable, decay_width_to_lifetime
    assert is_stable(1e20)
    assert not is_stable(1e10)
    tau = decay_width_to_lifetime(1e-40)
    assert tau > 1e15
    print(f"  PASS: test_stability_check")

def test_no_overclaiming():
    from grut_solver.sectors.dark_matter import SECTOR_STATUS, NONCLAIMS
    assert "Open" in SECTOR_STATUS
    assert len(NONCLAIMS) >= 3
    print(f"  PASS: test_no_overclaiming ({SECTOR_STATUS})")

if __name__ == "__main__":
    tests = [test_criteria_defined, test_stability_check, test_no_overclaiming]
    print("=" * 60); print("SECTOR 9 — DARK MATTER: VALIDATION"); print("=" * 60)
    p = f = 0
    for t in tests:
        try: t(); p += 1
        except Exception as e: print(f"  FAIL: {t.__name__}: {e}"); f += 1
    print(f"\n  {'='*50}\n  {p} PASSED, {f} FAILED out of {len(tests)}")
    if f == 0: print("  ALL SECTOR 9 TESTS PASS.")
    print(f"  {'='*50}")
