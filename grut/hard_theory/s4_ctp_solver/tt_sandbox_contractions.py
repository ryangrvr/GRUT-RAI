"""Minimal symbolic tensor contractions for the sandbox."""

from typing import Dict, List


def run_minimal_sandbox_contractions() -> Dict[str, object]:
    contractions_run: List[Dict[str, str]] = [
        {
            "rule": "metric_trace_identity_check",
            "expression": "g^{mu nu} h_TT_{mu nu} -> 0",
        },
        {
            "rule": "tt_trace_removal_symbolic_check",
            "expression": "nabla^mu h_TT_{mu nu} -> 0",
        },
        {
            "rule": "projector_idempotence_symbolic_check",
            "expression": "P_TT * P_TT -> P_TT",
        },
        {
            "rule": "paired_index_placeholder",
            "expression": "mu paired with mu",
        },
    ]

    return {
        "sandbox_id": "tt_minimal_contractions",
        "contractions_run": contractions_run,
        "full_contractions_performed": False,
        "propagators_evaluated": False,
        "finite_parts_computed": False,
        "extraction_performed": False,
        "r_extracted": False,
        "unresolved_free_indices": [],
        "status": "sandbox_symbolic",
        "promotes_claims": False,
    }
