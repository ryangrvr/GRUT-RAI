"""GRUT-RAI v4.1 — tests for TARGET 1D after round 3 of external review. The DOS/phase-space
framing (rounds 1–2) was the wrong object; the right object is the finite-T TT transport memory,
which FORKS on collisionality. Collisional ⇒ exponential ⇒ single-pole holds; free-streaming ⇒
Weinberg non-local Bessel-tail ⇒ single-pole fails. Collisionality is the free datum ⇒ ANCHOR
(the 1C conclusion, vindicated).
"""
from __future__ import annotations

from v4.targets import fast_mode_dos as fm
from v4 import gate
from v4.registry import REGISTRY


def test_collisional_branch_is_single_pole():
    """An exponential (viscous/Kubo) memory kernel is Markovian ⇒ single-pole holds."""
    d = fm.kernel_is_single_pole(lambda s: fm.collisional_kernel(s, 1.0))
    assert d["single_pole"] is True
    assert d["sign_changes"] == 0


def test_free_streaming_branch_fails_single_pole():
    """The free-streaming (Weinberg) TT kernel is power-law and oscillatory (Bessel tail) ⇒ NOT
    single-pole. This is the slow branch realized concretely — the opposite of 'every branch ≥1'."""
    d = fm.kernel_is_single_pole(fm.free_streaming_kernel)
    assert d["single_pole"] is False
    assert d["sign_changes"] > 5                      # oscillatory long memory
    assert -3.5 < d["envelope_loglog_slope"] < -2.5   # ~s^-3 power law, not exponential


def test_the_fork_holds_then_fails():
    """The two branches disagree: collisional HOLDS, free-streaming FAILS — so the verdict turns
    on collisionality, which the action does not fix."""
    fork = {b["branch"].split()[0]: b for b in fm.the_fork()}
    assert fork["collisional"]["verdict"] == "HOLDS"
    assert fork["collisionless"]["verdict"] == "FAILS"


def test_single_pole_is_anchor_collisionality_free():
    """single_pole reverted to ANCHOR (the 1C conclusion) — collisionality is the free datum; the
    gate passes; there is no leftover fast_mode_content scaffolding."""
    assert REGISTRY["constitutive_law_single_pole"].tier == gate.Tier.ANCHOR
    assert "fast_mode_content" not in REGISTRY
    assert gate.validate(REGISTRY) == []


def test_pending_review_tier_was_removed():
    """The PENDING_REVIEW tier (added round 2) was reverted — its framing was over-optimistic."""
    assert not hasattr(gate.Tier, "PENDING_REVIEW")
