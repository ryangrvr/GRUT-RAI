"""Hard guardrails for Stage 5C tensor placeholders."""

from dataclasses import asdict, is_dataclass
from typing import Any, Dict, List


FORBIDDEN_MARKERS = (
    "computed",
    "evaluated",
    "finite_part_computed",
    "tensor_propagator_evaluated",
    "full_contraction",
    "r_route_promoted",
)
ALLOWED_EXACT = {"not_evaluated", "not_computed"}


def _scan_value(value: Any, path: str, issues: List[str]) -> None:
    if is_dataclass(value):
        _scan_value(asdict(value), path, issues)
        return

    if isinstance(value, dict):
        for key, nested in value.items():
            if key == "evaluated" and nested is False:
                continue
            if key == "can_compute_full_3loop" and nested is False:
                continue
            _scan_value(nested, f"{path}.{key}" if path else str(key), issues)
        return

    if isinstance(value, (list, tuple, set)):
        for index, nested in enumerate(value):
            _scan_value(nested, f"{path}[{index}]", issues)
        return

    if isinstance(value, str):
        if value in ALLOWED_EXACT:
            return
        lowered = value.lower()
        for marker in FORBIDDEN_MARKERS:
            if marker in lowered:
                issues.append(f"forbidden_marker:{marker}@{path}")
        return


def enforce_tensor_placeholder_guard(result: Dict[str, object]) -> Dict[str, object]:
    issues: List[str] = []

    finite_part = result.get("finite_part")
    if finite_part and finite_part != "not_computed":
        issues.append("finite_part_computed")

    _scan_value(result, "", issues)

    tensor_flow = result.get("tensor_flow", {})
    if tensor_flow.get("status") not in {"tracked_not_contracted"}:
        issues.append("tensor_flow_status_changed")

    constraint_status = result.get("constraint_status", {})
    if constraint_status.get("status") not in {"constraint_applied_structural"}:
        issues.append("constraint_status_changed")

    return {
        "guard": "tensor_placeholder_guard",
        "status": "fail" if issues else "pass",
        "issues": issues,
        "promotes_claims": False,
    }
