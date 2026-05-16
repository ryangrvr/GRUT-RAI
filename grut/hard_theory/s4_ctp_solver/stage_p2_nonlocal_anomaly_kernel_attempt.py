"""Stage P2 nonlocal anomaly kernel derivation attempt."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage_p1_nonlocal_anomaly_source_plan import (
    run_stage_p1_nonlocal_anomaly_source_plan,
)
from grut.hard_theory.s4_ctp_solver.stageN2_imaginary_causal_sector_audit import (
    run_stageN2_imaginary_causal_sector_audit,
)
from grut.hard_theory.s4_ctp_solver.nonlocal_anomaly_kernel_attempt import (
    attempt_nonlocal_anomaly_kernel,
)


def run_stage_p2_nonlocal_anomaly_kernel_attempt() -> Dict[str, object]:
    stage_p1 = run_stage_p1_nonlocal_anomaly_source_plan()
    stageN2 = run_stageN2_imaginary_causal_sector_audit()

    attempt = attempt_nonlocal_anomaly_kernel(stageN2)

    return {
        "stage": "P2",
        "status": "nonlocal_anomaly_kernel_derivation_attempt",
        "kernel_found": attempt.get("kernel_found"),
        "kernel_candidates": attempt.get("kernel_candidates", []),
        "missing_reasons": attempt.get("missing_reasons", []),
        "acceptance_tests_remaining": stage_p1.get("acceptance_tests", []),
        "protected_source_derived": False,
        "r_computation_allowed": False,
        "next_required_action": "derive_nonlocal_anomaly_kernel",
        "promotes_claims": False,
        "stage_p1": stage_p1,
        "stageN2": stageN2,
    }
