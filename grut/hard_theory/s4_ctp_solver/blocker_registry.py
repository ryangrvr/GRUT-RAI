"""Registry of extraction blockers and required inputs."""

from typing import Dict, List


def register_blockers() -> List[Dict[str, object]]:
    return [
        {
            "blocker_id": "finite_part_not_computed",
            "current_status": "open",
            "required_inputs": ["finite parts"],
            "required_tests": ["finite_part_validation"],
            "difficulty": "frontier",
            "dependencies": [
                "tensor_contractions_not_resolved",
                "convergence_not_established",
            ],
            "closure_status": "open",
        },
        {
            "blocker_id": "convergence_not_established",
            "current_status": "open",
            "required_inputs": ["spectral convergence proof"],
            "required_tests": ["convergence_audit"],
            "difficulty": "high",
            "dependencies": [],
            "closure_status": "open",
        },
        {
            "blocker_id": "tensor_contractions_not_resolved",
            "current_status": "open",
            "required_inputs": ["explicit tensor contractions"],
            "required_tests": ["tensor_contraction_validation"],
            "difficulty": "frontier",
            "dependencies": ["full_S4_propagator_missing"],
            "closure_status": "open",
        },
        {
            "blocker_id": "ward_identity_not_fully_verified",
            "current_status": "open",
            "required_inputs": ["Ward identity verification"],
            "required_tests": ["ward_identity_consistency"],
            "difficulty": "high",
            "dependencies": [],
            "closure_status": "open",
        },
        {
            "blocker_id": "independent_replication_missing",
            "current_status": "open",
            "required_inputs": ["independent replication"],
            "required_tests": ["replication_audit"],
            "difficulty": "frontier",
            "dependencies": [],
            "closure_status": "open",
        },
        {
            "blocker_id": "full_S4_propagator_missing",
            "current_status": "open",
            "required_inputs": ["full S4 propagators"],
            "required_tests": ["propagator_validation"],
            "difficulty": "frontier",
            "dependencies": [],
            "closure_status": "open",
        },
    ]
