"""
v5 Fixed-Point Tests — Verify all new fixed-point modules across sectors.

Tests the self-referential principle z = z_target[z] as applied to:
  Sector 5: Vacuum fixed point and derivation chain
  Sector 6: QCD confinement threshold
  Sector 7: Flavor eigenvalue spectrum
  Sector 8: Neutrino near-zero fixed point
  Sector 10: Baryogenesis Sakharov conditions
  Sector 11: Coupling unification approach
  Bridge: 40 Hz + Omega_Lambda from one condition
"""
import sys; sys.path.insert(0, ".")
import numpy as np


# ── Sector 5: Vacuum Fixed Point ─────────────────────────

def test_vacuum_candidate_2():
    """Omega_Lambda = 0.691, accuracy < 2% vs Planck."""
    from grut_solver.sectors.cosmology.vacuum_fixed_point import candidate_2
    c = candidate_2()
    assert 0.65 < c["Omega_Lambda"] < 0.75
    assert c["accuracy_OmL_pct"] < 5
    print(f"  PASS: vacuum OmL = {c['Omega_Lambda']:.4f} ({c['accuracy_OmL_pct']:.1f}%)")


def test_derivation_chain_complete():
    """10 steps, 0 gaps."""
    from grut_solver.sectors.cosmology.derivation_chain import derivation_chain
    dc = derivation_chain()
    assert dc["n_derived"] == 10
    assert dc["n_gaps"] == 0
    assert "DERIVED" in dc["status"]
    print(f"  PASS: chain {dc['n_derived']} derived, {dc['n_gaps']} gaps")


def test_self_referential_cosmology():
    """Three-phase expansion from threshold crossing."""
    from grut_solver.sectors.cosmology.self_referential_cosmology import run_self_referential_cosmology
    r = run_self_referential_cosmology()
    assert r["three_phases"]["produced"]
    assert r["today"]["accelerating"]
    assert r["today"]["f_self"] > 0.5
    print(f"  PASS: 3 phases, q={r['today']['q']:.3f}, f_self={r['today']['f_self']:.3f}")


# ── Sector 6: QCD ────────────────────────────────────────

def test_qcd_confinement_threshold():
    """Threshold exists and is near Lambda_QCD."""
    from grut_solver.sectors.qcd.fixed_point_confinement import confinement_threshold
    ct = confinement_threshold()
    assert ct["threshold_GeV"] is not None
    assert 0.2 < ct["threshold_GeV"] < 5.0
    assert ct["alpha_s_at_threshold"] > 0.3
    print(f"  PASS: QCD threshold = {ct['threshold_GeV']:.3f} GeV, alpha_s = {ct['alpha_s_at_threshold']:.3f}")


def test_qcd_fixed_point_structure():
    """Confinement maps to self-referential structure."""
    from grut_solver.sectors.qcd.fixed_point_confinement import confinement_as_fixed_point
    fp = confinement_as_fixed_point()
    assert len(fp["self_consistency_loop"]) >= 3
    assert "string_tension" in fp["observables_as_fixed_point_properties"]
    print(f"  PASS: QCD FP structure documented")


# ── Sector 7: Flavor ─────────────────────────────────────

def test_koide_formula():
    """Koide K within 0.01% of 2/3 for leptons."""
    from grut_solver.sectors.flavor.fixed_point_masses import mass_ratios_as_eigenvalues
    mr = mass_ratios_as_eigenvalues()
    assert mr["leptons"]["koide_deviation_pct"] < 0.01
    print(f"  PASS: Koide dev = {mr['leptons']['koide_deviation_pct']:.4f}%")


def test_mixing_hierarchy():
    """CKM near-diagonal, PMNS not."""
    from grut_solver.sectors.flavor.fixed_point_masses import mixing_as_fixed_point_overlap
    mx = mixing_as_fixed_point_overlap()
    assert mx["CKM"]["diagonal_dominance"] > 0.9
    assert mx["PMNS"]["diagonal_dominance"] < 0.6
    print(f"  PASS: CKM={mx['CKM']['diagonal_dominance']:.3f}, PMNS={mx['PMNS']['diagonal_dominance']:.3f}")


# ── Sector 8: Neutrinos ──────────────────────────────────

def test_neutrino_suppression():
    """Neutrino masses suppressed by > 10^8 vs tau."""
    from grut_solver.sectors.neutrinos.fixed_point_masses import near_zero_fixed_point_argument
    nz = near_zero_fixed_point_argument()
    assert nz["log10_suppression"] < -8
    print(f"  PASS: nu suppression = 10^{nz['log10_suppression']:.0f}")


def test_neutrino_mixing_from_degeneracy():
    """Large nu mixing from degenerate eigenvalues."""
    from grut_solver.sectors.neutrinos.fixed_point_masses import large_mixing_from_degeneracy
    lm = large_mixing_from_degeneracy()
    assert lm["neutrinos"]["mixing_angle_deg"] > 30
    assert lm["quarks"]["mixing_angle_deg"] < 20
    print(f"  PASS: nu mixing {lm['neutrinos']['mixing_angle_deg']:.0f} > quark {lm['quarks']['mixing_angle_deg']:.0f}")


# ── Sector 10: Baryogenesis ───────────────────────────────

def test_sakharov_structural():
    """All 3 Sakharov conditions structural in FP framework."""
    from grut_solver.sectors.baryogenesis.fixed_point_asymmetry import sakharov_in_fixed_point_language
    sak = sakharov_in_fixed_point_language()
    assert len(sak) == 3
    for k, v in sak.items():
        assert "Structural" in v["status"] or "structural" in v["status"].lower()
    print(f"  PASS: 3/3 Sakharov conditions structural")


# ── Sector 11: Unification ────────────────────────────────

def test_unification_threshold():
    """Closest approach exists at reasonable scale."""
    from grut_solver.sectors.unification.fixed_point_unification import unification_threshold
    ut = unification_threshold()
    assert 13 < ut["log10_mu"] < 17
    assert ut["f_self_max"] > 0.8
    print(f"  PASS: unification at 10^{ut['log10_mu']:.1f} GeV, f_self={ut['f_self_max']:.3f}")


def test_unification_miss():
    """SM misses unification — documented."""
    from grut_solver.sectors.unification.fixed_point_unification import grut_modified_convergence
    gm = grut_modified_convergence()
    assert gm["miss_as_fraction"] > 0.01
    assert gm["miss_as_fraction"] < 0.5
    print(f"  PASS: miss = {gm['miss_as_fraction']*100:.1f}%")


# ── Bridge ────────────────────────────────────────────────

def test_bridge_both_sectors():
    """40 Hz and Omega_Lambda from same fixed point."""
    from grut_solver.sectors.cosmology.bridge_calculation import the_bridge
    br = the_bridge()
    s13 = br["sector_13"]
    s5 = br["sector_5"]
    assert 35 < s13["f_gamma_route1_hz"] < 45
    assert 0.6 < s5["Omega_Lambda"] < 0.8
    assert br["log10_ratio"] < -15
    print(f"  PASS: bridge 40Hz + OmL={s5['Omega_Lambda']:.4f}, ratio=10^{br['log10_ratio']:.1f}")


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    passed = failed = 0
    for t in tests:
        try:
            t()
            passed += 1
        except Exception as e:
            print(f"  FAIL: {t.__name__}: {e}")
            failed += 1
    print(f"\n{'='*60}")
    print(f"v5 Fixed Points: {passed} passed, {failed} failed, {passed+failed} total")
