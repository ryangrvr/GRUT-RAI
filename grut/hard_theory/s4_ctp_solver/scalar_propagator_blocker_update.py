"""Update full S4 propagator blocker status (scalar-only)."""

from typing import Dict


def update_full_s4_propagator_blocker_scalar_only() -> Dict[str, object]:
    return {
        "blocker": "full_S4_propagator_missing",
        "scalar_conformal_subproblem": "partially_closed",
        "tt_graviton_propagator": "open",
        "ghost_propagator": "open",
        "vector_tensor_modes": "open",
        "overall_blocker_closed": False,
        "promotes_claims": False,
    }
