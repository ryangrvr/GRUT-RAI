"""Define protection requirements for c_final_candidate sources."""

from typing import Dict, List


_PROTECTED_SCHEME_CLASSES = {
    "scheme_protected",
    "scheme_protected_candidate",
    "scheme_protected_benchmarked",
    "nonlocal_scheme_protected",
}

_REQUIRED_EVIDENCE = [
    "nonlocal_kernel_or_R_log_box_R_structure",
    "anomaly_channel_derivation",
    "scheme_independence_proof",
    "regulator_cancellation_trace",
    "counterterm_nonmixing_check",
]


def required_protection_evidence() -> List[str]:
    return list(_REQUIRED_EVIDENCE)


def _is_nonlocal(source: Dict[str, object]) -> bool:
    if source.get("locality_class") == "nonlocal":
        return True
    return source.get("protection_class") in {"nonlocal", "anomaly_protected"}


def _is_anomaly_protected(source: Dict[str, object]) -> bool:
    if source.get("protection_class") == "anomaly_protected":
        return True
    return source.get("anomaly_protected") is True


def _is_scheme_protected(source: Dict[str, object]) -> bool:
    for key in ("invariant_class", "scheme_sensitivity", "classification", "scheme_class"):
        if source.get(key) in _PROTECTED_SCHEME_CLASSES:
            return True
    return False


def current_protection_status(source: Dict[str, object]) -> Dict[str, bool]:
    return {
        "nonlocal": _is_nonlocal(source),
        "anomaly_protected": _is_anomaly_protected(source),
        "scheme_protected": _is_scheme_protected(source),
    }


def build_source_protection_requirement(
    source_id: str, source_record: Dict[str, object]
) -> Dict[str, object]:
    status = current_protection_status(source_record)
    return {
        "source_id": source_id,
        "current_status": status,
        "required_evidence": required_protection_evidence(),
        "can_be_reclassified_now": all(status.values()) is True,
        "promotes_claims": False,
    }
