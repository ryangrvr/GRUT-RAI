# R3 — Scale Selection on S⁴: Honest Verdict

**Date:** April 2026
**Status:** Question reduced to specific technical issue; NOT cleanly closed.

## Sources consulted

1. **Hu & Verdaguer (2008)**, *Stochastic Gravity: Theory and Applications*,
   Living Reviews in Relativity 11, 3. Saved locally as
   `/tmp/hv/lrr-2008-3.pdf` (112 pages, comprehensive review).

2. **Hu & Verdaguer (2003)**, same title, earlier arXiv version
   (gr-qc/0307032v1, 75 pages). Saved locally as
   `/tmp/paper2/0307032v1.pdf`.

3. **Osborn (2003)**, eq (36) already in `papers/references/`.

## The R3 question

On Euclidean S⁴ of radius 1/H_inf, with SM matter, the CTP effective
action has a coefficient of the form:

```
Im(Γ_CTP) ⊃ ε(μ) × b_free × (Euler integral on S⁴)
```

where ε(μ) = 1 + (1/3)(29C − 12R_ψ − (5/2)R_φ) × g²(μ)/(16π²).

Question: at what scale μ is g(μ) naturally evaluated, and does
this reproduce ε(M_Z) ≈ 1.16 (Planck match) or ε(H_inf) ≈ 1.03
(Planck miss)?

## Scale scan (from r3_scale_selection.py)

| Scale μ | α_s(μ) | ε_SU3 | ε_combined | Ω_Λ | vs Planck |
|:---|:---:|:---:|:---:|:---:|:---:|
| Λ_QCD (0.3 GeV) | 0.48 | 1.645 | 1.643 | 0.123 | −82% |
| **M_Z (91 GeV)** | **0.118** | **1.160** | **1.155** | **0.689** | **−0.04% ← PLANCK** |
| m_top (173 GeV) | 0.109 | 1.147 | 1.143 | 0.709 | +3.0% |
| 1 TeV | 0.090 | 1.121 | 1.116 | 0.754 | +9.4% |
| 10 TeV | 0.073 | 1.099 | 1.093 | 0.794 | +15.2% |
| m_thermal (1.6×10¹² GeV) | 0.029 | 1.039 | 1.032 | 0.904 | +31.3% |
| H_inf (10¹³ GeV) | 0.027 | 1.037 | 1.030 | 0.908 | +31.8% |
| M_Planck | 0.019 | 1.026 | 1.018 | 0.930 | +35% |

**Planck-matching μ is in a narrow 50–200 GeV window. H_inf and
M_Planck miss by 30%+.**

## What Hu-Verdaguer's framework actually says

From HV 2008, two key passages:

**(1) At pos 129430 (noise kernel in massless limit):**
> "In the massless case, we can use the **arbitrariness of the mass
> scale µ** to eliminate one of the parameters α̅ or β̅."

**(2) At pos 213772 (CTP action in Hartle-Hawking vacuum on dS):**
> "In this action ℓ² = 16πG, α = (2880π²)⁻¹, and **µ̅ is an arbitrary
> mass scale**. We are interested in computing the CTP effective
> action for the matter action and when the field φ is initially in
> the Hartle-Hawking vacuum. This is equivalent to saying that the
> initial state of the field is described by a thermal density matrix
> at a finite temperature T = T_H."

**HV explicitly state: μ̅ is arbitrary.** Physical observables are
μ-independent. The specific numerical values of individual coefficients
depend on μ choice, but the full effective action is RG-invariant at
the order computed.

**Their framework does NOT provide a unique scale selection that
forces μ = M_Z.**

## What this means for R_GRUT = ε

The identification R_GRUT = ε with the observed numerical value
1.15428 ↔ 1.1537 match at 0.04% holds specifically when ε is
evaluated at μ = M_Z. At other scales, the numerical match fails
substantially:

- μ = M_Z: Ω_Λ = 0.689 (match)
- μ = H_inf (standard dS choice): Ω_Λ = 0.908 (fails by 30%)

**If the standard HV practice (μ = H) is the correct scale
selection, the R_GRUT = ε identification FAILS.**

The M_Z choice that DOES match Planck is NOT forced by HV. It
would need a GRUT-specific structural argument.

## Three possible interpretations

### (α) The identification fails structurally

Standard dS QFT practice (μ = H with RG improvement) gives
Ω_Λ ≈ 0.91, which is inconsistent with Planck. Under this reading,
the R_GRUT = ε identification fails, and the M_Z match is a
numerical coincidence.

### (β) A GRUT-specific mechanism picks out M_Z

The CTP source doubling picture (Step 5) argued that
(g_+ − g_-) ~ g³/(16π²) comes from the 1-loop self-energy of
the coupling source. The natural scale for a matter self-energy
IS the matter mass. Under this reading, the SM self-energy is
computed at scales where matter is "fully on" (= top mass ~ M_Z).

This interpretation is NOT standard HV, but it's not in conflict
with HV either. HV say μ̅ is arbitrary; a specific physical
argument can select it for a specific observable.

### (γ) The 2-loop RG improvement compensates

At strict 2-loop, ε(μ) is accompanied by ln(μ²/M²) correction
terms. The combination:

```
full 2-loop coefficient = ε(μ) + explicit log(μ) terms
```

may be RG-invariant. If so, the Ω_Λ prediction would depend on
the full 2-loop structure rather than just ε(μ). This requires
doing the explicit 2-loop calculation to verify.

## Honest verdict on R3

**R3 is NOT cleanly closed by the HV framework alone.**

Under standard HV practice: μ = H, identification fails by 30%.

For the identification to hold at M_Z, GRUT needs EITHER:
- (α) A specific CTP-structural argument that selects the
  matter-self-energy scale (= top mass / M_Z) rather than the
  curvature scale, OR
- (β) A full 2-loop calculation showing that ε(μ) + accompanying
  logs is RG-invariant and matches the M_Z scheme result.

The "obvious" matter-decoupling argument (heavy fields decouple,
leaving lighter fields contributing at M_Z) **does not apply** in
the standard form because all SM matter is LIGHTER than H_inf
(no heavy fields to decouple from S⁴'s perspective).

## What this changes

The earlier task-01-to-05 synthesis concluded "one genuinely open
question remaining (R3)." R3 has now been examined and remains
open at the level of HV standard practice. The honest situation:

- The R_GRUT = ε identification at μ = M_Z gives a 0.04% match
  to Planck.
- The standard dS effective-action practice would evaluate at
  μ = H_inf, giving a 30% miss.
- The difference between these is a genuine scale-selection
  question that is NOT answered by the HV framework.

The specialist calculation (R3 resolution) would involve:
- Explicit 2-loop calculation on S⁴ with SM matter
- Checking whether RG-invariant observable matches 0.04% or misses by 30%
- If matches: establishes R_GRUT = ε via full perturbative
  treatment
- If misses: confirms the M_Z match is scheme-specific /
  coincidental

## Status update

Moving from:
> "One genuinely open question remaining (R3). Needs specialist."

To:
> "R3 examined rigorously. The M_Z scale that gives Planck match is
> NOT standard dS effective-action practice (which would give μ = H
> and fail Planck). The identification R_GRUT = ε requires either
> a CTP-specific mechanism to select μ = M_Z over μ = H, or a full
> 2-loop calculation showing the RG-invariant observable matches
> the M_Z result. This is the specific question for the specialist."

## Honesty protocol

This is where I have to stay honest. The earlier tasks 01-05 were
overly optimistic in framing "R3 is the only open question and the
infrastructure exists." A more careful reading of HV reveals that
their infrastructure does NOT actually select μ = M_Z — it leaves
μ arbitrary. The M_Z choice that makes GRUT's identification work
is GRUT-specific and needs its own justification.

This correction strengthens rather than weakens the "honesty ledger"
for this derivation attempt. The identification is still plausible
but the scale-selection argument is thinner than earlier drafts
claimed.

## For GRUT documentation

The V7 main doc and Zenodo paper should reflect this:
- R_GRUT = ε gives 0.04% Planck match at μ = M_Z
- Standard dS practice (μ = H) would give 30% miss
- The M_Z selection requires a specific CTP mechanism (Step 5)
- Whether that mechanism is physical or scheme-dependent is the
  genuine open question

This is a more honest framing than "the only open question is
specialist verification of the O(1) coefficient."
