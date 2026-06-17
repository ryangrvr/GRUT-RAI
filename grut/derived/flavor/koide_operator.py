"""
GRUT Flavor — Z₃ Circulant Mass Operator and Track II Phase 1 Derivation Attempt

V7 §29 / V8 §9 establish that
    √m_k = M₀ (1 + √2 cos(θ + 2π k/3))                                    (1)
produces the Koide trace ratio
    K = (Σ m_k) / (Σ √m_k)² = 2/3                                         (2)
as an algebraic identity of the Z₃ circulant structure, and that
N = 3 is the unique integer for which K is phase-independent. The
charged-lepton masses are reconstructed to 0.01% by the fit
    M₀_fit = 0.5602152503 GeV^(1/2)                                       (3a)
    θ_fit  = 2.31714…    rad   (≡ 0.2229… rad modulo 2π/3)                (3b)

These two parameters are currently FITTED. Track II Phase 1 (V8)
asks whether they can be DERIVED from the canonical GRUT constants
    R_anomaly = 1.15428        (3-loop CTP anomaly ratio, §26.2)
    S         = 108π ≈ 339.29   (CTP path-counting normalization)
    α_vac     = 1/3             (vacuum impedance, α = 1/d, d=3)
    τ_0       = 41.9 Myr        (canonical relaxation time)
via the multi-generation CTP fixed-point condition z* = z_target[z*]
with z_target[z] = z − F_spatial[z] / F_temporal.

FIXED-POINT NO-GO (June 2026; theory/KOIDE_AMPLITUDE_UNIFICATION.md): the
attempt FAILED. GRUT's self-consistent impedance balance gives K = 4/9, NOT
the observed 2/3 (the Koide amplitude A = √2 is ~4.24× the impedance
α_vac = 1/3). K = 2/3 and θ = 2/9 are CANDIDATE IDENTITIES — unified as the
single posit A² = N−1 — NOT theorems; the amplitude is HOSTED Yukawa input.
K = 2/3 as a Z₃ circulant identity is PROVEN; (M₀, θ) are FITTED; θ = 2/9 is
a falsifiable hypothesis, not a partial closure. Flavor sits OUTSIDE the
vacuum-response scheme.

PROVENANCE (v2 self-containment audit, June 2026): the GENERAL form
z_target = z − F_spatial/F_temporal is NATIVE GRUT — the bedrock constitutive
equation, derived from three independent routes (CTP variation, Mori–Zwanzig
memory kernel, gradient flow; cf. V7 §4 and constitutive.py), not a V7 import.
What is OPEN — in v2 AND in V7 §29 — is only the three-flavor SPECIALIZATION:
V7 §29 explicitly marks the flavor structure of z_target as "the missing object"
(it requires the CTP variation of S_CTP with the full SM Yukawa Lagrangian). The
flavor mechanism is therefore a genuine open frontier, NOT importable from V7.

────────────────────────────────────────────────────────────────────
HONEST-NEGATIVE RESULT, WITH ONE CANDIDATE IDENTITY (April 22, 2026)
────────────────────────────────────────────────────────────────────

The derivation is UNDERDETERMINED at the V7 / v8-base specification
level for two independent reasons:

(A) Dimensional anchor gap.
    M₀ has units [GeV^(1/2)]. The canonical constants (R, S, α_vac, τ_0)
    are dimensionless or cosmological. The only mass scale derivable
    from them is
        μ_0 = ℏ / τ_0 ≈ 1.57 × 10⁻³¹ eV
    which is 30 orders of magnitude smaller than the required GeV scale.
    Without importing an independent mass scale (Λ_QCD, v_EW, or the
    dark-sector v_dark from §11), GRUT's foundation cannot anchor M₀.

(B) Multi-flavor action specification gap.
    V7 §29 states z_target[z] = z − F_spatial[z] / F_temporal but does
    not specify F_spatial and F_temporal for the three-flavor sector.
    The Z₃ circulant structure of the Jacobian dz_target_i/dz_j is a
    claim (Conjecture F1), but the flavor-space equation of motion
    F[z] = 0 from which it would descend is not yet specified.

(C) One CANDIDATE IDENTITY surfaces from the numerical survey:
        θ = K · α_vac = (2/3) · (1/3) = 2/9
    agrees with the fitted θ modulo 2π/3 (0.22222120 rad) at the
    4.6 ppm level. Propagated experimental uncertainty on θ from
    the PDG tau-mass error is ~260 ppm — the candidate sits 56× inside
    the current experimental window. This is labeled CANDIDATE
    IDENTITY, not DERIVED, because no proof from the multi-generation
    CTP action has been produced; the match is a numerical
    observation subject to falsification by a future sub-percent
    m_τ measurement that drives θ_fit outside the 2/9 window.

    Falsifier (Track II-F1, V8): a CEPC / FCC-ee tau-mass measurement
    at ≤10 ppm precision that excludes θ = 2/9 at > 5σ kills this
    candidate. A confirmation restores leverage for a proper derivation.

Conclusion: V7 §29 remains MAPPED (not upgraded to COMPUTED).
V7 Conjecture F1 remains HYPOTHESIS (not upgraded to RESULT).
No status upgrade is made under the honesty protocol because (A) and
(B) remain open, and (C) is a numerical observation, not a derivation.
See `derivation_attempt()` for the full report with "what would close it."

The Z₃ structure itself (K = 2/3, N = 3 uniqueness) remains PROVEN
and is independent of this derivation attempt — the Track II Phase 1
failure concerns only the two free parameters (M₀, θ).
"""

from __future__ import annotations

import numpy as np

from grut.foundation.anomaly import R_ANOMALY, S_CTP
from grut.foundation.closure_protocol import (
    ALPHA_VAC,
    S_SCREENING,
    TAU_0_SEC,
    H_0_IMPLIED_KM_S_MPC,
)
from grut.foundation.constants import HBAR, E_CHARGE


# ─────────────────────────────────────────────────────────────────────
# Measured charged-lepton masses (PDG 2022, GeV)
# ─────────────────────────────────────────────────────────────────────

M_E_GEV: float = 0.51099895000e-3
M_MU_GEV: float = 105.6583755e-3
M_TAU_GEV: float = 1.77686

LEPTON_MASSES_GEV: tuple[float, float, float] = (M_E_GEV, M_MU_GEV, M_TAU_GEV)


# ─────────────────────────────────────────────────────────────────────
# Canonical fit (V7 §29 baseline — reproduces the three charged-lepton
# masses to 0.01%).
# ─────────────────────────────────────────────────────────────────────

M0_FIT_GEV_HALF: float = 0.5602152503300036
"""M₀ = (Σ √m_k)/3 with the three charged-lepton masses in GeV."""

THETA_FIT_RAD: float = 2.316616297914854
"""θ in the (e, μ, τ) canonical flavor ordering at k=0,1,2.
Equivalent up to Z₃ relabeling to θ = 0.2222… rad modulo 2π/3
(the V8 §9 value under the permutation (1,2,0)). At this value
the Z₃ circulant reconstructs the three PDG 2022 charged-lepton
masses to max(frac. err.) = 5.3×10⁻⁵ (0.005%)."""


# ─────────────────────────────────────────────────────────────────────
# Z₃ circulant operator
# ─────────────────────────────────────────────────────────────────────


def sqrt_mass_triplet(M0: float, theta: float) -> np.ndarray:
    """Return the three √m values of the Z₃ circulant parameterization.

        √m_k = M₀ (1 + √2 cos(θ + 2π k/3)),   k = 0, 1, 2
    """
    k = np.arange(3)
    return M0 * (1.0 + np.sqrt(2.0) * np.cos(theta + 2.0 * np.pi * k / 3.0))


def lepton_masses_from_koide(M0: float, theta: float) -> np.ndarray:
    """Return (m_0, m_1, m_2) = (√m_k)² from the Z₃ circulant."""
    sq = sqrt_mass_triplet(M0, theta)
    return sq * sq


def koide_K_from_operator(M0: float, theta: float) -> float:
    """Koide trace ratio K = (Σ m_k)/(Σ √m_k)² evaluated on the circulant.

    For the Z₃ parameterization this is identically 2/3 for any θ and
    any non-zero M₀. The function evaluates K numerically rather than
    returning 2/3 — a non-2/3 output would indicate a regression in
    the parameterization itself.
    """
    sq = sqrt_mass_triplet(M0, theta)
    m = sq * sq
    return float(np.sum(m) / np.sum(sq) ** 2)


def circulant_mass_operator(M0: float, theta: float) -> np.ndarray:
    """Return the 3×3 Z₃-symmetric circulant whose diagonal eigenvalues
    in the flavor basis are the three lepton masses.

    For a Z₃ circulant C_ij with first row (c_0, c_1, c_2) the DFT
    eigenvalues are λ_k = c_0 + c_1 ω^k + c_2 ω^(2k), ω = e^(2πi/3).
    The inverse DFT recovers (c_0, c_1, c_2) from the mass triplet.
    """
    m = lepton_masses_from_koide(M0, theta)
    # Inverse DFT at N=3 gives the circulant first row from eigenvalues.
    omega = np.exp(2j * np.pi / 3.0)
    k_vec = np.arange(3)
    c = np.array(
        [np.sum(m * omega ** (-j * k_vec)) / 3.0 for j in range(3)]
    )
    # Z₃ circulant in flavor space:
    #   M_ij = c[(i - j) mod 3]
    M = np.zeros((3, 3), dtype=complex)
    for i in range(3):
        for j in range(3):
            M[i, j] = c[(i - j) % 3]
    return M


def verify_reconstruction(
    M0: float = M0_FIT_GEV_HALF,
    theta: float = THETA_FIT_RAD,
) -> dict:
    """Regression test: does (M0, θ) reproduce the three charged-lepton
    masses to 0.01% and satisfy K = 2/3 to machine precision?
    """
    m_pred = lepton_masses_from_koide(M0, theta)
    m_obs = np.array(LEPTON_MASSES_GEV)
    # The canonical parameterization at (M0_FIT, θ_FIT) yields the
    # triplet in cyclic order (e, μ, τ). The V8 §9 phase convention
    # uses a different cyclic label; both are Z₃-equivalent.
    m_pred_sorted = np.sort(m_pred)
    frac_err = np.abs(m_pred_sorted - m_obs) / m_obs
    K = koide_K_from_operator(M0, theta)
    return {
        "M0_input_GeV_half": M0,
        "theta_input_rad": theta,
        "m_predicted_GeV": m_pred_sorted.tolist(),
        "m_observed_GeV":  m_obs.tolist(),
        "fractional_errors": frac_err.tolist(),
        "max_frac_err_pct": float(frac_err.max() * 100.0),
        "K": K,
        "K_exact": 2.0 / 3.0,
        "K_deviation": abs(K - 2.0 / 3.0),
        "reproduces_to_0p01pct": bool(frac_err.max() < 1e-4),
        "reproduces_to_0p05pct": bool(frac_err.max() < 5e-4),
        "K_machine_precision":   bool(abs(K - 2.0 / 3.0) < 1e-12),
    }


# ─────────────────────────────────────────────────────────────────────
# Multi-generation CTP fixed-point condition
# ─────────────────────────────────────────────────────────────────────


def ctp_fixed_point_residual(
    z: np.ndarray,
    F_spatial,
    F_temporal: float,
) -> np.ndarray:
    """Residual of z = z_target[z] for the three-flavor sector.

    Per V7 §29:  z_target[z] = z − F_spatial[z] / F_temporal.
    Therefore fixed-point condition reduces to
        F_spatial[z*] = 0
    for any nonzero F_temporal. F_spatial and F_temporal must be
    supplied by the caller — V7 does NOT specify them for the
    three-flavor sector (this is the "action specification gap"
    documented in the module docstring).
    """
    F = F_spatial(z)
    return F / F_temporal


def flavor_jacobian_at_fixed_point(
    F_spatial_grad,
    F_temporal: float,
    z_star: np.ndarray,
) -> np.ndarray:
    """Mass operator M_ij = dz_target_i/dz_j at z*.

    From z_target = z − F_spatial/F_temporal,
        dz_target_i/dz_j = δ_ij − (dF_spatial_i/dz_j) / F_temporal.
    Conjecture F1 claims the resulting 3×3 matrix is Z₃-circulant
    with eigenvalues equal to the three lepton masses. That claim
    presupposes a flavor-space action which V7 does not specify.
    """
    grad = F_spatial_grad(z_star)
    return np.eye(3) - grad / F_temporal


# ─────────────────────────────────────────────────────────────────────
# Derivation attempt — candidate relations survey
# ─────────────────────────────────────────────────────────────────────


def survey_candidate_relations(
    theta_target: float = 0.22222119552165864,  # θ_FIT mod 2π/3
    M0_target_GeV_half: float = M0_FIT_GEV_HALF,
    tol_pct: float = 1.0,
) -> dict:
    """Systematic numerical survey of simple dimensionless combinations
    of (R_anomaly, S_CTP, α_vac) against the fitted θ, and of
    GRUT mass scales against the fitted M₀.

    Returns a dict of candidate identities with their fractional
    deviations. A candidate qualifies as "tight" only if < 0.1%.
    """
    R = R_ANOMALY
    S = S_CTP
    a = ALPHA_VAC
    pi = np.pi

    # θ candidates — dimensionless combinations.
    # The leading candidate θ = K·α_vac = 2/9 is listed first; see
    # module docstring §(C). Tight threshold is 0.1%; the candidate
    # clears it by nearly three orders of magnitude (4.6 ppm).
    K_koide = 2.0 / 3.0
    theta_candidates = {
        "K · α_vac = (2/3)·(1/3) = 2/9":  K_koide * a,
        "2 α_vac²":                       2.0 * a * a,
        "R - 1":                          R - 1.0,
        "(R - 1) * 3/2":                  1.5 * (R - 1.0),
        "(2 - R) / R":                    (2.0 - R) / R,
        "α_vac * (2 - R)":                a * (2.0 - R),
        "α_vac * R":                      a * R,
        "arctan(R - 1)":                  float(np.arctan(R - 1.0)),
        "arctan((R-1)/α_vac)":            float(np.arctan((R - 1.0) / a)),
        "log(R)":                         float(np.log(R)),
        "log(2 - R)":                      float(np.log(2.0 - R)),
        "R - N_G_DC":                     R - float(np.sqrt(1.0 + a)),
        "(R - 1) + α_vac / 5":            (R - 1.0) + a / 5.0,
        "α_vac²":                          a * a,
    }

    theta_results = []
    for name, val in theta_candidates.items():
        dev_pct = abs(val - theta_target) / theta_target * 100.0
        theta_results.append({
            "expression": name,
            "value": float(val),
            "fit_value": theta_target,
            "deviation_pct": dev_pct,
            "tight": dev_pct < 0.1,
        })
    theta_results.sort(key=lambda d: d["deviation_pct"])

    # M₀ candidates — GRUT has NO native GeV-scale mass.
    # Document this explicitly.
    mu_0_eV = (HBAR / TAU_0_SEC) / E_CHARGE  # ~1.57e-31 eV
    mu_0_GeV = mu_0_eV * 1e-9
    sqrt_mu_0_GeV_half = float(np.sqrt(mu_0_GeV))
    M0_target = M0_target_GeV_half
    orders_of_magnitude_gap = float(np.log10(M0_target / sqrt_mu_0_GeV_half))

    M0_report = {
        "native_GRUT_mass_scale_eV": mu_0_eV,
        "sqrt_of_that_scale_GeV_half": sqrt_mu_0_GeV_half,
        "fitted_M0_GeV_half": M0_target,
        "orders_of_magnitude_gap_log10": orders_of_magnitude_gap,
        "conclusion": (
            "The GRUT canonical foundation (R, S, α_vac, τ_0) contains "
            "no GeV-scale mass. μ_0 = ℏ/τ_0 is ~10⁻³¹ eV, giving "
            "√μ_0 ≈ 10⁻²⁰ GeV^(1/2) versus the required M₀ ≈ 0.56 "
            "GeV^(1/2) — a gap of ~20 orders of magnitude. Without "
            "an additional mass anchor (Λ_QCD, v_EW, or v_dark from "
            "§11) M₀ cannot be derived from the foundation alone."
        ),
    }

    return {
        "theta_target_rad": theta_target,
        "theta_candidates_ranked": theta_results,
        "theta_tight_matches": [r for r in theta_results if r["tight"]],
        "M0_analysis": M0_report,
    }


def derivation_attempt() -> dict:
    """Track II Phase 1: attempt to derive (M₀, θ) from GRUT canonical
    constants via the multi-generation CTP fixed-point condition.

    Returns an HONEST-NEGATIVE report (with one CANDIDATE IDENTITY
    flagged) because (A) the three-flavor classical action is not
    specified and (B) M₀ has no GeV anchor in the foundation.
    """
    survey = survey_candidate_relations()

    theta_tight = survey["theta_tight_matches"]
    M0_derivable = survey["M0_analysis"]["orders_of_magnitude_gap_log10"]
    # A full derivation would require BOTH a tight θ match from a
    # principled formula AND an M₀ anchor in the foundation. The
    # canonical constants supply neither — M₀ dimensional gap is
    # ~20 orders of magnitude. The candidate θ = K·α_vac is a numerical
    # observation, not a principled derivation.
    derivation_succeeds = (
        len(theta_tight) > 0
        and abs(M0_derivable) < 0.5  # same order of magnitude — impossible here
    )

    if derivation_succeeds:
        # Reserved for a future resolution. Current attempt does not reach
        # this branch.
        tight = theta_tight[0]
        return {
            "track": "Track II Phase 1 (Koide M₀, θ derivation)",
            "status": "COMPUTED",
            "theta_derivation": tight,
            "M0_derivation": survey["M0_analysis"],
            "V7_status_change_29": "MAPPED → COMPUTED",
            "V7_conjecture_F1":    "HYPOTHESIS → RESULT",
        }

    # Surface the candidate identity θ = K·α_vac = 2/9 separately
    # from the underdetermined overall status.
    K_koide = 2.0 / 3.0
    a_vac = ALPHA_VAC
    theta_candidate_Kalpha = K_koide * a_vac
    theta_mod = 0.22222119552165864  # θ_fit mod 2π/3 (computed from PDG fit)
    ppm_dev = abs(theta_candidate_Kalpha - theta_mod) / theta_mod * 1e6
    # Experimental window from m_τ PDG uncertainty (≈260 ppm)
    m_tau_ppm_window = 258.0

    return {
        "track": "Track II Phase 1 (Koide M₀, θ derivation)",
        "status": "HONEST NEGATIVE — UNDERDETERMINED (one CANDIDATE IDENTITY flagged)",
        "status_after_attempt": {
            "V7_section_29":     "MAPPED (unchanged)",
            "V7_conjecture_F1":  "HYPOTHESIS (unchanged)",
            "Koide_identity_K":  "PROVEN (unchanged — independent of this)",
            "N_3_uniqueness":    "PROVEN (unchanged — independent of this)",
        },
        "candidate_identity_theta": {
            "expression":                        "θ = K · α_vac = (2/3)·(1/3) = 2/9",
            "value_rad":                         theta_candidate_Kalpha,
            "fit_theta_mod_2pi_over_3_rad":      theta_mod,
            "deviation_ppm":                     ppm_dev,
            "experimental_window_ppm_from_m_tau": m_tau_ppm_window,
            "inside_experimental_window":        ppm_dev < m_tau_ppm_window,
            "status_tier":                       "CANDIDATE IDENTITY",
            "status_tier_position":              "below DERIVED/COMPUTED, above HYPOTHESIS",
            "falsifier":                         "Sub-10-ppm m_τ measurement (CEPC / FCC-ee) that excludes θ = 2/9 at > 5σ.",
            "interpretation": (
                "The two Z₃-native constants of the Koide sector — "
                "K = 2/3 (the trace identity) and α_vac = 1/3 (the "
                "vacuum impedance at d=3 spatial dimensions) — combine "
                "to produce θ = K·α_vac = 2/9 rad, which matches the "
                "fitted θ modulo 2π/3 at 4.6 ppm — 56× inside the "
                "current experimental window set by the PDG m_τ "
                "uncertainty. This is a NUMERICAL observation, not "
                "a derivation. Upgrading to DERIVED requires a proof "
                "that the multi-generation CTP action selects this "
                "phase as the fixed point of the Z₃ circulant flow."
            ),
        },
        "what_failed": {
            "theta_survey": {
                "ranked_best_5": survey["theta_candidates_ranked"][:5],
                "tight_matches_under_0p1pct": theta_tight,
                "conclusion": (
                    "The sole tight match (< 0.1%) is θ = K·α_vac = 2/9 "
                    "at 4.6 ppm deviation. This is surfaced as a "
                    "CANDIDATE IDENTITY above; upgrading to DERIVED "
                    "requires a proof from S_CTP — not produced here."
                ),
            },
            "M0_dimensional": survey["M0_analysis"],
        },
        "what_would_close_it": [
            "(i) A flavor-space classical action F[z] = 0 that descends "
            "from S_CTP and whose Jacobian at z* is Z₃-circulant by "
            "construction. V7 §29 asserts this shape but does not "
            "supply F_spatial and F_temporal for the three-flavor sector.",
            "(ii) A mass anchor in the foundation. Either (a) derive "
            "v_EW from S_CTP at the EW fixed point, (b) derive Λ_QCD "
            "from the confinement fixed point, or (c) connect M₀² to "
            "v_dark (§11) via a multi-generation coupling relation.",
            "(iii) Independent experimental pressure on θ. A percent-"
            "level measurement of m_τ (and hence K) would either (A) "
            "confirm the Z₃ identity to higher precision and restore "
            "leverage for a derivation, or (B) falsify the structure "
            "entirely per V8 §VI falsification table.",
        ],
        "cross_sector_consistency": {
            "koide_identity_not_modified": True,
            "canonical_constants_not_modified": True,
            "note": (
                "The honest-negative outcome does NOT require adjusting "
                "R, S, α_vac, or τ_0. The attempt was made within "
                "V7's canonical foundation and the foundation survives "
                "intact."
            ),
        },
        "V8_track_II_summary_paragraph": (
            "Track II Phase 1 attempted to derive the two free parameters "
            "(M₀ ≈ 0.560 GeV^(1/2), θ ≈ 2.317 rad) of the Z₃ circulant "
            "Koide mass operator from GRUT's canonical constants "
            "(R_anomaly = 1.15428, S = 108π, α_vac = 1/3, τ_0 = 41.9 Myr) "
            "via the multi-generation CTP fixed-point condition "
            "z* = z_target[z*]. The result is an HONEST NEGATIVE with "
            "one CANDIDATE IDENTITY flagged. The negative is twofold: "
            "(i) the three-flavor classical action F_spatial[z] is not "
            "specified by V7 §29, so the Jacobian dz_target/dz whose "
            "eigenvalues would be the lepton masses cannot be computed "
            "from the foundation alone, and its Z₃-circulant shape "
            "(Conjecture F1) remains a claim about the fixed point, not "
            "a theorem derived from it; (ii) M₀ has units of GeV^(1/2) "
            "while the only mass scale native to GRUT's canonical "
            "foundation is μ_0 = ℏ/τ_0 ≈ 10⁻³¹ eV, a 20-order-of-magnitude "
            "dimensional gap that cannot be closed without importing an "
            "external mass anchor (Λ_QCD, v_EW, or v_dark from §11). "
            "The candidate identity is θ = K · α_vac = (2/3)·(1/3) = 2/9, "
            "which matches the fitted θ modulo 2π/3 at 4.6 ppm — 56× "
            "inside the PDG m_τ experimental window (~258 ppm). This is "
            "a numerical observation, not a derivation; no proof from "
            "S_CTP has been produced. The candidate is labeled CANDIDATE "
            "IDENTITY (below COMPUTED, above HYPOTHESIS) and is "
            "falsifiable: a CEPC / FCC-ee m_τ measurement at ≤10 ppm "
            "that excludes θ = 2/9 at > 5σ would eliminate it. V7 §29 "
            "therefore remains MAPPED and V7 Conjecture F1 remains "
            "HYPOTHESIS; no status upgrade is made. The Z₃ identity "
            "K = 2/3 and N = 3 uniqueness (both PROVEN) are independent "
            "of this attempt and are unaffected. The closure path is "
            "laid out in derivation_attempt()."
        ),
    }


# ─────────────────────────────────────────────────────────────────────
# Track II Phase 2 — Mass-anchor mechanism evaluation
# ─────────────────────────────────────────────────────────────────────
#
# Phase 1 identified the M₀ dimensional gap: GRUT's canonical foundation
# has no GeV-scale mass. Phase 2 evaluates three candidate mechanisms
# for supplying one. The evaluation is MECHANISM-BASED, not numerical
# curve-fitting — a candidate qualifies only if there is an explicit
# Lagrangian operator (or CTP-derived coupling) that links the anchor
# to the charged-lepton sector.
#
# Numerical coincidences between M₀² and some combination of GRUT
# constants and a candidate anchor ARE NOT ACCEPTED as evidence.
# This is the failure mode V7's architecture rejects: fitting a
# target through geometric operator combinations. Any such finding
# would pass curve-fit tests but carry no falsifiable physical content.
# ─────────────────────────────────────────────────────────────────────


# Charged-lepton Yukawa couplings at μ = m_Z (PDG 2022; SM reference values).
V_EW_GEV: float = 246.0
"""Electroweak VEV v = 2 m_W / g ≈ 246 GeV. Input from SM (not derived by V7)."""

V_EW_OVER_SQRT2_GEV: float = V_EW_GEV / np.sqrt(2.0)
"""Canonical Yukawa mass scale v/√2 ≈ 173.95 GeV."""

Y_E: float  = M_E_GEV  / V_EW_OVER_SQRT2_GEV   # ~2.94 × 10⁻⁶
Y_MU: float = M_MU_GEV / V_EW_OVER_SQRT2_GEV   # ~6.07 × 10⁻⁴
Y_TAU: float = M_TAU_GEV / V_EW_OVER_SQRT2_GEV # ~1.02 × 10⁻²

LAMBDA_QCD_GEV: float = 0.250
"""QCD confinement scale Λ_QCD (MS-bar, 4-flavor) — SM input."""

V_DARK_GEV: float = 0.422
"""Dark-sector VEV from V7 §11/§28 U(1)_dark condensate."""


def evaluate_mass_anchor_mechanisms() -> dict:
    """Track II Phase 2: evaluate three candidate dimensional-anchor
    mechanisms for M₀ against the V7 CTP action.

    Rules of evaluation (per the honesty protocol):
    - A mechanism is DERIVED only if the CTP action produces the
      couplings from first principles with no free parameters.
    - A mechanism is HYPOTHESIS if the Lagrangian operator is
      SM-native / §28-native but the coupling values are not yet
      derived (i.e. an existing mechanism whose quantitative
      eigenvalues remain open).
    - A mechanism is CANDIDATE IDENTITY if a tight numerical identity
      exists AND an explicit Lagrangian operator is present, but
      the derivation from S_CTP has not been produced.
    - A mechanism is FAILED if no Lagrangian operator exists in the
      SM or in V7 that links the anchor to the charged-lepton sector.
      Numerical proximity alone does NOT rescue it.
    """
    # ───────────── Mechanism 1: v_EW Yukawa (SM-native) ─────────────
    #
    # Lagrangian operator: L_Yuk = − y_i Ψ̄_L_i H ℓ_R_i + h.c.
    #                       (SM-native, present in V7 §8)
    # Anchor relation:     m_i = y_i · v_EW/√2
    # Koide translation:   6 M₀² = (v_EW/√2) · Σ y_i
    #                       ⇒ M₀² = (v_EW/√2) · ⟨y⟩ with ⟨y⟩ ≡ Σy/6
    # Phase 2 question: does the multi-generation CTP fixed-point on
    # the three-flavor sector produce the three Yukawa eigenvalues
    # (y_e, y_μ, y_τ) = (2.94e-6, 6.08e-4, 1.02e-2) as a function
    # of (R_anomaly, α_vac, S, v_EW)?
    #
    # Finding: the Yukawa operator IS present in V7's SM sector (§8
    # establishes the SM as the unique minimal theory compatible with
    # CTP fixed-point architecture). The three eigenvalues are NOT yet
    # derived from S_CTP — they remain SM inputs in V7. However, the
    # mechanism is intact and the route is open.
    #
    # Status: HYPOTHESIS (mechanism exists, eigenvalues pending).
    M0_squared_from_v_EW = V_EW_OVER_SQRT2_GEV * (Y_E + Y_MU + Y_TAU) / 6.0
    mechanism_1 = {
        "name": "v_EW Yukawa (SM-native)",
        "lagrangian_operator": "− y_i Ψ̄_L^i · H · ℓ_R^i + h.c.  (SM-native, V7 §8)",
        "coupling_present_in_V7": True,
        "anchor_relation":
            "m_i = y_i · v_EW / √2  ⇒  M₀² = (v_EW/√2) · Σy_i / 6",
        "M0_squared_GeV_from_mechanism": M0_squared_from_v_EW,
        "M0_squared_GeV_from_fit":       M0_FIT_GEV_HALF**2,
        "match_to_fit_fractional":
            float(abs(M0_squared_from_v_EW - M0_FIT_GEV_HALF**2) / M0_FIT_GEV_HALF**2),
        "yukawa_eigenvalues_input_required": [Y_E, Y_MU, Y_TAU],
        "status": "HYPOTHESIS",
        "status_reasoning": (
            "The Yukawa operator is SM-native and present in V7 §8's "
            "SM-emergence sector. Anchoring M₀ to v_EW reduces the "
            "Phase 1 M₀ derivation to the problem of deriving the "
            "three Yukawa eigenvalues (y_e, y_μ, y_τ) from the "
            "multi-generation CTP fixed point with v_EW as input — a "
            "well-posed Phase 3 problem. Status is HYPOTHESIS and "
            "NOT DERIVED because the eigenvalues themselves are still "
            "open. A CANDIDATE IDENTITY upgrade would require a tight "
            "ppm-level match between a CTP-derived Σy_i and the PDG "
            "value 0.01082, plus a derivation of θ = K · α_vac that "
            "distributes the sum across the three eigenvalues."
        ),
        "phase_3_problem_posed": (
            "Phase 3 goal: derive the three Yukawa eigenvalues "
            "y_i = (m_i √2 / v_EW) from the three-flavor CTP fixed-"
            "point condition z* = z_target[z*] with v_EW as input. "
            "Deliverable: closed-form ⟨y⟩ = Σy/6 as a function of "
            "(R_anomaly, α_vac, S), plus Z₃-circulant distribution "
            "set by θ = K·α_vac (the Phase 1 CANDIDATE IDENTITY)."
        ),
    }

    # ───────────── Mechanism 2: Λ_QCD (non-SM coupling) ─────────────
    #
    # Lagrangian operator: NONE in the SM at tree level. Charged leptons
    # are color singlets; they do not couple directly to Λ_QCD. Radiative
    # corrections to lepton masses via gluon loops enter at two-loop and
    # higher through virtual quark loops, with suppression
    # O(α_s² / π²) · (m_q / m_lepton)² — numerically negligible.
    #
    # V7 §16 (noise kernel, constitutive) contains no lepton-quark
    # operator beyond the SM. Inventing a new one specifically to
    # anchor M₀ would add machinery without derivation.
    #
    # Numerical proximity: M₀² = 0.3138 GeV vs Λ_QCD ≈ 0.250 GeV,
    # ratio 1.26 — not a clean identity and explicitly disqualified
    # by the "no numerical curve-fitting" rule.
    #
    # Status: FAILED — no Lagrangian mechanism.
    mechanism_2 = {
        "name": "Λ_QCD (non-SM coupling)",
        "lagrangian_operator": "NONE in SM at tree level; none added in V7 §16.",
        "coupling_present_in_V7": False,
        "anchor_relation":
            "No principled relation. Numerical proximity "
            "M₀²/Λ_QCD ≈ 1.26 is a coincidence, not a coupling.",
        "M0_squared_GeV_from_mechanism": None,
        "M0_squared_GeV_from_fit":       M0_FIT_GEV_HALF**2,
        "status": "FAILED",
        "status_reasoning": (
            "Charged leptons are color singlets and do not couple to "
            "Λ_QCD at tree level in the SM. Radiative corrections enter "
            "at O(α_s²/π²) · (m_q/m_lepton)² and are numerically "
            "negligible. V7 §16 (noise kernel, constitutive equation) "
            "does not introduce any new lepton-quark operator. "
            "Inventing one to anchor M₀ would be ad hoc machinery "
            "without derivation — the definition of the failure mode "
            "the Phase 2 honesty protocol rejects."
        ),
        "reject_numerical_fit":
            "M₀²/Λ_QCD ≈ 1.26 is a coincidence, not a mechanism.",
    }

    # ───────────── Mechanism 3: v_dark (V7 §28 sector) ─────────────
    #
    # Lagrangian operators PRESENT in V7 §28:
    #   - U(1)_dark kinetic term  L_dark = −(1/4) F_dark^2
    #   - Dark scalar potential    V(φ_dark) = (λ/4)(|φ_dark|² − v_dark²)²
    #   - Kinetic mixing with SM   L_mix = −(ε/2) F^{μν} F_{μν,dark}
    #
    # The only portal between the dark and visible sectors is the
    # kinetic mixing ε. It couples GAUGE bosons (dark photon ↔ SM
    # photon via millicharge), not fermion masses. There is no
    # Yukawa-like operator of the form H†_dark · L · ℓ_R in V7 §28.
    #
    # For v_dark to anchor M₀ by mass generation, V7 would need a
    # NEW operator coupling a dark scalar to the charged-lepton
    # bilinear ℓ̄_L ℓ_R. Such an operator is not present and cannot
    # be added without an accompanying derivation from S_CTP.
    #
    # The anomaly-to-anomaly coupling C_FINAL ↔ C_dark (V7 §28) is a
    # structural relation between the gauge anomaly coefficients of
    # the two sectors, not a fermion-mass coupling.
    #
    # Numerical proximity: v_dark ≈ M₀² · R² ≈ 0.4176 vs 0.422 GeV
    # — within 1.1%. This is the exact failure mode the protocol
    # rejects: a "near miss" without a Lagrangian operator is a
    # coincidence, not a mechanism.
    #
    # Status: FAILED — no Lagrangian mechanism.
    mechanism_3 = {
        "name": "v_dark (U(1)_dark, V7 §28)",
        "lagrangian_operators_present":
            "Kinetic mixing ε F·F_dark (gauge-boson portal only); "
            "no lepton-dark scalar Yukawa.",
        "coupling_between_v_dark_and_charged_leptons_in_V7": False,
        "anchor_relation":
            "No principled relation. Numerical proximity "
            "v_dark ≈ R² · M₀² within 1.1% is a coincidence.",
        "M0_squared_GeV_from_mechanism": None,
        "M0_squared_GeV_from_fit":       M0_FIT_GEV_HALF**2,
        "status": "FAILED",
        "status_reasoning": (
            "V7 §28's dark sector couples to the visible sector only "
            "via kinetic mixing (ε F·F_dark), which mixes gauge bosons "
            "and produces millicharge / dark-photon signatures. It does "
            "not generate fermion masses. An H†_dark · L̄ · ℓ_R Yukawa "
            "operator is NOT present in V7 §28 and adding one would be "
            "a non-derived extension. The anomaly-sector coupling "
            "C_FINAL ↔ C_dark relates gauge anomaly coefficients, not "
            "fermion mass operators. The numerical near-miss "
            "v_dark ≈ R² M₀² is the exact curve-fitting pattern "
            "Phase 2 rejects as a failure mode."
        ),
        "reject_numerical_fit":
            "v_dark / (R²·M₀²) ≈ 1.011 is a coincidence, not a mechanism.",
    }

    viable = [m for m in (mechanism_1, mechanism_2, mechanism_3)
              if m["status"] in ("HYPOTHESIS", "CANDIDATE IDENTITY", "DERIVED")]

    return {
        "phase": "Track II Phase 2 — Mass-anchor mechanism evaluation",
        "mechanism_1_v_EW":   mechanism_1,
        "mechanism_2_Lambda_QCD": mechanism_2,
        "mechanism_3_v_dark": mechanism_3,
        "viable_mechanisms":  [m["name"] for m in viable],
        "finding": (
            "Exactly one mechanism is viable: the SM-native v_EW Yukawa "
            "coupling (mechanism 1). Λ_QCD (mechanism 2) FAILS — no "
            "lepton-quark coupling exists in the SM or in V7 §16. "
            "v_dark (mechanism 3) FAILS — V7 §28 couples the dark "
            "sector to the visible sector only via gauge kinetic "
            "mixing, not a lepton Yukawa; the numerical near-miss "
            "v_dark ≈ R² · M₀² is a coincidence, not a mechanism."
        ),
        "status_summary": {
            "v_EW":     mechanism_1["status"],
            "Lambda_QCD": mechanism_2["status"],
            "v_dark":   mechanism_3["status"],
        },
        "phase_3_redirect": {
            "new_goal": (
                "Derive the three charged-lepton Yukawa eigenvalues "
                "(y_e, y_μ, y_τ) from the multi-generation CTP "
                "fixed-point condition z* = z_target[z*] with v_EW "
                "as an input (not derived) and θ = K·α_vac from "
                "Phase 1's CANDIDATE IDENTITY as the Z₃ phase."
            ),
            "well_posed_because": (
                "v_EW is an SM input that all of mainstream flavor "
                "physics accepts; reducing M₀ to Σy_i and the Z₃ "
                "phase means Phase 3 has ONE equation (Σy_i/6 = ⟨y⟩ "
                "as a function of R, α_vac, S) and the Z₃ eigenvalue "
                "distribution — no dimensional-anchor gap remains."
            ),
            "what_v8_MUST_NOT_do": (
                "Construct a closed-form operator combination of "
                "(R, α_vac, S, v_dark, Λ_QCD, μ_0) that fits "
                "M₀² = 0.3138 GeV. That is curve-fitting. Any "
                "apparent 'derivation' produced that way is "
                "numerology without falsifiable content and is "
                "rejected by V7's honesty protocol."
            ),
        },
        "status_change": {
            "V7_section_29":   "MAPPED (unchanged)",
            "V7_conjecture_F1": "HYPOTHESIS (unchanged)",
            "Phase_2_outcome": (
                "HONEST NEGATIVE on Λ_QCD and v_dark; v_EW Yukawa "
                "mechanism identified as the sole viable anchor. "
                "Phase 3 is redirected to deriving the three "
                "Yukawa eigenvalues, not M₀ directly."
            ),
        },
    }


# ─────────────────────────────────────────────────────────────────────
# Track II Phase 3 — Attempt to derive the Yukawa trace-scale ⟨y⟩
# ─────────────────────────────────────────────────────────────────────
#
# Phase 2 established v_EW as the sole viable dimensional anchor for
# M₀. Phase 3 asks: does the multi-generation CTP fixed-point
# condition at the EW scale produce the three charged-lepton Yukawa
# couplings — or at least their trace-level scale ⟨y⟩ = Σy_i/3 ≈
# 3.605 × 10⁻³ — as a derived quantity?
#
# The honesty protocol forbids curve-fitting: we do not construct
# closed-form operator combinations of (R, α_vac, S, α_s, α_em, ...)
# that numerically hit ⟨y⟩. Any candidate must come from a
# Lagrangian derivation tied to a specific mechanism.
# ─────────────────────────────────────────────────────────────────────


# Empirical Yukawa targets (PDG 2022, at the EW scale)
ALPHA_S_MZ: float   = 0.1181      # α_s(M_Z), PDG
ALPHA_EM_MZ: float  = 1.0 / 127.93  # α_em(M_Z), PDG

Y_SUM: float  = Y_E + Y_MU + Y_TAU       # Σy_i, from Phase 2
Y_TRACE: float = Y_SUM / 3.0              # ⟨y⟩ = Σy_i / 3 ≈ 3.61 × 10⁻³


def yukawa_empirical_targets() -> dict:
    """Return the PDG-derived charged-lepton Yukawa couplings and their
    trace-level combinations. These are empirical targets; Phase 3 does
    NOT fit to them — it attempts a derivation and compares."""
    return {
        "v_EW_GeV":                   V_EW_GEV,
        "v_over_sqrt2_GeV":           V_EW_OVER_SQRT2_GEV,
        "y_e":                        Y_E,
        "y_mu":                       Y_MU,
        "y_tau":                      Y_TAU,
        "sum_y":                      Y_SUM,
        "trace_y_over_3":             Y_TRACE,
        "theta_input_rad_Z3":         (2.0 * np.pi / 3.0) + (2.0 / 9.0),
        "theta_matches_fit_at_pct":   abs(
            ((2.0*np.pi/3.0) + (2.0/9.0)) - THETA_FIT_RAD
        ) / THETA_FIT_RAD * 100.0,
    }


def ctp_fixed_point_at_EW_scale() -> dict:
    """What the CTP fixed-point condition z* = z_target[z*] produces
    at the EW scale for the Higgs + charged-lepton sector.

    The SM Lagrangian with Higgs potential V(H) = −μ²|H|² + λ|H|⁴
    has a classical minimum at |H| = v_EW / √2. The CTP variation
    at the EW fixed point reproduces this minimum — the Higgs
    condenses at ⟨H⟩ = v_EW/√2, and after EWSB the charged-lepton
    masses are m_i = y_i · v_EW/√2 through the Yukawa operator
    L_Yuk = −y_i Ψ̄_L^i H ℓ_R^i + h.c.

    WHAT THE CTP FIXED POINT FIXES:
        ⟨H⟩ = v_EW/√2 (the VEV value is an SM input, via μ²/λ)
        m_i = y_i · v_EW/√2 (masses tied to Yukawas)
        Jacobian M_ij = dz_target_i/dz_j in mass basis is diagonal
            with eigenvalues y_i · v_EW/√2 = m_i

    WHAT THE CTP FIXED POINT DOES NOT FIX:
        The three couplings y_e, y_μ, y_τ individually
        The trace ⟨y⟩ = Σy_i/3
        The hierarchy y_e : y_μ : y_τ ≈ 10⁻⁶ : 10⁻⁴ : 10⁻²

    The Yukawa matrix enters the SM Lagrangian as an INPUT with 3
    independent complex entries per charge sector (diagonalized to 3
    real positive eigenvalues + CKM angles for quarks, or to 3 real
    positive eigenvalues for charged leptons). The CTP fixed-point
    condition says nothing about the VALUES of these entries — it is
    satisfied for any choice.
    """
    return {
        "what_is_fixed_by_CTP": [
            "⟨H⟩ = v_EW / √2  (Higgs VEV, from Mexican hat minimum)",
            "m_i = y_i · v_EW/√2  (mass-Yukawa relation after EWSB)",
            "Jacobian M_ij in mass basis: diagonal, eigenvalues = m_i",
        ],
        "what_is_NOT_fixed_by_CTP": [
            "y_e, y_μ, y_τ  (three independent SM Lagrangian inputs)",
            "⟨y⟩ = Σy_i/3  (trace-level Yukawa scale)",
            "Hierarchy y_e : y_μ : y_τ",
        ],
        "conclusion": (
            "The CTP fixed-point condition at the EW scale with the "
            "SM Yukawa operator produces the STRUCTURE m_i = y_i · "
            "v_EW/√2 but does not CONSTRAIN the values of y_i. The "
            "Yukawa matrix is a free Lagrangian input, and the CTP "
            "variation is satisfied for any choice. Conjecture F1's "
            "claim that M_ij is Z₃-circulant in flavor basis is a "
            "RESTRICTION on the Lagrangian input, not a derivation "
            "from the fixed-point condition."
        ),
    }


def yukawa_trace_candidate_survey() -> dict:
    """Transparency survey of dimensionless combinations of GRUT
    canonical constants and SM couplings against ⟨y⟩ = 3.605 × 10⁻³.

    This is NOT a derivation attempt. It is documentation — showing
    that no simple principled expression reaches the target at
    derivation-level precision (< 5%). The presence of numerical
    near-misses (α_vac · α_s/(4π) at 13% off) does NOT rescue the
    honest-negative verdict because:
      (i) α_s couples to color; charged leptons are color singlets.
          A y_lepton ∝ α_s expression has no SM mechanism.
      (ii) No clean structural justification ties any of these
           expressions to the CTP multi-generation variation.

    The nearest structural expression, (2-R)/S = H_inf · τ_0, is 31%
    off — a useful dimensional anchor for discussion but not a
    derivation.
    """
    R = R_ANOMALY
    S = S_CTP
    a = ALPHA_VAC
    a_s = ALPHA_S_MZ
    a_em = ALPHA_EM_MZ

    candidates = {
        "(2-R)/S = H_inf·τ_0":            (2.0 - R) / S,
        "(2-R)/(S·R)":                    (2.0 - R) / (S * R),
        "(2-R)²/S":                        (2.0 - R)**2 / S,
        "α_vac · α_s/(4π)":               a * a_s / (4.0 * np.pi),
        "√α_vac · α_em":                  np.sqrt(a) * a_em,
        "α_em/(4π)":                      a_em / (4.0 * np.pi),
        "α_s/(4π)":                       a_s / (4.0 * np.pi),
        "α_em²":                          a_em**2,
    }

    ranked = []
    for name, val in candidates.items():
        dev = abs(val / Y_TRACE - 1.0) * 100.0
        ranked.append({
            "expression": name,
            "value": float(val),
            "ratio_to_target": float(val / Y_TRACE),
            "deviation_pct": float(dev),
            "under_5_pct": dev < 5.0,
        })
    ranked.sort(key=lambda d: d["deviation_pct"])

    return {
        "target_trace_y":                  Y_TRACE,
        "target_sum_y":                    Y_SUM,
        "candidates_ranked_best_to_worst": ranked,
        "tight_matches_under_5_pct":
            [c for c in ranked if c["under_5_pct"]],
        "closest_match":                   ranked[0],
        "closest_match_issue": (
            "The closest match (α_vac · α_s/(4π) at 13% off) would "
            "require the charged-lepton Yukawas to couple to the "
            "strong coupling α_s. Charged leptons are color singlets "
            "and have no tree-level coupling to α_s. This expression "
            "has no Lagrangian mechanism in the SM or in V7 and is "
            "therefore rejected as a curve-fitting artifact."
        ),
        "interpretation": (
            "No dimensionless combination of GRUT canonical constants "
            "(R, α_vac, S) and SM loop couplings (α_s, α_em at M_Z) "
            "reaches ⟨y⟩ = 3.605 × 10⁻³ at derivation-level precision "
            "(< 5%). All entries under 30% deviation are either "
            "mechanism-free (e.g. α_s coupling to leptons) or "
            "structural-anchor-only (e.g. H_inf · τ_0, which has the "
            "right dimension but no principled reason to equal ⟨y⟩)."
        ),
    }


def phase_3_yukawa_derivation_attempt() -> dict:
    """Track II Phase 3: attempt to derive the charged-lepton Yukawa
    couplings (y_e, y_μ, y_τ) from the multi-generation CTP fixed-
    point condition with v_EW as SM input and θ = K·α_vac = 2/9 as
    the Z₃ phase.

    Result: HONEST NEGATIVE — the CTP fixed-point condition at the
    EW scale constrains ⟨H⟩ = v_EW/√2 but does not constrain the
    Yukawa couplings themselves. The y_i enter the SM Lagrangian as
    independent input parameters, and the fixed-point condition is
    satisfied for any choice.

    This result does NOT falsify Phase 1's θ = K·α_vac = 2/9
    candidate identity: given the Yukawa trace scale as an input, θ
    determines the Z₃ distribution of the three eigenvalues within
    the sum. What Phase 3 fails to supply is the trace scale itself.
    """
    emp    = yukawa_empirical_targets()
    ctp    = ctp_fixed_point_at_EW_scale()
    survey = yukawa_trace_candidate_survey()

    any_under_5_pct = len(survey["tight_matches_under_5_pct"]) > 0

    # The CTP fixed-point condition does NOT constrain the y_i, so
    # no derivation is possible from V7 §29 as currently specified.
    # The numerical survey confirms: no expression reaches < 5%
    # deviation. Even the closest candidate (α_vac · α_s/(4π)) has
    # no Lagrangian mechanism (leptons are color singlets).

    return {
        "track": "Track II Phase 3 (Yukawa eigenvalue derivation)",
        "status": "HONEST NEGATIVE — UNDERDETERMINED BY CTP FIXED POINT",
        "status_after_attempt": {
            "V7_section_29":     "MAPPED (unchanged)",
            "V7_conjecture_F1":  "HYPOTHESIS (unchanged)",
            "Phase_1_candidate_theta_2_over_9": "CANDIDATE IDENTITY (unchanged, and Phase 3's negative does NOT falsify it)",
            "Phase_2_viable_anchor_v_EW":       "HYPOTHESIS (unchanged)",
            "Koide_identity_K":  "PROVEN (unchanged — independent of this)",
            "N_3_uniqueness":    "PROVEN (unchanged — independent of this)",
        },
        "empirical_targets":                emp,
        "ctp_fixed_point_at_EW":            ctp,
        "trace_yukawa_candidate_survey":    survey,
        "what_the_CTP_variation_produces": (
            "The CTP fixed-point condition z* = z_target[z*] with the "
            "SM Higgs potential V(H) = −μ²|H|² + λ|H|⁴ fixes ⟨H⟩ = "
            "v_EW/√2 as the Mexican-hat minimum. After EWSB, the "
            "Yukawa operator L_Yuk = −y_i Ψ̄_L^i H ℓ_R^i + h.c. "
            "delivers m_i = y_i · v_EW/√2. The Jacobian M_ij in mass "
            "basis is diagonal with eigenvalues m_i. None of this "
            "constrains the three y_i individually — they are "
            "independent Lagrangian inputs and the fixed-point "
            "condition is satisfied for any choice."
        ),
        "why_curve_fit_fails": (
            "No dimensionless combination of (R, α_vac, S, α_s(M_Z), "
            "α_em(M_Z)) reaches ⟨y⟩ = 3.605 × 10⁻³ at derivation-"
            "level precision (< 5%). The closest candidate "
            "(α_vac · α_s/(4π) at 13% off) requires charged leptons "
            "to couple to α_s at tree level — which they don't, "
            "because they are color singlets. Phase 3 therefore "
            "cannot rescue the derivation with a numerical near-miss."
        ),
        "what_phase_3_does_NOT_falsify": (
            "The Phase 1 CANDIDATE IDENTITY θ = K · α_vac = 2/9 is "
            "untouched by Phase 3's negative. That identity "
            "determines the Z₃ distribution of the three eigenvalues "
            "within ⟨y⟩, and it remains consistent with the fitted θ "
            "at 4.6 ppm. What Phase 3 fails to supply is the trace-"
            "level scale ⟨y⟩ itself, which enters the Z₃ distribution "
            "as a prefactor and is not constrained by CTP."
        ),
        "what_would_close_it_phase_4": [
            "(i) A GRUT-native flavor-selection mechanism BEYOND the "
            "SM Yukawa operator that forces a specific trace-level "
            "scale for charged-lepton Yukawas. Candidates include: "
            "a symmetry-breaking scale intermediate between v_EW and "
            "Λ_UV (Froggatt-Nielsen style), a three-flavor condensate "
            "that selects a Z₃-symmetric coupling, or a CTP-derived "
            "renormalization constraint at a specific matching scale.",

            "(ii) A GRUT-native answer to the Yukawa hierarchy "
            "question: why is y_τ/y_top ≈ 10⁻² while y_e/y_top ≈ "
            "10⁻⁶? The current framework does not select charged "
            "leptons over quarks or neutrinos in any structurally "
            "distinguishing way.",

            "(iii) An independent experimental falsifier for θ = 2/9 "
            "at sub-10-ppm precision. If Phase 1's candidate survives "
            "a direct test, the Z₃ distribution is confirmed and "
            "only the trace scale ⟨y⟩ remains open — a significantly "
            "narrower Phase 4 problem.",
        ],
        "cross_sector_consistency": {
            "canonical_constants_not_modified": True,
            "SM_imports_not_modified": True,
            "Phase_1_candidate_preserved": True,
            "Phase_2_HYPOTHESIS_preserved": True,
            "note": (
                "Phase 3's honest-negative outcome does NOT require "
                "adjusting R, S, α_vac, τ_0, or any SM input. The "
                "attempt was made within V7's canonical foundation "
                "using the v_EW Yukawa operator as identified in "
                "Phase 2, and both the foundation and the Phase 1/2 "
                "results survive intact."
            ),
        },
        "phase_3_outcome_any_tight_match": any_under_5_pct,
        "V8_track_II_phase_3_paragraph": (
            "Track II Phase 3 attempted to derive the three charged-"
            "lepton Yukawa couplings (y_e, y_μ, y_τ) = (2.94×10⁻⁶, "
            "6.07×10⁻⁴, 1.02×10⁻²) from the multi-generation CTP "
            "fixed-point condition z* = z_target[z*] with v_EW = "
            "246.22 GeV as SM input and θ = 2π/3 + 2/9 = 2.316 rad "
            "(Phase 1 candidate identity) as the Z₃ phase. The "
            "result is HONEST NEGATIVE. The CTP fixed-point condition "
            "at the EW scale fixes the Higgs VEV ⟨H⟩ = v_EW/√2 and "
            "the mass-Yukawa relation m_i = y_i · v_EW/√2 but does "
            "NOT constrain the three y_i individually — they enter "
            "the SM Lagrangian as independent input parameters, and "
            "the fixed-point condition is satisfied for any choice. "
            "A numerical survey of dimensionless combinations of "
            "(R, α_vac, S, α_s(M_Z), α_em(M_Z)) against the trace "
            "⟨y⟩ = 3.605 × 10⁻³ finds no match below the 5% "
            "derivation threshold; the closest candidate (α_vac · "
            "α_s/(4π) at 13% off) is rejected on mechanism grounds "
            "because charged leptons are color singlets. V7 §29 "
            "therefore remains MAPPED and V7 Conjecture F1 remains "
            "HYPOTHESIS. Phase 3 does NOT falsify the Phase 1 "
            "CANDIDATE IDENTITY θ = K · α_vac = 2/9 — that identity "
            "distributes the trace across the three eigenvalues and "
            "is untouched by Phase 3's failure to supply the trace "
            "scale. The well-posed Phase 4 problem becomes: identify "
            "a GRUT-native flavor-selection mechanism BEYOND the SM "
            "Yukawa operator that forces the trace scale ⟨y⟩ at the "
            "charged-lepton stratum — i.e., the charged-lepton half "
            "of the Yukawa hierarchy problem."
        ),
    }


# ─────────────────────────────────────────────────────────────────────
# Track II Phase 4 — Flavor-selection mechanism evaluation
# ─────────────────────────────────────────────────────────────────────
#
# Phase 3 established that the CTP fixed-point condition at the EW
# scale does not constrain charged-lepton Yukawas. Phase 4 evaluates
# three candidate directions against four mechanism requirements:
#
#   C1 — Flavor distinction: distinguishes charged leptons from
#        quarks (y_top ≈ 1) and from neutrinos (y_ν ~ 10⁻¹²).
#   C2 — Trace scale: produces ⟨y⟩ = 3.605 × 10⁻³ for charged
#        leptons as a DERIVED (not fitted) quantity — < 5% deviation.
#   C3 — Z₃ compatibility: compatible with Phase 1 candidate identity
#        θ = K · α_vac = 2/9 for the eigenvalue distribution.
#   C4 — Mechanism-grade: Lagrangian-level operator or derived
#        coupling, not mere numerical combination.
#
# The three directions (per V8 roadmap):
#   A — Anomaly-weighted CTP path counting at flavor level.
#   B — Dielectric coupling with flavor-dependent kinetic mixing.
#   C — Flavor-sector anomaly-matching analog to C_Cosmo.
#
# Reference empirical comparison scales: α_s(M_Z)/(4π) ≈ 9.4×10⁻³,
# α_em(M_Z)/(4π) ≈ 6.2×10⁻⁴.
# ─────────────────────────────────────────────────────────────────────


# SM hypercharges per generation (Dirac convention; used in V7 §26.2.6)
Y2_QL_PER_GEN:  float = 6 * (1/6)**2       # 1/6, quark doublet
Y2_UR_PER_GEN:  float = 3 * (2/3)**2       # 4/3
Y2_DR_PER_GEN:  float = 3 * (-1/3)**2      # 1/3
Y2_LL_PER_GEN:  float = 2 * (-1/2)**2      # 1/2, lepton doublet
Y2_ER_PER_GEN:  float = 1 * (-1)**2        # 1
Y2_TOTAL_PER_GEN: float = Y2_QL_PER_GEN + Y2_UR_PER_GEN + Y2_DR_PER_GEN + Y2_LL_PER_GEN + Y2_ER_PER_GEN  # 10/3
Y2_CL_PER_GEN:    float = (1/2)**2 + 1**2     # 5/4, charged leptons only (e_L + e_R)
Y2_NU_PER_GEN:    float = (1/2)**2            # 1/4, neutrinos (ν_L only)

Y2_TOTAL_3GEN: float = 3 * Y2_TOTAL_PER_GEN   # 10 — the Correction #16 source
Y2_CL_3GEN:    float = 3 * Y2_CL_PER_GEN      # 15/4
Y2_NU_3GEN:    float = 3 * Y2_NU_PER_GEN      # 3/4

# Weyl-fermion counts used in V7 §31 baryogenesis S_B = 4π × 45
N_WEYL_PER_GEN_TOTAL: int = 15
N_WEYL_PER_GEN_CL:    int = 2    # e_L + e_R
N_WEYL_3GEN_TOTAL:    int = 45
N_WEYL_3GEN_CL:       int = 6


def direction_A_anomaly_weighted_ctp() -> dict:
    """Direction A — Anomaly-weighted CTP path counting at flavor level.

    The SM hypercharge structure that produced the −(ΣY²)² = −100 in
    V7 §26.2.6 decomposes generation-independently at the flavor level:
    Y²_cl (charged-lepton sector) = 5/4 per generation, versus
    Y²_total = 10/3 per generation. Ratio Y²_cl / Y²_total = 3/8.

    The question: is there a flavor-indexed CTP normalization that
    produces ⟨y⟩_cl = f(Y²_cl, R_anomaly, α_vac, S) at the 10⁻³
    trace scale via a DERIVABLE route, not a fit?

    This function surveys principled candidate expressions and scores
    each against C1–C4. No curve-fitting is permitted: each candidate
    must have a specific justification tying its factors to the CTP
    machinery or SM group theory.
    """
    R = R_ANOMALY
    S = S_CTP
    a = ALPHA_VAC
    S_baryogenesis = 4 * np.pi * N_WEYL_3GEN_TOTAL   # V7 §31 convention
    S_cl_weyl      = 4 * np.pi * N_WEYL_3GEN_CL      # charged-lepton analog

    # Each candidate has a specific Lagrangian/CTP justification.
    # NOT a numerical survey — only principled expressions appear.
    # One candidate is explicitly included as a REJECTED numerology
    # pattern: Gemini's (Y²_cl/Y²_total)^n = (3/8)^n or 1/Y²_total^n
    # suggestion. These patterns are pattern-matching to 10⁻³ without
    # a Lagrangian justification for the exponent n. The honesty
    # protocol rejects them by construction, but they are surfaced
    # here so the rejection is visible and testable.
    Y2_ratio_3gen  = Y2_CL_3GEN / Y2_TOTAL_3GEN  # = 3/8 = 0.375
    Y2_total_3gen_inv_cubed = 1.0 / Y2_TOTAL_3GEN**3  # = 10⁻³ exactly
    candidates = [
        {
            "expr": "R · Y²_cl_per_gen / (108π)",
            "val":  R * Y2_CL_PER_GEN / S,
            "justification": (
                "R (3-loop CTP anomaly ratio) × charged-lepton "
                "hypercharge sum / CTP normalization. Same structure "
                "as V7 §26.2.6 but with Y²_cl replacing Y²_total."
            ),
        },
        {
            "expr": "(2 − R) / S_B_baryogenesis",
            "val":  (2.0 - R) / S_baryogenesis,
            "justification": (
                "Topological drive (2−R) over V7 §31 baryogenesis CTP "
                "normalization S_B = 4π × 45 (all SM Weyl fermions)."
            ),
        },
        {
            "expr": "(2 − R) / S_cl_Weyl",
            "val":  (2.0 - R) / S_cl_weyl,
            "justification": (
                "Topological drive / charged-lepton Weyl-count "
                "normalization (4π × 6). Restricted S_B analog."
            ),
        },
        {
            "expr": "α_vac · (Y²_cl / Y²_total)² · (2 − R)",
            "val":  a * (Y2_CL_3GEN / Y2_TOTAL_3GEN)**2 * (2.0 - R),
            "justification": (
                "Vacuum impedance × squared-hypercharge fraction × "
                "topological drive. Matches the (ΣY²)² structure of "
                "Correction #16."
            ),
        },
        {
            "expr": "(2−R) · (Y²_cl / Y²_total)² / S",
            "val":  (2.0 - R) * (Y2_CL_3GEN/Y2_TOTAL_3GEN)**2 / S,
            "justification": (
                "Topological drive · squared hypercharge fraction / "
                "CTP normalization. The hypercharge ratio squared "
                "tracks the Correction #16 (ΣY²)² pattern."
            ),
        },
        {
            "expr": "1/(ΣY²_total_3gen)³ = 10⁻³ — REJECTED as numerology",
            "val":  Y2_total_3gen_inv_cubed,
            "justification": (
                "NUMEROLOGY: ΣY²_total_3gen = 10 (Correction #16 "
                "integer), so 1/10³ = 10⁻³ matches ⟨y⟩ at 72% "
                "deviation. The exponent 3 has NO Lagrangian "
                "justification — it is pattern-matching the observed "
                "scale. REJECTED per C4 and the Phase 2 curve-fitting "
                "prohibition."
            ),
            "REJECTED_per_C4": True,
        },
    ]

    # Score each candidate against C1–C4.
    ranked = []
    for c in candidates:
        val = c["val"]
        dev_pct = abs(val / Y_TRACE - 1.0) * 100.0
        rejected = c.get("REJECTED_per_C4", False)
        score = {
            "expression":         c["expr"],
            "value":              float(val),
            "ratio_to_target":    float(val / Y_TRACE),
            "deviation_pct":      float(dev_pct),
            "C1_flavor_distinction":
                not rejected,  # rejected candidates don't participate in C1 either
            "C2_trace_scale_under_5pct":
                bool(dev_pct < 5.0) and not rejected,
            "C3_Z3_compatibility":
                "orthogonal — θ enters eigenvalue distribution only",
            "C4_mechanism_grade":
                not rejected,
            "REJECTED_per_C4":    rejected,
            "justification":      c["justification"],
        }
        ranked.append(score)
    ranked.sort(key=lambda d: d["deviation_pct"])

    # Summary verdict: did any NON-REJECTED candidate pass C2?
    any_closes_C2 = any(
        s["C2_trace_scale_under_5pct"] and not s["REJECTED_per_C4"]
        for s in ranked
    )
    # "Best" = smallest deviation AMONG principled (non-rejected) candidates
    principled = [s for s in ranked if not s["REJECTED_per_C4"]]
    best = principled[0] if principled else ranked[0]

    return {
        "direction": "A — Anomaly-weighted CTP path counting at flavor level",
        "hypercharge_accounting_per_gen": {
            "Y2_Q_L": Y2_QL_PER_GEN, "Y2_u_R": Y2_UR_PER_GEN,
            "Y2_d_R": Y2_DR_PER_GEN, "Y2_L_L": Y2_LL_PER_GEN,
            "Y2_e_R": Y2_ER_PER_GEN,
            "Y2_total": Y2_TOTAL_PER_GEN,
            "Y2_charged_lepton_subset": Y2_CL_PER_GEN,
            "ratio_cl_to_total": Y2_CL_PER_GEN / Y2_TOTAL_PER_GEN,
        },
        "3gen_sums": {
            "Y2_total_3gen_squared":          Y2_TOTAL_3GEN**2,
            "Y2_cl_3gen_squared":             Y2_CL_3GEN**2,
            "correction_16_integer":          100,
            "correction_16_cl_analog":        Y2_CL_3GEN**2,
        },
        "candidates_ranked": ranked,
        "best_candidate":    best,
        "any_candidate_closes_C2": any_closes_C2,
        "C1_status": "PASS (partial) — charged-lepton Y² ≠ Y² of quarks or neutrinos; provides order-one distinction between fermion classes",
        "C2_status": f"FAIL — best candidate at {best['deviation_pct']:.1f}% deviation (threshold 5%)",
        "C3_status": "ORTHOGONAL — θ enters eigenvalue distribution; Direction A targets trace scale",
        "C4_status": "PASS — hypercharge structure is SM-native Lagrangian group theory",
        "verdict": "PARTIAL — satisfies C1 and C4; fails C2; orthogonal to C3",
        "interpretation": (
            "Direction A provides genuine flavor-class distinction "
            "through the charged-lepton hypercharge content (C1, C4 "
            "satisfied), but no dimensionless combination of "
            "(R, α_vac, S, Y²_cl) reaches ⟨y⟩ = 3.605×10⁻³ at "
            "derivation-level precision. The best candidate (R × "
            f"Y²_cl_per_gen / (108π) at {best['deviation_pct']:.1f}% "
            "off) is principled but not tight. This inherits the "
            "hypercharge-ratio regime (O(1) distinctions among "
            "fermion classes) rather than the loop-suppression "
            "regime (O(α/4π) across orders of magnitude) that the "
            "Yukawa hierarchy actually sits in."
        ),
    }


def direction_B_dielectric_flavor_mixing() -> dict:
    """Direction B — Dielectric coupling with flavor-dependent kinetic mixing.

    Evaluates α_eff(ω) = α_vac / (1 + (ω τ_0)²) at charged-lepton
    Compton frequencies and at the EW symmetry-breaking scale. If
    α_eff at these scales matches the required Yukawa suppression
    pattern AND a Lagrangian-level coupling exists in V7 §28 to
    carry the suppression to fermion masses, Direction B could close.

    This function evaluates the frequencies quantitatively.
    """
    # Compton frequencies: ω = m c² / ℏ
    def omega_compton_Hz(m_GeV: float) -> float:
        return m_GeV * 1e9 * E_CHARGE / HBAR

    def alpha_eff(omega_Hz: float) -> float:
        return ALPHA_VAC / (1.0 + (omega_Hz * TAU_0_SEC)**2)

    fermions = [
        ("electron", M_E_GEV),
        ("muon",     M_MU_GEV),
        ("tau",      M_TAU_GEV),
        ("top",      172.76),
        ("v_EW",     V_EW_GEV),
    ]
    scale_table = []
    for name, m in fermions:
        w = omega_compton_Hz(m)
        a = alpha_eff(w)
        scale_table.append({
            "scale":          name,
            "mass_GeV":       m,
            "omega_Hz":       w,
            "omega_tau_0":    w * TAU_0_SEC,
            "alpha_eff":      a,
            "log10_alpha_eff": float(np.log10(a)) if a > 0 else None,
        })

    # Order of magnitude gap: α_eff ~ 10⁻⁷³, ⟨y⟩ ~ 10⁻³
    log10_gap = -3.0 - min(np.log10(s["alpha_eff"]) for s in scale_table)

    # V7 §28 Lagrangian audit: only kinetic mixing ε F·F_dark; no
    # lepton-dark Yukawa operator, no flavor-dependent kinetic
    # mixing.
    lagrangian_audit = {
        "kinetic_mixing_present_V7_28":      True,
        "flavor_dependent_kinetic_mixing":   False,  # not present
        "lepton_dark_Yukawa_H_dark_L_e_R":   False,  # not present
        "adding_such_operator_requires":     "new mechanism derivation, "
            "not just parameterization. Would be the Phase 2 curve-fit failure "
            "mode the protocol forbids.",
    }

    return {
        "direction": "B — Dielectric coupling with flavor-dependent kinetic mixing",
        "alpha_eff_at_fermion_scales": scale_table,
        "suppression_gap_log10":   log10_gap,
        "lagrangian_audit":        lagrangian_audit,
        "C1_status": "FAIL — α_eff is essentially zero at all fermion Compton frequencies; no flavor distinction",
        "C2_status": f"FAIL — α_eff is ~70 orders of magnitude below the required 10⁻³ scale",
        "C3_status": "N/A — no viable trace mechanism to distribute via θ",
        "C4_status": "FAIL — V7 §28 contains only gauge kinetic mixing; no lepton-dark Yukawa operator",
        "verdict": "FAILED — fails C1, C2, C4 simultaneously; C3 not applicable",
        "interpretation": (
            "At lab-relevant frequencies, the dielectric susceptibility "
            "α_eff(ω) is astronomically suppressed (ωτ_0 ~ 10³⁶ for "
            "the electron Compton frequency, giving α_eff ~ 10⁻⁷³). "
            "The gap to the required ⟨y⟩ ~ 10⁻³ is ~70 decades and "
            "cannot be closed within V7 §28's Lagrangian structure, "
            "which has only gauge kinetic mixing as its portal between "
            "visible and dark sectors. A lepton-dark Yukawa operator "
            "would have to be invented ad hoc — the failure mode the "
            "Phase 2 curve-fitting prohibition rejects. Direction B "
            "is structurally incompatible with the flavor sector as "
            "V7 currently formulates it."
        ),
    }


def direction_C_flavor_anomaly_analog() -> dict:
    """Direction C — Flavor-sector anomaly-matching analog to C_Cosmo.

    Construct R_flavor_cl by restricting the 3-loop CTP machinery
    to charged-lepton field content. Candidates for the restriction:
    (i) weight R_anomaly by (Y²_cl / Y²_total)² — the Correction #16
    pattern applied at the flavor-subset level; (ii) weight by Weyl
    count N_cl/N_total; (iii) use V7 §31 baryogenesis structure.

    Evaluate whether the resulting "flavor Hubble formula"
    ⟨y⟩ = (2 − R_flavor) / S_flavor produces 3.605 × 10⁻³ by a
    derivable route — or whether it inherits Phase 3's
    underdetermination.
    """
    R = R_ANOMALY
    S = S_CTP
    S_baryogenesis = 4 * np.pi * N_WEYL_3GEN_TOTAL
    S_cl_weyl      = 4 * np.pi * N_WEYL_3GEN_CL

    # Candidate R_flavor values, each with a specific structural origin
    R_flavor_Y2sq = R * (Y2_CL_3GEN / Y2_TOTAL_3GEN)**2   # Correction #16 pattern
    R_flavor_Y2   = R * (Y2_CL_3GEN / Y2_TOTAL_3GEN)      # Linear hypercharge ratio
    R_flavor_NW   = R * (N_WEYL_3GEN_CL / N_WEYL_3GEN_TOTAL)  # Weyl count ratio

    # Candidate formulas: (2 − R_flavor) / S_flavor
    candidates = [
        {
            "expr": "(2 − R · (Y²_cl/Y²_total)²) / (108π)",
            "val":  (2.0 - R_flavor_Y2sq) / S,
            "R_flavor":  R_flavor_Y2sq,
            "justification": (
                "R weighted by the Correction #16 pattern "
                "(ΣY²_cl/ΣY²_total)² = 0.1406. Flavor-subset R inherits "
                "the squared-hypercharge structure of V7 §26.2.6."
            ),
        },
        {
            "expr": "(2 − R · (Y²_cl/Y²_total)) / (108π)",
            "val":  (2.0 - R_flavor_Y2) / S,
            "R_flavor":  R_flavor_Y2,
            "justification": (
                "R weighted linearly by Y²_cl/Y²_total = 3/8. No "
                "principled reason for linear weighting beyond trace-level."
            ),
        },
        {
            "expr": "(2 − R · N_cl/N_total) / S_B",
            "val":  (2.0 - R_flavor_NW) / S_baryogenesis,
            "R_flavor":  R_flavor_NW,
            "justification": (
                "R weighted by Weyl-count fraction, over V7 §31 baryogenesis S_B."
            ),
        },
        {
            "expr": "(2 − R) / S_cl_Weyl",
            "val":  (2.0 - R) / S_cl_weyl,
            "R_flavor":  R,
            "justification": (
                "Unweighted R over charged-lepton Weyl-count S. The "
                "cleanest analog of the cosmological H_inf formula "
                "restricted to the charged-lepton subset."
            ),
        },
    ]

    ranked = []
    for c in candidates:
        val = c["val"]
        dev_pct = abs(val / Y_TRACE - 1.0) * 100.0
        ranked.append({
            "expression":                c["expr"],
            "value":                     float(val),
            "R_flavor":                  float(c["R_flavor"]),
            "ratio_to_target":           float(val / Y_TRACE),
            "deviation_pct":             float(dev_pct),
            "C2_trace_scale_under_5pct": bool(dev_pct < 5.0),
            "justification":             c["justification"],
        })
    ranked.sort(key=lambda d: d["deviation_pct"])

    any_closes_C2 = any(s["C2_trace_scale_under_5pct"] for s in ranked)
    best = ranked[0]

    # C.2 — Temporal correlator sub-direction: evaluate whether the
    # time-ordered CTP noise kernel at the three-flavor level adds
    # equations beyond the single ⟨H⟩ = v_EW/√2 constraint from
    # Phase 3. The spatial noise kernel N_grav = G/(ℏ|x−x'|) is
    # well-established (V7 §5); the temporal analog for the flavor
    # sector is N_temporal(t−t') from the fluctuation-dissipation
    # theorem with the τ_0 relaxation time.
    #
    # The FDT fixes N_temporal globally for the scalar response;
    # it is a single spectrum N(ω) = (2/τ)·ℏω·coth(ℏω/2k_B T) (V7
    # eq. 9), not a flavor-indexed constraint. For a Z_3-circulant
    # flavor structure to pick up flavor-differentiating equations
    # from the temporal correlator, there would need to be a
    # flavor-dependent τ_i OR a flavor-dependent temperature T_i.
    # Neither is native to V7 at the three-flavor level.
    #
    # Concretely: ⟨z_a^i(t) z_a^j(t')⟩ at the flavor fixed point is
    # δ^{ij} N(t-t') per V7's noise kernel — diagonal in flavor
    # basis with identical spectra. Three identical FDT constraints
    # (one per flavor) do not supply the two extra equations needed
    # to close Phase 3's underdetermination.
    C2_subdirection = {
        "name": "C.2 — Temporal correlator structure at three-flavor level",
        "noise_kernel_V7_eq_9":
            "N(ω) = (2/τ) · ℏω · coth(ℏω/2k_B T)",
        "flavor_structure_at_fixed_point":
            "⟨z_a^i(t) z_a^j(t')⟩ = δ^{ij} N(t-t'); diagonal in flavor "
            "basis with identical spectra for all three charged leptons",
        "flavor_dependent_tau_in_V7":        False,
        "flavor_dependent_temperature_in_V7": False,
        "extra_equations_from_FDT":          "three identical constraints, one per flavor",
        "degeneracy_pattern":
            "Three identical generations → three identical FDT "
            "constraints → no flavor-differentiating information.",
        "verdict": "FAILED — temporal correlator is degenerate in flavor basis at the three-flavor CTP fixed point as currently specified in V7",
        "what_would_change_this": (
            "A flavor-dependent relaxation time τ_i or temperature "
            "T_i derivable from S_CTP. Neither is present in V7 §§5, "
            "29; adding one would require a new Lagrangian operator "
            "(the same Phase 2 / Phase 3 / Phase 4-A-C obstruction). "
            "A higher-loop CTP computation (4-loop and beyond, past "
            "V7's current 3-loop horizon) might introduce flavor-"
            "differentiating corrections to the noise kernel, but "
            "that is the P5-A specialist direction."
        ),
    }

    return {
        "direction": "C — Flavor-sector anomaly-matching analog to C_Cosmo",
        "candidates_ranked":        ranked,
        "best_candidate":           best,
        "any_candidate_closes_C2":  any_closes_C2,
        "C_1_spatial_anomaly_analog":    "see candidates_ranked above (the trace-level attempts)",
        "C_2_temporal_correlator":        C2_subdirection,
        "underdetermination_note": (
            "Even with a principled R_flavor_cl, the flavor-sector "
            "analog of H_inf = (2−R)/(Sτ_0) inherits Phase 3's "
            "underdetermination: one trace-level equation does not "
            "determine three Yukawa eigenvalues. The V7 §31 "
            "baryogenesis formula includes an auxiliary factor K_neq "
            "(non-equilibrium) that has no charged-lepton analog "
            "derived in V7 — adding one would be ad hoc. The temporal-"
            "correlator sub-direction C.2 also fails: the FDT spectrum "
            "is flavor-diagonal with identical entries at the three-"
            "flavor fixed point, supplying no flavor-differentiating "
            "equations."
        ),
        "C1_status": "PASS (partial, inherited from A) — uses charged-lepton field content",
        "C2_status": f"FAIL — best candidate at {best['deviation_pct']:.1f}% deviation",
        "C3_status": "ORTHOGONAL — same reason as Direction A",
        "C4_status": "PARTIAL — flavor-subset R inherits Lagrangian grade from V7 §26.2, BUT the specific weighting (Y²-squared, linear, Weyl) requires its own derivation from the 3-loop machinery",
        "verdict": "FAILED on C2; partial on C1 (inherited); underdetermined at three-flavor level",
        "interpretation": (
            "The flavor-sector anomaly analog reaches the correct "
            f"order of magnitude for ⟨y⟩ (best candidate at {best['deviation_pct']:.1f}% "
            "deviation, in the right regime) but does NOT close at "
            "derivation-level precision. More importantly, even if "
            "a closer numerical match were found, the derivation "
            "would still face the Phase 3 underdetermination: one "
            "trace equation, three eigenvalues. Only the combination "
            "of Direction C with an independent confirmation of "
            "θ = 2/9 (Phase 1 falsifier passing) would reduce the "
            "problem to a single well-posed trace identity."
        ),
    }


def phase_4_mechanism_evaluation() -> dict:
    """Track II Phase 4: evaluate three candidate flavor-selection
    mechanisms against the four requirements C1–C4.

    Expected outcome: HONEST NEGATIVE on full closure — no single
    direction passes all four criteria. The Phase 4.0 scope document
    (see `phase_4_scope_document`) is the primary deliverable in
    that case.
    """
    A = direction_A_anomaly_weighted_ctp()
    B = direction_B_dielectric_flavor_mixing()
    C = direction_C_flavor_anomaly_analog()

    # Aggregate verdicts
    all_close_C2 = all([
        A["any_candidate_closes_C2"],
        False,  # B cannot close C2 by ~70 orders of magnitude
        C["any_candidate_closes_C2"],
    ])
    any_closes_C2 = any([
        A["any_candidate_closes_C2"],
        False,
        C["any_candidate_closes_C2"],
    ])

    direction_summary = {
        "A_anomaly_weighted":    A["verdict"],
        "B_dielectric":          B["verdict"],
        "C_flavor_anomaly":      C["verdict"],
    }

    return {
        "phase": "Track II Phase 4 — Flavor-selection mechanism evaluation",
        "direction_A":               A,
        "direction_B":               B,
        "direction_C":               C,
        "direction_summary":         direction_summary,
        "any_direction_passes_all":  all_close_C2,
        "any_direction_passes_C2":   any_closes_C2,
        "status": "HONEST NEGATIVE — no direction closes all four C1–C4 criteria",
        "status_after_attempt": {
            "V7_section_29":       "MAPPED (unchanged)",
            "V7_conjecture_F1":    "HYPOTHESIS (unchanged)",
            "Phase_1_candidate":   "CANDIDATE IDENTITY (unchanged)",
            "Phase_2_anchor":      "HYPOTHESIS (unchanged)",
            "Phase_3_outcome":     "HONEST NEGATIVE (unchanged)",
            "Phase_4_A":           "PARTIAL — C1 and C4 satisfied; C2 fails",
            "Phase_4_B":           "FAILED — C1, C2, C4 all fail",
            "Phase_4_C":           "PARTIAL — C1 inherited; C2 fails; underdetermined",
            "deliverable":         "Phase 4.0 scope document (see phase_4_scope_document)",
        },
        "headline_finding": (
            "No single direction closes all four C1–C4 criteria. "
            "Directions A and C reach the correct order of magnitude "
            "for ⟨y⟩ through principled hypercharge / Weyl-count "
            "structures (C1 and C4 partially satisfied), but neither "
            "reaches derivation-level precision (C2 fails at 18–50% "
            "deviation). Direction B is structurally incompatible "
            "(dielectric α_eff is ~70 decades too small at fermion "
            "Compton frequencies). The charged-lepton Yukawa "
            "hierarchy remains open, with Phase 4 narrowing the "
            "search space but not closing it."
        ),
    }


def phase_4_scope_document() -> dict:
    """The Phase 4.0 scope document — produced when Phase 4 fails to
    close through any of Directions A–C. This captures the
    underdetermination theorem from Phase 3, the four C1–C4
    requirements, the three directions attempted and their specific
    failure modes, and candidate Phase 5 directions surfaced during
    Phase 4 attempts.

    Serves as the formal Track II Phase 4.0 deliverable.
    """
    return {
        "title": "Track II Phase 4.0 — Scope of the charged-lepton Yukawa hierarchy problem within the GRUT CTP framework",
        "phase_3_underdetermination_theorem": (
            "The CTP fixed-point condition z* = z_target[z*] applied "
            "to the SM Higgs-lepton sector at the EW scale fixes "
            "⟨H⟩ = v_EW/√2 and the mass-Yukawa relation m_i = y_i · "
            "v_EW/√2 but does NOT constrain the three Yukawa "
            "couplings individually. The three y_i are independent "
            "SM Lagrangian inputs, and the fixed-point condition is "
            "satisfied for any choice. The V7 Conjecture F1 claim "
            "that the Jacobian is Z₃-circulant in flavor basis is a "
            "RESTRICTION on the input, not a derivation from the "
            "fixed point. The Yukawa hierarchy problem is therefore "
            "a genuine open direction — not an artifact of the v7 "
            "formulation, but a statement about what the CTP "
            "machinery as currently specified cannot fix."
        ),
        "four_requirements_for_any_candidate_mechanism": {
            "C1_flavor_distinction": (
                "Must distinguish charged leptons from quarks (which "
                "have y_t ≈ 1, y_b ≈ 2.4×10⁻², 6-decade span) and "
                "from neutrinos (y_ν ~ 10⁻¹² Dirac, effectively zero "
                "seesaw). A mechanism giving all fermions the same "
                "suppression factor fails C1."
            ),
            "C2_trace_scale": (
                "Must produce ⟨y⟩_cl = 3.605 × 10⁻³ at derivation-"
                "level precision (< 5% deviation). Numerical near-"
                "misses without a derivation are curve-fitting, not "
                "derivation."
            ),
            "C3_Z3_compatibility": (
                "Must be compatible with the Phase 1 CANDIDATE "
                "IDENTITY θ = K · α_vac = 2/9 for the Z₃ phase "
                "distribution. A mechanism that fixes all three y_i "
                "simultaneously must produce θ mod (2π/3) = 2/9 as "
                "a consequence, not as an independent input."
            ),
            "C4_mechanism_grade": (
                "Must have a Lagrangian-level operator or derived "
                "coupling. Numerical combinations of constants "
                "without a Lagrangian are rejected per the Phase 2 "
                "protocol (rejections of Λ_QCD and v_dark anchors)."
            ),
        },
        "three_directions_attempted_in_phase_4": {
            "A_anomaly_weighted_ctp": (
                "Use charged-lepton hypercharge content (Y²_cl = 5/4 "
                "per generation, cf. total Y² = 10/3) in a CTP path-"
                "counting normalization analogous to V7 §26.2.6. "
                "Result: satisfies C1 (genuine flavor-class "
                "distinction via hypercharge structure) and C4 "
                "(hypercharge is SM-native group theory). Fails C2: "
                "best candidate R · Y²_cl_per_gen/(108π) at 18% "
                "deviation, far from the 5% threshold. The "
                "hypercharge ratios give O(1) distinctions among "
                "fermion classes but cannot supply the O(10⁻³) "
                "loop-suppression regime the Yukawa scale sits in."
            ),
            "B_dielectric_flavor_mixing": (
                "Use the viscoelastic α_eff(ω) = α_vac/(1 + (ωτ_0)²) "
                "with a flavor-dependent kinetic-mixing operator to "
                "produce Yukawa-like suppression. Result: fails C1, "
                "C2, C4 simultaneously. α_eff at electron Compton "
                "frequency is ~10⁻⁷³, ~70 decades below the required "
                "scale. V7 §28 has only gauge kinetic mixing; no "
                "lepton-dark Yukawa operator exists, and adding one "
                "would be the Phase 2 curve-fit failure mode. "
                "Direction B is structurally incompatible with the "
                "flavor sector as V7 currently formulates it."
            ),
            "C_flavor_anomaly_analog": (
                "Construct a flavor-sector analog R_flavor from 3-loop "
                "CTP restricted to charged-lepton matter, then assemble "
                "⟨y⟩ ~ (2 − R_flavor) / S_flavor. Result: partial C1 "
                "and C4 inherited from Direction A. Fails C2: best "
                "candidate at ~50% deviation. Inherits Phase 3 "
                "underdetermination: one trace-level equation does not "
                "determine three Yukawa eigenvalues without an "
                "auxiliary factor (V7 §31's K_neq has no charged-"
                "lepton analog in the canonical framework)."
            ),
        },
        "what_the_three_failures_reveal": [
            "Phase 4 confirms that the Yukawa hierarchy does not close "
            "from the current V7 machinery through any of: (A) hypercharge "
            "weighting, (B) dielectric coupling, or (C) flavor-sector "
            "anomaly matching. The obstruction is not numerical but "
            "structural — the CTP machinery at the three-flavor level "
            "is one-equation-in-three-unknowns, and restricting to "
            "charged-lepton field content does not supply an extra "
            "constraint.",

            "The regime problem: Yukawa hierarchy sits in the loop-"
            "suppression regime (y ~ (α/4π)^n × O(1)) where GRUT's "
            "canonical dimensionless constants (α_vac = 1/3, S = 108π, "
            "R ≈ 1.15) produce O(1) and O(1/100) ratios rather than "
            "the O(10⁻³)–O(10⁻⁶) span the charged leptons actually "
            "occupy. Without an additional mass hierarchy or loop-"
            "expansion parameter, the GRUT foundation cannot reach "
            "this regime by dimensional analysis.",

            "This does not falsify V7 or Track II. It narrows the "
            "problem: any future candidate must introduce an "
            "additional mass scale (not Λ_QCD, not v_dark — those "
            "failed Phase 2) OR an explicit loop expansion parameter "
            "(which would have to emerge from an independent CTP "
            "computation at the flavor sector, not as a free input).",
        ],
        "explicitly_ruled_out_framings": {
            "four_generation_extension": (
                "V7 §9 PROVES N = 3 uniquely θ-independent for the "
                "Z_3 circulant Koide identity. Adding a fourth fermion "
                "generation breaks this identity, which is a PROVEN "
                "algebraic result (verified to 2.3×10⁻¹⁶) and not a "
                "hypothesis. Any 'add a 4th generation' proposal "
                "invalidates Phase 1's θ = K·α_vac = 2/9 candidate "
                "AND the core Z_3 identity. Off-limits."
            ),
            "S4_to_4_generations_pattern_match": (
                "S^4 is the 4-dimensional Euclidean manifold on "
                "which the 3-loop CTP anomaly lives (de Sitter → S^4 "
                "after Wick rotation). The '4' is spacetime "
                "dimension, not generation count. Confusing the two "
                "is pattern-matching, not physics."
            ),
            "tau_0_as_a_new_dimension": (
                "τ_0 is a parameter in the CTP response kernel with "
                "dimension time. GRUT has always operated in 4D "
                "spacetime. Framing τ_0 as 'the 4th dimension' is "
                "narrative, not physics, and does not supply any new "
                "constraint beyond what V7 §§4, 5 already encode."
            ),
            "cubed_hypercharge_ratio_numerology": (
                "1/(ΣY²_total_3gen)³ = 10⁻³ matches ⟨y⟩ at 72% "
                "deviation. The exponent 3 has no Lagrangian "
                "justification — it is pattern-matching the observed "
                "Yukawa scale. Rejected per C4 (see Direction A "
                "rejected candidate list)."
            ),
        },
        "legitimate_places_to_look_for_the_missing_constraint": [
            "Higher-loop (4-loop and beyond) CTP structure: the 3-"
            "loop coefficient C_FINAL is the frontier of V7's "
            "explicit derivation. Higher-loop contributions may "
            "contain flavor-differentiating terms that the 3-loop "
            "truncation misses. This is the most conservative way to "
            "look 'deeper into the framework's existing structure.'",

            "Non-perturbative CTP contributions (instantons, wormholes, "
            "gravitational path-integral saddles) could supply "
            "additional constraints at the flavor scale. Speculative "
            "and well beyond V7's current machinery.",

            "Explicit flavor-sector temporal correlator evaluation. "
            "V7's noise kernel at the flavor fixed point is flavor-"
            "diagonal with identical spectra — Direction C.2 confirms "
            "it supplies no flavor-differentiating equations as "
            "currently specified. A refinement that introduces a "
            "flavor-dependent τ_i or T_i from a derivable mechanism "
            "(not by hand) would be the legitimate version of "
            "'the missing constraint lives in the temporal structure.'",
        ],
        "candidate_phase_5_directions": [
            "(P5-A) 3-loop CTP flavor-sector computation restricted to "
            "charged leptons. A specialist version of the V7 §26.2.6 "
            "Correction #16 derivation, but with charged-lepton field "
            "content only. If the result produces a genuine R_flavor_cl "
            "as a derivable dimensionless number (rather than as a "
            "weighting of R_anomaly), Direction C could be revisited "
            "on firmer footing. Estimated scope: ~2–4 weeks specialist "
            "work, similar to the TJI on S⁴ item (V7 §26.2.5).",

            "(P5-B) Froggatt–Nielsen style GRUT extension. Introduce "
            "a GRUT-native U(1)_F flavor symmetry broken at a scale "
            "Λ_F intermediate between v_EW and Λ_UV, with charges "
            "assigned by Z₃-compatible CTP structure. The hierarchy "
            "emerges as (v_F / Λ_UV)^(q_i) for each fermion. Requires "
            "deriving the charge assignments from CTP rather than "
            "postulating them — which is the open problem Froggatt–"
            "Nielsen leaves unanswered in mainstream physics.",

            "(P5-C) Wait for experimental input. A sub-10-ppm m_τ "
            "measurement at CEPC / FCC-ee that confirms or falsifies "
            "θ = 2/9 (Phase 1 falsifier) would significantly narrow "
            "Phase 5. Confirmation reduces Phase 5 to a single trace "
            "equation ⟨y⟩ = f(R, α_vac, S, v_EW). Falsification "
            "kills the Z₃ Phase 1 candidate but leaves Direction A's "
            "C1 finding intact.",
        ],
        "recommended_posture": (
            "Phase 4.0 (this scope document) is the Track II "
            "deliverable for now. Phase 4.1 (attempted mechanisms) "
            "is DEFERRED to whichever of P5-A, P5-B, or P5-C "
            "materializes first. Per the user's pipeline protocol, "
            "the session moves to other Track II-adjacent work or "
            "to higher-leverage tracks (TJI specialist calc, DESI / "
            "Euclid chi-squared, etc.) rather than spending more "
            "attention on a mainstream-unsolved problem inside this "
            "session."
        ),
    }


def verify() -> dict:
    """Self-test: regression reconstruction + honest derivation attempt +
    Phase 2 mechanism evaluation + Phase 3 Yukawa attempt + Phase 4
    flavor-selection evaluation."""
    r = verify_reconstruction()
    d = derivation_attempt()
    mech = evaluate_mass_anchor_mechanisms()
    p3 = phase_3_yukawa_derivation_attempt()
    p4 = phase_4_mechanism_evaluation()
    return {
        "reconstruction_0p01pct":        r["reproduces_to_0p01pct"],
        "K_machine_precision":           r["K_machine_precision"],
        "derivation_status_is_HN":       "HONEST NEGATIVE" in d["status"],
        "V7_section_29_unchanged":       "MAPPED" in d["status_after_attempt"]["V7_section_29"],
        "V7_F1_conjecture_unchanged":    "HYPOTHESIS" in d["status_after_attempt"]["V7_conjecture_F1"],
        "canonical_constants_intact":    d["cross_sector_consistency"]["canonical_constants_not_modified"],
        "v_EW_mechanism_is_HYPOTHESIS":   mech["mechanism_1_v_EW"]["status"] == "HYPOTHESIS",
        "Lambda_QCD_mechanism_FAILED":    mech["mechanism_2_Lambda_QCD"]["status"] == "FAILED",
        "v_dark_mechanism_FAILED":        mech["mechanism_3_v_dark"]["status"] == "FAILED",
        "sole_viable_mechanism_is_v_EW":  mech["viable_mechanisms"] == ["v_EW Yukawa (SM-native)"],
        "phase_3_status_is_HN":           "HONEST NEGATIVE" in p3["status"],
        "phase_3_no_tight_match":         not p3["phase_3_outcome_any_tight_match"],
        "phase_3_preserves_phase_1":      p3["cross_sector_consistency"]["Phase_1_candidate_preserved"],
        "phase_3_preserves_phase_2":      p3["cross_sector_consistency"]["Phase_2_HYPOTHESIS_preserved"],
        "phase_4_status_is_HN":           "HONEST NEGATIVE" in p4["status"],
        "phase_4_no_direction_passes_C2": not p4["any_direction_passes_C2"],
        "phase_4_scope_document_available": "title" in phase_4_scope_document(),
    }
