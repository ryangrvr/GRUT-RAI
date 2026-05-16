"""Diagnose Stage 12C legality failures for R."""

from typing import Dict, List, Tuple

from grut.hard_theory.s4_ctp_solver.r_cancellation_check import check_r_cancellation
from grut.hard_theory.s4_ctp_solver.r_structure_compatibility import (
    check_r_structure_compatibility,
)
from grut.hard_theory.s4_ctp_solver.r_legality_audit import audit_r_legality_inputs
from grut.hard_theory.s4_ctp_solver.r_legality_decision import decide_r_legality


_ALLOWED_NONLOCAL = {"nonlocal", "anomaly_protected"}


def _classification_map(classifications: Dict[str, object]) -> Dict[str, str]:
    entries = classifications.get("classifications", [])
    if not isinstance(entries, list):
        return {}

    result = {}
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        candidate_key = entry.get("candidate_key")
        classification = entry.get("classification")
        if candidate_key:
            result[candidate_key] = classification
    return result


def _scheme_class(candidate: Dict[str, object], mapping: Dict[str, str]) -> str | None:
    if candidate.get("classification"):
        return candidate.get("classification")
    candidate_key = candidate.get("candidate_key")
    return mapping.get(candidate_key)


def _protection_class(candidate: Dict[str, object]) -> str | None:
    return candidate.get("protection_class")


def _is_missing_metadata(pair: Dict[str, object], structural: Dict[str, object]) -> bool:
    numerator = pair.get("numerator", {})
    denominator = pair.get("denominator", {})

    if numerator.get("candidate_key") is None or denominator.get("candidate_key") is None:
        return True
    if pair.get("renorm_structure_shared") is None:
        return True
    if structural.get("reason", "").startswith("missing_"):
        return True
    if numerator.get("renorm_structure_id") is None:
        return True
    if denominator.get("renorm_structure_id") is None:
        return True
    return False


def _categorize_failures(
    pair: Dict[str, object],
    numerator_scheme: str | None,
    denominator_scheme: str | None,
    structural: Dict[str, object],
    cancellation: Dict[str, object],
) -> List[str]:
    failures: List[str] = []

    if numerator_scheme == "scheme_fragile":
        failures.append("numerator_scheme_fragile")
    if denominator_scheme == "scheme_fragile":
        failures.append("denominator_scheme_fragile")

    numerator_protection = _protection_class(pair.get("numerator", {}))
    denominator_protection = _protection_class(pair.get("denominator", {}))
    if (numerator_protection in _ALLOWED_NONLOCAL) ^ (
        denominator_protection in _ALLOWED_NONLOCAL
    ):
        failures.append("mixed_local_nonlocal")

    if pair.get("renorm_structure_shared") is False:
        failures.append("renormalization_mismatch")
    elif structural.get("reason") == "renorm_structure_mismatch":
        failures.append("renormalization_mismatch")

    if cancellation.get("cancellation_valid") is False:
        failures.append("cancellation_failure")

    if _is_missing_metadata(pair, structural):
        failures.append("missing_metadata")

    return failures


def _minimal_repair(failure_reasons: List[str]) -> str:
    if "missing_metadata" in failure_reasons:
        return "add metadata"
    if "mixed_local_nonlocal" in failure_reasons:
        return "isolate nonlocal source"
    if "numerator_scheme_fragile" in failure_reasons or "denominator_scheme_fragile" in failure_reasons:
        return "remove fragile local term"
    if "renormalization_mismatch" in failure_reasons:
        return "reclassify candidate"
    if "cancellation_failure" in failure_reasons:
        return "no legal repair possible"
    return "no legal repair possible"


def diagnose_r_legality_repair(
    classifications: Dict[str, object],
    candidate_pairs: List[Dict[str, object]],
) -> Dict[str, object]:
    mapping = _classification_map(classifications)
    pair_reports: List[Dict[str, object]] = []
    failure_reasons: List[str] = []

    for pair in candidate_pairs:
        structural = check_r_structure_compatibility(pair)
        cancellation = check_r_cancellation(pair)
        audit = audit_r_legality_inputs(pair, structural, cancellation)
        decision = decide_r_legality(pair, structural, cancellation, audit)

        numerator = pair.get("numerator", {})
        denominator = pair.get("denominator", {})
        numerator_scheme = _scheme_class(numerator, mapping)
        denominator_scheme = _scheme_class(denominator, mapping)

        rejection_reason = (
            "eligible" if decision.get("r_legal") else decision.get("reason")
        )

        failures = _categorize_failures(
            pair, numerator_scheme, denominator_scheme, structural, cancellation
        )
        failure_reasons.extend(failures)

        pair_reports.append(
            {
                "numerator": numerator.get("candidate_key"),
                "denominator": denominator.get("candidate_key"),
                "numerator_scheme_class": numerator_scheme,
                "denominator_scheme_class": denominator_scheme,
                "structural_compatibility": structural,
                "cancellation_readiness": cancellation,
                "rejection_reason": rejection_reason,
                "failure_categories": failures,
                "promotes_claims": False,
            }
        )

    unique_failures = sorted(set(failure_reasons))
    minimal_repair = _minimal_repair(unique_failures)

    return {
        "stage": "12C-R1",
        "status": "r_legality_repair_diagnostic",
        "candidate_pairs_examined": len(candidate_pairs),
        "failure_reasons": unique_failures,
        "minimal_repair": minimal_repair,
        "r_computation_allowed": False,
        "promotes_claims": False,
        "pair_reports": pair_reports,
    }
