# P-6 — IS THE ACCESS SEED DYNAMICALLY SELECTABLE? VERDICT

**Date:** 2026-09-25 · **Charter:** `P6_SEED_SELECTION_CHARTER_01.md`
(frozen at `179c108` before the run) · **Authority:** GitHub Issue #2,
owner comment 5827344342 · **Instrument:** `calc/p6_seed_selection.py` ·
**Artifact:** `P6_SEED_SELECTION_RESULT.json` (sha `542c967101e0c8f7…`) ·
**Battery 38/39** — the one failure is a frozen gate preserved as found,
with a labeled post-hoc diagnostic (below). All halt-grade analytic
identities held (8.7e-15 refactorization invariance, 0.0 degenerate
symmetry identity, < 1e-12 swap and conservation checks); matched
controls at exactly 0.

## THE ANSWER

> **The seed is irreducibly supplied — with one precisely bounded
> exception.** Dynamics selects access **exactly up to its own block
> (central) decomposition and no further.** Inside an irreducible
> block, every tested selection principle either fails to select or
> reduces to standard structure. Per the frozen decision rule: **the
> access seed is retained as NON-DERIVED INPUT.**

### Where the selector works (L-S, the positive control)

Reducible dynamics (spin 1 decoupled from a hidden 2-spin sector):
cl({I, σ_x¹}; H) closes at exactly the site-1 algebra, dim 4, with zero
overlap (residual = 1 to 1e-9) against every hidden operator.
**SELECTED-IN-CLASS for reducible dynamics** — and this is central
decomposition, standard structure: **NULL-REDUNDANT** as a new
principle.

### Where selection fails, leg by leg

- **Minimality is interface-relative (L-A):** same dynamics, two
  declared interfaces — cl({I, σ_z¹}) = the parity commutant, dim 8;
  cl({I, σ_x¹}) = everything, dim 16. "The smallest dynamically closed
  algebra preserving the interface" changes with the interface. The
  owner's binding distinction is now a measurement: *minimal given a
  chosen interface ≠ uniquely selected by the dynamics.*
- **Causal structure + conservation cannot select, and the
  counterexample stands (L-B/E):** on the 3-spin chain, the end seeds
  σ_z¹ and σ_z³ share the causal graph, the conservation law
  ([H, P] < 1e-12), and — measured — the **identical** dynamical closure
  (both exactly the 32-dim parity commutant, two-sided span gap
  1.1e-13). Yet the coupled physics differs by **0.287** in the probe
  coherence. The closure selector is **non-injective over physically
  inequivalent seeds**: two seeds it cannot tell apart are physically
  different accesses. Owner point E is discharged constructively —
  **UNDERDETERMINED-SEED.**
- **Symmetry constrains equivariantly but cannot select (L-C):** on the
  exact swap-symmetric model the degenerate seed orbit {σ_z¹} vs {σ_z²}
  is indistinguishable (coherence diff 0.0, halt-grade analytic; the
  closures are exact W-images, gap 0.0). Any covariant selector is
  indifferent on the orbit; the choice is supplied (or spontaneous),
  not derived.
- **Sufficiency is order-relative (L-D1):** the P-4 order-6 pair,
  consumed at seed level: identical in-access hierarchy through
  declared order 4 (0.0 mismatch), separated by the newly coupled
  λ = 0.4 probe at 2.7e-2 with λ-scaling ratio 54.9 ∈ [0.7, 1.4]×2⁶.
  "Minimal sufficient access at order n" fails at the first unmatched
  order — never final.
- **Minimality is path-dependent even at fixed interface (L-D2):** for
  the same interface B₀ = σ_x¹ and the same dynamics, backward
  elimination in the two frozen orders lands on **two different minimal
  sufficient seeds** — M_fwd = {G3, G4, G5} vs M_rev = {G1, G3, G4} —
  each verified sufficient AND minimal (no single element removable).
  **PATH-DEPENDENT:** "the minimal sufficient seed" does not exist as a
  definite description.
- **Representation control (L-F):** entangling refactorization leaves
  the coherence invariant (8.7e-15) and the closure transforms exactly
  covariantly (V·cl(S; H)·V† = cl(VSV†; VHV†), gap 3.6e-14, dims
  32/32). No coordinate change masqueraded as selection anywhere above.

## THE FROZEN GATE THAT FAILED — preserved, and it teaches

The L-C broken-companion gate (H_C + 0.3σ_z² should separate the seeds
by > 0.01) **FAILED with a difference of exactly 0.0 and stays red.**
The labeled post-hoc diagnostic: σ_z¹ − σ_z² **annihilates the
even-parity block exactly** (residual 0.0 on both even basis states),
and the reachable sector from |↓↓⟩ *is* that block — so the two seeds
coincide as operators on the reachable sector for ANY z-fields,
symmetric or not. From the odd-block state |↓↑⟩ the same pair separates
by 1.503. The gate was mis-aimed: it assumed asymmetric fields lift the
degeneracy, but the degeneracy was never the symmetry's — it belongs to
the **reachable sector**. Reading (diagnostic, not promoted): seed
distinctions are physical only relative to the reachable/accessible
sector — degeneracies of selection are *more* generic than the symmetry
case the charter targeted, consistent with P-5's "access lives at its
changes."

## DEFECT HISTORY (disclosed)

1. First run: the closure's Gram–Schmidt used an absolute tolerance on
   unnormalized product matrices whose norms grow exponentially across
   sweeps — spans inflated to dim 64/64 (L-B) and dim 96 (L-F), the
   latter in a 64-dimensional space, a numerical impossibility that
   proved the bug. Fixed by normalizing every candidate before
   projection (relative tolerance, the charter's stated construction);
   post-fix L-B lands exactly on the 32-dim parity commutant (gap
   1.1e-13) and L-F covariance holds at 3.6e-14.
2. The L-C broken-companion gate failed as-run and is preserved red
   (above). No verdict-bearing quantity was edited post hoc.

## WHAT STANDS AFTER P-5 → P-6, AT RECORDED STRENGTH

> The candidate chain closes its access layer as: microscopic dynamics →
> influence hierarchy → sector structure → **access seed = non-derived
> input** (selected by dynamics only up to block decomposition; beyond
> that: interface-relative, order-relative, path-dependent,
> degeneracy-ridden, and non-injectively compressed by every closure
> invariant) → effective physics. No entropy/complexity/least-action/
> simplicity selector was evaluated (prohibited without its own
> charter). ℏ located-not-generated; type-III stays a boundary map; no
> proof-of-QM.

**The non-derived remainder:** realized hierarchy point per sector ·
ℏ's scale · type-III boundary · **the access seed (now attack-tested:
non-derived in-class, not merely non-derived-so-far).**

## HARD STOP

Verdict recorded. Per the owner's frozen decision rule: path dependence
AND inequivalent equally admissible seeds were both demonstrated, so
**the access seed is retained as non-derived input, and the owner may
now open geometry or gravity.** Λ_R, Matsubara, Π₀, U5 remain fenced;
ω⁷/class-4 stays open until the owner rules.
