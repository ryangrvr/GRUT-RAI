"""Stage 7I convergence control repair attempt."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage7e_tt_regularization import (
    run_stage7e_tt_regularization,
)
from grut.hard_theory.s4_ctp_solver.tt_convergence_metrics import (
    compute_tt_convergence_metrics,
)
from grut.hard_theory.s4_ctp_solver.tt_convergence_thresholds import (
    define_convergence_thresholds,
)
from grut.hard_theory.s4_ctp_solver.tt_convergence_repair import (
    evaluate_convergence_repair,
)
from grut.hard_theory.s4_ctp_solver.tt_convergence_audit import (
    audit_convergence_repair,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage7i_convergence_repair() -> Dict[str, object]:
    stage7e = run_stage7e_tt_regularization()
    metrics = compute_tt_convergence_metrics(stage7e.get("regularized", []))
    thresholds = define_convergence_thresholds()
    repair = evaluate_convergence_repair(metrics, thresholds)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_convergence_repair({**repair, "guard": guard})

    return {
        "stage": "7I",
        "status": "convergence_control_repair_attempt",
        "repair_status": repair.get("repair_status"),
        "convergence_observed": repair.get("convergence_observed"),
        "convergence_proven": False,
        "blocker_closed": False,
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "stage7e": stage7e,
        "metrics": metrics,
        "thresholds": thresholds,
        "repair": repair,
        "audit": audit,
        "guard": guard,
    }
