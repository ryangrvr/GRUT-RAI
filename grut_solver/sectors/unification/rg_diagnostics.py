"""Running coupling diagnostics for unification analysis."""
import numpy as np

# SM one-loop beta coefficients (SU(3), SU(2), U(1)_Y with GUT normalization)
B_COEFFS = {"b1": 41/10, "b2": -19/6, "b3": -7}

# Couplings at M_Z (PDG)
ALPHA_MZ = {"alpha1": 1/59.0, "alpha2": 1/29.6, "alpha3": 1/8.4}

def alpha_running(mu_GeV: float, coupling: str = "alpha3") -> float:
    """One-loop running: 1/alpha(mu) = 1/alpha(M_Z) - b/(2pi) ln(mu/M_Z)."""
    M_Z = 91.2
    b = B_COEFFS[coupling.replace("alpha", "b")]
    inv_alpha_MZ = 1 / ALPHA_MZ[coupling]
    return 1 / (inv_alpha_MZ - b / (2*np.pi) * np.log(mu_GeV / M_Z))

def convergence_metric(mu_GeV: float) -> dict:
    """Compute spread of 1/alpha_i at scale mu."""
    inv_alphas = {}
    for name in ["alpha1", "alpha2", "alpha3"]:
        a = alpha_running(mu_GeV, name)
        inv_alphas[name] = 1/a if a > 0 else float('inf')
    vals = list(inv_alphas.values())
    spread = max(vals) - min(vals)
    return {"mu_GeV": mu_GeV, "inv_alphas": inv_alphas, "spread": spread,
            "note": "SM couplings do NOT unify. Spread never reaches zero."}

def find_closest_approach(mu_min: float = 1e4, mu_max: float = 1e18,
                           n_points: int = 200) -> dict:
    """Find the scale of closest approach (minimum spread)."""
    scales = np.geomspace(mu_min, mu_max, n_points)
    best = {"mu": 0, "spread": float('inf')}
    for mu in scales:
        r = convergence_metric(mu)
        if r["spread"] < best["spread"]:
            best = {"mu": mu, "spread": r["spread"]}
    return {**best, "note": "SM one-loop: miss by ~3% at ~10^15 GeV. No unification."}
