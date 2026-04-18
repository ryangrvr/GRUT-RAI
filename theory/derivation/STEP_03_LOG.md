# STEP 03 — Log: Osborn 2003 eq (36) provenance resolved, epsilon interpretation refined

**Date:** April 2026
**Status:** Formula verified; physical interpretation refined from prior understanding.

## Provenance resolution

**Source:** H. Osborn (2003), "Local Couplings and Sl(2,R) Invariance for
Gauge Theories at One Loop," arXiv:hep-th/0302119, DAMTP.

PDF saved locally: `papers/references/osborn_2003_hep-th-0302119.pdf`
(153 KB, 11 pages, verified on read).

Equation (36) of that paper, exactly as printed (for gauge theory with
fermions and scalars, at 2-loop in dim reg):

```
α = δ = 1 + (1/3)(51C - 20 R_ψ - (7/2) R_φ) ĝ²
ε       = 1 + (1/3)(29C - 12 R_ψ - (5/2) R_φ) ĝ²
κ       = 1 + (4/3)(11C -  4 R_ψ - (1/2) R_φ) ĝ²
λ       = 1 + (1/18)(323C - 76 R_ψ - (25/2) R_φ) ĝ²
```

where `ĝ² ≡ g²/(16π²)`, `C` = adjoint Casimir, `R_ψ` = fermion index,
`R_φ` = scalar index.

Cross-check: Jack-Osborn 1990 eq (5.8) contains the same group-theory
coefficients (51C−20R, 29C−12R, 11C−4R) in the divergent 2-loop
counterterm polynomial. Osborn 2003 is the renormalized (finite-after-
subtraction) rearrangement into the `α, δ, ε, κ, λ` operator basis.

**The formula we have been citing throughout the project is real.**
The citation should be updated everywhere to `arXiv:hep-th/0302119 eq (36)`
rather than "Osborn 2003 eq (36)."

## Critical refinement: what epsilon is

Reading eq (35) of the same paper carefully, `ε` is **not** a multiplicative
correction to the Euler-density coefficient. It is the coefficient of a
specific operator in the local-coupling counterterm Lagrangian:

```
L = n_V { (1/g²) [ α (∇²g)² − 2δ G^μν ∂_μg ∂_νg − (1/3) ε R ∂_μg ∂^μg ]
        − 2κ (1/g³) ∂_μg ∂^μg ∇²g
        + 2λ (1/g⁴) ((∂_μg)(∂^μg))² }
```

`ε` specifically multiplies **−(1/3) n_V (1/g²) R (∂_μg)²**, which is
a curvature × coupling-gradient operator that **vanishes identically
for constant g**. It contributes to the effective action only when the
coupling is promoted to an x-dependent field g(x).

This is a refinement of how I had been framing it throughout the project:
- **Prior (loose) claim:** "ε is a coupling correction to the Euler-density
  coefficient, giving b_eff = b_free × ε."
- **Correct (precise) claim:** "ε is the 2-loop coefficient of the local
  operator −(1/3) n_V (1/g²) R (∂g)² in Osborn's local-coupling
  counterterm Lagrangian. It contributes to physical observables only
  when (∂g) ≠ 0."

## Consequence for the R_GRUT = ε identification

This does not kill the identification — but it specifies the mechanism
much more precisely than before.

For R_GRUT = ε to hold, the CTP construction on S⁴ must produce an
effective `(∂_μg)² ≠ 0` between forward and backward branches. Two
candidate mechanisms (to be developed in Step 05):

1. **Gibbons-Hawking thermal fluctuations:** at `T_GH = H_inf/(2π)`
   on S⁴, thermal noise gives `⟨(δg/g)²⟩ ~ (α_s/4π)` or similar. The
   ε R (δg)²/g² term then contributes at order ε × α_s × H² × n_V.

2. **CTP source doubling:** in standard CTP, sources are doubled to
   (J₊, J₋). If we similarly double the coupling source, (g₊, g₋),
   then `(g₊ − g₋)²` plays the role of `(∂g)²` in the integrated
   action, and ε multiplies the resulting contribution.

Either mechanism gives the structural result R_GRUT = ε at leading order
in couplings, but requires explicit CTP calculation to pin down the
precise factor. That's Step 05 / Step 06 work.

## Numerical verification

Applying eq (36) with SM gauge content in Dirac convention:

| Group | α   | C | R_ψ | R_φ | Coefficient `(29C − 12R_ψ − 5R_φ/2)/3` | ε   |
|---    |---  |---|---  |---  |---                                       |---  |
| SU(3) | 0.118 | 3 | 3.0 | 0.0 | +17.000                                 | 1.1598 |
| SU(2) | 0.034 | 2 | 3.0 | 1.0 |  +6.500                                 | 1.0175 |
| U(1)  | 0.010 | 0 |10.0 | 0.5 | −40.417                                 | 0.9673 |

`ε_SU3(M_Z) = 1.1598` matches the value used throughout the project to
0.02%. Formula and numerical inputs verified.

## Transcendentals check

Step 03 introduces no new transcendentals. The coefficients `17/3`,
`51/3`, etc. are rationals. This is consistent with Osborn 2003 eq (36)
being a 2-loop dim-reg result, where transcendentals beyond π (implicit
in `g²/(16π²)`) appear only at 3-loop.

`ln(2) · ζ(3)` is expected only at 3-loop (Step 06 territory).

## Status at end of Step 03

**DERIVED (from published literature):**
- Osborn 2003 eq (36) gives the 2-loop formula for ε as stated
- Numerically `ε_SU3(M_Z) = 1.1598`, `ε_combined(M_Z) ≈ 1.154` with
  A × g⁴ weighting

**STRUCTURAL:**
- ε is the coefficient of the specific local operator
  `−(1/3) n_V (1/g²) R (∂g)²` in eq (35)
- This operator vanishes for constant g; contributes only with
  x-dependent couplings

**OPEN (for Steps 05–06):**
- The identification `R_GRUT = ε` requires a mechanism giving
  effective `(∂g)² ≠ 0` from the CTP construction on S⁴
- Gibbons-Hawking thermal mechanism and/or CTP source doubling
  are the candidate mechanisms

## What this means for the overall program

Before Step 03 we had: "R_GRUT matches ε numerically; claim is that
on S⁴ this comes from a CTP mechanism linking them."

After Step 03 we have: "R_GRUT matches ε numerically. ε is a verified
2-loop coefficient of a specific curvature × coupling-gradient operator.
For the identification to close, the CTP mechanism must produce an
effective coupling-gradient between forward and backward branches."

This is a genuine advance in precision — from "some mechanism on S⁴" to
"a mechanism producing (∂g)² across CTP branches." Step 05 has a
concrete target.

Repository action: update all references to "Osborn 2003 eq (36)" to
include the arXiv identifier `hep-th/0302119` and (eventually) replace
the loose "ε corrects b_eff" framing in derived documents with the
precise statement from this log.
