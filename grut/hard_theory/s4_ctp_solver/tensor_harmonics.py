"""Tensor harmonic structural placeholders for Stage 3B."""

from dataclasses import dataclass
from typing import Tuple

import sympy as sp


@dataclass(frozen=True)
class TensorHarmonicRecord:
    harmonic_type: str
    eigenvalue: sp.Expr
    status: str
    evaluated: bool
    notes: Tuple[str, ...]


def scalar_harmonic_placeholder() -> TensorHarmonicRecord:
    return TensorHarmonicRecord(
        harmonic_type="scalar",
        eigenvalue=sp.Symbol("lambda_scalar"),
        status="structural_placeholder",
        evaluated=False,
        notes=("scalar harmonics use explicit spectral basis",),
    )


def transverse_vector_harmonic_placeholder() -> TensorHarmonicRecord:
    return TensorHarmonicRecord(
        harmonic_type="transverse_vector",
        eigenvalue=sp.Symbol("lambda_vector_T"),
        status="structural_placeholder",
        evaluated=False,
        notes=("no explicit contraction claim",),
    )


def transverse_traceless_tensor_harmonic_placeholder() -> TensorHarmonicRecord:
    return TensorHarmonicRecord(
        harmonic_type="transverse_traceless_tensor",
        eigenvalue=sp.Symbol("lambda_tensor_TT"),
        status="structural_placeholder",
        evaluated=False,
        notes=("no explicit contraction claim",),
    )
