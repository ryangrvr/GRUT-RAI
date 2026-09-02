#!/usr/bin/env python3
"""Tests for the GRUT Resident (resident.py) -- Layers 2-3, the deterministic floor.

Covers the spec exactly:
  - a clean proposal passes (new substantive -> FLAG-FOR-FIREWALL, not BLOCK; clean metadata
    change -> PASS);
  - a laundering proposal BLOCKS;
  - a proposal re-opening a settled-negative FLAGS;
  - a tier-contradiction FLAGS;
  - the dependency graph is acyclic and resolves;
  - the live register still audits GREEN +16 with tiers unchanged;
  - plus: prior-lineage flags, unresolved-deps blocks, downstream works, the resident never
    turns a substantive claim into a silent PASS (laundering harder, never banking easier).

Pure stdlib (unittest). Run:  python3 provenance/test_resident.py
"""
import json
import os
import unittest

from auditor import audit, DEFAULT_TIERS
from resident import (dependency_graph, downstream, propose, check_change,
                      consistency_flags)

HERE = os.path.dirname(os.path.abspath(__file__))


def load_register():
    with open(os.path.join(HERE, "sources.json")) as f:
        sources = json.load(f)
    source_ids = {k for k in sources if not k.startswith("_")}
    with open(os.path.join(HERE, "claims.json")) as f:
        claims = json.load(f)["claims"]
    return claims, source_ids


# ---------------------------------------------------------------------------------------------
# CASE ENUMERATORS. See expected_red.py and OPEN_PASSES.txt: a declared expected-red is declared at
# (test, CASE) granularity, because declaring a SET-VALUED test red silences it for every future
# member of the set. These are the single implementation; the tests below assert the sets are
# empty, and the runner diffs them against what is declared.

_CLEAN_ANNOTATION = {"differentiator": "reworded; no content/provenance/lineage change"}


def tier_contradiction_cases(claims=None):
    """Every live claim carrying a TIER-CONTRADICTION -- ALL of them, not the first."""
    claims = claims if claims is not None else load_register()[0]
    return {c["id"] for c in claims
            if any("TIER-CONTRADICTION" in f for f in consistency_flags(c, claims))}


def clean_annotation_rejection_cases(claims=None, source_ids=None):
    """Every live claim where a PRESENTATIONAL-ONLY edit is refused FOR A TIER CONTRADICTION.

    Widened past the single node the test names -- enumerating one node would rebuild at case
    granularity the same blind spot case granularity exists to remove -- and it earned that
    immediately: rung2_kms_gate is in this set and was never declared, because the test fails on
    rung1 and stops.

    TWO EXCLUSIONS, NAMED HERE RATHER THAN LEFT IMPLICIT, because a narrowing that is not written
    down at the point of narrowing is indistinguishable from a blind spot:

      1. DESIGNED FLAGS. 11 claims carrying a closed disposition refuse any edit as re-opening
         settled ground (RE-OPENS / BUILDS-ON-CLOSED). That is the gate working, pinned by its own
         tests, and not a red.

      2. SURFACED, NOT ADJUDICATED -- 21 claims BLOCK on a presentational edit with the reason
         "invalid tier". They are the vacuum-cluster nodes, carrying the physics vocabulary
         (postulate / measured / heuristic / open). auditor.audit() IS scope-aware -- the live
         audit filters to ledger_scope == "grut" -- but resident.check_change() is NOT, so it
         judges every node against DEFAULT_TIERS and refuses all 21. The failure is SAFE (it
         blocks; it does not wave anything through) and no test covers it because no test edits
         those nodes. Which vocabulary the resident should enforce per scope is a governance
         question, and the physics tier vocabulary is itself awaiting a ruling. Not folded in
         here: it is a different defect from the one this test is failing on, and quietly
         enlarging a declared case set with an unrelated finding would bury it.
    """
    if claims is None or source_ids is None:
        claims, source_ids = load_register()
    out = set()
    for c in claims:
        r = check_change(c["id"], dict(_CLEAN_ANNOTATION), claims, source_ids)
        if r["verdict"] != "PASS" and any("TIER-CONTRADICTION" in f for f in r["consistency_flags"]):
            out.add(c["id"])
    return out


def newclaim(**kw):
    base = dict(
        id="proposed_x",
        statement="A proposed claim.",
        tier="to-derive",
        sources=["kubo1966"],
        overturning_computation="a calc that would kill it",
        ledger_delta=0,
        depends_on=["rung1_inin_formalism"],
    )
    base.update(kw)
    return base


class TestResident(unittest.TestCase):
    def setUp(self):
        self.claims, self.src = load_register()

    # ---- graph ----
    def test_live_graph_acyclic_and_resolves(self):
        graph, errors = dependency_graph(self.claims)
        self.assertEqual(errors, [], f"live dependency graph must be a valid DAG; errors={errors}")
        self.assertIn("mu_linear", graph)
        self.assertIn("p_tt_ansatz", graph["mu_linear"])  # the spec's example edge

    def test_cycle_is_detected(self):
        a = newclaim(id="a", depends_on=["b"])
        b = newclaim(id="b", depends_on=["a"])
        _, errors = dependency_graph([a, b])
        self.assertTrue(any("CYCLE" in e for e in errors))

    def test_unresolved_edge_is_detected(self):
        a = newclaim(id="a", depends_on=["ghost"])
        _, errors = dependency_graph([a])
        self.assertTrue(any("does not resolve" in e for e in errors))

    def test_downstream(self):
        # p_tt_ansatz is depended on by mu_linear
        dn = downstream("p_tt_ansatz", self.claims)
        self.assertIn("mu_linear", dn)
        # rung1 is foundational -> many dependents
        self.assertGreater(len(downstream("rung1_inin_formalism", self.claims)), 5)

    # ---- clean proposals ----
    def test_clean_new_substantive_flags_for_firewall(self):
        # a clean, disciplined new substantive claim is NOT blocked, but defaults to FLAG
        r = propose(newclaim(), self.claims, self.src)
        self.assertEqual(r["verdict"], "FLAG-FOR-FIREWALL")
        self.assertEqual(r["discipline"]["blocking"], [])
        self.assertFalse(r["ledger"]["net_changes"])  # ledger_delta 0
        self.assertEqual(r["dependencies"]["unresolved"], [])

    def test_clean_annotation_change_passes(self):
        # changing ONLY a presentational annotation (differentiator) is non-substantive -> PASS
        r = check_change("rung1_inin_formalism", dict(_CLEAN_ANNOTATION), self.claims, self.src)
        self.assertEqual(r["verdict"], "PASS")
        self.assertFalse(r["substantive"])
        # ...and it must hold for EVERY node, not only the one named above. The enumerator is the
        # single implementation the runner diffs against; its docstring names the two exclusions.
        bad = sorted(clean_annotation_rejection_cases(self.claims, self.src))
        self.assertEqual(bad, [], f"a presentational-only edit is refused for a tier "
                                  f"contradiction at: {bad}")

    # ---- laundering BLOCKS ----
    def test_laundering_proposal_blocks(self):
        r = propose(newclaim(tier="derived", ledger_delta=2), self.claims, self.src)
        self.assertEqual(r["verdict"], "BLOCK")
        self.assertTrue(r["discipline"]["laundering_blocked"])

    def test_missing_source_blocks(self):
        r = propose(newclaim(sources=[]), self.claims, self.src)
        self.assertEqual(r["verdict"], "BLOCK")

    def test_unresolved_dependency_blocks(self):
        r = propose(newclaim(depends_on=["ghost_claim"]), self.claims, self.src)
        self.assertEqual(r["verdict"], "BLOCK")
        self.assertEqual(r["dependencies"]["unresolved"], ["ghost_claim"])

    # ---- re-opening a settled-negative / closed disposition FLAGS ----
    def test_change_to_settled_negative_flags(self):
        # rung9b_bridge is assumed/settled-negative; trying to change it re-opens settled ground
        r = check_change("rung9b_bridge", {"tier": "derived", "ledger_delta": 0},
                         self.claims, self.src)
        self.assertEqual(r["verdict"], "FLAG-FOR-FIREWALL")
        self.assertTrue(any("RE-OPENS" in f for f in r["consistency_flags"]))

    def test_new_claim_building_on_closed_flags(self):
        # a new claim that rests on the refuted info_i2 builds on closed ground -> FLAG
        r = propose(newclaim(depends_on=["info_i2_beyond_standard_bridge"]),
                    self.claims, self.src)
        self.assertEqual(r["verdict"], "FLAG-FOR-FIREWALL")
        self.assertTrue(any("BUILDS-ON-CLOSED" in f for f in r["consistency_flags"]))

    # ---- tier contradiction FLAGS ----
    def test_tier_contradiction_flags(self):
        # 'derived' (a result) resting on 'rung7_wz' (to-derive) is a contradiction
        r = propose(newclaim(tier="derived", ledger_delta=-1, depends_on=["rung7_wz"]),
                    self.claims, self.src)
        self.assertEqual(r["verdict"], "FLAG-FOR-FIREWALL")
        self.assertTrue(any("TIER-CONTRADICTION" in f for f in r["consistency_flags"]))

    def test_derived_pending_on_assumed_is_NOT_a_contradiction(self):
        # mu_linear (derived-pending) legitimately rests on p_tt_ansatz (assumed) -- no flag.
        # A NEW derived-pending claim resting on an assumed input must not raise TIER-CONTRADICTION.
        r = propose(newclaim(tier="derived-pending", depends_on=["p_tt_ansatz"]),
                    self.claims, self.src)
        self.assertFalse(any("TIER-CONTRADICTION" in f for f in r["consistency_flags"]))

    # ---- prior-lineage: AUTHORITATIVE on the structured `prior_lineage` field; regex demoted to a hint ----
    def test_prior_lineage_flags_on_structured_field(self):
        # a claim that DECLARES prior_lineage is flagged (the structured field is authoritative)
        r = propose(newclaim(prior_lineage=True), self.claims, self.src)
        self.assertTrue(any("PRIOR-LINEAGE" in f for f in r["consistency_flags"]))
        self.assertEqual(r["verdict"], "FLAG-FOR-FIREWALL")

    def test_prior_lineage_regex_is_hint_only_never_flags(self):
        # a 'v4'-mentioning statement WITHOUT the declaration does NOT flag (regex demoted to a hint)
        from resident import _prior_lineage
        c = newclaim(statement="Ported from the v4 lineage: a propagating-relic pole.")
        self.assertFalse(_prior_lineage(c))                        # authoritative field says clean
        r = propose(c, self.claims, self.src)
        self.assertFalse(any("PRIOR-LINEAGE" in f for f in r["consistency_flags"]))  # never flags alone
        self.assertTrue(r["hints"])                                # ...but it MAY warn (a hint fires)

    def test_lineage_hint_both_directions(self):
        # the demoted regex, as a non-authoritative HINT, must still WARN on real lineage and be SILENT
        # on the current program / current version (v5) -- pins the version-token near-miss.
        from resident import _lineage_hint
        for s in ["imports the v4 dark-matter line", "the v2/v3 hierarchy is inherited",
                  "ported from a previous version of the model"]:
            self.assertIsNotNone(_lineage_hint({"statement": s}), f"hint expected: {s!r}")
        for s in ["Version II universality program", "the genuine V2 frontier",
                  "the v5 clean rebuild", "consistent with the v5 register"]:
            self.assertIsNone(_lineage_hint({"statement": s}), f"no hint expected: {s!r}")

    def test_live_register_no_false_prior_lineage(self):
        # no live claim's statement may false-trip PRIOR-LINEAGE (the V2 entry claims included)
        from resident import _prior_lineage
        for c in self.claims:
            self.assertFalse(_prior_lineage(c),
                             f"{c['id']} statement false-flags PRIOR-LINEAGE: {c.get('statement','')[:80]!r}")

    # ---- the resident never makes banking easier ----
    def test_substantive_never_silent_passes(self):
        # even a perfectly clean substantive new claim cannot be PASS -- always >= FLAG
        r = propose(newclaim(), self.claims, self.src)
        self.assertNotEqual(r["verdict"], "PASS")

    def test_check_change_nonexistent_blocks(self):
        r = check_change("no_such_id", {"tier": "shown"}, self.claims, self.src)
        self.assertEqual(r["verdict"], "BLOCK")

    # ---- firewall-found false negatives: now closed ----
    def test_cycle_via_change_blocks(self):
        # rung8 already depends_on rung6; making rung6 depend_on rung8 closes a 2-cycle.
        r = check_change("rung6_qm_limit",
                         {"depends_on": ["rung1_inin_formalism", "rung2_kms_gate", "rung8_falsifier"]},
                         self.claims, self.src)
        self.assertEqual(r["verdict"], "BLOCK")
        self.assertTrue(r["dependencies"]["introduces_cycle"])
        self.assertTrue(any("CYCLE" in f for f in r["consistency_flags"]))

    def test_falsifier_degradation_flags(self):
        # rewriting a banked claim's overturning_computation must NOT be a silent PASS
        r = check_change("rung1_inin_formalism", {"overturning_computation": "x"}, self.claims, self.src)
        self.assertEqual(r["verdict"], "FLAG-FOR-FIREWALL")
        self.assertTrue(r["substantive"])

    def test_sub_status_change_flags(self):
        # changing a closed-state marker (sub_status) is substantive -> FLAG, never silent PASS
        r = check_change("rung9a_value", {"sub_status": "now totally different"}, self.claims, self.src)
        self.assertEqual(r["verdict"], "FLAG-FOR-FIREWALL")
        self.assertTrue(r["substantive"])

    def test_laundering_waiver_surfaced(self):
        # a declared laundering_ok waiver is surfaced to the firewall (not silent), still FLAG
        r = propose(newclaim(tier="shown", ledger_delta=3, laundering_ok=True, stance_justification="test stance: declared for the 1b waiver-cost rule (2026-08-09) -- a waiver without a stated stance now BLOCKS"), self.claims, self.src)
        self.assertEqual(r["verdict"], "FLAG-FOR-FIREWALL")        # not BLOCK (waiver), not PASS
        self.assertTrue(r["discipline"]["laundering_waiver"])
        self.assertTrue(any("LAUNDERING-WAIVER" in w for w in r["discipline"]["warnings"]))

    def test_prior_lineage_broadened_is_hint_not_flag(self):
        # broadened prose (v4 / 'previous version' / 'propagating relic') -> a HINT fires, but it NEVER
        # flags alone (structured `prior_lineage` is undeclared, so no PRIOR-LINEAGE flag).
        from resident import _lineage_hint
        for s in ("Ported from v4.", "From a previous version of GRUT.", "propagating  relic pole"):
            self.assertIsNotNone(_lineage_hint({"statement": s}), f"hint expected: {s!r}")
            r = propose(newclaim(statement=s), self.claims, self.src)
            self.assertFalse(any("PRIOR-LINEAGE" in f for f in r["consistency_flags"]),
                             f"regex must NOT flag alone: {s!r}")

    # ---- provenance/lineage edits must never bank easier than a fresh claim ----
    def test_sources_change_flags(self):
        # gutting a banked claim's provenance basis (5 sources -> 1) must NOT be a silent PASS
        r = check_change("rung1_inin_formalism", {"sources": ["kubo1966"]}, self.claims, self.src)
        self.assertNotEqual(r["verdict"], "PASS")
        self.assertEqual(r["verdict"], "FLAG-FOR-FIREWALL")
        self.assertTrue(r["substantive"])

    def test_depends_on_emptying_flags(self):
        # orphaning a banked result by emptying its depends_on must NOT be a silent PASS
        r = check_change("rung2_kms_gate", {"depends_on": []}, self.claims, self.src)
        self.assertNotEqual(r["verdict"], "PASS")
        self.assertEqual(r["verdict"], "FLAG-FOR-FIREWALL")
        self.assertTrue(r["substantive"])
        self.assertTrue(any("ORPHANED-RESULT" in f for f in r["consistency_flags"]))

    def test_orphaning_a_shown_result_flags(self):
        # same hole on a different result-tier claim (rung4 shown, had two deps)
        r = check_change("rung4_love_kk", {"depends_on": []}, self.claims, self.src)
        self.assertEqual(r["verdict"], "FLAG-FOR-FIREWALL")
        self.assertTrue(any("ORPHANED-RESULT" in f for f in r["consistency_flags"]))

    def test_legit_rootless_axiom_not_orphan_flagged(self):
        # rung1 (the stance) is legitimately rootless; a cosmetic edit must NOT raise ORPHANED-RESULT
        r = check_change("rung1_inin_formalism", {"differentiator": "reworded"}, self.claims, self.src)
        self.assertFalse(any("ORPHANED-RESULT" in f for f in r["consistency_flags"]))

    def test_prior_lineage_no_false_positive_on_historical_note(self):
        # mu_linear's tier_note legitimately mentions the v4 code history; a cosmetic edit must
        # NOT raise PRIOR-LINEAGE (the heuristic scans only the claim's assertion, not the notes)
        r = check_change("mu_linear", {"differentiator": "reworded note"}, self.claims, self.src)
        self.assertFalse(any("PRIOR-LINEAGE" in f for f in r["consistency_flags"]))

    # ---- overseer verify-the-verifier: founding_h2 disposition + boundary_condition ----
    def test_founding_h2_disposition_softening_flags(self):
        # founding_h2 is disfavored (marker now in sub_status); softening its disposition via any
        # edit must fire RE-OPENS, never a silent PASS (the verify-the-verifier's confirmed hole).
        r = check_change("founding_h2_R_zeta_bridge",
                         {"tier_note": "FAVORABLE & LIVE near-term lead"}, self.claims, self.src)
        self.assertNotEqual(r["verdict"], "PASS")
        self.assertEqual(r["verdict"], "FLAG-FOR-FIREWALL")
        self.assertTrue(any("RE-OPENS" in f for f in r["consistency_flags"]))

    def test_boundary_condition_change_flags(self):
        # editing a claim's conditions (boundary_condition) silently broadens it -> must FLAG.
        # arrow_of_time carries a real boundary_condition and is not otherwise closed.
        r = check_change("arrow_of_time",
                         {"boundary_condition": "broadened: removed the existence/direction split"},
                         self.claims, self.src)
        self.assertEqual(r["verdict"], "FLAG-FOR-FIREWALL")
        self.assertTrue(r["substantive"])

    def test_disposition_markers_live_in_sub_status(self):
        # the durable rule: every claim the resident must treat as closed has its marker in
        # sub_status (not only tier_note). Confirm the live closed/disfavored set is sub_status-marked.
        import resident as _r
        for cid in ("rung9b_bridge", "mu_linear", "founding_h2_R_zeta_bridge",
                    "founding_h3_doubleslit_anchor", "info_i2_beyond_standard_bridge",
                    "info_i3_distinct_consequence"):
            cl = next(c for c in self.claims if c["id"] == cid)
            self.assertTrue(_r._is_closed(cl), f"{cid} must be recognized closed via sub_status")

    # ---- live register regression: GREEN +16, tiers unchanged, graph valid ----
    def test_live_register_green_current_net_tiers_unchanged(self):  # renamed from ...plus16... 2026-08-24: the number leaves the identifier so the NAME can never go stale; the pin lives below
        # SCOPED 2026-08-04: these assertions are about GRUT'S register. The same file now also
        # carries the vacuum-cluster physics map under a different vocabulary and a separate
        # ledger (validate_scoped.py); it must not enter GRUT's count.
        grut = [c for c in self.claims if c.get("ledger_scope", "grut") == "grut"]
        r = audit(grut, self.src, DEFAULT_TIERS)
        self.assertTrue(r.ok, f"live register must audit clean; blocks={r.blocking}")
        self.assertEqual(r.net, 16)       # +16: the response_lorentz_covariance +1 (booked 2026-08-24) was RETIRED 2026-08-30 by the owner-adjudicated Q1^TT-and-Q5^TT discharge, per the node's own retire clause
        self.assertEqual(len(grut), 53)   # 52 + kr_contract_retarded_tier4 (banked 2026-09-01, delta 0, owner relay); 51 + response_lorentz_covariance (2026-08-24); 50 + the Ruling-B split's second half (2026-08-23) before that
        # depends_on present on every claim; tiers are the banked ones
        for c in self.claims:
            self.assertIn("depends_on", c, f"{c['id']} missing depends_on metadata")
        graph, errors = dependency_graph(self.claims)
        self.assertEqual(errors, [])

    def test_ledger_graph_reconciliation_current_net_no_double_count(self):  # renamed from ...plus16... 2026-08-24, same reason
        # A3 RECONCILIATION: net = sum of ledger_delta over DISTINCT nodes (each id once) == +14 (post the 2026-08-02 rung7 booking and the 2026-08-17 rung1 bath-genuineness booking).
        # The blind-sum auditor cannot catch a double count, so this pins it structurally: the promoted
        # borrowed premises carry ZERO credit (their +1 stays inside the borrower), so growing the graph
        # cost zero honesty. A node carrying +1 AND its borrower keeping its delta would push net to +14
        # and fail here.
        ids = [c["id"] for c in self.claims]
        self.assertEqual(len(ids), len(set(ids)), "duplicate claim ids -> a node counted twice")
        net = sum(c.get("ledger_delta", 0) for c in self.claims
                  if isinstance(c.get("ledger_delta"), int) and not isinstance(c.get("ledger_delta"), bool))
        self.assertEqual(net, 16, "net over distinct nodes must be +16 (rung7 books 3; rung1 formalism 4 + ontology 1 since Ruling B 2026-08-23; response_lorentz_covariance RETIRED 2026-08-30 by the owner-adjudicated discharge)")
        # the A3 promoted premises are zero-credit re-typings (borrowers keep their declared deltas)
        by_id = {c["id"]: c for c in self.claims}
        for cid in ("born_rule", "entropy_area_unruh", "past_hypothesis", "lambda_undetermined"):
            self.assertEqual(by_id[cid]["ledger_delta"], 0, f"{cid} must carry ZERO GRUT-derivation credit")
        # borrowers unchanged (still carry their recovery deltas -- the input is counted ONCE, in them)
        self.assertEqual(by_id["rung6_qm_limit"]["ledger_delta"], 2)
        self.assertEqual(by_id["rung5_gr_limit"]["ledger_delta"], 2)
        self.assertEqual(by_id["arrow_of_time"]["ledger_delta"], 1)

    def test_no_tier_contradiction_in_live_register(self):
        # the live register must contain no shown/derived claim resting on an open input.
        # COLLECTS EVERY CASE: the loop this replaced stopped at the first, which is how
        # rung2_kms_gate stayed out of the expected-red declaration that named only rung1.
        bad = sorted(tier_contradiction_cases(self.claims))
        self.assertEqual(bad, [], f"tier-contradiction in the live register at: {bad}")

    # ---- regression: 'neither derived nor refuted' is OPEN, not a closed disposition ----
    def test_negated_refuted_is_not_closed(self):
        from resident import _is_closed
        # rung3's 'neither derived nor refuted' is an OPEN anchor -- must NOT read as closed
        rung3 = next(c for c in self.claims if c["id"] == "rung3_single_pole")
        self.assertFalse(_is_closed(rung3),
                         "rung3 ('neither derived nor refuted') is OPEN, must not be flagged closed")
        # a genuine closed disposition (STRUCTURED field) MUST still read as closed
        i2 = next(c for c in self.claims if c["id"] == "info_i2_beyond_standard_bridge")
        self.assertTrue(_is_closed(i2), "info_i2 (disposition=screened-refuted) is a closed disposition")
        self.assertTrue(_is_closed({"disposition": "screened-refuted", "tier": "to-derive"}))
        # ...while prose that MENTIONS a marker (a negation OR a cross-reference to ANOTHER claim's
        # marker) but has NO `disposition` field is OPEN -- the three regex near-misses can no longer
        # false-close (rung3 'neither refuted'; a u6-style 'info_i2 was refuted' cross-ref):
        self.assertFalse(_is_closed({"sub_status": "neither derived nor refuted", "tier": "derived-pending"}))
        self.assertFalse(_is_closed({"sub_status": "info_i2 was refuted (see tier_note)", "tier": "to-derive"}))

    def test_rung3_dependents_have_no_false_builds_on_closed(self):
        # rung3 is OPEN, so claims resting on it must NOT carry a (false) BUILDS-ON-CLOSED via rung3
        for cid in ("rung5_gr_limit", "rung7_wz", "rung7_w2_wa_sign"):
            c = next(x for x in self.claims if x["id"] == cid)
            flags = consistency_flags(c, self.claims)
            self.assertFalse(any("BUILDS-ON-CLOSED" in f and "rung3_single_pole" in f for f in flags),
                             f"{cid} falsely flagged as building on closed rung3: {flags}")

    def test_all_genuine_closed_claims_still_caught(self):
        # the disposition refactor must not let a genuinely-closed claim slip to open: each carries a
        # STRUCTURED disposition and reads closed (the other direction of the both-directions regression).
        from resident import _is_closed
        for cid in ("info_i2_beyond_standard_bridge", "rung9b_bridge", "mu_linear",
                    "founding_h2_R_zeta_bridge", "founding_h3_doubleslit_anchor",
                    "info_i3_distinct_consequence", "l0_r2_exact_unique_breaker"):
            c = next(x for x in self.claims if x["id"] == cid)
            self.assertTrue(_is_closed(c), f"{cid} must still read closed (structured disposition)")

    def test_disposition_refactor_no_live_false_close(self):
        # no OPEN claim (no disposition field) may read closed, even if its prose mentions a marker
        # token as a cross-reference/negation (the u6 / rung3 near-misses, live).
        from resident import _is_closed
        for c in self.claims:
            if c.get("disposition") is None:
                self.assertFalse(_is_closed(c),
                                 f"{c['id']} has no disposition but reads closed -- prose false-close leaked")


if __name__ == "__main__":
    unittest.main(verbosity=2)
