"""Stage 6C scalar propagator closure subproblem."""

from typing import Dict, List

import sympy as sp

from grut.hard_theory.s4_ctp_solver.s4_scalar_propagator_closed_form import (
    build_conformal_scalar_propagator_closed_form,
)
from grut.hard_theory.s4_ctp_solver.scalar_propagator_validation import (
    validate_conformal_scalar_propagator,
    compare_spectral_to_closed_form,
)
from grut.hard_theory.s4_ctp_solver.scalar_propagator_convergence import (
    diagnose_scalar_spectral_convergence,
)
from grut.hard_theory.s4_ctp_solver.scalar_propagator_blocker_update import (
    update_full_s4_propagator_blocker_scalar_only,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage6c_scalar_propagator() -> Dict[str, object]:
    record = build_conformal_scalar_propagator_closed_form()
    validation = validate_conformal_scalar_propagator(record)

    radius = sp.symbols("a", positive=True)
    l_max_values: List[int] = [2, 4, 6]
    comparison = compare_spectral_to_closed_form(l_max_values, radius)
    convergence = diagnose_scalar_spectral_convergence(l_max_values)
    blocker_update = update_full_s4_propagator_blocker_scalar_only()

    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())

    return {
        "stage": "6C",
        "status": "scalar_propagator_closure_partial",
        "scalar_conformal_closed_form": True,
        "spectral_comparison_run": True,
        "convergence_proven": False,
        "overall_full_s4_propagator_blocker_closed": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "record": record,
        "validation": validation,
        "comparison": comparison,
        "convergence": convergence,
        "blocker_update": blocker_update,
        "guard": guard,
    }
