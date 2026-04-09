"""Sector 8 — Neutrinos: Validation Test Suite"""
import sys; sys.path.insert(0, "."); import numpy as np

def test_dirac_mass():
    from grut_solver.sectors.neutrinos.neutrino_mass_models import dirac_mass
    m = dirac_mass(1e-12)
    assert m > 0 and m < 1e-6  # should be tiny
    print(f"  PASS: test_dirac_mass (m = {m:.2e} GeV)")

def test_seesaw():
    from grut_solver.sectors.neutrinos.neutrino_mass_models import seesaw_type1
    m = seesaw_type1(y_nu=0.1, M_R=1e14)
    assert 0 < m < 1  # should be sub-eV scale in GeV
    print(f"  PASS: test_seesaw (m = {m:.2e} GeV)")

def test_mass_scale_scan():
    from grut_solver.sectors.neutrinos.neutrino_mass_models import mass_scale_scan
    s = mass_scale_scan()
    assert len(s) >= 4
    print(f"  PASS: test_mass_scale_scan ({len(s)} entries)")

def test_pmns_row_norms():
    """PMNS |U| row norms: sum |U_ij|^2 ~ 1 for each row."""
    from grut_solver.sectors.neutrinos.pmns_diagnostics import PMNS_PDG
    for i in range(3):
        row_norm = float(np.sum(PMNS_PDG[i]**2))
        assert abs(row_norm - 1.0) < 0.1, f"Row {i} norm = {row_norm}"
    print(f"  PASS: test_pmns_row_norms (all rows sum ~ 1)")

def test_mixing_angles():
    from grut_solver.sectors.neutrinos.pmns_diagnostics import angle_summary
    a = angle_summary()
    assert 30 < a["theta_12"] < 40
    assert "NOT derived" in a["note"]
    print(f"  PASS: test_mixing_angles (theta_12 = {a['theta_12']} deg, labeled input)")

def test_oscillation():
    from grut_solver.sectors.neutrinos.oscillation_observables import oscillation_probability_2flavor
    P = oscillation_probability_2flavor(dm2=2.5e-3, L_km=295, E_GeV=0.6)
    assert 0 <= P <= 1
    print(f"  PASS: test_oscillation (P = {P:.4f} at T2K-like params)")

def test_mass_splittings():
    from grut_solver.sectors.neutrinos.oscillation_observables import mass_splitting_summary
    s = mass_splitting_summary()
    assert s["dm2_21_eV2"] < s["dm2_32_eV2"]
    assert "NOT derived" in s["note"]
    print(f"  PASS: test_mass_splittings (dm21={s['dm2_21_eV2']:.2e}, dm32={s['dm2_32_eV2']:.2e})")

def test_no_overclaiming():
    from grut_solver.sectors.neutrinos import SECTOR_STATUS
    from grut_solver.sectors.neutrinos.neutrino_mass_models import MODEL_STATUS
    assert "Open" in SECTOR_STATUS
    assert "OPEN" in MODEL_STATUS["GRUT-native mechanism"]
    print(f"  PASS: test_no_overclaiming ({SECTOR_STATUS})")

if __name__ == "__main__":
    tests = [test_dirac_mass, test_seesaw, test_mass_scale_scan, test_pmns_row_norms,
             test_mixing_angles, test_oscillation, test_mass_splittings, test_no_overclaiming]
    print("=" * 60); print("SECTOR 8 — NEUTRINOS: VALIDATION"); print("=" * 60)
    p = f = 0
    for t in tests:
        try: t(); p += 1
        except Exception as e: print(f"  FAIL: {t.__name__}: {e}"); f += 1
    print(f"\n  {'='*50}\n  {p} PASSED, {f} FAILED out of {len(tests)}")
    if f == 0: print("  ALL SECTOR 8 TESTS PASS.")
    print(f"  {'='*50}")
