# L0 ACCESS BRIDGE — OWNER RULING 01

**Date:** 2026-09-29 · Given in session, on `L0_ACCESS_BRIDGE_01.md` (commit `ba3cc59`; Issue #2
comment `5898544714`). Recorded from the owner's words; any misstatement is corrected by owner
edit, not defended.

**The bridge formulation is ACCEPTED as the working post-EA-0 gate. No terminal is assigned.**

## 1. Independent verification: AUTHORIZED (narrow)

- **Output:** `L0_ACCESS_BRIDGE_VERIFICATION_01.md`.
- **Verdict scale:** VERIFIED / VERIFIED-WITH-NARROWER-SCOPE / IMPORTED-STANDARD / NOT
  ESTABLISHED / COUNTEREXAMPLE.
- **Scope:** only claims that could change the bridge outcome. No new physics model, no numerical
  member campaign, and no attempt to force a terminal.

**The targets:**
- **A. Geometry path** K → G_AA(ω) → recovered geometry, with its exact scope. **Geometry recovery
  from K with declared access sets ≠ derivation of the access sets.** Do not turn "the classical
  substrate already reaches geometry" into "geometry is fully derived from Level-0 without access
  input".
- **B. Linear classical collapse**, item by item: observability; controllability; the
  invariant/Krylov structures; Jacobian support; the future-readout quotient. **Intended
  statement:** these structures are functions of K and the declared output/input locations, not of
  the current state x. The state selects values and orbits within them.
- **C. Seed-reduction qualification.** The allowed version:

  > Within the declared Level-0 coordinate-observable class, the P-6-style "which operator within
  > a site?" freedom is absent or collapsed: the retained observable is the site's real
  > coordinate and its declared response structure. The remaining localization choice is which
  > site/set of sites is accessed. If arbitrary nonlinear local outputs g(x_i) are admitted,
  > output-map choice may reappear and must be priced rather than silently identified.

  Verify which observable class the earned records actually authorize.

## 2. Value versus structure: OWNER RULING (binding for the bridge)

> **Continuous state-dependent reweighting of a fixed support does NOT count as structural
> access.**

- CL-6 and CL-7 do not establish DIRECT-CLASSICAL access merely because their weights or
  Gramians vary with x₀.
- **A value/weight change** is, for example:
  - J_ii(x) = −K_ii − 12βx_i², which varies continuously while the off-diagonal support stays
    fixed;
  - a variational Gramian that changes continuously in magnitude while keeping the same rank and
    nullspace.
- **A change counts as structural only when an invariant structural object changes:**
  - observability rank;
  - accessibility/controllability rank;
  - nullspace / unobservable subspace;
  - equivalence class of indistinguishable states;
  - exact support/adjacency;
  - dimension of the accessible quotient;
  - another preregistered discrete/invariant structural change.
- **Do not manufacture structure by thresholding a small continuous weight.** Any threshold needs
  a separately justified physical criterion.
- **Binding:** access structure ≠ geometry/metric values carried on that structure. A continuous
  change in weights may change the recovered metric geometry; that still does not mean access
  changed.

## 3. The L0-1c rank-drop theorem task: AUTHORIZED, in sequence

This runs only after the verifier confirms the CL-3/CL-4/CL-5 definitions. It is theorem-only (no
trajectory simulation campaign), and its output is `L0_ACCESS_RANKDROP_THEOREM_01.md`.

- **Target:** exactly the earned L0-1c class, V = ½xᵀK_bx + βΣx_i⁴ and
  f = −K_bx − 4βx^{∘3}, whose off-diagonal support is already known to be state-independent.
- **The question:**

  > Can the nonlinear observability or accessibility structure lose rank at particular states
  > even though the interaction graph never changes?

- **Observability leg.** For h_i(x) = x_i, the Hermann–Krener codistribution. Determine:
  - the generic rank;
  - whether rank-deficient states exist;
  - the algebraic drop set;
  - whether a drop occurs for the actual C1-a bath chain K_b;
  - whether the drop changes the indistinguishability class.
- **Accessibility leg.** The autonomous model has **no control input.** Do not silently add one.
  An injected g_i is an additional probe/input structure unless it is explicitly a diagnostic, and
  that pricing goes on the face. CL-4 may not carry CL-3's evidentiary weight.
- **Outcomes:** RANK-CONSTANT / RANK-DROP-EXISTS / CLASS-SPLIT / PROBE-DEPENDENT / UNFORMULABLE.
  A rank drop is a candidate structural access change **only if it changes the exact
  distinguishability structure**, not merely a numerical conditioning measure.

## 4. Lift table: highest-priority verification corrections

- **LF-1 Koopman.** Distinguish three things: the canonical composition operator on a chosen
  function algebra; an L²(μ) realization, which needs a measure or function-space choice; and
  unitary evolution, which needs an invariant measure. **Do not make "Koopman is noncanonical"
  broader than the actual choice dependence.**
- **LF-2 Liouville.** Distinguish the mathematical representation (density evolution is standard
  once a distribution is part of the description) from added physical state content (a single
  deterministic trajectory supplies no probability measure).
- **LF-4 dilation.** Replace "the first step required" with:

  > a conservative dilation is one possible route to a Hamiltonian structure, but the record does
  > not select a unique dilation.

  **The relevant fact is non-uniqueness.** Also replace "the first-order dissipative flow has no
  symplectic structure" with:

  > no canonical symplectic structure has been earned from the present Level-0 data.

- **LF-5/LF-6 and ħ (mandatory).** An abstract noncommutative CCR/CAR lift can often be written
  after choosing a normalization and statistics, **without deriving the physical value of ħ.**
  *Identifying* that algebra with physical quantum mechanics needs the quantum action scale, which
  GRUT has not derived. **Do not say that writing any CCR/CAR algebra literally requires a derived
  physical ħ.** The bridge question is whether the *physical* lift is forced.
- **LF-6 statistics.** Verify separately the existence and canonicity of bosonic and of fermionic
  second quantization, and whether the same classical contraction data select between them. If
  both survive, that supports NONUNIQUE-LIFT unless earned structure selects the statistics. **Do
  not presuppose that they represent the same physical degree of freedom.**
- **Modular flow.** State the exact hypotheses of the triviality claim.

## 5. Do not preselect Route C

| Route | Meaning |
|---|---|
| **A** | Classical structural objects reduce repeatedly to generator structure (→ S-5). |
| **B** | The L0-1c observability theorem finds genuine state-dependent rank changes: a direct classical state/access mechanism. |
| **C** | No direct classical structural access survives, and no unique physical lift is forced. |

The verification and the rank-drop theorem are what distinguish them.

## 6. No numerical physics

- **Permitted:** exact algebra; theorem proofs; symbolic manipulation as proof support; small
  abstract counterexamples or controls, clearly labelled as mathematics.
- **Not permitted:** parameter sweeps marketed as results; EA-1; reopening gravity; S-5
  execution; new empirical claims.

## 7. Sequence and HARD STOP

1. The independent bridge verification.
2. Additive corrections, if required.
3. If the CL-3 definitions survive, the L0-1c rank-drop theorem.
4. Present both records.
5. **HARD STOP** for the owner's ruling on the bridge terminal and Route A/B/C.

**No bridge terminal is assigned before those two records.**

> The remaining direct classical opportunity: **does the L0-1c nonlinear flow cause exact
> observability/indistinguishability rank changes?** If no, the native classical access route is
> looking genuinely thin. If yes, we finally have state-dependent structure without importing
> quantum algebra.
