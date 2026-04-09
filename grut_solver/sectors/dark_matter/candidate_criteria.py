"""Dark-matter candidate viability criteria."""

VIABILITY_CRITERIA = {
    "stability": "Lifetime > age of universe (~4.3e17 s). Decay channels must be suppressed.",
    "neutrality": "Electrically neutral (Q = 0). Color-neutral (SU(3) singlet).",
    "coupling": "Interaction cross-section < direct-detection bounds (~10^-46 cm^2 for ~100 GeV).",
    "relic_abundance": "Omega_DM h^2 = 0.120 +/- 0.001 (Planck 2018).",
    "structure": "Must be compatible with observed large-scale structure and halo profiles.",
}

CANDIDATE_TYPES = {
    "hidden_response_field": {
        "description": "A constitutive response field weakly coupled to SM via portal interactions.",
        "status": "TODO: not yet identified or constructed.",
    },
    "topological_soliton": {
        "description": "Stable topological excitation (defect) of the constitutive vacuum.",
        "status": "TODO: defect sector exists (Sector 4 legacy) but not adapted for DM.",
    },
    "sterile_neutrino": {
        "description": "Right-handed neutrino as warm/cold DM candidate.",
        "status": "TODO: connects to Sector 8 neutrino mass models.",
    },
}

def viability_checklist(candidate: dict) -> dict:
    """Check a candidate against all viability criteria. Returns pass/fail per criterion."""
    results = {}
    for criterion, description in VIABILITY_CRITERIA.items():
        results[criterion] = candidate.get(criterion, "NOT EVALUATED")
    return results
