# Review packet — the termination condition, before signing

> **VERSION 2 EXISTS (2026-08-10): the document now under review is
> `provenance/prereg/PREREG_TERMINATION_2026-08-10.txt`, sealed at `05fa401bc1fe649b…`,
> UNSIGNED and not in force.** It supersedes the 2026-08-09 seal structurally on all seven
> pressure points below: every channel carries an explicit still-open outcome (P1, P2, P5,
> P6-corroboration); no trigger fires across channels — C1(b)'s mu_linear execution is replaced
> by a pre-registered adjudication (P4); thresholded outcomes fire only on thresholds frozen by
> name before the data are read (P7); C3(a) states its own A8 unreachability condition (P3);
> the date/window ranking is explicit (P6); C4(a) quotes the node's falsifier exactly (minor).
> **The outside review should read v2 against P1–P7 as its checklist** — the points below stand
> as the record of what v2 claims to fix, and the review's job is to check it actually does,
> plus anything neither pass found. v1 remains on disk as immutable, unsigned history.

*Prepared 2026-08-09 for adversarial outside review; v2 pointer added 2026-08-10. The original
document reviewed below is `provenance/prereg/PREREG_TERMINATION_2026-08-09.txt`, sealed at
sha256 `c504576ef0a2abd0…` (full hash in `provenance/prereg/MANIFEST.txt`), **UNSIGNED and
therefore not in force**. THE EDIT RULE, stated before anything else: the sealed file is immutable. If
this review finds anything that must change, the remedy is a NEW sealed version superseding the
old — recorded as such in the manifest — never an edit. A fix applied quietly to a sealed stop
condition would be the certifier-inside-the-certified failure, applied to the program's ending.*

## The one question to aim at

**Is "still open" genuinely reportable as an outcome for each channel — or does the document's
structure quietly pressure every channel toward a resolved reading at deposit time?**

This is the honest-uncertainty-flattened-at-the-boundary failure mode, pointed at the document
whose entire job is to bind future behavior. It must be read adversarially before signing,
because after signing every ambiguity resolves under deposit-day incentives, not review-day ones.

## The builder's pre-read: four candidate pressure points (verify, don't inherit)

These are handed over as *questions with evidence pointers*, not verdicts. Each was found by
reading the sealed text against the instruments it cites; the reviewer should re-derive them
independently — the point of an outside read is that it does not inherit in-house conclusions.

**P1 — C2 has no "inconclusive" outcome.** C2's three outcomes are: crossing at kill grade /
strengthens short of kill / consistent with a constant. But the program's own recorded
experience of this exact channel is a fourth state: **dataset-combination-dependent ambiguity**
(that is what DR2 was — the register's own rider on `vc_w_equals_minus_one` records the DR2
significance as SN-compilation-dependent, always model-framed; the packet's first draft dressed
a paraphrase of this in quotation marks, caught by the verification pass and fixed here). If DR3 lands the same way, C2 as sealed has no
labeled home for it, and the nearest bin ("consistency with a constant", (c)) is a *resolved*
reading of an unresolved result. Question: does C2 need an explicit (d) = "no register-grade
verdict extractable; channel still open"?

**P2 — C3 has no outcome for "the calc was never run."** C3's outcomes (a)/(b) both presuppose
the TT-auto rigorous channel *produced a window verdict*. But the date clause stops in-house
calculation at 2026-12-31 *"or upon completion of the two Part-7 time-boxed calcs, whichever is
EARLIER"* — so the date can arrive with the calc unrun, and C3 then has no pre-registered
outcome. The closing paragraph's "including 'still open', stated as such" saves it generically,
but note the tension: the same sentence says the deposit "reports each channel in whichever of
its **pre-registered outcomes** obtains," and *still-open is not one of C3's pre-registered
outcomes*. A deposit-day reader wanting a resolved C3 can cite the specific outcome list against
the general clause. Question: should each channel carry its own explicit still-open line, so the
general clause never has to fight a specific list?

**P3 — C3(a)'s predicate may be unreachable as sealed.** C3(a) requires the window to close "at
every declared family member" — but the A8 demotion (which the sealed file itself invokes:
"A8 discipline applies") established that every number the TT-auto gate emits is
κ-conditional/insertion-contaminated, and the activation-scale frontier that would lift this is
"resolved from outside" — i.e., possibly never. If κ-conditionality persists, (a) cannot fire cleanly — while (b), which ships the surviving window as an ALLOWANCE with the
insertion declared, plausibly can — which combined with P2 makes
C3(a) the outcome most likely to be *forced* into a resolved costume at deposit. Question: as
sealed, can C3's closing branch terminate honestly at all without the external κ resolution?

**P4 — C1(b) may execute a trigger on the wrong channel's answer.** C1(b) says a cut-class
answer to the dispatch fires "the armed tier trigger recorded in the mu_linear ruling…
EXECUTES (no re-litigation)." But the trigger as banked (`mu_linear.boundary_condition`;
X_FLOOR_MAP D1′) has a *specific* predicate: **Π₀ ≠ 0 ESTABLISHED — a spin-0 (trace-correlator)
result** — and the register's own kill-condition list names TRIGGER-LAUNDERING as "firing on
under-determined or conditional-on-commitment returns." The dispatch's question is the **TT
channel's** pole-vs-cut. A TT cut-class answer refutes `rung3_single_pole` as stated (C1(b)'s
first sentence is right) — but whether it satisfies the *mu_linear trigger's own sealed
predicate* is exactly the kind of channel distinction this register polices everywhere else
(the spin-0/spin-2 orthogonality is banked at three separate nodes). Question: does C1(b)
conflate "rung3 refuted" with "the Π₀ trigger predicate met," and if so, does the sealed text
order a trigger-laundering the register itself forbids? (If confirmed: new sealed version
before signing — this one binds a mechanical, no-re-litigation action to possibly the wrong
predicate.) An independent verification pass has since adjudicated on the texts: **confirmed a
real channel conflation** — with the nuance that a *defensible* route to the same tier move
exists (a TT-cut answer plausibly forecloses `mu_linear`'s only remaining graduation route),
but reaching it requires exactly the adjudication step C1(b)'s "no re-litigation" forbids, and
the instrument that would deliver the trigger's literal Π₀ predicate is the *trace-channel
sibling brief* (unsent, resource-gated), not this dispatch. The remedy stands: new sealed
version, with C1(b) binding either to the correct predicate or to an explicit adjudication
step.

## Three further pressure points, found by the independent verification pass (2026-08-10)

**P5 — C1 has no outcome for a determinate answer that is neither pole nor cut.** The one prior
run of this exact question returned exactly that fourth state (`rung3_single_pole.sub_status`:
"earned-under-determined", externally reviewed), and the dispatch's own one-pager names a third
decisive return C1 omits (Rider A's GR-ratio lock — ironically the one return that actually
speaks to P4's Π₀ predicate). C1(c) requires "NO RESPONSE", so an under-determined or partial
reply has no honest home; deposit-day incentive is to force it into (b) or mislabel it (c).

**P6 — the C1 clock can straddle the termination date.** The send date has no deadline and
C1(c) allows six months; if sent after ~2026-07-01 the window crosses 2026-12-31, leaving C1 in
no pre-registered outcome at deposit-writing time — and a pole-class answer arriving *after*
the date but *inside* the window gets two contradictory dispositions (C1(a): "continues PAST
the termination date"; THE DATE: the exception applies only to answers "arriving BEFORE that
date"), with no clause ranking. Corroboration that the P2-class ambiguity is live, not
hypothetical: the companion log already records C3 "in its pre-registered 'still open' state" —
calling still-open pre-registered when it appears in no channel's outcome list.

**P7 — C2(a)'s "kill grade" is a dangling reference.** The sealed preamble promises every
threshold is "ALREADY RECORDED in the register or its frozen instruments, cited by name," but
the rung7 overturning clauses are structural/proof conditions with **no frozen statistical
threshold for an observed crossing** anywhere in the register — so the (a)/(b) boundary would
be graded under deposit-day incentives, the precise failure the preamble claims to exclude.
Same remedy class as P4: pin the reference or freeze the threshold, in a new sealed version.

*(Minor, same pass: C4(a)'s parenthetical gloss of `method_novelty`'s falsifier drops the
"different problem" leg and adds a "confirmed by" leg — a lossy paraphrase in a file that
elsewhere refuses to restate thresholds; and the node graduates "toward" a banked contribution,
weaker than the sealed gloss implies.)*

## What reads as genuinely well-built (so the review doesn't re-litigate it)

The anti-cherry-pick clause (all channels report, every time); C1(c)'s non-response outcome
with the explicit "not evidence for either horn" fence; C4(b)'s no-inflation clause; the
outcomes-first rationale; the signature block making unsigned = not-in-force structural; the
blind-safe seal. The reviewer's time is best spent on P1–P7 and on anything neither pass found.

## Context pointers

- `STAGE_CLOSE_2026-08-09.md` — the stage the condition would terminate; the two owner acts.
- `X_FLOOR_MAP.md` — D1′ (the trigger's predicate, verbatim), D3 (the deposit terminal C3
  feeds), A8 (the κ-conditionality demotion C3 must live with).
- `mu_linear.boundary_condition` in `provenance/claims.json` — the armed trigger's exact text.
- `SIGNATURE_AUDIT.md` — the signature-null background against which C3's "window" language
  should be read.
- `provenance/prereg/README.txt` — the seal discipline and the blind-safe rule the file obeys.

---

## Continuation (2026-08-10): the v3 pre-seal stress record, and why v3 is NOT sealed

The plan was: draft v3, stress it adversarially, seal, deliver. Three stress rounds ran. Each
round's fixes closed the found holes; each next round found new ones — increasingly in the fix
machinery itself. The builder's pre-declared stopping rule ("still blocking → relay the
residuals as open design questions rather than iterate forever") fired after round 3. **The v3
draft exists (`provenance/prereg/PREREG_TERMINATION_V3_2026-08-10.txt`), is stamped
DRAFT — NOT SEALED on its face, and binds nothing.**

### Round 1 (three auditors, on the first draft)
Found and fixed in-draft: an exactly-one violation in C4 (three buckets, most-likely state
landed in all three); the "D1 route" — a planning-map term presented as register vocabulary
(the v2 defect class recurring in miniature, caught by the new citation discipline);
unowned reply classification; silent foreclosure-by-inaction on C2(a)/C3(a); a stop trigger
retirement could never fire; a missing worst-case bucket (a completed data-kill had nowhere
to land); elastic deposit timing with optional, asymmetric consumption; five citation-coverage
gaps (all quotes verified true — format/coverage defects, not misquotes).

### Round 2 (scenario re-stress + fresh hostile read, on the revised draft)
Confirmed the round-1 fixes landed, then found: the C4 refinement overlap (the standing
partial-discharge precedent made one refinement permanently true); the classification rule's
caveat-escape ("conditional in some respect" as a near-universal exit from the kill outcome);
the boilerplate-decline strategy (U6 declines cost nothing and preserve every option); and
more. All fixed in-draft, including the classification-is-adjudication mechanism, U6's
create-or-decline duties, and the C3(e) data-kill bucket.

### Round 3 (final fix-verify + fresh hostile read)
**Still blocking, and the blockers are now in the round-2 fix machinery itself:**
- The C3 reach-partition fix opened a zero-bucket corner (threshold frozen + activation
  unresolved + register-grade below-threshold window → no outcome fires).
- The classification triad has no home for a non-substantive reply ("received, will look"),
  and both readings of "every reply" are exploitable — one flips a channel outcome, the
  other silently disarms stop trigger (iii).
- The classification-adjudication's own register-facing test is exempt from the citation
  check — the exact v2 defect class can recur unchecked inside the one entry that gates the
  stop trigger.
- U3's "before the data are READ" keys blindness to an unverifiable private act (the fix is
  "before the release LANDS" — carried over unnoticed from v2 through every round).
- Plus substantive: C3 has no retirement bucket though the stop sanctions retiring its calc;
  C3(e)'s universal quantifier leaves mixed-member endstates homeless; the decline duty has
  no content bar; the consumption duty is gameable by writing the deposit fast; the
  two-classification-entries rehoming joint is unowned; **and a usability finding: the
  document's operating burden now plausibly exceeds what a single signer can execute
  correctly.**

### The design fork — the owner's ruling, not the builder's

**(A) Fix round four on this architecture.** Every round-3 finding has an auditor-specified
fix. But three rounds of evidence say the fixes are the source of the next round's corners,
and the document is already past the usability line. Choosing (A) means accepting that the
stress loop may not converge.

**(B) Structural simplification — rebuild v3 short, on the primitives that survived all three
rounds unscathed:** still-open first-class everywhere with causes stated; thresholds frozen
before releases land, else the thresholded outcome cannot fire and the foreclosure is stated;
every owner act, omission, and received communication logged with the reply quoted; every
consequence at a node executes only at that node per its own text through recorded
adjudication; consumption symmetric and dutiful; one deposit-timing rule. Channels then list
only their resolved outcomes plus the universal still-open — the per-channel bespoke machinery
(where every round-2/3 defect lived) mostly dissolves into the universal rules. Shorter,
weaker in stated precision, stronger under hostile reading, operable by one signer.

**(C) No signed stop condition.** The stage close already binds nothing; the owner may decide
a stop condition of this complexity is worse than the status quo of two named owner acts plus
judgment, with the register discipline as the honesty instrument.

**The builder's recommendation: (B).** The three-round record is itself the argument: what
survived every hostile read is the small set of universal rules; what kept failing is the
channel-specific machinery. A stopping rule the signer cannot operate fails on deposit day
exactly like a misquote — just later and quieter.

### What stands regardless of the fork
The citation-verification guard (`provenance/test_register_citations.py`, 12 covered quotes,
bite-tested on v2's real defect) is live and green. v1 and v2 remain sealed, unsigned history.
The C1 clock has not started. Nothing about the dispatch is gated on this fork.


---

## Gate record (2026-08-10): the fork executed — v4 sealed as passed

The owner ruled the fork: one short rebuild against a pre-sealed gate, one internal adversarial
pass, then decide — no round five, with outcome (C) as a first-class result if the pass failed.

**The gate** (`PREREG_V4_GATE_2026-08-10.txt`, sealed `09a0da08…` BEFORE drafting): the four
round-3 failure cases must each land in exactly one home; hard size limit (75 lines / 7500
chars); a burden test (a non-drafting hostile reader produces correct deposit lines mechanically
in one read); no new bespoke exception machinery; any failure → (C).

**The document** (`PREREG_TERMINATION_V4_2026-08-10.txt`, sealed `f4bc613c…`): 71 lines, 5,876
characters. Five rules (still-open first-class with plain-word causes; nodes decide; public
events only; quotes decide and log entries assert nothing — a violating entry is void on its
face; one clock). Five channels, each: source node, resolved outcomes, still-open with cause.
Three register quotes (Q1–Q3), the only register text the condition uses, machine-verified both
ways. Reply classification is a pure quote check: a reply resolves a channel only if its own
words assert the class unconditionally — acknowledgments, caveats, conflicts, silence are
still-open with words quoted. No classification-adjudication machinery exists to exploit.

**The pass** (two non-drafting auditors): **PASS, zero blocking findings.** K1 (the zero-bucket
corner) lands in C3(a) alone; K2 ("received, will look") is still-open and cannot touch the stop
trigger; K3 (register assertion in a log entry) is void on its face — nothing to patrol; K4 (a
private-act freeze) is unwritable under R3. Thirteen deposit lines (seven required, six
adversarially invented) produced mechanically in one read. Size within limit. No exception
machinery.

**Non-blocking notes, preserved for the external reviewer's judgment** (per the gate's no-repair
rule, v4 is sealed exactly as passed; these were NOT applied): (i) C3 carries three resolved
outcomes where the gate's template said one-or-two — the auditors adjudicated it load-bearing
(without the retirement outcome, a retired calc front would recreate the zero-bucket class);
(ii) one word each would harden two existential clauses against a rushed signer
("uncontradicted" in C1(a)/(b); "none excluded" in C3(a)) — the compound situations are already
classified by name in the still-open lists, so lines were producible, but the wording invites a
second look; (iii) R5's consume-everything duty and R1's "landed inside the deposit month and
unconsumed" cause form a seam a motivated owner could use on a late-landing adverse release —
the deposit line stays truthful and unambiguous, but the page does not prevent the dodge;
(iv) smaller notes: R5(iii)'s ordering parenthetical covers one ordering explicitly; "decline"
is used in R3 without an on-page definition; C1's classes are defined by reference to the
dispatch one-pager rather than on-page.

**For the external reviewer:** read v4 against the gate and this record. The question is not
"can it be improved" (it can — see the notes) but the gate's own: does every state land in
exactly one home, can one signer execute it under pressure, and is every register assertion
verified or structurally impossible? If your answer requires repairing v4, the sealed decision
rule says that is the (C) outcome, not a v5 — argue it that way.


---

## Signing package (2026-08-10): transcript produced, disclosure prepared, two records

**1. The burden-test transcript is now reproducible, not attested.** The thirteen deposit
lines (seven required, six adversarially invented), verbatim from the workflow record, live in
`provenance/prereg/RESULT_V4_GATE_2026-08-10.txt`, citing the gate's hash — the evidentiary
record of a pass that already happened; v4's sealed text is untouched.

**2. THE PREPARED SIGNING DISCLOSURE** — to be appended by the owner to the companion event
file AT SIGNING, verbatim, alongside the signature record. Descriptive throughout; it
interprets no clause and repairs nothing:

> SIGNING OF v4 (sha256 = f4bc613c5ec38cd7fe780366d710c7b0e0741f50586ff5f75dde73ded9a8fa61).
> The signer records, descriptively and without interpreting any clause, a seam identified by
> external adversarial review AFTER the gate pass and NOT repaired here — the gate's
> no-round-five rule governs, and a repair would be the (C) outcome.
>
> R1 lists "landed inside the deposit month and unconsumed" among the still-open causes. R5
> scopes consumption of external results to "before the deposit." Three descriptive facts
> about their interaction:
>
> (1) SELF-REPORTING. R1 requires the cause stated in plain words, so any use of that clause
> appears on the face of the deposit as "landed, unconsumed." It cannot hide a channel, force
> a resolved reading, or be used silently.
>
> (2) PERMANENCE. In-house calculation has stopped by then under R5, and no clause requires
> the deferred result to be consumed after the deposit is written. A channel reported
> still-open for this cause may remain so.
>
> (3) SILENCE. This document does not address post-deposit consumption of a landed result —
> it neither requires nor forbids it. Whether the register may later consume it is
> undetermined by this condition.
>
> Scope of the gate pass: the gate (PREREG_V4_GATE_2026-08-10.txt, sha256 =
> 09a0da0898e869709e6a39c890463310409bda5be0a87e7b831fc4e144ca5dc6) tested cases K1–K4. This
> seam was not among them. The pass verdict is earned for K1–K4 and says nothing about this
> interaction.

**3a. The scope note, recorded so it cannot be over-read later:** "PASS, zero blocking
findings" is earned for exactly the four sealed cases plus the burden and size conditions.
The R1/R5 consumption seam was never a gate case; the pass says nothing about it. The seam's
three faces are as the disclosure states; the external reviewer's permanence catch (the
document provides no post-deposit path that forces a deferred read) sharpened the in-house
scoring, which had stopped at self-reporting.

**3b. The fourteenth instance, recorded with the pattern it belongs to:** the first draft of
the disclosure entry carried the qualifier "where consumption was feasible" — a feasibility
standard appearing in neither R1 nor R5, which read against a future use of the clause would
have functioned as exactly the gloss on register-adjacent text that v4's R4 voids. A remedy
designed to avoid smuggling an interpretation, smuggling one in its qualifier — the
certifier-inside-the-certified shape, fourteenth appearance in this program, first appearing
inside the remedy for its own class. Caught by the external reviewer; struck before logging.

**What must not happen, restated as the standing rule of this package:** no edits to v4, no
round five, no binding caveat. The document seals as passed or the condition lands on (C);
those are the only two states the gate left available. The remaining acts are the owner's:
sign or decline; send the dispatch (independent of all of this, and still the only artifact
that can settle the physics). One forward note: under v4's R5, the two Part-7 fronts
(the rigorous TT-auto calc and xi_ij) are now stop trigger (ii) — formally part of the stop
condition, not merely queued work.


---

## Signed (2026-08-10)

The owner signed v4. The signing entry — the prepared three-part disclosure verbatim, the
signature, and the in-force declaration — is in the companion event file
(`provenance/prereg/RESULT_TERMINATION_events.txt`), citing v4's hash per its log rule. The
sealed file is byte-unchanged (`f4bc613c…` verified post-signing). **The termination condition
is IN FORCE.** This packet's remaining audience is the deposit-day reader: the gate record, the
burden transcript, and the disclosure above are the context v4's one page deliberately does not
carry.
