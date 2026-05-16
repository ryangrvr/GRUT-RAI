"""Diagram-local tensor contraction fragments for Stage 8B."""

from typing import Dict, List


def define_local_contraction_fragments() -> List[Dict[str, object]]:
    fragments: List[Dict[str, object]] = [
        {
            "fragment_id": "projector_metric_local_contraction",
            "scope": "local_only",
            "requires_propagator": False,
            "requires_full_diagram": False,
            "allowed_by_sandbox": True,
            "status": "fragment_defined",
            "promotes_claims": False,
        },
        {
            "fragment_id": "tt_trace_removal_fragment",
            "scope": "local_only",
            "requires_propagator": False,
            "requires_full_diagram": False,
            "allowed_by_sandbox": True,
            "status": "fragment_defined",
            "promotes_claims": False,
        },
        {
            "fragment_id": "paired_index_tensor_placeholder_fragment",
            "scope": "local_only",
            "requires_propagator": False,
            "requires_full_diagram": False,
            "allowed_by_sandbox": True,
            "status": "fragment_defined",
            "promotes_claims": False,
        },
        {
            "fragment_id": "local_vertex_index_pairing_fragment",
            "scope": "local_only",
            "requires_propagator": False,
            "requires_full_diagram": False,
            "allowed_by_sandbox": True,
            "status": "fragment_defined",
            "promotes_claims": False,
        },
    ]

    return fragments
