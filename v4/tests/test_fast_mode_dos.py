"""GRUT-RAI v4.1 — tests for TARGET 1D (fast_mode_dos.py) after round 2 of external review.
Encode the CORRECTED state: the massless linear-coupling J(ω) is Ohmic (s=1, marginal) once the
1/ω_k mode normalization is kept (the earlier s=2 conflated DOS with J); the exponent is
collisionality-dependent across branches but every clean branch is s≥1 and sub-Ohmic is forbidden
by masslessness; single-pole-ness is PENDING_REVIEW (a strong argument, not a theorem).
"""
from __future__ import annotations

import copy

from v4.targets import fast_mode_dos as fm
from v4 import gate
from v4.gate import Claim, Tier, Novelty, Step, validate
from v4.registry import REGISTRY


def test_dos_is_omega_squared_but_is_not_J():
    """The DOS is ρ~ω², but J(ω) is NOT the DOS — keeping that distinction is the whole fix."""
    assert abs(fm.massless_dos_exponent(d_space=3) - 2.0) < 0.05


def test_linear_coupling_is_ohmic_marginal_not_super_ohmic():
    """With the 1/ω_k mode normalization, massless linear coupling gives J~ω ⇒ s=1 (Ohmic,
    marginal), NOT the s=2 claimed in round 1 (which dropped the 1/ω_k factor)."""
    assert abs(fm.linear_coupling_s(d_space=3) - 1.0) < 0.1


def test_cross_branch_every_clean_branch_geq_1():
    """The exponent is collisionality-dependent; every CLEAN branch (collisional s=1, collisionless
    vacuum s≈2) is ≥1. The collisionless-thermal branch is a δ(ω) (no exponent yet)."""
    rows = fm.cross_branch_map()
    clean = [r for r in rows if r["geq1"] is True]
    assert len(clean) == 2
    assert all(r["geq1"] for r in clean)
    assert any(r["geq1"] is None for r in rows)        # the δ(ω) branch, honestly flagged


def test_sub_ohmic_forbidden_by_masslessness():
    """The one robust leg: s<1 needs an IR-enhanced DOS masslessness forbids."""
    assert fm.sub_ohmic_is_forbidden()["forbidden"] is True


def test_single_pole_is_pending_review_with_a_settle_target():
    """single_pole re-tiered DERIVED → PENDING_REVIEW; the gate passes and it names the finite-T
    computation that would settle it (the de-graduate/graduate condition)."""
    c = REGISTRY["constitutive_law_single_pole"]
    assert c.tier == gate.Tier.PENDING_REVIEW
    assert c.target and "finite-T" in c.target
    assert validate(REGISTRY) == []


def test_pending_review_caps_derived_consumer():
    """The new tier carries the anti-laundering bite: a DERIVED claim may NOT consume a
    PENDING_REVIEW input — proof the gate treats 'argued but unsettled' as not-yet-usable."""
    reg = copy.copy(REGISTRY)
    reg["would_launder"] = Claim(
        "would_launder", "a result 'derived' from an unsettled argument", Tier.DERIVED,
        inputs=("constitutive_law_single_pole",), derivation_ref="x", check=lambda: True,
        step=Step.DERIVE, novelty=Novelty.ORIGINAL)
    v = validate(reg)
    assert any("anti-laundering" in m and "would_launder" in m for m in v), v


def test_pending_review_requires_a_target():
    """A PENDING_REVIEW claim with no settle-target is a gate violation (like OPEN)."""
    reg = copy.copy(REGISTRY)
    reg["pend_no_target"] = Claim("pend_no_target", "argued, no settle condition",
                                  Tier.PENDING_REVIEW)
    assert any("PENDING-REVIEW must name a computable target" in m for m in validate(reg))
