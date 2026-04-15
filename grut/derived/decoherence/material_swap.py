"""
Material Swap Experiment — F2 Geometry Dependence

The decisive test: take TWO spheres of IDENTICAL MASS but different
density (gold vs silica). GRUT predicts DIFFERENT decoherence rates.
Every mass-only model predicts IDENTICAL rates.

The key: at the same mass, different density means different R.
Different R means different S(l/R). Different S means different Lambda.

This experiment doesn't need to reach the absolute rate — it only
needs to measure the RATIO between two materials. Systematic errors
cancel in the ratio.
"""

import numpy as np
from grut.foundation.constants import G, HBAR, AMU

MATERIALS = {
    "gold": {"rho": 19300, "symbol": "Au", "Z": 79},
    "silica": {"rho": 2200, "symbol": "SiO2", "Z": 14},
    "diamond": {"rho": 3510, "symbol": "C", "Z": 6},
    "silicon": {"rho": 2330, "symbol": "Si", "Z": 14},
    "tungsten": {"rho": 19250, "symbol": "W", "Z": 74},
    "osmium": {"rho": 22590, "symbol": "Os", "Z": 76},
    "aluminum": {"rho": 2700, "symbol": "Al", "Z": 13},
    "lead": {"rho": 11340, "symbol": "Pb", "Z": 82},
}


def material_swap_experiment(m_amu=1e9, l_m=1e-7, mat_a="gold", mat_b="silica"):
    """Run the material swap: same mass, two materials, compare rates.
    
    This is the cleanest geometry test because:
    1. Mass is identical → mass-only models predict ratio = 1
    2. Separation is identical → no l-dependent systematics
    3. Only R differs → the ratio IS the geometry signal
    """
    m_kg = m_amu * AMU
    rho_a = MATERIALS[mat_a]["rho"]
    rho_b = MATERIALS[mat_b]["rho"]
    
    R_a = (3 * m_kg / (4 * np.pi * rho_a))**(1/3)
    R_b = (3 * m_kg / (4 * np.pi * rho_b))**(1/3)
    
    ratio_a = l_m / R_a
    ratio_b = l_m / R_b
    S_a = min(1.0, ratio_a**3 / 6.0)
    S_b = min(1.0, ratio_b**3 / 6.0)
    
    L_a = G * m_kg**2 * S_a / (HBAR * l_m)
    L_b = G * m_kg**2 * S_b / (HBAR * l_m)
    
    rate_ratio = L_a / L_b if L_b > 0 else float('inf')
    
    # What mass-only models predict
    L_mass_only = G * m_kg**2 / (HBAR * l_m)  # no S factor
    
    # Determine the regime
    both_far = ratio_a >= 1 and ratio_b >= 1
    both_near = ratio_a < 1 and ratio_b < 1
    mixed = not both_far and not both_near
    
    if both_far:
        regime = "far-field (both l > R): ratio = 1.0 (no discrimination)"
        discriminating = False
    elif both_near:
        # In near field: S = (l/R)^3/6, so Lambda ∝ l^2/R^3 ∝ l^2 rho
        expected_ratio = rho_a / rho_b  # near-field ratio = density ratio
        regime = f"near-field (both l < R): ratio = ρ_a/ρ_b = {expected_ratio:.2f}"
        discriminating = True
    else:
        regime = "mixed (one near, one far): maximum discrimination"
        discriminating = True
    
    return {
        "experiment": {
            "mass_amu": m_amu, "mass_kg": m_kg,
            "separation_m": l_m, "separation_um": l_m * 1e6,
            "material_a": mat_a, "material_b": mat_b,
        },
        "material_a": {
            "name": mat_a, "rho": rho_a,
            "R_m": R_a, "R_um": R_a * 1e6, "R_nm": R_a * 1e9,
            "l_over_R": ratio_a, "S_l_R": S_a,
            "Lambda_Hz": L_a,
        },
        "material_b": {
            "name": mat_b, "rho": rho_b,
            "R_m": R_b, "R_um": R_b * 1e6, "R_nm": R_b * 1e9,
            "l_over_R": ratio_b, "S_l_R": S_b,
            "Lambda_Hz": L_b,
        },
        "rate_ratio": {
            "GRUT": rate_ratio,
            "mass_only_models": 1.0,
            "difference_pct": abs(rate_ratio - 1.0) * 100,
            "discriminating": discriminating,
        },
        "regime": regime,
        "predictions": {
            "GRUT": f"Λ({mat_a})/Λ({mat_b}) = {rate_ratio:.4f}",
            "CSL": "Λ(A)/Λ(B) = 1.000 (no geometry dependence)",
            "constant_floor": "Λ(A)/Λ(B) = 1.000 (mass-only)",
            "DP_point": "Λ(A)/Λ(B) = 1.000 (point mass, no extended body)",
        },
        "verdict": {
            "measurable": abs(rate_ratio - 1.0) > 0.01,
            "precision_needed_pct": abs(rate_ratio - 1.0) * 100 / 5,  # 5-sigma
            "confirmation": f"Rate ratio = {rate_ratio:.3f} ± {abs(rate_ratio-1)*100/5:.1f}% (differs from 1.0)",
            "falsification": "Rate ratio = 1.000 within measurement error",
        },
    }


def optimal_material_pair(m_amu=1e9, l_m=1e-7):
    """Find the material pair with maximum rate ratio for best discrimination."""
    m_kg = m_amu * AMU
    best_ratio = 1.0
    best_pair = ("gold", "silica")
    
    results = []
    mat_names = list(MATERIALS.keys())
    for i in range(len(mat_names)):
        for j in range(i+1, len(mat_names)):
            a, b = mat_names[i], mat_names[j]
            rho_a, rho_b = MATERIALS[a]["rho"], MATERIALS[b]["rho"]
            R_a = (3*m_kg/(4*np.pi*rho_a))**(1/3)
            R_b = (3*m_kg/(4*np.pi*rho_b))**(1/3)
            S_a = min(1.0, (l_m/R_a)**3/6)
            S_b = min(1.0, (l_m/R_b)**3/6)
            L_a = G*m_kg**2*S_a/(HBAR*l_m)
            L_b = G*m_kg**2*S_b/(HBAR*l_m)
            ratio = L_a/L_b if L_b > 0 else 1
            deviation = abs(ratio - 1.0)
            
            results.append({
                "pair": f"{a} vs {b}", "ratio": ratio,
                "deviation_pct": deviation * 100,
                "rho_ratio": rho_a / rho_b,
            })
            
            if deviation > abs(best_ratio - 1.0):
                best_ratio = ratio
                best_pair = (a, b)
    
    results.sort(key=lambda x: x["deviation_pct"], reverse=True)
    
    return {
        "mass_amu": m_amu, "separation_m": l_m,
        "best_pair": best_pair,
        "best_ratio": best_ratio,
        "best_deviation_pct": abs(best_ratio - 1.0) * 100,
        "all_pairs": results[:10],  # top 10
    }


def separation_scan_two_materials(m_amu=1e9, mat_a="gold", mat_b="silica", n=100):
    """Scan the rate ratio as a function of separation.
    
    The ratio changes dramatically near the kink of each material.
    Maximum discrimination occurs when one material is in the near field
    and the other is in the far field.
    """
    m_kg = m_amu * AMU
    rho_a = MATERIALS[mat_a]["rho"]
    rho_b = MATERIALS[mat_b]["rho"]
    R_a = (3*m_kg/(4*np.pi*rho_a))**(1/3)
    R_b = (3*m_kg/(4*np.pi*rho_b))**(1/3)
    
    l_min = min(R_a, R_b) * 0.1
    l_max = max(R_a, R_b) * 20
    l_vals = np.logspace(np.log10(l_min), np.log10(l_max), n)
    
    data = []
    max_dev = 0
    l_max_dev = 0
    
    for l in l_vals:
        S_a = min(1.0, (l/R_a)**3/6)
        S_b = min(1.0, (l/R_b)**3/6)
        L_a = G*m_kg**2*S_a/(HBAR*l)
        L_b = G*m_kg**2*S_b/(HBAR*l)
        ratio = L_a/L_b if L_b > 0 else 1
        dev = abs(ratio - 1.0)
        
        data.append({
            "l_m": float(l), "log_l": float(np.log10(l)),
            "ratio": float(ratio), "deviation_pct": float(dev*100),
        })
        
        if dev > max_dev:
            max_dev = dev
            l_max_dev = l
    
    return {
        "mass_amu": m_amu, "mat_a": mat_a, "mat_b": mat_b,
        "R_a_m": R_a, "R_b_m": R_b,
        "max_deviation_pct": max_dev * 100,
        "l_at_max_deviation_m": l_max_dev,
        "optimal_separation": f"{l_max_dev*1e9:.1f} nm" if l_max_dev < 1e-6 else f"{l_max_dev*1e6:.2f} μm",
        "data": data,
    }
