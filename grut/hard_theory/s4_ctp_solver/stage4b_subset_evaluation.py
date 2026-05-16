"""Stage 4B subset evaluation gate."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.three_loop_subset_flat import flat_subset_topologies
from grut.hard_theory.s4_ctp_solver.subset_evaluation_engine import (
    evaluate_3loop_subset,
    compare_subset_to_known_structure,
)


def run_stage4b_subset_evaluation() -> Dict[str, object]:
    topologies = flat_subset_topologies()
    evaluations = [evaluate_3loop_subset(topo, {}) for topo in topologies]
    comparisons = [compare_subset_to_known_structure(ev, topo) for ev, topo in zip(evaluations, topologies)]

    factorizable = [t for t in topologies if t.factorization_possible]
    factorizable_ok = [
        comp for comp, topo in zip(comparisons, topologies)
        if topo.factorization_possible and comp["status"] == "consistent"
    ]
    inconsistencies = [comp["comparison"] for comp in comparisons if comp["status"] == "inconsistent"]

    return {
        "stage": "4B",
        "status": "subset_evaluation",
        "topologies_evaluated": len(topologies),
        "factorizable_cases_verified": len(factorizable_ok),
        "nonfactorizable_cases_attempted": len(topologies) - len(factorizable),
        "any_inconsistencies": inconsistencies,
        "can_attempt_curved_subsets": len(factorizable_ok) == len(factorizable),
        "can_compute_full_3loop": False,
        "promotes_claims": False,
    }
