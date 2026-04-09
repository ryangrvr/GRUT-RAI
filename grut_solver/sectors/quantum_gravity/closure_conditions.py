"""Exact closure conditions for quantum gravity sector."""

CLOSURE_CONDITIONS = [
    "Quantized gravitational sector (graviton or equivalent mode structure)",
    "UV completion (finite predictions at Planck scale)",
    "Self-consistent backreaction (metric responds to quantized matter)",
    "Black-hole information resolution",
    "Recovery of classical GR in the appropriate limit",
]

def closure_status() -> dict:
    """Return closure conditions with status."""
    return {
        "conditions": CLOSURE_CONDITIONS,
        "n_met": 0,
        "n_total": len(CLOSURE_CONDITIONS),
        "status": "OPEN (0/5 conditions met)",
        "note": "This is the deepest open gate in the GRUT program.",
    }
