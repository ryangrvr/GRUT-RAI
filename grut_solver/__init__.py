"""
GRUT Solver — Grand Responsive Universe Theory

A zero-parameter gravitational decoherence framework with adversarial self-testing.

Quick start:
    from grut_solver import GRUTSolver
    solver = GRUTSolver()
    result = solver.decoherence(m=1e-14, R=50e-9, l=100e-9, T_env=10e-3, P=1e-10)

Direct access:
    from grut_solver import lambda_grav, boundary_mass, compute_budget
"""

__version__ = "1.0.0"

from grut_solver.solver import GRUTSolver
from grut_solver.usl.gravitational import lambda_grav, boundary_mass, suppression_factor
from grut_solver.budget.total import compute_budget

__all__ = [
    "GRUTSolver",
    "lambda_grav",
    "boundary_mass",
    "suppression_factor",
    "compute_budget",
]
