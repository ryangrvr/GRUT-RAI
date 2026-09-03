# H¹ CAMPAIGN — STAGE 2B.4.2.5: INDEPENDENT ROUTE B (CLOSED)

**Date:** 2026-09-03 · **Instrument:** `wall_kr_h1_stage2b425_routeB.py` ·
**Artifact:** `WALL_KR_H1_STAGE2B425_RESULT.json` · **Battery: 26/26, zero failures.**
**VERDICT: `ROUTE-B-CLOSED`** — explicitly **not** yet called a theorem, Class 1, or
GRUT-anything; the final theorem/classification stage comes afterward, per the order.
Read-only on frozen artifacts; register sha256 identical pre/post; A-F unselected; nothing
banked. W-0.

## GOVERNANCE FIX ADOPTED

`v4` is now verified **by ref identity** — HEAD == origin/v4 — not by branch name (the local
branch is `master`; "v4" is the remote ref). The earlier `HEAD=="master"` label/prose mismatch
is corrected exactly as instructed.

## INDEPENDENCE DISCIPLINE, HELD

Route B never read `B_mixed`, the 146/146 split, the 39 classes, or the 8-class core. Its
inputs: the frozen flat **C⁰** vertex entries, and the O(H) line residual **derived from the
mode-function product rule** — L1 re-derived in-run (the BD state piece enters pair products
only at O(H²); the O(H) dressing is purely conformal, −(u+u′)·W_flat per line). A
**construction-validation gate** confirms the mode-derived m_key equals the machinery m_key at
a representative key (cross-check only, not a proof input).

## THE RESULT

**M = Σ over 36 native routing keys of V_k · m_k ≡ 0, pointwise in n̂, pre-angular** —
d-symbolic (no d = 3), ω-free in m_k, q-symbolic. Post-angular zero as consistency.

## THE LADDER CLOSED FORM — GATED PER KEY (all 36)

$$ m_{key} = i\,\mathrm{pref}\,(g+h-e-f)\,(-1)^{e+f}\,q^{N-1}\,W_{flat}^2, \qquad N=e+f+g+h $$

with (e,f) the vertex-1 and (g,h) the vertex-2 derivative orders. **The weight is vertex-2
minus vertex-1 derivative totals — manifestly antisymmetric under vertex exchange.**

## THE MINIMAL COLLECTIVE UNIT — PROPAGATOR-FREE

The identity reduces, per total-order sector N ∈ {0,1,2,3,4}, to the purely combinatorial
flat-vertex statement

$$ \sum_{k:\,N\ \text{fixed}} V_k\,(g+h-e-f)\,(-1)^{e+f} = 0 $$

**gated for every sector.** 14 keys vanish individually (weight or V zero); 22 cancel within
their N-sector. No propagator algebra remains in the identity.

## STRUCTURAL STRENGTHENING — MOMENTUM CONSERVATION IS NOT LOAD-BEARING

The planned Control C *expected* that breaking the equal-and-opposite line routing would
destroy the identity. **The data refuted the expectation** (disclosed): with a fully symbolic
independent line-B momentum q_B, **M(q, q_B) ≡ 0 identically** — the identity **decomposes per
line**, exactly as the independent leg-1 verification predicted.

## WHAT IS LOAD-BEARING (controls with teeth)

- **Control A detects:** perturbing one flat-vertex coefficient V_k breaks the sector identity
  — the C⁰ entries are load-bearing.
- **Control B/D detects:** flipping one key's weight/residual sign breaks it — the
  derivative-demotion weight structure is load-bearing.

## INDEPENDENT ADVERSARIAL VERIFICATION — 3/3 CONFIRMED, ZERO ERRORS

Three legs (ladder; compensator bookkeeping; Euler representation) all **CONFIRMED** by
independent agents, with sharpenings adopted: the closed form above (leg 1); the
**error fingerprint** — a residual ∝ 2(u+u′)·Σ⁰ diagnoses exactly the double-compensation
bug (leg 2); the Euler-derivative representation of M as the total internal-frequency
derivative of the contracted vertex pair at the eigenvalue point (leg 3 — the antisymmetry
link to Protection 1 assessed as *plausible, not yet established*).

## CLASSIFICATION EVIDENCE (no verdict)

Route B used **only**: the flat EH C⁰ vertex, (−i d/du) derivative algebra, momentum routing,
P^TT contraction, and the O(H) conformal dressing of the massless line. It did **not** use BD
state specifics beyond that dressing, retarded/CTP structure, angular d-continuation, or any
dynamical ingredient.

## DISCLOSED CONSTRUCTION DEFECTS (self-caught, fixed at source)

1. **Double-compensation:** the compensator was first applied per line (yielding
   +4(u+u′) instead of +2), making M ≠ 0 — caught by the M-gate, fixed, and now
   fingerprinted by leg 2. An intermediate run consequently printed `ROUTE-B-UNRESOLVED`;
   that verdict was an artifact of this bug plus the wrong Control-C expectation, both
   corrected under gate.
2. **Key packing** in the second implementation (((ν₁ᵛ¹,ν₁ᵛ²),(ν₂ᵛ¹,ν₂ᵛ²)) vs the frozen
   ((ν₁ᵛ¹,ν₂ᵛ¹),(ν₁ᵛ²,ν₂ᵛ²))) — crashed on a KeyError, fixed to the frozen convention.

## SECOND IMPLEMENTATION

Explicit P^TT dyads at exact rational directions with ν-decomposed index contraction — a
structurally different path from the cdecomp/moment machinery — gives **M = 0 at every
direction**. The representation cross-check against the 2B.4.2.4 native aggregate zero is
recorded as validation only.

## VERDICT: `ROUTE-B-CLOSED`. The theorem/classification stage is next and is NOT entered here.

## W-0 STATUS — Route B independently closed; no low-frequency physics; A-F unchanged; nothing banked.
