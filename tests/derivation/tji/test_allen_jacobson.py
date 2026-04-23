"""Regression tests for grut.derivation.tji.allen_jacobson — interface stub.

The Allen-Jacobson S⁴ propagator module is a STUB: all evaluation
functions raise Phase1Pending. These tests pin the interface so any
silent implementation change (accidental removal of Phase1Pending, etc.)
is caught before it goes out the door.

The actual Phase-1 implementation replaces these tests with forward-
evaluation checks. Until then, we assert "pending" at every entry
point.
"""

from __future__ import annotations

import pytest


class TestAllenJacobsonModuleImports:
    def test_module_importable(self):
        from grut.derivation.tji import allen_jacobson  # noqa: F401

    def test_phase1_pending_is_NotImplementedError_subclass(self):
        from grut.derivation.tji.allen_jacobson import Phase1Pending
        assert issubclass(Phase1Pending, NotImplementedError)

    def test_s4_propagator_exists(self):
        from grut.derivation.tji.allen_jacobson import s4_propagator  # noqa: F401

    def test_tji_on_s4_exists(self):
        from grut.derivation.tji.allen_jacobson import tji_on_s4  # noqa: F401


class TestStubRaisesPhase1Pending:
    def test_s4_propagator_raises_phase1_pending(self):
        from grut.derivation.tji.allen_jacobson import s4_propagator, Phase1Pending
        with pytest.raises(Phase1Pending):
            s4_propagator(Z=0.5)

    def test_tji_on_s4_raises_phase1_pending(self):
        from grut.derivation.tji.allen_jacobson import tji_on_s4, Phase1Pending
        with pytest.raises(Phase1Pending):
            tji_on_s4(D=4, k_squared=1.0, indices=((1, 0), (1, 0), (1, 0)))

    def test_phase1_pending_message_references_plan_doc(self):
        from grut.derivation.tji.allen_jacobson import s4_propagator, Phase1Pending
        try:
            s4_propagator(Z=0.5)
        except Phase1Pending as e:
            msg = str(e)
            assert "Allen-Jacobson" in msg
            assert "Phase-1" in msg or "Phase 1" in msg
            assert "TJI_PHASE_1_CALCULATION_PLAN" in msg

    def test_tji_on_s4_message_references_flat_space_analog(self):
        from grut.derivation.tji.allen_jacobson import tji_on_s4, Phase1Pending
        try:
            tji_on_s4(D=4, k_squared=1, indices=((1,0),(1,0),(1,0)))
        except Phase1Pending as e:
            msg = str(e)
            assert "flat_space" in msg or "flat-space" in msg
            assert "S⁴" in msg or "S^4" in msg


class TestInterfaceSpec:
    """The interface_spec() return value pins the Phase-1 contract:
    function names, argument lists, target rational, reference paper.
    Any Phase-1 implementation must keep this spec stable."""

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
            assert k in s, f"interface_spec missing key {k}"

    def test_spec_status_is_stub(self):
        from grut.derivation.tji.allen_jacobson import interface_spec
        s = interface_spec()
        assert "STUB" in s["implementation_status"]
        assert "Phase1Pending" in s["raises"]

    def test_spec_target_rational_is_minus_100(self):
        """V7 §26.2.6 / Correction #16: target finite rational is −100,
        identified as −(Σ_SM Y²)² = −10². If Phase-1 produces a different
        rational, the framework's structural claim needs revisiting."""
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
