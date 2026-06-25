"""GRUT-RAI v4.1 — tests for TARGET 3 (deborah_scaling.py), CORRECTED after an adversarial
pre-screen. The honest content: a dividing scale L*=c_s·τ exists ONLY on the single-τ (Maxwell /
collisional) branch; the power-law / free-streaming branch is scale-free (no L*). So the mechanism
does NOT bypass the kernel fork — it presupposes the collisional side, and the two branches predict
different scale-structure (an observable handle on the fork). The character discriminant is
DEGENERATE. The claim is HOSTED/PLACE (a definitional substitution), not DERIVED.
"""
from __future__ import annotations

from v4.targets import deborah_scaling as ds
from v4 import gate
from v4.registry import REGISTRY


def test_dividing_scale_only_on_single_tau_branch():
    """L* exists for Maxwell/multi-mode (a single/finite τ); it is None for power-law (scale-free,
    no characteristic time) — crossover_scale refuses to manufacture a fictitious L* (pre-screen C-C)."""
    assert ds.crossover_scale(1.0, 3e10, "maxwell") == 3e10
    assert ds.crossover_scale(1.0, 3e10, "multi_mode") == 3e10
    assert ds.crossover_scale(1.0, 3e10, "power_law") is None
    assert ds.has_dividing_scale("maxwell") and not ds.has_dividing_scale("power_law")


def test_crossover_scale_linear_in_free_cs():
    """L* = c_s·τ — symbolic only, a function of the FREE parameter c_s; no physical scale computed."""
    assert ds.crossover_scale(2.0, 30.0) == 10 * ds.crossover_scale(2.0, 3.0)


def test_peak_counter_fixed_three_modes_reads_three():
    """The pre-screen (C-B) caught the non-strict-tie over-count: 3 modes read 4. Fixed → 3."""
    assert ds.rheology_character("multi_mode")["loss_peaks"] == 3


def test_character_clean_limits():
    """Clean-limit character: Maxwell one crossover, power-law scale-free, multi-mode a hierarchy."""
    assert ds.rheology_character("maxwell")["loss_peaks"] == 1
    p = ds.rheology_character("power_law")
    assert p["loss_peaks"] == 0 and p["tan_delta_logspread"] < 0.2 and "scale-free" in p["character"]
    assert ds.rheology_character("multi_mode")["loss_peaks"] >= 2


def test_discriminant_is_degenerate():
    """The kernel→character map is many-to-one (closely-spaced multi-mode mimics Maxwell; a continuum
    mimics power-law) — so it does NOT invert to a unique kernel (pre-screen C-B/C-C). Disclosed, not hidden."""
    assert ds.discriminant_is_degenerate() is True


def test_banked_claim_is_the_discriminant_not_the_algebra():
    """What is banked is the branch CONTRAST (rheology_scale_discriminant), HOSTED/PLACE — a
    definitional substitution of two anchors, NOT 'De runs with scale' as a derivation (reviewer's
    flag: a definition must not wear a target's clothes). The contentful forward claim is the
    OUTWARD power_spectrum_branch_test, not the algebra."""
    c = REGISTRY["rheology_scale_discriminant"]
    assert c.tier == gate.Tier.HOSTED and c.step == gate.Step.PLACE and c.check is None
    assert "relaxation_kernel" in c.inputs
    assert "deborah_runs_with_scale" not in REGISTRY    # renamed away from the algebra
    assert gate.validate(REGISTRY) == []


def test_persistent_memory_is_conjectural_with_tension():
    """The 'remembers ever since' claim was lifted OUT of the closure anchor to a CONJECTURAL claim
    that states the coarse-grained-dissipation tension loudly (reviewer's C-D follow-up) — not a
    wording fix smoothed into an anchor."""
    assert REGISTRY["persistent_memory_conjecture"].tier == gate.Tier.CONJECTURAL
    assert "ENERGY" in REGISTRY["closure_condition"].statement   # closure trimmed to energy/closed


def test_spine_four_inputs_are_anchors():
    for cid in ("relaxation_kernel", "closure_condition", "driving_strain", "scale_coupling"):
        assert REGISTRY[cid].tier == gate.Tier.ANCHOR
