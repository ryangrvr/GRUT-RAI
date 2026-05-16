"""Identify blockers that prevent legal extraction."""

from typing import Dict, List


def identify_extraction_blockers(candidate: Dict[str, object]) -> Dict[str, object]:
    blockers: List[str] = [
        "finite_part_not_computed",
        "convergence_not_established",
        "scheme_alignment_missing",
        "Ward_identity_not_fully_verified",
        "independent_replication_missing",
        "full_S4_propagator_missing",
    ]

    symbolic_form = str(candidate.get("symbolic_form", "")).lower()
    source_topologies = " ".join(candidate.get("source_topologies", [])).lower()
    associated = str(candidate.get("associated_invariant", "")).lower()
    if "tensor" in symbolic_form or "tensor" in source_topologies or "tensor" in associated:
        blockers.append("tensor_contractions_not_resolved")

    required_for_extraction = [
        "finite parts",
        "convergence proof",
        "explicit tensor contractions",
        "scheme-aligned definitions",
        "Ward verification",
        "independent replication",
    ]

    return {
        "candidate_id": candidate.get("candidate_id", "unknown_candidate"),
        "blockers": blockers,
        "can_extract_now": False,
        "required_for_extraction": required_for_extraction,
    }
