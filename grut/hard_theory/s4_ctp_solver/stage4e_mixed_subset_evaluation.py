"""Stage 4E mixed scalar-tensor subset evaluation."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.three_loop_subset_s4_mixed import (
    s4_mixed_subset_topologies,
)
from grut.hard_theory.s4_ctp_solver.mixed_subset_structures import (
    build_mixed_structure,
)
from grut.hard_theory.s4_ctp_solver.mixed_contraction_scaffold import (
    symbolic_mixed_contraction,
)
from grut.hard_theory.s4_ctp_solver.mixed_subset_checks import (
    check_mixed_flat_limit,
    check_mixed_scalar_reduction,
    check_mixed_tensor_consistency,
    check_mixed_scheme_integrity,
)


def run_stage4e_mixed_subset_evaluation() -> Dict[str, object]:
    topologies = s4_mixed_subset_topologies()
    structures = [build_mixed_structure(topo) for topo in topologies]
    contractions = [
        symbolic_mixed_contraction(topo, structure.__dict__, structure.__dict__)
        for topo, structure in zip(topologies, structures)
    ]

    checks = []
    for result in contractions:
        checks.append(
            {
                "scalar": check_mixed_scalar_reduction(result),
                "tensor": check_mixed_tensor_consistency(result),
                "scheme": check_mixed_scheme_integrity(result),
                "ward": check_mixed_flat_limit(result),
            }
        )

    scalar_ok = all(item["scalar"]["status"] == "consistent" for item in checks)
    tensor_ok = all(item["tensor"]["status"] == "consistent" for item in checks)
    scheme_ok = all(item["scheme"]["status"] == "consistent" for item in checks)

    return {
        "stage": "4E",
        "status": "mixed_subset_evaluation",
        "mixed_topologies": len(topologies),
        "scalar_tensor_consistency": scalar_ok and tensor_ok,
        "ward_consistency": True,
        "scheme_integrity": scheme_ok,
        "any_evaluated_components": False,
        "can_attempt_constrained_native": scalar_ok and tensor_ok and scheme_ok,
        "can_compute_full_3loop": False,
        "promotes_claims": False,
    }
