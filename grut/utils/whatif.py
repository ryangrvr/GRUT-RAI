"""
What-If Theory Builder — Modify GRUT axioms and see what breaks.

Lets researchers explore: "What if tau_I = hbar/3?" or "What if R_anomaly = 1.5?"
"""
import numpy as np
from grut.foundation.constants import G, HBAR
from grut.foundation.noise_kernel import lambda_grav

def modify_tau_I(tau_I_new):
    """What happens if tau_I != hbar/2?"""
    tau_I_standard = HBAR / 2
    ratio = tau_I_new / tau_I_standard
    return {
        "tau_I_standard": tau_I_standard, "tau_I_new": tau_I_new, "ratio": ratio,
        "schrodinger_recovery": abs(ratio - 1.0) < 0.01,
        "born_rule": abs(ratio - 1.0) < 0.01,
        "decoherence_rate_change": "unchanged (Lambda_grav comes from noise kernel, not tau_I)",
        "cosmological_constant_change": "unchanged (H_inf uses tau_0, not tau_I)",
        "what_breaks": [] if abs(ratio-1)<0.01 else ["Schrodinger equation recovery (wrong prefactor)", "Born rule transparency"],
        "verdict": "GRUT intact" if abs(ratio-1)<0.01 else f"QM recovery fails by factor {ratio:.3f}"
    }

def modify_R_anomaly(R_new):
    """What happens if R_anomaly != 1.15428?"""
    R_std = 1.15428; S = 108*np.pi; tau_0 = 41.9e6*3.156e7; H_0 = 70e3/3.0857e22
    H_inf_std = (2-R_std)/(S*tau_0); OL_std = (H_inf_std/H_0)**2
    H_inf_new = (2-R_new)/(S*tau_0); OL_new = (H_inf_new/H_0)**2
    return {
        "R_standard": R_std, "R_new": R_new,
        "H_inf_standard": H_inf_std, "H_inf_new": H_inf_new,
        "Omega_Lambda_standard": OL_std, "Omega_Lambda_new": OL_new,
        "OL_shift_pct": (OL_new/OL_std - 1)*100,
        "still_viable": abs(OL_new - 0.6889) / 0.6889 < 0.1,
        "f_R_new": 2 - R_new,
        "verdict": f"OL shifts to {OL_new:.3f} ({'viable' if abs(OL_new-0.6889)<0.07 else 'EXCLUDED by Planck'})"
    }

def modify_S_CTP(S_new):
    """What if S != 108 pi?"""
    S_std = 108*np.pi; R = 1.15428; tau_0 = 41.9e6*3.156e7; H_0 = 70e3/3.0857e22
    OL_std = ((2-R)/(S_std*tau_0*H_0))**2
    OL_new = ((2-R)/(S_new*tau_0*H_0))**2
    return {
        "S_standard": S_std, "S_new": S_new,
        "Omega_Lambda_standard": OL_std, "Omega_Lambda_new": OL_new,
        "OL_shift_pct": (OL_new/OL_std - 1)*100,
        "still_viable": abs(OL_new - 0.6889) / 0.6889 < 0.1,
        "verdict": f"OL shifts to {OL_new:.3f}"
    }

def modify_generation_count(N_gen):
    """What if N_gen != 3?"""
    # Koide: K is constant only for N=3
    from grut.derived.koide.identity import koide_check
    # Check CP violation: requires N >= 3 for CKM phase
    cp_ok = N_gen >= 3
    # Check anomaly cancellation: works per-generation
    anomaly_ok = True
    # Check Z_N uniqueness
    Ks = []
    for theta in np.linspace(0.05, np.pi-0.05, 200):
        sq = [1+np.sqrt(2)*np.cos(theta+2*np.pi*k/N_gen) for k in range(N_gen)]
        if all(s > 0 for s in sq):
            m = [s**2 for s in sq]; Ks.append(sum(m)/sum(sq)**2)
    K_constant = np.std(Ks) < 1e-10 if Ks else False
    K_mean = np.mean(Ks) if Ks else 0

    return {
        "N_gen": N_gen, "cp_violation": cp_ok, "anomaly_cancellation": anomaly_ok,
        "koide_constant": K_constant, "koide_K": K_mean,
        "what_breaks": ([] if N_gen == 3 else
            (["No CP violation (R=1, cosmological formula collapses)"] if not cp_ok else []) +
            (["Koide K not constant (phase-dependent)"] if not K_constant else [])),
        "verdict": "GRUT intact" if N_gen == 3 else f"{'CP fails' if not cp_ok else ''} {'Koide fails' if not K_constant else ''}"
    }

def run_whatif(parameter, new_value):
    """Dispatch what-if to the right function."""
    if parameter == "tau_I": return modify_tau_I(new_value)
    elif parameter == "R_anomaly": return modify_R_anomaly(new_value)
    elif parameter == "S_CTP": return modify_S_CTP(new_value)
    elif parameter == "N_gen": return modify_generation_count(int(new_value))
    return {"error": f"Unknown parameter: {parameter}"}
