"""Stage P4 protected kernel integration bridge."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.stage_p2_nonlocal_kernel_derivation import (
    run_stage_p2_nonlocal_kernel_derivation,
)
from grut.hard_theory.s4_ctp_solver.stage_p3_nonlocal_form_construction import (
    run_stage_p3_nonlocal_form_construction,
)
from grut.hard_theory.s4_ctp_solver.nonlocal_kernel_integration import (
    integrate_nonlocal_kernels,
)
from grut.hard_theory.s4_ctp_solver.integrated_kernel_acceptance import (
    evaluate_integrated_candidate,
)


def run_stage_p4_protected_kernel_integration() -> Dict[str, object]:
    stage_p2 = run_stage_p2_nonlocal_kernel_derivation()
    stage_p3 = run_stage_p3_nonlocal_form_construction()

    integrated = integrate_nonlocal_kernels(stage_p2, stage_p3)

    integrated_candidates: List[Dict[str, object]] = []
    remaining_failures: List[Dict[str, object]] = []

    for entry in integrated:
        evaluated = evaluate_integrated_candidate(entry)
        integrated_candidates.append(evaluated)
        acceptance = evaluated.get("acceptance", {})
        remaining_failures.append(
            {
                "source_type": evaluated.get("source_type"),
                "failures": acceptance.get("failures", []),
                "promotes_claims": False,
            }
        )

    return {
        "stage": "P4",
        "status": "protected_kernel_integration_bridge",
        "integrated_candidates": integrated_candidates,
        "remaining_failures": remaining_failures,
        "protected_source_derived": False,
        "r_computation_allowed": False,
        "rerun_scheme_stability_recommended": False,
        "promotes_claims": False,
        "stage_p2": stage_p2,
        "stage_p3": stage_p3,
    }
