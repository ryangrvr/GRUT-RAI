# What Today Actually Accomplished

## Before today (morning state)

GRUT's cosmological constant prediction rested on R = 1.15428.

- **Origin:** Mathematica notebook that constructed hand-chosen functions
  A(x) and B(x), took their Laurent series, and read off coefficients whose
  ratio gave 1.15428.
- **Justification:** Presented as "3-loop CTP anomaly on de Sitter S⁴."
- **Auditability:** None. The integers in the expressions (99, 576·ln 2·ζ₃,
  etc.) didn't trace to Feynman diagram counting or any identifiable
  physics calculation.
- **Falsifiability:** None. No one could verify or refute the specific value.

Status: black-box constant.

## After today

GRUT's cosmological constant prediction rests on one undetermined physical
quantity with a precise definition and extraction procedure.

- **R_1loop = 1.027** is verified from Birrell-Davies 1-loop trace anomaly
  coefficients for the Standard Model field content. This piece is
  independently checkable from published physics.
- **The gap is quantified:** 12.5% between R_1loop = 1.027 and the value
  required (~1.15) to match the observed Ω_Λ = 0.689.
- **The mechanism is named:** the integrated Osborn w_i term in the
  consistency condition 8 ∂_i β_b = χ^g_ij β^j − L_β w_i. Confirmed as
  the published method by Prochazka-Zwicky 2017.
- **The specific coefficient is identified:** c_w, the coupling dependence
  of the □R anomaly coefficient at 1-loop.
- **The paper it lives in is identified:** Jack-Osborn, NPB 343 (1990),
  Section 4 — with Osborn (2003), hep-th/0302119 as a more direct reference.
- **The test is precise:**
  - If c_w ≈ −1: prediction derived from standard physics
  - If c_w ≈ +1: mechanism fails in a specific documented way
  - If c_w is scheme-dependent at leading order: framework is scheme-sensitive

Status: one specific calculation by one physicist with one paper can resolve it.

## The transformation

From: "Trust this number"
To:   "Here's the specific calculation that determines whether this number
       is right."

The answer is still unknown. The question is now precise.

## What's verified along the way

- 1-loop verification passed exactly: a_SM = 283/120, b_SM = -3487/1440,
  R_1loop = 3487/3396 = 1.02680.
- Single-scale Osborn shift is negligible (~0.01%) — a real calculation that
  confirms the integrated mechanism is necessary, not a single-scale effect.
- Prochazka-Zwicky 2017 validates our integrated approach (their equation 38
  is our integration).
- The w_i term is the unique source of differential shift between Δa and Δb.
  Without it, R doesn't move.
- The sign constraint (Δb̄ > 0 by unitarity, combined with Δβ_a = 2Δb̄ at
  CBZ-FP) raises a real question about whether the mechanism can push R
  in the direction GRUT needs. This question is now explicitly on the table.

## What's removed from the framework

- The 3-loop CTP construction that produced C_FINAL = 1.14021×10⁻⁴ and
  R_ANOMALY = 1.15428 through Laurent expansion of hand-designed functions.
  That construction was not a derivation. Referring to it as such was the
  core methodological error the other Claude session identified.
- All downstream predictions that depended on those constants (Ω_Λ, η_B,
  dark matter couplings) are now labeled CONDITIONAL in the v7 appendices.

## What's kept intact

- The Diósi-Anastopoulos-Hu gravitational decoherence prediction. Independent
  of the anomaly constants. Verified to match published physics.
- The six scaling laws, the geometry kink at l = 6^(1/3)R, the isotope test,
  the material swap, the entanglement protection experiment — all follow
  from the Diósi kernel applied to extended bodies.
- Koide K = 2/3 as an observed empirical relation.
- GRUT RAI as a computation and reproducibility platform.

## The honest book framing

GRUT is a conditional framework. Its decoherence sector is real physics.
Its cosmological constant prediction is a conditional ansatz that depends
on one specific coefficient whose extraction from established QFT literature
is a well-defined, bounded calculation.

Before today that was obscured by an asserted constant dressed as derivation.
After today it's stated cleanly.

## Next step

When c_w arrives from Jack-Osborn 1990 (via the brother or any theorist with
the paper), the pipeline in `grut/foundation/osborn_assembly.py` takes the
number and produces Ω_Λ. No adjustments, no target-matching, no curve-fitting.
Whatever falls out is the answer.

If Ω_Λ matches Planck: the framework works.
If it doesn't: the framework fails in a specific way that tells us what
to investigate next.

Both outcomes are physics.
