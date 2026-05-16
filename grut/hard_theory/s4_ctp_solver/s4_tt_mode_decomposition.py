"""TT mode decomposition on S4 (structural)."""

from typing import Dict


def define_tt_mode_decomposition() -> Dict[str, object]:
    return {
        "decomposition_id": "s4_tt_modes",
        "mode_structure": "harmonic_tensor_modes",
        "indices": ["l", "mode_label"],
        "status": "defined_structural",
        "promotes_claims": False,
    }
