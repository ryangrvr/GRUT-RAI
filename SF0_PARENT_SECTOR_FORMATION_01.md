# SF-0 — PARENT-SECTOR FORMATION / LAW-SELECTION: definitions (pre-registered) and record audit

> **OWNER RULING (Issue #2 comment `5903310812`; `SF0_OWNER_RULING_01.md`): R-F = (b).
> SF-0 = FORMULABLE-IN-EXISTING-CLASS (CA-1 F conserved filling sectors).** The proposed
> REQUIRES-NEW-PARENT in §5 is **NOT ADOPTED**. §§4–5 are kept as filed; see §6.
> SF-1 charter: `SF1_FORMATION_CHARTER_01.md` (draft; not run).

**Previous status: §4 audit and §5 proposed outcome ADDED (REQUIRES-NEW-PARENT, conditional on owner
ruling R-F); awaiting owner ruling.** §§0–3 below are unchanged since `123abaa`.

**Original status (§§0–3): PRE-REGISTERED.** They are committed **before any candidate is inspected**, per
the owner's direction ("The audit must define the equivalence relation before inspecting a
candidate"). The §4 audit and the §5 outcome are added in a later commit.
- **Authority:** `SF0_CAMPAIGN_OWNER_DIRECTION_01.md` (Issue #2 comment `5903141169`).
- **No new numerical physics.**
- **Date:** 2026-09-30 · **Branch:** `master-w25bu9`.

## §0 H-SF (verbatim from the direction)

> There exists a declared parent system X with fixed microscopic degrees of freedom, locality
> structure, generator, couplings and numerical parameters, for which two or more dynamically
> stable / asymptotically persistent sectors S_A, S_B, … are selected only by admissible state,
> history or boundary data, and the sectors possess inequivalent effective-law structure.

## §1 The coarse-graining map 𝓔 (declared before inspection)

For a candidate parent X with admissible states ρ, the effective law is L_eff = 𝓔[X, ρ]. 𝓔 must be
**declared per candidate class, before its sectors are examined,** and must use only X and ρ. The
default constructions, one of which each candidate must use:

- **𝓔-lin (linearization about a persistent state).** Let ρ* be the persistent limit or stable
  invariant state reached from ρ (a stable fixed point, periodic orbit or invariant sector).
  L_eff = the linearized generator of fluctuations about ρ*, restricted to the declared retained
  observables, together with its low-frequency response of the retained observables.
- **𝓔-sector (restriction to an exact invariant sector).** If X has an exact invariant sector 𝒮
  selected by ρ (a conserved charge value, a topological sector, a reachable invariant subspace),
  then L_eff = the generator restricted to 𝒮 (or its linearization about the persistent state in
  𝒮), with the same retained-observable response.
- **𝓔-RG (a declared coarse-graining).** Only if the record already contains an explicit,
  pre-declared RG/block map for that class.

**Forbidden:**
- choosing 𝓔 differently for different sectors of the same candidate;
- selecting the retained observables per sector;
- any 𝓔 that uses a parameter not in X.

## §2 The structural invariants (pre-registered list)

A difference in L_eff counts as **law-level** only if at least one of the following differs, each
read off L_eff at identity/theorem grade or by an exact criterion:

| # | Invariant | How it is read off L_eff |
|---|---|---|
| I-z | Dynamic exponent z (ω ~ k^z of the lowest excitation branch) | dispersion of the linearized generator |
| I-s | Low-frequency response exponent/class s of the retained kernel (e.g. exponential/gapped vs power-law ~ t^{−s}) | the pole-sensitive memory class (O-5 corrected form) |
| I-pc | Pole vs branch-cut structure of the retained response G(z) | analytic structure of the reduced resolvent |
| I-gap | Gapped vs gapless | spectral gap of L_eff = 0 or > 0 (exact) |
| I-q | Quasiparticle / statistics content (number of gapless branches; occupation structure where a lift is declared) | branch count; Sym vs Λ structure |
| I-c | Causal/propagation cone class (finite maximal group velocity vs none; light-cone vs diffusive) | support growth of the retained response |
| I-d | Effective dimensionality / topology (spectral dimension; topology of the effective coupling graph) | spectral density exponent; graph invariants |
| I-sym | Exact symmetry / conservation algebra of L_eff | commutant / conserved quantities of L_eff |

**A value difference inside one class is NOT law-level.** Examples: a different gap *value*, a
different velocity *value*, a different amplitude, or continuous reweighting of a fixed support.
This is binding per `L0_ACCESS_BRIDGE_OWNER_RULING_01.md` §2 and the direction.

## §3 The equivalence relation ≃ (pre-registered)

L_eff^A ≃ L_eff^B iff every invariant in §2 coincides after applying any composition of:

1. **basis change / invertible field redefinition** that preserves the declared locality structure;
2. **relabeling** by an automorphism of the parent's site net (a permutation preserving X);
3. **constant rescalings** of time, space, field amplitude or units;
4. **parent symmetry:** mapping ρ_A to ρ_B by a symmetry g of X (g X g⁻¹ = X). Symmetry-copy vacua
   are **equivalent by definition**;
5. **representational lift change** that preserves every effective observable (per
   `L0_LIFT_SELECTION_EVALUATION_01.md`: Λ-K, Λ-KvN and Liouville-δ are representational).

**Law-inequivalence (≄)** holds iff, after the quotient above, at least one §2 invariant differs at
identity/theorem grade. **"Different value, same class" ⇒ ≃.**

**Candidate classification (seven questions, per the direction):**
- (1) same generator;
- (2) same parameters;
- (3) selection by state/history only;
- (4) persistence (an invariant set is stable or exactly invariant under X);
- (5) a §2 invariant differs;
- (6) not reducible by §3;
- (7) sector not declared in the inputs.

H-SF-positive requires **yes** on all seven.

**Mechanical outcome rule (frozen in the direction):** the strongest surviving candidate decides.
The ordering is:

> ALREADY-DEMONSTRATED > FORMULABLE-IN-EXISTING-CLASS > STATE-NOT-LAW / SECTOR-SMUGGLED >
> REQUIRES-NEW-PARENT > UNFORMULABLE

**Tie-break note (declared now):** if every candidate is STATE-NOT-LAW or SECTOR-SMUGGLED and no
existing class contains the ingredients for a clean test, the gate outcome is
**REQUIRES-NEW-PARENT**, with the per-candidate labels recorded. The reason: the direction's
REQUIRES-NEW-PARENT means "current substrate classes cannot host the test", and that is the
operative gate fact.

## §4 Record audit

*(Added after §§0–3 were committed at `123abaa`. §§0–3 are unchanged.)*

- **Method:**
  - Two independent read-only audits applied §§1–3 as frozen.
  - No computation was run.
  - Line citations are to the record as of `123abaa`.
- **Per-candidate 𝓔:**
  - 𝓔-lin for flows.
  - 𝓔-sector for exactly invariant sectors.
  - No candidate had a pre-declared 𝓔-RG.

Q1–Q7 are the §3 questions. Y = yes, N = no, — = moot.

| Candidate | Q1 gen | Q2 par | Q3 state-sel | Q4 persist | Q5 inv. differs | Q6 irreducible | Q7 not declared | Label |
|---|---|---|---|---|---|---|---|---|
| **CA-1** (P, M, T, D, F) | N | N | N | — | Y (I-z, I-q, I-c), across generators | Y | N | **SECTOR-SMUGGLED** |
| **P-6 L-C** (parity blocks of H_C′) | Y | Y | Y | Y | N | — | Y | **STATE-NOT-LAW** |
| **P-6 L-S** (tensor factors) | Y | Y | N | — | N | — | N (per-sector retained observables, forbidden by §1) | **STATE-NOT-LAW** |
| **P-6 seed pair** {σ_z¹},{σ_z²} | Y | Y | N (supplied seeds) | Y | N | N (swap copy, §3(4)) | N | **STATE-NOT-LAW / SECTOR-SMUGGLED** |
| **P-6 L-D1** | N (baths y_A ≠ y_B) | N | N | — | — | — | N | **SECTOR-SMUGGLED** |
| **P-1** X1/X2/X3 | N (three V) | N | N | — | N at fixed V | X1 partitions = symmetry copies | N | **SECTOR-SMUGGLED** |
| **FS-1**, as recorded (H + hO) | N | N | N | Y | I-d plausibly, via coupling change | — | N | **SECTOR-SMUGGLED** |
| **FS-1**, fixed-H charge sectors | Y | Y | Y | Y | N (quadratic ⇒ state-blind law) | — | Y | **STATE-NOT-LAW** |
| **S-1** exponent classes | N | N | N | — | Y (I-s), across vertices | Y | N | **SECTOR-SMUGGLED** |
| **L0-1c** 𝒞₂ convex quartic, β ≥ 0 | Y | Y | N (one attractor) | Y (one set) | N | — | — | **STATE-NOT-LAW** (single sector) |
| **L0-1c** with β < 0 or indefinite K | N (fenced by name) | N | — | — | — | — | — | outside class → **REQUIRES-NEW-PARENT** |
| **O-5** 𝒞₁ / 𝒞₃ (Hurwitz-linear; OU) | Y | Y | N (one fixed point / one stationary law) | Y | N | — | — | **STATE-NOT-LAW** |
| **O-6** 𝒦_N conservative tori | Y | Y | Y | Y | N (same A on every torus) | — | Y | **STATE-NOT-LAW** |
| **U3** P4 / continuum (d = 1 vs d ≥ 2) | N (M, d vary) | N | N | Y | Y (I-s, I-d), across parents | Y | N | **SECTOR-SMUGGLED** |
| **U3** S4 double-well toy | — (hand-set scalar) | — | — | — | N (±√(−r/u) Z₂ copy) | N | N | **STATE-NOT-LAW** |
| **L0-1a** pin 0 vs 0.3 | N (pin is a parameter) | N | N | — | Y (I-s), across parents | Y | N | **SECTOR-SMUGGLED** |
| **u5/u6** order parameter | — | — | — | — | — | — | N (vacuum charge content is a fenced input) | **SECTOR-SMUGGLED / UNFORMULABLE** at scope |

**Key citations:**
- CA-1: `CA1_CARRIER_CHARTER_01.md:43-51`, `calc/ca1_carrier.py:75-85` (the generator branches on `kind`) and `CA1_CARRIER_VERDICT_01.md:70-71`.
- P-6: `P6_SEED_SELECTION_VERDICT_01.md:27-29, 50-54, 75-86`.
- P-1: `RELATIONAL_ONTOLOGY_CHARTER_01.md:47-58`.
- FS-1: `calc/fs1_free.py:289`, `FS1_FREE_VERDICT_01.md:31-36, 58-59`.
- S-1: `SECTOR_SELECTION_VERDICT_01.md:13-16`.
- L0-1c: `L0_1C_CHARTER_01.md:52-59` ("∇²V(0) = K_b exactly, for every β … β < 0 … out of scope").
- O-5/O-6:
  - `L0_1F_REVIEW_01.md:47` (stable limit cycles are "outside the record's classes");
  - `L0_1G_DORD_B_DESIGN_01.md:39-44, 60-61`.
- U3: `archive/adjudicator-track_90218f5/calc/u3_*` and `U3_*_RESULT.json` ("N is a free structural input").
- L0-1a: `L0_1A_VERDICT_01.md:16-22`.

**Repository-wide sweep** (including archive/):
- Search terms:
  - multi-attractor, bistab/multistab;
  - nonconvex, hysteresis, double well;
  - metastable, first-order/phase transition;
  - topological, winding, basin.
- No declared parent hosts coexisting, symmetry-inequivalent persistent sectors.
- The hits are:
  - external-literature corpus entries;
  - observation-only rrp notes ("not a candidate");
  - a graph-spectral winding count on one fixed geometry (`G2_SPECTRAL_VERDICT_01.md:72`).

**Structural reasons the existing classes cannot host a clean test:**
- **Linear/Gaussian classes** (𝒞₁, 𝒞₃, 𝒦_N, P-1, FS-1, CA-1 P/T/D):
  - The equations of motion do not depend on the state.
  - So every §2 invariant of L_eff is state-independent, and any sector multiplicity is STATE-NOT-LAW by construction.
- **𝒞₂:** strictly convex with a unique minimiser. It has a single sector by construction.
- **Finite spin classes (P-6):**
  - Every sector is gapped, discrete and pole-only.
  - Only I-sym or I-q could differ, and in L-C they do not.
- **The only law-level contrasts on record** (I-s: L0-1a pin, S-1 vertex, U3 d; I-z/I-q/I-c: CA-1) all run **across parents**.

### §4.1 Borderline item for owner ruling (R-F): CA-1 F filling sectors

- **Setup:** CA-1 F is free fermions, h = −(S + S⁻¹), on a ring. Particle number N is exactly conserved and set only by initial data (Q1–Q4, Q7 = Y). The record computes only half filling (`calc/rs1_retained.py:62`).
- **What differs, and what does not:**
  - Auditor analysis, **not a record claim and not computed:**
    - At finite filling 0 < ν < 1, the particle–hole excitations about the Fermi sea have z = 1 (v_F = 2 sin πν) and two gapless points.
    - In the dilute limit (fixed N, L → ∞), the lowest branch is the band bottom, with z = 2 and one minimum.
  - The single-particle generator is identical in every sector.
- **Why it is flagged rather than decided:** §2 reads I-z from "the lowest excitation branch of the linearized generator". That wording is ambiguous between:
  - (a) the single-particle law. On this reading every filling is ≃ and the case is STATE-NOT-LAW;
  - (b) the excitation law about the persistent state (the Fermi sea).
- **Arguments against (b)** (the auditor's recommended reading is (a)):
  - The z = 2 case is the measure-zero ν → 0 edge of a family in which every finite density has z = 1. That is a value-level (Lifshitz-density) effect, closer to continuous reweighting than a change of law.
  - ν ↔ 1 − ν is a particle–hole symmetry copy.
  - At finite L every sector is gapped, so the contrast exists only as a thermodynamic-limit statement about a density-zero "sector".
- **The consequence is recorded, not decided:** under reading (b), CA-1 F would be the one existing-class candidate for FORMULABLE-IN-EXISTING-CLASS. **This audit applies §2 as written, with reading (a), and does not promote the case.**

## §5 Outcome

- **ALREADY-DEMONSTRATED:** no. No record shows one fixed parent with ≥2 state- or history-selected, law-inequivalent persistent sectors.
- **FORMULABLE-IN-EXISTING-CLASS:** no under §2 reading (a). The only candidate is CA-1 F, and only under reading (b); see §4.1 / R-F.
- **Every audited candidate is STATE-NOT-LAW or SECTOR-SMUGGLED.** No existing class contains the ingredients for a clean test, per the structural reasons in §4.
- By the pre-registered tie-break (§3), the result is:

> **SF-0 OUTCOME (proposed, mechanical): REQUIRES-NEW-PARENT**, with the per-candidate labels in §4.
> This is conditional on owner ruling R-F (§4.1). If the owner adopts reading (b), the outcome
> becomes FORMULABLE-IN-EXISTING-CLASS (CA-1 F filling sectors), and only then would
> `SF1_FORMATION_CHARTER_01.md` be drafted. **No SF-1 charter is drafted here.**

**What this does not say:**
- It does not say H-SF is false. It says the declared substrate classes cannot host the test.
- It does not say formation is impossible, or that S-5 is thereby forced.
- It makes no multiverse claim.

### §5.1 Minimal extra ingredient (per the direction; no model is designed)

A parent that could host a clean SF test must add **at least one** of the following to the declared
classes. Each item is stated as what the current classes lack, not as a construction.

- **M-1. Non-convexity with symmetry-inequivalent coexisting persistent states.**
  - 𝒞₂ is strictly convex, and 𝒞₁/𝒞₃/𝒦_N are linear.
  - The nearest record ingredient (indefinite K plus even quartic, or the U3 double well) yields only Z₂ copies, which are ≃ by §3(4).
  - The parent needs ≥2 stable persistent states **not related by any symmetry of X**.
- **M-2. A persistent state whose linearization differs in a §2 invariant.**
  - Even with M-1, finite-N gapped Hessians share every §2 invariant.
  - A law-level difference needs one of:
    - a marginal (zero-curvature) persistent state coexisting with a gapped one (I-gap, I-s);
    - a thermodynamic-limit ordered phase with an extra gapless branch, i.e. genuine spontaneous breaking of a continuous symmetry (I-q, I-z). This needs field degrees of freedom beyond the record's finite classes.
- **M-3. Interacting conserved/topological charges:** a restricted generator that depends on the charge sector. In every conserved class on record (FS-1, 𝒦_N, P-6), the restricted generator is sector-independent or finite and gapped.
- **M-4. State-dependent kinetic/coupling structure:** a metric g(x) or a state-dependent coupling. L0-1c fixed g Euclidean (`L0_1F_DORD_THEOREM_01.md:54-55`), and "nonlinearity in the couplings" was named only as a future fork.

**Requirements on any new parent:**
- M-1 alone is insufficient. A clean test needs **M-1 together with (M-2 or M-3 or M-4)**, or M-3 alone.
- Any parent adding these would be a **new declared parent.** It must be frozen byte-for-byte (generator, couplings, constants) **before** any sector is examined.
- It must not be tuned so that it guarantees two inequivalent sectors.
- It inherits §§1–3 unchanged.

### §5.2 Owner choices (HARD STOP)

1. **Rule R-F** (§4.1: read §2's I-z as the single-particle law, (a), or as the excitation law about the persistent state, (b)).
2. **Rule on the SF-0 outcome.** If REQUIRES-NEW-PARENT, choose one:
   - (i) build a new parent carrying M-1 + (M-2 | M-3 | M-4), or M-3. This needs a campaign-specific v4 exception.
   - (ii) return to S-5 (currently HELD).
   - (iii) abandon the route.

No physics was run. No SF-1 charter was drafted.

## §6 Owner ruling and terminal (added; §§0–5 unchanged)

**Source:** Issue #2 comment `5903310812`, recorded in `SF0_OWNER_RULING_01.md`.

- **R-F = (b).** The excitation law of the exact invariant particle-number sector is the frozen
  object under 𝓔-sector (§1) and I-z (§2). Reading (a), the one-particle hopping matrix taken in
  isolation, discards the sector restriction.
- **§4.1 objections:**
  - "edge-only" is a **scope qualification**, not a value reduction;
  - PH maps ν ↔ 1 − ν, not a finite density onto the dilute sector;
  - finite-size gaps do not erase a thermodynamic-limit z (the RS-1 / CA-1 precedent).
- **Terminal:** **SF-0 = FORMULABLE-IN-EXISTING-CLASS (CA-1 F conserved filling sectors).**
- **Carried scope qualifications:**
  - The dilute family is the ν → 0 edge.
  - Formation here means **by conserved sector / boundary data, not by attractor selection.**
  - The reference state is **declared** as the sector ground state; it is not reached dynamically.
  - H-SF is **not** demonstrated.
- **The §5.1 minimal-ingredient list (M-1 … M-4)** stays on record as a description of what the
  *other* audited classes lack. It is not an active branch.
