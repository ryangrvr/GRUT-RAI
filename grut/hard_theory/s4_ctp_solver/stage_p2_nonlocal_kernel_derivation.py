"""Stage P2 nonlocal anomaly kernel derivation attempt."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.stage_p1_nonlocal_anomaly_source_plan import (
    run_stage_p1_nonlocal_anomaly_source_plan,
)
from grut.hard_theory.s4_ctp_solver.stageN2_imaginary_causal_sector_audit import (
    run_stageN2_imaginary_causal_sector_audit,
)
from grut.hard_theory.s4_ctp_solver.stage9c_regularized_integrand import (
    run_stage9c_regularized_integrand,
)
from grut.hard_theory.s4_ctp_solver.stage11b_subtraction_dry_run import (
    run_stage11b_subtraction_dry_run,
)
from grut.hard_theory.s4_ctp_solver.stage12g_r_route_terminal_audit import (
    run_stage12g_r_route_terminal_audit,
)
from grut.hard_theory.s4_ctp_solver.nonlocal_kernel_targets import (
    define_nonlocal_kernel_targets,
)
from grut.hard_theory.s4_ctp_solver.nonlocal_kernel_symbolic_derivation import (
    attempt_symbolic_derivation,
)
from grut.hard_theory.s4_ctp_solver.kernel_regulator_cancellation import (
    check_regulator_cancellation,
)
from grut.hard_theory.s4_ctp_solver.kernel_ward_ctp_consistency import (
    check_ward_ctp_consistency,
)
from grut.hard_theory.s4_ctp_solver.nonlocal_kernel_acceptance import (
    evaluate_kernel_acceptance,
)


def run_stage_p2_nonlocal_kernel_derivation() -> Dict[str, object]:
    stage_p1 = run_stage_p1_nonlocal_anomaly_source_plan()
    stageN2 = run_stageN2_imaginary_causal_sector_audit()
    stage9c = run_stage9c_regularized_integrand()
    stage11b = run_stage11b_subtraction_dry_run()
    stage12g = run_stage12g_r_route_terminal_audit()

    targets = define_nonlocal_kernel_targets()
    derived = attempt_symbolic_derivation(targets, stageN2)

    regulator_check = check_regulator_cancellation(stage9c, stage11b)

    accepted_kernels: List[Dict[str, object]] = []
    failed_kernels: List[Dict[str, object]] = []

    for target, candidate in zip(targets, derived):
        causal_required = bool(target.get("causal_structure_required"))
        ward_ctp = check_ward_ctp_consistency(stage12g, stageN2, causal_required)
        acceptance = evaluate_kernel_acceptance(candidate, regulator_check, ward_ctp)
        entry = {
            "source_type": target.get("source_type"),
            "candidate": candidate,
            "regulator_check": regulator_check,
            "ward_ctp_check": ward_ctp,
            "acceptance": acceptance,
            "promotes_claims": False,
        }
        if acceptance.get("accepted"):
            accepted_kernels.append(entry)
        else:
            failed_kernels.append(entry)

    protected_source_derived = bool(accepted_kernels)

    return {
        "stage": "P2",
        "status": "nonlocal_anomaly_kernel_derivation_attempt",
        "kernels_attempted": len(targets),
        "accepted_kernels": accepted_kernels,
        "failed_kernels": failed_kernels,
        "protected_source_derived": protected_source_derived,
        "r_computation_allowed": False,
        "rerun_scheme_stability_recommended": protected_source_derived,
        "promotes_claims": False,
        "stage_p1": stage_p1,
        "stageN2": stageN2,
        "stage9c": stage9c,
        "stage11b": stage11b,
        "stage12g": stage12g,
    }
