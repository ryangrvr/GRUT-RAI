# Problem Statement for the Physicist: The w_i Question

## Context

GRUT's cosmological constant prediction depends on the ratio R = |β_b/β_a| of
trace anomaly coefficients (Euler density over Weyl²) for SM field content.

At 1-loop, summing Birrell-Davies coefficients over SM content:

    a_SM = 283/120 ≈ 2.358
    b_SM = -3487/1440 ≈ -2.422
    R_1loop = 3487/3396 ≈ 1.0268

The framework's cosmological prediction requires R ≈ 1.15 to match Planck's
observed Ω_Λ = 0.6889. The gap is about 12.5%.

## What We Learned from Osborn's Consistency Condition

Following your suggestion to use Jack & Osborn (NPB 343, 1990) and Osborn
(NPB 363, 1991) instead of 2-loop graviton Feynman diagrams, we implemented
the local RG equation. The central relation is:

    8 ∂_i β_b = χ^g_ij β^j - L_β w_i     (Osborn eq 31)

with the Zamolodchikov metric at 1-loop:

    χ^g_ij dg^i dg^j = (1/16π²)(4 n_V/g²) (dg)²

Integrating along SM gauge couplings at M_Z (α_s, α_W, α_Y), with w_i = 0,
gives Δβ_b ≈ -8.6 × 10⁻⁴. Adding the 1-loop Yukawa contribution
(tr(dΓ_i dΓ_i)/(16π²)²) gives a tiny asymmetric shift of -0.008% in R.

## The Key Finding

**At leading order with w_i = 0, the shifts Δa and Δb are proportional to the
same Zamolodchikov metric contracted with the same β-functions. They move in
lockstep. The ratio R = |b/a| barely changes.**

The equation for a is (analogously):

    8 ∂_i β_a = χ^a_ij β^j

The equation for b has the extra -L_β w_i term:

    8 ∂_i β_b = χ^g_ij β^j - L_β w_i

**The only way R shifts is through this asymmetry** — the w_i term in the b
equation that has no counterpart in the a equation.

## The Sharper Question

The w_i coefficients in Osborn eq (31) — the ones multiplying the Lie
derivative L_β w_i — what are they for the SM field content?

Jack & Osborn (NPB 343, 1990) give the general structure. The w_i are related
to the ambiguous total-derivative term (□R coefficient) in the trace anomaly.
Even though w_i is scheme-dependent, L_β w_i contracted with β^j gives a
scheme-independent contribution to the running of b.

**Can you extract the w_i coefficients for the SM at 1-loop, so we can compute
how much they shift R relative to the a equation?**

That's the calculation. If L_β w_i · β^i produces a shift at the 10% level
when integrated along the SM RG trajectory, the framework's R ≈ 1.15 has
support from established physics. If it doesn't, we know the Osborn approach
doesn't produce the needed shift and the framework either has a different
mechanism or the prediction is wrong.

## Infrastructure

The Python code is in `grut/foundation/osborn_rg.py`. It computes:
- Zamolodchikov metric at 1-loop
- β-function integrand (1/8) χ^g_ij β^j
- Integrated shift Δβ_b from g=0 to g_SM for each gauge coupling
- Comparison to the 1-loop baseline

To add your w_i result, feed the contribution L_β w_i · β^i into the
integration and the module will compute the updated R.

## What We Committed Not To Do

- No target-guided adjustments. Whatever number the w_i calculation gives,
  that's the answer.
- No fabricated coefficients. If the calculation is beyond current tools,
  we say so.
- The 1-loop verification passed exactly. The infrastructure is trustworthy.

## References

- I. Jack, H. Osborn, "Analogs for the c theorem for four-dimensional
  renormalisable field theories," Nucl. Phys. B 343 (1990) 647-688.
- H. Osborn, "Weyl consistency conditions and a local renormalisation group
  equation for general renormalisable field theories," Nucl. Phys. B 363
  (1991) 486-526. Available: https://www.damtp.cam.ac.uk/user/ho10/loc.pdf
- Birrell & Davies, "Quantum Fields in Curved Space," CUP 1982 (1-loop
  coefficients, Table 6.1).
