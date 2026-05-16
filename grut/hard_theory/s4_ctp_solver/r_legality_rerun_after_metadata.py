"""Re-run scheme stability and R legality after metadata completion."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.coefficient_scheme_classifier import (
    classify_coefficient_candidates,
)
from grut.hard_theory.s4_ctp_solver.scheme_stability_rules import (
    define_scheme_stability_rules,
)
from grut.hard_theory.s4_ctp_solver.scheme_stability_audit import (
    audit_scheme_stability,
)
from grut.hard_theory.s4_ctp_solver.r_candidate_selector import (
    identify_r_candidate_pairs,
)
from grut.hard_theory.s4_ctp_solver.r_structure_compatibility import (
    check_r_structure_compatibility,
)
from grut.hard_theory.s4_ctp_solver.r_cancellation_check import check_r_cancellation
from grut.hard_theory.s4_ctp_solver.r_legality_audit import (
    audit_r_legality_inputs,
)
from grut.hard_theory.s4_ctp_solver.r_legality_decision import decide_r_legality


def rerun_legality_after_metadata(
    stage12c_r3: Dict[str, object],
) -> Dict[str, object]:
    metadata_completed = stage12c_r3.get("metadata_completed") is True
    registry = stage12c_r3.get("registry", {})
    stage12c_r2 = stage12c_r3.get("stage12c_r2", {})
    stage11e = stage12c_r2.get("stage11e", {})

    if not metadata_completed:
        return {
            "metadata_completed": False,
            "candidate_pairs_examined": 0,
            "valid_pairs": [],
            "blocked_pairs": [],
            "r_legal": False,
            "remaining_blockers": ["metadata_incomplete"],
            "r_computation_allowed": False,
            "next_required_action": "repair_remaining_legality_blockers",
            "promotes_claims": False,
        }

    classifications = classify_coefficient_candidates(registry)
    rules = define_scheme_stability_rules()
    scheme_audit = audit_scheme_stability(classifications, rules)

    selections = identify_r_candidate_pairs(classifications, registry, stage11e)
    candidate_pairs = selections.get("candidate_pairs", [])

    valid_pairs: List[Dict[str, object]] = []
    blocked_pairs: List[Dict[str, object]] = []

    for pair in candidate_pairs:
        structural = check_r_structure_compatibility(pair)
        cancellation = check_r_cancellation(pair)
        audit = audit_r_legality_inputs(pair, structural, cancellation)
        decision = decide_r_legality(pair, structural, cancellation, audit)

        if decision.get("r_legal"):
            valid_pairs.append(
                {
                    "pair": pair,
                    "structural": structural,
                    "cancellation": cancellation,
                    "audit": audit,
                    "decision": decision,
                    "promotes_claims": False,
                }
            )
        else:
            blocked_pairs.append(
                {
                    "pair": pair,
                    "structural": structural,
                    "cancellation": cancellation,
                    "audit": audit,
                    "decision": decision,
                    "reason": decision.get("reason"),
                    "promotes_claims": False,
                }
            )

    remaining_blockers = {item.get("reason") for item in blocked_pairs if item.get("reason")}
    if scheme_audit.get("all_r_inputs_stable") is False:
        remaining_blockers.add("scheme_stability_failed")

    remaining_blockers_list = sorted(remaining_blockers)
    r_legal = bool(valid_pairs)

    return {
        "metadata_completed": True,
        "candidate_pairs_examined": len(candidate_pairs),
        "valid_pairs": valid_pairs,
        "blocked_pairs": blocked_pairs,
        "r_legal": r_legal,
        "remaining_blockers": remaining_blockers_list,
        "r_computation_allowed": False,
        "next_required_action": "run_stage12d_controlled_symbolic_attempt"
        if r_legal
        else "repair_remaining_legality_blockers",
        "promotes_claims": False,
        "classifications": classifications,
        "scheme_audit": scheme_audit,
    }
