"""Align protected kernels to S4 Euler/Weyl anomaly channels."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.anomaly_basis_projection import (
    project_kernel_to_anomaly_basis,
)


def _registered_candidates(stage_p7: Dict[str, object]) -> List[Dict[str, object]]:
    stage_p6 = stage_p7.get("stage_p6", {})
    return list(stage_p6.get("registered_candidates", []))


def build_kernel_projections(
    stage_p7: Dict[str, object],
    s4_identities: Dict[str, object],
    off_shell_continuation: bool = False,
) -> List[Dict[str, object]]:
    projections: List[Dict[str, object]] = []

    for entry in _registered_candidates(stage_p7):
        source_type = entry.get("source_type")
        kernel_id = entry.get("kernel_id") or source_type
        projection = project_kernel_to_anomaly_basis(
            source_type,
            s4_identities,
            off_shell_continuation=off_shell_continuation,
        )
        projections.append(
            {
                "kernel_id": kernel_id,
                "source_type": source_type,
                **projection,
                "promotes_claims": False,
            }
        )

    return projections
