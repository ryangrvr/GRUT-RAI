"""CMB Boltzmann scoping — quantitative answers to the four questions.

This module computes the framework's CMB predictions at recombination
and packages them for the scoping document. Implementation of an actual
modified Boltzmann code (CLASS/CAMB) is a separate, multi-session task;
this module bounds the effort by establishing what the modification
would actually produce.

The four scoping questions
--------------------------

Q1. What is ωτ_0 at recombination?
    For both the expansion-rate frequency H(z_rec) and the acoustic-mode
    frequency ω_acoustic = c_s × k_first-peak.

Q2. What does n_g(ω) do to the sound horizon?
    The Lorentzian susceptibility shifts r_s and d_A. The angular peak
    scale θ_* = r_s / d_A inherits the difference.

Q3. What would a CLASS/CAMB modification look like?
    Per-equation scoping; effort estimate.

Q4. Success vs failure criteria.
    Compare predicted Δn_g/n_g to Planck precision (3 × 10⁻⁴), CMB-S4
    target precision (5 × 10⁻⁵), and LiteBIRD's polarization sensitivity.

Reference cosmology
-------------------
    Planck 2018 (Aghanim et al. 2020) baseline:
        H_0   = 67.66 km/s/Mpc
        Ω_m   = 0.3158
        Ω_Λ   = 0.6842
        Ω_r   = 9.18 × 10⁻⁵   (photons + 3 massless neutrinos)
        z_rec = 1100
        r_s   = 144.4 Mpc (comoving sound horizon at recombination)
        θ_*   = 1.04097 × 10⁻²    (Planck precision: 3 × 10⁻⁴)
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from grut.foundation.closure_protocol import (
    ALPHA_VAC,
    TAU_0_SEC,
    n_g_refractive,
    susceptibility_chi,
)


# ─────────────────────────────────────────────────────────────────────
# Cosmological inputs (Planck 2018 baseline)
# ─────────────────────────────────────────────────────────────────────

H_0_KM_S_MPC: float = 67.66
OMEGA_M: float = 0.3158
OMEGA_R: float = 9.18e-5
OMEGA_L: float = 0.6842
Z_RECOMBINATION: float = 1100.0
R_S_COMOVING_MPC: float = 144.4
THETA_STAR: float = 1.04097e-2
PLANCK_THETA_PRECISION: float = 3e-4
CMB_S4_TARGET_PRECISION: float = 5e-5

# Unit conversions
MPC_M: float = 3.086e22
KM_M: float = 1e3
C_LIGHT: float = 2.998e8


# ─────────────────────────────────────────────────────────────────────
# Q1: ωτ_0 at recombination
# ─────────────────────────────────────────────────────────────────────

def H_0_Hz(H_0_km_s_Mpc: float = H_0_KM_S_MPC) -> float:
    """H_0 converted from km/s/Mpc to Hz (s⁻¹)."""
    return H_0_km_s_Mpc * KM_M / MPC_M


def H_at_redshift(z: float, h0_kms: float = H_0_KM_S_MPC) -> float:
    """Friedmann equation with Planck-2018 baseline, Hz."""
    expansion_factor_sq = (
        OMEGA_M * (1 + z) ** 3
        + OMEGA_R * (1 + z) ** 4
        + OMEGA_L
    )
    return H_0_Hz(h0_kms) * math.sqrt(expansion_factor_sq)


def omega_acoustic_first_peak(
    z: float = Z_RECOMBINATION,
    r_s_comoving_Mpc: float = R_S_COMOVING_MPC,
    R_baryon_photon: float = 0.6,
) -> float:
    """Angular frequency of the first acoustic peak at redshift z.

    k r_s = π → k_comoving = π / r_s.
    Physical k at the redshift of interest = k_comoving × (1+z).
    Sound speed c_s ≈ c / √(3(1+R)) with R ≈ 0.6 at recombination.
    Returns ω = c_s × k_phys in Hz.
    """
    k_comoving_per_Mpc = math.pi / r_s_comoving_Mpc
    k_phys_per_Mpc = k_comoving_per_Mpc * (1 + z)
    k_phys_per_m = k_phys_per_Mpc / MPC_M
    c_s = C_LIGHT / math.sqrt(3 * (1 + R_baryon_photon))
    return c_s * k_phys_per_m


def omega_tau_0(omega_Hz: float, tau_0: float = TAU_0_SEC) -> float:
    """Dimensionless ωτ_0 — the constitutive regime parameter."""
    return omega_Hz * tau_0


# ─────────────────────────────────────────────────────────────────────
# Q2: n_g(ω) shift in the sound horizon
# ─────────────────────────────────────────────────────────────────────

def alpha_eff(omega_tau: float, alpha: float = ALPHA_VAC) -> float:
    """α_eff(X) = α / (1 + X²) — frequency-gated coupling."""
    return alpha / (1.0 + omega_tau ** 2)


def n_g_at_omega(omega_Hz: float, tau_0: float = TAU_0_SEC) -> float:
    """n_g(ω) = √(1 + α/(1+(ωτ_0)²))."""
    return n_g_refractive(omega_Hz, tau_0_sec=tau_0)


def delta_n_g_over_n_g(omega_Hz: float, tau_0: float = TAU_0_SEC) -> float:
    """(n_g − 1) / n_g — leading-order fractional shift relative to GR."""
    n = n_g_at_omega(omega_Hz, tau_0)
    return (n - 1.0) / n


def sound_horizon_shift_estimate(
    omega_H_rec_tau: float,
) -> float:
    """Leading-order GRUT shift in r_s.

    The Friedmann equation is modified by H² → H² × n_g²(H τ_0). For
    ωτ_0 ≫ 1, n_g² ≈ 1 + α/(ωτ_0)². The fractional shift:

        Δr_s / r_s ≈ −(1/2) × α / (ωτ_0)²

    (Negative because faster expansion ⟹ less sound-horizon
    accumulation; positive shift in 1/H ⟹ more accumulation.)
    """
    return 0.5 * ALPHA_VAC / (1.0 + omega_H_rec_tau ** 2)


# ─────────────────────────────────────────────────────────────────────
# Scoping report
# ─────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class CMBScopingReport:
    """All four questions' quantitative answers, packaged."""
    # Q1 — ωτ_0 at recombination
    H_rec_Hz: float
    H_rec_over_H_0: float
    omega_tau_0_expansion: float
    omega_acoustic_Hz: float
    omega_tau_0_acoustic: float
    # Q2 — n_g shift
    delta_n_g_over_n_g_at_H_rec: float
    delta_n_g_over_n_g_at_acoustic: float
    sound_horizon_shift_relative: float
    theta_star_shift_relative: float  # leading order = same as r_s shift
    # Q4 — observability
    planck_precision: float
    cmb_s4_precision: float
    detectability_now: bool
    detectability_cmb_s4: bool


def cmb_scoping_report() -> CMBScopingReport:
    """Compute all scoping numbers for the four questions."""
    H_rec = H_at_redshift(Z_RECOMBINATION)
    omega_tau_H = omega_tau_0(H_rec)

    omega_ac = omega_acoustic_first_peak()
    omega_tau_ac = omega_tau_0(omega_ac)

    dn_H = delta_n_g_over_n_g(H_rec)
    dn_ac = delta_n_g_over_n_g(omega_ac)

    drs = sound_horizon_shift_estimate(omega_tau_H)
    # Leading-order: θ_* = r_s / d_A; both inherit the n_g correction.
    # The dominant shift to θ_* comes through r_s (recombination-era
    # acoustic horizon). d_A integrates predominantly through z ≈ 0–1
    # where ωτ_0 ≪ 1 (fluid regime); however GRUT's Ω_Λ matches Planck
    # to 0.04% by construction, so d_A is essentially the same as ΛCDM
    # in the framework. Net θ_* shift ≈ r_s shift to leading order.
    dtheta = drs

    return CMBScopingReport(
        H_rec_Hz=H_rec,
        H_rec_over_H_0=H_rec / H_0_Hz(),
        omega_tau_0_expansion=omega_tau_H,
        omega_acoustic_Hz=omega_ac,
        omega_tau_0_acoustic=omega_tau_ac,
        delta_n_g_over_n_g_at_H_rec=dn_H,
        delta_n_g_over_n_g_at_acoustic=dn_ac,
        sound_horizon_shift_relative=drs,
        theta_star_shift_relative=dtheta,
        planck_precision=PLANCK_THETA_PRECISION,
        cmb_s4_precision=CMB_S4_TARGET_PRECISION,
        detectability_now=dtheta > PLANCK_THETA_PRECISION,
        detectability_cmb_s4=dtheta > CMB_S4_TARGET_PRECISION,
    )


# ─────────────────────────────────────────────────────────────────────
# Verification harness
# ─────────────────────────────────────────────────────────────────────

def verify() -> dict:
    """Six legs covering the four scoping questions."""
    rep = cmb_scoping_report()
    return {
        # Q1: ωτ_0 at recombination is large but finite (deep crystal,
        # but not infinite — corrections exist)
        "expansion_omega_tau_in_50_to_100_band": (
            50 < rep.omega_tau_0_expansion < 100
        ),
        "acoustic_omega_tau_in_100_to_200_band": (
            100 < rep.omega_tau_0_acoustic < 200
        ),
        # Q2: predicted shifts are O(10⁻⁵)
        "delta_n_g_at_H_rec_in_band": (
            1e-5 < rep.delta_n_g_over_n_g_at_H_rec < 1e-4
        ),
        "delta_n_g_at_acoustic_in_band": (
            1e-6 < rep.delta_n_g_over_n_g_at_acoustic < 1e-4
        ),
        # Q4: Planck cannot detect; CMB-S4 sits near the threshold
        "below_planck_precision": (
            rep.theta_star_shift_relative < rep.planck_precision
        ),
        "cmb_s4_within_factor_5_of_threshold": (
            0.2 * rep.cmb_s4_precision
            < rep.theta_star_shift_relative
            < 5 * rep.cmb_s4_precision
        ),
    }


# ─────────────────────────────────────────────────────────────────────
# Q3: CLASS / CAMB modification scoping (descriptive)
# ─────────────────────────────────────────────────────────────────────

CLASS_ENTRY_POINTS: dict[str, str] = {
    "background_module": (
        "background.c — Friedmann equation H²(a) = (8πG/3) ρ. "
        "GRUT modification: H² × n_g²(H τ_0). Self-consistent because "
        "the relevant ω is H itself; resolved by iteration or direct "
        "substitution."
    ),
    "perturbations_module_einstein": (
        "perturbations.c::perturb_einstein() — Newtonian-gauge "
        "Poisson: k² Φ = −4πG a² δρ. GRUT modification: "
        "k² Φ = −4πG a² δρ × n_g²(ω) where ω = ∂_t Φ / Φ at the "
        "perturbation's natural frequency. Most consequential entry point."
    ),
    "thermodynamics_module": (
        "thermodynamics.c — recombination history and visibility "
        "function. GRUT modification: minor (T(z), z_rec largely "
        "unchanged because the Saha equation depends on photon "
        "thermodynamics, not gravity). Likely no patch needed."
    ),
}

CAMB_ENTRY_POINTS: dict[str, str] = {
    "equations_f90": (
        "equations.f90 — derivs() function evolves the Boltzmann + "
        "Einstein system. GRUT modification: same as CLASS — apply "
        "n_g²(ω) factor in the gravitational potential equation."
    ),
    "gauge_invariant_perturbations": (
        "GaugeInterface.f90 — gauge-invariant perturbation variables. "
        "GRUT modification: ensure n_g²(ω) factor is gauge-invariant; "
        "most cleanly applied in synchronous or Newtonian gauge."
    ),
}


CLASS_CAMB_EFFORT_ESTIMATE: str = (
    "4-8 weeks specialist work. Tasks: (1) add τ_0 and α_vac as new "
    "cosmological parameters; (2) modify the gravitational Poisson "
    "equation in the perturbations module to apply n_g²(ω); (3) "
    "calibrate against unmodified CLASS/CAMB output for ωτ_0 ≫ 1 "
    "(reproduces ΛCDM); (4) re-derive C_l power spectra; (5) MCMC "
    "fit against Planck likelihood. Phase-2+ task. Requires CLASS or "
    "CAMB experience and access to Planck likelihood code."
)


if __name__ == "__main__":
    rep = cmb_scoping_report()
    print("=" * 78)
    print("CMB Boltzmann scoping — quantitative answers")
    print("=" * 78)
    print()
    print("Q1. ωτ_0 at recombination (z_rec = 1100):")
    print(f"     H_rec              = {rep.H_rec_Hz:.3e} Hz "
          f"({rep.H_rec_over_H_0:.2e} × H_0)")
    print(f"     H_rec × τ_0        = {rep.omega_tau_0_expansion:.1f}    "
          "(expansion-rate ωτ_0)")
    print(f"     ω_acoustic         = {rep.omega_acoustic_Hz:.3e} Hz "
          "(first acoustic peak)")
    print(f"     ω_acoustic × τ_0   = {rep.omega_tau_0_acoustic:.1f}    "
          "(acoustic-mode ωτ_0)")
    print(f"     → Both ≫ 1 — vacuum is in DEEP CRYSTAL regime at "
          "recombination.")
    print()
    print("Q2. n_g(ω) shift at recombination:")
    print(f"     Δn_g/n_g at H_rec       = {rep.delta_n_g_over_n_g_at_H_rec:.2e}")
    print(f"     Δn_g/n_g at acoustic    = {rep.delta_n_g_over_n_g_at_acoustic:.2e}")
    print(f"     Δr_s/r_s (leading)      = {rep.sound_horizon_shift_relative:.2e}")
    print(f"     Δθ_*/θ_* (≈ Δr_s/r_s)   = {rep.theta_star_shift_relative:.2e}")
    print()
    print("Q3. CLASS/CAMB modification entry points:")
    for k, v in CLASS_ENTRY_POINTS.items():
        print(f"     • CLASS/{k}: {v[:80]}...")
    print(f"     Effort: {CLASS_CAMB_EFFORT_ESTIMATE.split('.')[0]}.")
    print()
    print("Q4. Detectability:")
    print(f"     Planck 2018 precision:    {rep.planck_precision:.1e}  "
          f"detectable now: {rep.detectability_now}")
    print(f"     CMB-S4 target precision:  {rep.cmb_s4_precision:.1e}  "
          f"detectable @ S4: {rep.detectability_cmb_s4}")
    print()
    print("Verify:")
    for k, v in verify().items():
        mark = "PASS" if v else "FAIL"
        print(f"  [{mark}] {k}")
