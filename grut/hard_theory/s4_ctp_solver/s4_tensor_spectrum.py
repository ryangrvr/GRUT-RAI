"""S4 tensor spectral records for Stage 3C structural audits."""

from dataclasses import dataclass
from typing import Tuple

import sympy as sp

from grut.hard_theory.s4_ctp_solver.s4_spectral_basis import (
    scalar_laplacian_eigenvalue,
    scalar_harmonic_degeneracy,
)


@dataclass(frozen=True)
class TensorSpectralRecord:
    mode_type: str
    l: int
    radius: sp.Expr
    eigenvalue_expression: sp.Expr
    degeneracy_expression: sp.Expr
    status: str
    warning: str


def scalar_mode_record(l: int, radius: sp.Expr) -> TensorSpectralRecord:
    return TensorSpectralRecord(
        mode_type="scalar",
        l=l,
        radius=radius,
        eigenvalue_expression=scalar_laplacian_eigenvalue(l, radius),
        degeneracy_expression=scalar_harmonic_degeneracy(l),
        status="benchmarked_scalar",
        warning="",
    )


def transverse_vector_mode_record(l: int, radius: sp.Expr) -> TensorSpectralRecord:
    return TensorSpectralRecord(
        mode_type="transverse_vector",
        l=l,
        radius=radius,
        eigenvalue_expression=sp.Symbol("lambda_vector_T"),
        degeneracy_expression=sp.Symbol("degeneracy_vector_T"),
        status="structural_tensor_placeholder",
        warning="transverse vector spectrum not benchmarked",
    )


def transverse_traceless_tensor_mode_record(l: int, radius: sp.Expr) -> TensorSpectralRecord:
    return TensorSpectralRecord(
        mode_type="transverse_traceless_tensor",
        l=l,
        radius=radius,
        eigenvalue_expression=sp.Symbol("lambda_tensor_TT"),
        degeneracy_expression=sp.Symbol("degeneracy_tensor_TT"),
        status="symbolic_tensor_spectrum",
        warning="TT tensor spectrum not benchmarked",
    )


def tensor_mode_records(l: int, radius: sp.Expr) -> Tuple[TensorSpectralRecord, ...]:
    return (
        scalar_mode_record(l, radius),
        transverse_vector_mode_record(l, radius),
        transverse_traceless_tensor_mode_record(l, radius),
    )
