"""Closure plans for each blocker."""

from typing import Dict, List


def build_blocker_closure_plan() -> List[Dict[str, object]]:
    return [
        {
            "blocker_id": "finite_part_not_computed",
            "next_module": "finite_part_evaluator",
            "minimum_test": "finite_part_validation",
            "promotion_condition": "finite_part_defined_and_verified",
            "failure_condition": "finite_part_missing",
        },
        {
            "blocker_id": "convergence_not_established",
            "next_module": "spectral_convergence_audit",
            "minimum_test": "convergence_audit",
            "promotion_condition": "convergence_bounds_verified",
            "failure_condition": "convergence_unverified",
        },
        {
            "blocker_id": "tensor_contractions_not_resolved",
            "next_module": "tensor_contraction_engine",
            "minimum_test": "tensor_contraction_validation",
            "promotion_condition": "tensor_contractions_resolved",
            "failure_condition": "tensor_contractions_missing",
        },
        {
            "blocker_id": "ward_identity_not_fully_verified",
            "next_module": "ward_identity_verifier",
            "minimum_test": "ward_identity_consistency",
            "promotion_condition": "ward_identities_verified",
            "failure_condition": "ward_identities_missing",
        },
        {
            "blocker_id": "independent_replication_missing",
            "next_module": "replication_audit_bundle",
            "minimum_test": "replication_audit",
            "promotion_condition": "independent_replication_available",
            "failure_condition": "replication_missing",
        },
        {
            "blocker_id": "full_S4_propagator_missing",
            "next_module": "s4_propagator_solver",
            "minimum_test": "propagator_validation",
            "promotion_condition": "full_s4_propagators_defined",
            "failure_condition": "propagator_missing",
        },
    ]
