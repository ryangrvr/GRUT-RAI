"""Index repair proposals for TT contraction readiness."""

from typing import Dict, List


def repair_tt_index_structure(readiness_output: Dict[str, object]) -> Dict[str, object]:
    index_structure = readiness_output.get("index_structure", {})
    free_indices = list(index_structure.get("free_indices", []))
    repairs_proposed: List[str] = []

    if not index_structure.get("complete"):
        repairs_proposed.append("complete_index_pairing")
    if free_indices:
        repairs_proposed.append("resolve_free_indices")
    if not index_structure.get("tt_constraints_respected"):
        repairs_proposed.append("restore_tt_constraints")

    illegal_free_indices_remaining = bool(free_indices)

    return {
        "repair": "tt_index_structure",
        "repairs_proposed": repairs_proposed,
        "illegal_free_indices_remaining": illegal_free_indices_remaining,
        "status": "repair_proposed",
        "contractions_performed": False,
        "promotes_claims": False,
    }
