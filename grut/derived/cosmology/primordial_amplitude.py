"""GRUT — Primordial scalar amplitude A_s from CTP noise kernel.

Goal
----
Determine whether GRUT's framework can produce the observed primordial
scalar amplitude A_s ≈ 2.1 × 10⁻⁹ (Planck 2018) from its native
infrastructure — the CTP noise kernel, τ₀, α_vac, the screening factor
S, and (no) inflationary epoch — without introducing new parameters.

Closure of this gap would promote H₀'s detailed Friedmann route from
"one-parameter (N_total)" toward zero-parameter, AND give the Genesis
Hypothesis its first quantitative content. Failure narrows what
Genesis would need to provide.

Three computational paths
-------------------------

Path A — OU-process variance (linearized constitutive equation):
    The constitutive equation around z = 0 with KMS noise reduces to
    an Ornstein-Uhlenbeck process:
            τ₀ ḣ + h = ξ(t),  ⟨ξ(t)ξ(t')⟩ = N_T(t-t')
    The static variance ⟨h²⟩ is computable. We evaluate at T = T_peak
    (the τ₀-dual temperature where ℏ/τ₀ = k_B T_peak ≈ 5.78e-27 K — the
    NATURAL noise temperature for an OU process of relaxation time τ₀,
    NOT the 54.7 MK thermal-transition T_c) and at
    T = T_CMB (today's relevant background temperature for surviving
    modes). To make the variance dimensionless (matching A_s), we
    rescale by the Planck energy density (ρ_Pl × τ₀³ — the only
    natural dimensionless rescaling from GRUT scales + Planck constants).

Path B — Inflationary substitution:
    The standard inflationary formula
            A_s = H²_inf / (8 π² ε M²_Pl,red)
    is evaluated with GRUT's H_inf (the terminal velocity, not an
    inflationary H) and ε = (H_inf τ₀)² (the spectral_running.py
    convention for the dimensionless slow-roll analog). This is the
    "naive substitution" — answers what the standard formula gives
    when fed GRUT's late-time H_inf.

Path C — Natural dimensional ratios:
    Tabulates the GRUT framework's dimensionless number candidates
    that COULD have order ~10⁻⁹: α/S², α²/S², (H_inf τ₀)², (H_inf
    τ₀)⁴, (k_B T_c / E_Pl)^p for various p. Reports each with
    formula and value. Identifies the closest match (without forcing
    one).

Honesty protocol
----------------
- Each path returns its actual computed value vs A_s = 2.1×10⁻⁹.
- "Match" requires order-of-magnitude agreement (factor 10).
- If no path matches: register honest negative with the specific
  numerical results and the closure condition (Genesis becoming
  formal, OR an inflationary-epoch identification not currently
  in the framework).
- No ε-tuning. No A_s-fitting. Whatever falls out, falls out.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np

from grut.foundation.constants import (
    C as C_LIGHT,
    E_PLANCK,
    G,
    HBAR,
    K_B,
    M_PLANCK,
    T_PLANCK,
    L_PLANCK,
)
from grut.foundation.closure_protocol import (
    ALPHA_VAC,
    H_0_IMPLIED_KM_S_MPC,
    MPC_IN_M,
    R_REFRACTIVE,
    S_SCREENING,
    TAU_0_SEC,
    TAU_LAMBDA_SEC,
)
from grut.foundation.tau_hierarchy_decision import T_PEAK_NOISE_KERNEL_K


# ─────────────────────────────────────────────────────────────────────
# Reference observables
# ─────────────────────────────────────────────────────────────────────

A_S_PLANCK_2018: float = 2.1e-9
"""Observed primordial scalar amplitude at pivot k_* = 0.05 Mpc⁻¹.
Planck 2018 (arXiv:1807.06209)."""

T_CMB_K: float = 2.7255
"""CMB temperature today [K]."""

# Reduced Planck mass: M_Pl_red = M_Pl / sqrt(8π).
# M_Pl here is the standard Planck mass √(ℏc/G).
M_PLANCK_REDUCED: float = M_PLANCK / math.sqrt(8.0 * math.pi)

E_PLANCK_REDUCED: float = M_PLANCK_REDUCED * C_LIGHT**2

# H_inf_today = (2 - R)/(S × τ₀) — the framework's terminal velocity.
H_INF_HZ: float = (2.0 - R_REFRACTIVE) / (S_SCREENING * TAU_0_SEC)

# T_peak — the τ₀-dual temperature where k_B T = ℏ/τ₀ ("boiling point
# of gravity"), ≈5.78e-27 K. This is the natural KMS-noise temperature
# for the OU process below (whose relaxation time IS τ₀). It is NOT the
# 54.7 MK thermal-transition T_c (closure_protocol.T_C_KELVIN_CANONICAL,
# the τ_micro-dual). Single source of truth: tau_hierarchy_decision.
T_PEAK_KELVIN: float = T_PEAK_NOISE_KERNEL_K  # == HBAR / (TAU_0_SEC * K_B)


# ─────────────────────────────────────────────────────────────────────
# Path A — OU-process variance from KMS noise kernel
# ─────────────────────────────────────────────────────────────────────


def kms_noise_amplitude(omega_hz: float, tau_sec: float, T_kelvin: float) -> float:
    """KMS thermal noise spectrum N(ω) = (2/τ) × ℏω × coth(ℏω/(2k_BT))."""
    if tau_sec <= 0 or omega_hz <= 0:
        return 0.0
    if T_kelvin <= 0:
        # Pure quantum limit: coth → 1
        return (2.0 / tau_sec) * HBAR * omega_hz
    x = HBAR * omega_hz / (2.0 * K_B * T_kelvin)
    if x > 50:
        coth = 1.0
    elif x < 1e-10:
        coth = 1.0 / x  # classical-limit expansion
    else:
        coth = math.cosh(x) / math.sinh(x)
    return (2.0 / tau_sec) * HBAR * omega_hz * coth


def ou_variance_h_dimensional(
    T_kelvin: float,
    tau_sec: float = TAU_0_SEC,
    omega_uv_hz: float = 1.0 / T_PLANCK,
    omega_ir_hz: float | None = None,
) -> dict:
    """Stationary variance ⟨h²⟩ for the OU process τ₀ ḣ + h = ξ(t).

    ⟨h²⟩ = ∫ dω/(2π) × N_T(ω) / (1 + ω²τ²)

    The integrand at high T (classical) has the logarithmic UV
    divergence ∫ dω/(1+ω²τ²) which converges (∝ π/τ at the limit),
    but the quantum noise N(ω) → ℏω/τ at large ω introduces a
    logarithmic UV divergence ∫ ℏω/(τ × (1+ω²τ²)) dω ~ ln(ω_uv τ).
    We cut off at ω_uv = 1/t_Planck.

    Returns:
        variance_J_s : ⟨h²⟩ in dimensions of J·s (energy × time, the
                       natural unit for the integrated KMS spectrum)
        dimensionless_planck_normed : ⟨h²⟩ × ω_Pl² / (k_B T_Pl × τ_Pl)
                       (rescaling that produces a dimensionless number)
        formula_note : What the integral computes physically
    """
    if omega_ir_hz is None:
        omega_ir_hz = 1.0 / (1e6 * tau_sec)  # 6 decades below 1/τ

    n_pts = 4000
    omegas = np.logspace(
        math.log10(omega_ir_hz),
        math.log10(omega_uv_hz),
        n_pts,
    )

    integrand = np.array([
        kms_noise_amplitude(om, tau_sec, T_kelvin) / (1.0 + (om * tau_sec) ** 2)
        for om in omegas
    ])

    # Trapezoidal integration in log-space:
    #   ∫ f(ω) dω = ∫ f(ω) × ω × d(ln ω)
    integrand_log = integrand * omegas
    log_omegas = np.log(omegas)
    variance_J_s = float(np.trapezoid(integrand_log, log_omegas) / (2.0 * math.pi))

    # Dimensionless normalization. Variance has dimensions [energy × time]
    # in our convention. The natural Planck-scale rescaling is:
    #   ⟨h²⟩ / (E_Pl × t_Pl) = ⟨h²⟩ / ℏ
    # (since E_Pl × t_Pl = ℏ exactly).
    dimensionless_planck_normed = variance_J_s / HBAR

    return {
        "T_kelvin": T_kelvin,
        "tau_sec": tau_sec,
        "omega_uv_hz": omega_uv_hz,
        "omega_ir_hz": omega_ir_hz,
        "variance_J_s": variance_J_s,
        "dimensionless_planck_normed": dimensionless_planck_normed,
        "formula_note": (
            "⟨h²⟩ = ∫ dω/(2π) × (2/τ) ℏω coth(ℏω/(2k_BT)) / (1+ω²τ²); "
            "rescaled by ℏ to produce a dimensionless number."
        ),
    }


def path_a_ou_variance() -> dict:
    """Path A: stationary variance of OU process driven by KMS noise.

    Evaluated at T = T_peak (the τ₀-dual framework temperature, not the
    54.7 MK T_c) and at T = T_CMB (today). The 'at_T_c' result key is
    retained for API stability but holds the T_peak evaluation."""
    at_Tpeak = ou_variance_h_dimensional(T_kelvin=T_PEAK_KELVIN)
    at_TCMB = ou_variance_h_dimensional(T_kelvin=T_CMB_K)

    return {
        "name": "OU-process variance from KMS noise kernel",
        "at_T_c": at_Tpeak,
        "at_T_CMB": at_TCMB,
        "vs_A_s_at_Tc": at_Tpeak["dimensionless_planck_normed"] / A_S_PLANCK_2018,
        "vs_A_s_at_TCMB": at_TCMB["dimensionless_planck_normed"] / A_S_PLANCK_2018,
    }


# ─────────────────────────────────────────────────────────────────────
# Path B — Inflationary-formula substitution
# ─────────────────────────────────────────────────────────────────────

# From spectral_running.py: n_s = 1 - 2x²/(1+x²), x = Hτ. Solving for
# x at observed n_s = 0.9649:
N_S_OBSERVED: float = 0.9649
H_TAU_FROM_NS: float = math.sqrt(
    (1.0 - N_S_OBSERVED) / (2.0 - (1.0 - N_S_OBSERVED))
)


def path_b_inflationary_formula() -> dict:
    """Path B: standard inflationary formula with GRUT inputs.

    A_s = H²_inf / (8 π² ε M²_Pl,red)

    With:
        H_inf  = GRUT's terminal velocity (2-R)/(Sτ₀)  — late-time, not
                 inflationary
        ε       = (H_inf τ₀)² — spectral_running.py convention
        M_Pl,red = M_Pl / √(8π)
    """
    H_inf_per_sec = H_INF_HZ
    epsilon = (H_inf_per_sec * TAU_0_SEC) ** 2

    # H_inf in energy units = ℏ × ω = ℏ × H_inf
    E_H_inf_J = HBAR * H_inf_per_sec
    # E²_H_inf / E²_Pl_red gives the dimensionless squared ratio
    ratio_squared = (E_H_inf_J / E_PLANCK_REDUCED) ** 2

    A_s_path_b = ratio_squared / (8.0 * math.pi**2 * epsilon)

    # Also report epsilon-from-n_s variant (a different ε convention)
    eps_from_ns = H_TAU_FROM_NS**2
    A_s_path_b_eps_ns = ratio_squared / (8.0 * math.pi**2 * eps_from_ns)

    return {
        "name": "Inflationary-formula substitution",
        "H_inf_hz": H_inf_per_sec,
        "epsilon_HinfTau_squared": epsilon,
        "epsilon_from_ns_match": eps_from_ns,
        "ratio_E_Hinf_to_E_PlanckReduced_squared": ratio_squared,
        "A_s_path_b_eps_HinfTau": A_s_path_b,
        "A_s_path_b_eps_ns": A_s_path_b_eps_ns,
        "vs_A_s_path_b_eps_HinfTau": A_s_path_b / A_S_PLANCK_2018,
        "vs_A_s_path_b_eps_ns": A_s_path_b_eps_ns / A_S_PLANCK_2018,
        "formula_note": (
            "A_s = H²/(8π² ε M²_Pl,red). GRUT has no inflationary epoch — "
            "H_inf here is the LATE-TIME terminal velocity, ~10⁻⁵² of "
            "M_Pl. Standard inflation requires H ~ 10⁻⁵ M_Pl. The "
            "expected order of magnitude for this naive substitution "
            "is ~ (H_late/M_Pl)² / ε ~ 10⁻¹⁰⁴/0.018 ~ 10⁻¹⁰²."
        ),
    }


# ─────────────────────────────────────────────────────────────────────
# Path C — Natural dimensional ratios
# ─────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class DimensionalCandidate:
    name: str
    formula: str
    value: float

    @property
    def vs_A_s(self) -> float:
        return self.value / A_S_PLANCK_2018

    @property
    def log10_diff(self) -> float:
        if self.value <= 0:
            return float("-inf")
        return math.log10(self.value) - math.log10(A_S_PLANCK_2018)


def path_c_dimensional_ratios() -> dict:
    """Path C: natural GRUT dimensional ratios.

    Tabulates dimensionless candidates from GRUT's framework constants.
    None of these is 'derived' from the noise kernel directly; they
    are dimensional candidates the framework offers."""

    # Convenience: H_inf × τ₀ is the natural dimensionless cosmological
    # parameter; equals (2-R)/S = 0.845/108π ≈ 2.49e-3.
    H_inf_tau = H_INF_HZ * TAU_0_SEC

    # T_peak-related ratios (τ₀-dual temperature; candidate name kept as
    # "kT_c_over_E_Pl" for API stability — the formula ℏ/(τ₀ E_Pl) is
    # explicit, so no ambiguity with the 54.7 MK thermal-transition T_c).
    kT_c_over_E_Pl = K_B * T_PEAK_KELVIN / E_PLANCK
    tau_0_over_t_Pl = TAU_0_SEC / T_PLANCK

    candidates = [
        DimensionalCandidate(
            name="alpha_over_S_squared",
            formula="α / S²",
            value=ALPHA_VAC / S_SCREENING**2,
        ),
        DimensionalCandidate(
            name="alpha_squared_over_S_squared",
            formula="α² / S²",
            value=ALPHA_VAC**2 / S_SCREENING**2,
        ),
        DimensionalCandidate(
            name="alpha_over_S_cubed",
            formula="α / S³",
            value=ALPHA_VAC / S_SCREENING**3,
        ),
        DimensionalCandidate(
            name="H_inf_tau_squared",
            formula="(H_inf × τ₀)² = ((2-R)/S)²",
            value=H_inf_tau**2,
        ),
        DimensionalCandidate(
            name="H_inf_tau_fourth",
            formula="(H_inf × τ₀)⁴ = ((2-R)/S)⁴",
            value=H_inf_tau**4,
        ),
        DimensionalCandidate(
            name="alpha_times_H_inf_tau_squared",
            formula="α × (H_inf × τ₀)²",
            value=ALPHA_VAC * H_inf_tau**2,
        ),
        DimensionalCandidate(
            name="H_inf_tau_squared_over_S",
            formula="(H_inf × τ₀)² / S",
            value=H_inf_tau**2 / S_SCREENING,
        ),
        DimensionalCandidate(
            name="kT_c_over_E_Pl",
            formula="k_B T_c / E_Pl = ℏ/(τ₀ E_Pl) = t_Pl/τ₀",
            value=kT_c_over_E_Pl,
        ),
        DimensionalCandidate(
            name="kT_c_over_E_Pl_squared",
            formula="(k_B T_c / E_Pl)²",
            value=kT_c_over_E_Pl**2,
        ),
        DimensionalCandidate(
            name="t_Pl_over_tau_0",
            formula="t_Pl / τ₀",
            value=1.0 / tau_0_over_t_Pl,
        ),
        DimensionalCandidate(
            name="alpha_squared_times_H_inf_tau_squared",
            formula="α² × (H_inf × τ₀)²",
            value=ALPHA_VAC**2 * H_inf_tau**2,
        ),
    ]

    # Closest-match search (smallest |log10 ratio|)
    closest = min(candidates, key=lambda c: abs(c.log10_diff))

    return {
        "name": "Natural GRUT dimensional ratios",
        "candidates": [
            {
                "name": c.name,
                "formula": c.formula,
                "value": c.value,
                "vs_A_s": c.vs_A_s,
                "log10_diff_from_As": c.log10_diff,
            }
            for c in candidates
        ],
        "closest_match": {
            "name": closest.name,
            "formula": closest.formula,
            "value": closest.value,
            "vs_A_s": closest.vs_A_s,
            "log10_diff_from_As": closest.log10_diff,
        },
        "formula_note": (
            "Dimensional candidates from GRUT's framework constants. "
            "None is 'derived' from the noise kernel — they are "
            "natural ratios the framework offers. Closest match is "
            "reported but NOT promoted to a derivation."
        ),
    }


# ─────────────────────────────────────────────────────────────────────
# Master verdict
# ─────────────────────────────────────────────────────────────────────


def primordial_amplitude_attempt() -> dict:
    """Run all three paths and produce the honest verdict."""
    A = path_a_ou_variance()
    B = path_b_inflationary_formula()
    C = path_c_dimensional_ratios()

    # Check whether any path produces A_s within an order of magnitude
    def within_decade(value: float) -> bool:
        if value <= 0:
            return False
        return 0.1 <= (value / A_S_PLANCK_2018) <= 10.0

    # Distinguish DERIVATION-tier matches (Path A or Path B closing within
    # a decade) from DIMENSIONAL-COINCIDENCE matches (Path C — many
    # candidates tested, getting one within a decade is statistically
    # plausible).
    A_derivation_match = within_decade(A["at_T_CMB"]["dimensionless_planck_normed"])
    B_match_eps_HinfTau = within_decade(B["A_s_path_b_eps_HinfTau"])
    B_match_eps_ns = within_decade(B["A_s_path_b_eps_ns"])
    derivation_path_matches = (
        A_derivation_match or B_match_eps_HinfTau or B_match_eps_ns
    )

    # Path C dimensional candidates — count how many fall within a decade.
    C_within_decade = [
        c for c in C["candidates"] if within_decade(c["value"])
    ]

    if derivation_path_matches:
        # An actual physical-route derivation produced A_s. This would
        # be a real closure.
        verdict = "DERIVATION_MATCH"
        verdict_detail = (
            "A physical-route derivation (OU-process variance or "
            "inflationary-formula substitution) produced A_s within an "
            "order of magnitude. This warrants careful inspection — "
            "see per-path values."
        )
    elif C_within_decade:
        # No physical derivation closed, but a dimensional candidate
        # landed close. This is a CLUE, not a derivation.
        verdict = "HONEST_NEGATIVE_WITH_DIMENSIONAL_CLUE"
        clue_descriptions = "; ".join(
            f"{c['formula']} = {c['value']:.3e} (factor {c['vs_A_s']:.2f})"
            for c in C_within_decade
        )
        verdict_detail = (
            f"Path A (OU-process variance, ratio "
            f"{A['vs_A_s_at_TCMB']:.2e}) and Path B (inflationary "
            f"substitution, ratio {B['vs_A_s_path_b_eps_HinfTau']:.2e}) "
            f"both fail by 10+ orders of magnitude. The framework's "
            f"natural dimensional combinations include "
            f"{len(C_within_decade)} candidate(s) within a decade of "
            f"A_s = 2.1e-9: {clue_descriptions}. With "
            f"{len(C['candidates'])} dimensional candidates tested, "
            f"finding ~1 within a decade is statistically plausible "
            f"coincidence and is NOT a derivation. The closest "
            f"candidate is flagged as a CLUE worth physical motivation, "
            f"not promoted to closure."
        )
    else:
        verdict = "HONEST_NEGATIVE"
        verdict_detail = (
            "No path within an order of magnitude of A_s = 2.1e-9. "
            "GRUT's natural dimensional combinations and OU-process "
            "variance from the KMS noise kernel do not reproduce the "
            "observed primordial amplitude. Closure requires the "
            "framework to provide an inflationary epoch (currently "
            "absent) or a different identification of the primordial "
            "mode amplitude than the OU-process variance."
        )

    return {
        "A_s_observed": A_S_PLANCK_2018,
        "path_a_ou_variance": A,
        "path_b_inflationary_formula": B,
        "path_c_dimensional_ratios": C,
        "derivation_path_matches": derivation_path_matches,
        "dimensional_candidates_within_decade": C_within_decade,
        "verdict": verdict,
        "verdict_detail": verdict_detail,
        "closure_conditions": [
            "Genesis Hypothesis (Appendix A) becoming formal — derive an "
            "inflationary-like epoch with H ~ 10⁻⁵ M_Pl from the null "
            "fixed-point destabilization timescale",
            "OR identify a different primordial mode (not the OU-process "
            "variance of metric perturbations) whose amplitude maps to "
            "A_s with GRUT's existing scales",
            "OR document that A_s, like N_total, is observation-anchored "
            "input — not zero-parameter from current framework foundations",
        ],
        "discipline_note": (
            "No ε-tuning, no A_s-fitting. The numbers reported are what "
            "the framework's existing infrastructure produces under the "
            "specified physical interpretations."
        ),
    }


if __name__ == "__main__":
    import json
    result = primordial_amplitude_attempt()
    # Pretty-print, casting numpy/floats to standard
    def serializable(obj):
        if isinstance(obj, dict):
            return {k: serializable(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [serializable(x) for x in obj]
        if isinstance(obj, (np.floating, float)):
            return float(obj)
        return obj
    print(json.dumps(serializable(result), indent=2))
