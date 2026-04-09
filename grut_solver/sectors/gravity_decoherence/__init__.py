"""
Sector 3 — Gravitational Decoherence

Status: Predictive, zero-parameter, experimentally untested
Claim: GRUT predicts intrinsic gravitational decoherence with zero free parameters.

This sector is a thin interface layer over the existing grut_solver core modules.
The substance lives in grut_solver/usl/, grut_solver/budget/, grut_solver/kill/,
and grut_solver/experiments/. This package provides standardized access.
"""

SECTOR_STATUS = "Predictive, zero-parameter, experimentally untested"
SECTOR_NAME = "Gravitational Decoherence"

# ── Canonical module map ────────────────────────────────────
# This documents WHERE each capability lives in the main package.

MODULE_MAP = {
    "USL rate":              "grut_solver.usl.gravitational.lambda_grav",
    "Geometry correction":   "grut_solver.usl.gravitational.suppression_factor",
    "Boundary mass":         "grut_solver.usl.gravitational.boundary_mass",
    "Anomaly channel":       "grut_solver.usl.anomaly.lambda_anomaly",
    "Anomaly crossover":     "grut_solver.usl.anomaly.two_channel_rate",
    "Scaling laws":          "grut_solver.usl.scaling",
    "Validity envelope":     "grut_solver.usl.validity",
    "Emergent timescales":   "grut_solver.usl.emergent_scales",
    "Many-body (Bell/GHZ)":  "grut_solver.usl.many_body",
    "Gas channel":           "grut_solver.budget.gas.lambda_gas",
    "Blackbody channel":     "grut_solver.budget.blackbody",
    "Full budget":           "grut_solver.budget.total.compute_budget",
    "Uncertainty budget":    "grut_solver.budget.total.budget_with_uncertainty",
    "Systematic floor":      "grut_solver.budget.systematic",
    "Unknown floor":         "grut_solver.budget.unknown_floor",
    "Kill framework":        "grut_solver.kill.model_comparison",
    "Competing models":      "grut_solver.experiments.competing_models",
    "Platforms":             "grut_solver.experiments.platforms",
    "Figures":               "grut_solver.figures",
    "Full solver":           "grut_solver.solver.GRUTSolver",
}

# ── Convenience re-exports ──────────────────────────────────
from grut_solver.usl.gravitational import lambda_grav, suppression_factor, boundary_mass
from grut_solver.usl.anomaly import lambda_anomaly, c_final, r_anomaly
from grut_solver.usl.many_body import entanglement_discriminant, lambda_ghz_3
from grut_solver.budget.total import compute_budget
from grut_solver.kill.model_comparison import run_all_kill_tests, kill_summary
