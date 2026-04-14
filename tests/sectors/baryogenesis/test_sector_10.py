"""Sector 10 — Baryogenesis: Validation"""
import sys; sys.path.insert(0, ".")

def test_sakharov_checklist():
    from grut_solver.sectors.baryogenesis.sakharov_checks import sakharov_checklist
    r = sakharov_checklist()
    assert len(r["conditions"]) == 3
    assert not r["all_met"], "Not all Sakharov conditions are met"
    print(f"  PASS: test_sakharov_checklist (all_met = {r['all_met']})")

def test_toy_asymmetry():
    from grut_solver.sectors.baryogenesis.asymmetry_scaffold import toy_asymmetry_evolution
    r = toy_asymmetry_evolution(epsilon=1e-8, Gamma=1e10, T_dec=1e10)
    assert "TOY MODEL" in r["note"]
    print(f"  PASS: test_toy_asymmetry (N_B = {r['N_B_final']:.2e}, toy)")

def test_no_overclaiming():
    from grut_solver.sectors.baryogenesis import SECTOR_STATUS, NONCLAIMS
    # Status upgraded from Open to Computed (two-route anomaly)
    assert "Computed" in SECTOR_STATUS or "Open" in SECTOR_STATUS
    assert len(NONCLAIMS) >= 1  # documented nonclaims exist
    print(f"  PASS: test_no_overclaiming ({SECTOR_STATUS})")

if __name__ == "__main__":
    tests = [test_sakharov_checklist, test_toy_asymmetry, test_no_overclaiming]
    print("=" * 60); print("SECTOR 10 — BARYOGENESIS: VALIDATION"); print("=" * 60)
    p = f = 0
    for t in tests:
        try: t(); p += 1
        except Exception as e: print(f"  FAIL: {t.__name__}: {e}"); f += 1
    print(f"\n  {'='*50}\n  {p} PASSED, {f} FAILED out of {len(tests)}")
    if f == 0: print("  ALL SECTOR 10 TESTS PASS.")
    print(f"  {'='*50}")
