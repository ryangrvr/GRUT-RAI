"""Extended TT projector representation in harmonic space (structural)."""

from typing import Dict, List


def extend_tt_projector() -> Dict[str, object]:
    properties: List[str] = ["transverse", "traceless", "idempotent_placeholder"]
    return {
        "projector_id": "tt_projector_extended",
        "properties": properties,
        "representation": "harmonic_space_structural",
        "status": "structural_only",
        "promotes_claims": False,
    }
