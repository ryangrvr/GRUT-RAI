"""Formal checklist for legal coefficient extraction."""

from typing import Dict, List


CRITERIA_ITEMS: List[str] = [
    "finite_part_computed",
    "spectral_convergence_established",
    "tensor_contractions_resolved",
    "scheme_alignment_fixed",
    "ward_identity_verified",
    "cross_topology_consistency_confirmed",
    "independent_replication_available",
]


def define_extraction_criteria() -> Dict[str, object]:
    return {
        "criteria": list(CRITERIA_ITEMS),
        "all_required": True,
        "promotes_claims": False,
    }
