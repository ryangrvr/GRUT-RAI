"""Sector 11 — Coupling Unification: Validation"""
import sys; sys.path.insert(0, ".")

def test_rg_diagnostics():
    from grut_solver.sectors.unification.rg_diagnostics import convergence_metric
    r = convergence_metric(1e15)
    assert r["spread"] > 0, "Couplings should not exactly unify in SM"
    print(f"  PASS: test_rg_diagnostics (spread at 10^15 GeV = {r['spread']:.2f})")

def test_closest_approach():
    from grut_solver.sectors.unification.rg_diagnostics import find_closest_approach
    r = find_closest_approach()
    assert r["mu"] > 1e10, f"Closest approach at {r['mu']:.0e} GeV"
    assert r["spread"] > 0, "SM does NOT unify"
    print(f"  PASS: test_closest_approach (mu = {r['mu']:.1e}, spread = {r['spread']:.2f})")

def test_unification_summary():
    from grut_solver.sectors.unification.convergence_metrics import unification_summary
    s = unification_summary()
    assert not s["sm_unifies"]
    assert s["grut_modifies_running"] == "OPEN"
    print(f"  PASS: test_unification_summary (SM unifies: {s['sm_unifies']})")

def test_no_overclaiming():
    from grut_solver.sectors.unification import SECTOR_STATUS
    assert "Open" in SECTOR_STATUS
    print(f"  PASS: test_no_overclaiming ({SECTOR_STATUS})")

if __name__ == "__main__":
    tests = [test_rg_diagnostics, test_closest_approach, test_unification_summary, test_no_overclaiming]
    print("=" * 60); print("SECTOR 11 — COUPLING UNIFICATION: VALIDATION"); print("=" * 60)
    p = f = 0
    for t in tests:
        try: t(); p += 1
        except Exception as e: print(f"  FAIL: {t.__name__}: {e}"); f += 1
    print(f"\n  {'='*50}\n  {p} PASSED, {f} FAILED out of {len(tests)}")
    if f == 0: print("  ALL SECTOR 11 TESTS PASS.")
    print(f"  {'='*50}")
