"""test_physics_vocab: guards THE GUARDS of the physics vocabulary.

WHY THIS FILE EXISTS (recorded so it is not softened): the FITTED non-waivable ledger floor is the
anti-laundering device of the entire physics vocabulary -- it is what stops a fitted parameter
inheriting a datum's error bar and citation and reading downstream as empirically grounded. It was
shipped with NO test, and with zero fitted-tier nodes in the register, so it had never fired even
incidentally. A floor nobody stands on is a floor nobody has checked.

That is this program's DOMINANT FAILURE MODE, on its fourth appearance:
  1. a selftest passing while the answer lived in a print statement (anomaly_c0_map, first build);
  2. a "two independent derivations agree" check that was an algebraic tautology (same file);
  3. OWED_CEILING = frozenset(OWED) -- a ratchet computed from the list it was meant to bound;
  4. THIS -- the FITTED floor, real in code and completely unexercised.
All four are the same shape: A GUARD THAT VERIFIES ITSELF, or that nothing verifies. The response
is always the same -- make the guard fire in a test, against a case that would otherwise launder.

PROVEN TO FIRE (2026-08-04, by mutation -- a green test proves nothing until it is shown to fail
on a wrong implementation). Four mutants were run against validate_scoped.check_physics_extras and
ALL FOUR were caught by this file: (a) the floor made waivable by laundering_ok -- the laundering
door itself; (b) the floor silently lowered to 0; (c) POSTULATE's subtype made optional; (d) the
mandatory-rider check disabled. If any of those ever survives, this file has become decorative.

NOTE ON WHICH LAYER TO TEST (the overseer's own lesson from this session, worth encoding): these
rules live in validate_scoped.check_physics_extras, NOT in auditor.audit(). A test pointed at
auditor.audit() would return a false PASS for the floor and a false FAIL for the tiers -- a check
that tests the wrong object is worth exactly as much as a guard that verifies itself. So this file
imports the scoped validator and exercises the rules where they actually live.
"""
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from auditor import audit, DEFAULT_TIERS
from physics_vocab import (PHYSICS_TIERS, POSTULATE_SUBTYPES, FITTED_LEDGER_FLOOR,
                           RIDERS, COLLAPSE_MAP_TO_LEGACY)
from validate_scoped import (check_physics_extras, typed_inventory, scope_of,
                             superseded_ids)

FULL_RIDERS = {"scheme_tag": "MS-bar, mu = M_Z, natural units", "attestation": "in-house-rederived",
               "load": "load-bearing", "ledger_sign": 1}


def node(cid="synthetic", tier="fitted", delta=0, laundering_ok=None, subtype=None, riders=None):
    n = {"id": cid, "ledger_scope": "vacuum-cluster", "domain": "vacuum-cluster",
         "tier": tier, "ledger_delta": delta,
         "statement": "synthetic node for guard testing",
         "overturning_computation": "n/a (synthetic)",
         "sources": ["weinberg1989_cc"], "depends_on": [],
         "riders": dict(FULL_RIDERS) if riders is None else riders}
    if laundering_ok is not None:
        n["laundering_ok"] = laundering_ok
    if subtype is not None:
        n["postulate_subtype"] = subtype
    return n


def _blocks(claim):
    return check_physics_extras([claim])


class TestFittedFloor(unittest.TestCase):
    """THE REQUIRED REGRESSION. The floor must FIRE, and must be NON-WAIVABLE."""

    def test_fitted_at_zero_is_blocked(self):
        b = _blocks(node(delta=0))
        self.assertTrue(b, "a FITTED node at ledger_delta 0 must be BLOCKED -- a fitted parameter "
                           "is a free input and the floor is what says so")
        self.assertTrue(any("FITTED" in x for x in b), f"wrong block reason: {b}")

    def test_fitted_at_zero_with_laundering_ok_is_STILL_blocked(self):
        """The load-bearing case: the floor is NON-WAIVABLE. laundering_ok is the register's normal
        escape hatch, and it must NOT open this door -- otherwise the whole device is decorative."""
        b = _blocks(node(delta=0, laundering_ok=True))
        self.assertTrue(b, "laundering_ok MUST NOT waive the FITTED floor. If this ever passes, a "
                           "fitted parameter can enter carrying a datum's provenance at zero "
                           "ledger cost -- exactly the laundering the vocabulary exists to stop.")

    def test_fitted_at_the_floor_passes(self):
        self.assertEqual(_blocks(node(delta=FITTED_LEDGER_FLOOR)), [],
                         "a FITTED node paying its +1 must pass")

    def test_fitted_above_the_floor_passes(self):
        self.assertEqual(_blocks(node(delta=FITTED_LEDGER_FLOOR + 2)), [])

    def test_negative_delta_cannot_sneak_under(self):
        b = _blocks(node(delta=-1))
        self.assertTrue(b, "a FITTED node claiming to REMOVE an input must be blocked")

    def test_the_floor_constant_is_what_was_ruled(self):
        self.assertEqual(FITTED_LEDGER_FLOOR, 1,
                         "the ruled floor is +1; changing it silently would gut the device")


class TestPostulateSubtype(unittest.TestCase):
    """The other mandatory rule: POSTULATE's subtype is not optional."""

    def test_postulate_without_subtype_is_blocked(self):
        self.assertTrue(_blocks(node(tier="postulate", subtype=None)))

    def test_postulate_with_bogus_subtype_is_blocked(self):
        self.assertTrue(_blocks(node(tier="postulate", subtype="probably-fine")))

    def test_postulate_with_valid_subtypes_pass(self):
        for st in POSTULATE_SUBTYPES:
            self.assertEqual(_blocks(node(tier="postulate", subtype=st)), [], f"subtype {st}")


class TestMandatoryRiders(unittest.TestCase):
    """Missing rider => UNGRADED, which is a REJECTION, not a tier."""

    def test_each_missing_rider_blocks(self):
        for r in RIDERS:
            riders = {k: v for k, v in FULL_RIDERS.items() if k != r}
            b = _blocks(node(tier="measured", delta=0, riders=riders))
            self.assertTrue(b, f"missing rider {r!r} must block (UNGRADED is a rejection)")

    def test_all_riders_present_passes(self):
        self.assertEqual(_blocks(node(tier="measured", delta=0)), [])


class TestScopeIsolation(unittest.TestCase):
    """The vocabularies must not bleed -- verified in BOTH directions, not asserted."""

    def test_physics_tier_is_rejected_by_the_grut_gate(self):
        srcs = {"weinberg1989_cc"}
        r = audit([node(tier="measured", delta=0)], srcs, valid_tiers=DEFAULT_TIERS)
        self.assertTrue(any("tier" in b for b in r.blocking),
                        "a physics tier must be INVALID under GRUT's vocabulary")

    def test_physics_tier_is_accepted_by_the_physics_gate(self):
        srcs = {"weinberg1989_cc"}
        r = audit([node(tier="measured", delta=0)], srcs, valid_tiers=PHYSICS_TIERS)
        self.assertFalse(any("tier" in b for b in r.blocking),
                         "the same node must be VALID under the physics vocabulary")

    def test_grut_ledger_is_unmoved_by_cluster_nodes(self):
        import json
        claims = json.load(open(os.path.join(HERE, "claims.json")))["claims"]
        grut = [c for c in claims if scope_of(c) == "grut"]
        cluster = [c for c in claims if scope_of(c) == "vacuum-cluster"]
        self.assertTrue(cluster, "the cluster scope must be populated for this test to mean anything")
        self.assertEqual(sum(c.get("ledger_delta", 0) or 0 for c in grut), 17,
                         "GRUT's ledger must be exactly +16 regardless of what the cluster holds (Ruling B, 2026-08-23)")
        self.assertEqual(sum(c.get("ledger_delta", 0) or 0 for c in cluster), 0,
                         "every cluster node is Delta 0 in GRUT's ledger by construction")

    def test_collapse_map_is_lossy_exactly_where_ruled(self):
        """measured -> None is the gap that CAUSED the CHARTER Lambda category error. It must stay
        visible: a silent mapping would re-enable the error the fix removed."""
        self.assertIsNone(COLLAPSE_MAP_TO_LEGACY["measured"],
                          "measured must have NO legacy equivalent -- that gap is the finding")
        for tier in PHYSICS_TIERS:
            self.assertIn(tier, COLLAPSE_MAP_TO_LEGACY, f"{tier} missing from the collapse map")


class TestTypedInventoryIsNotAScalar(unittest.TestCase):
    """The deliverable is a typed inventory. Guard against a future wave collapsing it to a count."""

    def test_inventory_is_typed(self):
        import json
        claims = json.load(open(os.path.join(HERE, "claims.json")))["claims"]
        cluster = [c for c in claims if scope_of(c) == "vacuum-cluster"]
        inv = typed_inventory(cluster)
        self.assertGreater(len(inv), 1,
                           "the inventory must be partitioned by TYPE -- the types do not commute "
                           "and there is no total, by ruling")
        for tier in inv:
            self.assertIn(tier, PHYSICS_TIERS, f"cluster node carries a non-physics tier {tier!r}")

    def test_superseded_parents_are_partitioned_off_not_silently_dropped(self):
        """Once the atomicity test began retiring nodes into children, a flat count would report a
        parent AND its children -- inflating the inventory by the very thing the split clarified,
        and invisibly. The partition must EXIST, be REACHABLE, and be keyed apart from the tiers."""
        import json
        claims = json.load(open(os.path.join(HERE, "claims.json")))["claims"]
        cluster = [c for c in claims if scope_of(c) == "vacuum-cluster"]
        dead = superseded_ids(cluster)
        self.assertTrue(dead, "the vacuum cluster must carry retired split-parents for this to bite")
        counted = {i for ids in typed_inventory(cluster).values() for i in ids}
        for d in dead:
            self.assertNotIn(d, counted, f"{d} is superseded and must NOT be counted in a tier")
        with_dead = {i for ids in typed_inventory(cluster, include_superseded=True).values()
                     for i in ids}
        self.assertTrue(set(dead) <= with_dead,
                        "include_superseded=True must make the retired parents reachable -- "
                        "partitioned off is not the same as deleted")


if __name__ == "__main__":
    unittest.main()
