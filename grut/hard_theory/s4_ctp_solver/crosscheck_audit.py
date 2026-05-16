"""Cross-check audit harness for Stage 3E."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.crosscheck_registry import crosscheck_registry
from grut.hard_theory.s4_ctp_solver.crosscheck_routes import (
    compute_via_heat_kernel,
    compute_via_spectral_sum,
    compute_via_flat_limit,
    compute_via_ward_identity,
)
from grut.hard_theory.s4_ctp_solver.consistency_metrics import (
    compare_symbolic_forms,
    compare_limit_behavior,
    compare_scheme_metadata,
)


def run_crosscheck(quantity_id: str) -> Dict[str, object]:
    registry = crosscheck_registry()
    quantity = registry.get(quantity_id)
    if quantity is None:
        return {
            "quantity_id": quantity_id,
            "routes_used": [],
            "consistency_summary": {},
            "overall_status": "incomplete_routes",
            "promotes_claims": False,
        }

    parameters = {}
    routes = {
        "heat_kernel": compute_via_heat_kernel,
        "spectral": compute_via_spectral_sum,
        "flat_limit": compute_via_flat_limit,
        "ward_identity": compute_via_ward_identity,
    }

    results = {}
    for route in quantity.available_routes:
        results[route] = routes[route](quantity_id, parameters)

    heat = results["heat_kernel"]
    spectral = results["spectral"]
    flat = results["flat_limit"]
    ward = results["ward_identity"]

    summary = {
        "heat_vs_spectral": compare_symbolic_forms(heat, spectral)["status"],
        "heat_vs_flat": compare_limit_behavior(heat, flat)["status"],
        "spectral_vs_flat": compare_limit_behavior(spectral, flat)["status"],
        "ward_consistency": compare_scheme_metadata(heat, ward)["status"],
    }

    if any(value == "inconsistent" for value in summary.values()):
        overall = "inconclusive"
    elif any(value == "inconclusive" for value in summary.values()):
        overall = "inconclusive"
    else:
        overall = "crosschecked_structurally"

    return {
        "quantity_id": quantity_id,
        "routes_used": list(results.keys()),
        "consistency_summary": summary,
        "overall_status": overall,
        "promotes_claims": False,
    }
