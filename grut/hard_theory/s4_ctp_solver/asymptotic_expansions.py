"""Asymptotic expansion scaffolds for Stage 3 partials."""

from typing import Tuple

import sympy as sp

from grut.hard_theory.s4_ctp_solver.diagram_topologies import DiagramTopology
from grut.hard_theory.s4_ctp_solver.three_loop_partials import (
    ThreeLoopPartial,
    base_verification_state,
)

WARNING = "Stage 3 partial: not a full 3-loop S4 CTP evaluation."


def _partial(
    topology: DiagramTopology,
    approximation_type: str,
    expression: sp.Expr,
    omitted_terms: Tuple[str, ...],
    assumptions: Tuple[str, ...],
) -> ThreeLoopPartial:
    return ThreeLoopPartial(
        topology=topology,
        background="S4",
        approximation_type=approximation_type,
        expression=expression,
        assumptions=assumptions,
        omitted_terms=omitted_terms,
        status="speculative_internal",
        verification_state=base_verification_state(),
        warning=WARNING,
        scheme_label=topology.scheme_label,
        regulator_label=topology.regulator_label,
    )


def large_radius_expansion(topology: DiagramTopology, order: int) -> ThreeLoopPartial:
    """Large-radius expansion placeholder for a topology."""
    expr = sp.Symbol(f"{topology.topology_id}_large_radius_order_{order}")
    omitted = (f"O(a^(-{order + 2}))",)
    assumptions = ("a >> 1", WARNING)
    return _partial(topology, "large_radius_expansion", expr, omitted, assumptions)


def small_curvature_expansion(topology: DiagramTopology, order: int) -> ThreeLoopPartial:
    """Small-curvature expansion placeholder for a topology."""
    expr = sp.Symbol(f"{topology.topology_id}_small_curvature_order_{order}")
    omitted = (f"O(R^{order + 1})",)
    assumptions = ("|R| small", WARNING)
    return _partial(topology, "small_curvature_expansion", expr, omitted, assumptions)


def heat_kernel_truncated_expansion(topology: DiagramTopology, max_a_n: int) -> ThreeLoopPartial:
    """Heat-kernel truncation placeholder for a topology."""
    expr = sp.Symbol(f"{topology.topology_id}_hk_truncated_a_{max_a_n}")
    omitted = (f"a_{max_a_n + 1} and higher",)
    assumptions = ("heat-kernel truncation", WARNING)
    return _partial(topology, "heat_kernel_truncated", expr, omitted, assumptions)


def flat_limit_projection(topology: DiagramTopology) -> ThreeLoopPartial:
    """Flat-limit projection placeholder for a topology."""
    expr = sp.Symbol(f"{topology.topology_id}_flat_limit")
    omitted = ("curvature corrections omitted",)
    assumptions = ("a -> infinity", WARNING)
    return _partial(topology, "flat_limit_check", expr, omitted, assumptions)
