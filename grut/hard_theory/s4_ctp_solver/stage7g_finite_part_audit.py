"""Stage 7G finite-part eligibility audit."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage7d_tt_diagnostics import (
    run_stage7d_tt_diagnostics,
)
from grut.hard_theory.s4_ctp_solver.stage7e_tt_regularization import (
    run_stage7e_tt_regularization,
)
from grut.hard_theory.s4_ctp_solver.stage7f_tt_renormalization_dry_run import (
    run_stage7f_tt_renormalization_dry_run,
)
from grut.hard_theory.s4_ctp_solver.finite_part_requirements import (
    define_finite_part_requirements,
)
from grut.hard_theory.s4_ctp_solver.finite_part_readiness_checks import (
    evaluate_finite_part_readiness,
)
from grut.hard_theory.s4_ctp_solver.finite_part_blockers import (
    identify_finite_part_blockers,
)
from grut.hard_theory.s4_ctp_solver.finite_part_eligibility_decision import (
    decide_finite_part_eligibility,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage7g_finite_part_audit() -> Dict[str, object]:
    stage7d = run_stage7d_tt_diagnostics()
    stage7e = run_stage7e_tt_regularization()
    stage7f = run_stage7f_tt_renormalization_dry_run()

    requirements = define_finite_part_requirements()
    readiness = evaluate_finite_part_readiness(stage7d, stage7e, stage7f)
    blockers = identify_finite_part_blockers(readiness)
    decision = decide_finite_part_eligibility(readiness, blockers)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())

    return {
        "stage": "7G",
        "status": "finite_part_eligibility_audit",
        "eligible": decision.get("eligible"),
        "readiness_score": readiness.get("readiness_score"),
        "blockers": blockers.get("blockers"),
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "requirements": requirements,
        "readiness": readiness,
        "decision": decision,
        "guard": guard,
    }
