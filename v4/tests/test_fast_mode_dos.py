"""GRUT-RAI v4.1 — tests for TARGET 1D (fast_mode_dos.py) and the single_pole graduation.
Encode the post-review result: GRUT's committed massless fast modes have DOS ρ~ω² ⇒ s≥1
(super-Ohmic) ⇒ single-pole is a THEOREM (DERIVED, not anchored). The sub-Ohmic escape needs an
IR-enhanced DOS masslessness forbids; the §6 AH kernel is itself super-Ohmic (no §2/§6 tension).
"""
from __future__ import annotations

from v4.targets import fast_mode_dos as fm
from v4 import gate
from v4.registry import REGISTRY


def test_massless_dos_is_super_ohmic():
    """A massless field in 3+1D has DOS ρ(ω) ~ ω² — the edge relativity FIXES (not free)."""
    assert abs(fm.massless_dos_exponent(d_space=3) - 2.0) < 0.05


def test_J_exponents_are_super_ohmic():
    """Linear coupling ⇒ s=2; stress-tensor coupling ⇒ s=5. Both ≥ 1 ⇒ FAST/single-pole."""
    assert abs(fm.J_exponent("linear") - 2.0) < 0.05
    assert abs(fm.J_exponent("stress_tensor") - 5.0) < 0.1


def test_sub_ohmic_escape_needs_ir_enhanced_dos():
    """The only s<1 baths are IR-enhanced (non-relativistic / glassy) — masslessness excludes
    them. GRUT's committed bath is not among the slow cases."""
    rows = {r["bath"][:8]: r for r in fm.dos_edges_table()}
    grut = [r for r in fm.dos_edges_table() if "GRUT" in r["bath"]][0]
    assert grut["s"] >= 1.0
    assert all(r["s"] < 1.0 for r in fm.dos_edges_table() if "GRUT" not in r["bath"])


def test_ah_kernel_super_ohmic_resolves_sec6_tension():
    """§6's Anastopoulos–Hu kernel is super-Ohmic (s≈3); by FDT it always committed s≥1, so §2
    and §6 agree once §2 is corrected — the specialist's cleanest catch, resolved by agreement."""
    ah = fm.ah_kernel_is_super_ohmic()
    assert abs(ah["J_AH_exponent"] - 3.0) < 0.1
    assert abs(ah["J_recovered_exponent"] - ah["J_AH_exponent"]) < 0.1   # FDT identity closes


def test_gate_check_passes():
    """The runnable gate check returns True (s≥1 by both couplings, super-Ohmic DOS)."""
    assert fm.check_single_pole_super_ohmic() is True


def test_single_pole_graduated_to_derived():
    """single_pole is now DERIVED (graduated from ANCHOR), consuming the explicit fast_mode_content
    anchor, with a passing check; the gate still passes and renders it SPLIT."""
    c = REGISTRY["constitutive_law_single_pole"]
    assert c.tier == gate.Tier.DERIVED
    assert c.check() is True
    assert gate.validate(REGISTRY) == []
    assert "fast_mode_content" in gate.anchored_inputs(REGISTRY, "constitutive_law_single_pole")
    assert REGISTRY["fast_mode_content"].tier == gate.Tier.ANCHOR


def test_alpha_still_anchor_q_protection_only_alpha():
    """The α anchor holds (specialist-confirmed); the two-anchor symmetry was over-tight — only α
    is Q-protected now, and single-pole no longer is (it graduated)."""
    assert REGISTRY["alpha"].tier == gate.Tier.ANCHOR
    assert REGISTRY["constitutive_law_single_pole"].tier == gate.Tier.DERIVED
