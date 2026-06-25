"""GRUT-RAI v4.1 — tests for TARGET 1C (curved_bath.py) and the single_pole→ANCHOR re-tier.
These encode the (C) result: the curved-space IR exponent s is NOT fixed by what GRUT
supplies (collisional⇒1, collisionless⇒free DOS-edge), 1B's Hubble-friction lean is broken,
the de Sitter-IR slow channel is closed, and the gate carries the re-tier honestly.
"""
from __future__ import annotations

import pytest

from v4.targets import curved_bath as cb
from v4 import gate
from v4.registry import REGISTRY


def test_free_bath_s_is_the_free_dos_edge():
    """Collisionless (Gaussian) bath: J(ω) is the coupling-weighted DOS, so s = the DOS edge p,
    which is free data — the action does not fix it."""
    for p in (-0.5, 0.0, 0.5, 1.0):
        assert abs(cb.ir_slope(cb.free_bath_J(p), 1e-3) - p) < 1e-2


def test_interacting_bath_s_is_one():
    """Collisional bath (finite shear viscosity, Drude/Kubo): s = 1, independent of any DOS edge."""
    assert abs(cb.ir_slope(cb.interacting_bath_J(), 1e-3) - 1.0) < 1e-2


def test_s_three_ways_disagree():
    """The three determinations the action allows DISAGREE ⇒ s not robust ⇒ outcome (C)."""
    r = cb.s_three_ways(p_free=0.5)
    assert r["agree"] is False
    assert abs(r["collisional_Kubo"] - 1.0) < 1e-2          # collisional ⇒ fast
    assert r["collisionless_DOS_edge"] < 1.0               # collisionless ⇒ slow (here 0.5)


def test_hubble_friction_lean_is_broken():
    """1B claimed Hubble friction pushes s↑ (fast). Modeled as line broadening, it ADDS weight
    at ω=0 (ρ_H(0)>0) even for a super-Ohmic edge — driving s toward 0 (slow), not fast."""
    for H in (1e-3, 1e-2, 1e-1):
        b = cb.hubble_broadening(p=2.0, H=H)
        assert b["rho_H_at_0"] > 0.0           # weight added at ω=0 ⇒ sub-Ohmic-ward
        assert b["s_below_H"] < 0.5            # not the s≥1 a 'fast' lean would need


def test_ds_ir_enhancement_channel_closed():
    """The de Sitter scalar IR enhancement lives in ⟨φ²⟩ (IR-divergent); the TT-shear couples to
    T~(∂φ)², which is IR-finite. So dS enhancement does NOT force s<1 — that slow channel is closed."""
    a = cb.ds_ir_protection(kmin=1e-3)
    b = cb.ds_ir_protection(kmin=1e-5)
    assert b["phi2_IR_divergent"] > a["phi2_IR_divergent"]          # ⟨φ²⟩ grows as floor→0
    assert abs(b["dphi2_IR_finite"] - a["dphi2_IR_finite"]) < 1e-3  # ⟨(∂φ)²⟩ floor-independent
    assert a["stress_tensor_IR_protected"] is True


def test_grut_curved_ir_exponent_raises():
    """The action's missing datum (the bath transport/collisionality) RAISES — not assumed."""
    with pytest.raises(NotImplementedError):
        cb.grut_curved_ir_exponent()


def test_single_pole_was_corrected_to_derived_post_review():
    """1C ORIGINALLY re-tiered single_pole OPEN→ANCHOR on a free-DOS-edge argument. External
    review (2026-06-24) showed that argument backwards for a relativistic vacuum, so single_pole
    GRADUATED ANCHOR→DERIVED (super-Ohmic theorem, Target 1D). This test pins the correction; the
    still-valid 1C legs (H-friction break, dS-IR protection) are tested above and still pass."""
    assert REGISTRY["constitutive_law_single_pole"].tier == gate.Tier.DERIVED
    assert gate.validate(REGISTRY) == []
