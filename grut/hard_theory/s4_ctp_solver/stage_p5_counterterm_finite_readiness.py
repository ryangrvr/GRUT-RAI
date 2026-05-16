"""Stage P5 counterterm nonmixing and finite-isolation readiness."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.stage_p4_protected_kernel_integration import (
    run_stage_p4_protected_kernel_integration,
)
from grut.hard_theory.s4_ctp_solver.stage11b_subtraction_dry_run import (
    run_stage11b_subtraction_dry_run,
)
from grut.hard_theory.s4_ctp_solver.stage3d_scheme_audit import (
    run_stage3d_scheme_audit,
)
from grut.hard_theory.s4_ctp_solver.stage7f_tt_renormalization_dry_run import (
    run_stage7f_tt_renormalization_dry_run,
)
from grut.hard_theory.s4_ctp_solver.stage11c_finite_part_benchmark_gate import (
    run_stage11c_finite_part_benchmark_gate,
)
from grut.hard_theory.s4_ctp_solver.kernel_counterterm_overlap import (
    evaluate_counterterm_overlap,
)
from grut.hard_theory.s4_ctp_solver.kernel_nonmixing_check import (
    check_counterterm_nonmixing,
)
from grut.hard_theory.s4_ctp_solver.kernel_finite_extractability import (
    evaluate_finite_extractability,
)
from grut.hard_theory.s4_ctp_solver.kernel_p5_acceptance import (
    evaluate_p5_acceptance,
)

_TARGETS = {
    "Im_log_minus_box_i_epsilon",
    "R_log_box_R",
    "Weyl_log_box_Weyl",
}


def run_stage_p5_counterterm_finite_readiness() -> Dict[str, object]:
    stage_p4 = run_stage_p4_protected_kernel_integration()
    stage11b = run_stage11b_subtraction_dry_run()
    stage3d = run_stage3d_scheme_audit()
    stage7f = run_stage7f_tt_renormalization_dry_run()
    stage11c = run_stage11c_finite_part_benchmark_gate()

    integrated = stage_p4.get("integrated_candidates", [])

    readiness_candidates: List[Dict[str, object]] = []
    blocked_kernels: List[Dict[str, object]] = []

    for entry in integrated:
        if entry.get("source_type") not in _TARGETS:
            continue

        candidate = entry.get("candidate", {})
        overlap = evaluate_counterterm_overlap(candidate)
        nonmixing = check_counterterm_nonmixing(candidate, overlap, stage11b, stage7f, stage3d)
        finite = evaluate_finite_extractability(candidate, nonmixing, stage11c)
        acceptance = evaluate_p5_acceptance(candidate, nonmixing, finite, False)

        record = {
            "source_type": entry.get("source_type"),
            "candidate": candidate,
            "overlap": overlap,
            "nonmixing": nonmixing,
            "finite_extractability": finite,
            "acceptance": acceptance,
            "promotes_claims": False,
        }

        if acceptance.get("accepted_readiness"):
            readiness_candidates.append(record)
        else:
            blocked_kernels.append(record)

    return {
        "stage": "P5",
        "status": "counterterm_nonmixing_finite_readiness",
        "kernels_checked": len(readiness_candidates) + len(blocked_kernels),
        "readiness_candidates": readiness_candidates,
        "blocked_kernels": blocked_kernels,
        "protected_source_derived": False,
        "r_computation_allowed": False,
        "rerun_p2_recommended": bool(readiness_candidates),
        "promotes_claims": False,
        "stage_p4": stage_p4,
        "stage11b": stage11b,
        "stage3d": stage3d,
        "stage7f": stage7f,
        "stage11c": stage11c,
    }
