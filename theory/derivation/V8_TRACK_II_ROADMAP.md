# V8 Track II Roadmap — Yukawa Sector as a CTP Fixed-Point Problem

**Date filed:** April 20, 2026
**V7 status of flavor sector:** MAPPED (§29), not DERIVED.
**Milestone (6 months):** fixed-point existence check. Not fermion masses.

## Honest diagnosis of V7 §29

V7 maps Koide and CKM/PMNS as trace constraints of a 3-generation
fixed-point operator. The six-step chain is outlined. Step 1 (V7 line
1832, explicit) notes: "the multi-generation CTP variation with
off-diagonal Yukawa couplings and flavor mixing. This has not been done
in any framework, not just GRUT."

**What V7 has:**
- K = 2/3 Koide value verified to 0.005% against measured lepton masses.
- K = 2/3 proven as the Z₃-circulant trace identity to 2.3×10⁻¹⁶.
- N = 3 uniquely selected by simultaneous Koide, Ω_Λ, η_B constraints.
- CKM hierarchical eigenvalue structure explained qualitatively.
- PMNS large mixing explained qualitatively as near-degenerate eigenvalues.
- Explicit "conjecture (Spectral Koide)" labeling K = 2/3 as a trace
  theorem about self-referential 3×3 operators.

**What V7 does NOT have:**
- Explicit CTP action for the Yukawa sector in Keldysh basis.
- The `y_target,i[y]` functional for Yukawa couplings.
- The fixed-point equation `y_i = y_target,i[y]`.
- The mass matrix `M_ij` at the fixed point.
- Any eigenvalue computation.
- Numerical values for M₀ (overall scale) or θ (phase angle).
- Any connection between R = 1.15428 and flavor eigenvalues.

V7 §29 self-labels: "M₀ and theta remain undetermined — they are the
spectral data of the operator that GRUT identifies but cannot yet compute."

## What Track II is (and isn't)

**Is:** A program to execute steps 1-4 of the V7 §29 six-step chain.

**Isn't:** A program to predict the electron mass. Don't promise that.

The deliverable at 6 months is a yes/no answer to a single question:
**Does a multi-flavor fixed point exist for the SM Yukawa sector under
the CTP constitutive equation?** If yes, Track II proceeds to eigenvalue
extraction. If no, Track II terminates honestly.

## Step II.1 — Single-generation CTP Yukawa action (flat space)

Start as simple as possible:
- One generation, one Yukawa coupling y.
- Flat space, not S⁴ (scope correction carried over from brother's earlier audit).
- 1-loop CTP effective action with one fermion + Higgs.

Concrete deliverables:
1. Write the Keldysh-basis Yukawa Lagrangian with sources y_r, y_a.
2. Compute Γ_CTP[y_r, y_a] to 1-loop with SM fermion content at one
   generation.
3. Extract y_target(y) = y − (dF/dy)⁻¹ F[y] where F[y] is the CTP
   equation-of-motion residual.
4. Find y_FP such that y_FP = y_target(y_FP).
5. Check: is y_FP ≠ 0? (A trivial fixed point y_FP = 0 terminates the
   track — means Yukawa isn't dynamically selected.)

Required inputs:
- Schwinger-Keldysh formalism for fermionic fields (standard, well-known).
- 1-loop Yukawa β-function in CTP (extension of Osborn local-coupling
  framework from gauge to Yukawa sector).
- Numerical root-finding for the fixed-point equation.

Difficulty: **Medium.** 1-loop CTP β-functions for Yukawa couplings
exist in the literature (finite-T QFT community). Adapting them to the
GRUT constitutive-equation framework is straightforward manipulation,
not new physics.

## Step II.2 — Three-generation extension

Only pursue if Step II.1 finds a non-trivial fixed point.

Deliverables:
1. Keldysh Yukawa Lagrangian with full Y_ij matrix (3×3 complex).
2. Multi-generation β-function 3×3 matrix: β_Y_ij(Y).
3. Fixed point condition: Y_ij = Y_target,ij(Y).
4. Numerical root-finding in 18-dimensional real parameter space
   (3×3 complex = 18 real).
5. Extract eigenvalues of Y^FP † Y^FP × v².
6. Compute K = (Σ m_i)² / (3 Σ m_i²) and compare to 2/3.

Difficulty: **Hard.** The 18-dim fixed-point search is nontrivial;
physical constraints (unitarity of CKM) reduce the search space but
not trivially.

## Step II.3 — Connection to R and S⁴ topology (IF Step II.2 succeeds)

The V7 conjecture: the Yukawa fixed-point structure inherits
constraints from the same S⁴ topology that produces R_anomaly = 1.15428.

Deliverables:
- Does the Yukawa 1-loop CTP effective action on S⁴ (rather than flat
  space) give the same fixed point? If yes, the Koide trace constraint
  inherits from S⁴ topology via the same boundary conditions
  f(1) = 1, f(2) = 0.
- Numerical test: compute the Yukawa fixed-point eigenvalue ratio on
  S⁴ vs flat space. If they differ, the S⁴ topology contributes
  nontrivially to flavor structure.

Difficulty: **Very hard.** S⁴ Yukawa CTP with three generations is at
the research frontier.

## What Track II does not attempt to predict

- Electron mass absolute value (M₀ scale). This requires the
  normalization of the Yukawa fixed point, which is a separate
  problem.
- Top mass. Same.
- θ (the overall Koide phase). This is a spectral invariant that may
  or may not be forced by Z₃ symmetry.
- Neutrino mass scale (requires extension to Dirac/Majorana structure).

What Track II CAN predict (if all three steps succeed):
- The trace ratio K = 2/3 as a theorem, not an observation.
- The CKM hierarchy pattern (NOT the mixing angles, but the pattern
  of large vs small).
- The PMNS near-degeneracy pattern.
- Whether R = 1.15428 and the Yukawa eigenvalues are connected.

## Rejected short-cuts (do not waste cycles)

- **Fitting y_target,i to give K = 2/3 by construction.** That's not a
  derivation. The fixed point must be found independently and K = 2/3
  must fall out.
- **Choosing a specific 3×3 parametrization that makes the algebra
  easy.** The 18-dim search is the honest space; reduce it only with
  physical constraints (CKM unitarity, gauge invariance).
- **Predicting the electron mass at 6 months.** Not the milestone.
  Fixed-point existence is.

## Milestone schedule

| Month | Deliverable | Decision point |
|:---|:---|:---|
| 2 | Single-generation CTP Yukawa action written | is the algebra tractable? |
| 4 | y_FP computed for one generation | is y_FP ≠ 0? |
| 6 | 3-generation β-function matrix written | does a fixed-point exist in 18D? |
| 9 | K = 2/3 check at fixed point | does the trace identity emerge? |
| 12 | S⁴ topology test | is Koide inherited from S⁴? |

**The honest milestone at 6 months is a yes/no.** If yes, Track II is
an active research program. If no, Track II is a closed negative like
Track VII V7's Ω_dm — documented and shelved.

## Ledger

**15 corrections caught. 0 hallucinations.**

The scoping above replaces any previous Track II planning that promised
specific masses or used "we'll predict the electron mass" framing.
What we can honestly promise is the fixed-point existence check. That
is achievable. That is worth 6 months.
