"""Appendix Q-A — GRUT Quantum Conceptual Charter.

This module encodes the binding charter for the entire GRUT Quantum Program.
It defines the program objective, stage sequence, Appendix P discipline rules,
forbidden failure modes, and entry nonclaims that govern all subsequent
quantum-sector work (Q-B through Q-F).

PURPOSE
-------
Q-A is the pre-derivation framework for the GRUT Quantum Program.
It does NOT derive quantum mechanics. It does NOT claim GRUT is a
quantum theory. It establishes the disciplined structure within which
quantum-sector questions will be asked and answered.

The charter enforces three things:
  1. Program scope: what the quantum program is and is not about
  2. Appendix P discipline: every quantum claim must carry a status class
  3. Forbidden failure modes: 7 specific prohibited reasoning patterns

STAGE SEQUENCE
--------------
  Q0   Quantum Entry Inventory (DONE: inventory_complete__quantum_gap_fully_documented)
  Q-A  Quantum Conceptual Charter (THIS MODULE)
  Q-B  Quantum Kinematics
  Q-C  Quantum Microdynamics
  Q-C.5 Classical Limit Recovery
  Q-D  Measurement and Decoherence
  Q-E  Benchmark Toy Problems
  Q-F  Interference and Wave Phenomena

APPENDIX P DISCIPLINE RULES (6)
---------------------------------
  QA-R1: Every quantum claim must carry an explicit Appendix P status class.
  QA-R2: No native_canon for any quantum claim unless derived from first
         principles without new DOF.
  QA-R3: If new field content required, classify as MIP minimum (not MBU).
  QA-R4: Bounded negative results preserved as BSR — not promoted.
  QA-R5: Regime qualifiers mandatory for effective_reduction claims.
  QA-R6: No compatible_but_ad_hoc claim without stating why not motivated.

FORBIDDEN FAILURE MODES (7)
----------------------------
  FFM1: born_rule_from_constitutive_ode
  FFM2: wavefunction_from_real_scalar
  FFM3: quantum_decoherence_from_relaxation
  FFM4: fermionic_statistics_without_hopf
  FFM5: stable_particle_without_skyrme
  FFM6: hilbert_space_from_ctp_doubling
  FFM7: interference_from_topology_alone

CHARTER VERDICT
---------------
  "quantum_program_authorized_and_staged"
  — all nonclaims registered, stage sequence defined, discipline rules active,
    forbidden failure modes encoded. The program may proceed to Q-B.

NONCLAIMS AT ENTRY (6)
----------------------
  1. NOT claiming GRUT is a quantum theory or derivable from quantum mechanics.
  2. NOT claiming the charter constitutes a derivation of any quantum result.
  3. NOT claiming stage success is expected or guaranteed at any stage.
  4. NOT claiming Q-B through Q-F are pre-solved.
  5. NOT claiming that authorization implies the quantum program will succeed.
  6. NOT claiming that Appendix P classification of a claim validates the claim.

See: grut/q0_quantum_entry_inventory.py (Q0 inventory, gap assessment)
     grut/appendix_p_taxonomy_audit.py (status classes, boundary rules)
     grut/fermionic_emergence_audit.py (E1 obstruction, Hopf absence)
     grut/localized_bosonic_object_audit.py (E2 obstruction, Derrick)
     grut/skyrme_term_nativity_audit.py (L4 motivated_but_unbuilt)
     grut/o3_nativity_audit.py (O(3) motivated_independent_postulation)
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

# ================================================================
# Stage sequence
# ================================================================

QUANTUM_PROGRAM_STAGES: List[str] = [
    "Q0_quantum_entry_inventory",
    "QA_quantum_conceptual_charter",
    "QB_quantum_kinematics",
    "QC_quantum_microdynamics",
    "QC5_classical_limit",
    "QD_measurement_and_decoherence",
    "QE_benchmark_toy_problems",
    "QF_interference_and_wave_phenomena",
]

N_STAGES: int = 8

# ================================================================
# Phase success criterion types
# ================================================================

ALLOWED_SUCCESS_CRITERION_TYPES: frozenset = frozenset({
    "success",          # primary goal achieved
    "partial",          # main structure identified, substantial work remaining
    "bounded_negative", # proved cannot do X — a useful constraint (BSR)
    "extension_level",  # requires new postulate — classified MIP or CAH
})

# ================================================================
# Appendix P discipline
# ================================================================

N_APPENDIX_P_DISCIPLINE_RULES: int = 6

APPENDIX_P_DISCIPLINE_RULE_IDS: List[str] = [
    "QA-R1", "QA-R2", "QA-R3", "QA-R4", "QA-R5", "QA-R6",
]

# ================================================================
# Forbidden failure modes
# ================================================================

N_FORBIDDEN_FAILURE_MODES: int = 7

FORBIDDEN_FAILURE_MODE_IDS: List[str] = [
    "FFM1", "FFM2", "FFM3", "FFM4", "FFM5", "FFM6", "FFM7",
]

FORBIDDEN_FAILURE_MODE_NAMES: List[str] = [
    "born_rule_from_constitutive_ode",
    "wavefunction_from_real_scalar",
    "quantum_decoherence_from_relaxation",
    "fermionic_statistics_without_hopf",
    "stable_particle_without_skyrme",
    "hilbert_space_from_ctp_doubling",
    "interference_from_topology_alone",
]

# ================================================================
# Charter verdicts
# ================================================================

ALLOWED_CHARTER_VERDICTS: frozenset = frozenset({
    "quantum_program_authorized_and_staged",
    "quantum_program_blocked__preconditions_not_met",
})

CHARTER_VERDICT_AUTHORIZED: str = "quantum_program_authorized_and_staged"
CHARTER_VERDICT_BLOCKED: str = "quantum_program_blocked__preconditions_not_met"

# ================================================================
# Entry nonclaims
# ================================================================

QA_ENTRY_NONCLAIMS: List[str] = [
    "NOT_claiming_grut_is_quantum_theory_or_derivable_from_qm",
    "NOT_claiming_charter_constitutes_derivation_of_any_quantum_result",
    "NOT_claiming_stage_success_expected_or_guaranteed_at_any_stage",
    "NOT_claiming_qb_through_qf_are_pre_solved",
    "NOT_claiming_authorization_implies_quantum_program_will_succeed",
    "NOT_claiming_appendix_p_classification_validates_a_claim",
]

N_QA_ENTRY_NONCLAIMS: int = 6

# ================================================================
# Dataclasses
# ================================================================


@dataclass
class QAProgramObjective:
    """The precise objective of the GRUT Quantum Program."""
    statement: str
    scope: str
    what_is_not_in_scope: List[str]   # at least 5 items
    required_preconditions: List[str]
    preconditions_met: bool


@dataclass
class QAStageDef:
    """Definition of one stage in the quantum program sequence."""
    stage_id: str               # e.g. "QB_quantum_kinematics"
    stage_name: str             # human-readable name
    stage_index: int            # 0-based index in QUANTUM_PROGRAM_STAGES
    primary_question: str       # the central question this stage answers
    success_criterion_type: str # one of ALLOWED_SUCCESS_CRITERION_TYPES
    success_criterion_description: str
    appendix_p_class_expected: str  # what Appendix P class a successful result would receive
    depends_on: List[str]           # list of stage_ids that must complete first
    hard_blockers_if_fail: List[str]  # what is blocked if this stage returns bounded_negative
    notes: List[str] = field(default_factory=list)


@dataclass
class QAAppendixPDisciplineRule:
    """One Appendix P discipline rule for the quantum program."""
    rule_id: str           # e.g. "QA-R1"
    rule_statement: str
    violation_would_be: str   # which forbidden inference pattern is prevented
    tests_for: str            # which Appendix P boundary rule (B1–B7) is enforced
    notes: List[str] = field(default_factory=list)


@dataclass
class QAForbiddenFailureMode:
    """One forbidden failure mode — a reasoning pattern that is prohibited."""
    mode_id: str           # e.g. "FFM1"
    name: str              # short label
    description: str       # what this failure mode consists of
    why_forbidden: str     # which doctrine or established result it violates
    related_appendix: str  # module or appendix establishing the relevant constraint
    notes: List[str] = field(default_factory=list)


@dataclass
class QAEntryNonclaims:
    """The binding entry nonclaims for the quantum program."""
    nonclaims: List[str]
    n_nonclaims: int          # must be >= 6
    all_registered: bool      # True


@dataclass
class QACharter:
    """Master charter result for the GRUT Quantum Program."""
    valid: bool
    objective: QAProgramObjective
    stage_sequence: List[QAStageDef]
    appendix_p_rules: List[QAAppendixPDisciplineRule]
    forbidden_failure_modes: List[QAForbiddenFailureMode]
    entry_nonclaims: QAEntryNonclaims
    q0_inventory_linked: bool     # True: Q-A depends on Q0 completing
    charter_verdict: str          # one of ALLOWED_CHARTER_VERDICTS
    diagnostics: Dict[str, Any] = field(default_factory=dict)


# ================================================================
# Builder functions
# ================================================================

def build_program_objective() -> QAProgramObjective:
    """Build the program objective for the GRUT Quantum Program."""
    return QAProgramObjective(
        statement=(
            "Determine, in a disciplined pre-derivation form, whether and how "
            "the canonical GRUT architecture can be extended to address "
            "quantum-mechanical phenomena — beginning from an honest inventory "
            "of what is present, absent, and obstructed, and proceeding stage "
            "by stage with explicit Appendix P classification of every result."
        ),
        scope=(
            "The quantum program covers Q0 through Q-F: inventory, charter, "
            "kinematics, microdynamics, classical limit, measurement, toy benchmarks, "
            "and interference. Each stage returns a result classified by Appendix P."
        ),
        what_is_not_in_scope=[
            "deriving quantum mechanics from GRUT in this charter stage",
            "claiming GRUT is already a quantum theory",
            "computing quantum amplitudes, probabilities, or interference patterns",
            "replacing the Appendix P taxonomy with a quantum-specific one",
            "adjudicating which quantum interpretation (Copenhagen, MWI, etc.) applies",
            "resolving the measurement problem or quantum foundations debates",
        ],
        required_preconditions=[
            "Q0 inventory complete (q0_complete == True)",
            "Appendix P taxonomy locked (taxonomy_complete__sufficient_for_quantum_readiness)",
            "Fermionic emergence obstruction documented (E1 BSR)",
            "Bosonic particle obstruction documented (E2 MBU)",
            "O(3) nativity verdict recorded (motivated_independent_postulation)",
        ],
        preconditions_met=True,
    )


def build_stage_sequence() -> List[QAStageDef]:
    """Build the 8-stage quantum program sequence.

    Each stage has a primary question, success criterion type, expected
    Appendix P class if successful, dependencies, and hard blockers if
    the stage returns a bounded_negative.
    """
    return [
        QAStageDef(
            stage_id="Q0_quantum_entry_inventory",
            stage_name="Quantum Entry Inventory",
            stage_index=0,
            primary_question=(
                "What quantum-relevant ingredients does GRUT already contain, "
                "what is absent, and what is structurally obstructed?"
            ),
            success_criterion_type="success",
            success_criterion_description=(
                "A complete, deterministic inventory of 25 items across categories A–E, "
                "with Appendix P classification and gap assessment."
            ),
            appendix_p_class_expected="bounded_structural_result",
            depends_on=[],
            hard_blockers_if_fail=[
                "All subsequent stages: Q-A cannot be authorized without Q0 completing."
            ],
            notes=[
                "STATUS: COMPLETE. q0_verdict = inventory_complete__quantum_gap_fully_documented.",
            ],
        ),
        QAStageDef(
            stage_id="QA_quantum_conceptual_charter",
            stage_name="Quantum Conceptual Charter",
            stage_index=1,
            primary_question=(
                "What are the binding commitments, stage structure, discipline rules, "
                "and forbidden failure modes for the GRUT Quantum Program?"
            ),
            success_criterion_type="success",
            success_criterion_description=(
                "A binding charter with 8 stages, 6 Appendix P discipline rules, "
                "7 forbidden failure modes, and ≥6 entry nonclaims."
            ),
            appendix_p_class_expected="bounded_structural_result",
            depends_on=["Q0_quantum_entry_inventory"],
            hard_blockers_if_fail=[
                "Q-B through Q-F: undisciplined quantum claims without status classification."
            ],
            notes=[
                "STATUS: THIS MODULE. charter_verdict = quantum_program_authorized_and_staged.",
            ],
        ),
        QAStageDef(
            stage_id="QB_quantum_kinematics",
            stage_name="Quantum Kinematics",
            stage_index=2,
            primary_question=(
                "What quantum objects — states, observables, configuration space — "
                "can GRUT support, given its canonical architecture and the "
                "Q0-identified ingredients?"
            ),
            success_criterion_type="partial",
            success_criterion_description=(
                "Identify the minimal kinematic structure needed to represent "
                "quantum states over the GRUT configuration space; classify each "
                "component by Appendix P status."
            ),
            appendix_p_class_expected="motivated_but_unbuilt",
            depends_on=["QA_quantum_conceptual_charter"],
            hard_blockers_if_fail=[
                "Q-C: no microdynamics without identified state space.",
                "Q-D: measurement requires prior kinematic structure.",
            ],
            notes=[
                "Expected result: partial — configuration space identifiable, "
                "Hilbert space requires new postulate (MIP).",
            ],
        ),
        QAStageDef(
            stage_id="QC_quantum_microdynamics",
            stage_name="Quantum Microdynamics",
            stage_index=3,
            primary_question=(
                "What microdynamic law governs the quantum objects identified in Q-B? "
                "Does GRUT architecture constrain or motivate the microdynamic form?"
            ),
            success_criterion_type="partial",
            success_criterion_description=(
                "Identify candidate microdynamic laws compatible with GRUT constitutive "
                "architecture; classify each route by Appendix P status."
            ),
            appendix_p_class_expected="motivated_but_unbuilt",
            depends_on=["QB_quantum_kinematics"],
            hard_blockers_if_fail=[
                "Q-C.5: no classical limit recovery without microdynamics.",
            ],
            notes=[
                "Four candidate routes from quantum_program_q1.py provide background: "
                "open-quantum-systems, stochastic, non-Markovian, holographic.",
            ],
        ),
        QAStageDef(
            stage_id="QC5_classical_limit",
            stage_name="Classical Limit Recovery",
            stage_index=4,
            primary_question=(
                "Does the microdynamic law from Q-C recover tau * dPhi/dt + Phi = X "
                "in the appropriate macroscopic/classical limit?"
            ),
            success_criterion_type="success",
            success_criterion_description=(
                "Demonstrate that the Q-C microdynamic law reduces to the canonical "
                "constitutive ODE in the classical limit; classify as BSR if proved."
            ),
            appendix_p_class_expected="bounded_structural_result",
            depends_on=["QC_quantum_microdynamics"],
            hard_blockers_if_fail=[
                "The microdynamics candidate is rejected: does not satisfy the "
                "anchor constraint. Return to Q-C with new candidate."
            ],
            notes=[
                "This is the non-negotiable anchor constraint: recovery of the "
                "constitutive ODE is mandatory for any Q-C candidate.",
            ],
        ),
        QAStageDef(
            stage_id="QD_measurement_and_decoherence",
            stage_name="Measurement and Decoherence",
            stage_index=5,
            primary_question=(
                "How does measurement and decoherence work in a GRUT quantum extension? "
                "Can the tau-relaxation structure inform the decoherence mechanism?"
            ),
            success_criterion_type="extension_level",
            success_criterion_description=(
                "Identify what new postulates (MIP or CAH) are required for a "
                "measurement and decoherence formalism; classify each by Appendix P."
            ),
            appendix_p_class_expected="motivated_independent_postulation",
            depends_on=["QC5_classical_limit"],
            hard_blockers_if_fail=[
                "Q-E and Q-F: toy problems without measurement theory have limited scope.",
            ],
            notes=[
                "Expected to require new DOF: measurement apparatus coupling is absent (D7).",
                "Forbidden: FFM3 quantum_decoherence_from_relaxation.",
            ],
        ),
        QAStageDef(
            stage_id="QE_benchmark_toy_problems",
            stage_name="Benchmark Toy Problems",
            stage_index=6,
            primary_question=(
                "Do one or more toy quantum benchmarks (harmonic oscillator, "
                "two-level system, or similar) close under the Q-C microdynamics?"
            ),
            success_criterion_type="partial",
            success_criterion_description=(
                "Demonstrate at least one toy benchmark problem that closes under "
                "the Q-C microdynamic law, or establish a bounded_negative result "
                "proving which toy problems are structurally inaccessible."
            ),
            appendix_p_class_expected="bounded_structural_result",
            depends_on=["QD_measurement_and_decoherence"],
            hard_blockers_if_fail=[
                "Q-F: interference requires prior successful toy benchmark."
            ],
            notes=[
                "A bounded_negative result (proving which toy problems cannot close) "
                "is equally valuable as a positive result.",
            ],
        ),
        QAStageDef(
            stage_id="QF_interference_and_wave_phenomena",
            stage_name="Interference and Wave Phenomena",
            stage_index=7,
            primary_question=(
                "Can the GRUT quantum extension model interference and wave phenomena? "
                "What field content and postulates are required?"
            ),
            success_criterion_type="extension_level",
            success_criterion_description=(
                "Classify the postulates required for interference modeling; "
                "determine whether an MIP-level complex amplitude extension "
                "enables a quantitative fringe law."
            ),
            appendix_p_class_expected="motivated_independent_postulation",
            depends_on=["QE_benchmark_toy_problems"],
            hard_blockers_if_fail=[
                "Interference modeling remains unresolved; "
                "result classified as open at Appendix Q-F level."
            ],
            notes=[
                "Forbidden: FFM7 interference_from_topology_alone.",
                "Requires complex amplitude (absent: D3); new DOF postulate mandatory.",
            ],
        ),
    ]


def build_appendix_p_rules() -> List[QAAppendixPDisciplineRule]:
    """Build the 6 Appendix P discipline rules for the quantum program."""
    return [
        QAAppendixPDisciplineRule(
            rule_id="QA-R1",
            rule_statement=(
                "Every quantum claim made in stages Q-B through Q-F must carry "
                "an explicit Appendix P status class (NC, ER, BSR, WCH, MBU, "
                "MIP, CAH, or FOI). Unclassified claims are not accepted."
            ),
            violation_would_be="motivated_postulate_as_native",
            tests_for="B3_bounded_vs_working",
            notes=[
                "This rule applies to every positive claim and every negative result.",
                "It is the master enforcement rule; all other rules are specializations.",
            ],
        ),
        QAAppendixPDisciplineRule(
            rule_id="QA-R2",
            rule_statement=(
                "No claim in the quantum program may be classified native_canon "
                "unless it is derived from GRUT first principles without new "
                "degrees of freedom. Quantum claims almost always require new DOF; "
                "native_canon is the exception, not the default."
            ),
            violation_would_be="usefulness_as_nativity",
            tests_for="B1_native_vs_effective",
            notes=[
                "In practice, no quantum claim is expected to be native_canon.",
                "The constitutive ODE (B1) is the only current native_canon item "
                "directly relevant to the quantum program.",
            ],
        ),
        QAAppendixPDisciplineRule(
            rule_id="QA-R3",
            rule_statement=(
                "If a quantum claim requires new field content (new DOF not present "
                "in canonical GRUT), it must be classified motivated_independent_postulation "
                "at minimum. It may not be classified motivated_but_unbuilt — "
                "MBU requires no new DOF in principle."
            ),
            violation_would_be="unbuilt_route_as_solved",
            tests_for="B5_motivated_unbuilt_vs_motivated_postulation",
            notes=[
                "Examples: complex amplitude (D3), Hilbert space (D1), spinors (D5) "
                "all require new DOF → must be MIP at minimum.",
            ],
        ),
        QAAppendixPDisciplineRule(
            rule_id="QA-R4",
            rule_statement=(
                "Bounded negative results in the quantum program — proved architectural "
                "obstructions, proved impossibilities within stated assumptions — must "
                "be recorded and preserved as bounded_structural_result. They may not "
                "be silently demoted to 'open questions' without justification."
            ),
            violation_would_be="obstruction_as_impossibility_in_principle",
            tests_for="B2_effective_vs_bounded",
            notes=[
                "E1 (fermionic emergence, 3 layers) and E2 (stable bosonic particle, "
                "Derrick) are the two current BSR obstructions.",
                "New obstructions discovered in Q-B through Q-F must be recorded as BSR.",
            ],
        ),
        QAAppendixPDisciplineRule(
            rule_id="QA-R5",
            rule_statement=(
                "All effective_reduction claims in the quantum program must state "
                "the regime in which the reduction holds. The regime must be "
                "physically specified (e.g., 'in the Galley CTP regime', "
                "'in the static equilibrium limit', 'in the non-relativistic limit')."
            ),
            violation_would_be="effective_regime_success_as_covariant_canon",
            tests_for="B1_native_vs_effective",
            notes=[
                "The Galley CTP structure (A4/B2/C4) is effective_reduction with "
                "explicit regime qualifier.",
            ],
        ),
        QAAppendixPDisciplineRule(
            rule_id="QA-R6",
            rule_statement=(
                "No claim may be classified compatible_but_ad_hoc without an "
                "explicit statement of why it is not motivated. The statement must "
                "explain which of B6's criteria (≥2 convergent motivations, uniqueness, "
                "≥1 constrained parameter) are absent."
            ),
            violation_would_be="compatibility_as_derivation",
            tests_for="B6_motivated_postulation_vs_compatible_adhoc",
            notes=[
                "Category D items (D1–D9) are classified CAH because: "
                "no convergent motivations from GRUT architecture, "
                "not unique among possible additions, no parameters constrained.",
            ],
        ),
    ]


def build_forbidden_failure_modes() -> List[QAForbiddenFailureMode]:
    """Build the 7 forbidden failure modes for the quantum program."""
    return [
        QAForbiddenFailureMode(
            mode_id="FFM1",
            name="born_rule_from_constitutive_ode",
            description=(
                "Treating the constitutive ODE tau * dPhi/dt + Phi = X as generating "
                "a Born probability rule or probabilistic interpretation of Phi. "
                "This would interpret the real scalar Phi as a probability amplitude."
            ),
            why_forbidden=(
                "The constitutive ODE is a deterministic dissipative evolution law "
                "for a real scalar. It has no probabilistic content. Born rule requires "
                "a complex amplitude on a Hilbert space — both absent (D1, D3, D4)."
            ),
            related_appendix="grut/canon.py",
            notes=[
                "Violates hard rule: do_not_treat_suggestive_as_present.",
                "The dissipative structure is classical, not quantum.",
            ],
        ),
        QAForbiddenFailureMode(
            mode_id="FFM2",
            name="wavefunction_from_real_scalar",
            description=(
                "Treating the canonical real scalar Phi as a quantum wavefunction "
                "or complex amplitude psi. This would use the nontrivial Phi profile "
                "as evidence that GRUT contains wavefunction structure."
            ),
            why_forbidden=(
                "Phi is real-valued. Complex amplitude requires a new degree of freedom "
                "(D3: absent). The real-to-complex promotion is a BG1-class gap: "
                "irreducible DOF change. Any complex amplitude must be classified MIP."
            ),
            related_appendix="grut/canon.py",
            notes=[
                "Violates Appendix P forbidden inference: usefulness_as_nativity.",
                "Violates QA-R3: new DOF requires MIP classification.",
            ],
        ),
        QAForbiddenFailureMode(
            mode_id="FFM3",
            name="quantum_decoherence_from_relaxation",
            description=(
                "Treating the tau-relaxation in the constitutive ODE as equivalent "
                "to quantum decoherence — the process by which quantum superpositions "
                "become classical mixtures via environmental entanglement."
            ),
            why_forbidden=(
                "Tau-relaxation is classical dissipation: a deterministic approach "
                "to equilibrium for a c-number field. Quantum decoherence requires "
                "a superposition state on a Hilbert space, environmental entanglement, "
                "and a density matrix. None of these are present (D1, D6 absent)."
            ),
            related_appendix="grut/tau_level1_audit.py",
            notes=[
                "Violates hard rule: do_not_treat_suggestive_as_present.",
                "Decoherence requires D1, D6 as prerequisites.",
            ],
        ),
        QAForbiddenFailureMode(
            mode_id="FFM4",
            name="fermionic_statistics_without_hopf",
            description=(
                "Claiming fermionic statistics emerge from the O(3) extension or "
                "from any part of GRUT without the Hopf term. This would use "
                "pi_2(S^2) = Z (bosonic winding) as if it provided fermionic statistics."
            ),
            why_forbidden=(
                "Fermionic statistics from O(3) require the Wilczek-Zee mechanism: "
                "adding the Hopf term with theta = pi. The Hopf term is absent from "
                "GRUT (Layer 3 of fermionic_emergence_audit.py BSR obstruction). "
                "pi_2(S^2) = Z gives integer bosonic winding only."
            ),
            related_appendix="grut/fermionic_emergence_audit.py",
            notes=[
                "E1 is classified BSR specifically because of this obstruction.",
                "The Hopf term could be added as a new MIP postulate — "
                "doing so would NOT be FFM4. FFM4 prohibits claiming fermionic "
                "statistics WITHOUT postulating the Hopf term.",
            ],
        ),
        QAForbiddenFailureMode(
            mode_id="FFM5",
            name="stable_particle_without_skyrme",
            description=(
                "Claiming GRUT supports a stable bosonic localized particle "
                "without first establishing the Skyrme term L4. This would use "
                "the hedgehog profile in Phase D1+ as if it were Derrick-stable."
            ),
            why_forbidden=(
                "Derrick's theorem proves the hedgehog is Derrick-unstable in D=3 "
                "without L4. The hedgehog collapses under spatial rescaling. "
                "L4 is motivated_but_unbuilt (Appendix N), conditioned on O(3) "
                "nativity (Appendix O). Appendix M verdict: "
                "particle_candidate_not_yet_established."
            ),
            related_appendix="grut/localized_bosonic_object_audit.py",
            notes=[
                "E2 is classified MBU precisely because the resolution path "
                "(O(3) + L4) is identified but not traversed.",
                "FFM5 prohibits claiming the particle exists before L4 is established.",
            ],
        ),
        QAForbiddenFailureMode(
            mode_id="FFM6",
            name="hilbert_space_from_ctp_doubling",
            description=(
                "Treating the Galley CTP doubled fields (Phi_1, Phi_2) or the "
                "CTP doubled action as constituting a Hilbert space or supporting "
                "quantum superposition between the two field copies."
            ),
            why_forbidden=(
                "The CTP doubling is a classical formal technique for dissipative "
                "dynamics. The two fields are related by the physical limit projection "
                "Phi_- -> 0. They do not span a Hilbert space, do not support "
                "superposition, and are not quantum mechanically entangled. "
                "Hilbert space structure is absent (D1)."
            ),
            related_appendix="grut/galley_truncation.py",
            notes=[
                "The CTP structure is effective_reduction (A4, B2) not native_canon.",
                "At equilibrium: Phi_1 = Phi_2 = Phi_eq exactly — "
                "the two copies merge, not superpose.",
            ],
        ),
        QAForbiddenFailureMode(
            mode_id="FFM7",
            name="interference_from_topology_alone",
            description=(
                "Claiming that topological winding numbers (from O(3) or any "
                "topological sector) constitute or generate interference phenomena. "
                "This would treat integer Q in Z as if it implied complex amplitudes "
                "and interference fringes."
            ),
            why_forbidden=(
                "Interference requires complex amplitudes (D3: absent) that can "
                "add with phase differences. Topological winding is a real-valued "
                "integer invariant with no phase structure. Q in {0,1,2,...} is "
                "discreteness, not amplitude. Interference requires the Q-F stage "
                "extension with MIP-level complex amplitude postulate."
            ),
            related_appendix="grut/o3_nativity_audit.py",
            notes=[
                "Violates hard rule: do_not_treat_suggestive_as_present.",
                "The discreteness of topological charge is suggestive of quantum "
                "numbers but does not constitute quantum interference.",
            ],
        ),
    ]


def build_entry_nonclaims() -> QAEntryNonclaims:
    """Build the entry nonclaims for the quantum program charter."""
    return QAEntryNonclaims(
        nonclaims=list(QA_ENTRY_NONCLAIMS),
        n_nonclaims=N_QA_ENTRY_NONCLAIMS,
        all_registered=True,
    )


def assign_charter_verdict(
    objective: QAProgramObjective,
    stages: List[QAStageDef],
    rules: List[QAAppendixPDisciplineRule],
    modes: List[QAForbiddenFailureMode],
    nonclaims: QAEntryNonclaims,
) -> str:
    """Compute the charter verdict from the assembled components.

    Returns CHARTER_VERDICT_AUTHORIZED if all preconditions are met;
    CHARTER_VERDICT_BLOCKED otherwise.
    """
    if not objective.preconditions_met:
        return CHARTER_VERDICT_BLOCKED
    if len(stages) < N_STAGES:
        return CHARTER_VERDICT_BLOCKED
    if len(rules) < N_APPENDIX_P_DISCIPLINE_RULES:
        return CHARTER_VERDICT_BLOCKED
    if len(modes) < N_FORBIDDEN_FAILURE_MODES:
        return CHARTER_VERDICT_BLOCKED
    if nonclaims.n_nonclaims < 6:
        return CHARTER_VERDICT_BLOCKED
    if not nonclaims.all_registered:
        return CHARTER_VERDICT_BLOCKED
    # Verify stage ordering
    for i, stage in enumerate(stages):
        if stage.stage_index != i:
            return CHARTER_VERDICT_BLOCKED
    # Verify all success criterion types are valid
    for stage in stages:
        if stage.success_criterion_type not in ALLOWED_SUCCESS_CRITERION_TYPES:
            return CHARTER_VERDICT_BLOCKED
    return CHARTER_VERDICT_AUTHORIZED


# ================================================================
# Master function
# ================================================================

def run_qa_quantum_charter() -> QACharter:
    """Run the Q-A Quantum Conceptual Charter.

    Assembles all components (objective, stage sequence, discipline rules,
    forbidden failure modes, nonclaims) and assigns the charter verdict.
    Returns a fully populated QACharter.
    """
    objective = build_program_objective()
    stages = build_stage_sequence()
    rules = build_appendix_p_rules()
    modes = build_forbidden_failure_modes()
    nonclaims = build_entry_nonclaims()

    # Sanity checks
    assert len(stages) == N_STAGES, (
        f"Expected {N_STAGES} stages, got {len(stages)}"
    )
    assert len(rules) == N_APPENDIX_P_DISCIPLINE_RULES, (
        f"Expected {N_APPENDIX_P_DISCIPLINE_RULES} rules, got {len(rules)}"
    )
    assert len(modes) == N_FORBIDDEN_FAILURE_MODES, (
        f"Expected {N_FORBIDDEN_FAILURE_MODES} modes, got {len(modes)}"
    )
    assert nonclaims.n_nonclaims >= 6, (
        f"Need >= 6 nonclaims, got {nonclaims.n_nonclaims}"
    )

    # Verify stage sequence integrity
    for i, stage in enumerate(stages):
        assert stage.stage_index == i, (
            f"Stage {stage.stage_id} has index {stage.stage_index}, expected {i}"
        )
        assert stage.success_criterion_type in ALLOWED_SUCCESS_CRITERION_TYPES, (
            f"Stage {stage.stage_id} has invalid criterion type "
            f"{stage.success_criterion_type}"
        )

    # Verify rule IDs
    rule_ids = [r.rule_id for r in rules]
    for expected_id in APPENDIX_P_DISCIPLINE_RULE_IDS:
        assert expected_id in rule_ids, f"Rule {expected_id} missing"

    # Verify forbidden failure mode IDs and names
    mode_ids = [m.mode_id for m in modes]
    mode_names = [m.name for m in modes]
    for expected_id in FORBIDDEN_FAILURE_MODE_IDS:
        assert expected_id in mode_ids, f"FFM {expected_id} missing"
    for expected_name in FORBIDDEN_FAILURE_MODE_NAMES:
        assert expected_name in mode_names, f"FFM name {expected_name} missing"

    # Q0 linkage: Q-A depends_on must include Q0, and Q-B must depend on Q-A
    qa_stage = next(s for s in stages if s.stage_id == "QA_quantum_conceptual_charter")
    assert "Q0_quantum_entry_inventory" in qa_stage.depends_on, (
        "Q-A must depend on Q0"
    )
    qb_stage = next(s for s in stages if s.stage_id == "QB_quantum_kinematics")
    assert "QA_quantum_conceptual_charter" in qb_stage.depends_on, (
        "Q-B must depend on Q-A"
    )

    charter_verdict = assign_charter_verdict(
        objective, stages, rules, modes, nonclaims
    )

    assert charter_verdict == CHARTER_VERDICT_AUTHORIZED, (
        f"Charter should be authorized; got {charter_verdict}"
    )

    diagnostics: Dict[str, Any] = {
        "n_stages": len(stages),
        "n_appendix_p_rules": len(rules),
        "n_forbidden_failure_modes": len(modes),
        "n_entry_nonclaims": nonclaims.n_nonclaims,
        "stage_ids": [s.stage_id for s in stages],
        "rule_ids": [r.rule_id for r in rules],
        "ffm_names": [m.name for m in modes],
        "preconditions_met": objective.preconditions_met,
        "q0_linked": True,
        "charter_verdict": charter_verdict,
        "all_stages_have_valid_criterion_types": all(
            s.success_criterion_type in ALLOWED_SUCCESS_CRITERION_TYPES
            for s in stages
        ),
        "success_stage_count": sum(
            1 for s in stages if s.success_criterion_type == "success"
        ),
        "partial_stage_count": sum(
            1 for s in stages if s.success_criterion_type == "partial"
        ),
        "bounded_negative_stage_count": sum(
            1 for s in stages if s.success_criterion_type == "bounded_negative"
        ),
        "extension_level_stage_count": sum(
            1 for s in stages if s.success_criterion_type == "extension_level"
        ),
    }

    return QACharter(
        valid=True,
        objective=objective,
        stage_sequence=stages,
        appendix_p_rules=rules,
        forbidden_failure_modes=modes,
        entry_nonclaims=nonclaims,
        q0_inventory_linked=True,
        charter_verdict=charter_verdict,
        diagnostics=diagnostics,
    )
