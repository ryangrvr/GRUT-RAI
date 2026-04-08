"""
GRUT Solver — General Relaxation Unified Theory

A zero-parameter gravitational decoherence framework with adversarial self-testing.

Usage:
    from grut_solver import GRUTSolver
    solver = GRUTSolver()
    result = solver.decoherence(m=1e-14, R=50e-9, l=100e-9, T_env=10e-3, P=1e-10)
"""

__version__ = "1.0.0"

from grut_solver.solver import GRUTSolver

__all__ = ["GRUTSolver"]
