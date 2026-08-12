"""test_consumed_by: makes the zeta_interior_family armed trigger's PRECONDITION checkable.

WHY (overseer ruling 2026-08-09): the Delta-0 warrant on the c0-collapse was corrected from a
CONDITION ("nothing result-tier rests on it" -- which fired eight days after it was written) to a
CRITERION ("booking happens at ACCEPTANCE"). The safety of that ruling is an armed trigger: if any
collapse-consuming artifact is ever accepted, the booking is re-audited. But the trigger named an
artifact THE DEPENDENCY GRAPH CANNOT SEE -- the frozen gate is a calc, not a register node, so
zeta_interior_family had zero inbound edges and 'executed not re-litigated' reduced to 'someone
will remember'. That is the edge-blindness finding one layer out: closed for omission nodes
(test_sweep_ledger), open for CALC-CONSUMERS. This file closes it.

The register now carries a structured `consumed_by` on the node; this test FAILS if any listed
consumer's status becomes anything but held/non-banking. A failure here IS the trigger firing:
the correct response is the re-audit the warrant promises, never an edit to this file's whitelist.

Proven to fire by mutation (in-test, against a copied record): a consumer status flipped to
'accepted' must FAIL the check. Ninth-instance rule: a guard is only real if something fails.
"""
import copy
import json
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

# The ONLY statuses under which the Delta-0 warrant holds. Anything else -- 'accepted', 'banked',
# 'graduated', a typo, a new invented grade -- fails, and failing is the point: acceptance is the
# event the armed trigger fires on, and an unrecognized status is treated as acceptance-like
# (fail-closed), never waved through.
NON_ACCEPTED_STATUSES = {"held-at-flag", "non-banking-screen"}


def _node():
    claims = json.load(open(os.path.join(HERE, "claims.json")))["claims"]
    return next(c for c in claims if c["id"] == "zeta_interior_family")


def _check(node):
    """Returns a list of blocking reasons; empty == the warrant's precondition holds."""
    bad = []
    consumers = node.get("consumed_by") or []
    if not consumers:
        bad.append("zeta_interior_family has no consumed_by registry -- the armed trigger's "
                   "precondition is unrecorded and 'executed not re-litigated' is prose again")
    for c in consumers:
        art, status = c.get("artifact"), c.get("status")
        if not art or not os.path.exists(os.path.join(HERE, "..", art)):
            bad.append(f"consumed_by names {art!r}, which does not exist on disk -- a registry of "
                       f"phantom consumers checks nothing")
        if status not in NON_ACCEPTED_STATUSES:
            bad.append(f"consumed_by[{art}] status is {status!r} -- NOT a held/non-banking grade. "
                       f"THE ARMED TRIGGER HAS FIRED: the Delta-0 warrant's precondition no longer "
                       f"holds and the c0-collapse booking must be RE-AUDITED for a dial at this "
                       f"acceptance (see the node's ledger_note). Do not edit this whitelist; "
                       f"execute the re-audit.")
    return bad


class TestConsumedBy(unittest.TestCase):

    def test_the_registry_exists_and_names_both_known_consumers(self):
        arts = {c["artifact"] for c in _node().get("consumed_by") or []}
        self.assertIn("calc/isw_tt_auto.py", arts, "the frozen gate is the consumer that fired "
                                                   "the old warrant; it must be registered")
        self.assertIn("calc/sigma0_anomaly_screen.py", arts)

    def test_the_precondition_holds_today(self):
        self.assertEqual(_check(_node()), [])

    def test_an_accepted_consumer_FIRES_the_trigger(self):
        """THE MUTATION: flip one status to 'accepted' -- the check must fail and must say the
        trigger has fired, naming the re-audit."""
        m = copy.deepcopy(_node())
        m["consumed_by"][0]["status"] = "accepted"
        bad = _check(m)
        self.assertTrue(any("ARMED TRIGGER HAS FIRED" in b for b in bad), bad)

    def test_an_unknown_status_fails_closed(self):
        """A new invented grade must not slip past as not-technically-accepted."""
        m = copy.deepcopy(_node())
        m["consumed_by"][0]["status"] = "provisionally-fine"
        self.assertTrue(_check(m), "an unrecognized status must fail closed")

    def test_a_phantom_consumer_fails(self):
        m = copy.deepcopy(_node())
        m["consumed_by"][0]["artifact"] = "calc/does_not_exist.py"
        self.assertTrue(any("does not exist on disk" in b for b in _check(m)))

    def test_the_warrant_is_criterion_based_and_cites_this_file(self):
        """The ledger_note must carry the corrected warrant (criterion + trigger) and point here --
        a checkable precondition nobody can find is a remembered one."""
        note = _node()["ledger_note"]
        for phrase in ("booking happens at ACCEPTANCE", "ARMED TRIGGER", "test_consumed_by.py",
                       "WARRANT CORRECTED 2026-08-09"):
            self.assertIn(phrase, note)
        self.assertNotIn("BECAUSE nothing result-tier rests on it", note,
                         "the fired condition-based warrant must be gone, not coexisting")


if __name__ == "__main__":
    unittest.main()
