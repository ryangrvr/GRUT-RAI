"""
Module 6: Running coupling diagnostics.

Status: DOCUMENTED (analytical formulas). Whether GRUT modifies the QCD
beta function is an OPEN QUESTION.
"""

import numpy as np


def beta_function_1loop(g_s: float, N_f: int = 6, N_c: int = 3) -> float:
    """One-loop QCD beta function.

    beta(g_s) = -(11 N_c/3 - 2 N_f/3) g_s^3 / (16 pi^2)

    For N_c = 3, N_f = 6 (SM): coefficient b_0 = 11 - 4 = 7.
    beta < 0 => asymptotic freedom (coupling decreases at high energy).
    """
    b_0 = 11 * N_c / 3 - 2 * N_f / 3
    return -b_0 * g_s**3 / (16 * np.pi**2)


def alpha_s_running(mu: float, alpha_s_ref: float = 0.1185,
                     mu_ref: float = 91.2, N_f: int = 6, N_c: int = 3) -> float:
    """One-loop running of alpha_s = g_s^2 / (4 pi).

    alpha_s(mu) = alpha_s(mu_ref) / (1 + b_0 alpha_s(mu_ref)/(2 pi) ln(mu/mu_ref))

    Parameters
    ----------
    mu : float        Energy scale [GeV].
    alpha_s_ref : float  alpha_s at reference scale.
    mu_ref : float    Reference scale [GeV] (default: M_Z).
    """
    b_0 = 11 * N_c / 3 - 2 * N_f / 3
    if mu <= 0 or mu_ref <= 0:
        return 0.0
    return alpha_s_ref / (1 + b_0 * alpha_s_ref / (2 * np.pi) * np.log(mu / mu_ref))


def running_coupling_table() -> dict:
    """Compute alpha_s at several energy scales."""
    scales = [1.0, 2.0, 5.0, 10.0, 91.2, 200.0, 1000.0, 10000.0]
    results = []
    for mu in scales:
        a_s = alpha_s_running(mu)
        results.append({"mu_GeV": mu, "alpha_s": a_s})
    return {
        "table": results,
        "note": (
            "Standard one-loop QCD running. Whether GRUT's constitutive structure "
            "modifies this running is an OPEN QUESTION. The formulas here are "
            "standard QCD, not a GRUT prediction."
        ),
    }


# ── Open question ───────────────────────────────────────────
GRUT_MODIFICATION_STATUS = {
    "question": "Does the GRUT constitutive structure modify the QCD beta function?",
    "status": "OPEN",
    "note": (
        "If the constitutive target functional introduces additional terms "
        "in the QCD action, these could modify the running at some scale. "
        "No such modification has been computed or demonstrated."
    ),
}
