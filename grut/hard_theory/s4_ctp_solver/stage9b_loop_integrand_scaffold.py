"""Stage 9B loop integrand assembly scaffold."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage9a_propagator_attachment import (
    run_stage9a_propagator_attachment,
)
from grut.hard_theory.s4_ctp_solver.loop_integrand_components import (
    build_loop_integrand_components,
)
from grut.hard_theory.s4_ctp_solver.loop_integrand_assembly import (
    assemble_loop_integrand_scaffold,
)
from grut.hard_theory.s4_ctp_solver.loop_integrand_validation import (
    validate_loop_integrand_scaffold,
)
from grut.hard_theory.s4_ctp_solver.loop_integrand_audit import (
    audit_loop_integrand_scaffold,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage9b_loop_integrand_scaffold() -> Dict[str, object]:
    stage9a = run_stage9a_propagator_attachment()
    components = build_loop_integrand_components(stage9a)
    integrand = assemble_loop_integrand_scaffold(components)
    validation = validate_loop_integrand_scaffold(integrand)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_loop_integrand_scaffold({**integrand, "guard": guard}, validation)

    integrand_valid = validation.get("status") == "valid_integrand_scaffold"

    return {
        "stage": "9B",
        "status": "loop_integrand_scaffold",
        "integrand_valid": integrand_valid,
        "integration_performed": False,
        "propagators_evaluated": False,
        "amplitude_computed": False,
        "can_advance_to_regularized_integrand": audit.get(
            "can_advance_to_regularized_integrand"
        ),
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "stage9a": stage9a,
        "components": components,
        "integrand": integrand,
        "integrand_summary": integrand.get("integrand_summary"),
        "validation": validation,
        "audit": audit,
        "guard": guard,
    }
