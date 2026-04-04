# Appendix P — GRUT Extension Taxonomy and Canon Boundary Audit

**Module:** `grut/appendix_p_taxonomy_audit.py`
**Tests:** `tests/test_appendix_p_taxonomy_audit.py` (232 tests, all passing)
**Primary verdict:** `taxonomy_complete__sufficient_for_quantum_readiness`
**Ambiguous items:** none
**Status classes:** 8 (minimal and sufficient)
**Classified items:** 12

---

## 1. Why Appendix P Is Needed

Every prior appendix (A–O) produces a result and assigns it a status — native,
motivated, obstructed, effective, and so on. But the status labels have been
used informally. Before Appendix Q (Quantum) begins, the classification grammar
must be made explicit and binding, for three reasons:

**1. Category confusion is the primary failure mode for quantum work.**
The quantum sector will need to extend, correct, or supplement every classical
result. Without precise class definitions, the following errors are easy to
commit:
- Treating a *motivated postulate* (O(3)) as *native canon* when quantizing
- Treating a *regime-specific* result (τ_eff) as *covariant*
- Treating a *bounded obstruction* (fermionic emergence) as a *principle-level
  impossibility*
- Treating *compatibility* with a prior result as *derivation* from it

**2. The extension chain (M → N → O) is load-bearing.**
The chain `particle_candidate_not_yet_established → motivated_but_unbuilt (L₄)
→ motivated_independent_postulation (O(3))` is the current doctrinal frontier.
Its three nodes have three different status classes that must not be conflated.

**3. Appendix Q must know what it inherits.**
When the quantum sector begins, it inherits a precise classification of what is
native, what is an effective reduction, what is a working hypothesis, and what
is an explicitly introduced postulate. Appendix P formalizes that inheritance.

---

## 2. The Final Doctrinal Taxonomy

Eight status classes, minimal and sufficient:

| Class | Short label | Postulate required? | New DOF? | Constructive? |
|---|---|---|---|---|
| `native_canon` | NC | No | No | Yes |
| `effective_reduction` | ER | No | No | Yes |
| `bounded_structural_result` | BSR | No | No | Yes |
| `working_canon_hypothesis` | WCH | No | No | Yes |
| `motivated_but_unbuilt` | MBU | No | No | Yes |
| `motivated_independent_postulation` | MIP | **Yes** | **Yes** | Yes |
| `compatible_but_ad_hoc` | CAH | **Yes** | **Yes** | Yes |
| `forbidden_or_inconsistent` | FOI | — | — | **No** |

---

## 3. Exact Definitions

### 3.1 `native_canon`

Derived from GRUT's first principles. No regime qualifier needed for validity.
No free parameters beyond the canonical constants (τ², α_vac, β_Q, M_ext,
R_eq, ω₀). Valid across all GRUT-applicable physical domains.

*Admissibility:* follows by derivation; no regime qualifier; no new parameters;
quarantine respected.

*Exclusion:* requires a regime qualifier; introduces new field content; asserted
not derived; works only in a specific physical limit.

### 3.2 `effective_reduction`

Valid in a specified physical regime. In that regime it reduces to or
approximates native canon. Outside the stated regime validity is not guaranteed.
Claims must include the regime qualifier.

*Admissibility:* valid within explicitly stated regime; regime qualifier precisely
defined; reduces to/approximates native canon in the regime limit.

*Exclusion:* claims validity outside the regime; does not reduce to native canon
in any limit.

### 3.3 `bounded_structural_result`

A proved mathematical or architectural result within explicitly stated
assumptions. The result is demonstrated — not asserted — within the stated
conditions. Makes no claims beyond those assumptions. Includes both positive
theorems and negative results (obstruction, partial closure, proved
impossibility within stated architecture).

*Admissibility:* proved within stated assumptions; assumptions explicit;
derivation self-contained; scope clearly limited.

*Exclusion:* claims beyond stated assumptions without proof; asserted not proved.

### 3.4 `working_canon_hypothesis`

Asserted as canonical for load-bearing purposes. Part of the working
architecture; predictions depend on it. Not fully derived from first principles.
Adopted provisionally, subject to deeper derivation.

*Admissibility:* currently load-bearing; predictions depend on it; asserted not
derived; no new field content.

*Exclusion:* derived from first principles → upgrade to `native_canon`; not
load-bearing → `compatible_but_ad_hoc` at most.

### 3.5 `motivated_but_unbuilt`

The derivation path is structurally identified and coherent within existing
field content. No new DOFs are required in principle. The path has not been
traversed. Motivated by GRUT architecture; is the natural result of a known
construction; that construction is not yet complete.

*Admissibility:* path explicitly identified and named; no new DOFs in principle;
motivation from GRUT architecture; path is coherent not merely compatible.

*Exclusion:* path requires new DOFs → `motivated_independent_postulation`;
no coherent path → `compatible_but_ad_hoc` at most.

### 3.6 `motivated_independent_postulation`

Requires new field content (DOF increase) that cannot be derived from existing
field content — a BG1-class gap that is mathematically irresolvable by
derivation. The postulate is uniquely selected and strongly motivated by ≥2
convergent independent reasons. ≥1 parameter is constrained by canonical GRUT
quantities.

*Admissibility (all three required):*
1. New DOF content with BG1-class gap
2. ≥2 convergent independent motivations
3. ≥1 parameter constrained by GRUT canon

*Exclusion:* <2 motivations → `compatible_but_ad_hoc`; 0 parameters constrained
→ `compatible_but_ad_hoc`; contradicts established results → `forbidden_or_inconsistent`.

### 3.7 `compatible_but_ad_hoc`

Consistent with GRUT architecture. Not motivated by it. Not required by it.
Introduces unconstrained free parameters. Replaceable without architectural
loss.

*Admissibility:* consistent with prior doctrine; no established result
contradicted.

*Exclusion:* contradicts established results → `forbidden_or_inconsistent`;
≥2 convergent motivations + uniqueness + ≥1 parameter constrained →
`motivated_independent_postulation`; clear derivation path without new DOFs →
`motivated_but_unbuilt`.

### 3.8 `forbidden_or_inconsistent`

Contradicts an established GRUT result (`native_canon` or
`bounded_structural_result`), violates the pre-matter quarantine perimeter, or
requires a mathematical impossibility proved within the stated architecture.
Claims in this class must not be made.

*Admissibility:* contradiction of established result; quarantine violation;
proved impossibility.

*Exclusion:* inconsistency is merely a gap → `motivated_but_unbuilt` or weaker;
blocked only in current architecture not in principle → `bounded_structural_result`
for the obstruction.

---

## 4. Exact Boundary Conditions Between Classes

```
native_canon ──B1── effective_reduction ──B2── bounded_structural_result
                                                     │
                                                    B3
                                                     │
                                         working_canon_hypothesis
                                                     │
                                                    B4
                                                     │
                                         motivated_but_unbuilt
                                                     │
                                                    B5  ← key: new DOF?
                                                     │
                                     motivated_independent_postulation
                                                     │
                                                    B6  ← key: ≥2 motivations?
                                                     │
                                         compatible_but_ad_hoc
                                                     │
                                                    B7  ← key: contradiction?
                                                     │
                                         forbidden_or_inconsistent
```

### B1: `native_canon` vs `effective_reduction`

**Test:** Does validity require a regime qualifier?

- YES → `effective_reduction`
- NO → `native_canon`

*Example:* The constitutive ODE as a defining equation → `native_canon`.
τ_eff (requires quasi-static regime) → `effective_reduction`.

### B2: `effective_reduction` vs `bounded_structural_result`

**Test:** Regime-specific approximation, or proved theorem within stated conditions?

- Approximation → `effective_reduction`
- Proved statement (often negative) → `bounded_structural_result`

*Example:* Galley CTP as dissipation framework → `effective_reduction`.
Phi bifurcation theorem → `bounded_structural_result`.

### B3: `bounded_structural_result` vs `working_canon_hypothesis`

**Test:** Derived (proved) or asserted for working purposes?

- Proved within stated assumptions → `bounded_structural_result`
- Asserted as load-bearing → `working_canon_hypothesis`

*Example:* Derrick's theorem (E₂+3E_V>0 proved) → `bounded_structural_result`.
β_Q = 2 (asserted, not derived) → `working_canon_hypothesis`.

### B4: `working_canon_hypothesis` vs `motivated_but_unbuilt`

**Test:** Currently load-bearing in working canon, or a prospective extension?

- In working canon, predictions depend on it → `working_canon_hypothesis`
- Prospective, path identified, not yet adopted → `motivated_but_unbuilt`

*Example:* β_Q = 2 (predictions depend on it now) → `working_canon_hypothesis`.
L₄ Skyrme term (path identified via Route 3, not in working canon) → `motivated_but_unbuilt`.

### B5: `motivated_but_unbuilt` vs `motivated_independent_postulation`

**Test:** Does the construction require new field content (a BG1-class gap)?

- No new DOFs required → `motivated_but_unbuilt`
- New DOFs required; BG1-class gap; irresolvable by derivation → `motivated_independent_postulation`

*Example:* L₄ (given O(3) already canonical: next term in same field space) →
`motivated_but_unbuilt`. O(3) triplet (1→3 scalars: irresolvable gap) →
`motivated_independent_postulation`.

**This is the sharpest boundary in the taxonomy.** It separates "can in principle
be derived" from "can never be derived — must be postulated."

### B6: `motivated_independent_postulation` vs `compatible_but_ad_hoc`

**Test:** Does the proposed extension have ≥2 convergent independent motivations
AND uniqueness AND ≥1 parameter constrained?

- All three → `motivated_independent_postulation`
- Fails at least one → `compatible_but_ad_hoc`

*Example:* O(3) (CM1 topological uniqueness + CM2 Component B + η²=τ²/(12π)) →
`motivated_independent_postulation`. Adding L₄ without O(3) nativity established
(e free, not uniquely selected) → `compatible_but_ad_hoc`.

### B7: `compatible_but_ad_hoc` vs `forbidden_or_inconsistent`

**Test:** Does the addition contradict an established result or violate
the quarantine perimeter?

- Consistent with all established results → `compatible_but_ad_hoc`
- Contradicts established result OR quarantine violation → `forbidden_or_inconsistent`

*Example:* Adding any unconstrained scalar sector consistent with doctrine →
`compatible_but_ad_hoc`. Claiming V(Φ)=λ|Φ|⁴ stabilizes the hedgehog (contradicts
Derrick scaling) → `forbidden_or_inconsistent`.

---

## 5. Classification Table

| Item | Primary Class | Key Justification |
|---|---|---|
| Scalar field + constitutive architecture | `native_canon` | Founding elements; no regime qualifier; derived from first principles |
| Pre-matter quarantine perimeter | `native_canon` | Definitional boundary of GRUT; founding commitment |
| τ_eff domain declaration | `effective_reduction` | Valid only in quasi-static regime; requires regime qualifier |
| Galley CTP Route B | `effective_reduction` | Dissipation framework; post-projection reduces to Route C; projection assumed not derived |
| Phi sector bifurcation | `bounded_structural_result` | Proved architectural result within GRUT framework |
| Fermionic emergence obstruction | `bounded_structural_result` | Proved obstruction in current architecture (π₂(ℝ)=0; Hopf absent); **negative result** |
| g₋ source closure | `bounded_structural_result` | Source path proved closed; homogeneous path open; within Galley formalism |
| Component B deficit requirement | `bounded_structural_result` | 1/r² support necessity proved within stated architecture |
| β_Q = 2 canonical hypothesis | `working_canon_hypothesis` | Load-bearing; predictions depend on it; not derived from first principles |
| Localized bosonic object program | `motivated_but_unbuilt` | Path identified (O(3)+L₄+Derrick); not traversed |
| Skyrme term L₄ | `motivated_but_unbuilt` | Route 3 identified (O(3) derivative expansion); conditioned on O(3) nativity |
| O(3) sector nativity | `motivated_independent_postulation` | BG1 irresolvable; uniqueness (CM1); Component B (CM2); η²=τ²/(12π) |

**Class distribution:**
- native_canon: 2
- effective_reduction: 2
- bounded_structural_result: 4
- working_canon_hypothesis: 1
- motivated_but_unbuilt: 2
- motivated_independent_postulation: 1
- compatible_but_ad_hoc: 0 primary (used in nonclaims)
- forbidden_or_inconsistent: 0 primary (used in firewall)

---

## 6. Allowed and Forbidden Claims by Class

### `native_canon`
**Allowed:**
- This result is architecturally required by GRUT
- Predictions from this result are native GRUT predictions
- This holds in all GRUT-applicable domains

**Forbidden:**
- Extending to matter sector without quarantine declaration
- Claiming quantum validity without explicit quantum derivation

### `effective_reduction`
**Allowed:**
- In the [stated] regime, this result holds
- This is a regime-specific description of canonical dynamics

**Forbidden:**
- Treating the effective result as exact outside its regime
- Regime success implies native canon validity

### `bounded_structural_result`
**Allowed:**
- Under assumptions [X], result [Y] is proved
- Within the stated architecture, [obstruction/closure] is established
- The negative result [N] is proved for the stated class of architectures

**Forbidden:**
- The bounded result implies a universal theorem
- An obstruction within stated architecture implies impossibility in principle
- The result extends beyond stated assumptions without proof

### `working_canon_hypothesis`
**Allowed:**
- Under the canonical hypothesis [X], predictions are ...
- Sensitivity of results to this hypothesis is documented
- A derivation would upgrade this to native_canon

**Forbidden:**
- Claiming the hypothesis is derived from first principles
- Treating sensitivity audit results as derived predictions

### `motivated_but_unbuilt`
**Allowed:**
- A derivation path exists: [Route description]
- Once [prerequisite] is met, this follows as ...
- Adding this after [prerequisite] would not be ad hoc

**Forbidden:**
- Treating the identified path as a completed derivation
- Claiming the result is established because the path is identified
- Using in predictions before the derivation is built

### `motivated_independent_postulation`
**Allowed:**
- This postulate is uniquely motivated by [topology/uniqueness argument]
- One parameter is constrained: [explicit constraint]
- This is the minimal necessary extension for [stated purpose]
- This is the best-motivated available choice

**Forbidden:**
- Treating the motivated postulate as derived from canon
- Claiming topological uniqueness implies derivability
- Using partial parameter constraint to claim native status

### `compatible_but_ad_hoc`
**Allowed:**
- This addition is consistent with GRUT architecture
- No prior audit is violated
- This is one of several compatible choices

**Forbidden:**
- Claiming the addition is motivated by GRUT architecture
- Treating consistency as motivation or derivation

### `forbidden_or_inconsistent`
**Allowed:**
- This claim is forbidden because it contradicts [established result]
- This claim requires a proved impossibility

**Forbidden:**
- Any positive assertion for an item in this class
- Treating the forbidden claim as "not yet disproved"

---

## 7. Dependency Logic

The classification table encodes a dependency graph:

```
scalar_constitutive_core (NC)
    ├── pre_matter_quarantine_perimeter (NC)
    ├── tau_eff_domain_declaration (ER)
    │       └── phi_sector_bifurcation (BSR)
    ├── beta_q_canonical_hypothesis (WCH)
    ├── fermionic_emergence_obstruction (BSR, negative)
    ├── galley_ctp_route_b (ER)
    │       ├── g_minus_source_closure (BSR)
    │       └── component_b_deficit_requirement (BSR)
    │               └── o3_sector_nativity (MIP)
    │                       ├── skyrme_term_nativity (MBU)
    │                       │       └── localized_bosonic_object_program (MBU)
    │                       └── localized_bosonic_object_program (MBU)
    └── fermionic_emergence_obstruction (BSR)
            └── o3_sector_nativity (MIP)
```

**Key dependency rule:** No item can be classified at a level more
established than its dependencies permit.
- O(3) is `motivated_independent_postulation` — it cannot be `native_canon`
  regardless of how useful it is.
- L₄ is `motivated_but_unbuilt` — its classification is conditional on O(3)
  being adopted; before that, adding L₄ is `compatible_but_ad_hoc`.
- Component B supply is open — the requirement is `bounded_structural_result`
  but the supply (O(3) hedgehog) is `motivated_independent_postulation`.

**The crucial asymmetry in the chain:**
- O(3) will always be a postulate (BG1 is permanent).
- L₄ can become motivated (not ad hoc) once O(3) is adopted.
- The bosonic particle candidate can become established once L₄ is built.

---

## 8. How Appendix P Prepares Appendix Q

### What Appendix Q inherits

| Inherited item | Status | Quantum significance |
|---|---|---|
| Scalar Φ, constitutive ODE | `native_canon` | Canonical starting point for quantization |
| τ_eff domain | `effective_reduction` | Valid only in quasi-static regime; quantum corrections may extend or break this |
| Phi bifurcation | `bounded_structural_result` | Proved in classical architecture; must be rechecked in quantum context |
| Fermionic obstruction | `bounded_structural_result` (negative) | **Architecture must address this explicitly** — fermions require new structure |
| β_Q = 2 | `working_canon_hypothesis` | **Not proved** — quantum derivation could resolve or change this |
| O(3) nativity | `motivated_independent_postulation` | Postulate declared; quantum work begins with this postulate explicitly labeled |
| L₄ nativity | `motivated_but_unbuilt` | Path exists; quantum sector may complete or modify it |
| Quarantine perimeter | `native_canon` | All quantum work respects this boundary |

### What Appendix P prevents Appendix Q from doing

- Silently promoting O(3) from `motivated_independent_postulation` to `native_canon`
  in the quantum context without explicit justification
- Treating the fermionic obstruction as a proof that fermions are impossible in all
  extensions, rather than as a bounded result for the current architecture
- Treating τ_eff quantum corrections as fully covariant without regime derivation
- Treating β_Q = 2 as a proved quantum prediction rather than a working hypothesis
  that could shift under quantum derivation

### Missing classes

None. The 8 status classes are sufficient for Appendix Q. New quantum results will
be classified using `native_canon`, `effective_reduction`, `bounded_structural_result`,
or `working_canon_hypothesis` as appropriate. No new class type is needed.

**Verdict on quantum readiness:** Appendix P is sufficient as the pre-quantum
finisher. No doctrinal gaps were found.

---

## 9. The Eight Forbidden Inference Patterns

These are the primary failure modes in applying the taxonomy. Each corresponds to
a boundary violation in B1–B7.

| Pattern | What it forbids | Boundary violated |
|---|---|---|
| `compatibility_as_derivation` | L₄ compatible with GRUT ≠ L₄ derived from GRUT | B5/B6 |
| `usefulness_as_nativity` | O(3) useful for Component B ≠ O(3) native to GRUT | B5 |
| `uniqueness_as_derivability` | O(3) is the unique choice ≠ O(3) is derivable from Φ | B5 |
| `observed_coincidence_as_closure` | η²=τ²/(12π) is a numerical fact; mechanism unknown | B6 |
| `effective_regime_success_as_covariant_canon` | Quasi-static success ≠ covariant canonical result | B1 |
| `motivated_postulate_as_native` | O(3) is motivated postulate ≠ O(3) is native | B5 |
| `unbuilt_route_as_solved` | Route 3 is identified ≠ Route 3 is traversed | B3/B4 |
| `obstruction_as_impossibility_in_principle` | Fermionic obstruction in current arch ≠ fermions impossible for all extensions | B3 |

---

## 10. Nonclaims

1. **NOT** claiming any extension is derived from canonical GRUT.
2. **NOT** promoting `motivated_independent_postulation` to `native_canon`.
3. **NOT** treating motivated postulates as architecturally required.
4. **NOT** claiming the taxonomy is complete for all possible future extensions —
   it covers all audited items; new items will be classified as they arise.
5. **NOT** closing any open audit — Appendix P classifies status, not results.
6. **NOT** treating `working_canon_hypothesis` as proved.
7. **NOT** treating `bounded_structural_result` as universally valid beyond its
   stated assumptions.
8. **NOT** claiming the fermionic obstruction closes the fermionic question in
   principle for all extensions.

---

## 11. Final Verdict

**The taxonomy is complete and sufficient to serve as the pre-quantum finisher.**

The 8-class taxonomy is:
- **Minimal:** no class is redundant; no two classes are semantically equivalent
- **Sufficient:** all 12 audited GRUT items are unambiguously classified
- **Quantum-ready:** all items needed by Appendix Q are classified with their
  exact status, allowed claims, forbidden claims, and dependency relationships

The full audit chain M → N → O → P is now doctrine-locked:

| Appendix | Module | Primary verdict |
|---|---|---|
| M | `localized_bosonic_object_audit.py` | `particle_candidate_not_yet_established` |
| N | `skyrme_term_nativity_audit.py` | `no_native_skyrme_support_found` / `motivated_but_unbuilt` |
| O | `o3_nativity_audit.py` | `o3_auxiliary_but_minimally_motivated` / `motivated_independent_postulation` |
| P | `appendix_p_taxonomy_audit.py` | `taxonomy_complete__sufficient_for_quantum_readiness` |

The grammar of GRUT extensions is now formally specified. Appendix Q may proceed.
