"""Extract the dominant physical intent classification for R."""

from typing import Dict, List


_VALID_CLASSES = {
    "anomaly_final_cosmological_ratio",
    "causal_ctp_response_ratio",
    "curvature_anomaly_ratio",
}


def extract_physical_intent(statements: List[Dict[str, object]]) -> Dict[str, object]:
    classes = []
    explicit_roles = False
    sources: List[str] = []

    for statement in statements:
        classification = statement.get("classification")
        if classification in _VALID_CLASSES:
            classes.append(classification)
        if statement.get("explicit_roles") is True:
            explicit_roles = True
        source = statement.get("source")
        if source and source not in sources:
            sources.append(source)

    unique_classes = sorted(set(classes))

    if not unique_classes:
        return {
            "intent_classification": "undefined_or_ambiguous",
            "explicit_roles": False,
            "source_support": sources,
            "promotes_claims": False,
        }

    if len(unique_classes) > 1:
        return {
            "intent_classification": "conflicting",
            "explicit_roles": False,
            "source_support": sources,
            "conflicting_classes": unique_classes,
            "promotes_claims": False,
        }

    return {
        "intent_classification": unique_classes[0],
        "explicit_roles": explicit_roles,
        "source_support": sources,
        "promotes_claims": False,
    }
