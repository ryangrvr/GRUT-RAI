# v4 TERMINATION RECONCILIATION (Product B, quarantined) — the criterion-by-criterion matrix

**Date (as-of):** 2026-09-27 · **Authority:**
`GR2_SYNTHESIS_OWNER_RULING_01.md` ("Proceed with the quarantined v4
termination reconciliation"), under the hard rule quoted below.
**The condition reconciled:** `provenance/prereg/PREREG_TERMINATION_V4_2026-08-10.txt`,
sha256 `f4bc613c5ec38cd7fe780366d710c7b0e0741f50586ff5f75dde73ded9a8fa61`
(verified on disk this date), **IN FORCE since the logged signing of
2026-08-10** (signatory D. Ryan Grover; clerical name correction logged
2026-08-12). **The binding record of channel states:** the canonical
append-only event log `provenance/prereg/RESULT_TERMINATION_events.txt`
(last entry 2026-08-12), per v4's R4 ("quotes decide, entries assert
nothing") and its log rule. Supporting obligation text:
`STAGE_CLOSE_2026-08-09.md`.

**The hard rule (the owner's, binding on this document):**

> The v4 reconciliation may determine the historical status of the v4
> termination criteria; it may not modify the scientific conclusions of
> GR2. [...] Do not retroactively change the meaning of a v4 criterion
> because GR2 produced a different result. If a criterion demanded
> something GR2 now shows was not derived, the reconciliation should
> say so plainly.

## 0. What this document is, and is not

- It is a **historical status matrix** of the v4 criteria as of
  2026-09-27, each classification tied to the sealed v4 wording and the
  canonical log's quoted entries.
- It is **NOT the v4 deposit.** Under R5 the deposit is written only
  "in the first wave after the stop, within one calendar month," in
  v4's own one-line-per-channel form. The stop has not fired (§1), so
  the deposit is not due, and nothing here preempts its form or
  content.
- Per R2 ("this file executes nothing"), this document likewise
  **executes nothing**: no node consequence, no register move, no
  channel-line change.
- It **modifies no GR2 conclusion**, adopts no re-pose of C1, and
  changes the meaning of no criterion.

## 1. Finding 0 — the stop clock (R5, verbatim against the record)

R5: *"in-house physics calculation STOPS at the earliest of (i)
2026-12-31; (ii) both Part-7 fronts discharged (calc completed, or
retired with a statement naming what dies and why); (iii) a logged
reply whose own words assert the cut class unconditionally."*

| trigger | v4 wording requires | record | fired? |
|---|---|---|---|
| R5(i) | the date 2026-12-31 | today is 2026-09-27 | **NO** |
| R5(ii) | both Part-7 fronts discharged | C3 and C5 both undischarged (rows below) | **NO** |
| R5(iii) | a logged reply asserting the cut class unconditionally | no reply from the audience of record is logged at all; the one quoted-reply entry was reclassified in the log itself as in-house tool output, and its quoted words assert neither class | **NO** |

**Consequences, stated plainly:** (a) the v4 condition is in force and
its clock is **running**; (b) in-house physics calculation is
**permitted** until the stop fires — the entire GR-2 campaign
(2026-09-26/27) was in-house calculation conducted legitimately under
the running clock, and nothing in GR-2 fired, advanced, or blocked any
stop trigger; (c) the deposit is a **future obligation**, due within
one calendar month after whichever trigger fires first (earliest
candidate: 2026-12-31 under R5(i)).

## 2. The matrix

Each row: the criterion's verbatim operative wording (per R4, quotes
decide); the evidence that wording requires; the canonical-log state;
the v4-native channel line (R1: RESOLVED or STILL OPEN with cause —
"there is no third form"); and the owner's-scheme classification.

| # | criterion (verbatim core) | required evidence (per its own wording) | canonical-log state | v4-native line | **classification** |
|---|---|---|---|---|---|
| R5(i) | "in-house physics calculation STOPS at the earliest of (i) 2026-12-31" | arrival of the date | date not reached | (clock rule; running) | **NOT SATISFIED** |
| R5(ii) | "(ii) both Part-7 fronts discharged (calc completed, or retired with a statement naming what dies and why)" | C3 and C5 each RESOLVED per their own texts | neither discharged | (clock rule; running) | **NOT SATISFIED** |
| R5(iii) | "(iii) a logged reply whose own words assert the cut class unconditionally" | a logged reply, its operative words quoted, asserting CUT unconditionally | none exists; the 2026-08-10 quoted material is in-house tool output per the log's own clarifying entry, and asserts neither class | (clock rule; running) | **NOT SATISFIED** |
| C1 | "THE DISPATCH (pole-vs-cut...). RESOLVED: (a) a reply asserts the POLE class in its own words, unconditionally; (b) ... the CUT class likewise" | a send to the audience of record (two author groups) logged with words quoted; a qualifying reply | "the dispatch remains unsent as of this entry" (signing entry); the clarifying entry: "with no logged transmission to the audience of record, C1's still-open cause is 'unsent'"; the research note marks the dispatch HELD with the ill-posedness evidence on its face; a candidate re-pose is recorded, **not adopted** | **STILL OPEN — cause: unsent** (R1) | **NOT SATISFIED** |
| C2 | "DESI DR3... RESOLVED: (a) a crossing at the frozen threshold, agreed across the release's own headline combinations; (b) constancy at the release's own grade..." | a public release landed and consumed; for (a), an R3-frozen crossing threshold manifested BEFORE the release | no DR3 event has landed in the log; **no crossing threshold has been frozen in a manifested instrument**, so per R3's own mechanics outcome (a) presently *cannot fire* — that foreclosure is stated here as R3 requires | **STILL OPEN — cause: data not landed** (R1) | **NOT TESTED** |
| C3 | "THE TT-AUTO CALC (first Part-7 front)... RESOLVED: (a) a register-grade window SURVIVES... ships as an ALLOWANCE, never a prediction (Q2); (b) the family EXCLUDED at register grade...; (c) RETIRED with a statement naming what dies and why" | a register-grade run under the operative gate record ("the SECOND freeze of calc/isw_tt_auto.py"), or a retirement statement | 2026-08-09: "The Part-7 calcs named in channel C3's scope were NOT executed this stage; C3 remains in its pre-registered 'still open' state"; no later C3 event. (The file `calc/isw_tt_auto.py` exists in this repository via the clean-rebuild import, commits `2c522b2`/`fb1242f`; file presence is not a register-grade run, and per R4 the channel state is the log's.) | **STILL OPEN — obstruction: unrun** (R1) | **NOT SATISFIED** |
| C4 | "THE METHOD (node method_novelty). RESOLVED: full discharge of Q3, all three legs... Anything less — no uptake, adoption without a caught error, any proper subset of the legs: STILL OPEN" — Q3: "GRADUATES... ONLY on independent EXTERNAL validation — a DIFFERENT team, on a DIFFERENT problem, where the method's discipline catches a REAL error **(not its own)**" | an external team, external problem, real error caught by the method's discipline — all three legs, with quotes | zero legs discharged; the standing audited line: "no outside physicist has answered any physics question put by this program" (complete 49/49 audit, log entry 2026-08-12) | **STILL OPEN — cause: no uptake; zero legs discharged** (R1) | **NOT SATISFIED** |
| C5 | "THE XI_IJ / GAMMA_T CALC (second Part-7 front)... RESOLVED: (a) computed at register grade, consumed at its own node per R2; (b) RETIRED with a statement naming what dies and why" | a register-grade computation consumed at its node, or a retirement statement | the obligation stands exactly as recorded: "ξ_ij ... and the Boltzmann-grade TT-auto channel ... are next-stage scope or abandoned-with-statement; this file records that they are OWED-OR-RETIRED, not quietly dropped" (`STAGE_CLOSE_2026-08-09.md`); no later C5 event | **STILL OPEN — cause: unrun; owed-or-retired** (R1) | **NOT SATISFIED** |

**Labels not used, and why:** no criterion is **SATISFIED** or
**PARTIALLY SATISFIED** on the current record (C4's three legs stand at
zero, not a fraction; C1's in-house attempts touch no channel line by
the log's own rulings). No v4 criterion is **SUPERSEDED**: v4
superseded v1/v2, but nothing has superseded any criterion *of* v4 —
the one vocabulary drift (the v1/v2 "six-month window" imported into a
log entry) was corrected inside the log itself on 2026-08-10 and never
belonged to v4.

## 3. The C4 name collision (flagged so it cannot mislead)

The GR-2 records repeatedly say results feed **"C4"** — e.g. GR2-b/c/d
verdicts: "the demonstration half of an irreducibility certificate ...
feeding C4 and Layer 7." That "C4" is the **completion problem** (the
irreducibility-certificate coordinate of the completion program). It is
**not** v4's channel **C4** (method_novelty / Q3 graduation). No GR2
statement about the completion problem reads on the termination
channel, and this reconciliation counts none of them toward it. The
collision is recorded here precisely so the hard rule cannot be
violated by vocabulary accident.

## 4. Where GR2 bears on the v4 criteria — said plainly, without changing any meaning

1. **C4/Q3 demanded external validation; GR2 supplied internal
   validation only.** GR2's identity-gate catches (GR2-b run 1, GR2-c
   run 1, GR2-d's pre-run Amendment 01) are the method's discipline
   catching **its own** errors, in-house — exactly the class Q3's own
   words exclude ("not its own"). They advance C4 by zero legs. If the
   program wants credit for those events under a method criterion, that
   requires a *new* criterion adopted by the owner, never a rereading
   of Q3.
2. **C3 and C5 are computations in a channel whose definition rests on
   supplied structure that GR2 has now adjudicated as unforced.** The
   TT channel is classified in the record under TT-1's supplied
   premise (per-sector v = c), and GR2-d/d2 adjudicated the common
   causal cone as an unforced primitive (with an in-class quantum
   counterexample pair). This changes **nothing** about C3/C5's
   criteria, their still-open status, or Q2's meaning — Q2's own text
   already caps any survival at "ALLOWS up to the edge; it predicts
   nothing." It means a future C3 RESOLVED(a) allowance would ship
   with its supplied premises now explicitly graded by the GR2 record.
   Stated per the owner's instruction: **the v4 fronts presuppose, in
   their channel's physics, structure that GR2 has now shown the core
   does not derive** — and the criteria are reported against their
   original wording regardless.
3. **No GR2 result fires, advances, or blocks any stop trigger**, and
   no GR2 result is rounded into any channel's RESOLVED form (R1:
   "still-open is never rounded into a resolved outcome").

## 5. The disposition (as of 2026-09-27)

> **The v4 termination condition is IN FORCE and RUNNING. No criterion
> is satisfied, in whole or in part. No stop trigger has fired. The
> deposit is not yet due. Both Part-7 fronts remain OWED-OR-RETIRED.
> The dispatch remains unsent and HELD. C2 awaits data that has not
> landed and a threshold that was never frozen. C4 stands at zero of
> three legs, and GR2's internal catches cannot be counted toward it
> under Q3's own words.**

The historical criteria are reported exactly as sealed; nothing here
reinterprets them in the light of GR2, and nothing in GR2 is modified
by them.

## 6. Standing and next steps (all the owner's)

- **This matrix awaits the owner's independent adjudication** (the
  authorizing ruling: "After the reconciliation is independently
  adjudicated, we can make one dated public-record update").
- After that adjudication, the single dated public-record update
  proceeds with its five recorded items (campaign completion;
  GRAVITY_UNDERDETERMINED; the dependency boundary; the v4 disposition
  separately identified; the GR2-a editorial instruction applied
  without upgrading any claim). **The public paper remains untouched
  until then.**
- Separately and later, the **v4 deposit** comes due within one
  calendar month after the stop fires (earliest candidate 2026-12-31),
  in v4's own one-line-per-channel form — a distinct future document
  that this reconciliation does not preempt.

**HARD STOP.** Reconciliation recorded pending owner adjudication.
