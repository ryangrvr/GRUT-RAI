"""Competing decoherence models for comparison with GRUT."""

import numpy as np
from grut_solver.constants import AMU


def lambda_csl(m: float, l: float, R: float,
               lambda_CSL: float = 1e-16, r_CSL: float = 1e-7) -> float:
    """Continuous Spontaneous Localization (CSL) decoherence rate [Hz].

    TWO free parameters: lambda_CSL, r_CSL.
    Standard GRW values: lambda_CSL=1e-16 Hz, r_CSL=1e-7 m.
    Adler values: lambda_CSL=1e-8 Hz, r_CSL=1e-7 m.

    Lambda = lambda_CSL * (m/amu)^2 * f(R, r_CSL) * g(l, r_CSL)
    """
    if m <= 0 or l <= 0 or R <= 0:
        return 0.0

    n_nucleons = m / AMU

    # Geometry factor
    if R < r_CSL:
        f_geom = 1.0
    else:
        f_geom = (r_CSL / R) ** 3

    # Localization factor
    if l < r_CSL:
        g_loc = (l / r_CSL) ** 2
    else:
        g_loc = 1.0

    return lambda_CSL * n_nucleons**2 * f_geom * g_loc


def lambda_standard_qm() -> float:
    """Standard QM prediction for gravitational decoherence: exactly zero."""
    return 0.0


def lambda_dp_point(m: float, l: float) -> float:
    """Diosi-Penrose point-mass (no extended-body correction)."""
    from grut_solver.constants import G, HBAR
    if m <= 0 or l <= 0:
        return 0.0
    return G * m**2 / (HBAR * l)
