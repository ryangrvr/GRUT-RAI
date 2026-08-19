#!/usr/bin/env python3
"""Tests for the GRUT Forward-Model Harness (harness.py) -- the generative face.

Hammers the guards from the brief:
  - THE CARDINAL INVARIANT (structural): admissible() has NO `data` parameter, and flipping the
    observational data NEVER changes admissibility (data can't tune the machine);
  - admissibility excludes a no-go violator (mu!=1 / trace-only), a non-KMS bath, an off-premise
    spectral form, and an un-sourced provenance choice;
  - the forward map: single-scale -> w=-1 derived (no inserted input); a 2nd scale -> inserted-input flag;
  - NO TUNING-AS-LAUNDERING: a kernel tuned to match DESI -> data_consistent False + laundering_flag;
  - default-broken: an empty admissible-and-matching set is a valid, returnable result;
  - no universe is ever tier 'shown'; the live register still audits GREEN +15 (harness writes nothing).

Pure stdlib (unittest). Run:  python3 provenance/test_harness.py
"""
import inspect
import json
import os
import unittest

from auditor import audit, DEFAULT_TIERS
import harness
import resident

HERE = os.path.dirname(os.path.abspath(__file__))


def load_claims():
    with open(os.path.join(HERE, "claims.json")) as f:
        return json.load(f)["claims"]


class TestHarness(unittest.TestCase):
    def setUp(self):
        self.claims = load_claims()

    # ---- THE CARDINAL INVARIANT ----
    def test_admissible_has_no_data_parameter(self):
        # the machine cannot see, hence cannot be tuned by, observation -- structural.
        sig = inspect.signature(harness.admissible)
        self.assertNotIn("data", sig.parameters,
                         "admissible() must NOT take data -- the cardinal invariant in code")

    def test_data_never_changes_admissibility(self):
        u = harness.universe("u")
        a1, _ = harness.admissible(u, self.claims)
        # evaluate with two WILDLY different observation sets; admissibility must be identical.
        obs_lcdm = dict(harness.OBSERVATIONS, desi_w0=-1.0, desi_wa=0.0)
        obs_phantom = dict(harness.OBSERVATIONS, desi_w0=-0.5, desi_wa=-2.0)
        r1 = harness.evaluate(u, self.claims, obs_lcdm)
        r2 = harness.evaluate(u, self.claims, obs_phantom)
        self.assertEqual(r1["admissible"], r2["admissible"])
        self.assertEqual(r1["admissible"], a1)
        # data_consistent is a SEPARATE field and may differ, but admissible is invariant.
        self.assertIsNot(r1["admissible"], None)

    def test_two_fields_are_separate(self):
        r = harness.evaluate(harness.universe("u"), self.claims)
        self.assertIn("admissible", r)
        self.assertIn("data_consistent", r)
        # data_consistent is only computed downstream of admissibility (None if inadmissible).
        bad = harness.evaluate(harness.universe("b", projector="trace-only"), self.claims)
        self.assertFalse(bad["admissible"])
        self.assertIsNone(bad["data_consistent"])

    # ---- admissibility excludes the right things ----
    def test_mu_not_1_excluded(self):
        r = harness.evaluate(harness.universe("trace", projector="trace-only"), self.claims)
        self.assertFalse(r["admissible"])
        self.assertFalse(r["admissibility"]["mu_linear"]["ok"])

    def test_non_kms_excluded(self):
        r = harness.evaluate(harness.universe("nokms", T=0.0), self.claims)
        self.assertFalse(r["admissible"])
        self.assertFalse(r["admissibility"]["kms_detailed_balance"])

    def test_off_premise_excluded(self):
        r = harness.evaluate(harness.universe("off", spectral_form="free-streaming"), self.claims)
        self.assertFalse(r["admissible"])
        self.assertFalse(r["admissibility"]["on_premise"])

    def test_unsourced_provenance_excluded(self):
        u = harness.universe("uns")
        u["provenance"]["projector"] = "ghost_rung"  # does not resolve to a register claim
        adm, rep = harness.admissible(u, self.claims)
        self.assertFalse(adm)
        self.assertFalse(rep["provenance_consistent"])

    def test_l0_r2_closed_disposition_bypass_fixed(self):
        # REGRESSION (pinned failing-before / passing-after): l0_r2_exact_unique_breaker has
        # disposition='screened-dissolves', which the RETIRED free-text marker scan MISSED, so a spec
        # sourcing a kernel input to it wrongly passed admissibility while resident._is_closed said closed.
        # The harness now consults the authoritative closed-check and REJECTS it.
        l0_r2 = next(c for c in self.claims if c["id"] == "l0_r2_exact_unique_breaker")
        self.assertTrue(resident._is_closed(l0_r2), "l0_r2 must be closed (disposition screened-dissolves)")
        u = harness.universe("bypass")
        u["provenance"]["L0"] = "l0_r2_exact_unique_breaker"  # source an active input to CLOSED ground
        adm, rep = harness.admissible(u, self.claims)
        self.assertFalse(adm, "sourcing a kernel input to a closed (screened-dissolves) claim must be inadmissible")
        self.assertFalse(rep["provenance_consistent"])

    def test_harness_and_resident_agree_on_closedness(self):
        # CROSS-SUBSYSTEM INVARIANT: for EVERY claim, the harness's provenance closed-check and the
        # resident's authoritative _is_closed AGREE. Sourcing an active kernel input (L0) to claim C makes
        # _provenance_consistent return ok=False IFF resident._is_closed(C) -- all other active inputs
        # stay open-sourced and resolving, so the only possible failure is L0 -> a closed claim. Asserts on
        # the STRUCTURED boolean, not the prose reason, so a reword of the message cannot affect it.
        for c in self.claims:
            u = harness.universe("agree")
            u["provenance"]["L0"] = c["id"]  # point one active input at this claim; others stay open-sourced
            ok, _ = harness._provenance_consistent(u, self.claims)
            self.assertEqual(not ok, resident._is_closed(c),
                             f"harness provenance ok={ok} disagrees with resident._is_closed "
                             f"({resident._is_closed(c)}) for {c['id']}")

    def test_interior_family_admissible_and_agrees_with_register(self):
        # CROSS-SUBSYSTEM REGRESSION (the KC5-dichotomy live bug, 2026-08-02): the interior is a banked
        # legal kernel family; the harness's mu/eta/Sigma must agree with calc/mu_slip_interior.py --
        # the banked source of truth -- at machine precision (same style as the disposition-divergence
        # regression that caught the last harness/register split).
        import sys
        sys.path.insert(0, os.path.join(os.path.dirname(HERE), "calc"))
        import mu_slip_interior as msi
        for x in (0.0, 0.01, 0.05, 0.3, 0.9):
            u = harness.universe("ix", projector="interior", x=x)
            adm, _ = harness.admissible(u, self.claims)
            self.assertTrue(adm, f"interior x={x} must be structurally admissible")
            p = harness.forward_mu(u["kernel"])
            self.assertAlmostEqual(p["mu"], msi.mu_x(x), places=14)
            self.assertAlmostEqual(p["eta"], msi.eta_x(x), places=14)
            self.assertAlmostEqual(p["Sigma"], msi.Sigma_x(x), places=14)
            self.assertAlmostEqual(p["isw_sigma_nominal"], msi.isw_sigma(x), places=12)
        # pin the ANCHOR plumbing (the drift-pin that just did its job: isw_exclusion.py landed and
        # revised the anchor -- harness scale, harness edge, and calc must move together).
        self.assertAlmostEqual(harness.OBSERVATIONS["mu_window_edge_x"], msi.EDGE, places=12)

    def test_isw_window_lives_in_data_layer_not_admissibility(self):
        # THE SCREENED SPLIT: the ISW window edge is OBSERVATION -> it bounds data_consistent, never
        # admissibility. x above the edge stays admissible; and editing the observed edge changes the
        # data verdict but NEVER admissibility (the cardinal invariant, strengthened).
        inside = harness.evaluate(harness.universe("in", projector="interior", x=0.03), self.claims)
        outside = harness.evaluate(harness.universe("out", projector="interior", x=0.70), self.claims)
        self.assertTrue(inside["admissible"] and outside["admissible"])
        self.assertTrue(bool(inside["data_consistent"]))
        self.assertFalse(bool(outside["data_consistent"]))
        widened = dict(harness.OBSERVATIONS, mu_window_edge_x=1.0)
        r2 = harness.evaluate(harness.universe("out2", projector="interior", x=0.70), self.claims, widened)
        self.assertTrue(bool(r2["data_consistent"]))              # data verdict follows the observation...
        self.assertEqual(outside["admissible"], r2["admissible"])  # ...admissibility does not move.

    def test_trace_only_exclusion_is_structural_not_data(self):
        # trace-only stays inadmissible, but on the SEPARATE-UNIVERSE (internal/structural) leg alone;
        # the empirical ISW grounds migrated to the data layer (now the COMPUTED ~2.0sigma cross +
        # the lensing-bound window -- the retired 32 appears nowhere live).
        u = harness.universe("tr", projector="trace-only")
        adm, rep = harness.admissible(u, self.claims)
        self.assertFalse(adm)
        blob = str(rep)
        self.assertIn("SEPARATE", blob.upper())
        self.assertIn("DATA-layer", blob)

    def test_interior_structural_range_fence(self):
        # the [0,1) fence itself (firewall tightening 2026-08-03): x=1.0 (the trace-only ENDPOINT)
        # and x<0 are structurally inadmissible -- previously exercised live but pinned nowhere.
        for x in (1.0, -0.1):
            u = harness.universe("edge", projector="interior", x=x)
            adm, _ = harness.admissible(u, self.claims)
            self.assertFalse(adm, f"interior x={x} must be structurally inadmissible")

    def test_trace_only_exclusion_basis_is_structured(self):
        # pin the exclusion GROUNDS structurally, not by prose substring (firewall tightening): a
        # legitimate reword keeps passing; an illegitimate regrounding (e.g. onto the ISW) fails.
        u = harness.universe("tr2", projector="trace-only")
        adm, rep = harness.admissible(u, self.claims)
        self.assertFalse(adm)
        self.assertEqual(rep["mu_linear"]["exclusion_basis"], "separate-universe-endpoint")
        # and trace-only maps to the banked x=1 family member in the DATA layer (defense-in-depth:
        # the ISW leg of the endpoint exclusion stays expressible downstream of admissibility).
        p = harness.forward_mu(u["kernel"])
        self.assertEqual(p["x"], 1.0)
        self.assertAlmostEqual(p["mu"], 4.0 / 3.0, places=12)

    def test_clean_TT_vacuum_admissible(self):
        r = harness.evaluate(harness.universe("clean"), self.claims)
        self.assertTrue(r["admissible"])

    # ---- forward map: derived vs inserted-input ----
    def test_single_scale_wz_is_derived_lcdm(self):
        p = harness.forward_wz({"second_scale": None})
        self.assertEqual(p["w0"], -1.0)
        self.assertEqual(p["wa"], 0.0)
        self.assertFalse(p["needs_unsourced_input"])

    def test_second_scale_flags_inserted_input(self):
        # an inserted 2nd scale -> evolving + needs_unsourced_input (the SIGN-AGNOSTIC invariant; the
        # no-match result is carried by the invariant, NOT by the wa sign -- rung7_w2 overseer ruling).
        p = harness.forward_wz({"second_scale": 1e3, "tuned_active": False})
        self.assertTrue(p["needs_unsourced_input"])
        self.assertTrue(p["evolves"])
        # the sign is now frontier-indeterminate; the representative is chosen DESI-sign (wa<=0) for the showcase
        self.assertLessEqual(p["wa"], 0)
        self.assertIn("frontier", p.get("sign_status", ""))

    def test_decoherence_signature_follows_from_N(self):
        p = harness.forward_decoherence({"L0": 1.0, "T": 1.0})
        self.assertEqual(p["basis"], "energy")
        self.assertFalse(p["needs_unsourced_input"])  # shape derived from N, not inserted

    # ---- NO TUNING-AS-LAUNDERING ----
    def test_tuned_desi_match_flags_laundering(self):
        r = harness.evaluate(harness.universe("tuned", second_scale=1e3, tuned_active=True), self.claims)
        self.assertTrue(r["admissible"])                       # not a no-go violation -> admissible
        self.assertFalse(r["data_consistent"])                 # a tuned match does NOT pass
        self.assertTrue(r["data_comparison"]["laundering_flag"])

    def test_clean_lcdm_is_data_consistent_without_laundering(self):
        r = harness.evaluate(harness.universe("clean"), self.claims)
        self.assertTrue(r["data_consistent"])
        self.assertFalse(r["data_comparison"]["laundering_flag"])

    # ---- default-broken + no graduation ----
    def test_empty_admissible_set_is_valid(self):
        family = [harness.universe("a", projector="trace-only"),
                  harness.universe("b", T=0.0),
                  harness.universe("c", spectral_form="free-streaming")]
        summary = harness.sample_family(self.claims, family)
        self.assertEqual(summary["n_admissible"], 0)          # empty set is a real, returnable result
        self.assertEqual(summary["admissible_ids"], [])

    def test_no_universe_is_ever_shown(self):
        for u in (harness.universe("x"), harness.universe("y", projector="trace-only")):
            self.assertNotEqual(u["tier"], "shown")
            self.assertEqual(u["tier"], "candidate")

    # ---- firewall-found laundering holes: now closed ----
    def test_inserted_input_match_flagged_under_any_precision(self):
        # widening the precision must NOT let an inserted-input (2-scale) universe collect a clean match.
        u = harness.universe("u2", second_scale=1e3)              # wa<0 (DESI-sign), needs_unsourced_input
        wide = dict(harness.OBSERVATIONS, w_precision=0.5)        # widen so |wa|=0.3 reads near LambdaCDM
        r = harness.evaluate(u, self.claims, wide)
        self.assertTrue(r["admissible"])
        self.assertFalse(r["data_consistent"])                   # an inserted-input match is NOT clean
        self.assertTrue(r["data_comparison"]["laundering_flag"])  # the LCDM branch is now guarded too

    def test_evolving_DESI_sign_branch_still_flagged_laundering(self):
        # rung7_w2 ruling: the passive 2-scale representative now carries the DESI-SIGN (dissipative) branch
        # -- it MATCHES DESI's wa sign within precision, yet must STILL be refused on inserted-input grounds
        # alone (the no-match result is carried by the evolving=>needs_unsourced_input INVARIANT, not the sign).
        u = harness.universe("desi_sign", second_scale=1e3)
        r = harness.evaluate(u, self.claims)
        wz = r["predictions"]["wz"]
        self.assertLess(wz["wa"], 0)                                  # DESI's sign
        self.assertTrue(wz["wa"] * harness.OBSERVATIONS["desi_wa"] > 0)
        self.assertTrue(r["admissible"])                              # not a no-go violation
        self.assertTrue(r["data_comparison"]["per_observable"]["wz"]["near_desi_evolving"])  # matches DESI's sign
        self.assertTrue(r["data_comparison"]["laundering_flag"])      # ...yet flagged
        self.assertFalse(r["data_consistent"])                       # ...and refused

    def test_omitted_evolves_key_cannot_smuggle_clean_match(self):
        # firewall (omitted-key lens): a hand-built wz that OMITS 'evolves'/'needs_unsourced_input' must NOT
        # collect a clean DESI match -- the guard keys on the OBSERVABLE (wa != 0), not the self-declared flag.
        smuggle = {"wz": {"w0": -0.95, "wa": -0.4},                       # DESI-sign, NO evolves/needs keys
                   "decoherence": {"S_at_zero": 0.0}}
        report = harness.data_consistent(smuggle)
        self.assertTrue(report["laundering_flag"])                       # nonzero wa => evolving => flagged
        self.assertFalse(report["data_consistent"])                      # never clean
        # and a genuine flat LambdaCDM (wa=0) is still clean
        flat = {"wz": {"w0": -1.0, "wa": 0.0, "evolves": False, "needs_unsourced_input": False},
                "decoherence": {"S_at_zero": 0.0}}
        self.assertTrue(harness.data_consistent(flat)["data_consistent"])

    @unittest.skipUnless(__debug__, "forward_map's key assert is stripped under python -O; "
                                    "the -O-safe guard is the data_consistent hardening, tested above")
    def test_forward_map_requires_explicit_evolves_key(self):
        # forward_map must reject a wz missing the explicit flags (defense-in-depth for the forward path)
        k = harness.universe("fm", second_scale=1e3)["kernel"]   # a complete kernel (tidal/deco need L0,T)
        orig = harness.forward_wz
        try:
            harness.forward_wz = lambda kern: {"w0": -0.95, "wa": -0.4, "rung": "rung7_wz"}  # drops the keys
            with self.assertRaises(AssertionError):
                harness.forward_map({"kernel": k})
        finally:
            harness.forward_wz = orig

    def test_sign_flip_leaves_clean_count_unchanged(self):
        # the sign correction must NOT change which universes are CLEAN: only the single-scale LambdaCDM is
        # clean; both evolving branches (DESI-sign passive + tuned) stay laundering-flagged, never clean.
        family = [harness.universe("c1"),                                  # single-scale -> clean LambdaCDM
                  harness.universe("c2", second_scale=1e3),               # DESI-sign passive -> flagged
                  harness.universe("c3", second_scale=1e3, tuned_active=True)]  # tuned -> flagged
        summary = harness.sample_family(self.claims, family)
        self.assertEqual(summary["n_data_consistent_clean"], 1)           # still exactly one clean (the LCDM)
        self.assertEqual(summary["data_consistent_ids"], ["c1"])

    def test_live_inserted_input_without_provenance_inadmissible(self):
        # a live inserted input whose provenance key is missing is un-sourced -> inadmissible
        u = harness.universe("nosrc", second_scale=1e3)
        del u["provenance"]["second_scale"]
        adm, rep = harness.admissible(u, self.claims)
        self.assertFalse(adm)
        self.assertFalse(rep["provenance_consistent"])

    def test_sourcing_to_closed_claim_inadmissible(self):
        # cannot source a kernel choice to closed ground (mu_linear is a no_go_export)
        u = harness.universe("closed")
        u["provenance"]["projector"] = "mu_linear"  # closed disposition (no_go_export)
        adm, rep = harness.admissible(u, self.claims)
        self.assertFalse(adm)
        self.assertFalse(rep["provenance_consistent"])

    def test_open_source_rung3_not_false_flagged(self):
        # rung3's sub_status reads 'neither derived nor refuted' (OPEN) -- must NOT be treated as closed
        u = harness.universe("ok")  # spectral_form is sourced to rung3 by default
        adm, _ = harness.admissible(u, self.claims)
        self.assertTrue(adm)

    def test_L0_zero_does_not_crash(self):
        # an off-premise L0=0 spec must be cleanly inadmissible, not a ZeroDivisionError
        r = harness.evaluate(harness.universe("z0", L0=0.0, spectral_form="single-pole"), self.claims)
        self.assertFalse(r["admissible"])

    # ---- the harness writes no physics input; register stays GREEN +15 ----
    def test_register_unchanged_green_plus15(self):
        # sampling a whole family must not change the register
        before = [c["ledger_delta"] for c in load_claims()]
        harness.sample_family(self.claims, [harness.universe("z"), harness.universe("z2", second_scale=1e3)])
        after = load_claims()
        self.assertEqual([c["ledger_delta"] for c in after], before)  # untouched
        with open(os.path.join(HERE, "sources.json")) as f:
            source_ids = {k for k in json.load(f) if not k.startswith("_")}
        # SCOPED 2026-08-04: these assertions are about GRUT'S register. The same file now also
        # carries the vacuum-cluster physics map under a different vocabulary and a separate
        # ledger (validate_scoped.py); it must not enter GRUT's count.
        grut = [c for c in after if c.get("ledger_scope", "grut") == "grut"]
        r = audit(grut, source_ids, DEFAULT_TIERS)
        self.assertTrue(r.ok)
        self.assertEqual(r.net, 15)
        self.assertEqual(len(grut), 50)   # 46 + the x-floor wave's three delta-0 nodes (2026-08-09: passivity_channel_diagonal, x_no_pin_theorem, kk_static_transfer)


if __name__ == "__main__":
    unittest.main(verbosity=2)
