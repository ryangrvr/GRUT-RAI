"""Stage 9A propagator symbolic attachment layer."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage8d_diagram_skeleton import (
    run_stage8d_diagram_skeleton,
)
from grut.hard_theory.s4_ctp_solver.propagator_attachment_registry import (
    build_propagator_attachment_registry,
)
from grut.hard_theory.s4_ctp_solver.skeleton_propagator_attachment import (
    attach_propagators_to_skeleton,
)
from grut.hard_theory.s4_ctp_solver.propagator_attachment_validation import (
    validate_propagator_attachments,
)
from grut.hard_theory.s4_ctp_solver.propagator_attachment_audit import (
    audit_propagator_attachment,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage9a_propagator_attachment() -> Dict[str, object]:
    stage8d = run_stage8d_diagram_skeleton()
    skeleton = stage8d.get("skeleton", {})
    registry = build_propagator_attachment_registry()
    attachment_result = attach_propagators_to_skeleton(skeleton, registry)
    validation = validate_propagator_attachments(attachment_result)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_propagator_attachment({**attachment_result, "guard": guard}, validation)

    attachments_valid = validation.get("status") == "valid_attachment"

    return {
        "stage": "9A",
        "status": "propagator_symbolic_attachment",
        "attachments_valid": attachments_valid,
        "propagators_evaluated": False,
        "loops_evaluated": False,
        "can_advance_to_loop_integrand_assembly": audit.get(
            "can_advance_to_loop_integrand_assembly"
        ),
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "stage8d": stage8d,
        "registry": registry,
        "attachment_result": attachment_result,
        "validation": validation,
        "audit": audit,
        "guard": guard,
    }
