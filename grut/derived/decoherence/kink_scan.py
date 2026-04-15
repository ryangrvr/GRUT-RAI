"""
Geometry Kink Scan — The Extended-Body Fingerprint

The suppression factor S(l/R) = min(1, (l/R)^3/6) creates a sharp
slope change at l ~ 1.8R on a log-log plot of Lambda vs l.

Near field (l < R):  d(log Lambda)/d(log l) = +2  (slope +2)
Far field (l > R):   d(log Lambda)/d(log l) = -1  (slope -1)
Transition:          sharp kink over ~0.5 decades of l

No point-mass model has this kink. CSL has no geometry dependence.
Diosi-Penrose point-mass gives smooth l^-1 everywhere.
The SHAPE of the curve is the discriminator.
"""

import numpy as np
from grut.foundation.constants import G, HBAR, AMU


def kink_scan(m_kg, rho=19300, l_min=None, l_max=None, n_points=200):
    """High-resolution scan of Lambda vs l through the kink region.
    
    Returns the GRUT prediction, point-mass DP prediction, and CSL
    prediction for the same object, so the kink is visible as a
    difference between curves.
    """
    R = (3 * m_kg / (4 * np.pi * rho))**(1/3)
    
    if l_min is None:
        l_min = R * 0.05   # well into near field
    if l_max is None:
        l_max = R * 50     # well into far field
    
    l_kink = 1.8 * R  # the geometric kink location
    
    l_vals = np.logspace(np.log10(l_min), np.log10(l_max), n_points)
    
    grut_data = []
    dp_point_data = []  # Diosi-Penrose point mass (no extended body)
    csl_data = []       # CSL (state-independent, no geometry)
    
    # CSL parameters
    lambda_csl = 1e-16  # s^-1
    r_c = 1e-7          # m
    N_nucleons = m_kg / AMU
    
    for l in l_vals:
        # GRUT: extended body
        ratio = l / R
        S = min(1.0, ratio**3 / 6.0)
        L_grut = G * m_kg**2 * S / (HBAR * l)
        
        # Diosi-Penrose point mass: no S factor
        L_dp = G * m_kg**2 / (HBAR * l)
        
        # CSL: Lambda_CSL = lambda × N^2 × (1 - sinc(ql/hbar))
        # In high-l limit: ~lambda × N^2
        sinc_arg = l / r_c
        sinc_val = np.sin(sinc_arg) / sinc_arg if sinc_arg > 1e-10 else 1.0
        L_csl = lambda_csl * N_nucleons**2 * (1 - sinc_val)
        
        grut_data.append({"l": float(l), "Lambda": float(L_grut), "log_l": float(np.log10(l)), "log_Lambda": float(np.log10(L_grut)) if L_grut > 0 else -30})
        dp_point_data.append({"l": float(l), "Lambda": float(L_dp), "log_l": float(np.log10(l)), "log_Lambda": float(np.log10(L_dp))})
        csl_data.append({"l": float(l), "Lambda": float(L_csl), "log_l": float(np.log10(l)), "log_Lambda": float(np.log10(max(L_csl, 1e-30)))})
    
    # Compute local slope at each point for GRUT
    slopes = []
    for i in range(1, len(grut_data) - 1):
        dl = grut_data[i+1]["log_l"] - grut_data[i-1]["log_l"]
        dL = grut_data[i+1]["log_Lambda"] - grut_data[i-1]["log_Lambda"]
        slope = dL / dl if dl != 0 else 0
        slopes.append({"l": grut_data[i]["l"], "log_l": grut_data[i]["log_l"], "slope": float(slope)})
    
    # Find the kink: where slope changes most rapidly
    max_slope_change = 0
    kink_measured = l_kink
    for i in range(1, len(slopes) - 1):
        change = abs(slopes[i+1]["slope"] - slopes[i-1]["slope"])
        if change > max_slope_change:
            max_slope_change = change
            kink_measured = slopes[i]["l"]
    
    return {
        "object": {
            "m_kg": m_kg, "m_amu": m_kg / AMU, "m_pg": m_kg * 1e15,
            "rho": rho, "R_m": R, "R_um": R * 1e6,
        },
        "kink": {
            "l_predicted": l_kink, "l_predicted_um": l_kink * 1e6,
            "l_measured": kink_measured, "l_measured_um": kink_measured * 1e6,
            "agreement_pct": abs(kink_measured - l_kink) / l_kink * 100,
            "slope_before": 2.0, "slope_after": -1.0,
            "slope_change": 3.0,  # from +2 to -1
        },
        "curves": {
            "GRUT": grut_data,
            "Diosi_Penrose_point": dp_point_data,
            "CSL": csl_data,
        },
        "slopes": slopes,
        "discriminator": {
            "GRUT_has_kink": True,
            "DP_point_has_kink": False,
            "CSL_has_kink": False,
            "kink_is_unique_to": "GRUT (extended body suppression S(l/R))",
            "what_to_measure": "d(log Lambda)/d(log l) as function of l",
            "confirmation": "Slope changes from +2 to -1 near l = 1.8R",
            "falsification": "No slope change observed (smooth curve)",
        },
    }


def material_comparison(m_kg, l_m, materials=None):
    """F2 test: same mass, different materials → different rates.
    
    This is the geometry dependence signature. GRUT predicts different
    Lambda for gold vs silica at the same mass because R differs.
    Every mass-only model (CSL, constant floor) predicts identical rates.
    """
    if materials is None:
        materials = {"gold": 19300, "silica": 2200, "diamond": 3510, 
                     "silicon": 2330, "osmium": 22590}
    
    results = {}
    for name, rho in materials.items():
        R = (3 * m_kg / (4 * np.pi * rho))**(1/3)
        ratio = l_m / R
        S = min(1.0, ratio**3 / 6.0)
        L = G * m_kg**2 * S / (HBAR * l_m)
        
        results[name] = {
            "rho": rho, "R_m": R, "R_um": R * 1e6,
            "l_over_R": ratio, "S_l_R": S,
            "Lambda_Hz": L, "t_coh_s": 1/L if L > 0 else float('inf'),
        }
    
    # Compute ratios between all pairs
    names = list(results.keys())
    ratios = {}
    for i in range(len(names)):
        for j in range(i+1, len(names)):
            a, b = names[i], names[j]
            r = results[a]["Lambda_Hz"] / results[b]["Lambda_Hz"] if results[b]["Lambda_Hz"] > 0 else 0
            ratios[f"{a}/{b}"] = r
    
    # Mass-only models predict ratio = 1.0 for all pairs
    max_ratio = max(ratios.values()) if ratios else 1
    min_ratio = min(ratios.values()) if ratios else 1
    
    return {
        "mass_kg": m_kg, "mass_amu": m_kg / AMU, "separation_m": l_m,
        "materials": results,
        "ratios": ratios,
        "max_ratio": max_ratio, "min_ratio": min_ratio,
        "geometry_dependence_detected": max_ratio / min_ratio > 1.1 if min_ratio > 0 else False,
        "discriminator": {
            "GRUT_predicts": "Different rates for different materials at same mass",
            "CSL_predicts": "Same rate (mass-only, no geometry)",
            "constant_floor_predicts": "Same rate",
            "test": f"Compare gold vs silica at m={m_kg/AMU:.0e} amu, l={l_m*1e6:.1f} μm",
            "confirmation": f"Rate ratio ≠ 1 (GRUT predicts gold/silica = {ratios.get('gold/silica', 0):.2f})",
            "falsification": "Rate ratio = 1 within measurement error",
        },
    }


def entanglement_test():
    """F5 test: Bell states decohere slower than separable states.
    
    GRUT: Lambda depends on the STATE through the mass distribution.
    A Bell-entangled pair has a different effective mass distribution
    than a separable state of the same total mass.
    
    CSL: state-independent (Lambda depends only on mass and N).
    """
    return {
        "prediction": {
            "GRUT": "Lambda(Bell) < Lambda(separable) — entanglement protects coherence",
            "CSL": "Lambda(Bell) = Lambda(separable) — state-independent",
            "DP_point": "Lambda(Bell) < Lambda(separable) — also state-dependent",
        },
        "test": {
            "prepare": "Two identical masses, one in separable superposition, one in Bell state",
            "measure": "Decoherence rate for each",
            "confirmation": "Bell rate < separable rate",
            "falsification": "Bell rate = separable rate (rules out GRUT AND DP)",
            "note": "This test discriminates GRUT+DP from CSL, not GRUT from DP. Use F6 (kink) to discriminate GRUT from DP.",
        },
        "discriminator_power": "MEDIUM — distinguishes state-dependent (GRUT, DP) from state-independent (CSL)",
    }


def full_kink_analysis(m_amu=1e9, rho=19300, l_m=1e-7):
    """Complete geometry kink + material comparison analysis."""
    m_kg = m_amu * AMU
    kink = kink_scan(m_kg, rho)
    materials = material_comparison(m_kg, l_m)
    entanglement = entanglement_test()
    
    return {
        "kink_scan": kink,
        "material_comparison": materials,
        "entanglement_test": entanglement,
        "combined_verdict": (
            "Three geometry-based discriminators: "
            "(1) Kink at l=1.8R — unique to GRUT, kills all point-mass models. "
            "(2) Material dependence — same mass, different rate. Kills CSL and constant floor. "
            "(3) Entanglement protection — state-dependent rate. Kills CSL. "
            "Combined with the separation anti-scaling (β=-1), these four tests "
            "provide unambiguous discrimination of GRUT from all alternatives."
        ),
    }
