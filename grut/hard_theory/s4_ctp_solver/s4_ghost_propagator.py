"""Ghost propagator structural representation on S4."""

from typing import Dict

import sympy as sp


def build_ghost_propagator_structure(operator: Dict[str, object]) -> Dict[str, object]:
    l = sp.symbols("l", integer=True, nonnegative=True)
    a = sp.symbols("a", positive=True)
    vector_laplacian = sp.Function("lambda_vector")(l, a)
    denominator = vector_laplacian + sp.symbols("curvature_shift")
    vector_spectrum_tracking = {
        "basis": "vector_harmonics_placeholder",
        "eigenvalue": vector_laplacian,
        "degeneracy": sp.Function("D_vector")(l),
        "status": "structural_only",
    }

    return {
        "propagator_id": "s4_ghost_propagator_structural",
        "field": "ghost",
        "index_structure": "vector",
        "background": "S4",
        "representation": "spectral_truncated_or_symbolic",
        "operator_id": operator.get("operator_id"),
        "denominator": denominator,
        "vector_spectrum_tracking": vector_spectrum_tracking,
        "zero_mode_issue": "possible",
        "status": "structural_only",
        "promotes_claims": False,
    }
