"""Multi-topology native attempt pipeline for Stage 5B."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.native_attempt_pipeline import run_native_attempt_pipeline
from grut.hard_theory.s4_ctp_solver.native_attempt_evaluation import evaluate_native_attempt
from grut.hard_theory.s4_ctp_solver.native_attempt_audit import audit_native_attempt
from grut.hard_theory.s4_ctp_solver.native_attempt_topology import NativeAttemptTopology
from grut.hard_theory.s4_ctp_solver.native_attempt_topology_set import (
    NativeAttemptTopologyEntry,
)


def _as_native_attempt_topology(entry: NativeAttemptTopologyEntry) -> NativeAttemptTopology:
    return NativeAttemptTopology(
        topology_id=entry.topology_id,
        loop_order=entry.loop_order,
        background=entry.background,
        topology_type=entry.topology_type,
        native_attempt=entry.native_attempt,
    )


def run_native_attempt_multi_pipeline(
    topology_list: List[NativeAttemptTopologyEntry],
) -> Dict[str, object]:
    results = []
    audits = []

    for entry in topology_list:
        topology = _as_native_attempt_topology(entry)
        _ = run_native_attempt_pipeline(topology, {})
        result = evaluate_native_attempt(topology)
        results.append(result)
        audits.append(audit_native_attempt(result))

    return {
        "topologies": [entry.topology_id for entry in topology_list],
        "results": results,
        "audits": audits,
        "status": "multi_native_attempt",
        "promotes_claims": False,
    }
