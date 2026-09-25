# GRUT FORMALIZATION 02 — the mathematical statement of GRUT (datum/fibration architecture)

**Date:** 2026-09-25 · **Authority:** owner ruling accepting
Formalization 01 (with its AMENDMENT 01 tightening) and authorizing
*"a formalized theory-paper draft built directly on the
datum/fibration architecture"* answering three questions in
mathematical terms. · **Status: FORMALIZATION, NOTHING BANKED. Not
for external distribution** (D-1 standing direction). Serves as
Formalization 02 and Theory Paper Draft 03 in one document. The
grading vocabulary of Formalization 01 §0 — [IDENTITY] ·
[DERIVED-IN-CLASS] · [FAMILY-FACT] · [SUPPLIED] · [UNDEFINED] — is
carried in full and binding; the red register bounds every statement.

**The three questions (owner, verbatim in force):**

1. **What is the core object?**
2. **What exactly is the inventory fiber?**
3. **What constitutes closure of the theory without assuming that
   every primitive must become derived?**

**Two standing qualifications (owner, binding, kept prominent):**
"one theory on the core" is a **checked property of the assembled
record, never a theorem in the ordinary mathematical sense**; and
**the termination points are part of the theory, not omissions from
it.**

---

## 1. Q1 — THE CORE OBJECT

### 1.1 The core data and representation equivalence

**Definition 1 (core data).** Let 𝕆_stat ⊂ 𝕆 be the admitted classes
(Formalization 01, Definition 1) restricted to stationary microscopic
laws (the P0 time-translation clause). The core data are

    𝔻_core = { (M, 𝔞, ρ) : M ∈ 𝕆_stat, 𝔞 an access assignment,
                ρ a state on M's algebra }.

**Definition 2 (representation equivalence).** (M₁, 𝔞₁, ρ₁) ∼_rep
(M₂, 𝔞₂, ρ₂) iff an isomorphism of the underlying algebras
intertwines dynamics, state, and seed. The record's controls verify
that every core functional below is constant on ∼_rep-classes:
Givens scrambles (4.3e-25), exact Lanczos re-representation
(machine precision, all access levels), channel congruence
covariance, noncommutative congruence (2.6e-10).
**[DERIVED-IN-CLASS]** (G-2, D-1 E4, P-3). The core object is
therefore defined on 𝔻_core/∼_rep.

### 1.2 The core object itself

**Definition 3 (the core object).** The core object is the assignment

    Core : 𝔻_core/∼_rep ⟶ ( 𝒞(𝔇), ℐ(𝔇), ℐ(𝔇)|_𝔞, 𝒢(𝔇) )

i.e. the tuple-valued functional sending each core datum to its
continuum reduction (K_R, ρ(τ)), its influence hierarchy, the
accessible restriction, and the recoverable geometry — together with
the **compatibility relations** the record has checked among them:

| relation | content | grade / source |
|---|---|---|
| R1 (kernel downstream) | K_R = K_R(M, 𝔞): exact spectral form; realization dimension = #distinct eliminated modes; partition-dependence explicit | [DERIVED-IN-CLASS] (P3/P4/E4a; P-1) |
| R2 (admissibility) | ℐ(𝔇) satisfies hierarchy positivity ⟺ ρ ≥ 0 on 𝒜_R; Gaussian face in 𝔠_Gauss, vacuum on the floor | [IDENTITY] + [DERIVED-IN-CLASS] (P-2/P-3/P-4; GR-1 for the gravitational point) |
| R3 (interface completeness) | for declared 𝔞, in-class, ℐ|_𝔞 tracks every physical difference | [DERIVED-IN-CLASS] (P-4; D-1 as its two-point exemplar) |
| R4 (counting) | sector ↦ exponent class by locality+symmetry additive counting; per-branch, masked at eigenvalue level (gate red) | [DERIVED-IN-CLASS] (S-1, P-3) |
| R5 (geometry from data) | 𝒢 = geo(ℐ|_𝔞); recovery certified where the functionals are; selection graded exactly by access class; topology below circumference order invisible | [DERIVED-IN-CLASS] (G-2, GS-1; G-1's eight reds bound the functional family) |
| R6 (unit-change coherence) | dimensionless accessible data are the unit-change discriminator; co-stretch ≡ unit change | [IDENTITY] (SX-1) |
| R7 (cross-fork datum sharing) | the same underlying data are pushed through several maps with consistent outputs (the GS-1 path through geo and the SX-1 counterexample; the phonon ring through count, F8.3, sel_Σ candidates; the hidden networks through ι_ℐ, restr, geo) | checked property of the assembled record |

**Statement Q1 (the answer).** The core object exists as one
structure: a single assignment on 𝔻_core/∼_rep whose components
satisfy R1–R7 on the record's common model families, with no internal
consistency test finding one layer requiring an assumption another
layer had ruled out. **Grade: a checked property of the assembled
record, in-class — not a theorem about all of 𝕆_stat.** What would
upgrade it: proving R1–R6 as class-level theorems (ordinary
mathematics, no new physics); what would break it: any future fork
exhibiting a datum on which the diagram fails to commute.

The core object's own boundary is part of its definition: Core is
undefined off stationary M (seam S1) and outputs no absolute geometry
(F7.5) and no causal relation between sectors (seam S2).

---

## 2. Q2 — THE INVENTORY FIBER

### 2.1 The inventory space

**Definition 4 (inventory space).** The inventory space is the typed
product

    𝕴 = ∏_{k=1}^{11} 𝕀ₖ

with coordinates and types:

| k | coordinate | type of the assignment |
|---|---|---|
| I1 | access seed | a subalgebra S ⊂ 𝒜 (an access specification) |
| I2 | CARRIER | an identification: geometry-recovery seed = probe access seed |
| I3 | probe structure | a field structure: massless, gauge/Lorentz-redundant representation + coupling class |
| I4 | universal reach | a claim about the exchange graph: all sectors in one exchange-coupled component |
| I5 | co-stretch declaration | a rule for how constant probes act on intrinsic scales |
| I6 | light-cone relation | a relation on sector pairs (relative cone data) |
| I7 | ℏ | a positive constant (the cone's floor height) |
| I8 | Born/outcomes | a probability measure and selection rule |
| I9 | noncommutativity | the commutant structure class of 𝒜 |
| I10 | states & boundary data | ρ-selections, arrow orientation, boundary/initial data (and, on FRW: a state choice, a temperature structure, a stationary reduction) |
| I11 | sector content | ρ(τ) support and τ₀; the retained sector's dispersion ω(p), curvature included |

**Definition 5 (fiber and fibration).** For ι ∈ 𝕴, the fiber 𝔗_ι is
the core object extended by the conditional maps of Formalization 01
§3 evaluated at ι (cons, univ, sel_Σ, unit, grav). GRUT's conditional
branch is the fibration

    π : 𝔗 ⟶ 𝕴 ,   π⁻¹(ι) = 𝔗_ι ,

each fiber internally coherent at [DERIVED-IN-CLASS] strength (the
branch verdicts), glued to the *same* core object.

### 2.2 What the campaign did to the fibration — the base is carved

The campaign did **not** collapse fibers. It did two provable things:

**(a) It carved the admissible base.** The record's earned constraints
cut 𝕴 down to an admissible region 𝕴_adm and partition what survives:

| carving | region removed / partitioned | grade / source |
|---|---|---|
| massless probe ⇒ conservation | assignments with I3 = massless probe and a non-conserved coupling: exchange positivity fails (−10.6, −17.8) — removed | [DERIVED-IN-CLASS] (CC-1) |
| cone cuts the classical carrier | I2-assignments realizing the carrier classically: ν − J/2 = −0.192 < 0 — removed | [DERIVED-IN-CLASS] (CA-1) |
| sector-class carving | given I2 + I3: candidate retained sectors reduced to the gapless z = 1 accessible-Goldstone class (fermions/flexural/gapped/magnon eliminated; one gate red) | [DERIVED-IN-CLASS] (RS-1) |
| channel-existence partition | I6 × I11 partitioned by E ∈ {dead (exact cone match), open (∝ subluminality/curvature), closed (superluminal)} | [DERIVED-IN-CLASS] classification (TT-1) |
| universality carving | I4-assignments with exchange: non-universal clocks removed (forced ≥ 0.13); decoupled assignments: not removed, but proven observable-yet-unforbidden | [DERIVED-IN-CLASS] (U-1, S4-1) |
| co-stretch dichotomy | I5 space is genuinely two-valued in ≥2-scale sectors (rigid stretch observable, 0.013); vacuous in single-scale sectors | [DERIVED-IN-CLASS] (SX-1) |

**(b) It refuted candidate sections.** A **section over a coordinate**
is an earned map s : 𝔻_core → 𝕀ₖ. Each terminating fork is a proof
that a named family of candidate sections fails:

| coordinate | section family refuted | source |
|---|---|---|
| I1 (seed) | minimality; dynamical closure (non-injective, 0.287; path-dependent; degenerate control unselectable — gate red) | P-6 |
| I2 (CARRIER) | substrate-operator determination (four genuinely different sectors carry identical recovered geometry to 4e-14); non-carrier baths admissible | CA-1 |
| I3 (probe) | every earned constant-level selector (𝔠, geometry, regularity, driven-stationarity — the last an [IDENTITY] restatement) admits non-conserved couplings; only the massless probe forces C_cons | CC-1 |
| I4 (reach) | clock-only dynamical probes mediate no exchange (⟨H_B⟩ constant to 7.5e-15): reach is not self-generating | U-1 |
| I5 (co-stretch) | earned structure detects all four constant actions and forbids none | SX-1 |
| I6/I11 | the channel classifies but does not select the class (all three regions realizable in 𝕆_c) | TT-1 |
| I7 (ℏ) | emergence attempt failed (prior record); the cone locates, does not generate | P-2 + register |
| I8 (Born) | tested derivation routes negative | Experiment-P |

**Statement Q2 (the answer).** The inventory fiber is the coherent
conditional theory 𝔗_ι over one point of a typed, **earned-carved**
base 𝕴_adm. The campaign's exact accomplishment, stated formally:

> **No tested section of π exists, and the base is provably smaller
> and provably partitioned. We did not prove the fibers collapse; we
> mapped where they remain.**

C1–C4 acquire their precise meaning here: each is an attempt either to
construct a section s : 𝕴_needed → 𝔗 from earned structure, or to
establish that the coordinate is genuinely primitive (§3).

---

## 3. Q3 — CLOSURE WITHOUT DERIVATION-FUNDAMENTALISM

### 3.1 The three closed statuses (each a certificate, not a mood)

**Definition 6 (closed statuses).** An inventory coordinate 𝕀ₖ is
**formally closed** when it carries exactly one of:

- **DERIVED-SECTION:** an earned map s : 𝔻_core → 𝕀ₖ at
  [DERIVED-IN-CLASS] strength or better, produced by a chartered fork
  with its class scope stated. *(Certificate: the fork's frozen
  verdict.)*
- **IRREDUCIBLE PRIMITIVE:** an underdetermination demonstration at
  stated scope — exhibit distinct coordinate values with identical
  accessible core data (the D-1/P-6/SX-1-L-C form), or a
  classification proving the coordinate independent of the core datum
  in the admitted classes — followed by promotion to a **declared
  axiom carrying its measured content**. *(Certificate: the
  demonstration + the owner's declaration.)*
- **DOMAIN DATUM:** the coordinate is explicitly typed as
  boundary/state data *within the theory's domain* — in the way
  initial conditions belong to classical mechanics: not derived, not
  claimed impossible-to-derive, but formally placed, with the
  demonstration that all theory outputs are well-defined given the
  datum and carry no hidden dependence beyond it. *(Certificate: the
  typing + the well-definedness check.)*

**Definition 7 (closure of GRUT — the owner's tightened criterion).**

> GRUT is **closed as one theory** when (a) the domain is explicitly
> enlarged across seams S1 and S2 (or each seam is proved a permanent
> domain boundary with the new priced input named), and (b) every
> coordinate of 𝕴 carries one of the three closed statuses, with its
> certificate.

Nothing here demands that any coordinate become derived. What is
outlawed is only an *uncertified* supplied input — a coordinate whose
status is habit rather than proof or explicit typing.

### 3.2 The per-coordinate closure state (where each certificate stands today)

| coordinate | evidence held today | what closure requires |
|---|---|---|
| I1 seed | section-family refutations (P-6) **and** an in-class underdetermination exhibit at limited access (identical closures / single-site families) — substantial but scope-limited evidence toward IRREDUCIBLE PRIMITIVE; no certificate declared | a full-scope underdetermination classification, or a new selector family surviving the P-6 battery, or owner declaration as axiom with measured content (C3) |
| I2 CARRIER | carrier-set carved (classical cut); determination refuted | same trichotomy; rides I1 (the coincidence is between seeds) |
| I3 probe | forcing direction established *given* the probe; no selector for the probe itself | C4: derive the probe among declared alternatives, or classify it independent (a CC-1-grade battery whose alternatives all survive), or declare |
| I4 reach | non-self-generation shown; universality derived under it | C4 companion; possibly DOMAIN DATUM (which sectors exist and touch is arguably boundary data) |
| I5 co-stretch | the dichotomy is proved real (not vacuous) in ≥2-scale sectors; neither branch forbidden | likely IRREDUCIBLE PRIMITIVE candidate: the underdetermination exhibit already exists in-class (SX-1); needs scope statement + declaration |
| I6 light cone | classifier only | C2: construct `cause` under exchange (section), or prove interface-completeness excludes it (irreducibility), or type as domain datum |
| I7 ℏ | located (floor height); emergence failed on tested routes | C5: generative account, or an irreducibility classification, or declaration (the located content is exactly what the axiom would carry) |
| I8 Born/outcomes | routes tested negative | C5 companion; same trichotomy |
| I9 noncommutativity | commutative substrates produced nothing quantum (as tested) | classification or declaration |
| I10 states/boundary | arrow decomposition (existence derived, orientation imported); no-pin | the natural **DOMAIN DATUM** candidates; closure = the explicit typing + well-definedness check |
| I11 sector content | fully open: no certificate in either direction on dispersion curvature; ρ-support no-gos exist within P0 | the narrowest naked coordinate; any of the three statuses would be new (feeds C7's premises) |

**Statement Q3 (the answer).** Closure of GRUT is Definition 7: domain
enlargement across the seams plus a certified status — derived,
irreducible-primitive, or domain-datum — on all eleven coordinates.
The table shows the theory is closer to closure than a raw count
suggests: several coordinates already hold the *demonstration half*
of an irreducibility certificate at stated scope (I1, I5 most
sharply), and I10 is a natural domain-datum typing awaiting its
well-definedness check. The genuinely naked coordinate is I11.

---

## 4. THE MATHEMATICAL STATEMENT OF GRUT

Assembling §§1–3, at the record's strength:

> **GRUT = ( 𝕆_stat/P0 , 𝔄 , Core , π : 𝔗 → 𝕴_adm , 𝕴-status map ,
>          domain boundaries {S1, S2} , red register , kill
>          conditions )**
>
> — an admitted local class with its principles; the cross-cutting
> access structure; the core object (one checked structure on
> 𝔻_core/∼_rep delivering continuum dynamics, the influence
> hierarchy with its admissibility cone and counting law, and
> access-relative geometry); the conditional branch as a fibration
> over the earned-carved inventory base; the current closure status
> of every coordinate; the two domain boundaries; and the integrity
> bounds.
>
> **The termination points are part of the theory, not omissions from
> it** (owner ruling, binding): a map that terminates at 𝕀ₖ is a
> statement of where physics stops being derivable from the core
> datum in the admitted classes — content, exactly as a conservation
> law is content.

Physical reading, one sentence, per the binding claim-form: local
microscopic dynamics generates the core object; the inventory buys the
effective/gravitational branch; the fibration's carved base and
refuted sections are the campaign's theorems; the seams and the
status map are the theory's own statement of what remains.

**What this document makes possible (and Draft 02/Formalization 01
could not):** C1 and C2 are now *domain-extension problems for a
specified mathematical object* — does 𝔻_core extend across S1
(non-stationary M) and does the datum type extend across S2
(inter-sector causal data) — rather than further phenomenology. C3–C5
are *status problems* on named coordinates with their certificate
forms fixed. C6 remains measurement. C7 remains a confrontation of
one conditional composite, inheriting L1 through sel_Σ.

---

## 5. GOVERNANCE

- Built on Formalization 01 as amended; evidence flows through Draft
  02 and the synthesis to the frozen record; frozen verdicts win over
  every formalization statement, which are then amended by dated
  entry.
- Binding qualifications carried: "one theory on the core" is a
  checked property, never an ordinary theorem; grading vocabulary
  binding; no [IDENTITY] cited as physics; no formal notation
  upgrades a status; the red register bounds all claims.
- Fences carried in full (no absolute exponent; ω⁷ occupancy-only
  outside its scoped row; v3 closed; ℏ located-not-generated; operator
  ordering fenced; Λ_R/Matsubara/Π₀/U5 untouched; no external
  dispatch). No physics fork is opened by this document.

## HARD STOP

Formalization 02 recorded: the core object (Q1), the inventory fiber
over the earned-carved base with the refuted-sections table (Q2), and
closure by three certified statuses without derivation-fundamentalism
(Q3) — assembled into the mathematical statement of GRUT in §4. The
decision this stop waits on: **the owner reads the statement and
rules — amend, or select the first true completion attack (the owner
has indicated C1 or C2, now well-posed as domain-extension problems
for the specified object).**
