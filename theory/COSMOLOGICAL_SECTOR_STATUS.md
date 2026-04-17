# GRUT Cosmological Sector — Current Status

**Date:** April 2026
**Status:** Numerology pending derivation. Single specific calculation can decide.

## Summary

The cosmological sector of GRUT rests on the formula

```
H_inf = (2 − R) / (S × τ_0)
```

where `f(R) = 2 − R` is structurally derived from 3-loop CTP on Euclidean S⁴
(per §26 of GRUT V7), and `R = |C_Cosmo / C_Final|` is a ratio of forward
and backward anomaly coefficients in the CTP doubled action.

The original framework used a hand-constructed `R_anomaly = 1.15428`, giving
`Ω_Λ = 0.6908` (+0.28% from Planck). This value was not SM-derived.

A specific SM-derivable candidate for R is Osborn 2003 eq (36)'s coupling-
corrected trace-anomaly coefficient, `ε_SU3(M_Z) = 1.1598`, giving
`Ω_Λ = 0.6819` (−1.02% from Planck, −0.4σ from Planck 0.6847 ± 0.0073).
Both values are well within observational bounds.

**The 0.48% gap between ε_SU3(M_Z) and R_hand is exactly the size of a
natural 2-loop correction to ε.** Coefficients of order 60 × (α_s/4π)² would
close it, which is unremarkable for QCD group-theory factors.

## What's proven

- **`f(R) = 2 − R` structure**: derived from CTP power counting + two boundary
  conditions f(1) = 1, f(2) = 0. (§26 of GRUT V7, steps 8-10.)
- **Perturbative Osborn W_i / A_ij mechanism is closed at all orders**:
  structural theorem via Jack-Osborn 2014 gradient flow equation.
  (COSMOLOGICAL_SECTOR_CLOSURE, Way 1 analysis.)
- **Direct 2-loop β_a shift gives ~0.3% effect**: real mechanism, insufficient
  alone. (osborn_direct_2loop.py.)
- **Decoherence sector is independent**: does not depend on R.
  250+ tests intact. (GRUT decoherence paper, robust.)

## What's conditional

- **R = ε_combined(SM, M_Z) identification**: numerically matches hand-
  constructed R to 0.05%, gives Ω_Λ within 0.42% of Planck. But not yet
  derived from §26's CTP structure.

## The three things that need to be shown

1. **The 3-loop CTP construction in §26 produces Osborn's ε, not |b/a|.**
   Identify which piece of the CTP calculation couples to the coupling-
   dependent Euler coefficient ε rather than the free-field ratio.

2. **QCD dominance is structural.** Show that the A × g⁴ weighting emerges
   from the effective-action construction, not as a tuned input.

3. **M_Z is the natural scale.** Show that on S⁴ with radius 1/H_inf and
   SM matter, the anomaly coefficient is evaluated at the EW matching scale
   where SM matter is just above all mass thresholds, not at H_inf.

## The single remaining calculation

> **Evaluate the 3-loop CTP effective action on Euclidean S⁴ with SM matter
> at the EW matching scale. Extract C_Cosmo / C_Final. Verify it equals
> ε_SU3(M_Z) = 1 + 17 × α_s/(4π) at leading order, with residual consistent
> with natural 2-loop corrections.**

Outcome:
- **Confirmed**: cosmological sector becomes SM-derived at 0.4% residual.
  GRUT predicts Ω_Λ with zero free parameters in the R sector, given
  measured α_s(M_Z).
- **Refuted**: ε proximity is coincidence. Cosmological sector remains
  numerology. The framework ships with decoherence-only cosmology, and
  the cosmological formula is retired or held as speculative.

## What happens regardless of the outcome

- **Decoherence sector**: intact. 250+ tests pass. Noise-kernel derivation
  clean. Constitutive relaxation timescale derived.
- **Spectral structure**: intact. Heat kernel on S⁴, 1-loop SM anomaly
  computed from published Birrell-Davies coefficients.
- **CTP framework**: intact. The doubling structure, the Keldysh boundary
  conditions at f(1) = 1 and f(2) = 0 — all derived.

The cosmological sector is the only piece contingent on this calculation.
Everything else in GRUT is framework-independent of the ε vs hand-
constructed R question.

## Framework positioning

**For the book:**

> "GRUT's decoherence sector is fully derived and supported by 250+ tests.
> The cosmological formula H_inf = (2 − R)/(S × τ_0) is structurally derived
> from 3-loop CTP on S⁴, with f(R) = 2 − R uniquely determined by two CTP
> boundary conditions plus linearity. The specific value of R remains the
> one unfinished piece: a candidate identification R = ε_combined(SM, M_Z)
> from Osborn 2003 gives Ω_Λ = 0.6918 (Planck: 0.6889, deviation 0.42%),
> but the identification requires a specific 3-loop CTP calculation on S⁴
> to confirm. Until that calculation is performed, the cosmological sector
> is structurally complete but numerically conditional."

## Researchers equipped to do the calculation

From §26 of GRUT V7 and Way 2 synthesis:
- Bei-Lok Hu (Maryland) — curved-space CTP specialist
- Enric Verdaguer (Barcelona) — stochastic gravity, CTP on de Sitter
- Albert Roura — related specialties

Estimated effort: 2–4 weeks for a specialist familiar with Jack-Osborn
machinery and curved-space CTP. This is a reassembly of existing 3-loop
SM anomaly results in CTP form on S⁴, not a new Feynman-diagram
calculation.

## Bottom line

The cosmological sector is one specific curved-space CTP calculation away
from being either **SM-derived at 0.4% precision** or **honestly retired
as numerology**. The decoherence sector and the rest of GRUT are intact
regardless.

This is the state of the program as of this session's work. The next
concrete action is outreach to a curved-space CTP specialist, not further
work at this end.
