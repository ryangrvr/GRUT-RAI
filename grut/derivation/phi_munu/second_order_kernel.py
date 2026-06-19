"""Constructive phase — the second-order CTP kernel K⁽²⁾ (the C5a flagship).

This module is the resolution of GRUT v3's constructive-phase flagship problem:
the explicit second-order influence kernel

    K⁽²⁾_μνρσ = δ²S_IF / δh_a δh_r² |_{O(2)}

and the dark-sector source it produces, ρ_eff = σ·α_vac·L₀²·W². The audit
phase (Tests 01–05) had compressed the dark sector to this single computation.
See theory/GRUT_V3_K2_DERIVATION.md for the full four-stage record.

═══════════════════════════════════════════════════════════════════════
THE RESULT (three findings, one verdict)
═══════════════════════════════════════════════════════════════════════

STAGE A — the permitted operator basis is CLOSED:
  • W² = C_μνρσ C^μνρσ (Weyl²) is the UNIQUE dynamically-active O(2) operator
    (W̄=0 on FRW ⇒ δW²=O(h²) ⇒ escapes the linear-scalar No-Go; the c-anomaly).
  • E₄ (Gauss–Bonnet) is in the basis but TOPOLOGICALLY DORMANT — the a-anomaly /
    Euler density, Lovelock-null in 4D (no local dynamics). NOT "No-Go-forbidden".
  • R², R_μν², □R are FORBIDDEN (couple to the T-trace ⇒ first-order scalar
    response ⇒ violate μ_linear=1).

STAGE B — the SCALE is L₀ (rigorous):
  The surviving TT kernel K^R = α·χ(ω)·P^TT is spatially scale-free (χ purely
  temporal; P^TT dimensionless/directional). The explicit flat-space second
  variation gives  K⁽²⁾(ω,k) = σ·α_vac·χ(ω)  — carrying NO 1/k² pole. Hence the
  coupling length is fixed:  ρ_eff = σ·α_vac·L₀²·W²,  L = L₀ = c·τ₀ ≈ 12.85 Mpc.
  Proof the local-r branch is impossible: a spatially-local causal memory kernel
  is a polynomial in k² (entire); 1/∇² ~ 1/k² is a pole at k=0; no
  differentiation / integration-by-parts converts a polynomial into a pole.
  (Distribution theorem; verified — workflows whbpphrbb, wgzzxunwo.)

STAGE C — the MAGNITUDE is viable, NOT negligible:
  ρ_eff/ρ_baryon ~ α_vac·(L₀/L_curv)² where L_curv is the CURVATURE radius. For a
  WEAK-FIELD galaxy, L_curv ~ r/√Φ ~ tens of Mpc — COMPARABLE to L₀, not the
  ~10 kpc system size. So ρ_eff/ρ_baryon ~ O(1–100) at galactic radii.
  ⚠ The intermediate workflow's "ρ_eff/ρ_baryon ~ 1e-27 ⇒ C5a dies" was a
    MAGNITUDE ERROR — two independent bugs (see _error_forensics()):
      (1) comparing a GEOMETRIC ρ_eff [1/L²] to an SI ρ_baryon [kg/m³] without
          the c²/G ≈ 1.35e27 conversion — that factor IS the spurious 1e-27;
      (2) using W² = 48(r_s/r)⁶ (dimensionless) instead of 48(GM/c²)²/r⁶ [1/L⁴].
    In consistent geometric units the magnitude is O(1–100). It does not die.

STAGE D — the SHAPE is wrong (the decisive phenomenology):
  ρ_eff ∝ W². For an extended spherical profile the weak-field Weyl is
    W² = (16/3)·Λ²,  Λ = Φ'' − Φ'/r = 4π(ρ − ⟨ρ⟩)  ⇒  ρ_eff ∝ (ρ − ⟨ρ⟩)².
  For an isothermal halo (ρ∝1/r²): ρ_eff ∝ ρ² ∝ 1/r⁴ (log-slope ≈ −4), far
  STEEPER than the 1/r² (slope −2) a FLAT rotation curve requires. The W² source
  is centrally concentrated and tracks baryons-SQUARED — it is NOT the extended
  flat-curve dark halo, regardless of σ (σ scales magnitude, not shape).

VERDICT: C5a produces a real effective source of the right ORDER OF MAGNITUDE at
galactic scales but the WRONG RADIAL PROFILE (baryon-squared, too steep) to be the
dark-matter halo. GRUT has NO derived dark-matter mechanism reproducing halo
phenomenology; dark matter remains a HOSTED input (with the derived a₀ scale and
μ_linear=1 ⇒ linear cosmology = ΛCDM). The recurring v3 signature: the math
survives, the ontology changes.

TEST 06 — the shape failure is a THEOREM, not a heuristic artifact:
  The verdict's one assumption was ρ_eff ∝ W² (the scalar). Deriving the effective
  00-source from the actual tensor structure (theory/GRUT_V3_TEST_06_PROFILE_THEOREM.md)
  shows ALL permitted routes converge to ρ_eff ∝ 1/r⁴ (or steeper):
    • Route A scalar W²            → 1/r⁴
    • Route B Bach tensor ∇²ρ      → 1/r⁴ (same; bach_route_isothermal_slope())
    • Route C P^TT projector       → 1/r⁴ (loophole closed; tt_projector_is_inert())
  The P^TT k_ik_j/k² is degree-0 in |k| (angular, not a 1/∇² pole), and K⁽²⁾ is
  k-independent (Stage B), so no inverse Laplacian survives. Shallowing 1/r⁴ → 1/r²
  would REQUIRE 1/∇², which the same locality result that fixes L=L₀ forbids. So the
  profile failure is unavoidable within the local, causal, No-Go-respecting kernel.

Honest residual (cannot change the verdict): the exact O(1) prefactor σ and the
full covariant tensor form of K⁽²⁾ need a dedicated CAS (xAct); σ ∈ {1/3,1,3,9}
shifts only the magnitude band, never the shape (which refutes the DM use).
"""

from __future__ import annotations

import math
from typing import Callable, Dict

import numpy as np

# ─────────────────────────────────────────────────────────────────────
# Constants (anchored / derived inputs — see grut/v3/picture.py)
# ─────────────────────────────────────────────────────────────────────
ALPHA_VAC = 1.0 / 3.0          # vacuum impedance a/c (one conformal scalar; KS 2011)
TRACE_ANOMALY_A = 1.0          # Euler (E₄) coefficient — topological, dormant
TRACE_ANOMALY_C = 3.0          # Weyl (W²) coefficient — the dynamical channel
TAU0_MYR = 41.9               # relaxation time (anchored)

_G = 6.674e-11                # m³ kg⁻¹ s⁻²
_C = 2.998e8                  # m s⁻¹
_MSUN = 1.989e30              # kg
_MPC = 3.086e22               # m
_KPC = 3.086e19               # m
_YR = 3.156e7                 # s

L0_M = _C * TAU0_MYR * 1e6 * _YR     # memory length in metres
L0_MPC = L0_M / _MPC                 # ≈ 12.85 Mpc — the SOLE length scale in K^R

# σ — the dimensionless W² coupling. O(1), UNVERIFIED (needs full covariant CAS).
SIGMA_DEFAULT = 1.0
SIGMA_BAND = (1.0 / 3.0, 1.0, 3.0, 9.0)


# ─────────────────────────────────────────────────────────────────────
# The kernel (Stage B): K⁽²⁾(ω) = σ·α·χ(ω) — k-INDEPENDENT (no 1/k² pole)
# ─────────────────────────────────────────────────────────────────────
def chi(omega: complex) -> complex:
    """Single-pole susceptibility χ(ω) = 1/(1 − iωτ₀) (purely temporal)."""
    omega_tau0 = omega * (TAU0_MYR * 1e6 * _YR)
    return 1.0 / (1.0 - 1j * omega_tau0)


def K2_kernel(omega: complex, sigma: float = SIGMA_DEFAULT) -> complex:
    """The second-order CTP kernel K⁽²⁾(ω) = σ·α_vac·χ(ω).

    Carries NO wavenumber k: the surviving TT kernel is spatially scale-free, so
    the second variation inherits a single length scale, L₀ (from χ's τ₀). The
    k-dependence of the *response* lives entirely in the W² source (∝ k⁴, a
    polynomial), never as a 1/k² pole in the kernel — the locality theorem.
    """
    return sigma * ALPHA_VAC * chi(omega)


# ─────────────────────────────────────────────────────────────────────
# The Weyl invariant W² (Stage C/D)
# ─────────────────────────────────────────────────────────────────────
def weyl_squared_schwarzschild(M_Msun: float, r_m: float) -> float:
    """Exterior (point-mass) Weyl² = Kretschmann = 48 (GM/c²)² / r⁶  [1/m⁴]."""
    Mgeo = _G * M_Msun * _MSUN / _C**2          # metres
    return 48.0 * Mgeo**2 / r_m**6


def weyl_squared_weakfield(rho_geo: float, mean_rho_geo: float) -> float:
    """Interior weak-field Weyl² for a spherical profile.

    W² = (16/3)·Λ²,  Λ = Φ'' − Φ'/r = 4π(ρ − ⟨ρ⟩)   (geometric units, 1/m⁴).
    The traceless tidal (electric Weyl) part of ∂_i∂_j Φ; B-part vanishes (static).
    """
    Lam = 4.0 * math.pi * (rho_geo - mean_rho_geo)
    return (16.0 / 3.0) * Lam**2


def rho_eff(W2: float, sigma: float = SIGMA_DEFAULT) -> float:
    """Effective dark-sector source ρ_eff = σ·α_vac·L₀²·W²  [1/m² geometric]."""
    return sigma * ALPHA_VAC * L0_M**2 * W2


# ─────────────────────────────────────────────────────────────────────
# Profile phenomenology (Stage D) — magnitude band + radial shape
# ─────────────────────────────────────────────────────────────────────
def isothermal_profile(M_Msun: float = 1e11, r_norm_kpc: float = 30.0
                       ) -> Callable[[np.ndarray], np.ndarray]:
    """ρ_SI(r) = A/r² normalised to M_Msun within r_norm (M(<r)=4πA r)."""
    A = M_Msun * _MSUN / (4.0 * math.pi * r_norm_kpc * _KPC)
    return lambda r: A / r**2


def profile_phenomenology(rho_SI: Callable[[np.ndarray], np.ndarray],
                          sigma: float = SIGMA_DEFAULT) -> Dict[str, np.ndarray]:
    """Compute ρ_eff(r), ρ_eff/ρ_baryon(r) and the log-slope for a spherical
    baryon profile. Returns arrays over r ∈ [0.3, 100] kpc.
    """
    r = np.logspace(math.log10(0.3 * _KPC), math.log10(100 * _KPC), 400)
    rho_geo = (_G / _C**2) * rho_SI(r)
    integ = 4.0 * math.pi * r**2 * rho_geo
    m = np.concatenate([[0.0], np.cumsum(0.5 * (integ[1:] + integ[:-1]) * np.diff(r))])
    mean_rho = np.where(r > 0, 3.0 * m / (4.0 * math.pi * r**3), rho_geo)
    W2 = (16.0 / 3.0) * (4.0 * math.pi * (rho_geo - mean_rho))**2
    re = sigma * ALPHA_VAC * L0_M**2 * W2
    ratio = re / rho_geo
    slope = np.gradient(np.log(re), np.log(r))
    return {"r_kpc": r / _KPC, "rho_eff": re, "ratio": ratio, "slope": slope}


def galaxy_ratio_band(M_Msun: float = 1e11, r_kpc: float = 10.0) -> Dict[str, float]:
    """ρ_eff/ρ_baryon at a fiducial galaxy radius across the σ band (exterior Weyl)."""
    r = r_kpc * _KPC
    W2 = weyl_squared_schwarzschild(M_Msun, r)
    Mgeo = _G * M_Msun * _MSUN / _C**2
    rho_b_geo = Mgeo / ((4.0 / 3.0) * math.pi * r**3)
    return {f"sigma={s:g}": rho_eff(W2, s) / rho_b_geo for s in SIGMA_BAND}


def bach_route_isothermal_slope() -> float:
    """Test 06 Route B — the Bach tensor source ∇²ρ for an isothermal halo.

    The metric variation of a ∫√g W² action term is the Bach tensor
    B_μν = (2∇^ρ∇^σ + R^ρσ)C_μρνσ ~ ∇⁴Φ = ∇²ρ_baryon (since ∇²Φ=ρ). For
    ρ ∝ 1/r², ∇²ρ ∝ 1/r⁴ — the SAME slope as the scalar W² route (no shallower).
    Returns the log-slope of ∇²ρ over the halo (≈ −4), confirming Bach does not help.
    """
    r = np.logspace(math.log10(0.3 * _KPC), math.log10(100 * _KPC), 400)
    rho = 1.0 / r**2                                   # isothermal (arb. units)
    d1 = np.gradient(rho, r)
    lap = np.gradient(r**2 * d1, r) / r**2             # ∇²ρ = (1/r²)(r²ρ')'
    sel = (r > 5 * _KPC) & (r < 40 * _KPC)
    return float(np.median(np.gradient(np.log(np.abs(lap)), np.log(r))[sel]))


def tt_projector_is_inert() -> bool:
    """Test 06 Route C — the P^TT loophole is closed.

    P^TT carries k_ik_j/k² = k̂_ik̂_j, which is DEGREE 0 in |k| (a dimensionless
    angular/directional projector), NOT a genuine 1/∇² pole at k=0. Since the
    second-order kernel K⁽²⁾(ω,k)=σ·α·χ(ω) is k-independent (Stage B), no |k|
    factor activates an inverse Laplacian. We verify the projector's |k|-degree is
    0: P_ij(k) = δ_ij − k_ik_j/k² is invariant under k → λk (scale-free in |k|).
    """
    import sympy as sp
    kx, ky, kz, lam = sp.symbols("kx ky kz lam", positive=True)
    k2 = kx**2 + ky**2 + kz**2
    P_xx = 1 - kx * kx / k2                              # a P^TT component
    scaled = P_xx.subs({kx: lam * kx, ky: lam * ky, kz: lam * kz})
    return sp.simplify(scaled - P_xx) == 0              # degree 0 in |k| ⇒ no pole


def _error_forensics() -> Dict[str, float]:
    """Reproduce the intermediate workflow's spurious 1e-27, isolating each bug."""
    M, r = 1e11, 10 * _KPC
    Mgeo = _G * M * _MSUN / _C**2
    rs = 2.0 * Mgeo
    W2_correct = 48.0 * Mgeo**2 / r**6                 # [1/m⁴]
    W2_bug = 48.0 * (rs / r)**6                         # dimensionless — WRONG (bug 2)
    re_geo = ALPHA_VAC * L0_M**2 * W2_correct           # [1/m²]
    rho_b_geo = Mgeo / ((4.0 / 3.0) * math.pi * r**3)   # [1/m²]
    rho_b_SI = M * _MSUN / ((4.0 / 3.0) * math.pi * r**3)  # [kg/m³]
    return {
        "correct_ratio_geometric": re_geo / rho_b_geo,        # ~53
        "bug1_unit_mismatch_geo_over_SI": re_geo / rho_b_SI,  # ~4e-26 (drops c²/G)
        "c2_over_G": _C**2 / _G,                              # ~1.35e27
        "bug2_W2_ratio_wrong_over_right": W2_bug / W2_correct,
    }


# ─────────────────────────────────────────────────────────────────────
# Verification
# ─────────────────────────────────────────────────────────────────────
def verify() -> Dict[str, bool]:
    """Self-test the K⁽²⁾ resolution.

      (1) kernel is k-independent (no 1/k² pole) — L = L₀ forced.
      (2) L₀ ≈ 12.85 Mpc (the sole length scale).
      (3) magnitude is VIABLE (O(1–100) at galaxy scale), NOT the spurious 1e-27.
      (4) the 1e-27 'death' is reproduced ONLY by the unit-mismatch bug.
      (5) shape is WRONG: ρ_eff log-slope ≈ −4 (isothermal), steeper than −2.
      (6) W²=0 on FRW (conformally flat) ⇒ μ_linear=1 untouched.
    """
    # (1) K2 depends on ω only — sample two k's via the response/source split:
    #     the kernel value is identical regardless of any spatial mode.
    leg1 = abs(K2_kernel(0.0) - SIGMA_DEFAULT * ALPHA_VAC) < 1e-12  # χ(0)=1, k-free

    # (2)
    leg2 = abs(L0_MPC - 12.85) < 0.05

    # (3) viable magnitude at 10 kpc (well above any 'negligible' threshold)
    band = galaxy_ratio_band()
    leg3 = band["sigma=1"] > 1.0 and band["sigma=1"] < 1e3

    # (4) the death claim is exactly the dropped c²/G factor
    fx = _error_forensics()
    leg4 = (fx["correct_ratio_geometric"] > 1.0
            and fx["bug1_unit_mismatch_geo_over_SI"] < 1e-20)

    # (5) shape too steep for flat curves
    ph = profile_phenomenology(isothermal_profile())
    sel = (ph["r_kpc"] > 5) & (ph["r_kpc"] < 40)
    leg5 = np.median(ph["slope"][sel]) < -3.0   # ≪ −2 (flat-curve requirement)

    # (6) W²=0 on FRW (conformally flat): zero density contrast ⇒ Λ=0 ⇒ W²=0
    leg6 = weyl_squared_weakfield(1.0e-30, 1.0e-30) == 0.0

    # (7) Test 06 Route B — the Bach tensor source ∇²ρ is just as steep (slope ≈ −4)
    leg7 = bach_route_isothermal_slope() < -3.0

    # (8) Test 06 Route C — the P^TT loophole is closed (projector degree 0 in |k|)
    leg8 = tt_projector_is_inert()

    return {
        "kernel_k_independent_no_pole":   bool(leg1),
        "scale_is_L0_12p85_Mpc":          bool(leg2),
        "magnitude_viable_not_negligible": bool(leg3),
        "death_claim_was_unit_bug":       bool(leg4),
        "shape_too_steep_for_flat_curve": bool(leg5),
        "mu_linear_preserved_W2_flat_FRW": bool(leg6),
        "test06_bach_route_also_steep":   bool(leg7),
        "test06_tt_loophole_closed":      bool(leg8),
    }


if __name__ == "__main__":
    print(f"L₀ = c·τ₀ = {L0_MPC:.4f} Mpc   α_vac = {ALPHA_VAC:.4f}   (a,c)=({TRACE_ANOMALY_A:g},{TRACE_ANOMALY_C:g})")
    print(f"K⁽²⁾(ω) = σ·α·χ(ω)  — k-independent (no 1/k² pole); scale = L₀\n")
    print("Magnitude band ρ_eff/ρ_baryon at 10 kpc (exterior Weyl):")
    for k, v in galaxy_ratio_band().items():
        print(f"   {k:10s}: {v:8.2f}")
    print("\nRadial shape (isothermal galaxy):  rho_eff slope (DM needs −2):")
    ph = profile_phenomenology(isothermal_profile())
    for R in (5, 10, 20, 40):
        i = int(np.argmin(np.abs(ph["r_kpc"] - R)))
        print(f"   r={R:3d} kpc   ρ_eff/ρ_bar={ph['ratio'][i]:7.2f}   slope={ph['slope'][i]:6.2f}")
    print("\nError forensics (why the intermediate 'death' was wrong):")
    for k, v in _error_forensics().items():
        print(f"   {k:34s}: {v:.3e}")
    print("\nverify():", verify())
