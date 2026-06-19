"""Tests for the Spectrum Program Phase III — Mori–Zwanzig memory function.

Confirms that first-order-ness is the Markovian limit of MZ (controlled by the
τ_micro≪τ₀ hierarchy) and that the MZ memory function cannot produce a
dark-capable (off-axis) pole for the slow responsive vacuum.
"""

from grut.derivation.phi_munu.mori_zwanzig_kernel import (
    markovian_limit,
    second_level,
    off_axis_threshold,
    is_overdamped,
    slow_fast_separation_forbids_dark,
    fast_pole_is_suppressed,
    verify,
)
from grut.derivation.phi_munu.pole_spectrum import admits_dark_capable_mode


def test_all_legs_pass():
    assert all(verify().values())


def test_markovian_limit_is_single_grut_pole():
    ml = markovian_limit(1.0)
    assert len(ml) == 1
    assert ml[0]["kind"] == "relaxational"
    assert ml[0]["stable"]
    assert not admits_dark_capable_mode(ml)


def test_off_axis_threshold_is_tau0_over_4():
    assert abs(off_axis_threshold(1.0) - 0.25) < 1e-9
    # memory faster than τ₀/4 → overdamped (on-axis, no dark mode)
    assert is_overdamped(1.0, 0.24)
    # memory slower than τ₀/4 → underdamped (off-axis, dark-capable)
    assert not is_overdamped(1.0, 0.26)


def test_slow_variable_never_hosts_dark_mode():
    # A genuine slow variable (τ_K ≪ τ₀) is always overdamped.
    for tauK in (1e-1, 1e-3, 1e-9, 1e-20):
        assert is_overdamped(1.0, tauK)
        assert not admits_dark_capable_mode(second_level(1.0, tauK))


def test_grut_hierarchy_forbids_dark_mode():
    # THE THEOREM at GRUT's actual τ_micro/τ₀ ~ 1e-34 hierarchy.
    assert slow_fast_separation_forbids_dark()


def test_resonant_kernel_escape_requires_slow_memory():
    # The only route to a long-lived dark pole is a memory kernel MUCH slower than
    # the variable (τ_K ≫ τ₀, a resonant medium = a foundational extension).
    assert admits_dark_capable_mode(second_level(1.0, 1e4))
    # a marginally-slow kernel (τ_K just above τ₀/4) is off-axis but still a
    # heavily damped resonance, not a long-lived relic:
    assert not admits_dark_capable_mode(second_level(1.0, 0.3))


def test_fast_pole_is_suppressed_effective_single_pole():
    assert fast_pole_is_suppressed(1.0, 1e-3)
