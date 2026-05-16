"""Audit for TT contraction repair stage."""

from typing import Dict


def audit_tensor_contraction_repair(
    index_repair: Dict[str, object],
    projector_repair: Dict[str, object],
    ordering_protocol: Dict[str, object],
    guard: Dict[str, object],
) -> Dict[str, object]:
    no_contractions = index_repair.get("contractions_performed") is False
    projector_not_evaluated = projector_repair.get("projector_evaluated") is False
    protocol_defined = ordering_protocol.get("status") == "protocol_defined"
    guard_ok = guard.get("guard") == "tensor_placeholder_guard"

    future_sandbox_allowed = (
        not index_repair.get("illegal_free_indices_remaining")
        and projector_repair.get("canonical_form")
        and protocol_defined
    )

    status = (
        "valid_repair"
        if all([no_contractions, projector_not_evaluated, guard_ok, protocol_defined])
        else "invalid_repair"
    )

    return {
        "audit": "tensor_contraction_repair",
        "status": status,
        "blocker_closed": False,
        "future_sandbox_allowed": future_sandbox_allowed,
        "contractions_performed": False,
        "can_compute_finite_parts": False,
        "promotes_claims": False,
    }
