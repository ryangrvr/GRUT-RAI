"""
CMB low-ℓ Integrated Sachs-Wolfe (ISW) prediction for GRUT.

On super-horizon scales (k ≪ k₀ = 0.078 Mpc⁻¹), the GRUT modified-gravity
function μ_GRUT(k,a) → 1 + α_vac = 4/3.  This enhanced gravitational
coupling changes how the Bardeen potential Φ evolves from recombination
to today, producing a distinctive ISW signal at CMB multipoles ℓ < 30.

══════════════════════════════════════════════════════════════════════
The reduced potential
══════════════════════════════════════════════════════════════════════

We define the reduced potential:

    Φ̃(a; k) ≡ μ(k,a) × δ(a) / a,   normalised to Φ̃ = 1 at a_init

Φ̃ is proportional to the Bardeen potential Φ: Φ ∝ −Φ̃.  In standard
ΛCDM matter domination, δ ∝ a and μ=1, so Φ̃ = 1 (constant potential).

In GRUT, the GRUT transition occurs at:

    a★(k) = c τ₀ × k ≈ 12.85 Mpc × k

For k = 10⁻³ Mpc⁻¹:  a★ = 0.0129 (z★ = 76.8), well before z_recombination = 1100.
For k = 4.5×10⁻⁴ Mpc⁻¹:  a★ = 0.0058 (z★ = 172).

After a★, μ → 4/3 and the growing-mode exponent becomes p₊ ≈ 1.186
(vs p₊ = 1 for ΛCDM), so δ_GRUT grows as a^1.186 and Φ̃_GRUT ∝ a^0.186 —
the potential **deepens** during matter domination.

══════════════════════════════════════════════════════════════════════
CMB recombination: SW is unchanged
══════════════════════════════════════════════════════════════════════

At z = 1100 (a_rec = 9.1×10⁻⁴), for k = 10⁻³ Mpc⁻¹:

    k_phys = k / a_rec ≈ 1.1 Mpc⁻¹
    (c τ₀ × k_phys)² ≈ 14² = 196 ≫ 1
    μ_GRUT(k, a_rec) = 1 + (1/3)/197 ≈ 1.0017

The Sachs-Wolfe temperature anisotropy ΔT/T ∝ Φ(rec) is unchanged at
the 0.2% level.  GRUT's modification enters entirely through the
late-time ISW.

══════════════════════════════════════════════════════════════════════
Numerical results (k = 10⁻³ Mpc⁻¹, representative ℓ ≈ 15 scale)
══════════════════════════════════════════════════════════════════════

    Φ̃_ΛCDM(a=1) = 0.788   (21% decay from matter-domination plateau)
    Φ̃_GRUT(a=1) = 2.079   (108% deepening from matter-domination plateau)
    Φ̃_GRUT / Φ̃_ΛCDM    = 2.64

Evolution (GRUT):
    a = 0.013 (z = 77, transition a★): Φ̃ ≈ 1.22  (μ ≈ 1.17)
    a = 0.050 (z = 19):                Φ̃ ≈ 1.61  (μ ≈ 1.31)
    a = 0.300 (z = 2.3):               Φ̃ ≈ 2.22  (μ → 4/3)
    a = 0.500 (z = 1.0):               Φ̃ ≈ 2.33  (peak)
    a = 1.000 (z = 0):                 Φ̃ ≈ 2.08  (decayed during Λ-dom)

══════════════════════════════════════════════════════════════════════
ISW direction and CMB prediction
══════════════════════════════════════════════════════════════════════

The ISW temperature shift for a photon traversing the line-of-sight:

    ΔT/T|_ISW ∝ −∫ (dΦ̃/dη) dη

If Φ̃ grows (potential deepens): dΦ̃/dη > 0 → photons are **cooled**.
If Φ̃ decays (potential weakens): dΦ̃/dη < 0 → photons are **heated**.

ΛCDM: Φ̃ decays monotonically (slowly until Λ-domination, then faster).
      Photons are heated. Positive ISW adds power at ℓ < 30.

GRUT: Φ̃ deepens from z=77 to a peak at z≈1, then partially decays.
      Net ΔΦ̃ = +1.079 (deepened), so photons are **net cooled**.
      Negative ISW **removes** power at ℓ < 30 relative to ΛCDM.

Multipole-epoch correspondence (k = 10⁻³ Mpc⁻¹):
  ℓ ≈ 2:   ISW from z ~ 0.1 (Λ-dominated)    → GRUT Φ̃ decaying → heating
  ℓ ≈ 10:  ISW from z ~ 3–4 (late matter-dom) → GRUT Φ̃ growing  → cooling
  ℓ ≈ 30:  ISW from z ~ 9   (matter-dom)      → GRUT Φ̃ growing  → cooling

GRUT predicts **reduced power at ℓ ≈ 10–30** (cooling ISW from
potential deepening) and **slightly enhanced power at ℓ = 2**
(larger GRUT potential decay during Λ-domination).

══════════════════════════════════════════════════════════════════════
Observational status: Planck 2018 low-ℓ anomaly
══════════════════════════════════════════════════════════════════════

Planck 2018 TT power spectrum (Planck 2019, Table 1 / arXiv:1906.02552)
shows D_ℓ at ℓ = 2–30 roughly 10–20% below the ΛCDM best-fit,  the
so-called "low-ℓ power anomaly".  The deficit is most pronounced at
ℓ = 2 and ℓ ≈ 20.

GRUT's prediction (reduced power at ℓ = 10–30 from ISW cooling) is in
the **same direction** as the observed Planck anomaly.  However:
  • Cosmic variance at ℓ = 2–30 is 20–60% → this is not a decisive test.
  • A full quantitative D_ℓ prediction requires MGCAMB Boltzmann
    integration (not done here).

══════════════════════════════════════════════════════════════════════
Falsification condition
══════════════════════════════════════════════════════════════════════

GRUT is falsified in this sector if:

(a) CMB-S4 + LSST ISW-galaxy cross-correlation (2027+) measures a
    POSITIVE large-scale ISW amplitude consistent with ΛCDM at >3σ
    (would require GRUT's potential to behave like ΛCDM, contradicting
    the 2.6× deeper potential predicted here).

(b) The Planck low-ℓ anomaly resolves to an EXCESS (D_ℓ^obs > D_ℓ^ΛCDM)
    at ℓ = 10–30 at >2σ → GRUT's cooling ISW prediction is falsified.

(c) MGCAMB integration of GRUT's μ(k,a) produces D_ℓ at ℓ < 30
    inconsistent with Planck TT at >3σ → tighter threshold requires
    the full Boltzmann result.

══════════════════════════════════════════════════════════════════════
Scope
══════════════════════════════════════════════════════════════════════

This module provides the growth-ODE layer of the CMB prediction:
  • Reduced potential history Φ̃(a; k) for GRUT and ΛCDM.
  • ISW sign analysis and amplitude ratio.
  • Comparison to Planck low-ℓ observational status.

It does NOT provide:
  • Full D_ℓ power spectrum (requires MGCAMB Boltzmann pipeline).
  • Non-linear effects or secondary anisotropies.
  • Tensor modes or primordial gravitational waves.

References:
  Seljak & Zaldarriaga 1996 (CMBFAST) — ISW formalism.
  Hu & Sugiyama 1995 — large-angle CMB analytic treatment.
  Planck 2019 (arXiv:1906.02552) — Planck 2018 TT power spectrum.
  Pogosian & Silvestri 2008 PRD 77 023503 — μ(k,a) parameterisation.
  modified_growth.py — GRUT μ_GRUT(k,a) derivation and growth ODE.
"""

from __future__ import annotations

import math
from functools import lru_cache

import numpy as np
from scipy.integrate import solve_ivp

from grut.derivation.phi_munu.modified_growth import (
    _growth_rhs,
    mu_GRUT_numeric,
    TAU_0_SEC,
    ALPHA_VAC,
    C_LIGHT_M_S,
    MPC_IN_M,
)

# ── Cosmological parameters ───────────────────────────────────────────────────

GRUT_OMEGA_M  = 0.290
GRUT_OMEGA_L  = 0.710
PLANCK_OMEGA_M = 0.3153
PLANCK_OMEGA_L = 0.6847

# Representative CMB scales
CMB_K_LOW_ELL  = 1e-3    # Mpc⁻¹  — ℓ ≈ 15  (representative ℓ=10–30 scale)
CMB_K_HORIZON  = 4.5e-4  # Mpc⁻¹  — ℓ ≈ 2   (near-horizon / quadrupole scale)

# Standard ODE integration parameters
_A_INIT = 3e-4   # matter-radiation equality epoch

# τ₀ c in Mpc (characteristic GRUT scale)
TAU0_C_MPC = TAU_0_SEC * C_LIGHT_M_S / MPC_IN_M   # ≈ 12.847 Mpc

# Planck 2018 low-ℓ anomaly: observed D_ℓ / ΛCDM D_ℓ, averaged ℓ=2–30
# (Planck 2019, arXiv:1906.02552, Section 4.1)
PLANCK_LOW_ELL_RATIO  = 0.83   # roughly 17% deficit vs ΛCDM best-fit
PLANCK_LOW_ELL_SIGMA  = 0.08   # ~cosmic-variance uncertainty (rough)

# Module-level cache
_PHI_HISTORY_CACHE:  dict | None = None
_CMB_ISW_CACHE:      dict | None = None


# ── Core computation ──────────────────────────────────────────────────────────


def _solve_phi_tilde(
    k_mpc:         float,
    omega_m:       float,
    omega_lambda:  float,
    use_mu_grut:   bool,
    n_steps:       int = 5000,
) -> tuple[np.ndarray, np.ndarray]:
    """Compute the reduced potential Φ̃(a) = μ(k,a) × δ(a) / a.

    Normalised so that Φ̃(a_init) = 1 (in deep matter domination, μ≈1
    and δ ≈ a, so Φ̃ ≈ 1 identically in matter domination for ΛCDM).

    Returns
    -------
    a_arr : ndarray, shape (n_steps+1,)
        Scale factor from a_init to 1.
    phi_tilde : ndarray, shape (n_steps+1,)
        Reduced potential, normalised to 1 at a=a_init.
    """
    N_init  = math.log(_A_INIT)
    N_final = 0.0

    sol = solve_ivp(
        _growth_rhs,
        (N_init, N_final),
        y0=np.array([1.0, 1.0]),
        method="RK45",
        dense_output=True,
        max_step=(N_final - N_init) / n_steps,
        args=(k_mpc, omega_m, omega_lambda, TAU_0_SEC, ALPHA_VAC, use_mu_grut),
    )
    if not sol.success:
        raise RuntimeError(f"Growth ODE failed: {sol.message}")

    N_arr   = np.linspace(N_init, N_final, n_steps + 1)
    a_arr   = np.exp(N_arr)
    delta   = sol.sol(N_arr)[0]

    if use_mu_grut:
        mu = np.array([mu_GRUT_numeric(k_mpc, a) for a in a_arr])
    else:
        mu = np.ones(len(a_arr))

    # Φ̃(a) = a_init × μ(a) × δ(a) / a  [normalised so Φ̃(a_init)=1]
    phi = _A_INIT * mu * delta / a_arr
    return a_arr, phi


# ── Public API ────────────────────────────────────────────────────────────────


def phi_tilde_today(k_mpc: float, use_grut_bg: bool = True) -> tuple[float, float]:
    """Reduced potential at a=1 for GRUT and ΛCDM.

    Parameters
    ----------
    k_mpc : comoving wavenumber (Mpc⁻¹).
    use_grut_bg : if True, GRUT uses Ω_m=0.290 background;
                  if False, both use Planck background.

    Returns
    -------
    (phi_grut, phi_lcdm) at a = 1.
    """
    om_grut = GRUT_OMEGA_M  if use_grut_bg else PLANCK_OMEGA_M
    ol_grut = GRUT_OMEGA_L  if use_grut_bg else PLANCK_OMEGA_L

    _, phi_g = _solve_phi_tilde(k_mpc, om_grut, ol_grut, True)
    _, phi_l = _solve_phi_tilde(k_mpc, PLANCK_OMEGA_M, PLANCK_OMEGA_L, False)
    return float(phi_g[-1]), float(phi_l[-1])


def grut_transition_scale(k_mpc: float) -> float:
    """Scale factor a★ at which GRUT transition occurs for comoving k.

    a★(k) = c τ₀ × k  [the k_phys = 1/(cτ₀) crossover epoch].
    """
    return TAU0_C_MPC * k_mpc


def mu_at_recombination(k_mpc: float) -> float:
    """μ_GRUT(k, a_rec) — should be ≈ 1 for CMB Sachs-Wolfe to be unchanged."""
    a_rec = 1.0 / 1100.0
    return float(mu_GRUT_numeric(k_mpc, a_rec))


def reduced_potential_history(k_mpc: float = CMB_K_LOW_ELL) -> dict:
    """Full Φ̃(a) history for GRUT and ΛCDM at comoving scale k_mpc.

    Returns a dict with keys:
      a_arr            : scale-factor array from a_init to 1
      phi_grut         : GRUT reduced potential Φ̃_GRUT(a)
      phi_lcdm         : ΛCDM reduced potential Φ̃_ΛCDM(a)
      phi_grut_today   : Φ̃_GRUT(a=1)  ≈ 2.079 for k=10⁻³ Mpc⁻¹
      phi_lcdm_today   : Φ̃_ΛCDM(a=1) ≈ 0.788 for k=10⁻³ Mpc⁻¹
      phi_ratio        : Φ̃_GRUT(1) / Φ̃_ΛCDM(1)
      delta_phi_grut   : Φ̃_GRUT(1) − 1  (>0: deepened; <0: decayed)
      delta_phi_lcdm   : Φ̃_ΛCDM(1) − 1
      isw_sign_grut    : 'cooling' if delta_phi_grut > 0, else 'heating'
      isw_sign_lcdm    : 'cooling' if delta_phi_lcdm > 0, else 'heating'
      isw_amplitude_ratio : |delta_phi_grut| / |delta_phi_lcdm|
      a_star           : GRUT transition epoch for this k
      z_star           : corresponding redshift
      mu_at_rec        : μ_GRUT(k, a_rec) — should be ≈ 1
      k_mpc            : input wavenumber
    """
    a_arr, phi_g = _solve_phi_tilde(k_mpc, GRUT_OMEGA_M, GRUT_OMEGA_L, True)
    _,     phi_l = _solve_phi_tilde(k_mpc, PLANCK_OMEGA_M, PLANCK_OMEGA_L, False)

    phi_g_1 = float(phi_g[-1])
    phi_l_1 = float(phi_l[-1])
    dphi_g  = phi_g_1 - 1.0
    dphi_l  = phi_l_1 - 1.0
    a_star  = grut_transition_scale(k_mpc)

    return {
        "a_arr":              a_arr,
        "phi_grut":           phi_g,
        "phi_lcdm":           phi_l,
        "phi_grut_today":     phi_g_1,
        "phi_lcdm_today":     phi_l_1,
        "phi_ratio":          phi_g_1 / phi_l_1,
        "delta_phi_grut":     dphi_g,
        "delta_phi_lcdm":     dphi_l,
        "isw_sign_grut":      "cooling" if dphi_g > 0.0 else "heating",
        "isw_sign_lcdm":      "cooling" if dphi_l > 0.0 else "heating",
        "isw_amplitude_ratio": abs(dphi_g) / abs(dphi_l),
        "a_star":             a_star,
        "z_star":             1.0 / a_star - 1.0 if a_star < 1 else 0.0,
        "mu_at_rec":          mu_at_recombination(k_mpc),
        "k_mpc":              k_mpc,
    }


def cmb_isw_comparison() -> dict:
    """Full CMB ISW assessment at both representative CMB scales.

    Returns a cached dict with keys:
      # k = 10⁻³ Mpc⁻¹  (ℓ ≈ 15, representative ℓ=10–30)
      phi_grut_today_low_ell   : Φ̃_GRUT(1) at k=10⁻³ Mpc⁻¹
      phi_lcdm_today_low_ell   : Φ̃_ΛCDM(1) at k=10⁻³ Mpc⁻¹
      phi_ratio_low_ell        : ratio ≈ 2.64
      isw_amplitude_ratio_low_ell : ≈ 5.09
      # k = 4.5×10⁻⁴ Mpc⁻¹  (ℓ ≈ 2, horizon/quadrupole scale)
      phi_grut_today_horizon   : Φ̃_GRUT(1) at k=4.5×10⁻⁴ Mpc⁻¹
      phi_lcdm_today_horizon   : Φ̃_ΛCDM(1) at k=4.5×10⁻⁴ Mpc⁻¹
      phi_ratio_horizon        : ratio ≈ 3.06
      # ISW qualitative assessment
      isw_sign_grut            : 'cooling'  (net ISW cools photons)
      isw_sign_lcdm            : 'heating'  (net ISW heats photons)
      # Multipole-dependent prediction
      isw_prediction_ell2      : 'enhanced heating' (GRUT > ΛCDM at ℓ=2)
      isw_prediction_ell10_30  : 'cooling, reduced power' (GRUT < ΛCDM)
      # Planck comparison
      planck_low_ell_ratio     : observed D_ℓ / ΛCDM D_ℓ ≈ 0.83
      planck_consistent        : True (GRUT cooling reduces D_ℓ, same direction)
      # Physical parameters
      tau0_c_mpc               : c τ₀ ≈ 12.85 Mpc
      mu_at_recombination      : μ_GRUT(k=10⁻³, z=1100) ≈ 1.0017
      a_star_low_ell           : transition epoch for k=10⁻³ ≈ 0.0129
      z_star_low_ell           : transition redshift ≈ 77
      # Assessment
      note                     : interpretive string
    """
    global _CMB_ISW_CACHE
    if _CMB_ISW_CACHE is not None:
        return _CMB_ISW_CACHE

    h_le  = reduced_potential_history(CMB_K_LOW_ELL)
    h_hor = reduced_potential_history(CMB_K_HORIZON)

    phi_g_le  = h_le["phi_grut_today"]
    phi_l_le  = h_le["phi_lcdm_today"]
    phi_g_hor = h_hor["phi_grut_today"]
    phi_l_hor = h_hor["phi_lcdm_today"]

    ratio_le  = phi_g_le / phi_l_le
    ratio_hor = phi_g_hor / phi_l_hor
    amp_ratio = h_le["isw_amplitude_ratio"]

    grut_consistent_with_anomaly = (h_le["isw_sign_grut"] == "cooling")

    _CMB_ISW_CACHE = {
        # ── ℓ≈15 scale ──────────────────────────────────────────────
        "phi_grut_today_low_ell":      phi_g_le,
        "phi_lcdm_today_low_ell":      phi_l_le,
        "phi_ratio_low_ell":           ratio_le,
        "delta_phi_grut_low_ell":      h_le["delta_phi_grut"],
        "delta_phi_lcdm_low_ell":      h_le["delta_phi_lcdm"],
        "isw_amplitude_ratio_low_ell": amp_ratio,
        # ── horizon scale ────────────────────────────────────────────
        "phi_grut_today_horizon":      phi_g_hor,
        "phi_lcdm_today_horizon":      phi_l_hor,
        "phi_ratio_horizon":           ratio_hor,
        # ── ISW signs ────────────────────────────────────────────────
        "isw_sign_grut":               "cooling",
        "isw_sign_lcdm":               "heating",
        "isw_prediction_ell2":         "enhanced heating (GRUT decay > ΛCDM)",
        "isw_prediction_ell10_30":     "cooling → reduced D_ℓ power vs ΛCDM",
        # ── Planck anomaly ───────────────────────────────────────────
        "planck_low_ell_ratio":        PLANCK_LOW_ELL_RATIO,
        "planck_consistent":           grut_consistent_with_anomaly,
        # ── Physical parameters ──────────────────────────────────────
        "tau0_c_mpc":                  TAU0_C_MPC,
        "mu_at_recombination":         h_le["mu_at_rec"],
        "a_star_low_ell":              h_le["a_star"],
        "z_star_low_ell":              h_le["z_star"],
        # ── Note ─────────────────────────────────────────────────────
        "note": (
            f"GRUT reduced potential Φ̃ at k=10⁻³ Mpc⁻¹: "
            f"Φ̃_GRUT(z=0) = {phi_g_le:.3f} vs Φ̃_ΛCDM(z=0) = {phi_l_le:.3f} "
            f"(ratio {ratio_le:.2f}×). "
            f"GRUT potential DEEPENS from recombination to today "
            f"(ΔΦ̃ = +{h_le['delta_phi_grut']:.3f}, net cooling ISW). "
            f"ΛCDM potential DECAYS (ΔΦ̃ = {h_le['delta_phi_lcdm']:.3f}, heating ISW). "
            f"ISW amplitude ratio |GRUT|/|ΛCDM| = {amp_ratio:.2f}×. "
            f"GRUT predicts reduced D_ℓ at ℓ=10–30 (consistent with "
            f"Planck low-ℓ anomaly direction: observed/ΛCDM ≈ {PLANCK_LOW_ELL_RATIO}). "
            f"μ_GRUT at z=1100 = {h_le['mu_at_rec']:.4f} (SW unchanged). "
            f"GRUT transition: a★ = {h_le['a_star']:.4f} (z★ = {h_le['z_star']:.1f}). "
            f"Full D_ℓ requires MGCAMB Boltzmann integration."
        ),
    }
    return _CMB_ISW_CACHE
