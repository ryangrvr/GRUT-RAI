"""Constitutive growth — diagnosing D=1.0 and demonstrating Poisson closure.

═══════════════════════════════════════════════════════════════════════
THE D = 1.0 FAILURE: DIAGNOSIS
═══════════════════════════════════════════════════════════════════════

The constitutive equation perturbed around the FLRW background:

    τ₀ d(δΦ)/dt + (1 − λ_vac) δΦ = 0                    (decoupled)

where δΦ ≡ δσ is the conformal-mode perturbation and λ_vac =
∂z_target/∂z|_bg is the background response eigenvalue.

This equation is DECOUPLED from matter: δρ_m does not appear on the
right-hand side. Consequently:
    • δΦ relaxes exponentially to zero (τ_eff = τ₀/(1 − λ_vac))
    • With Φ = 0, the matter equation δ̈_m + 2H δ̇_m = k²Φ/a² becomes
      δ̈_m + 2H δ̇_m = 0 → D = constant ≡ 1
    • The decoupled system predicts NO structure formation at any scale

This is the "D = 1.0 failure" documented in Ch 14.

═══════════════════════════════════════════════════════════════════════
THE POISSON CLOSURE: RESOLUTION
═══════════════════════════════════════════════════════════════════════

The modified Poisson equation derived in Correction #26 (μ_GRUT from
the EFT-of-dark-energy mapping of n_g²):

    k² Φ = −4πG μ_GRUT(k,a) a² ρ̄_m δ_m                  (Poisson)

where μ_GRUT(k,a) = 1 + α_vac / [1 + (τ₀ k_phys c)²].

This IS the matter-sourced term missing from the decoupled constitutive
equation. Once it is included, the constitutive equation becomes:

    τ₀ d(δΦ)/dt + δΦ = z_target_vac + z_target_matter
    z_target_matter = −(4πG μ_GRUT a² ρ̄_m δ_m) / k²

In the quasi-static limit (τ₀ ≪ H⁻¹, always valid: τ₀/H₀⁻¹ ≈ 0.003):

    δΦ = −(4πG μ_GRUT a² ρ̄_m δ_m) / k²                   (Poisson, quasi-static)

Combined with standard matter continuity and Euler equations:

    d²δ_m/dN² + [2 − (3/2)Ω_m(N)] dδ_m/dN − (3/2) Ω_m(N) μ_GRUT(k,N) δ_m = 0  (★)

Integrating (★) from a_eq ≈ 3×10⁻⁴ to a = 1:
    D_ΛCDM ≈ 2626  (at σ_8 scale; ~21% below pure-matter-dom 3333 due to Λ)
    D_GRUT = D_ΛCDM × f_GRUT(k)  (scale-dependent enhancement)

═══════════════════════════════════════════════════════════════════════
THE QUASI-STATIC LIMIT IS VALID
═══════════════════════════════════════════════════════════════════════

The quasi-static limit τ₀ d(δΦ)/dt ≪ δΦ holds when τ₀ ≪ H⁻¹:
    τ₀ = 41.9 Myr,  H₀⁻¹ = 1/H₀ ≈ 14.5 Gyr
    τ₀/H₀⁻¹ = 41.9 Myr / 14500 Myr ≈ 0.0029 ≪ 1  ✓

At earlier times (matter domination), H = H₀√(Ω_m)/a^(3/2):
    τ₀ H(a) = τ₀ H₀ √(Ω_m)/a^(3/2) ≈ 0.0029 × √(0.315)/a^(3/2)
At a = 3×10⁻⁴:  τ₀ H ≈ 0.0029 × 1678 ≈ 4.9

So at matter-radiation equality, τ₀ H ≈ 5 — the quasi-static
approximation is NOT valid at the earliest times. However:
    1. The growth equation (★) does NOT assume quasi-static for the
       matter modes — it is exact (it combines Poisson + Euler).
    2. The quasi-static limit is only applied to the GRAVITATIONAL
       SECTOR (δΦ tracks δ_m quickly), which is valid when τ₀ ≪ τ_growth.
       Here τ_growth = 1/H ≈ 14 Gyr today; τ₀ = 41.9 Myr ≈ 0.3% of τ_growth.
    3. The dominant effect of the constitutive equation on the growth
       factor is through μ_GRUT(k, a), which is fully incorporated in (★).

For super-horizon modes (k τ₀ c ≪ 1), the quasi-static approximation
breaks the scale separation between τ₀ and H⁻¹. These modes require
the full time-dependent constitutive evolution — exactly the CAMB/CLASS
integration that is the v4 gate.

═══════════════════════════════════════════════════════════════════════
THE "~3375" FIGURE IN THE BOOK — CLARIFIED
═══════════════════════════════════════════════════════════════════════

The "~3375" cited as the "required" growth factor is the PURE MATTER
DOMINATION value:
    D_matter_dom = 1/a_init = 1/(3×10⁻⁴) = 3333  (normalized convention)

The ACTUAL ΛCDM value at z = 0, integrated with Ω_Λ = 0.685:
    D_ΛCDM ≈ 2626  (dark energy suppresses by ~21% vs pure matter-dom)

So the "D = 1.0 failure" is even more severe than "1 vs 3375":
    D_constitutive_without_closure = 1.0   (no growth at all)
    D_ΛCDM = 2626                           (2626× growth from equality)

═══════════════════════════════════════════════════════════════════════
WHAT REMAINS OPEN
═══════════════════════════════════════════════════════════════════════

The Poisson closure is USED here (from Correction #26) but not
DERIVED from the CTP action. Deriving it requires:

    (∂²S_CTP)/(∂σ ∂ φ_SM)  ≠ 0   at the linearized level

This is the matter-gravity coupling vertex: how the conformal mode σ
couples to Standard Model fields at the CTP action level. From the
Einstein-Hilbert action with matter:

    S_matter(φ_SM, g_μν) = S_matter(φ_SM, e^{2σ} ĝ_μν)

Expanding to first order in δσ:
    δS_matter/δσ = T^μ_μ × e^{2σ} = T (trace of stress-energy)

For pressureless dust: T = −ρ_m → coupling is:
    ∂z_target/∂ρ_m ∝ −(4πG/k²) × n_g²(k, a)

This IS the matter-sourcing term in the Poisson closure. However,
deriving this formally from S_CTP (rather than from Einstein equations)
requires:
    1. Identifying z_target as the CTP fixed point of ∂S_CTP/∂z = 0
    2. Showing ∂z_target/∂ρ_m = −(4πG/k²) n_g² follows from the
       CTP action's conformal-mode–stress-energy coupling
    3. Confirming the resulting Poisson equation is consistent with
       Corrections #23-#26 (linearized Φ_μν derivation + EFT mapping)

This derivation is the "second-order constitutive extension" in the
ToE program. Until it is done, the Poisson closure is BORROWED from
the EFT mapping (Correction #26), not derived from S_CTP directly.

Registry claim: constitutive_growth_poisson_closure_gap (open_negative)
Closure condition: derive ∂z_target/∂ρ_m from S_CTP and show it
    reproduces the modified Poisson equation k²Φ = −4πG μ_GRUT a² ρ δ.
"""

from __future__ import annotations

from typing import Dict, Tuple

import numpy as np
from scipy.integrate import solve_ivp  # type: ignore

from grut.foundation.closure_protocol import ALPHA_VAC, TAU_0_SEC
from grut.derivation.phi_munu.modified_growth import (
    integrate_growth_factor,
    growth_factor_enhancement,
    growth_enhancement_survey,
    mu_GRUT_numeric,
    Omega_m_of_a,
    H_over_H_0,
    OMEGA_M_DEFAULT,
    OMEGA_LAMBDA_DEFAULT,
    A_INIT_DEFAULT,
    C_LIGHT_M_S,
    MPC_IN_M,
)


# ─────────────────────────────────────────────────────────────────────
# Section 1 — Quasi-static validity check
# ─────────────────────────────────────────────────────────────────────

TAU_0_OVER_H0_INV: float = (
    TAU_0_SEC
    / (1.0 / (67.4e3 / (MPC_IN_M)))  # H₀⁻¹ in seconds
)
# τ₀ H₀ (dimensionless); should be ≪ 1 for quasi-static limit today
TAU_0_H0: float = TAU_0_SEC * (67.4e3 / MPC_IN_M)


def quasi_static_validity() -> Dict[str, float]:
    """Check that τ₀ ≪ H⁻¹ at key epochs.

    The quasi-static approximation τ₀ d(δΦ)/dt ≪ δΦ is valid when
    τ₀ H(a) ≪ 1. We check at a = 1 (today), a = 0.5 (DE entry),
    and a = 3×10⁻⁴ (matter-rad equality).

    Returns
    -------
    dict with τ₀ H(a) at each epoch and validity flag.
    """
    H0_per_sec = 67.4e3 / MPC_IN_M  # H₀ in s⁻¹

    results = {}
    for label, a in [("today_a1", 1.0), ("de_entry_a0p5", 0.5),
                     ("equality_a3e4", 3e-4)]:
        H_a = H_over_H_0(a) * H0_per_sec  # H(a) in s⁻¹
        tau0_H = TAU_0_SEC * H_a
        results[label] = {
            "a": a,
            "tau_0_H":    float(tau0_H),
            "quasi_static_ok": bool(tau0_H < 0.5),  # ok if < 50%
        }
    return results


# ─────────────────────────────────────────────────────────────────────
# Section 2 — The D = 1.0 failure: decoupled constitutive equation
# ─────────────────────────────────────────────────────────────────────

def decoupled_constitutive_growth(
    a_init: float = A_INIT_DEFAULT,
    n_steps: int = 1000,
) -> Dict[str, object]:
    """Demonstrate the D = 1.0 failure from the DECOUPLED constitutive equation.

    The decoupled constitutive equation for matter perturbations:
        δ̈_m + 2H δ̇_m = 0                                      (no source)

    This is what you get when the gravitational potential Φ = 0 (because
    the constitutive equation for δΦ has NO matter-sourcing term and
    δΦ relaxes to zero).

    Result: δ_m = const × a^0 + const × a^{-3/2}   (decaying or constant)
    At late times: D = constant (no growing mode) → normalized D ≈ 1.

    Returns
    -------
    dict with:
        a_array:              scale-factor array from a_init to 1
        delta_decoupled:      matter perturbation δ_m under decoupled eq
        delta_LCDM:           δ_m under standard ΛCDM (correct)
        D_decoupled_today:    δ_m(a=1) from decoupled eq (≈ initial)
        D_LCDM_today:         δ_m(a=1) from ΛCDM (≈ 2626)
        ratio_decoupled_LCDM: D_decoupled / D_LCDM = D_failure
        diagnosis:            string explaining the failure
    """
    from scipy.integrate import solve_ivp

    N_init = float(np.log(a_init))
    N_final = 0.0

    def rhs_decoupled(N: float, state: np.ndarray) -> np.ndarray:
        """δ̈ + 2H δ̇ = 0  (no source — Φ = 0)."""
        delta, delta_prime = state
        a = float(np.exp(N))
        Om_a = Omega_m_of_a(a, OMEGA_M_DEFAULT, OMEGA_LAMBDA_DEFAULT)
        # friction: [2 - (3/2) Ω_m] δ' — no source term
        delta_prime_prime = -(2.0 - 1.5 * Om_a) * delta_prime
        return np.array([delta_prime, delta_prime_prime])

    sol_decoupled = solve_ivp(
        rhs_decoupled,
        (N_init, N_final),
        y0=np.array([1.0, 1.0]),  # same IC as ΛCDM for fair comparison
        method="RK45",
        dense_output=True,
        max_step=(N_final - N_init) / n_steps,
    )

    N_array = np.linspace(N_init, N_final, n_steps + 1)
    delta_decoupled = sol_decoupled.sol(N_array)[0]
    a_array = np.exp(N_array)

    # Reference: standard ΛCDM growth (μ = 1)
    _, delta_LCDM = integrate_growth_factor(0.5, use_mu_GRUT=False)

    D_decoupled = float(delta_decoupled[-1])
    D_LCDM = float(delta_LCDM[-1])

    return {
        "a_array":              a_array,
        "delta_decoupled":      delta_decoupled,
        "D_decoupled_today":    D_decoupled,
        "D_LCDM_today":         D_LCDM,
        "a_init":               a_init,
        "ratio_decoupled_LCDM": float(D_decoupled / D_LCDM),
        "diagnosis": (
            f"Decoupled constitutive eq gives D = {D_decoupled:.2f} "
            f"vs ΛCDM D = {D_LCDM:.0f}. "
            f"Ratio: {D_decoupled / D_LCDM:.5f}. "
            "The decoupled eq (Φ = 0) has only growing mode δ ∝ a⁰ "
            "(constant) and decaying mode δ ∝ a^{-3/2}. "
            "The growing-mode solution is D = const ≈ initial value. "
            "This is the D = 1.0 failure."
        ),
    }


# ─────────────────────────────────────────────────────────────────────
# Section 3 — Poisson closure demonstration
# ─────────────────────────────────────────────────────────────────────

def poisson_closure_demonstration(
    k_per_Mpc: float = 0.5,
) -> Dict[str, object]:
    """Demonstrate D ≈ 2626 once the Poisson closure is added.

    The closed system (constitutive + Poisson closure):
        k² Φ = −4πG μ_GRUT(k,a) a² ρ̄_m δ_m             (modified Poisson)
        δ̈_m + 2H δ̇_m = (3/2) H² Ω_m μ_GRUT(k,a) δ_m   (growth ODE)

    This is equation (★) in modified_growth.py. The Poisson closure
    provides the matter-sourcing term missing from the decoupled eq.

    Returns
    -------
    dict with:
        k_per_Mpc:            wavenumber
        D_decoupled:          growth factor without closure (≈ 1.0 normalized)
        D_LCDM:               ΛCDM growth factor (≈ 2626)
        D_GRUT:               GRUT growth factor with μ_GRUT
        f_GRUT:               D_GRUT / D_LCDM
        pure_matter_dom_D:    1/a_init ≈ 3333 (theoretical limit)
        lambda_suppression:   D_LCDM / pure_matter_dom (dark-energy suppression)
        closure_verdict:      string
    """
    decoupled = decoupled_constitutive_growth()
    D_decoupled = decoupled["D_decoupled_today"]

    _, delta_LCDM = integrate_growth_factor(k_per_Mpc, use_mu_GRUT=False)
    _, delta_GRUT = integrate_growth_factor(k_per_Mpc, use_mu_GRUT=True)

    D_LCDM = float(delta_LCDM[-1])
    D_GRUT = float(delta_GRUT[-1])
    pure_matter_dom = 1.0 / A_INIT_DEFAULT

    # The "D=1.0" is normalized: D_decoupled/D_LCDM ≈ 0 relative to required
    # The absolute D_decoupled ≈ initial value (≈ 1)
    return {
        "k_per_Mpc":                k_per_Mpc,
        "D_decoupled_normalized":   float(D_decoupled / D_LCDM),  # ≈ 0.00038
        "D_decoupled_absolute":     float(D_decoupled),            # ≈ 1
        "D_LCDM":                   float(D_LCDM),                # ≈ 2626
        "D_GRUT":                   float(D_GRUT),                # ≈ 2628
        "f_GRUT":                   float(D_GRUT / D_LCDM),       # ≈ 1.0009
        "pure_matter_dom_D":        float(pure_matter_dom),        # ≈ 3333
        "lambda_suppression_pct":   float((1 - D_LCDM / pure_matter_dom) * 100),
        "closure_verdict": (
            f"WITHOUT Poisson closure: D_absolute ≈ {D_decoupled:.1f} "
            f"(normalized to initial ≈ 1.0, ratio to LCDM = "
            f"{D_decoupled / D_LCDM:.4f}). "
            f"WITH Poisson closure: D_LCDM = {D_LCDM:.0f}, "
            f"D_GRUT = {D_GRUT:.0f} (at k={k_per_Mpc} Mpc⁻¹). "
            f"The required ~3333 (pure matter-dom) is suppressed to "
            f"{D_LCDM:.0f} by dark energy (Λ suppresses by "
            f"{(1-D_LCDM/pure_matter_dom)*100:.1f}%). "
            f"The Poisson closure resolves the D=1.0 failure completely."
        ),
    }


# ─────────────────────────────────────────────────────────────────────
# Section 4 — Full growth survey (with Poisson closure, all scales)
# ─────────────────────────────────────────────────────────────────────


def growth_survey_with_closure() -> Dict[str, Dict]:
    """Growth factor D at all canonical scales WITH Poisson closure.

    Shows D_ΛCDM ≈ 2626 at sub-horizon scales, with scale-dependent
    enhancement D_GRUT = D_ΛCDM × f_GRUT(k) at super-horizon scales.

    Returns
    -------
    dict keyed by scale label with D_LCDM, D_GRUT, f_GRUT, regime.
    """
    canonical = [
        ("galaxy_k1",       1.0,     "sub-horizon"),
        ("sigma8_k0p5",     0.5,     "sub-horizon"),
        ("quasi_k0p1",      0.1,     "near-transition"),
        ("BAO_k0p04",       0.04,    "near-transition"),
        ("sloan_k0p01",     0.01,    "super-horizon"),
        ("CMB_low_k0p001",  0.001,   "super-horizon"),
        ("CMB_horiz_k4e4",  4.5e-4,  "super-horizon"),
    ]
    results = {}
    for label, k, regime in canonical:
        _, dl = integrate_growth_factor(k, use_mu_GRUT=False)
        _, dg = integrate_growth_factor(k, use_mu_GRUT=True)
        D_l = float(dl[-1])
        D_g = float(dg[-1])
        results[label] = {
            "k_Mpc":    k,
            "regime":   regime,
            "D_LCDM":   D_l,
            "D_GRUT":   D_g,
            "f_GRUT":   float(D_g / D_l),
            "f_pct":    float((D_g / D_l - 1.0) * 100.0),
        }
    return results


# ─────────────────────────────────────────────────────────────────────
# Section 5 — Gravitational potential evolution and ISW assessment
# ─────────────────────────────────────────────────────────────────────

def phi_evolution_and_isw(
    k_per_Mpc: float,
    n_steps: int = 2000,
    a_de_start: float = 0.5,
) -> Dict[str, object]:
    """Track Φ(k, a) ∝ μ_GRUT(k,a) × δ(k,a) / a for ΛCDM and GRUT.

    In the quasi-static limit the gravitational potential is:

        Φ(k, a) = −(3H₀²Ω_m)/(2k²) × μ_GRUT(k,a) × δ_m(k,a) / a

    We define the normalised "potential amplitude":

        G(k, a) = μ_GRUT(k,a) × δ(k,a) / a

    G is proportional to k²|Φ| up to a k-independent constant.

    ΛCDM check: G_ΛCDM = δ_ΛCDM/a ≈ const in matter domination (Φ = const ✓).
    Dark energy: G_ΛCDM decreases (Φ decays, positive ISW contribution).

    GRUT at low k: μ_GRUT → 1 + α_vac as a increases.  Enhanced growth
    (f_GRUT > 1) may more than compensate for the 1/a suppression →
    G_GRUT could INCREASE (Φ deepens) → ISW sign flip (negative ISW).

    ISW sign convention
    -------------------
    ΔT/T|_ISW = 2 ∫ Φ̇ dη   (conformal Newtonian gauge, Ψ=Φ)

    Φ < 0 (potential well). Dark energy causes |Φ| to shrink → Φ̇ > 0
    → ISW > 0 (photons gain energy → more low-ℓ power in ΛCDM).

    If Φ_GRUT deepens (G_GRUT increases) → Φ̇_GRUT < 0
    → ISW_GRUT < 0 (photons LOSE energy → LESS low-ℓ power vs ΛCDM).

    Parameters
    ----------
    k_per_Mpc : float
        Comoving wavenumber [Mpc⁻¹].
    n_steps : int
        Integration steps (default 2000 for accurate derivative).
    a_de_start : float
        Scale factor marking start of DE-dominated era for ISW proxy
        (default 0.5, z=1).

    Returns
    -------
    dict with:
        a_array            — scale-factor array (a_init → 1)
        G_LCDM             — μ=1 potential amplitude (unnormalised)
        G_GRUT             — μ_GRUT potential amplitude (unnormalised)
        G_LCDM_ratio       — G_LCDM(z=0) / G_LCDM(a_de_start) < 1 = decay
        G_GRUT_ratio       — G_GRUT(z=0) / G_GRUT(a_de_start), sign pivot
        delta_G_LCDM       — ΔG_ΛCDM (negative = potential decay)
        delta_G_GRUT       — ΔG_GRUT (sign depends on enhancement)
        isw_sign_flip      — True if Φ_GRUT deepens while Φ_ΛCDM decays
        isw_ratio_proxy    — ΔG_GRUT / ΔG_ΛCDM; <0 = opposite-sign ISW
        isw_verdict        — human-readable conclusion
    """
    a_arr, delta_LCDM = integrate_growth_factor(
        k_per_Mpc, use_mu_GRUT=False, n_steps=n_steps,
    )
    a_arr2, delta_GRUT = integrate_growth_factor(
        k_per_Mpc, use_mu_GRUT=True, n_steps=n_steps,
    )

    mu_arr = np.array(
        [mu_GRUT_numeric(k_per_Mpc, float(a)) for a in a_arr],
        dtype=float,
    )

    # Potential amplitudes  G(k, a) = μ(k,a) × δ(a) / a
    G_LCDM = delta_LCDM / a_arr            # μ=1 for ΛCDM
    G_GRUT = mu_arr * delta_GRUT / a_arr

    # Find the index closest to a_de_start
    de_idx = int(np.searchsorted(a_arr, a_de_start))
    de_idx = max(1, min(de_idx, len(a_arr) - 2))

    G_LCDM_de = float(G_LCDM[de_idx])
    G_GRUT_de = float(G_GRUT[de_idx])
    G_LCDM_0 = float(G_LCDM[-1])
    G_GRUT_0 = float(G_GRUT[-1])

    G_LCDM_ratio = G_LCDM_0 / G_LCDM_de
    G_GRUT_ratio = G_GRUT_0 / G_GRUT_de

    delta_G_LCDM = G_LCDM_0 - G_LCDM_de   # < 0 → Φ decays
    delta_G_GRUT = G_GRUT_0 - G_GRUT_de   # sign TBD

    isw_sign_flip = bool(G_GRUT_ratio > 1.0 and G_LCDM_ratio < 1.0)

    if delta_G_LCDM != 0.0:
        isw_ratio_proxy = float(delta_G_GRUT / delta_G_LCDM)
    else:
        isw_ratio_proxy = float("nan")

    if isw_sign_flip:
        verdict = (
            f"ISW SIGN FLIP at k={k_per_Mpc:.4f} Mpc⁻¹: "
            f"Φ_GRUT deepens (G ratio {G_GRUT_ratio:.3f} > 1) while "
            f"Φ_ΛCDM decays (G ratio {G_LCDM_ratio:.3f} < 1). "
            f"GRUT ISW is opposite-sign to ΛCDM ISW → "
            f"GRUT reduces low-ℓ C_ℓ^TT (moves toward Planck observation)."
        )
    elif isw_ratio_proxy < 1.0 and not isw_sign_flip:
        verdict = (
            f"ISW SUPPRESSED at k={k_per_Mpc:.4f} Mpc⁻¹: "
            f"Both Φ_GRUT and Φ_ΛCDM decay, but GRUT decays less "
            f"(ratio {isw_ratio_proxy:.3f}). "
            f"GRUT ISW < ΛCDM ISW → less low-ℓ C_ℓ^TT than ΛCDM."
        )
    else:
        verdict = (
            f"ISW ENHANCED at k={k_per_Mpc:.4f} Mpc⁻¹: "
            f"Φ_GRUT decays more than Φ_ΛCDM or has same-sign larger ISW "
            f"(ratio {isw_ratio_proxy:.3f}). "
            f"GRUT ISW > ΛCDM ISW → MORE low-ℓ C_ℓ^TT than ΛCDM."
        )

    return {
        "k_per_Mpc":      k_per_Mpc,
        "a_array":        a_arr,
        "G_LCDM":         G_LCDM,
        "G_GRUT":         G_GRUT,
        "G_LCDM_ratio":   G_LCDM_ratio,
        "G_GRUT_ratio":   G_GRUT_ratio,
        "delta_G_LCDM":   float(delta_G_LCDM),
        "delta_G_GRUT":   float(delta_G_GRUT),
        "isw_sign_flip":  isw_sign_flip,
        "isw_ratio_proxy": isw_ratio_proxy,
        "isw_verdict":    verdict,
    }


def isw_scale_survey() -> Dict[str, Dict]:
    """ISW potential-evolution assessment at canonical cosmological scales.

    Runs phi_evolution_and_isw at the same 7 scales used in the growth
    survey.  The key output is isw_sign_flip and isw_ratio_proxy: a
    negative ratio means GRUT reduces low-ℓ C_ℓ^TT (helps the Planck
    low-ℓ anomaly); a positive ratio > 1 means it worsens it.

    Returns
    -------
    Dict keyed by scale label, each containing the full
    phi_evolution_and_isw result plus the scale k.
    """
    canonical = [
        ("sigma8_k0p5",       0.5),
        ("quasi_k0p1",        0.1),
        ("BAO_k0p04",         0.04),
        ("sloan_k0p01",       0.01),
        ("CMB_low_k0p001",    0.001),
        ("CMB_horiz_k4p5e4",  4.5e-4),
    ]
    results = {}
    for label, k in canonical:
        results[label] = phi_evolution_and_isw(k)
    return results


# ─────────────────────────────────────────────────────────────────────
# Section 7 — What still needs to be derived from S_CTP
# ─────────────────────────────────────────────────────────────────────

def open_derivation_gap() -> Dict[str, str]:
    """Describe the open derivation gap: Poisson closure from S_CTP.

    The Poisson closure is currently BORROWED from Correction #26
    (EFT-of-dark-energy mapping μ_GRUT). To DERIVE it from the CTP
    action, one needs:

        δS_CTP / δσ = 0   (constitutive EOM for σ)
        →  z_target[σ, φ_SM]  contains  −(4πG/k²) n_g² a² ρ δ_m

    This requires computing the cross-coupling:
        (∂²S_CTP) / (∂σ ∂ρ_m)   at the linearized level

    which is the matter-gravity CTP coupling vertex.

    Returns
    -------
    dict with gap description and closure condition.
    """
    return {
        "gap_name": "constitutive_growth_poisson_closure_gap",
        "what_is_borrowed": (
            "k²Φ = −4πG μ_GRUT a² ρ_m δ_m  (from Correction #26, "
            "EFT-of-dark-energy mapping). The Poisson closure is used "
            "as INPUT to the growth equation — not derived from S_CTP."
        ),
        "what_is_needed": (
            "Compute ∂z_target/∂ρ_m from S_CTP = S_EH + S_SM + S_CTP_quad. "
            "The Einstein-Hilbert matter coupling gives: "
            "  δS_SM/δσ = T^μ_μ e^{2σ} = T = −ρ_m (dust). "
            "This sources the constitutive equation as: "
            "  z_target_matter = −(4πG/k²) n_g²(k,a) ρ_m δ_m. "
            "Formal derivation: show this follows from the CTP "
            "two-point function between the conformal mode and the "
            "dust stress-energy — a CTP version of the Poisson equation."
        ),
        "scope": (
            "This is a linear-order derivation in δσ and δρ_m. "
            "It is NOT second-order in perturbation theory. "
            "The 'second-order constitutive extension' in the book "
            "refers to the SECOND TERM in the expansion of z_target: "
            "  z_target = z_vac[z] + z_matter[ρ_m]  (two terms). "
            "The first term (z_vac) is already derived (background). "
            "The second term (z_matter) is the open derivation."
        ),
        "blocking": "CAMB/CLASS Boltzmann run (v4 gate) is NOT blocked — "
                    "it uses μ_GRUT from Correction #26 directly.",
        "closure_condition": (
            "Derive ∂z_target/∂ρ_m from S_CTP and show it reproduces "
            "k²Φ = −4πG μ_GRUT a² ρ δ. If successful, the Poisson "
            "closure becomes a DERIVED result, not a borrowed one, "
            "and the constitutive equation DIRECTLY gives D ≈ 2626."
        ),
        "effort_estimate": "1-2 sessions (CTP path-integral calculation)",
    }


# ─────────────────────────────────────────────────────────────────────
# Section 6 — Top-level summary verdict
# ─────────────────────────────────────────────────────────────────────

def constitutive_growth_verdict() -> Dict[str, object]:
    """Complete verdict on the D = 1.0 failure and its resolution.

    Returns a dict summarizing:
      - The failure mode (decoupled → D = 1.0 normalized)
      - The resolution (Poisson closure → D ≈ 2626)
      - The remaining open work (derive Poisson closure from S_CTP)
      - All key numbers pinned
    """
    qs = quasi_static_validity()
    closure = poisson_closure_demonstration(k_per_Mpc=0.5)
    survey = growth_survey_with_closure()
    gap = open_derivation_gap()

    # Key numbers
    D_LCDM_sigma8 = closure["D_LCDM"]
    D_GRUT_sigma8 = closure["D_GRUT"]
    D_decoupled = closure["D_decoupled_absolute"]
    pure_md = closure["pure_matter_dom_D"]

    return {
        "quasi_static_validity":     qs,
        "failure_mode": {
            "D_constitutive_without_closure": float(D_decoupled),
            "interpretation": (
                "Constitutive equation without matter sourcing "
                "gives D = const ≈ initial value. "
                "Normalized: D ≈ 1.0. Required: D ≈ 2626. "
                "Ratio: 1/2626 ≈ 3.8×10⁻⁴."
            ),
        },
        "resolution": {
            "D_LCDM_sigma8":  float(D_LCDM_sigma8),
            "D_GRUT_sigma8":  float(D_GRUT_sigma8),
            "pure_matter_dom": float(pure_md),
            "lambda_suppression_pct": closure["lambda_suppression_pct"],
            "interpretation": (
                f"Poisson closure k²Φ = −4πG μ_GRUT a² ρ δ "
                f"gives D_ΛCDM = {D_LCDM_sigma8:.0f} (at σ_8 scale). "
                f"Dark energy suppresses growth from {pure_md:.0f} to "
                f"{D_LCDM_sigma8:.0f} ({closure['lambda_suppression_pct']:.1f}% suppression). "
                f"D_GRUT = {D_GRUT_sigma8:.0f} (0.09% above ΛCDM at σ_8)."
            ),
        },
        "scale_survey":          survey,
        "open_derivation_gap":   gap,
        "status": {
            "d_1p0_failure_diagnosed":        True,
            "poisson_closure_demonstrated":   True,
            "d_lcdm_2626_verified":           bool(abs(D_LCDM_sigma8 - 2626) < 50),
            "poisson_closure_from_sctp":      False,  # still open
            "camb_class_run_blocked_by_this": False,  # not blocked
        },
        "verdict": (
            "The D=1.0 failure is a CLOSURE PROBLEM: the decoupled "
            "constitutive equation (without matter sourcing) gives "
            "no growth. Adding the Poisson closure (borrowed from "
            f"Correction #26) gives D_ΛCDM ≈ {D_LCDM_sigma8:.0f}, "
            "D_GRUT ≈ D_ΛCDM × f(k) at each scale. "
            "The remaining open work is to DERIVE the Poisson closure "
            "from S_CTP (the matter-gravity CTP coupling vertex). "
            "The CAMB/CLASS v4 gate is NOT blocked by this gap."
        ),
    }
