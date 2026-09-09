# CANDIDATE MINING PASS 02 — RESULT: **NO CURRENT CANDIDATE QUALIFIES**

> **Status:** complete. **Outcome:** no external-dispatch candidate in the record currently
> qualifies. Nothing sent — **this program has never sent a dispatch to anyone.** Q3 remains
> **OPEN**. Register untouched (74 nodes, sha256 `beaeb84e8a6f8468`). Ledger delta 0. No physics
> run, no observable built, no new primitive, no status changed.
>
> **Date:** 2026-09-09.

---

## 0. FOR A READER WITHOUT CONTEXT

This program (GRUT) is trying to select **one narrow technical question it could send to an outside
specialist** — something it has never actually done. The selection is governed by rules the owner
ruled on, and the pass below applies them to the whole record and returns **nothing that qualifies.**

Two governing rules matter most, and both were derived from prior failures in this same effort:

**The weak reading (governing).** A valid candidate must have an **explicit, recoverable,
pre-committed two-way state map** — *if the answer is YES, this specific thing changes; if NO, this
other specific thing changes* — written down **before** the question is asked. The map may be a
governance stipulation already in the record; **it does not have to be derived.** A negative answer
need not damage the framework: it may close a branch, eliminate an assumption, redirect the program,
or establish a competing interpretation.

**The external-source fidelity gate (new, added after the failure in §4).** A candidate that depends
on an outside paper **may not manufacture its scientific fork by laying this program's own
terminology over a source that poses a different question.**

---

## 1. THE FOUR-AXIS SEPARATION — the deliverable of this pass

Candidates are adjudicated on four axes that **may never substitute for one another**:

| Axis | Asks |
|---|---|
| **Formal map validity** | Is there an explicit, recoverable, pre-committed two-way map? |
| **Source fidelity** | Is the fork the question the source actually poses, or our vocabulary laid over it? |
| **Scientific question validity** | Is it a real, live, well-posed question worth answering? |
| **Dispatchability** | Could it actually be sent, self-contained and framework-neutral? |

**This separation is not bookkeeping — it is what produced the result.** The two strongest
candidates this effort has produced failed on *different* axes, and each would have shipped had the
axes been collapsed:

- **The SLOT test** (retired, §4) — **passed** formal map validity, **failed** source fidelity.
- **u5/u6 KNOB 1** (§3) — **passed both of those**, and failed the two the SLOT round never reached.

---

## 2. METHOD

Three independent mining sweeps over five sources (register nodes with two-answer maps; the freeze's
reopening conditions; the *strengthened-by* / *weakened-or-falsified-by* lists; open Q3 branches;
other registered questions), then a **provenance/state-transition verifier** and a **hostile
candidate refuter** run *concurrently* against the pooled result, then a **referee** adjudicating
conflicts on all four axes. Six agents. The verifier and refuter reached opposite verdicts on the
one survivor; the referee resolved against it, on the record.

---

## 3. THE ONE SURVIVOR, AND WHY IT FAILED

**Candidate: u5/u6 KNOB 1.** At the passive, KMS-equilibrium, relativistically covariantized fixed
point: is the reversible mode-coupling (Poisson-bracket) structure **RG-relevant** — the classes
separated by a nonzero fixed-point anomalous dimension (**SHARP**) — or continuously **DEFORMABLE**
into one another?

| Axis | Verdict |
|---|---|
| Formal map validity | **PASS** |
| Source fidelity | **PASS** — limb 5 only, with a binding restriction |
| Scientific question validity | **FAIL** |
| Dispatchability | **FAIL** |

**The map is genuine and was found, not supplied.** `provenance/claims.json`, node
`u6_constitutive_order`, `boundary_condition`, banked 2026-07-04 — **two months before any dispatch
selection existed**:

> *"ONE computation settles BOTH: SHARP => u6's order parameter is real AND u5 counts a genuine
> phase structure (a family); DEFORMABLE => the order parameter collapses AND u5 is rigid (one
> class)."*

Both nodes are live (`tier: to-derive`, `depends_on: []`), and **both outcomes are pre-registered as
first-class** — the negative is explicitly *"still useful, not a new theorem"*, not a failure.

**It is genuinely unrun.** The only executed artifact scopes itself away: *"Scope: **TOY/SCALING** —
symmetry + naive scaling, **not** the rigorous fixed-point RG"*, *"this toy does not resolve it"*,
*"horn UNDECIDED"*.

**It dies because the object the map is keyed on is not specified.** The bracket `{φ, C}` whose
RG-relevance *is* the question is undefined until the slow-variable / coarse-graining set is chosen —
and the record says that choice is undischarged. `calc/RESULTS_u5u6_deformability.md:39`: a fenced
input *"distinct from u6's already-held coarse-graining/slow-variable conditional … which remains
**live and un-discharged**"*; the register's guard *"PASSES — but only GIVEN the slow-variable /
coarse-graining identification (a CONDITIONAL pass, not absolute)"*.

The referee searched independently: **no document declares a slow-variable set for this sector.** The
nearest authoritative typing is `PHYSICS_LEDGER/WALL_KR_U3_EFT_BASELINE_RESULT.json` —
*"the choice of slow variables is exactly the Mori-Zwanzig 'which P' question, unanswered here."*

Both scorecards had mis-billed that input to a downstream knob. It belongs to **this** question's own
object.

---

## 4. WHY THE PREVIOUS CANDIDATE WAS RETIRED (context for the new gate)

The prior selection was the **SLOT test** — a question about §4.3 of CLPW, *An Algebra of Observables
for de Sitter Space* (arXiv:2206.10780v5). It passed the formal governance test. A **primary-source
read** then failed it, and it is retired. The source findings are preserved as reusable evidence in
`program/DISPATCH_CANDIDATE_01.md` §8:

- *"Without a second observer, the question is more difficult and appears not to have a simple limit
  for G_N → 0"* — so asking whether the limit *"goes through rigorously"* presupposed a claim the
  paper does not make.
- `d` is defined on **(0, ∞]** — *"any positive real number or ∞"* — so `d = 0` is **outside** the
  Murray–von Neumann classification, which is why §4.3 calls it problematic.
- `d ~ G_N^{1/2}` is explicitly conditional: *"**If this is the correct answer**, then…"*.
- The observer/clock is an explicit added Hilbert-space factor entering the constraint, *"since 𝒜^H
  is trivial, the only way to get anything sensible."* The clock language is the paper's own.

**The deciding finding:** CLPW poses **no input-counting question at all**, and the fork's answer was
already visible in §2.4 without §4.3. *"Relative temporal datum alone"* is this program's phrase, not
the paper's. **The corpus's reading of the material failed, not the material.**

---

## 5. THE STRUCTURAL FINDING — **CORRECTED 2026-09-09. THE GENERALIZATION IS WITHDRAWN.**

> ### ⛔ THREE DEFECTS IN THIS SECTION, CORRECTED SURGICALLY. The candidate adjudications in §3 and
> ### §6 are UNAFFECTED and stand.
>
> **DEFECT 1 — COUNT.** The text below said *"the same kill, four times over"* and *"Four different
> candidates, one shape"* over a table with **FIVE** rows. The original wording is left visible.
> **The count was wrong**, and the corrected analysis does **not** rely on the "four times"
> generalization. Note which row the miscount omitted: the fifth is **u5/u6 KNOB 1**, the only row
> naming the **slow-variable / coarse-graining choice** — i.e. the row the generalization was drawn
> from is the row the headline count dropped.
>
> *(An earlier wording of this callout called that "the projection decision". **Corrected**: the row
> names the slow-variable choice, and §9.2 is precisely the finding that "choose P" is
> **under-determined by** "choose the slow variables". §9.4 bars collapsing A and C absent proven
> equivalence — so the earlier wording performed the very collapse this correction forbids. Caught in
> audit, not in self-review.)*
>
> **DEFECT 2 — THE Π₀ ROW'S PREMISE IS SUPERSEDED.** The row rests on
> `GRUT_PROGRAM_FREEZE.md:49-51` (commit `7399765`, 2026-09-06 **14:39**): *"the specific partition
> used by the contract was never declared in D1–D5."* A later document the **same afternoon**,
> `GRUT_MODEL_FRAMEWORK.md:37` (commit `cc6c147`, 2026-09-06 **14:45**), states: *"the contract's
> operative partition (external-leg vs internal-line) was historically **undeclared** — **now
> declared here**."* The later record **declares** what the earlier one calls undeclared. **Whether
> Π₀'s rejection survives this correction is NOT settled here** — the corpus is not made to
> reconcile itself by interpretation, and no reconciliation is chosen.
>
> **DEFECT 3 — THE GENERALIZATION IS WITHDRAWN.** *"One shape"* was tested as a formal hypothesis
> and **FAILED** — §9.

The mining sweep flagged it and the referee confirmed it is the **same kill, four times over**
*(count wrong — see above; five rows)*:

> ### The object the map is keyed on is defined against something the record explicitly never declared.

| Candidate | The undeclared thing |
|---|---|
| Π₀ | a system/bath partition — the freeze itself says *"the specific partition used by the contract was never declared in D1–D5"* (`GRUT_PROGRAM_FREEZE.md:49-51`) |
| χ_∞ | a renormalization condition nobody has stated |
| *lifted vs protected* | a decision criterion that is itself an undone Q2-BRIDGE deliverable |
| pole-vs-cut | an ω conjugate to cosmic time the target corpus does not define |
| **u5/u6 KNOB 1** | **the slow-variable / coarse-graining choice** |

**~~Four different candidates, one shape.~~ WITHDRAWN** — the count was wrong (five rows), and the
generalization was subsequently tested and failed (§9). What survives is only the per-candidate
observation that each named object depends on some unresolved construction choice. **That the
choices are the SAME choice is refuted.**

---

## 6. CORRECTIONS TO THE PRIOR PASS, VERIFIED

- **Two of nine claimed two-way maps are not maps.** `rung7_w2_wa_sign` adjudicates its own tension
  in-node (*"THE SECOND LAW FIXES THE SIDE, NOT THE SLOPE … both fully passive"*) and its NO branch is
  written nowhere; `vc_w_equals_minus_one` carries a map **the register itself marks defective**.
- **Two more are already answered** (`eft_operator_basis`; `response_lorentz_covariance`, discharged
  2026-08-30).
- **RESIDUE** (freeze key #2) is **one-sided, confirmed at all three sites** — its two limbs are two
  different deliverables, not two answers to one question.
- **O2 (freeze key #1) stays rejected, but two stated grounds are STRUCK as wrong**: it is *not*
  "merely continue investigating" (both branches are terminal), and its negative branch *does* carry
  a state change — `GRUT_PROGRAM_FREEZE.md:125` reads *"Any ONE of the following justifies
  unfreezing."* It has the **strongest map in the corpus** — the only entry appearing on both the
  strengthened and weakened lists — and fails on other grounds, now recorded correctly.

---

## 7. WHAT THIS RESULT IS AND IS NOT

**Is:** no candidate currently in the record can be dispatched, and the blocker is object-level
specification rather than any of the things previously blamed.

**Is not:** a finding that the framework is unfalsifiable; a claim that no candidate could exist; an
argument from the register's `derived`-tier count (a story about that count was advanced earlier in
this effort, **refuted, and withdrawn**); or an interpretation of the K_R campaign's zero out-degree
as scientific failure (separately classified **scientifically justified**).

**No candidate was rejected on size or cost** — a void ground. **No rejection used the withdrawn
"the adjudication rule must be derived" standard** — also void. Both were checked by all auditors.

**23 rejections** are recorded with their axis and exact reason, available for re-examination.

---

## 8. STANDING LESSON — **REVISED 2026-09-09**

The prior wording — *"the object the map is keyed on is defined against something the record
explicitly never declared"* — was useful and **overgeneralized**. Replaced by the narrower audited
lesson:

> **Object specification is itself FACTORED.** Several candidate objects depend on unresolved
> construction choices, and the record must not collapse distinct choices — slow-variable selection,
> system/bath partition, the projection P, inner-product choice, the state supplying it, cutoff
> choice, gauge/field-redefinition freedom — into one "effective description" decision **unless the
> record establishes their equivalence.**
>
> **The attempted common-blocker hypothesis H was tested and FAILED (§9).**

And the prior lesson, which stands unchanged: a two-way governance map is **necessary but not
sufficient**; the thing dispatched must also be the scientific question the source actually poses.

The selection machinery has now twice prevented an external investigation from being spent on a
question that would not have survived contact: once on source fidelity, once on object
specification. Both catches came from adversarial passes, neither from self-review.


---

## 9. HYPOTHESIS H — TESTED AND **FAILED** (added 2026-09-09)

**H, as formulated:** *multiple currently blocked candidate objects are undefined because the choice
of retained/slow variables — the Mori-Zwanzig "which P" decision — has not been declared.*

### 9.1 Verdict: **FAIL**

**The referee's co-determination criterion.** X is *the same decision* as choosing P **iff**, holding
every other declared input fixed: **(i)** declaring P fixes X with no residual freedom, **and**
**(ii)** declaring X fixes P with no residual freedom. If either direction leaves residual freedom,
X is merely **RELATED** — and a candidate blocked on X does not support H.

**Zero of the tested candidates satisfy it.** u5/u6 KNOB 1 comes closest and fails **sufficiency**:
its bracket `{φ, C}` requires a **second, non-P declaration** — the fenced conserved-charge input —
which is a different decision.

### 9.2 The finding that is prior to any candidate: **H's subject is not one decision**

*"Choose P"* is under-determined by *"choose the slow variables."* `calc/mz_inheritance.py:31-34`
records that *"the Mori-Zwanzig kernel does not currently denote a unique object, and the two objects
it could denote answer this question **OPPOSITELY**"* — the same retained variable admits the
**Kubo-Mori** and the **symmetrised** inner products. The second half is booked as missing:
*"the state supplying the inner product (unpriced anywhere)."*

**So there was never one undeclared decision for multiple candidates to share.**

### 9.3 What this does **NOT** establish

**It does NOT prove the five obstructions are independent.** It establishes only that **P is not
their demonstrated common decision.** No claim is made here about which construction choices are
ultimately independent and which are related by a proven equivalence — that is an open question and
this document does not answer it.

### 9.4 The seven choices, to be kept SEPARATE until equivalence is proven

**A** slow-variable selection · **B** system/bath partition · **C** the Mori-Zwanzig projection P ·
**D** inner-product choice · **E** the state supplying the inner product · **F** cutoff/separation
scale · **G** gauge/field-redefinition freedom.

**No pair may be collapsed unless an authoritative source establishes equivalence.** The record
explicitly declines to adjudicate at least one such pair: on partition-vs-P it carries two competing
orderings (Zurek: split → coarse-graining; Mori-Zwanzig: choosing P *is* the partition) and states,
at `PHYSICS_LEDGER/WALL_KR_U3_SPECIFICATION.md:78-79`: **"None is selected. This is the sharpest
single result of the audit."**

### 9.5 P remains OPEN — but is not a master key

The projection choice is still a legitimate unresolved ingredient, recorded as **ASSUMED**: *"the
choice of slow variables is exactly the Mori-Zwanzig 'which P' question, unanswered here"*
(`PHYSICS_LEDGER/WALL_KR_U3_EFT_BASELINE_RESULT.json:26`). It is
now represented **alongside** the other choices rather than elevated above them.

**P also cannot be declared from authorized structure.** The split is booked as a **priced input**,
not a convention — *"STANCE, not derivation"* (`provenance/claims.baseline.json`, `rung1`
`ledger_note`) — and declaring it as one would run the freeze's own rule backwards:
*"a supplied structure may never be re-reported as a derived one"* (`GRUT_PROGRAM_FREEZE.md:23`).

---

## 10. NEW UPSTREAM DEFECT — **OPEN RECONCILIATION ISSUE**, not adjudicated here

Two same-day descriptions of what the program's split **is**, and the corpus does not reconcile them:

| Record | Says |
|---|---|
| `WALL_KR_U3_SCALE_SPLIT_CORRECTION.md:73-75` | *"an EFT program whose split is a **cutoff choice**"* — **unretracted** |
| `WALL_KR_U3_EFT_BASELINE.md:28` | *"there is **no cutoff parameter** whose placement could be varied"* — and at **`:24`** the split is ruled **"NOT B (Wilsonian momentum-shell)"** |

**Are they answering the same question?** Not established. The record logs the debt itself, with the
consequence spelled out: *"If these pose **different questions** rather than describe one twice,
status F becomes correct and D is an artifact of treating a contradiction as a typo."*

**This is NOT reconciled by interpretation here**, and neither statement is declared wrong. It is
recorded as an **open reconciliation issue**, upstream of everything this pass touched, and it bears
on a status grade. **It is the owner's to rule on.**

---

## 11. CORRECTION PROVENANCE

Corrections applied 2026-09-09 after the projection-operator precondition test. **Surgical:** the
count defect, the Π₀ provenance defect, and the withdrawn generalization are marked in place with
the original wording left visible. **No earlier commit was altered.** The candidate adjudications
(§3, §6) and the four-axis result (§1) are **unchanged** and were not rewritten to compensate.
**No new scientific claim is introduced by this correction**, no ledger or register status changed,
nothing sent, no computation run.
