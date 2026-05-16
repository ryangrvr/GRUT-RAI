"""Assemble the historical definition record for the R route."""

from typing import Dict, List


def _definition_sources(definitions: List[Dict[str, object]]) -> List[str]:
    sources: List[str] = []
    for definition in definitions:
        for source in definition.get("source_refs", []) or []:
            if source and source not in sources:
                sources.append(source)
    return sources


def _collect_definitions() -> List[Dict[str, object]]:
    return [
        {
            "definition_id": "r_cosmo_over_final_magnitude",
            "definition_text": "R = |C_Cosmo / C_Final|",
            "numerator_role": "C_Cosmo",
            "denominator_role": "C_Final",
            "signed": False,
            "source_refs": [
                "grut/foundation/anomaly.py",
                "theory/ZENODO_EPSILON_IDENTIFICATION.md",
                "ui/api/routes.py",
            ],
            "notes": "Magnitude-only convention retained for legacy reporting.",
        },
        {
            "definition_id": "r_cosmo_over_final_signed",
            "definition_text": "R = C_Cosmo / C_Final",
            "numerator_role": "C_Cosmo",
            "denominator_role": "C_Final",
            "signed": True,
            "source_refs": ["grut/foundation/anomaly.py"],
            "notes": "Signed ratio exposed for physical interpretation.",
        },
        {
            "definition_id": "r_forward_backward_anomaly_ratio",
            "definition_text": "R = forward/backward anomaly coefficient ratio",
            "numerator_role": "forward_anomaly",
            "denominator_role": "backward_anomaly",
            "signed": None,
            "source_refs": ["theory/ZENODO_EPSILON_IDENTIFICATION.md"],
            "notes": "CTP doubled-action wording without explicit kernel mapping.",
        },
    ]


def _definition_status(definitions: List[Dict[str, object]]) -> Dict[str, object]:
    if not definitions:
        return {"status": "missing", "ambiguity_reason": "no_definitions"}

    role_pairs = {
        (definition.get("numerator_role"), definition.get("denominator_role"))
        for definition in definitions
    }
    signed_variants = {definition.get("signed") for definition in definitions}

    if len(role_pairs) > 1:
        return {
            "status": "ambiguous",
            "ambiguity_reason": "multiple_role_pairs",
        }

    signed_variants = {value for value in signed_variants if value is not None}
    if len(signed_variants) > 1:
        return {
            "status": "ambiguous",
            "ambiguity_reason": "signed_vs_unsigned",
        }

    return {"status": "ok", "ambiguity_reason": None}


def build_r_definition_history() -> Dict[str, object]:
    definitions = _collect_definitions()
    status = _definition_status(definitions)
    sources = _definition_sources(definitions)

    definition_status = status.get("status")
    r_definition_found = bool(definitions)
    ambiguity_reason = status.get("ambiguity_reason")

    if definition_status == "missing":
        r_definition_source = None
    elif definition_status == "ambiguous":
        r_definition_source = "multiple_sources"
    else:
        r_definition_source = sources[0] if sources else None

    return {
        "r_definition_found": r_definition_found,
        "definition_status": definition_status,
        "ambiguity_reason": ambiguity_reason,
        "definitions": definitions,
        "definition_sources": sources,
        "r_definition_source": r_definition_source,
        "promotes_claims": False,
    }
