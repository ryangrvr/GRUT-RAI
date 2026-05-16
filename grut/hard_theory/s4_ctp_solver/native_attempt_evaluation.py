"""Native attempt evaluation for Stage 5A."""

from typing import Dict, List

import sympy as sp

from grut.hard_theory.s4_ctp_solver.native_attempt_topology import NativeAttemptTopology
from grut.hard_theory.s4_ctp_solver.native_attempt_pipeline import run_native_attempt_pipeline
from grut.hard_theory.s4_ctp_solver.ctp_imaginary_scaffold import (
    emit_imaginary_causal_scaffold,
)


def evaluate_native_attempt(topology: NativeAttemptTopology) -> Dict[str, object]:
    steps = run_native_attempt_pipeline(topology, {})
    expression = sp.Symbol("native_attempt_expression")

    return {
        "topology_id": topology.topology_id,
        "evaluation_steps": steps,
        "expression": expression,
        "ctp_imaginary_scaffold": emit_imaginary_causal_scaffold(),
        "divergence_structure": "1/epsilon^3",
        "finite_part": "not_computed",
        "tensor_components": "none",
        "status": "native_attempt_internal",
        "limitations": [
            "spectral truncation",
            "no full contraction",
            "no convergence proof",
            "scheme dependence unresolved",
        ],
        "promotes_claims": False,
    }
