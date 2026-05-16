"""Map TT divergence structures to counterterms (structural)."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.counterterms import counterterm_registry


def map_tt_divergences_to_counterterms(
    regularized_results: List[Dict[str, object]],
) -> Dict[str, object]:
    registry = counterterm_registry()
    counterterms_required = list(registry.keys())

    unmapped_divergences: List[str] = []
    for result in regularized_results:
        if result.get("scheme") == "zeta_placeholder":
            unmapped_divergences.append("zeta_placeholder_divergence")

    return {
        "mapping_status": "mapped_structurally",
        "counterterms_required": counterterms_required,
        "unmapped_divergences": unmapped_divergences,
        "promotes_claims": False,
    }
