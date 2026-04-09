"""Convergence / near-unification metrics."""
from grut_solver.sectors.unification.rg_diagnostics import find_closest_approach

GRUT_MODIFICATION_STATUS = {
    "question": "Does the GRUT constitutive structure modify SM running?",
    "status": "OPEN",
    "note": "No computation performed. Standard SM running used as baseline.",
}

def unification_summary() -> dict:
    """Summary of unification status."""
    closest = find_closest_approach()
    return {
        "closest_approach_GeV": closest["mu"],
        "minimum_spread": closest["spread"],
        "sm_unifies": False,
        "grut_modifies_running": "OPEN",
        "note": closest["note"],
    }
