"""Stage 10D native integrand partition map."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage9c_regularized_integrand import (
    run_stage9c_regularized_integrand,
)
from grut.hard_theory.s4_ctp_solver.native_integrand_partition import (
    partition_native_integrand,
)
from grut.hard_theory.s4_ctp_solver.partition_eligibility import (
    classify_partition_eligibility,
)
from grut.hard_theory.s4_ctp_solver.partition_dependency_graph import (
    build_partition_dependency_graph,
)
from grut.hard_theory.s4_ctp_solver.partition_map_audit import (
    audit_partition_map,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage10d_integrand_partition_map() -> Dict[str, object]:
    stage9c = run_stage9c_regularized_integrand()
    integrand = stage9c.get("stage9b", {}).get("integrand", {})
    partitions = partition_native_integrand(integrand)
    classifications = [classify_partition_eligibility(partition) for partition in partitions]
    graph = build_partition_dependency_graph(partitions)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_partition_map(partitions, classifications, graph, guard)

    tested_count = len(
        [partition for partition in partitions if partition.get("partition_type") == "tested_minimal"]
    )

    return {
        "stage": "10D",
        "status": "native_integrand_partition_map",
        "partition_count": len(partitions),
        "tested_partition_count": tested_count,
        "integrations_performed": False,
        "full_integrand_used": False,
        "can_advance_to_partition_dry_runs": audit.get(
            "can_advance_to_partition_dry_runs"
        ),
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "stage9c": stage9c,
        "partitions": partitions,
        "classifications": classifications,
        "graph": graph,
        "audit": audit,
        "guard": guard,
    }
