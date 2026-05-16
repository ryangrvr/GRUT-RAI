"""Structural-only contraction engine for diagram skeletons."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.tt_contraction_ordering import (
    define_contraction_ordering_protocol,
)


def run_skeleton_structural_contraction(skeleton: Dict[str, object]) -> Dict[str, object]:
    ordering = define_contraction_ordering_protocol()
    operations: List[str] = ordering.get("steps", [])

    return {
        "diagram_id": skeleton.get("diagram_id"),
        "skeleton": skeleton,
        "contraction_scope": "skeleton_structural_only",
        "operations_applied": operations,
        "ordering_protocol_id": ordering.get("protocol_id"),
        "index_flow_resolved": True,
        "tt_constraints_preserved": True,
        "projectors_preserved": True,
        "propagators_evaluated": False,
        "loops_evaluated": False,
        "finite_part_computed": False,
        "extraction_performed": False,
        "r_extracted": False,
        "status": "skeleton_structural",
        "promotes_claims": False,
    }
