"""Gate 3 Mathematica/HypExp JSON importer with strict validation."""

from __future__ import annotations

from dataclasses import asdict
import json
from pathlib import Path
from typing import Any, Dict, Optional

import sympy as sp

from grut.hard_theory.s4_ctp_solver.gate3_euler_coefficient_extraction import (
    EulerCoefficientResult,
)

_REQUIRED_KEYS = {
    "coefficient_name",
    "value",
    "epsilon_pole",
    "finite_part",
    "scheme",
    "regulator",
    "channel",
    "projection",
    "protected",
    "source_tool",
    "source_file",
    "manual_target_matching",
    "status",
    "blocker",
}


def _is_resolved_scalar(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return False
    if isinstance(value, (int, float)):
        return True
    if isinstance(value, str):
        return False
    if isinstance(value, sp.Basic):
        return bool(value.is_number) and not value.has(sp.Integral, sp.Derivative)
    return False


def _is_resolved_pole_term(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return False
    if isinstance(value, (int, float)):
        return True
    if isinstance(value, str):
        return False
    if isinstance(value, sp.Basic):
        epsilon = sp.Symbol("epsilon")
        return value.free_symbols <= {epsilon} and not value.has(sp.Integral, sp.Derivative)
    return False


def _parse_symbolic_field(value: Any) -> Any:
    if value is None:
        return None
    if isinstance(value, (int, float, bool)):
        return value
    if isinstance(value, str):
        stripped = value.strip()
        if stripped == "":
            return None
        try:
            return sp.sympify(stripped)
        except Exception:
            return stripped
    return value


def _validate_payload(payload: Dict[str, Any]) -> list[str]:
    errors: list[str] = []

    missing = sorted(_REQUIRED_KEYS - set(payload.keys()))
    if missing:
        errors.append(f"missing_required_keys:{','.join(missing)}")
        return errors

    if not payload.get("scheme"):
        errors.append("missing_scheme")
    if not payload.get("regulator"):
        errors.append("missing_regulator")
    if payload.get("channel") != "Euler":
        errors.append("non_euler_channel")
    if payload.get("projection") != "round_s4_euler":
        errors.append("non_round_s4_projection")
    if payload.get("manual_target_matching") is True:
        errors.append("manual_target_matching_true")
    if payload.get("protected") is False:
        errors.append("unprotected_coefficient")

    status = payload.get("status")
    if status not in {"computed", "blocked", "scheme_fragile", "invalid"}:
        errors.append("invalid_status")

    if status == "computed":
        if payload.get("value") in (None, ""):
            errors.append("computed_missing_value")
        if payload.get("finite_part") in (None, ""):
            errors.append("computed_missing_finite_part")

    if status == "blocked" and not payload.get("blocker"):
        errors.append("blocked_missing_blocker")

    return errors


def import_mathematica_coefficient(json_path: str) -> Dict[str, Any]:
    """Import and validate one Mathematica coefficient JSON artifact."""
    path = Path(json_path)
    raw: Dict[str, Any]
    try:
        raw = json.loads(path.read_text())
    except Exception as exc:
        return {
            "accepted": False,
            "status": "rejected",
            "errors": [f"json_read_failure:{exc}"],
            "result": None,
            "raw": None,
            "source_path": str(path),
        }

    errors = _validate_payload(raw)
    if errors:
        return {
            "accepted": False,
            "status": "rejected",
            "errors": errors,
            "result": None,
            "raw": raw,
            "source_path": str(path),
        }

    result = EulerCoefficientResult(
        coefficient_name=str(raw["coefficient_name"]),
        channel=str(raw["channel"]),
        value=_parse_symbolic_field(raw["value"]),
        epsilon_pole=_parse_symbolic_field(raw["epsilon_pole"]),
        finite_part=_parse_symbolic_field(raw["finite_part"]),
        scheme=str(raw["scheme"]),
        regulator=str(raw["regulator"]),
        protected=bool(raw["protected"]),
        status=str(raw["status"]),
        blocker=None if raw["blocker"] is None else str(raw["blocker"]),
        local_vs_nonlocal_role="protected_nonlocal_R_log_box_R",
        round_s4_projection=True,
        euler_only_condition_w2_zero=True,
        massless_or_conformal_limit="imported_from_mathematica",
        manual_target_matched=bool(raw["manual_target_matching"]),
        provenance=f"{raw['source_tool']}:{raw['source_file']}",
    )

    if result.status == "computed":
        computed_errors: list[str] = []
        if not _is_resolved_scalar(result.value):
            computed_errors.append("computed_value_not_resolved_scalar")
        if not _is_resolved_scalar(result.finite_part):
            computed_errors.append("computed_finite_part_not_resolved_scalar")
        if result.epsilon_pole is not None and not _is_resolved_pole_term(result.epsilon_pole):
            computed_errors.append("computed_epsilon_pole_not_resolved_scalar")
        if computed_errors:
            return {
                "accepted": False,
                "status": "rejected",
                "errors": computed_errors,
                "result": None,
                "raw": raw,
                "source_path": str(path),
            }

    return {
        "accepted": True,
        "status": "imported",
        "errors": [],
        "result": result,
        "result_dict": asdict(result),
        "raw": raw,
        "source_path": str(path),
    }
