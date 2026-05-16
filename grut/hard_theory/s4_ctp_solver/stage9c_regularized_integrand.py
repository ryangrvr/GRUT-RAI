"""Stage 9C regularized integrand scaffold."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage9b_loop_integrand_scaffold import (
    run_stage9b_loop_integrand_scaffold,
)
from grut.hard_theory.s4_ctp_solver.integrand_regularization_scheme import (
    define_integrand_regularization_scheme,
)
from grut.hard_theory.s4_ctp_solver.integrand_regularization_attachment import (
    attach_regularization_to_integrand,
)
from grut.hard_theory.s4_ctp_solver.regularized_integrand_validation import (
    validate_regularized_integrand,
)
from grut.hard_theory.s4_ctp_solver.regularized_integrand_audit import (
    audit_regularized_integrand,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage9c_regularized_integrand() -> Dict[str, object]:
    stage9b = run_stage9b_loop_integrand_scaffold()
    integrand = stage9b.get("integrand", {})
    scheme = define_integrand_regularization_scheme()
    result = attach_regularization_to_integrand(integrand, scheme)
    validation = validate_regularized_integrand(result)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_regularized_integrand({**result, "guard": guard}, validation)

    return {
        "stage": "9C",
        "status": "regularized_integrand_scaffold",
        "regularization_attached": True,
        "integration_performed": False,
        "amplitude_computed": False,
        "can_advance_to_integration_dry_run": audit.get(
            "can_advance_to_integration_dry_run"
        ),
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "stage9b": stage9b,
        "scheme": scheme,
        "result": result,
        "validation": validation,
        "audit": audit,
        "guard": guard,
    }
