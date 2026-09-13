# P6_RATIFICATION_PACKAGE_01 — proposed amendments for the nine declared stale-net cases

**Status: PROPOSAL ONLY — NOTHING IN THIS FILE HAS BEEN APPLIED.** P6's stanza rules
amending these public-facing documents "a wave-governed act rather than a bookkeeping
edit" that "CLOSES WHEN: the owner rules on whether to amend the four documents, and the
amendment lands." The owner also directed (2026-09-12): leave the nine cases exactly
where they are until the P6 ruling. This package exists so that ruling can be a one-word
ratification (or a per-line selection); on ratification the amendments land, the nine
declarations are removed from `expected_red.py`, the stale-net test goes green, and P6
closes with the ruling recorded. Rejection costs nothing — the cases stay declared-red.

Register truth as of `e76953a`: **net +16 · 74 nodes (53 GRUT-scope + 21 vacuum-cluster)
· waived-by-stance +9 across 4 waivers** (`rung1_inin_formalism` +4, `rung5_gr_limit` +2,
`rung6_qm_limit` +2, `p_tt_ansatz` +1 — validate.py's own output, 2026-09-13).

Each case below: the defect, the proposed replacement (verbatim old → new), and the
principle used (correct-the-figure for present-tense state; historical-cue for genuine
history — the test's own two remedies). Line numbers are as declared; anchors are matched
by text at apply time, so drift-proof.

---

## Case 1+2 — `GRUT_ToE.md:7` and `README.md:19` (identical vocabulary gloss)

**Defect:** the gloss teaches the vocabulary on a stale example ("net +13 ... unchanged
for weeks and meant to stay unchanged" — false twice over: the figure moved, and it is
*meant to move only by adjudicated events*, which is the more accurate lesson).

**Proposed (correct figure + repair the claim):**
- OLD: `**net +13** is the blind SUM of the register's underived-input ledger — the standing price of every assumption, unchanged for weeks and meant to stay unchanged — not a count of new entries;`
- NEW: `**net +16** is the blind SUM of the register's underived-input ledger — the standing price of every assumption, moving only by dated, owner-adjudicated events (+13 → +15 → +17 → +16 across 2026-08, each in the build log) — not a count of new entries;`

## Case 3 — `GRUT_ToE.md:53` (validator description)

**Defect:** present-tense tool description with stale numbers.
- OLD: `**GREEN at net +13 (GRUT); 70 nodes total (49 GRUT-scope + 21 cluster).**`
- NEW: `**GREEN at net +16 (GRUT); 74 nodes total (53 GRUT-scope + 21 cluster).**`

## Case 4 — `GRUT_ToE.md:172` (the itemized-inputs passage)

**Defect:** present-tense "Net **+13**" heading an itemization that was true at its
writing (19 named items). Updating the itemization is content work beyond a P6 edit.

**Proposed (historical cue; RECOMMENDED):**
- OLD: `Net **+13**. (The list names 19 dependency *items*;`
- NEW: `Net **+13** as of this section's 2026-08 itemization (current net: the REGISTER-SYNC stamp in the header). (The list names 19 dependency *items*;`

*Alternative (owner may prefer): re-itemize the section against the live register — a
wave-scale rewrite, not proposed here.*

## Case 5 — `GRUT_ToE.md:243` (runbook line)

**Defect:** a runbook comment pinning numbers the tool itself prints — the exact pattern
(hand-typed figure beside a machine emitter) that the SYNC stamps were invented to end.

**Proposed (number-free; RECOMMENDED):**
- OLD: `python3 provenance/validate.py        # the gate: GREEN, net +13 GRUT (70 nodes total)`
- NEW: `python3 provenance/validate.py        # the gate: prints the live net and counts (pinned by the REGISTER-SYNC stamp above)`

## Cases 6+7 — `GRUT_ToE.md:252` and `:253` (dated build-log entries)

**Defect:** genuinely historical lines (dated log entries) whose "net +13" lacks a cue
string the test recognizes.

**Proposed (minimal cue insertion, history untouched):** in each entry, replace
`net +13` → `net +13 at that adjudication` (the test's own recognized cue; figures and
all other text unchanged).

## Case 8 — `README.md:22` (the front-matter summary paragraph)

**Defect:** present-tense front-matter with four stale facts: the net (+13→+16), the
counts (49+21=70 → 53+21=74), the waived total (+8 over waivers listed at +3/+2/+2/+1 →
+9 at +4/+2/+2/+1), and a deleted node name (`rung1_inin_action` → split 2026-08-23 into
`rung1_inin_formalism`).

**Proposed:**
- OLD: `> physical picture (net **+13** GRUT; 49 GRUT-scope nodes + 21 vacuum-cluster = 70 in \`claims.json\`, validator GREEN). Of the **+13**, **+8 rides on four declared \`laundering_ok\` waivers** (\`rung1_inin_action\` +3, \`rung5_gr_limit\` +2, \`rung6_qm_limit\` +2, \`p_tt_ansatz\` +1), each carrying a written stance justification`
- NEW: `> physical picture (net **+16** GRUT; 53 GRUT-scope nodes + 21 vacuum-cluster = 74 in \`claims.json\`, validator GREEN). Of the **+16**, **+9 rides on four declared \`laundering_ok\` waivers** (\`rung1_inin_formalism\` +4, \`rung5_gr_limit\` +2, \`rung6_qm_limit\` +2, \`p_tt_ansatz\` +1), each carrying a written stance justification`

## Case 9 — `GRUT_II_What_Survived.md:83` (the Version-I retrospective banner)

**Defect:** a retrospective document's banner reading as present tense ("45 nodes · net
+13 · … 109 register tests").

**Proposed (historical cue; the figures are the point of the document and stay):**
- OLD: `**45 nodes · net +13 · \`validate.py\` PASS (register hygiene) · 109 register tests + the mutation battery.**`
- NEW: `**As of the Version I close: 45 nodes · net +13 · \`validate.py\` PASS (register hygiene) · 109 register tests + the mutation battery.** *(Live figures: the REGISTER-SYNC stamp in this file's header.)*`

---

## On ratification (mechanics, pre-stated)

1. Apply the ratified subset verbatim (assert-before-write on every anchor).
2. Remove exactly the corresponding declared cases from `expected_red.py`'s P6 entry
   (stale-case discipline); if all nine land, remove the declaration and close P6's
   stanza with the ruling (append-only).
3. Regenerate ripple targets (SYNC markers unaffected — none of these edits touches a
   marker); doc pins re-checked and re-accepted last.
4. Full suite + `expected_red.py`; the stale-net test must go green (or shrink to the
   unratified remainder); commit citing this package and the ruling; push.
5. Also in the same wave (builder-scope tool fix, no P6 ruling needed, listed for
   visibility): `validate.py`'s hardcoded output prose "the +8 is in the net" → computed
   figure (its own printed waived total is already correct at +9; only the prose constant
   is stale).

*Package prepared 2026-09-13. The 10th former case (GRUT_II_Agenda.md:7) was cued by the
builder inside 161a883 before this package existed — separately disclosed on dc110ba and
still owner-ratifiable; ratifying this package ratifies that call by the same principle
(Case 4 uses the same cue mechanism).*
