"""Stage 11B divergence subtraction dry-run."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage11a_single_partition_integration import (
    run_stage11a_single_partition_integration,
)
from grut.hard_theory.s4_ctp_solver.partition_divergence_identifier import (
    identify_partition_divergences,
)
from grut.hard_theory.s4_ctp_solver.partition_counterterm_mapper import (
    map_partition_divergences_to_counterterms,
)
from grut.hard_theory.s4_ctp_solver.subtraction_dry_run_plan import (
    build_subtraction_dry_run_plan,
)
from grut.hard_theory.s4_ctp_solver.subtraction_dry_run_audit import (
    audit_subtraction_dry_run,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage11b_subtraction_dry_run() -> Dict[str, object]:
    stage11a = run_stage11a_single_partition_integration()
    divergences = identify_partition_divergences(stage11a)
    mapping = map_partition_divergences_to_counterterms(divergences)
    plan = build_subtraction_dry_run_plan(mapping)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_subtraction_dry_run(plan, mapping, guard)

    return {
        "stage": "11B",
        "status": "divergence_subtraction_dry_run",
        "divergences_identified": True,
        "subtractions_performed": False,
        "regulator_removed": False,
        "finite_part_computed": False,
        "can_advance_to_finite_part_benchmark": audit.get(
            "can_advance_to_finite_part_benchmark"
        ),
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "stage11a": stage11a,
        "divergences": divergences,
        "mapping": mapping,
        "plan": plan,
        "audit": audit,
        "guard": guard,
    }
