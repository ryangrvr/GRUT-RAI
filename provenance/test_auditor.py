#!/usr/bin/env python3
"""Tests for the generalized discipline auditor (auditor.audit / audit_claim).

Mirrors the discipline exactly:
  - a clean claim PASSES;
  - a missing-source claim BLOCKS;
  - an unknown-source claim BLOCKS;
  - a missing-falsifier claim BLOCKS;
  - an invalid tier BLOCKS;
  - a laundering rung (net-positive shown/derived/derived-pending, unflagged) BLOCKS;
  - laundering_ok exempts a declared stance/recovery;
  - assumed + positive WARNS (non-blocking);
  - the engine is NOT GRUT-specific (custom vocab, non-GRUT claims);
  - REGRESSION: the live GRUT register still audits GREEN at net +15.

Pure stdlib (unittest). Run:  python3 provenance/test_auditor.py
"""
import json
import os
import unittest

from auditor import audit, audit_claim, DEFAULT_TIERS

HERE = os.path.dirname(os.path.abspath(__file__))
SRCS = {"src_a", "src_b"}


def claim(**kw):
    """A minimal clean claim; override fields via kwargs."""
    base = dict(
        id="c",
        tier="shown",
        sources=["src_a"],
        overturning_computation="a calc that would falsify it",
        ledger_delta=0,
    )
    base.update(kw)
    return base


class TestAuditor(unittest.TestCase):
    # --- clean ---
    def test_clean_passes(self):
        r = audit([claim()], SRCS)
        self.assertTrue(r.ok)
        self.assertEqual(r.blocking, [])
        self.assertEqual(r.net, 0)

    def test_net_is_blind_sum(self):
        r = audit([claim(id="a", ledger_delta=3, laundering_ok=True, stance_justification="test stance: declared for the 1b waiver-cost rule (2026-08-09) -- a waiver without a stated stance now BLOCKS"),
                   claim(id="b", tier="assumed", ledger_delta=-1)], SRCS)
        self.assertTrue(r.ok)
        self.assertEqual(r.net, 2)

    # --- sourcing ---
    def test_missing_source_blocks(self):
        r = audit([claim(sources=[])], SRCS)
        self.assertFalse(r.ok)
        self.assertTrue(any("NO sources" in b for b in r.blocking))

    def test_unknown_source_blocks(self):
        r = audit([claim(sources=["not_in_register"])], SRCS)
        self.assertFalse(r.ok)
        self.assertTrue(any("not in register" in b for b in r.blocking))

    # --- falsifiability ---
    def test_missing_falsifier_blocks(self):
        r = audit([claim(overturning_computation="")], SRCS)
        self.assertFalse(r.ok)
        self.assertTrue(any("overturning_computation" in b for b in r.blocking))

    # --- tiering ---
    def test_invalid_tier_blocks(self):
        r = audit([claim(tier="totally-made-up")], SRCS)
        self.assertFalse(r.ok)
        self.assertTrue(any("invalid tier" in b for b in r.blocking))

    def test_ledger_delta_must_be_int(self):
        r = audit([claim(ledger_delta=1.5)], SRCS)
        self.assertFalse(r.ok)
        self.assertTrue(any("must be int" in b for b in r.blocking))

    def test_bool_ledger_delta_rejected(self):
        # isinstance(True, int) is True in Python; a JSON `true` must not be miscounted as +1
        r = audit([claim(ledger_delta=True)], SRCS)
        self.assertFalse(r.ok)
        self.assertTrue(any("must be int" in b for b in r.blocking))
        self.assertEqual(r.net, 0)

    # --- anti-laundering ---
    def test_laundering_blocks(self):
        # net-positive on a derivation tier, not flagged => laundering
        r = audit([claim(tier="derived-pending", ledger_delta=2)], SRCS)
        self.assertFalse(r.ok)
        self.assertTrue(any("LAUNDERING" in b for b in r.blocking))

    def test_laundering_blocks_on_shown_and_derived(self):
        for t in ("shown", "derived", "derived-pending"):
            r = audit([claim(tier=t, ledger_delta=1)], SRCS)
            self.assertFalse(r.ok, f"{t}+1 unflagged must block")
            self.assertTrue(any("LAUNDERING" in b for b in r.blocking))

    def test_laundering_ok_exempts(self):
        r = audit([claim(tier="shown", ledger_delta=3, laundering_ok=True, stance_justification="test stance: declared for the 1b waiver-cost rule (2026-08-09) -- a waiver without a stated stance now BLOCKS")], SRCS)
        self.assertTrue(r.ok)
        self.assertEqual(r.blocking, [])

    def test_assumed_positive_warns_not_blocks(self):
        r = audit([claim(tier="assumed", ledger_delta=2)], SRCS)
        self.assertTrue(r.ok)                       # warning, not blocking
        self.assertEqual(r.blocking, [])
        self.assertTrue(any("recovery-with-imports" in w for w in r.warnings))

    def test_negative_or_zero_delta_never_launders(self):
        for t in ("shown", "derived", "derived-pending", "assumed", "to-derive"):
            r = audit([claim(tier=t, ledger_delta=-1)], SRCS)
            self.assertTrue(r.ok, f"{t} with -1 must not block")
            self.assertEqual(r.warnings, [])

    # --- single-claim API ---
    def test_audit_claim_returns_tuple(self):
        blocking, warnings, delta, flagged = audit_claim(
            claim(ledger_delta=3, laundering_ok=True, stance_justification="test stance: declared for the 1b waiver-cost rule (2026-08-09) -- a waiver without a stated stance now BLOCKS"), SRCS)
        self.assertEqual(blocking, [])
        self.assertEqual(delta, 3)
        self.assertTrue(flagged)

    # --- generality (NOT GRUT-specific) ---
    def test_works_on_non_grut_claim_set_and_custom_vocab(self):
        custom_tiers = {"observed", "modeled"}
        cl = [dict(id="x", tier="observed", sources=["src_b"],
                   overturning_computation="re-measure", ledger_delta=0)]
        r = audit(cl, SRCS, valid_tiers=custom_tiers)
        self.assertTrue(r.ok)
        # the GRUT vocab would have rejected 'observed'
        r2 = audit(cl, SRCS, valid_tiers=DEFAULT_TIERS)
        self.assertFalse(r2.ok)

    # --- regression: the live register stays GREEN at +12 ---
    def test_live_register_audits_green_at_booked_net(self):
        with open(os.path.join(HERE, "sources.json")) as f:
            sources = json.load(f)
        source_ids = {k for k in sources if not k.startswith("_")}
        with open(os.path.join(HERE, "claims.json")) as f:
            claims = json.load(f)["claims"]
        # SCOPED 2026-08-04: GRUT's register only. The file also carries the vacuum-cluster
        # physics map under its own vocabulary and its own ledger (validate_scoped.py).
        claims = [c for c in claims if c.get("ledger_scope", "grut") == "grut"]
        r = audit(claims, source_ids, DEFAULT_TIERS)
        self.assertTrue(r.ok, f"live register must audit clean; blocks={r.blocking}")
        self.assertEqual(r.net, 15, "net ledger must be +15 (the 2026-08-02 restriction booking + the 2026-08-17 rung1 bath-genuineness booking)")
        self.assertEqual(len(claims), 50, "GRUT scope holds 50 nodes (38 GRUT claims incl. eft_operator_basis + zeta_interior_family + the x-floor trio passivity_channel_diagonal/x_no_pin_theorem/kk_static_transfer + 11 borrowed/open-field scaffold + emergence_chain, the building-stage construction node, delta 0)")


if __name__ == "__main__":
    unittest.main(verbosity=2)
