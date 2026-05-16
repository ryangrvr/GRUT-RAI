"""Define a derivation plan for nonlocal anomaly-protected sources."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.nonlocal_anomaly_source_requirements import (
    required_source_types,
)


def build_nonlocal_anomaly_derivation_plan() -> List[Dict[str, object]]:
    plan: List[Dict[str, object]] = []
    for source_type in required_source_types():
        plan.append(
            {
                "source_type": source_type,
                "required_derivation": "derive_nonlocal_anomaly_kernel",
                "required_inputs": [
                    "ctp_branch_structure",
                    "imaginary_log_marker",
                    "nonlocal_kernel_extraction",
                    "regulator_consistency_trace",
                    "ward_identity_constraints",
                ],
                "status": "not_derived",
                "promotes_claims": False,
            }
        )
    return plan
