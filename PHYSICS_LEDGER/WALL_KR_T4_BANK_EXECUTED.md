# TIER-4 BANK — EXECUTED

**Date:** 2026-09-01 · **Authorization:** owner relay in-session ("I
would actually bank Tier 4 … execute the formal bank relay for Tier 4
only"). · **Mechanism:** the repository's own bank gate
(`provenance/bankgate.py`), followed exactly.

## WHAT WAS BANKED

Node **`kr_contract_retarded_tier4`** in `provenance/claims.json`:
tier `shown`, **ledger_delta 0** — a scoped computed record, not a
strength claim. No derivation credit accrues to any GRUT rung; rung3
single-pole remains derived-pending; the 2026-08-30 +1 retirement is
untouched. The statement banks the Tier-4 result **with every
conditionality verbatim** (reference-slice-only no-zero bound; |λ| ≪ 1;
ω ≫ H with ω ≪ H refused; NO pole claim; H⁰ locals via the symbolic
Λ_R; H² locals unresolved/fork-gated; Ward excluded-not-repaired) and
explicitly records that it is **NOT a Class-C consequence
classification** (that cell stays CC-C).

## LEDGER, VISIBLE BEFORE/AFTER

| | before | after |
|---|---|---|
| net (blind sum of ledger_delta) | **+16** | **+16** |
| GRUT-scope node count | 52 | **53** |

## THE MECHANISM'S OWN STEPS, AS EXECUTED

1. **bankgate run 1** — my node drew a legitimate TIER-CONTRADICTION
   flag (`shown` resting on `derived-pending` rung3). **Repaired
   honestly, not accepted**: T4 never assumes rung3's single-pole
   claim, so rung3 moved from `depends_on` (now rung1 + rung2, both
   `shown`) to an edge-note cross-reference. The gate's discipline
   improved the node.
2. **bankgate run 2** — the node surfaces as the by-design NEW-NODE
   flag only. Recorded owner-reviewed in the **held-ledger**
   (`held_flags.json`, fingerprint-keyed, single entry) with the
   relay quote. **The baseline was NOT blanket-accepted**: 23
   pre-existing unreviewed flags (accumulated since the last accept)
   remain surfaced by design — sweeping them under a T4-only
   authorization would have laundered them past the firewall.
3. **Designed ripples, each fixed by its documented pattern:** the two
   count pins amended 52 → 53 with riders (`test_auditor.py`,
   `test_resident.py` — the pins' own historical pattern); the node
   declared OFF_CHAIN in the emergence chain ("a record pointed at the
   chain's open anchor, not a link") and `EMERGENCE_CHAIN.md`
   regenerated; the glossary's audit denominator 73 → 74 (numerator 18
   unchanged — the node contains no "specialist"); the doc-register
   pins re-pinned after reconciliation.
4. **Stash-proof suite comparison** (the mechanism's own precedent,
   commit `8e64588`): full provenance suite WITHOUT my changes = 13
   failures (pre-existing, including the two stash-proven at the
   2026-08-30 bank); WITH my changes = **the identical 13** — zero new
   failures, zero silently resolved. `test_auditor` +
   `test_bankgate`: 33/33 green, asserting net +16 and count 53.

## WHAT WAS NOT DONE

No GRUT success claimed; no Class-C outcome assigned (CC-C stands); no
Λ_R value; no H² IR resolution; fork (ii) NOT invoked; no frozen
scientific artifact touched (Tier-4 artifact byte-identical,
`d916ef32…`); the 23 pre-existing bankgate flags NOT accepted; the
two pre-existing test_resident failures NOT patched (stash-proven
pre-existing, per the mechanism's precedent).

## OWNER ITEMS SURFACED BY THIS BANK

- The **23 accumulated pre-existing bankgate flags** await your review
  before any future `--accept` baseline refresh (relay-and-hold, by
  design — but the backlog is now explicitly on your desk).
- The consequence cell remains **CC-C** with its three named unblocks
  (D4 dual-gauge; the low-frequency/epoch-window path; the face
  adjudication) — Option 1 (close the Wall here) requires nothing
  further.
