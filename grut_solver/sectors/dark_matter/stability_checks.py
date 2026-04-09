"""Generic stability and lifetime utilities."""
import numpy as np

AGE_UNIVERSE_S = 4.35e17  # seconds

def is_stable(lifetime_s: float) -> bool:
    """A DM candidate is stable if lifetime > age of universe."""
    return lifetime_s > AGE_UNIVERSE_S

def decay_width_to_lifetime(Gamma_GeV: float) -> float:
    """Convert decay width [GeV] to lifetime [s]. tau = hbar / Gamma."""
    hbar_GeV_s = 6.582e-25  # GeV s
    if Gamma_GeV <= 0: return float('inf')
    return hbar_GeV_s / Gamma_GeV
