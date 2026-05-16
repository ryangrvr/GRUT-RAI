"""Stage 8A controlled tensor contraction sandbox."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage7k_tensor_contraction_repair import (
    run_stage7k_tensor_contraction_repair,
)
from grut.hard_theory.s4_ctp_solver.tt_sandbox_rules import (
    define_sandbox_contraction_rules,
)
from grut.hard_theory.s4_ctp_solver.tt_sandbox_contractions import (
    run_minimal_sandbox_contractions,
)
from grut.hard_theory.s4_ctp_solver.tt_sandbox_results import (
    validate_sandbox_results,
)
from grut.hard_theory.s4_ctp_solver.tt_sandbox_audit import (
    audit_tensor_contraction_sandbox,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage8a_tensor_contraction_sandbox() -> Dict[str, object]:
    stage7k = run_stage7k_tensor_contraction_repair()
    rules = define_sandbox_contraction_rules()
    results = run_minimal_sandbox_contractions()
    validation = validate_sandbox_results(results)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_tensor_contraction_sandbox({**results, "guard": guard}, validation)

    sandbox_valid = validation.get("status") == "valid_sandbox"

    return {
        "stage": "8A",
        "status": "tensor_contraction_sandbox",
        "sandbox_valid": sandbox_valid,
        "full_contractions_performed": False,
        "can_advance_to_limited_contractions": audit.get(
            "can_advance_to_limited_contractions"
        ),
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "stage7k": stage7k,
        "rules": rules,
        "results": results,
        "validation": validation,
        "audit": audit,
        "guard": guard,
    }
