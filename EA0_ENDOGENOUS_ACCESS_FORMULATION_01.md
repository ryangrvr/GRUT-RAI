# EA-0 — ENDOGENOUS ACCESS: FORMULATION / THEOREM GATE 01

**STATUS: FORMULATION DOCUMENT — PROPOSED TERMINAL FOR OWNER RULING. NOT A RESULT OF ANY RUN.**
- No computation. No member evaluated. No physics model chosen for an attack.
- The lemmas below are proved in sketch at identity/standard-mathematics grade. **One independent
  verification pass is recommended before the owner rules** (house precedent: O-2 design rev 2).
- **Authority:** `LEVEL0_FOREST_SYNTHESIS_OWNER_RULING_01.md` §5 (EA-0 AUTHORIZED; EA-1 NOT YET
  AUTHORIZED).
- **Date:** 2026-09-29 · **Branch:** `master-w25bu9`.

**The question (owner, verbatim):**

> Can a state-dependent access structure 𝒳(ρ) be defined mechanically in a declared class without
> supplying either (a) an access seed or (b) an arbitrary criterion whose choice performs the
> selection?

**Allowed terminals:** FORMULABLE · CLASS-SPLIT · SEED-SMUGGLED · CRITERION-SMUGGLED ·
TRIVIAL/IDENTITY · NONUNIQUE · UNFORMULABLE. **A negative terminal is success.**

## §0 Bottom line

**Proposed terminal: CLASS-SPLIT.** It comes with a precise obstruction, and the owner must decide
whether that obstruction amounts to a renamed primitive.

1. **A seedless, criterion-free, representation-covariant, localized, state-dependent object
   exists and is canonical:** the reach-compressed local net 𝔈(ρ) (§3, candidate C-6; §8). It uses
   no access seed and no free parameter.
   - **It does presuppose the substrate's local net {𝒜_x}.** That is the L0-1b locality
     ingredient, not an observer seed. **The owner must rule whether presupposing it is
     admissible** (§6.3).
2. **Its state dependence is TRIVIAL by identity in every class the record has earned** (§4):
   - trivial for faithful states (every Gibbs state; every stationary state of a primitive
     dissipative substrate, including the declared L0 substrate);
   - trivial for generic pure states of generic dynamics;
   - trivial for response geometry in the quadratic class.
3. **It is non-trivial exactly when the generator carries exact invariant structure aligned with
   local configurations:** local conservation laws, Hilbert-space fragmentation, or kinematic
   constraints (Lemma L7).
   - Then a localized state change really does remove available local distinctions and
     interaction edges. That is the "state exclusion" semantics, and it only ever **coarsens**
     (Lemma L4).
   - **But the exclusion structure is carried by H, not produced by ρ.** The state only selects
     *which* of the generator's sectors is realized.
4. **The only net-free routes to localization need a criterion:**
   - P-1's intrinsic functionals are plural, and all three are **state-independent** in the
     tested class (Lemma L8);
   - locality-from-spectrum needs the criterion "H is k-local" (literature, cited, unverified).

   These are **NONUNIQUE / CRITERION-SMUGGLED** unless the owner rules k-locality principled
   (§5, §6.3).
5. **The precise obstruction (§9):**

> In a fixed-algebra framework, a state can change *structure* (as opposed to values on a fixed
> structure) seedlessly only through its support within the generator's invariant-subspace
> lattice. On every earned class that lattice is trivial relative to the local net. So
> endogenous access, where non-trivial, is endogenous to **the generator**, not to the state. It
> is a property of H, read out by ρ.

   The needed ingredient, exact local exclusion structure in H, is **not in the Level-0 earned
   bundle and is derived by no record.** On the reading of this document that makes the route
   **generator-carried**, i.e. dependent on S-5 (derive the generator), rather than a new
   independent primitive.

## §1 Definition of access for this program

Fixed from the record, not invented here:
- P-5 verdict §1–3: access is representational in its labeling, canonical-given-a-seed in its
  algebra, and declarative in its seed.
- P-6 frozen machinery: the dynamical closure cl(S;H).
- GS-1: geometry is recovered from site-resolved access data.

**Definition A (access, this program).** Given a substrate (𝒜, 𝒞, ρ), where 𝒜 is the
operator algebra, 𝒞 the dynamics (a unitary group e^{−iHt}, or a dissipative semigroup e^{t𝓛})
and ρ a state, an **access structure** is a triple 𝒳 = (𝒮, 𝒪_𝒮, F_𝒮):
- **𝒮** — *what is coupled*: a set of operators through which a retained sector, probe or
  observer interacts with Ω. This is the **seed** in P-5/P-6.
- **𝒪_𝒮** — the operator structure 𝒮 generates under 𝒞, e.g. cl(𝒮;H). It is canonical given 𝒮
  (P-5).
- **F_𝒮** — the interface data: the influence hierarchy of ρ as seen through 𝒮. By P-4's scoped
  standing (with `P4_HIERARCHY_CORRECTION_01.md`), it is complete as the interface for the
  declared access, in class.

**Definition A′ (access for geometry).** A *relational* access structure is an indexed family
{𝒳_x}_{x∈Λ} over a set of loci Λ, together with an adjacency relation between loci read off
the dynamics. A single global 𝒳 is **not** relational (owner 5c: "a canonical global reachable
algebra that contains no relational localization is not yet 𝒳 for geometry").

**Definition S (seedless).** 𝒳(ρ) is *seedless* if its construction consumes no choice of 𝒮
beyond what is fixed by (𝒜, 𝒞, ρ) and declared substrate structure. Whether the local net
{𝒜_x} counts as declared substrate structure or as a seed is an owner ruling (§6.3).

## §2 Four distinctions (formal), and the trap between them

Fix the substrate. Let U_t be the dynamics.

| Level | Object | State-dependent how | Example | Counts as endogenous access? |
|---|---|---|---|---|
| **(a) observable values** | ω_ρ(A) = Tr ρA for A in a *fixed* structure, including response ⟨[A(t),B]⟩_ρ and correlations | always (values) | mutual-information distances; modular data −log ρ_x; state-dependent response in an interacting system | **No** (owner 5d) |
| **(b) reachable sector** | P_ρ, the projector onto the smallest 𝒞-invariant subspace containing supp ρ (Lemma L1) | through supp ρ | the N-particle sector of a number-conserving H | only as input to (c); it is **global** |
| **(c) access** | the structure {𝒪_x(ρ)}: which operators are *available/distinguishable* at x, as a function of ρ, with no supplied 𝒮 | through the structure itself | P_ρ𝒜_xP_ρ (§3 C-6); the local stabilizer 𝒜_x ∩ {ρ}′ (§3 C-5) | **Yes, if seedless and non-trivial** |
| **(d) relational geometry** | G_𝒳(ρ): adjacency/distance recovered from {𝒪_x(ρ)} and 𝒞 | through (c), or spuriously through (a) | Γ(ρ) (§8) | yes, **only if it comes through (c)** |

**The trap.** (d) can vary with ρ purely through (a): correlation-derived geometry changes with
the state even when access is fixed. EA-0 therefore requires every (d)-claim to factor through a
(c)-object. **Any construction whose ρ-dependence enters only through expectation values on a
fixed structure is classified as TRIVIAL for access (a correlation readout), however structural
it looks.**

## §3 Candidate seedless constructions and kill tests

**Kill tests (owner 5c):**
- **T1** seedless?
- **T2** representation-covariant, i.e. 𝒳(VρV†; VHV†) = V𝒳(ρ;H)V†?
- **T3** localized/relational?
- **T4** avoids generic collapse to the whole algebra, or to a constant?
- **T5** more than standard support/central-decomposition mathematics (NULL-REDUNDANT
  otherwise)?
- **T6** distinguishes neighboring/relational structure, not only a global sector?

| # | Candidate | T1 | T2 | T3 | T4 | T5 | T6 | Classification |
|---|---|---|---|---|---|---|---|---|
| C-0 | cl(S;H) restricted to Reach(ρ) (P-6 L-C) | **✗** (contains S) | ✓ | depends on S | — | — | — | **SEED-SMUGGLED.** Kept as a **control**: it quotients seeds by the reachable sector (P-6 L-C: σ_z¹ ≡ σ_z² on the even block) but derives none. |
| C-1 | Reachable subspace P_ρ (Lemma L1) | ✓ | ✓ | **✗** (global) | ✗ for faithful ρ (L2) and generic pure ρ (L3) | ✗ (Krylov/cyclic subspace) | ✗ | **TRIVIAL/IDENTITY** as access: global and non-relational. |
| C-2 | Observables modulo equality on the reachable support, 𝒜/{A : P_ρAP_ρ = 0} | ✓ | ✓ | ✗ (global) | ✗ (as C-1) | ✗ (compression) | ✗ | **TRIVIAL/IDENTITY** (C-1 in operator form). |
| C-3 | State/dynamics-generated algebra {ρ(t) : t}″ and its central decomposition | ✓ | ✓ | ✗ (global) | ✗ (generic non-stationary ρ: generically the whole algebra; stationary faithful ρ, e.g. Gibbs: the functions of H) | ✗ (standard; = P-6 L-S central decomposition) | ✗ | **TRIVIAL/IDENTITY; NULL-REDUNDANT.** |
| C-4 | Modular/entanglement structure of local reduced states (K_x = −log ρ_x; MI distances) | ✓ given the net | ✓ | ✓ | ✓ | ✗ (borrowed "geometry from entanglement" literature) | ✓ | **TRIVIAL for access** by §2: pure (a)-type correlation readout. |
| C-5 | Local stabilizer / operational distinguishability, D_x(ρ) := 𝒜_x ⊖ (𝒜_x ∩ {ρ}′) (local operations that change ρ) and its dynamical version 𝒜_x ∩ ⋂_t {ρ(t)}′ | ✓ given the net | ✓ | ✓ | ✗ generic (L5): {ρ}′ ∩ 𝒜_x = ℂ𝟙 for entangled faithful ρ; for Gibbs ρ it equals the local conserved quantities of H | ✗ | only through local conserved quantities of H, or through local purity/product structure of ρ (an (a)-type readout) | **CLASS-SPLIT:** trivial generically; non-trivial only via generator structure (as C-6) or correlation structure (as C-4). |
| C-6 | **Reach-compressed local net** 𝒪_x(ρ) := P_ρ𝒜_xP_ρ, with interaction graph Γ(ρ) (§8) | **✓** given the net (no S, no parameter) | ✓ (L1) | **✓** | ✗ for faithful/generic states (L2, L3); ✓ with exact local invariant structure in 𝒞 (L7) | partly (the object is standard compression; the *relational monotone* Γ(ρ) ⊆ Γ is its only content, L4) | **✓** where non-trivial | **CLASS-SPLIT:** TRIVIAL on earned/generic classes; FORMULABLE where 𝒞 carries exact local exclusion structure (supplied with the class). |
| C-7 | Energetic reach: compression to a spectral window or isolated band P_band of H | ✓ | ✓ | ✓ given the net | ✓ | ✗ (Schrieffer–Wolff / blockade physics) | ✓ (kinetic constraints emerge) | **CRITERION-SMUGGLED** if the window is a free choice. With an **isolated band** (gap-fixed, no free parameter) it is **state-independent**: P_band depends on H only, and ρ enters as conditioning within a fixed compressed structure, an (a)-type readout. So it **derives the exclusion kinematics without fine-tuning, but not as state-dependent access.** |
| C-8 | P-1's subsystem functional 𝔖[𝒜,𝒞,ρ] | ✓ anchor-free (C1–C3) | ✓ | selects among **site subsets**, so presupposes the net | ✓ in X2 | — | partial (a partition, not a net) | **NONUNIQUE** (criterion plurality; §5) **and state-independent in the tested class** (L8). It addresses the *seed* question, not state dependence. |
| C-9 | Locality from the spectrum (select the tensor-product structure in which H is k-local) | ✓ net-free | ✓ | ✓ | generic uniqueness *if a local TPS exists* (literature) | ✗ (external result) | ✓ | **CRITERION-SMUGGLED unless the owner rules "H is k-local" principled.** L0-1b makes locality an earned *ingredient*, which may license it. **Cited, not verified in-house:** Cotler, Penington & Ranard, "Locality from the spectrum" (2019). It is state-independent either way. |

**Pattern across all ten candidates** (a finding over the examined set, **not** a no-go theorem):
- every seedless, covariant candidate is **(i)** global, or **(ii)** trivial generically, or
  **(iii)** state-dependent only through an (a)-type correlation readout, or **(iv)** non-trivially
  state-dependent only through **exact local invariant structure of the generator**;
- every candidate that supplies localization without the net needs a criterion (C-8, C-9).

## §4 Theorem and identity constraints (proof sketches)

**L1 (reach; canonical).**
- **Statement:** for unitary 𝒞 = e^{−iHt} on a finite-dimensional ℋ, let P_ρ be the projector
  onto 𝒦(ρ) := span{e^{−iHt}ψ : ψ ∈ supp ρ, t ∈ ℝ}. Then 𝒦(ρ) is the smallest H-invariant
  subspace containing supp ρ, and P_ρ = Σ_λ Π(E_λ supp ρ), where E_λ are the spectral
  projections of H and Π projects onto the span. Also [P_ρ, H] = 0 and
  P_{VρV†}(VHV†) = V P_ρ V†.
- **Proof:** 𝒦(ρ) is invariant and contains supp ρ. Any invariant subspace containing supp ρ
  contains every e^{−iHt}ψ. The spectral form follows from e^{−iHt} = Σ e^{−iλt}E_λ and the
  linear independence of the e^{−iλt}. Covariance is immediate. ∎
- **Consequence:** no seed and no parameter.

**L2 (faithful collapse).**
- **Statement:** if ρ has full rank, then P_ρ = 𝟙. Every Gibbs state e^{−βH}/Z (β < ∞) is full
  rank, so **reach-based access is trivial at every finite temperature.**
- **Dissipative analogue** (standard semigroup structure theory, cited as standard): if e^{t𝓛}
  is primitive (unique stationary state, of full rank), the asymptotic support is everything.
- **The declared L0 substrate** (linear, gapped, accretive K, non-degenerate noise Q ≻ 0) has a
  unique full-support Gaussian stationary state (standard OU). **So on the earned substrate,
  asymptotic reach-based access is TRIVIAL by identity.** ∎

**L3 (generic pure collapse).**
- **Statement:** if H has non-degenerate spectrum and ψ has E_λψ ≠ 0 for every λ, then
  dim 𝒦(ψ) = dim ℋ, so P_ψ = 𝟙.
- **Proof:** by L1, P_ψ = Σ_λ Π(E_λψ). Each term is the rank-one projector onto the eigenvector,
  so the sum is 𝟙. ∎
- **Consequence:** generic pure states of generic dynamics give trivial reach.
- **Where it is non-trivial:** only states supported on a proper invariant subspace (eigenstate
  mixtures of low spectral complexity, or symmetry/fragmentation sectors).

**L4 (compression only coarsens; monotone relational content).**
- **Statements:**
  - 𝒪_x(ρ) = P_ρ𝒜_xP_ρ is the image of 𝒜_x under the compression A ↦ P_ρAP_ρ, which is
    completely positive and unital onto P_ρ.
  - It is an **operator system, not in general an algebra**: P A P · P B P ≠ P AB P unless P
    commutes with 𝒜_x.
  - Distinct A ≠ B can have equal images (P-6 L-C).
  - Define Γ as the relation x ~ y (x ≠ y) iff ∃ A ∈ 𝒜_x, B ∈ 𝒜_y with [A,[H,B]] ≠ 0, and
    Γ(ρ) as x ~_ρ y iff ∃ such A, B with P_ρ[A,[H,B]]P_ρ ≠ 0. Then **Γ(ρ) ⊆ Γ.**
- **Proof:** if [A,[H,B]] = 0 then its compression is 0. ∎
- **Consequences:**
  - the definition is decomposition-free (no choice of local terms h_xy);
  - **state-dependence of this access can only *remove* distinctions and edges, never add
    them.** That matches the "state exclusion" semantics exactly;
  - it also fixes a **structural prediction any EA-1 would inherit: exclusion, never
    inclusion.**

**L5 (the local stabilizer collapses generically).**
- **Statement:** if ρ is full rank with non-degenerate spectrum, {ρ}′ is the maximal abelian
  algebra of ρ's eigenprojectors. Then 𝒜_x ∩ {ρ}′ = ℂ𝟙 unless some non-trivial local operator
  is diagonal in ρ's eigenbasis.
- For ρ = e^{−βH}/Z with non-degenerate H, {ρ}′ = {H}′. So 𝒜_x ∩ {ρ}′ are exactly the **local
  conserved quantities of H.** ∎
- **Consequence:** C-5's state-dependence is generator-carried (local conserved quantities) or
  reads the state's local product/purity structure, which is (a)-type.

**L6 (the quadratic identity; carried from the synthesis).** In a quadratic canonical system the
commutators of the linear fields are c-numbers. So response data ⟨[A(t),B]⟩_ρ for linear A, B,
and any geometry built from them, are ρ-independent. A quadratic member read through its response
channel is a **negative control only.** ∎

**L7 (when Γ(ρ) ≠ Γ).**
- **Statement:** an edge x–y is removed iff every double commutator [A,[H,B]] (A ∈ 𝒜_x,
  B ∈ 𝒜_y) is annihilated by compression to 𝒦(ρ).
- This needs 𝒦(ρ) to be a **proper** invariant subspace on which the x–y coupling acts
  trivially. That is, H must possess an invariant subspace, containing supp ρ, **aligned with a
  local configuration**: a local conservation law, a fragmented Krylov sector, or a kinematic
  constraint.
- A *localized* change of ρ alters Γ(ρ) only if it moves supp ρ between such sectors. ∎
- **Degenerate regime (caveat):** if rank P_ρ is small compared with the local dimension, the
  compression turns operators into numbers. In the extreme case (ρ an eigenstate, P_ρ of rank
  one), P_ρ[A,[H,B]]P_ρ is just the expectation value ⟨[A,[H,B]]⟩. C-6 then degenerates into an
  **(a)-type readout.**
  - C-6 counts as (c)-type access only when the invariant sectors are large enough to keep
    operator content: **extensive** sectors whose shape depends on local configurations (e.g.
    fragmented Krylov sectors).
  - Exact conserved quantities that merely fix eigenstates (e.g. the mode occupations of an
    integrable quadratic model, including local integrals of motion in localized phases) put
    C-6 in this degenerate regime. They do **not** give structural access.
- **Consequence: the state selects; the generator supplies the sectors.**

**L8 (P-1's intrinsic criteria are state-independent in the tested class).**
- **Statement:** in `RELATIONAL_ONTOLOGY_CHARTER_01.md` §1.3:
  - C1 (memory-kernel rank) is computed from V_SE and Ω_E;
  - C3 (causal cohesion) is computed from the propagator G(t) = Ω⁻¹sin(Ωt), with a declared scale
    t* = 2.0;
  - C2 uses the *ground state* of V.

  All three are functions of V (i.e. of 𝒞) alone. So the X2 selection is 𝔖[𝒜,𝒞], not
  𝔖[𝒜,𝒞,ρ]. ∎
- **Consequence:** P-1's genuine anchor-free selection addresses the *seed* and *partition*
  question. It supplies **no state dependence.** C3 also carries a declared scale (t*), a
  parameter choice to be audited like a criterion.

## §5 The criterion-selection problem (owner 5b)

The P-1 criterion class is {C1 rank, C2 ground-state MI, C3 causal cohesion}. They are
inequivalent (`RELATIONAL_ONTOLOGY_MAP_01.md` §1; `RELATIONAL_ONTOLOGY_OWNER_RULING_01.md` §1:
"criterion-plurality … a genuine discovery"). **Choosing C3 because it succeeded in X2 is
forbidden and is not done here.**

| Option | Status on the record | Reason |
|---|---|---|
| **(1)** A unique functional forced by earned structure | **NOT ESTABLISHED** | The earned Level-0 bundle consists only of ingredient → property edges (gap → memory, passivity → positivity, locality → geometry, linearity → exact reduction; floor deposit §3). None is a subsystem criterion, and none singles out C1, C2 or C3. |
| **(2)** The criteria are equivalent in a stated subclass | **YES, in the exactly reducible subclass only (identity grade)** | If V is block-diagonal with S a block, then V_SE = 0: C1's kernel vanishes identically, C2's MI = 0, and C3's cohesion is unbounded. All three single out the decoupled block. This is P-6's L-S central decomposition: **NULL-REDUNDANT.** Beyond it, no record shows agreement, and X2 shows disagreement (C1 picked [7,9]). |
| **(3)** A higher principle selects among them without new supplied structure | **UNFORMULATED** on the record | Entropy, complexity, least-action and simplicity selectors are prohibited without their own charter (P-6 charter). None is chartered. |
| **(4)** Criterion pluralism is irreducible | **OPEN, and NONUNIQUE at recorded scope** | Plurality is measured (X1–X3). Irreducibility is **unproved**. The criterion-unification fork named in the P-1 map §4 (item "P-2 — criterion unification", later superseded in numbering by the executed P-2 influence cone) **was never run.** |

**Verdict for the P-1 route (C-8): NONUNIQUE at recorded scope.**
- Independently of the criterion question, it is **state-independent** in the tested class (L8).
- It also **presupposes the site net**: the partition family is subsets of sites.
- So even a resolved criterion would yield a seedless *partition/net*, not *state-dependent*
  access.

## §6 No-smuggling audit

### §6.1 Against P-6 (the seed)

| P-6 finding | Does C-6 evade it? |
|---|---|
| The seed is supplied (non-derived in-class) | C-6 contains **no seed.** It compresses *every* local algebra 𝒜_x, not chosen operators within a site. This is P-6's construction with S replaced by the whole net, which removes the "which operators" choice. |
| Interface-relative minimality (L-A) | No interface is declared in C-6, so this is not applicable. |
| Non-injective closure (L-B/E) | C-6 inherits non-injectivity *as its content* (L4: coarsening only). It claims no selection among seeds. |
| Degenerate orbits (L-C) | Covariance (L1) makes C-6 equivariant, so it cannot break a symmetry. Its state-dependence is exactly P-6's L-C reachable-sector diagnostic, **now applied to the net rather than to a seed.** |
| Path dependence (L-D2) | No elimination procedure is involved, so this is not applicable. |

**Verdict:** C-6 is **not SEED-SMUGGLED.** C-0 is, and is kept as a control.

### §6.2 Against GR2 (the supplied quadruple and the probe)

- **No member of {coupling class, spin, reach, cone} enters.** Γ(ρ) is an interaction-support
  relation, not a propagation speed or a coupling class.
- **No probe is supplied** (STATE_EXCLUSION D2). Γ(ρ) is defined from double commutators of the
  substrate's own local algebras, compressed by the substrate's own reach.
- **The GR2 non-selections are untouched and not reopened** (forest ruling §4).

### §6.3 The one presupposition left: the local net {𝒜_x} (OWNER RULING REQUIRED)

Every localized candidate (C-4, C-5, C-6, C-7, C-8) presupposes the substrate's site net. C-9 is
the only net-free candidate, and it needs the criterion "H is k-local". This yields a
**trilemma for localization**:

- **(i) Net presupposed.**
  - This is declared substrate structure: the L0-1b locality ingredient, certified necessary for
    P_geometry.
  - It is neither an observer seed nor a selection criterion.
  - **Operator reading:** admissible, *if* the owner treats the net as substrate data, just as
    the generator is treated as presupposed (S-5).
- **(ii) A criterion selects it.** Either P-1 (NONUNIQUE) or k-locality (CRITERION-SMUGGLED unless
  ruled principled).
- **(iii) Nothing localizes.** Then access is global only (C-1 to C-3), which is TRIVIAL for
  geometry.

## §7 Outcome taxonomy applied

| Scope | Terminal |
|---|---|
| C-0 (seed restricted to reach) | SEED-SMUGGLED (control) |
| C-1, C-2, C-3 (global reach and algebra constructions) | TRIVIAL/IDENTITY (non-relational; NULL-REDUNDANT) |
| C-4 (entanglement/modular) | TRIVIAL for access (correlation readout, §2 trap) |
| C-5 (local stabilizer) | CLASS-SPLIT (trivial generically; otherwise generator- or correlation-carried) |
| C-6 on **every earned class** (quadratic response, faithful and Gibbs states, primitive dissipative substrate including the declared L0 substrate, generic pure states) | **TRIVIAL/IDENTITY** (L2, L3, L6) |
| C-6 on classes with **exact local invariant structure** in 𝒞 (fragmentation, local conservation, kinematic constraints) | **FORMULABLE**, with the exclusion structure carried by the generator (L7) |
| C-7 (energetic band) | CRITERION-SMUGGLED (free window), or state-independent (isolated band) |
| C-8 (P-1 functional) | NONUNIQUE (and state-independent in class, L8) |
| C-9 (locality from spectrum) | CRITERION-SMUGGLED pending an owner ruling on k-locality (external, unverified) |
| **EA-0 overall** | **CLASS-SPLIT (proposed)**, with the obstruction of §9 |

## §8 The minimal mathematical object (the FORMULABLE branch)

If the owner admits the net (§6.3) and wishes to keep the route open, the object an EA-1 would
manipulate is

> **𝔈(ρ) = ( P_ρ , {𝒪_x(ρ) = P_ρ𝒜_xP_ρ}_{x∈Λ} , Γ(ρ) ),**

with Γ(ρ) defined in L4. Its properties:
- **Seedless and parameter-free** (L1).
- **Covariant** (L1).
- **Local and relational** (L4).
- **Monotone:** exclusion only (L4).
- **Trivial on every earned class** (L2, L3, L6).
- **Non-trivial iff 𝒞 has exact local invariant structure with extensive,
  configuration-dependent sectors** (L7, including its degenerate-regime caveat).

**Consequence for EA-1 (if the owner ever authorizes it).** EA-0 already settles EA-1's original
question structurally: *a localized state change alters Γ(ρ) iff it moves supp ρ between
generator-supplied local sectors.* A run would only re-measure L7. **The live question moves
upstream**, and EA-1 would have to be re-posed as:

> **Is exact local invariant/exclusion structure in the generator forced by earned Level-0
> ingredients, or is it supplied with the class?**

That is a question about the generator. **It folds into S-5.**

Its clean death condition, fixed now: *on every class built only from earned ingredients (gap,
passivity, locality, with linearity deleted as L0-1c permits), the generator has no exact local
invariant structure with extensive, configuration-dependent sectors (beyond the global conserved
quantities, and beyond eigenstate-level sectors that reduce C-6 to (a)-type readouts, L7 caveat)*
→ the route is CLOSED at that scope: endogenous access reduces to a presupposed property of the
generator.

## §9 The precise obstruction (the reason the proposal is not FORMULABLE outright)

1. **Fixed-algebra lemma pattern.** With 𝒜 fixed, a state can influence *structure*, as opposed
   to values on structure, seedlessly only through its support relative to 𝒞's invariant
   subspaces (C-1, C-6), or through its own symmetry {ρ}′ (C-5). Everything else is an (a)-type
   readout (§2).
2. **The earned bundle makes that route trivial.** Faithful and stationary states (L2), generic
   dynamics (L3) and quadratic response (L6) all make support-based structure collapse. The one
   exception is the global conserved sectors, which are not relational.
3. **Non-triviality needs a new ingredient.** It requires **exact local invariant structure in
   the generator** (L7). No Level-0 record earns it, and no record derives it.
4. **So "endogenous access", where it exists, is generator-carried.** The state selects among
   sectors that H supplies. Calling that "state-dependent access" is accurate at the level of
   (c). But it **renames a property of H**, so the primitive moves to the generator (S-5); it is
   not eliminated.
5. **Localization itself needs the net, or a criterion** (§6.3).

**What would overturn this obstruction:** a seedless, covariant, localized construction whose
non-trivial ρ-dependence survives on faithful states of generic local dynamics without being an
(a)-type readout. None is known to this document, and none appears on the record. **This is a
finding over the examined candidates, not a proved no-go theorem.** Promoting it to a theorem
would need an owner-authorized theorem attempt (e.g. a characterization of all covariant
state-to-operator-system maps built from (𝒜,𝒞,ρ)).

## §10 What this document does not claim

- It does not choose a physical attack model (owner 5d). Fragmentation and constraint classes
  are named only as the place where L7 is non-trivial.
- It does not claim that access, distinguishability or equivalence classes are fundamental.
- It does not relitigate GR2. It does not modify the floor, P-1, P-4, P-5 or P-6.
- It does not treat the external locality-from-spectrum result as verified.
- It does not authorize EA-1.

**HARD STOP** for owner review. **The decision (owner):** did EA-0 produce a genuinely seedless,
non-circular access map, or merely rename the primitive? The operator's proposed reading:

- **seedless: yes** (C-6), given the net;
- **non-circular: yes**;
- **non-trivial on earned classes: no**;
- **where non-trivial, it renames a property of the generator.**

**Proposed terminal: CLASS-SPLIT.** The alternative the owner may prefer is
**TRIVIAL/IDENTITY on the earned scope, with the constrained-class branch recorded as
generator-carried (→ S-5).**
