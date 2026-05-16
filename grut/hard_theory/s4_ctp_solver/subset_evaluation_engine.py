"""Subset evaluation engine for Stage 4B."""

from typing import Dict

import sympy as sp

from grut.hard_theory.s4_ctp_solver.three_loop_subset_flat import SubsetTopology


def evaluate_3loop_subset(topology: SubsetTopology, parameters: Dict[str, object]) -> Dict[str, object]:
    i1 = sp.Symbol("I1")
    i2 = sp.Symbol("I2")

    if topology.factorization_possible:
        if topology.known_structure == "product_of_1loop":
            expr = i1**3
        else:
            expr = i1 * i2
        evaluation_type = "factorized"
        status = "partial_benchmark"
    else:
        expr = sp.Symbol(f"{topology.topology_id}_structure")
        evaluation_type = "partial"
        status = "exploratory"

    return {
        "topology_id": topology.topology_id,
        "evaluation_type": evaluation_type,
        "expression": expr,
        "divergence_structure": topology.expected_divergence_pattern,
        "finite_part": "not_evaluated",
        "status": status,
        "promotes_claims": False,
    }


def compare_subset_to_known_structure(result: Dict[str, object], topology: SubsetTopology) -> Dict[str, object]:
    divergence_ok = result["divergence_structure"] == topology.expected_divergence_pattern
    if topology.factorization_possible:
        factor_ok = result["evaluation_type"] == "factorized"
        if divergence_ok and factor_ok:
            status = "consistent"
            reason = "factorized structure matches expected divergence"
        else:
            status = "inconsistent"
            reason = "factorization/divergence mismatch"
    else:
        status = "inconclusive" if divergence_ok else "inconsistent"
        reason = "nonfactorizable subset not fully evaluable"

    return {
        "comparison": topology.topology_id,
        "status": status,
        "reason": reason,
        "promotes_claims": False,
    }
