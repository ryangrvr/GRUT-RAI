# Appendix Q0 — GRUT Quantum Entry Inventory

**Module:** `grut/q0_quantum_entry_inventory.py`
**Tests:** `tests/test_q0_quantum_entry_inventory.py` (155 tests, all passing)
**Depends on:** Appendix P (taxonomy), Appendices L/M/N/O (bosonic/fermionic audits)
**Q0 verdict:** `inventory_complete__quantum_gap_fully_documented`

---

## 1. The Question

Q0 asks one precise question before any quantum derivation is attempted:

> **What quantum-relevant ingredients does GRUT's canonical architecture already
> contain, what is structurally absent, and what is proved to be obstructed?**

This question is answered by a deterministic, code-backed inventory of 25 items
across five categories, each carrying an Appendix P status class, a reference to
the supporting audit, and explicit allowed and forbidden claims.

Q0 does **not** attempt to derive quantum mechanics. It does **not** claim GRUT
is a quantum theory. It establishes, with doctrinal precision, the starting
conditions for the quantum program that follows.

---

## 2. Hard Epistemic Rules

Six rules govern the entire inventory. They are tested explicitly and enforced
in the module code.

| Rule | Meaning |
|------|---------|
| **prefer_absence_over_implication** | If an ingredient is not demonstrably present, it is absent. A suggestive structure is not the structure itself. |
| **prefer_obstruction_over_vague_openness** | If a proved audit result forecloses an ingredient, it is obstructed — not "open" or "under investigation." |
| **do_not_treat_suggestive_as_present** | Phase-like behavior ≠ phase. Scale selection ≠ quantization. Winding number ≠ complex amplitude. Relaxation ≠ decoherence. |
| **no_silent_promotion_to_native_canon** | No ingredient may be reclassified to `native_canon` without a derivation from GRUT first principles. |
| **regime_qualifiers_mandatory_for_effective_reduction** | Any `effective_reduction` claim must state the regime in which the reduction holds. |
| **obstructed_items_cite_appendix_audit** | Every obstructed item must cite the specific module or appendix that establishes the obstruction. |

These rules are not aspirational. They are logical consequences of the Appendix P
taxonomy and are the minimal conditions for honest audit work.

---

## 3. Category A — State-Like (5 items)

**Definition:** Configuration variables, field variables, memory variables, response
variables, and phase-bearing variables present in canonical GRUT.

| ID | Name | Presence | Appendix P | Audit |
|----|------|----------|------------|-------|
| A1 | scalar_field_phi | present | `native_canon` | `canon.py` |
| A2 | canonical_relaxation_time_tau_sq | present | `native_canon` | `tau_level1_audit.py` |
| A3 | barrier_amplitude_a | present | `native_canon` | `barrier_action_sector.py` |
| A4 | galley_ctp_doubled_field_vars | present | `effective_reduction` | `galley_truncation.py` |
| A5 | topological_winding_charge_o3 | **conditionally_present** | `motivated_independent_postulation` | `o3_nativity_audit.py` |

### A1 — Scalar Field Φ

The canonical real scalar is the foundational GRUT state variable, derived from
first principles without free parameters. It is real-valued: no imaginary part,
no internal phase degree of freedom, no internal O(3) symmetry (unless the O(3)
postulate is adopted; see A5).

**Allowed:** "Φ is a real scalar configuration variable derived from GRUT first
principles without free parameters."
**Forbidden:** "Φ functions as a complex quantum amplitude or wavefunction."

### A2 — Canonical Relaxation Time τ²

τ² = 3/2 is derived from GRUT equilibrium architecture. It appears in the
numerical identity η² = τ²/(12π) = 1/(8π), which connects the O(3) VEV to
the Component B coefficient. The identity is a verified mathematical fact;
its physical mechanism is not established.

**Allowed:** "τ² = 3/2 is derived as the canonical equilibrium relaxation timescale."
**Forbidden:** "τ defines a quantum uncertainty relation or sets a quantum of action."

### A3 — Barrier Amplitude A

The barrier amplitude A governs the barrier action a_Q ~ (r_s/R)^β_Q. A_crit sets
the Killing horizon in the dynamic regime (Appendix J, locked). The Equilibrium
Source Degeneracy Theorem establishes that the barrier action space is
underdetermined at equilibrium.

**Allowed:** "A is a canonical state variable governing barrier dynamics."
**Forbidden:** "A behaves as a quantum probability amplitude with Born-rule interpretation."

### A4 — Galley CTP Doubled Field Variables

The CTP doubled fields (Φ₁, Φ₂) are valid in the Galley non-equilibrium regime.
They are classical: the two copies are related by the physical limit projection
Φ₋ → 0, not by quantum superposition. The Galley projection is a structural
assumption, not a derived attractor.

**Allowed:** "The CTP doubled fields are a valid effective formalism for dissipative
scalar dynamics in the Galley regime."
**Forbidden:** "The CTP doubled field space constitutes a Hilbert space or supports
quantum superposition."

### A5 — Topological Winding Charge (O(3))

The O(3) topological winding charge Q ∈ π₂(S²) = ℤ is **conditionally present**:
it requires the O(3) motivated independent postulate. BG1 (1 → 3 real scalars) is
mathematically irresolvable by derivation. The postulate is uniquely motivated by
topological necessity and Component B phenomenology (η² = τ²/(12π)).

**Allowed:** "Under the O(3) postulate, integer Q ∈ ℤ is a state variable."
**Forbidden:** "The winding charge is derived from the canonical real scalar Φ
without new field content."

---

## 4. Category B — Dynamics-Like (4 items)

**Definition:** Constitutive evolution laws, memory kernels, retarded structures,
dissipative mechanisms, and coarse-grained attractors.

| ID | Name | Presence | Appendix P | Audit |
|----|------|----------|------------|-------|
| B1 | constitutive_ode | present | `native_canon` | `canon.py` |
| B2 | galley_ctp_retarded_action | present | `effective_reduction` | `galley_truncation.py` |
| B3 | barrier_action_aq_dissipative | present | `native_canon` | `barrier_action_sector.py` |
| B4 | equilibrium_relaxation_attractor | present | `native_canon` | `tov_interior.py` |

### B1 — Constitutive ODE

τ_eff · dΦ/dt + Φ = X is the **anchor constraint** for the entire quantum program.
Any microdynamic law proposed in Q-C must recover this equation in the appropriate
macroscopic/classical limit. This is non-negotiable.

The constitutive ODE is irreversible (dissipative), first-order, and real-valued.
It has no probabilistic content.

**Forbidden failure mode FFM1:** Treating this equation as generating a Born
probability rule or acting as a Schrödinger-like equation.

### B2 — Galley CTP Retarded Action

The Galley CTP effective action provides retarded, causal dissipative structure.
At static equilibrium (Φ₁ = Φ₂ = Φ_eq), the g₋ source T^Φ₁_μν − T^Φ₂_μν
vanishes exactly (Appendix K, `g_minus_closure_audit.py`). The CTP doubled action
is classical-dissipative, not a quantum field theory path integral.

**Regime qualifier mandatory:** Valid in the Galley non-equilibrium CTP regime only.

### B3 — Barrier Action Dissipative

The barrier action a_Q is classical and real-valued. It governs barrier crossing,
not quantum tunneling. The scaling form a_Q ~ (r_s/R)^β_Q is the WCH β_Q hypothesis.

### B4 — Equilibrium Relaxation Attractor

GRUT has a static equilibrium (Φ_eq, R_eq, M_ext) — a classical fixed point, not
a quantum ground state. R_eq = 1/3, M_ext = 0.5, τ² = 3/2, α_vac = 1/3. The
equilibrium is the basis for the g₋ static closure argument.

---

## 5. Category C — Quantum-Adjacent Structural (5 items)

**Definition:** Structural features that resemble quantum ingredients but are **not**
quantum mechanical in content. Hard rule: `do_not_treat_suggestive_as_present`.

| ID | Name | Presence | Appendix P | Audit |
|----|------|----------|------------|-------|
| C1 | integer_topological_winding_z | **conditionally_present** | `motivated_independent_postulation` | `o3_nativity_audit.py` |
| C2 | tau_omega0_scale_selection | present | `working_canon_hypothesis` | `tau_family_audit.py` |
| C3 | component_b_deficit_requirement | present | `bounded_structural_result` | `route_c_deficit.py` |
| C4 | retarded_causal_kernel_structure | present | `effective_reduction` | `galley_memory.py` |
| C5 | z2_phi_reflection_symmetry | present | `native_canon` | `canon.py` |

### C1 — Integer Topological Winding ℤ

Under the O(3) postulate, integer winding Q ∈ {0, ±1, ±2, ...} provides
discreteness analogous to quantum numbers. But Q is a topological integer, not
a Hilbert space eigenvalue. The discreteness is suggestive but does not constitute
quantization.

**Forbidden failure mode FFM7:** Claiming interference from winding numbers alone.

### C2 — τ, ω₀ Scale Selection

GRUT selects definite timescales (τ² = 3/2, ω₀² = 27). This is suggestive of
quantization but is a classical phenomenon. Scale selection ≠ quantization.

### C3 — Component B Deficit Requirement

The interior deficit program (Phase 6C) requires a 1/r² tail ε_B ~ A_B/r² as a
proved structural requirement. This is a BSR result. The O(3) hedgehog provides
the matching shape and normalization (η² = τ²/(12π) ≈ 0.03979), but the
requirement exists independently of the O(3) postulate.

### C4 — Retarded Causal Kernel Structure

The Galley memory kernel is retarded and causal. Retarded causality is a *necessary*
but not *sufficient* condition for compatibility with quantum dynamics. The kernel
is classical-dissipative, not unitary.

### C5 — Z₂ Reflection Symmetry

Φ → −Φ is the only continuous-parameter-free internal symmetry of the canonical
real scalar. Z₂ is suggestive of charge conjugation but has no quantum content
in the absence of Hilbert space structure. Z₂ ≠ U(1).

---

## 6. Category D — Missing (9 items)

**Definition:** Quantum ingredients absent from canonical GRUT and not derivable
from it. These are classified `compatible_but_ad_hoc` — consistent with GRUT but
not motivated by it. Adding them requires new postulates.

**Why "absent" not "unbuilt":** The distinction matters. `motivated_but_unbuilt`
(MBU) applies when a derivation path exists in principle and requires no new DOF.
None of the Category D items can be derived from canonical GRUT without new field
content or new structural postulates — they are absent, not merely untraversed.

| ID | Name | Presence | Appendix P |
|----|------|----------|------------|
| D1 | hilbert_space_structure | absent | `compatible_but_ad_hoc` |
| D2 | operator_algebra | absent | `compatible_but_ad_hoc` |
| D3 | complex_amplitude_wavefunction | absent | `compatible_but_ad_hoc` |
| D4 | born_rule | absent | `compatible_but_ad_hoc` |
| D5 | spinorial_fields | absent | `compatible_but_ad_hoc` |
| D6 | entanglement_formalism | absent | `compatible_but_ad_hoc` |
| D7 | measurement_postulate | absent | `compatible_but_ad_hoc` |
| D8 | quantum_path_integral | absent | `compatible_but_ad_hoc` |
| D9 | decoherence_formalism | absent | `compatible_but_ad_hoc` |

### Key absences explained

**D1 — Hilbert Space:** No inner product, no complete normed vector space over ℂ.
The CTP doubling is not a Hilbert space (FFM6).

**D3 — Complex Amplitude:** Φ is real. Promoting Φ to a complex field ψ is a
BG1-class discrete DOF change: irreducible, requires MIP classification at minimum.

**D4 — Born Rule:** No probability measure defined. The constitutive ODE is
deterministic (FFM1).

**D8 — Quantum Path Integral:** The Galley CTP action is real-valued and classical.
A quantum path integral requires exp(iS) — a complex phase — which is absent.

**D9 — Decoherence Formalism:** τ-relaxation is classical dissipation toward a
fixed point. Quantum decoherence requires superposition states on a Hilbert space
plus environmental entanglement — both absent (D1, D6). FFM3 prohibits conflating
the two.

---

## 7. Category E — Obstructed (2 items)

**Definition:** Ingredients where a proved audit result establishes that they
cannot emerge from the canonical GRUT architecture under the stated assumptions.
Hard rule: `prefer_obstruction_over_vague_openness`. Hard rule:
`obstructed_items_cite_appendix_audit`.

| ID | Name | Presence | Appendix P | Audit |
|----|------|----------|------------|-------|
| E1 | fermionic_emergence | obstructed | `bounded_structural_result` | `fermionic_emergence_audit.py` |
| E2 | stable_bosonic_localized_object | obstructed | `motivated_but_unbuilt` | `localized_bosonic_object_audit.py` |

### E1 — Fermionic Emergence (BSR, 3-layer obstruction)

Fermionic emergence is obstructed at three independent layers:

| Layer | Field Content | Obstruction |
|-------|--------------|-------------|
| Layer 1 | Canonical scalar Φ | π₂(ℝ) = 0 — no topological winding; hard obstruction |
| Layer 2 | O(3) extension | π₂(S²) = ℤ — integer winding is bosonic only |
| Layer 3 | O(3) + Hopf term | Hopf term **absent** from GRUT; would provide π₃(S²) = ℤ and half-integer Berry phase via Wilczek-Zee |

Classified `bounded_structural_result` because the obstruction is proved within
the stated architecture. The Hopf term could be added as a new MIP postulate —
doing so would address Layer 3, but this is currently an independent postulate
chain beyond the canonical architecture.

**Nonclaim:** NOT claiming fermionic emergence is impossible in principle. The
obstruction is conditional on the stated architecture.

### E2 — Stable Bosonic Localized Object (MBU, Derrick obstruction)

Derrick's theorem establishes in D = 3:

    dE/dλ|_{λ=1} = E₂ + 3E_V > 0    always (without L₄)

The hedgehog in Phase D1+ is Derrick-unstable whether or not the Mexican hat
potential is included (the field-space quartic λ|Φ|⁴ scales as λ³, same sign as
E₂). Only the Skyrme gradient-quartic term L₄ — absent from GRUT — stabilizes
the soliton (L₄ scales as λ⁻¹).

Classified `motivated_but_unbuilt` (not BSR) because the resolution path is
identified: O(3) postulate + L₄ (the unique next-order O(3) EFT term, per
Appendix N). The path is coherent; it has not been traversed.

**Appendix M verdict:** `particle_candidate_not_yet_established`

**Contrast with E1:** E1 is BSR because no resolution path is identified within
the stated architecture for the Hopf-free case. E2 is MBU because the resolution
path (O(3) + L₄) is identified and structurally coherent.

---

## 8. Quantum Gap Summary

The Q0 inventory establishes the following architectural facts:

**What is present:**
- 14 items (present + conditionally present) across categories A, B, C
- Core canonical GRUT: Φ (NC), τ² (NC), constitutive ODE (NC), barrier action (NC)
- Effective formalism: Galley CTP structure (ER, with regime qualifier)
- Conditionally present: O(3) winding charge (MIP — requires independent postulate)
- Quantum-adjacent structural: integer topology, scale selection, causal kernel, Z₂ symmetry, Component B

**What is absent:**
- 9 items (Category D): Hilbert space, operator algebra, complex amplitude, Born rule,
  spinors, entanglement, measurement, quantum path integral, decoherence

**What is obstructed:**
- E1: Fermionic emergence — 3-layer BSR obstruction (Hopf term absent)
- E2: Stable bosonic particle — Derrick obstruction (L₄ absent, MBU resolution path identified)

**The gap is architectural.** Closing it requires new field content postulates
classified at minimum as `motivated_independent_postulation`. No Category D item
can be derived from canonical GRUT without new DOF.

---

## 9. Allowed and Forbidden Claims Per Category

| Category | Allowed claim type | Forbidden claim type |
|----------|--------------------|----------------------|
| A (present, NC/ER) | "derives from GRUT canon without additional postulates" | "is a quantum object" |
| A5/C1 (conditionally present, MIP) | "provides topological discreteness under O(3) postulate" | "is derived from canonical real scalar" |
| B (dynamics, NC/ER) | "is a classical dissipative evolution structure" | "generates Born probabilities or quantum amplitudes" |
| C (quantum-adjacent) | "is structurally suggestive; not quantum mechanical in content" | "implies quantum mechanics is derivable" |
| D (absent, CAH) | "could be added as an independent postulate" | "is present in or derivable from canonical GRUT" |
| E (obstructed, BSR/MBU) | "is obstructed under stated architectural assumptions; [E2: resolution path identified]" | "emerges from canonical architecture without stated postulate" |

---

## 10. Nonclaims

1. **NOT** claiming quantum-adjacent structure implies quantum mechanics is derivable.
2. **NOT** claiming the CTP doubled action is a Hilbert space formalism.
3. **NOT** claiming τ-relaxation is quantum decoherence.
4. **NOT** claiming Z₂ symmetry or topological winding numbers generate complex amplitudes.
5. **NOT** claiming that "present" items make GRUT a quantum theory.
6. **NOT** claiming obstructions are permanent beyond the stated architectural assumptions.
7. **NOT** claiming Category D items cannot be added — only that they are currently absent.

---

## 11. Readiness for Q-A

The Q0 inventory satisfies all Appendix P quantum readiness checks:

| Check | Status |
|-------|--------|
| Taxonomy used throughout | ✓ All 25 items carry Appendix P status class |
| Bounded negatives preserved | ✓ E1 (BSR), E2 (MBU) recorded and not promoted |
| Fermionic obstruction preserved | ✓ E1 three-layer BSR cited |
| Free parameters identified | ✓ O(3) η² partially constrained; Skyrme e free noted |
| Extension postulates marked | ✓ A5/C1 marked as MIP |
| No silent promotions | ✓ No D-category item classified native_canon |
| Hard rules applied | ✓ All 6 hard epistemic rules enforced |

**Q0 verdict:** `inventory_complete__quantum_gap_fully_documented`

The program proceeds to Q-A (Quantum Conceptual Charter).

---

## References

| Source | Relevance |
|--------|-----------|
| `grut/appendix_p_taxonomy_audit.py` | 8 status classes, 7 boundary rules, 8 forbidden inference patterns |
| `grut/fermionic_emergence_audit.py` | E1: 3-layer fermionic obstruction (BSR) |
| `grut/localized_bosonic_object_audit.py` | E2: Derrick obstruction, particle_candidate_not_yet_established |
| `grut/o3_nativity_audit.py` | A5/C1: O(3) MIP; η² = τ²/(12π); BG1 irresolvable |
| `grut/skyrme_term_nativity_audit.py` | L₄ motivated_but_unbuilt; e free |
| `grut/galley_truncation.py` | A4/B2/C4: CTP effective reduction |
| `grut/tau_level1_audit.py` | A2: τ² = 3/2 derived (NC) |
| `grut/g_minus_closure_audit.py` | B4: g₋ static source vanishes under Galley projection |
| `grut/route_c_deficit.py` | C3: Component B 1/r² structural requirement (BSR) |
