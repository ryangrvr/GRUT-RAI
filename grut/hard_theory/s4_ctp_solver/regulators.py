"""Regulator placeholders for the S4 CTP scaffold."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Regulator:
    name: str
    description: str


def dimensional_regularization() -> Regulator:
    return Regulator(
        name="dimensional",
        description="Dimensional regularization placeholder.",
    )


def heat_kernel_cutoff() -> Regulator:
    return Regulator(
        name="heat_kernel_cutoff",
        description="Heat-kernel cutoff placeholder.",
    )


def zeta_regularization() -> Regulator:
    return Regulator(
        name="zeta",
        description="Zeta-function regularization placeholder.",
    )
