# U3 / AQFT RECONCILIATION — **AUDIT & SPECIFICATION ONLY**

**Date:** 2026-09-02 · **Instrument:** `wall_kr_u3_aqft_reconciliation.py` ·
**Artifact:** `WALL_KR_U3_AQFT_RECONCILIATION_RESULT.json` · **Battery: 27/27, zero failures.**
**Read-only** (register sha256 identical pre/post; worktree unchanged). **No physics. No A-F
selection. No U0 created. U3 not solved. Nothing banked.** W-0.

## EVIDENCE PROVENANCE — READ THIS FIRST

The dispatched independent hostile comparison **returned empty** (two results, both null).
Every external-literature statement below is **the auditor's own knowledge, labelled
INFERENCE-FROM-KNOWLEDGE, not independently verified in this run**, and should be checked
externally before being relied upon. This is recorded rather than glossed.

## VERDICT: **REFINEMENT, NOT DISSOLUTION**

## A WITHDRAWAL FIRST

The prior audit (`6675d1c`) flagged that U3 "may be **ill-posed** in relativistic QFT."
**That was too strong and is withdrawn.** It conflated *"the naive factorization is not
fundamental"* with *"the question is confused."* Those are different claims, and only the
first is supported.

## PART 1 — THE TWO STATEMENTS, HELD APART

They are not the same statement, and collapsing them is what produced the error above.

| | |
|---|---|
| **S1** | local QFT algebras generally do not admit the naive tensor factorization of finite-dimensional QM |
| **S2** | the split property can provide a tensor-product structure for suitably separated regions |

**AQFT structure** *(inference-from-knowledge)*:

- **Primitive:** a net of local von Neumann algebras `A(O)` over regions, a state, and the
  causal/inclusion structure of regions.
- **Why S1:** in a vacuum representation the algebra of a bounded region is typically a
  **type III₁ factor**. Type III factors carry no trace and no density matrices, so `H` does
  **not** split as `H_O ⊗ H_O′` with `A(O)` acting on one factor.
- **What the split property supplies:** for a **strict** inclusion `O₁ ⊂⊂ O₂` (a spacelike
  collar), an **intermediate type I factor** `N` with `A(O₁) ⊂ N ⊂ A(O₂)`. A type I factor
  **does** carry a tensor-product structure.
- **Assumptions required:** strict spacelike separation plus nuclearity/energy conditions. The
  split property is a **hypothesis satisfied by good theories**, not an automatic feature.
- **The decisive residue:** the intermediate type I factor is **not unique**. The factorization
  it supplies depends on the choice of `N` and the collar — so subsystem structure is
  **available-under-conditions, not canonical**.

That last point is the one that matters, and it is exactly your correction.

## PART 2 — THE THREE INTERPRETATIONS

| | status |
|---|---|
| **A** — fundamental Hilbert factorization `H = H_S ⊗ H_B` | **NOT SUPPORTED as fundamental** — displaced, not merely unproven |
| **B** — algebraic subsystem structure `A_S, A_B ⊂ A` | **MEANINGFUL; the natural formulation** — where the question should be posed |
| **C** — emergent/operational subsystem structure | **MEANINGFUL and PARTIALLY ANSWERED** — sufficient conditions supplied; necessity not shown |

**No interpretation is rendered ill-posed.**

## PART 3/4 — WHY THIS IS REFINEMENT

A genuine dissolution would require showing that "why split?" is a **category mistake**. AQFT
shows no such thing. It **displaces one candidate definition** (A) while **supplying a rigorous
replacement** (B) and **explicit sufficient conditions** (C). That is refinement.

**The refined question:**

> Under what conditions on the primitive structure — algebra, causal/inclusion relations,
> state, scale — does a subsystem/bath structure become **available**, and is any such
> structure **canonical** or one of many admissible choices?

Canonicity is now explicit, because the split property forces it. Seven candidate primitives
are listed — causal structure, local algebras, the split property, state dependence, modular
structure, scale/coarse-graining, operational accessibility — and **none is selected**.

## PART 5 — TRIANGULATION

| framework | primitive | partition | reduction | what it leaves unexplained |
|---|---|---|---|---|
| Zurek / decoherence | `H_S ⊗ H_B` + interaction | **ASSUMED** | partial trace | why the factorization exists |
| Mori-Zwanzig | a projector `P` | **CHOSEN** (`P` *is* the partition) | generalized Langevin | what selects `P` |
| **AQFT** | net of algebras + state + causality | **NOT primitive**; available under split | restriction to a subalgebra | why nuclearity/split holds; which `N` |
| Effective field theory | field content + a scale | **BY SCALE** | integrate out heavy modes | what selects the scale |
| Wilsonian coarse-graining | cutoff + blocking rule | the blocking rule *is* the partition | RG flow | what selects the blocking rule |

**Every framework leaves something unexplained before it can speak of reduced dynamics — and
that residue is precisely U3's territory.** AQFT is the only one of the five in which the
partition is neither primitive nor chosen.

## PART 6 — CLASSIFICATION: **UNCHANGED — U3-REQUIRES-DEFINITION**

**A deliberate non-upgrade.** AQFT *supplies* a candidate primitive (algebra + causal structure
+ state), so the pre-U3 gap found in `6675d1c` is now **fillable** rather than missing. The
remaining work is choosing or unifying a definition — **not** settling an unresolved deeper
primitive. So `U3-REQUIRES-DEEPER-PRIMITIVE` is **not** justified, and neither is
`NOT-YET-WELL-POSED`: under interpretation B the question is precisely statable, which is the
opposite of ill-posed.

## WHAT U3 IS ACTUALLY ASKING

U3 asks, of a physical description that admits some notion of parts, what determines whether
that division belongs to the structure being described or to the description of it. It does not
presuppose that a division exists: stated algebraically, the question is under what conditions
on a system's primitive structure — its observables, their causal and inclusion relations, the
state, and any scale — a subsystem/environment structure is **available at all**, whether those
conditions are forced or contingent, and whether any resulting structure is canonical or one
admissible choice among many. An answer must exhibit either the conditions under which such
structure is compelled, or a demonstration that it is irreducibly chosen — in both cases by
derivation rather than stipulation.

## WHAT WOULD COUNT AS A U3 DERIVATION — THE DELETION TEST

**Remove every partition-valued object from the inputs. If the derivation still runs, it is a
candidate. If it fails, the split was an input and the argument is disqualified.**

This is symmetric — it equally rejects a "fundamental" answer that smuggles in a factorization
and an "emergent" answer that smuggles in a projector — and it rejects all five disallowed
moves: assuming `H_S ⊗ H_B`; assuming a projector `P`; assuming a system/environment
decomposition; renaming coarse-graining; deriving decoherence after assuming the split.

## GUF RELEVANCE — EXPLICITLY HYPOTHETICAL

No GUF exists, and none is registered. **If** a future framework derived effective subsystem
structure from a deeper common primitive, its contribution beyond sector-by-sector response
calculation would be this: sector calculations each *begin* by choosing a partition, so their
agreement is currently a family resemblance among separately-made choices. A derivation of when
partitions are available would convert that resemblance into a shared consequence, and would
tell you which sectors' constitutive descriptions are *compelled* rather than merely
*available*. That is a statement about the scope of a language, not about the nature of
reality — and CHARTER §8 plus `u4`'s "interpretation cannot precede the theorem" both bind it
to arrive after the theorems, not before.

## W-0 STATUS — AQFT/external-foundation comparison reconciled; U3 classification reviewed; no physics executed; A-F unchanged; nothing banked.
