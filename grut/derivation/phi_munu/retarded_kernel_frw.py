"""Phase 2D (completed) — the FRW retarded kernel beyond quasi-static.

Derives GRUT's modified-gravity response on FRW *without* the quasi-static
(QS) reduction, resolving the low-ℓ CMB ISW problem at the level of the
constitutive kernel rather than a phenomenological filter.

═══════════════════════════════════════════════════════════════════════
THE PROBLEM THIS CLOSES
═══════════════════════════════════════════════════════════════════════
The QS susceptibility χ_eq(k) = 1/(1+(τ₀k_phys)²) [frw_explicit.py] gives
μ = 1+α χ_eq. Run through full Boltzmann (MGCAMB) it over-predicts the
low-ℓ CMB ISW by ~2.6× (≈29σ). The QS reduction was justified there by
(τ₀H)² ≪ 1 "at all epochs" — an ARITHMETIC ERROR: (τ₀H)²=1 at z≈77 and
≈2×10⁵ at equality. QS is valid for growth (k≳10⁻², z★≲7) but INVALID for
the low-ℓ ISW modes (k≲3×10⁻³, z★≳30). See theory/CMB_ISW_EQUALITY_FILTER.md.

═══════════════════════════════════════════════════════════════════════
THE DERIVATION (two structural forks, both settled from GRUT's own CTP)
═══════════════════════════════════════════════════════════════════════
GRUT is a memory-response theory; the fundamental object is the retarded
kernel G^R(k,η,η'), not the algebraic μ(k,a).

FORK 1 — temporal order: FIRST-ORDER (relaxation), not second-order (wave).
  • constitutive.py: the bedrock law τ dz/dt + z = z_target is first-order
    (Mori-Zwanzig), and is itself "Route 1: CTP variation."
  • noise_kernel.py: FDT noise N=(2/τ)ℏω·coth(...) is Ohmic — dissipation
    rate 1/τ, the signature of first-order friction.
  • linearized_ctp_action.py (eq. line 59): the susceptibility is the
    SINGLE-POLE χ(ω) = 1/(1 − iωτ₀) — the Fourier transform of exponential
    (first-order) relaxation.
  ⇒ The second-order operator 1+τ₀²(−□_g) in frw_explicit.py is the wrong
    covariantization: it imposed Lorentz invariance (∂_η² wave term, giving
    a spurious χ∝1/(1−ω²τ₀²)) on a medium that HAS a rest frame (cosmic
    frame). The correct covariantization of a first-order dissipative
    response is along the medium 4-velocity: 1 − iωτ₀ → 1 + τ₀ uᵘ∂ᵤ.

FORK 2 — what relaxes: the INTENSIVE susceptibility χ (n_g²=1+αχ), toward
  its scale-dependent static equilibrium χ_eq(k) = 1/(1+(τ₀k_phys)²).
  (NOT the extensive response amplitude χ·δρ_m, which would carry memory of
  the decaying past source and OVERSHOOT. χ is the susceptibility per the
  framework's own n_g²=1+αχ.) The static (ω=0) limit reproduces frw_explicit.

THE MASTER EQUATION (factorizes as χ(ω,k)=χ_eq(k)/(1−iωτ₀)):

    ┌──────────────────────────────────────────────────────────────────┐
    │  (L₀/a) ∂_η χ(k,η) + χ(k,η) = 1/(1 + (L₀ k/a)²) ,   μ = 1 + α χ   │
    └──────────────────────────────────────────────────────────────────┘

  L₀ = τ₀c ≈ 12.85 Mpc, α = 1/3, η conformal time (Mpc), k comoving (1/Mpc).
  ∂_η→0 (QS) recovers μ = 1+α/(1+(L₀k_phys)²). ZERO free parameters.

═══════════════════════════════════════════════════════════════════════
BEHAVIOUR (this module; cf. theory note §0)
═══════════════════════════════════════════════════════════════════════
The relaxation lag suppresses χ below χ_eq exactly when the equilibrium
rises faster than τ₀ allows (τ₀H ≳ 1, i.e. z ≳ 77) — the ISW-mode turn-on:
  R ≡ χ/χ_eq :  k=10⁻³ → 0.26 (z=77), 0.47 (z=50), 0.94 (z=20), 1.00 (z=0)
  Growth modes (k≳10⁻²): χ_eq≈0 at high z, R≈1 where χ_eq matters → σ₈/BAO
  intact. Today R→1 for all modes (relaxation has equilibrated).
  But the lag only DELAYS: by z≲15 χ→χ_eq=1 (μ→4/3 in full).

FULL-BOLTZMANN VERDICT (mugamma_par==5 in MGCAMB; validated: GR-limit=stock CAMB,
ratio→1 at ℓ=220, σ₈ +2.8%): the derived kernel does NOT rescue the low-ℓ CMB.
D_ℓ/D_ℓ^ΛCDM = 2.79× at ℓ=15 (~32σ) — marginally LARGER than the ad hoc f_subH
version (2.6×). vs ΛCDM the potential still deepens fully → ISW still large.
(R=χ/χ_eq<1 is suppression vs the no-filter QS value, NOT vs ΛCDM.) Source coupling
also fails: μ multiplies the gauge-invariant comoving density (already (k/aH)²-
suppressed super-horizon), but the ISW modes are genuine sub-horizon overdensities
at the sourcing epoch (k~10⁻³ enters horizon z~60) → unsuppressed source. ROOT CAUSE:
χ_eq→1 (μ→4/3) as k→0 — the large-scale dark-sector enhancement itself — over-produces
the low-ℓ ISW. HONEST VERDICT: the low-ℓ CMB falsifies GRUT's derived large-scale
linear response; σ₈/BAO/growth (k≳10⁻²) unaffected. See theory/CMB_ISW_EQUALITY_FILTER.md §0.1.
"""

from __future__ import annotations

import math
from functools import lru_cache
from typing import Dict

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d

from grut.foundation.closure_protocol import TAU_0_SEC, ALPHA_VAC

C_LIGHT_KM_S = 299792.458
L0_MPC = TAU_0_SEC * 299792458.0 / 3.0857e22      # τ₀c ≈ 12.847 Mpc

# Default ΛCDM background (Planck 2018)
_OM = 0.3153
_OL = 1.0 - _OM
_OR = 9.2e-5
_H0_OVER_C = 67.4 / C_LIGHT_KM_S                   # Mpc⁻¹


# ─────────────────────────────────────────────────────────────────────
# Background a(η) for the FRW relaxation
# ─────────────────────────────────────────────────────────────────────
@lru_cache(maxsize=4)
def _background(om=_OM, ol=_OL, orad=_OR):
    a = np.logspace(-4.7, 0.0, 6000)
    H_over_c = _H0_OVER_C * np.sqrt(om / a**3 + ol + orad / a**4)
    integrand = 1.0 / (a**2 * H_over_c)
    eta = np.concatenate([[0.0], np.cumsum(0.5 * (integrand[1:] + integrand[:-1]) * np.diff(a))])
    a_of_eta = interp1d(eta, a, bounds_error=False, fill_value=(a[0], a[-1]))
    return a, eta, a_of_eta


def chi_eq(k_Mpc: float, a: float) -> float:
    """Quasi-static (static-equilibrium) susceptibility χ_eq = 1/(1+(L₀k/a)²)."""
    return 1.0 / (1.0 + (L0_MPC * k_Mpc / a) ** 2)


def solve_chi(k_Mpc: float, om=_OM, ol=_OL, orad=_OR):
    """Solve the master equation (L₀/a)χ' + χ = χ_eq for χ(k,η).

    Returns (a_grid, chi_of_a) where chi_of_a is an interp1d in a.
    """
    a, eta, a_of_eta = _background(om, ol, orad)

    def rhs(et, y):
        aa = float(a_of_eta(et))
        return [(aa / L0_MPC) * (chi_eq(k_Mpc, aa) - y[0])]

    eta_i = eta[np.argmin(np.abs(a - 1e-4))]
    sol = solve_ivp(rhs, (eta_i, eta[-1]), [chi_eq(k_Mpc, a[np.argmin(np.abs(a - 1e-4))])],
                    method="LSODA", rtol=1e-9, atol=1e-13, dense_output=True)
    # map back to a-grid
    mask = eta >= eta_i
    chi_vals = np.empty_like(a)
    chi_vals[~mask] = chi_eq(k_Mpc, a[~mask][0] if (~mask).any() else a[0])
    chi_vals[mask] = sol.sol(eta[mask])[0]
    return a, interp1d(a, chi_vals, bounds_error=False, fill_value=(chi_vals[0], chi_vals[-1]))


def mu_eff(k_Mpc: float, a: float, alpha: float = ALPHA_VAC) -> float:
    """Derived effective μ(k,a) = 1 + α χ(k,a) from the full retarded kernel."""
    _, chi = solve_chi(k_Mpc)
    return 1.0 + alpha * float(chi(a))


def suppression_R(k_Mpc: float, a: float) -> float:
    """R = χ/χ_eq — the kernel's suppression of the QS response (1 ⇒ QS recovered)."""
    _, chi = solve_chi(k_Mpc)
    return float(chi(a)) / chi_eq(k_Mpc, a)


# ─────────────────────────────────────────────────────────────────────
# Verification
# ─────────────────────────────────────────────────────────────────────
def verify() -> Dict[str, bool]:
    """Self-test the derived kernel.

      (1) QS recovered today (R→1) for all modes.
      (2) Growth modes (k≳1e-2) ≈ QS where χ_eq matters (z<5).
      (3) ISW modes (k=1e-3) strongly suppressed during turn-on (z~50-77).
      (4) τ₀→0 (QS) limit: χ → χ_eq everywhere.
    """
    def R(k, z):
        return suppression_R(k, 1.0 / (1.0 + z))

    leg1 = all(abs(R(k, 0.0) - 1.0) < 0.02 for k in (1e-3, 1e-2, 0.1))
    leg2 = abs(R(0.1, 3.0) - 1.0) < 0.05               # growth mode ~QS at z=3
    leg3 = R(1e-3, 50.0) < 0.6 and R(1e-3, 77.0) < 0.4  # ISW mode suppressed at turn-on

    # (4) τ₀→0 limit: scale L0 down by 1e-3 → χ tracks χ_eq (R≈1 even at z=77)
    global L0_MPC
    _save = L0_MPC
    try:
        L0_MPC = _save * 1e-3
        solve_chi.cache_clear() if hasattr(solve_chi, "cache_clear") else None
        a, chi = solve_chi(1e-3)
        leg4 = abs(float(chi(1.0 / 78.0)) / (1.0 / (1.0 + (_save * 1e-3 * 1e-3 * 78.0) ** 2)) - 1.0) < 0.05
    finally:
        L0_MPC = _save
    return {
        "qs_recovered_today":            bool(leg1),
        "growth_modes_match_qs":         bool(leg2),
        "isw_modes_suppressed_at_turnon": bool(leg3),
        "qs_limit_as_tau0_to_zero":      bool(leg4),
    }


if __name__ == "__main__":
    print(f"L0 = τ₀c = {L0_MPC:.4f} Mpc,  α = {ALPHA_VAC:.4f}")
    print("\nDerived kernel R=χ/χ_eq (1 ⇒ QS; <1 ⇒ suppressed):")
    print(f"{'k[1/Mpc]':>10}  z=0    z=20   z=50   z=77")
    for k in (1e-3, 3e-3, 1e-2, 0.1):
        vals = [suppression_R(k, 1.0 / (1.0 + z)) for z in (0, 20, 50, 77)]
        print(f"{k:10.0e}  " + "  ".join(f"{v:.3f}" for v in vals))
    print("\nverify():", verify())
