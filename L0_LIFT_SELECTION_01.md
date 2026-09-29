# L0 LIFT SELECTION 01 — does any earned structure select among the surviving lifts?

> **EVALUATED 2026-09-29.** The corrections are in `L0_LIFT_SELECTION_CORRECTIONS_01.md` (LS-1 … LS-10), which govern where they conflict with this text.
> The evaluation is `L0_LIFT_SELECTION_EVALUATION_01.md`. **TERMINAL (owner ruling 02, comment `5899585621`): IRREDUCIBLE/SUPPLIED.** The D-5 ambiguity is resolved procedurally, and CONSTRAINED-NONUNIQUE is not adopted.

**STATUS: FROZEN PRE-REGISTRATION (amended per owner ruling `5899215672`, recorded in
`L0_LIFT_SELECTION_OWNER_RULING_01.md`). The freeze is this commit. NOT A RESULT.**
- **R-0 is settled.**
  - **EARNED selectors:** D-1, D-4 (narrowed) and D-5 (narrowed).
  - **CRITERION (priced only; never counted toward a terminal):** D-2, D-3, D-6 and D-7.
  - No discriminator outside D-1 … D-7 may be added.
- The identities I-1 … I-4 below are **front-run and unverified.** Independent verification
  (V-1 … V-7) precedes any evaluation. Failed identities are corrected additively and their
  dependent predictions struck.
- No new mathematics beyond identities.
- No evaluation of any discriminator.
- No empirical selectors.
- **Authority:** `L0_ACCESS_BRIDGE_OWNER_RULING_02.md` §9.
- **Date:** 2026-09-29 · **Branch:** `master-w25bu9`.

**The question (owner, verbatim):**

> Is there any earned structural discriminator that selects among the surviving lifts, or is the
> lift/formation choice an additional supplied datum?

**This gate consumes the bridge result and does not rerun it.**
- **The bridge (terminal):** NONUNIQUE-LIFT. The same contraction data support bosonic and
  fermionic extensions with the same one-particle evolution; they differ on multiparticle
  observables.
- **Binding rules:**
  - **no Standard-Model or other empirical fact enters as a selector** (the empirical firewall
    is later);
  - **death criteria are pre-registered here (§5), before any evaluation;**
  - no thresholds.

## §1 The surviving lifts (from the verified record)

| # | Lift | Algebra | Canonicity (verified) | Covers the nonlinear L0-1c flow? |
|---|---|---|---|---|
| Λ-K | Koopman / Liouville on functions, or δ-states | commutative | the composition operator is canonical; δ-states are representational | yes |
| Λ-KvN | Koopman–von Neumann on half-densities, with λᵢ = −i∂ᵢ | noncommutative (x–λ), no ħ | canonical unitary; **representational of CL-6** for access | yes |
| Λ-H | Conservative / Hamiltonian extensions: the cotangent lift H = pᵀf; Bateman; FKM baths; the Sz.-Nagy minimal unitary dilation | Poisson (quantizable with priced choices) | the cotangent lift is canonical. Sz.-Nagy is unique up to unitary equivalence (imported). Non-minimal physical baths are **not** unique | the cotangent lift: yes; the dilations: linear core |
| Λ-B | Bosonic quasi-free second quantization Γ_B(e^{−Kt}) | real one-particle space: **commutative** (Mehler/OU); noncommutative only with a **supplied complex structure** | canonical as a functor | **no:** quasi-free lifts exist canonically only for linear contractions |
| Λ-F | Fermionic quasi-free second quantization Γ_F(e^{−Kt}) | real one-particle space: **Clifford (CAR)**, noncommutative with no complex structure needed | canonical as a functor; CP for accretive K | **no** (as for Λ-B) |

## §2 Front-run identities (to be verified; stated, not evaluated)

- **I-1 (shared descent from K).** Every lift in §1 reproduces the one-particle evolution
  e^{−Kt} and hence the **earned retained-site kernel** k(τ) = e₁ᵀe^{−K_bτ}e₁:
  - Λ-B and Λ-F by construction (verified: C(t) = e^{−Kt}C₀e^{−Kt} for both, to 1e-16);
  - Λ-K and Λ-KvN because they transport classical trajectories exactly;
  - the Λ-H dilations because they reproduce the reduced dynamics by construction.

  **Consequence:** at the earned access declaration (the retained end-site identity readout) all
  lifts agree. By the banked narrow content of H-PROJ (the forest ruling §1: realizations
  indistinguishable under the complete declared accessible data are operationally equivalent at
  that interface), **they are operationally equivalent at the earned interface.**
- **I-2 (the first spectral discriminator, Λ-K/Λ-B vs Λ-F).**
  - On polynomial observables the Koopman generator of ẋ = −Kx has spectrum
    {−Σₖ nₖλₖ : nₖ ∈ ℕ} (monomials in normal coordinates; standard). This coincides with the
    bosonic Fock number spectrum.
  - The fermionic quasi-free generator has nₖ ∈ {0, 1}.
  - **The first distinguishing object is the two-quanta-in-one-mode sector** (−2λₖ present vs
    Pauli-excluded). Equivalently, the four-point / two-particle correlations: a Wick permanent vs
    a Wick determinant (the verifier's ⟨n₁n₂⟩: 0.0667 vs 0.0296).
- **I-3 (dilations are invisible at earned access).** Every Λ-H dilation reproduces e₁ᵀe^{−Kt}e₁
  exactly. They differ **only in bath observables**, which lie outside the earned access. So the
  first discriminator among dilations needs **unearned access.**
- **I-4 (the nonlinear class).** Quasi-free lifts are defined canonically only for linear
  contractions. The earned L0-1c flow (on-site quartic) has **no** quasi-free lift without a
  further (non-unique) interacting second-quantization choice. Λ-K, Λ-KvN and the cotangent lift
  cover it canonically.

## §3 Candidate discriminators drawn only from earned Level-0 structure

**Each must be ruled EARNED or CRITERION by the owner *before* it is evaluated** (§5, rule R-0).
The operator's predicted status is shown only to make the pre-registration auditable. It is not a
result.

| # | Discriminator | Source (earned?) | What it would test | Predicted status (front-run) |
|---|---|---|---|---|
| D-1 | The retained-site kernel, P_memory, P_positivity, the geometry support | L0-1a/b/c, the floor (earned) | whether any lift alters the earned predicates | **non-discriminating** (I-1) |
| D-2 | **Coverage of the whole earned class** (a lift must apply canonically to the linear **and** L0-1c nonlinear members) | L0-1c (the nonlinear class is earned). *Whether "must cover" is earned or a criterion is the owner's ruling.* | whether quasi-free lifts are excluded | **CRITERION (owner R-0).** Recorded as the quasi-free lifts' scope/price limitation. Cannot exclude them. |
| D-3 | **Classical limit / correspondence with the declared FDT noise** | L0-1e (the stochastic members are a *declared extension*, not the earned deterministic core). A correspondence principle is **not** earned | whether a lift's occupation statistics admit the classical equipartition limit that the FDT-held members use | **CRITERION (owner R-0).** Cannot select statistics. Reported as a price only. |
| D-4 | **Source passivity/accretivity compatibility** (amended A): does the lift preserve the already-earned passive/accretive contraction structure on the classical/one-particle sector from which it descends? | L0-1a passivity, R-4 accretivity (earned) | preservation of the descended contraction's passivity/accretivity | **EARNED (narrowed).** CP is reported separately as a lift-internal property, not as a selector. |
| D-5 | **Source ordering compatibility** (amended B): does the lift preserve or faithfully represent the strict Lyapunov/order structure earned in O-5, when restricted to the descended source observables? | O-5 (earned, theorem-document scope) | preservation of the O-5 Lyapunov/order structure on source observables | **EARNED (narrowed).** No lifted entropy functional is required. |
| D-6 | Commuting local net (amended C) | The fact (commuting classical site coordinates; the declared net) is earned. **Tensor-product locality of all field generators, as against graded locality with commuting even algebras, is not earned.** | compatibility check only | **CRITERION.** Any fermionic "exclusion" is only a priced interpretation. |
| D-7 | One real coordinate per site (amended D) | The fact is earned. **Requiring no additional complex structure is a minimality criterion.** | pricing of supplied complex structure | **CRITERION.** A complex structure is reported as a supplied price, never as an exclusion. |

**Former "tension" paragraph: WITHDRAWN by amendment.** D-2, D-6 and D-7 are CRITERION, so their
predicted exclusions (quasi-free coverage, fermion locality, bosonic complex structure) are
**priced interpretations only.** The earlier prediction that "no non-representational lift
survives without supplied structure" is withdrawn as a selector-based prediction. It is kept in
the git history, commit `66725e5`.

## §4 Shared vs distinguishing properties (the owner's minimum comparison)

| Pair | Shared (descends from K) | First distinguishing observable (front-run) |
|---|---|---|
| Λ-B vs Λ-F | one-particle dynamics; two-point function; k(τ); support graph; CP for accretive K | the two-quanta sector: n_k = 2 present vs excluded; four-point / Wick permanent vs determinant (I-2) |
| Λ-KvN vs Λ-B/Λ-F | classical trajectory transport; Jacobian-support access graph (CL-6) | whether there is particle-number (Fock) structure at all. KvN's noncommutativity is x–λ only |
| Λ-K vs Λ-B (real) | the Koopman polynomial spectrum = the bosonic number spectrum (I-2); both commutative on the real space | the carrier: functions of x (Koopman) vs the Gaussian L²(γ) Segal picture. **Possibly unitarily equivalent** (Segal isomorphism). **To verify:** if so, they collapse to one lift |
| Λ-H dilations among themselves | the reduced dynamics at the earned site | bath observables only (unearned access; I-3) |

## §5 Pre-registered adjudication rules and death criteria (frozen on owner approval of this draft)

**The rules:**
- **R-0 (SETTLED by owner ruling `5899215672`).** Before any evaluation, the owner rules each of D-1 … D-7 as **EARNED** (usable as a
  selector) or **CRITERION** (usable only as a priced assumption and never counted toward
  selection). No discriminator may be added after evaluation begins; new ones go to a successor
  list.
- **R-1.** A lift counts as **excluded** only when an EARNED discriminator excludes it at
  identity/theorem grade, **at earned access**, with no thresholds and no empirical input.
- **R-2.** Lifts proved unitarily or representationally equivalent (e.g. Λ-K vs real Λ-B, if the
  Segal equivalence holds) are merged before counting.
- **R-3.** Representational lifts (Λ-K, Λ-KvN, Liouville-δ) never count as "physical lifts
  selected".

**The terminals (each exhaustive condition fixed now):**

| Terminal | Condition |
|---|---|
| **SELECTED-IN-CLASS** | Exactly one **non-representational** lift survives all EARNED discriminators, in a declared class, with no added access and no criterion. |
| **CONSTRAINED-NONUNIQUE** | EARNED discriminators exclude at least one lift, but at least two inequivalent non-representational lifts survive. |
| **IRREDUCIBLE/SUPPLIED** | No EARNED discriminator excludes any non-representational lift. Every separating constraint is either identical across lifts at earned access (I-1, I-3) or needs a CRITERION or unearned access. **The lift/formation choice is then an additional supplied datum.** |
| **REPRESENTATIONAL-ONLY** | EARNED discriminators exclude every non-representational lift, so that only representational lifts remain. **Earned structure then selects "no new physics".** |
| **UNFORMULABLE** | The lifts cannot be compared on common earned structure without supplied structure (e.g. if D-2 is ruled EARNED and no lift family covers the whole earned class non-representationally). |

**Kill conditions for this gate's own claims:**
- Any front-run identity in §2 that fails verification is withdrawn before evaluation, and the
  §3 predictions that depend on it are struck.
- If the owner rules D-6 or D-7 CRITERION, their tension (§3) is recorded as **priced**, not as
  exclusion.

## §6 What evaluation would involve (for owner authorization; none executed)

1. One independent verification of I-1 … I-4 and of the Segal-equivalence question (§4, row 3).
2. The owner's R-0 rulings on D-1 … D-7.
3. Theorem-grade evaluation of the EARNED discriminators only: exact algebra, standard results
   cited with hypotheses, abstract counterexamples labelled as mathematics.

**HARD STOP** for owner review. No S-5 run, no EA-1, no gravity reopening, no new numerical
physics.
