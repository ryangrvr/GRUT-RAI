# H¹ DYNAMICAL THEOREM CAMPAIGN — STAGE 1: RECONSTRUCTION + COEFFICIENT LOCUS

**Date:** 2026-09-03 · **Instrument:** `wall_kr_h1_dynamical_stage1.py` ·
**Artifact:** `WALL_KR_H1_DYNAMICAL_STAGE1_RESULT.json` · **Battery: 21/21, zero failures.**
**Per the work order, this is the RECONSTRUCTION stage only — the A/B/C adjudication is
deliberately NOT made here.** Read-only on frozen artifacts; register sha256 identical
pre/post; A-F unselected; nothing banked. W-0.

## THE STAGE'S CENTRAL RESULT: THE ZERO'S LOCUS IS NOW EXACT

The frozen record's phrase "the H¹ sector vanishes identically" is now pinned to its precise
locus, and it is the strongest possible one:

> **coeff(H,1) of `sig_g`, `sig_l`, `ret_wigner` and `nk_wigner` is IDENTICALLY ZERO,
> pointwise, at the integrand level — in both CTP combinations, in general d, for all u_b —
> before any integration or cone reduction.**

This is stronger than the GRADE-stage statement (Im Σ_H1 = 0 after cone reduction): there is
nothing for the reduction to cancel, because the integrand's O(H) part is the zero function.

**Disclosed false negative from this campaign's own first pass:** an `expand()`-only census
reported "16 nonzero H¹ terms" in every object. They are unmerged exponential *fractions* —
`expand` does not combine e^{2iqu′}/e^{2iqu} — and the zero appears only under
together/cancel/powsimp. Recorded so the wrong test cannot recur.

## STEP 1 — DECLARED DYNAMICS, VERIFIED FROM FROZEN SOURCES

- **State:** the exact BD mode of the chart, frozen in T2 verbatim:
  h(u) = e^{−iku}[(1−Hu) + iH/k] — polynomial in H, terminating at O(H).
- **Frozen GRADE record:** Im Σ_H1 = 0 in closed form, **general d**.
- **Frozen ASSEMBLE record:** the H¹ fork scan found no divergence class in either
  combination.
- The T3 integrand cache is git-tracked frozen content (sha recorded).

## STEP 5 SCOUT — THE MECHANISM, PROVED IN PARTS, WITH ITS HONEST COMPLICATION

Executed sub-lemmas (each a gated symbolic identity, not an argument):

- **L0 (exact):** h′(u) = −ik(1−Hu)e^{−iku}. The derivative of the BD mode carries the *same*
  conformal factor — the H from differentiating (1−Hu) cancels against the phase derivative of
  the state piece.
- **L1:** the (0,0) and (1,1) pairs equal flat × (1−Hu)(1−Hu′) through O(H) — **the BD state
  piece iH/k enters pair products only at O(H²)** (exhibited with its exact O(H²) residual).
- **L2 (the honest complication):** the mixed pairs (1,0) and (0,1) are **not** conformal at
  O(H): each carries an extra residual **−H × (flat pair)**, in closed form.

**Consequently the pointwise zero decomposes into exactly two cancellations:**

| | content | status |
|---|---|---|
| **C1** | conformal weight balance — two vertices' a² weight (+2Hu_i each) against two lines' conformal dressing (−H(u+u′) each) | algebraic identity, gated |
| **C2** | the sum of mixed-derivative residuals (−H × flat pair per one-derivative line) over the T1 vertex's derivative routing vanishes | **the genuinely dynamical half — a FLAT-VERTEX identity, precisely isolated, NOT yet proven** |

**A bonus the mechanism gives for free:** since the state piece enters at O(H²) (L1) and h′ is
exactly conformal (L0), the same structure explains **why the loop's first curvature
correction is O(H²)** — the H² sector is where the BD state piece first speaks.

## WHAT REMAINS BEFORE ADJUDICATION (all decision-free)

1. **(iv)** read the per-vertex a-weight off the frozen T1 artifact (C1 assumes a²; the
   general-d zero suggests the D3 continuation keeps chart weights at their d=3 values —
   to be verified, not assumed).
2. **(C2)** prove or refute the mixed-residual flat-vertex identity — Step 3's independent
   route *is* this derivation.
3. **Step 6 controls:** an α-vacuum-like O(H) admixture and a weight deformation a² → a³,
   each of which should break the zero on the toy assembly.
4. **Step 7 note, already visible:** the pointwise integrand zero leaves no room for a
   loop-generated *local* H¹ either — b and c are both killed at the source if C1+C2 close.

## VERDICT: **DEFERRED** — stage 1 only, per the work order.

## W-0 STATUS — H¹ reconstruction stage complete; no low-frequency physics; A-F unchanged; nothing banked.
