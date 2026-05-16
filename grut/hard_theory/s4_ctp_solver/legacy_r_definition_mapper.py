"""Extract legacy R-definition candidates for protected-kernel mapping."""

from typing import Dict, List


_LEGACY_RATIO_TOKENS = (
    "c_cosmo",
    "c_final",
    "forward",
    "backward",
    "anomaly",
)


def _definition_roles(definition: Dict[str, object]) -> Dict[str, object]:
    numerator = definition.get("numerator_role")
    denominator = definition.get("denominator_role")
    text = (definition.get("definition_text") or "").lower()

    if numerator and denominator:
        return {
            "numerator_role": numerator,
            "denominator_role": denominator,
        }

    if "c_cosmo" in text and "c_final" in text:
        if "c_cosmo" in text.split("/")[0]:
            return {"numerator_role": "C_Cosmo", "denominator_role": "C_Final"}
        return {"numerator_role": "C_Final", "denominator_role": "C_Cosmo"}

    if "forward" in text and "backward" in text:
        return {
            "numerator_role": "forward_anomaly",
            "denominator_role": "backward_anomaly",
        }

    return {"numerator_role": None, "denominator_role": None}


def _inverse_definition(definition: Dict[str, object]) -> Dict[str, object]:
    return {
        "definition_id": f"inverse_of_{definition.get('definition_id', 'legacy')}",
        "definition_text": f"inverse({definition.get('definition_text')})",
        "numerator_role": definition.get("denominator_role"),
        "denominator_role": definition.get("numerator_role"),
        "signed": definition.get("signed"),
        "source_refs": definition.get("source_refs", []),
        "notes": "Inverted legacy definition for completeness.",
    }


def extract_legacy_definitions(definition_history: Dict[str, object]) -> List[Dict[str, object]]:
    definitions = definition_history.get("definitions", [])
    legacy: List[Dict[str, object]] = []

    for definition in definitions:
        text = (definition.get("definition_text") or "").lower()
        if not any(token in text for token in _LEGACY_RATIO_TOKENS):
            continue

        roles = _definition_roles(definition)
        legacy.append(
            {
                "definition_id": definition.get("definition_id"),
                "legacy_definition": definition.get("definition_text"),
                "numerator_role": roles.get("numerator_role"),
                "denominator_role": roles.get("denominator_role"),
                "signed": definition.get("signed"),
                "source_refs": definition.get("source_refs", []),
                "promotes_claims": False,
            }
        )

    has_inverse = any(
        entry.get("numerator_role") == "C_Final"
        and entry.get("denominator_role") == "C_Cosmo"
        for entry in legacy
    )
    has_forward = any(
        entry.get("numerator_role") == "C_Cosmo"
        and entry.get("denominator_role") == "C_Final"
        for entry in legacy
    )
    if has_forward and not has_inverse:
        inverse = _inverse_definition(
            {
                "definition_id": "legacy_c_cosmo_over_c_final",
                "definition_text": "C_Cosmo / C_Final",
                "numerator_role": "C_Cosmo",
                "denominator_role": "C_Final",
                "signed": False,
            }
        )
        legacy.append(
            {
                "definition_id": inverse.get("definition_id"),
                "legacy_definition": inverse.get("definition_text"),
                "numerator_role": inverse.get("numerator_role"),
                "denominator_role": inverse.get("denominator_role"),
                "signed": inverse.get("signed"),
                "source_refs": inverse.get("source_refs", []),
                "promotes_claims": False,
            }
        )

    return legacy
