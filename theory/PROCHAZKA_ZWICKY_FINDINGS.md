# Findings from Prochazka-Zwicky 2017 (arXiv:1703.01239)

## HONEST HEADLINE

The GRUT Ω_Λ prediction currently has one undetermined constant.

- **Previously:** R = 1.15428 (asserted, from constructed Mathematica notebook)
- **Now:** c_w ≈ −1 (solved for by binary search to match observed Ω_Λ)

The framing is better because c_w has definite physical meaning and
a definite extraction procedure from the literature (Jack-Osborn 1990).
But the epistemic standing is unchanged: one parameter chosen to match
observation.

**What was a fit before is still a fit.** The test — unchanged — is the
independent extraction of c_w from published physics. If it comes out near
−1 with the correct sign, the prediction is derived. If it comes out near
+1 (wrong sign), the mechanism fails in a specific, documented way. Either
outcome is publishable.

## What we observed running the numbers

From `osborn_integrated.py` running c_w scan:

| c_w | R | Ω_Λ | Status |
|-----|---|-----|--------|
| +0 | 1.027 | 0.914 | No w_i, starting point |
| +0.5 | 0.963 | 1.038 | WRONG direction, getting worse |
| +1.0 | 0.900 | 1.169 | WRONG direction, "natural" value gives wrong answer |
| +2.0 | 0.773 | 1.454 | Way worse |
| −0.5 | 1.090 | 0.799 | Better |
| −1.0 | 1.154 | 0.691 | MATCH (but solved for) |
| −2.0 | 1.281 | 0.499 | Overshoots |

The "natural O(1) positive" value that was handwaved as plausible is
actually wrong by 70%. Only c_w ≈ −1 works, and that was found by
binary search.

## For the brother's review

Following the lead to Prochazka-Zwicky, I was able to extract the published PDF
and pull out the specific equations. Here's what's in the paper and what it
means for GRUT.

## The paper structurally matches our approach

**Equation (38):**
```
Δb̄ = (1/8) ∫ χ^MS_gg · (β/2)² d ln μ'
```

This is EXACTLY the integrated Osborn consistency condition we've been
implementing. The (β/2)² instead of simple β is because they're computing
the BoxR coefficient change from the ⟨ΘΘ⟩ 2-point function, where
Θ = (β/2)[G²]. That's a slight reformulation but structurally identical
to what our osborn_integrated.py does.

**Validation:** Our pipeline (sum 1-loop field content → integrate Zamolodchikov
metric contracted with β-functions along RG flow) is the right approach. PZ
confirms this is the published method.

## The explicit NNLO result at CBZ-FP

**Equation (60):**
```
Δb̄ = κ²/(7200π² N_c²) × [ 1 + 2(7/25)²κ + (5³·4231)/(3³·25⁴)κ² + O(κ³) ]
```

where κ = -3β₀/(2N_c) is the Caswell-Banks-Zaks expansion parameter.

**Problem:** This is at the CBZ fixed point, where N_f is tuned close to
11N_c/2 such that κ is small. For SM QCD at M_Z with N_f = 6, we have
κ = -7/2, which is O(1) not small — the CBZ expansion doesn't converge.

**What we CAN extract:** The NUMERICAL STRUCTURE of the calculation for a
known, controlled case. The sign is positive (Δb̄ > 0 by unitarity, stated
explicitly in the paper).

## The critical structural claim

**From line 1267-1268 of the paper:**
> "In QCD-like theories Δβ_a = 2Δb̄ + O(κ⁶)"

Here Δβ_a is the change in the Euler density coefficient (the a-theorem
quantity) and Δb̄ is the BoxR coefficient change.

**In PZ's convention:**
- "a" = Euler density coefficient (the a-theorem monotonic quantity)
- "b̄" = BoxR coefficient

**Translating to our convention:**
- Our "b" = Euler coefficient = PZ "a"
- Our "a" = Weyl² coefficient = PZ "b" (not discussed in detail in this section)
- Our "c" = BoxR coefficient = PZ "b̄"

So PZ's "Δβ_a = 2Δb̄" translates to: **Δb = 2Δc in our notation.**

## The concerning consequence (pending brother's sign/convention check)

If this relation holds generally (even approximately) for SM:

- Unitarity: Δb̄ > 0, so Δc > 0 in our notation
- PZ relation: Δb (Euler shift) = 2Δc > 0 in our notation
- Our b_1loop = -3487/1440 = -2.42 (negative)
- Δb > 0 means b becomes LESS negative, so |b| decreases
- R = |b/a| would DECREASE (if a stays roughly constant)

**This is the wrong direction for GRUT.** To reach R = 1.15 from R_1loop = 1.027
we need |b| to INCREASE, i.e., Δb < 0.

## Numerical illustration

| Δb̄ | Δb = 2Δb̄ | b_new | R_new |
|-----|---------|-------|-------|
| 0 | 0 | -2.4215 | 1.0268 |
| +0.05 | +0.10 | -2.3215 | 0.9844 |
| +0.10 | +0.20 | -2.2215 | 0.9420 |
| +0.20 | +0.40 | -2.0215 | 0.8572 |

All positive Δb̄ (required by unitarity) push R DOWN from 1.027, never up
toward 1.15.

## Possible ways out (questions for the brother)

1. **Convention check:** Am I reading PZ's conventions correctly? If their
   "a" is actually Weyl² (not Euler), the translation flips and Δa (Weyl²)
   increases with Δb̄. That would mean a_denominator increases, R decreases
   even more strongly — doesn't help.

2. **CBZ-specific vs general:** The relation Δβ_a = 2Δb̄ is stated "up to
   O(κ⁶)". In the CBZ regime this is a tight constraint. For SM QCD where
   κ is O(1), does this relation break down? If yes, could the w_i term
   dominate in a way that flips the sign?

3. **The absorptive part:** Could the CTP imaginary contribution (which
   PZ does NOT discuss) flip the effective sign?

4. **Different CTP quantity:** Could GRUT's cosmological formula actually
   involve a different combination than |b/a|? E.g., something like
   (b - c)/a or |b|^α/a^β for some CTP-specific exponents?

## What's settled

- The integrated Osborn approach is the correct published method.
- The formula at the CBZ-FP is exactly computed to NNLO.
- Δb̄ > 0 is required by unitarity.
- The relation Δβ_a = 2Δb̄ is published for QCD-like theories at CBZ-FP.

## What the brother should check

1. Confirm my convention translation (PZ "a" = our "b" = Euler coefficient).
2. Does the Δβ_a = 2Δb̄ relation extend outside the CBZ regime for SM?
3. If the sign constraint is real, what modification of the GRUT formula
   could accommodate R = 1.027 while still producing Ω_Λ near 0.69?
   - Is S = 108π the right normalization?
   - Is τ_0 = 41.9 Myr the right timescale?
   - Is f(R) = 2-R the right functional form?
   - Does the CTP formulation use |b|/a, (2-b)/a, or something else?

## References

- M. Prochazka, R. Zwicky, "On the Flow of □R Weyl-Anomaly,"
  Phys. Rev. D 96, 045011 (2017), arXiv:1703.01239
- Equation (38): integrated Osborn form
- Equation (60): NNLO CBZ result
- Line 1267: Δβ_a = 2Δb̄ relation
