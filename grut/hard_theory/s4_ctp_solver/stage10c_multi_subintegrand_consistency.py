"""Stage 10C multi-subintegrand consistency check."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage9c_regularized_integrand import (
    run_stage9c_regularized_integrand,
)
from grut.hard_theory.s4_ctp_solver.native_subintegrand_set import (
    select_native_subintegrand_set,
)
from grut.hard_theory.s4_ctp_solver.multi_subintegrand_engine import (
    run_multi_subintegrand_attempt,
)
from grut.hard_theory.s4_ctp_solver.multi_subintegrand_consistency import (
    compare_subintegrand_behaviors,
)
from grut.hard_theory.s4_ctp_solver.multi_subintegrand_audit import (
    audit_multi_subintegrand,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage10c_multi_subintegrand_consistency() -> Dict[str, object]:
    stage9c = run_stage9c_regularized_integrand()
    integrand = stage9c.get("stage9b", {}).get("integrand", {})
    scheme = stage9c.get("scheme", {})
    subintegrands = select_native_subintegrand_set(integrand)
    for subintegrand in subintegrands:
        subintegrand["scheme_id"] = scheme.get("scheme_id")
        subintegrand["default_regulator"] = scheme.get("default_regulator")

    attempts = run_multi_subintegrand_attempt(subintegrands)
    comparison = compare_subintegrand_behaviors(attempts)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    comparison_with_guard = {**comparison, "guard": guard}
    audit = audit_multi_subintegrand(attempts, comparison_with_guard)

    return {
        "stage": "10C",
        "status": "multi_subintegrand_consistency",
        "subintegrands_attempted": len(subintegrands),
        "behavior_consistent": comparison.get("consistent"),
        "finite_parts_computed": False,
        "amplitude_computed": False,
        "can_advance_to_native_integrand_partition": audit.get(
            "can_advance_to_native_integrand_partition"
        ),
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "stage9c": stage9c,
        "subintegrands": subintegrands,
        "attempts": attempts,
        "comparison": comparison_with_guard,
        "audit": audit,
        "guard": guard,
    }
