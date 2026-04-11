"""
Sector 4 — Gravity

Status: Partial
Identity: Matter/organization theory within standard Einstein gravity.

This sector documents the gravity-facing results of the GRUT program,
including locked negative results (TOV interior worsens) and frozen routes
(singularity resolution failed). The novel predictive content lives in
Sector 3 (gravitational decoherence).

The underlying computational modules live in the original GRUT codebase
(grut/tov_interior.py, grut/collapse.py, etc.), not in grut_solver/.
This package provides a standardized interface and status documentation.
"""

SECTOR_STATUS = "Partial (expanded)"
SECTOR_NAME = "Gravity"
GRAVITY_IDENTITY = "Matter/organization theory within standard Einstein gravity"

# ── Locked numerical results (from program_state.py) ────────
LOCKED_RESULTS = {
    "f_R_eq_static": -17.71,           # Static scalar-only TOV metric function
    "m_R_eq_static": 3.118,            # Mass function at R_eq [km]
    "A_Schw_reference": -5.0,           # Schwarzschild baseline
    "A_crit_dynamic": 0.93,             # Critical processing amplitude
    "weak_field_correction": 1e-16,     # delta_beta ~ 10^-16 (observationally silent)
    "singularity_routes_tested": 10,
    "singularity_routes_succeeded": 0,
}

# ── Status of sub-components ────────────────────────────────
COMPONENT_STATUS = {
    "semiclassical_coupling":       "demonstrated",
    "static_tov_interior":          "demonstrated (negative result, LOCKED)",
    "dynamic_interior":             "demonstrated (transient only)",
    "singularity_resolution":       "FAILED (10 routes, all frozen)",
    "weak_field_exterior":          "constrained (observationally silent)",
    "gravitational_decoherence":    "see Sector 3 (predictive)",
    "graviton":                     "OPEN (not present)",
    "full_backreaction":            "OPEN (not closed)",
    "uv_completion":                "OPEN (not present)",
    # ── Direction 2: Constitutive Gravity ──
    "constitutive_gravity":          "EXPLORED (Bianchi gate: naive FAILS, projected PASSES)",
    "gw_constitutive":               "COMPUTED (observationally silent for both tau candidates)",
    "qnm_constitutive":              "COMPUTED (shift ~ 10^-40, unobservable)",
    "singularity_constitutive":      "COMPUTED (regularizes at Planck time, bouncing cosmology)",
    "cosmological_memory":           "COMPUTED (negligible at late times with canonical tau)",
    # ── Direction 1: Stochastic Gravity ──
    "stochastic_gravity":            "SCAFFOLDED (noise kernel computed, connects to Sector 3)",
    "einstein_langevin":             "CONSISTENT (automatic from CTP axiom)",
}

# ── New Directions (2025) ──────────────────────────────────
NEW_DIRECTIONS = {
    "direction_2_constitutive": {
        "equation": "G_mn + tau_grav P_mn^ab u^l nabla_l G_ab = 8piG T_mn",
        "status": "Viable (projected form passes Bianchi)",
        "positive_results": ["Singularity regularization at Planck scale"],
        "negative_results": ["GW/QNM effects observationally dead", "No DE help at canonical tau"],
    },
    "direction_1_stochastic": {
        "equation": "<G_mn> + tau D_t <G_mn> = 8piG <T_mn> + xi_mn",
        "status": "Consistent (automatic from CTP, zero new structure)",
        "positive_results": ["Connects USL to metric fluctuations", "UV regulation from tau"],
        "negative_results": ["Stochastic decoherence subdominant to Diosi"],
    },
}

# ── Module map (original codebase, not grut_solver) ─────────
LEGACY_MODULE_MAP = {
    "TOV interior":         "grut/tov_interior.py",
    "Numerical monopole":   "grut/numerical_monopole.py",
    "Dynamical collapse":   "grut/collapse.py",
    "Metric deficit":       "grut/metric_deficit.py",
    "Dynamical interior":   "grut/dynamical_interior.py",
    "Self-consistent coupling": "grut/self_consistent_coupling.py",
    "Weak-field constraint": "grut/weak_field_tau_constraint.py",
    "Singularity phenom":   "grut/singularity_resolution_phenomenology.py",
}

# ── Link to Sector 3 ────────────────────────────────────────
SECTOR_3_LINK = {
    "module": "grut_solver.sectors.gravity_decoherence",
    "note": "The novel predictive content for gravity lives in Sector 3.",
}
