"""Tier provenance -- no tier moves silently again.

WHY THIS LAYER EXISTS (2026-09-13). Commit 67059a8 moved EIGHT nodes shown ->
derived-pending inside a commit titled 'R1/R2 complete + format pass': zero in-commit
rationale, no tier_note change, and a whole-file reformat that made even the textual diff
unreadable. The move was honest in content (P1A_EDGE_ADJUDICATION_01 later ruled the
demotions legitimately reachable) and defective in provenance -- it had to be
RECONSTRUCTED by field-level git archaeology, and the in-tree comment that first recorded
it undercounted the set by half (four of eight). The register's own certificate (dc110ba)
discloses this as unblessed paperwork.

THE RULE: `provenance/TIER_BASELINE.json` pins every node's tier (and the node set
itself). A tier change, node addition, or node removal is legal ONLY as a commit that
also updates the baseline and appends a changelog entry carrying date, authority, and
rationale. A drift between register and baseline is therefore always one of two things: a
silent change (the 67059a8 defect, now named by a failing test) or a half-done legal
change (baseline edited, changelog forgotten -- also named). The changelog is
APPEND-ONLY; git guards deletions, and the seed entries record the three changes already
reconstructed at inception.

This guards BOOKKEEPING, not physics: nothing here says a tier is right -- only that it
cannot move without leaving a record the suite can see.
"""
import json
import os
import re
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))


def _load():
    with open(os.path.join(HERE, "claims.json")) as f:
        claims = json.load(f)["claims"]
    with open(os.path.join(HERE, "TIER_BASELINE.json")) as f:
        pin = json.load(f)
    return claims, pin


class TestTierProvenance(unittest.TestCase):

    def test_every_tier_matches_the_baseline(self):
        """The core assertion: register tiers == pinned baseline, node-for-node.

        On failure, the remedy is NOT to silence this test: update TIER_BASELINE.json's
        `baseline` AND append a `changelog` entry (date, authority, rationale) in the
        SAME commit as the register change. A tier change without that record is the
        67059a8 defect."""
        claims, pin = _load()
        base = pin["baseline"]
        current = {c["id"]: c.get("tier") for c in claims}
        drifted = []
        for cid, tier in current.items():
            if cid not in base:
                drifted.append(f"NODE ADDED silently: {cid!r} (tier {tier!r}) is not in the baseline")
            elif base[cid] != tier:
                drifted.append(f"TIER MOVED silently: {cid!r} {base[cid]!r} -> {tier!r}")
        for cid in base:
            if cid not in current:
                drifted.append(f"NODE REMOVED silently: {cid!r} (was {base[cid]!r})")
        self.assertFalse(drifted,
                         "register tiers drifted from TIER_BASELINE.json with no record:\n  "
                         + "\n  ".join(drifted)
                         + "\nRemedy: update the baseline AND append a changelog entry "
                           "(date, authority, rationale) in the same commit. A tier change "
                           "with no changelog entry is the 67059a8 defect this test exists "
                           "to prevent.")

    def test_changelog_entries_are_well_formed(self):
        """Every entry must carry a date, a non-empty authority, a non-empty rationale,
        and a changes map of id -> [from, to] with from != to (None = added/removed)."""
        _claims, pin = _load()
        log = pin.get("changelog", [])
        self.assertTrue(log, "the changelog may not be emptied -- it is append-only history")
        for i, e in enumerate(log):
            where = f"changelog[{i}]"
            self.assertTrue(re.match(r"^\d{4}-\d{2}-\d{2}", str(e.get("date", ""))),
                            f"{where}: date must start YYYY-MM-DD, got {e.get('date')!r}")
            self.assertTrue(str(e.get("authority", "")).strip(),
                            f"{where}: authority is empty -- a tier change needs a named authority")
            self.assertTrue(str(e.get("rationale", "")).strip(),
                            f"{where}: rationale is empty -- 'format pass' is not a rationale")
            changes = e.get("changes", {})
            self.assertTrue(changes, f"{where}: changes map is empty")
            for cid, pair in changes.items():
                self.assertEqual(len(pair), 2, f"{where}:{cid}: changes need [from, to]")
                self.assertNotEqual(pair[0], pair[1],
                                    f"{where}:{cid}: from == to ({pair[0]!r}) records no change")

    def test_seed_history_is_present(self):
        """The three reconstructed changes at inception stay recorded: the 8e64588
        retirement, the d5e9a99 bank, and the 67059a8 eight-node demotion. Removing a
        seed entry is history-rewriting, which this file forbids."""
        _claims, pin = _load()
        commits = {e.get("commit") for e in pin.get("changelog", [])}
        for want in ("8e64588", "d5e9a99", "67059a8"):
            self.assertIn(want, commits,
                          f"seed changelog entry for {want} is missing -- the changelog is "
                          f"append-only and inception history stays")
        eight = [e for e in pin["changelog"] if e.get("commit") == "67059a8"]
        self.assertEqual(len(eight), 1)
        self.assertEqual(len(eight[0]["changes"]), 8,
                         "the 67059a8 entry must record all EIGHT demotions -- an earlier "
                         "in-tree comment undercounted the set at four, and the corrected "
                         "count is part of what this file preserves")
