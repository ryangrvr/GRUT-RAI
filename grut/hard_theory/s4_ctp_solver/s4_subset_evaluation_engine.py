"""Evaluation engine for S4 scalar subset evaluations (Stage 4C)."""

from typing import Dict, List

import sympy as sp

from grut.hard_theory.s4_ctp_solver.three_loop_subset_s4_scalar import S4SubsetTopology
from grut.hard_theory.s4_ctp_solver.s4_subset_expansions import (
    evaluate_s4_subset_via_spectral,
    evaluate_s4_subset_via_curvature_expansion,
)
from grut.hard_theory.s4_ctp_solver.s4_curvature_corrections import (
    check_flat_limit,
    check_small_curvature_limit,
    check_scaling_behavior,
)


def evaluate_s4_subset(topology: S4SubsetTopology, radius: sp.Expr) -> Dict[str, object]:
    if topology.evaluation_type == "spectral_truncated":
        return evaluate_s4_subset_via_spectral(topology, topology.truncation_level, radius)
    return evaluate_s4_subset_via_curvature_expansion(topology, 2, radius)


def run_consistency_checks(result: Dict[str, object]) -> List[Dict[str, object]]:
    return [
        check_flat_limit(result),
        check_small_curvature_limit(result),
        check_scaling_behavior(result),
    ]
