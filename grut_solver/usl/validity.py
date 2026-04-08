"""
USL Validity Envelope — Where the Markovian derivation is trustworthy.

The USL Lambda = G m^2 / (hbar l) is derived from the CTP influence
functional in the MARKOVIAN limit (instantaneous bath response).

This module defines the regime boundaries:
  W_tau* ~ 0.7 decades:  VALID/MARGINAL boundary (eps_M < 5%)
  W_tau** ~ 1.8 decades: MARGINAL/INVALID boundary (eps_M < 20%)

Beyond W_tau**, the full non-Markovian memory kernel is required.
The USL is NOT trustworthy in that regime.

W_tau = log10(tau_max / tau_min) for the spectral width of the bath.

From Program G (G2-A validity envelope).
"""

import numpy as np


# Markovian validity thresholds (from program_g_g2a_validity_envelope.py)
W_TAU_STAR = 0.7       # VALID/MARGINAL boundary [decades]
W_TAU_STAR_STAR = 1.8   # MARGINAL/INVALID boundary [decades]
EPS_VALID = 0.05         # Markovian error below this = VALID
EPS_MARGINAL = 0.20      # Markovian error below this = MARGINAL


def markovian_error(W_tau: float) -> float:
    """Estimated Markovian approximation error eps_M at spectral width W_tau.

    Empirical boundary law from Program G:
      eps_M ~ 0.55 * (1 - exp(-W_tau / 4.5))

    Parameters
    ----------
    W_tau : float   Spectral width of the bath [decades].

    Returns
    -------
    float   Estimated fractional error of the Markovian approximation.
    """
    if W_tau <= 0:
        return 0.0
    return 0.55 * (1.0 - np.exp(-W_tau / 4.5))


def validity_regime(W_tau: float) -> str:
    """Classify the Markovian validity regime.

    Returns 'VALID', 'MARGINAL', or 'INVALID'.
    """
    eps = markovian_error(W_tau)
    if eps < EPS_VALID:
        return "VALID"
    elif eps < EPS_MARGINAL:
        return "MARGINAL"
    else:
        return "INVALID"


def classify_system(system_name: str) -> dict:
    """Classify a named physical system's Markovian validity.

    Returns dict with W_tau, eps_M, regime, and whether USL is trustworthy.
    """
    # Physical archetype mapping from Program G
    archetypes = {
        "dilute_gas":       0.0,
        "dense_gas":        0.5,
        "warm_plasma":      1.5,
        "neutron_star":     3.0,
        "galaxy_interior":  5.0,
        "early_universe":   10.0,
        "lab_nanoparticle": 0.3,
        "lab_optomech":     0.1,
    }

    W = archetypes.get(system_name, None)
    if W is None:
        return {"error": f"Unknown system: {system_name}. Known: {list(archetypes.keys())}"}

    eps = markovian_error(W)
    regime = validity_regime(W)

    return {
        "system": system_name,
        "W_tau_decades": W,
        "eps_M": eps,
        "regime": regime,
        "usl_trustworthy": regime in ("VALID", "MARGINAL"),
        "needs_memory_kernel": regime == "INVALID",
    }


def usl_error_bar(m: float, l: float, R: float, W_tau: float = 0.3) -> dict:
    """Compute USL prediction WITH Markovian validity error bar.

    Parameters
    ----------
    m, l, R : float   Standard USL parameters.
    W_tau : float     Spectral width of the experimental bath [decades].

    Returns
    -------
    dict with lambda_grav, eps_markov, lambda_lo, lambda_hi, regime.
    """
    from grut_solver.usl.gravitational import lambda_grav

    Lg = lambda_grav(m, l, R)
    eps = markovian_error(W_tau)
    regime = validity_regime(W_tau)

    return {
        "lambda_grav": Lg,
        "eps_markov": eps,
        "lambda_lo": Lg * (1 - eps),
        "lambda_hi": Lg * (1 + eps),
        "regime": regime,
        "trustworthy": regime != "INVALID",
    }
