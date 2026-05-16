"""Stage P8 R legality rerun with protected kernel candidates."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.stage_p7_protected_scheme_injection import (
    run_stage_p7_protected_scheme_injection,
)
from grut.hard_theory.s4_ctp_solver.stage_p5_counterterm_finite_readiness import (
    run_stage_p5_counterterm_finite_readiness,
)
from grut.hard_theory.s4_ctp_solver.stage_p4_protected_kernel_integration import (
    run_stage_p4_protected_kernel_integration,
)
from grut.hard_theory.s4_ctp_solver.stage12b_scheme_stability_audit import (
    run_stage12b_scheme_stability_audit,
)
from grut.hard_theory.s4_ctp_solver.protected_pair_selector import (
    select_protected_pairs,
)
from grut.hard_theory.s4_ctp_solver.protected_pair_structure_check import (
    check_protected_pair_structure,
)
from grut.hard_theory.s4_ctp_solver.protected_pair_cancellation_readiness import (
    assess_protected_pair_cancellation_readiness,
)
from grut.hard_theory.s4_ctp_solver.protected_pair_legality_audit import (
    audit_protected_pair_legality,
)


def run_stage_p8_r_legality_with_protected_kernels() -> Dict[str, object]:
    stage_p7 = run_stage_p7_protected_scheme_injection()
    stage_p5 = run_stage_p5_counterterm_finite_readiness()
    stage_p4 = run_stage_p4_protected_kernel_integration()
    stage12b = run_stage12b_scheme_stability_audit()

    stage_p6 = stage_p7.get("stage_p6", {})
    pairs = select_protected_pairs(stage_p7, stage_p6)

    valid_pairs: List[Dict[str, object]] = []
    blocked_pairs: List[Dict[str, object]] = []

    for pair in pairs:
        structure = check_protected_pair_structure(pair, stage_p4, stage_p5)
        cancellation = assess_protected_pair_cancellation_readiness(pair, structure)
        audit = audit_protected_pair_legality(
            pair, stage_p7.get("scheme_protected_candidates", [])
        )

        entry = {
            "pair": pair,
            "structure": structure,
            "cancellation": cancellation,
            "audit": audit,
            "promotes_claims": False,
        }

        if (
            structure.get("status") == "pass"
            and cancellation.get("cancellation_ready") is True
            and audit.get("status") == "pass"
        ):
            valid_pairs.append(entry)
        else:
            blocked_pairs.append(entry)

    r_legal = bool(valid_pairs)
    next_action = "run_controlled_symbolic_r_attempt" if r_legal else "repair_pair_legality"

    return {
        "stage": "P8",
        "status": "r_legality_with_protected_kernels",
        "candidate_pairs_examined": len(pairs),
        "valid_pairs": valid_pairs,
        "blocked_pairs": blocked_pairs,
        "r_legal": r_legal,
        "r_computation_allowed": False,
        "next_required_action": next_action,
        "promotes_claims": False,
        "stage_p7": stage_p7,
        "stage_p5": stage_p5,
        "stage_p4": stage_p4,
        "stage12b": stage12b,
    }
