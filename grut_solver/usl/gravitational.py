"""
GRUT USL — Gravitational Decoherence Rate

THE central prediction of the GRUT framework.
ZERO free parameters.

    Lambda_grav = G m^2 / (hbar l) * S(l/R)

where S(l/R) is the extended-body suppression factor from the Diosi integral.
"""

from grut_solver.constants import G, HBAR
import numpy as np


def suppression_factor(l: float, R: float) -> float:
    """Extended-body suppression factor S(l/R).

    For a uniform-density sphere of radius R with superposition separation l:
      S = 1                  for l >= 2R  (far-field, point-mass limit)
      S = (l/R)^3 / 6       for l <  2R  (near-field, overlapping)

    Derived from: Diosi integral over gravitational self-energy of extended
    mass distribution (Kappa-Prime, CTP influence functional).

    This correction can suppress the decoherence rate by up to 10^4
    at typical nanoparticle operating points. Point-mass Diosi-Penrose
    models miss this entirely.

    Parameters
    ----------
    l : float
        Superposition separation [m].
    R : float
        Particle radius [m]. Must be > 0.

    Returns
    -------
    float
        Dimensionless suppression factor in [0, 1].
    """
    if R <= 0:
        raise ValueError(f"Radius must be positive, got R={R}")
    if l <= 0:
        return 0.0

    ratio = l / R
    if ratio >= 2.0:
        return 1.0
    else:
        return min(1.0, (ratio ** 3) / 6.0)


def lambda_grav(m: float, l: float, R: float = None) -> float:
    """GRUT gravitational decoherence rate [Hz].

    Lambda = G m^2 / (hbar l) * S(l/R)

    ZERO free parameters. The rate is fully determined by (m, l, R)
    and fundamental constants (G, hbar).

    Parameters
    ----------
    m : float
        Mass of the object in superposition [kg].
    l : float
        Spatial separation of superposition branches [m].
    R : float, optional
        Particle radius [m]. If None, uses point-mass limit (S=1).

    Returns
    -------
    float
        Decoherence rate [Hz]. Always >= 0.
    """
    if m <= 0 or l <= 0:
        return 0.0

    rate_point = G * m**2 / (HBAR * l)

    if R is None:
        return rate_point

    S = suppression_factor(l, R)
    return rate_point * S


def lambda_grav_point(m: float, l: float) -> float:
    """Point-mass gravitational decoherence (Diosi-Penrose, no geometry).

    Lambda_DP = G m^2 / (hbar l)

    This is what GRUT reduces to for l >> 2R (far field).
    It is what the Diosi-Penrose model predicts for ALL l (no R dependence).
    """
    if m <= 0 or l <= 0:
        return 0.0
    return G * m**2 / (HBAR * l)


def t_coherence_grav(m: float, l: float, R: float = None) -> float:
    """Gravitational coherence time [s].

    t_coh = 1 / Lambda_grav = hbar l / (G m^2 S(l/R))
    """
    rate = lambda_grav(m, l, R)
    if rate <= 0:
        return float('inf')
    return 1.0 / rate


def boundary_mass(l: float, t_obs: float) -> float:
    """Quantum-classical boundary mass [kg].

    The mass above which gravitational decoherence destroys coherence
    within observation time t_obs at superposition separation l.

    m_boundary = sqrt(hbar l / (G t_obs))

    Parameters
    ----------
    l : float
        Superposition separation [m].
    t_obs : float
        Observation time [s].

    Returns
    -------
    float
        Boundary mass [kg]. Objects heavier than this are "classical"
        on the timescale t_obs at separation l.
    """
    if l <= 0 or t_obs <= 0:
        return 0.0
    return np.sqrt(HBAR * l / (G * t_obs))
