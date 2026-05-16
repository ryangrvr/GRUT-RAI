"""Cross-check registry for Stage 3E audits."""

from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class CrosscheckQuantity:
    quantity_id: str
    available_routes: List[str]
    current_route_status: Dict[str, str]
    scheme_dependence: str
    expected_consistency_relation: str
    status: str


def crosscheck_registry() -> Dict[str, CrosscheckQuantity]:
    return {
        "scalar_1loop_effective_action": CrosscheckQuantity(
            quantity_id="scalar_1loop_effective_action",
            available_routes=["heat_kernel", "spectral", "flat_limit", "ward_identity"],
            current_route_status={
                "heat_kernel": "implemented",
                "spectral": "partial",
                "flat_limit": "partial",
                "ward_identity": "not_available",
            },
            scheme_dependence="scheme_dependent",
            expected_consistency_relation="heat_kernel ~ spectral ~ flat_limit (structural)",
            status="registered_not_crosschecked",
        ),
        "curvature_R2_sector": CrosscheckQuantity(
            quantity_id="curvature_R2_sector",
            available_routes=["heat_kernel", "spectral", "flat_limit", "ward_identity"],
            current_route_status={
                "heat_kernel": "partial",
                "spectral": "partial",
                "flat_limit": "partial",
                "ward_identity": "not_available",
            },
            scheme_dependence="scheme_dependent",
            expected_consistency_relation="R^2 sector alignment across routes",
            status="registered_not_crosschecked",
        ),
    }
