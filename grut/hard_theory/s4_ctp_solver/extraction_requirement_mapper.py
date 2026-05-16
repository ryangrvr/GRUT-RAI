"""Map extraction blockers to actionable requirements."""

from typing import Dict, List


_BLOCKER_MAPPING = {
    "finite_part_not_computed": {
        "required_action": "compute finite parts",
        "difficulty": "frontier",
        "stage_dependency": "Stage 4C+",
    },
    "convergence_not_established": {
        "required_action": "establish spectral convergence",
        "difficulty": "high",
        "stage_dependency": "Stage 3B+",
    },
    "tensor_contractions_not_resolved": {
        "required_action": "resolve tensor contractions",
        "difficulty": "frontier",
        "stage_dependency": "Stage 4D+",
    },
    "scheme_alignment_missing": {
        "required_action": "fix scheme alignment",
        "difficulty": "high",
        "stage_dependency": "Stage 3D+",
    },
    "Ward_identity_not_fully_verified": {
        "required_action": "verify Ward identities",
        "difficulty": "high",
        "stage_dependency": "Stage 3C+",
    },
    "independent_replication_missing": {
        "required_action": "independent replication",
        "difficulty": "frontier",
        "stage_dependency": "External audit",
    },
    "full_S4_propagator_missing": {
        "required_action": "compute full S4 propagators",
        "difficulty": "frontier",
        "stage_dependency": "Stage 3B+",
    },
}


def map_blockers_to_requirements(candidate: Dict[str, object]) -> Dict[str, object]:
    blockers = candidate.get("blockers", [])
    requirements: List[Dict[str, str]] = []

    for blocker in blockers:
        mapping = _BLOCKER_MAPPING.get(
            blocker,
            {
                "required_action": "resolve blocker",
                "difficulty": "high",
                "stage_dependency": "TBD",
            },
        )
        requirements.append(
            {
                "blocker": blocker,
                "required_action": mapping["required_action"],
                "difficulty": mapping["difficulty"],
                "stage_dependency": mapping["stage_dependency"],
            }
        )

    return {
        "candidate_id": candidate.get("candidate_id", "unknown_candidate"),
        "requirements": requirements,
        "can_satisfy_now": False,
    }
