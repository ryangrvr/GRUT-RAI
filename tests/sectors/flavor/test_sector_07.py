"""Sector 7 — Flavor / Masses: Validation Test Suite"""
import sys; sys.path.insert(0, "."); import numpy as np

def test_yukawa_table():
    from grut_solver.sectors.flavor.yukawa_scan import yukawa_table
    t = yukawa_table()
    assert len(t) == 9, f"Expected 9 fermions, got {len(t)}"
    top = [f for f in t if f["name"] == "top"][0]
    assert abs(top["y_f"] - 0.995) < 0.01
    print(f"  PASS: test_yukawa_table (9 fermions, y_top = {top['y_f']:.3f})")

def test_hierarchy_ratio():
    from grut_solver.sectors.flavor.yukawa_scan import hierarchy_ratio
    r = hierarchy_ratio()
    assert r > 3e5, f"Hierarchy = {r}"
    print(f"  PASS: test_hierarchy_ratio ({r:.0f}x)")

def test_mass_matrix_diag():
    from grut_solver.sectors.flavor.mass_matrix_tools import diagonalize
    M = np.diag([0.0022, 1.28, 173.0])
    d = diagonalize(M)
    assert abs(d["masses"][2] - 173.0) < 0.01
    assert d["hierarchy"] > 1e4
    print(f"  PASS: test_mass_matrix_diag (hierarchy = {d['hierarchy']:.0f})")

def test_ckm_row_norms():
    """CKM |V| row norms: sum |V_ij|^2 ~ 1 for each row."""
    from grut_solver.sectors.flavor.ckm_diagnostics import CKM_PDG
    for i in range(3):
        row_norm = float(np.sum(CKM_PDG[i]**2))
        assert abs(row_norm - 1.0) < 0.1, f"Row {i} norm = {row_norm}"
    print(f"  PASS: test_ckm_row_norms (all rows sum ~ 1)")

def test_ckm_hierarchy():
    from grut_solver.sectors.flavor.ckm_diagnostics import hierarchy_summary
    h = hierarchy_summary()
    assert h["V_us"] > h["V_cb"] > h["V_ub"]
    assert "NOT derived" in h["note"]
    print(f"  PASS: test_ckm_hierarchy (V_us > V_cb > V_ub, labeled as input)")

def test_no_overclaiming():
    from grut_solver.sectors.flavor import SECTOR_STATUS
    assert "Open" in SECTOR_STATUS
    print(f"  PASS: test_no_overclaiming ({SECTOR_STATUS})")

if __name__ == "__main__":
    tests = [test_yukawa_table, test_hierarchy_ratio, test_mass_matrix_diag,
             test_ckm_row_norms, test_ckm_hierarchy, test_no_overclaiming]
    print("=" * 60); print("SECTOR 7 — FLAVOR / MASSES: VALIDATION"); print("=" * 60)
    p = f = 0
    for t in tests:
        try: t(); p += 1
        except Exception as e: print(f"  FAIL: {t.__name__}: {e}"); f += 1
    print(f"\n  {'='*50}\n  {p} PASSED, {f} FAILED out of {len(tests)}")
    if f == 0: print("  ALL SECTOR 7 TESTS PASS.")
    print(f"  {'='*50}")
