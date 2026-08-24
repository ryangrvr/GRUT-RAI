# Replacement Priority — post definition-as-target audit

**Date:** 2026-08-23. Ranking: load-bearing reach · physical importance · falsifiability ·
computational tractability · **in-house buildability (walls A–C checked BEFORE work starts)**.

| rank | replacement | load-bearing | falsifiable | tractable | in-house? | wall risk |
|---|---|---|---|---|---|---|
| 1 | **rung7_w3 no-crossing** — replace wz_sign.py citation with the kernel-family discriminator result (already built) | HIGH (rung7 family) | yes — crossing vs non-crossing per kernel | done; needs formal write-up + parameter-boundary scan | YES | none — pure response theory |
| 2 | **two-pole/oscillatory boundary scan** for rung7_w3: map the crossing/non-crossing boundary in (τ₁/τ₂, A₁/A₂, γ/Ω) space | medium-high | yes | moderate — grid scan of existing machinery | YES | none |
| 3 | **rung8 two-band test with oscillatory modes**: does a damped-oscillator kernel produce O(1) in two bands while staying passive+cosmologically-allowed? | HIGH (kills or saves the generic no-go) | yes | moderate — reuse H₀τ bound machinery per mode | LIKELY | wall C (TTW in-out premise) touches the cosmological side |
| 4 | rung3 single-pole emergence: microscopic derivation of relaxation-time scale from collisional/analytic-bath class | highest importance | partially | hard — genuine research calculation | UNCERTAIN | wall A adjacent |
| 5 | remaining grep-only calc files: hand-read for the same pattern | low each | n/a | cheap | YES | none |

## Notes

1. **Rank 1 is nearly free:** the discriminator already computed the honest answer; what remains
   is writing the parameter-boundary section and re-pointing rung7_w3's citation. No physics left
   undone for the no-crossing observable at current scope.
2. **Rank 2 is the natural extension** and directly serves Category 3 of the substitution test:
   it establishes whether ANY admissible two-real-pole kernel crosses under some weighting
   (expected: no — monotonicity argument suggests the whole real-relaxation class is safe).
3. **Rank 3 decides whether the O(1) no-go generalizes** beyond Debye. If oscillatory modes give
   O(1) two-band signatures within cosmological bounds, the no-go is Debye-specific; if not,
   it strengthens to the full admissible family.
4. Rank 4 is where walls bite: flagging now per instruction rather than discovering mid-work.
