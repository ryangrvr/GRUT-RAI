# H¹ CAMPAIGN — STAGE 2B.4.2.1: THE FROZEN OBJECT'S STRUCTURAL CENSUS

**Date:** 2026-09-03 · **Instrument:** `wall_kr_h1_stage2b421_census.py` ·
**Artifact:** `WALL_KR_H1_STAGE2B421_RESULT.json` · **Battery: 12/12, zero failures.**
**2B.4.2.1 only — load, verify, census. No grouping, no simplification, no cancellation.**
Frozen store verified by sha; round-trip exact (292 terms). Read-only; register sha256
identical pre/post; A-F unselected; nothing banked. W-0.

## THE CENSUS (exp-free numerator / denominator split)

| quantity | structure |
|---|---|
| **net phase** | **ONE class: e^{2iq(u′−u)} — all 292 terms** |
| endpoint (numerators) | at most LINEAR in u and u′; occupancy **u-only = 146, u′-only = 146, both = 0, neither = 0** |
| numerator ω | degrees 0..4 (64/36/100/48/44) |
| numerator q | degrees 0..2 |
| numerator d | degrees 0..2 |
| denominators | **endpoint-free**; (d-polynomial, deg 2..6) × q^{0,1,2} |

## WHAT THE CENSUS ALREADY SETTLES FOR THE LATER STAGES (recorded, not pursued)

1. **The phase-class question (2B.4.2.3) is answered: there is exactly ONE phase class.**
   Whatever cancels, cancels inside e^{2iq(u′−u)} — no cross-phase mechanism exists.
2. **The endpoint split is perfectly balanced and disjoint**: 146 u-linear terms against
   146 u′-linear terms, no uu′ terms, no endpoint-free terms. A u ↔ u′ pairing is the
   natural involution candidate for 2B.4.2.5 — noted as a candidate only.
3. The denominators are endpoint-free d-polynomials (× small q powers), so the cancellation
   is a statement about **rational functions of (d, ω, q) paired across the u/u′ split**.

## CENSUS-PASS CORRECTIONS (disclosed)

Two representation traps struck the census itself before the numbers above stabilized: exp
factors hiding inside composite (Add) denominators defeated the first phase-stripper
(`factor_terms` fix), and one gate encoded a wrong expectation (q-free denominators) that the
data corrected. Both fixed at the gate/census level; the frozen object was never touched.

## VERDICT: DEFERRED — census only.

## W-0 STATUS — census complete; grouping stages not entered; A-F unchanged; nothing banked.
