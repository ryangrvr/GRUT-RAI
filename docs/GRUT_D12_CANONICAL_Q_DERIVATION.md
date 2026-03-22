# GRUT Phase D12: Canonical Source/Charge Derivation

## 1. Executive Result

**D12 classification: principled_and_strongly_constrained**

Q is best identified with the topological winding number (n) times the O(3)
vacuum expectation value (eta):

    Q = n * eta,    n in Z,    eta^2 = 1/(8*pi)

This identification is:

- **Topologically grounded**: n is an integer homotopy invariant from
  pi_2(S^2) = Z, classifying hedgehog configurations of the O(3) triplet.
- **Quantized**: n takes integer values only; it cannot be continuously
  deformed.
- **Topologically conserved**: for smooth field configurations, n is invariant
  under continuous deformation.
- **Coefficient-matched**: eta^2 = 1/(8*pi) = COMP_B_COEFF, determined by
  a single free parameter (eta) of the defect sector.
- **Aligned with all tested requirements**: shape match (1/r^2 tail),
  defect realization (O(3) hedgehog), and D11 exact closure viability.

However, Q is **not canonically derived** because the O(3) triplet sector is
a minimal extension of canonical GRUT, not a consequence of the scalar-memory
theory.  The extension is uniquely selected by the homotopy requirement
(pi_2 non-trivial demands at least an O(3) triplet), but the requirement
for the extension itself is not derived from within GRUT.

---

## 2. Why Q Remains the Main Blocker After D11

D11 established that the dual-sector Companion architecture (macro scalar +
defect hedgehog) survives exact two-field treatment.  The D9 proxy is
retrospectively assessed as a good approximation on the physical domain
[R_eq, R_ext] = [1/3, 2.0].  The Companion architecture is therefore
numerically viable.

The remaining blocker is not numerical viability but **ontological status**.
The defect sector's charge-like parameter Q has been:

- Used in the Family 4 source law (X = M/r^2 + Q/r) since Source-Law
  Program I.
- Realized through the O(3) hedgehog defect (D1-D2) with tail energy
  eta^2/r^2.
- Validated through D6-D11 companion architecture construction and exact
  closure.

But Q has never been **canonically derived**.  It was introduced as a
candidate through source-law narrowing and defect-sector admissibility.
The question is: does it earn a stronger status than "adopted through
narrowing"?

D12 answers this question by systematic ontology testing.

---

## 3. What Phase 6C and Source-Law Program I Require of Q

### 3.1 Phase 6C: Two-Component Decomposition

The Phase 6 static equilibrium gives f(R_eq) = -17.71 (LOCKED).  The
minimal additive energy density that restores metric positivity decomposes
as:

    epsilon_min(r) = Component A + Component B
                   = |rho_eq(r)| + 1/(8*pi*r^2)

| Component | Form | Radial dependence | Coefficient | Source |
|-----------|------|-------------------|-------------|--------|
| A | M^2/(2*tau^2*r^4) | 1/r^4 | RHO_EQ_COEFF | Scalar-memory sector (LOCKED) |
| B | 1/(8*pi*r^2) | 1/r^2 | COMP_B_COEFF = 1/(8*pi) | Unknown (D12 target) |

### 3.2 Route B/C Closure

- **Route C (Markov)**: Energy density is 1/r^4 only.  Insufficient.
- **Route C (non-Markov)**: Source-profile locking theorem: any kernel
  K(s) leaves epsilon ~ 1/r^4.  Structurally closed.
- **Route B (Galley CTP)**: Post-projection identical to Route C.
  Pre-projection g_- sector uncomputed but does not provide 1/r^2.

All GRUT-native classical mechanisms for Component B are exhausted.

### 3.3 Source-Law Program I: Family Taxonomy

Five source families tested.  Results:

| Family | Formula | Viable? | GRUT-native? | Component B? |
|--------|---------|---------|--------------|--------------|
| 1 (algebraic, p=1/2) | X = sqrt(M)/r | Yes | No (singular F(Phi)) | Yes |
| 2 (gradient) | X = M/r^2 + derivatives | No | Yes | No (structurally closed) |
| 3 (integral) | X = M/r^2 + integral | Contaminated | No | Contaminated |
| 4 (defect/topological) | X = M/r^2 + Q/r | Yes | No (Q undefined) | Yes (cleanest) |
| 5 (processing-invariant) | X = G(Phi_eq, ...) | Collapses | Yes | No |

Family 4 is the cleanest viable mechanism.  It requires Q.

### 3.4 What Q Must Supply (Requirement Summary)

| Requirement ID | Source Phase | What Q must supply |
|----------------|-------------|-------------------|
| REQ_6C_SHAPE | Phase 6C | Energy density with 1/r^2 radial profile |
| REQ_6C_COEFF | Phase 6C | Coefficient equals or tunable to 1/(8*pi) |
| REQ_ROUTEBC_CLOSURE | Route B/C + SLP-I | GRUT-native origin or principled extension |
| REQ_D1_ADMISSIBILITY | D1 | Alignment with O(3) hedgehog defect realization |
| REQ_D11_VIABILITY | D11 | Consistency with exact coupled BVP solution |

---

## 4. Candidate Ontologies for Q

Six candidate ontologies were tested:

### 4.1 Topological Winding Number

**Formula**: Q = n * eta, n in Z, eta = 1/sqrt(8*pi)

**Justification**: The O(3) triplet has vacuum manifold S^2 with
pi_2(S^2) = Z (D1 homotopy analysis).  The hedgehog ansatz
Phi_a = eta * f(r) * hat{x}_a has winding number n = 1.  The asymptotic
energy density is eta^2/r^2, matching Component B.

**Strengths**: Quantized, topologically conserved, matches all five
requirements (4 strong, 1 partial), non-circular.

**Weakness**: Requires the O(3) triplet extension.  The partial score on
REQ_ROUTEBC_CLOSURE reflects that the extension is principled (uniquely
selected by homotopy) but still external to canonical GRUT.

### 4.2 Noether Charge from O(3)

**Formula**: Q_a = integral d^3x (dL/d(dot{Phi}_a))

**Justification**: O(3) global symmetry gives three conserved Noether
charges in the unbroken phase.

**Fatal obstruction**: The hedgehog breaks O(3) completely (maps spatial
directions to field directions).  No Noether charge survives symmetry
breaking.  The hedgehog has zero Noether charge.

**Rating**: Eliminated.

### 4.3 Geometric Support Invariant

**Formula**: Q_geom defined by Q_geom^2/(2*tau^2) = 1/(8*pi)

**Justification**: Backward definition from the Phase 6C requirement.

**Fatal obstruction**: Circular.  Defines Q by requiring it to match
Component B.  Provides no independent explanatory content.

**Rating**: Eliminated.

### 4.4 Curvature-Triggered Source Invariant

**Formula**: L_trigger = xi * R * |vec_Phi|^2

**Justification**: Non-minimal curvature coupling could nucleate defects
in regions of strong gravity.  Aligned with D10 trigger analysis.

**Weakness**: The coupling constant xi is a free parameter (not fixed to
produce eta^2 = 1/(8*pi)).  The tail profile depends on the curvature
profile, not guaranteed to be 1/r^2.  Adds a free parameter beyond the
topological candidate.

**Rating**: Weakly viable.

### 4.5 Memory-Sector Emergent Charge

**Formula**: Q_mem = functional of integral kernel K(t-t')

**Justification**: If the memory equation could generate Q through
nonlocal effects, Q would be GRUT-native.

**Fatal obstruction**: Source-Law Program I proves: (a) the source-profile
locking theorem closes all kernel-based routes, (b) Family 5
(processing-invariant) collapses to Family 1 at equilibrium.  No 1/r^2
mechanism exists in the memory sector.

This is the only GRUT-native candidate.  It is eliminated by mechanism,
not by nativeness.

**Rating**: Eliminated.

### 4.6 Effective Defect Charge

**Formula**: Q_eff defined by epsilon_defect(r) -> Q_eff^2/r^2 as r -> infinity

**Justification**: Operational definition: Q_eff is whatever coefficient
appears in the 1/r^2 tail of the defect energy density.

**Weakness**: Purely phenomenological.  Does not identify the microscopic
origin of Q.  Shape and coefficient match are definitional (circular in a
weak sense).  No conservation or quantization.

**Rating**: Weakly viable.

---

## 5. Derivational Tests and Eliminations

### 5.A Requirement-Matching Table

| Requirement | Topological winding | Noether charge | Geometric invariant | Curvature trigger | Memory emergent | Effective charge |
|-------------|:-------------------:|:--------------:|:-------------------:|:-----------------:|:---------------:|:----------------:|
| REQ_6C_SHAPE | **STRONG** | partial | partial | partial | none | **STRONG** |
| REQ_6C_COEFF | **STRONG** | none | weak | weak | none | weak |
| REQ_ROUTEBC_CLOSURE | partial | none | weak | partial | none | none |
| REQ_D1_ADMISSIBILITY | **STRONG** | weak | weak | partial | none | partial |
| REQ_D11_VIABILITY | **STRONG** | none | weak | partial | none | partial |
| **Total strong** | **4** | **0** | **0** | **0** | **0** | **1** |
| **Total partial** | **1** | **1** | **1** | **4** | **0** | **2** |
| **Total failed** | **0** | **4** | **4** | **1** | **5** | **2** |

### 5.B Candidate Ontology Ranking Table

| Rank | Candidate | Justification source | Shape match | Coeff match | Topology/Geometry | Conservation | GRUT-native | Rating |
|------|-----------|---------------------|:-----------:|:-----------:|:-----------------:|:------------:|:-----------:|--------|
| 1 | Topological winding number | pi_2(S^2) = Z | Yes | Yes | Topological | Quantized (n in Z) | No | **best_supported** |
| 2 | Effective defect charge | Operational definition | Yes (def.) | Yes (tuned) | Neither | None | No | weakly_viable |
| 3 | Curvature-triggered source | Non-minimal coupling | Partial | No | Geometric | None | No | weakly_viable |
| 4 | Noether charge | O(3) symmetry | Partial | No | Geometric (broken) | Broken | No | eliminated |
| 5 | Geometric support invariant | Phase 6C requirement | Yes (taut.) | Yes (taut.) | Nominal | None | No | eliminated |
| 6 | Memory-sector emergent | Memory kernel | No | No | Neither | N/A | **Yes** | eliminated |

### 5.C Eliminations

Three candidates eliminated:

1. **Noether charge**: O(3) is completely broken by the hedgehog.  No
   surviving Noether charge.
2. **Geometric support invariant**: Circular definition.  Defines Q from
   the requirement rather than deriving it.
3. **Memory-sector emergent**: Mechanism-eliminated by Source-Law Program I.
   This is the only GRUT-native candidate, and its elimination is the
   core reason why Q cannot be canonically derived.

### 5.D Upgrades

One candidate upgraded to best_supported:

- **Topological winding number**: 4/5 requirements strongly satisfied,
  quantized (n in Z), topologically conserved, non-circular.  The single
  partial score (REQ_ROUTEBC_CLOSURE) reflects that the O(3) extension is
  principled but not derived.

---

## 6. Mapping from Q to the Defect Realization

The mapping from Q to the O(3) hedgehog defect is:

    Q = n * eta

where:
- n is the winding number from pi_2(S^2) = Z
- eta is the O(3) VEV, with eta^2 = 1/(8*pi) fixed by Component B

The hedgehog ansatz Phi_a = eta * f(r) * hat{x}_a (D1) produces the
radial profile f(r) satisfying:

    f'' + (2/r)f' - (2/r^2)f - lambda*eta^2*f*(f^2-1) = 0
    f(0) = 0, f(infinity) = 1

The energy density decomposes (D1-D2) as:

    epsilon(r) = (1/2)*eta^2*(f')^2 + eta^2*f^2/r^2 + (1/4)*lambda*eta^4*(f^2-1)^2

In the asymptotic regime (f -> 1, f' -> 0):

    epsilon(r) -> eta^2/r^2 = COMP_B_COEFF/r^2

This is exactly Component B.

The mapping is:
1. Phase 6C identifies Component B = 1/(8*pi*r^2)
2. D1 identifies O(3) triplet as minimal admissible field content
3. The hedgehog tail gives epsilon -> eta^2/r^2
4. The coefficient match requires eta^2 = 1/(8*pi) = COMP_B_COEFF
5. The winding number n = 1 is the minimal hedgehog sector

D2 confirms this numerically.  D6-D11 confirm the Companion architecture
survives coupling and exact closure.

---

## 7. Canon Classification of Q After D12

### Classification: principled_and_strongly_constrained

**Canon statement**: Q is the topological winding number (n) times the
O(3) vacuum expectation value (eta): Q = n * eta with n in Z and
eta^2 = 1/(8*pi).  This identification is principled (topologically
grounded, quantized, conserved) and strongly constrained (uniquely
selected by the homotopy requirement and coefficient matching), but
not canonically derived (the O(3) sector is a minimal extension, not
a consequence of GRUT).

**Why not "canonically derived"**: The only GRUT-native candidate
(memory-sector emergent) is mechanism-eliminated.  The topological
winding number requires the O(3) triplet, which is an extension.
The extension is uniquely selected by the homotopy requirement, but
the need for the extension is not itself derived from the GRUT
scalar-memory structure.

**Why not "still effective only"**: The topological candidate scores
4/5 requirements strong, is quantized and conserved, and is selected
by a principled mathematical criterion (homotopy theory).  This is
materially stronger than a purely phenomenological parameterization.

---

## 8. Remaining Ontology Gaps

After D12, the following gaps remain:

1. **O(3) sector derivation**: The O(3) triplet is a minimal extension
   of GRUT, not derived from it.  Closing this gap requires showing
   that the GRUT field equations or their quantum corrections necessarily
   produce an O(3) triplet, or identifying a deeper principle that
   simultaneously requires both sectors.

2. **eta value derivation**: eta^2 = 1/(8*pi) is fixed by the Phase 6C
   requirement, not predicted by the topology.  A canonical derivation
   would need to predict this value from first principles.

3. **Winding number selection**: n = 1 is assumed as the minimal
   hedgehog.  No stability or energetic argument selects n = 1 over
   higher winding numbers within the current framework.

4. **Lambda and g_p prediction**: The defect self-coupling lambda and
   portal coupling g_p remain scanned parameters (D9-D11).  No mechanism
   predicts their values.

5. **Dynamical source**: D11 keeps X(r) = M/r^2 fixed.  A fully
   self-consistent treatment would need to allow the source to respond
   to the defect back-reaction.

---

## 9. Recommended Canon Update

### Before D12

- Q: undefined in canonical GRUT
- Defect sector: provisional candidate extension (D1 status)
- Component B: identified requirement, no mechanism (Phase 6C status)
- Source ontology: partially viable, no GRUT-native mechanism (SLP-I status)

### After D12

- Q: topological winding number n * eta, principled and strongly
  constrained (D12 status)
- Defect sector: best-supported realization of Component B through
  O(3) hedgehog with pi_2(S^2) = Z
- Component B: realized by defect sector with eta^2 = 1/(8*pi),
  validated through D11 exact closure
- Source ontology: **principled_and_strongly_constrained** (upgraded
  from "partially viable")

### Canon-level claims after D12

1. Q = n * eta is the best-supported ontology for the Component B source.
2. The O(3) triplet is the minimal admissible field content (pi_2 criterion).
3. The winding number is quantized (n in Z) and topologically conserved.
4. The coefficient eta^2 = 1/(8*pi) is determined by a single parameter
   matching the Phase 6C requirement.
5. The defect realization is validated through D1-D2 (admissibility and
   numerics) and D6-D11 (architecture and exact closure).

### Canon-level non-claims after D12

1. Q is NOT canonically derived.
2. The O(3) sector is NOT derived from GRUT.
3. eta^2 = 1/(8*pi) is NOT predicted; it is required.
4. n = 1 is NOT derived; it is assumed.
5. Lambda and g_p are NOT predicted; they are scanned.

---

## 10. Explicit Nonclaims

1. D12 does not claim Q is derived from first principles.  "Principled
   and strongly constrained" is materially weaker than "derived."

2. D12 does not equate topological grounding with canonical derivation.
   A quantity can be topologically well-defined and still not uniquely
   required by the deeper theory.

3. D12 does not claim the O(3) triplet is the unique field content for
   metric positivity.  It is the minimal admissible content from D1's
   homotopy analysis.

4. D12 does not confuse source-class signature with particle
   identification.  Q = n * eta is a source ontology statement, not a
   particle physics claim.

5. D12 does not use elegance, thematic similarity, consciousness,
   observer, or philosophical arguments as physics evidence.

6. D12 does not claim to close the ontology gap completely.  It narrows
   the gap from "undefined" to "principled and strongly constrained"
   and precisely identifies what remains.

7. The winding number n = 1 for the minimal hedgehog is assumed, not
   derived from a stability or energetic argument.

8. D12 does not address whether the GRUT framework uniquely requires
   metric positivity in the strong-field interior.

9. D12 makes no prediction about lambda (defect self-coupling) or g_p
   (portal coupling).

10. The classification is within the six tested candidate ontologies.
    Untested ontologies may exist.

---

## Appendix A: Closure of the Logical Circle

Phase 6C identifies the metric positivity obstruction and its two-component
decomposition (A ~ 1/r^4, B ~ 1/r^2).  Route B/C and Source-Law Program I
exhaust GRUT-native mechanisms, isolating Family 4 (Q/r) as the only clean
candidate.  D1's homotopy analysis selects the O(3) triplet as the minimal
admissible field content (pi_2(S^2) = Z), whose hedgehog configuration
produces Q = n * eta with tail energy eta^2/r^2.  D2 through D9 construct
and validate the dual-sector architecture, and D11 confirms it survives
exact treatment.  Q is therefore best understood as the topological winding
number (n = 1) times the O(3) vacuum expectation value (eta), with
eta^2 = 1/(8*pi) fixed by the Component B requirement.  This identification
is principled and strongly constrained -- the topology selects the field
content, the homotopy quantizes the winding number, and the coefficient is
determined by a single parameter (eta) -- but it is not a canonical
derivation because the O(3) sector is an extension of GRUT, not derived
from it.

---

## Appendix B: Phase D12 Outcome Table

| Phase | Status | Classification |
|-------|--------|---------------|
| D12 | PRINCIPLED | principled_and_strongly_constrained |

Phase status key:
- LOCKED: result cannot change without upstream revision
- STRONGLY SUPPORTED: multiple independent tests confirm
- PROVISIONAL: formulated but not yet fully validated
- REJECTED: failed in tested form
- PROXY-DEPENDENT: result depends on a proxy that may not survive exact test
- PRINCIPLED: ontologically grounded and strongly constrained, but not derived

---

## Appendix C: Assumptions (10)

1. Q refers to the charge-like parameter in the Family 4 source law
   modification X = M/r^2 + Q/r.
2. The requirement chain is reconstructed from documented prior-phase results.
3. Candidate ontologies are tested against five explicit requirements.
4. The topological winding number analysis uses pi_2(S^2) = Z.
5. The hedgehog tail energy density eta^2/r^2 is from D1-D2 (locked).
6. No new physics is introduced in D12.
7. The classification logic is deterministic.
8. Conservation of topological charge means: winding number n is integer
   and invariant under continuous deformation.
9. The coefficient matching condition eta^2 = 1/(8*pi) is a requirement
   from Phase 6C, not a prediction.
10. D12 does not address particle identification or quantum corrections.

---

## Appendix D: Regression Status

- Module tests: 109 passed, 0 failed (tests/test_canonical_q_derivation.py)
- 11 test classes covering: constants, classification options, assumptions,
  requirements, candidates, specific candidate properties, ranking,
  matching table, logical circle, D12 classification, serialization
- Full repository regression: to be confirmed after D12 integration

---

## Appendix E: Code Summary

**Module**: `grut/canonical_q_derivation.py` (~850 lines)

Key structures:
- 5 `PhaseRequirement` entries reconstructing the D1-D11 requirement chain
- 6 `OntologyCandidate` entries with per-requirement test results
- 30 explicit `OntologyTest` evaluations (6 candidates x 5 requirements)
- Lexicographic ranking with tier assignment
- `LogicalCircleClosure` linking all phases into a coherent chain
- `D12Classification` with final canon statement

No hidden scoring.  All matching logic is in `_evaluate_single_match`,
dispatched on (candidate_id, requirement_id) pairs.  Every evaluation
is traceable to a specific function branch.
