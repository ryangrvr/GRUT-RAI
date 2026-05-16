"""Tensor structure records for Stage 4D subsets."""

from dataclasses import dataclass
from typing import Tuple

import sympy as sp


@dataclass(frozen=True)
class TensorStructureRecord:
    index_structure: sp.Expr
    symmetry_properties: Tuple[str, ...]
    tt_constraints: Tuple[str, ...]
    status: str


def tt_propagator_placeholder() -> TensorStructureRecord:
    return TensorStructureRecord(
        index_structure=sp.Symbol("P_TT_mu_nu_rho_sigma"),
        symmetry_properties=("mu<->nu", "rho<->sigma", "(mu nu)<->(rho sigma)"),
        tt_constraints=("transverse", "traceless"),
        status="symbolic_tensor_structure",
    )


def graviton_vertex_structure() -> TensorStructureRecord:
    return TensorStructureRecord(
        index_structure=sp.Symbol("V_graviton"),
        symmetry_properties=("vertex_symmetry",),
        tt_constraints=("transverse", "traceless"),
        status="symbolic_tensor_structure",
    )


def index_contraction_structure() -> TensorStructureRecord:
    return TensorStructureRecord(
        index_structure=sp.Symbol("C_mu_nu_rho_sigma"),
        symmetry_properties=("contraction_placeholder",),
        tt_constraints=("transverse", "traceless"),
        status="symbolic_tensor_structure",
    )
