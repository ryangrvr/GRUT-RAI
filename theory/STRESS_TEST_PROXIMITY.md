# Stress Test: How Robust is the 0.46% Proximity?

## The question

The observation: ε_SU3(M_Z) = 1.1596 and R_needed = 1.1543 agree to 0.46%.
Is this agreement robust across reasonable variations in inputs and
assumptions, or does it fall apart as soon as any choice is perturbed?

## Test results

### Test A: α_s(M_Z) uncertainty ✓ ROBUST
- α_s = 0.1181 ± 0.0011 (PDG)
- ε range: 1.1583 to 1.1613 (0.26% spread)
- Gap to R_needed: stays near 0.47% across the PDG range

**Conclusion:** Not sensitive to α_s measurement uncertainty.

### Test B: Scale choice ✗ FRAGILE
At different μ with 1-loop running:

| Scale | α_s | ε_SU3 | Diff from R_needed |
|-------|-----|-------|-------------------|
| 10 GeV | 0.090 | 1.121 | **−2.87%** |
| M_Z (91 GeV) | 0.118 | 1.160 | +0.47% |
| m_top (173) | 0.130 | 1.176 | +1.88% |
| 500 GeV | 0.154 | 1.208 | +4.65% |
| 1 TeV | 0.174 | 1.236 | +7.08% |
| 10 TeV | 0.316 | 1.427 | +23.6% |

**Conclusion:** The 0.46% match is specific to evaluating at M_Z. There
is no strong physics argument for M_Z being the "right" scale for the
cosmological anomaly. Why not m_top? Why not the QCD confinement scale?
Without a principled reason to pick M_Z, the proximity is a scale-choice
artifact.

### Test C: Dirac vs Weyl convention ✗ CRITICAL
- Dirac convention: A = 17, ε = 1.160
- Weyl convention: A = 5, ε = 1.047

**Factor of ~3 difference in the correction size.** The SUSY cross-check
(Osborn line 655: 2R_ψ = C + R) confirms Dirac, but if the convention
was off, the whole match would disappear. The proximity is entirely
dependent on this convention being the right one.

### Test D: 2-loop correction size ~ same as the gap
- (α_s/π)² ≈ 0.141% at M_Z
- Gap: 0.47%
- 2-loop correction could plausibly move ε by a few × 0.1%

**Conclusion:** A 2-loop correction of natural size could close the gap,
or widen it — depends on sign. Not informative without the actual 2-loop
calculation.

### Test E: H_0 dependence ✗ SIGNIFICANT
R_needed depends on which H_0 we use:

| H_0 (km/s/Mpc) | R_needed | Diff to ε_SU3 |
|-----------------|----------|---------------|
| 67.4 (Planck) | 1.1867 | **−2.27%** |
| 70.0 (midrange) | 1.1553 | +0.47% |
| 73.0 (SH0ES) | 1.1191 | +3.63% |

**This is probably the most important test.** The 0.46% match is not
a feature of the physics — it's a feature of choosing H_0 = 70.
With Planck's H_0 = 67.4, the match is 2.3% off in one direction.
With SH0ES's 73.0, it's 3.6% off in the other direction.

The Hubble tension itself (currently unresolved) means R_needed varies
by ~5% depending on which H_0 measurement you trust.

### Test F: Combination rules for SM ✓ ROBUST
Different ways to combine the three gauge groups all give 1.16-1.18:

| Combination | Result |
|-------------|--------|
| QCD alone | 1.1598 |
| QCD + SU(2) + U(1) added | 1.1618 |
| QCD × SU(2) × U(1) multiplied | 1.1618 |

The EW cancellation keeps the answer near 1.16 regardless of combination rule.

## The honest conclusion

The 0.46% proximity is:

- **Robust** to α_s uncertainty, to SM combination rule, to EW cancellation
- **Fragile** to scale choice (5-10% variation at nearby scales)
- **Critically dependent** on Dirac vs Weyl convention (factor of 3)
- **Specific** to H_0 = 70 km/s/Mpc — with Planck's H_0, the gap is 2.3%,
  with SH0ES's H_0, the gap is 3.6%

What this tells us:

1. **The match is not as clean as it looked.** It depends on specific
   choices that could reasonably be different. The "0.5% agreement"
   framing oversells the robustness.

2. **The order-of-magnitude match IS real.** ε_SU3 at electroweak scale
   is ~1.15, and R_needed is ~1.15. These are both O(1) numbers in the
   right range, agreeing at the few-percent level across reasonable
   choices.

3. **The Hubble tension becomes structurally important.** GRUT's
   cosmological formula H_inf = (2-R)/(S·τ_0) implicitly assumes a
   specific H_0. The framework's Ω_Λ prediction is actually a
   prediction about ε vs H_0 consistency.

4. **Scale choice is the weakest link.** If the brother's answer to
   Q1 is "yes, CTP selects ε," we need a principled argument for
   WHICH scale ε is evaluated at. Without that, the match is
   parameter-dependent.

## What this means practically

The brother's questions are still the right ones, but:

- **Q1 answer alone is not enough.** Even if CTP selects ε over b/a,
  we need to know at what scale. Is it M_Z? M_top? The horizon scale?
  The scale where cosmological decoherence transitions?

- **The H_0 dependence of R_needed cuts both ways.** If the SM
  trace anomaly really determines R, and R determines Ω_Λ, then
  knowing ε fixes Ω_Λ and therefore predicts H_0. That would be
  a prediction, not a fit — but only if ε and Ω_Λ are both computable.

- **The framework's scale ambiguity is a real concern.** The asserted
  values (S = 108π, τ_0 = 41.9 Myr) have scale content built in.
  If ε is the right object but evaluated at the wrong scale, the
  "match" is coincidence. If evaluated at the right scale, the match
  could be meaningful.

## A more honest headline

**At M_Z with Dirac convention and H_0 = 70, ε_SU3 and R_needed agree
to 0.46%.** Change the scale, switch to Weyl convention, or adopt
Planck's H_0 instead, and the gap grows to 2-10%. The order-of-magnitude
proximity is real; the 0.5% precision is not a feature of physics,
it's a feature of specific input choices.

The stress test doesn't kill the hypothesis. But it does replace
"striking 0.5% match" with "ε_SU3 is in the right ballpark at the
electroweak scale, with a specific sub-percent match contingent on
several choices."

That's still interesting. It's just not unambiguous evidence.
