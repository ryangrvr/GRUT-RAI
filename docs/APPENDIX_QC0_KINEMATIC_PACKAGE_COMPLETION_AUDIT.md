# Appendix Q-C0 — Kinematic Package Completion Audit

**Status:** Appendix P class `motivated_independent_postulation`
**Module:** `grut/qc0_kinematic_package_audit.py`
**Tests:** `tests/test_qc0_kinematic_package_audit.py`
**Depends on:** Q-B (`qb_quantum_state_space.py`), Q-B.5 (`qb5_complex_structure_audit.py`), Q0, Q-A

---

## 1. The Question

> Given Q-B (no native quantum state space, quantization blocked, CTP mapping compatible only) and Q-B.5 (complex structure J is MIP, J alone is not sufficient, doubled-field complexification is obstructed, Q-C authorized only if J is postulated), **what is the minimal additional kinematic package required for GRUT to support a well-defined quantum dynamics layer, and what is the doctrinal status of each required element?**

This is a *completion audit*, not a construction. Q-C0 does not build the quantum dynamics — it audits the pre-conditions for Q-C by identifying every kinematic ingredient that must exist before Q-C can be meaningfully attempted. The output is a minimum package specification with Appendix P classification on every element.

### What Q-C0 Does Not Claim

1. **NOT** claiming that identifying a kinematic package constitutes solving quantum microdynamics — that is Q-C.
2. **NOT** claiming that J alone provides full quantum kinematics (superposition, norm, dynamics, observables all require separate ingredients).
3. **NOT** claiming that any native bilinear form constitutes a quantum inner product without the J postulate.
4. **NOT** claiming that positivity is solved by open-system compatibility alone — the ghost obstruction from Q-B.5 eliminates all CTP-based norms.
5. **NOT** claiming that identifying the generator *class* (Lindbladian-like) is the same as deriving the generator *value* — that is Q-C.
6. **NOT** claiming that the postulated kinematic package receives `native_canon` classification — all Q-C results carry MIP minimum.
7. **NOT** claiming that density-matrix language compatibility implies full quantum closure.
8. **NOT** claiming that pre-Hilbert space topology resolves state ontology — completeness and Born rule are Q-D territory.

---

## 2. Inherited Results (Q-B and Q-B.5)

### From Q-B (`qb_quantum_state_space.py`):

| Verdict | Value | Class |
|---------|-------|-------|
| Primary state space | `density_matrix_or_functional_state_required` | BSR |
| Quantization route | `quantization_route_currently_blocked` | BSR |
| CTP mapping | `compatible_only` | CAH |

Key finding: there is no native quantum state space in GRUT. The constitutive ODE τ dΦ/dt + Φ = X produces no Hilbert space, no operator algebra, and no complex amplitude. The CTP doubled field structure is compatible with open-system quantum descriptions but does not provide one natively.

### From Q-B.5 (`qb5_complex_structure_audit.py`):

| Verdict | Value | Class |
|---------|-------|-------|
| Primary J status | `complex_structure_motivated_independent_postulation` | MIP |
| Sufficiency verdict | `J_necessary_but_not_sufficient` | — |
| Doubled-field verdict | `doubled_field_pair_complexification_obstructed` | BSR |
| Readiness verdict | `proceed_only_if_J_is_postulated` | — |

Key finding: J (a map J: ℝ_Φ → ℝ_Φ with J² = −1) qualifies for MIP postulation with two convergent motivations (CTP structural analogy + O(3) topological sector) and no new degrees of freedom. However, J alone is not sufficient — an inner product and a generator class are also required. The CTP ghost obstruction (Φ₋ growth rate sign +1) eliminates all CTP-based complexification routes.

**Minimum Q-B.5 package:** {J (MIP), inner product (MIP), generator class (MBU)}.

Q-C0 confirms and specifies this minimum package with full per-element analysis.

---

## 3. Hard Epistemic Rules

The following rules govern this audit (inherited from Q-A charter and Appendix P):

1. **Prefer absence over implication** — if an ingredient is not present, classify it absent, not "implicitly available".
2. **Prefer obstruction over vague openness** — ghost-contaminated norms are FOI, not "open questions".
3. **No silent promotion** — no ingredient may be reclassified to `native_canon` or `effective_reduction` without a rigorous derivation.
4. **Regime qualifiers mandatory** — if a claim holds only in a regime, state the regime.
5. **Obstructed items cite the audit** — ghost obstruction traces to Q-B.5 Track F.
6. **QA-R3 applies throughout** — any new kinematic structure requires MIP minimum.

---

## 4. Track A — Missing-Package Inventory (7 Ingredients)

Seven kinematic ingredients are required for a well-defined quantum dynamics layer. Their statuses range from `extension_level_only` (J, inherited from Q-B.5) to `absent` (inner product, norm, positivity, generator, observable) and `partially_present` (state-space topology).

| ID | Name | Status | Appendix P | Native Analog |
|----|------|--------|------------|---------------|
| KI1 | complex_structure_J | extension_level_only | MIP | CTP Keldysh split (algebraic J²=−1, dynamically obstructed) |
| KI2 | compatible_inner_product_g | absent | MIP | real L² pairing (structural base, not complex without J) |
| KI3 | norm_normalization_rule | absent | MIP | none |
| KI4 | positivity_condition | absent | MIP | none (CTP norm grows: ghost obstruction) |
| KI5 | state_space_topology | partially_present | BSR | real linear field space ℝ_Φ (NC) |
| KI6 | dynamics_generator | absent | MBU | constitutive ODE (classical analog of Markovian generator) |
| KI7 | observable_expectation_structure | absent | CAH | none (not needed for Q-C) |

**Summary counts:** 0 already present, 1 partially present (KI5), 5 absent (KI2–KI4, KI6–KI7), 0 obstructed, 1 extension-level (KI1).

### KI1 — Complex Structure J

J: ℝ_Φ → ℝ_Φ with J² = −1. Inherited from Q-B.5 as MIP. The CTP Keldysh split (Φ₊ = (Φ₁+Φ₂)/2, Φ₋ = Φ₁−Φ₂) suggests a natural candidate for J (Φ₊ ↔ Φ₋ exchange), which formally satisfies J² = −1. However, this candidate is dynamically obstructed: the Φ₋ ghost mode satisfies dΦ₋/dt = +Φ₋/τ (growth rate sign +1), so any norm built on the CTP pair grows under dynamics. Status: `extension_level_only` (MIP postulate required).

### KI2 — Compatible Inner Product g

A positive-definite real symmetric bilinear form g on field space satisfying the J-compatibility condition g(Jψ, Jφ) = g(ψ, φ). This upgrades to a Hermitian inner product via ⟨ψ|φ⟩ℂ = g(ψ,φ) + ig(Jψ,φ).

GRUT natively has the real L² pairing ∫φ(x)ψ(x)dx on field configurations. This is a native, positive-definite real symmetric bilinear form. However, it is not a complex inner product without J. The J-compatibility condition is a condition *on J* (require J to be a g-isometry), not an additional postulate about g. The natural minimal choice: use the native L² form and postulate J to be its isometry. Status: `absent` (MIP postulate required).

### KI3 — Norm

||ψ||² = g(ψ, ψ) follows from the inner product g. Once g is postulated positive definite, the norm is defined. This is not an independent postulate — it is derived from KI2. Status: `absent` (inherits MIP classification from g).

### KI4 — Positivity

The condition g(ψ,ψ) ≥ 0 with equality only at ψ = 0. This is the positive-definiteness condition on g — part of the inner product postulate. The Q-B.5 ghost obstruction (d|Ψ_CTP|²/dt = 2Φ₋²/τ > 0) eliminates all CTP-based norms as dynamically admissible probability norms. Ghost-safe positivity requires postulating g to be positive definite, independent of the CTP structure. Status: `absent` (MIP, part of g postulate).

### KI5 — State-Space Topology (partially present)

Topology is the one partially-present ingredient. GRUT natively provides a real linear vector space ℝ_Φ of field configurations (native_canon level). The quantum extension requires:

1. After J (MIP): complex vector space ℂ_Φ
2. After J + g (MIP): pre-Hilbert space (complex inner-product space without completeness)
3. After completion (Q-D territory): full Hilbert space ℋ

Minimum for Q-C: a pre-Hilbert space. Projective space (Born rule normalization), completeness (spectral theory), and density-operator cones are Q-D territory. Status: `partially_present` (BSR — topology is the deterministic consequence of J + g once postulated).

### KI6 — Dynamics Generator

A generator specifying how quantum states evolve. The generator *class* is constrained by Q-C0 (Lindbladian-like, see Track E). The generator *value* is Q-C's primary deliverable. Status: `absent` (MBU — motivated by open-system character and CTP structure; construction not yet done).

### KI7 — Observable / Expectation-Value Structure

An observable map O: state_space → ℝ and expectation-value rule ⟨O⟩ = Tr(ρO). Not needed for Q-C (which finds the dynamics law, not extracts predictions). Required in Q-D (measurement) and Q-E (benchmarks). Inseparable from the inner product when eventually needed. Status: `absent` (CAH — compatible with the package but not independently motivated for Q-C).

---

## 5. Track B — Inner Product Candidates (5 Candidates, 1 Viable)

Five routes to an inner product were tested. Only one (IP5, the MIP postulate) is viable.

| Candidate | Name | Viable | Class | Reason |
|-----------|------|--------|-------|--------|
| IP1 | real_L²_field_space_pairing | No | CAH | Real form only; not complex without J |
| IP2 | ctp_doubled_field_pairing | No | FOI | Ghost-contaminated; d\|Ψ\|²/dt = 2Φ₋²/τ > 0 |
| IP3 | o3_sector_induced_pairing | No | CAH | Wrong sector: Map(D,S²), not ℝ_Φ |
| IP4 | effective_open_system_hilbert_schmidt | No | CAH | Circular: requires prior Hilbert space |
| IP5 | postulated_j_compatible_positive_definite_g | **Yes** | **MIP** | Uses IP1 base + J-compatibility |

### IP1 — Real L² Pairing

g_R(ψ,φ) = ∫ψ(x)φ(x)dx is native to the real field space. It is positive definite as a real form (∫ψ²dx > 0 for ψ ≠ 0) and serves as the natural structural base for the MIP postulate. But it is not a complex inner product without J. Classified CAH: real pairing present natively; complex upgrade requires MIP.

### IP2 — CTP Doubled-Field Pairing (FOI)

Any inner product that uses Φ₋ as a basis element inherits the Q-B.5 ghost obstruction: d|Ψ_CTP|²/dt = 2Φ₋²/τ > 0. A norm that grows under dynamics is not dynamically admissible as a probability norm. The physical limit Φ₁ = Φ₂ = Φ collapses to IP1 (no complexification). Classified **FOI** (forbidden_or_inconsistent).

### IP3 — O(3) Sector Metric (CAH)

The round metric on the O(3) target space S² induces an L² pairing on Map(D, S²). This is defined on the O(3) sector, not on the canonical real scalar field space {Φ: D → ℝ}. Since Φ ∈ ℝ (not in S²), the O(3) metric cannot be transferred to the scalar sector without an additional linking postulate. Classified CAH.

### IP4 — Hilbert-Schmidt (CAH, Circular)

The Hilbert-Schmidt inner product Tr(ρ†σ) requires a prior Hilbert space ℋ over which to take the trace. GRUT does not supply ℋ natively. This is the same circularity rejected in Q-B.5 ER2: quantum in → quantum out. Classified CAH.

### IP5 — Postulated J-Compatible g (MIP, Viable)

Postulate a positive-definite real symmetric bilinear form g on field space satisfying:
- **J-compatibility:** g(Jψ, Jφ) = g(ψ, φ)
- **Positive definiteness:** g(ψ, ψ) > 0 for ψ ≠ 0

Natural minimal choice: use the native L² form (IP1) and postulate J to be its isometry. The Hermitian inner product is then:
$$\langle \psi | \phi \rangle_\mathbb{C} = g(\psi, \phi) + i\, g(J\psi, \phi)$$

This construction is the least-invasive extension of the native real structure. Qualifies for MIP with two convergent motivations (same as J in Q-B.5) and τ²=3/2 constraining compatible dynamics.

**Inner product verdict: `inner_product_motivated_independent_postulation`**

---

## 6. Track C — Norm and Positivity Audit

### Ghost Obstruction (Inherited from Q-B.5 Track F)

The Φ₋ ghost mode satisfies dΦ₋/dt = +Φ₋/τ (growth rate sign +1, Q-B.5 Track F). The CTP-based norm Φ₊² + Φ₋² satisfies:

$$\frac{d}{dt}|\Psi_{CTP}|^2 = \frac{d}{dt}(\Phi_+^2 + \Phi_-^2) = +\frac{2\Phi_-^2}{\tau} > 0$$

Any inner product built on the CTP pair is dynamically growing — it cannot serve as a conservation law or probability norm. This eliminates IP2 (FOI) and establishes the ghost obstruction as a hard constraint on the positivity audit.

### Ghost-Safe Norm via IP5

The MIP inner product g (IP5) is defined on the real field space independently of the CTP ghost structure. Once g is postulated positive definite:

$$\|\psi\|^2 = g(\psi, \psi) > 0 \quad \forall\ \psi \neq 0$$

This is a ghost-safe norm. Whether the dynamics preserves it is Q-C's question (the generator must be chosen to satisfy this constraint).

### Open-System Positivity

In the Lindbladian picture, ∂ₜρ = −i[H,ρ] + Σ_k(L_k ρ L_k† − ½{L_k†L_k, ρ}) preserves ρ ≥ 0 and Tr(ρ) = 1. This is not a derivation of positivity — it is a consistency check: if g is postulated positive definite and a Lindbladian generator is identified (Q-C), then open-system positivity is preserved by construction.

| Check | Result |
|-------|--------|
| Ghost obstruction inherited | True |
| Φ₋ growth rate sign | +1 |
| CTP-based norm ghost contaminated | True |
| CTP-based norm valid | **False** |
| J-compatible norm available with postulate | True |
| Positivity native | **False** |
| Positivity effectively recoverable | **False** |
| Positivity requires postulate | **True** |
| Open-system Lindblad compatible | True |

**Positivity verdict: `positivity_requires_postulate`**

---

## 7. Track D — State-Space Topology

The native GRUT topology is a real linear vector space ℝ_Φ of scalar field configurations. The kinematic package upgrades this in two steps:

| Step | Topology | Requires |
|------|----------|----------|
| Native | Real linear space ℝ_Φ | NC (no postulate) |
| After J | Complex linear space ℂ_Φ | MIP (J postulate) |
| After J + g | Pre-Hilbert space (complex inner-product space) | MIP (J + g postulate) |
| Q-D | Full Hilbert space ℋ | Completeness (Q-D) |

**Minimum for Q-C: complex linear pre-Hilbert space** (complex inner-product space without completeness requirement). This is sufficient for defining quantum states, their overlaps, and the action of a generator.

Items deferred beyond Q-C:
- **Projective space ℂP(ℋ):** Needed for Born rule normalization (Q-D territory).
- **Density-operator cone:** Naturally derived from pre-Hilbert space; available once g is established.
- **Topological completeness / Hilbert space:** Needed for spectral theory (Q-D territory).
- **Functional space over histories:** Compatible but not a Q-C minimum.

The topology result is classified **BSR** (bounded_structural_result): once J and g are postulated, the pre-Hilbert space topology is a deterministic structural consequence.

---

## 8. Track E — Generator Class Audit

Given the kinematic package {J (MIP), g (MIP)}, multiple generator classes are kinematically admissible. The question is which class is also consistent with GRUT's architectural character (first-order, dissipative, open-system).

| Generator Class | Kinematically Admissible | GRUT Consistent |
|----------------|------------------------|-----------------|
| Hamiltonian (pure unitary) | Yes | **No** — GRUT is dissipative |
| Lindbladian (Markovian open system) | Yes | **Yes** |
| Memory-kernel (non-Markovian) | Yes | **Yes** |
| Influence-functional | Yes | **Yes** |
| Non-Hermitian effective | Yes | Yes (effective) |

### Why Hamiltonian is GRUT-Inconsistent

The constitutive ODE τ dΦ/dt + Φ = X is intrinsically dissipative: the τ dΦ/dt term represents relaxation to equilibrium, not reversible oscillation. There is no conserved energy in GRUT's native structure (the equilibrium is set by dissipation, not a potential minimum). A pure Hamiltonian generator iℏ ∂ₜΨ = HΨ would be structurally inconsistent with GRUT's dissipative character.

### Why Lindbladian is the Primary Class

The GRUT constitutive ODE is a first-order ODE in time — the minimal structure for a Markovian master equation. The Lindbladian:

$$\partial_t \rho = -i[H, \rho] + \sum_k \left(L_k \rho L_k^\dagger - \tfrac{1}{2}\{L_k^\dagger L_k, \rho\}\right)$$

is the minimal Markovian open-system generator. It:
1. Is consistent with GRUT's first-order temporal structure.
2. Preserves density matrix positivity (ρ ≥ 0) and trace (Tr(ρ) = 1).
3. Provides the GRUT constitutive ODE as a natural classical analog (τ∂ₜρ + ρ = X[ρ] in Markovian form).

The memory-kernel generator ∂ₜρ(t) = ∫₀ᵗ K(t−s)ρ(s)ds is also admissible and more naturally connected to GRUT's retarded kernel structure (Q0 item C4). This may prove to be the more natural class for Q-C — it is listed as an additional admissible class.

**Generator class verdict: `lindbladian_like_generator_kinematically_admissible`**

---

## 9. Track F — Observable / Expectation-Value Structure

**Observable structure is not a Q-C prerequisite.** Q-C's deliverable is the dynamics law (the generator), not prediction extraction from states. Observables become necessary in:
- **Q-D** (measurement and decoherence): observable = measurement operator
- **Q-E** (benchmark toy problems): observable = measurable quantity

The expectation-value formula ⟨O⟩ = Tr(ρO) (in density-matrix language) is inseparable from the inner product g when eventually needed. Deferring observable structure to Q-D avoids premature Born-rule commitment.

**Observable verdict: `not_needed_yet_for_QC`**

---

## 10. Track G — Minimum Kinematic Package

The minimum package for Q-C entry has exactly three elements:

| Element | Appendix P Class | Description |
|---------|-----------------|-------------|
| J: ℝ_Φ → ℝ_Φ with J² = −1 | **MIP** | Complex structure enabling superposition |
| Compatible inner product g with g(Jψ,Jφ)=g(ψ,φ), positive definite | **MIP** | Hermitian norm, ghost-safe positivity |
| Generator class: Lindbladian-like (Markovian open-system) | **MBU** | Identifies Q-C's search space |

This package is *minimal* in the sense that removing any element makes Q-C undefined:
- Without J: no complex linear structure, no complex superposition.
- Without g: no norm, no inner product, no positivity.
- Without generator class: Q-C has no constrained search space.

### What Is Not In the Minimum Package

The following are intentionally deferred:

- Born rule: Q-D territory
- Measurement postulate: Q-D territory
- Topological completeness (Hilbert space): Q-D territory
- Observable structure: Q-D / Q-E territory
- Entanglement structure: not addressed in Q-C0
- Interference formalism: Q-F territory

**Package verdict: `minimum_kinematic_package_identified`**

---

## 11. Track H — Appendix P Classification

Full per-element Appendix P classification:

| Element | Class | Allowed Claim | Forbidden Claim |
|---------|-------|---------------|-----------------|
| J (KI1) | MIP | J may be postulated; enables complex superposition; constrained by τ²=3/2 | J is natively derived; postulated J receives NC classification |
| Inner product g (KI2) | MIP | Positive-definite J-compatible g may be postulated at MIP level | Native L² pairing constitutes a complex inner product |
| Norm from g (KI3) | MIP | ‖ψ‖² = g(ψ,ψ) > 0 is a ghost-safe norm derived from postulated g | Any norm implies positivity is solved; CTP norm is admissible |
| Positivity from g (KI4) | MIP | Positivity = positive-definiteness condition on postulated g | Positivity is natively available; open-system compat. implies Lindblad derived |
| Pre-Hilbert topology (KI5) | BSR | Pre-Hilbert topology is the deterministic consequence of J + g | Topology alone solves state ontology; pre-Hilbert implies Born rule |
| Lindbladian generator class (KI6) | MBU | Generator class is kinematically admissible; class identified; value is Q-C | Identifying class implies law is derived; Lindblad structure derived from GRUT |

**Overall package Appendix P class: `motivated_independent_postulation`** (dominant class for the two primary elements J and g).

No element in the quantum kinematic package receives `native_canon` classification.

---

## 12. Track I — Readiness for Q-C

| Condition | Status |
|-----------|--------|
| Native GRUT sufficient for Q-C | **False** |
| Package postulation required | **True** |
| J postulated (MIP) | Required condition |
| Inner product g postulated (MIP) | Required condition |
| Generator class identified (MBU) | Required condition |
| Q-C can proceed with postulate | **True** |
| Q-C Appendix P floor | `motivated_independent_postulation` |

### Conditions for Q-C

Q-C may begin once:
1. J is postulated at MIP level (J² = −1, commutes with GRUT evolution operator)
2. g is postulated at MIP level (J-compatible, positive definite)
3. Lindbladian-like generator class is accepted as Q-C's search space
4. All Q-C results carry MIP minimum Appendix P floor (per QA-R3)
5. Q-C0 nonclaims are registered and honored throughout Q-C
6. Ghost obstruction is explicitly cited; CTP-based norms are excluded from all Q-C constructions
7. Q-C deliverable is the generator *value* (not the class, which is already identified)

**Readiness verdict: `ready_only_if_package_is_postulated`**

---

## 13. Allowed and Forbidden Claims

### Allowed

- The minimum kinematic package for Q-C is identified: {J (MIP), g (MIP), generator class (MBU)}.
- The inner product verdict is `inner_product_motivated_independent_postulation`.
- Positivity requires postulate: ghost-contaminated CTP norms are dynamically inadmissible (FOI).
- The Lindbladian generator class is kinematically admissible given GRUT's Markovian structure.
- Pre-Hilbert space (complex inner-product space without completeness) is the minimum topology.
- The native real L² pairing serves as the structural base for the MIP inner product postulate.
- Observable structure is not a Q-C prerequisite; it is deferred to Q-D.
- Q-C readiness verdict: `ready_only_if_package_is_postulated`.
- All Q-C results carry MIP minimum Appendix P classification.
- Memory-kernel and influence-functional generators are also kinematically admissible.

### Forbidden

- J alone solves full quantum kinematics.
- The native real L² pairing constitutes a complex inner product.
- Any bilinear form establishes a physical quantum inner product.
- The CTP norm |Ψ|² = Φ₊² + Φ₋² is dynamically admissible (it is ghost-contaminated, FOI).
- Open-system compatibility implies Lindblad structure is derived from GRUT.
- Generator class identification implies the microdynamic law is derived.
- Pre-Hilbert space topology solves state ontology.
- The postulated kinematic package receives `native_canon` classification.
- Density-matrix compatibility implies full quantum closure.
- Positivity is natively available or effectively recoverable without postulate.

---

## 14. Nonclaims

1. **NOT** claiming J alone solves full quantum kinematics — J enables complex superposition only; norm, dynamics, and observables require separate ingredients.
2. **NOT** claiming any bilinear form establishes a physical inner product — the real L² pairing is native but J-compatibility and positivity are postulated.
3. **NOT** claiming any norm implies positivity is solved — the ghost obstruction rules out CTP-based norms; positivity requires an explicit postulate.
4. **NOT** claiming open-system compatibility implies Lindblad structure is derived — the Lindblad class is kinematically admissible, not derived from GRUT architecture.
5. **NOT** claiming generator class compatibility implies actual microdynamics is derived — identifying the generator class is not the same as finding the law; that is Q-C.
6. **NOT** claiming state-space topology guess solves state ontology — pre-Hilbert topology is the minimum; completeness and Born rule are Q-D territory.
7. **NOT** claiming the postulated package receives `native_canon` classification — all Q-C results carry MIP minimum per Q-A charter rule QA-R3.
8. **NOT** claiming density-matrix compatibility implies full quantum closure — density-matrix language is compatible but quantum closure is not established.

---

## 15. Five Hard-Gated Verdicts

| Verdict | Value | Class |
|---------|-------|-------|
| `package_verdict` | `minimum_kinematic_package_identified` | BSR |
| `inner_product_verdict` | `inner_product_motivated_independent_postulation` | MIP |
| `positivity_verdict` | `positivity_requires_postulate` | BSR |
| `generator_class_verdict` | `lindbladian_like_generator_kinematically_admissible` | MBU |
| `readiness_verdict` | `ready_only_if_package_is_postulated` | — |

**Overall Q-C0 Appendix P class: `motivated_independent_postulation`**

---

## 16. Readiness for Q-C

Q-C may proceed with the following explicit understanding:

1. The kinematic package {J (MIP), g (MIP), generator class (MBU)} must be explicitly postulated before Q-C begins.
2. No Q-C result may claim `native_canon`, `effective_reduction`, or `working_canon_hypothesis` — all results carry MIP minimum.
3. The ghost obstruction (Φ₋ growth rate sign +1) must be explicitly cited in any Q-C construction that considers norms or inner products.
4. The generator *class* (Lindbladian-like) is identified; Q-C's deliverable is the generator *value* — the actual law governing quantum state evolution.
5. Bounded negative results from Q-C are acceptable and should be preserved as BSR findings.
6. Observable structure, Born rule, completeness, and measurement postulate remain deferred to Q-D.

**Q-C is authorized contingent on explicit postulation of the minimum kinematic package.**

---

*See also:*
- *Appendix Q-B: `docs/APPENDIX_QB_QUANTUM_STATE_SPACE.md`*
- *Appendix Q-B.5: `docs/APPENDIX_QB5_COMPLEX_STRUCTURE_AND_KINEMATIC_UPGRADE.md`*
- *Appendix P taxonomy: `grut/appendix_p_taxonomy_audit.py`*
- *Q-A charter: `docs/APPENDIX_QA_QUANTUM_CONCEPTUAL_CHARTER.md`*
