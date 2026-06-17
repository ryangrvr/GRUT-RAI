"""
S₈ tension assessment — GRUT vs weak gravitational lensing surveys.

S₈ = σ₈ × (Ω_m / 0.3)^0.5 is the combination of the amplitude and shape of
the matter power spectrum most tightly constrained by cosmic shear.  It is the
principal axis of the CMB–lensing tension: Planck CMB predicts S₈ ≈ 0.832,
while weak lensing (WL) surveys consistently find S₈ ≈ 0.75–0.78, a ~3σ
discrepancy.

GRUT modifies both ingredients:
  σ₈^GRUT  = 0.817  (slightly above Planck 0.811; CAMB Scenario D, Chapter 9)
  Ω_m^GRUT = 0.290  (below Planck 0.315; from first-principles Friedmann solution)

These partially cancel in S₈:
  S₈^GRUT   = 0.817 × (0.290/0.3)^0.5 = 0.803
  S₈^Planck = 0.811 × (0.315/0.3)^0.5 = 0.831

GRUT's lower Ω_m reduces S₈ by 3.4% relative to Planck, bringing it ~60%
of the way from Planck towards the WL measurements.

Key results (locked from direct computation):
  GRUT  S₈ = 0.803    RMS tension vs 4 WL surveys = 1.535σ   χ²/N = 2.356
  Planck S₈ = 0.831   RMS tension vs 4 WL surveys = 2.741σ   χ²/N = 7.511
  Tension reduction: GRUT is 1.79× less discrepant with WL than Planck.
  GRUT does not fully resolve the S₈ tension (all four WL values remain below
  GRUT's 0.803), but the discrepancy is reduced from ~3σ to ~1.5σ.

Dataset: 4 cosmic-shear measurements from KiDS, HSC-SSP, and DES Y3.

References (dataset):
  Hildebrandt+2017 — MNRAS 465, 1454  (KiDS-450)
  Asgari+2021      — A&A 645, A104    (KiDS-1000)
  Dalal+2023       — A&A 679, A96     (HSC-SSP Year 3)
  Abbott+2022      — PRD 105, 023520  (DES Year 3, 3×2pt)

Reference (Planck CMB baseline):
  Planck Collaboration 2020 — A&A 641, A6, Table 2  (TT+TE+EE+lowE)
"""

from __future__ import annotations

import math
from typing import NamedTuple

# ── Cosmological parameters ───────────────────────────────────────────────────

GRUT_SIGMA8    = 0.817     # σ₈(z=0) — CAMB Scenario D (full GRUT cosmology)
GRUT_OMEGA_M   = 0.290     # Ω_m — GRUT first-principles Friedmann solution

PLANCK_SIGMA8  = 0.811     # σ₈(z=0) — Planck 2018 TT+TE+EE+lowE
PLANCK_OMEGA_M = 0.3153    # Ω_m — Planck 2018

# Planck CMB S₈ reported directly in Planck 2018 Table 2
PLANCK_S8_CMB       = 0.832    # S₈ = σ₈ √(Ω_m/0.3) from Planck CMB
PLANCK_S8_CMB_SIGMA = 0.013    # 1σ uncertainty

S8_OMEGA_REF = 0.3    # reference Ω_m for S₈ definition

# ── WL dataset ────────────────────────────────────────────────────────────────


class S8Point(NamedTuple):
    """One published S₈ = σ₈(Ω_m/0.3)^0.5 measurement."""
    s8:        float   # measured value
    sigma:     float   # 1σ uncertainty
    survey:    str     # survey name
    reference: str     # citation


# 4-point cosmic shear compilation, sorted ascending by S₈
WL_DATA: tuple[S8Point, ...] = (
    S8Point(0.745, 0.039, "KiDS-450",   "Hildebrandt+2017"),
    S8Point(0.766, 0.020, "KiDS-1000",  "Asgari+2021"),
    S8Point(0.769, 0.032, "HSC-SSP Y3", "Dalal+2023"),
    S8Point(0.776, 0.017, "DES Y3",     "Abbott+2022"),
)

N_WL_POINTS = len(WL_DATA)  # 4

# ── Module-level cache ────────────────────────────────────────────────────────

_COMPARISON_CACHE: dict | None = None


# ── S₈ formula ────────────────────────────────────────────────────────────────


def compute_s8(sigma8: float, omega_m: float) -> float:
    """S₈ = σ₈ × (Ω_m / 0.3)^0.5."""
    return sigma8 * math.sqrt(omega_m / S8_OMEGA_REF)


def grut_s8() -> float:
    """GRUT predicted S₈ = 0.817 × (0.290/0.3)^0.5 = 0.803."""
    return compute_s8(GRUT_SIGMA8, GRUT_OMEGA_M)


def planck_s8_lss() -> float:
    """Planck LSS-derived S₈ = 0.811 × (0.3153/0.3)^0.5 = 0.831."""
    return compute_s8(PLANCK_SIGMA8, PLANCK_OMEGA_M)


# ── Full tension comparison ───────────────────────────────────────────────────


def s8_tension_comparison() -> dict:
    """GRUT vs Planck S₈ tension against 4 WL surveys.

    Returns a dict with keys:
      grut_s8              : GRUT predicted S₈
      planck_s8_lss        : Planck S₈ derived from σ₈ and Ω_m
      planck_s8_cmb        : Planck S₈ from Table 2 (direct)
      planck_s8_cmb_sigma  : 1σ uncertainty on Planck Table 2 S₈
      n_wl_points          : number of WL measurements
      wl_s8                : array of WL S₈ values
      wl_sigma             : array of 1σ uncertainties
      tensions_grut        : (S₈^GRUT − S₈_obs) / σ for each WL survey
      tensions_planck      : (S₈^Planck − S₈_obs) / σ for each WL survey
      chi2_N_grut          : χ²/N over WL surveys for GRUT
      chi2_N_planck        : χ²/N over WL surveys for Planck
      rms_grut             : RMS tension (σ units) for GRUT
      rms_planck           : RMS tension (σ units) for Planck
      tension_reduction    : rms_planck / rms_grut — factor by which GRUT
                             is less discrepant with WL surveys than Planck
      note                 : interpretive summary string
    """
    global _COMPARISON_CACHE
    if _COMPARISON_CACHE is not None:
        return _COMPARISON_CACHE

    s8_g = grut_s8()
    s8_p = planck_s8_lss()

    wl_s8    = [pt.s8    for pt in WL_DATA]
    wl_sigma = [pt.sigma for pt in WL_DATA]

    tensions_g = [(s8_g - obs) / sig for obs, sig in zip(wl_s8, wl_sigma)]
    tensions_p = [(s8_p - obs) / sig for obs, sig in zip(wl_s8, wl_sigma)]

    n = N_WL_POINTS
    chi2_N_g = sum(t**2 for t in tensions_g) / n
    chi2_N_p = sum(t**2 for t in tensions_p) / n
    rms_g    = math.sqrt(chi2_N_g)
    rms_p    = math.sqrt(chi2_N_p)
    reduction = rms_p / rms_g

    _COMPARISON_CACHE = {
        "grut_s8":             s8_g,
        "planck_s8_lss":       s8_p,
        "planck_s8_cmb":       PLANCK_S8_CMB,
        "planck_s8_cmb_sigma": PLANCK_S8_CMB_SIGMA,
        "n_wl_points":         n,
        "wl_s8":               wl_s8,
        "wl_sigma":            wl_sigma,
        "tensions_grut":       tensions_g,
        "tensions_planck":     tensions_p,
        "chi2_N_grut":         chi2_N_g,
        "chi2_N_planck":       chi2_N_p,
        "rms_grut":            rms_g,
        "rms_planck":          rms_p,
        "tension_reduction":   reduction,
        "note": (
            f"GRUT S₈ = {s8_g:.3f} vs Planck S₈ = {s8_p:.3f}. "
            f"GRUT RMS tension vs 4 WL surveys = {rms_g:.3f}σ (χ²/N = {chi2_N_g:.3f}). "
            f"Planck RMS tension = {rms_p:.3f}σ (χ²/N = {chi2_N_p:.3f}). "
            f"Tension reduction factor GRUT/Planck = {reduction:.2f}×. "
            "GRUT's lower Ω_m = 0.290 reduces S₈ by 3.4% vs Planck, partially "
            "resolving the S₈ tension (~1.5σ vs ~2.7σ). "
            "GRUT still overpredicts S₈ relative to all 4 WL surveys; the tension "
            "is reduced but not eliminated."
        ),
    }
    return _COMPARISON_CACHE
