"""Stage 12C R construction legality gate."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.stage11e_cross_partition_finite_consistency import (
    run_stage11e_cross_partition_finite_consistency,
)
from grut.hard_theory.s4_ctp_solver.stage12a_coefficient_assembly_dry_run import (
    run_stage12a_coefficient_assembly_dry_run,
)
from grut.hard_theory.s4_ctp_solver.stage12b_scheme_stability_audit import (
    run_stage12b_scheme_stability_audit,
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
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def _pair_block_reason(pair: Dict[str, object]) -> str:
    return pair.get("reason") or "pair_blocked"


def run_stage12c_r_legality_gate() -> Dict[str, object]:
    stage11e = run_stage11e_cross_partition_finite_consistency()
    stage12a = run_stage12a_coefficient_assembly_dry_run()
    stage12b = run_stage12b_scheme_stability_audit()

    selections = identify_r_candidate_pairs(
        stage12b.get("classifications", {}),
        stage12a.get("registry", {}),
        stage11e,
    )

    candidate_pairs = selections.get("candidate_pairs", [])
    valid_pairs: List[Dict[str, object]] = []
    blocked_pairs: List[Dict[str, object]] = []

    for pair in candidate_pairs:
        if pair.get("selection_status") != "eligible":
            blocked_pairs.append(
                {
                    "pair": pair,
                    "reason": _pair_block_reason(pair),
                    "promotes_claims": False,
                }
            )
            continue

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

    r_legal = bool(valid_pairs)
    blocking_reason = "none" if r_legal else "no_valid_pairs"
    if not r_legal and blocked_pairs:
        blocking_reason = blocked_pairs[0].get("reason") or blocking_reason

    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())

    return {
        "stage": "12C",
        "status": "r_legality_gate",
        "candidate_pairs": candidate_pairs,
        "valid_pairs": valid_pairs,
        "blocked_pairs": blocked_pairs,
        "r_legal": r_legal,
        "blocking_reason": blocking_reason,
        "can_compute_c_final": False,
        "can_compute_c_cosmo": False,
        "can_compute_r": False,
        "can_extract": False,
        "promotes_claims": False,
        "stage11e": stage11e,
        "stage12a": stage12a,
        "stage12b": stage12b,
        "guard": guard,
    }
