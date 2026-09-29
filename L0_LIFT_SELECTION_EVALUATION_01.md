# L0 LIFT SELECTION — EVALUATION 01 (EARNED selectors only) and mechanical terminal

**Status:** evaluation of **D-1, narrowed D-4 and narrowed D-5 only**, per owner ruling `5899215672`.
- **Inputs:** the frozen pre-registration `L0_LIFT_SELECTION_01.md` (`a14c722`), the verification
  and corrections (`a767d39`, committed **before** this evaluation).
- **Method:** identity/theorem grade, using standard results already verified. No new discriminator.
  No empirical selector. No numerical physics.
- **HARD STOP at the end.**

## §0 Two frozen-text issues, handled before any verdict (disclosed, not chosen for outcome)

**(i) D-1 vs D-2 (the verifier's flag).**
- D-1 is EARNED: "use only the predicates actually earned at their recorded scope".
- The earned L0-1c nonlinear predicates would exclude the quasi-free lifts, which provably cannot
  reproduce r(τ; a, β).
- **The owner's D-2 ruling states verbatim** that the whole-class demand "cannot exclude quasi-free
  lifts inside this gate. Record lack of nonlinear coverage as a price/scope limitation, not an
  earned exclusion."
- **So D-1 is evaluated on each lift's domain of definition** (the linear core for quasi-free lifts),
  and nonlinear non-coverage is recorded as a **price.** This applies the ruling's text; it is not an
  operator choice.
- Likewise, D-1's frozen text tests "whether any lift **alters the earned predicates**", i.e. the
  properties of k(τ). The lift-specific **readout identification** (verification §1) is a **price**,
  not a D-1 test. A "same readout operator type" requirement would be a **new discriminator** and is
  not used.

**(ii) The reading of D-5.** The frozen D-5 does not say whether "source-descended observable" means:
- **(R-a)** O-5's V evaluated on the lift's descended one-particle data (orbit, amplitude vector,
  mean, or covariance); or
- **(R-b)** the operator image of V in the lift, with expectations in the lift's states.

The verifier flagged that this must be fixed uniformly and in advance. **It was not fixed in the
pre-registration.** This evaluation therefore reports **both**, and applies frozen rule **R-1**
literally: *a lift is excluded only when an EARNED discriminator excludes it at identity/theorem
grade.* An exclusion that holds under one admissible reading of the frozen discriminator and fails
under another is **not** an identity-grade exclusion by that discriminator. **The owner may rule the
reading.** §4 states exactly what would change.

## §1 D-1: earned kernel / memory / positivity / earned geometry-support content

| Lift | Reproduces k(τ) and its earned predicates on its domain? | Readout identification (price) | Nonlinear L0-1c (price, D-2) | D-1 |
|---|---|---|---|---|
| Λ-K | yes, exact | x₁ in δ-states | covered | pass |
| Λ-KvN | yes (β = 0 for any ψ with mean e₁) | ⟨M_{x₁∘φ_τ}⟩ | covered only in the δ-limit | pass |
| Λ-H cotangent | yes, exact | x₁∘π, any p₀ | covered | pass |
| Λ-H Sz.-Nagy | yes (amplitude) | ⟨e₁,U(τ)e₁⟩; zero bath component | linear only | pass |
| Λ-H FKM | **exactness NOT-ESTABLISHED** (a finite bath cannot; the infinite Ohmic overdamped limit, mean only) | — | — | **not evaluable at identity grade → not excluded (R-1)** |
| Λ-B complex | yes (amplitude / coherent mean) | declared per V-1 | linear only | pass |
| Λ-B real (OU) | yes, P^resp via the conditional mean | E[X₁(τ)\|x₀] | linear only | pass |
| Λ-F complex Fock | yes (amplitude; ⟨{a₁(τ),a₁†}⟩; k² via ⟨n₁⟩) | a two-time or amplitude readout; the odd one-time readout vanishes under superselection | linear only | pass |
| Λ-F real Clifford | yes (degree-1 amplitude) | as above | linear only | pass |

- The **geometry-support content at earned access** (a single retained site) is shared by
  construction: every lift descends from the same K_b. It excludes nothing.
- **D-1 excludes no lift.**

## §2 D-4 (narrowed): preserves the earned passive/accretive structure of the descended contraction?

- Every lift's descended one-particle map is e^{−K_bt} or its transpose (verification §1). K_b is
  symmetric positive definite, so it is accretive (R-4) and e^{−K_bt} is a strict contraction.
  **Each lift preserves it identically.**
- **Domain notes, recorded as prices and not exclusions:**
  - Sz.-Nagy and real Λ-B exist **because** K is accretive (they are consistent with D-4);
  - the cotangent H is indefinite, and Hamiltonian passivity ≠ R-4 accretivity (not a failure of
    the descended contraction);
  - FKM is not evaluable (exactness).
- **CP** is reported separately as lift-internal: Λ-B and Λ-F quasi-free semigroups are CP for
  accretive K. **It is not a selector** (owner ruling A).
- **D-4 excludes no lift.**

## §3 D-5 (narrowed): preserves or faithfully represents O-5's strict Lyapunov/order structure on source-descended observables?

**What O-5 earned** (`L0_1F_DORD_THEOREM_01.md` §2):
- **𝒞₁/𝒞₂:** a strict Lyapunov function on relaxing **orbits**, e.g. V = ½|x|² with
  V̇ = −xᵀK_sx < 0 for accretive K.
- **𝒞₃ (stationary OU):** "does not order its sample paths". Only **law-level** lag
  distinguishability is earned (D-5 of O-5).

| Lift | (R-a) V on descended one-particle data | (R-b) operator image of V, in lift states |
|---|---|---|
| Λ-K | orbit e^{−Kt}x: strict decrease ✓ | U_tV = V∘φ_t, pointwise strictly decreasing ✓ |
| Λ-KvN | ✓ | ⟨M_{V∘φ_t}⟩ strictly decreasing for ψ ≠ δ₀ ✓ |
| Λ-H cotangent | ✓ (base orbit) | V∘π ✓ |
| Λ-H Sz.-Nagy | ✓ (compressed vector) | ⟨U(t)v, (P⊕0)U(t)v⟩ = \|e^{−Kt}v\|²_P ✓ |
| Λ-H FKM | not evaluable | not evaluable |
| Λ-B complex | ✓ (amplitude / covariance TC₀T†) | ⟨dΓ(P)⟩ = tr(P·TC₀T†), strictly decreasing for C₀ ≠ 0 ✓ |
| Λ-B real (OU) | mean e^{−Kt}x₀: ✓ | E[V(X_t)] = V(Tx₀) + ½tr(P(I − TTᵀ)): **not monotone** (it rises from x₀ = 0). **Fails the 𝒞₁ path-level structure.** But O-5 itself disclaims path ordering for the stochastic class, where only law-level structure is earned, and the OU lift **is** that class |
| Λ-F complex Fock | ✓ (one-particle data) | ⟨dΓ(P)⟩ = tr(P·TC₀T†) ✓ |
| Λ-F real Clifford | ✓ (degree-1 vector data) | the image of quadratic V is the scalar tr P: **cannot represent** O-5's quadratic Lyapunov structure ✗ |

**D-5 outcome by reading:**
- **(R-a):** excludes no lift.
- **(R-b):** fails **Λ-F real Clifford** (identity grade). It fails **Λ-B real (OU)** only if the
  𝒞₁ path-level structure is applied to a lift that instantiates the class for which O-5 explicitly
  did *not* earn path ordering. That is itself a second reading question.

**Under R-1 as frozen:** D-5's exclusions are **reading-dependent**, so they are **not identity-grade
exclusions by the frozen discriminator. D-5 excludes no lift.**

## §4 Mechanical terminal (from the frozen §5 mapping)

**What survives every EARNED selector, under every admissible reading:**
- at least **four inequivalent non-representational lifts:**
  1. the cotangent (Hamiltonian) extension;
  2. the Sz.-Nagy minimal unitary dilation;
  3. the complex bosonic quasi-free lift;
  4. the complex fermionic quasi-free lift;
- plus the representational Λ-K and Λ-KvN;
- FKM is not evaluable.

**No EARNED selector distinguishes among the four.** They differ only through priced structures:
- the statistics (Sym² vs Λ²);
- the complex/symplectic doubling (both quasi-free lifts, since N = 23 is odd);
- the bath preparation and the dilation type;
- an indefinite Hamiltonian;
- the readout identification;
- parity superselection;
- the linear-only domain;
- ħ, for physical identification.

> **TERMINAL (mechanical, R-1 as frozen): IRREDUCIBLE/SUPPLIED.**
> No EARNED discriminator excludes any non-representational lift at identity grade. Every
> separating constraint is either common to all lifts at the earned interface, or needs a CRITERION
> (D-2, D-3, D-6, D-7), a supplied structure, or unearned access. **The lift/formation choice is an
> additional supplied datum at this gate's scope.**

**What would change it (stated, not adopted):** if the owner rules D-5 to mean **(R-b)**, and
counts **real Clifford Λ-F** (or real OU Λ-B, under the further 𝒞₁-structure reading) as a lift
distinct from its complex variant, then at least one lift is excluded while at least four survive.
The mapping would then give **CONSTRAINED-NONUNIQUE.** Under every reading, **no unique physical
lift is selected.**

**Disclosure.** This terminal coincides with the outcome the owner anticipated as "likely" in the
ruling. It was assigned by the frozen R-1 and §5 mapping, **not** from that anticipation. The one
place where operator handling mattered, the under-specified D-5 reading, is set out in §0(ii) and
§4 for the owner to overrule.

## §5 Scope and fences

- The scope is the Level-0 earned structure (the linear core, plus L0-1c as a price), the earned
  retained-site interface, and the lifts listed in the frozen §1 plus the verified variants.
- This is **not** a multiverse or formation result (interpretation fence). No Standard-Model
  selector was used.

**HARD STOP** for owner review. No S-5, no EA-1, no gravity reopening, no numerical physics.
