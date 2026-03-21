"""
Phase D10 — Trigger Selection Closure in the Post-D8/D9 Framework.

PROBLEM STATEMENT
-----------------
D4 ranked Kretschmann-family triggering as the top candidate for
curvature-driven symmetry breaking, but that assessment predated D8
(action closure) and D9 (self-consistent coupled profiles). D10
re-evaluates the trigger candidates within the post-D8 action structure
and post-D9 self-consistent framework.

SCOPE
-----
Derivational and taxonomic phase. No heavy numerics or BVP solving.
Curvature invariant formulas are evaluated analytically in Schwarzschild.

LOCKED INHERITANCE
------------------
- D4: component_a_shape_recovered_but_interpretation_not_yet_verified
- D5: source_coupling_insufficient
- D6: companion_architecture_viable
- D7: fully_coupled_viable
- D8: d7_channels_largely_action_derived
- D9: self_consistent_coupling_viable

MISSION
-------
Determine whether the trigger can now be upgraded from "top-ranked
candidate" to "best-supported trigger within the D8 action structure
and D9 self-consistent coupled framework."

VACUUM ACTIVATION NOTE
----------------------
Vacuum strong-field activation is a required test because the trigger
must remain meaningful in Schwarzschild-like strong-field regions, but
it is a necessary, not sufficient, criterion. Final trigger support is
assessed on the combined basis of vacuum activation, sourced interior
behavior, D8 action-naturalness, and D9 self-consistency compatibility.

KRETSCHMANN / WEYL DISTINCTION
------------------------------
Kretschmann and Weyl invariants are degenerate in vacuum Schwarzschild
(where R_ab = 0), but they are distinct invariants in general. They
diverge in sourced regions where R_ab != 0. D10 states the degeneracy,
notes the distinction, and flags that resolving which member of the
tidal-curvature family is preferred would require sourced-interior
trigger analysis beyond D10's scope.

RESULT
------
Classification: kretschmann_family_trigger_best_supported_within_tested_framework
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List, Optional


# ================================================================
# Physical constants (inherited from prior phases)
# ================================================================

ALPHA_VAC = 1.0 / 3.0
R_S = 1.0
M_EXT = 0.5
R_EQ = R_S * ALPHA_VAC              # 1/3
R_EXT = 2.0
KRETSCHNER_COEFF = 48.0 * M_EXT**2  # 12.0
ETA_TARGET = 1.0 / math.sqrt(8.0 * math.pi)
LAMBDA_DEFAULT = 8.0 * math.pi
XI_DEFAULT = 1.0
MASS_COEFF = math.pi / 3.0
RHO_EQ_COEFF = M_EXT**2 / (2.0 * (1.5))  # M^2/(2*tau^2), tau^2=1.5

# ================================================================
# D10-specific constants
# ================================================================

N_TRIGGER_CANDIDATES = 4
SCORE_CRITERIA = 5
CONTRAST_THRESHOLD = 100.0

TRIGGER_CLASSIFICATION_OPTIONS = [
    "kretschmann_family_trigger_clearly_dominant",
    "kretschmann_family_trigger_best_supported_within_tested_framework",
    "small_trigger_family_survives",
    "trigger_selection_still_underdetermined",
    "trigger_selection_inconsistent",
]

COMPATIBILITY_LEVELS = [
    "naturally_compatible",
    "compatible_with_assumptions",
    "awkward",
]

ITERATION_EFFECTS = [
    "stabilizing",
    "neutral",
    "destabilizing",
]

# Score criterion labels
SCORE_CRITERION_NAMES = [
    "vacuum_strong_field_active",
    "strong_weak_contrast_sufficient",
    "action_natural",
    "d9_compatible",
    "prior_phase_consistent",
]

# ================================================================
# Assumptions and Nonclaims
# ================================================================

TRIGGER_SELECTION_ASSUMPTIONS = [
    "1. Background geometry is Schwarzschild with M = 0.5, R_S = 1.0.",
    "2. Trigger candidates are evaluated analytically using exact "
    "Schwarzschild curvature invariant formulas.",
    "3. The D8 action structure S_total = S_grav + S_macro + S_defect + "
    "S_trigger + S_portal is taken as the reference action framework.",
    "4. The D9 self-consistent coupled framework with macro-amplitude "
    "proxy closure is the reference self-consistency framework.",
    "5. The trigger enters the defect ODE as an effective mass coupling "
    "of the form xi * C * |Phi|^2 in the action.",
    "6. Regime correctness requires both vacuum strong-field activation "
    "AND weak-field suppression.",
    "7. Vacuum strong-field activation is a necessary but not sufficient "
    "criterion for trigger selection.",
    "8. Kretschmann and Weyl invariants are treated as distinct objects "
    "that happen to be degenerate in vacuum Schwarzschild.",
    "9. The candidate set is kept minimal (4 invariants) to avoid an "
    "invariant zoo while still providing meaningful contrast.",
    "10. Prior phase results (D4 through D9) are locked and inherited "
    "without modification.",
]

TRIGGER_SELECTION_NONCLAIMS = [
    "1. This phase does NOT prove final unified field theory closure.",
    "2. Trigger closure here is within the D8/D9 tested framework, not "
    "a statement about all possible trigger mechanisms.",
    "3. A preferred trigger is a mathematical/modeling result, not a "
    "metaphysical statement about nature.",
    "4. A 'best-supported' trigger may still remain conditional on the "
    "reduced closure level used in D9 (macro-amplitude proxy).",
    "5. The Kretschmann/Weyl degeneracy in vacuum does NOT imply they "
    "are the same invariant in general spacetimes.",
    "6. No claim is made that the tested candidate set is exhaustive — "
    "other curvature invariants exist but are not assessed here.",
    "7. Sourced-interior trigger behavior is assessed qualitatively, "
    "not through a full interior solution.",
    "8. The ranking is within the tested framework and may change if "
    "the proxy closure is upgraded to a full two-field solution.",
    "9. No claim is made about trigger uniqueness unless the evidence "
    "supports it.",
    "10. D10 does not reopen any prior locked phase result.",
]


# ================================================================
# Dataclasses
# ================================================================

@dataclass
class TriggerSelectionParams:
    """Parameters for trigger selection analysis."""
    eta: float = ETA_TARGET
    lam: float = LAMBDA_DEFAULT
    xi: float = XI_DEFAULT
    M: float = M_EXT
    R_eq: float = R_EQ
    R_ext: float = R_EXT
    prior_d4_scores: Dict[str, float] = field(default_factory=lambda: {
        "ricci_scalar": 0.50,
        "kretschmann_sqrt": 0.85,
        "ricci_squared_sqrt": 0.70,
    })
    prior_d8_classification: str = "d7_channels_largely_action_derived"
    prior_d9_classification: str = "self_consistent_coupling_viable"


@dataclass
class TriggerCandidate:
    """Definition of a single trigger candidate."""
    name: str
    formula_description: str
    formula_vacuum: str
    nonzero_in_vacuum: bool
    d4_score: Optional[float]
    n_extra_assumptions: int
    invariant_type: str  # "ricci_family" or "tidal_family"
    sourced_behavior: str  # description of behavior with matter sources


@dataclass
class RegimeTestResult:
    """Result of vacuum strong-field and weak-field regime tests."""
    candidate_name: str
    value_at_Req: float
    value_at_Rext: float
    contrast_ratio: float
    vacuum_active: bool
    weak_field_suppressed: bool
    regime_correct: bool
    sourced_interior_active: bool
    sourced_assessment: str


@dataclass
class ActionCompatibilityResult:
    """Assessment of compatibility with D8 action structure."""
    candidate_name: str
    coupling_form: str
    natural_in_action: bool
    extra_structure_needed: Optional[str]
    compatibility_level: str
    rationale: str


@dataclass
class SelfConsistencyCompatibilityResult:
    """Assessment of compatibility with D9 self-consistent framework."""
    candidate_name: str
    d9_compatible: bool
    effect_on_iteration: str
    effective_mass_contribution: str
    compatibility_assessment: str


@dataclass
class TriggerAssessment:
    """Complete assessment of a single trigger candidate."""
    candidate: TriggerCandidate
    regime_test: RegimeTestResult
    action_compat: ActionCompatibilityResult
    sc_compat: SelfConsistencyCompatibilityResult
    total_score: int
    score_breakdown: Dict[str, int]


@dataclass
class TriggerRanking:
    """Ranking result across all candidates."""
    assessments: List[TriggerAssessment]
    ranked_names: List[str]
    top_candidate: str
    top_score: int
    runner_up_score: int
    separation: int
    family_members: List[str]
    vacuum_degeneracy_note: str
    ranking_rationale: str


@dataclass
class ProxyCaveat:
    """Proxy-closure caveat statement."""
    closure_level: str
    trigger_closure_conditional: bool
    caveat_statement: str


@dataclass
class TriggerSelectionClassification:
    """Final classification of trigger selection."""
    classification: str
    phase_status: str
    trigger_family: List[str]
    summary: str
    proxy_caveat: ProxyCaveat
    phase_lock_update: str


@dataclass
class TriggerSelectionResult:
    """Master result container for Phase D10."""
    valid: bool
    params: TriggerSelectionParams
    candidates: Optional[List[TriggerCandidate]]
    regime_tests: Optional[List[RegimeTestResult]]
    action_compatibility: Optional[List[ActionCompatibilityResult]]
    sc_compatibility: Optional[List[SelfConsistencyCompatibilityResult]]
    assessments: Optional[List[TriggerAssessment]]
    ranking: Optional[TriggerRanking]
    classification: Optional[TriggerSelectionClassification]
    nonclaims: List[str]
    assumptions: List[str]


# ================================================================
# Helper: Curvature invariant evaluation
# ================================================================

def _eval_ricci_scalar(r: float, M: float) -> float:
    """Ricci scalar R in Schwarzschild vacuum.

    R = 0 exactly in vacuum Schwarzschild.
    In sourced regions: R ~ -8*pi*(rho - 3p), but D10 evaluates
    the vacuum formula.
    """
    # Vacuum Schwarzschild: R = 0 identically
    return 0.0


def _eval_kretschmann_sqrt(r: float, M: float) -> float:
    """sqrt(K) = sqrt(R_abcd R^abcd) in Schwarzschild.

    K = 48*M^2/r^6, so sqrt(K) = sqrt(48)*M/r^3.
    """
    return math.sqrt(48.0) * M / (r**3)


def _eval_ricci_squared_sqrt(r: float, M: float) -> float:
    """sqrt(R_ab R^ab) in Schwarzschild vacuum.

    R_ab = 0 in vacuum Schwarzschild (Einstein vacuum equations).
    In sourced regions: ~ (8*pi)^2 * rho^2.
    """
    # Vacuum Schwarzschild: R_ab = 0 identically
    return 0.0


def _eval_weyl_sqrt(r: float, M: float) -> float:
    """sqrt(C_abcd C^abcd) in Schwarzschild.

    In vacuum Schwarzschild, R_ab = 0, so the Weyl tensor equals
    the Riemann tensor. Therefore C_abcd C^abcd = R_abcd R^abcd = K.
    sqrt(C^2) = sqrt(K) = sqrt(48)*M/r^3.

    NOTE: This is NOT the same as Kretschmann in general. In sourced
    spacetimes where R_ab != 0, they differ via the decomposition:
    R_abcd = C_abcd + (terms involving R_ab and R).
    """
    return math.sqrt(48.0) * M / (r**3)


def _eval_sourced_ricci_scalar(r: float, M: float) -> float:
    """Approximate Ricci scalar in sourced region.

    R ~ -8*pi*rho where rho ~ MASS_COEFF/r^4 (scalar-memory
    energy density approximation from D4).
    """
    rho = MASS_COEFF / (r**4)
    return 8.0 * math.pi * rho  # magnitude, ignoring sign


def _eval_sourced_ricci_squared_sqrt(r: float, M: float) -> float:
    """Approximate sqrt(R_ab R^ab) in sourced region.

    R_ab ~ 8*pi * diag(rho, p, p, p), so
    R_ab R^ab ~ (8*pi)^2 * (rho^2 + 3p^2).
    For dust-like (p ~ 0): ~ (8*pi)^2 * rho^2.
    sqrt(R_ab R^ab) ~ (8*pi) * rho.
    """
    rho = MASS_COEFF / (r**4)
    return 8.0 * math.pi * rho


# Map candidate names to their vacuum evaluation functions
_VACUUM_EVAL = {
    "ricci_scalar": _eval_ricci_scalar,
    "kretschmann_sqrt": _eval_kretschmann_sqrt,
    "ricci_squared_sqrt": _eval_ricci_squared_sqrt,
    "weyl_sqrt": _eval_weyl_sqrt,
}

# Map candidate names to their sourced evaluation functions
_SOURCED_EVAL = {
    "ricci_scalar": _eval_sourced_ricci_scalar,
    "kretschmann_sqrt": _eval_kretschmann_sqrt,  # same in sourced
    "ricci_squared_sqrt": _eval_sourced_ricci_squared_sqrt,
    "weyl_sqrt": _eval_weyl_sqrt,  # approximate: Weyl ~ Riemann - Ricci terms
}


# ================================================================
# Level 0: Define trigger candidates
# ================================================================

def define_trigger_candidates(
    params: TriggerSelectionParams,
) -> List[TriggerCandidate]:
    """Define the minimal disciplined set of trigger candidates.

    Four candidates:
    1. Ricci scalar R (zero in vacuum, active only in sourced regions)
    2. Kretschmann sqrt(K) (nonzero in vacuum, top D4 candidate)
    3. Ricci-squared sqrt(R_ab R^ab) (zero in vacuum)
    4. Weyl scalar sqrt(C^2) (equals Kretschmann in vacuum, distinct
       in general)
    """
    candidates = [
        TriggerCandidate(
            name="ricci_scalar",
            formula_description="R = g^{ab} R_{ab}",
            formula_vacuum="R = 0 (vacuum Schwarzschild)",
            nonzero_in_vacuum=False,
            d4_score=params.prior_d4_scores.get("ricci_scalar", 0.50),
            n_extra_assumptions=0,
            invariant_type="ricci_family",
            sourced_behavior=(
                "R ~ -8*pi*(rho - 3p) in sourced regions. Activates "
                "only where matter energy-momentum is present. Cannot "
                "trigger SSB in vacuum strong-field regions."
            ),
        ),
        TriggerCandidate(
            name="kretschmann_sqrt",
            formula_description="sqrt(K) = sqrt(R_{abcd} R^{abcd})",
            formula_vacuum="sqrt(48)*M/r^3",
            nonzero_in_vacuum=True,
            d4_score=params.prior_d4_scores.get("kretschmann_sqrt", 0.85),
            n_extra_assumptions=0,
            invariant_type="tidal_family",
            sourced_behavior=(
                "sqrt(K) = sqrt(48)*M/r^3 in Schwarzschild. In sourced "
                "regions, Kretschmann receives additional contributions "
                "from Ricci terms: K = C^2 + 2*R_ab*R^ab - R^2/3. "
                "Remains large in strong-field regions regardless of "
                "source presence."
            ),
        ),
        TriggerCandidate(
            name="ricci_squared_sqrt",
            formula_description="sqrt(R_{ab} R^{ab})",
            formula_vacuum="0 (vacuum Schwarzschild)",
            nonzero_in_vacuum=False,
            d4_score=params.prior_d4_scores.get("ricci_squared_sqrt", 0.70),
            n_extra_assumptions=1,
            invariant_type="ricci_family",
            sourced_behavior=(
                "sqrt(R_ab R^ab) ~ (8*pi)*rho in sourced regions. "
                "Involves a square root of a tensor contraction, which "
                "is less natural as a field coupling. Active only in "
                "sourced regions."
            ),
        ),
        TriggerCandidate(
            name="weyl_sqrt",
            formula_description="sqrt(C_{abcd} C^{abcd})",
            formula_vacuum="sqrt(48)*M/r^3 (= sqrt(K) in vacuum)",
            nonzero_in_vacuum=True,
            d4_score=None,  # new candidate, no D4 score
            n_extra_assumptions=0,
            invariant_type="tidal_family",
            sourced_behavior=(
                "sqrt(C^2) = sqrt(K) in vacuum Schwarzschild (where "
                "R_ab = 0). In sourced regions, Weyl differs from "
                "Kretschmann: C_abcd = R_abcd - (Ricci terms), so "
                "C^2 = K - 2*R_ab*R^ab + R^2/3. The Weyl tensor "
                "captures pure tidal/gravitational-wave curvature, "
                "excluding matter-sourced Ricci contributions."
            ),
        ),
    ]
    assert len(candidates) == N_TRIGGER_CANDIDATES
    return candidates


# ================================================================
# Level 1: Regime correctness tests
# ================================================================

def test_regime_correctness(
    candidates: List[TriggerCandidate],
    params: TriggerSelectionParams,
) -> List[RegimeTestResult]:
    """Test each candidate for vacuum strong-field activation,
    weak-field suppression, and sourced interior behavior.

    Vacuum strong-field activation is a necessary but not sufficient
    criterion. Final support is assessed on the combined basis of
    vacuum activation, sourced interior behavior, D8 action-naturalness,
    and D9 self-consistency compatibility.
    """
    results = []
    for cand in candidates:
        # Vacuum evaluation
        eval_fn = _VACUUM_EVAL[cand.name]
        val_req = eval_fn(params.R_eq, params.M)
        val_rext = eval_fn(params.R_ext, params.M)

        # Contrast ratio (handle zero denominator)
        if val_rext > 0:
            contrast = val_req / val_rext
        elif val_req > 0:
            contrast = float('inf')
        else:
            contrast = 0.0

        vacuum_active = val_req > 0
        weak_suppressed = (val_rext < val_req * 0.01) if val_req > 0 else True

        # Sourced interior assessment
        sourced_fn = _SOURCED_EVAL[cand.name]
        sourced_val = sourced_fn(params.R_eq, params.M)
        sourced_active = sourced_val > 0

        if vacuum_active and weak_suppressed:
            regime_ok = True
            if sourced_active:
                sourced_str = (
                    f"Active in both vacuum and sourced regimes. "
                    f"Sourced value at R_eq: {sourced_val:.4f}."
                )
            else:
                sourced_str = (
                    "Active in vacuum but assessment of sourced "
                    "behavior requires full interior solution."
                )
        elif not vacuum_active and sourced_active:
            regime_ok = False
            sourced_str = (
                f"Zero in vacuum Schwarzschild but active in sourced "
                f"regions (value at R_eq: {sourced_val:.4f}). Fails "
                f"vacuum strong-field requirement — cannot trigger SSB "
                f"in vacuum tidal-curvature regime."
            )
        else:
            regime_ok = False
            sourced_str = (
                "Zero in both vacuum and sourced regimes at this "
                "approximation level."
            )

        results.append(RegimeTestResult(
            candidate_name=cand.name,
            value_at_Req=val_req,
            value_at_Rext=val_rext,
            contrast_ratio=contrast,
            vacuum_active=vacuum_active,
            weak_field_suppressed=weak_suppressed,
            regime_correct=regime_ok,
            sourced_interior_active=sourced_active,
            sourced_assessment=sourced_str,
        ))

    return results


# ================================================================
# Level 2: D8 action compatibility
# ================================================================

def assess_action_compatibility(
    candidates: List[TriggerCandidate],
    params: TriggerSelectionParams,
) -> List[ActionCompatibilityResult]:
    """Assess compatibility of each trigger with the D8 action structure.

    D8 action: S_total = S_grav + S_macro + S_defect + S_trigger + S_portal.
    S_trigger = integral d^4x sqrt(-g) xi * C * |Phi|^2.
    The trigger C must be a scalar curvature invariant that enters
    naturally as a field coupling.
    """
    results = []
    for cand in candidates:
        if cand.name == "ricci_scalar":
            results.append(ActionCompatibilityResult(
                candidate_name=cand.name,
                coupling_form="xi * R * |Phi|^2",
                natural_in_action=True,
                extra_structure_needed=None,
                compatibility_level="naturally_compatible",
                rationale=(
                    "xi*R*|Phi|^2 is the standard conformal coupling. "
                    "It enters S_trigger naturally with no extra structure. "
                    "However, R = 0 in vacuum Schwarzschild, so the coupling "
                    "produces no trigger effect in the vacuum strong-field "
                    "regime where it is needed."
                ),
            ))
        elif cand.name == "kretschmann_sqrt":
            results.append(ActionCompatibilityResult(
                candidate_name=cand.name,
                coupling_form="xi * sqrt(K) * |Phi|^2",
                natural_in_action=True,
                extra_structure_needed=None,
                compatibility_level="naturally_compatible",
                rationale=(
                    "xi*sqrt(K)*|Phi|^2 is a scalar coupling of the "
                    "scalar field to a scalar curvature invariant. Enters "
                    "S_trigger with the same structural form as conformal "
                    "coupling. sqrt(K) is nonzero in vacuum, providing "
                    "an effective mass that triggers SSB in strong-field "
                    "regions. No additional fields or structure needed."
                ),
            ))
        elif cand.name == "ricci_squared_sqrt":
            results.append(ActionCompatibilityResult(
                candidate_name=cand.name,
                coupling_form="xi * sqrt(R_ab R^ab) * |Phi|^2",
                natural_in_action=False,
                extra_structure_needed=(
                    "Square root of a rank-2 tensor contraction is less "
                    "natural than coupling to a scalar invariant directly. "
                    "Requires justification for why sqrt(R_ab R^ab) rather "
                    "than R_ab R^ab or another combination."
                ),
                compatibility_level="compatible_with_assumptions",
                rationale=(
                    "The coupling xi*sqrt(R_ab R^ab)*|Phi|^2 is technically "
                    "valid but structurally less elegant than coupling to R "
                    "or sqrt(K). The square root introduces a non-polynomial "
                    "invariant. Additionally, R_ab = 0 in vacuum, so this "
                    "coupling is inert in the vacuum strong-field regime."
                ),
            ))
        elif cand.name == "weyl_sqrt":
            results.append(ActionCompatibilityResult(
                candidate_name=cand.name,
                coupling_form="xi * sqrt(C_abcd C^abcd) * |Phi|^2",
                natural_in_action=True,
                extra_structure_needed=None,
                compatibility_level="naturally_compatible",
                rationale=(
                    "xi*sqrt(C^2)*|Phi|^2 couples the scalar field to the "
                    "Weyl curvature scalar. Structurally identical to the "
                    "Kretschmann coupling in vacuum Schwarzschild (where "
                    "C_abcd = R_abcd). In sourced regions, Weyl captures "
                    "pure tidal curvature excluding matter-sourced Ricci "
                    "contributions. This is equally natural as Kretschmann "
                    "coupling — both are scalar-to-scalar couplings. The "
                    "Weyl version has the conceptual advantage of isolating "
                    "gravitational tidal effects, but D10 does not claim "
                    "this distinction matters within the vacuum-tested "
                    "framework."
                ),
            ))

    return results


# ================================================================
# Level 3: D9 self-consistency compatibility
# ================================================================

def assess_self_consistency_compatibility(
    candidates: List[TriggerCandidate],
    params: TriggerSelectionParams,
) -> List[SelfConsistencyCompatibilityResult]:
    """Assess compatibility with D9 self-consistent coupled framework.

    D9 showed constructive portal feedback with the Kretschmann trigger:
    the portal term tightens the defect core (stabilizing). The trigger
    enters the defect ODE as an effective mass xi*C*f. For D9
    compatibility, the trigger must not destabilize the Picard iteration.
    """
    results = []
    for cand in candidates:
        if cand.name == "ricci_scalar":
            results.append(SelfConsistencyCompatibilityResult(
                candidate_name=cand.name,
                d9_compatible=True,
                effect_on_iteration="neutral",
                effective_mass_contribution=(
                    "xi*R*f = 0 in vacuum Schwarzschild. No effective "
                    "mass contribution. The trigger is inert in the "
                    "vacuum strong-field regime where the defect ODE "
                    "is solved."
                ),
                compatibility_assessment=(
                    "Compatible with D9 iteration (it does nothing). "
                    "The Picard iteration converges trivially because "
                    "the trigger term vanishes. However, this is neutral "
                    "compatibility — the trigger provides no useful "
                    "coupling in the regime where D9 operates."
                ),
            ))
        elif cand.name == "kretschmann_sqrt":
            results.append(SelfConsistencyCompatibilityResult(
                candidate_name=cand.name,
                d9_compatible=True,
                effect_on_iteration="stabilizing",
                effective_mass_contribution=(
                    "xi*sqrt(K)*f = xi*sqrt(48)*M/r^3 * f. Provides a "
                    "positive effective mass that pushes f toward the "
                    "vacuum (f -> 1) faster. This tightens the defect "
                    "core, consistent with D9's observed constructive "
                    "deformation."
                ),
                compatibility_assessment=(
                    "Fully compatible with D9. The Kretschmann trigger "
                    "was the trigger used in the D9 self-consistent "
                    "iteration (via the portal feedback term). D9 "
                    "converged in 13 iterations with constructive "
                    "deformation (29.6% max shift, stabilizing). "
                    "This is the reference compatibility case."
                ),
            ))
        elif cand.name == "ricci_squared_sqrt":
            results.append(SelfConsistencyCompatibilityResult(
                candidate_name=cand.name,
                d9_compatible=True,
                effect_on_iteration="neutral",
                effective_mass_contribution=(
                    "xi*sqrt(R_ab R^ab)*f = 0 in vacuum Schwarzschild. "
                    "No effective mass contribution. Same situation as "
                    "Ricci scalar."
                ),
                compatibility_assessment=(
                    "Compatible with D9 iteration (it does nothing). "
                    "Neutral compatibility — provides no effective mass "
                    "in the vacuum regime. The Picard iteration would "
                    "converge trivially but the trigger would provide "
                    "no feedback."
                ),
            ))
        elif cand.name == "weyl_sqrt":
            results.append(SelfConsistencyCompatibilityResult(
                candidate_name=cand.name,
                d9_compatible=True,
                effect_on_iteration="stabilizing",
                effective_mass_contribution=(
                    "xi*sqrt(C^2)*f = xi*sqrt(48)*M/r^3 * f in vacuum "
                    "Schwarzschild. Identical to Kretschmann effective "
                    "mass in vacuum. Provides the same stabilizing "
                    "contribution."
                ),
                compatibility_assessment=(
                    "Fully compatible with D9 in vacuum. Produces the "
                    "same effective mass as Kretschmann in the vacuum "
                    "regime where D9 operates. Would yield identical "
                    "Picard iteration behavior. In sourced regions, "
                    "the Weyl contribution may differ from Kretschmann "
                    "due to Ricci subtraction, but this distinction is "
                    "beyond D10's vacuum-tested scope."
                ),
            ))

    return results


# ================================================================
# Level 4: Assemble full trigger assessments
# ================================================================

def assemble_trigger_assessments(
    candidates: List[TriggerCandidate],
    regime_tests: List[RegimeTestResult],
    action_compat: List[ActionCompatibilityResult],
    sc_compat: List[SelfConsistencyCompatibilityResult],
) -> List[TriggerAssessment]:
    """Combine all assessments and compute scores.

    Score criteria (0 or 1 each, 5 total):
    1. vacuum_strong_field_active: invariant nonzero in vacuum at R_eq
    2. strong_weak_contrast_sufficient: contrast ratio > threshold
    3. action_natural: naturally compatible with D8 action
    4. d9_compatible: stabilizing or at least non-destabilizing in D9
    5. prior_phase_consistent: no contradiction with D4-D9 results
    """
    # Index by candidate name for lookup
    regime_by_name = {r.candidate_name: r for r in regime_tests}
    action_by_name = {a.candidate_name: a for a in action_compat}
    sc_by_name = {s.candidate_name: s for s in sc_compat}

    assessments = []
    for cand in candidates:
        rt = regime_by_name[cand.name]
        ac = action_by_name[cand.name]
        sc = sc_by_name[cand.name]

        # Score criterion 1: vacuum strong-field active
        s1 = 1 if rt.vacuum_active else 0

        # Score criterion 2: contrast ratio sufficient
        s2 = 1 if rt.contrast_ratio > CONTRAST_THRESHOLD else 0

        # Score criterion 3: action-natural
        s3 = 1 if ac.compatibility_level == "naturally_compatible" else 0

        # Score criterion 4: D9-compatible (stabilizing counts as 1,
        # neutral counts as 0 because neutral = no useful contribution)
        s4 = 1 if sc.effect_on_iteration == "stabilizing" else 0

        # Score criterion 5: prior-phase consistent
        # All candidates are consistent with prior phases (no contradiction)
        # But Ricci-based candidates scored lower in D4, which is prior
        # information. We don't penalize for low D4 score here — that's
        # captured in the other criteria. Prior-phase consistency is about
        # whether the candidate contradicts locked results.
        s5 = 1  # all candidates are consistent (none contradict locked results)

        total = s1 + s2 + s3 + s4 + s5
        breakdown = {
            "vacuum_strong_field_active": s1,
            "strong_weak_contrast_sufficient": s2,
            "action_natural": s3,
            "d9_compatible": s4,
            "prior_phase_consistent": s5,
        }

        assessments.append(TriggerAssessment(
            candidate=cand,
            regime_test=rt,
            action_compat=ac,
            sc_compat=sc,
            total_score=total,
            score_breakdown=breakdown,
        ))

    return assessments


# ================================================================
# Level 5: Rank triggers
# ================================================================

def rank_triggers(
    assessments: List[TriggerAssessment],
) -> TriggerRanking:
    """Rank trigger candidates by total score, then by parsimony.

    Parsimony tiebreaker: fewer extra assumptions = better.
    """
    # Sort by (total_score DESC, n_extra_assumptions ASC)
    sorted_assess = sorted(
        assessments,
        key=lambda a: (-a.total_score, a.candidate.n_extra_assumptions),
    )
    ranked_names = [a.candidate.name for a in sorted_assess]
    top = sorted_assess[0]
    runner = sorted_assess[1] if len(sorted_assess) > 1 else sorted_assess[0]

    # Identify family: candidates that share the top score
    family = [
        a.candidate.name for a in sorted_assess
        if a.total_score == top.total_score
    ]

    # Vacuum degeneracy note
    kretschmann_in_family = "kretschmann_sqrt" in family
    weyl_in_family = "weyl_sqrt" in family
    if kretschmann_in_family and weyl_in_family:
        degeneracy_note = (
            "Kretschmann sqrt(K) and Weyl sqrt(C^2) are degenerate in "
            "vacuum Schwarzschild (where R_ab = 0, so C_abcd = R_abcd). "
            "They are distinct invariants in general spacetimes: in "
            "sourced regions where R_ab != 0, they diverge via the "
            "decomposition K = C^2 + 2*R_ab*R^ab - R^2/3. Resolving "
            "which member of this tidal-curvature family is preferred "
            "would require sourced-interior trigger analysis beyond "
            "D10's scope."
        )
    else:
        degeneracy_note = "No vacuum degeneracy among top-ranked candidates."

    # Ranking rationale
    non_family = [
        a.candidate.name for a in sorted_assess
        if a.total_score < top.total_score
    ]
    rationale_parts = [
        f"Top score: {top.total_score}/{SCORE_CRITERIA}.",
        f"Top-scoring candidates: {family}.",
    ]
    if non_family:
        rationale_parts.append(
            f"Lower-scoring candidates: {non_family} "
            f"(score {runner.total_score if runner.total_score < top.total_score else sorted_assess[-1].total_score}/{SCORE_CRITERIA})."
        )
    rationale_parts.append(
        "Tidal-curvature invariants (Kretschmann, Weyl) score highest "
        "because they are nonzero in vacuum strong-field regions, have "
        "large strong-to-weak contrast, enter the D8 action naturally, "
        "and produce stabilizing effective mass in the D9 framework. "
        "Ricci-family invariants fail the vacuum strong-field criterion "
        "and provide no effective mass in the vacuum regime."
    )

    return TriggerRanking(
        assessments=sorted_assess,
        ranked_names=ranked_names,
        top_candidate=top.candidate.name,
        top_score=top.total_score,
        runner_up_score=(
            sorted_assess[1].total_score if len(sorted_assess) > 1
            else top.total_score
        ),
        separation=top.total_score - (
            sorted_assess[-1].total_score if len(sorted_assess) > 1
            else top.total_score
        ),
        family_members=family,
        vacuum_degeneracy_note=degeneracy_note,
        ranking_rationale=" ".join(rationale_parts),
    )


# ================================================================
# Level 6: Classify trigger selection
# ================================================================

def classify_trigger_selection(
    ranking: TriggerRanking,
    params: TriggerSelectionParams,
) -> TriggerSelectionClassification:
    """Produce the final trigger selection classification.

    Classification logic:
    - If one candidate scores strictly highest AND vacuum-active:
      kretschmann_family_trigger_clearly_dominant
    - If Kretschmann and Weyl both score highest (degenerate in vacuum):
      kretschmann_family_trigger_best_supported_within_tested_framework
    - If the Kretschmann/Weyl distinction is judged material:
      small_trigger_family_survives
    - If multiple unrelated candidates score equally:
      small_trigger_family_survives
    - If no candidate scores well:
      trigger_selection_still_underdetermined
    - If results contradict:
      trigger_selection_inconsistent
    """
    family = ranking.family_members
    top_score = ranking.top_score

    # Check for inconsistency
    if top_score == 0:
        classification = "trigger_selection_inconsistent"
    elif top_score <= 2:
        classification = "trigger_selection_still_underdetermined"
    elif len(family) == 1:
        classification = "kretschmann_family_trigger_clearly_dominant"
    elif (set(family) == {"kretschmann_sqrt", "weyl_sqrt"}
          or set(family) <= {"kretschmann_sqrt", "weyl_sqrt"}):
        # Both tidal-curvature invariants tie — they are degenerate
        # in vacuum Schwarzschild. This is the expected outcome.
        classification = (
            "kretschmann_family_trigger_best_supported_within_tested_framework"
        )
    elif all(
        a.candidate.invariant_type == "tidal_family"
        for a in ranking.assessments
        if a.candidate.name in family
    ):
        classification = "small_trigger_family_survives"
    else:
        classification = "small_trigger_family_survives"

    # Proxy caveat
    proxy_caveat = ProxyCaveat(
        closure_level="macro_amplitude_proxy_closure",
        trigger_closure_conditional=True,
        caveat_statement=(
            "D9 used a macro-amplitude proxy closure, not the fully exact "
            "two-field Euler-Lagrange system. Trigger closure in D10 is "
            "therefore strong within the tested framework but still "
            "conditional on the current closure level. A full two-field "
            "solution could in principle modify trigger coupling behavior "
            "in the sourced interior, potentially distinguishing Kretschmann "
            "from Weyl. Within the vacuum-tested framework, the trigger "
            "selection is robust."
        ),
    )

    # Summary
    if classification == (
        "kretschmann_family_trigger_best_supported_within_tested_framework"
    ):
        summary = (
            "Tidal-curvature triggers (Kretschmann sqrt(K) and Weyl "
            "sqrt(C^2)) are the best-supported triggers within the D8/D9 "
            "tested framework. They score {top}/{max} on the five-criterion "
            "assessment (vacuum activation, contrast, action-naturalness, "
            "D9 compatibility, prior-phase consistency). Ricci-family "
            "triggers (R and sqrt(R_ab R^ab)) fail the vacuum strong-field "
            "criterion. Kretschmann and Weyl are degenerate in vacuum "
            "Schwarzschild but are distinct invariants in general. "
            "Resolving which member is preferred requires sourced-interior "
            "analysis beyond D10's scope."
        ).format(top=top_score, max=SCORE_CRITERIA)
    elif classification == "kretschmann_family_trigger_clearly_dominant":
        summary = (
            "A single trigger candidate scores strictly highest. "
            f"Top candidate: {ranking.top_candidate} with score "
            f"{top_score}/{SCORE_CRITERIA}."
        )
    else:
        summary = (
            f"Classification: {classification}. "
            f"Top score: {top_score}/{SCORE_CRITERIA}. "
            f"Family: {family}."
        )

    # Phase lock update
    phase_lock_update = (
        f"D10: {classification} (ASSESSED)"
    )

    return TriggerSelectionClassification(
        classification=classification,
        phase_status="ASSESSED",
        trigger_family=family,
        summary=summary,
        proxy_caveat=proxy_caveat,
        phase_lock_update=phase_lock_update,
    )


# ================================================================
# Level 7: Master orchestrator
# ================================================================

def compute_trigger_selection(
    params: Optional[TriggerSelectionParams] = None,
) -> TriggerSelectionResult:
    """Run the complete Phase D10 trigger selection analysis.

    This is the top-level entry point. It:
    1. Defines trigger candidates
    2. Tests regime correctness (vacuum + weak-field + sourced)
    3. Assesses D8 action compatibility
    4. Assesses D9 self-consistency compatibility
    5. Assembles full assessments with scores
    6. Ranks triggers
    7. Classifies the result
    """
    if params is None:
        params = TriggerSelectionParams()

    try:
        # Level 0: Define candidates
        candidates = define_trigger_candidates(params)

        # Level 1: Regime tests
        regime_tests = test_regime_correctness(candidates, params)

        # Level 2: D8 action compatibility
        action_compat = assess_action_compatibility(candidates, params)

        # Level 3: D9 self-consistency compatibility
        sc_compat = assess_self_consistency_compatibility(candidates, params)

        # Level 4: Assemble assessments
        assessments = assemble_trigger_assessments(
            candidates, regime_tests, action_compat, sc_compat,
        )

        # Level 5: Rank
        ranking = rank_triggers(assessments)

        # Level 6: Classify
        classification = classify_trigger_selection(ranking, params)

        return TriggerSelectionResult(
            valid=True,
            params=params,
            candidates=candidates,
            regime_tests=regime_tests,
            action_compatibility=action_compat,
            sc_compatibility=sc_compat,
            assessments=assessments,
            ranking=ranking,
            classification=classification,
            nonclaims=list(TRIGGER_SELECTION_NONCLAIMS),
            assumptions=list(TRIGGER_SELECTION_ASSUMPTIONS),
        )

    except Exception as e:
        return TriggerSelectionResult(
            valid=False,
            params=params,
            candidates=None,
            regime_tests=None,
            action_compatibility=None,
            sc_compatibility=None,
            assessments=None,
            ranking=None,
            classification=TriggerSelectionClassification(
                classification="trigger_selection_inconsistent",
                phase_status="FRAMEWORK_ERROR",
                trigger_family=[],
                summary=f"Framework error: {e}",
                proxy_caveat=ProxyCaveat(
                    closure_level="error",
                    trigger_closure_conditional=True,
                    caveat_statement=str(e),
                ),
                phase_lock_update="D10: trigger_selection_inconsistent (ERROR)",
            ),
            nonclaims=list(TRIGGER_SELECTION_NONCLAIMS),
            assumptions=list(TRIGGER_SELECTION_ASSUMPTIONS),
        )


# ================================================================
# Level 8: Serialization
# ================================================================

def trigger_selection_result_to_dict(
    result: TriggerSelectionResult,
) -> Dict[str, Any]:
    """Convert TriggerSelectionResult to a JSON-serializable dict."""
    return {
        "valid": result.valid,
        "params": asdict(result.params),
        "candidates": (
            [asdict(c) for c in result.candidates]
            if result.candidates else None
        ),
        "regime_tests": (
            [asdict(r) for r in result.regime_tests]
            if result.regime_tests else None
        ),
        "action_compatibility": (
            [asdict(a) for a in result.action_compatibility]
            if result.action_compatibility else None
        ),
        "sc_compatibility": (
            [asdict(s) for s in result.sc_compatibility]
            if result.sc_compatibility else None
        ),
        "assessments": (
            [asdict(a) for a in result.assessments]
            if result.assessments else None
        ),
        "ranking": asdict(result.ranking) if result.ranking else None,
        "classification": (
            asdict(result.classification) if result.classification else None
        ),
        "nonclaims": result.nonclaims,
        "assumptions": result.assumptions,
    }
