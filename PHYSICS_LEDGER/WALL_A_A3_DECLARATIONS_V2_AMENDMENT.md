# WALL A, STAGE A3 — V2 AMENDMENT (supersedes ONE clause of the frozen v1)

**Date:** 2026-08-25 · **Supersedes:** exactly one clause of the frozen
`WALL_A_A3_DECLARATIONS.md` (sha256 `87e2d24d5be6d67970f4089a09aa61a28d4de8cf6471f987af3db1c2ac015f6e`)
and its mirror in `WALL_A_A3_REGISTRY.json` (sha256
`faa977d40f1ba31836e35b18223c1f573559b49649a84fad237a3809aae59b55`).
The frozen v1 files are NOT edited — this amendment is the superseding v2 the frozen
protocol requires. Every other clause of v1 stands unchanged and un-reopened.

## The superseded clause (Declaration 5 / checker-correction F3, as frozen)

> "Genuine residual freedom: xi^0 = C(x)/a(eta) plus time-independent spatial
> reparametrisations; fixed by requiring the synchronous coordinates coincide with the
> unfixed-computation coordinates asymptotically as eta -> -infty"

## The corrected clause (v2, binding from this date)

The full residual family preserving synchronous gauge (δg₀₀ = δg₀ᵢ = 0) is:

```
ζ⁰   = C(x)/a(η)
ζ_i  = C_i(x) − (∂_i C) · Ia(η),      Ia′(η) = 1/a(η)
```

The C-coupled spatial piece is **mandatory and time-dependent**: with ζ⁰ = C(x)/a and
time-independent ζ_i, one gets δh₀ᵢ = (∂_iC)/a ≠ 0 whenever C has spatial gradient —
the v1 "product" family exits the gauge. The parameter count (one C, three C_i, all
functions of x only) is unchanged from v1. **The fixing prescription is unchanged and
still suffices**: asymptotic coincidence with the unfixed computation at η → −∞ kills
the entire C-sector (both ζ⁰ = C/a and its coupled −(∂_iC)·Ia piece; e.g. on the de
Sitter chart a = −1/(Hη) both grow without bound as η → −∞) and fixes the C_i. The
post-prescription statement of v1 — the surviving freedom is time-independent spatial
reparametrisation, all removed — stands.

## Provenance (why this amendment exists — the mechanism working, recorded)

1. The A4 instrument (`wall_a_a4_dual_gauge.py`, built by the CHECKER while the usual
   builder was stalled) claimed to "re-derive" the frozen family — but its ζ_i conjunct
   was a **hard-coded True** (a print-statement fact, the exact defect class this
   program hunts, this time in the checker's own code).
2. The independent verifier fleet **refuted** the family claim by performing the
   substitution the instrument skipped, exhibited the gauge-exit of the v1 family, and
   confirmed the corrected family both ways with a(η) arbitrary. It simultaneously
   confirmed the invariance identity (step 4), the sign conventions by an independent
   diffeo-invariance derivation, and — critically — that steps 4–5 hold for **arbitrary**
   ζ, so the gauge-invariant-content conclusion of A4 is untouched by this error.
3. The instrument was corrected to compute what it had asserted (gates g3b/g3c: the true
   family preserves both synchronous conditions; the refuted product family exits the
   gauge — negative control), and re-runs exit 0.

## Scope of damage, stated exactly

- **Unaffected:** every A4 physics conclusion (slice equality, invariance identity, TT
  blindness, plants, guard), because they hold for arbitrary ζ; the v1 fixing
  prescription; the parameter count; every other frozen declaration (D1–D4, the rest of
  D5, the registry's barred lists, blind criteria, and discharge map).
- **Corrected:** the pre-prescription characterisation of the residual family, in the
  frozen F3 clause and in the A4 instrument's step 3.

This amendment is itself immutable once hashed; its sha256 is recorded in
AGENT_COORDINATION.md and the commit. Any further change requires a v3 citing this file.
