"""Stage 12D controlled R extraction attempt."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage12c_r_legality_gate import (
    run_stage12c_r_legality_gate,
)
from grut.hard_theory.s4_ctp_solver.r_symbolic_construction import build_symbolic_r
from grut.hard_theory.s4_ctp_solver.r_cancellation_execution import (
    execute_r_cancellation,
)
from grut.hard_theory.s4_ctp_solver.r_finite_isolation import (
    isolate_r_finite_structure,
)
from grut.hard_theory.s4_ctp_solver.r_physical_validation import (
    validate_r_physical_properties,
)
from grut.hard_theory.s4_ctp_solver.r_extraction_audit import audit_r_extraction
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage12d_r_extraction_attempt() -> Dict[str, object]:
    stage12c = run_stage12c_r_legality_gate()
    valid_pairs = stage12c.get("valid_pairs", [])

    if stage12c.get("r_legal") is not True or not valid_pairs:
        guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
        return {
            "stage": "12D",
            "status": "r_extraction_attempt",
            "r_attempted": True,
            "r_value": None,
            "valid": False,
            "failure_reason": "no_legal_pairs",
            "promotes_claims": False,
            "stage12c": stage12c,
            "guard": guard,
        }

    pair = valid_pairs[0].get("pair", {})
    symbolic_r = build_symbolic_r(pair)
    cancellation = execute_r_cancellation(symbolic_r)
    finite = isolate_r_finite_structure(cancellation)
    validation = validate_r_physical_properties(symbolic_r, cancellation)
    audit = audit_r_extraction(symbolic_r, cancellation, validation)

    valid = (
        finite.get("isolation_ok")
        and validation.get("valid") is True
        and audit.get("status") == "valid"
    )

    r_value = finite.get("finite_structure") if valid else None
    failure_reason = None if valid else audit.get("violations")

    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())

    return {
        "stage": "12D",
        "status": "r_extraction_attempt",
        "r_attempted": True,
        "r_value": r_value,
        "valid": valid,
        "failure_reason": failure_reason,
        "promotes_claims": False,
        "pair": pair,
        "symbolic_r": symbolic_r,
        "cancellation": cancellation,
        "finite": finite,
        "validation": validation,
        "audit": audit,
        "stage12c": stage12c,
        "guard": guard,
    }
