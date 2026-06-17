"""CMB low-ℓ ISW *amplitude* for GRUT — validated line-of-sight pipeline.

═══════════════════════════════════════════════════════════════════════
PURPOSE  (front #1: "turn the certified ISW direction into an amplitude")
═══════════════════════════════════════════════════════════════════════

`cmb_isw.py` certifies the *direction* of GRUT's low-ℓ ISW (the reduced
potential Φ̃ history) but explicitly defers the *amplitude*:
"Full D_ℓ requires MGCAMB Boltzmann integration."  This module computes
that amplitude with a transparent, fully-validated line-of-sight method —
no Fortran black box, every step auditable and cross-checked against CAMB.

ARCHITECTURE (differential, anchored to CAMB's exact ΛCDM)
---------------------------------------------------------
    C_ℓ^GRUT = (2/π)∫ k² dk 𝒫_R(k) |Θ_ℓ^ΛCDM(k) + ΔΘ_ℓ(k)|²

  • Θ_ℓ^ΛCDM(k)  : CAMB's EXACT temperature transfer (0.1%-accurate).
  • ΔΘ_ℓ(k)      : the GRUT differential ISW transfer, computed here as
                     ΔΘ_ℓ(k) = ∫_η dη  d/dη[(Φ+Ψ)_ΛCDM (r−1)]  j_ℓ(k(η₀−η))
  • (Φ+Ψ)_GRUT  = (Φ+Ψ)_ΛCDM × r(k,η), with the potential RATIO
                     r(k,a) = μ(k,a) · δ_GRUT(k,a)/δ_ΛCDM(k,a)
                   taken from the modified linear-growth ODE.  Using a
                   *ratio* makes the result insensitive to the simplified
                   ODE's absolute-shape errors (radiation, ICs): those
                   cancel between GRUT and ΛCDM.
  • The SW×ISW cross-term is handled EXACTLY because Θ_ℓ^ΛCDM is exact.

CRITICAL PHYSICS FIX (vs cmb_isw.py / modified_growth.py)
---------------------------------------------------------
The growth ODE in modified_growth.py uses the UNFILTERED Poisson source
μ = 1 + α/(1+(τ₀ k_phys)²).  Applied to near-/super-horizon modes
(k ≲ aH) this spuriously over-enhances the potential, because the
sub-horizon Newtonian growth equation is invalid there.  GRUT's canonical
prescription (the native-CAMB injection, "Axiom A1") instead carries the
sub-Hubble filter

    μ(k,a) = 1 + f_subH(k,a) · α / (1 + (τ₀c · k/a)²),
    f_subH(k,a) = (k/aH)² / (1 + (k/aH)²)   →  1 sub-horizon, → 0 super-horizon

This module uses the FILTERED μ (consistent with the native injection).
cmb_isw.py's headline ratio Φ̃_GRUT/Φ̃_ΛCDM = 2.64× is the *unfiltered*
over-estimate and should not be read as the physical amplitude.

═══════════════════════════════════════════════════════════════════════
VALIDATION CHAIN  (see tests/derived/test_isw_amplitude.py)
═══════════════════════════════════════════════════════════════════════
  (V1) k-integral / normalization: reconstructing C_ℓ from CAMB's own
       transfer reproduces CAMB's C_ℓ to 0.1% over ℓ=2–30.            ✓
  (V2) ISW projection: SW(=⅓Ψ_rec j_ℓ) + ISW(=∫(Φ+Ψ)' j_ℓ) rebuilt
       from CAMB's own Weyl matches CAMB's exact transfer to ~13% at
       ℓ=2 (rising to ~25% by ℓ=10 as the ⅓Ψ SW approximation and the
       neglected Doppler term bite).  These systematics are IDENTICAL
       for GRUT and ΛCDM (recombination SW unchanged, μ(z=1100)≈1.002)
       and cancel in the differential ΔΘ.                            ✓
  (V3) growth ratio r matches the analytic growing-mode exponent
       p₊(μ) and cmb_isw.py's documented Φ̃ evolution.                ✓

═══════════════════════════════════════════════════════════════════════
⚠ SUPERSEDED RESULT — read this first
═══════════════════════════════════════════════════════════════════════
This approximate line-of-sight module returned D_ℓ^GRUT/D_ℓ^ΛCDM ≈ 5–11
across ℓ=2–30.  THAT NUMBER IS A CONTAMINATION ARTIFACT and must not be
quoted.  It used `import camb` from the project default, which is the
GRUT-MODIFIED fork at ~/camb_grut (μ_GRUT hardcoded always-on in
equations.f90 ~L2244–2272).  So the "ΛCDM base" transfer here was already
GRUT-modified, and the differential double-counted.  True stock ΛCDM at
ℓ=2 is D₂≈1024 (CAMB 1.5.8 PyPI), not the fork's 1714.

DEFINITIVE RESULT (full relativistic MGCAMB, μ,γ=1; see
theory/CMB_ISW_EQUALITY_FILTER.md and ~/mgcamb_grut):
  • Naive GRUT (instantaneous f_subH = (k/aH)²):  D_ℓ ratio peaks at
    2.61× at ℓ≈16 → ~29σ cosmic-variance tension, wrong sign vs Planck.
  • With the equality-scale quasi-static filter f_eq=(k/k_eq)²/(1+(k/k_eq)²),
    k_eq=0.073 Ω_m h²≈0.0104 Mpc⁻¹ (ZERO free parameters):  D_ℓ ratio
    0.99–1.00 across ℓ=2–30 (CMB tension removed), σ₈ +2.8%, BAO intact.
  MGCAMB GR-limit reproduces stock CAMB exactly (validated); the 2.61×
  is numerically bulletproof and corroborated by the ~/camb_grut fork.

PHYSICS: GRUT's μ is a quasi-static, sub-horizon response.  The
instantaneous f_subH uses the *current* horizon and wrongly admits
near-horizon modes (k~10⁻³) where QS fails.  Requiring the response to
hold throughout matter domination → reference scale = equality horizon
k_eq.  See the theory note.

RESOLVED (Correction #38, June 2026): the k_eq filter has NO derivable
CTP/memory-kernel basis — the ISW-driving modes are fully sub-horizon at
the sourcing epoch, so no causal cutoff is derivable, and the full
retarded kernel does NOT rescue the linear branch (2.79×/32σ). The "ZERO
free parameters" framing above is therefore moot: the filter is a
post-hoc screening, now RETIRED (a domain-boundary marker, not a
GRUT-derived screening). The honest resolution is not a filter —
linear cosmology = ΛCDM (μ_linear = 1 forced; see
theory/PROJECTOR_CONSISTENCY_NOGO.md §5).

This module is retained only as a transparent line-of-sight cross-check;
the numbers below are NOT the GRUT prediction.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from functools import lru_cache
from typing import Dict, Tuple

import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import spherical_jn

from grut.derivation.phi_munu.modified_growth import (
    Omega_m_of_a,
    TAU_0_SEC,
    ALPHA_VAC,
    C_LIGHT_M_S,
    MPC_IN_M,
)

# ─────────────────────────────────────────────────────────────────────
# Fixed Planck-2018 background (TT+TE+EE+lowE+lensing, Table 2)
# ─────────────────────────────────────────────────────────────────────
PLANCK_H0 = 67.4
PLANCK_OMBH2 = 0.02237
PLANCK_OMCH2 = 0.1200
PLANCK_TAU = 0.0544
PLANCK_AS = 2.101e-9
PLANCK_NS = 0.9649
PLANCK_MNU = 0.06
K_PIVOT = 0.05            # Mpc⁻¹  (CAMB default scalar pivot)
T_CMB_MUK = 2.7255e6      # μK

# Derived background scalars
_H0_OVER_C = PLANCK_H0 / (C_LIGHT_M_S / 1000.0)   # Mpc⁻¹  (H0/c)
TAU0_C_MPC = TAU_0_SEC * C_LIGHT_M_S / MPC_IN_M    # ≈ 12.85 Mpc
_OMEGA_M = (PLANCK_OMBH2 + PLANCK_OMCH2 + PLANCK_MNU / 93.14) / (PLANCK_H0 / 100.0) ** 2
_OMEGA_L = 1.0 - _OMEGA_M

# Growth-ODE start (deep matter domination)
_A_INIT = 3e-4


# ─────────────────────────────────────────────────────────────────────
# GRUT modified-gravity μ with the Axiom-A1 sub-Hubble filter
# ─────────────────────────────────────────────────────────────────────
def _aH_Mpc(a: float) -> float:
    """Comoving Hubble rate aH(a) in Mpc⁻¹ for the Planck ΛCDM background."""
    return _H0_OVER_C * a * math.sqrt(_OMEGA_M / a**3 + _OMEGA_L)


def f_subH(k_Mpc: float, a: float) -> float:
    """Sub-Hubble (causal) filter f_subH = (k/aH)²/(1+(k/aH)²) — Axiom A1.

    → 1 deep sub-horizon (k≫aH);  → 0 super-horizon (k≪aH).
    """
    x = (k_Mpc / _aH_Mpc(a)) ** 2
    return x / (1.0 + x)


def mu_grut(k_Mpc: float, a: float) -> float:
    """Filtered GRUT modified-gravity function (matches the native injection).

        μ(k,a) = 1 + f_subH(k,a) · α_vac / (1 + (τ₀c · k/a)²)
    """
    k_phys = k_Mpc / a
    return 1.0 + f_subH(k_Mpc, a) * ALPHA_VAC / (1.0 + (TAU0_C_MPC * k_phys) ** 2)


# ─────────────────────────────────────────────────────────────────────
# Modified linear-growth ODE (e-fold time), fixed Planck background
# ─────────────────────────────────────────────────────────────────────
def _growth_rhs(N: float, y, k_Mpc: float, use_mu: bool):
    a = math.exp(N)
    Om = Omega_m_of_a(a, _OMEGA_M, _OMEGA_L)
    mu = mu_grut(k_Mpc, a) if use_mu else 1.0
    delta, dprime = y
    return [dprime, -(2.0 - 1.5 * Om) * dprime + 1.5 * Om * mu * delta]


def potential_ratio(k_Mpc: float, a_grid: np.ndarray) -> np.ndarray:
    """Potential ratio r(k,a) = μ(k,a)·δ_GRUT/δ_ΛCDM on a_grid.

    Both ODEs share the Planck background and identical ICs, so the
    simplified-physics errors cancel in the ratio (V3).  r → 1 at early
    times and for sub-transition k (k ≳ 0.1 Mpc⁻¹).
    """
    if k_Mpc > 0.2:                       # GRUT modification negligible
        return np.ones_like(a_grid)
    N = np.log(a_grid)
    common = dict(method="RK45", rtol=1e-7, atol=1e-9, dense_output=True)
    sg = solve_ivp(_growth_rhs, (math.log(_A_INIT), 0.0), [1.0, 1.0],
                   args=(k_Mpc, True), **common)
    sl = solve_ivp(_growth_rhs, (math.log(_A_INIT), 0.0), [1.0, 1.0],
                   args=(k_Mpc, False), **common)
    mu = np.array([mu_grut(k_Mpc, a) for a in a_grid])
    return mu * sg.sol(N)[0] / sl.sol(N)[0]


# ─────────────────────────────────────────────────────────────────────
# CAMB ΛCDM base (cached): transfer Θ_ℓ(k), Weyl(k,η), background timing
# ─────────────────────────────────────────────────────────────────────
@dataclass
class _CambBase:
    k: np.ndarray            # transfer k-grid (Mpc⁻¹)
    L: np.ndarray            # multipoles
    Theta: np.ndarray        # (nL, nk) ΛCDM temperature transfer, per-R
    PR: np.ndarray           # primordial 𝒫_R(k) on the k-grid
    eta0: float              # conformal time today (Mpc)
    eta: np.ndarray          # ascending conformal-time grid (Mpc)
    a: np.ndarray            # scale factor on eta grid
    src_lcdm: np.ndarray     # (nk, nη) (Φ+Ψ)_ΛCDM / R from CAMB Weyl


@lru_cache(maxsize=1)
def _camb_base(lmax: int = 60, nz_late: int = 200, nz_mid: int = 80) -> _CambBase:
    import camb
    pars = camb.CAMBparams()
    pars.set_cosmology(H0=PLANCK_H0, ombh2=PLANCK_OMBH2, omch2=PLANCK_OMCH2,
                       tau=PLANCK_TAU, mnu=PLANCK_MNU,
                       neutrino_hierarchy="degenerate")
    pars.InitPower.set_params(As=PLANCK_AS, ns=PLANCK_NS, r=0)
    pars.set_for_lmax(lmax, lens_potential_accuracy=0)
    res = camb.get_results(pars)

    td = res.get_cmb_transfer_data("scalar")
    k = td.q.copy()
    L = np.array(td.L)
    Theta = td.delta_p_l_k[0].copy()                  # temperature, per-R
    PR = PLANCK_AS * (k / K_PIVOT) ** (PLANCK_NS - 1.0)

    eta0 = res.conformal_time(0.0)
    # z-grid: clean matter+DE regime (z<200); GRUT differential vanishes above.
    zg = np.unique(np.concatenate([
        np.linspace(200.0, 30.0, nz_mid),
        np.linspace(29.5, 0.0, nz_late)]))[::-1]
    etaz = np.array([res.conformal_time(z) for z in zg])
    order = np.argsort(etaz)
    eta = etaz[order]
    a = (1.0 / (1.0 + zg))[order]
    ev = res.get_redshift_evolution(k, zg, ["Weyl"])  # (nk,nz,1): k²(Φ+Ψ)/2 per R
    src = 2.0 * ev[:, :, 0] / (k[:, None] ** 2)        # (Φ+Ψ)/R
    src = src[:, order]

    return _CambBase(k=k, L=L, Theta=Theta, PR=PR, eta0=eta0,
                     eta=eta, a=a, src_lcdm=src)


# ─────────────────────────────────────────────────────────────────────
# GRUT differential ISW transfer and the C_ℓ comparison
# ─────────────────────────────────────────────────────────────────────
def _differential_transfer(base: _CambBase) -> np.ndarray:
    """ΔΘ_ℓ(k) = ∫ d/dη[(Φ+Ψ)_ΛCDM (r−1)] · j_ℓ(k(η₀−η)) dη."""
    nk, nz = base.src_lcdm.shape
    r = np.ones((nk, nz))
    for ik, kk in enumerate(base.k):
        r[ik] = potential_ratio(float(kk), base.a)
    ddiff = np.gradient(base.src_lcdm * (r - 1.0), base.eta, axis=1)
    x = base.k[:, None] * (base.eta0 - base.eta)[None, :]
    dTheta = np.empty((len(base.L), nk))
    for li, l in enumerate(base.L):
        dTheta[li] = np.trapezoid(ddiff * spherical_jn(int(l), x), base.eta, axis=1)
    return dTheta


def _Dl(Cl: np.ndarray, L: np.ndarray) -> np.ndarray:
    return L * (L + 1) / (2.0 * np.pi) * Cl * T_CMB_MUK**2


def isw_amplitude(lmax: int = 30) -> Dict:
    """Full validated GRUT low-ℓ ISW amplitude prediction.

    Returns a dict with per-ℓ ΛCDM and GRUT D_ℓ (μK²), the ratio, and the
    auto/cross decomposition, plus a top-level verdict.
    """
    base = _camb_base()
    lnk = np.log(base.k)
    dTheta = _differential_transfer(base)

    rows = []
    for li, l in enumerate(base.L):
        if l > lmax:
            break
        Cl = 4 * np.pi * np.trapezoid(base.PR * base.Theta[li] ** 2, lnk)
        cross = 4 * np.pi * np.trapezoid(base.PR * 2 * base.Theta[li] * dTheta[li], lnk)
        auto = 4 * np.pi * np.trapezoid(base.PR * dTheta[li] ** 2, lnk)
        Clg = Cl + cross + auto
        f = T_CMB_MUK**2 * l * (l + 1) / (2 * np.pi)
        rows.append({
            "ell": int(l),
            "D_lcdm_muK2": Cl * f,
            "D_grut_muK2": Clg * f,
            "ratio": float(Clg / Cl),
            "cross_pct": float(100 * cross / Cl),
            "auto_pct": float(100 * auto / Cl),
        })

    ratios = np.array([r["ratio"] for r in rows])
    return {
        "method": "validated line-of-sight differential ISW (CAMB-anchored)",
        "background": "Planck 2018 fixed (H0=67.4, Ωm=%.4f)" % _OMEGA_M,
        "mu_prescription": "filtered (Axiom A1 sub-Hubble), matches native injection",
        "per_ell": rows,
        "ratio_min": float(ratios.min()),
        "ratio_max": float(ratios.max()),
        "verdict": (
            "⚠ CONTAMINATED CROSS-CHECK — do not quote. This pipeline's "
            "ΛCDM base is the GRUT-modified ~/camb_grut fork, so the %.1f–%.1f× "
            "here double-counts. DEFINITIVE (MGCAMB, see theory/"
            "CMB_ISW_EQUALITY_FILTER.md): naive GRUT 2.6× peak (~29σ); with the "
            "zero-parameter equality-scale filter k_eq=0.073 Ωm h², D_ℓ ratio "
            "0.99–1.00 (CMB consistent) and σ₈ +2.8%."
            % (ratios.min(), ratios.max())
        ),
    }


if __name__ == "__main__":
    out = isw_amplitude()
    print(out["method"], "|", out["background"])
    print(out["mu_prescription"])
    print(f"\n{'ℓ':>3} {'D_ΛCDM':>9} {'D_GRUT':>9} {'ratio':>7} {'cross%':>8} {'auto%':>8}")
    for r in out["per_ell"]:
        print(f"{r['ell']:3d} {r['D_lcdm_muK2']:9.1f} {r['D_grut_muK2']:9.1f} "
              f"{r['ratio']:7.2f} {r['cross_pct']:+8.1f} {r['auto_pct']:8.1f}")
    print("\n" + out["verdict"])
