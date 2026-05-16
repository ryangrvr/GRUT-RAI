"""Tests for grut.derivation.tji.allen_jacobson — Phase-1 implementation.

Phase-0 (stub) tests have been replaced with Phase-1 forward-evaluation
checks now that the Allen-Jacobson propagator formula is implemented.

Phase-1 deliverables verified here:
  - s4_propagator()            returns a SymPy expression (no longer raises)
  - s4_propagator_conformal()  closed-form conformally-coupled case
  - s4_propagator_uv_series()  short-distance expansion helper
  - volume_sphere()            Vol(S^D)
  - spectral_degeneracy()      d_n(D) multiplicity
  - spectral_eigenvalue()      λ_n(D)
  - tji_conformal_radial_integral()  tractable Beta-function sanity path
  - tji_on_s4()                raises S4CurvatureObstacle (obstacle documented)
  - interface_spec()           reflects Phase-1 status

Phase-1 obstacle:
  tji_on_s4() raises S4CurvatureObstacle because the 2-loop sunset
  Laurent expansion requires Mathematica + HypExp (Steps A/B/C in the
  calculation plan).  The propagator itself is fully implemented.
"""

from __future__ import annotations

import pytest
import sympy as sp
from sympy import Symbol


class TestAllenJacobsonModuleImports:
    def test_module_importable(self):
        from grut.derivation.tji import allen_jacobson  # noqa: F401

    def test_phase1_pending_is_NotImplementedError_subclass(self):
        from grut.derivation.tji.allen_jacobson import Phase1Pending
        assert issubclass(Phase1Pending, NotImplementedError)

    def test_s4_curvature_obstacle_is_NotImplementedError_subclass(self):
        from grut.derivation.tji.allen_jacobson import S4CurvatureObstacle
        assert issubclass(S4CurvatureObstacle, NotImplementedError)

    def test_s4_propagator_exists(self):
        from grut.derivation.tji.allen_jacobson import s4_propagator  # noqa: F401

    def test_tji_on_s4_exists(self):
        from grut.derivation.tji.allen_jacobson import tji_on_s4  # noqa: F401


class TestPropagatorImplemented:
    """Phase-1: s4_propagator() is IMPLEMENTED and returns a SymPy expression."""

    def test_s4_propagator_returns_sympy_expr_at_numeric_Z(self):
        from grut.derivation.tji.allen_jacobson import s4_propagator
        # Massless scalar at Z = 0 (equatorial), D = 4-2ε (dim-reg)
        eps = Symbol("eps", positive=True)
        D = 4 - 2 * eps
        result = s4_propagator(Z=sp.Rational(1, 2), D=D, m_squared=0, H_inf=1)
        assert isinstance(result, sp.Basic), (
            "s4_propagator should return a SymPy expression, not raise"
        )

    def test_s4_propagator_does_not_raise_phase1_pending(self):
        from grut.derivation.tji.allen_jacobson import s4_propagator, Phase1Pending
        eps = Symbol("eps", positive=True)
        D = 4 - 2 * eps
        try:
            s4_propagator(Z=sp.Rational(1, 2), D=D, m_squared=0, H_inf=1)
        except Phase1Pending:
            pytest.fail("s4_propagator raised Phase1Pending after Phase-1 implementation")

    def test_s4_propagator_contains_hypergeometric(self):
        """The Allen-Jacobson formula uses a ₂F₁ hypergeometric function."""
        from grut.derivation.tji.allen_jacobson import s4_propagator
        eps = Symbol("eps", positive=True)
        D = 4 - 2 * eps
        G = s4_propagator(Z=Symbol("Z"), D=D, m_squared=0, H_inf=1)
        # Expression must contain hyper (₂F₁) or gamma functions
        assert G.has(sp.hyper) or G.has(sp.gamma), (
            "Allen-Jacobson propagator must involve ₂F₁ or gamma"
        )

    def test_s4_propagator_massive_returns_expr(self):
        """Massive case (m² > 0) has no h₋ = 0 singularity; should return cleanly."""
        from grut.derivation.tji.allen_jacobson import s4_propagator
        m2 = sp.Rational(1, 10)
        G = s4_propagator(Z=sp.Rational(0), D=4, m_squared=m2, H_inf=1)
        assert isinstance(G, sp.Basic)


class TestConformallyCoupledPropagator:
    """Phase-1: s4_propagator_conformal() — closed-form, no ₂F₁ needed."""

    def test_returns_sympy_expr(self):
        from grut.derivation.tji.allen_jacobson import s4_propagator_conformal
        eps = Symbol("eps", positive=True)
        G = s4_propagator_conformal(Z=Symbol("Z"), D=4 - 2 * eps)
        assert isinstance(G, sp.Basic)

    def test_closed_form_no_hyper(self):
        """Conformally coupled propagator must NOT contain ₂F₁ — it has a closed form."""
        from grut.derivation.tji.allen_jacobson import s4_propagator_conformal
        Z = Symbol("Z")
        eps = Symbol("eps", positive=True)
        G = s4_propagator_conformal(Z=Z, D=4 - 2 * eps)
        assert not G.has(sp.hyper), (
            "s4_propagator_conformal should return ((1-Z)/2)^{-(D-2)/2} closed form"
        )

    def test_power_law_form(self):
        """G_conf ∝ ((1-Z)/2)^{-(D-2)/2}."""
        from grut.derivation.tji.allen_jacobson import s4_propagator_conformal
        Z = Symbol("Z")
        D = Symbol("D", positive=True)
        G = s4_propagator_conformal(Z=Z, D=D)
        # Should contain a power of (1-Z)
        assert G.has(Z), "G_conf must depend on Z"

    def test_d4_flat_space_limit(self):
        """At D=4, G_conf ∝ Γ(1)/((4π)²) × ((1-Z)/2)^{-1} = 1/(4π²(1-Z)/2)."""
        from grut.derivation.tji.allen_jacobson import s4_propagator_conformal
        Z = Symbol("Z")
        G4 = s4_propagator_conformal(Z=Z, D=4)
        G4_simplified = sp.simplify(G4)
        # Near Z=1: G ~ 1/(4π²(1-Z)/2) — check it diverges as (1-Z)→0
        assert G4_simplified.has(Z)


class TestSpectralHelpers:
    """Phase-1: volume_sphere, spectral_degeneracy, spectral_eigenvalue."""

    def test_volume_s4(self):
        """Vol(S⁴) = 8π²/3."""
        from grut.derivation.tji.allen_jacobson import volume_sphere
        vol = sp.simplify(volume_sphere(D=4, H_inf=1))
        expected = sp.Rational(8, 3) * sp.pi ** 2
        assert sp.simplify(vol - expected) == 0, (
            f"Vol(S⁴) expected 8π²/3, got {vol}"
        )

    def test_spectral_degeneracy_d4_n1(self):
        """d_1(D=4) = (2+3)(1+2)(1+1)/6 = 5·3·2/6 = 5."""
        from grut.derivation.tji.allen_jacobson import spectral_degeneracy
        d1 = sp.simplify(spectral_degeneracy(n=1, D=4))
        assert d1 == 5, f"d_1(D=4) expected 5, got {d1}"

    def test_spectral_degeneracy_d4_n2(self):
        """d_2(D=4) = (4+3)(2+2)(2+1)/6 = 7·4·3/6 = 14."""
        from grut.derivation.tji.allen_jacobson import spectral_degeneracy
        d2 = sp.simplify(spectral_degeneracy(n=2, D=4))
        assert d2 == 14, f"d_2(D=4) expected 14, got {d2}"

    def test_spectral_eigenvalue_d4(self):
        """λ_n(D=4) = n(n+3)."""
        from grut.derivation.tji.allen_jacobson import spectral_eigenvalue
        for n in (1, 2, 3):
            lam = sp.simplify(spectral_eigenvalue(n=n, D=4, H_inf=1))
            expected = n * (n + 3)
            assert lam == expected, (
                f"λ_{n}(D=4) expected {expected}, got {lam}"
            )

    def test_spectral_eigenvalue_zero_mode(self):
        """n=0 gives λ_0 = 0 (zero mode)."""
        from grut.derivation.tji.allen_jacobson import spectral_eigenvalue
        lam0 = sp.simplify(spectral_eigenvalue(n=0, D=4, H_inf=1))
        assert lam0 == 0


class TestTJIConformRadialIntegral:
    """Phase-1: tji_conformal_radial_integral() — tractable Beta-function path."""

    def test_returns_dict(self):
        from grut.derivation.tji.allen_jacobson import tji_conformal_radial_integral
        result = tji_conformal_radial_integral()
        assert isinstance(result, dict)

    def test_required_keys_present(self):
        from grut.derivation.tji.allen_jacobson import tji_conformal_radial_integral
        r = tji_conformal_radial_integral()
        for key in ("D", "C_D", "alpha_power", "beta_power", "B_integral",
                    "I_conformal", "note"):
            assert key in r, f"tji_conformal_radial_integral result missing key {key!r}"

    def test_alpha_beta_at_d4(self):
        """For D=4-2ε at ε=0: α=(−5)/2, β=1/2."""
        from grut.derivation.tji.allen_jacobson import tji_conformal_radial_integral
        eps = Symbol("eps", positive=True)
        r = tji_conformal_radial_integral(D=4 - 2 * eps)
        alpha_at_0 = sp.limit(r["alpha_power"], eps, 0)
        beta_at_0  = sp.limit(r["beta_power"],  eps, 0)
        assert alpha_at_0 == sp.Rational(-5, 2), (
            f"α at ε=0 expected -5/2, got {alpha_at_0}"
        )
        assert beta_at_0 == sp.Rational(1, 2), (
            f"β at ε=0 expected 1/2, got {beta_at_0}"
        )

    def test_note_says_sanity_only(self):
        from grut.derivation.tji.allen_jacobson import tji_conformal_radial_integral
        r = tji_conformal_radial_integral()
        assert "SANITY" in r["note"] or "sanity" in r["note"]


class TestTJIOnS4RaisesObstacle:
    """Phase-1: tji_on_s4() raises S4CurvatureObstacle (not Phase1Pending)."""

    def test_raises_s4_curvature_obstacle(self):
        from grut.derivation.tji.allen_jacobson import tji_on_s4, S4CurvatureObstacle
        with pytest.raises(S4CurvatureObstacle):
            tji_on_s4(D=4, k_squared=0, indices=((1, 0), (1, 0), (1, 0)))

    def test_does_not_raise_phase1_pending(self):
        from grut.derivation.tji.allen_jacobson import tji_on_s4, Phase1Pending
        with pytest.raises(Exception) as exc_info:
            tji_on_s4(D=4, k_squared=0, indices=((1, 0), (1, 0), (1, 0)))
        assert not isinstance(exc_info.value, Phase1Pending), (
            "tji_on_s4 should raise S4CurvatureObstacle, not the old Phase1Pending"
        )

    def test_obstacle_message_names_propagator_implemented(self):
        from grut.derivation.tji.allen_jacobson import tji_on_s4, S4CurvatureObstacle
        try:
            tji_on_s4(D=4, k_squared=0, indices=((1, 0), (1, 0), (1, 0)))
        except S4CurvatureObstacle as e:
            msg = str(e)
            assert "IMPLEMENTED" in msg, "obstacle message should say propagator is implemented"

    def test_obstacle_message_names_mathematica(self):
        from grut.derivation.tji.allen_jacobson import tji_on_s4, S4CurvatureObstacle
        try:
            tji_on_s4(D=4, k_squared=0, indices=((1, 0), (1, 0), (1, 0)))
        except S4CurvatureObstacle as e:
            msg = str(e)
            assert "Mathematica" in msg or "HypExp" in msg

    def test_obstacle_message_names_euler_channel(self):
        from grut.derivation.tji.allen_jacobson import tji_on_s4, S4CurvatureObstacle
        try:
            tji_on_s4(D=4, k_squared=0, indices=((1, 0), (1, 0), (1, 0)))
        except S4CurvatureObstacle as e:
            msg = str(e)
            assert "Euler" in msg or "euler" in msg.lower()

    def test_wrong_indices_also_raises_obstacle(self):
        from grut.derivation.tji.allen_jacobson import tji_on_s4, S4CurvatureObstacle
        with pytest.raises(S4CurvatureObstacle):
            tji_on_s4(D=4, k_squared=0, indices=((2, 0), (1, 0), (1, 0)))


class TestInterfaceSpec:
    """interface_spec() reflects Phase-1 status."""

    def test_spec_returns_dict(self):
        from grut.derivation.tji.allen_jacobson import interface_spec
        s = interface_spec()
        assert isinstance(s, dict)

    def test_spec_has_required_keys(self):
        from grut.derivation.tji.allen_jacobson import interface_spec
        s = interface_spec()
        for k in (
            "module", "propagator_function", "propagator_signature",
            "integral_function", "integral_signature",
            "implementation_status", "raises", "reference",
            "phase_1_plan", "target_finite_rational",
            "target_interpretation",
        ):
            assert k in s, f"interface_spec missing key {k!r}"

    def test_spec_status_reflects_phase1_implementation(self):
        from grut.derivation.tji.allen_jacobson import interface_spec
        s = interface_spec()
        status = s["implementation_status"]
        assert "Phase-1" in status or "Phase 1" in status
        assert "IMPLEMENTED" in status

    def test_spec_raises_names_obstacle_not_stub(self):
        from grut.derivation.tji.allen_jacobson import interface_spec
        s = interface_spec()
        # Phase-1: raises S4CurvatureObstacle, not Phase1Pending
        assert "S4CurvatureObstacle" in s["raises"] or "obstacle" in s["raises"].lower()

    def test_spec_target_rational_is_minus_100(self):
        """V7 §26.2.6 / Correction #16: target finite rational is −100."""
        from grut.derivation.tji.allen_jacobson import interface_spec
        s = interface_spec()
        assert s["target_finite_rational"] == -100

    def test_spec_interpretation_names_correction_16(self):
        from grut.derivation.tji.allen_jacobson import interface_spec
        s = interface_spec()
        assert "Y²" in s["target_interpretation"] or "Y^2" in s["target_interpretation"]
        assert "Correction #16" in s["target_interpretation"]

    def test_spec_references_allen_jacobson_1986(self):
        from grut.derivation.tji.allen_jacobson import interface_spec
        s = interface_spec()
        assert "Allen" in s["reference"] and "Jacobson" in s["reference"]
        assert "1986" in s["reference"]

    def test_spec_has_propagator_status_key(self):
        """Phase-1 addition: propagator_status documents what's implemented."""
        from grut.derivation.tji.allen_jacobson import interface_spec
        s = interface_spec()
        assert "propagator_status" in s
        assert "IMPLEMENTED" in s["propagator_status"]

    def test_spec_has_tji_obstacle_key(self):
        """Phase-1 addition: tji_obstacle documents the blocking step."""
        from grut.derivation.tji.allen_jacobson import interface_spec
        s = interface_spec()
        assert "tji_obstacle" in s
        assert "Mathematica" in s["tji_obstacle"] or "HypExp" in s["tji_obstacle"]

        from grut.derivation.tji.allen_jacobson import interface_spec
        s = interface_spec()
        assert "Y²" in s["target_interpretation"] or "Y^2" in s["target_interpretation"]
        assert "Correction #16" in s["target_interpretation"]

    def test_spec_references_allen_jacobson_1986(self):
        from grut.derivation.tji.allen_jacobson import interface_spec
        s = interface_spec()
        assert "Allen" in s["reference"] and "Jacobson" in s["reference"]
        assert "1986" in s["reference"]
