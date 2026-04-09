"""
Sector 5 — Cosmology

Status: Partial / Conditional
Key failure: Dark-energy replacement (rho_eq < 0) is PERMANENTLY FAILED.
Key asset: Significant computational infrastructure for H(z), growth, lensing, rotation.

The underlying cosmology modules live in the original GRUT codebase (grut/)
and tools/ directories. This package provides a standardized interface
and honest status documentation.
"""

SECTOR_STATUS = "Partial / Conditional"
SECTOR_NAME = "Cosmology"

# ── Failed claims (PERMANENTLY WITHDRAWN) ───────────────────
FAILED_CLAIMS = {
    "dark_energy_replacement": {
        "route": "XII Alpha",
        "reason": "rho_eq < 0 is anti-accelerating; w = -1 wrong sign",
        "status": "PERMANENTLY_FAILED",
    },
    "late_universe_modification": {
        "reason": "No viable route found",
        "status": "FAILED",
    },
}

# ── Conditional content ─────────────────────────────────────
CONDITIONAL_CONTENT = {
    "dynamical_regulator": {
        "description": "Three-regime H*tau transition (XII Alpha revised)",
        "status": "conditional",
    },
    "early_universe_modification": {
        "description": "Modification at T ~ 10^12 K (XII Gamma)",
        "status": "conditional",
    },
}

# ── Nonclaims (explicit) ────────────────────────────────────
NONCLAIMS = [
    "Dark energy solution",
    "Cosmological closure",
    "Late-universe modification",
    "Precision CMB/BAO fit",
    "Natural screening length derivation",
]

# ── Working computational modules ───────────────────────────
LEGACY_MODULE_MAP = {
    "LCDM reference":         "grut/lcdm_reference.py",
    "Hubble tension metrics":  "grut/hubble_tension_metrics.py",
    "Bounce extension":        "grut/cosmological_bounce_extension.py",
    "Dark sector analysis":    "grut/dark_sector_extension.py",
    "Lensing calculator":      "grut/lensing.py",
    "Rotation curves":         "grut/rotation_curves.py",
    "Cosmological viability":  "grut/wg_range_viability_cosmological_audit.py",
    "Operators (H(z), growth)":"grut/operators.py",
    "Conversion (E(z))":       "grut/conversion.py",
}

TOOL_MAP = {
    "Cosmology sweep":        "tools/sweep_cosmology.py",
    "Hubble tension packet":  "tools/build_hubble_tension_packet.py",
    "Lensing pipeline":       "tools/run_lensing_packet.py",
    "Rotation batch":         "tools/run_rotation_batch.py",
}

# ── Component status ────────────────────────────────────────
COMPONENT_STATUS = {
    "background_evolution":     "implemented (H(z), E(z), Omega_m)",
    "growth_factor":            "implemented (D, f, fsigma8)",
    "lcdm_reference":           "implemented",
    "hubble_tension_metrics":   "implemented (residuals, RMS)",
    "lensing":                  "implemented (kappa, gamma, magnification)",
    "rotation_curves":          "implemented (v(r), residuals)",
    "bounce_analysis":          "implemented (softening only, not full bounce)",
    "dark_sector_analysis":     "implemented (framework; DE route FAILED)",
    "dark_energy_mechanism":    "PERMANENTLY FAILED (rho_eq < 0)",
    "perturbation_spectrum":    "NOT IMPLEMENTED",
    "cmb_bao_fit":              "NOT IMPLEMENTED",
    "screening_length":         "FREE PARAMETER (naturalness problem)",
    "early_universe_regulator": "CONDITIONAL (not validated)",
}
