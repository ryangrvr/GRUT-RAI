# U3 SCALE-SPLIT LEGITIMACY / EFT BASELINE AUDIT

**Date:** 2026-09-03 · **Instrument:** `wall_kr_u3_eft_baseline_audit.py` ·
**Artifact:** `WALL_KR_U3_EFT_BASELINE_RESULT.json` · **Battery: 30/30, zero failures.**
**Read-only** (register sha256 identical pre/post; worktree unchanged). **No physics. No A-F
selection. U3 not solved. Nothing banked.** W-0.

Evidence is labelled **GRUT-INTERNAL FACT / SOURCE-DERIVED FACT / MODEL INFERENCE / OPEN**.
The prior AQFT comparison is **not** reused as evidence here.

## U3-STATUS: **A — MOSTLY STANDARD EFT QUESTION**

---

## PART 1 — WHAT GRUT ACTUALLY DOES **[GRUT-INTERNAL FACT]**

The contract's "fast modes" language describes *what the bath is*. It does **not** specify a
cutoff — and the implementation contains none:

- **No momentum shell, no band, no fast-mode cutoff** anywhere in the ledger.
- Regularization is *"dimensional continuation ONLY; NO explicit IR scale."*
- The operation performed is a **one-loop self-energy**, not a Wilsonian RG step.

**Category: NOT B (Wilsonian momentum-shell).** The implemented split is the **external-leg vs
internal-line partition** of a one-loop influence-functional calculation — closest to **E/H**: a
*diagrammatic* partition described in scale/mode language.

**The consequence that matters: there is no cutoff parameter whose placement could be varied.**
The loop integrates **all** internal momenta, soft ones included.

That also explains something already on the record. **The O(H²) IR divergence — the whole
origin of fork-(ii) — is what happens when there is no actual scale split.** A genuine fast/slow
cutoff would have regulated the IR by construction. The blocker exists *because* GRUT's split
is not a Wilsonian scale split.

## PART 2 — WILSONIAN BASELINE, AND YOUR CORRECTION ADOPTED **[SOURCE-DERIVED]**

"Placement is immaterial" was too strong, and I withdraw it. The five freedoms are **not**
interchangeable:

| freedom | status |
|---|---|
| **cutoff-choice** | observables independent of the *value* — **provided** RG running/matching is consistent |
| **projection-choice** | **NOT generally free.** A different projection is a *different effective theory*, not a rescheme |
| **field-redefinition** | on-shell observables invariant; off-shell Green's functions **not** |
| **physical scale hierarchy** | a **fact** about the system — an input, never an output |
| **universality of observables** | low-energy observables depend on the UV through finitely many couplings |

Decoupling and universality hold for a **controlled construction with consistent matching**.
They do not make an arbitrary projection interchangeable.

## PART 3 — THE RESIDUE

| candidate residue | classification |
|---|---|
| why this scale hierarchy exists | **OUTSIDE WILSONIAN SCOPE** — an input |
| why these are the natural effective variables | **ASSUMED** — the Mori-Zwanzig "which P" question |
| why TT modes are the correct probe | **ASSUMED** — `p_tt_ansatz`, tier `assumed`, *"the projector P^TT chosen (not derived)"* |
| why the bath is approximately Gaussian | **ASSUMED** — one loop *is* the Gaussian truncation |
| why retarded response is valid | **ALREADY EXPLAINED** — causality + SK structure |
| why memory/nonlocal response emerges | **ALREADY EXPLAINED** — integrating out *massless* modes generically gives nonanalytic, nonlocal terms |

## PART 4 — THREE FORMULATIONS, NONE SELECTED

- **U3-A** (controlled description): well-posed, **not novel** — textbook EFT validity.
- **U3-B** (dynamically privileged): well-posed, **genuinely open** — but it is the known
  scale/variable-selection problem, not GRUT-specific.
- **U3-C** (invariance under admissible splits): well-posed *in principle*, but **not currently
  testable against GRUT** — the construction has no split parameter to vary.

## PART 5 — NOVELTY: **A, with a C component**

Applied to GRUT's *actual* split, U3 is largely **standard EFT/open-system bookkeeping**. The
residue is the **known** scale/variable-selection problem.

Nothing needs withdrawing: `u3`'s own `differentiator` field already says
**NON-DIFFERENTIATING**.

## PART 6 — THE FOUR CONDITIONS TO U4

Weak coupling · Gaussianity · near-equilibrium · timescale separation — **all four are standard
open-system/EFT assumptions. None is GRUT-specific.** In GRUT the fourth is the ε_H domain
condition, made unusually explicit.

So the four conditions do not by themselves make U4 a new layer. What would is whether
constitutive structure is **forced** rather than assumed — exactly what `u4` is fenced against
pre-answering.

## PART 7 — THE MEMORY RESIDUE, AND THE UNCOMFORTABLE PART

**[SOURCE-DERIVED]** A nonlocal/retarded kernel follows essentially automatically from
integrating out **gapless** modes: massless intermediate states put a branch cut on the real
axis, so the effective action is not a local derivative expansion.

**[GRUT-INTERNAL]** The campaign's own Tier-4 result is exactly that — a branch point at ω = 0
with a real-axis cut, gapless two-graviton continuum. The **expected** structure, obtained
rigorously.

**[MODEL INFERENCE]** So "memory" *per se* is not the distinctive claim. GRUT's distinctive
claim was **finite memory / single-pole** structure — and the campaign's own benchmark found
**s = 5 with no pole**, contradicting it.

**What would be distinctive:** a derivation that the *specific* kernel is **forced** rather than
one of many admissible ones. That is `u2`/`u4` territory, not `u3`.

## PART 8 — ANSWERS

1. **GRUT's actual split:** a diagrammatic external/internal partition of a one-loop
   influence-functional calculation, dimensionally regularized, with **no cutoff parameter**.
2. **What Wilsonian theory already explains:** the retarded form, and the nonlocal/memory
   structure as the generic consequence of gapless intermediate states.
3. **What it does not:** why this hierarchy; why these variables; why TT; why Gaussian.
4. **Strongest remaining formulation:** U3-B.
5. **Is it novel?** No — it is the known scale/variable-selection problem.
6. **What would count as solving it:** the deletion test from `f5a9e69` — remove every
   partition-valued object from the inputs; if the derivation still runs, it is a candidate.
7. **Worth pursuing?** *Assessment, not a decision:* **not as "the deepest frontier."** U3 is a
   graph isolate, largely standard, and its most testable form is not posable against the
   current construction. The genuinely distinctive question has moved to `u2`/`u4` — whether the
   specific kernel is forced.

## W-0 STATUS — U3 scale/mode legitimacy audited against the Wilsonian/EFT baseline; no physics executed; A-F unchanged; nothing banked.
