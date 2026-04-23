"""Regression tests for grut.derivation.tji.flat_space.

The flat-space TJI Laurent expansion is a pinned, exact symbolic
calculation. These tests assert Fraction-level equality (not float
approximation) for the finite rational and pole coefficients produced
in the raw gamma-function scheme.

Phase-0 contract:
    - `finite_rational_raw_scheme()` returns Fraction(-541, 2304) exactly.
    - Pole coefficients 1/ε² = -1/64 and 1/ε rational part = -25/384
      are exact rationals pinned by the test.
    - The FeynCalc reference 7/4 is documented as Phase-0.5 TODO;
      equality with the raw-scheme result is NOT asserted here.

If any of these values silently drift in a future refactor, the test
fails — catching the regression before it propagates.
"""

from __future__ import annotations

from fractions import Fraction

import pytest


class TestFlatSpaceModuleImports:
    def test_module_importable(self):
        from grut.derivation.tji import flat_space  # noqa: F401

    def test_has_expected_functions(self):
        from grut.derivation.tji import flat_space
        for name in (
            "laurent_expansion_raw",
            "finite_rational_raw_scheme",
            "pole_structure",
            "feyncalc_reference",
            "verify",
        ):
            assert hasattr(flat_space, name), f"missing {name}"


class TestFiniteRationalRawScheme:
    """The ε⁰ rational in the raw gamma-function scheme is exactly
    -541/2304 (verified by independent computation, October 2026)."""

    def test_returns_dict_with_expected_keys(self):
        from grut.derivation.tji.flat_space import finite_rational_raw_scheme
        r = finite_rational_raw_scheme()
        for k in ("sympy_rational", "python_fraction", "as_decimal",
                  "raw_eps0_coefficient", "scheme", "status"):
            assert k in r

    def test_finite_rational_is_exact_minus_541_over_2304(self):
        from grut.derivation.tji.flat_space import finite_rational_raw_scheme
        r = finite_rational_raw_scheme()
        assert r["python_fraction"] == Fraction(-541, 2304), (
            f"Raw-scheme ε⁰ rational drifted: got {r['python_fraction']}, "
            f"expected Fraction(-541, 2304). If this is intentional, "
            f"update the test AND document the scheme change in "
            f"theory/derivation/TJI_PHASE_1_CALCULATION_PLAN.md."
        )

    def test_finite_rational_is_sympy_Rational(self):
        import sympy as sp
        from grut.derivation.tji.flat_space import finite_rational_raw_scheme
        r = finite_rational_raw_scheme()
        assert isinstance(r["sympy_rational"], sp.Rational)

    def test_status_is_COMPUTED(self):
        from grut.derivation.tji.flat_space import finite_rational_raw_scheme
        assert finite_rational_raw_scheme()["status"] == "COMPUTED"

    def test_scheme_is_raw_gamma_function(self):
        from grut.derivation.tji.flat_space import finite_rational_raw_scheme
        assert "raw" in finite_rational_raw_scheme()["scheme"]


class TestPoleStructure:
    """Double-pole coefficient (ε^-2) and single-pole rational part
    (ε^-1, γ_E dropped) are pinned exact rationals."""

    def test_double_pole_is_minus_one_over_64(self):
        from grut.derivation.tji.flat_space import pole_structure
        p = pole_structure()
        assert p["double_pole_as_fraction"] == Fraction(-1, 64)

    def test_single_pole_rational_part_is_minus_25_over_384(self):
        from grut.derivation.tji.flat_space import pole_structure
        p = pole_structure()
        assert p["single_pole_rational_fraction"] == Fraction(-25, 384)


class TestFeynCalcReferenceDocumented:
    """The FeynCalc 7/4 value is documented (not asserted). Phase-0.5
    is the reconciliation-to-7/4 item."""

    def test_feyncalc_reference_is_7_over_4(self):
        from grut.derivation.tji.flat_space import feyncalc_reference
        ref = feyncalc_reference()
        assert ref["feyncalc_rational"] == Fraction(7, 4)

    def test_feyncalc_reference_notes_scheme_gap(self):
        from grut.derivation.tji.flat_space import feyncalc_reference
        ref = feyncalc_reference()
        assert "scheme" in ref["status_vs_this_module"].lower()
        assert "Phase-0.5" in ref["status_vs_this_module"]

    def test_raw_scheme_value_differs_from_feyncalc_by_scheme(self):
        """Until Phase-0.5 reconciles conventions, the two values
        are NOT equal. This test pins the non-equality so a future
        'coincidence' where they happen to align numerically gets
        flagged (would indicate a regression or scheme drift)."""
        from grut.derivation.tji.flat_space import (
            finite_rational_raw_scheme, feyncalc_reference,
        )
        raw = finite_rational_raw_scheme()["python_fraction"]
        ref = feyncalc_reference()["feyncalc_rational"]
        assert raw != ref, (
            f"Raw-scheme result {raw} matched FeynCalc reference {ref} — "
            f"if this is intentional (Phase-0.5 completed), update this "
            f"test to assert equality and remove the Phase-0.5 pending flag."
        )


class TestVerifyBlock:
    def test_verify_all_checks_pass(self):
        from grut.derivation.tji.flat_space import verify
        v = verify()
        for key, val in v.items():
            assert val is True, f"verify() check failed: {key}"
