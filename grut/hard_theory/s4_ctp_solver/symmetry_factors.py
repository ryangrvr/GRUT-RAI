"""Symmetry factor scaffolds for Stage 4B subsets."""

from typing import Dict

import sympy as sp

from grut.hard_theory.s4_ctp_solver.three_loop_subset_flat import SubsetTopology


def compute_symmetry_factor(topology: SubsetTopology) -> Dict[str, object]:
    factors = {
        "scalar_triple_bubble": sp.Rational(1, 6),
        "figure_eight_times_bubble": sp.Rational(1, 4),
        "nested_double_loop_with_bubble": sp.Rational(1, 2),
        "sunset_extension_scalar": sp.Rational(1, 2),
    }
    if topology.topology_id not in factors:
        return {
            "topology_id": topology.topology_id,
            "symmetry_factor": None,
            "status": "unknown_topology",
            "promotes_claims": False,
        }
    return {
        "topology_id": topology.topology_id,
        "symmetry_factor": factors[topology.topology_id],
        "status": "structural_verified",
        "promotes_claims": False,
    }
