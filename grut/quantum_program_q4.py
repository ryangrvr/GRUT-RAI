"""GRUT Phase Q4 — Program Fork Audit and Phase-Completion Decision.

Determines which next move is most justified for completing the present
recovery/spectral phase of the Future Quantum Program:

    Path A — Circularity-Break Program
    Path B — Noise/Fluctuation Program
    Path C — Canon-Closure / Consolidation Program

CENTRAL FINDING:
  Path C (Canon-Closure) is the best next move.

  The recovery/spectral phase Q1-Q3 forms a complete and self-consistent
  structured-extension result. The correct next step is formal consolidation,
  not deeper derivation.

  - Path A (circularity break) is PREMATURE: the first-order constitutive
    kernel is an axiom, not a theorem. No visible non-circular route exists
    in the current architecture to derive it from fast-mode elimination.
    Attempting it now would manufacture a dressed-up restatement.

  - Path B (noise/fluctuation) is CONCEPTUALLY REQUIRED BUT NOT READY:
    a physically meaningful bath interpretation demands companion noise
    structure, but GRUT currently provides no temperature, no noise
    observables, and no route to derive (vs import) the FDT relation.
    Attempting it now would import standard results as if they were GRUT
    derivations.

  - Path C (consolidation) is HONEST: it registers Q1-Q3 as a completed
    phase with explicit boundaries, identifies what the next phase requires
    (circularity break OR noise structure), and does not manufacture
    authority that the current architecture cannot support.

LOCKED INHERITANCE:
  Appendix C: All blockers remain (no amplitudes, Born rule, interference,
              measurement, collapse/decoherence, particle ontology).
  Q1: CTP/Galley recovery shell — exact at tree level, bath unspecified.
  Q2: Drude/Lorentzian self-bath identification — structural match only.
  Q3: Algebraic grounding in interior PDE — partially circular.

NONCLAIMS:
  1. This module does NOT solve the circularity.
  2. This module does NOT derive noise or fluctuation spectra.
  3. This module does NOT claim the current phase resolves any Appendix C blocker.
  4. "Consolidation" means registering what has been established and what has not.
  5. Q4 does NOT close the Future Quantum Program — it closes the first
     recovery/spectral phase and identifies what the next phase requires.
  6. The fork decision is based on feasibility and honesty, not ambition.

See: quantum_program_q1.py, quantum_program_q2.py, quantum_program_q3.py
     for upstream structures.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Dict, Any, Literal


# ================================================================
# Constants — Locked Inheritance
# ================================================================

# Phase completion requirements
PHASE_NAME = "recovery_spectral_phase"
PHASE_DESCRIPTION = (
    "Determine whether the published GRUT constitutive memory law can be "
    "interpreted as a candidate emergent dissipative limit, identify the "
    "bath type, and ground the spectral structure in the interior sector."
)

# What each prior phase established
Q1_ESTABLISHED = (
    "The published constitutive memory law tau dPhi/dt + Phi = X can be "
    "treated as a candidate emergent dissipative limit of a deeper "
    "doubled/open-system structure (CTP/Galley). Recovery is exact at "
    "tree level. Bath DOF are unspecified."
)

Q2_ESTABLISHED = (
    "The strongest bath-type candidate is a Drude/Lorentzian self-bath "
    "of fast memory modes. The published tau_eff formula has the exact "
    "functional form of Lorentzian susceptibility from a single-pole "
    "ohmic bath with cutoff Omega = 1/tau_0. This is a structural match, "
    "not a derivation."
)

Q3_ESTABLISHED = (
    "The interior PDE dispersion relation explicitly contains the "
    "single-pole Lorentzian 1/(1+i*omega*tau) as the memory sector's "
    "susceptibility. The Q2 Drude clue is algebraically grounded in the "
    "published interior sector. The grounding is partially circular: the "
    "single-pole form follows from the first-order axiom."
)

# What remains unresolved after Q1-Q3
UNRESOLVED_AFTER_Q3 = [
    "The circularity is not broken: the Lorentzian is algebraically "
    "guaranteed by the first-order memory law",
    "The physical bath DOF are not identified",
    "The spectral density is not derived from first principles",
    "No noise/fluctuation spectrum is computed or constrainable",
    "No temperature or energy scale is available for FDT",
    "No Appendix C blocker is resolved",
    "The covariant interior metric is missing (Phase V obstruction)",
    "Loop corrections (quantum Phi_- fluctuations) are not computed",
    "The Galley ghost Phi_- connection to bath noise is not established",
]

# Forbidden claims at Q4 level
Q4_FORBIDDEN_CLAIMS = [
    "breaks_circularity",
    "derives_noise_spectrum",
    "derives_born_rule",
    "derives_interference",
    "derives_measurement",
    "resolves_appendix_c",
    "completes_quantum_program",
    "proves_bath_physical",
    "derives_first_order_law",
    "derives_fdt",
    "identifies_bath_dof",
]


# ================================================================
# Type Definitions
# ================================================================

PathStatus = Literal[
    "best_next_move",
    "valuable_but_secondary",
    "premature",
    "reject_for_now",
]

FeasibilityLevel = Literal[
    "feasible_now",
    "visible_but_underdetermined",
    "likely_premature",
    "circularity_not_breakable_yet",
    "conceptually_required_but_not_ready",
]

PhaseCompletionStatus = Literal[
    "complete_for_consolidation",
    "requires_circularity_break",
    "requires_fluctuation_structure",
    "requires_both",
    "incomplete_and_blocked",
]


# ================================================================
# Data Structures
# ================================================================

@dataclass
class PathDefinition:
    """Definition of a Q4 fork path."""
    name: str
    label: str
    goal: str
    core_question: str
    why_needed_now: str

    # Relationship to prior phases
    depends_on_q1: bool = False
    depends_on_q2: bool = False
    depends_on_q3: bool = False
    q1_dependency_description: str = ""
    q2_dependency_description: str = ""
    q3_dependency_description: str = ""

    # Assessment columns
    canon_continuity: str = ""
    formal_tractability: str = ""
    risk_of_circular_restatement: str = ""
    risk_of_manufactured_authority: str = ""
    expected_upgrade_value: str = ""
    what_remains_blocked_if_successful: str = ""

    # Classification
    status: PathStatus = "reject_for_now"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "label": self.label,
            "goal": self.goal,
            "core_question": self.core_question,
            "why_needed_now": self.why_needed_now,
            "depends_on": {
                "q1": self.depends_on_q1,
                "q2": self.depends_on_q2,
                "q3": self.depends_on_q3,
            },
            "canon_continuity": self.canon_continuity,
            "formal_tractability": self.formal_tractability,
            "risk_of_circular_restatement": self.risk_of_circular_restatement,
            "risk_of_manufactured_authority": self.risk_of_manufactured_authority,
            "expected_upgrade_value": self.expected_upgrade_value,
            "what_remains_blocked_if_successful": self.what_remains_blocked_if_successful,
            "status": self.status,
        }


@dataclass
class SuccessCriteria:
    """What would count as success for a given path."""
    path: str
    criteria: List[str] = field(default_factory=list)
    minimum_for_success: str = ""
    would_upgrade_from: str = ""
    would_upgrade_to: str = ""
    upgrade_is_material: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return {
            "path": self.path,
            "criteria": self.criteria,
            "minimum_for_success": self.minimum_for_success,
            "would_upgrade_from": self.would_upgrade_from,
            "would_upgrade_to": self.would_upgrade_to,
            "upgrade_is_material": self.upgrade_is_material,
        }


@dataclass
class FeasibilityAudit:
    """Feasibility audit for a specific path."""
    path: str
    feasibility: FeasibilityLevel = "likely_premature"

    # Audit questions and answers
    questions: List[Dict[str, str]] = field(default_factory=list)

    # Required structures
    structures_needed: List[str] = field(default_factory=list)
    structures_present: List[str] = field(default_factory=list)
    structures_missing: List[str] = field(default_factory=list)
    structures_extendable: List[str] = field(default_factory=list)

    # Risk assessment
    likely_to_produce_real_derivation: bool = False
    likely_to_restate_existing: bool = False
    likely_to_import_external: bool = False

    # Summary
    summary: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "path": self.path,
            "feasibility": self.feasibility,
            "questions": self.questions,
            "structures_needed": self.structures_needed,
            "structures_present": self.structures_present,
            "structures_missing": self.structures_missing,
            "structures_extendable": self.structures_extendable,
            "likely_to_produce_real_derivation": self.likely_to_produce_real_derivation,
            "likely_to_restate_existing": self.likely_to_restate_existing,
            "likely_to_import_external": self.likely_to_import_external,
            "summary": self.summary,
        }


@dataclass
class PhaseCompletionTest:
    """Test for whether the current recovery/spectral phase is complete."""
    phase_status: PhaseCompletionStatus = "incomplete_and_blocked"

    # What has been achieved
    q1_contribution: str = ""
    q2_contribution: str = ""
    q3_contribution: str = ""
    combined_statement: str = ""

    # Completion conditions
    circularity_break_required_for_completion: bool = False
    fluctuation_structure_required_for_completion: bool = False
    consolidation_sufficient_for_completion: bool = False

    # Rationale
    rationale: str = ""

    # What the next phase would address
    next_phase_targets: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "phase_status": self.phase_status,
            "q1_contribution": self.q1_contribution,
            "q2_contribution": self.q2_contribution,
            "q3_contribution": self.q3_contribution,
            "combined_statement": self.combined_statement,
            "circularity_break_required": self.circularity_break_required_for_completion,
            "fluctuation_structure_required": self.fluctuation_structure_required_for_completion,
            "consolidation_sufficient": self.consolidation_sufficient_for_completion,
            "rationale": self.rationale,
            "next_phase_targets": self.next_phase_targets,
        }


@dataclass
class DocumentConstraints:
    """Constraints for any future document summarising Q1-Q4."""
    safe_claims: List[str] = field(default_factory=list)
    unsafe_claims: List[str] = field(default_factory=list)
    strongest_defensible_classification: str = ""
    q4_framing: str = ""
    # One of: "fork_decision", "phase_completion_audit",
    #         "structured_extension", "speculative_horizon", "failure"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "safe_claims": self.safe_claims,
            "unsafe_claims": self.unsafe_claims,
            "strongest_defensible_classification": self.strongest_defensible_classification,
            "q4_framing": self.q4_framing,
        }


@dataclass
class Q4Result:
    """Master result from Phase Q4 Fork Audit and Completion Decision."""
    executive_determination: str = ""
    # One of:
    #   "path_a_best_next_move"
    #   "path_b_best_next_move"
    #   "path_c_consolidation_best_next_move"
    #   "alternative_path_best"

    # Locked inheritance
    q1_established: str = Q1_ESTABLISHED
    q2_established: str = Q2_ESTABLISHED
    q3_established: str = Q3_ESTABLISHED
    unresolved_after_q3: List[str] = field(
        default_factory=lambda: list(UNRESOLVED_AFTER_Q3)
    )

    # Paths
    paths: List[PathDefinition] = field(default_factory=list)
    best_path: str = ""
    best_path_status: str = ""

    # Success criteria
    success_criteria: List[SuccessCriteria] = field(default_factory=list)

    # Feasibility audits
    feasibility_audits: List[FeasibilityAudit] = field(default_factory=list)

    # Phase completion
    phase_completion: PhaseCompletionTest = field(
        default_factory=PhaseCompletionTest
    )

    # Hard blockers surviving Q4
    hard_blockers_after_q4: List[Dict[str, Any]] = field(default_factory=list)

    # Safe/unsafe claims
    safe_claims: List[str] = field(default_factory=list)
    unsafe_claims: List[str] = field(default_factory=list)
    nonclaims: List[str] = field(default_factory=list)

    # Document constraints
    document_constraints: DocumentConstraints = field(
        default_factory=DocumentConstraints
    )

    # Next phase recommendation
    next_phase_recommendation: str = ""

    # Classification
    q4_classification: str = ""
    # One of:
    #   "fork_decision"
    #   "phase_completion_audit"
    #   "structured_extension"
    #   "speculative_horizon"
    #   "failure"

    valid: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return {
            "executive_determination": self.executive_determination,
            "best_path": self.best_path,
            "best_path_status": self.best_path_status,
            "q1_established": self.q1_established,
            "q2_established": self.q2_established,
            "q3_established": self.q3_established,
            "unresolved_after_q3": self.unresolved_after_q3,
            "paths": [p.to_dict() for p in self.paths],
            "success_criteria": [s.to_dict() for s in self.success_criteria],
            "feasibility_audits": [f.to_dict() for f in self.feasibility_audits],
            "phase_completion": self.phase_completion.to_dict(),
            "hard_blockers_after_q4": self.hard_blockers_after_q4,
            "safe_claims": self.safe_claims,
            "unsafe_claims": self.unsafe_claims,
            "nonclaims": self.nonclaims,
            "document_constraints": self.document_constraints.to_dict(),
            "next_phase_recommendation": self.next_phase_recommendation,
            "q4_classification": self.q4_classification,
            "valid": self.valid,
        }


# ================================================================
# Path Builders
# ================================================================

def build_path_a() -> PathDefinition:
    """Path A — Circularity-Break Program."""
    return PathDefinition(
        name="A",
        label="Circularity-Break Program",
        goal=(
            "Derive or visibly motivate the first-order constitutive kernel "
            "from deeper mode elimination or reduction, so that the "
            "Lorentzian is no longer merely embedded but emergent."
        ),
        core_question=(
            "Can the first-order memory law tau dPhi/dt + Phi = X be derived "
            "from elimination of fast modes, so that its first-order character "
            "is an output rather than an axiom?"
        ),
        why_needed_now=(
            "The Q3 circularity is the most prominent open issue: the "
            "Lorentzian spectral structure is algebraically guaranteed by "
            "the first-order axiom. Breaking this circularity would upgrade "
            "Q3 from algebraic_grounding to derivational_origin."
        ),
        depends_on_q1=True,
        depends_on_q2=True,
        depends_on_q3=True,
        q1_dependency_description=(
            "Uses the CTP/Galley recovery shell as the parent formalism "
            "from which the first-order law would be derived."
        ),
        q2_dependency_description=(
            "Uses the Drude bath identification to constrain what the "
            "fast modes should look like."
        ),
        q3_dependency_description=(
            "Directly targets the Q3 circularity: first-order axiom -> "
            "Lorentzian -> first-order axiom."
        ),
        canon_continuity="high",
        formal_tractability="low",
        risk_of_circular_restatement="very_high",
        risk_of_manufactured_authority="high",
        expected_upgrade_value=(
            "If successful: algebraic_grounding -> derivational_origin. "
            "This would be a major upgrade but there is no visible route."
        ),
        what_remains_blocked_if_successful=(
            "All Appendix C blockers. Noise spectrum still unknown. "
            "Bath DOF still formal. Temperature/energy scale absent."
        ),
        status="premature",
    )


def build_path_b() -> PathDefinition:
    """Path B — Noise/Fluctuation Program."""
    return PathDefinition(
        name="B",
        label="Noise/Fluctuation Program",
        goal=(
            "Determine whether a physically meaningful dissipative bath "
            "interpretation requires a companion fluctuation/noise structure, "
            "and whether any such structure is derivable or constrainable "
            "from current GRUT architecture."
        ),
        core_question=(
            "If the Q2 Drude bath interpretation is physically meaningful, "
            "what companion noise/fluctuation spectrum must exist, and can "
            "any signature of it be derived or constrained from published "
            "GRUT structures?"
        ),
        why_needed_now=(
            "A dissipative bath without noise is thermodynamically incomplete. "
            "If the bath interpretation is more than formal, the noise sector "
            "is a structural necessity. This would be the first non-circular "
            "discriminator between formal-shell and physical-bath readings."
        ),
        depends_on_q1=True,
        depends_on_q2=True,
        depends_on_q3=False,
        q1_dependency_description=(
            "Uses the CTP/Galley structure. In CTP formalism, the ghost "
            "field Phi_- encodes noise; its fluctuations are the noise "
            "kernel. But this connection is not established in GRUT."
        ),
        q2_dependency_description=(
            "Uses the Drude bath identification. A Drude bath has a known "
            "noise spectrum via FDT: S(omega) proportional to "
            "omega * Omega^2 / (omega^2 + Omega^2) * coth(h_bar*omega/2kT). "
            "But this requires a temperature."
        ),
        q3_dependency_description=(
            "Does not directly depend on Q3. The noise question is "
            "independent of whether the Lorentzian is grounded or circular."
        ),
        canon_continuity="moderate",
        formal_tractability="low_to_moderate",
        risk_of_circular_restatement="moderate",
        risk_of_manufactured_authority="high",
        expected_upgrade_value=(
            "If successful: bath interpretation upgraded from formal to "
            "physically testable. Would provide the first empirical "
            "discriminator. But success requires structures not yet present."
        ),
        what_remains_blocked_if_successful=(
            "All Appendix C blockers. Circularity not addressed. "
            "First-order law still axiomatic. No quantum measurement theory."
        ),
        status="valuable_but_secondary",
    )


def build_path_c() -> PathDefinition:
    """Path C — Canon-Closure / Consolidation Program."""
    return PathDefinition(
        name="C",
        label="Canon-Closure / Consolidation Program",
        goal=(
            "Register Q1-Q3 as a completed recovery/spectral phase. "
            "Consolidate into a coherent structured-extension statement "
            "with explicit nonclaims, boundaries, and identification of "
            "what the next phase requires."
        ),
        core_question=(
            "Is the current Q1-Q3 result set complete enough for the "
            "recovery/spectral phase, or would further immediate probing "
            "manufacture false authority?"
        ),
        why_needed_now=(
            "Path A has no visible non-circular route. Path B requires "
            "structures not present. The honest assessment is that Q1-Q3 "
            "form a self-consistent phase result, and the next real "
            "progress requires new architecture (covariant interior metric, "
            "temperature/energy scale, or deeper substrate theory) that "
            "is not available in the current published structure."
        ),
        depends_on_q1=True,
        depends_on_q2=True,
        depends_on_q3=True,
        q1_dependency_description="Registers Q1 as the parent-formalism layer.",
        q2_dependency_description="Registers Q2 as the bath-identification layer.",
        q3_dependency_description="Registers Q3 as the algebraic-grounding layer.",
        canon_continuity="highest",
        formal_tractability="high",
        risk_of_circular_restatement="low",
        risk_of_manufactured_authority="lowest",
        expected_upgrade_value=(
            "No upgrade to prior results. The value is honest closure: "
            "registering what has been established, what has not, and "
            "what the next phase would need to address."
        ),
        what_remains_blocked_if_successful=(
            "Everything that was blocked before. Path C does not resolve "
            "any blocker. It registers the current state with integrity."
        ),
        status="best_next_move",
    )


# ================================================================
# Success Criteria Builders
# ================================================================

def build_success_criteria_a() -> SuccessCriteria:
    """Success criteria for Path A — Circularity Break."""
    return SuccessCriteria(
        path="A",
        criteria=[
            "A visible non-circular route from fast-mode elimination to "
            "the first-order constitutive kernel must be identified",
            "The route must use structures already present in or naturally "
            "extendable from the published GRUT interior sector",
            "The derivation must produce tau dPhi/dt + Phi = X as output, "
            "not assume it as input",
            "The route must not smuggle the first-order form through "
            "a disguised assumption (e.g., assuming a single relaxation "
            "mode a priori)",
            "Success must materially upgrade Q3 from algebraic_grounding "
            "toward derivational_origin",
        ],
        minimum_for_success=(
            "Identify at least one non-circular derivational pathway "
            "that does not assume the first-order form in any step."
        ),
        would_upgrade_from="algebraic_grounding",
        would_upgrade_to="derivational_origin",
        upgrade_is_material=True,
    )


def build_success_criteria_b() -> SuccessCriteria:
    """Success criteria for Path B — Noise/Fluctuation."""
    return SuccessCriteria(
        path="B",
        criteria=[
            "Determine whether a companion noise/fluctuation structure is "
            "formally required by the bath interpretation",
            "Identify any current GRUT structure from which noise content "
            "could be constrained (not merely imported from standard FDT)",
            "If constrained: specify the noise kernel form and identify "
            "what observable it predicts",
            "Must remain inside structured extension — not jump to "
            "speculative horizon or quantum measurement theory",
            "Must materially upgrade the bath interpretation from formal "
            "to physically discriminable",
        ],
        minimum_for_success=(
            "Establish whether FDT-companion noise is a structural "
            "necessity (not merely a desideratum), and identify at least "
            "one GRUT-internal constraint on its form."
        ),
        would_upgrade_from="structural_bath_identification",
        would_upgrade_to="physically_constrainable_bath",
        upgrade_is_material=True,
    )


def build_success_criteria_c() -> SuccessCriteria:
    """Success criteria for Path C — Consolidation."""
    return SuccessCriteria(
        path="C",
        criteria=[
            "Q1-Q3 are coherently registered as a completed phase with "
            "no internal contradictions",
            "All boundaries and nonclaims are explicit",
            "The circularity is acknowledged without pretending it is resolved",
            "The next phase's requirements are clearly identified",
            "No manufactured authority is introduced by the consolidation",
        ],
        minimum_for_success=(
            "A coherent statement of what the recovery/spectral phase "
            "established and what it did not, suitable for document use."
        ),
        would_upgrade_from="three_separate_phase_results",
        would_upgrade_to="consolidated_phase_statement",
        upgrade_is_material=False,
    )


# ================================================================
# Feasibility Audit Builders
# ================================================================

def build_feasibility_a() -> FeasibilityAudit:
    """Feasibility audit for Path A — Circularity Break."""
    return FeasibilityAudit(
        path="A",
        feasibility="likely_premature",
        questions=[
            {
                "q": (
                    "Can the first-order kernel plausibly arise from "
                    "elimination of fast modes already present in the "
                    "published interior sector?"
                ),
                "a": (
                    "No. The published interior sector has three modes: "
                    "one relaxation (memory) and two oscillatory (BDCC). "
                    "The relaxation mode IS the first-order memory law. "
                    "The oscillatory modes are 'system' modes, not 'bath' "
                    "modes that could be eliminated to produce the memory law. "
                    "There are no deeper fast modes to eliminate."
                ),
            },
            {
                "q": (
                    "Is there any evidence beyond algebraic embedding?"
                ),
                "a": (
                    "Partially. The coupling constant 2*alpha*omega_g^2, "
                    "the structural identity omega_0*tau=1, and the damping "
                    "rate are non-circular derived elements. But none of "
                    "these explain WHY the memory law is first-order. They "
                    "describe consequences of coupling a first-order system "
                    "to oscillatory modes."
                ),
            },
            {
                "q": (
                    "Would attempting this now likely produce real derivation, "
                    "or just a dressed-up restatement?"
                ),
                "a": (
                    "Dressed-up restatement. Any derivation that starts from "
                    "the published GRUT equations inherits the first-order "
                    "constitutive law as an axiom. To break the circularity, "
                    "one would need a deeper substrate (e.g., a second-order "
                    "system whose overdamped limit is first-order). The KG "
                    "overdamped limit (Family A in Q1) is such a route, but "
                    "it introduces propagating modes not present in GRUT and "
                    "requires an external damping mechanism."
                ),
            },
            {
                "q": (
                    "What exact structures would be needed to avoid "
                    "circularity?"
                ),
                "a": (
                    "A microscopic second-order (or higher) dynamics for the "
                    "memory field, with an explicit bath coupling that "
                    "provides the damping, and a demonstrable limit in which "
                    "the fast modes are eliminated and the first-order law "
                    "emerges. This requires: (1) a second-order parent "
                    "equation, (2) identified bath DOF providing damping, "
                    "(3) a scale separation argument, (4) an explicit "
                    "elimination procedure."
                ),
            },
            {
                "q": "Are those structures present, missing, or extendable?",
                "a": (
                    "Mostly missing. (1) The KG overdamped limit (Q1 Family A) "
                    "is a candidate parent but introduces new physics. "
                    "(2) Bath DOF are unidentified (Q2 blocker). (3) No scale "
                    "separation has been verified. (4) No elimination procedure "
                    "has been carried out. The CTP/Galley structure (Q1 Family B) "
                    "could in principle accommodate this, but requires the bath "
                    "spectral density as input — which is what we are trying "
                    "to derive."
                ),
            },
        ],
        structures_needed=[
            "Second-order parent dynamics for the memory field",
            "Identified bath DOF providing damping",
            "Verified scale separation (fast bath vs slow memory)",
            "Explicit mode-elimination procedure (Mori-Zwanzig or equivalent)",
        ],
        structures_present=[
            "KG overdamped limit as candidate parent (Q1 Family A)",
            "CTP/Galley formalism as environment framework (Q1 Family B)",
            "Interior linearization with three-pole structure (Q3 Route B)",
        ],
        structures_missing=[
            "Physical identity of bath DOF",
            "Bath spectral density from first principles",
            "Scale separation verification across mass range",
            "Covariant interior metric for gravitational mode spectrum",
        ],
        structures_extendable=[
            "The CTP/Galley ghost field Phi_- could in principle encode "
            "bath fluctuations, but the connection is not established",
            "The KG+Galley combined system (Q1) could provide a parent, "
            "but the golden-ratio growth rate phi/tau complicates it",
        ],
        likely_to_produce_real_derivation=False,
        likely_to_restate_existing=True,
        likely_to_import_external=False,
        summary=(
            "Path A is likely premature. The first-order memory law is the "
            "foundational axiom of GRUT. No visible route exists to derive it "
            "from the published interior sector without either (a) importing "
            "a second-order parent not present in GRUT, or (b) identifying "
            "bath DOF not yet known. Attempting it now would most likely "
            "produce a dressed-up restatement of the algebraic grounding "
            "already achieved in Q3."
        ),
    )


def build_feasibility_b() -> FeasibilityAudit:
    """Feasibility audit for Path B — Noise/Fluctuation."""
    return FeasibilityAudit(
        path="B",
        feasibility="conceptually_required_but_not_ready",
        questions=[
            {
                "q": (
                    "Does a dissipative bath interpretation strongly imply "
                    "companion fluctuation structure?"
                ),
                "a": (
                    "Yes, formally. The fluctuation-dissipation theorem (FDT) "
                    "is a structural consequence of equilibrium statistical "
                    "mechanics: any system with dissipation coupled to a "
                    "thermal bath must have a noise spectrum satisfying "
                    "S(omega) = 2*Im[chi(omega)] * (n_bar(omega) + 1/2) in "
                    "the quantum case, or S(omega) = 2*kT*Im[chi(omega)]/omega "
                    "classically. This is a theorem, not a model choice."
                ),
            },
            {
                "q": (
                    "Is a noise analysis more likely to yield non-circular "
                    "information than another circularity attack?"
                ),
                "a": (
                    "In principle, yes — the noise spectrum is independent "
                    "content not already contained in the dissipation kernel. "
                    "However, applying FDT requires a temperature or energy "
                    "scale, which GRUT does not provide. Without it, the "
                    "noise spectrum is underdetermined up to an overall "
                    "scale factor."
                ),
            },
            {
                "q": (
                    "Is there any visible route to constrain a noise kernel "
                    "from current GRUT response architecture?"
                ),
                "a": (
                    "Marginally. The CTP/Galley structure has a natural noise "
                    "sector: in the doubled-field formalism, the Phi_- "
                    "fluctuations encode the noise kernel via the Hadamard "
                    "propagator G_H = <{Phi_-(x), Phi_-(x')}>/2. But "
                    "computing this requires: (a) specifying the bath state, "
                    "(b) computing loop corrections, (c) defining what "
                    "'temperature' means for the GRUT memory field. None of "
                    "these are currently available."
                ),
            },
            {
                "q": (
                    "Would this remain inside structured extension, or jump "
                    "to speculative horizon?"
                ),
                "a": (
                    "The conditional statement 'IF the bath interpretation is "
                    "physical AND FDT applies, THEN the noise kernel has form "
                    "S(omega) proportional to omega*Omega^2/(omega^2+Omega^2)' "
                    "is structured extension. Actually computing the noise "
                    "from GRUT internals would require speculative horizon "
                    "structures (temperature, quantum state, loop corrections)."
                ),
            },
            {
                "q": (
                    "Would such a program help distinguish formal bath shell "
                    "from physically meaningful bath?"
                ),
                "a": (
                    "Yes, in principle. If noise signatures could be derived "
                    "and tested (e.g., gravitational-wave background residuals, "
                    "BDCC mass-function scatter), this would be the first "
                    "empirical test of the bath interpretation. But no "
                    "concrete testable prediction is currently derivable."
                ),
            },
        ],
        structures_needed=[
            "Temperature or energy scale for the memory sector",
            "CTP noise kernel from Phi_- Hadamard propagator",
            "Bath state specification (thermal? vacuum? other?)",
            "Loop corrections in the doubled-field system",
            "Observable noise signature in GRUT phenomenology",
        ],
        structures_present=[
            "CTP/Galley formalism with Phi_- ghost mode (Q1)",
            "Drude bath spectral density form (Q2)",
            "Dissipation kernel: exponential K(s) = (1/tau)*exp(-s/tau) (canon)",
            "Structural form of FDT noise (standard theory, importable)",
        ],
        structures_missing=[
            "Temperature/energy scale for the memory field",
            "Bath state specification",
            "Loop corrections (Phi_- fluctuations)",
            "Observable noise signatures",
            "Connection between Phi_- fluctuations and physical noise",
        ],
        structures_extendable=[
            "The conditional FDT statement is derivable without new physics: "
            "given the Drude dissipation kernel, FDT constrains the noise "
            "kernel form up to temperature",
            "Route C non-Markov kernel (route_c_nonmarkov_kernel.py) provides "
            "spectral-representable kernel framework that could host noise",
        ],
        likely_to_produce_real_derivation=False,
        likely_to_restate_existing=False,
        likely_to_import_external=True,
        summary=(
            "Path B is conceptually required but not ready. FDT demands "
            "companion noise if the bath is physical — this is formal "
            "necessity, not strategic choice. However, executing a noise "
            "program requires temperature, bath state, and loop corrections "
            "that are all absent. The conditional statement 'IF FDT THEN "
            "noise has Drude form' is derivable but tautological. Any "
            "deeper result requires speculative-horizon structures."
        ),
    )


def build_feasibility_c() -> FeasibilityAudit:
    """Feasibility audit for Path C — Consolidation."""
    return FeasibilityAudit(
        path="C",
        feasibility="feasible_now",
        questions=[
            {
                "q": "Are Paths A and B both too underdetermined right now?",
                "a": (
                    "Yes. Path A has no visible non-circular route. Path B "
                    "requires structures (temperature, bath state, loop "
                    "corrections) not present in current GRUT architecture. "
                    "Neither can be executed with integrity using only the "
                    "published structures."
                ),
            },
            {
                "q": (
                    "Would further immediate probing manufacture false "
                    "authority?"
                ),
                "a": (
                    "Yes. Attempting circularity break without new structures "
                    "would produce dressed-up restatement. Attempting noise "
                    "derivation without temperature would produce imported "
                    "standard results presented as GRUT content. Both would "
                    "manufacture authority the architecture cannot support."
                ),
            },
            {
                "q": (
                    "Is the honest next step consolidation rather than fresh "
                    "extension?"
                ),
                "a": (
                    "Yes. Q1-Q3 form a coherent phase result: parent formalism "
                    "(CTP/Galley) + bath type (Drude/Lorentzian) + algebraic "
                    "grounding (interior PDE). This is a complete "
                    "recovery/spectral phase with acknowledged limitations. "
                    "The next real progress requires new architecture."
                ),
            },
        ],
        structures_needed=[
            "Coherent summary of Q1-Q3 as a phase result",
            "Explicit nonclaims preventing overclaim",
            "Identification of what the next phase requires",
        ],
        structures_present=[
            "Q1 module with recovery shell",
            "Q2 module with bath identification",
            "Q3 module with algebraic grounding",
            "Full test suites for all three phases",
            "Hard blocker inventories at each phase",
            "Safe/unsafe claim registries",
        ],
        structures_missing=[],
        structures_extendable=[],
        likely_to_produce_real_derivation=False,
        likely_to_restate_existing=False,
        likely_to_import_external=False,
        summary=(
            "Path C is feasible now. All structures needed for consolidation "
            "are present. The Q1-Q3 modules provide a complete, tested, and "
            "self-consistent phase result. Consolidation is the honest next "
            "step because neither A nor B can be executed with integrity "
            "using current architecture."
        ),
    )


# ================================================================
# Phase Completion Test Builder
# ================================================================

def build_phase_completion_test() -> PhaseCompletionTest:
    """Determine whether the recovery/spectral phase is complete."""
    return PhaseCompletionTest(
        phase_status="complete_for_consolidation",
        q1_contribution=(
            "Established parent formalism: the constitutive memory law is "
            "a candidate emergent dissipative limit of a CTP/Galley "
            "open-system structure."
        ),
        q2_contribution=(
            "Identified bath type: Drude/Lorentzian self-bath is the "
            "strongest structural match, with the published tau_eff formula "
            "having the exact form of Lorentzian susceptibility."
        ),
        q3_contribution=(
            "Provided algebraic grounding: the interior PDE dispersion "
            "relation explicitly contains the Lorentzian, with non-trivial "
            "coupling and emergent three-pole mode structure."
        ),
        combined_statement=(
            "The published GRUT constitutive memory law tau dPhi/dt + Phi = X "
            "can be interpreted as the dissipative limit of an open-system "
            "structure (Q1) with Drude-type bath character (Q2), algebraically "
            "grounded in the interior PDE sector (Q3). This interpretation is "
            "internally consistent but partially circular (the Lorentzian "
            "follows from the first-order axiom) and does not constitute a "
            "first-principles derivation. All Appendix C blockers remain."
        ),
        circularity_break_required_for_completion=False,
        fluctuation_structure_required_for_completion=False,
        consolidation_sufficient_for_completion=True,
        rationale=(
            "The recovery/spectral phase asks: can the memory law be "
            "interpreted as an emergent dissipative limit with identifiable "
            "spectral structure? Q1-Q3 answer: yes, with caveats. The phase "
            "is complete in the sense that the recovery shell is established, "
            "the bath type is identified, and the grounding is achieved. The "
            "circularity and noise questions belong to the NEXT phase, which "
            "requires new architecture. Demanding circularity break or noise "
            "derivation for phase completion would block indefinitely on "
            "structures that do not yet exist."
        ),
        next_phase_targets=[
            "Circularity break: derive the first-order law from a deeper "
            "substrate (requires second-order parent or identified bath DOF)",
            "Noise/fluctuation structure: derive or constrain companion "
            "noise (requires temperature/energy scale and bath state)",
            "Covariant interior metric: resolve Phase V lapse obstruction "
            "(required for gravitational mode spectrum)",
            "Galley ghost connection: establish Phi_- as physical noise "
            "carrier (requires loop corrections)",
            "Observational signatures: identify testable predictions of "
            "the bath interpretation (requires noise spectrum or mass-"
            "function scatter analysis)",
        ],
    )


# ================================================================
# Hard Blockers After Q4
# ================================================================

def build_hard_blockers_after_q4() -> List[Dict[str, Any]]:
    """Hard blockers surviving through Q4."""
    return [
        {
            "name": "circularity_not_broken",
            "type": "structural",
            "survives_q4": True,
            "q4_update": (
                "Q4 assessed Path A (circularity break) as likely_premature. "
                "No visible non-circular route exists in current architecture."
            ),
        },
        {
            "name": "noise_spectrum_unknown",
            "type": "currently_missing_potentially_extendable",
            "survives_q4": True,
            "q4_update": (
                "Q4 assessed Path B (noise/fluctuation) as "
                "conceptually_required_but_not_ready. FDT demands noise if "
                "bath is physical, but temperature and bath state are missing."
            ),
        },
        {
            "name": "no_born_rule",
            "type": "structural",
            "survives_q4": True,
            "q4_update": "No change. Appendix C boundary.",
        },
        {
            "name": "no_measurement_coupling",
            "type": "structural",
            "survives_q4": True,
            "q4_update": "No change. Appendix C boundary.",
        },
        {
            "name": "no_interference_formalism",
            "type": "structural",
            "survives_q4": True,
            "q4_update": "No change. Appendix C boundary.",
        },
        {
            "name": "no_particle_ontology",
            "type": "structural",
            "survives_q4": True,
            "q4_update": "No change. Appendix C boundary.",
        },
        {
            "name": "no_experiment_framework",
            "type": "structural",
            "survives_q4": True,
            "q4_update": "No change. Appendix C boundary.",
        },
        {
            "name": "spectral_density_not_first_principles",
            "type": "currently_missing_potentially_extendable",
            "survives_q4": True,
            "q4_update": (
                "Unchanged from Q3. Algebraically grounded but not derived."
            ),
        },
        {
            "name": "covariant_interior_metric_missing",
            "type": "structural",
            "survives_q4": True,
            "q4_update": "No change. Phase V obstruction.",
        },
        {
            "name": "loop_corrections_unknown",
            "type": "currently_missing_potentially_extendable",
            "survives_q4": True,
            "q4_update": (
                "Q4 identifies this as prerequisite for Path B (noise). "
                "Phi_- fluctuations encode noise kernel in CTP formalism."
            ),
        },
        {
            "name": "bath_dof_unidentified",
            "type": "currently_missing_potentially_extendable",
            "survives_q4": True,
            "q4_update": (
                "Q4 identifies this as prerequisite for Path A (circularity "
                "break). Physical bath modes are not known."
            ),
        },
        {
            "name": "no_temperature_or_energy_scale",
            "type": "currently_missing_potentially_extendable",
            "survives_q4": True,
            "q4_update": (
                "Q4 identifies this as prerequisite for Path B (noise). "
                "FDT requires temperature; GRUT provides none for "
                "the memory field."
            ),
        },
    ]


# ================================================================
# Document Constraints Builder
# ================================================================

def build_document_constraints() -> DocumentConstraints:
    """Build constraints for any future document summarising Q1-Q4."""
    return DocumentConstraints(
        safe_claims=[
            "The published GRUT constitutive memory law can be interpreted "
            "as a candidate emergent dissipative limit of a CTP/Galley "
            "open-system structure (Q1).",

            "The strongest bath-type candidate is a Drude/Lorentzian self-bath "
            "with the published tau_eff having the exact functional form of "
            "Lorentzian susceptibility (Q2).",

            "The interior PDE dispersion relation explicitly contains the "
            "single-pole Lorentzian as the memory sector's susceptibility, "
            "providing algebraic grounding for the bath-type identification "
            "(Q3).",

            "The grounding is partially circular: the Lorentzian follows from "
            "the first-order constitutive axiom. Non-circular elements include "
            "the coupling constant, three-pole mode structure, structural "
            "identity, and derived damping rates.",

            "Q4 determined that the recovery/spectral phase is complete for "
            "consolidation. The circularity break and noise program are "
            "identified as next-phase targets, not current-phase requirements.",

            "All Appendix C blockers (no amplitudes, Born rule, interference, "
            "measurement, collapse/decoherence, particle ontology) remain "
            "in force throughout Q1-Q4.",
        ],
        unsafe_claims=[
            "The circularity is broken or breakable with current tools.",
            "The bath interpretation is physically validated.",
            "A noise/fluctuation spectrum has been derived.",
            "The first-order memory law is derived from deeper principles.",
            "FDT has been applied or proven within GRUT.",
            "Any Appendix C blocker is resolved.",
            "The recovery/spectral phase constitutes a quantum theory of GRUT.",
            "The bath DOF are identified with specific physical modes.",
            "The temperature of the memory bath is known.",
            "Q1-Q4 prove that GRUT memory has a dissipative origin.",
            "The three-pole spectrum is the complete interior mode content.",
        ],
        strongest_defensible_classification=(
            "Structured extension with acknowledged limitations. Q1-Q3 form "
            "a coherent recovery/spectral phase result: parent formalism "
            "(CTP/Galley) + bath type (Drude) + algebraic grounding (interior "
            "PDE). Q4 closes the phase with explicit nonclaims and identifies "
            "next-phase requirements."
        ),
        q4_framing="phase_completion_audit",
    )


# ================================================================
# Master Builder
# ================================================================

def run_q4_assessment() -> Q4Result:
    """Execute Phase Q4 Fork Audit and Phase-Completion Decision."""

    paths = [build_path_a(), build_path_b(), build_path_c()]

    success_criteria = [
        build_success_criteria_a(),
        build_success_criteria_b(),
        build_success_criteria_c(),
    ]

    feasibility_audits = [
        build_feasibility_a(),
        build_feasibility_b(),
        build_feasibility_c(),
    ]

    phase_completion = build_phase_completion_test()
    hard_blockers = build_hard_blockers_after_q4()
    doc_constraints = build_document_constraints()

    safe_claims = [
        "Q1-Q3 form a coherent recovery/spectral phase: parent formalism "
        "(CTP/Galley) + bath type (Drude/Lorentzian) + algebraic grounding "
        "(interior PDE).",

        "The circularity (first-order axiom -> Lorentzian -> first-order "
        "axiom) is acknowledged and not broken.",

        "Path A (circularity break) is assessed as likely_premature: no "
        "visible non-circular route exists in current architecture.",

        "Path B (noise/fluctuation) is assessed as "
        "conceptually_required_but_not_ready: FDT demands noise if bath "
        "is physical, but temperature and bath state are absent.",

        "Path C (consolidation) is the best next move: Q1-Q3 form a "
        "complete phase result and further probing would manufacture "
        "false authority.",

        "The phase is complete for consolidation. The circularity break "
        "and noise program belong to the next phase.",

        "All Appendix C blockers remain in force.",
    ]

    unsafe_claims = [
        "The circularity can be broken with current tools.",
        "A noise spectrum is derivable from current GRUT architecture.",
        "The bath interpretation is physically validated.",
        "FDT is native to GRUT.",
        "The first-order memory law has been derived.",
        "Any Appendix C blocker is resolved or mitigated.",
        "Q4 introduces new physics or new formal results.",
        "The recovery/spectral phase proves dissipative origin.",
        "Consolidation is equivalent to completion of the quantum program.",
    ]

    nonclaims = [
        "Q4 does NOT break the circularity.",
        "Q4 does NOT derive noise or fluctuation spectra.",
        "Q4 does NOT resolve any Appendix C blocker.",
        "'Phase completion' means the recovery/spectral phase question has "
        "been answered to the extent current architecture permits — not that "
        "the quantum program is complete.",
        "'Consolidation' means honest registration of established results "
        "and explicit identification of open problems.",
        "Q4 is a phase-completion audit, not a derivation or extension.",
        "Path C being 'best next move' reflects feasibility constraints, "
        "not that circularity and noise are unimportant.",
        "The next phase requires new architecture (covariant interior "
        "metric, temperature/energy scale, or deeper substrate theory) "
        "that is not available in current published GRUT.",
    ]

    result = Q4Result(
        executive_determination="path_c_consolidation_best_next_move",
        paths=paths,
        best_path="C",
        best_path_status="best_next_move",
        success_criteria=success_criteria,
        feasibility_audits=feasibility_audits,
        phase_completion=phase_completion,
        hard_blockers_after_q4=hard_blockers,
        safe_claims=safe_claims,
        unsafe_claims=unsafe_claims,
        nonclaims=nonclaims,
        document_constraints=doc_constraints,
        next_phase_recommendation=(
            "The next phase of the Future Quantum Program should target "
            "either (a) circularity break via a deeper substrate theory "
            "from which the first-order law emerges, or (b) noise/fluctuation "
            "structure via identification of temperature/energy scale and "
            "bath state. Both require new architecture not present in the "
            "current published GRUT. The choice between (a) and (b) depends "
            "on which new structure becomes available first: identified bath "
            "DOF would enable (a); a temperature/energy scale would enable (b). "
            "Resolution of the Phase V lapse obstruction (covariant interior "
            "metric) would potentially enable both."
        ),
        q4_classification="phase_completion_audit",
        valid=True,
    )

    _validate_q4(result)
    return result


# ================================================================
# Validation Guard
# ================================================================

def _validate_q4(result: Q4Result) -> None:
    """Validate that Q4 result does not overclaim."""

    # Executive determination must be one of the allowed values
    allowed_executives = {
        "path_a_best_next_move",
        "path_b_best_next_move",
        "path_c_consolidation_best_next_move",
        "alternative_path_best",
    }
    if result.executive_determination not in allowed_executives:
        raise ValueError(
            f"Executive '{result.executive_determination}' not in "
            f"{allowed_executives}"
        )

    # Classification must be one of the allowed values
    allowed_classifications = {
        "fork_decision",
        "phase_completion_audit",
        "structured_extension",
        "speculative_horizon",
        "failure",
    }
    if result.q4_classification not in allowed_classifications:
        raise ValueError(
            f"Classification '{result.q4_classification}' not in "
            f"{allowed_classifications}"
        )

    # Must have at least 3 paths
    if len(result.paths) < 3:
        raise ValueError(
            f"Q4 must evaluate at least 3 paths, got {len(result.paths)}"
        )

    # Exactly one path must be best_next_move
    best_paths = [p for p in result.paths if p.status == "best_next_move"]
    if len(best_paths) != 1:
        raise ValueError(
            f"Exactly one path must be best_next_move, got {len(best_paths)}"
        )

    # The best path must match the executive determination
    if result.best_path == "A" and result.executive_determination != "path_a_best_next_move":
        raise ValueError("best_path=A but executive is not path_a_best_next_move")
    if result.best_path == "B" and result.executive_determination != "path_b_best_next_move":
        raise ValueError("best_path=B but executive is not path_b_best_next_move")
    if result.best_path == "C" and result.executive_determination != "path_c_consolidation_best_next_move":
        raise ValueError("best_path=C but executive is not path_c_consolidation_best_next_move")

    # Forbidden claims check
    for claim in Q4_FORBIDDEN_CLAIMS:
        # Check safe claims don't contain forbidden claims
        for sc in result.safe_claims:
            low = sc.lower()
            if claim == "breaks_circularity" and "circularity is broken" in low:
                raise ValueError(f"Safe claim appears to assert '{claim}'")
            if claim == "derives_noise_spectrum" and "noise spectrum has been derived" in low:
                raise ValueError(f"Safe claim appears to assert '{claim}'")
            if claim == "resolves_appendix_c" and "appendix c blocker is resolved" in low:
                raise ValueError(f"Safe claim appears to assert '{claim}'")

    # Must have nonclaims
    if len(result.nonclaims) < 3:
        raise ValueError(
            f"Q4 must have at least 3 nonclaims, got {len(result.nonclaims)}"
        )

    # Must have hard blockers
    if len(result.hard_blockers_after_q4) < 5:
        raise ValueError(
            f"Q4 must preserve at least 5 hard blockers, got "
            f"{len(result.hard_blockers_after_q4)}"
        )

    # Phase completion must be set
    if result.phase_completion.phase_status == "incomplete_and_blocked":
        # If incomplete, consolidation should not be best path
        if result.best_path == "C":
            raise ValueError(
                "Phase is incomplete_and_blocked but consolidation is "
                "recommended — contradiction."
            )

    # Document constraints must have q4_framing
    allowed_framings = {
        "fork_decision",
        "phase_completion_audit",
        "structured_extension",
        "speculative_horizon",
        "failure",
    }
    if result.document_constraints.q4_framing not in allowed_framings:
        raise ValueError(
            f"Document framing '{result.document_constraints.q4_framing}' "
            f"not in {allowed_framings}"
        )
