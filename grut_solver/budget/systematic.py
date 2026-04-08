"""
Systematic Error Budget — Intrinsic theoretical uncertainties.

The constitutive law tau dPhi/dt + Phi = X is derived from a microscopic
T-matrix calculation. The derivation introduces systematic errors:

1. Ward residual: alpha = 1.177 (leading-order particle-hole violation)
   -> 2.1% uncertainty in constitutive parameters at kappa_0/k_F = 0.10
   -> 3.6% total quadrature uncertainty (tau shift + D shift + memory)

2. Exchange correction: does NOT restore Ward identity (H2 result)
   -> alpha pinned at 1.011 after exchange (negligible change)

3. Markovian approximation: eps_M from validity envelope (see usl/validity.py)

These are INTRINSIC theory errors — they exist even with perfect experiments.

From Programs H (H1-H3) and I (I1).
"""

import numpy as np


# Ward residual parameters (from program_h_ward_residual.py)
WARD_ALPHA = 1.177           # Scaling exponent: Delta_W ~ kappa_0^alpha
WARD_ALPHA_UNCERTAINTY = 0.043  # Uncertainty on alpha
WARD_ALPHA_WITH_EXCHANGE = 1.011  # After exchange correction (H2)

# Constitutive parameter uncertainties at kappa_0/k_F = 0.10 (from H3/I1)
DELTA_TAU_PCT = 1.5          # tau renormalization uncertainty [%]
DELTA_D_PCT = 1.2            # Noise coefficient uncertainty [%]
DELTA_MEMORY_PCT = 2.8       # Memory kernel uncertainty [%]
DELTA_TOTAL_PCT = 3.6        # Total quadrature uncertainty [%]

# Compressibility mismatch from H3
DELTA_KAPPA_PCT = 2.11       # delta_kappa/kappa at kappa_0/k_F = 0.10


def ward_classification(alpha: float = None) -> str:
    """Classify the Ward residual scaling.

    alpha >= 1.8: 'higher-order' (truncation artifact, benign)
    0.7 <= alpha < 1.8: 'leading-order' (ladder topology insufficient)
    alpha < 0.7: 'non-perturbative' (fundamental inconsistency)
    """
    if alpha is None:
        alpha = WARD_ALPHA

    if alpha >= 1.8:
        return "higher-order"
    elif alpha >= 0.7:
        return "leading-order"
    else:
        return "non-perturbative"


def constitutive_error_budget() -> dict:
    """Return the full systematic error budget for the constitutive sector.

    These errors propagate to ANY prediction derived from the constitutive law.
    The USL is insensitive to most of these (it lives in the gravitational
    sector, not the constitutive sector). But precision measurements of
    decoherence rates inherit this floor.
    """
    return {
        "ward_alpha": WARD_ALPHA,
        "ward_alpha_err": WARD_ALPHA_UNCERTAINTY,
        "ward_classification": ward_classification(),
        "exchange_correction_effective": False,  # H2: exchange does NOT help
        "ward_alpha_post_exchange": WARD_ALPHA_WITH_EXCHANGE,
        "delta_tau_pct": DELTA_TAU_PCT,
        "delta_D_pct": DELTA_D_PCT,
        "delta_memory_pct": DELTA_MEMORY_PCT,
        "delta_total_pct": DELTA_TOTAL_PCT,
        "delta_kappa_pct": DELTA_KAPPA_PCT,
        "note": (
            "The Ward residual alpha=1.177 means the self-consistent T-matrix "
            "violates the particle-hole Ward identity at LEADING ORDER. "
            "This is a systematic of the ladder approximation, not a fundamental "
            "inconsistency. The total constitutive uncertainty is 3.6% in quadrature. "
            "The USL prediction (gravitational sector) is structurally insensitive "
            "to this error."
        ),
    }


def apply_systematic_to_rate(lambda_hz: float, sector: str = "gravitational") -> dict:
    """Apply systematic error bars to a decoherence rate prediction.

    Parameters
    ----------
    lambda_hz : float   Predicted rate [Hz].
    sector : str        'gravitational' or 'constitutive'.

    Returns
    -------
    dict with rate, error_pct, rate_lo, rate_hi.
    """
    if sector == "gravitational":
        # USL is derived from the CTP influence functional, not from the
        # constitutive T-matrix. Its systematic is from the Markovian
        # approximation, not from the Ward residual.
        # The Ward residual does NOT directly affect the USL.
        error_pct = 0.0  # USL has zero constitutive systematic
        note = "Gravitational sector: Ward residual does not propagate."
    elif sector == "constitutive":
        error_pct = DELTA_TOTAL_PCT
        note = f"Constitutive sector: {DELTA_TOTAL_PCT}% systematic from Ward residual."
    else:
        error_pct = DELTA_TOTAL_PCT  # conservative
        note = "Unknown sector: applying full constitutive systematic."

    return {
        "rate_hz": lambda_hz,
        "systematic_pct": error_pct,
        "rate_lo": lambda_hz * (1 - error_pct / 100),
        "rate_hi": lambda_hz * (1 + error_pct / 100),
        "note": note,
    }
