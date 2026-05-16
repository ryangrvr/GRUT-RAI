"""Stage 7A scalar spectral inversion benchmark on S4."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.s4_scalar_propagator_closed_form import (
    build_conformal_scalar_propagator_closed_form,
)
from grut.hard_theory.s4_ctp_solver.scalar_inversion_engine import (
    run_scalar_inversion_engine,
)
from grut.hard_theory.s4_ctp_solver.scalar_inversion_comparison import (
    compare_to_closed_form,
)
from grut.hard_theory.s4_ctp_solver.scalar_inversion_audit import (
    audit_scalar_inversion,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage7a_scalar_inversion() -> Dict[str, object]:
    l_values: List[int] = [5, 10, 20, 50]
    inversion = run_scalar_inversion_engine(l_values)
    closed_form = build_conformal_scalar_propagator_closed_form()
    comparison = compare_to_closed_form(inversion["results"], closed_form)
    audit_input = {
        **inversion,
        "convergence_observed": comparison["convergence_observed"],
    }
    audit = audit_scalar_inversion(audit_input)

    can_apply_to_tt = (
        comparison["convergence_observed"]
        and comparison["agreement"] == "converging"
    )

    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())

    return {
        "stage": "7A",
        "status": "scalar_inversion_benchmark",
        "inversion_performed": True,
        "tt_inversion_performed": False,
        "convergence_observed": comparison["convergence_observed"],
        "convergence_proven": False,
        "can_apply_to_tt": can_apply_to_tt,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "inversion": inversion,
        "comparison": comparison,
        "audit": audit,
        "guard": guard,
    }
