"""Tests for the Locality–No-Halo Theorem (spectral form) — Test 07."""

from grut.derivation.phi_munu.locality_no_halo import (
    spectral_fingerprints,
    pole_response_is_extended,
    grut_kernel_is_analytic_at_k0,
    verify,
)


def test_all_legs_pass():
    assert all(verify().values())


def test_halo_is_k0_singular_source_is_not():
    fp = spectral_fingerprints()
    # a 1/r^2 halo is singular at k=0 (slope ~ -1); a localized source is analytic (~0)
    assert abs(fp["halo_1_over_r2_slope"] + 1.0) < 0.15
    assert abs(fp["localized_source_slope"]) < 0.15


def test_only_a_pole_delocalizes():
    fp = spectral_fingerprints()
    # analytic kernel keeps the source localized; the 1/k^2 pole delocalizes it
    assert abs(fp["analytic_kernel_slope"]) < 0.15
    assert abs(fp["pole_kernel_slope"] + 2.0) < 0.2
    assert pole_response_is_extended()


def test_grut_kernel_has_no_k0_pole():
    assert grut_kernel_is_analytic_at_k0()
