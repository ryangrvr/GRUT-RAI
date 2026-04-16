# Osborn 2003 ε Coefficients Evaluated for the Standard Model

## Status

Steps 1-3 of the brother's calculation done. Step 4 (ε → w_g mapping via
consistency relations) flagged as requiring his input.

## Equation (36) from Osborn 2003 (hep-th/0302119)

The one-loop coupling-dependence of the local effective action for a gauge
theory includes the term:

    L ⊃ -(1/3) ε R ∂_μ g ∂^μ g / g²

with (at 1-loop, with ĝ² = g²/(16π²)):

    ε = 1 + (1/3)(29 C - 12 R_ψ - (5/2) R_φ) × ĝ² + O(ĝ⁴)

where:
- C = Casimir of the adjoint representation (C_A)
- R_ψ = sum over Weyl fermions of T(R_f) with tr(t^a_ψ t^b_ψ) = -δ^ab R_ψ
- R_φ = sum over complex scalars of T(R_s)

## SM Group Theory Data

### SU(3)_c (QCD)
- C = C_A(SU(3)) = 3
- R_ψ: 3 generations × [Q_L (2 Weyl in fund) + u_R (1 Weyl in fund) + d_R (1 Weyl in fund)]
  = 3 × (2·(1/2) + (1/2) + (1/2)) = 3 × 2 = **6**
- R_φ = 0 (Higgs is color singlet)

### SU(2)_L (weak isospin)
- C = C_A(SU(2)) = 2
- R_ψ: 3 generations × [Q_L (3 colors × 1 doublet) + L_L (1 doublet)]
  = 3 × (3·(1/2) + (1/2)) = 3 × 2 = **6**
- R_φ: 1 Higgs doublet = **1/2**

### U(1)_Y (hypercharge)
- C = 0 (abelian)
- R_ψ = Σ(Y²) over all Weyl fermions
  Per generation:
    Q_L (6 Weyls × Y=1/6): 6 × 1/36 = 1/6
    u_R (3 Weyls × Y=2/3): 3 × 4/9 = 4/3
    d_R (3 Weyls × Y=-1/3): 3 × 1/9 = 1/3
    L_L (2 Weyls × Y=-1/2): 2 × 1/4 = 1/2
    e_R (1 Weyl × Y=-1): 1
    Total per gen: 1/6 + 4/3 + 1/3 + 1/2 + 1 = **10/3**
  3 generations: **10**
- R_φ: Higgs doublet with Y=1/2, 2 complex components × (1/2)² = **1/2**

## Evaluated ε Coefficients

| Group | C | R_ψ | R_φ | A = (1/3)(29C - 12R_ψ - (5/2)R_φ) | Sign |
|-------|---|-----|-----|-----------------------------------|------|
| SU(3)_c | 3 | 6 | 0 | **+5** | positive |
| SU(2)_L | 2 | 6 | 1/2 | **−61/12 ≈ −5.083** | negative |
| U(1)_Y | 0 | 10 | 1/2 | **−485/12 ≈ −40.417** | negative |

where ε = 1 + A × g²/(16π²).

## What these numbers mean

The ε coefficient encodes how the R · ∂g · ∂g term in the 1-loop effective
action depends on the gauge coupling. The sign pattern:

- QCD: positive (gauge contribution 29·3 = 87 beats fermion −12·6 = −72, net +15/3 = +5)
- EW: negative (fermion/hypercharge contribution dominates gauge)

## What's still needed (brother's step)

Derive w_g_i from ε_i via the Weyl consistency relations in Osborn 1991:

1. Start from L in eq (35) of Osborn 2003 (scheme-dependent combination)
2. Apply integration-by-parts: R ∂g ∂g ↔ □R (g) ↔ ∂g (□R) terms
3. Combine with the other coefficients α, δ, ε, κ, λ from eq (36)
4. Apply [Dσ, Dσ'] = 0 from Osborn 1991 eq (30)
5. Extract the scheme-independent combination L_β w_i

The result is w_g for each SM gauge coupling, which feeds directly into
the integrated Osborn equation already implemented in osborn_integrated.py.

## Handoff

When w_g_i values arrive, plug into grut/foundation/osborn_assembly.py via:

    compute_omega_lambda_from_inputs(c_w_scalar=?, c_w_dirac=?, c_w_vector=?)

Or directly into osborn_integrated.py via the c_w_gauge parameter.

## References

- H. Osborn, "Local Couplings and Sl(2,R) Invariance for Gauge Theories at
  One Loop," hep-th/0302119 (2003). Equation (36) above.
- I. Jack, H. Osborn, "Analogs of the c-theorem for Four Dimensional
  Renormalisable Field Theories," Nucl.Phys. B343 (1990) 647. Sections 3-4.
- H. Osborn, "Weyl consistency conditions and a local renormalisation group
  equation," Nucl.Phys. B363 (1991) 486. Equations (29)-(31) define w_i.
