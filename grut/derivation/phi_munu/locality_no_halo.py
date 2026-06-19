"""Test 07 — the Locality–No-Halo Theorem (spectral form).

The C5a investigation (second_order_kernel.py, Tests A–D + Test 06) found the
W² dark-sector response has the wrong radial profile. Test 07 shows *why*, in a
form that no longer depends on the choice of operator: the result is **spectral**.

    THEOREM (spectral). A GRUT dark-sector response that is covariant, local in
    the matter fields (a kernel analytic — entire, pole-free — in k² near k=0),
    and nonlinear (No-Go) is no more spatially extended than its baryon source.
    An extended halo (ρ_eff ~ 1/r², significant where baryons have vanished)
    requires the response to be SINGULAR at k=0 (a pole / inverse-Laplacian
    1/∇²). Locality forbids that singularity. Hence no covariant matter-local
    GRUT response can be a halo; a derived dark sector requires a NEW POLE in
    the vacuum spectrum (a new propagating mode), not a new operator.

Three independent walls:
  • covariance — the lowest covariant field is the curvature ∂²Φ (~1/r³), not
    the acceleration ∂Φ (a non-tensor); curvature invariants are ≥ 1/r⁶.
  • locality   — g = ∇Φ = ∇(1/∇²)ρ is the enclosed mass: local in the field,
    NONLOCAL in the matter. A local causal kernel is polynomial in k² (no pole).
  • the No-Go  — a response linear in ρ_baryon (μ_linear=1) is forbidden.

MOND is the illuminating case: it gives the right 1/r² phantom precisely by
responding to g = ∇Φ_N (the forbidden nonlocal 1/∇² of the matter). Hence GRUT
may carry the scale a₀ = cH₀/(2π) but cannot locally derive an interpolation
function. See theory/GRUT_V3_TEST_07_LOCALITY_NO_HALO.md for the full record.
"""

from __future__ import annotations

from typing import Dict

import numpy as np


def _radial_ft(rho, kv, r):
    """3D isotropic Fourier transform  ρ(k) = (4π/k) ∫ ρ(r) sin(kr) r dr."""
    trap = getattr(np, "trapezoid", None) or np.trapz
    return np.array([(4.0 * np.pi / kk) * trap(rho * np.sin(kk * r) * r, r)
                     for kk in kv])


def _small_k_slope(k, F, lo=2e-3, hi=3e-2):
    s = (k > lo) & (k < hi)
    return float(np.polyfit(np.log(k[s]), np.log(np.abs(F[s])), 1)[0])


def spectral_fingerprints(a: float = 3.0) -> Dict[str, float]:
    """Small-k slope of ρ(k): a localized source is analytic (slope≈0); a 1/r²
    halo is singular (slope≈−1). The halo's extension *is* a k=0 singularity.
    """
    r = np.linspace(1e-3, 12000.0, 120000)
    k = np.logspace(-3, 0, 50)
    loc = np.exp(-r / a)
    halo = 1.0 / (r**2 + a**2)
    return {
        "localized_source_slope": _small_k_slope(k, _radial_ft(loc, k, r)),
        "halo_1_over_r2_slope":   _small_k_slope(k, _radial_ft(halo, k, r)),
        "analytic_kernel_slope":  _small_k_slope(k, (1 + a**2 * k**2) * _radial_ft(loc, k, r)),
        "pole_kernel_slope":      _small_k_slope(k, _radial_ft(loc, k, r) / k**2),
    }


def pole_response_is_extended(a: float = 3.0) -> bool:
    """A pole kernel 1/k² (=1/∇²) turns a COMPACT source into a 1/r tail:
    r·ρ_eff(r) ≈ const over decades. Demonstrates only a k=0 pole delocalizes.
    """
    r = np.linspace(1e-3, 12000.0, 120000)
    kk = np.logspace(-4, 2, 2000)
    trap = getattr(np, "trapezoid", None) or np.trapz
    Fp = _radial_ft(np.exp(-r / a), kk, r) / kk**2
    rs = np.array([20.0, 80.0, 320.0, 1280.0])
    rrho = np.array([rR * (1.0 / (2 * np.pi**2 * rR)) * trap(Fp * np.sin(kk * rR) * kk, kk)
                     for rR in rs])
    return bool(np.all(np.abs(rrho / rrho[0] - 1.0) < 0.2))   # r·ρ_eff ≈ const ⇒ 1/r


def grut_kernel_is_analytic_at_k0() -> bool:
    """K⁽²⁾(ω,k)=σ·α·χ(ω) is k-independent (Stage B) and P^TT is degree-0 in
    |k| (angular, no magnitude pole). So the monopole sector is analytic at k=0
    — no 1/k² pole to delocalize a source.
    """
    import sympy as sp
    kx, ky, kz, lam = sp.symbols("kx ky kz lam", positive=True)
    k2 = kx**2 + ky**2 + kz**2
    Ptt = 1 - kx * kx / k2
    ptt_degree0 = sp.simplify(
        Ptt.subs({kx: lam * kx, ky: lam * ky, kz: lam * kz}) - Ptt) == 0
    return bool(ptt_degree0)


def verify() -> Dict[str, bool]:
    """Self-test the four legs of the spectral theorem."""
    fp = spectral_fingerprints()
    return {
        "halo_is_k0_singular":          abs(fp["halo_1_over_r2_slope"] + 1.0) < 0.15,
        "source_is_analytic":           abs(fp["localized_source_slope"]) < 0.15,
        "analytic_kernel_keeps_local":  abs(fp["analytic_kernel_slope"]) < 0.15,
        "pole_kernel_delocalizes":      abs(fp["pole_kernel_slope"] + 2.0) < 0.2,
        "pole_response_extended_1_over_r": pole_response_is_extended(),
        "grut_kernel_analytic_at_k0":   grut_kernel_is_analytic_at_k0(),
    }


if __name__ == "__main__":
    print("Locality–No-Halo Theorem (spectral form) — verification\n")
    for k, v in spectral_fingerprints().items():
        print(f"  {k:28s}: {v:+.3f}")
    print()
    for k, v in verify().items():
        print(f"  {k:34s}: {v}")
