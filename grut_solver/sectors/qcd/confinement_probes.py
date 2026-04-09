"""
Module 5: Confinement probes — exploratory diagnostics.

Status: SCAFFOLD. First-pass diagnostics for confinement-sensitive observables.
These are NOT full QCD results. They are computational entry points.
"""

# TODO: Implement string-tension extraction from Wilson loop area-law fit
# TODO: Implement static quark-antiquark potential V(r) = -alpha/r + sigma*r
# TODO: Implement Polyakov loop (finite-temperature confinement order parameter)
# TODO: Implement flux-tube profile measurement

IMPLEMENTATION_STATUS = {
    "wilson_area_law_scan": "implemented (toy lattice, exploratory)",
    "string_tension_extraction": "TODO",
    "static_potential_Vr": "TODO",
    "polyakov_loop": "TODO",
    "flux_tube_profile": "TODO",
}

NOTE = (
    "Confinement probes are scaffolded but not demonstrated. "
    "The Wilson loop toy lattice provides a computational framework; "
    "actual confinement requires Monte Carlo importance sampling on "
    "a physical SU(3) lattice action, which is beyond the current scope."
)
