"""Inject protected source candidates into scheme-stability audit flow."""

from __future__ import annotations

from typing import Dict, List


def inject_protected_sources(stage_p6: Dict[str, object]) -> List[Dict[str, object]]:
    injected: List[Dict[str, object]] = []
    for entry in stage_p6.get("registered_candidates", []):
        injected.append(
            {
                "candidate_id": entry.get("protected_source_candidate_id"),
                "source_type": entry.get("source_type"),
                "kernel_id": entry.get("kernel_id"),
                "locality_class": "nonlocal",
                "invariant_class": "anomaly_protected_nonlocal_kernel",
                "counterterm_nonmixing_verified": entry.get(
                    "counterterm_nonmixing_verified"
                )
                is True,
                "finite_extractability": entry.get("finite_extractability") is True,
                "coefficient_value": None,
                "physical_coefficient_computed": False,
                "promotes_claims": False,
            }
        )

    return injected
