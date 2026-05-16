"""Map partition divergences to counterterms (structural only)."""

from typing import Dict, List


_COUNTERTERMS = [
    "cosmological_constant",
    "Einstein_Hilbert",
    "R_squared",
    "Ricci_squared",
    "Riemann_squared",
    "Weyl_squared",
    "Euler_density",
    "box_R",
]


def map_partition_divergences_to_counterterms(
    divergences: Dict[str, object],
) -> Dict[str, object]:
    identified = divergences.get("divergences_identified", [])
    mapped: List[str] = []
    unmapped: List[str] = []

    if identified:
        mapped = ["cosmological_constant", "Einstein_Hilbert"]
        unmapped = [item for item in identified if item not in mapped]

    if not identified:
        mapping_status = "unmapped"
    elif unmapped:
        mapping_status = "partial"
    else:
        mapping_status = "mapped_structural"

    return {
        "mapped_counterterms": mapped,
        "unmapped_divergences": unmapped,
        "mapping_status": mapping_status,
        "promotes_claims": False,
    }
