"""
Vacuum Fixed Point — Two Candidate Formulas for H_∞

The vacuum expansion rate (cosmological constant) from GRUT constants.
Two candidates, both using R_anomaly = 1.15428 (the 3-loop anomaly ratio,
NOT R_volumetric = 1.5428 which is the archival boundary).

CANDIDATE 1: H_∞ = 1 / (R_anomaly × S × τ₀)
  Predicted: H_∞ = 1.931 × 10⁻¹⁸ Hz
  Ω_Λ = 0.725 (vs observed 0.70, +3.6%)

CANDIDATE 2 (better): H_∞ = (2 - R_anomaly) / (S × τ₀)
  Predicted: H_∞ = 1.885 × 10⁻¹⁸ Hz
  Ω_Λ = 0.690 (vs observed 0.70, -1.4%) — essentially Planck 2018

Constants used:
  R_anomaly = 1.15428  (|C_Cosmo / C_Final|, from 3-loop calculation)
  S = 108π = 339.292   (CTP normalization)
  τ₀ = 41.9 Myr        (canonical relaxation time)

R DISAMBIGUATION:
  R_anomaly = 1.15428 — the 3-loop anomaly ratio. Lives in constants.py.
    Gives sub-2% accuracy on H_∞. Used in both candidate formulas.
  R_volumetric = 1.5428 — the archival/whole-hole boundary.
    Gives ~24% error. Does NOT belong in the vacuum formula.
  These are different quantities from different physics. Must not be confused.

STATUS: CANDIDATE DERIVATION — two formulas, zero free parameters, sub-2%
accuracy. ~30 combinations tested, so P(coincidence) ~ 30-60%. A rigorous
CTP derivation would confirm or deny.
"""

import numpy as np
from grut_solver.constants import G, HBAR, C, T_PLANCK, L_PLANCK

# The three GRUT constants (all pre-existing, none fitted to cosmology)
R_ANOMALY = 1.15428             # |C_Cosmo / C_Final| (3-loop anomaly ratio)
S = 108 * np.pi                 # CTP normalization (= 339.292)
TAU_0_S = 41.9e6 * 3.1557e7    # 41.9 Myr in seconds (= 1.3222e15 s)
TAU_0_YR = 41.9e6

# NOTE: R_volumetric = 1.5428 is a DIFFERENT quantity (archival boundary).
# It does NOT belong in the vacuum formula. See R DISAMBIGUATION above.
R_VOLUMETRIC = 1.5428  # for reference only — NOT used in formulas

# Observed values (for comparison — NOT inputs)
H0_SI = 70.0 * 1e3 / 3.0857e22   # 70 km/s/Mpc
OMEGA_LAMBDA_OBS = 0.70
LAMBDA_OBS = 1.1056e-52           # m^-2


def candidate_1() -> dict:
    """Candidate 1: H_∞ = 1 / (R_anomaly × S × τ₀)

    The vacuum expansion rate = inverse of the anomaly-weighted
    response volume.
    """
    H_inf = 1.0 / (R_ANOMALY * S * TAU_0_S)
    H_inf_obs = H0_SI * np.sqrt(OMEGA_LAMBDA_OBS)

    return {
        "name": "Candidate 1",
        "formula": "H_inf = 1 / (R_anomaly * S * tau_0)",
        "H_inf_hz": H_inf,
        "H_inf_obs_hz": H_inf_obs,
        "ratio": H_inf / H_inf_obs,
        "accuracy_H_pct": abs(H_inf / H_inf_obs - 1) * 100,
        "Omega_Lambda": (H_inf / H0_SI)**2,
        "accuracy_OmL_pct": abs((H_inf / H0_SI)**2 / OMEGA_LAMBDA_OBS - 1) * 100,
        "Lambda_m2": 3 * H_inf**2 / C**2,
    }


def candidate_2() -> dict:
    """Candidate 2: H_∞ = (2 - R_anomaly) / (S × τ₀)

    The vacuum rate involves the "tipping distance" (2 - R).
    R_anomaly = 1.15428, so (2 - R) = 0.84572.

    Physical interpretation: the anomaly ratio R measures how far the
    cosmological sector deviates from the local sector. The factor
    (2 - R) is the complementary distance — how much "room" remains
    for vacuum expansion. When R = 1: (2-R) = 1, maximum rate.
    When R → 2: (2-R) → 0, no vacuum expansion (degenerate).
    """
    two_minus_R = 2.0 - R_ANOMALY
    H_inf = two_minus_R / (S * TAU_0_S)
    H_inf_obs = H0_SI * np.sqrt(OMEGA_LAMBDA_OBS)

    return {
        "name": "Candidate 2 (preferred)",
        "formula": "H_inf = (2 - R_anomaly) / (S * tau_0)",
        "two_minus_R": two_minus_R,
        "H_inf_hz": H_inf,
        "H_inf_obs_hz": H_inf_obs,
        "ratio": H_inf / H_inf_obs,
        "accuracy_H_pct": abs(H_inf / H_inf_obs - 1) * 100,
        "Omega_Lambda": (H_inf / H0_SI)**2,
        "accuracy_OmL_pct": abs((H_inf / H0_SI)**2 / OMEGA_LAMBDA_OBS - 1) * 100,
        "Lambda_m2": 3 * H_inf**2 / C**2,
    }


def both_candidates() -> dict:
    """Compare both candidates side by side."""
    c1 = candidate_1()
    c2 = candidate_2()

    return {
        "candidate_1": c1,
        "candidate_2": c2,
        "preferred": "Candidate 2",
        "reason": (
            f"Candidate 2 gives Omega_Lambda = {c2['Omega_Lambda']:.4f} "
            f"(vs Planck 0.6889, error {c2['accuracy_OmL_pct']:.1f}%). "
            f"Candidate 1 gives {c1['Omega_Lambda']:.4f} "
            f"(error {c1['accuracy_OmL_pct']:.1f}%). "
            f"The (2-R) factor has a natural interpretation as the "
            f"complementary anomaly distance."
        ),
        "constants_used": {
            "R_anomaly": R_ANOMALY,
            "S": S,
            "tau_0_s": TAU_0_S,
            "all_pre_existing": True,
            "none_fitted_to_cosmology": True,
        },
    }


def physical_interpretation() -> dict:
    """Physical meaning of the two candidates."""
    return {
        "tau_0": {
            "value": f"{TAU_0_YR/1e6:.1f} Myr",
            "origin": "3-loop gravitational anomaly coefficient C_FINAL",
            "role": "Local constitutive relaxation time (decoherence scale)",
        },
        "S": {
            "value": f"108 pi = {S:.2f}",
            "origin": "CTP influence functional normalization",
            "role": "Effective degrees of freedom in the closed-time-path",
        },
        "R_anomaly": {
            "value": f"{R_ANOMALY}",
            "origin": "|C_Cosmo / C_Final| from 3-loop calculation",
            "role": "Bridge between local and cosmological anomaly sectors",
            "NOT": "R_volumetric = 1.5428 (archival boundary, different quantity)",
        },
        "candidate_1_interpretation": (
            "H_∞ = 1/(R × S × τ₀): the vacuum expansion rate is the inverse "
            "of the anomaly-weighted response volume. The vacuum sustains "
            "one quantum of expansion in its CTP phase space."
        ),
        "candidate_2_interpretation": (
            "H_∞ = (2-R)/(S × τ₀): the vacuum rate is modulated by the "
            "complementary anomaly distance (2-R). When the cosmological "
            "anomaly equals the local anomaly (R=1), the rate is maximal. "
            "As R → 2, the two sectors cancel and the vacuum rate vanishes. "
            "R = 1.154 gives (2-R) = 0.846 — the vacuum is 84.6% of maximum."
        ),
    }


def honest_assessment() -> dict:
    """Is this a derivation or numerology?"""
    c2 = candidate_2()

    return {
        "in_favor": [
            "Three independently derived constants — none fitted to cosmology",
            f"Candidate 2: Omega_Lambda = {c2['Omega_Lambda']:.4f} (Planck: 0.6889, error {c2['accuracy_OmL_pct']:.1f}%)",
            "The (2-R) factor has a geometric interpretation (complementary anomaly distance)",
            "Both formulas produce the 10^-52 m^-2 scale without fine-tuning",
            "Connects to the self-referential threshold framework (Sectors 5 & 13)",
        ],
        "against": [
            "Found by systematic search (~30 combinations), not derived from a Lagrangian",
            "P(coincidence) ~ 30-60% given the number of combinations tested",
            "The exact step where these formulas emerge from the CTP action is not shown",
            "Accuracy depends on H_0: different with Planck (67.4) vs SH0ES (73) values",
        ],
        "what_would_confirm": (
            "A rigorous calculation showing that the CTP effective action in the "
            "zero-matter limit produces a vacuum energy whose Hubble rate is "
            "exactly (2-R)/(S × τ₀). This requires the full gravitational "
            "influence functional — Sector 12 territory."
        ),
        "what_would_kill": (
            "Better measurements of R_anomaly, S, or τ₀ that shift the predicted "
            "Ω_Λ outside the observed range. Or a rigorous CTP calculation that "
            "produces a different formula."
        ),
        "status": "CANDIDATE — not confirmed, not dismissed",
    }


def full_vacuum_analysis() -> dict:
    """Complete vacuum fixed point analysis with both candidates."""
    return {
        "candidates": both_candidates(),
        "interpretation": physical_interpretation(),
        "assessment": honest_assessment(),
    }
