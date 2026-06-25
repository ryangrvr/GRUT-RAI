"""GRUT-RAI v4.1 — tests for TARGET 5 (bath_collisionality.py): a FAILED resolution attempt, kept
as an honest record. These pin the verified reasons it fails — so the memory-character route is not
retried as if it worked. Single-pole stays an ANCHOR; the fork is unresolved; the only resolution is
the z·T_TT vertex computation.
"""
from __future__ import annotations

from v4.targets import bath_collisionality as bc
from v4 import gate
from v4.registry import REGISTRY


def test_grut_own_chi_mem_rings_when_underdamped():
    """GRUT's own viscoelastic χ_mem is monotone overdamped (τ_K<τ₀/4) but RINGS underdamped
    (τ_K>τ₀/4) — so 'viscoelastic' does NOT entail monotone memory (pre-screen B2/B3)."""
    assert bc.memory_sign_changes(bc.chi_mem_kernel(tauK=0.1)) == 0     # overdamped: monotone
    assert bc.memory_sign_changes(bc.chi_mem_kernel(tauK=1.0)) > 5      # underdamped: rings


def test_sign_change_discriminator_is_unsound():
    """The fatal catch: the monotone-vs-oscillatory test MISCLASSIFIES GRUT's own underdamped
    (collisional) χ_mem as free-streaming. The discriminator is unsound (it only 'works' in the
    overdamped τ_K<τ₀/4 regime, which is already the single-pole answer)."""
    assert bc.sign_change_discriminator_is_unsound() is True


def test_envelope_is_the_real_distinction():
    """The real separator is the envelope class: χ_mem has an EXPONENTIAL envelope (collisional),
    Weinberg has a POWER-LAW envelope (free-streaming) — but reading it needs GRUT's actual kernel."""
    exp_rate, _ = bc.envelope_logslopes(bc.chi_mem_kernel(1.0))
    _, powerlaw_slope = bc.envelope_logslopes(bc.free_streaming_memory())
    assert exp_rate > 0.2                       # χ_mem decays exponentially (rate ~1/2τ_K)
    assert 2.0 < powerlaw_slope < 4.0           # Weinberg ~ t^-3 power-law envelope


def test_single_pole_unresolved_remains_anchor():
    """The attempt did NOT buy single-pole: it stays an ANCHOR, the fork is unresolved, and the
    registry never banked a 'resolution' claim (bath_collisionality is a standalone record, not a
    registry claim)."""
    assert REGISTRY["constitutive_law_single_pole"].tier == gate.Tier.ANCHOR
    assert "bath_collisionality" not in " ".join(REGISTRY.keys())
    assert len(bc.residual_dials()) == 3        # measure-zero corner of 3 dials, not less free
