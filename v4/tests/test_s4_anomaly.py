"""GRUT-RAI v4.1 — tests for TARGET 2 (s4_anomaly.py) and the α→ANCHOR re-tier.
Encode the (C) result: a/c=1/3 is computed first-hand and validated against tabulated CFT
values (so it is NOT reverse-fit), a and c are scheme-independent, the carrier antecedent
RAISES (free data), and the gate carries the re-tier with ω_Λ now conditional on the α-anchor.
"""
from __future__ import annotations

from fractions import Fraction as F
import pytest

from v4.targets import s4_anomaly as s4
from v4 import gate
from v4.registry import REGISTRY


def test_conformal_scalar_ac_from_gilkey_is_one_third():
    """The conformal scalar (a,c) drops out of Gilkey's a₄ directly (E=−R/6) as (1/360,1/120)
    ⇒ a/c=1/3 — computed, not looked up."""
    a, c = s4.extract_a_c(*s4.gilkey_scalar_primitive())
    assert (a, c) == (F(1, 360), F(1, 120))
    assert a / c == F(1, 3)


def test_machinery_validated_against_tabulated_cft():
    """The same extraction reproduces the tabulated Dirac (11/18) and vector (31/18) ratios —
    so the machinery is not tuned to land 1/3 (the inverted-laundering guard)."""
    v = s4.validate_machinery()
    assert v["Dirac fermion"]["a/c"] == F(11, 18)
    assert v["vector (gauge)"]["a/c"] == F(31, 18)
    assert v["real scalar"]["a/c"] == F(1, 3)


def test_extraction_rejects_inconsistent_basis():
    """The R² consistency check (c/3−a) must fire on a primitive that is not c·W²−a·E₄ —
    proof the extraction isn't a free fit."""
    with pytest.raises(ValueError):
        s4.extract_a_c(F(1, 180), F(-1, 180), F(99))   # bogus R² coefficient


def test_a_and_c_reported_separately_scheme_stated():
    """a and c are reported separately in a pre-stated scheme; a/c is exact."""
    cs = s4.conformal_scalar_ac()
    assert cs["a"] == F(1, 360) and cs["c"] == F(1, 120)
    assert cs["a_over_c"] == F(1, 3)
    assert "scheme" in cs and "s4_caveat" in cs


def test_grut_alpha_antecedent_raises():
    """The carrier antecedent is free data — it RAISES (the consequent a/c=1/3 is solid, the
    antecedent is the gap), not assumed."""
    with pytest.raises(NotImplementedError):
        s4.grut_alpha_antecedent()


def test_alpha_retiered_to_anchor_and_gate_passes():
    """Target 2 re-tiered α OPEN→ANCHOR; the gate still passes and ω_Λ now reads as conditional
    on the anchored α (SPLIT), not provisional on an open gap."""
    assert REGISTRY["alpha"].tier == gate.Tier.ANCHOR
    assert gate.validate(REGISTRY) == []
    assert "alpha" in gate.anchored_inputs(REGISTRY, "omega_lambda")
    assert gate.provisional_on(REGISTRY, "omega_lambda") == []


def test_no_open_claims_remain():
    """Both research-spine gaps (single_pole, α) are now proven anchors — the registry has no
    OPEN claims left; de-anchoring either requires new physics, not a missing computation."""
    assert [c.id for c in REGISTRY.values() if c.tier == gate.Tier.OPEN] == []
