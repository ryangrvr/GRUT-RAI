# Task 02 — ζ(3) transcendental check

**Date:** April 2026
**Status:** Structural consistency established; coefficient derivation deferred.

## Question

GRUT's hand-constructed C_FINAL contains `576 × ln(2) × ζ(3)` as one of
three rational terms. Does this combination (with specific coefficient
576) arise naturally from thermal physics on S⁴?

## What's established

1. **ln(2)·ζ(3) is a verified 3-loop thermal signature.** Standard
   references (Kapusta-Gale FT QFT, Arnold-Zhai 1995 QCD free energy
   at 3 loops) show this combination appearing at 3-loop in thermal
   field theory with bosons+fermions. Its presence at 3-loop is
   structurally correct — not something the hand-construction
   "invented."

2. **ζ(3) does NOT arise at 1-loop on S⁴.** The 1-loop heat-kernel
   expansion (Seeley-DeWitt) gives rational × π² terms only.
   The a_4 coefficient for various spins (scalar 1/360, fermion 11/720,
   vector 31/180) contains no ζ values — these are purely local
   curvature invariants.

3. **The coefficient 576 has several natural factorizations:**
   - `576 = 4 × 12² = 4 × (n_V_SM)²` (SM gauge boson count)²
   - `576 = 24²` (SU(5) adjoint dimension; SM has 12 gauge bosons but
     fermion generators raise to 24 in unified picture)
   - `576 = 2⁶ × 3²` (combinatorial factor from specific diagram
     topology)

   Only an explicit 3-loop calculation would determine which (if any)
   is physically correct.

## What's NOT established

1. Whether GRUT's specific coefficient 576 is derived from SM
   physics on S⁴ at 3-loop, or chosen aesthetically to match a
   target. Without doing the 3-loop calculation, this is undetermined.

2. Whether the rational combinations 99 + 2π² + 576·ln(2)·ζ(3) have
   a natural 3-loop decomposition (vacuum-bubble + gauge + fermion
   contributions) that GRUT's hand-construction was approximating.

## Honest conclusion

The transcendental STRUCTURE of C_FINAL is consistent with 3-loop
thermal field theory on S⁴. This is evidence that the hand-construction
was pulling from real physics, not pure numerology. But the specific
COEFFICIENT 576 is not derivable from this level of analysis.

Task 02 is a structural consistency check, not a derivation. It
strengthens (but does not prove) the claim that GRUT's hand-construction
captures actual physics.

## What would close this question

The same 3-loop specialist calculation needed for Step 06:

- Compute the 3-loop effective action on S⁴ with SM matter at the
  electroweak matching scale
- Extract the coefficient of E₄ (Euler density) from the finite
  part
- Check: does this coefficient have the form `A + B·π² + C·ln(2)·ζ(3)`
  with `A ≈ 99 × constant`, `B ≈ 2 × constant`, `C ≈ 576 × constant`?

If yes: GRUT's hand-construction is essentially the correct physical
result, and the specific numerical value R_hand = 1.15428 is physical.

If no: GRUT's hand-construction produced the right transcendental
structure (consistent with the thermal S⁴ pattern) but with
coefficients chosen non-rigorously. The SM-derivable alternative
through ε_combined remains valid.

## Next

Task 03: Re-read Osborn 2003 paper for any higher-order (beyond 2-loop)
information. The paper states "to two-loop order" for eq (36). Check
the appendix and references for 3-loop or partial extensions.
