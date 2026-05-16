"""Stage 12A coefficient assembly dry-run."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage11e_cross_partition_finite_consistency import (
    run_stage11e_cross_partition_finite_consistency,
)
from grut.hard_theory.s4_ctp_solver.coefficient_candidate_registry import (
    build_coefficient_candidate_registry,
)
from grut.hard_theory.s4_ctp_solver.coefficient_assembly_rules import (
    define_coefficient_assembly_rules,
)
from grut.hard_theory.s4_ctp_solver.coefficient_assembly_dry_run import (
    run_coefficient_assembly_dry_run,
)
from grut.hard_theory.s4_ctp_solver.coefficient_assembly_audit import (
    audit_coefficient_assembly_dry_run,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage12a_coefficient_assembly_dry_run() -> Dict[str, object]:
    stage11e = run_stage11e_cross_partition_finite_consistency()
    partition_results = stage11e.get("attempts", {}).get("results", [])
    registry = build_coefficient_candidate_registry(partition_results)
    rules = define_coefficient_assembly_rules()
    assembly = run_coefficient_assembly_dry_run(registry, rules)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_coefficient_assembly_dry_run(assembly, guard)

    return {
        "stage": "12A",
        "status": "coefficient_assembly_dry_run",
        "candidate_buckets_created": True,
        "physical_coefficients_computed": False,
        "can_compute_c_final": False,
        "can_compute_c_cosmo": False,
        "can_compute_r": False,
        "can_extract": False,
        "promotes_claims": False,
        "stage11e": stage11e,
        "registry": registry,
        "rules": rules,
        "assembly": assembly,
        "audit": audit,
        "guard": guard,
    }
