# S5-0 — GENERATOR ORIGIN: can the generator be derived rather than presupposed? (audit/formulation only)

**STATUS: AUDIT COMPLETE.**
- §§0–4 were pre-registered at `afab923` and are unchanged.
- §5 (the audit) and §6 (the proposed mechanical outcome, **GENERATOR-IRREDUCIBLE/SUPPLIED**) have
  been added.
- Awaiting owner ruling. **HARD STOP.**
- **Authority:** `SFG0_OWNER_RULING_01.md` §6 (Issue #2 comment `5903805047`).
- **No new numerical physics and no v4 exception.**
- **Date:** 2026-09-30 · **Branch:** `master-w25bu9`.

**Disclosure.** The auditor holds one prior expectation: the Level-0 program *declared*
ẋ = −Kx as its substrate premise, which would make selectors "earned" downstream of it circular.
The P-0 premise audit and the H-1 circularity check (§3) are written so that this expectation is
tested, not assumed.

## §0 Question (ruling §6.1)

For the already-earned substrate/structural data, does any existing GRUT principle select the
**form (kind) of the temporal generator**, or do multiple inequivalent generators remain compatible
with the same substrate data? Symbolically: substrate/static structure ⟹? generator class.

Magnitudes of derived constants are **out of scope.**

## §1 Comparison set and comparison object (frozen)

**Static datum shared by all classes.** A symmetric positive (semi)definite K on a declared site net,
together with its geometry. Two declared instances:
- **(R)** the CA-1 ring K(k) = 4 sin²(k/2);
- **(B)** the Level-0 bath block K_b (open chain, pin 0.3), also written K_N.

| Tag | Generator class | Where declared (to be verified in §5) |
|---|---|---|
| **G-D** | first-order dissipative, ẋ = −Kx (and the gradient ẋ = −∇V, 𝒞₂) | Level-0 / EA-0; CA-1 D (with noise) |
| **G-S** | Schrödinger-type, iψ̇ = Kψ | CA-1 M |
| **G-W** | conservative wave/phonon, q̈ = −Kq (Hamiltonian on T\*) | CA-1 P/T; O-6 𝒦_N |
| **G-OU** | stochastic, dx = −Kx dt + B dW | 𝒞₃; CA-1 D |
| **G-L** | dilation / lift realizations: Sz.-Nagy; quasi-free Lindblad loss; cotangent pᵀf | lift-selection records |
| **G-F** | fermionic hopping, i ċ = hc with h = K − 2 (CA-1 F) | CA-1 F / SF-1 |

- **Comparison object (common, time-structure-neutral as far as possible):** the pair (K, 𝒜). Here 𝒜
  is the generator as an operator-valued function of K on its declared state space, together with
  its **type**:
  - a real contraction semigroup;
  - a unitary group;
  - a symplectic/Hamiltonian flow;
  - a Markov semigroup;
  - a CP semigroup / dilation.
- **Invariants for "genuinely inequivalent":** the SF-0 §2 list, read on the retained response of a
  common declared observable:
  - the dispersion functional (for example −K vs −iK vs ±i√K);
  - I-z, I-gap, I-pc, I-c;
  - reversibility (time-reversal symmetric vs not);
  - norm or energy conservation vs contraction.
- **Representational equivalence ≃_G.** G-a ≃_G G-b iff an invertible map between the state spaces
  intertwines the two flows (on the same K) and maps the declared observables to each other. This
  follows `L0_LIFT_SELECTION_EVALUATION_01.md`: Koopman/KvN/Liouville are representational.
  - **Declared now:** a map that changes the K-functional counts as **a different class on the same
    K**. An example is G-W on K ≅ G-S on √K.

## §2 Selector inventory and admission (frozen)

**Admissible selectors** (ruling §6.3; record items only):

| # | Selector |
|---|---|
| S-loc | locality |
| S-pos | positivity/passivity/accretivity |
| S-gap | gap/memory |
| S-geo | geometry |
| S-acc | retained access |
| S-obs | observability |
| S-ord | strict Lyapunov / order (D-ORD / O-series) |
| S-cm | complete monotonicity, where earned |
| S-cone | influence-cone / noise-response |
| S-LG | Lorentz/gauge (**SUPPLIED**, per record status) |
| S-FDT | FDT/equilibrium, with its conditioning |
| S-var | earned variational/gradient formulation |
| S-symp | declared conservative/symplectic structure |
| S-SF | the SF-1/SFG-0 result |

**Candidate imports, listed and not consumed:** least action, maximum entropy, minimal complexity,
and similar.

**Grade of each selector, taken from the record** (quoted status):
- **EARNED**: an accepted finding or theorem, unconditional at its scope;
- **CONDITIONAL**;
- **SUPPLIED**;
- **CRITERION** (priced only).

Only EARNED selectors can *select*. The others are recorded as **prices.**

## §3 Mandatory checks (frozen)

- **P-0 premise audit.** For each generator class, establish from the record whether it entered as
  a **declared premise** (substrate definition, charter assumption) or as a **derived** result. Quote
  the entry point.
- **H-1 circularity.** A selector whose *statement presupposes* a time-evolution form cannot select
  that class over others. Examples: a Lyapunov/passivity property defined only for ẋ = −Kx, or an
  "earned" result obtained after assuming ẋ = −Kx. Such a selector is re-graded **CRITERION
  (definitional).** Each selector's H-1 status must be stated with a citation.
- **NG-1 no-go (ruling §6.6):**

  > If the same K-level substrate and geometry support dissipative, unitary/Schrödinger and
  > conservative/wave generators, then K + geometry alone cannot select the generator.

  - Accepted only at the scope demonstrated (CA-1 and related records). That scope must be stated:
    which K, which classes, and which geometry observables.
  - Then ask whether any **EARNED** (post-H-1) selector breaks the degeneracy.
  - A break by SUPPLIED Lorentz, gauge, statistics or lift assumptions is recorded as a **price**.
- **Primitive-price table (ruling §6.4; descriptive):** the extra structure each class needs beyond
  K and site locality, with record citations where the record states it.

## §4 Outcomes and determination rule (frozen; no ranking)

**Outcomes (ruling §6.5):**
- GENERATOR-SELECTED-IN-CLASS;
- GENERATOR-CONSTRAINED-NONUNIQUE;
- GENERATOR-IRREDUCIBLE/SUPPLIED;
- CLASS-SPLIT;
- REPRESENTATIONAL-ONLY;
- UNFORMULABLE.

This is a **determination procedure applied to the audit's findings.** It expresses no preference.
Take the first step that applies.

1. **UNFORMULABLE:** the §1 comparison object cannot be stated for the declared classes without
   importing the temporal structure under test. (The P-0/H-1 findings feed this.)
2. **REPRESENTATIONAL-ONLY:** every pair of classes in the comparison set is ≃_G on the same K.
3. Otherwise, take the post-H-1 **EARNED** selectors and, for each declared substrate instance
   (R, B, or any further declared substrate class), record which ≄_G classes each selector
   eliminates at identity/record grade.
   - **CLASS-SPLIT:** different substrate classes leave different unique survivors, under declared
     conditions.
   - **GENERATOR-SELECTED-IN-CLASS:** exactly one class survives, consistently.
   - **GENERATOR-CONSTRAINED-NONUNIQUE:** at least one class is eliminated, but several survive.
   - **GENERATOR-IRREDUCIBLE/SUPPLIED:** no class is eliminated by an EARNED selector. The only
     separations come from SUPPLIED, CONDITIONAL or CRITERION items, which are recorded as prices.

**Fences:**
- No S5-1 run, no SF-2 and no new parent.
- No gravity reopen, no Π₀ and no cosmology.
- Imports are not consumed.

## §5 Audit

**Method.**
- Two independent read-only audits: (A) P-0, the comparison set, ≃_G, NG-1 and prices;
  (B) selector grades and H-1.
- Nothing was computed on any declared member.
- **[AA]** marks auditor-derived analysis, which is not a record claim.

### §5.1 P-0 premise audit: the generator is a declared premise, and the record says so

The first-order dissipative form entered in four steps. **None of them derives it from something
more primitive.**

1. **Chosen to match a target.** In
   `archive/adjudicator-track_90218f5/calc/u3_minimal_generative_ontology.py:4-10, 246-251, 316-338`:
   - the conservative candidate C4 is dropped because its kernel is not completely monotone (CM);
   - the winner is a "RESISTIVE PERSISTENT SECTOR: local first-order dynamics";
   - dissipation is booked as "the irreducible import".
2. **Admitted as a principle.** "Autonomous first-order dynamics; passivity" are admitted principles
   (`archive/adjudicator-track_90218f5/GRUT_SKELETON_01.md:96-99`). They are "P0 … definitional for
   𝕆" (`GRUT_FORMALIZATION_01.md:61-63, 73-76`).
3. **Narrowed by charter.** `C1_STATIONARITY_SEAM_CHARTER_01.md:47-48` gives "Class … ẋ = −K(t)x".
   `L0_1C_CHARTER_01.md:70-75` makes it "the record's kernel convention", with second order "out of
   scope".
4. **Labelled "earned" afterwards,** as the substrate on which Level-0 certified property edges
   (`EA0_CORRECTIONS_01.md:15-16`; `EA0_ENDOGENOUS_ACCESS_FORMULATION_01.md:250`).

**The record states the conclusion itself:**
- "The generator is therefore a presupposition on this document's face"
  (`L0_1F_DORD_THEOREM_01.md:27-40` (line 34), `:256-260`);
- "The generator is presupposed, not derived (S-5)" (`L0_1_FLOOR_DEPOSIT_01.md:66, 138`);
- time/update ordering was "Never weakened or derived" (`L0_1_NECESSITY_SWEEP_DESIGN_01.md:37`).

**K is also declared:**
- springs and pin (`calc/c1_seam.py:58-69`);
- graph Laplacian plus pins (`CA1_CARRIER_CHARTER_01.md:40-43`; `GS1_GEOMETRY_SELECTION_CHARTER_01.md:56`);
- "has not derived the existence or uniqueness of the local net" (`EA0_OWNER_RULING_02.md:51-53`).

**Where the other classes entered:**
- G-S, G-W, G-OU and G-F are declared candidates or deletion forks (CA-1 M/P/T/D/F, O-6 𝒦_N, L0-1e).
- **G-L is defined as lifts *of* e^{−K_b t}**, so it is downstream of G-D, not a peer.

**Strongest counterargument.**
- The record derives *effective* irreversibility from a conservative substrate in the
  infinite-volume limit (`GRUT_WORKING_THEORY_01.md:109`; O-6 emergent dissipation).
- Rebuttal: that result gives an algebraic, oscillatory kernel class, not e^{−Kτ} on the same K.
  The arrow's direction stays SUPPLIED (`GRUT_WORKING_THEORY_01.md:113`), and no record derives
  ẋ = −Kx.

### §5.2 Comparison set (verified) and ≃_G

| Class | (R) CA-1 ring K | (B) Level-0 K_b / K_N |
|---|---|---|
| G-D | D's response, the heat kernel (`calc/ca1_carrier.py:34-35`) | L0-1a/b/c |
| G-S | M (`CA1_CARRIER_CHARTER_01.md:48`) | **not declared** |
| G-W | P, T | O-6 𝒦_N (`L0_1G_CHARTER_01.md:45-47`, with K₂₃ = K_b) |
| G-OU | D with T ≥ 0 | L0-1e; real Λ-B |
| G-L | — | Sz.-Nagy, cotangent, quasi-free Lindblad (lifts of e^{−K_b t}) |
| G-F | F: h = K − 2 | complex-fermion lift only (descends to G-D) |

**Correction to the §1 framing: no record ran a cross-class geometry comparison on (B)**
(`L0_ACCESS_BRIDGE_VERIFICATION_01.md:37`).

**≃_G findings [AA, anchored to the record]: no pair is ≃_G on the same K.**

| Pair | Separating invariants |
|---|---|
| G-W vs G-S | Dispersion ±i√K vs −iK (z = 1 vs z = 2; RS-1). Short-time t^{2d+1} vs t^d (CA-1). G-W on K ≅ G-S on √K is a different class on K by §1. |
| G-D vs G-S | Spectrum real vs imaginary; contraction vs unitary |
| G-OU vs G-D | Record: "NO MERGE"; Koopman is a singular ε → 0 limit, "not an equivalence" (`L0_LIFT_SELECTION_VERIFICATION_01.md:76-99`). Invariants: fluctuation content and invariant measure. |
| G-L vs G-D | A dilation is an isometric embedding, not invertible. Record: "inequivalent non-representational lifts". **G-L is a realization of G-D, not a peer.** |
| G-F vs G-S | At one-particle level they are equal up to a global phase, e^{−i(K−2)t} = e^{2it}e^{−iKt}. The CA-1 hop numbers agree to 15 digits. The real separation is supplied statistics plus filling (state). |

### §5.3 NG-1 at its demonstrated scope: ACCEPTED at that scope

> On the 1D periodic Laplacian ring (N = 256 for the resistance profile, N = 64 for hop recovery),
> K together with the geometry observables {normalized resistance profile, graph hop distance}
> **cannot select** among G-W (P, T), G-S (M) and G-D/G-OU (D). The reason is that these observables
> are functions of K⁻¹ or of K's sparsity pattern.

**Qualifiers:**
- The resistance leg is "close to an identity" (`CA1_CARRIER_VERDICT_01.md:70`), because it is
  computed from each sector's declared static kernel 1/K.
- The hop metric is support-level: "independent of dynamics type"
  (`L0_ACCESS_BRIDGE_VERIFICATION_01.md:39`).
- **It is not demonstrated on (B).**

**What does differ:**
- z and the short-time exponent. These are labels of the generator itself.
- F's additive metric (A = 1.02), which comes from statistics and state.
- B flexural (a different K-functional).
- The magnon, cut by the supplied Lorentz layer.
- D, cut by the P-2 cone. That cut is conditional on the ℏ floor; see §5.4.

### §5.4 Selector inventory, grades and H-1

**Main H-1 finding.** Nearly every Level-0 dynamical predicate is defined on
k(τ) = e₁ᵀe^{−Kτ}e₁, which is the G-D kernel. Record statements:
- "Scope of every statement here … ẋ = −Kx … Unitary quantum generators … are a different object"
  (`L0_1_FLOOR_DESIGN_01.md:15-20`);
- "the record's kernel convention" (`L0_1C_CHARTER_01.md:70-75`).

| Selector | Record grade | H-1 | Post-H-1 | Eliminates on (R) / (B) |
|---|---|---|---|---|
| S-loc | NECESSITY-CERTIFIED (geometry line; static) | static, not circular | **EARNED** | none / none. Every class generator is degree-1 in K [AA]. |
| S-pos | NECESSITY-CERTIFIED; R-4 = accretivity; lift D-4 EARNED (narrowed) | defined on the G-D kernel/semigroup; "Hamiltonian passivity ≠ R-4 accretivity" | **CRITERION (definitional)**; K ⪰ 0 is the shared datum | none |
| S-gap | NECESSITY-CERTIFIED for P_memory; register "assumed … STANCE" | read on k(τ); the gapped G-W chain has algebraic memory on record (`L0_1G_OWNER_RULING_02.md:36-38`) | **CRITERION** | none (vacuous on the gapless ring) |
| S-geo | CA-1 "identical recovered geometric data" | static | **EARNED** | none. The F cut is conditional on CARRIER (IRREDUCIBLE INPUT), so it is a price. |
| S-acc | EA-0 UNFORMULABLE at earned scope; bridge TRIVIAL/IDENTITY; accessibility PROBE-DEPENDENT | identity-grade only | EARNED (identity) / CONDITIONAL | none |
| S-obs | RANK-CONSTANT theorem | a property of (K, e₁) | **EARNED** | none. At the retained site the static G(z) is class-neutral; the class shows only through a time-domain readout, i.e. through the structure under test. |
| S-ord | O-5 DISCHARGED: "**The generator is presupposed, not derived (S-5)**"; O-6 FALSIFIED (strict form); O-7 "Holds: primitive dissipative generators … Fails: emergent" | orientation "is the generator's sign" | **CRITERION (definitional)** | Used as a selector it is a restatement of "dissipative", not a selection |
| S-cm | class-split; "On the symmetric subclass CM is identity-held … not a test there" | Bernstein: CM ⟺ the G-D reading of a positive spectral measure [AA] | **CRITERION** | none. This is historical circularity: CM chose G-D (u3), and G-D ⇒ CM. |
| S-cone | GR2-d D-PARTIAL, "0/7 … eliminated", fronts are labels. P-2 is DERIVED-IN-CLASS with "ℏ … [SUPPLIED]" | P-2 floor = quantum content | GR2-d: not a selector. **P-2: CONDITIONAL** | On (R), classical G-D/G-OU (CA-1 D) are cut **conditional on the supplied ℏ floor**, and the quantum-completed dissipative class survives (`CA1_CARRIER_VERDICT_01.md:75-77`). On (B): not run. |
| S-LG | "Lorentz covariance is itself a supplied symmetry" | temporal by statement | **SUPPLIED (price)** | If supplied: on (R), IR z = 1 removes G-D, G-OU and G-S. On (B): no boosts. |
| S-FDT | O-3 DISCHARGED (identity); lift D-3 CRITERION; P-2: "KMS, FDT … are STATES inside 𝔠" | the Einstein relation presupposes a first-order drift | **CRITERION** | none |
| S-var | 𝒞₂ is the declared "kernel convention" | the gradient-flow form *is* G-D | **CRITERION (definitional)** | none |
| S-symp | "no canonical symplectic structure has been earned"; lift IRREDUCIBLE/SUPPLIED | presupposes a conservative flow | **SUPPLIED (price)** | If supplied: removes G-D and G-OU |
| S-SF | SF-1 accepted within one free-fermion parent; SFG-0: "Level-0 does not select that statistics or that conservative realization" | presupposes a fixed unitary G-F | EARNED at its scope; **CRITERION** as a selector | none. Using it to select would be a teleological import. |

**Candidate imports found in the record (listed, not consumed):**
- least action, entropy and "simplicity": "PROHIBITED as selectors here" (P-6 charter);
- relative entropy;
- minimality (D-7; bears on G-S);
- universality (D-2) and classical limit (D-3);
- tensor locality (D-6);
- Past Hypothesis / imported arrow;
- the finite-memory ontology stance;
- the KMS gate;
- Onsager/passivity as a classifier;
- empirical eliminators (attraction, light bending, light speed; "outside the record");
- a formation/teleological requirement [AA].

### §5.5 Primitive-price table (descriptive; record-cited)

| Class | Extra structure beyond K and site locality |
|---|---|
| G-D | Orientation bit and clock magnitude; mobility Γ (metric g); one real coordinate per site; a dissipation import (u3:333-338); arrow direction SUPPLIED |
| 𝒞₂ | Metric g (declared Euclidean) and potential V |
| G-S | Complex structure (ℝ²³ has none, so doubling is needed: "N extra real directions; σ normalization; J-linear extension"); ℏ; the readout identification |
| G-W | Momenta (phase-space doubling), a symplectic form (even dimension), masses, H, and an initial ensemble ("declared past hypothesis") |
| G-OU | Noise covariance Q ("declared substrate datum"), temperature, and FDT pairing (Q = K + Kᵀ for real Λ-B) |
| G-L | Bath realization and preparation; an infinite-dimensional dilation or indefinite H; readout; statistics; doubling; parity; ℏ. **It presupposes G-D.** |
| G-F | CAR statistics (supplied), complexification, parity superselection, filling (state), on-site shift |

## §6 Outcome

**Determination procedure (§4):**
1. **UNFORMULABLE: does not fire, but is contested.**
   - The comparison object can be stated as a *formal* comparison of declared operators, where 𝒜 is
     a function of K with its type, the type being fixed by 𝒜 via Lumer–Phillips, and a shared,
     uninterpreted one-parameter index.
   - Against: calling 𝒜 "the time generator", and the orientation/reversibility labels, read the
     structure under test. The no-`t` rule (`LEVEL0_DIRECTION_01.md:64-68`) is not met as written.
   - Those readings are handled by H-1, so step 1 is not triggered. **Flagged for owner ruling
     (F-1).**
2. **REPRESENTATIONAL-ONLY: no.** No pair is ≃_G on the same K (§5.2).
3. **EARNED post-H-1 selectors: S-loc, S-geo, S-obs, and S-acc at identity grade.** They eliminate
   **no class on (R) or (B)** at identity/record grade.
   - The only elimination the record calls "earned" is CA-1's P-2 cone cut of classical D. Under the
     record's later grading it is **CONDITIONAL on the supplied ℏ floor**, and it leaves a
     quantum-completed dissipative class.
   - Every other separation comes from CRITERION (definitional) or SUPPLIED items, which are prices.

> **S5-0 OUTCOME (proposed, mechanical): GENERATOR-IRREDUCIBLE/SUPPLIED.**
> - Nothing already earned selects the kind of time evolution.
> - The first-order dissipative generator is a **declared premise**, which the record itself states
>   ("presupposed, not derived").
> - The Level-0 properties that appear to favour it (passivity, gap → memory, CM, strict order,
>   FDT, gradient form) are **definitional to it** (H-1).
> - The static, non-circular earned structure (locality, geometry, observability, access identity)
>   is **generator-neutral**.
> - On the one K where classes were compared, **NG-1 holds at its demonstrated scope.**
> - Every surviving distinction is priced (§5.5) and supplied: statistics, complex structure,
>   symplectic structure, noise, orientation, Lorentz/gauge, ℏ floor.

**Flags for owner ruling:**
- **F-1. UNFORMULABLE alternative.** If the owner holds that the generator "type" itself imports the
  temporal structure under test, step 1 fires instead. The substantive reading (nothing earned
  selects the generator) is the same either way.
- **F-2. P-2 cone regrade.** CA-1's own verdict says "earned structure (the P-2 cone) eliminates a
  genuinely different carrier" (`CA1_CARRIER_VERDICT_01.md:17-19`). This audit reads it as
  CONDITIONAL, citing the later grading (ℏ floor SUPPLIED; `GRUT_WORKING_THEORY_01.md:329-332`) and
  CA-1's own escape clause. It needs owner confirmation, because it overrides CA-1's wording.
- **F-3. Pre-registration defect (auditor's own).** The §1 rule "a map that changes the K-functional
  counts as a different class" also catches a **scalar** rescaling c·K (the CA-1 T twin). That is a
  time-unit change, which SF-0 §3(3) quotients out.
  - Proposed correction: quotient constant rescalings in ≃_G.
  - No elimination above depends on it, so the outcome is unaffected.
- **F-4. Scope.** NG-1 is demonstrated on (R) only. No cross-class comparison exists on (B).
- **F-5. Class status.** G-L is a realization of G-D, not a peer. G-F differs from G-S only by
  supplied statistics plus state. The effective comparison set is therefore {G-D, G-OU, G-W, G-S},
  plus statistics as a separate supplied axis.

**What this does not say:**
- that the generator is underivable in principle;
- that any imported principle (least action, maximum entropy, …) would or would not select it;
- anything about derived magnitudes.

**Reading.** Together with the lift result (IRREDUCIBLE/SUPPLIED) and SFG-0 (no earned formation
variable), GRUT's supplied structure now reaches the **generator itself**. Level-0 certified property
edges *on* a presupposed dissipative generator over a declared K. **Neither the kind of time
evolution nor K is derived from anything earned.**

**Fences:**
- No new physics, no imports consumed, no S5-1.
- No SF-2, no gravity, no Π₀, no cosmology.

**HARD STOP for owner ruling:**
- the S5-0 terminal;
- F-1 … F-5;
- the next step.
