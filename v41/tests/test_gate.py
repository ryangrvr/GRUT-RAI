"""GRUT-RAI v4.1 — proof that the gate WORKS.

It is not enough that the gate passes on the honest registry; it must REJECT a
laundered claim. These tests build deliberately-bad claims and assert the gate
catches each one. This is the executable evidence behind Principle 0 — the only
kind of evidence that counts (not "it sounded rigorous", not agent consensus).
"""
from __future__ import annotations

import copy

from v41.gate import Claim, Tier, Novelty, Step, validate
from v41.registry import REGISTRY


def _clone():
    return copy.copy(REGISTRY)  # shallow: claims are immutable enough for these tests


def test_honest_registry_passes():
    assert validate(REGISTRY) == [], validate(REGISTRY)


def test_laundering_open_input_rejected():
    """A DERIVED claim that CONSUMES an OPEN input must be rejected. Built on a SYNTHETIC OPEN
    claim so the test is independent of which live claims happen to be OPEN (α/single-pole are
    now anchors — the gate-logic test must still stand)."""
    reg = _clone()
    reg["synthetic_open"] = Claim("synthetic_open", "an open gap", Tier.OPEN,
                                  target="some computable target")
    reg["laundered"] = Claim(
        "laundered", "result 'derived' from an open gap.", Tier.DERIVED,
        inputs=("synthetic_open", "tau0"),
        derivation_ref="x", check=lambda: True, step=Step.DERIVE,
        novelty=Novelty.ORIGINAL)
    v = validate(reg)
    assert any("anti-laundering" in m and "laundered" in m for m in v), v


def test_derived_requires_passing_check():
    reg = _clone()
    reg["no_check"] = Claim("no_check", "claims derived, no check", Tier.DERIVED,
                            inputs=("ctp_action",), derivation_ref="x",
                            check=None, novelty=Novelty.ORIGINAL)
    reg["bad_check"] = Claim("bad_check", "check returns False", Tier.DERIVED,
                             inputs=("ctp_action",), derivation_ref="x",
                             check=lambda: False, novelty=Novelty.ORIGINAL)
    v = validate(reg)
    assert any("requires a runnable check" in m for m in v), v
    assert any("did not return True" in m for m in v), v


def test_derived_requires_novelty():
    reg = _clone()
    reg["no_nov"] = Claim("no_nov", "derived, no novelty tag", Tier.DERIVED,
                          inputs=("ctp_action",), derivation_ref="x",
                          check=lambda: True, novelty=None)
    assert any("requires a novelty tag" in m for m in validate(reg))


def test_reused_requires_citation():
    reg = _clone()
    reg["reused_no_cite"] = Claim("reused_no_cite", "reused, no cite", Tier.DERIVED,
                                  inputs=("ctp_action",), derivation_ref="x",
                                  check=lambda: True, novelty=Novelty.REUSED)
    assert any("requires a citation" in m for m in validate(reg))


def test_open_requires_target():
    reg = _clone()
    reg["open_no_target"] = Claim("open_no_target", "open, no target", Tier.OPEN)
    assert any("must name a computable target" in m for m in validate(reg))


def test_resolved_over_open_blocker_rejected():
    reg = _clone()
    reg["synthetic_open"] = Claim("synthetic_open", "an open gap", Tier.OPEN,
                                  target="some computable target")
    reg["premature"] = Claim("premature", "claims resolved over an open blocker",
                             Tier.HOSTED, blocker_id="synthetic_open", resolved=True)
    assert any("cannot be RESOLVED while blocker" in m for m in validate(reg))


def test_missing_input_rejected():
    reg = _clone()
    reg["dangling"] = Claim("dangling", "input does not exist", Tier.HOSTED,
                            inputs=("no_such_claim",))
    assert any("not in registry" in m for m in validate(reg))
