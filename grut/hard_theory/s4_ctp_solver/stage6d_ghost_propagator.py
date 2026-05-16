"""Stage 6D ghost propagator closure subproblem."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.s4_ghost_operator import define_ghost_operator
from grut.hard_theory.s4_ctp_solver.s4_ghost_propagator import (
    build_ghost_propagator_structure,
)
from grut.hard_theory.s4_ctp_solver.ghost_propagator_validation import (
    validate_ghost_propagator,
)
from grut.hard_theory.s4_ctp_solver.ghost_propagator_blocker_update import (
    update_ghost_blocker_status,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage6d_ghost_propagator() -> Dict[str, object]:
    operator = define_ghost_operator()
    propagator = build_ghost_propagator_structure(operator)
    validation = validate_ghost_propagator(propagator, operator)
    blocker_update = update_ghost_blocker_status()
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())

    return {
        "stage": "6D",
        "status": "ghost_propagator_closure_partial",
        "ghost_operator_defined": True,
        "ghost_structure_built": True,
        "validated": validation["status"] == "structural_validated",
        "overall_full_s4_propagator_blocker_closed": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "operator": operator,
        "propagator": propagator,
        "validation": validation,
        "blocker_update": blocker_update,
        "guard": guard,
    }
