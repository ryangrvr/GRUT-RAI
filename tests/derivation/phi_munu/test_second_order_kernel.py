"""Regression tests for the second-order CTP kernel K⁽²⁾ (the C5a flagship).

Pins the constructive-phase resolution (theory/GRUT_V3_K2_DERIVATION.md):
  - the kernel K⁽²⁾(ω)=σ·α·χ(ω) is k-independent (no 1/k² pole) ⇒ scale = L₀
  - L₀ = c·τ₀ ≈ 12.85 Mpc (the sole length)
  - the magnitude is VIABLE, O(1–100) at galaxy scales — NOT the spurious 1e-27
  - the discredited 1e-27 'death' is exactly the dropped geometric→SI c²/G factor
  - the shape is WRONG: ρ_eff ∝ W² ∝ ρ_baryon² ∝ 1/r⁴ (slope ≈ −4), steeper than −2
  - W²=0 on conformally-flat FRW ⇒ μ_linear=1 untouched
"""

from __future__ import annotations

import numpy as np

from grut.derivation.phi_munu import second_order_kernel as K2


def test_L0_is_12p85_Mpc():
    assert abs(K2.L0_MPC - 12.85) < 0.05


def test_kernel_is_k_independent_no_pole():
    # K⁽²⁾ depends on ω only; at ω=0, χ=1 ⇒ K⁽²⁾ = σ·α exactly, with no k argument.
    assert abs(K2.K2_kernel(0.0) - K2.SIGMA_DEFAULT * K2.ALPHA_VAC) < 1e-12


def test_susceptibility_limits():
    # GR recovery at high ω; full constitutive at ω→0.
    assert abs(K2.chi(0.0) - 1.0) < 1e-12
    big = K2.chi(1e6 / (K2.TAU0_MYR * 1e6 * K2._YR))
    assert abs(big) < 1e-3


def test_magnitude_viable_not_negligible():
    band = K2.galaxy_ratio_band(M_Msun=1e11, r_kpc=10.0)
    # O(1–100), emphatically not the discredited 1e-27 death claim.
    assert 1.0 < band["sigma=1"] < 1e3
    assert band["sigma=0.333333"] > 1.0


def test_death_claim_was_a_unit_bug():
    fx = K2._error_forensics()
    # Correct (consistent geometric units) is O(10); the '1e-27' appears ONLY when a
    # geometric ρ_eff is divided by an SI ρ_baryon (dropping c²/G ≈ 1.35e27).
    assert fx["correct_ratio_geometric"] > 1.0
    assert fx["bug1_unit_mismatch_geo_over_SI"] < 1e-20
    assert abs(fx["bug1_unit_mismatch_geo_over_SI"] * fx["c2_over_G"]
               - fx["correct_ratio_geometric"]) / fx["correct_ratio_geometric"] < 1e-6


def test_shape_too_steep_for_flat_curve():
    ph = K2.profile_phenomenology(K2.isothermal_profile())
    sel = (ph["r_kpc"] > 5) & (ph["r_kpc"] < 40)
    slope = np.median(ph["slope"][sel])
    # ρ_eff ∝ 1/r⁴ (slope ≈ −4) ≪ the −2 a flat rotation curve needs.
    assert slope < -3.0


def test_shape_is_sigma_independent():
    # σ scales magnitude only; the radial slope is identical across the band.
    s_lo = K2.profile_phenomenology(K2.isothermal_profile(), sigma=1 / 3)["slope"]
    s_hi = K2.profile_phenomenology(K2.isothermal_profile(), sigma=9.0)["slope"]
    assert np.allclose(s_lo, s_hi, atol=1e-9)


def test_W2_vanishes_on_flat_FRW():
    # Conformally-flat (zero density contrast) ⇒ W²=0 ⇒ μ_linear=1 preserved.
    assert K2.weyl_squared_weakfield(1e-30, 1e-30) == 0.0


def test_test06_bach_route_is_also_steep():
    # Route B: the Bach tensor source ∇²ρ for an isothermal halo is ∝ 1/r⁴ (slope ≈ −4),
    # the SAME as the scalar W² route — the 4-derivative structure does not shallow it.
    assert K2.bach_route_isothermal_slope() < -3.0


def test_test06_tt_projector_loophole_is_closed():
    # Route C: P^TT's k_ik_j/k² is degree-0 in |k| (angular), not a genuine 1/∇² pole.
    assert K2.tt_projector_is_inert() is True


def test_verify_all_legs_pass():
    assert all(K2.verify().values())
