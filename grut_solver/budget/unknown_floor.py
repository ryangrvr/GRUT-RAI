"""Unknown decoherence floor — the adversarial nuisance model.

THIS IS THE CRITICAL MODULE.

Any experiment that sees a decoherence plateau must answer:
"Could this plateau come from an UNKNOWN noise source rather than gravity?"

This module parameterizes all possible unknown floors and tests whether
they can mimic the GRUT prediction.
"""

import numpy as np


def lambda_constant_floor(Lambda_floor: float) -> float:
    """A constant, pressure-independent decoherence floor [Hz].

    This is the simplest nuisance model: some unknown physics produces
    a constant decoherence rate that mimics the GRUT plateau.

    One free parameter: Lambda_floor.

    GRUT distinguishes itself from this because:
    - The GRUT plateau HEIGHT depends on m^2 and S(l/R)
    - A constant floor does not vary with m or R
    - Two measurements at different m discriminate

    Parameters
    ----------
    Lambda_floor : float   The constant floor rate [Hz].
    """
    return max(0.0, Lambda_floor)


def lambda_mass_dependent_floor(Lambda_0: float, m: float, m_ref: float,
                                alpha: float) -> float:
    """A mass-dependent unknown floor [Hz].

    Lambda = Lambda_0 * (m / m_ref)^alpha

    Two free parameters: Lambda_0, alpha.
    GRUT predicts alpha = 2.0 exactly (or ~1 in near-field).
    If the data fit alpha != 2: either GRUT is wrong or this floor is wrong.

    Parameters
    ----------
    Lambda_0 : float   Reference rate at m_ref [Hz].
    m : float          Particle mass [kg].
    m_ref : float      Reference mass [kg].
    alpha : float      Mass scaling exponent.
    """
    if m <= 0 or m_ref <= 0 or Lambda_0 <= 0:
        return 0.0
    return Lambda_0 * (m / m_ref) ** alpha


def lambda_geometry_dependent_floor(Lambda_0: float, l: float, R: float,
                                    beta: float) -> float:
    """A geometry-dependent unknown floor [Hz].

    Lambda = Lambda_0 * (l/R)^beta

    Two free parameters: Lambda_0, beta.
    GRUT predicts beta = 3 in near-field (from extended body).
    Any other beta discriminates.

    Parameters
    ----------
    Lambda_0 : float   Reference rate [Hz].
    l : float          Superposition separation [m].
    R : float          Particle radius [m].
    beta : float       Geometry scaling exponent.
    """
    if Lambda_0 <= 0 or l <= 0 or R <= 0:
        return 0.0
    return Lambda_0 * (l / R) ** beta


def can_floor_mimic_grut(Lambda_grut_values: np.ndarray,
                         parameter_values: np.ndarray,
                         max_free_params: int = 2) -> dict:
    """Test whether a polynomial floor with <= max_free_params can fit GRUT.

    Fits Lambda = a_0 + a_1*x + a_2*x^2 + ... to the GRUT predictions.
    If the residual is small, the floor CAN mimic GRUT (bad for GRUT).
    If the residual is large, the floor CANNOT mimic GRUT (good for GRUT).

    Parameters
    ----------
    Lambda_grut_values : array  GRUT predictions at various parameter values.
    parameter_values : array    The varied parameter (m, R, P, etc.).
    max_free_params : int       Maximum polynomial degree + 1 for the floor.

    Returns
    -------
    dict with keys:
        can_mimic : bool   True if floor fits GRUT to < 10% residual.
        residual : float   RMS fractional residual of best fit.
        fit_params : array Best-fit polynomial coefficients.
    """
    if len(Lambda_grut_values) < max_free_params + 1:
        return {"can_mimic": True, "residual": 0.0, "fit_params": None,
                "reason": "Not enough data points to discriminate."}

    # Log-space fit for power-law discrimination
    valid = (Lambda_grut_values > 0) & (parameter_values > 0)
    if np.sum(valid) < max_free_params + 1:
        return {"can_mimic": True, "residual": 0.0, "fit_params": None,
                "reason": "Not enough valid data points."}

    log_x = np.log10(parameter_values[valid])
    log_y = np.log10(Lambda_grut_values[valid])

    # Fit polynomial in log-log space
    coeffs = np.polyfit(log_x, log_y, min(max_free_params - 1, len(log_x) - 1))
    log_y_fit = np.polyval(coeffs, log_x)

    residual = np.sqrt(np.mean((log_y - log_y_fit)**2))
    # In log10 space: residual of 0.1 = factor of 1.26 = 26% error

    can_mimic = residual < 0.05  # < 12% error = can mimic

    return {
        "can_mimic": can_mimic,
        "residual_dex": residual,
        "residual_pct": (10**residual - 1) * 100,
        "fit_params": coeffs,
        "fit_degree": len(coeffs) - 1,
        "reason": f"{'CAN' if can_mimic else 'CANNOT'} mimic GRUT with {max_free_params}-param floor "
                  f"(residual: {residual:.3f} dex = {(10**residual-1)*100:.1f}%)",
    }
