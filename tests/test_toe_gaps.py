"""Tests for TOE gap modules — mass operator, inflation, hierarchy, strong CP, generations, gauge group."""

import numpy as np


# === Module 1: Mass Operator ===

def test_koide_z3_exact():
    """Z_3 circulant gives K = 2/3 exactly for all theta."""
    from grut_solver.sectors.flavor.mass_operator import koide_proof_z3
    proof = koide_proof_z3()
    assert proof["all_exact"], f"Max deviation: {proof['K_max_deviation']}"


def test_lepton_fit():
    """M0 and theta reproduce lepton masses to < 1%."""
    from grut_solver.sectors.flavor.mass_operator import fit_m0_theta_to_leptons
    fit = fit_m0_theta_to_leptons()
    assert fit["max_error_pct"] < 1.0, f"Max error: {fit['max_error_pct']:.2f}%"


def test_quark_koide():
    """Quark sectors have computable Koide ratios (not necessarily 2/3)."""
    from grut_solver.sectors.flavor.mass_operator import apply_to_quarks
    quarks = apply_to_quarks()
    for name, data in quarks.items():
        assert np.isfinite(data["K"]), f"{name} Koide is not finite"


def test_mass_operator_runs():
    """Full mass operator analysis completes."""
    from grut_solver.sectors.flavor.mass_operator import full_mass_operator_analysis
    r = full_mass_operator_analysis()
    assert r["status"].startswith("COMPUTED")
    assert len(r["honest_negatives"]) >= 3


# === Module 2: Constitutive Inflation ===

def test_spectral_index_physical():
    """Spectral index n_s is in physical range [0.9, 1.0]."""
    from grut_solver.sectors.cosmology.constitutive_inflation import spectral_index_constitutive
    # At the required H tau for Planck
    x_req = np.sqrt(0.0351 / 1.9649)
    ns = spectral_index_constitutive(1.0, x_req)
    assert 0.9 < ns["n_s"] < 1.0


def test_tensor_scalar_computed():
    """Tensor-to-scalar ratio is computed and finite."""
    from grut_solver.sectors.cosmology.constitutive_inflation import compare_to_planck
    planck = compare_to_planck()
    # r depends on the assumed standard r_standard; the constitutive
    # suppression factor is what matters
    assert 0 < planck["r_predicted"] < 1.0
    assert np.isfinite(planck["r_predicted"])


def test_inflation_analysis_runs():
    """Full inflation analysis completes."""
    from grut_solver.sectors.cosmology.constitutive_inflation import full_inflation_analysis
    r = full_inflation_analysis()
    assert "COMPUTED" in r["status"] or "HYPOTHESIS" in r["status"]


# === Module 3: Hierarchy ===

def test_hierarchy_honest_negative():
    """Hierarchy analysis correctly identifies problem as unsolved."""
    from grut_solver.sectors.ew.hierarchy import full_hierarchy_analysis
    r = full_hierarchy_analysis()
    assert "NOT solved" in r["honest_negatives"][0]
    assert r["comparison"]["standard_cutoff_planck"]["hierarchy_problem"]


def test_hierarchy_comparison_computed():
    """Hierarchy comparison between standard and constitutive is computed."""
    from grut_solver.sectors.ew.hierarchy import uv_softening_comparison
    comp = uv_softening_comparison()
    # Both corrections should be finite and positive
    assert comp["standard_cutoff_planck"]["delta_m_GeV"] > 0
    assert comp["constitutive_tau_planck"]["delta_m_GeV"] > 0
    # Both should show hierarchy problem (delta m >> v_Higgs)
    assert comp["standard_cutoff_planck"]["hierarchy_problem"]


# === Module 4: Strong CP ===

def test_strong_cp_hypothesis():
    """Strong CP analysis produces a structural argument."""
    from grut_solver.sectors.qcd.strong_cp import full_strong_cp_analysis
    r = full_strong_cp_analysis()
    assert "HYPOTHESIS" in r["status"]
    assert r["neutron_edm"]["consistent"]


def test_no_axion_predicted():
    """Constitutive solution predicts no axion."""
    from grut_solver.sectors.qcd.strong_cp import comparison_to_axion
    r = comparison_to_axion()
    assert r["constitutive"]["new_particle"] == "None"


# === Module 5: Three Generations ===

def test_n3_unique_koide():
    """N = 3 is the unique integer with constant K = 2/3."""
    from grut_solver.sectors.flavor.three_generations import uniqueness_of_three
    r = uniqueness_of_three()
    assert r["N_unique"] == 3


def test_koide_n3_constant():
    """K is theta-independent for N = 3."""
    from grut_solver.sectors.flavor.three_generations import koide_for_n_generations
    r = koide_for_n_generations(3)
    assert r["K_is_constant"]
    assert r["K_equals_two_thirds"]


def test_koide_n4_varies():
    """K varies with theta for N = 4 (not constant)."""
    from grut_solver.sectors.flavor.three_generations import koide_for_n_generations
    r = koide_for_n_generations(4)
    assert not r["K_is_constant"]


# === Module 6: Gauge Group ===

def test_su3_confines():
    """SU(3) with 6 flavors confines."""
    from grut_solver.sectors.unification.gauge_group_argument import confinement_threshold_su_n
    r = confinement_threshold_su_n(3)
    assert r["confines"]
    assert r["Lambda_GeV"] is not None


def test_gauge_group_framing():
    """Gauge group analysis produces honest framing."""
    from grut_solver.sectors.unification.gauge_group_argument import full_gauge_group_analysis
    r = full_gauge_group_analysis()
    assert "FRAMING" in r["status"]
