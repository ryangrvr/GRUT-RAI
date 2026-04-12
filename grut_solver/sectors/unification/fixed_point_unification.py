"""
Coupling Unification as Approach to a Unified Self-Referential Fixed Point

THE CLAIM: At the unification scale, the three gauge sectors (U(1), SU(2), SU(3))
merge into a single self-referential fixed point. Below that scale, they separate
into three external-target equations with different running rates.

The "running" of the couplings IS the approach to (or departure from) the unified
fixed point. The fact that they don't quite converge in the SM means the SM doesn't
quite achieve the unified self-referential condition.

WHAT WE CAN COMPUTE:
  1. The self-referential fraction for each coupling as a function of energy
  2. The unified threshold (where all three fractions converge)
  3. Whether a GRUT-type self-referential condition improves convergence
  4. The constitutive coupling at the fixed point

STATUS: Computed. Standard SM running + self-referential analysis.
"""

import numpy as np


# SM one-loop beta coefficients (SU(3)_C, SU(2)_L, U(1)_Y with GUT normalization)
B_COEFFS = {
    "alpha1": 41.0/10.0,   # U(1)_Y (GUT normalized: 5/3 factor)
    "alpha2": -19.0/6.0,   # SU(2)_L
    "alpha3": -7.0,         # SU(3)_C
}

# Couplings at M_Z = 91.2 GeV (PDG 2022)
ALPHA_MZ = {
    "alpha1": 1.0/59.0,    # GUT normalized
    "alpha2": 1.0/29.6,
    "alpha3": 0.1185,
}

M_Z = 91.2  # GeV


def inv_alpha_running(mu_GeV: float, coupling: str) -> float:
    """One-loop running: 1/alpha(mu) = 1/alpha(M_Z) - b/(2pi) ln(mu/M_Z)."""
    b = B_COEFFS[coupling]
    inv_alpha_MZ = 1.0 / ALPHA_MZ[coupling]
    return inv_alpha_MZ - b / (2 * np.pi) * np.log(mu_GeV / M_Z)


def self_referential_fraction_gauge(mu_GeV: float) -> dict:
    """Self-referential fraction for each gauge coupling.

    In the constitutive picture, each gauge sector has:
      f_self = 0: running dominates (external-target, perturbative)
      f_self = 1: at the fixed point (unified, self-referential)

    We define f_self via how close the three couplings are to each other:
      f_self = 1 - spread/spread_max

    where spread = max(1/alpha_i) - min(1/alpha_i)
    and spread_max = spread at M_Z (maximum separation).
    """
    inv_alphas = {}
    for name in ["alpha1", "alpha2", "alpha3"]:
        inv_alphas[name] = inv_alpha_running(mu_GeV, name)

    vals = list(inv_alphas.values())
    spread = max(vals) - min(vals)

    # Spread at M_Z (reference maximum)
    spread_MZ = max(1/ALPHA_MZ["alpha1"], 1/ALPHA_MZ["alpha2"], 1/ALPHA_MZ["alpha3"]) - \
                min(1/ALPHA_MZ["alpha1"], 1/ALPHA_MZ["alpha2"], 1/ALPHA_MZ["alpha3"])

    f_self = max(0, 1 - spread / spread_MZ) if spread_MZ > 0 else 0

    return {
        "mu_GeV": mu_GeV,
        "inv_alphas": inv_alphas,
        "spread": spread,
        "f_self": f_self,
    }


def unification_threshold() -> dict:
    """Find the energy where f_self is maximized (closest approach).

    This is the gauge analog of:
      - Lambda_QCD for confinement (Sector 6)
      - z ~ 0.33 for cosmology (Sector 5)
      - 38,000 neurons for consciousness (Sector 13)
    """
    mu_values = np.geomspace(1e4, 1e18, 500)

    best_mu = 0
    best_f = 0
    best_spread = float('inf')

    results = []
    for mu in mu_values:
        r = self_referential_fraction_gauge(mu)
        results.append(r)
        if r["f_self"] > best_f:
            best_f = r["f_self"]
            best_mu = mu
            best_spread = r["spread"]

    # At the closest approach, what are the coupling values?
    at_best = self_referential_fraction_gauge(best_mu)

    return {
        "mu_unification_GeV": best_mu,
        "log10_mu": np.log10(best_mu),
        "f_self_max": best_f,
        "spread_at_closest": best_spread,
        "inv_alphas_at_closest": at_best["inv_alphas"],
        "unified_alpha_approx": 1.0 / np.mean(list(at_best["inv_alphas"].values())),
        "sector_5_analogue": "z ~ 0.33 (cosmic self-reference onset)",
        "sector_13_analogue": "38,000 neurons (consciousness onset)",
        "sector_6_analogue": f"Lambda_QCD ~ 0.2 GeV (confinement onset)",
        "note": (
            f"Closest approach at mu = {best_mu:.2e} GeV "
            f"(10^{np.log10(best_mu):.1f} GeV). "
            f"f_self = {best_f:.3f} (spread = {best_spread:.1f}). "
            f"SM couplings do NOT fully unify (f_self < 1). "
            f"The 'miss' is the residual distance from the self-referential "
            f"fixed point — structurally analogous to the Ward residual (3.6%) "
            f"in the electroweak sector."
        ),
    }


def unification_profile(n_points: int = 300) -> dict:
    """Compute f_self(mu) across the full energy range."""
    mu_values = np.geomspace(100, 1e18, n_points)

    inv_a1 = [inv_alpha_running(mu, "alpha1") for mu in mu_values]
    inv_a2 = [inv_alpha_running(mu, "alpha2") for mu in mu_values]
    inv_a3 = [inv_alpha_running(mu, "alpha3") for mu in mu_values]
    f_self = [self_referential_fraction_gauge(mu)["f_self"] for mu in mu_values]

    return {
        "mu_GeV": mu_values.tolist(),
        "log10_mu": np.log10(mu_values).tolist(),
        "inv_alpha1": inv_a1,
        "inv_alpha2": inv_a2,
        "inv_alpha3": inv_a3,
        "f_self": f_self,
    }


def grut_modified_convergence() -> dict:
    """Would a GRUT self-referential condition improve convergence?

    In standard QCD, the three couplings miss by ~3% at ~10^15 GeV.
    If the constitutive equation's self-referential condition acts as
    an attractor at the unification scale, it could pull the couplings
    closer together — analogous to how the vacuum fixed point produces
    Omega_Lambda without dark energy.

    The question: does z = z_target[z] for the unified gauge field
    shift the couplings enough to close the gap?

    The constitutive modification: at the fixed point, each coupling
    satisfies alpha_i = alpha_target_i[alpha_1, alpha_2, alpha_3].
    The self-referential condition is: all three targets converge to
    a single value alpha_GUT.

    This is structurally identical to the vacuum condition (2-R)/(S tau_0):
    the fixed-point value is determined by the anomaly structure.
    """
    threshold = unification_threshold()
    spread = threshold["spread_at_closest"]

    # The Ward residual in Sector 2 is 3.6%
    # The unification miss is spread / (1/alpha_GUT) ~ spread * alpha_GUT
    alpha_gut_approx = threshold["unified_alpha_approx"]
    miss_fraction = spread * alpha_gut_approx if alpha_gut_approx > 0 else 0

    return {
        "sm_miss_at_closest": spread,
        "miss_as_fraction": miss_fraction,
        "ward_residual_sector_2": 0.036,
        "structural_parallel": (
            f"Unification miss: {miss_fraction:.3f} ({miss_fraction*100:.1f}%). "
            f"Ward residual (Sector 2): 3.6%. "
            f"These are structurally similar — both measure the distance "
            f"from a self-referential fixed point. The Ward residual is the "
            f"constitutive systematic in the electroweak sector. The "
            f"unification miss is the constitutive systematic in the gauge sector."
        ),
        "prediction": (
            "If GRUT's self-referential condition acts as an attractor, "
            "the unification miss should be related to the anomaly ratio R "
            "or the Ward residual. This is a testable structural prediction."
        ),
        "status": "OPEN — the constitutive modification to RG running has not been computed",
    }


def full_unification_fixed_point_analysis() -> dict:
    """Complete unification as fixed-point analysis."""
    threshold = unification_threshold()
    profile = unification_profile()
    modified = grut_modified_convergence()

    return {
        "threshold": threshold,
        "profile": profile,
        "modified_convergence": modified,
        "verdict": (
            f"Gauge coupling unification maps onto the fixed-point framework. "
            f"Closest approach at mu = 10^{threshold['log10_mu']:.1f} GeV "
            f"(f_self = {threshold['f_self_max']:.3f}). SM couplings don't "
            f"fully converge — the residual miss is structurally analogous "
            f"to the Ward residual in Sector 2 and the Hubble tension in "
            f"Sector 5. Whether the constitutive self-referential condition "
            f"improves convergence is an open calculation."
        ),
    }
