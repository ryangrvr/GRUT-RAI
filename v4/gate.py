"""GRUT-RAI v4.1 — PRINCIPLE 0: the tier gate. The gate IS the product.

Every claim passes through this gate. The gate mechanizes the anti-laundering
rules so that no claim can be tier DERIVED unless it genuinely is — checked, and
not built on an open gap. `ci_check.py` fails the build on any violation.

Tier semantics
--------------
- AXIOM/ANCHOR are the load-bearing INPUTS, entered visibly. The CTP action and
  the measured scales (τ₀, τ_micro) are ANCHOR; deriving FROM them is allowed.
- DERIVED means: has a derivation_ref AND a passing runnable check AND a novelty
  tag, AND consumes NO OPEN/CONJECTURAL input (the anti-laundering rule). It MAY
  consume ANCHOR inputs, but every such consumption is force-surfaced as a SPLIT
  in the audit — never silently promoted.
- A DERIVED claim whose *transitive* input closure touches an OPEN is reported
  PROVISIONAL ("rests on OPEN: X") — true content, but contingent until X closes.

Design note (deviation from the brief, flagged): the brief's literal rule
"consumes an OPEN/ANCHOR input ⇒ not DERIVED" would empty the DERIVED set, since
Q and μ_linear=1 derive from the action (an ANCHOR). The hard bite is therefore
on OPEN/CONJECTURAL inputs; ANCHOR-consumption is allowed-but-surfaced.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Optional, Dict, List, Set, Tuple


class Tier(str, Enum):
    ANCHOR = "ANCHOR"            # a load-bearing input: the action, or a measured/adopted scale (τ₀, τ_micro)
    DERIVED = "DERIVED"          # computed + checked, consuming no OPEN/CONJECTURAL/PENDING input
    HOSTED = "HOSTED"            # received from outside (SM content), or a result built on an OPEN input
    FORBIDDEN = "FORBIDDEN"      # ruled out by the framework's own axioms (a no-go theorem)
    OPEN = "OPEN"               # no mechanism yet; attackable; MUST name a computable target
    CONJECTURAL = "CONJECTURAL"  # a structural hook only, far from derivation
    # a derivation-grade ARGUMENT that does not yet pass a SETTLING check — the deciding
    # computation or external adjudication is outstanding. NOT DERIVED (the check would settle
    # it), NOT OPEN (there IS a mechanism). Added 2026-06-24 on a reviewer's recommendation, to
    # hold a claim like single-pole-ness: argued s≥1 across branches, exact exponent open.
    PENDING_REVIEW = "PENDING-REVIEW"  # MUST name a target (the open computation that settles it)


class Novelty(str, Enum):
    ORIGINAL = "GRUT-ORIGINAL"
    REUSED = "KNOWN-REUSED"
    COMPOSITION = "NEW-COMPOSITION"


class Step(str, Enum):
    DERIVE = "DERIVE"   # the rung is computed forward from the action + anchors (new content)
    PLACE = "PLACE"     # a known result fitted into the structure (legitimate, not a derivation)


# Tiers that, appearing as a DIRECT input, hard-block a consumer from being DERIVED.
# PENDING_REVIEW caps too: a DERIVED claim may not rest on an argued-but-unsettled input.
_CAPPING = (Tier.OPEN, Tier.CONJECTURAL, Tier.PENDING_REVIEW)
# Tiers that, anywhere in the transitive closure, make a DERIVED claim PROVISIONAL.
_PROVISIONAL = (Tier.OPEN, Tier.CONJECTURAL, Tier.PENDING_REVIEW)


@dataclass
class Claim:
    id: str
    statement: str
    tier: Tier
    inputs: Tuple[str, ...] = ()
    derivation_ref: Optional[str] = None
    check: Optional[Callable[[], bool]] = None   # runnable; returns True iff the claim's check passes
    check_ref: Optional[str] = None              # human pointer to where the check lives
    blocker_id: Optional[str] = None
    resolved: bool = False
    step: Optional[Step] = None                  # DERIVE vs PLACE (forward rungs)
    novelty: Optional[Novelty] = None            # required on DERIVED
    novelty_cite: Optional[str] = None           # required if novelty is REUSED/COMPOSITION
    target: Optional[str] = None                 # required on OPEN: the computable target that would close it
    axiom: bool = False                          # True for the foundational action: deriving FROM it is clean, not a SPLIT
    notes: str = ""


def transitive_inputs(reg: Dict[str, Claim], cid: str) -> Set[str]:
    """All claim ids reachable through the inputs[] graph from `cid` (excluding cid)."""
    seen: Set[str] = set()
    stack = list(reg[cid].inputs) if cid in reg else []
    while stack:
        x = stack.pop()
        if x in seen or x not in reg:
            continue
        seen.add(x)
        stack.extend(reg[x].inputs)
    return seen


def provisional_on(reg: Dict[str, Claim], cid: str) -> List[str]:
    """OPEN/CONJECTURAL claims in cid's transitive closure — why a DERIVED claim is provisional."""
    return sorted(i for i in transitive_inputs(reg, cid)
                  if reg[i].tier in _PROVISIONAL)


def anchored_inputs(reg: Dict[str, Claim], cid: str) -> List[str]:
    """Direct measured-VALUE ANCHOR inputs a DERIVED claim consumes — surfaced as a
    SPLIT (mechanism derived, value anchored), never silent. The foundational axiom
    (axiom=True) is excluded: deriving FROM the action is what DERIVED means."""
    return sorted(i for i in reg[cid].inputs
                  if i in reg and reg[i].tier == Tier.ANCHOR and not reg[i].axiom)


def validate(reg: Dict[str, Claim]) -> List[str]:
    """Return the list of gate violations. Empty ⇒ the gate passes. ci_check raises on non-empty."""
    V: List[str] = []
    def err(c: Claim, msg: str) -> None:
        V.append(f"[{c.id}] {msg}")

    ids = set(reg)
    for c in reg.values():
        for inp in c.inputs:
            if inp not in ids:
                err(c, f"input '{inp}' not in registry")

        if c.tier == Tier.DERIVED:
            # Rule 1 — DERIVED requires a derivation_ref AND a passing runnable check.
            if not c.derivation_ref:
                err(c, "DERIVED requires a derivation_ref")
            if c.check is None:
                err(c, "DERIVED requires a runnable check (check=)")
            else:
                try:
                    if c.check() is not True:
                        err(c, "DERIVED check did not return True")
                except Exception as e:  # a check that raises is a failed check
                    err(c, f"DERIVED check raised: {e!r}")
            # Rule 3 — novelty tag required on DERIVED; citation required if reused/composed.
            if c.novelty is None:
                err(c, "DERIVED requires a novelty tag")
            elif c.novelty in (Novelty.REUSED, Novelty.COMPOSITION) and not c.novelty_cite:
                err(c, f"novelty {c.novelty.value} requires a citation (novelty_cite=)")
            # Rule 2 — anti-laundering: a DERIVED claim may not CONSUME an OPEN/CONJECTURAL input.
            for inp in c.inputs:
                if inp in reg and reg[inp].tier in _CAPPING:
                    err(c, f"anti-laundering: DERIVED consumes {reg[inp].tier.value} input "
                           f"'{inp}' — cap at HOSTED/OPEN until '{inp}' closes")

        # Rule 4 — OPEN (and PENDING_REVIEW) must name the computable target that would settle it.
        if c.tier in (Tier.OPEN, Tier.PENDING_REVIEW) and not c.target:
            err(c, f"{c.tier.value} must name a computable target (target=) that would settle it")

        # Rule 5 — RESOLVED only if its blocker is closed.
        if c.resolved and c.blocker_id:
            b = reg.get(c.blocker_id)
            if b is None:
                err(c, f"blocker '{c.blocker_id}' not in registry")
            elif b.tier in _PROVISIONAL:
                err(c, f"cannot be RESOLVED while blocker '{c.blocker_id}' is {b.tier.value}")
    return V
