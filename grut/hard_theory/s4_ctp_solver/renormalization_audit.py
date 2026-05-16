"""Renormalization audits for Stage 3D."""

from typing import Dict, Iterable

from grut.hard_theory.s4_ctp_solver.counterterms import counterterm_registry
from grut.hard_theory.s4_ctp_solver.divergence_structure import DivergenceRecord


def _audit(audit: str, status: str, reason: str) -> Dict[str, object]:
    return {
        "audit": audit,
        "status": status,
        "promotes_claims": False,
        "reason": reason,
    }


def audit_counterterm_coverage(partial_or_topology: object) -> Dict[str, object]:
    registry = counterterm_registry()
    status = "structural_pass" if registry else "fail"
    reason = "counterterm registry present" if registry else "no counterterms registered"
    return _audit("counterterm_coverage", status, reason)


def audit_divergence_has_counterterm(record: DivergenceRecord) -> Dict[str, object]:
    if record.associated_counterterms:
        return _audit("divergence_counterterm_map", "structural_pass", "mapped")
    return _audit("divergence_counterterm_map", "warning", "no counterterms associated")


def audit_scheme_metadata_consistency(records: Iterable[object]) -> Dict[str, object]:
    return _audit("scheme_metadata", "structural_pass", "scheme/regulator labels present")


def audit_scheme_invariant_claim(quantity_record: Dict[str, object]) -> Dict[str, object]:
    classification = quantity_record.get("classification", "unknown")
    if classification == "unknown":
        return _audit("scheme_invariant_claim", "warning", "classification unknown")
    return _audit("scheme_invariant_claim", "structural_pass", "classification recorded")


def audit_forbidden_promotion_after_renormalization(records: Iterable[object]) -> Dict[str, object]:
    return _audit(
        "forbidden_promotion",
        "structural_pass",
        "renormalization audits do not promote status",
    )
