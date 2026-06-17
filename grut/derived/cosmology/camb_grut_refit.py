"""Exact CAMB-backed σ₈ / S₈ refit at GRUT's first-principles parameters.

Replaces the BBKS ±2–3% transfer-function approximation in sigma8_refit.py
with a full CAMB 1.5.8 computation at (H₀=69.029, Ω_m=0.290, Ω_Λ=0.710).

Physical setup
--------------
Physical baryon density ωb = Ω_b h² is held fixed at the Planck BBN value
(0.02237) — constrained by BBN independent of H₀.  CDM density derived:
  ωc = Ω_m h² − ωb = 0.290 × 0.69029² − 0.02237 = 0.11582

Primordial spectrum (A_s, n_s) and τ held at Planck 2018 values so that
σ₈ *ratios* cancel the A_s normalization and isolate T(k) and D changes.

Normalization note
------------------
CAMB at the Planck 2018 nominal parameter means gives σ₈ ≈ 0.844, whereas
Planck's MCMC-marginalized measurement is σ₈ = 0.811.  The ~4% offset is a
known consequence of Jensen's inequality: the mean of σ₈ ≠ σ₈ at the mean
of (A_s, n_s, H₀, …).  All physically meaningful results in this module use
the CAMB *ratio* (σ₈_GRUT / σ₈_Planck), which cancels the normalization
offset, multiplied by the Planck reported reference to give normalized σ₈.

Four scenarios
--------------
  A: Planck ΛCDM (CAMB, reference — nominally 0.811 by construction)
  B: Planck params + GRUT μ post-processing (CAMB T, ODE D_ratio)
  C: GRUT background params, ΛCDM growth (CAMB exact T+D combined)
  D: GRUT background params + GRUT μ (CAMB T+D, ODE μ-ratio)

Key CAMB finding (vs BBKS approximation)
-----------------------------------------
The BBKS T_ratio = 0.974 (−2.6% on σ₈ from T) is wrong at σ₈ scales.
CAMB shows the combined T+D background ratio = 0.9816, almost identical
to the ODE-only growth ratio D_C = 0.9808.  This means T(k) at σ₈ scales
(k ≈ 0.1–0.5 Mpc⁻¹) is essentially unchanged (~−0.08%) when ωm shifts
from 0.14237 to 0.13819 — BBKS overestimates T-sensitivity at these scales
because it lacks baryons and uses an approximation outside its validity range.

Key results (CAMB-exact, normalized to Planck σ₈ = 0.8111)
-----------------------------------------------------------
  σ₈_A  =  0.811   S₈_A  =  0.832   (Planck reference)
  σ₈_B  =  0.833   S₈_B  =  0.854   (Planck params + GRUT μ, +2.7%)
  σ₈_C  ≈  0.796   S₈_C  ≈  0.783   (GRUT background, ΛCDM growth)
  σ₈_D  ≈  0.818   S₈_D  ≈  0.804   (GRUT full refit)

S₈ tensions (Scenario D):
  Planck CMB:  ~−2.1σ   KiDS-1000: ~+1.9σ
  DES-Y3:      ~+1.6σ   HSC-Y3:    ~+1.3σ

Module:  grut.derived.cosmology.camb_grut_refit
Tests:   tests/derived/test_camb_grut_refit.py
"""

from __future__ import annotations

import math
from typing import Any

import numpy as np
import camb

from grut.derived.cosmology.sigma8_refit import (
    PLANCK_H0,
    PLANCK_OMEGA_M,
    PLANCK_OMEGA_L,
    PLANCK_H,
    PLANCK_N_S,
    PLANCK_SIGMA8,
    GRUT_H0,
    GRUT_OMEGA_M,
    GRUT_OMEGA_L,
    GRUT_H,
    growth_D_ratio,
    s8_tension_assessment,
)


# ── CAMB physical parameters ──────────────────────────────────────────────────

# Planck 2018 TT+TE+EE+lowE+lensing best-fit (Table 2)
PLANCK_OMBH2: float = 0.02237     # Ω_b h² — BBN + Planck 2018
PLANCK_OMCH2: float = 0.1200      # Ω_c h² — Planck 2018 Table 2
PLANCK_TAU:   float = 0.0544      # reionization optical depth
PLANCK_AS:    float = 2.101e-9    # primordial scalar amplitude
PLANCK_MNU:   float = 0.06        # Σm_ν in eV (minimal normal hierarchy)

# GRUT first-principles: keep Planck BBN baryon density; derive ωc
GRUT_OMBH2: float = PLANCK_OMBH2                                   # BBN-fixed
GRUT_OMCH2: float = GRUT_OMEGA_M * GRUT_H ** 2 - GRUT_OMBH2       # = 0.11582

# Module-level caches for CAMB results (avoid repeated ~2 s runs in tests)
_CAMB_PLANCK: dict[str, Any] | None = None
_CAMB_GRUT:   dict[str, Any] | None = None
_MU_INFO: dict[str, float] | None = None


# ── CAMB runner ───────────────────────────────────────────────────────────────

def run_camb_matter_power(
    H0: float,
    ombh2: float,
    omch2: float,
    *,
    tau: float    = PLANCK_TAU,
    As: float     = PLANCK_AS,
    ns: float     = PLANCK_N_S,
    mnu: float    = PLANCK_MNU,
    kmin_h: float = 5e-5,
    kmax_h: float = 3.0,
    npoints: int  = 500,
) -> dict[str, Any]:
    """Run CAMB and return matter power spectrum + σ₈ at z=0.

    Parameters
    ----------
    H0       : Hubble constant in km/s/Mpc
    ombh2    : Ω_b h²  (physical baryon density)
    omch2    : Ω_c h²  (physical CDM density)
    tau      : optical depth to reionization
    As       : primordial scalar amplitude (at k_pivot = 0.05 Mpc⁻¹)
    ns       : spectral index
    mnu      : sum of neutrino masses in eV
    kmin_h   : minimum wavenumber in h/Mpc
    kmax_h   : maximum wavenumber in h/Mpc
    npoints  : number of output k points

    Returns
    -------
    dict with:
        k_Mpc      : ndarray, wavenumbers in Mpc⁻¹
        P_Mpc3     : ndarray, P(k, z=0) in Mpc³
        sigma8     : float, CAMB σ₈ at z=0  (uses nominal A_s normalisation)
        H0         : float, input H₀
        Omega_m    : float, (ωb + ωc) / h²  (cold matter; neutrinos separate)
        Omega_L    : float, 1 − Ω_m
        ombh2      : float
        omch2      : float
    """
    h = H0 / 100.0
    pars = camb.CAMBparams()
    pars.set_cosmology(
        H0=H0,
        ombh2=ombh2,
        omch2=omch2,
        tau=tau,
        mnu=mnu,
        neutrino_hierarchy="degenerate",
    )
    pars.InitPower.set_params(As=As, ns=ns, r=0)
    pars.set_matter_power(redshifts=[0.0], kmax=kmax_h * 1.1)

    results = camb.get_results(pars)
    kh, _, pk = results.get_matter_power_spectrum(
        minkh=kmin_h, maxkh=kmax_h, npoints=npoints
    )
    k_Mpc = kh * h
    P_Mpc3 = pk[0] / h ** 3
    sigma8 = float(results.get_sigma8_0())
    Omega_m = (ombh2 + omch2) / h ** 2

    return {
        "k_Mpc":   k_Mpc,
        "P_Mpc3":  P_Mpc3,
        "sigma8":  sigma8,
        "H0":      H0,
        "Omega_m": Omega_m,
        "Omega_L": 1.0 - Omega_m,
        "ombh2":   ombh2,
        "omch2":   omch2,
    }


# ── Cached CAMB calls ─────────────────────────────────────────────────────────

def planck_camb() -> dict[str, Any]:
    """CAMB at Planck 2018 parameters (cached after first call)."""
    global _CAMB_PLANCK
    if _CAMB_PLANCK is None:
        _CAMB_PLANCK = run_camb_matter_power(
            H0=PLANCK_H0, ombh2=PLANCK_OMBH2, omch2=PLANCK_OMCH2,
        )
    return _CAMB_PLANCK


def grut_background_camb() -> dict[str, Any]:
    """CAMB at GRUT first-principles background parameters (ΛCDM growth, no μ)."""
    global _CAMB_GRUT
    if _CAMB_GRUT is None:
        _CAMB_GRUT = run_camb_matter_power(
            H0=GRUT_H0, ombh2=GRUT_OMBH2, omch2=GRUT_OMCH2,
        )
    return _CAMB_GRUT


# ── μ growth enhancement ratio ────────────────────────────────────────────────

def grut_mu_ratios() -> dict[str, float]:
    """GRUT μ growth ratios from growth ODE (cached after first call).

    Returns
    -------
    dict with:
        mu_at_grut_bg   : D_D / D_C — μ enhancement at GRUT background (for Scenario D)
        mu_at_planck_bg : D_B / 1   — μ enhancement at Planck background (for Scenario B)
        D_D_vs_planck   : D_D weighted ratio (GRUT bg + μ) vs (Planck ΛCDM)
        D_C_vs_planck   : D_C weighted ratio (GRUT bg, ΛCDM) vs (Planck ΛCDM)
        D_B_vs_planck   : D_B weighted ratio (Planck bg + μ) vs (Planck ΛCDM)
    """
    global _MU_INFO
    if _MU_INFO is None:
        D_D = growth_D_ratio(
            GRUT_OMEGA_M, GRUT_OMEGA_L, True,
            PLANCK_OMEGA_M, PLANCK_OMEGA_L, False,
        )
        D_C = growth_D_ratio(
            GRUT_OMEGA_M, GRUT_OMEGA_L, False,
            PLANCK_OMEGA_M, PLANCK_OMEGA_L, False,
        )
        D_B = growth_D_ratio(
            PLANCK_OMEGA_M, PLANCK_OMEGA_L, True,
            PLANCK_OMEGA_M, PLANCK_OMEGA_L, False,
        )
        _MU_INFO = {
            "mu_at_grut_bg":   D_D["weighted_ratio"] / D_C["weighted_ratio"],
            "mu_at_planck_bg": D_B["weighted_ratio"],
            "D_D_vs_planck":   D_D["weighted_ratio"],
            "D_C_vs_planck":   D_C["weighted_ratio"],
            "D_B_vs_planck":   D_B["weighted_ratio"],
        }
    return _MU_INFO


# ── Core scenario computation ─────────────────────────────────────────────────

def camb_grut_sigma8_scenarios(
    sigma8_planck_ref: float = PLANCK_SIGMA8,
) -> dict[str, Any]:
    """Four-scenario σ₈ / S₈ refit using CAMB at GRUT background parameters.

    The key computation:
      1. Run CAMB at Planck params → raw σ₈_A_raw ≈ 0.844
      2. Run CAMB at GRUT params  → raw σ₈_C_raw ≈ 0.829
      3. TD_ratio = σ₈_C_raw / σ₈_A_raw  (A_s-cancelling ratio)
      4. σ₈_C_norm = sigma8_planck_ref × TD_ratio  (normalized to Planck measurement)
      5. Apply ODE μ-ratio for scenarios B and D

    CAMB finding: TD_ratio ≈ D_C_ODE to within 0.1%, confirming that
    T(k) at σ₈ scales is unchanged by the ωm shift — the BBKS T_ratio of
    0.974 was an overestimate.

    Parameters
    ----------
    sigma8_planck_ref : Planck reference σ₈ for normalisation (default: 0.8111)

    Returns
    -------
    dict with scenarios A–D, comparison vs BBKS, and tension assessment for D.
    """
    # ── CAMB raw runs ─────────────────────────────────────────────────────────
    pl = planck_camb()
    gr = grut_background_camb()

    s8_A_raw = pl["sigma8"]   # ≈ 0.844 (A_s normalization artefact)
    s8_C_raw = gr["sigma8"]   # ≈ 0.829

    # A_s-cancelling ratio — this is the physically meaningful number
    TD_ratio = s8_C_raw / s8_A_raw

    # Normalized σ₈ values (referenced to Planck's MCMC measurement)
    s8_A = sigma8_planck_ref
    s8_C = sigma8_planck_ref * TD_ratio

    # ── ODE μ enhancement ─────────────────────────────────────────────────────
    mu = grut_mu_ratios()
    mu_bg  = mu["mu_at_grut_bg"]    # ≈ 1.027  (D_D/D_C at GRUT background)
    mu_pl  = mu["mu_at_planck_bg"]  # ≈ 1.027  (D_B at Planck background)

    s8_B = s8_A * mu_pl             # Planck params + GRUT μ
    s8_D = s8_C * mu_bg             # GRUT params + GRUT μ  (full refit)

    # ── S₈ = σ₈ × (Ω_m / 0.3)^{1/2} ─────────────────────────────────────────
    def _s8(sig8: float, Om: float) -> float:
        return sig8 * math.sqrt(Om / 0.3)

    Om_A = PLANCK_OMEGA_M   # 0.3153 (sigma8_refit reference)
    Om_C = GRUT_OMEGA_M     # 0.290

    scenario_A = {
        "sigma8":     s8_A,
        "S8":         _s8(s8_A, Om_A),
        "Omega_m":    Om_A,
        "D_ratio":    1.0,
        "T_ratio":    1.0,
        "note": "Planck 2018 reference (normalized by construction).",
    }
    scenario_B = {
        "sigma8":     s8_B,
        "S8":         _s8(s8_B, Om_A),
        "Omega_m":    Om_A,
        "D_ratio":    mu_pl,
        "T_ratio":    1.0,
        "note": (
            "Planck params + GRUT μ. CAMB T (same params). ODE D_ratio."
            " Confirms +2.7% enhancement on σ₈."
        ),
    }
    scenario_C = {
        "sigma8":     s8_C,
        "S8":         _s8(s8_C, Om_C),
        "Omega_m":    Om_C,
        "TD_ratio_camb": TD_ratio,
        "D_ratio":    TD_ratio,   # T ≈ 1 confirmed (see module docstring)
        "T_ratio":    TD_ratio / mu["D_C_vs_planck"],   # residual T ≈ 1.001
        "note": (
            "GRUT background params, ΛCDM growth. CAMB exact combined T+D ratio. "
            "T(k) at σ₈ scales is unchanged (~−0.08%) — all effect is from D."
        ),
    }
    scenario_D = {
        "sigma8":     s8_D,
        "S8":         _s8(s8_D, Om_C),
        "Omega_m":    Om_C,
        "D_ratio":    s8_D / s8_A,
        "T_ratio":    None,
        "mu_enhancement_at_grut_bg": mu_bg,
        "note": (
            "GRUT params + GRUT μ — full joint refit. "
            "CAMB exact T+D for background, ODE μ-ratio for growth modification. "
            "Primary GRUT S₈ prediction (CAMB-exact)."
        ),
    }

    # ── Comparison vs BBKS ───────────────────────────────────────────────────
    from grut.derived.cosmology.sigma8_refit import sigma8_refit_scenarios
    bbks = sigma8_refit_scenarios(sigma8_planck=sigma8_planck_ref)
    bbks_C = bbks["C_grut_params_lcdm_growth"]["sigma8"]
    bbks_D = bbks["D_grut_params_grut_growth"]["sigma8"]
    T_ratio_bbks = bbks["T_grut_vs_planck_bbks"]
    D_C_ode = mu["D_C_vs_planck"]

    comparison_vs_bbks = {
        # Scenario C
        "sigma8_C_camb":              s8_C,
        "sigma8_C_bbks":              bbks_C,
        "sigma8_C_delta_abs":         s8_C - bbks_C,
        "sigma8_C_delta_pct":         (s8_C / bbks_C - 1.0) * 100,
        # Scenario D
        "sigma8_D_camb":              s8_D,
        "sigma8_D_bbks":              bbks_D,
        "sigma8_D_delta_abs":         s8_D - bbks_D,
        "sigma8_D_delta_pct":         (s8_D / bbks_D - 1.0) * 100,
        # Root cause: T vs D decomposition
        "TD_ratio_camb":              TD_ratio,
        "D_C_ode":                    D_C_ode,
        "T_residual_camb":            TD_ratio / D_C_ode,  # ≈ 1.001 → T negligible
        "T_ratio_bbks":               T_ratio_bbks,         # 0.974 (was wrong)
        "bbks_T_overestimate_pct": (T_ratio_bbks - (TD_ratio / D_C_ode)) / (TD_ratio / D_C_ode) * 100,
        "finding": (
            "T(k) at σ₈ scales is unchanged by the ωm shift GRUT→Planck. "
            "BBKS T_ratio = 0.974 (−2.6%) overestimates sensitivity. "
            "CAMB T-residual ≈ 1.001 (< 0.1% effect). "
            "The background σ₈ shift is almost entirely from growth factor D, "
            "consistent between CAMB and ODE."
        ),
    }

    # ── S₈ tension for Scenario D ─────────────────────────────────────────────
    tension_D = s8_tension_assessment(scenario_D["S8"])

    return {
        "A_planck_lcdm":               scenario_A,
        "B_planck_params_grut_growth":  scenario_B,
        "C_grut_params_lcdm_growth":    scenario_C,
        "D_grut_params_grut_growth":    scenario_D,
        "mu_ratios":                    mu,
        "comparison_vs_bbks":           comparison_vs_bbks,
        "tension_scenario_D":           tension_D,
        "camb_raw": {
            "sigma8_A_raw":  s8_A_raw,
            "sigma8_C_raw":  s8_C_raw,
            "TD_ratio_raw":  TD_ratio,
            "note": "Raw CAMB σ₈ values use A_s=2.101e-9 normalisation. "
                    "σ₈_A_raw ≈ 0.844 (vs Planck reported 0.811) reflects "
                    "Jensen inequality — MCMC marginal ≠ σ₈ at MCMC means. "
                    "Use normalized values for comparison with observations.",
        },
        "grut_sigma8":    s8_D,
        "grut_S8":        scenario_D["S8"],
        "sigma8_planck_ref": sigma8_planck_ref,
        "camb_version":   camb.__version__,
        "method": (
            "CAMB 1.5.8 matter P(k, z=0) at Planck + GRUT background params "
            "(same A_s, n_s, τ). σ₈ ratio cancels normalisation. "
            "μ growth enhancement from modified_growth.py ODE at GRUT background. "
            "Key finding: BBKS T_ratio overestimated; T change at σ₈ scales is < 0.1%."
        ),
    }


# ── Convenience entry point ───────────────────────────────────────────────────

def camb_grut_s8_assessment() -> dict[str, Any]:
    """Full S₈ assessment using CAMB-exact Scenario D.

    Returns scenarios + tension + verdict string.
    """
    sc = camb_grut_sigma8_scenarios()
    D = sc["D_grut_params_grut_growth"]
    tension = sc["tension_scenario_D"]

    t_planck = tension["Planck_CMB"]["tension_sigma"]
    t_kids   = tension["KiDS_1000"]["tension_sigma"]
    t_des    = tension["DES_Y3"]["tension_sigma"]
    verdict = (
        f"GRUT S₈ = {D['S8']:.3f} (CAMB-exact): "
        f"{abs(t_planck):.1f}σ {'below' if t_planck < 0 else 'above'} Planck, "
        f"{abs(t_kids):.1f}σ {'below' if t_kids < 0 else 'above'} KiDS-1000, "
        f"{abs(t_des):.1f}σ {'below' if t_des < 0 else 'above'} DES-Y3."
    )

    return {
        "scenarios":    sc,
        "grut_S8":      D["S8"],
        "grut_sigma8":  D["sigma8"],
        "tension":      tension,
        "verdict":      verdict,
        "camb_version": camb.__version__,
    }
