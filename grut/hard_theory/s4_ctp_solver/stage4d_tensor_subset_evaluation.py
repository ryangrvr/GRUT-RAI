"""Stage 4D tensor subset evaluation gate."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.three_loop_subset_s4_tensor import (
    s4_tensor_subset_topologies,
)
from grut.hard_theory.s4_ctp_solver.tensor_subset_structures import (
    tt_propagator_placeholder,
    graviton_vertex_structure,
    index_contraction_structure,
)
from grut.hard_theory.s4_ctp_solver.tensor_contraction_scaffold import (
    symbolic_tensor_contraction,
)
from grut.hard_theory.s4_ctp_solver.tensor_subset_checks import (
    check_tt_constraints,
    check_ward_tensor_consistency,
    check_ctp_tensor_branch_structure,
)


def run_stage4d_tensor_subset_evaluation() -> Dict[str, object]:
    topologies = s4_tensor_subset_topologies()
    structures = [
        tt_propagator_placeholder(),
        graviton_vertex_structure(),
        index_contraction_structure(),
    ]
    contractions = [
        symbolic_tensor_contraction(topo, structures) for topo in topologies
    ]
    checks = [
        [
            check_tt_constraints(record),
            check_ward_tensor_consistency(record),
            check_ctp_tensor_branch_structure(record),
        ]
        for record in contractions
    ]

    all_structural = all(
        record["status"] == "tensor_structure_only" for record in contractions
    )
    ward_ok = all(
        check[1]["status"] == "structural_pass" for check in checks
    )

    return {
        "stage": "4D",
        "status": "tensor_subset_structural",
        "tensor_topologies": len(topologies),
        "tensor_contractions_attempted": len(contractions),
        "all_tensor_structural": all_structural,
        "any_tensor_evaluated": False,
        "ward_consistency": ward_ok,
        "can_attempt_mixed_full_subsets": all_structural and ward_ok,
        "can_compute_full_3loop": False,
        "promotes_claims": False,
    }
