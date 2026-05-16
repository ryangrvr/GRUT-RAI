"""Validation for symbolic propagator attachments."""

from typing import Dict, List


FIELD_TO_PROPAGATOR = {
    "tt_graviton": "tt_s4_scaffold",
    "ghost": "ghost_s4_structural",
    "scalar": "scalar_conformal_s4",
}


def validate_propagator_attachments(attachment_result: Dict[str, object]) -> Dict[str, object]:
    issues: List[str] = []
    attachments = attachment_result.get("attachments", [])

    for attachment in attachments:
        field_type = attachment.get("field_type")
        expected = FIELD_TO_PROPAGATOR.get(field_type)
        if expected is None:
            issues.append(f"unknown_field_type:{field_type}")
            continue
        if attachment.get("propagator_id") != expected:
            issues.append(f"propagator_mismatch:{field_type}")

    if attachment_result.get("edges_covered") is not True:
        issues.append("edges_not_covered")

    if attachment_result.get("all_symbolic") is not True:
        issues.append("non_symbolic_attachment")

    if attachment_result.get("propagators_evaluated") is not False:
        issues.append("propagators_evaluated")

    if attachment_result.get("loops_evaluated") is not False:
        issues.append("loops_evaluated")

    if attachment_result.get("finite_part_computed") is not False:
        issues.append("finite_part_computed")

    if attachment_result.get("extraction_performed") is not False:
        issues.append("extraction_performed")

    if attachment_result.get("r_extracted") is not False:
        issues.append("r_extracted")

    status = "valid_attachment" if not issues else "invalid_attachment"

    return {
        "validation": "propagator_attachment",
        "status": status,
        "issues": issues,
        "promotes_claims": False,
    }
