"""Neutrino oscillation observables — mass splittings and probability."""
import numpy as np

# Measured mass-squared differences (eV^2)
DM2_21 = 7.53e-5   # solar
DM2_32 = 2.453e-3  # atmospheric (absolute value)

def oscillation_probability_2flavor(dm2: float, L_km: float, E_GeV: float,
                                     sin2_2theta: float = 1.0) -> float:
    """Two-flavor oscillation probability.

    P = sin^2(2 theta) sin^2(1.27 dm^2 L / E)
    dm^2 in eV^2, L in km, E in GeV.
    """
    arg = 1.27 * dm2 * L_km / E_GeV
    return sin2_2theta * np.sin(arg)**2

def mass_splitting_summary() -> dict:
    """Measured mass-squared differences."""
    return {
        "dm2_21_eV2": DM2_21,
        "dm2_32_eV2": DM2_32,
        "ordering": "OPEN (normal or inverted)",
        "absolute_scale": "OPEN (lightest mass unknown)",
        "note": "Measured values. NOT derived from GRUT.",
    }
