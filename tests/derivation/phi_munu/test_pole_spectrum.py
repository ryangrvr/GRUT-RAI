"""Tests for the Spectrum Program Phase I — Pole Classification Theorem."""

from grut.derivation.phi_munu.pole_spectrum import (
    first_order,
    second_order,
    admits_dark_capable_mode,
    coupled_relaxors_dark_capable,
    single_pole_passive_causal,
    positive_superposition_is_passive,
    verify,
)


def test_deriving_F_form_is_Q_admissible():
    # Q (FDT) forces causal+passive (Herglotz): the single-pole form is admissible,
    # and a positive Debye superposition is the general Q-admissible kernel.
    assert single_pole_passive_causal()
    assert positive_superposition_is_passive()


def test_all_legs_pass():
    assert all(verify().values())


def test_current_grut_is_single_relaxational_pole():
    fo = first_order()
    assert len(fo) == 1
    assert fo[0]["kind"] == "relaxational"
    assert fo[0]["stable"]
    assert not admits_dark_capable_mode(fo)   # no derived dark sector in current GRUT


def test_additional_pole_required_for_dark_mode():
    # overdamped inertial kernel: no off-axis pole at all
    assert not admits_dark_capable_mode(second_order(tau0=1.0, tau1=0.2))
    # heavily damped resonance (τ₁ ≈ τ₀): off-axis but NOT a relic (width ≈ mass)
    assert not admits_dark_capable_mode(second_order(tau0=1.0, tau1=1.0))
    # long-lived inertial kernel (τ₁ ≫ τ₀): a narrow dark-capable pole appears
    assert admits_dark_capable_mode(second_order(tau0=1.0, tau1=100.0))


def test_all_poles_are_causal():
    for poles in (first_order(), second_order(1.0, 1.0), second_order(1.0, 0.2)):
        assert all(p["stable"] for p in poles)


def test_phase2_relaxors_never_host_a_dark_mode():
    # Phase II verdict: coupling relaxational variables (no inertia) never yields a
    # stable off-axis (dark-capable) pole — a dark mode requires inertial matter DOF.
    assert not coupled_relaxors_dark_capable()
    assert admits_dark_capable_mode(second_order(1.0, 100.0))   # long-lived inertia does
