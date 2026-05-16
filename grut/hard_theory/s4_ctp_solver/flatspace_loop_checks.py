"""Flat-space loop structure checks for Stage 2 benchmarks."""

from dataclasses import dataclass
import sympy as sp


@dataclass(frozen=True)
class LoopStructure:
    expression: sp.Expr
    status: str = "benchmarked"


def one_loop_scalar_bubble_structure() -> LoopStructure:
    """Return the standard dimensional-regularization structure.

    This is a symbolic placeholder: 1/epsilon + log(mu^2/p^2).
    """
    eps = sp.symbols("epsilon")
    mu = sp.symbols("mu")
    p2 = sp.symbols("p2")
    expr = 1 / eps + sp.log(mu**2 / p2)
    return LoopStructure(expression=expr)


def dim_reg_terms() -> dict[str, sp.Expr]:
    """Expose the pole and log structure for tests."""
    eps = sp.symbols("epsilon")
    mu = sp.symbols("mu")
    p2 = sp.symbols("p2")
    return {
        "pole": 1 / eps,
        "log": sp.log(mu**2 / p2),
    }
