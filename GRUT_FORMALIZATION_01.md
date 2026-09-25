# GRUT FORMALIZATION 01 — the mathematical formulation of the theory, as rigorously as the record permits

**Date:** 2026-09-25 · **Authority:** owner ruling accepting Draft 02:
*"the next authorized work should be formalization of the mathematical
GRUT architecture, not another isolated experiment."* · **Status:
FORMALIZATION, NOTHING BANKED. Not for external distribution** (D-1
standing direction). Derived from `GRUT_THEORY_PAPER_WORKING_02.md`;
evidence flows through it to the frozen record. This document defines
objects and maps; it computes nothing and promotes nothing.

**The task (owner, verbatim in force):**

> Given these primitive inputs and these admitted microscopic classes,
> these are the mathematical objects and maps that constitute GRUT —
> with every map explicitly constructive, conditional, or terminating
> at an input or open seam.

and the deeper question the formalization must make precise:

> Does the assembled hierarchy actually constitute one theory, or is
> it still a collection of compatible constructions?

(§6 states and answers it at the record's strength.)

---

## 0. GRADING VOCABULARY (binding on every formal statement below)

Formal notation must not smuggle strength the record does not have.
Every definition is exact as a definition; every *statement* carries
exactly one grade:

- **[IDENTITY]** — mathematically exact; provable by algebra from the
  definitions (e.g. dimensional analysis, projector algebra, state
  positivity restatements). Identities are content-bearing only as
  classifications.
- **[DERIVED-IN-CLASS]** — established by a frozen instrument at check
  level, within the stated model class, at the stated tolerances.
  Not a theorem about all models; the class is part of the statement.
- **[FAMILY-FACT]** — demonstrated across a tested family (e.g. the
  infinite-volume limits): stronger than an example, weaker than a
  limit theorem. No general proof exists in the record.
- **[SUPPLIED]** — a primitive input (working term axioms-of-supply;
  external term *primitive inputs / irreducible structural inputs*),
  indexed I1–I11 per Draft 02 Part III.
- **[UNDEFINED]** — a composition or object the theory does not
  currently define; the seams live here.

A red gate blocks any statement that would contradict it; the red
register of Draft 02 IV.1 is carried unchanged.

---

## 1. THE ADMITTED MODEL CLASSES AND THE GRUT DATUM

**Definition 1 (admitted microscopic classes).** The record's
derivations live in the union 𝕆 = 𝕆_G ∪ 𝕆_S ∪ 𝕆_c of:

- **𝕆_G (quadratic/Gaussian networks):** finite site set X with a
  bounded-degree neighborhood structure 𝒩; real symmetric stiffness
  K ≥ 0 supported on 𝒩 (springs) plus on-site pins; unit masses;
  classical dynamics ẍ = −Kx, or the first-order passive form
  ẋ = Ax with A + Aᵀ ≤ 0; quantum member: the corresponding quadratic
  bosonic Hamiltonian. (The class of P-2, D-1, G-1/G-2, GS-1, SX-1,
  CA-1, RS-1, the kernel instruments.)
- **𝕆_S (finite spin/fermion systems):** finite tensor products of
  finite-dimensional site algebras with local Hamiltonians (Pauli
  classes of P-3, P-4, S4-1, FS-1; free-fermion members of CA-1/RS-1).
- **𝕆_c (declared continuum sectors):** dispersive continuum fields
  ω(p) declared per sector (the CP-1/EQ-1/TT-1 kinematic classes;
  tree-level 2→1 for the TT channel).

**P0 (admitted principles, definitional for 𝕆):** strict locality;
finite microscopic content per site; first-order autonomy (or the
quadratic second-order equivalent); passivity; time-translation
invariance of the microscopic law; standard open-system reduction.
The time-translation item is flagged: it bounds the domain (seam S1).

**Definition 2 (the GRUT datum).** A GRUT datum is a tuple

    𝔇 = ( M, 𝔞, ρ, ι )

where M ∈ 𝕆; 𝔞 is an **access assignment** (Definition 6): a seed
subalgebra together with its induced partition/retained sector; ρ is a
state on M's algebra; and ι is an **inventory assignment**: a choice
of the primitive inputs I1–I11 insofar as the construction at hand
consumes them (the probe P*, the light-cone relation, dispersion
content, ℏ, boundary data, …). The slots (M, 𝔞, ρ) are called the
**core datum**; ι is the **conditional datum**.

Everything in GRUT is a function of 𝔇. The typing of §5 records which
slots each map actually reads — this typing is the formal content of
"generative core vs conditional branch."

---

## 2. THE OBJECTS

### Definition 3 — 𝒪_local (the microscopic layer)

𝒪_local is the pair (M, P0), M ∈ 𝕆. The theory asserts **no substrate
ontology**: the record fixes a constraint system on candidate
substrates (the A1–A9 list of the ontology reconstruction, carried by
reference), not a preferred M. **[DERIVED-IN-CLASS / SUPPLIED mixture,
per A1–A9.]**

### Definition 4 — 𝒞_continuum (the continuum layer)

For finite M ∈ 𝕆 with retained sector R given by 𝔞, the reduction map
yields the generalized Langevin form

    q̇(t) = −∫₀ᵗ K_R(t−s) q(s) ds + drive,
    K_R(t) = Σ_k (v_{1k})² e^{λ_k t}.

𝒞_continuum is the assignment (M, 𝔞) ↦ (retained dynamics, K_R, ρ(τ))
together with its infinite-volume limits, where in the limit
K_R(t) = ∫ e^(−t/τ) dρ(τ) with ρ ≥ 0.

**F4.1** For finite M the reduction is exact and K_R has the stated
spectral form; the realization dimension equals the number of
*distinct* eliminated modes. **[DERIVED-IN-CLASS]** (P3 1.4e-16; P4
distinct-modes law with degenerate-pair control; E4a).

**F4.2** In the tested families, the infinite-volume limit produces
continuous spectra and irreversible response with late-time class
t^(−d/2); no damping is inserted. **[FAMILY-FACT]** (continuum-origin
6/6; infinite-bath 4/4; irreversibility-origin 3/4).

**F4.3** ρ ≥ 0 (Bernstein–Widder class) and repeated poles are
excluded by passivity. **[DERIVED-IN-CLASS]** (E5b). ρ is uniquely
recoverable from K_R iff all spectral moments are finite; the
gravitational kernels of interest are heavy-tailed, outside the
uniqueness class; the support structure is observable
unconditionally. **[DERIVED-IN-CLASS]** (E2a/E2b).

**F4.4 (domain bound — seam S1).** 𝒞_continuum is defined on
stationary backgrounds only. On the declared cosmological background
the exact kernel is two-time at order unity (best Δt-only residual
R = 0.516; same-lag drift 1.53) and no local transport rule extends
the stationary object (licensed lags ≲ 0.25/H₀, dead by ~0.8/H₀). The
composite "Definition 4 on a non-stationary background" is
**[UNDEFINED]**.

### Definition 5 — ℐ (the influence structure)

For (M, 𝔞, ρ), let 𝒜_R be the *-algebra generated by the retained
variables under the dynamics. The influence structure is the hierarchy

    ℐ(𝔇) = { C_n }_{n≥1},   C_n = connected n-point multi-time
                              correlation/response functionals of 𝒜_R in ρ,

with Gaussian face (K, N) ≡ (J, ν) (response/dissipation and
fluctuation spectra).

**F5.1 (admissibility, Gaussian).** Realizable Gaussian influence data
satisfy exactly

    𝔠_Gauss = { (J, ν) : J(ω) ≥ 0 , ν(ω) ≥ ℏ J(ω)/2 } ,

with minimality probed constructively (interior filled, incl. a
non-KMS profile; boundary saturated by the vacuum; three candidate
extra constraints counterexampled). **[DERIVED-IN-CLASS]** (P-2,
16/16). ℏ enters as the floor height: **[SUPPLIED]** (I7); the
classical branch is the same cone with the floor removed.

**F5.2 (admissibility, general).** At matrix level the cone lifts to
ν ± J/2 ≥ 0; at hierarchy level the single positive object is
complete positive-definiteness of ℐ — and this **is** state
positivity on 𝒜_R. **[IDENTITY]** (P-3/P-4; NULL-AS-NEW-PRINCIPLE:
formalization must not present it as an independent axiom).

**F5.3 (non-sufficiency of the face).** (K, N) does not determine ℐ:
exactly (K,N)-matched models split at κ₄ (coherence split 0.338), and
matched-through-order-k pairs first differ at the first unmatched
order (constructive at orders 4/6/8; the order-8 window gate **red**).
Finite matching never certifies; full-hierarchy matching certifies
in-class. **[DERIVED-IN-CLASS]** (P-3, P-4).

**F5.4 (interface completeness).** For declared access, in-class, no
physical difference exists that ℐ does not track (no
constraint-satisfying pair with an influence-untracked difference was
constructible). **[DERIVED-IN-CLASS]** (P-4; completeness OF THE
INTERFACE, never beyond access).

**F5.5 (dynamical selection).** The map
sector ↦ exponent class of its influence data is given by locality +
symmetry additive power counting (+2 per vertex momentum power;
phase-space increment d−1; +2m per order-m cancellation), acting
per-branch, with min-dominance masking at eigenvalue level (H3 gate
**red**, the masking law the diagnostic). Amplitudes and states are
never selected. **[DERIVED-IN-CLASS]** (S-1, P-3); the point-in-class
is **[SUPPLIED]** (I10).

### Definition 6 — 𝔄 (the access structure; cross-cutting)

An access assignment is 𝔞 = (S, 𝒜_S, ∂), where S ⊂ 𝒜 is a seed
subalgebra; 𝒜_S is its dynamically generated closure (the algebra
generated by ∪_t α_t(S), with the bicommutant as the symmetry-
respecting closure); and ∂ is the (possibly empty) set of
boundary-change events. 𝔄 acts on the theory in three roles:

- **(partition)** 𝔞 induces the retained sector consumed by
  Definition 4;
- **(reach)** 𝔞 restricts the interface: the accessible data are
  ℐ(𝔇)|_𝔞 ;
- **(events)** ∂ carries physical content (below).

**F6.1 (closure canonical).** 𝒜_S is canonical given S.
**[DERIVED-IN-CLASS]** (P-5).

**F6.2 (seed non-derivable, as attacked).** No tested functional
(minimality; dynamical closure) selects S from the dynamics: closure
is non-injective (identical closures, physically different seeds,
0.287), minimal sufficient seeds are path-dependent, and the
symmetry-degenerate control is unselectable (companion gate **red** at
0.0). S is **[SUPPLIED]** (I1). **[DERIVED-IN-CLASS]** for the
refutations (P-6).

**F6.3 (access-relativity).** If ℐ(𝔇₁)|_𝔞 = ℐ(𝔇₂)|_𝔞 then no
𝔞-experiment distinguishes 𝔇₁ from 𝔇₂ — including genuinely
non-isomorphic microscopic models (theorem-grade in 𝕆_G: identical
influence data from 9- and 11-dimensional baths, all S-local
observables equal to 4.5e-15, probes included). **[DERIVED-IN-CLASS]**
(D-1). Corollaries: medium-vs-relational and factorization/embedding
vocabularies are representational at fixed accessible data.

**F6.4 (event physicality).** Elements of ∂ are exactly where
in-access-identical models become distinguishable (post-quench split
0.38 after access extension). **[DERIVED-IN-CLASS]** (P-5).

**F6.5 (the subsystem functional).** Subsystemhood is a functional
𝔖[𝒜, dynamics, ρ], not a property of 𝒜; natural criteria (rank /
entanglement / cohesion) are inequivalent and coincide only where
structure is strong; selection is regime-trichotomous
(structured / symmetric / generic). **[DERIVED-IN-CLASS]** (P-1).

### Definition 7 — 𝒢 (the recoverable geometric layer)

For (ℐ|_𝔞), the recoverable geometry is

    𝒢(𝔇) = ( d_spec , d_hop , g_metric , topology data )|_𝔞 ,

the tuple of outputs of the certified functionals: spectral-dimension
estimators (heat-kernel/shell), the walk/moment hop metric, the
resistance/metric-density form, and local closed-walk topology
invariants — each defined **relative to 𝔞**.

**F7.1 (recovery).** In 𝕆_G ∪ 𝕆_S the functionals recover dimension
(1.000/2.000/2.942/1.000-quantum), hop metrics (anchors within 0.004;
exact additive integer triples), and metric density (1e-9), where the
arrival-time route fails (G-1's eight gates **red**, obstruction
located). **[DERIVED-IN-CLASS]** (G-2).

**F7.2 (selection, by access class).** With full site-resolved access,
𝒢 determines the model up to relabeling and eliminates isospectral
impostors; with dynamic boundary access, the ω²-order response
eliminates star–mesh equivalents that static data cannot; with static
boundary access it cannot; with single-site access non-isometric
families are not eliminated. **[DERIVED-IN-CLASS]** (GS-1 table).

**F7.3 (topology horizon).** Local walk data determine topology only
above circumference order (first distinguishing order = n, exactly).
**[DERIVED-IN-CLASS]** (G-2, GS-1).

**F7.4 (unit change).** A transformation is a pure unit change iff
every dimensionless accessible datum is invariant. **[IDENTITY]**
(operationalized dimensional analysis, SX-1). Under it: a uniform
co-stretch is a unit change **[IDENTITY]**; a constant rescaling need
not be (rigid stretch observable, 0.013) **[DERIVED-IN-CLASS]**; which
one a constant probe performs is the co-stretch declaration
**[SUPPLIED]** (I5).

**F7.5.** "Absolute geometry" is not an object of GRUT: no functional
of 𝔇 defines it. **[UNDEFINED]** (deliberately).

### Definition 8 — ℱ_eff (the effective sector/probe layer; conditional)

ℱ_eff assembles: sector classes inside 𝔠; the probe
P* = (massless, gauge/Lorentz-redundant field, universal reach)
**[SUPPLIED]** (I3, I4); the carrier identification CARRIER
**[SUPPLIED]** (I2, reduced to a coincidence of 𝔞-seeds); and the
coupling constraints these buy:

**F8.1** C_cons (the probe couples to a conserved local current)
follows from 𝔠-positivity of probe-mediated exchange **for P* and only
for P*** (massless exchange goes negative for non-conserved sources;
massive stays positive; every earned constant-level selector admits a
non-conserved coupling). **[DERIVED-IN-CLASS given I3]** (CC-1).

**F8.2** Clock universality is forced under exchange (≥ 0.13 vs 9e-16;
g → 0 continuous) and unforced — while observable — for genuinely
decoupled sectors. **[DERIVED-IN-CLASS given I4 / SUPPLIED beyond]**
(U-1, S4-1).

**F8.3** Given C_cons, O ~ H is forced for generic non-integrable
sectors; free/integrable sectors carry 2R-charge towers and escape —
**loophole L1**: the gravity-side retained sector is in the escape
class; GeoInv is a recorded candidate, unpromoted.
**[DERIVED-IN-CLASS / UNRESOLVED]** (S4-1, FS-1).

**F8.4** Given CARRIER + P*, earned structure selects the retained
sector's **class** — gapless, z = 1, locally accessible Goldstone —
by eliminating genuinely different candidates (fermions under local
access, flexural, gapped; the z = 2 magnon by the probe's IR
symmetric-stress requirement), with one gate **red** (flexural count).
The member, and its dispersion curvature, are **[SUPPLIED /
UNDEFINED]** (I11). **[DERIVED-IN-CLASS conditional]** (RS-1, CA-1).

### Definition 9 — 𝒢_grav (the graviton-response sector; conditional)

Given ℱ_eff with sector Σ and probe P*, 𝒢_grav consists of:

- the hierarchy point (K, N)_grav ∈ 𝔠 with the vacuum on the floor
  **[DERIVED-IN-CLASS]** (GR-1);
- the exponent-class occupancy: selected-by-structure-in-class
  (counterfactual battery; branch elimination structural); ω⁷ derived
  within class at exponent and coefficient level on the adjudicator
  track, **occupancy evidence only** program-wide; class-4 open with
  the obstruction = I1–I6 load-bearing; κ discharged
  **[DERIVED-IN-CLASS / gate open]**;
- the TT vertex functional: for on-shell kinematics
  (k = p₁+p₂, Ω = |k|), the map X ↦ Λ(X) = PXP − ½P tr(PX). Facts:
  Λ annihilates the improvement tower (Λ(kk) = 0, Λ(𝟙) = 0, k² = 0)
  **[IDENTITY]**; the TT image of the ≤4-derivative family has rank 1
  per kinematic point and the leading IR form factor is forced (T₃/T₁
  suppression exactly ∝ p²) **[DERIVED-IN-CLASS]**; higher form
  factors are non-unique (rank 3–4 by dispersion class; frozen count
  gate **red**) and inherit I5 **[CONSTRAINED]** (TT-1, CP-1);
- the existence classifier: E(Σ, P*) ∈ {dead, open, closed}, with
  E = dead iff the sector's cone matches the probe's exactly
  (collinear locus, vertex ≡ 0), open ∝ subluminality (from v < c or
  curvature, vertex ∝ α), closed for superluminal curvature (no
  on-shell locus). E reads I6; under per-sector v = c units it reads
  only I11. **[DERIVED-IN-CLASS classification; arguments SUPPLIED]**
  (TT-1);
- the **red** 3D dimension-consistency gate (5.362 vs 6 ± 0.6),
  blocking any 3D-consistency claim.

---

## 3. THE MAPS, TYPED (the formal content of the architecture)

Typing key: **CONSTRUCTIVE** (defined and computed on the core datum) ·
**CONDITIONAL(I…)** (defined once the named inputs are assigned) ·
**TERMINATES(x)** (no map exists in the record; x is the input or seam
where it stops).

| map | reads | type |
|---|---|---|
| ε : (M, 𝔞) → 𝒞_continuum | core | **CONSTRUCTIVE** on stationary 𝕆 (exact finite; FAMILY-FACT limits) **and on finite stepped-nonstationary 𝕆_G, in-class** (C1-a, owner-accepted: reduction exact to 1e-12, continuity to the stationary map established); S1's remainder partitioned into **C1-b** (infinite-volume nonstationary limit), **C1-c** (smooth modulation), and the **packaging certification** (C1-a2, authorized) *(AMENDMENT 02)* |
| ι_ℐ : (M, 𝔞, ρ) → ℐ | core | **CONSTRUCTIVE** (exact in 𝕆_G; hierarchy in 𝕆_S) |
| adm : ℐ → {admissible?} | core + I7 | **CONSTRUCTIVE** given ℏ (the cone; hierarchy positivity = state positivity [IDENTITY]) |
| count : sector → exponent class | core | **CONSTRUCTIVE** (per-branch; masking law) |
| dyn→𝔞 : dynamics → seed | — | **TERMINATES(I1)** (P-6 refutations; the record's only candidate maps are non-injective/path-dependent) |
| restr : ℐ → ℐ|_𝔞 | core | **CONSTRUCTIVE** |
| geo : (ℐ|_𝔞) → 𝒢 | core | **CONSTRUCTIVE**; injectivity graded by access class (F7.2) |
| abs : 𝒢 → absolute geometry | — | **TERMINATES(F7.5)** (undefined object) |
| cons : P* → C_cons | I3 | **CONDITIONAL(I3)** |
| univ : sectors → common clock | I4 | **CONDITIONAL(I4)** (derived under exchange) |
| sel_Σ : candidates → sector class | I2, I3 | **CONDITIONAL(I2, I3)**; member **TERMINATES(I11)** |
| unit : constant probe → unit-change? | I5 | **CONDITIONAL(I5)** (the classification itself is [IDENTITY]) |
| grav : (Σ, P*) → 𝒢_grav | I2–I6, I11 | **CONDITIONAL**; existence classifier reads I6 (or I11 under per-sector units); class-4 forcing **TERMINATES(I1–I6)** |
| cause : sector pairs → cone relation | — | **TERMINATES(S2)** (no earned construction; the causal analogue of geo does not exist in the record) |
| ℏ-gen, Born : — | — | **TERMINATE(I7, I8)** (routes tested, negative) |

This table **is** GRUT's mathematical architecture: seven objects,
sixteen typed maps, two terminating seams, one loophole (L1, inside
sel_Σ ∘ F8.3), and the red register bounding what any map may claim.

---

## 4. THE SEAMS AND THE LOOPHOLE, STATED FORMALLY

- **S1 (stationarity).** ε is defined on {stationary backgrounds} ⊂
  P0-models; the physically required domain includes backgrounds with
  ε_H = −Ḣ/H² = O(1), where the target object K(t, t′) is measured to
  be non-stationary at order unity and provably not locally
  transported. The composite ε∘(non-stationary M) is **[UNDEFINED]**.
  Closing it (C1) means either extending ε's domain constructively or
  proving a no-go with the new priced input named.
- **S2 (causality).** The record defines geo (spatial) but no map
  cause : (Σᵢ, Σⱼ) ↦ relative cone. I6 is a free input read by E. The
  only earned foothold is univ's exchange-forcing. Closing it (C2)
  means constructing cause under exchange, or proving interface-
  completeness excludes it at declared access.
- **L1 (self-consistency of sector selection).** sel_Σ selects a
  class whose gravity-side member lies in the escape class of F8.3's
  own universality argument. The architecture is consistent but not
  self-explaining at this node; GeoInv is the recorded candidate
  closure. Any C7 run reads sel_Σ, hence inherits L1 (Draft 02 IV.3).

---

## 5. WHAT THE THEORY *IS* (assembled statement)

**GRUT (formal statement).** GRUT is the tuple

    GRUT = ( 𝕆, P0, 𝔇-slots, {Definitions 3–9}, {typed maps of §3},
             inventory I1–I11, red register, kill conditions )

subject to the binding claim-form: the constructive/conditional typing
of §3 *is* the theory's claim, and any statement exceeding a map's
type is outside the theory.

Its physical reading, ordered by the four blocks of Draft 02:
(i) the **generative core** — ε, ι_ℐ, adm, count, restr, geo — is
constructive on the core datum; (ii) the **structural interface** — 𝔞
in its three roles — conditions every core map and is itself supplied
at the seed; (iii) the **conditional branch** — cons, univ, sel_Σ,
unit, grav — is defined exactly on inventory assignments; (iv) the
**completion tests** C1–C7 are, in this language, statements about
extending domains (C1, C2), constructing terminating maps or proving
their impossibility (C3, C4, C5), greening gates by measurement (C6),
and confronting one conditional composite with an external certified
object (C7).

---

## 6. THE ONE-THEORY QUESTION, MADE PRECISE AND ANSWERED

**Definition (one theory).** Call an assembled hierarchy **one theory
on a domain 𝔻** if there is a single datum type such that every object
is a functional of that datum, every map of §3 is defined on all of
𝔻, and the maps commute where composable — i.e., the architecture is a
single commuting diagram over 𝔻, not a family of diagrams glued by
hand.

**Answer, at the record's strength:**

1. **On the core domain — yes, one theory.** Take
   𝔻_core = {(M, 𝔞, ρ) : M ∈ 𝕆 stationary}. Every core map of §3 is a
   functional of this one datum, and the record's instruments already
   exercise the *same* datum through multiple maps (the same hidden
   networks feed ι_ℐ, restr, geo across forks; the same phonon ring
   feeds count, sel_Σ's candidates, F8.3). Compositionality was
   checked by the assembly test (synthesis §11): no map consumes what
   another refuted. **[DERIVED-IN-CLASS at the level of the assembled
   record — a checked property of the existing diagram, not a theorem
   about all of 𝕆.]**
2. **On the conditional branch — a fibered family, not yet one
   theory.** The branch maps are functionals of (core datum, ι):
   GRUT-with-inventory-assignment ι is one theory per fiber, and the
   record provides no section of ι (that is precisely what P-6, CC-1,
   U-1, CA-1, SX-1, TT-1 established). Formally: **GRUT is currently a
   fibered family of theories over the inventory space, with a
   distinguished, internally-coherent core fiber-independent part.**
3. **The two seams are domain boundaries, not gluing failures.** S1
   and S2 are places where the datum type itself is not yet defined
   broadly enough (non-stationary M; inter-sector causal data) — the
   diagram does not *fail* to commute there; it does not *exist*
   there.

**Consequence.** The owner's question resolves into a sharp completion
criterion, equivalent to (and refining) C1–C4:

> GRUT becomes **one theory simpliciter** when (a) the domain is
> explicitly enlarged across the seams S1 and S2, and (b) every
> inventory coordinate is assigned a **formally closed status** —
> either **derived**, or **established as an irreducible primitive**,
> or **explicitly fixed as boundary/state data within the theory's
> domain**. *(Tightened per AMENDMENT 01: a supplied input need not
> become a derived section for a legitimate one-theory formulation —
> a theory can coherently have axioms and primitive structures;
> "collapse of the fibration" was too strong.)*

Nothing in this criterion requires the inventory to empty; it requires
every coordinate's status to be *closed by proof or by explicit
typing* rather than by habit. That is the formal restatement of the
paper's headline sentence — and it prevents "one theory" from secretly
meaning "theory from nothing," which the campaign has already taught
the program not to demand.

---

## 7. GOVERNANCE

- Derived from Draft 02; evidence flows through it to the frozen
  record; where documents disagree the frozen verdicts win and all are
  amended by dated entry.
- The grading vocabulary of §0 is binding: no [IDENTITY] may be cited
  as physics; no [FAMILY-FACT] as a theorem; no [DERIVED-IN-CLASS]
  without its class; no formal notation upgrades a status.
- Fences carried in full (no absolute exponent; ω⁷ occupancy-only
  outside its scoped row; v3 closed; ℏ located-not-generated; operator
  ordering fenced; Λ_R/Matsubara/Π₀/U5 untouched; no external
  dispatch). No physics fork is opened by this document.

## HARD STOP

Formalization 01 recorded: the datum, the seven objects, the sixteen
typed maps, the seams as domain boundaries, and the one-theory answer
— **one theory on the core; a fibered family over the inventory on the
branch; completion = extend the domain and close every coordinate's
status.** The decision this stop waits on: **the owner reads the
formalization and rules — amend it, iterate the paper on top of it, or
select the first completion problem with the fibration picture in
hand.**

---

## AMENDMENT 01 (owner ruling, 2026-09-25 — applied as a dated amendment)

Formalization 01 is **accepted** with one tightening, applied above in
§6: the one-theory-simpliciter criterion must not require the
fibration to *collapse*. A coordinate is closed by any of **three**
statuses — derived, irreducible primitive, or explicitly typed
boundary/state data within the theory's domain — because a theory can
coherently have axioms and primitive structures; requiring derivation
of everything would smuggle back the "theory from nothing" demand the
campaign refuted. The owner also fixed two standing qualifications,
binding on successors: (i) "one theory on the core" is a **checked
property of the assembled record**, never a theorem in the ordinary
mathematical sense — the qualification stays prominent; (ii) **the
termination points are part of the theory, not omissions from it.**

Successor document: `GRUT_FORMALIZATION_02.md` (the mathematical
statement of GRUT on the datum/fibration architecture). No physics
fork before it exists (owner ruling).

## AMENDMENT 02 (owner ruling on C1-a, 2026-09-25 — applied as a dated amendment)

Per the owner's C1-a acceptance (recorded on Issue #2): the §3 map
table's ε row is updated — ε is CONSTRUCTIVE on stationary 𝕆 **and**
on finite stepped-nonstationary 𝕆_G in-class (the first actual domain
extension of the theory: 𝔻_core^stationary → 𝔻_core^stationary ∪
𝔻_core^stepped-nonstationary at finite in-class level). Seam S1's
remainder is explicitly partitioned into C1-b, C1-c, and the packaging
certification (C1-a2, authorized, not yet evaluated). The two C1-a
L-B reds remain red; the packaging boundary remains NOT certified; the
hard fences (no C2; ω⁷/Class-4/GR-1/closed forks untouched) are
unchanged.
