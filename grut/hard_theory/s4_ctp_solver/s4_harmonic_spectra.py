"""Structural harmonic spectra definitions on S4."""

from typing import Dict, List

import sympy as sp

from grut.hard_theory.s4_ctp_solver.s4_spectral_basis import scalar_laplacian_eigenvalue


def _scalar_modes(radius: sp.Expr, max_l: int = 2) -> List[Dict[str, object]]:
    modes = []
    for l in range(max_l + 1):
        modes.append(
            {
                "l": l,
                "eigenvalue": scalar_laplacian_eigenvalue(l, radius),
                "status": "benchmarked_scalar",
            }
        )
    return modes


def _vector_modes(radius: sp.Expr, max_l: int = 2) -> List[Dict[str, object]]:
    lambda_vector_t = sp.Symbol("lambda_vector_T")
    lambda_vector_l = sp.Symbol("lambda_vector_L")
    return [
        {
            "l": l,
            "mode": "transverse",
            "eigenvalue": lambda_vector_t,
            "status": "structural_placeholder",
        }
        for l in range(1, max_l + 1)
    ] + [
        {
            "l": l,
            "mode": "longitudinal",
            "eigenvalue": lambda_vector_l,
            "status": "structural_placeholder",
        }
        for l in range(1, max_l + 1)
    ]


def _tensor_modes(radius: sp.Expr, max_l: int = 2) -> List[Dict[str, object]]:
    lambda_tensor_tt = sp.Symbol("lambda_tensor_TT")
    lambda_tensor_trace = sp.Symbol("lambda_tensor_trace")
    return [
        {
            "l": l,
            "mode": "TT_placeholder",
            "eigenvalue": lambda_tensor_tt,
            "status": "structural_placeholder",
        }
        for l in range(2, max_l + 1)
    ] + [
        {
            "l": l,
            "mode": "trace",
            "eigenvalue": lambda_tensor_trace,
            "status": "structural_placeholder",
        }
        for l in range(0, max_l + 1)
    ]


def define_s4_harmonic_spectra() -> Dict[str, object]:
    radius = sp.symbols("a", positive=True)
    scalar_modes = _scalar_modes(radius)
    vector_modes = _vector_modes(radius)
    tensor_modes = _tensor_modes(radius)

    return {
        "spectra_id": "s4_harmonic_spectra",
        "scalar_modes": scalar_modes,
        "vector_modes": vector_modes,
        "tensor_modes": tensor_modes,
        "background": "S4",
        "status": "defined_structural",
        "promotes_claims": False,
    }
