# Program E — Stage E0-A: Foundational Charter Freeze

---

## 1. Identity

### Technical

Program E is a theorem-first axiomatic investigation that begins from five structural primitives about histories, observers, information, consistency, and probability — without importing any field content, gravitational model, or EFT ansatz — and tests whether these primitives constrain the class of admissible dynamical frameworks tightly enough to derive necessity results about irreversibility, geometry-coupling, decoherence structure, or uniqueness. Program E is a NEW LAYER above GRUT I-III. It does not extend, revise, or reinterpret the GRUT EFT program. It asks a question that GRUT could not answer internally: is there a reason the universe must work this way?

### Public-facing

Program E asks what the universe MUST look like if it is to contain histories, observers, locally accessible information, self-consistent dynamics, and well-defined probabilities. It does not start from any specific theory of gravity or matter. It starts from structural requirements that any admissible universe must satisfy, and tests whether these requirements constrain physics more tightly than expected.

### Separation statement

| Item | Status |
|------|--------|
| GRUT I-III is closed as a bounded EFT ansatz | INHERITED. Read-only. Not contested. |
| Program E is not a GRUT continuation | DECLARED. E uses no GRUT-specific fields, equations, or parameters as starting input. |
| Any mapping to GRUT-type dynamics occurs ONLY in E4 (if at all) | DECLARED. Stages E1-E3 are GRUT-free. |
| No ToE claim exists or is inherited | DECLARED. ToE status requires necessity + uniqueness + UV closure + experimental confirmation — none of which Program E assumes. |

---

## 2. Structural Primitives

These are the starting axioms. They are chosen to be model-independent: no mention of fields, spacetime dimension, metric signature, or coupling constants.

| # | Primitive | Formal statement | Model-dependence check |
|---|-----------|-----------------|:----------------------:|
| **P1** | **Histories exist.** | There exists a set H of histories h. Each history is a complete specification of what happens from an initial to a final condition. H is non-empty. | NO model content. H is abstract. |
| **P2** | **Observers exist within histories.** | For each h ∈ H, there exists at least one subsystem O(h) ⊂ h that can be identified as an observer: a subsystem that records, processes, and is affected by the rest of h. | NO model content. O is functionally defined (recording + processing), not materially defined. |
| **P3** | **Information is locally accessible.** | Observer O(h) can access information only from a causal neighborhood: a connected region of the history defined by a partial ordering ≤ (causality). Information from outside the causal past of O is inaccessible. | INTRODUCES: a partial ordering (causal structure). Does NOT introduce: metric, dimension, or specific spacetime. |
| **P4** | **Dynamics is globally self-consistent.** | The set H of allowed histories admits no logical contradiction: for any h ∈ H, no subsystem of h generates an outcome incompatible with another subsystem of the same h. Formally: there exists a consistency functional C[h] such that C[h] = 1 for all h ∈ H and C[h'] = 0 for any contradictory h' ∉ H. | NO model content. C is abstract. The consistency condition is logical, not dynamical. |
| **P5** | **Operational probability assignments are well-defined.** | For any partition of H into classes {H_α}, there exist non-negative real numbers p(H_α) with Σ_α p(H_α) = 1 that represent the probability of each class. These assignments are consistent: they satisfy the sum rule for refinements and coarsenings of the partition. | INTRODUCES: a probability measure on H. Does NOT introduce: quantum mechanics, Born rule, or specific dynamics. Consistent with both classical and quantum probability. |

### Model-dependence audit

| Primitive | Introduces | Does NOT introduce |
|-----------|-----------|-------------------|
| P1 | Set H | Fields, spacetime, dimension |
| P2 | Subsystem O ⊂ h | Matter content, consciousness, biology |
| P3 | Partial ordering ≤ | Metric, light cones, specific causal structure |
| P4 | Consistency functional C | Equations of motion, action principle |
| P5 | Probability measure p | Born rule, path integral, quantum mechanics |

**Ambiguity flag (AF-1):** P3 introduces a causal structure (partial ordering) without specifying its origin. In standard physics, causal structure comes from the metric. In Program E, it is PRIMITIVE — it is assumed, not derived from a metric. This is a deliberate choice: we do not assume spacetime geometry. The partial ordering could be implemented by a Lorentzian metric, a causal set, a discrete graph, or any other structure that provides a consistent partial ordering. Program E is agnostic about the implementation.

**Ambiguity flag (AF-2):** P5 assumes probabilities exist but does not specify whether they are classical or quantum. The Born rule is NOT assumed. If the theorem program requires quantum probability specifically, this must be added as an ADDITIONAL axiom (labeled explicitly) in E1.

---

## 3. Five-Axis Theorem Table

### Axis A1: Consistency of histories

| Field | Content |
|-------|---------|
| **Formal question** | Does the consistency condition P4, applied to histories with local information access P3, constrain the allowed dynamics to decoherent-history-type structures? |
| **Candidate frameworks** | Decoherent histories (Griffiths, Omnès, Gell-Mann & Hartle). Consistent histories formalism. Topos-theoretic approach (Isham, Döring). |
| **Success condition** | A theorem showing that P1+P3+P4 imply the existence of a decoherence functional D[h, h'] with the property that D[h, h'] ≈ 0 for sufficiently coarse-grained distinct histories. |
| **Failure condition** | A counterexample: a set H satisfying P1+P3+P4 that does NOT admit a decoherence functional. |

**Theorem T1: History consistency implies decoherence structure**

```
ASSUMPTIONS:
  P1 (histories exist), P3 (local information access), P4 (global consistency),
  P5 (probabilities well-defined).

  Additional: the probability assignment p(H_α) is additive on disjoint
  history classes (p(H_α ∪ H_β) = p(H_α) + p(H_β) for disjoint α, β).

CLAIM:
  For any partition of H into fine-grained histories {h_i}, the probability
  assignment p requires a decoherence condition:

  p(H_α) = Σ_{i ∈ α} p(h_i) is well-defined only if the "interference terms"
  between distinct fine-grained histories vanish:

  Re D(h_i, h_j) ≈ 0 for i ≠ j within the same coarse-grained class.

  This is the standard consistency condition of the decoherent histories formalism.

PROOF STANDARD: Full derivation from P1+P3+P4+P5+additivity, or counterexample.

DISPROOF CONDITION:
  A probability assignment satisfying P5 + additivity that is well-defined
  without any decoherence condition (i.e., works for histories with nonzero
  "interference" between components).

STRUCTURAL NECESSITY:
  If T1 is proven: the decoherence functional is a necessary consequence
  of consistent probability assignment over histories. This makes decoherence
  STRUCTURAL, not model-dependent.
```

---

### Axis A2: Covariance + irreversibility compatibility

| Field | Content |
|-------|---------|
| **Formal question** | Can irreversible dynamics (preferred time direction) coexist with diffeomorphism invariance (no preferred coordinates)? If so, what constraints does this impose on the dynamical structure? |
| **Candidate frameworks** | CTP formalism on curved backgrounds (Calzetta & Hu). Dissipative EFTs with diffeomorphism invariance (Salcedo et al. 2025). Thermal field theory on curved spacetime. |
| **Success condition** | A theorem showing that irreversible first-order dynamics on a diffeomorphism-invariant background necessarily takes a specific structural form (e.g., must couple to extrinsic curvature, must have a specific noise-dissipation relation). |
| **Failure condition** | A demonstration that any first-order dissipative structure can be made diffeomorphism-invariant without additional constraints (covariance imposes no structural restriction on the dissipative sector). |

**Theorem T2: Covariant irreversibility constrains dissipative coupling**

```
ASSUMPTIONS:
  P1, P3 (causal structure), P4 (consistency).
  Additional A2-1: The causal structure from P3 is implemented by a
    Lorentzian metric g_{μν} with diffeomorphism invariance.
  Additional A2-2: There exists a first-order dissipative scalar field Φ
    on this background, with dynamics derivable from a CTP action.
  Additional A2-3: The CTP action is diffeomorphism-invariant.

CLAIM:
  The dissipative term in the CTP action for Φ must involve the
  extrinsic curvature K_{μν} or the normal vector n^μ to a foliation.
  Specifically: a preferred time direction (needed for irreversibility)
  that is compatible with diffeomorphism invariance must be defined by
  the geometry (e.g., the unit normal to spatial hypersurfaces).

  This constrains the dissipative sector to couple to geometric
  objects (K, n), not to arbitrary external structures.

PROOF STANDARD: Derivation from A2-1..A2-3, or explicit counterexample
  (a diffeomorphism-invariant CTP action with dissipation that does NOT
  couple to geometric objects).

DISPROOF CONDITION:
  A diffeomorphism-invariant dissipative CTP action where the time
  direction is defined by a non-geometric structure (e.g., a fixed
  external vector field that is not derived from the metric).

STRUCTURAL NECESSITY:
  If T2 is proven: irreversible dynamics on a covariant background
  necessarily couples to geometry. This would provide a DERIVATION of
  geometry-coupling (not just an ansatz).
```

**Ambiguity flag (AF-3):** A2-1 imports a Lorentzian metric, which is model content beyond the primitives P1-P5. This is declared explicitly. T2 is a CONDITIONAL theorem: IF the causal structure is implemented by a Lorentzian metric, THEN covariant irreversibility constrains the dissipative coupling. The "if" is an additional axiom, not a primitive.

---

### Axis A3: Entropy / memory structural necessity

| Field | Content |
|-------|---------|
| **Formal question** | Does the existence of a consistent, locally accessible, probabilistic history framework necessarily imply an entropy-like monotonic functional? If so, does this functional constrain the dynamics to relaxational (equilibrium-approaching) form? |
| **Candidate frameworks** | Second law from typicality arguments (Goldstein, Lebowitz). Entropy from coarse-graining (Jaynes). Generalized second law (Bekenstein, Wall). |
| **Success condition** | A theorem: P1+P3+P4+P5 → existence of a functional S[h] that is non-decreasing along any consistent history. |
| **Failure condition** | A consistent history set H satisfying P1-P5 with no monotonic functional. |

**Theorem T3: Consistent histories require entropy growth**

```
ASSUMPTIONS:
  P1-P5 (all five primitives).
  Additional A3-1: H admits a coarse-graining operation that maps
    fine-grained histories to coarse-grained ones.
  Additional A3-2: The probability assignment p is "typical" in the sense
    that p is uniform (or near-uniform) over fine-grained histories consistent
    with each coarse-grained macrostate.

CLAIM:
  There exists a functional S[macrostate] = log(number of compatible
  microstates) that is non-decreasing in the causal ordering:
  if macrostate M₁ ≤ M₂ (M₂ is in the causal future of M₁), then
  S[M₂] ≥ S[M₁] with probability → 1 as the number of microstates grows.

PROOF STANDARD: Derivation (this is essentially the Boltzmann H-theorem
  argument applied to histories). The question is whether P1-P5 + A3-1 + A3-2
  are sufficient, or whether additional dynamical assumptions are needed.

DISPROOF CONDITION:
  A consistent history framework satisfying all assumptions where the
  Boltzmann entropy can decrease along consistent histories with
  non-negligible probability.

STRUCTURAL NECESSITY:
  If T3 is proven: entropy growth is a structural consequence of
  consistent probabilistic histories + typicality. This would ground
  irreversibility in information-theoretic structure, not in dynamics.
```

---

### Axis A4: Information-theoretic constraints

| Field | Content |
|-------|---------|
| **Formal question** | Does local information accessibility (P3), combined with consistency (P4), impose bounds on the rate of information loss that constrain the dynamical structure? |
| **Candidate frameworks** | Quantum channel capacity theory. Holographic bounds (Bousso). Bekenstein bound. Quantum error correction / approximate recovery. |
| **Success condition** | A theorem: P3+P4+P5 → the rate of information loss (mutual information decay) is bounded by a geometric quantity (e.g., area, curvature). |
| **Failure condition** | Demonstration that information loss rate is unconstrained by P3+P4+P5 alone (any rate is compatible). |

**Theorem T4: Local accessibility bounds information loss rate**

```
ASSUMPTIONS:
  P1-P5.
  Additional A4-1: The causal structure from P3 is implemented by a
    geometry with a notion of "area" bounding causal diamonds.
  Additional A4-2: The observer O has finite information-storage capacity
    bounded by the area of its causal boundary (a Bekenstein-type bound).

CLAIM:
  The rate at which the observer's information about the external history
  decays is bounded by a quantity proportional to the area of the
  observer's causal boundary divided by the Planck area:

  dI/dt ≤ A / (4 l_P²) × (some function of curvature)

  This bounds the dissipation/relaxation rate from above.

PROOF STANDARD: Derivation from the stated assumptions. Note: A4-1 and
  A4-2 import significant geometric and quantum-gravitational content
  (area, Planck length). These are ADDITIONAL axioms beyond P1-P5.

DISPROOF CONDITION:
  A system satisfying all assumptions where I decays faster than
  the area bound allows.

STRUCTURAL NECESSITY:
  If T4 is proven: the relaxation timescale τ is bounded below by a
  geometric quantity. This would partially DERIVE τ from geometry —
  a parameter-collapse result.
```

**Ambiguity flag (AF-4):** T4 imports the Bekenstein bound (A4-2), which is itself a deep conjecture, not a proven theorem in full generality. If T4 is pursued, the status of A4-2 must be tracked separately (proven for black holes, conjectured for general systems).

---

### Axis A5: Uniqueness theorem path

| Field | Content |
|-------|---------|
| **Formal question** | Given the constraints from T1-T4 (whichever are proven), is the resulting dynamics class unique, or does it admit multiple inequivalent realizations? |
| **Candidate frameworks** | Classification of consistent decoherence functionals. Classification of covariant dissipative EFTs. Uniqueness theorems for Markovian open quantum systems (Lindblad). |
| **Success condition** | A theorem: the dynamics class satisfying T1-T4 constraints is unique up to a finite number of parameters. |
| **Failure condition** | An explicit construction of two inequivalent dynamics satisfying all T1-T4 constraints. |

**Theorem T5: Uniqueness under structural constraints**

```
ASSUMPTIONS:
  T1 is proven (decoherence structure necessary).
  T2 is proven (covariant irreversibility couples to geometry).
  T3 is proven (entropy growth necessary).
  [T4 optional: information bound on τ.]

CLAIM:
  The class of first-order dissipative scalar dynamics on a covariant
  background satisfying T1+T2+T3 is a FINITE-DIMENSIONAL family
  parametrized by at most N free constants, where N is determined by
  the assumptions (not by the specific model).

  In the strongest case: N = 0 (unique dynamics, no free parameters).
  In the weakest case: N is bounded (finite parameter family).

PROOF STANDARD: Classification theorem. Enumerate the allowed dynamics
  classes and count free parameters.

DISPROOF CONDITION:
  An infinite-dimensional family of inequivalent dynamics satisfying
  all constraints. (This would mean the constraints are too weak to
  select a finite class.)

STRUCTURAL NECESSITY:
  If N = 0: the dynamics is uniquely determined by the axioms → ToE-level
  inevitability. If N > 0 but finite: partial inevitability (structural
  constraints reduce but do not eliminate freedom). If N = ∞: no
  inevitability (constraints are insufficient).
```

---

## 4. Exit-Token Criteria

| Token | Objective criteria |
|-------|--------------------|
| **necessity_emerges** | At least two of T1-T4 are PROVEN with full proofs from P1-P5 + explicitly labeled additional axioms. T5 shows N < ∞ (finite parameter family). The proven constraints rule out at least one member of the GRUT-III generic D1 class that satisfies the axioms but not the constraints. |
| **conditional_necessity** | At least one of T1-T4 is proven, but T5 shows N is still large (the constrained class is broad). The constraints narrow the generic class but do not determine a unique or small family. OR: T1-T4 require additional axioms (beyond P1-P5) that are themselves unproven conjectures (e.g., A4-2 Bekenstein bound). |
| **non_uniqueness_persists** | All of T1-T4 are either disproven (counterexample) or proven but T5 shows N = ∞ (infinite family survives). The structural primitives P1-P5 do not constrain the dynamics more than the generic D1 class already does. |
| **blocked** | The program cannot proceed: the primitives P1-P5 are too weak to derive any dynamical constraint, and no promising additional axiom has been identified. |

---

## 5. Claim Policy

### Allowed during Program E

| # | Claim | Condition |
|---|-------|-----------|
| EA1 | "Program E tests whether structural primitives constrain dynamics." | Always (descriptive). |
| EA2 | "Theorem T_n is proven / disproven / open." | Must have proof or counterexample at formal standard. |
| EA3 | "The constrained dynamics class has N free parameters." | Must be derived from a classification theorem (T5). |
| EA4 | "Primitive P_n combined with axiom A_n-m implies constraint C." | Must be an explicit derivation with labeled assumptions. |
| EA5 | GRUT-III established claims (E-F1..13) are inherited. | Read-only. No modification. |

### Forbidden during Program E

| # | Claim | Reason |
|---|-------|--------|
| EF1 | "The universe necessarily has GRUT-type dynamics." | Requires necessity_emerges + mapping-back (E4) + external validation. |
| EF2 | "Program E proves GRUT is a ToE." | F1 perpetual. ToE requires necessity + uniqueness (N=0) + UV completion + experimental confirmation. |
| EF3 | "GRUT-III's closure was wrong." | GRUT-III was correct at its level. Program E is a different level. |
| EF4 | "The structural primitives P1-P5 are the only possible axioms." | Axiom choice is underdetermined. Other primitive sets may exist. |
| EF5 | "Theorem T_n is proven" without explicit proof at formal standard. | No claim-by-assertion. |
| EF6 | Importing GRUT-specific content (Φ, X = β+αR, τ, USL) into E1-E3. | E1-E3 are GRUT-free by charter. GRUT content enters ONLY in E4 mapping. |
| EF7 | "Covariance is established" without explicit proof of T2. | GRUT-III blacklist X1 remains binding until T2 is proven. |

---

## 6. Stage Skeleton

| Stage | Intent | First gate | GRUT content? |
|-------|--------|-----------|:-------------:|
| **E1** | Formalize P1-P5 and additional axioms A_n-m. Check internal consistency of the axiom set. Test independence (no axiom is derivable from the others). | E1-G1: Axiom set formally stated, consistent, and independent. | NO |
| **E2** | Attempt proofs of T1-T4 from the E1 axiom set. For each: proof, counterexample, or impossibility argument. | E2-G1: Each T1-T4 has a definitive result. | NO |
| **E3** | Uniqueness pressure test (T5). If T1-T4 results constrain the dynamics class: classify it. Count free parameters N. Test against the generic D1 class from GRUT-III Book D. | E3-G1: N determined or bounded. Generic-class comparison completed. | MINIMAL (D1 class used as comparison only) |
| **E4** | Mapping-back test. If E2-E3 produce a constrained dynamics class: determine whether GRUT-type dynamics (relaxation-to-geometry, constitutive law form) is a member. If yes: GRUT is within the necessary class. If no: GRUT is excluded by the axioms. | E4-G1: GRUT membership in the constrained class explicitly tested. | YES (mapping test) |

---

## 7. Gate Table

| Gate | Criterion | Status | Evidence |
|:----:|-----------|:------:|---------|
| **E0A-G1** | Structural primitives defined without model dependence | **PASS** | P1-P5 introduce: set H, subsystem O, partial ordering ≤, consistency C, probability p. They do NOT introduce: fields, metric, dimension, coupling constants. Model-dependence audit in Section 2 confirms zero model content in P1-P5. Two ambiguity flags (AF-1, AF-2) are raised and logged, not hidden. |
| **E0A-G2** | Five theorem targets formal and testable | **PASS** | T1-T5 each have: assumptions, exact claim, proof standard, disproof condition, structural-necessity interpretation. Each is mathematically precise. Ambiguity flags AF-3 and AF-4 raised for T2 and T4 where additional axioms import model content. |
| **E0A-G3** | Exit-token criteria operational | **PASS** | Four tokens with objective criteria. necessity_emerges requires 2+ proofs + N < ∞ + exclusion of generic-class members. non_uniqueness_persists requires disproof or N = ∞. Criteria are binary-testable, not subjective. |
| **E0A-G4** | Claim policy anti-inflation complete | **PASS** | 5 allowed claims (EA1-EA5) with conditions. 7 forbidden claims (EF1-EF7) with reasons. Includes: no ToE (EF2), no GRUT import in E1-E3 (EF6), no covariance without proof (EF7). |
| **E0A-G5** | Workplan executable as theorem program | **PASS** | E1-E4 defined with one-line intents, first gates, and GRUT-content flags. Stages are ordered by logical dependency (E1 axioms → E2 proofs → E3 uniqueness → E4 mapping). No stage assumes the outcome of a later stage. |

## Decision Token

### **axiomatic_charter_frozen**

The charter defines a self-contained theorem program starting from five model-independent structural primitives. Five theorem targets are formally stated, each testable. Four exit tokens have objective criteria. Seven forbidden claims prevent inflation. The workplan is executable as a four-stage theorem program with no hidden assumptions and no GRUT-specific content in the first three stages.

Program E may begin at Stage E1.

---

*Program E Stage E0-A complete. Decision: axiomatic_charter_frozen. Five primitives (P1-P5): histories, observers, local access, consistency, probability. Five theorems (T1-T5): decoherence necessity, covariant irreversibility, entropy growth, information bounds, uniqueness. Four exit tokens. Seven anti-inflation rules. Four stages (E1-E4). Two ambiguity flags (AF-1: causal structure origin; AF-2: classical vs quantum probability). No model content in primitives. No GRUT import before E4. Charter frozen.*
