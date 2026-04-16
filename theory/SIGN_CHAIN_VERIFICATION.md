# The Sign Chain: What the Brother Must Verify

## Why this document exists

The simulated Q2 conclusion — "perturbative Osborn moves R the wrong
direction" — rests on a four-step sign chain. Each step is a place where
a convention error or missed minus sign in integration by parts can
flip the final answer.

Before we commit to "HONEST NEGATIVE" as the status of GRUT's
cosmological sector, the real brother needs to verify this chain
explicitly. Sign errors in multi-step anomaly calculations are
notoriously common and neither Ryan nor I are equipped to guarantee
this without his check.

---

## The chain, link by link

### Link 1: Δb̄ > 0 from unitarity

**Claim:** At a CBZ fixed point (and by extension in perturbative QCD
near it), the shift in the BoxR anomaly coefficient b̄ from UV to IR
is strictly positive.

**Source:** Prochazka-Zwicky 2017, arXiv:1703.01239, Section 2.5.

**Is this a theorem or an estimate?** 
A **theorem.** Follows from positivity of the ⟨ΘΘ⟩ two-point function
where Θ = (β/2)[G²]. Unitarity forces the sign.

**Check the brother needs to do:**
Verify that the theorem applies to our situation (SM QCD away from
CBZ) as well as the CBZ regime. If unitarity only guarantees Δb̄ > 0
at CBZ and we're far from CBZ, the sign is not locked.

**Confidence this link holds: HIGH** (if we're in the regime where
PZ's theorem applies).

---

### Link 2: Sign of w_i from b̄'s sign

**Claim:** If Δb̄ > 0, then the w_i coefficients in Osborn 1991 eq (31)
have a specific sign pattern.

**Source:** Follows from Osborn 1991 eq (31): 8∂_i β_b = χ^g_ij β^j − L_β w_i.

**The step:** If Δb̄ > 0 (by unitarity) and we can write b̄ in terms
of w_i via the consistency relations, then the sign of b̄'s flow
constrains the sign of w_i.

**Where sign errors can creep in:**
- The relation between b̄ (BoxR coefficient) and w_i (coupling-space
  vector) involves integration by parts on curved spacetime. IBP
  picks up signs from ∇_μ acting on Christoffel symbols.
- There's a sign convention in defining w_i that differs between
  Jack-Osborn 1990 and Osborn 1991.
- The β-function sign convention (β = +b_0 g³/(16π²) vs β = −b_0 g³/(16π²))
  affects which direction the flow goes.

**Check the brother needs to do:**
Work through the explicit derivation of w_i from b̄ using ONE
consistent sign convention throughout. Verify the overall sign
is what my simulation claimed (positive w_g for QCD with the
"b̄ > 0 implies positive w" reading).

**Confidence this link holds: MODERATE.** This is where I'm most
likely wrong. The IBP algebra has multiple sign-flipping steps.

---

### Link 3: Sign of L_β w_i in the Osborn equation

**Claim:** Given the sign of w_i from Link 2, the Lie derivative
L_β w_i has a specific sign in 8∂_i β_b = χ^g_ij β^j − L_β w_i.

**The step:** L_β w_i = β^j ∂_j w_i + w_j ∂_i β^j. The sign depends on:
- Sign of β_j (negative for asymptotically free like QCD, positive for
  not-asymptotically-free like U(1))
- Sign of ∂w/∂g (depends on how w scales with g)

**For QCD specifically:**
- β_g3 < 0 (asymptotic freedom at high energy)
- w_g3 ∝ 1/g (from the structure of Osborn 2003 eq 35)
- ∂w/∂g < 0 (because w decreases as g increases)
- β × ∂w/∂g = (neg) × (neg) = POSITIVE

So −L_β w_g3 has a NEGATIVE contribution from this piece (because
of the minus sign in front of L_β in Osborn eq 31).

**Where sign errors can creep in:**
- The "Lie derivative" convention: L_X Y = X^i ∂_i Y or (X^i ∂_i Y − Y^i ∂_i X)?
- Jack-Osborn 1990 uses a specific convention that differs from some
  other references.
- The sign of "flow UV → IR" vs "flow IR → UV" — the integration
  direction matters.

**Check the brother needs to do:**
Write out L_β w_i explicitly with one Lie derivative convention.
Verify the sign of −L_β w in the RHS of Osborn eq (31) for QCD
at M_Z.

**Confidence this link holds: LOW-MODERATE.** Lie derivatives on
coupling space with convention choices are a classic source of
sign errors.

---

### Link 4: Sign of ΔR given the sign of Δβ_b

**Claim:** If Δβ_b > 0 (b becomes less negative, i.e., |b| decreases),
then R = |b/a| decreases.

**The step:** R = |b/a|. If |b| decreases and a is roughly unchanged,
R decreases.

**This one is clean** — just arithmetic. No IBP, no conventions, just
the definition of R.

**But** — what if Δβ_a is NOT negligible? Then R could increase even
if |b| decreases, provided a decreases faster.

**Check the brother needs to do:**
Determine whether β_a (Weyl² coefficient) shifts comparably to β_b
under the same integrated flow. At leading order Osborn's consistency
doesn't constrain β_a via a w_a term (Osborn himself notes this in
eq 31 discussion). But at 2-loop and beyond, β_a can shift.

**Confidence this link holds: HIGH** (for the leading-order statement;
moderate if 2-loop matters).

---

## The bottom line

**Links 1 and 4 are solid.** Links 2 and 3 are where sign errors
commonly occur. My simulation followed through the chain with one
consistent set of conventions and got "ΔR < 0, wrong direction," but
with two intermediate links that involve multiple sign-flipping
operations (IBP, Lie derivatives on coupling space, beta function sign
conventions), I cannot rule out that a careful redo gives "ΔR > 0,
right direction."

## What the brother needs to explicitly verify

For each link in the chain, a specific check:

**Link 1:** Does PZ's unitarity theorem (Δb̄ > 0) apply for SM QCD
at M_Z, or only at CBZ-FP?

**Link 2:** Using Jack-Osborn 1990 section 4 conventions, does
Δb̄ > 0 imply w_g > 0 or w_g < 0 for asymptotically free gauge
theories?

**Link 3:** With Jack-Osborn's Lie derivative convention, what is
the sign of −L_β w_g in Osborn eq (31) for QCD at M_Z?

**Link 4:** At 1-loop, does Osborn's consistency condition constrain
β_a in a way parallel to its constraint on β_b? (If yes, Δa and Δb
could cancel in the R ratio. If no, R's direction is determined by
β_b alone.)

## What changes depending on his answer

### If he confirms the sign chain (ΔR negative)
- Cosmological sector: HONEST NEGATIVE
- Mechanism documented as perturbatively closed
- Book framing: decoherence paper + "cosmological sector open"

### If he finds a sign error in Link 2 or 3 (ΔR positive)
- The integrated Osborn route is still in play
- Run his actual w_g values through the pipeline
- Whatever Ω_Λ falls out is the answer — could be close to Planck,
  could be anything
- Framework status returns to CONDITIONAL pending numerical result

### If he finds that β_a shifts comparably at 2-loop (Link 4 complicates)
- The sign argument for R becomes subtle
- We'd need the full Δβ_a calculation alongside Δβ_b
- This is more work than 1-loop Osborn

## The explicit request for the brother

Please, when you work through Q2, don't just give me the w_g numbers.
Give me a paragraph confirming:

1. "Unitarity applies to SM QCD at M_Z: YES/NO/with-caveats"
2. "w_g sign for QCD from Jack-Osborn section 4 with their conventions: +/-"
3. "Sign of −L_β w_g in Osborn eq (31) at M_Z: +/-"
4. "Does β_a shift at this order: YES/NO, approximately by how much"

With those four statements, we know exactly which link locks and which
might flip. The numerical w_g values are important but the sign chain
verification is what lets us commit to "HONEST NEGATIVE" or "STILL IN
PLAY" honestly.

---

## Why Ryan is right to flag this

The four-link chain is exactly where I (Claude, simulating the brother)
am most likely to slip. I can write out the logic coherently, but
without hands-on experience with Osborn-style calculations, I can't
guarantee the conventions match between Jack-Osborn 1990, Osborn 1991,
Osborn 2003, and Prochazka-Zwicky 2017. Those four papers use slightly
different notation in places, and the small differences compound across
four sign-flipping operations.

The real brother, working through the papers himself, will catch any
slip I made. Until he does, the "HONEST NEGATIVE" conclusion is
provisional. It's the most likely outcome, but not locked.

**The honest framing to commit to TODAY:**

"Simulated analysis suggests the perturbative Osborn route closes in the
wrong direction (unitarity-consistent shift moves R down, not up). This
is a four-step sign chain that requires verification by a working QFT
theorist. Conclusion is PROVISIONAL pending that verification. If the
sign chain confirms: cosmological sector is an honest negative. If a
sign error is found in Links 2 or 3: the route is still open and we run
the integrated pipeline with the real w_g values."

That's the honest state. Not locked, not dismissed.
