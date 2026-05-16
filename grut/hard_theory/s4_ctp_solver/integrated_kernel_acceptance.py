"""Acceptance evaluation for integrated nonlocal kernel candidates."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.nonlocal_kernel_acceptance import (
    evaluate_kernel_acceptance,
)


def evaluate_integrated_candidate(entry: Dict[str, object]) -> Dict[str, object]:
    candidate = entry.get("candidate", {})
    regulator_check = entry.get("regulator_check", {})
    ward_ctp_check = entry.get("ward_ctp_check", {})

    acceptance = evaluate_kernel_acceptance(candidate, regulator_check, ward_ctp_check)
    return {
        **entry,
        "acceptance": acceptance,
        "promotes_claims": False,
    }
