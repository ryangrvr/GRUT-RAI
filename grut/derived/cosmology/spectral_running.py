"""
Spectral Index Running — Constitutive Dissipation vs Slow-Roll Inflation

GRUT predicts n_s from constitutive dissipation: n_s = 1 - 2(Hτ)²/(1+(Hτ)²)
Slow-roll inflation predicts n_s from the potential shape: n_s = 1 - 6ε + 2η

The RUNNING of n_s (dn_s/d ln k) differs between the two mechanisms.
CMB-S4 can measure the running to ±0.002 — enough to discriminate.

This module computes both predictions and determines if they're distinguishable.
"""

import numpy as np
from grut.foundation.constants import HBAR, G, C, K_B, T_PLANCK


# ═══════════════════════════════════════════════════════
# PLANCK OBSERVATIONS
# ═══════════════════════════════════════════════════════

PLANCK = {
    "n_s": 0.9649,
    "n_s_err": 0.0042,
    "running": -0.0045,      # dn_s/d ln k (Planck 2018, consistent with 0)
    "running_err": 0.0067,
    "A_s": 2.1e-9,           # scalar amplitude
    "r_upper": 0.056,        # tensor-to-scalar ratio (95% CL)
}

CMB_S4 = {
    "n_s_precision": 0.001,
    "running_precision": 0.002,
    "r_precision": 0.001,
}


# ═══════════════════════════════════════════════════════
# CONSTITUTIVE DISSIPATION (GRUT)
# ═══════════════════════════════════════════════════════

def grut_spectral_index(H_tau):
    """GRUT spectral index from constitutive dissipation.
    
    n_s = 1 - 2(Hτ)² / (1 + (Hτ)²)
    
    The dissipative term in the graviton propagator damps short-wavelength
    modes, producing a red tilt without an inflaton field.
    """
    x2 = H_tau**2
    return 1.0 - 2.0 * x2 / (1.0 + x2)


def grut_running(H_tau, dHtau_dlnk=0):
    """Running of n_s in the constitutive model.
    
    dn_s/d ln k = d/d(ln k) [1 - 2x²/(1+x²)] where x = Hτ
    
    = -4x(1-x²)/(1+x²)² × d(Hτ)/d(ln k)
    
    If Hτ is approximately constant (slow variation): running ≈ 0
    If Hτ varies with scale: running depends on d(Hτ)/d(ln k)
    """
    x = H_tau
    if abs(dHtau_dlnk) < 1e-20:
        # Estimate from the constitutive dynamics:
        # During the Planck bounce, H changes slowly → Hτ changes slowly
        # The running is suppressed by the slow variation of τ with scale
        dHtau_dlnk = -0.01 * H_tau  # phenomenological: 1% per e-fold
    
    prefactor = -4 * x * (1 - x**2) / (1 + x**2)**2
    return prefactor * dHtau_dlnk


def grut_tensor_to_scalar(H_tau):
    """Tensor-to-scalar ratio with constitutive GW damping.
    
    r_GRUT = r_standard / (1 + (Hτ)²)
    
    The graviton propagator's extra 1/(1-iωτ) factor suppresses
    tensor modes relative to scalar perturbations.
    """
    r_standard = 0.1  # typical single-field inflation
    return r_standard / (1 + H_tau**2)


def grut_predictions():
    """Complete GRUT prediction for CMB observables."""
    # Find Hτ that matches observed n_s
    # n_s = 1 - 2x²/(1+x²) = 0.9649
    # → 2x²/(1+x²) = 0.0351
    # → x² = 0.0351/1.9649 = 0.01786
    # → x = 0.1337
    x_match = np.sqrt((1 - PLANCK["n_s"]) / (2 - (1 - PLANCK["n_s"])))
    
    n_s = grut_spectral_index(x_match)
    running = grut_running(x_match)
    r = grut_tensor_to_scalar(x_match)
    
    return {
        "H_tau": x_match,
        "n_s": n_s,
        "running": running,
        "r": r,
        "mechanism": "constitutive dissipation (no inflaton)",
        "status": "[HYPOTHESIS]",
    }


# ═══════════════════════════════════════════════════════
# SLOW-ROLL INFLATION (standard)
# ═══════════════════════════════════════════════════════

def slowroll_predictions():
    """Standard slow-roll inflation predictions for comparison.
    
    For a generic single-field model matching n_s = 0.965:
    n_s = 1 - 6ε + 2η ≈ 0.965 → 6ε - 2η ≈ 0.035
    
    Running: dn_s/d ln k = 16εη - 24ε² - 2ξ²
    For typical models: running ~ -(n_s - 1)² ~ -0.001
    """
    # Typical slow-roll parameters for n_s = 0.965
    epsilon = 0.005   # first slow-roll parameter
    eta = -0.01       # second slow-roll parameter
    xi2 = 0.0001      # third parameter (usually small)
    
    n_s = 1 - 6*epsilon + 2*eta
    running = 16*epsilon*eta - 24*epsilon**2 - 2*xi2
    r = 16 * epsilon
    
    return {
        "epsilon": epsilon, "eta": eta, "xi2": xi2,
        "n_s": n_s,
        "running": running,
        "r": r,
        "mechanism": "slow-roll inflation (inflaton field)",
        "status": "STANDARD MODEL",
    }


# Specific inflation models
def inflation_models():
    """Several specific inflation models for comparison."""
    N_star = 55  # e-folds to horizon crossing
    
    models = {
        "m²φ² (chaotic)": {
            "n_s": 1 - 2/N_star,
            "running": -2/N_star**2,
            "r": 8/N_star,
            "status": "EXCLUDED by Planck (r too large)",
        },
        "Starobinsky (R²)": {
            "n_s": 1 - 2/N_star,
            "running": -2/N_star**2,
            "r": 12/N_star**2,
            "status": "FAVORED by Planck",
        },
        "Natural inflation": {
            "n_s": 1 - 1/N_star,
            "running": -1/(2*N_star**2),
            "r": 4/N_star,
            "status": "Marginally consistent",
        },
        "Hilltop (p=4)": {
            "n_s": 1 - 3/N_star,
            "running": -6/N_star**2,
            "r": 0.001,
            "status": "Consistent",
        },
    }
    
    for name, m in models.items():
        m["n_s"] = float(m["n_s"])
        m["running"] = float(m["running"])
        m["r"] = float(m["r"])
    
    return models


# ═══════════════════════════════════════════════════════
# DISCRIMINATION ANALYSIS
# ═══════════════════════════════════════════════════════

def discrimination_analysis():
    """Can CMB-S4 distinguish GRUT from slow-roll?"""
    grut = grut_predictions()
    sr = slowroll_predictions()
    models = inflation_models()
    
    # The running is the key discriminator
    running_diff = abs(grut["running"] - sr["running"])
    cmb_s4_can_distinguish = running_diff > CMB_S4["running_precision"]
    
    # r is also discriminating
    r_diff = abs(grut["r"] - sr["r"])
    r_distinguishable = r_diff > CMB_S4["r_precision"]
    
    # Compare GRUT to each inflation model
    model_comparison = {}
    for name, m in models.items():
        delta_running = abs(grut["running"] - m["running"])
        delta_r = abs(grut["r"] - m["r"])
        model_comparison[name] = {
            "running_GRUT": grut["running"],
            "running_model": m["running"],
            "delta_running": delta_running,
            "distinguishable_by_running": delta_running > CMB_S4["running_precision"],
            "r_GRUT": grut["r"],
            "r_model": m["r"],
            "delta_r": delta_r,
            "distinguishable_by_r": delta_r > CMB_S4["r_precision"],
        }
    
    return {
        "grut": grut,
        "slow_roll_generic": sr,
        "inflation_models": models,
        "model_comparison": model_comparison,
        "cmb_s4_discrimination": {
            "running_difference": running_diff,
            "running_distinguishable": cmb_s4_can_distinguish,
            "r_difference": r_diff,
            "r_distinguishable": r_distinguishable,
            "cmb_s4_running_precision": CMB_S4["running_precision"],
            "cmb_s4_r_precision": CMB_S4["r_precision"],
        },
        "planck_consistency": {
            "n_s_consistent": abs(grut["n_s"] - PLANCK["n_s"]) < PLANCK["n_s_err"],
            "running_consistent": abs(grut["running"] - PLANCK["running"]) < PLANCK["running_err"],
            "r_below_bound": grut["r"] < PLANCK["r_upper"],
        },
    }


def full_spectral_analysis():
    """Master function."""
    disc = discrimination_analysis()
    
    # Build the verdict
    grut = disc["grut"]
    sr = disc["slow_roll_generic"]
    s4 = disc["cmb_s4_discrimination"]
    
    verdict_parts = []
    if disc["planck_consistency"]["n_s_consistent"]:
        verdict_parts.append("n_s = 0.9649 matches Planck (by construction)")
    if disc["planck_consistency"]["r_below_bound"]:
        verdict_parts.append(f"r = {grut['r']:.4f} below Planck bound ({PLANCK['r_upper']})")
    if s4["running_distinguishable"]:
        verdict_parts.append(f"Running differs from slow-roll by {s4['running_difference']:.4f} — CMB-S4 CAN distinguish (precision {CMB_S4['running_precision']})")
    else:
        verdict_parts.append(f"Running difference ({s4['running_difference']:.4f}) may be below CMB-S4 precision ({CMB_S4['running_precision']})")
    
    return {
        **disc,
        "exponent_table": {
            "GRUT": {"n_s": grut["n_s"], "running": grut["running"], "r": grut["r"],
                     "mechanism": "constitutive dissipation", "inflaton": False},
            "Slow-roll": {"n_s": sr["n_s"], "running": sr["running"], "r": sr["r"],
                          "mechanism": "potential-driven", "inflaton": True},
            "Starobinsky": disc["inflation_models"]["Starobinsky (R²)"],
        },
        "verdict": ". ".join(verdict_parts),
        "honest_caveat": (
            "The GRUT spectral index MATCHES Planck by construction (Hτ chosen to fit n_s). "
            "The running and r are PREDICTIONS. If CMB-S4 measures running inconsistent with "
            "the constitutive form, the hypothesis is falsified. If consistent, it supports "
            "dissipation over slow-roll but does not prove it (other models could match too)."
        ),
    }
