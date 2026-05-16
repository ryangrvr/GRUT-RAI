"""Stage 3E cross-check audit gate."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.crosscheck_registry import crosscheck_registry


def run_stage3e_crosscheck_audit() -> Dict[str, object]:
    registry = crosscheck_registry()
    quantities_registered = len(registry)
    multi_route_quantities = sum(
        1 for entry in registry.values() if len(entry.available_routes) > 1
    )
    next_required: List[str] = [
        "fully evaluated routes",
        "scheme-aligned finite parts",
        "consistent cross-route agreement",
        "independent external replication",
    ]
    return {
        "stage": "3E",
        "status": "crosscheck_audit",
        "quantities_registered": quantities_registered,
        "multi_route_quantities": multi_route_quantities,
        "all_routes_agree": False,
        "can_compute_3loop": False,
        "promotes_claims": False,
        "next_required_for_promotion": next_required,
    }
