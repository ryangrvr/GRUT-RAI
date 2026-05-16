"""Define symbolic integration ordering for the dry-run plan."""

from typing import Dict, List


def define_integration_ordering() -> Dict[str, object]:
    ordering: List[str] = [
        "insert_regulator_factors",
        "contract_tensor_structure",
        "integrate_k1",
        "integrate_k2",
        "integrate_k3",
        "take_regulator_limits",
    ]
    return {
        "ordering": ordering,
        "justification": "structural_consistency",
        "status": "ordering_defined",
        "promotes_claims": False,
    }
