"""Loop-integrand components for symbolic scaffold assembly."""

from typing import Dict, List, Optional

from grut.hard_theory.s4_ctp_solver.stage9a_propagator_attachment import (
    run_stage9a_propagator_attachment,
)


def build_loop_integrand_components(
    stage9a_result: Optional[Dict[str, object]] = None,
) -> Dict[str, object]:
    if stage9a_result is None:
        stage9a_result = run_stage9a_propagator_attachment()

    attachment_result = stage9a_result.get("attachment_result", {})
    stage8d = stage9a_result.get("stage8d", {})
    skeleton = stage8d.get("skeleton", {})
    index_flow = stage8d.get("index_flow_trace", {})

    vertices: List[Dict[str, object]] = [
        {
            "vertex_id": node.get("node_id"),
            "placeholder": True,
            "indices": node.get("indices", []),
        }
        for node in skeleton.get("nodes", [])
    ]

    return {
        "components_id": "loop_integrand_components_v1",
        "propagators": attachment_result.get("attachments", []),
        "vertices": vertices,
        "index_flow": index_flow,
        "symmetry_factor": "S_placeholder",
        "regulator": "dim_reg_placeholder",
        "scheme": "ms_bar_placeholder",
        "loop_variables": ["k1", "k2", "k3"],
        "status": "components_symbolic",
        "promotes_claims": False,
    }
