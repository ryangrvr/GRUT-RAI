"""Controlled Stage 3 partial objects for 3-loop S4 CTP work."""

from dataclasses import dataclass
from typing import Dict, Tuple

import sympy as sp

from grut.hard_theory.s4_ctp_solver.diagram_topologies import DiagramTopology


@dataclass(frozen=True)
class ThreeLoopPartial:
    topology: DiagramTopology
    background: str
    approximation_type: str
    expression: sp.Expr
    assumptions: Tuple[str, ...]
    omitted_terms: Tuple[str, ...]
    status: str
    verification_state: Dict[str, bool]
    warning: str
    scheme_label: str
    regulator_label: str


def base_verification_state() -> Dict[str, bool]:
    return {
        "ward_identity_checked": False,
        "scheme_consistency_checked": False,
        "flat_limit_checked": False,
        "independent_replication": False,
    }
