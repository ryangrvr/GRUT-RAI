"""Stage 8C controlled fragment contractions."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.tt_local_contraction_fragments import (
    define_local_contraction_fragments,
)
from grut.hard_theory.s4_ctp_solver.tt_controlled_fragment import (
    define_controlled_tensor_fragment,
)
from grut.hard_theory.s4_ctp_solver.tt_fragment_contraction_engine import (
    run_controlled_fragment_contraction,
)
from grut.hard_theory.s4_ctp_solver.tt_fragment_contraction_validation import (
    validate_controlled_fragment_contraction,
)
from grut.hard_theory.s4_ctp_solver.tt_fragment_contraction_audit import (
    audit_controlled_fragment_contraction,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage8c_controlled_fragment_contractions() -> Dict[str, object]:
    local_fragments = define_local_contraction_fragments()
    fragment = define_controlled_tensor_fragment()
    result = run_controlled_fragment_contraction(fragment)
    validation = validate_controlled_fragment_contraction(result)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_controlled_fragment_contraction({**result, "guard": guard}, validation)

    controlled_fragment_valid = validation.get("status") == "valid_fragment"

    return {
        "stage": "8C",
        "status": "controlled_fragment_contraction_partial",
        "controlled_fragment_valid": controlled_fragment_valid,
        "full_contractions_performed": False,
        "can_advance_to_single_diagram_skeleton": audit.get(
            "can_advance_to_single_diagram_skeleton"
        ),
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "local_fragments": local_fragments,
        "fragment": fragment,
        "result": result,
        "validation": validation,
        "audit": audit,
        "guard": guard,
    }
