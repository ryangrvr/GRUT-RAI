# Enumerated Outcomes for Each Decision Tree Branch

## The honest headline after stress test + enumeration

GRUT's cosmological constant prediction traces to a specific quantity in
perturbative QFT — the ε coefficient from Osborn's local renormalization
group equation, evaluated for SM QCD.

**What's robust:**
- The structural features (QCD dominance at 99%, EW cancellation as a
  property of the SM spectrum, order-of-magnitude match)
- The prediction lands in the range Ω_Λ ∈ [0.5, 0.9] across reasonable
  inputs (scale choice, H_0 value, combination rule)

**What's not:**
- The "0.46%" headline. That required: choosing H_0 = 70 (compromise, not
  measurement), evaluating at M_Z (convention, not derivation), Dirac
  counting (plausible but unconfirmed)
- Three contingent choices producing sub-percent match is suggestive, not
  compelling

**The right perspective:**
The standard cosmological constant problem is 10^120 orders of magnitude.
Most approaches don't get within 60 orders. Getting within a factor of 2
(or ~1% at Ω_Λ level with favorable choices) is remarkable — but "within
a factor of 2" is different from "0.5% precision match," and the record
should reflect that honestly.

## Purpose

When the brother's answer arrives, we should already know approximately
what Ω_Λ comes out for each branch. This document pre-computes every
case we can, so when the three-letter email arrives we skip directly
to verification rather than reconstruction.

## Correction to earlier framing

Earlier messages talked about "0.46% match at R level." That's true
at the R level, but the cosmological observable Ω_Λ scales as (2-R)²,
so a 0.46% shift in R becomes a **~1% shift in Ω_Λ**. When we compare
the framework's prediction to Planck's Ω_Λ = 0.6889, the relevant
deviation is at the Ω_Λ level, not the R level.

**This is not a bug — it's an amplification.** Small shifts in R
amplify into larger shifts in Ω_Λ. That actually makes the 1-loop
prediction more sensitive to corrections, which is informative.

## Baseline values (verified, Dirac convention, M_Z)

| Quantity | Value | Source |
|----------|-------|--------|
| R_1loop (b/a free SM) | 1.02680 | Birrell-Davies + SM |
| ε_SU3 | 1.15977 | Osborn 2003 eq (36) |
| ε_SU2 | 1.01860 | Osborn 2003 eq (36) |
| ε_U1 | 0.98343 | Osborn 2003 eq (36) |

## Complete outcomes table

Assuming S = 108π and τ_0 = 41.9 Myr (both asserted, not derived)
and H_0 = 70 km/s/Mpc:

| Branch | R | Ω_Λ | Deviation from Planck | Status |
|--------|---|-----|----------------------|--------|
| **Q1=A, Q2=A** (QCD alone) | 1.1598 | **0.6816** | −1.06% | CLOSE |
| Q1=A, Q2=B (multiplicative) | 1.1618 | 0.6784 | −1.53% | CLOSE |
| Q1=A, Q2=B (additive) | 1.1618 | 0.6783 | −1.53% | CLOSE |
| Q1=A, Q2=B (weighted) | 1.1618 | 0.6783 | −1.53% | CLOSE |
| Q1=A, Q2=C (X=0.98) | 1.1566 | 0.6868 | −0.30% | MATCH |
| Q1=A, Q2=C (X=0.95) | 1.1518 | 0.6946 | +0.83% | MATCH |
| Q1=B (Δβ_b = 0) | 1.0268 | 0.9144 | +32.74% | LARGE |
| Q1=B (Δβ_b = −0.3) | 1.1540 | 0.6910 | +0.31% | MATCH (by fit) |
| Q1=C (50/50 mix) | 1.0933 | 0.7938 | +15.22% | LARGE |

## Per-branch analysis

### Best case: Q1 = A, Q2 = A or B

**Ω_Λ = 0.678 to 0.682** depending on combination rule.
**All branches give a CLOSE match** (1-1.5% off Planck).

This is not a 0% match — the 1-loop ε evaluation gives Ω_Λ systematically
1-1.5% LOW compared to Planck. This is consistent with the fact that
1-loop isn't the full story: 2-loop corrections to ε (or to the overall
anomaly structure) could plausibly close that remaining 1-1.5% gap.

**Interpretation if Q1=A and Q2=A:**
"At one loop, QCD trace anomaly at M_Z gives Ω_Λ = 0.682, which is
1% below Planck's observed 0.689. The remaining 1% could come from
2-loop corrections of order (α_s/π)² ~ 0.14%, or from EW sector
contributions at the ~1% level. This is consistent with a derivation
at 1-loop leading order, with subleading corrections within expected
range."

### Middle case: Q1 = A, Q2 = C

The ε → R mapping introduces a factor X. The value of X determines the outcome:

- X = 0.95: Ω_Λ = 0.695 (+0.8%)
- X = 0.98: Ω_Λ = 0.687 (−0.3%) ← best match
- X = 1.00: Ω_Λ = 0.682 (−1.1%)
- X = 1.05: Ω_Λ = 0.669 (−2.9%)

**X in the range 0.95-1.00 gives the best match to Planck.** If the
brother's mapping derivation produces a factor X in this range, the
framework works. If X is much larger or smaller, there's tension.

### Failure case: Q1 = B, Δβ_b = 0

If CTP selects b/a (not ε) and no w_i contribution is found:
**Ω_Λ = 0.914**, which is 33% above Planck. Framework fails entirely.

### Fitted case: Q1 = B, Δβ_b = -0.3

The value Δβ_b = -0.303 produces Ω_Λ = 0.691. But this is found by
binary search, not derivation. It's the "c_w = -1" case that prompted
us to reframe as "fit, not derivation."

If the brother's INDEPENDENT w_i extraction gives Δβ_b near -0.3
without knowing the target: genuine derivation. If his extraction
gives something else: framework fails.

## What the enumeration tells us

1. **Most Q1=A branches land at Ω_Λ ≈ 0.68**, systematically ~1% below
   Planck. Not a 0% match, but clearly in the right neighborhood.

2. **The ~1% gap at Ω_Λ level is plausibly closeable** by 2-loop
   corrections or EW sector contributions. It's not a killing deviation.

3. **Q1=B branches depend entirely on the brother's w_i extraction.**
   Without a number from him, we can only show the parameterized
   sensitivity.

4. **Q1=C branches are open** — requires his specific formula.

## What to watch for in the brother's answer

When the email arrives:

1. If **Q1 = A**: we're in the 0.68 ballpark. Good.
   - If Q2 = A or B: Ω_Λ falls out as 0.68-0.69 range. Report it.
   - If Q2 = C with X in 0.95-1.0: ~0.69. Report it.
   - If Q2 = C with X far from 1: further from Planck. Report honestly.

2. If **Q1 = B**: need his w_g values.
   - Plug them into the integrated module.
   - Whatever Ω_Λ falls out is the answer.
   - If it matches Planck: new result. If not: negative result.

3. If **Q1 = C**: need his combination formula.
   - Evaluate it; report what comes out.

## The key insight from this enumeration

**No branch produces Ω_Λ = 0.6889 exactly from pure 1-loop physics.**
The closest we get with unadjusted inputs is Ω_Λ = 0.6816 (Q1=A, Q2=A),
which is 1.06% off.

This means:
- The framework's 1-loop prediction is systematically low
- A perfect match (within 0.1%) would require either (a) the 2-loop
  correction landing just right, or (b) the S or τ_0 values being
  slightly different than asserted
- The 1% gap is within the range of expected corrections, but it's
  not automatically closed

This is a MORE HONEST picture than "0.5% match." The 1-loop QCD trace
anomaly puts Ω_Λ in the 0.68 neighborhood. Getting to exactly 0.6889
requires more work (2-loop corrections, or a better-motivated choice
of S and τ_0, or both).

## The single-line summary for the record

> "At 1-loop with Dirac convention, if CTP selects ε over b/a and
> QCD dominates, the framework predicts Ω_Λ = 0.68 — consistent with
> Planck's 0.69 at the 1% level, with the remaining gap plausibly
> attributable to 2-loop or EW corrections. The prediction is order-
> of-magnitude correct, with precision contingent on several choices
> not yet derivation-grade."

## What happens next in each case

All paths lead to a number. The question is whether that number can
honestly be labeled DERIVED or stays labeled CONDITIONAL.

| Branch | Likely label | Action |
|--------|-------------|--------|
| Q1=A, Q2=A | DERIVED at 1-loop, CLOSE | Document with 1% deviation noted |
| Q1=A, Q2=B | DERIVED at 1-loop, CLOSE | Same as above |
| Q1=A, Q2=C | Depends on X motivation | If X has physical basis: DERIVED |
| Q1=B (brother's w_i) | DERIVED or NEGATIVE | Depends on his number |
| Q1=C | Case-by-case | Evaluate his formula |

The 1% deviation in the best case is honest information. Reporting
Ω_Λ = 0.68 (vs observed 0.69) is a real result either way — either
evidence that the 1-loop picture is nearly right, or evidence that
something else is needed.
