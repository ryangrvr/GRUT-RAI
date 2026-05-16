"""Mixed scalar-tensor contraction scaffolds for Stage 4E."""

from typing import Dict

import sympy as sp

from grut.hard_theory.s4_ctp_solver.three_loop_subset_s4_mixed import S4MixedSubsetTopology
from grut.hard_theory.s4_ctp_solver.mixed_subset_structures import MixedSubsetStructure


def symbolic_mixed_contraction(
    topology: S4MixedSubsetTopology,
    scalar_data: Dict[str, object],
    tensor_data: Dict[str, object],
) -> Dict[str, object]:
    combined = sp.Symbol(f"{topology.topology_id}_mixed_structure")
    return {
        "topology_id": topology.topology_id,
        "scalar_component_used": True,
        "tensor_component_used": True,
        "contraction_status": "not_evaluated",
        "combined_structure": combined,
        "constraints_applied": ["TT", "Ward_placeholder"],
        "scheme_metadata": scalar_data["scheme_metadata"],
        "status": "mixed_structure_only",
        "promotes_claims": False,
    }
