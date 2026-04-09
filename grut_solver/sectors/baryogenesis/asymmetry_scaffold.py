"""Toy baryon-asymmetry evolution scaffold."""
import numpy as np

ETA_B_OBSERVED = 6.1e-10  # baryon-to-photon ratio (Planck 2018)

def toy_asymmetry_evolution(epsilon: float, Gamma: float, T_dec: float,
                             T_i: float = 1e12, T_f: float = 1e2,
                             N_steps: int = 1000) -> dict:
    """Toy model: dN_B/dT = -epsilon * Gamma * exp(-(T/T_dec)^2) / T.
    This is NOT a physical baryogenesis calculation. It is a scaffold
    showing how CTP nonequilibrium dynamics could generate an asymmetry.
    """
    T = np.geomspace(T_i, T_f, N_steps)
    N_B = 0.0
    for i in range(1, len(T)):
        dT = T[i] - T[i-1]
        source = -epsilon * Gamma * np.exp(-(T[i]/T_dec)**2) / T[i]
        N_B += source * dT

    return {"N_B_final": N_B, "epsilon": epsilon, "Gamma": Gamma, "T_dec": T_dec,
            "note": "TOY MODEL — not a physical BAU calculation."}
