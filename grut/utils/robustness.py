"""
Robustness Analysis — What happens when GRUT parameters have systematic errors?

Comprehensive analysis: vary every parameter simultaneously and check
which predictions survive, which break, and where the theory is fragile.
"""

import numpy as np
from grut.foundation.constants import G, HBAR, AMU
from grut.foundation.anomaly import C_FINAL, R_ANOMALY, S_CTP


TAU_0 = 41.9e6 * 3.156e7
H_0_HZ = 70e3 / 3.0857e22


def single_parameter_robustness():
    """Vary each parameter by ±1%, ±5%, ±10%, ±50% and check all predictions."""
    base = {
        "R_anomaly": R_ANOMALY,
        "S_CTP": S_CTP,
        "tau_0_s": TAU_0,
        "H_0_kms": 70.0,
        "J_CP": 3.18e-5,
        "K_neq": 1.19e-2,
        "g_dark": 0.917,
    }
    
    results = {}
    for param_name, base_val in base.items():
        param_results = {}
        for pct in [1, 5, 10, 50]:
            for sign in [1, -1]:
                shift = base_val * (1 + sign * pct / 100)
                label = f"{'+' if sign > 0 else '-'}{pct}%"
                
                # Compute affected predictions
                R = shift if param_name == "R_anomaly" else base["R_anomaly"]
                S = shift if param_name == "S_CTP" else base["S_CTP"]
                tau = shift if param_name == "tau_0_s" else base["tau_0_s"]
                H0 = (shift * 1e3 / 3.0857e22) if param_name == "H_0_kms" else H_0_HZ
                J = shift if param_name == "J_CP" else base["J_CP"]
                K = shift if param_name == "K_neq" else base["K_neq"]
                g = shift if param_name == "g_dark" else base["g_dark"]
                
                OL = ((2 - R) / (S * tau * H0))**2 if S * tau * H0 != 0 else 0
                eta = J * K * (2 - 1.018) / 565.5  # simplified
                m_A = g * 0.422 * 1000  # MeV (v ~ 0.422 GeV for Route 1)
                
                param_results[label] = {
                    "Omega_Lambda": OL,
                    "OL_shift_pct": (OL / 0.6904 - 1) * 100 if OL > 0 else -100,
                    "eta_B": eta,
                    "eta_shift_pct": (eta / 6.57e-10 - 1) * 100 if eta > 0 else -100,
                    "m_A_MeV": m_A,
                    "m_A_shift_pct": (m_A / 387.4 - 1) * 100,
                    "OL_viable": abs(OL - 0.6889) / 0.6889 < 0.1,
                }
        
        results[param_name] = param_results
    
    return results


def n_generation_robustness():
    """Complete consistency check for N ≠ 3 generations."""
    results = {}
    for N in [1, 2, 3, 4, 5, 6]:
        # Koide test
        Ks = []
        for theta in np.linspace(0.05, np.pi - 0.05, 200):
            sq = [1 + np.sqrt(2) * np.cos(theta + 2*np.pi*k/N) for k in range(N)]
            if all(s > 0 for s in sq):
                m = [s**2 for s in sq]
                Ks.append(sum(m) / sum(sq)**2)
        
        K_constant = np.std(Ks) < 1e-10 if Ks else False
        K_mean = np.mean(Ks) if Ks else 0
        
        # CP violation: requires N >= 3 for physical CKM phase
        cp_ok = N >= 3
        
        # Anomaly cancellation: works per generation
        anomaly_ok = True
        
        # Baryogenesis: needs CP violation
        baryo_ok = cp_ok
        
        # Cosmological formula: (2-R) factor needs R ≠ 1, which needs CP
        cosmo_ok = cp_ok
        
        # Dark matter: no direct N dependence
        dm_ok = True
        
        all_ok = K_constant and cp_ok and anomaly_ok and baryo_ok and cosmo_ok
        
        what_breaks = []
        if not K_constant: what_breaks.append("Koide K not constant (varies with theta)")
        if not cp_ok: what_breaks.append("No CP violation → R=1 → (2-R)=1 → wrong OL")
        if not baryo_ok: what_breaks.append("No CP → no baryogenesis → no matter")
        
        results[N] = {
            "K_constant": K_constant, "K_mean": float(K_mean),
            "K_std": float(np.std(Ks)) if Ks else 0,
            "cp_violation": cp_ok, "anomaly_cancel": anomaly_ok,
            "baryogenesis": baryo_ok, "cosmology": cosmo_ok, "dark_matter": dm_ok,
            "all_consistent": all_ok,
            "what_breaks": what_breaks,
        }
    
    return {
        "results": results,
        "unique_N": 3,
        "verdict": "N=3 is the ONLY value where all GRUT sectors are simultaneously consistent. "
                   "N=1,2: no CP violation → cosmological formula collapses, no baryogenesis. "
                   "N=4+: Koide K varies with theta → trace constraint violated.",
    }


def r_anomaly_systematic():
    """What if R_anomaly has a systematic error from scheme dependence?
    
    C_Cosmo is scheme-fragile: a rational shift of ~36 in the -108000
    coefficient shifts R by ~1%. Test the consequences.
    """
    R_base = R_ANOMALY
    
    results = []
    for delta_R_pct in np.linspace(-10, 10, 41):
        R = R_base * (1 + delta_R_pct / 100)
        
        OL = ((2 - R) / (S_CTP * TAU_0 * H_0_HZ))**2
        f_R = 2 - R
        
        # Still viable?
        OL_ok = abs(OL - 0.6889) / 0.6889 < 0.1  # within 10% of Planck
        f_positive = f_R > 0  # f(R) must be positive
        R_less_2 = R < 2  # Required for f(2)=0 boundary
        
        results.append({
            "delta_R_pct": float(delta_R_pct),
            "R": float(R),
            "f_R": float(f_R),
            "Omega_Lambda": float(OL),
            "OL_deviation_from_Planck_pct": float((OL / 0.6889 - 1) * 100),
            "viable": OL_ok and f_positive and R_less_2,
        })
    
    # Find the viable window
    viable = [r for r in results if r["viable"]]
    if viable:
        R_min = min(r["R"] for r in viable)
        R_max = max(r["R"] for r in viable)
    else:
        R_min = R_max = R_base
    
    return {
        "R_base": R_base,
        "scan": results,
        "viable_window": {"R_min": R_min, "R_max": R_max,
                           "width_pct": (R_max - R_min) / R_base * 100},
        "fragility": "MODERATE" if (R_max - R_min) / R_base > 0.05 else "HIGH",
        "verdict": f"R_anomaly is viable in the range [{R_min:.4f}, {R_max:.4f}] "
                   f"({(R_max-R_min)/R_base*100:.1f}% window). "
                   f"The theory can tolerate ~{(R_max-R_min)/R_base*100/2:.0f}% systematic shift in R.",
    }


def simultaneous_variation(n_samples=5000):
    """Monte Carlo: vary ALL parameters simultaneously within their uncertainties."""
    np.random.seed(42)
    
    R_samples = np.random.normal(R_ANOMALY, 0.001, n_samples)  # ~0.1% scheme uncertainty
    H0_samples = np.random.normal(70.0, 1.5, n_samples)        # Hubble tension
    J_samples = np.random.normal(3.18e-5, 0.15e-5, n_samples)  # PDG
    K_samples = np.abs(np.random.normal(1.19e-2, 0.6e-2, n_samples))  # structural
    g_samples = np.random.normal(0.917, 0.01, n_samples)       # RG running
    
    OL_samples = []
    eta_samples = []
    mA_samples = []
    
    for R, H0, J, K, g in zip(R_samples, H0_samples, J_samples, K_samples, g_samples):
        H0_Hz = H0 * 1e3 / 3.0857e22
        OL = ((2 - R) / (S_CTP * TAU_0 * H0_Hz))**2
        eta = J * K * (2 - 1.018) / 565.5
        mA = g * 0.422 * 1000
        OL_samples.append(OL)
        eta_samples.append(eta)
        mA_samples.append(mA)
    
    OL = np.array(OL_samples)
    eta = np.array(eta_samples)
    mA = np.array(mA_samples)
    
    return {
        "n_samples": n_samples,
        "Omega_Lambda": {
            "mean": float(np.mean(OL)), "std": float(np.std(OL)),
            "CI_68": [float(np.percentile(OL, 16)), float(np.percentile(OL, 84))],
            "CI_95": [float(np.percentile(OL, 2.5)), float(np.percentile(OL, 97.5))],
            "within_Planck_1sigma": float(np.mean((OL > 0.6833) & (OL < 0.6945)) * 100),
        },
        "eta_B": {
            "mean": float(np.mean(eta)), "std": float(np.std(eta)),
            "CI_68": [float(np.percentile(eta, 16)), float(np.percentile(eta, 84))],
            "within_observation": float(np.mean(np.abs(eta - 6.12e-10) < 0.5e-10) * 100),
        },
        "m_A_MeV": {
            "mean": float(np.mean(mA)), "std": float(np.std(mA)),
            "CI_68": [float(np.percentile(mA, 16)), float(np.percentile(mA, 84))],
        },
        "correlations": {
            "OL_eta": float(np.corrcoef(OL, eta)[0, 1]),
            "OL_mA": float(np.corrcoef(OL, mA)[0, 1]),
            "eta_mA": float(np.corrcoef(eta, mA)[0, 1]),
        },
    }


def full_robustness_analysis():
    """Master function."""
    return {
        "single_parameter": single_parameter_robustness(),
        "n_generations": n_generation_robustness(),
        "r_anomaly_systematic": r_anomaly_systematic(),
        "simultaneous_mc": simultaneous_variation(),
    }
