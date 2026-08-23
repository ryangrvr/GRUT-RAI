# The reality audit — charter

> **Written by Claude (checker) for Ox (builder), 2026-08-23, at the owner's direction.**
> Nothing in this audit banks. `claims.json` is not edited by it. Findings go to the owner as
> proposals; the bank gate and CHARTER §1.3/§5.3 relay apply as always.

## 0. What this is, and what it is NOT

Every audit this program has run has been a **provenance audit**: is the claim tiered, sourced,
falsifiable, priced, non-laundered. `validate.py` does that continuously and it is GREEN.

**This is not that.** `provenance/auditor.py`'s own docstring says it "verifies DISCIPLINE, not
TRUTH -- a wrong-but-well-provenanced claim passes." This audit asks the other question:

> **Is the claim true about the world, and would it survive a competent physicist reading it cold?**

**DO NOT RE-RUN PROVENANCE CHECKS.** They are green, they will stay green, and re-running them
produces the appearance of work. If your finding is "this node lacks a falsifier," you are in the
wrong audit.

## 1. Scope — everything, not just the register

1. All **71 register nodes** in `provenance/claims.json`.
2. Every **`calc/RESULTS_*.md`** finding, including quarantined and retracted ones (a retraction can
   itself be wrong).
3. The **standing documents'** physics claims: `GRUT_ToE.md`, `NO_GO_LEDGER.md`,
   `GRUT_I/II_What_Survived.md`, `EMERGENCE_CHAIN.md`, `SIGNATURE_AUDIT.md`, `ARROW_OF_TIME.md`.
4. The **method claims**: `method_novelty`, and `../claimledger` including the Nowak q-bio.PE cold
   run that this register does not book.

## 2. The four questions, per item

**Q1. What would have to be TRUE OF THE WORLD for this to hold?** State it as a physical condition,
not as a citation. If you cannot state it, that is the finding.

**Q2. What is the evidence it IS true?** Classify the item as exactly one of:
- **BORROWED** -- established physics taken from a source. Then **open the source and check it says
  what we say it says.** This program has a live precedent: the 2107.13905 "square of the number of
  e-foldings" inference was retired after source verification killed the premise twice.
- **DERIVED** -- we computed it. Then **re-run the computation** and say whether it reproduces.
- **ASSERTED** -- neither. Then say so plainly; an honest ASSERTED is a good outcome for this audit.

**Q3. THE LOAD-BEARING TEST -- and this program has never asked it.** *If this item were deleted
outright, what else falls?* Trace it forward through `depends_on`, through `attaches_to`, AND through
prose citation (the register carries ~0.78x as much node-to-node structure in prose as in edges, so
the graph alone will understate this). Report the blast radius.

**Q4. Does the claim's STRENGTH match its evidence?** The failure mode is a claim true at a narrower
scope than stated. Precedent from this session: rung4's "22-62 orders below detectability" is
CORRECT as a dephasing statement and does not cover the amplitude channel at all.

## 3. The verdict vocabulary — three buckets, and use them at earned strength

- **HOLDS** -- survives a cold outside reading at the strength stated.
- **HOLDS-NARROWER** -- true, but at a smaller scope than the text claims. **Say the true scope.**
  Expect this to be the most common non-trivial verdict; it is the shape of nearly every real defect
  this program has found in itself.
- **DOES NOT HOLD** -- the claim outruns its evidence. Say what evidence would be needed.

Plus, orthogonally: **SOURCE-MISMATCH** (borrowed, and the source does not support it) and
**UNREPRODUCED** (derived, and it did not re-run).

## 4. The fence that makes this audit honest

**"Everything holds" is a legitimate and fully expected outcome. Pre-register it now.**

An audit graded on how much it finds will manufacture findings, and this program's own record says
the pressure is real: two of five pre-registered compound/omission candidates were mislocated, one at
medium-high confidence. **The honest prior here is GOOD.** In the 2026-08-22 session, eight defects
were found and **zero were physics errors** -- the mode functions, kernels and derivations held every
time. What failed was checking and reporting, and both are now instrumented.

So: if a node holds, write HOLDS and move on. Do not decorate it with concerns.

## 5. Start here — items already known to be fragile

Not a prediction of failure; these have surfaced and deserve first pass.

| item | why |
|---|---|
| `rung3_single_pole` | the class-A pair is adverse to its super-Ohmic premise; the free theory supplies a FAMILY indexed by multipole where the node asserts THE memory time |
| `rung1_inin_action` | "responsive medium with **finite memory**" at tier `shown`, Δ4 -- four of the seven Class-C outcomes contradict it |
| `rung4_love_kk` | 22-62 orders is correct for dephasing, uncovered for the amplitude channel |
| `rung7_wz` | statement says the τ₂ mode is "booked in this claim's +2"; `ledger_delta` is 3 |
| `p_tt_ansatz` | rung3's own text calls the TT-only choice CHOSEN, not forced |
| `method_novelty` | prior-art screen never ran against formal methods (Lean/`#print axioms`, Metamath, reverse mathematics, Carcassi & Aidala) |
| ω_c wherever it appears | three in-corpus values spanning 39.6 orders, and the crossover goes as √ω_c |
| the `claimledger` Nowak run | the stronger of two cold-corpus runs, booked nowhere |

## 6. Anti-patterns — refuse these

1. **Provenance drift.** If the finding is about tiering or sourcing hygiene, it belongs to
   `validate.py`, not here.
2. **Manufactured findings.** See §4.
3. **Grading the register against itself.** A node is not validated by another node citing it.
4. **Self-certification creep.** See §7.
5. **Re-litigating settled retractions** unless you have a specific mathematical objection. The
   retraction of the quasinormal reading, the w_a sign, the 689 Hz falsifier, the ζ-hypothesis, the
   information principle -- all stand unless you can break one.
6. **Reaching for FORBIDDEN.** This rebuild banks zero entries at that strength and reporting that
   absence honestly is part of the discipline.

## 7. What this audit CANNOT do — state it in the output

It **cannot discharge the external-validation debt.** `method_novelty`'s own rule is that a claim
cannot be banked on self-verification, and `claims.json` records that **no outside human has ever
been contacted by this program.** An audit of the program by the program is the exact
conflict-of-interest the method exists to flag. It will find real things; it cannot certify the
result. Write that sentence into the output rather than leaving it implied.

## 8. Output

One file, `REALITY_AUDIT_RESULT.md`. Structure:

1. **The table** -- one row per item: id · classification (borrowed/derived/asserted) · verdict
   (holds / holds-narrower / does-not-hold / source-mismatch / unreproduced) · blast radius from Q3 ·
   one-line reason.
2. **What actually broke** -- only the non-HOLDS, ranked by blast radius. This is the section the
   owner reads first.
3. **The load-bearing map** -- the items with the largest blast radius, whether or not they hold.
   *This is the audit's most valuable output and it has never been produced.* If one node carries
   twenty others, that is worth knowing even when it holds.
4. **Source-verification log** -- every borrowed claim whose source you actually opened, and whether
   it said what we say it said.
5. **Reproduction log** -- every derived claim you re-ran, with the residual.
6. **The limits paragraph** from §7, verbatim in spirit.

**No net figures typed** (`PUBLIC_NUMBERS` rule); nets ride `validate.py` / `emit_public_numbers.py`.
Gate counts come from `emit_gate_status.py`, not from memory.

## 9. Sequencing note for the owner

This audit inventories a register that has four adjudications pending -- ω_c, `rung7_wz` +2/+3, the
`rung1` finite-memory clause, and the 6-vs-7 outcome enumeration -- plus the unbanked class-A
results. **Ruling on class A first is worth considering**, or the audit describes a register that
changes underneath it.
