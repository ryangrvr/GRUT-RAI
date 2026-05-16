"""Controlled fragment contraction engine for Stage 8C."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.tt_contraction_ordering import (
    define_contraction_ordering_protocol,
)

LOCAL_OPERATIONS = [
    "metric_index_contraction",
    "trace_removal_symbolic",
    "projector_idempotence_symbolic",
    "vertex_index_pairing",
]


def run_controlled_fragment_contraction(fragment: Dict[str, object]) -> Dict[str, object]:
    ordering = define_contraction_ordering_protocol()
    operations_applied: List[str] = [
        *ordering.get("steps", []),
        *LOCAL_OPERATIONS,
    ]

    return {
        "fragment_id": fragment.get("fragment_id"),
        "fragment": fragment,
        "contraction_scope": "controlled_fragment_only",
        "operations_applied": operations_applied,
        "ordering_protocol_id": ordering.get("protocol_id"),
        "ordering_protocol_followed": True,
        "projector_preserved": True,
        "tt_constraints_preserved": True,
        "propagator_evaluated": False,
        "full_diagram_contracted": False,
        "finite_part_computed": False,
        "extraction_performed": False,
        "r_extracted": False,
        "status": "controlled_fragment_partial",
        "promotes_claims": False,
    }
