"""Measurement backaction decoherence channel."""

import numpy as np
from grut_solver.constants import HBAR


def lambda_readout(eta_detection: float, n_photons_per_s: float,
                   omega_probe: float, l: float) -> float:
    """Decoherence from continuous position measurement (readout backaction) [Hz].

    Continuous monitoring of the particle position introduces measurement
    backaction via the Heisenberg uncertainty principle.

    The standard quantum limit (SQL) gives:
      Lambda_SQL = eta * Gamma_meas * (l / x_zpf)^2

    Parameters
    ----------
    eta_detection : float   Detection efficiency (0 to 1).
    n_photons_per_s : float Probe photon rate [Hz].
    omega_probe : float     Probe frequency [rad/s].
    l : float               Superposition separation [m].
    """
    if eta_detection <= 0 or n_photons_per_s <= 0 or l <= 0:
        return 0.0

    # Each detected photon localizes to ~ lambda_probe
    lambda_probe = 2 * np.pi * 3e8 / omega_probe if omega_probe > 0 else float('inf')
    if l < lambda_probe:
        decoh_per_photon = (l / lambda_probe)**2
    else:
        decoh_per_photon = 1.0

    return eta_detection * n_photons_per_s * decoh_per_photon
