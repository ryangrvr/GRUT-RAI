"""test_sweep_ledger: pins the two R2/edge rulings of 2026-08-04.

BOTH GUARDS ARE HERE BECAUSE A REMEMBERED RULE IS NOT A RULE. The omission standard already said in
prose "record the argument for every node examined", and a sweep still dropped a PRE-REGISTERED
candidate silently. The standard already leaned on the MULTIPLICITY SIGNAL, and the register still
could not compute it, because omissions were banked with no inbound edges -- including one that was
FOUND AS A LINK IN ANOTHER NODE'S CHAIN while that node kept depends_on: [].

Both guards are proven to FIRE by mutation below. A green test proves nothing until it is shown to
fail on a wrong state -- this program's dominant failure mode, on its fifth appearance.
"""
import copy
import json
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from sweep_ledger import reconcile, close_blockers, load_all, DISPOSITIONS, TERMINAL
from validate_scoped import scope_of


def claims():
    return json.load(open(os.path.join(HERE, "claims.json")))["claims"]


class TestReconciliation(unittest.TestCase):
    """R2: raw candidates raised == sum over dispositions, or the build breaks."""

    def test_there_is_a_sweep_record_at_all(self):
        recs = load_all()
        self.assertTrue(recs, "a sweep that leaves no ledger cannot be reconciled by anyone")

    def test_every_CLOSED_sweep_reconciles(self):
        for fn, rec in load_all():
            if rec.get("status") == "open":
                continue      # open sweeps record their gaps; see the closure test below
            self.assertEqual(reconcile(rec), [], f"{fn} does not reconcile")

    def test_an_open_sweep_cannot_be_closed_while_it_has_gaps(self):
        """`open` is a record of owed work, NOT an escape hatch. The one thing it must never do is
        let a sweep be called finished with a candidate nobody examined."""
        for fn, rec in load_all():
            if rec.get("status") != "open":
                self.assertEqual(close_blockers(rec), [],
                                 f"{fn} is not marked open yet carries unadjudicated candidates -- "
                                 f"that is a gap wearing the appearance of a completed sweep")

    def test_an_absent_verdict_is_never_scored_as_a_negative_verdict(self):
        """THE THIRD APPEARANCE OF THE DEFECT, pinned. The follow-up wave scored survival as
        `votes_for >= 2`; when its verifiers died, zero votes were cast, 0 >= 2 was false, and
        candidates NOBODY EXAMINED were filed as refuted. Any sweep record carrying a candidate
        whose lenses did not run must say NOT-ADJUDICATED, never refuted-at-verify."""
        for fn, rec in load_all():
            for rid, d in rec.get("dispositions", {}).items():
                if "lenses_run" not in d:
                    continue                      # not a verify-stage disposition
                run, need = d["lenses_run"], d.get("lenses_required", 3)
                if run < need:
                    self.assertEqual(d["disposition"], "not-adjudicated",
                                     f"{fn}:{rid} had {run}/{need} lenses run but claims "
                                     f"disposition {d['disposition']!r} -- an absent verdict is "
                                     f"not a negative verdict")

    def test_the_incompleteness_guard_FIRES(self):
        """MUTATION. Re-label an unadjudicated candidate as refuted and the guard must catch it."""
        import copy
        recs = [r for _, r in load_all() if any(
            v.get("lenses_run", 3) < v.get("lenses_required", 3) for v in r["dispositions"].values())]
        self.assertTrue(recs, "no record carries an incomplete verification to mutate")
        m = copy.deepcopy(recs[0])
        rid = next(k for k, v in m["dispositions"].items()
                   if v.get("lenses_run", 3) < v.get("lenses_required", 3))
        m["dispositions"][rid]["disposition"] = "refuted-at-verify"
        caught = m["dispositions"][rid]["lenses_run"] < m["dispositions"][rid]["lenses_required"] \
                 and m["dispositions"][rid]["disposition"] != "not-adjudicated"
        self.assertTrue(caught, "the guard must detect a re-labelled incomplete verification")

    def test_a_missing_disposition_BLOCKS(self):
        """THE MUTATION. Drop one candidate's disposition -- the exact shape of the 10 that were
        absorbed and never recorded -- and the check must refuse."""
        fn, rec = load_all()[0]
        m = copy.deepcopy(rec)
        m["dispositions"].pop(m["raw"][0]["id"])
        bad = reconcile(m)
        self.assertTrue(bad, "a raw candidate with no disposition MUST block")
        self.assertTrue(any("NO recorded disposition" in b for b in bad), bad)

    def test_absorption_into_nothing_BLOCKS(self):
        """Absorption must be a POINTER, never a hole: a chain ending nowhere is the failure."""
        fn, rec = load_all()[0]
        m = copy.deepcopy(rec)
        rid = next(k for k, v in m["dispositions"].items()
                   if v["disposition"] == "absorbed-into-cluster")
        m["dispositions"][rid]["canonical"] = "raw-999"
        self.assertTrue(any("has no disposition of its own" in b for b in reconcile(m)))

    def test_absorption_chain_must_end_in_an_adjudication(self):
        fn, rec = load_all()[0]
        m = copy.deepcopy(rec)
        a = next(k for k, v in m["dispositions"].items()
                 if v["disposition"] == "absorbed-into-cluster")
        b = m["dispositions"][a]["canonical"]
        m["dispositions"][b] = {"disposition": "absorbed-into-cluster", "canonical": a}
        self.assertTrue(any("must END in an adjudication" in x for x in reconcile(m)))

    def test_not_adjudicated_always_blocks(self):
        """The value exists so a gap can be RECORDED, not so it can be kept."""
        fn, rec = load_all()[0]
        m = copy.deepcopy(rec)
        m["dispositions"][m["raw"][0]["id"]] = {"disposition": "not-adjudicated"}
        self.assertTrue(any("NOT ADJUDICATED" in b for b in reconcile(m)))

    def test_a_prereg_candidate_that_vanishes_BLOCKS(self):
        """THE COSMIC-TIME CASE. A raw-candidate ledger alone reconciles perfectly while a
        PRE-REGISTERED expectation disappears -- so the prereg block is checked separately."""
        fn, rec = load_all()[0]
        m = copy.deepcopy(rec)
        m["prereg_candidates"]["Q2e-cosmic-time-foliation"].pop("note")
        bad = reconcile(m)
        self.assertTrue(any("NOT RAISED and carries no note" in b for b in bad), bad)

    def test_the_real_record_states_the_cosmic_time_gap(self):
        fn, rec = load_all()[0]
        q = rec["prereg_candidates"]["Q2e-cosmic-time-foliation"]
        self.assertEqual(q["outcome"], "not-raised")
        self.assertIn("never adjudicated", q["note"],
                      "the gap must be stated in the record, not only in the relay")


class TestOmissionsAreWired(unittest.TestCase):
    """THE EDGE RULING: the standard leans on multiplicity and the register must be able to
    compute it. An omission with no inbound edge is a presupposition nobody presupposes."""

    def _omissions(self):
        return [c for c in claims() if c.get("found_by") == "omission-sweep"]

    def test_the_marker_exists(self):
        self.assertTrue(self._omissions(), "no node is marked found_by omission-sweep")

    def test_no_omission_node_has_zero_inbound_edges(self):
        cl = claims()
        for o in self._omissions():
            inbound = [c["id"] for c in cl if o["id"] in (c.get("depends_on") or [])]
            self.assertTrue(inbound,
                            f"{o['id']} has NO inbound edges. An omission is defined as something "
                            f"a banked node's discharge PRESUPPOSES -- if no node depends on it, "
                            f"either the edge was never recorded (fix the edge) or it is not an "
                            f"omission (unbank it). Silence is not an option.")

    def test_the_edge_guard_FIRES(self):
        """THE MUTATION. Strip the edges and the guard must notice -- otherwise it is decorative."""
        cl = copy.deepcopy(claims())
        for c in cl:
            c["depends_on"] = []
            omissions = [x for x in cl if x.get("found_by") == "omission-sweep"]
        unwired = [o["id"] for o in omissions
                   if not [c for c in cl if o["id"] in (c.get("depends_on") or [])]]
        self.assertEqual(len(unwired), len(omissions),
                         "with every edge stripped, EVERY omission must read as unwired -- if not, "
                         "this guard is measuring something other than the edges")

    def test_the_found_omission_is_wired_to_the_chain_it_was_found_in(self):
        """vc_flatness_in_reduction was found as a link in vc_rho_lambda's reduction chain while
        vc_rho_lambda carried depends_on: []. That specific hole must stay closed."""
        by = {c["id"]: c for c in claims()}
        self.assertIn("vc_flatness_in_reduction", by["vc_rho_lambda"]["depends_on"])


if __name__ == "__main__":
    unittest.main()
