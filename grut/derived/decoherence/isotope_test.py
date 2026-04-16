"""
Isotope Decoherence Test — The Cleanest Geometry Discriminator

Compare nanoparticles of DIFFERENT ISOTOPES of the SAME ELEMENT.
Same chemistry, same surface, same charge — only nuclear mass differs.

Why this is CLEANER than material swap:
  - Material swap: gold vs silica differ in crystal structure, surface
    charge, optical properties, adsorbed layers. Critics can argue the
    decoherence difference is environmental, not gravitational.
  - Isotope test: Si-28 vs Si-30 are chemically IDENTICAL. Same lattice
    constant (to 1e-4), same surface, same trap response. The ONLY
    difference is nuclear mass → density → radius → S(l/R).

GRUT prediction: Λ ratio = (ρ_A/ρ_B) in near field (both l < R)
                  or (R_B/R_A)³ in far field via S factor.
Environmental:    Λ ratio = 1.000 (identical surfaces).

A nonzero deviation from 1.000 with isotopically pure nanoparticles
is essentially un-fakeable by environmental systematics.
"""

import numpy as np
from grut.foundation.constants import G, HBAR, AMU


# ═══════════════════════════════════════════════════════
# ISOTOPE DATABASE
# ═══════════════════════════════════════════════════════

ISOTOPES = {
    # Silicon isotopes (natural abundance Si: 2.329 g/cm³)
    "Si-28": {"element": "Si", "A": 28, "rho": 2329.0, "abundance": 0.9223,
              "note": "Dominant isotope, available 99.99% pure"},
    "Si-29": {"element": "Si", "A": 29, "rho": 2329.0 * 29/28, "abundance": 0.0468,
              "note": "Spin-1/2 nucleus (NMR active)"},
    "Si-30": {"element": "Si", "A": 30, "rho": 2329.0 * 30/28, "abundance": 0.0309,
              "note": "Available enriched for semiconductor industry"},

    # Germanium isotopes (natural Ge: 5.323 g/cm³)
    "Ge-70": {"element": "Ge", "A": 70, "rho": 5323.0, "abundance": 0.2057,
              "note": "Lightest stable Ge isotope"},
    "Ge-72": {"element": "Ge", "A": 72, "rho": 5323.0 * 72/70, "abundance": 0.2745,
              "note": "Most abundant"},
    "Ge-76": {"element": "Ge", "A": 76, "rho": 5323.0 * 76/70, "abundance": 0.0775,
              "note": "Used in 0vbb searches, available enriched"},

    # Calcium isotopes (natural Ca: 1.550 g/cm³)
    "Ca-40": {"element": "Ca", "A": 40, "rho": 1550.0, "abundance": 0.9694,
              "note": "Dominant isotope"},
    "Ca-48": {"element": "Ca", "A": 48, "rho": 1550.0 * 48/40, "abundance": 0.00187,
              "note": "Doubly magic nucleus, used in nuclear physics"},

    # Tungsten isotopes (natural W: 19250 kg/m³)
    "W-182": {"element": "W", "A": 182, "rho": 19250.0, "abundance": 0.2650,
              "note": "Second most abundant"},
    "W-186": {"element": "W", "A": 186, "rho": 19250.0 * 186/182, "abundance": 0.2843,
              "note": "Most abundant W isotope"},
}


def _lambda_grav(m_kg, l_m, R_m):
    """Compute Lambda_grav with extended-body suppression."""
    ratio = l_m / R_m
    S = min(1.0, ratio**3 / 6.0)
    return G * m_kg**2 * S / (HBAR * l_m)


def _radius_from_mass(m_kg, rho):
    """Sphere radius from mass and density."""
    return (3 * m_kg / (4 * np.pi * rho))**(1/3)


# ═══════════════════════════════════════════════════════
# CORE EXPERIMENT
# ═══════════════════════════════════════════════════════

def isotope_experiment(n_atoms=1e9, l_m=1e-7, iso_a="Si-28", iso_b="Si-30"):
    """Run the isotope decoherence test.

    Parameters
    ----------
    n_atoms : float
        Number of atoms in each nanoparticle (same count for both).
    l_m : float
        Superposition separation in meters.
    iso_a, iso_b : str
        Isotope labels from the ISOTOPES database.

    Returns
    -------
    dict with experiment parameters, per-isotope results, ratio, and verdict.
    """
    if iso_a not in ISOTOPES or iso_b not in ISOTOPES:
        avail = list(ISOTOPES.keys())
        return {"error": f"Unknown isotope. Available: {avail}"}

    spec_a = ISOTOPES[iso_a]
    spec_b = ISOTOPES[iso_b]

    if spec_a["element"] != spec_b["element"]:
        return {"error": f"Isotopes must be of the same element. "
                f"{iso_a} is {spec_a['element']}, {iso_b} is {spec_b['element']}."}

    # Masses: same number of atoms, different atomic mass
    m_a = n_atoms * spec_a["A"] * AMU
    m_b = n_atoms * spec_b["A"] * AMU

    # Densities differ by isotope mass ratio (same lattice, heavier nuclei)
    rho_a = spec_a["rho"]
    rho_b = spec_b["rho"]

    R_a = _radius_from_mass(m_a, rho_a)
    R_b = _radius_from_mass(m_b, rho_b)

    L_a = _lambda_grav(m_a, l_m, R_a)
    L_b = _lambda_grav(m_b, l_m, R_b)

    ratio_grut = L_a / L_b if L_b > 0 else float('inf')

    # Environmental prediction: identical surfaces → identical rates
    ratio_env = 1.0

    # What does GRUT predict analytically?
    mass_ratio = spec_a["A"] / spec_b["A"]
    # In far field: Lambda ~ m^2 / l, so ratio = (m_a/m_b)^2 = (A_a/A_b)^2
    far_field_ratio = mass_ratio**2
    # In near field (l < R): Lambda ~ m^2 * (l/R)^3 / l = m^2 l^2 / R^3
    #   R ~ (m/rho)^{1/3}, so R^3 ~ m/rho, and Lambda ~ m^2 l^2 rho / m = m l^2 rho
    #   ratio = (m_a rho_a) / (m_b rho_b) = (A_a rho_a) / (A_b rho_b)
    near_field_ratio = (spec_a["A"] * rho_a) / (spec_b["A"] * rho_b)

    # Determine regime
    l_over_R_a = l_m / R_a
    l_over_R_b = l_m / R_b
    both_far = l_over_R_a >= 1.8 and l_over_R_b >= 1.8
    both_near = l_over_R_a < 1.8 and l_over_R_b < 1.8

    if both_far:
        regime = "far-field"
        analytic_ratio = far_field_ratio
    elif both_near:
        regime = "near-field"
        analytic_ratio = near_field_ratio
    else:
        regime = "mixed (one near, one far)"
        analytic_ratio = ratio_grut  # no simple formula

    deviation_pct = abs(ratio_grut - 1.0) * 100
    precision_needed_5sigma = deviation_pct / 5.0

    return {
        "experiment": {
            "type": "isotope_decoherence_test",
            "description": f"{iso_a} vs {iso_b} nanoparticles, same atom count",
            "n_atoms": n_atoms,
            "separation_m": l_m,
            "separation_nm": l_m * 1e9,
        },
        "isotope_a": {
            "label": iso_a, "element": spec_a["element"], "A": spec_a["A"],
            "mass_kg": m_a, "mass_amu": m_a / AMU,
            "rho_kg_m3": rho_a,
            "R_m": R_a, "R_nm": R_a * 1e9,
            "l_over_R": l_over_R_a,
            "S_l_R": min(1.0, l_over_R_a**3 / 6.0),
            "Lambda_Hz": L_a,
            "t_coh_s": 1.0 / L_a if L_a > 0 else float('inf'),
            "availability": spec_a["note"],
        },
        "isotope_b": {
            "label": iso_b, "element": spec_b["element"], "A": spec_b["A"],
            "mass_kg": m_b, "mass_amu": m_b / AMU,
            "rho_kg_m3": rho_b,
            "R_m": R_b, "R_nm": R_b * 1e9,
            "l_over_R": l_over_R_b,
            "S_l_R": min(1.0, l_over_R_b**3 / 6.0),
            "Lambda_Hz": L_b,
            "t_coh_s": 1.0 / L_b if L_b > 0 else float('inf'),
            "availability": spec_b["note"],
        },
        "ratio": {
            "GRUT": ratio_grut,
            "environmental": ratio_env,
            "deviation_from_unity_pct": deviation_pct,
            "regime": regime,
            "analytic_ratio": analytic_ratio,
        },
        "discrimination": {
            "grut_vs_env_difference_pct": deviation_pct,
            "precision_needed_5sigma_pct": precision_needed_5sigma,
            "measurable": deviation_pct > 1.0,
            "why_clean": "Isotopes have identical chemistry, surface, crystal structure. "
                         "Only nuclear mass differs. Environmental systematics cancel exactly.",
        },
        "predictions": {
            "GRUT": f"Lambda({iso_a})/Lambda({iso_b}) = {ratio_grut:.4f} "
                    f"({deviation_pct:.1f}% deviation)",
            "CSL": "ratio = 1.000 (mass-only, no geometry)",
            "DP_point": f"ratio = {far_field_ratio:.4f} (point mass, same as far-field GRUT)",
            "environmental": "ratio = 1.000 (identical surfaces)",
        },
        "verdict": {
            "feasible": deviation_pct > 1.0 and precision_needed_5sigma < 5.0,
            "advantage_over_material_swap": "No surface chemistry systematics. "
                "Isotope purity controllable to 99.99%. Lattice constant identical to 0.01%.",
            "best_element": "Silicon (enriched isotopes commercially available, "
                "semiconductor industry supply chain)",
        },
    }


# ═══════════════════════════════════════════════════════
# ELEMENT SCAN
# ═══════════════════════════════════════════════════════

def element_scan(n_atoms=1e9, l_m=1e-7):
    """Compare all available isotope pairs for each element."""
    elements = {}
    for label, spec in ISOTOPES.items():
        elements.setdefault(spec["element"], []).append(label)

    results = []
    for elem, isos in elements.items():
        if len(isos) < 2:
            continue
        # Find the pair with max A difference
        pairs = []
        for i in range(len(isos)):
            for j in range(i+1, len(isos)):
                a, b = isos[i], isos[j]
                exp = isotope_experiment(n_atoms, l_m, a, b)
                if "error" in exp:
                    continue
                pairs.append({
                    "pair": f"{a} vs {b}",
                    "A_diff": abs(ISOTOPES[a]["A"] - ISOTOPES[b]["A"]),
                    "ratio_grut": exp["ratio"]["GRUT"],
                    "deviation_pct": exp["ratio"]["deviation_from_unity_pct"],
                    "precision_5sigma_pct": exp["discrimination"]["precision_needed_5sigma_pct"],
                    "regime": exp["ratio"]["regime"],
                })
        pairs.sort(key=lambda x: x["deviation_pct"], reverse=True)
        results.append({
            "element": elem,
            "n_isotopes": len(isos),
            "best_pair": pairs[0] if pairs else None,
            "all_pairs": pairs,
        })

    results.sort(key=lambda x: x["best_pair"]["deviation_pct"] if x["best_pair"] else 0,
                 reverse=True)

    return {
        "n_atoms": n_atoms, "separation_m": l_m,
        "elements": results,
        "overall_best": results[0]["best_pair"] if results else None,
        "ranking": [{"element": r["element"],
                     "best_pair": r["best_pair"]["pair"],
                     "deviation_pct": r["best_pair"]["deviation_pct"]}
                    for r in results if r["best_pair"]],
    }


# ═══════════════════════════════════════════════════════
# MASS SCAN
# ═══════════════════════════════════════════════════════

def mass_scan(iso_a="Si-28", iso_b="Si-30", l_m=1e-7, n_points=60):
    """Scan the isotope ratio as function of particle size (n_atoms)."""
    n_vals = np.logspace(6, 12, n_points)  # 10^6 to 10^12 atoms
    data = []

    for n in n_vals:
        exp = isotope_experiment(n, l_m, iso_a, iso_b)
        if "error" in exp:
            continue
        data.append({
            "n_atoms": float(n),
            "log_n": float(np.log10(n)),
            "ratio_grut": exp["ratio"]["GRUT"],
            "deviation_pct": exp["ratio"]["deviation_from_unity_pct"],
            "regime": exp["ratio"]["regime"],
            "Lambda_a_Hz": exp["isotope_a"]["Lambda_Hz"],
            "Lambda_b_Hz": exp["isotope_b"]["Lambda_Hz"],
        })

    # Find optimal mass
    if data:
        best = max(data, key=lambda x: x["deviation_pct"])
    else:
        best = None

    return {
        "iso_a": iso_a, "iso_b": iso_b, "separation_m": l_m,
        "data": data,
        "optimal_n_atoms": best["n_atoms"] if best else None,
        "max_deviation_pct": best["deviation_pct"] if best else 0,
        "optimal_regime": best["regime"] if best else "unknown",
    }


# ═══════════════════════════════════════════════════════
# SEPARATION SCAN
# ═══════════════════════════════════════════════════════

def separation_scan(iso_a="Si-28", iso_b="Si-30", n_atoms=1e9, n_points=80):
    """Scan the isotope ratio as function of superposition separation."""
    spec_a = ISOTOPES[iso_a]
    spec_b = ISOTOPES[iso_b]
    m_a = n_atoms * spec_a["A"] * AMU
    R_a = _radius_from_mass(m_a, spec_a["rho"])
    R_min = R_a * 0.05
    R_max = R_a * 50

    l_vals = np.logspace(np.log10(R_min), np.log10(R_max), n_points)
    data = []

    for l in l_vals:
        exp = isotope_experiment(n_atoms, float(l), iso_a, iso_b)
        if "error" in exp:
            continue
        data.append({
            "l_m": float(l),
            "l_nm": float(l * 1e9),
            "log_l": float(np.log10(l)),
            "ratio_grut": exp["ratio"]["GRUT"],
            "deviation_pct": exp["ratio"]["deviation_from_unity_pct"],
            "regime": exp["ratio"]["regime"],
        })

    if data:
        best = max(data, key=lambda x: x["deviation_pct"])
    else:
        best = None

    return {
        "iso_a": iso_a, "iso_b": iso_b, "n_atoms": n_atoms,
        "R_a_nm": R_a * 1e9,
        "data": data,
        "optimal_l_nm": best["l_nm"] if best else None,
        "max_deviation_pct": best["deviation_pct"] if best else 0,
    }


# ═══════════════════════════════════════════════════════
# FULL ANALYSIS
# ═══════════════════════════════════════════════════════

def full_isotope_analysis(n_atoms=1e9, l_m=1e-7):
    """Complete isotope decoherence analysis: all elements, optimal parameters."""
    si = isotope_experiment(n_atoms, l_m, "Si-28", "Si-30")
    ge = isotope_experiment(n_atoms, l_m, "Ge-70", "Ge-76")
    ca = isotope_experiment(n_atoms, l_m, "Ca-40", "Ca-48")
    scan = element_scan(n_atoms, l_m)

    return {
        "headline": "Isotope Decoherence Test — chemically identical, gravitationally different",
        "silicon": si,
        "germanium": ge,
        "calcium": ca,
        "element_ranking": scan["ranking"],
        "overall_best": scan["overall_best"],
        "summary": {
            "Si_28_vs_30_ratio": si["ratio"]["GRUT"],
            "Ge_70_vs_76_ratio": ge["ratio"]["GRUT"],
            "Ca_40_vs_48_ratio": ca["ratio"]["GRUT"],
            "env_prediction": 1.000,
            "advantage": "Zero surface-chemistry systematics. Isotope purity to 99.99%.",
            "recommended_element": "Silicon (commercially available enriched isotopes)",
        },
    }
