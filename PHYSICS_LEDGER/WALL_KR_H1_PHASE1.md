# H¹ CLOSURE — PHASE 1: FORMAL THEOREM / CLASSIFICATION

**Date:** 2026-09-03 · **Instrument:** `wall_kr_h1_phase1_theorem.py` ·
**Artifact:** `WALL_KR_H1_PHASE1_RESULT.json` · **Battery: 15/15, zero failures.**
**SCOPE VERDICT: `THEOREM-LOCAL`.** Phases 2–3 (physical deformations) not run; no
H1-THEOREM-A/B/C issued; no GRUT language. v4 verified by ref identity. Read-only; register
sha256 identical pre/post; A-F unselected; nothing banked. W-0.

## WHAT ROUTE B PROVES — NOW WITH ITS MECHANISM

Define, per external configuration, the pre-angular totals

$$ S_{j,m}(\hat n,\omega,q) \;=\; \sum_{\substack{k:\ e+f=j\\ g+h=m}} V_k $$

(j = vertex-1 derivative total, m = vertex-2 total). Then:

**THE VERTEX-SWAP RELATION — gated symbolically, all three frozen configurations
(plus_z, cross_z, plus_x):**

$$ S_{m,j} \;=\; (-1)^{\,j+m}\, S_{j,m} $$

**in the no-ω-flip form** (the ω-flipped variant is FALSE — ω needs no transformation,
matching Route B's finding).

**THE PAIRING PROOF — three lines, gated on the actual objects.** In the sector sum
Σ_{j+m=N} (m−j)(−1)^j S_{j,m}, pair (j,m) ↔ (m,j):

$$ (m-j)(-1)^j S_{j,m} + (j-m)(-1)^m S_{m,j}
 = (m-j)(-1)^j S_{j,m} + (j-m)(-1)^{j+2m} S_{j,m} = 0, $$

and the diagonal j = m carries zero weight. **The sector identity FOLLOWS FROM the swap
relation.** The mechanism of Protection 2 is therefore **vertex-exchange antisymmetry** — the
same mechanism class established for Protection 1.

## THE THEOREM, AT ITS STRONGEST HONEST SCOPE

> **THEOREM-LOCAL.** For the frozen flat Einstein-Hilbert cubic vertex under the declared TT
> contraction and routing conventions, and for every frozen external configuration, the
> O(H) mixed contribution satisfies Σ_k V_k·m_k ≡ 0 pointwise pre-angular; equivalently the
> propagator-free sector identity holds for N = 0..4; and both follow from the gated
> vertex-swap relation S_{m,j} = (−1)^{j+m}S_{j,m} together with the zero-weight diagonal.

**Separations kept, per the order:** this is a *frozen-construction identity* whose mechanism
is derived and gated — not yet a *general EH identity*. **NOT claimed:** THEOREM-EH-TT
(generalizing requires deriving the swap relation from vertex Bose symmetry plus the D2
relabeling for an *arbitrary* admissible contraction — named as the remaining generalization,
not asserted). **NOT claimed:** any GRUT-specific content; that is Phase 8's question.

## WHY THIS IS MORE THAN THE ROUTE-B GATE

Route B established *that* the sum vanishes and reduced it to per-sector combinatorics.
Phase 1 establishes *why*: a single two-index symmetry of the flat vertex-pair totals, from
which the vanishing follows by exact pairing. The identity is no longer an evaluated zero; it
is a consequence with a one-line cause.

## STATUS IN THE CLOSURE PACKAGE

Phase 1 green. Next per the package: Phase 2 (α-vacuum-like state deformation control) and
Phase 3 (a² → a³ weight deformation control) — **not run here**; then representation
robustness, final independent verification, the truth table, the A/B/C adjudication, the
standard-theory subtraction, and the closure memorandum.

## W-0 STATUS — Phase 1 complete; mechanism derived and gated; no deformations run; A-F unchanged; nothing banked.
