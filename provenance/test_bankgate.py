"""Tests for the bank-time gate (bankgate.bank_gate) -- the change that makes the self-audit LIVE.

Locks: no-diff is CLEAN; a new born-open node FLAGs (never silent PASS, never BLOCK); re-opening a
closed disposition FLAGs (RE-OPENS); a laundering ledger bump BLOCKs; co-added claims resolve each
other's depends_on (no false unresolved BLOCK); net-ledger drift is reported.
"""
import copy
import json
import os
import unittest

from bankgate import bank_gate

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    with open(os.path.join(HERE, "claims.json")) as f:
        claims = json.load(f)["claims"]
    with open(os.path.join(HERE, "sources.json")) as f:
        sources = json.load(f)
    return claims, {k for k in sources if not k.startswith("_")}


def _open_node(cid, delta=0, deps=("rung1_inin_action",)):
    return {"id": cid, "statement": "A born-open / borrowed scaffold sub-claim.",
            "tier": "to-derive", "sources": ["kubo1966"],
            "overturning_computation": "a calc that would kill it", "ledger_delta": delta,
            "depends_on": list(deps)}


class TestBankGate(unittest.TestCase):
    def setUp(self):
        self.claims, self.source_ids = load()

    def test_no_diff_is_clean(self):
        rep = bank_gate(self.claims, self.claims, self.source_ids)
        self.assertEqual(rep["overall"], "CLEAN")
        self.assertEqual(rep["n_changed"], 0)
        self.assertEqual(rep["net_baseline"], rep["net_working"])

    def test_new_open_node_flags_not_blocks_and_keeps_net(self):
        working = copy.deepcopy(self.claims) + [_open_node("scaffold_demo")]
        rep = bank_gate(self.claims, working, self.source_ids)
        self.assertEqual(rep["overall"], "FLAG-FOR-FIREWALL")           # born-open -> surfaced, never silent
        self.assertEqual(rep["net_working"], rep["net_baseline"])        # zero-credit -> net unchanged
        self.assertTrue(any(r["claim_id"] == "scaffold_demo" and r["is_new"] for r in rep["flags"]))

    def test_reopen_closed_disposition_flags(self):
        working = copy.deepcopy(self.claims)
        target = next(c for c in working if c["id"] == "rung9b_bridge")  # disposition='settled-negative'
        target["disposition"] = ""                                       # re-open it
        rep = bank_gate(self.claims, working, self.source_ids)
        self.assertEqual(rep["overall"], "FLAG-FOR-FIREWALL")
        r = next(r for r in rep["flags"] if r["claim_id"] == "rung9b_bridge")
        self.assertTrue(any("RE-OPENS" in fl for fl in r["consistency_flags"]))

    def test_laundering_ledger_bump_blocks(self):
        working = copy.deepcopy(self.claims) + [
            {"id": "launder_demo", "statement": "We derived something for free.",
             "tier": "derived", "sources": ["kubo1966"], "overturning_computation": "a calc",
             "ledger_delta": 2, "depends_on": ["rung1_inin_action"]}]
        rep = bank_gate(self.claims, working, self.source_ids)
        self.assertEqual(rep["overall"], "BLOCK")
        self.assertTrue(any(r["claim_id"] == "launder_demo" for r in rep["blocks"]))

    def test_co_added_deps_resolve_no_false_block(self):
        # B depends on A; both are NEW in the same diff. The gate must resolve A for B (no unresolved BLOCK).
        a = _open_node("scaffold_A")
        b = _open_node("scaffold_B", deps=("scaffold_A",))
        working = copy.deepcopy(self.claims) + [a, b]
        rep = bank_gate(self.claims, working, self.source_ids)
        self.assertEqual(rep["overall"], "FLAG-FOR-FIREWALL")           # substantive, but NOT blocked
        self.assertEqual([r["claim_id"] for r in rep["blocks"]], [])

    def test_net_drift_reported(self):
        working = copy.deepcopy(self.claims) + [_open_node("plus_one", delta=1)]
        rep = bank_gate(self.claims, working, self.source_ids)
        self.assertEqual(rep["net_working"], rep["net_baseline"] + 1)

    def test_match_verdict_reword_is_substantive_and_flags(self):
        # GAP-CLOSED (the superfluid/KNOB-2 catch): a B1 match_verdict is a CLAIM-bearing payload; a reword
        # can pre-answer an open node it attaches_to, so it must FLAG-FOR-FIREWALL, not pass as CLEAN.
        working = copy.deepcopy(self.claims)
        target = next(c for c in working if c.get("id") == "superfluid_bec_media")
        target["match_verdict"] = target["match_verdict"] + " (an edited claim about the vacuum.)"
        rep = bank_gate(self.claims, working, self.source_ids)
        self.assertEqual(rep["overall"], "FLAG-FOR-FIREWALL")
        self.assertTrue(any(r["claim_id"] == "superfluid_bec_media" for r in rep["flags"]))

    def test_deletion_flags(self):
        working = [c for c in copy.deepcopy(self.claims) if c["id"] != "rung4_love_kk"]
        rep = bank_gate(self.claims, working, self.source_ids)
        self.assertEqual(rep["overall"], "FLAG-FOR-FIREWALL")
        self.assertIn("rung4_love_kk", rep["deletions"])


if __name__ == "__main__":
    unittest.main()


class TestWaiverCostsAndSeverity(unittest.TestCase):
    """Part-1 close-out (2026-08-09): the review's two structural fixes, proven to fire."""

    def test_a_waiver_without_justification_BLOCKS(self):
        """1b: laundering_ok with no stance_justification must be a BLOCK, not a quiet flag."""
        import json, copy
        from auditor import audit
        claims = json.load(open(os.path.join(HERE, "claims.json")))["claims"]
        m = copy.deepcopy(claims)
        target = next(c for c in m if c.get("laundering_ok"))
        target.pop("stance_justification", None)
        srcs = set(json.load(open(os.path.join(HERE, "sources.json"))))
        r = audit(m, srcs)
        self.assertTrue(any("WITHOUT stance_justification" in b for b in r.blocking),
                        "a costless waiver must block -- that is 1b's whole content")

    def test_all_live_waivers_carry_justifications(self):
        import json
        claims = json.load(open(os.path.join(HERE, "claims.json")))["claims"]
        for c in claims:
            if c.get("laundering_ok"):
                self.assertTrue(str(c.get("stance_justification") or "").strip(),
                                f"{c['id']}: waiver without a declared stance")

    def test_tier_changes_get_their_own_severity(self):
        """1a: a tier/ledger/disposition move must classify TIER-OR-LEDGER, never SUBSTANTIVE."""
        import json, copy
        claims = json.load(open(os.path.join(HERE, "claims.json")))["claims"]
        srcs = set(json.load(open(os.path.join(HERE, "sources.json"))))
        work = copy.deepcopy(claims)
        t = next(c for c in work if c["id"] == "zeta_interior_family")
        t["tier"] = "derived"                    # the graduation the review demonstrated
        rep = bank_gate(claims, work, srcs)
        sev = {r["claim_id"]: r.get("_severity") for r in rep["flags"] + rep["blocks"] + rep["passes"]}
        self.assertEqual(sev.get("zeta_interior_family"), "TIER-OR-LEDGER",
                         f"an unearned graduation rendered as {sev.get('zeta_interior_family')!r} "
                         f"-- it must be categorically distinct, or it hides in alarm fatigue")
