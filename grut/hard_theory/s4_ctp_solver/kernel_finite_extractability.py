"""Assess finite coefficient extractability readiness for kernels."""

from __future__ import annotations

from typing import Dict


def evaluate_finite_extractability(
    candidate: Dict[str, object],
    nonmixing_report: Dict[str, object],
    stage11c: Dict[str, object],
) -> Dict[str, object]:
    benchmarks_pass = bool(stage11c.get("all_benchmarks_pass"))
    nonmixing_verified = bool(nonmixing_report.get("counterterm_nonmixing_verified"))
    coefficient_ok = candidate.get("coefficient") in {"symbolic_uncomputed", None}

    finite_extractability = bool(benchmarks_pass and nonmixing_verified and coefficient_ok)

    return {
        "kernel_id": candidate.get("kernel_id"),
        "finite_extractability": finite_extractability,
        "coefficient_status": "symbolic_extractable"
        if finite_extractability
        else "not_extractable",
        "coefficient_value": None,
        "promotes_claims": False,
    }
