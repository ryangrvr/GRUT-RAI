"""Assemble protected quotient selection report."""

from typing import Dict, List, Set, Tuple


def assemble_selection_report(
    ratios: List[Dict[str, object]],
    rule_reports: List[Dict[str, object]],
) -> Dict[str, object]:
    selected_union: Set[str] = set()
    selected_by_rule: List[Tuple[str, List[str]]] = []
    manual_choice = any(rule.get("manual_choice") is True for rule in rule_reports)

    for rule in rule_reports:
        selected = list(rule.get("selected_ratio_ids") or [])
        selected_by_rule.append((rule.get("rule_id"), selected))
        selected_union.update(selected)

    selection_rule_found = False
    selected_ratio_id = None

    if not manual_choice:
        if len(selected_union) == 1:
            selection_rule_found = True
            selected_ratio_id = next(iter(selected_union))
        else:
            selection_rule_found = False

    ratio_ids = []
    for ratio in ratios:
        ratio_id = ratio.get("ratio_id")
        if ratio_id and ratio_id not in ratio_ids:
            ratio_ids.append(ratio_id)

    unresolved = [ratio_id for ratio_id in ratio_ids if ratio_id != selected_ratio_id]

    if selection_rule_found:
        next_action = "advance_to_symbol_binding"
    else:
        next_action = "define_r_selection_principle"

    return {
        "selection_rule_found": selection_rule_found,
        "selected_ratio_id": selected_ratio_id,
        "unresolved_ratio_ids": unresolved,
        "selected_by_rule": [
            {
                "rule_id": rule_id,
                "selected_ratio_ids": selected,
                "promotes_claims": False,
            }
            for rule_id, selected in selected_by_rule
        ],
        "next_required_action": next_action,
        "promotes_claims": False,
    }
