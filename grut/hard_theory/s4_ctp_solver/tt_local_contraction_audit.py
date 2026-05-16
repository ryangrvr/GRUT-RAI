"""Audit for diagram-local tensor contractions."""

from typing import Dict, List


def audit_local_contractions(
    results: List[Dict[str, object]],
    validations: List[Dict[str, object]],
    guard: Dict[str, object],
) -> Dict[str, object]:
    all_valid = all(v.get("status") == "valid_local" for v in validations)
    local_only = all(r.get("contraction_scope") == "local_only" for r in results)
    no_propagators = all(r.get("propagator_evaluated") is False for r in results)
    no_full_diagram = all(r.get("full_diagram_contracted") is False for r in results)
    no_finite_parts = all(r.get("finite_part_computed") is False for r in results)
    guard_ok = guard.get("guard") == "tensor_placeholder_guard"

    status = (
        "valid"
        if all([all_valid, local_only, no_propagators, no_full_diagram, no_finite_parts, guard_ok])
        else "invalid"
    )

    return {
        "audit": "diagram_local_contractions",
        "status": status,
        "local_contractions_performed": bool(results),
        "full_contractions_performed": False,
        "can_advance_to_controlled_diagram_contractions": all_valid,
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
    }
