"""Sandbox rules for minimal TT tensor contractions."""

from typing import Dict, List


def define_sandbox_contraction_rules() -> Dict[str, object]:
    allowed: List[str] = [
        "metric_trace_identity_check",
        "projector_idempotence_symbolic_check",
        "paired_index_placeholder",
        "tt_trace_removal_symbolic_check",
    ]
    forbidden: List[str] = [
        "full_diagram_contraction",
        "propagator_contraction",
        "finite_coefficient_extraction",
        "unresolved_free_index_contraction",
    ]

    return {
        "rules_id": "tt_sandbox_contraction_rules_v1",
        "allowed": allowed,
        "forbidden": forbidden,
        "allows_full_contractions": False,
        "promotes_claims": False,
    }
