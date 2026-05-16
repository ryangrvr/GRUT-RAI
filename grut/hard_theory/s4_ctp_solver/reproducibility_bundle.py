"""Reproducibility bundle for external audits."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.audit_manifest import build_audit_manifest


def build_reproducibility_bundle() -> Dict[str, object]:
    manifest = build_audit_manifest()
    stage_statuses = {stage: entry.status for stage, entry in manifest.items()}
    module_list: List[str] = []
    for entry in manifest.values():
        module_list.extend(entry.implemented_modules)

    return {
        "package": "s4_ctp_solver",
        "stage_statuses": stage_statuses,
        "test_commands": [
            "pytest tests/hard_theory/s4_ctp_solver -q",
            "pytest -q",
        ],
        "module_list": sorted(set(module_list)),
        "benchmark_list": ["Stage 2 anomaly coefficients", "Stage 3B scalar spectra"],
        "known_limitations": [
            "no full 3-loop CTP evaluation",
            "partial/inconclusive crosschecks",
        ],
        "external_audit_notes": [
            "audits are structural and do not promote claims",
            "use refusal report for out-of-scope requests",
            "summary report helper available for Honesty Protocol",
        ],
        "can_compute_3loop": False,
    }
