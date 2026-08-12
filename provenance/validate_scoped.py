#!/usr/bin/env python3
"""validate_scoped: the SCOPED gate -- one register, several ledgers.

GRUT's ledger and the physics map's ledger must not contaminate each other. This is a FILTER plus a
per-scope tier vocabulary, not new machinery: auditor.audit() already accepts valid_tiers, and the
ledger is a blind sum over whatever list it is handed.

  * GRUT scope        -- the legacy vocabulary; its net must stay exactly where the overseer left it.
  * vacuum-cluster    -- the physics vocabulary (provenance/physics_vocab.py, ruled 2026-08-04);
                         every node is ledger_delta 0 IN GRUT'S LEDGER, and the cluster's own
                         output is a TYPED INVENTORY, not a scalar.

*** WHY NOT AN INTEGER (overseer ruling 2026-08-04): a count that sums a measured number, a
    proposition about the world, and a criterion with no truth-value has no honest gloss except
    the disclaimer, and an integer invites exactly the cross-cluster comparison the disclaimer
    forbids. The deliverable is the typed inventory with a count PER TYPE. ***
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from auditor import audit, DEFAULT_TIERS
from physics_vocab import PHYSICS_TIERS, POSTULATE_SUBTYPES, FITTED_LEDGER_FLOOR, RIDERS

SCOPES = {
    "grut": DEFAULT_TIERS,
    "vacuum-cluster": PHYSICS_TIERS,
}


def load():
    claims = json.load(open(os.path.join(HERE, "claims.json")))["claims"]
    sources = set(json.load(open(os.path.join(HERE, "sources.json"))).keys())
    return claims, sources


def scope_of(c):
    return c.get("ledger_scope", "grut")


def check_physics_extras(claims):
    """The rules the physics vocabulary adds on top of the shared auditor."""
    bad = []
    for c in claims:
        cid = c["id"]
        # POSTULATE's subtype is MANDATORY -- "is there a live published denial?" is a fact about
        # the world and the map's droppability column depends on it.
        if c["tier"] == "postulate":
            st = c.get("postulate_subtype")
            if st not in POSTULATE_SUBTYPES:
                bad.append(f"{cid}: postulate without a valid subtype ({st!r})")
        # FITTED's non-waivable floor -- the device that stops a fitted parameter inheriting a
        # datum's provenance. laundering_ok CANNOT lower it.
        if c["tier"] == "fitted" and (c.get("ledger_delta") or 0) < FITTED_LEDGER_FLOOR:
            bad.append(f"{cid}: FITTED must carry ledger_delta >= {FITTED_LEDGER_FLOOR} "
                       f"(non-waivable; laundering_ok does not apply)")
        # every quantitative claim needs its scheme; missing => UNGRADED, which is a REJECTION
        riders = c.get("riders") or {}
        for r in RIDERS:
            if r not in riders:
                bad.append(f"{cid}: missing mandatory rider {r!r} (UNGRADED is a rejection)")
    return bad


def typed_inventory(claims, include_superseded=False):
    """THE DELIVERABLE: counts per type, not a scalar.

    SUPERSEDED PARENTS ARE PARTITIONED OFF, NOT SILENTLY DROPPED (2026-08-04). Once the atomicity
    test began retiring nodes into children, a flat count would have reported a parent AND its two
    children -- inflating the inventory by exactly the thing the split was supposed to clarify. It
    would also have been INVISIBLE, since the number would merely have looked larger. Retired
    parents are returned under their own key so a reader sees them and cannot add them by accident.
    Same discipline as the two tallies (compounds / omissions) that are never summed."""
    inv = {}
    for c in claims:
        if c.get("disposition") == "superseded-by-split" and not include_superseded:
            continue
        inv.setdefault(c["tier"], []).append(c["id"])
    return inv


def superseded_ids(claims):
    """The retired-parent partition, returned SEPARATELY so typed_inventory stays keyed by TIER and
    nothing else. Returning it inside the inventory dict was the first attempt and a test caught it
    immediately: a non-tier key in a tier-keyed mapping is the same category-mixing this program
    refuses one level up, where the typed inventory exists precisely because types do not commute."""
    return [c["id"] for c in claims if c.get("disposition") == "superseded-by-split"]


def main():
    claims, sources = load()
    rc = 0
    for scope, vocab in SCOPES.items():
        subset = [c for c in claims if scope_of(c) == scope]
        if not subset:
            continue
        res = audit(subset, sources, valid_tiers=vocab)
        print("=" * 78)
        print(f"SCOPE: {scope}   ({len(subset)} nodes)")
        print(f"  net ledger (blind sum, THIS SCOPE ONLY): {res.net:+d}")
        if res.blocking:
            rc = 1
            print(f"  BLOCKING ({len(res.blocking)}):")
            for b in res.blocking[:12]:
                print("   -", b)
        else:
            print("  PASS: every claim tiered, sourced, falsifiable; no laundering.")
        if scope == "vacuum-cluster":
            extra = check_physics_extras(subset)
            if extra:
                rc = 1
                print(f"  PHYSICS-VOCAB BLOCKING ({len(extra)}):")
                for b in extra[:12]:
                    print("   -", b)
            inv = typed_inventory(subset)
            print("\n  THE TYPED INVENTORY (the deliverable -- NOT an integer):")
            for tier in ("measured", "derived", "fitted", "postulate", "heuristic", "open"):
                ids = inv.get(tier, [])
                if not ids:
                    continue
                print(f"    {tier:10s} x{len(ids):2d}  {', '.join(i[3:] for i in ids)}")
                if tier == "postulate":     # the CONTESTED/STANDARD split is mandatory, so show it
                    sub = {}
                    for i in ids:
                        c = next(x for x in subset if x["id"] == i)
                        sub.setdefault(c.get("postulate_subtype", "?"), []).append(i[3:])
                    for st in sorted(sub):
                        print(f"      -- {st:9s} x{len(sub[st]):2d}  {', '.join(sub[st])}")
            dead = superseded_ids(subset)
            if dead:
                # PRINTED, not merely excluded. A partition nobody can see is a silent drop, and a
                # silent drop is indistinguishable from an error in exactly the direction that
                # flatters the count.
                print(f"\n    RETIRED, NOT COUNTED (superseded by split) x{len(dead)}:  "
                      f"{', '.join(i[3:] for i in dead)}")
            drop = [c for c in subset if str(c.get("droppable", "")).startswith("DROPPABLE")]
            print(f"\n    droppable (an alternative formulation denies or omits it): {len(drop)}")
            print("    NOTE: the types do not commute. There is no total, by ruling.")
            print("    NOTE: compounds and omissions are SEPARATE TALLIES and are never summed --")
            print("          a compound is one node carrying two things (SPLIT it); an omission is")
            print("          a presupposition booked nowhere (ADD it). See OMISSION_STANDARD_v2.txt.")
    print("=" * 78)
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
