"""Diagram skeleton definition for Stage 8D."""

from typing import Dict, List


def define_tt_diagram_skeleton() -> Dict[str, object]:
    nodes: List[Dict[str, object]] = [
        {
            "node_id": "vertex_A",
            "indices": ["mu", "nu"],
            "role": "tensor_vertex",
        },
        {
            "node_id": "vertex_B",
            "indices": ["rho", "sigma"],
            "role": "tensor_vertex",
        },
        {
            "node_id": "vertex_C",
            "indices": ["alpha", "beta"],
            "role": "tensor_vertex",
        },
    ]

    edges: List[Dict[str, object]] = [
        {
            "edge_id": "edge_AB",
            "from": "vertex_A",
            "to": "vertex_B",
            "indices": ["mu", "rho"],
            "propagator": "tt_placeholder",
            "field_type": "tt_graviton",
        },
        {
            "edge_id": "edge_BC",
            "from": "vertex_B",
            "to": "vertex_C",
            "indices": ["sigma", "alpha"],
            "propagator": "ghost_placeholder",
            "field_type": "ghost",
        },
        {
            "edge_id": "edge_CA",
            "from": "vertex_C",
            "to": "vertex_A",
            "indices": ["beta", "nu"],
            "propagator": "scalar_placeholder",
            "field_type": "scalar",
        },
    ]

    return {
        "diagram_id": "tt_skeleton_v1",
        "nodes": nodes,
        "edges": edges,
        "propagators": "placeholders_only",
        "projectors_present": True,
        "loops_present": True,
        "evaluated": False,
        "promotes_claims": False,
    }
