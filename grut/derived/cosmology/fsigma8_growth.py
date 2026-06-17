"""
fσ₈(z) growth-rate comparison — GRUT vs published RSD observations.

The combined quantity fσ₈(z) = f(z) × σ₈(z) is the primary observable from
redshift-space distortions (RSD).  It is calibration-independent: f = dln D/dln a
is the logarithmic growth rate and σ₈(z) = σ₈(0) × D(z)/D(0) normalises the
amplitude.  The product fσ₈ is extracted from the ratio of the monopole and
quadrupole of the galaxy power spectrum, independent of galaxy bias.

GRUT modifies the Poisson equation by a factor μ_GRUT(k, a) = 1 + α_vac/[1 +
(τ₀ k_phys)²], α_vac = 1/3.  This enhances the gravitational coupling — and
hence the growth rate — on scales where τ₀ k_phys ≲ 1.

Scale dependence (at a = 1):
  k = 0.01 Mpc⁻¹: μ_eff ≈ 1.328  (near large-scale limit 4/3)
  k = 0.05 Mpc⁻¹: μ_eff ≈ 1.236  (representative RSD scale)
  k = 0.10 Mpc⁻¹: μ_eff ≈ 1.126  (small-scale suppression)
  k → 0            μ_eff → 4/3     (theoretical maximum)

The critical scale τ₀ c ≈ 12.85 Mpc, corresponding to k₀ ≈ 0.078 Mpc⁻¹.
Growth is enhanced for k ≪ k₀ and approaches GR for k ≫ k₀.

Key results (locked from ODE integration):
  GRUT fσ₈ (k=0.05 Mpc⁻¹, 13 RSD points):  χ²/N = 0.763,  RMS = 0.874σ
  Planck ΛCDM                             :  χ²/N = 0.422,  RMS = 0.650σ
  Both consistent with data; GRUT slightly high at z ~ 0.4–0.7 (~1σ)
  Large-scale limit (k→0): χ²/N = 2.10 — disfavoured by current RSD

Dataset: 13 published fσ₈ measurements, z = 0.02–1.40, from 6dFGRS, SDSS
(MGS, BOSS DR12), WiggleZ, VIPERS, and FastSound surveys.

References (dataset):
  Hudson & Turnbull 2012 — ApJL 751, L30 (2MRS peculiar velocity)
  Beutler+2012 — MNRAS 423, 3430 (6dFGRS)
  Howlett+2015 — MNRAS 449, 848 (SDSS MGS)
  Blake+2011   — MNRAS 415, 2876 (WiggleZ)
  Alam+2017    — MNRAS 470, 2617 (BOSS DR12 consensus)
  Blake+2012   — MNRAS 425, 405 (WiggleZ)
  de la Torre+2013 — A&A 557, A54 (VIPERS)
  Okumura+2016 — PASJ 68, 38 (FastSound)
"""

from __future__ import annotations

from typing import NamedTuple

import numpy as np

# ── Cosmological parameters ───────────────────────────────────────────────────

GRUT_OMEGA_M   = 0.290     # Ω_m — GRUT first-principles (Scenario D background)
GRUT_OMEGA_L   = 0.710     # Ω_Λ
GRUT_SIGMA8    = 0.817     # σ₈(z=0) — CAMB Scenario D (grut/derived/camb_grut_refit.py)
GRUT_K_RSD     = 0.05      # representative RSD scale, Mpc⁻¹ (μ_eff ≈ 1.24 at z=0)

PLANCK_OMEGA_M = 0.3153    # Ω_m — Planck 2018 TT+TE+EE+lowE
PLANCK_OMEGA_L = 0.6847    # Ω_Λ
PLANCK_SIGMA8  = 0.811     # σ₈(z=0) — Planck 2018

# ── RSD dataset ───────────────────────────────────────────────────────────────


class FsigmaPoint(NamedTuple):
    """One published fσ₈ measurement."""
    z_eff:    float   # effective redshift
    fsigma8:  float   # fσ₈ measured value
    sigma:    float   # 1σ statistical uncertainty
    reference: str   # citation


RSD_DATA: tuple[FsigmaPoint, ...] = (
    # ── Low-z peculiar velocity ───────────────────────────────────────
    FsigmaPoint(0.02,  0.428, 0.0465, "Hudson & Turnbull 2012"),  # 2MRS pv
    # ── 6dFGRS ───────────────────────────────────────────────────────
    FsigmaPoint(0.067, 0.423, 0.055,  "Beutler+2012"),
    # ── SDSS MGS ─────────────────────────────────────────────────────
    FsigmaPoint(0.15,  0.490, 0.145,  "Howlett+2015"),
    # ── WiggleZ ──────────────────────────────────────────────────────
    FsigmaPoint(0.22,  0.42,  0.07,   "Blake+2011"),
    # ── BOSS DR12 (3 consensus bins) ─────────────────────────────────
    FsigmaPoint(0.38,  0.497, 0.045,  "Alam+2017"),
    # ── WiggleZ ──────────────────────────────────────────────────────
    FsigmaPoint(0.41,  0.45,  0.04,   "Blake+2011"),
    FsigmaPoint(0.44,  0.413, 0.080,  "Blake+2012"),
    # ── BOSS DR12 ────────────────────────────────────────────────────
    FsigmaPoint(0.51,  0.458, 0.038,  "Alam+2017"),
    # ── WiggleZ ──────────────────────────────────────────────────────
    FsigmaPoint(0.60,  0.390, 0.063,  "Blake+2012"),
    # ── BOSS DR12 ────────────────────────────────────────────────────
    FsigmaPoint(0.61,  0.436, 0.034,  "Alam+2017"),
    # ── WiggleZ ──────────────────────────────────────────────────────
    FsigmaPoint(0.73,  0.437, 0.072,  "Blake+2012"),
    # ── VIPERS ───────────────────────────────────────────────────────
    FsigmaPoint(0.80,  0.47,  0.08,   "de la Torre+2013"),
    # ── FastSound ────────────────────────────────────────────────────
    FsigmaPoint(1.40,  0.482, 0.116,  "Okumura+2016"),
)

N_RSD_POINTS = len(RSD_DATA)  # 13

# ── Module-level cache ────────────────────────────────────────────────────────

_COMPARISON_CACHE: dict | None = None


# ── Growth ODE solver ─────────────────────────────────────────────────────────


def _solve_growth_fsigma8(
    omega_m: float,
    omega_lambda: float,
    use_mu_grut: bool,
    k_mpc: float,
    z_arr: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """Solve modified linear growth ODE; return f(z) and D_norm(z) on z_arr.

    Uses the same ODE as grut.derivation.phi_munu.modified_growth but exposes
    the derivative component (needed for f = d ln D / d ln a).

    Parameters
    ----------
    omega_m, omega_lambda : background cosmology
    use_mu_grut : if True use GRUT μ(k, a); if False GR (μ = 1)
    k_mpc : comoving wavenumber in Mpc⁻¹ at which to evaluate μ_GRUT
    z_arr : 1-D array of redshifts

    Returns
    -------
    f_arr     : growth rate f = d ln D / d ln a at each z
    D_norm    : D(z) / D(0), growth factor normalised to z = 0
    """
    from scipy.integrate import solve_ivp
    from grut.derivation.phi_munu.modified_growth import (
        _growth_rhs, TAU_0_SEC, ALPHA_VAC,
    )

    N_init  = np.log(1e-4)   # a_init = 0.0001 (deep matter era)
    N_final = 0.0             # a = 1, z = 0

    sol = solve_ivp(
        _growth_rhs,
        (N_init, N_final),
        y0=np.array([1.0, 1.0]),          # growing-mode IC: δ=1, dδ/dN=1
        method="RK45",
        dense_output=True,
        rtol=1e-9,
        atol=1e-12,
        args=(k_mpc, omega_m, omega_lambda, TAU_0_SEC, ALPHA_VAC, use_mu_grut),
    )

    if not sol.success:
        raise RuntimeError(f"Growth ODE integration failed: {sol.message}")

    # Growth factor normalization at z=0
    delta_0 = float(sol.sol(0.0)[0])

    # Evaluate ODE state at each requested redshift
    N_eval   = np.log(1.0 / (1.0 + np.asarray(z_arr, dtype=float)))
    states   = sol.sol(N_eval)      # shape (2, len(z_arr))
    delta    = states[0]             # δ(N)
    ddelta   = states[1]             # dδ/dN  =  f × δ

    # f(z) = d ln δ / d ln a = d ln δ / dN  =  dδ/dN / δ
    f_arr  = ddelta / delta
    D_norm = delta / delta_0         # D(z)/D(0), normalised

    return f_arr, D_norm


# ── Public prediction functions ───────────────────────────────────────────────


def grut_fsigma8(z_arr) -> np.ndarray:
    """GRUT predicted fσ₈(z) at representative RSD scale k = 0.05 Mpc⁻¹.

    Computes: fσ₈(z) = f_GRUT(z) × σ₈^GRUT × D_GRUT(z)/D_GRUT(0)

    where
      σ₈^GRUT = 0.817  — from CAMB Scenario D (full k-integrated computation)
      f_GRUT, D_norm   — from ODE with μ_GRUT(k=0.05, a) and GRUT background
    """
    z = np.atleast_1d(np.asarray(z_arr, dtype=float))
    f, D_norm = _solve_growth_fsigma8(
        GRUT_OMEGA_M, GRUT_OMEGA_L, True, GRUT_K_RSD, z,
    )
    return f * GRUT_SIGMA8 * D_norm


def lcdm_fsigma8(z_arr) -> np.ndarray:
    """Planck ΛCDM predicted fσ₈(z).

    Computes: fσ₈(z) = f_ΛCDM(z) × σ₈^Planck × D_ΛCDM(z)/D_ΛCDM(0)
    """
    z = np.atleast_1d(np.asarray(z_arr, dtype=float))
    f, D_norm = _solve_growth_fsigma8(
        PLANCK_OMEGA_M, PLANCK_OMEGA_L, False, GRUT_K_RSD, z,
    )
    return f * PLANCK_SIGMA8 * D_norm


def grut_fsigma8_large_scale(z_arr) -> np.ndarray:
    """GRUT fσ₈(z) in the large-scale limit (k = 0.01 Mpc⁻¹, μ → 4/3).

    Upper bound on GRUT growth enhancement; corresponds to k → 0 theoretical
    maximum (μ_eff ≈ 1.328 at z=0).  Current RSD data disfavours this limit
    (χ²/N ≈ 2.10); future large-scale surveys can test it directly.
    """
    z = np.atleast_1d(np.asarray(z_arr, dtype=float))
    f, D_norm = _solve_growth_fsigma8(
        GRUT_OMEGA_M, GRUT_OMEGA_L, True, 0.01, z,
    )
    return f * GRUT_SIGMA8 * D_norm


# ── Full comparison ───────────────────────────────────────────────────────────


def fsigma8_comparison() -> dict:
    """Compute GRUT vs RSD fσ₈ comparison statistics.

    Returns a dict with keys:
      n_points          : number of RSD measurements
      grut_fsigma8      : GRUT predicted fσ₈ at each z (k=0.05 Mpc⁻¹)
      lcdm_fsigma8      : Planck ΛCDM predicted fσ₈ at each z
      z_arr             : redshift array
      obs_fsigma8       : observed fσ₈ values
      obs_sigma         : 1σ uncertainties
      residuals_grut    : (pred − obs) / σ for GRUT
      residuals_lcdm    : (pred − obs) / σ for Planck
      chi2_N_grut       : χ²/N for GRUT
      chi2_N_lcdm       : χ²/N for Planck ΛCDM
      rms_grut          : RMS residual (σ units) for GRUT
      rms_lcdm          : RMS residual (σ units) for Planck
      k_rsd_mpc         : representative RSD scale used (Mpc⁻¹)
      grut_sigma8       : σ₈^GRUT used
      planck_sigma8     : σ₈^Planck used
      note              : interpretive summary
    """
    global _COMPARISON_CACHE
    if _COMPARISON_CACHE is not None:
        return _COMPARISON_CACHE

    z_arr     = np.array([p.z_eff   for p in RSD_DATA])
    obs_fs8   = np.array([p.fsigma8 for p in RSD_DATA])
    obs_sigma = np.array([p.sigma   for p in RSD_DATA])

    grut_pred = grut_fsigma8(z_arr)
    lcdm_pred = lcdm_fsigma8(z_arr)

    res_grut = (grut_pred - obs_fs8) / obs_sigma
    res_lcdm = (lcdm_pred - obs_fs8) / obs_sigma

    chi2_N_grut = float(np.sum(res_grut**2) / N_RSD_POINTS)
    chi2_N_lcdm = float(np.sum(res_lcdm**2) / N_RSD_POINTS)
    rms_grut    = float(np.sqrt(np.mean(res_grut**2)))
    rms_lcdm    = float(np.sqrt(np.mean(res_lcdm**2)))

    _COMPARISON_CACHE = {
        "n_points":       N_RSD_POINTS,
        "z_arr":          z_arr,
        "obs_fsigma8":    obs_fs8,
        "obs_sigma":      obs_sigma,
        "grut_fsigma8":   grut_pred,
        "lcdm_fsigma8":   lcdm_pred,
        "residuals_grut": res_grut,
        "residuals_lcdm": res_lcdm,
        "chi2_N_grut":    chi2_N_grut,
        "chi2_N_lcdm":    chi2_N_lcdm,
        "rms_grut":       rms_grut,
        "rms_lcdm":       rms_lcdm,
        "k_rsd_mpc":      GRUT_K_RSD,
        "grut_sigma8":    GRUT_SIGMA8,
        "planck_sigma8":  PLANCK_SIGMA8,
        "note": (
            f"GRUT fσ₈ computed at k={GRUT_K_RSD} Mpc⁻¹ (μ_eff ≈ 1.24 at z=0). "
            f"χ²/N = {chi2_N_grut:.3f} (GRUT) vs {chi2_N_lcdm:.3f} (Planck ΛCDM). "
            "Both consistent with data (χ²/N < 1). GRUT lies ~5% above Planck "
            "at z ~ 0.4–0.7, consistent within 1–2σ per point. "
            "Large-scale limit (k→0, μ→4/3) gives χ²/N ≈ 2.1 — disfavoured. "
            "Scale-dependent μ_GRUT self-limits the growth enhancement at RSD scales."
        ),
    }
    return _COMPARISON_CACHE
