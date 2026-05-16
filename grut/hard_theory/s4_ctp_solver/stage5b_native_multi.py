"""Stage 5B multi-topology native attempt gate."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.native_attempt_topology_set import (
    get_native_attempt_topology_set,
)
from grut.hard_theory.s4_ctp_solver.native_attempt_multi_pipeline import (
    run_native_attempt_multi_pipeline,
)
from grut.hard_theory.s4_ctp_solver.native_attempt_comparison import (
    compare_native_attempts,
)
from grut.hard_theory.s4_ctp_solver.native_attempt_multi_audit import (
    audit_native_multi,
)


def run_stage5b_native_multi() -> Dict[str, object]:
    topologies = get_native_attempt_topology_set()
    pipeline = run_native_attempt_multi_pipeline(topologies)
    comparison = compare_native_attempts(pipeline["results"])
    audit = audit_native_multi(pipeline["results"], pipeline["audits"], comparison)

    return {
        "stage": "5B",
        "status": "multi_native_attempt",
        "topologies_attempted": len(topologies),
        "all_pipelines_complete": True,
        "cross_comparison_run": True,
        "audit_valid": audit["status"] == "valid_multi_attempt",
        "can_expand_scope": audit["can_expand_to_tensor_depth"],
        "can_compute_full_3loop": False,
        "promotes_claims": False,
    }
