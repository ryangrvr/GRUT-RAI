"""
Joint σ₈ / S₈ parameter refit for GRUT cosmological parameters.

Background
----------
The existing +3.1% σ₈ enhancement (Correction #36, three-solver consensus:
CAMB +3.22%, ODE +3.137%, CLASS +3.132%) was computed at fixed Planck 2018
parameters (H₀ = 67.4, Ω_m = 0.315). GRUT's first-principles cosmology predicts
(H₀ = 69.03, Ω_m = 0.290, Ω_Λ = 0.710). This module quantifies the full S₈
at GRUT's own parameters via three independent effects:

  (1) GRUT μ growth modification — computed exactly via the existing growth ODE.
      D_GRUT/D_ΛCDM at the σ₈ scales (k ~ 0.1–0.5 Mpc⁻¹) weighted by W²_TH.
      This gives the +3.1% enhancement (at Planck params) and a slightly
      different value at GRUT params.

  (2) Background effect of GRUT's Ω_m = 0.290 — computed via growth ODE.
      Lower Ω_m → more Λ-domination → reduced matter growth → lower σ₈.
      Computed as D_ΛCDM(Ω_m=0.290) / D_ΛCDM(Ω_m=0.315) at the ODE level.

  (3) Transfer function correction — estimated via BBKS approximation.
      Γ = Ω_m h changes: Γ_Planck = 0.212, Γ_GRUT = 0.200 (−5.7%).
      This shifts the small-scale suppression of P(k) and affects the
      σ₈ integral. Computed numerically by integrating T²(k) W²_TH(kR₈)
      dk over the σ₈ window at both parameter sets.
      NOTE: This is an approximation — the full computation requires
      a Boltzmann code (CAMB/CLASS). The BBKS estimate carries ±2–3% uncertainty.

  (4) Explicit S₈ = σ₈ × (Ω_m/0.3)^0.5 factor — exact from definition.

Key result
----------
GRUT's lower Ω_m (0.290 vs 0.311) moves S₈ significantly toward the weak-
lensing range. The GRUT μ enhancement (+3.1%) partially offsets the lower-Ω_m
suppression. Net S₈_GRUT is between Planck (0.832) and KiDS/DES (~0.76–0.78).
The dominant driver is GRUT's first-principles Ω_m = 0.290, not the μ modification.

S₈ observational context
-------------------------
Planck CMB:  S₈ = 0.832 ± 0.013   (Planck 2018 TT+TE+EE+lowE+lensing)
KiDS-1000:   S₈ = 0.759 ± 0.024   (Asgari+2021, cosmic shear)
DES-Y3:      S₈ = 0.776 ± 0.017   (Amon+2022, cosmic shear)
HSC-Y3:      S₈ = 0.775 ± 0.022   (Dalal+2023, cosmic shear)
ACT DR4:     S₈ = 0.840 ± 0.030   (Aiola+2020, CMB-consistent)

Module:  grut.derived.cosmology.sigma8_refit
Tests:   tests/derived/test_sigma8_refit.py
"""

from __future__ import annotations

import math
from typing import NamedTuple

import numpy as np


# ── Reference cosmological parameters ────────────────────────────────────────

# Planck 2018 TT+TE+EE+lowE+lensing
PLANCK_H0      = 67.36
PLANCK_OMEGA_M = 0.3153
PLANCK_OMEGA_L = 0.6847
PLANCK_H       = PLANCK_H0 / 100.0   # dimensionless h
PLANCK_N_S     = 0.9649
PLANCK_SIGMA8  = 0.8111               # Planck 2018 Table 2

# GRUT first-principles (from grut_H_0_prediction, n_eras=329)
GRUT_H0      = 69.029
GRUT_OMEGA_M = 0.2900
GRUT_OMEGA_L = 0.7100
GRUT_H       = GRUT_H0 / 100.0

# S₈ observational surveys
S8_SURVEYS = {
    "Planck_CMB":  {"S8": 0.832, "sigma": 0.013, "source": "Planck 2018"},
    "KiDS_1000":   {"S8": 0.759, "sigma": 0.024, "source": "Asgari+2021"},
    "DES_Y3":      {"S8": 0.776, "sigma": 0.017, "source": "Amon+2022"},
    "HSC_Y3":      {"S8": 0.775, "sigma": 0.022, "source": "Dalal+2023"},
    "ACT_DR4":     {"S8": 0.840, "sigma": 0.030, "source": "Aiola+2020"},
}

# σ₈ window scale: R₈ = 8 Mpc/h (radius of top-hat filter)
def _R8_Mpc(h: float) -> float:
    """R₈ = 8 Mpc/h in Mpc (for given h = H₀/100)."""
    return 8.0 / h


# ── BBKS transfer function ────────────────────────────────────────────────────

def bbks_T(k_mpc: float, Omega_m: float, h: float) -> float:
    """Bardeen–Bond–Kaiser–Szalay (1986) CDM transfer function.

    Arguments
    ---------
    k_mpc    : comoving wavenumber in Mpc⁻¹
    Omega_m  : matter density parameter
    h        : H₀/100 (dimensionless)

    Returns T(k) ∈ (0, 1].

    Approximation — no baryons, T_CMB = 2.725 K.
    Shape parameter Γ = Ω_m h² / h = Ω_m h (Peebles convention).
    q = k / (Ω_m h²)  with k in Mpc⁻¹ and result dimensionless
    (i.e., this is k / (Γ × h Mpc⁻¹) with Γ = Ω_m h).
    """
    Gamma = Omega_m * h            # shape parameter (dimensionless h factor)
    q     = k_mpc / (Omega_m * h * h)  # = k / (Γ h Mpc⁻¹) with k in Mpc⁻¹
    if q <= 0.0:
        return 1.0
    num  = math.log(1.0 + 2.34 * q) / (2.34 * q)
    poly = (1.0
            + 3.89  * q
            + (16.1 * q) ** 2
            + (5.46 * q) ** 3
            + (6.71 * q) ** 4)
    return num / poly ** 0.25


def _tophat_W(k_mpc: float, R_mpc: float) -> float:
    """Top-hat window function W_TH(kR) in 3D.

    W_TH(x) = 3 [sin(x) − x cos(x)] / x³
    """
    x = k_mpc * R_mpc
    if x < 1e-4:
        return 1.0 - x * x / 10.0  # Taylor expansion
    return 3.0 * (math.sin(x) - x * math.cos(x)) / x ** 3


def sigma8_bbks_integral(Omega_m: float, h: float,
                         n_s: float = PLANCK_N_S) -> float:
    """Compute the dimensionless σ₈ window integral via BBKS.

    Returns the quantity
      I = [∫ dk/k × Δ²_BBKS(k) × W²_TH(kR₈)]^{1/2}
    where Δ²_BBKS(k) ∝ k^{n_s} T²(k).

    The absolute normalization (A_s) is NOT included — this is only
    meaningful as a ratio I_GRUT / I_Planck to give the σ₈ transfer-
    function correction factor.
    """
    R8 = _R8_Mpc(h)
    # Integrate over k from k_min to k_max covering the σ₈ window
    k_min = 0.005   # Mpc⁻¹ — negligible window below this
    k_max = 2.0     # Mpc⁻¹ — window killed by W_TH above this
    n_pts = 1000
    k_arr = np.linspace(k_min, k_max, n_pts)
    dk    = k_arr[1] - k_arr[0]

    integrand = np.array([
        (k ** (n_s + 2.0))
        * bbks_T(k, Omega_m, h) ** 2
        * _tophat_W(k, R8) ** 2
        for k in k_arr
    ])
    # σ₈² ∝ ∫ dk k^{n_s+2} T²(k) W²(kR₈)
    # (from σ₈² = ∫ P(k) k² W² dk/(2π²), P(k) ∝ k^{n_s} T²)
    integral = np.trapezoid(integrand, k_arr)
    return math.sqrt(max(integral, 0.0))


def bbks_sigma8_ratio(
    Omega_m_A: float, h_A: float,
    Omega_m_B: float, h_B: float,
    n_s: float = PLANCK_N_S,
) -> float:
    """Ratio σ₈_A / σ₈_B from BBKS transfer function + window integral.

    Accounts for both the Γ = Ω_m h shape parameter change and the
    R₈ = 8/h window scale change. Does NOT include growth factor effects.
    """
    I_A = sigma8_bbks_integral(Omega_m_A, h_A, n_s)
    I_B = sigma8_bbks_integral(Omega_m_B, h_B, n_s)
    return I_A / I_B


# ── Growth factor via ODE ─────────────────────────────────────────────────────

# k grid for the growth factor window integral.
# Must span k ~ 0.01–0.5 Mpc⁻¹ where the σ₈ window has support.
# Coarser is faster; 12 log-spaced points captures the variation.
_K_GRID = np.geomspace(0.01, 0.50, 12)


def _D_at_k(k: float, Omega_m: float, OL: float,
             use_mu_GRUT: bool) -> float:
    """D(a=1, k) from the growth ODE at given parameters."""
    from grut.derivation.phi_munu.modified_growth import integrate_growth_factor
    _, delta = integrate_growth_factor(k, use_mu_GRUT,
                                       Omega_m=Omega_m, Omega_Lambda=OL)
    return float(delta[-1])


def growth_D_ratio(
    Omega_m_A: float, OL_A: float, use_mu_A: bool,
    Omega_m_B: float, OL_B: float, use_mu_B: bool,
    Omega_m_ref: float = PLANCK_OMEGA_M,
    h_ref: float = PLANCK_H,
    n_s: float = PLANCK_N_S,
) -> dict:
    """σ₈-window-weighted growth factor ratio D_A / D_B.

    Computes the effective growth ratio as seen by the σ₈ integral:

      R_D = sqrt( ∫ dk T²_ref(k) D²_A(k) W²_TH(kR₈) k^{n_s-1}
                / ∫ dk T²_ref(k) D²_B(k) W²_TH(kR₈) k^{n_s-1} )

    where T_ref is held at Planck BBKS (so the T change is accounted
    for separately in bbks_sigma8_ratio).

    The ODE is evaluated at _K_GRID (12 log-spaced points 0.01–0.5 Mpc⁻¹).
    """
    R8 = _R8_Mpc(h_ref)

    # Compute integrand weights  w(k) = T²_ref(k) W²_TH(kR₈) k^{n_s+2}
    # (σ₈² ∝ ∫ dk k^{n_s+2} T² W² D² from P(k) ∝ k^{n_s} T²)
    weights = np.array([
        bbks_T(k, Omega_m_ref, h_ref) ** 2
        * _tophat_W(k, R8) ** 2
        * k ** (n_s + 2.0)
        for k in _K_GRID
    ])

    # Growth factors at each k
    dA_vals = np.array([_D_at_k(k, Omega_m_A, OL_A, use_mu_A)
                        for k in _K_GRID])
    dB_vals = np.array([_D_at_k(k, Omega_m_B, OL_B, use_mu_B)
                        for k in _K_GRID])

    # Weighted σ₈ integrals ∝ sigma8²
    int_A = np.trapezoid(weights * dA_vals ** 2, _K_GRID)
    int_B = np.trapezoid(weights * dB_vals ** 2, _K_GRID)

    weighted_ratio = math.sqrt(int_A / int_B)

    per_k = {f"k_{k:.3f}": float(dA_vals[i] / dB_vals[i])
             for i, k in enumerate(_K_GRID)}

    return {
        "weighted_ratio": weighted_ratio,
        "per_k":          per_k,
        "n_k_points":     len(_K_GRID),
    }


# ── Main refit function ───────────────────────────────────────────────────────

def sigma8_refit_scenarios(sigma8_planck: float = PLANCK_SIGMA8) -> dict:
    """Compute σ₈ and S₈ for four cosmological scenarios.

    Scenarios
    ---------
    A: Planck ΛCDM                — reference (σ₈ = σ₈_Planck by definition)
    B: Planck params + GRUT μ     — growth modification only; confirms +3.1%
    C: GRUT params + ΛCDM growth  — background Ω_m effect only
    D: GRUT params + GRUT μ       — full joint refit

    For scenarios C and D the σ₈ estimate uses:
      σ₈ = σ₈_Planck × D_ratio(ODE) × T_ratio(BBKS)

    where:
      D_ratio = window-weighted growth factor ratio (exact for μ modification,
                approximate for background changes at the ODE level)
      T_ratio = BBKS σ₈ window integral ratio (approximate, ±2–3% uncertainty)

    The T_ratio is computed via the full σ₈ window integral (not a single-k
    estimate) to account for both the Γ shape change and the R₈ = 8/h window
    scale change.

    Returns
    -------
    dict with keys A, B, C, D each containing:
      sigma8         : σ₈ estimate
      S8             : S₈ = σ₈ × (Ω_m / 0.3)^0.5
      Omega_m        : matter density used
      D_ratio        : growth factor ratio vs Planck ΛCDM
      T_ratio        : BBKS transfer function ratio vs Planck ΛCDM
      S8_explicit_factor : √(Ω_m / 0.3)
      note           : uncertainty/caveat string
    """
    # ── Transfer function ratios (BBKS, approximate) ──────────────────────────
    T_planck_planck = 1.0                          # reference (= ratio of identical)
    T_grut_vs_planck = bbks_sigma8_ratio(
        GRUT_OMEGA_M, GRUT_H,
        PLANCK_OMEGA_M, PLANCK_H,
    )

    # ── Growth factor ratios (ODE, exact for μ; approximate for background) ───
    # Baseline denominator: Planck ΛCDM
    D_B = growth_D_ratio(PLANCK_OMEGA_M, PLANCK_OMEGA_L, True,
                         PLANCK_OMEGA_M, PLANCK_OMEGA_L, False)
    D_C = growth_D_ratio(GRUT_OMEGA_M, GRUT_OMEGA_L, False,
                         PLANCK_OMEGA_M, PLANCK_OMEGA_L, False)
    D_D = growth_D_ratio(GRUT_OMEGA_M, GRUT_OMEGA_L, True,
                         PLANCK_OMEGA_M, PLANCK_OMEGA_L, False)

    # ── σ₈ and S₈ ─────────────────────────────────────────────────────────────
    def _s8_factor(Om: float) -> float:
        return math.sqrt(Om / 0.3)

    def _make_entry(Om: float, D_rat: float, T_rat: float, note: str) -> dict:
        sig8 = sigma8_planck * D_rat * T_rat
        S8   = sig8 * _s8_factor(Om)
        return {
            "sigma8":           sig8,
            "S8":               S8,
            "Omega_m":          Om,
            "D_ratio":          D_rat,
            "T_ratio":          T_rat,
            "S8_explicit_factor": _s8_factor(Om),
            "note":             note,
        }

    scenario_A = {
        "sigma8":           sigma8_planck,
        "S8":               sigma8_planck * _s8_factor(PLANCK_OMEGA_M),
        "Omega_m":          PLANCK_OMEGA_M,
        "D_ratio":          1.0,
        "T_ratio":          1.0,
        "S8_explicit_factor": _s8_factor(PLANCK_OMEGA_M),
        "note": "Reference. σ₈ = Planck 2018 Table 2 (TT+TE+EE+lowE+lensing).",
    }

    scenario_B = _make_entry(
        PLANCK_OMEGA_M,
        D_B["weighted_ratio"],
        T_planck_planck,
        "Planck params + GRUT μ modification. D_ratio from ODE (exact for μ). "
        "T unchanged (same params). Should recover ~+3.1% on σ₈.",
    )

    scenario_C = _make_entry(
        GRUT_OMEGA_M,
        D_C["weighted_ratio"],
        T_grut_vs_planck,
        "GRUT params + ΛCDM growth (μ=1). D_ratio = background Ω_m change only. "
        "T_ratio from BBKS window integral (approximate, ±2–3%). "
        "S₈ factor = √(0.290/0.3) = 0.983.",
    )

    scenario_D = _make_entry(
        GRUT_OMEGA_M,
        D_D["weighted_ratio"],
        T_grut_vs_planck,
        "GRUT params + GRUT μ modification. Full joint refit. "
        "D_ratio = background + μ effects from ODE. T_ratio BBKS (approx). "
        "This is the primary GRUT S₈ prediction.",
    )

    return {
        "A_planck_lcdm":              scenario_A,
        "B_planck_params_grut_growth": scenario_B,
        "C_grut_params_lcdm_growth":  scenario_C,
        "D_grut_params_grut_growth":  scenario_D,
        "sigma8_planck_input":        sigma8_planck,
        "T_grut_vs_planck_bbks":      T_grut_vs_planck,
        "D_details": {
            "B_mu_only":    D_B,
            "C_bg_only":    D_C,
            "D_full":       D_D,
        },
        "caveat": (
            "T_ratio from BBKS (no baryons, T_CMB=2.725K) carries ±2–3% "
            "uncertainty. Full result requires CAMB/CLASS at GRUT params. "
            "D_ratio from growth ODE is exact for the μ modification; "
            "the background-only D change is also exact in the ODE framework. "
            "Transfer function and growth effects are treated independently "
            "(no cross-coupling between modified T and modified D)."
        ),
    }


# ── S₈ tension assessment ─────────────────────────────────────────────────────

def s8_tension_assessment(S8_value: float) -> dict:
    """Distance in σ from each observational S₈ measurement.

    Returns dict of survey_name → {delta_S8, tension_sigma, direction}.
    Positive tension_sigma means S8_value is above the survey central value.
    """
    result = {}
    for name, m in S8_SURVEYS.items():
        delta = S8_value - m["S8"]
        tension = delta / m["sigma"]
        result[name] = {
            "S8_survey":      m["S8"],
            "sigma_survey":   m["sigma"],
            "delta_S8":       delta,
            "tension_sigma":  tension,
            "direction":      "high" if delta > 0 else "low",
            "source":         m["source"],
        }
    return result


# ── Convenience entry point ───────────────────────────────────────────────────

def grut_s8_assessment() -> dict:
    """Full S₈ assessment for GRUT scenario D (full joint refit).

    Returns scenarios dict + tension assessment for scenario D.
    """
    scenarios = sigma8_refit_scenarios()
    D = scenarios["D_grut_params_grut_growth"]
    tension = s8_tension_assessment(D["S8"])
    return {
        "scenarios":       scenarios,
        "grut_S8":         D["S8"],
        "grut_sigma8":     D["sigma8"],
        "grut_D_ratio":    D["D_ratio"],
        "grut_T_ratio":    D["T_ratio"],
        "tension":         tension,
        "verdict": _verdict(D["S8"], tension),
    }


def _verdict(S8: float, tension: dict) -> str:
    """One-line plain-English verdict on S₈ tension."""
    t_planck = tension["Planck_CMB"]["tension_sigma"]
    t_kids   = tension["KiDS_1000"]["tension_sigma"]
    t_des    = tension["DES_Y3"]["tension_sigma"]
    return (
        f"GRUT S₈ = {S8:.3f}: "
        f"{abs(t_planck):.1f}σ {'below' if t_planck < 0 else 'above'} Planck, "
        f"{abs(t_kids):.1f}σ {'below' if t_kids < 0 else 'above'} KiDS-1000, "
        f"{abs(t_des):.1f}σ {'below' if t_des < 0 else 'above'} DES-Y3."
    )
