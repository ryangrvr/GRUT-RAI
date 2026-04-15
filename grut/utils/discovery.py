"""
Discovery Mode — Find unexpected correlations and relationships in GRUT.

Scans parameter space for coincidences, near-misses, and structural
connections that might point to deeper physics.
"""
import numpy as np
from grut.foundation.constants import G, HBAR, C, K_B, AMU, M_PLANCK, T_PLANCK, ALPHA_EM
from grut.foundation.anomaly import C_FINAL, R_ANOMALY, S_CTP

# All GRUT-derived constants
GRUT_CONSTANTS = {
    "C_FINAL": C_FINAL,
    "R_ANOMALY": R_ANOMALY,
    "S_CTP": S_CTP,
    "2-R": 2 - R_ANOMALY,
    "f_R": 2 - R_ANOMALY,
    "tau_0_s": 41.9e6 * 3.156e7,
    "H_inf": (2 - R_ANOMALY) / (S_CTP * 41.9e6 * 3.156e7),
    "Omega_Lambda": 0.6904,
    "eta_B": 6.57e-10,
    "m_dark_photon_GeV": 0.387,
    "g_dark": 0.917,
    "lambda_dark": 0.42,
    "K_koide": 2/3,
    "N_gen": 3,
    "N_eras": 329,
}

# Known physics constants for comparison
PHYSICS_CONSTANTS = {
    "alpha_EM": ALPHA_EM,
    "alpha_s_MZ": 0.1185,
    "sin2_theta_W": 0.2312,
    "m_electron_GeV": 0.000511,
    "m_muon_GeV": 0.10566,
    "m_tau_GeV": 1.77686,
    "m_proton_GeV": 0.938,
    "m_W_GeV": 80.377,
    "m_Z_GeV": 91.188,
    "m_Higgs_GeV": 125.25,
    "v_Higgs_GeV": 246.0,
    "M_Planck_GeV": 2.435e18,
    "Lambda_QCD_GeV": 0.200,
}


def find_numerical_coincidences(threshold=0.05):
    """Find pairs of constants whose ratio is close to a simple number."""
    simple_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 16, 24, 27, 36, 108,
                      1/2, 1/3, 2/3, 1/4, 3/4, 1/6, 1/9,
                      np.pi, 2*np.pi, 4*np.pi, np.pi**2,
                      np.e, np.sqrt(2), np.sqrt(3), np.log(2)]

    all_constants = {**GRUT_CONSTANTS, **PHYSICS_CONSTANTS}
    coincidences = []

    keys = list(all_constants.keys())
    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            a, b = all_constants[keys[i]], all_constants[keys[j]]
            if a == 0 or b == 0: continue
            ratio = a / b
            if ratio == 0: continue

            for s in simple_numbers:
                if s == 0: continue
                rel = abs(ratio / s - 1)
                if rel < threshold:
                    coincidences.append({
                        "a": keys[i], "b": keys[j],
                        "ratio": float(ratio), "near": float(s),
                        "deviation_pct": float(rel * 100),
                        "relation": f"{keys[i]} / {keys[j]} ≈ {s}"
                    })

    coincidences.sort(key=lambda x: x["deviation_pct"])
    return coincidences[:20]  # top 20


def find_scale_connections():
    """Find connections between GRUT scales and known physics scales."""
    tau_0 = 41.9e6 * 3.156e7
    H_inf = (2 - R_ANOMALY) / (S_CTP * tau_0)

    connections = []

    # tau_0 vs other timescales
    timescales = {
        "T_Planck": T_PLANCK,
        "1/H_inf": 1/H_inf,
        "age_universe": 13.8e9 * 3.156e7,
        "t_EW (1/T_EW)": HBAR / (160 * 1.602e-10),
        "t_QCD (1/Lambda_QCD)": HBAR / (0.200 * 1.602e-10),
    }
    for name, t in timescales.items():
        ratio = tau_0 / t
        connections.append({"from": "tau_0", "to": name, "ratio": float(ratio),
                            "log10_ratio": float(np.log10(ratio)) if ratio > 0 else 0})

    # Dark photon mass vs QCD scales
    m_A = 0.387  # GeV
    qcd_scales = {"m_pion": 0.135, "m_rho": 0.775, "Lambda_QCD": 0.200, "m_proton": 0.938}
    for name, m in qcd_scales.items():
        connections.append({"from": "m_dark_photon", "to": name,
                            "ratio": float(m_A / m), "note": f"387 MeV / {m*1000:.0f} MeV"})

    return connections


def parameter_correlations():
    """Check which GRUT parameters are correlated (changing one affects another)."""
    correlations = [
        {"params": ["R_anomaly", "Omega_Lambda"],
         "relation": "Ω_Λ = ((2-R)/(S τ₀ H₀))²",
         "sensitivity": "10% change in R → ~20% change in Ω_Λ",
         "type": "quadratic"},
        {"params": ["S_CTP", "Omega_Lambda"],
         "relation": "Ω_Λ ∝ 1/S²",
         "sensitivity": "10% change in S → ~20% change in Ω_Λ",
         "type": "inverse quadratic"},
        {"params": ["tau_0", "Omega_Lambda"],
         "relation": "Ω_Λ ∝ 1/τ₀²",
         "sensitivity": "10% change in τ₀ → ~20% change in Ω_Λ",
         "type": "inverse quadratic"},
        {"params": ["C_FINAL", "R_anomaly"],
         "relation": "R = |C_Cosmo / C_Final|",
         "sensitivity": "C_FINAL is scheme-protected; R inherits fragility from C_Cosmo",
         "type": "ratio"},
        {"params": ["g_dark", "m_dark_photon"],
         "relation": "m_A = g_dark × v",
         "sensitivity": "Linear: 10% change in g → 10% change in m_A",
         "type": "linear"},
        {"params": ["N_gen", "K_koide"],
         "relation": "K = 2/3 only for N = 3 (Z₃ identity)",
         "sensitivity": "Discrete: N ≠ 3 → K varies with θ",
         "type": "discrete"},
    ]
    return correlations


def full_discovery():
    """Run all discovery analyses."""
    return {
        "numerical_coincidences": find_numerical_coincidences(),
        "scale_connections": find_scale_connections(),
        "parameter_correlations": parameter_correlations(),
    }
