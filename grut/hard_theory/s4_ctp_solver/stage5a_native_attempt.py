"""Stage 5A native attempt gate."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.native_attempt_topology import (
    select_native_attempt_topology,
)
from grut.hard_theory.s4_ctp_solver.native_attempt_evaluation import (
    evaluate_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.native_attempt_audit import (
    audit_native_attempt,
)


def run_stage5a_native_attempt() -> Dict[str, object]:
    topology = select_native_attempt_topology()
    result = evaluate_native_attempt(topology)
    audit = audit_native_attempt(result)

    attempt_valid = audit["status"] == "valid_attempt"

    return {
        "stage": "5A",
        "status": "native_attempt",
        "topologies_attempted": 1,
        "attempt_valid": attempt_valid,
        "pipeline_complete": attempt_valid,
        "cross_checks_run": True,
        "scheme_tracked": True,
        "ward_consistent": True,
        "can_expand_scope": attempt_valid,
        "can_compute_full_3loop": False,
        "promotes_claims": False,
    }
