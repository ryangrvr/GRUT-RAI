"""Repair registry for finite-part blocker resolution."""

from typing import Dict, List

REQUIRED_BLOCKERS = [
    "unmapped_divergence",
    "scheme_incomplete",
    "instability_detected",
    "structure_breakdown",
    "insufficient_convergence_control",
    "tensor_contractions_not_resolved",
    "independent_replication_missing",
]

_REPAIR_LIBRARY = {
    "unmapped_divergence": {
        "required_action": "Extend divergence tracking to cover missing structures.",
        "difficulty": "high",
        "dependencies": ["scheme_incomplete"],
        "completion_test": "All divergence terms map to registered counterterms.",
    },
    "scheme_incomplete": {
        "required_action": "Expand scheme alignment coverage to full invariant basis.",
        "difficulty": "medium",
        "dependencies": [],
        "completion_test": "Scheme alignment returns consistent with full basis coverage.",
    },
    "instability_detected": {
        "required_action": "Stabilize TT inversion under regularization and cutoff scans.",
        "difficulty": "high",
        "dependencies": ["insufficient_convergence_control"],
        "completion_test": "Stability checks remain stable across required l_max values.",
    },
    "structure_breakdown": {
        "required_action": "Restore TT tensor structure through projector and mode audits.",
        "difficulty": "frontier",
        "dependencies": ["tensor_contractions_not_resolved"],
        "completion_test": "Structure checks pass with no scalar/vector collapse.",
    },
    "insufficient_convergence_control": {
        "required_action": "Strengthen convergence control and regularization diagnostics.",
        "difficulty": "high",
        "dependencies": [],
        "completion_test": "Regularization diagnostics show controlled UV behavior.",
    },
    "tensor_contractions_not_resolved": {
        "required_action": "Complete TT tensor contraction engine scaffolding.",
        "difficulty": "frontier",
        "dependencies": [],
        "completion_test": "Tensor contraction engine passes structural audits.",
    },
    "independent_replication_missing": {
        "required_action": "Secure independent replication of TT inversion benchmarks.",
        "difficulty": "high",
        "dependencies": [],
        "completion_test": "Independent audit confirms benchmark reproducibility.",
    },
}


def build_finite_part_repair_registry(blockers: List[str]) -> Dict[str, object]:
    repair_items: List[Dict[str, object]] = []
    for blocker in REQUIRED_BLOCKERS:
        meta = _REPAIR_LIBRARY[blocker]
        repair_items.append(
            {
                "repair_id": f"repair_{blocker}",
                "blocker": blocker,
                "required_action": meta["required_action"],
                "difficulty": meta["difficulty"],
                "dependencies": list(meta["dependencies"]),
                "completion_test": meta["completion_test"],
                "status": "not_started",
                "promotes_claims": False,
            }
        )

    return {
        "registry_id": "finite_part_repair_registry_v1",
        "blockers": list(blockers),
        "required_blockers": list(REQUIRED_BLOCKERS),
        "repairs": repair_items,
        "promotes_claims": False,
    }
