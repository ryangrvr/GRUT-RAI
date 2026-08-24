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


def _open_node(cid, delta=0, deps=("rung1_inin_formalism",)):
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
             "ledger_delta": 2, "depends_on": ["rung1_inin_formalism"]}]
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


class TestBaselineIsNotGitHead(unittest.TestCase):
    """REGRESSION LOCK (2026-08-10). `git init` once silently switched the gate's baseline from
    the --accept snapshot to git HEAD, so committing a register edit auto-accepted it -- the
    pre-upload pass consumed its own pending flag. The baseline must be claims.baseline.json
    UNCONDITIONALLY: version control records HISTORY, the snapshot records ACCEPTANCE. Without
    this test the defect silently returns; this class has recurred enough to earn a permanent
    guard."""

    def test_resolver_reads_the_snapshot_not_head(self):
        """Direct: the resolver's label must be the snapshot file, and its content must equal the
        snapshot's content -- in a tree where git HEAD and the snapshot DISAGREE (they do right
        now whenever an accepted state differs from the last commit; construct the disagreement
        explicitly so the test does not depend on repo state)."""
        import bankgate, json, copy
        baseline, label = bankgate._resolve_baseline()
        self.assertEqual(label, bankgate.BASELINE,
                         f"baseline resolved to {label!r} -- git HEAD must never be a baseline "
                         f"source; commit is not accept")
        snap = json.load(open(os.path.join(HERE, bankgate.BASELINE)))["claims"]
        self.assertEqual(baseline, snap)

    def test_a_committed_but_unaccepted_edit_still_flags(self):
        """Behavioral: simulate the exact failure -- an edit present in the working set (as it
        would be after `git commit`) but NOT in the snapshot. The gate MUST report it. Under the
        old resolver this returned CLEAN because HEAD already contained the edit."""
        import bankgate, json, copy
        baseline, _ = bankgate._resolve_baseline()
        working = copy.deepcopy(baseline)
        target = next(c for c in working if c["id"] == "rung3_single_pole")
        target["boundary_condition"] = (target.get("boundary_condition", "") +
                                        " [SIMULATED COMMITTED-BUT-UNACCEPTED EDIT]")
        srcs = set(json.load(open(os.path.join(HERE, "sources.json"))))
        rep = bank_gate(baseline, working, srcs)
        self.assertEqual(rep["overall"], "FLAG-FOR-FIREWALL",
                         "a committed-but-unaccepted edit must FLAG -- if this is CLEAN, "
                         "commit has become accept again")
        self.assertEqual([r["claim_id"] for r in rep["flags"]], ["rung3_single_pole"])

    def test_no_git_invocation_remains_in_bankgate(self):
        """The module must not consult git at all -- a future 'helpful' fallback is the same
        regression wearing a smaller hat."""
        import inspect, bankgate
        src = inspect.getsource(bankgate)
        self.assertNotIn("git", src.replace("git init converted", "").replace("GIT INIT CONVERTED", "")
                         .replace("`git init`", "").replace("git HEAD", "").replace("under git ", ""),
                         "bankgate must not invoke git; only prose mentions of the regression are allowed")


class TestNonSubstantiveChangesAreReported(unittest.TestCase):
    """2026-08-12: a nine-edit batch produced six flags and three SILENT passes, and the gate
    reported only six. The classification is defensible (tier_note/ledger_note are commentary and
    sit in neither the SUBSTANTIVE_FIELDS path nor the consistency-flag path); the SILENCE is not.
    A gate that can swallow three of nine identical edits can swallow a real one."""

    def _pair(self):
        import json, copy
        base = json.load(open(os.path.join(HERE, "claims.baseline.json")))["claims"]
        work = copy.deepcopy(base)
        # a commentary-only edit: touches no substantive field, raises no consistency flag
        t = next(c for c in work if c["id"] == "rung7_wz")
        t["ledger_note"] = t.get("ledger_note", "") + " [commentary-only edit for the test]"
        srcs = set(json.load(open(os.path.join(HERE, "sources.json"))))
        return base, work, srcs

    def test_a_commentary_only_edit_is_reported_not_dropped(self):
        base, work, srcs = self._pair()
        rep = bank_gate(base, work, srcs)
        ids = [r["claim_id"] for r in rep["silent_changes"]]
        self.assertIn("rung7_wz", ids,
                      "a commentary-only edit must be REPORTED under silent_changes -- a change "
                      "the gate does not count is a change nobody can see")

    def test_it_is_still_not_flagged(self):
        """The classification must not drift the other way: reporting is not flagging, and turning
        every comment edit into a firewall item would restore the alarm fatigue 1a removed."""
        base, work, srcs = self._pair()
        rep = bank_gate(base, work, srcs)
        self.assertNotIn("rung7_wz", [r["claim_id"] for r in rep["flags"]])
        self.assertEqual(rep["overall"], "CLEAN")

    def test_the_two_flag_paths_are_documented_in_source(self):
        import inspect, bankgate
        src = inspect.getsource(bankgate)
        self.assertIn("SUBSTANTIVE_FIELDS", src)
        self.assertIn("consistency flag", src)
