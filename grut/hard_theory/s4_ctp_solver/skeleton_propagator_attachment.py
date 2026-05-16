"""Attach symbolic propagator records to a diagram skeleton."""

from typing import Dict, List


def attach_propagators_to_skeleton(
    skeleton: Dict[str, object],
    registry: List[Dict[str, object]],
) -> Dict[str, object]:
    registry_by_type = {record["field_type"]: record for record in registry}
    attachments: List[Dict[str, object]] = []
    edges = skeleton.get("edges", [])

    for edge in edges:
        field_type = edge.get("field_type")
        record = registry_by_type.get(field_type)
        attachments.append(
            {
                "edge_id": edge.get("edge_id"),
                "field_type": field_type,
                "propagator_id": record.get("propagator_id") if record else None,
                "evaluation_status": record.get("evaluation_status") if record else None,
            }
        )

    edges_covered = all(attachment.get("propagator_id") for attachment in attachments)
    all_symbolic = all(
        attachment.get("evaluation_status") in {"symbolic_only", "scaffold_not_evaluated"}
        for attachment in attachments
    )

    return {
        "diagram_id": skeleton.get("diagram_id"),
        "attachments": attachments,
        "edges_covered": edges_covered,
        "all_symbolic": all_symbolic,
        "propagators_evaluated": False,
        "loops_evaluated": False,
        "finite_part_computed": False,
        "extraction_performed": False,
        "r_extracted": False,
        "status": "propagator_symbolic_attachment",
        "promotes_claims": False,
    }
