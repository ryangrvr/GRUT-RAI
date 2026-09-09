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

## 5. THE STRUCTURAL FINDING — more informative than the selection

The mining sweep flagged it and the referee confirmed it is the **same kill, four times over**:

> ### The object the map is keyed on is defined against something the record explicitly never declared.

| Candidate | The undeclared thing |
|---|---|
| Π₀ | a system/bath partition — the freeze itself says *"the specific partition used by the contract was never declared in D1–D5"* (`GRUT_PROGRAM_FREEZE.md:49-51`) |
| χ_∞ | a renormalization condition nobody has stated |
| *lifted vs protected* | a decision criterion that is itself an undone Q2-BRIDGE deliverable |
| pole-vs-cut | an ω conjugate to cosmic time the target corpus does not define |
| **u5/u6 KNOB 1** | **the slow-variable / coarse-graining choice** |

**Four different candidates, one shape.** This is a different diagnosis from any reached earlier in
this effort. Not missing maps, not missing adjudication rules, not cost, not frontier difficulty:
**the program's questions are well-mapped and under-specified at the object level.** Every dispatch
attempt has now died there.

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

## 8. STANDING LESSON

> A two-way governance map is **necessary but not sufficient**. The thing dispatched must also be the
> scientific question the source actually poses — **and its object must be specified.**

The selection machinery has now twice prevented an external investigation from being spent on a
question that would not have survived contact: once on source fidelity, once on object
specification. Both catches came from adversarial passes, neither from self-review.
