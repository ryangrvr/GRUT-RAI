# H¹ CAMPAIGN — STAGE 2B.1: TAGGED RECONSTRUCTION (COMPLETE)

**Date:** 2026-09-03 · **Instrument:** `wall_kr_h1_stage2b1_reconstruction.py` ·
**Artifact:** `WALL_KR_H1_STAGE2B1_RESULT.json` · **Battery: 18/18, zero failures.**
**2B.1 only.** The reconstruction runs on the frozen T3 machinery itself (exec'd with a
sentinel stage), so every routing/sign/endpoint convention is the frozen one. **The Stage-1
pointwise zero was never read — the reconstruction reproduces it.** Read-only on frozen
artifacts; register sha256 identical pre/post; A-F unselected; nothing banked. W-0.

## THE RECONSTRUCTION

Five assemblies through the frozen `assemble()` routine, split by linearity levers:

| object | content |
|---|---|
| Σ⁰_flat | flat vertices × flat lines (H-free, gated) |
| A_vertex | full C-matrices × flat lines, O(H) — 246 terms |
| B_lines | H⁰ C-matrices × full W, O(H) — 270 terms |

**A_vertex + B_lines ≡ 0 pointwise** — the Stage-1 zero, reproduced from the split
assemblies alone.

## THE TAGS, AND WHAT THEY REVEALED

**C1 closes as predicted:** A_weight = +2(u+u′)·Σ⁰_flat cancels the two-line conformal
dressing −2(u+u′)·Σ⁰_flat exactly. A detecting control confirms the two-line count is
load-bearing.

**The 2A cross-cancellation hypothesis is REFUTED by the reconstruction.** C2′ was
hypothesized as [R_TT insertion] + [mixed W-residuals] cancelling *each other*. They do not
need to: **each vanishes separately.**

- **Protection 1:** A_R = A_vertex − A_weight **≡ 0 at the raw expand level.** The
  total-frequency insertion is annihilated on its own.
- **Protection 2:** B_mixed = B_lines − B_pureconf **≡ 0** (phase-merged, 292 unmerged
  terms). The ν-derivative-hits-conformal residuals cancel among themselves.

## THE MECHANISM OF PROTECTION 1 — DEMONSTRATED BY CONTRAST, TWICE CORRECTED

- **Angular-orthogonality conjecture: REFUTED by its own gate.** S inserted *without* the
  frequency factor **survives** at O(H).
- **The kill switch is the frequency factor.** S inserted *with* (ω+ν₁+ν₂) is annihilated at
  the raw level, in isolation from the weight.
- **Entry-wise completeness, exact:** C¹ = 2u·C⁰ + (ω+ν₁+ν₂)·C_S for **all 36** C-matrix
  entries — nothing untagged remains.

**Mechanism:** under the frozen vertex-2 convention (ω → −ω, u → u′), the (ω+ν₁+ν₂)
insertion is **vertex-exchange antisymmetric** on the flat eigenvalue structure, while the
S ⊗ C⁰ contraction is symmetric — the two vertices' insertions cancel pairwise.

## TWO SELF-CAUGHT DEFECTS, DISCLOSED

1. **The identical-printing-symbols trap, again — inside this instrument's own lever.** A
   plain `Symbol('H')` in the synthetic C-entries versus the module's assumed `H` made
   Isolation B read nonzero. Diagnosed by an entry-wise identity check; rebuilt with module
   symbols throughout.
2. Three earlier gate "failures" were **representation artifacts** (unmerged exponential
   fractions under expand-level comparison) — the standing lesson, applied to the gates
   themselves.

## WHAT REMAINS OPEN (verdict stays DEFERRED)

Protection 1 now has a demonstrated mechanism at reconstruction level. **Protection 2 — the
self-cancellation of the mixed residuals — has no mechanism yet**; that is the remaining
Route-B/2B.4 target. The three negative controls (2B.6–2B.8), the classification (2B.5), and
the C2′ verdict all remain open.

## W-0 STATUS — 2B.1 complete; pointwise zero reproduced with exact tags; no low-frequency physics; A-F unchanged; nothing banked.
