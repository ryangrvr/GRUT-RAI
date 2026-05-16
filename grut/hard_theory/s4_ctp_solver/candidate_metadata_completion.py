"""Complete metadata fields for coefficient candidates."""

from typing import Dict, List, Tuple

from grut.hard_theory.s4_ctp_solver.candidate_metadata_schema import (
    required_candidate_metadata_fields,
)


def _derive_renormalization_structure(stage11e: Dict[str, object]) -> str | None:
    attempts = stage11e.get("attempts", {})
    results = attempts.get("results", []) if isinstance(attempts, dict) else []

    scheme_ids = {result.get("scheme_id") for result in results if result.get("scheme_id")}
    regulators = {
        result.get("default_regulator")
        for result in results
        if result.get("default_regulator")
    }
    if len(scheme_ids) == 1 and len(regulators) == 1:
        return f"{next(iter(scheme_ids))}:{next(iter(regulators))}"
    return None


def _default_metadata(candidate_key: str) -> Dict[str, object]:
    if candidate_key == "nonlocal_scheme_protected_candidate":
        return {
            "tensor_origin_class": None,
            "loop_order": 3,
            "regulator_dependence_class": None,
            "renormalization_structure": None,
            "invariant_class": "scheme_protected",
            "locality_class": "nonlocal",
            "scheme_class_source": "stage12b",
            "cancellation_inputs_available": None,
        }
    if candidate_key == "scheme_fragile_candidate":
        return {
            "tensor_origin_class": None,
            "loop_order": 3,
            "regulator_dependence_class": None,
            "renormalization_structure": None,
            "invariant_class": "scheme_fragile",
            "locality_class": "local",
            "scheme_class_source": "stage12b",
            "cancellation_inputs_available": None,
        }
    if candidate_key == "c_cosmo_candidate":
        return {
            "tensor_origin_class": None,
            "loop_order": 3,
            "regulator_dependence_class": None,
            "renormalization_structure": None,
            "invariant_class": "scheme_fragile",
            "locality_class": "local",
            "scheme_class_source": "stage12b",
            "cancellation_inputs_available": None,
        }
    return {
        "tensor_origin_class": None,
        "loop_order": 3,
        "regulator_dependence_class": None,
        "renormalization_structure": None,
        "invariant_class": "scheme_fragile",
        "locality_class": "local",
        "scheme_class_source": "stage12b",
        "cancellation_inputs_available": None,
    }


def _missing_fields(candidate: Dict[str, object], required: List[str]) -> List[str]:
    missing: List[str] = []
    for field in required:
        if field not in candidate or candidate.get(field) is None:
            missing.append(field)
    return missing


def complete_candidate_metadata(
    registry: Dict[str, object],
    stage11e: Dict[str, object],
    diagnostic: Dict[str, object],
) -> Dict[str, object]:
    required_fields = required_candidate_metadata_fields()
    candidate_buckets = registry.get("candidate_buckets", {})
    renorm_structure = _derive_renormalization_structure(stage11e)
    cancellation_available = bool(
        stage11e.get("attempts", {}).get("results", [])
        if isinstance(stage11e.get("attempts", {}), dict)
        else []
    )

    missing_fields: List[str] = []

    for candidate_key, candidate in candidate_buckets.items():
        if not isinstance(candidate, dict):
            continue

        defaults = _default_metadata(candidate_key)
        defaults["renormalization_structure"] = renorm_structure
        defaults["regulator_dependence_class"] = defaults.get("regulator_dependence_class")
        defaults["cancellation_inputs_available"] = cancellation_available

        for field, value in defaults.items():
            candidate.setdefault(field, value)

        missing_fields.extend(_missing_fields(candidate, required_fields))

    metadata_completed = not missing_fields

    return {
        "registry": registry,
        "metadata_completed": metadata_completed,
        "missing_fields": sorted(set(missing_fields)),
        "promotes_claims": False,
    }
