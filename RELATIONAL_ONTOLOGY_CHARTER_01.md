# RELATIONAL ONTOLOGY ATTACK — CHARTER + P-1 PRE-REGISTRATION (frozen before evaluation)

**Date:** 2026-09-25 · **Chartered by:** owner, verbatim central elements:

> "Primitive reality may be relational dynamical structure, not a
> constitutive medium. Treat the following only as a candidate, not an
> assumption: Reality₀ = (𝒜, 𝒞, ρ) … The central problem is therefore:
> **Can the system/bath partition itself be derived from deeper correlation
> structure, rather than postulated?** … Most important: find a calculation
> that distinguishes A. genuine emergent subsystem structure, B. subsystem
> structure as representational/gauge freedom, C. fundamentally
> observer-relative subsystem structure. **If the proposed relational
> ontology cannot be made mathematically sharper than a philosophical
> restatement, say so.** … The goal is not to make GRUT work."

**Binding constraints:** the hypothesis is a candidate and is ALLOWED TO
FAIL; the old responsive-medium architecture is not the default; locality,
Lorentz invariance, finite dimensionality, tensor factorization, and a
preferred substrate are NOT assumed; no prediction campaign; Λ_R, Matsubara,
Π₀, U5 stay fenced. Register untouched; ledger 0.

**Recorded anchors this attack builds on (not re-derived):** CPR
uniqueness-given-existence as the lone positive control (finite type I,
existence measure-zero generically); ROOT-1's Wilsonian countermodel (the
kernel is partition-dependent — an invariant criterion has real work to do);
the AQFT deletion test ("remove every partition-valued object from the
inputs; if the derivation still runs, it is a candidate"); the U3 residue
(the well-posed part of "why this split" is the choice-of-slow-variables
problem); RRT-0's sector-selection UNRESOLVED and reference ABSENT.

---

## 1. INSTRUMENT P-1 — PARTITION SELECTION FROM CORRELATION STRUCTURE

**Scope declaration (epistemic level, fixed now):** P-1 is a TOY-CLASS
structural probe in the exactly solvable Gaussian world — closed quadratic
Hamiltonians H = ½pᵀp + ½qᵀVq, ground states, exact reduced dynamics. Its
verdict is about **whether the proposed invariant-criterion class can select
subsystems at all** in worlds where everything is computable, and about
which of A/B/C the class exhibits there. It says nothing directly about
reality; it makes the A/B/C distinction operational, which is what the
owner asked for. A criterion class that cannot select subsystems even here
cannot do so anywhere.

### 1.1 Testbeds (frozen; N = 10 sites; fixed seed 20260925 for X3)

- **X1 — homogeneous ring:** V = periodic tridiagonal, uniform diagonal ω₀²+2κ,
  off-diagonal −κ (ω₀ = 1, κ = 0.5). Translation-invariant: any legitimate
  intrinsic criterion must return scores constant on translation orbits.
  **Role: B-detector and rigging control** — a criterion that selects a
  unique partition here is broken, and the run HALTS on it.
- **X2 — impurity chain:** open chain, uniform bulk (ω₀ = 1, κ = 0.5), one
  distinguished light oscillator at site 0 (ω_imp² = 0.09) coupled weakly
  (g = 0.1) to site 1. The physically "intended" subsystem is {0} — but the
  instrument is NOT told this; whether the criteria find it is the test.
  **Role: A-detector.**
- **X3 — random network:** V = AᵀA + 0.1·I with A entries i.i.d. from the
  seeded generator (positive definite, no designed structure).
  **Role: C-detector** (CPR: generic existence is measure-zero).

### 1.2 Partition family (frozen)

All decompositions X = S ∪ E with S a subset of sites, |S| ∈ {1, 2}
(10 + 45 = 55 partitions per testbed). No other family is consulted.

### 1.3 The criteria (frozen definitions; three INTRINSIC, one ANCHORED)

For each partition, all computed exactly from V (eigendecomposition):

- **C1 — memory-kernel realization rank (intrinsic).** Eliminating E gives
  the exact GLE kernel K_S(t) = V_SE Ω_E⁻¹ sin(Ω_E t) V_ES,
  Ω_E = √V_EE — a sum over E-modes μ with coupling weights
  w_μ = |V_SE e_μ|²/ω_μ. Score = participation rank
  PR = (Σw_μ)²/Σw_μ² (the effective number of bath modes S sees),
  **minimized**: a natural subsystem is one whose environment acts through
  few effective modes per system dimension (score normalized by |S|).
- **C2 — ground-state mutual information per boundary (intrinsic).**
  I(S:E) computed exactly from the ground-state covariance (symplectic
  eigenvalues ν = sqrt(eig((V^{-1/2})_SS(V^{1/2})_SS))/... standard Gaussian
  formulae), **minimized per site of S**: a natural subsystem is minimally
  entangled with its complement per unit size.
- **C3 — causal cohesion (intrinsic).** From the full propagator
  G(t) = Ω⁻¹sin(Ωt): cohesion = ‖G_SS(t*)‖_F / ‖G_SE(t*)‖_F at declared
  t* = 2.0, **maximized**: a natural subsystem responds to itself more than
  it leaks.
- **C4 — anchored minimal realization.** A designated probe observable is
  fixed per testbed (X1: site 0 position — an arbitrary anchor, disclosed as
  such; X2: site 0; X3: site argmax diag(V)). Score: the smallest |S|
  containing the probe such that S's isolated dynamics (V_SS alone)
  reproduces the probe's exact autocorrelation to declared tolerance 10%
  over t ∈ [0, 10]; ties broken by C1. **C4 exists to expose
  observer-relativity:** it always selects something, BY CONSTRUCTION,
  because it consumes an anchor.

### 1.4 Pre-registered decision rules (before any number exists)

Per testbed, per intrinsic criterion: the winner and the **selection gap**
g = (runner-up score − winner score)/|winner score| (orientation per
criterion). "SELECTS" = g ≥ 0.20 AND the winner is stable under the
coarse-graining check (2:1 blocking of the chain; the winner's image must
win in the blocked system by the same rule). Symmetry orbits in X1 are
handled first: scores constant on an orbit to 10⁻⁶ count as a TIE-ORBIT,
which is correct behavior, not a selection.

**Signatures (exhaustive):**

- **A-signature:** in X2, at least two of C1–C3 SELECT the SAME partition,
  and in X1 all intrinsic criteria return TIE-ORBITs. (Whether the selected
  partition is the impurity is reported but not required — no rigging.)
- **B-signature:** intrinsic criteria select only up to ties/orbits or
  finite families in all testbeds, coherently (same families).
- **C-signature:** intrinsic criteria disagree with each other about the
  winner (or select nothing stable) in X2 or X3, while C4 selects — i.e.,
  selection happens only when an anchor is consumed.
- **NOT-SHARPER-THAN-PHILOSOPHY:** if any verdict above flips under the
  declared tolerance moved by ±50% (g threshold 0.10–0.30, C4 tolerance
  5–15%), the instrument reports exactly that, per the owner's requirement.

### 1.5 Controls (halt on miss) and fences

- Eigensolver control: reproduce the analytic spectrum of the uniform ring
  (ω_k² = ω₀² + 4κ sin²(πk/N)) to 10⁻⁹.
- GLE control: for a 2-oscillator system, the exact kernel
  K(t) = g² sin(ω_E t)/ω_E reproduced from the general formula.
- Gaussian-MI control: pure global state ⇒ S_vN(S) = S_vN(E) to 10⁻⁹.
- X1 rigging control (above): unique selection in X1 HALTS the run.
- NO-DEFAULT fence: the responsive-medium architecture appears nowhere in
  P-1; nothing in the code knows which answer GRUT would prefer.
- NO-CAMPAIGN fence: P-1 measures the criterion class; it proposes no
  ontology, evaluates no discriminator, changes no register field.

## 2. THE DERIVATIONAL LEGS (report sections, no computation)

Mapped against the mined record, statuses per the owner's five classes:
observer/system/environment as effective roles of one structure (against
CLPW's recorded direction); geometry-from-correlations (against the 1Space
sevenfold non-circularity failure and the ROOT-0 no-sub-QFT finding);
whether noncommutativity must be primitive (against: complexness =
formulation choice; the linear no-go; the III₁-vs-finite-type-I
obstruction; noncommutativity itself UNTESTED); whether the kernel, memory,
dissipation, and non-stationarity results are natural in the relational
picture (against the K(t,t′) chain just completed).

## 3. DELIVERABLES AND STOP

1. `calc/partition_selection_p1.py` — pure stdlib, self-checking, emits
   `PARTITION_SELECTION_P1_RESULT.json` (sha-hashed); signature computed
   mechanically by §1.4.
2. `RELATIONAL_ONTOLOGY_MAP_01.md` — the P-1 verdict; the new dependency
   graph (every arrow DERIVED / CONDITIONALLY DERIVED / EMPIRICAL INPUT /
   OPEN / DISDERIVED); the minimum mathematics of (𝒜,𝒞,ρ) **or** the
   honest statement that it is not yet sharper than philosophy.
3. **HARD STOP at the map** (the waiting decision: the owner reads the
   signature and the graph and rules on the relational candidate). Fenced
   routes untouched throughout.
