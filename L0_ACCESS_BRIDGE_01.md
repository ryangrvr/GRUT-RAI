# L0 ACCESS BRIDGE 01 — can the earned classical substrate support an access/state structure, and is there a priced map to the later algebra?

**STATUS: FORMULATION DRAFT FOR OWNER REVIEW — NOT A RESULT; NO TERMINAL PROPOSED.**
- No computation. No member evaluated. No physics model chosen.
- The items marked **front-run** are identity-grade or standard-mathematics observations written
  under the house "identities first" rule. **Each needs one independent verification pass before
  it bears any terminal** (the EA-0 precedent).
- **Authority:** `EA0_OWNER_RULING_02.md` §7.
- **Date:** 2026-09-29 · **Branch:** `master-w25bu9`.

**The question (owner, verbatim):**

> What is the minimal access/distinguishability structure that can be defined directly on the
> classical deterministic Level-0 substrate, and is there a derived or uniquely priced map from
> that structure to the later algebraic access formalism?

**Binding rules:**
- **No silent lift.**
- Do not import Hilbert-space support, density matrices or operator compression by analogy.
- Do not call a standard mathematical embedding a derived physical ontology merely because it
  exists.
- **Do not optimize for UNIQUE-LIFT.**
- A collapse is an acceptable result.

## §0 What this draft already shows (front-run; to be verified)

1. **The gap is narrower than "substrate → everything".** The geometry leg already runs on K-level
   data:
   - G-2/GS-1 recover geometry from the resolvent G_AA(ω) = [(K − ω²)⁻¹]_AA, a function of K
     alone;
   - G-2's quantum XX leg reduces exactly to the one-magnon hopping problem;
   - the static resolvent reading (K + z)⁻¹ is R-3-admitted at linear-class scope.

   So **classical substrate → geometry has a K-level path** (with *declared* access sets). **The
   "?" sits on the other branch:** classical substrate → state/access algebra (P-5/P-6/EA-0) and
   → influence/quantum structure (P-2 to P-4).
2. **Classical route on the linear substrate: structural state-dependence collapses by identity.**
   Every candidate built from K on ẋ = −Kx is **independent of the state x**:
   - Kalman observability and controllability subspaces;
   - the Krylov and invariant-subspace lattice;
   - the Jacobian graph;
   - the indistinguishability quotient.

   The state enters only as values (the orbit). This is the classical twin of the EA-0 quantum
   collapse, but it is **native to the earned substrate**, with no lift.
3. **Classical route on L0-1c's nonlinear class: supports stay fixed; only weights move.**
   - The earned potential is V = ½xᵀK_bx + βΣx_i⁴, with an **on-site** quartic term.
   - So the Jacobian J(x) = −K_b − 12β·diag(x_i²) has the **same off-diagonal support as K_b for
     every state.**
   - The state changes on-site stiffness, and hence effective transmission, **continuously**. It
     never changes the interaction topology.
   - **The live question for the classical route** is the owner's value-vs-structure line: does
     a continuous, state-dependent reweighting of a fixed support count as *structural* access?
     This draft does not decide it (§3, CL-6/CL-7).
4. **Lift route: every map to the noncommutative algebra of P-5/P-6 needs supplied structure.**
   - The earned flow is **first-order and dissipative**, so it has no symplectic structure.
     Quantization is not directly defined.
   - The available path is **dissipative flow → (conservative dilation; non-unique) →
     Hamiltonian system → (quantization; ħ supplied, P-2 "located, not generated"; a choice of
     statistics, CCR or CAR) → algebra.**
   - Commutative lifts (Koopman, Liouville) are canonical given the flow, but they are
     **commutative**. On them EA-0's double commutators vanish identically, and the P-5/P-6 seed
     and closure machinery has nothing to act on.
   - **Leaning (not proposed): toward Route C, the category boundary.** That needs the §4 table
     verified.

## §1 The two sides, stated exactly from the record

**Side L — the earned Level-0 substrate:**
- **L0-1a/b:** ẋ = −Kx on Λ = N sites (the C1-a chain, `calc/c1_seam.py: build_K`; K = pin·𝟙 +
  weighted Laplacian; real symmetric, positive definite with the gap).
- **L0-1c:** ẋ = −∇V, with V = ½xᵀK_bx + βΣᵢxᵢ⁴ (`L0_1C_CHARTER_01.md:65-67`).
- **Properties:** classical, deterministic, first order, dissipative. **One real coordinate per
  site.**
- **Observables:** coordinate functionals, notably the retained site x₁ and its response kernel
  k(τ) = e₁ᵀe^{−Kτ}e₁.
- **Asymptotics:** the point mass δ₀.
- **Declared extension, not part of the earned deterministic core:** L0-1e's stochastic members,
  dx = −Kx dt + B dW with Q = 2·diag(T_i), T_i ≥ 0. Noise there is a *declared datum*, and whether
  it is primitive or derived is unformulable at second order (S-1).

**Side A — the later algebraic access formalism:**
- (𝒜, 𝒞, ρ, 𝒳) on finite **quantum spin** algebras (P-5, P-6: "exact finite spin models"): unitary
  H, density operators, seed S, closure cl(S;H).
- EA-0: P_ρ and P_ρ𝒜_xP_ρ.
- P-2 to P-4: influence functionals, with the commutator face scaled by ħ.

**Side G — geometry recovery:**
- G-2/GS-1: geometry from the K-resolvent at declared access sets (unit masses; K = weighted
  Laplacian + pins).
- The quantum leg is validated to equal classical hopping (`G2_SPECTRAL_CHARTER_01.md:94-100`).

**One structural fact that lowers the seed problem on Side L.** With **one coordinate per site**,
"which operator at the coupled site" (P-6's seed within a site) has no content: everything
observable at site i is a function of xᵢ. **On Side L, the seed problem reduces to "which
sites"**, i.e. to the net's index set.

## §2 The four levels, restated natively on Side L

Mirrors EA-0 §2, with no quantum objects.

| Level | Side-L object | Example |
|---|---|---|
| (a) values | x(t), and functions and correlations of it | the orbit; k(τ) evaluated along it |
| (b) reach | the orbit {e^{−Kt}x₀}; the smallest K-invariant subspace containing x₀ (Krylov 𝒦(x₀) = span{Kʲx₀}) | global |
| (c) access | the distinguishability/observability structure available from declared local coordinate sets, **as a function of the state** | CL-3 to CL-7 below |
| (d) geometry | adjacency/distance recovered from (c) together with the dynamics | G-2/GS-1-type recovery |

The EA-0 trap carries over: **any ρ-dependence (here x-dependence) that enters only through values
on a fixed structure is TRIVIAL for access.**

## §3 Classical route: candidates, kill tests, front-run identities

**Kill tests (owner 7.1):**
- **K1** intrinsic to the earned data?
- **K2** needs an access seed (beyond the net's index set)?
- **K3** state-dependent *structurally*, not only in values?
- **K4** local/relational?
- **K5** covariant under the correct classical transformations? That means site permutations
  preserving K's pattern and site-local reparametrizations xᵢ ↦ φᵢ(xᵢ), **not** GL(N), which
  would erase locality.
- **K6** reconstructs the earned geometry in G-2/GS-1 language?
- **K7** collapses for the linear deterministic substrate?

| # | Candidate | Front-run (linear, L0-1a/b) | Front-run (L0-1c, on-site quartic) | Open items |
|---|---|---|---|---|
| CL-1 | Reachable set / orbit / Krylov 𝒦(x₀) | The classical analogue of EA-0 L1/L3: for K with simple spectrum, 𝒦(x₀) = the span of eigenvectors that x₀ overlaps. It is ℝᴺ for generic x₀. **Global** (K4 ✗). Asymptote δ₀. | Orbits of a nonlinear flow; no linear Krylov analogue. | TRIVIAL/IDENTITY as access (non-relational). |
| CL-2 | Invariant subspaces / manifolds | The spectral subspaces of K: **state-independent**. The state only selects which one it lies on. That is the *generator-carried by identity* pattern again. | Stable/slow manifolds of the vector field: also state-independent objects. | Same identity as EA-0 C-8 §9.3–4: carried by construction. |
| CL-3 | Observability from declared local coordinates (Kalman: 𝒪_A = span{(Kᵀ)ʲe_a : a ∈ A}; nonlinear: the observability codistribution d𝒪_A(x) = span{dL_fʲ x_a}) | **State-independent** (linear systems). The seedless family over single sites {𝒪_i}: for a connected chain with every eigenvector overlapping e_i, each site observes everything, so it collapses. **K7 ✓ (collapse).** | The codistribution rank can depend on x only on proper algebraic subsets. Generic rank is inherited from the linear part near 0. **Whether any x drops rank is to be verified.** | The one candidate that can be *structurally* state-dependent on Side L, if rank drops occur. It needs the index set A (a net-level choice). |
| CL-4 | Controllability / accessibility from local inputs (span{Kʲe_i}; Lie-bracket accessibility distribution) | State-independent; the same collapse. | Accessibility distribution: state-dependent only through rank drops (to verify). | It requires declared input sites, which are **seed-like** unless taken as the whole net family. |
| CL-5 | Indistinguishability of initial conditions under declared local observables (x₀ ~_A x₀′ iff the same future readout) | The quotient ℝᴺ / 𝒰_A (𝒰_A the unobservable subspace) is **state-independent**; trivial when 𝒰_A = 0. | A genuinely nonlinear relation. Its classes can be state-dependent where CL-3's rank drops. | The same live content as CL-3. |
| CL-6 | Local response / Jacobian structure J(x) = Df(x) | J = −K is constant, so the **graph is state-independent**. | J(x) = −K_b − 12β·diag(xᵢ²): **the off-diagonal support is fixed for all x; only on-site stiffness varies.** The effective transmission of a perturbation through a highly excited (stiff) site is suppressed continuously, a *soft* blocking. | **The central open question: value or structure?** Continuous reweighting of a fixed support. The owner's criterion decides. The draft does not. |
| CL-7 | State-dependent distinguishable perturbations: the variational Gramian W_{ij}(x₀,T) of δẋ = J(x(t))δx (how well a perturbation at j is seen at i along the base trajectory) | Equals the linear Gramian: **state-independent**. | Varies continuously with x₀ through the J(x(t)) weights. The support is generically unchanged. | The same value-vs-structure question as CL-6. |
| CL-8 | Quotient by identical future accessible trajectories | = CL-5. | = CL-5. | — |

**Classical-route summary (front-run):**
- **Linear (L0-1a/b):** every candidate collapses by identity. That means TRIVIAL/IDENTITY on the
  earned linear substrate, and here the label is native, not a category error.
- **Nonlinear (L0-1c):** supports are fixed. Structural state-dependence can come only from
  **rank drops** (CL-3, CL-4, CL-5), which are unverified. Otherwise it is continuous reweighting
  (CL-6, CL-7), which falls under the owner's value-vs-structure ruling.
- **K6 (geometry):** CL-3/CL-6 on the linear substrate carry exactly K's support and resolvent
  data. That is what G-2/GS-1 consume, so **the earned geometry is reconstructible at K-level
  with declared access sets, without any lift.**

## §4 Lift route: candidates and pricing

**Pricing questions per lift (owner 7.2):** Is it mathematically canonical? Physically unique?
Faithful? Local-net preserving? State-selection preserving? Merely a change of representation? An
additional postulate?

| # | Lift | Canonical? | Physically unique? | Faithful? | Net-preserving? | Output algebra | Front-run price |
|---|---|---|---|---|---|---|---|
| LF-1 | Koopman, U^t f = f∘φ_t | Given a function space. **Choosing the space and measure is a choice:** L²(δ₀) is one-dimensional (degenerate); on L²(Lebesgue) U^t is not unitary (volume contraction) | No | Yes (on rich enough spaces) | Yes (functions of xᵢ) | **Commutative** | REPRESENTATIONAL on linear observables (U^t on linear functionals is the dual flow e^{−Kᵀt}). Otherwise NONUNIQUE (the function-space choice). It cannot reach P-5/P-6's noncommutative machinery. |
| LF-2 | Liouville / continuity equation on densities | Yes, given the vector field (standard) | Needs the **ensemble postulate**: a state is a measure, not a trajectory | Yes | Yes (marginals) | **Commutative** | ADDITIONAL POSTULATE (the ensemble). The support analogue of reach → δ₀. |
| LF-3 | Stochastic (OU / Fokker–Planck) | Given Q | **Q is a declared datum** (L0-1e). Primitive vs derived is unformulable at second order (S-1) | — | Yes | **Commutative** | ADDITIONAL DATUM. Full support iff (K,B) controllable (standard). Not earned for the deterministic core. |
| LF-4 | Conservative dilation (Ford–Kac–Mazur-type bath; S-1's attached theorem) | **No:** many baths reproduce the same K | No | Reproduces the reduced correlation (S-1) | Adds bath sites (the net is extended) | Classical Hamiltonian (Poisson) | NONUNIQUE. It is the first step needed before any quantization, since the first-order dissipative flow has no symplectic form. |
| LF-5 | Quantization of a Hamiltonian system (after LF-4) | Not canonical beyond quadratic order (standard ordering obstructions) | Needs **ħ (supplied**, P-2 "located, not generated") | — | Yes, if quantized site-locally | **Noncommutative** (CCR) | ADDITIONAL POSTULATE (ħ) + NONUNIQUE (LF-4). |
| LF-6 | Second quantization of the contraction semigroup e^{−Kt} (quasi-free CP semigroup; standard functor) | **Yes, as a functor** on linear contractions | Needs a **choice of statistics** (CCR vs CAR) and **ħ** | Yes on one-particle data | Yes | **Noncommutative** | CRITERION (statistics) + ħ. It is the most canonical noncommutative lift available for the linear core. Worth verifying first. |

**Lift-route summary (front-run):**
- Every **commutative** lift (LF-1 to LF-3) is at best canonical-given-a-choice, and it cannot
  host the P-5/P-6/EA-0 noncommutative machinery. On a commutative algebra all commutators vanish,
  so Γ is empty (verifier §1a).
- Every **noncommutative** lift (LF-5, LF-6) needs at least ħ (supplied) plus a statistics choice
  or a non-unique dilation.
- **No lift is forced by earned structure** on this reading. A UNIQUE-LIFT outcome would need an
  in-house argument that singles out LF-6's statistics and ħ, and none exists on the record.

## §5 Rival state-derived mechanisms: kept alive, gated by the bridge

| Rival (from the verifier) | Is its state object available on Side L? | Front-run |
|---|---|---|
| Eigenspaces of a state-like object | Only after LF-2/LF-3 (a measure or Gaussian covariance Σ). In LF-3, Σ solves KΣ + ΣKᵀ = Q | Available only as priced. Σ's eigenspaces are state-dependent through Q, so they are (a)-type unless structural |
| Modular flow | Only after a lift. **On a commutative lift the modular automorphism group is trivial** (standard) | Dies on LF-1 to LF-3. Survives only on LF-5/LF-6 (priced) |
| Supports of local marginals | After LF-2/LF-3: supports of the marginal measures of xᵢ | For a deterministic δ-state, trivial. For Gaussian LF-3, full whenever Tᵢ > 0 |
| Γ′ (compressed operator systems) | Only on noncommutative lifts | Priced as LF-5/LF-6 |

**Rule (owner 7.3):** none of these rivals enters the Side-L argument unless a bridge makes its
object available. That keeps the reach-based construction from winning by default.

## §6 Outcome taxonomy (owner 7.4) and what would decide it

| Outcome | What would have to be shown |
|---|---|
| **DIRECT-CLASSICAL** | A useful, structurally state-dependent, seedless-relative-to-net access object exists natively on Side L. **Most likely candidates:** CL-3/CL-5 rank drops on L0-1c, or an owner ruling that CL-6/CL-7 reweighting counts as structural. |
| **REPRESENTATIONAL-LIFT** | A lift exists but only re-expresses Side-L content (e.g. LF-1 on linear observables). |
| **UNIQUE-LIFT** | One lift is forced by earned structure. **Nothing on the record forces one.** |
| **NONUNIQUE-LIFT** | Several inequivalent lifts survive (LF-4, LF-6 statistics). |
| **SEED/CRITERION-SMUGGLED** | Any lift or candidate that needs a supplied function space, statistics, ħ or seed and presents it as derived. |
| **TRIVIAL/IDENTITY** | The classical route collapses (it does on the linear substrate, §3). |
| **UNFORMULABLE** | No well-defined bridge question can be posed without supplied structure. |

**No terminal is proposed in this draft.**
- The front-run reading suggests a composite: TRIVIAL/IDENTITY for the classical route on the
  linear core; an open value-vs-structure question on L0-1c; and NONUNIQUE-LIFT plus supplied ħ on
  the lift route.
- That composite is **not** adopted here.

## §7 Dependency consequence (owner 7.5)

| Route | Condition for it to be chosen (after this gate) |
|---|---|
| **A: generator origin / S-5** | Access, order and geometry repeatedly reduce to genuine generator structure *within a common earned formalism*. On Side L, CL-2 and CL-3/CL-6 already reduce to K (or V) by identity. Whether that is a finding or a tautology must be judged as it was for EA-0. |
| **B: state-derived access** | A seedless structural notion survives independently of generator-sector reach. On Side L only CL-3/CL-5 rank drops, or a ruling on CL-6/CL-7, could supply one. |
| **C: category boundary** | Classical Level-0 and the later algebraic/quantum structure cannot be connected without a new supplied principle. The front-run lift table points this way (ħ and statistics supplied; dilation non-unique). **Route C would itself be an important result.** |

## §8 Proposed next steps within the gate (for owner decision; none executed)

1. **One independent verification pass** of §0 and §§3–5: the front-run identities, the LF
   pricing, and the modular-triviality and marginal-support statements.
2. **An owner ruling on the value-vs-structure line** for Side L. Does continuous, state-dependent
   reweighting of a fixed support (CL-6/CL-7) count as structural access? The classical route's
   non-linear branch turns on it.
3. **A theorem task, if authorized:** do CL-3/CL-4 rank drops occur for L0-1c's V, and on what
   set? This can be settled algebraically (Lie derivatives of polynomial vector fields); it needs
   no member simulation.

**HARD STOP** for owner review. No new numerical physics. No EA-1. No S-5 execution.
