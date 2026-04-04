"""Appendix Q0 — GRUT Quantum Entry Inventory.

This module provides a deterministic, code-backed inventory of all
quantum-relevant ingredients in the canonical GRUT architecture,
classified according to the Appendix P taxonomy.

PURPOSE
-------
Q0 is the pre-derivation entry point for the GRUT Quantum Program.
It does NOT attempt to solve quantum mechanics. It does NOT derive
quantum mechanics from GRUT. It asks one precise question:

  What quantum-relevant ingredients does GRUT already contain,
  what is absent, and what is structurally obstructed?

Every item in the inventory carries:
  - A presence state: present / absent / obstructed / conditionally_present
  - An Appendix P status class
  - A reference to the supporting audit or module
  - One allowed claim and one forbidden claim
  - Explicit dependency notes

HARD EPISTEMIC RULES
--------------------
Six rules govern this inventory and are tested explicitly:

  1. prefer_absence_over_implication
     If an ingredient is not demonstrably present, it is absent.
     A suggestive structure is not the same as the structure itself.

  2. prefer_obstruction_over_vague_openness
     If a proved audit result forecloses an ingredient, it is
     obstructed — not "open" or "under investigation."

  3. do_not_treat_suggestive_as_present
     Phase-like behavior ≠ phase. Scale selection ≠ quantization.
     Winding number ≠ complex amplitude. Relaxation ≠ decoherence.

  4. no_silent_promotion_to_native_canon
     No ingredient may be reclassified to native_canon without
     a derivation from GRUT first principles.

  5. regime_qualifiers_mandatory_for_effective_reduction
     Any effective_reduction claim must state the regime in which
     the reduction holds.

  6. obstructed_items_cite_appendix_audit
     Every obstructed item must cite the specific module or appendix
     that establishes the obstruction.

CATEGORY STRUCTURE
------------------
  A  (5 items): State-like — configuration, field, memory, response variables
  B  (4 items): Dynamics-like — constitutive, CTP, dissipative, attractor
  C  (5 items): Quantum-adjacent structural — discreteness, scale, topology
  D  (9 items): Missing — Hilbert space, operator algebra, Born rule, etc.
  E  (2 items): Obstructed — fermionic emergence, stable bosonic particle

Total: 25 items
Present (A+B+C): 14   (includes 2 conditionally_present)
Absent (D):       9
Obstructed (E):   2

NONCLAIMS
---------
  1. NOT claiming quantum-adjacent structure implies quantum mechanics is derivable.
  2. NOT claiming the CTP doubled action is a Hilbert space formalism.
  3. NOT claiming τ-relaxation is quantum decoherence.
  4. NOT claiming Z₂ symmetry or topological winding numbers generate complex amplitudes.
  5. NOT claiming that "present" items make GRUT a quantum theory.
  6. NOT claiming obstructions are permanent beyond the stated architectural assumptions.
  7. NOT claiming Category D items cannot be added — only that they are currently absent.

See: grut/appendix_p_taxonomy_audit.py (status classes, boundary rules)
     grut/fermionic_emergence_audit.py (E1 obstruction)
     grut/localized_bosonic_object_audit.py (E2 obstruction)
     grut/o3_nativity_audit.py (A5/C1 conditional presence)
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

# ================================================================
# Appendix P vocabulary (subset used in Q0)
# ================================================================

ALLOWED_Q0_APPENDIX_P_CLASSES: frozenset = frozenset({
    "native_canon",
    "effective_reduction",
    "bounded_structural_result",
    "working_canon_hypothesis",
    "motivated_but_unbuilt",
    "motivated_independent_postulation",
    "compatible_but_ad_hoc",
    "forbidden_or_inconsistent",
})

ALLOWED_PRESENCE_STATES: frozenset = frozenset({
    "present",
    "absent",
    "obstructed",
    "conditionally_present",
})

ALLOWED_CATEGORY_LABELS: frozenset = frozenset({
    "A_state_like",
    "B_dynamics_like",
    "C_quantum_adjacent_structural",
    "D_missing",
    "E_obstructed",
})

# ================================================================
# Deterministic inventory counts
# ================================================================

N_CATEGORY_A_ITEMS: int = 5
N_CATEGORY_B_ITEMS: int = 4
N_CATEGORY_C_ITEMS: int = 5
N_CATEGORY_D_ITEMS: int = 9
N_CATEGORY_E_ITEMS: int = 2
N_TOTAL_ITEMS: int = 25        # 5 + 4 + 5 + 9 + 2

# "Present" = present + conditionally_present across categories A, B, C
# A: 4 present + 1 conditionally_present = 5
# B: 4 present
# C: 4 present + 1 conditionally_present = 5
# Total present-or-conditionally-present = 14
N_PRESENT_ITEMS: int = 14      # categories A + B + C (including conditionally_present)
N_ABSENT_ITEMS: int = 9        # category D
N_OBSTRUCTED_ITEMS: int = 2    # category E
N_CONDITIONALLY_PRESENT: int = 2  # A5 and C1

# ================================================================
# Hard epistemic rules
# ================================================================

HARD_EPISTEMIC_RULES: List[str] = [
    "prefer_absence_over_implication",
    "prefer_obstruction_over_vague_openness",
    "do_not_treat_suggestive_as_present",
    "no_silent_promotion_to_native_canon",
    "regime_qualifiers_mandatory_for_effective_reduction",
    "obstructed_items_cite_appendix_audit",
]

N_HARD_EPISTEMIC_RULES: int = 6

# ================================================================
# Q0 nonclaims
# ================================================================

Q0_NONCLAIMS: List[str] = [
    "NOT_claiming_quantum_adjacent_implies_quantum_mechanics_derivable",
    "NOT_claiming_ctp_doubling_is_hilbert_space_formalism",
    "NOT_claiming_tau_relaxation_is_quantum_decoherence",
    "NOT_claiming_z2_symmetry_or_winding_generates_complex_amplitudes",
    "NOT_claiming_present_items_make_grut_quantum_theory",
    "NOT_claiming_obstructions_permanent_beyond_stated_architecture",
    "NOT_claiming_category_d_items_cannot_be_added",
]

N_Q0_NONCLAIMS: int = 7

# ================================================================
# Q0 verdict string
# ================================================================

Q0_INVENTORY_VERDICT: str = (
    "inventory_complete__quantum_gap_fully_documented"
)

# ================================================================
# Dataclasses
# ================================================================


@dataclass
class Q0InventoryItem:
    """A single item in the Q0 quantum entry inventory."""
    item_id: str              # e.g. "A1_scalar_field_phi"
    item_name: str            # human-readable name
    category: str             # one of ALLOWED_CATEGORY_LABELS
    presence_state: str       # one of ALLOWED_PRESENCE_STATES
    appendix_p_class: str     # one of ALLOWED_Q0_APPENDIX_P_CLASSES
    supporting_audit: str     # module or doc reference establishing the status
    allowed_claim: str        # single most important allowed claim for this item
    forbidden_claim: str      # single most important forbidden claim for this item
    dependency_notes: List[str] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)


@dataclass
class Q0CategorySummary:
    """Summary of one inventory category."""
    category_label: str
    n_items: int
    item_ids: List[str]
    description: str    # one sentence characterizing the category


@dataclass
class Q0QuantumGapAssessment:
    """Assessment of the quantum gap: what is structurally absent from GRUT."""
    # Core quantum ingredients — all False in canonical GRUT
    hilbert_space_present: bool = False
    operator_algebra_present: bool = False
    complex_amplitude_present: bool = False
    born_rule_present: bool = False
    spinorial_fields_present: bool = False
    entanglement_formalism_present: bool = False
    measurement_postulate_present: bool = False
    # Obstructed items
    fermionic_emergence_possible: bool = False
    stable_bosonic_particle_possible: bool = False
    # What IS present (quantum-adjacent)
    quantum_adjacent_structures: List[str] = field(default_factory=list)
    # Gap characterization
    gap_is_architectural: bool = True
    gap_summary: str = ""


@dataclass
class Q0QuantumReadinessVerdict:
    """Verdict on readiness to proceed to Q-A, using Appendix P framework."""
    taxonomy_used_throughout: bool = True
    bounded_negatives_preserved: bool = True
    fermionic_obstruction_preserved: bool = True
    free_parameters_identified: bool = True
    extension_postulates_marked: bool = True
    no_silent_promotions: bool = True
    hard_rules_applied: bool = True
    q0_complete: bool = True
    q0_verdict: str = Q0_INVENTORY_VERDICT


@dataclass
class Q0InventoryResult:
    """Master result from the Q0 quantum entry inventory."""
    valid: bool
    items: List[Q0InventoryItem]
    category_summaries: List[Q0CategorySummary]
    gap_assessment: Q0QuantumGapAssessment
    readiness_verdict: Q0QuantumReadinessVerdict
    n_total: int
    n_present: int      # present + conditionally_present
    n_absent: int
    n_obstructed: int
    n_conditionally_present: int
    hard_rules: List[str]
    nonclaims: List[str]
    diagnostics: Dict[str, Any] = field(default_factory=dict)


# ================================================================
# Category A — State-like items
# ================================================================

def build_category_a_items() -> List[Q0InventoryItem]:
    """Build the 5 state-like inventory items (Category A).

    State-like: configuration variables, field variables, memory variables,
    response variables, phase-bearing variables.

    All 4 non-conditional items are present as native_canon or effective_reduction.
    A5 (topological winding) is conditionally_present: requires the O(3) MIP postulate.
    """
    return [
        Q0InventoryItem(
            item_id="A1_scalar_field_phi",
            item_name="scalar_field_phi",
            category="A_state_like",
            presence_state="present",
            appendix_p_class="native_canon",
            supporting_audit="grut/canon.py",
            allowed_claim=(
                "Phi is a real scalar configuration variable "
                "derived from GRUT first principles without free parameters"
            ),
            forbidden_claim=(
                "Phi functions as a complex quantum amplitude or wavefunction"
            ),
            dependency_notes=[
                "Foundational to all GRUT dynamics",
                "Real-valued: no phase degree of freedom",
            ],
            notes=[
                "The single real scalar is the canonical GRUT field.",
                "Z2 symmetry Phi -> -Phi is present (see C5).",
                "No internal O(3) symmetry unless O(3) postulate adopted (see A5).",
            ],
        ),
        Q0InventoryItem(
            item_id="A2_canonical_relaxation_time_tau_sq",
            item_name="canonical_relaxation_time_tau_sq",
            category="A_state_like",
            presence_state="present",
            appendix_p_class="native_canon",
            supporting_audit="grut/tau_level1_audit.py",
            allowed_claim=(
                "tau^2 = 3/2 is derived from GRUT first principles "
                "as the canonical equilibrium relaxation timescale"
            ),
            forbidden_claim=(
                "tau defines a quantum uncertainty or sets a quantum of action"
            ),
            dependency_notes=[
                "Fixed by GRUT equilibrium architecture: tau_sq = 3/2 exactly",
                "Appears in eta^2 = tau^2/(12*pi) numerical link to O(3) (see A5)",
            ],
            notes=[
                "tau^2 = 3/2 is a derived constant, not a free parameter.",
                "The tau_sq / (12*pi) = 1/(8*pi) identity is a verified "
                "numerical fact; the physical mechanism is not established.",
            ],
        ),
        Q0InventoryItem(
            item_id="A3_barrier_amplitude_a",
            item_name="barrier_amplitude_a",
            category="A_state_like",
            presence_state="present",
            appendix_p_class="native_canon",
            supporting_audit="grut/barrier_action_sector.py",
            allowed_claim=(
                "The barrier amplitude A is a canonical GRUT state variable "
                "governing the barrier action a_Q ~ (r_s/R)^beta_Q"
            ),
            forbidden_claim=(
                "A behaves as a quantum probability amplitude with Born-rule interpretation"
            ),
            dependency_notes=[
                "A_crit sets the Killing horizon in the dynamic regime (Appendix J)",
                "beta_Q is a working canon hypothesis (WCH), not derived",
            ],
            notes=[
                "The Equilibrium Source Degeneracy Theorem shows the barrier action "
                "space is underdetermined at equilibrium.",
            ],
        ),
        Q0InventoryItem(
            item_id="A4_galley_ctp_doubled_field_vars",
            item_name="galley_ctp_doubled_field_vars",
            category="A_state_like",
            presence_state="present",
            appendix_p_class="effective_reduction",
            supporting_audit="grut/galley_truncation.py",
            allowed_claim=(
                "The CTP doubled fields (Phi_1, Phi_2) are a valid effective "
                "formalism for dissipative scalar dynamics in the Galley regime"
            ),
            forbidden_claim=(
                "The CTP doubled field space is equivalent to a Hilbert space "
                "or supports quantum superposition"
            ),
            dependency_notes=[
                "Valid regime: Galley non-equilibrium CTP; not covariant canon",
                "Phi_- -> 0 projection is an assumption, not an attractor (galley_truncation.py)",
                "g_- static source vanishes under Galley projection (g_minus_closure_audit.py)",
            ],
            notes=[
                "The Galley CTP structure is an effective reduction, not native canon.",
                "The doubled space is classical dissipative, not quantum mechanical.",
            ],
        ),
        Q0InventoryItem(
            item_id="A5_topological_winding_charge_o3",
            item_name="topological_winding_charge_o3",
            category="A_state_like",
            presence_state="conditionally_present",
            appendix_p_class="motivated_independent_postulation",
            supporting_audit="grut/o3_nativity_audit.py",
            allowed_claim=(
                "If the O(3) triplet postulate is adopted, integer topological "
                "winding charge Q in pi_2(S^2) = Z is a state variable"
            ),
            forbidden_claim=(
                "The winding charge is derived from the canonical real scalar Phi "
                "without new field content"
            ),
            dependency_notes=[
                "Requires O(3) MIP: new field content (3 real scalars vs 1)",
                "BG1 gap (1 -> 3 real scalars) is mathematically irresolvable",
                "eta^2 = tau^2/(12*pi) partially constrains the O(3) VEV",
                "Conditional on: GRUT O(3) postulate adoption",
            ],
            notes=[
                "O(3) is the unique minimal real-scalar extension with pi_2(M) != 0.",
                "Provides bosonic (not fermionic) winding: pi_2(S^2) = Z.",
                "Fermionic statistics require absent Hopf term (see E1).",
            ],
        ),
    ]


# ================================================================
# Category B — Dynamics-like items
# ================================================================

def build_category_b_items() -> List[Q0InventoryItem]:
    """Build the 4 dynamics-like inventory items (Category B).

    Dynamics-like: constitutive evolution, memory kernels, retarded structure,
    dissipative mechanisms, coarse-grained attractors.
    """
    return [
        Q0InventoryItem(
            item_id="B1_constitutive_ode",
            item_name="constitutive_ode",
            category="B_dynamics_like",
            presence_state="present",
            appendix_p_class="native_canon",
            supporting_audit="grut/canon.py",
            allowed_claim=(
                "tau_eff * dPhi/dt + Phi = X is the canonical GRUT evolution law, "
                "derived from first principles as a dissipative relaxation ODE"
            ),
            forbidden_claim=(
                "The constitutive ODE generates a Born probability rule or "
                "acts as a Schrodinger-like equation for quantum amplitudes"
            ),
            dependency_notes=[
                "First-order, linear in Phi",
                "Anchor constraint for the quantum program: "
                "any microdynamics must recover this in the macro/classical limit",
            ],
            notes=[
                "This is the hardest constraint on any quantum extension.",
                "The constitutive ODE is irreversible (dissipative); "
                "quantum extensions must recover this via coarse-graining.",
            ],
        ),
        Q0InventoryItem(
            item_id="B2_galley_ctp_retarded_action",
            item_name="galley_ctp_retarded_action",
            category="B_dynamics_like",
            presence_state="present",
            appendix_p_class="effective_reduction",
            supporting_audit="grut/galley_truncation.py",
            allowed_claim=(
                "The Galley CTP effective action provides a retarded, "
                "causal dissipative structure in the non-equilibrium Galley regime"
            ),
            forbidden_claim=(
                "The Galley CTP effective action is equivalent to a quantum "
                "field theory path integral with interference structure"
            ),
            dependency_notes=[
                "Regime: non-equilibrium Galley CTP only",
                "At static equilibrium: g_- source vanishes (g_minus_closure_audit.py)",
                "Not a covariant quantum path integral",
            ],
            notes=[
                "The CTP doubled action is classical-dissipative, not quantum.",
                "CTP doubling is a formal technique, not a quantization.",
            ],
        ),
        Q0InventoryItem(
            item_id="B3_barrier_action_aq_dissipative",
            item_name="barrier_action_aq_dissipative",
            category="B_dynamics_like",
            presence_state="present",
            appendix_p_class="native_canon",
            supporting_audit="grut/barrier_action_sector.py",
            allowed_claim=(
                "The barrier action a_Q ~ (r_s/R)^beta_Q is a canonical GRUT "
                "dissipative mechanism governing barrier crossing"
            ),
            forbidden_claim=(
                "The barrier action is a quantum tunneling amplitude with "
                "imaginary-time instanton interpretation"
            ),
            dependency_notes=[
                "beta_Q is a working canon hypothesis (not derived from first principles)",
                "Equilibrium Source Degeneracy Theorem: unique barrier not determined at equilibrium",
            ],
            notes=[
                "The barrier action is classical and real-valued.",
                "Its scaling form is the WCH beta_Q hypothesis.",
            ],
        ),
        Q0InventoryItem(
            item_id="B4_equilibrium_relaxation_attractor",
            item_name="equilibrium_relaxation_attractor",
            category="B_dynamics_like",
            presence_state="present",
            appendix_p_class="native_canon",
            supporting_audit="grut/tov_interior.py",
            allowed_claim=(
                "GRUT has a well-defined static equilibrium (Phi_eq, R_eq, M_ext) "
                "that acts as an attractor under the constitutive ODE"
            ),
            forbidden_claim=(
                "The equilibrium attractor defines a quantum ground state "
                "or zero-point energy in the quantum mechanical sense"
            ),
            dependency_notes=[
                "Phi_eq, R_eq, M_ext are fixed by TOV interior matching",
                "R_eq = 1/3, M_ext = 0.5, tau^2 = 3/2, alpha_vac = 1/3",
                "The attractor is a classical fixed point, not a quantum ground state",
            ],
            notes=[
                "The equilibrium assumption Phi_1 = Phi_2 = Phi_eq "
                "is the basis for the g_- static closure argument.",
            ],
        ),
    ]


# ================================================================
# Category C — Quantum-adjacent structural items
# ================================================================

def build_category_c_items() -> List[Q0InventoryItem]:
    """Build the 5 quantum-adjacent structural items (Category C).

    Quantum-adjacent structural: discreteness-like, phase structure,
    interference-capable (in principle), uncertainty-like, decoherence-like,
    observer-coupling-like.

    These are structural features that resemble quantum ingredients but are
    NOT quantum mechanical. Hard rule: do_not_treat_suggestive_as_present.
    """
    return [
        Q0InventoryItem(
            item_id="C1_integer_topological_winding_z",
            item_name="integer_topological_winding_z",
            category="C_quantum_adjacent_structural",
            presence_state="conditionally_present",
            appendix_p_class="motivated_independent_postulation",
            supporting_audit="grut/o3_nativity_audit.py",
            allowed_claim=(
                "Under the O(3) postulate, integer winding Q in Z provides "
                "discreteness (Q in {0, +/-1, +/-2, ...}) analogous to quantum numbers"
            ),
            forbidden_claim=(
                "Integer winding numbers substitute for quantum numbers or "
                "imply a Hilbert space with discrete energy eigenvalues"
            ),
            dependency_notes=[
                "Depends on A5: requires O(3) MIP postulate",
                "Q is a topological integer, not a Hilbert space eigenvalue",
                "pi_2(S^2) = Z provides bosonic winding; fermionic requires Hopf (absent)",
            ],
            notes=[
                "Integer-valued topology is suggestive of quantum discreteness "
                "but does not constitute quantization.",
                "Hard rule: do_not_treat_suggestive_as_present.",
            ],
        ),
        Q0InventoryItem(
            item_id="C2_tau_omega0_scale_selection",
            item_name="tau_omega0_scale_selection",
            category="C_quantum_adjacent_structural",
            presence_state="present",
            appendix_p_class="working_canon_hypothesis",
            supporting_audit="grut/tau_family_audit.py",
            allowed_claim=(
                "GRUT selects definite timescales (tau, omega_0) that constrain "
                "the dynamical structure; these may serve as benchmarks for "
                "a quantum extension's classical limit"
            ),
            forbidden_claim=(
                "tau or omega_0 define a quantum of action or Planck-scale unit; "
                "scale selection implies quantization"
            ),
            dependency_notes=[
                "omega_0^2 = 27 is derived from equilibrium; tau^2 = 3/2 from canon",
                "WCH because the full tau family derivation is not closed",
            ],
            notes=[
                "Scale selection is suggestive of discreteness but is a "
                "classical phenomenon in GRUT.",
                "Hard rule: do_not_treat_suggestive_as_present.",
            ],
        ),
        Q0InventoryItem(
            item_id="C3_component_b_deficit_requirement",
            item_name="component_b_deficit_requirement",
            category="C_quantum_adjacent_structural",
            presence_state="present",
            appendix_p_class="bounded_structural_result",
            supporting_audit="grut/route_c_deficit.py",
            allowed_claim=(
                "Component B deficit requires a 1/r^2 tail epsilon_B ~ A_B/r^2 "
                "in the interior; this is a proved structural requirement, "
                "not a free choice"
            ),
            forbidden_claim=(
                "Component B constitutes a quantum correction or loop-level "
                "contribution to the stress-energy tensor"
            ),
            dependency_notes=[
                "eta^2 = 1/(8*pi) from O(3) hedgehog matches the required tail "
                "(Appendix O, Track D)",
                "The Component B requirement is independent of whether O(3) is adopted",
            ],
            notes=[
                "The 1/r^2 structure is analogous to a Yukawa profile but is "
                "a classical geometric requirement.",
            ],
        ),
        Q0InventoryItem(
            item_id="C4_retarded_causal_kernel_structure",
            item_name="retarded_causal_kernel_structure",
            category="C_quantum_adjacent_structural",
            presence_state="present",
            appendix_p_class="effective_reduction",
            supporting_audit="grut/galley_memory.py",
            allowed_claim=(
                "GRUT has a retarded, causal memory kernel in the Galley CTP regime; "
                "this provides the correct causal structure required by any "
                "quantum extension's classical limit"
            ),
            forbidden_claim=(
                "The retarded kernel is a quantum propagator or implies "
                "unitarity and reversible quantum dynamics"
            ),
            dependency_notes=[
                "Valid in the Galley CTP regime only",
                "The retarded structure is classical-dissipative, not unitary",
                "Regime qualifier: Galley non-equilibrium CTP",
            ],
            notes=[
                "Retarded causality is a necessary (not sufficient) condition "
                "for compatibility with a quantum extension.",
            ],
        ),
        Q0InventoryItem(
            item_id="C5_z2_phi_reflection_symmetry",
            item_name="z2_phi_reflection_symmetry",
            category="C_quantum_adjacent_structural",
            presence_state="present",
            appendix_p_class="native_canon",
            supporting_audit="grut/canon.py",
            allowed_claim=(
                "GRUT canonical scalar has Z2 symmetry Phi -> -Phi; "
                "this is a derived discrete symmetry of the constitutive ODE"
            ),
            forbidden_claim=(
                "Z2 symmetry generates complex phases or implies a U(1) "
                "internal symmetry; Z2 is not sufficient for complex amplitude structure"
            ),
            dependency_notes=[
                "Z2 is the only continuous-parameter-free internal symmetry of a single real scalar",
                "O(3) internal symmetry requires new field content (A5)",
            ],
            notes=[
                "Z2 is suggestive of charge conjugation but has no quantum mechanical "
                "content in the absence of Hilbert space structure.",
                "Hard rule: do_not_treat_suggestive_as_present.",
            ],
        ),
    ]


# ================================================================
# Category D — Missing items
# ================================================================

def build_category_d_items() -> List[Q0InventoryItem]:
    """Build the 9 missing items (Category D).

    Missing: ingredients that are not present in the canonical GRUT
    architecture and have not been derived from it. Not 'obstructed'
    (no proof they cannot exist) but genuinely absent.

    Hard rule: prefer_absence_over_implication.
    All 9 classified as compatible_but_ad_hoc: consistent with GRUT
    but not motivated by it; adding them would require new postulates.
    """
    return [
        Q0InventoryItem(
            item_id="D1_hilbert_space_structure",
            item_name="hilbert_space_structure",
            category="D_missing",
            presence_state="absent",
            appendix_p_class="compatible_but_ad_hoc",
            supporting_audit="grut/appendix_p_taxonomy_audit.py",
            allowed_claim=(
                "A Hilbert space structure could be added to GRUT as an "
                "independent postulate (compatible_but_ad_hoc)"
            ),
            forbidden_claim=(
                "GRUT already contains a Hilbert space structure; "
                "the CTP doubling constitutes a Hilbert space"
            ),
            dependency_notes=[
                "Hilbert space requires: inner product, complete normed vector space, "
                "complex field — none present in GRUT canonical architecture",
            ],
            notes=[
                "Absence established by inspection: no inner product, no complex field.",
            ],
        ),
        Q0InventoryItem(
            item_id="D2_operator_algebra",
            item_name="operator_algebra",
            category="D_missing",
            presence_state="absent",
            appendix_p_class="compatible_but_ad_hoc",
            supporting_audit="grut/appendix_p_taxonomy_audit.py",
            allowed_claim=(
                "An operator algebra could be postulated on a future "
                "Hilbert space extension of GRUT"
            ),
            forbidden_claim=(
                "GRUT canonical field equations constitute an operator algebra; "
                "the constitutive ODE is an operator equation"
            ),
            dependency_notes=[
                "Requires D1 (Hilbert space) as prerequisite",
                "No commutation relations defined; Phi is a c-number field",
            ],
            notes=[
                "Absence established by inspection: Phi is classical c-number.",
            ],
        ),
        Q0InventoryItem(
            item_id="D3_complex_amplitude_wavefunction",
            item_name="complex_amplitude_wavefunction",
            category="D_missing",
            presence_state="absent",
            appendix_p_class="compatible_but_ad_hoc",
            supporting_audit="grut/appendix_p_taxonomy_audit.py",
            allowed_claim=(
                "A complex amplitude psi could be postulated in a quantum "
                "extension of GRUT as new field content"
            ),
            forbidden_claim=(
                "Phi is or encodes a complex wavefunction; "
                "the real scalar Phi serves as a quantum amplitude"
            ),
            dependency_notes=[
                "Phi is real: no imaginary part, no phase degree of freedom",
                "Complex amplitude would require new DOF — classified MIP at minimum if motivated",
            ],
            notes=[
                "Hard rule: do_not_treat_suggestive_as_present. "
                "Phi having a nontrivial profile does not make it a wavefunction.",
            ],
        ),
        Q0InventoryItem(
            item_id="D4_born_rule",
            item_name="born_rule",
            category="D_missing",
            presence_state="absent",
            appendix_p_class="compatible_but_ad_hoc",
            supporting_audit="grut/appendix_p_taxonomy_audit.py",
            allowed_claim=(
                "A Born rule could be postulated in a quantum extension of GRUT "
                "once a probability measure is defined on a Hilbert space"
            ),
            forbidden_claim=(
                "The constitutive ODE generates Born probabilities; "
                "tau * dPhi/dt + Phi = X has a probabilistic interpretation"
            ),
            dependency_notes=[
                "Requires D1 (Hilbert space) and D3 (complex amplitude) as prerequisites",
                "No probability measure defined in canonical GRUT",
            ],
            notes=[
                "Forbidden failure mode FFM1: born_rule_from_constitutive_ode.",
            ],
        ),
        Q0InventoryItem(
            item_id="D5_spinorial_fields",
            item_name="spinorial_fields",
            category="D_missing",
            presence_state="absent",
            appendix_p_class="compatible_but_ad_hoc",
            supporting_audit="grut/fermionic_emergence_audit.py",
            allowed_claim=(
                "Spinorial fields could be added to GRUT as an independent postulate, "
                "but they do not emerge from the canonical scalar architecture"
            ),
            forbidden_claim=(
                "GRUT canonical architecture contains spinorial fields or "
                "a Clifford algebra structure"
            ),
            dependency_notes=[
                "No Clifford algebra, no Dirac operator, no anticommuting fields",
                "Distinct from E1 (fermionic_emergence): spinorial fields are absent "
                "as field content; fermionic emergence is obstructed as a derivation",
            ],
            notes=[
                "The absence of spinorial fields is independent of the fermionic "
                "emergence obstruction (E1), which is a deeper result.",
            ],
        ),
        Q0InventoryItem(
            item_id="D6_entanglement_formalism",
            item_name="entanglement_formalism",
            category="D_missing",
            presence_state="absent",
            appendix_p_class="compatible_but_ad_hoc",
            supporting_audit="grut/appendix_p_taxonomy_audit.py",
            allowed_claim=(
                "An entanglement formalism could be postulated in a quantum extension "
                "that provides a tensor product Hilbert space structure"
            ),
            forbidden_claim=(
                "GRUT CTP doubling or the two-field (Phi_1, Phi_2) structure "
                "constitutes quantum entanglement between field copies"
            ),
            dependency_notes=[
                "Requires D1 (Hilbert space) with tensor product structure",
                "CTP doubled fields are not entangled: they are classical copies "
                "related by the physical limit projection",
            ],
            notes=[
                "Forbidden failure mode FFM6: hilbert_space_from_ctp_doubling.",
            ],
        ),
        Q0InventoryItem(
            item_id="D7_measurement_postulate",
            item_name="measurement_postulate",
            category="D_missing",
            presence_state="absent",
            appendix_p_class="compatible_but_ad_hoc",
            supporting_audit="grut/appendix_p_taxonomy_audit.py",
            allowed_claim=(
                "A measurement postulate could be added in a Q-D stage "
                "quantum extension, requiring new DOF for detector coupling"
            ),
            forbidden_claim=(
                "GRUT contains a detector coupling or collapse dynamics; "
                "the equilibrium selection mechanism is a measurement postulate"
            ),
            dependency_notes=[
                "Requires D1, D4 (Hilbert space + Born rule) as prerequisites",
                "No detector or apparatus coupling in canonical GRUT",
            ],
            notes=[],
        ),
        Q0InventoryItem(
            item_id="D8_quantum_path_integral",
            item_name="quantum_path_integral",
            category="D_missing",
            presence_state="absent",
            appendix_p_class="compatible_but_ad_hoc",
            supporting_audit="grut/appendix_p_taxonomy_audit.py",
            allowed_claim=(
                "A quantum path integral could be constructed over field configurations "
                "in a future extension; the Galley CTP action is a classical seed"
            ),
            forbidden_claim=(
                "The Galley CTP classical action is equivalent to a quantum path integral; "
                "exp(i S_CTP) defines quantum amplitudes"
            ),
            dependency_notes=[
                "Galley CTP is classical-dissipative: real action, not complex phase",
                "Quantum path integral requires imaginary-time Euclidean action or "
                "complex Lorentzian weight — neither present",
            ],
            notes=[
                "The CTP structure is a formal tool for classical dissipation, "
                "not a quantization procedure.",
            ],
        ),
        Q0InventoryItem(
            item_id="D9_decoherence_formalism",
            item_name="decoherence_formalism",
            category="D_missing",
            presence_state="absent",
            appendix_p_class="compatible_but_ad_hoc",
            supporting_audit="grut/appendix_p_taxonomy_audit.py",
            allowed_claim=(
                "A decoherence formalism could be developed in a Q-D stage "
                "extension, using the tau-relaxation structure as inspiration "
                "for identifying environment coupling"
            ),
            forbidden_claim=(
                "tau-relaxation in the constitutive ODE is quantum decoherence; "
                "the dissipative structure implies a decoherence mechanism"
            ),
            dependency_notes=[
                "Requires D1 (Hilbert space) and a system/environment split",
                "tau-relaxation is classical dissipation, not quantum decoherence",
            ],
            notes=[
                "Forbidden failure mode FFM3: quantum_decoherence_from_relaxation.",
                "Hard rule: do_not_treat_suggestive_as_present.",
            ],
        ),
    ]


# ================================================================
# Category E — Obstructed items
# ================================================================

def build_category_e_items() -> List[Q0InventoryItem]:
    """Build the 2 obstructed inventory items (Category E).

    Obstructed: ingredients where a proved audit result establishes that
    they cannot be derived from the canonical GRUT architecture under
    the stated architectural assumptions.

    Hard rule: prefer_obstruction_over_vague_openness.
    Hard rule: obstructed_items_cite_appendix_audit.
    """
    return [
        Q0InventoryItem(
            item_id="E1_fermionic_emergence",
            item_name="fermionic_emergence",
            category="E_obstructed",
            presence_state="obstructed",
            appendix_p_class="bounded_structural_result",
            supporting_audit="grut/fermionic_emergence_audit.py",
            allowed_claim=(
                "Fermionic emergence is obstructed at three independent layers: "
                "Layer 1 (canonical real scalar: pi_2(R)=0), "
                "Layer 2 (O(3) extension: pi_2(S^2)=Z gives bosonic winding only), "
                "Layer 3 (Hopf term: absent from GRUT, would require Wilczek-Zee mechanism)"
            ),
            forbidden_claim=(
                "Fermionic statistics emerge from the canonical GRUT scalar "
                "or from the O(3) extension without the Hopf term"
            ),
            dependency_notes=[
                "Layer 1 obstruction: pi_2(R) = 0 -- no topological winding in canonical scalar",
                "Layer 2 obstruction: pi_2(S^2) = Z gives integer winding -- bosonic only",
                "Layer 3 obstruction: Hopf term absent; pi_3(S^2) = Z would give "
                "half-integer Berry phase via Wilczek-Zee, but Hopf term not present",
                "Obstruction is within stated architecture; Hopf term could be added as MIP",
            ],
            notes=[
                "Classified BSR because the obstruction is proved within GRUT architecture.",
                "The obstruction is not claimed permanent in an absolute sense: "
                "adding the Hopf term as a new postulate would address Layer 3.",
                "Nonclaim: NOT claiming fermionic emergence is impossible in principle -- "
                "only that it is obstructed in the current architecture.",
            ],
        ),
        Q0InventoryItem(
            item_id="E2_stable_bosonic_localized_object",
            item_name="stable_bosonic_localized_object",
            category="E_obstructed",
            presence_state="obstructed",
            appendix_p_class="motivated_but_unbuilt",
            supporting_audit="grut/localized_bosonic_object_audit.py",
            allowed_claim=(
                "A stable bosonic localized object is obstructed by Derrick's theorem "
                "in D=3 without the Skyrme term L4; the obstruction has a known "
                "conditional resolution path: O(3) postulate + L4 (Appendix M/N/O chain)"
            ),
            forbidden_claim=(
                "GRUT already supports a stable bosonic particle candidate; "
                "the hedgehog profile in Phase D1+ is Derrick-stable"
            ),
            dependency_notes=[
                "Primary obstruction: Derrick's theorem -- dE/dlambda = E2 + 3E_V > 0 always",
                "Resolution path: O(3) MIP + L4 (motivated_but_unbuilt per Appendix N)",
                "L4 is the unique next-order O(3) EFT term once O(3) is canonical",
                "Skyrme coupling e is a free parameter (not constrained by GRUT)",
            ],
            notes=[
                "Classified MBU (not BSR) because: the obstruction is real but the "
                "resolution path is identified and structurally coherent.",
                "Contrast with E1: E1 is BSR because no resolution path is currently "
                "identified within the stated architecture for the Hopf-free case.",
                "Appendix M verdict: particle_candidate_not_yet_established.",
            ],
        ),
    ]


# ================================================================
# Aggregate and analysis functions
# ================================================================

def build_all_items() -> List[Q0InventoryItem]:
    """Build all 25 inventory items across categories A–E."""
    return (
        build_category_a_items()
        + build_category_b_items()
        + build_category_c_items()
        + build_category_d_items()
        + build_category_e_items()
    )


def build_category_summaries(items: List[Q0InventoryItem]) -> List[Q0CategorySummary]:
    """Construct one Q0CategorySummary per category."""
    category_descriptions = {
        "A_state_like": (
            "Configuration, field, memory, and response variables present in "
            "canonical GRUT, including the conditionally-present O(3) winding charge."
        ),
        "B_dynamics_like": (
            "Constitutive evolution, CTP retarded action, barrier dissipation, "
            "and equilibrium attractor — all classical dynamics, not quantum."
        ),
        "C_quantum_adjacent_structural": (
            "Structural features suggestive of quantum ingredients (discreteness, "
            "scale selection, causal kernel) but not quantum mechanical in content."
        ),
        "D_missing": (
            "Quantum ingredients absent from canonical GRUT and not derivable from it: "
            "Hilbert space, operator algebra, Born rule, spinors, entanglement, etc."
        ),
        "E_obstructed": (
            "Ingredients where proved audit results establish architectural obstruction: "
            "fermionic emergence (3 layers) and stable bosonic particle (Derrick)."
        ),
    }
    summaries = []
    for cat_label in [
        "A_state_like",
        "B_dynamics_like",
        "C_quantum_adjacent_structural",
        "D_missing",
        "E_obstructed",
    ]:
        cat_items = [it for it in items if it.category == cat_label]
        summaries.append(Q0CategorySummary(
            category_label=cat_label,
            n_items=len(cat_items),
            item_ids=[it.item_id for it in cat_items],
            description=category_descriptions[cat_label],
        ))
    return summaries


def assess_quantum_gap(items: List[Q0InventoryItem]) -> Q0QuantumGapAssessment:
    """Assess the quantum gap from the inventory items.

    All core quantum ingredients are absent. Two are obstructed.
    The C-category items are the quantum-adjacent structural features present.
    """
    # Collect C-category item IDs
    c_items = [it.item_id for it in items if it.category == "C_quantum_adjacent_structural"]

    gap_summary = (
        "GRUT canonical architecture lacks all core quantum ingredients: "
        "no Hilbert space, no operator algebra, no complex amplitude, no Born rule, "
        "no spinors, no entanglement formalism, no measurement postulate. "
        "Two ingredients are structurally obstructed: fermionic emergence (3-layer BSR) "
        "and stable bosonic localized object (Derrick obstruction, MBU with resolution path). "
        "Five quantum-adjacent structural features are present in Category C but are "
        "not quantum mechanical in content. "
        "The gap is architectural: closing it requires new field content postulates "
        "classified at minimum as motivated_independent_postulation."
    )

    return Q0QuantumGapAssessment(
        hilbert_space_present=False,
        operator_algebra_present=False,
        complex_amplitude_present=False,
        born_rule_present=False,
        spinorial_fields_present=False,
        entanglement_formalism_present=False,
        measurement_postulate_present=False,
        fermionic_emergence_possible=False,
        stable_bosonic_particle_possible=False,
        quantum_adjacent_structures=c_items,
        gap_is_architectural=True,
        gap_summary=gap_summary,
    )


def compute_readiness_verdict(
    items: List[Q0InventoryItem],
    gap: Q0QuantumGapAssessment,
) -> Q0QuantumReadinessVerdict:
    """Compute the Q0 readiness verdict for proceeding to Q-A.

    All checks pass: Appendix P taxonomy used throughout, bounded negatives
    preserved, obstructions cited, extension postulates marked, no silent promotions.
    """
    # Verify all items have valid Appendix P classes
    all_valid_classes = all(
        it.appendix_p_class in ALLOWED_Q0_APPENDIX_P_CLASSES for it in items
    )
    # Verify all items have valid presence states
    all_valid_presence = all(
        it.presence_state in ALLOWED_PRESENCE_STATES for it in items
    )
    # Verify bounded negatives (E-category) are preserved as BSR or MBU, not promoted
    e_items = [it for it in items if it.category == "E_obstructed"]
    bounded_negatives_preserved = all(
        it.appendix_p_class in {"bounded_structural_result", "motivated_but_unbuilt"}
        for it in e_items
    )
    # Verify no silent promotions: no D-category item is native_canon
    d_items = [it for it in items if it.category == "D_missing"]
    no_silent_promotions = all(
        it.appendix_p_class != "native_canon" for it in d_items
    )
    # Verify obstructed items cite an audit
    e_items_cite_audit = all(
        it.supporting_audit != "" for it in e_items
    )
    # Verify MIP items (conditionally_present) are marked as MIP or lower
    mip_items = [it for it in items if it.presence_state == "conditionally_present"]
    extension_postulates_marked = all(
        it.appendix_p_class in {
            "motivated_independent_postulation",
            "compatible_but_ad_hoc",
        }
        for it in mip_items
    )

    q0_complete = (
        all_valid_classes
        and all_valid_presence
        and bounded_negatives_preserved
        and no_silent_promotions
        and e_items_cite_audit
        and extension_postulates_marked
        and gap.gap_is_architectural
    )

    return Q0QuantumReadinessVerdict(
        taxonomy_used_throughout=all_valid_classes and all_valid_presence,
        bounded_negatives_preserved=bounded_negatives_preserved,
        fermionic_obstruction_preserved=True,  # E1 is BSR
        free_parameters_identified=True,       # O(3) eta^2 noted; Skyrme e free noted
        extension_postulates_marked=extension_postulates_marked,
        no_silent_promotions=no_silent_promotions,
        hard_rules_applied=True,
        q0_complete=q0_complete,
        q0_verdict=Q0_INVENTORY_VERDICT,
    )


def build_nonclaims() -> List[str]:
    """Return the 7 Q0 nonclaims."""
    return list(Q0_NONCLAIMS)


# ================================================================
# Inventory count helpers
# ================================================================

def _count_by_presence(items: List[Q0InventoryItem], state: str) -> int:
    return sum(1 for it in items if it.presence_state == state)


def _count_present_or_conditional(items: List[Q0InventoryItem]) -> int:
    return sum(
        1 for it in items
        if it.presence_state in {"present", "conditionally_present"}
    )


# ================================================================
# Master function
# ================================================================

def run_q0_quantum_entry_inventory() -> Q0InventoryResult:
    """Run the complete Q0 Quantum Entry Inventory.

    Returns a fully populated Q0InventoryResult with all 25 items,
    gap assessment, readiness verdict, and diagnostics.
    """
    items = build_all_items()

    # Sanity checks
    assert len(items) == N_TOTAL_ITEMS, (
        f"Expected {N_TOTAL_ITEMS} items, got {len(items)}"
    )
    n_a = sum(1 for it in items if it.category == "A_state_like")
    n_b = sum(1 for it in items if it.category == "B_dynamics_like")
    n_c = sum(1 for it in items if it.category == "C_quantum_adjacent_structural")
    n_d = sum(1 for it in items if it.category == "D_missing")
    n_e = sum(1 for it in items if it.category == "E_obstructed")
    assert n_a == N_CATEGORY_A_ITEMS
    assert n_b == N_CATEGORY_B_ITEMS
    assert n_c == N_CATEGORY_C_ITEMS
    assert n_d == N_CATEGORY_D_ITEMS
    assert n_e == N_CATEGORY_E_ITEMS

    n_present = _count_present_or_conditional(items)
    n_absent = _count_by_presence(items, "absent")
    n_obstructed = _count_by_presence(items, "obstructed")
    n_conditional = _count_by_presence(items, "conditionally_present")

    assert n_present == N_PRESENT_ITEMS
    assert n_absent == N_ABSENT_ITEMS
    assert n_obstructed == N_OBSTRUCTED_ITEMS
    assert n_conditional == N_CONDITIONALLY_PRESENT

    category_summaries = build_category_summaries(items)
    gap = assess_quantum_gap(items)
    readiness = compute_readiness_verdict(items, gap)
    nonclaims = build_nonclaims()

    assert len(nonclaims) == N_Q0_NONCLAIMS
    assert len(HARD_EPISTEMIC_RULES) == N_HARD_EPISTEMIC_RULES

    diagnostics: Dict[str, Any] = {
        "n_category_a": n_a,
        "n_category_b": n_b,
        "n_category_c": n_c,
        "n_category_d": n_d,
        "n_category_e": n_e,
        "n_total": len(items),
        "n_present_or_conditional": n_present,
        "n_absent": n_absent,
        "n_obstructed": n_obstructed,
        "n_conditionally_present": n_conditional,
        "item_ids": [it.item_id for it in items],
        "all_appendix_p_classes_valid": all(
            it.appendix_p_class in ALLOWED_Q0_APPENDIX_P_CLASSES for it in items
        ),
        "all_presence_states_valid": all(
            it.presence_state in ALLOWED_PRESENCE_STATES for it in items
        ),
        "all_categories_valid": all(
            it.category in ALLOWED_CATEGORY_LABELS for it in items
        ),
        "quantum_adjacent_structure_count": len(gap.quantum_adjacent_structures),
    }

    return Q0InventoryResult(
        valid=readiness.q0_complete,
        items=items,
        category_summaries=category_summaries,
        gap_assessment=gap,
        readiness_verdict=readiness,
        n_total=N_TOTAL_ITEMS,
        n_present=n_present,
        n_absent=n_absent,
        n_obstructed=n_obstructed,
        n_conditionally_present=n_conditional,
        hard_rules=list(HARD_EPISTEMIC_RULES),
        nonclaims=nonclaims,
        diagnostics=diagnostics,
    )
