"""Collect physical-intent statements for R from authoritative sources."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List
import re


_PRIMARY_SOURCES = [
    Path("theory/ZENODO_EPSILON_IDENTIFICATION.md"),
    Path("theory/hard_theory/GRUT_RAI_V3_S4_CTP_SOLVER_LADDER.md"),
    Path("grut/foundation/anomaly.py"),
    Path("README.md"),
    Path("ARCHITECTURE.md"),
]


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def _classify_statement(text: str) -> Dict[str, object]:
    lowered = text.lower()
    if "c_cosmo" in lowered and "c_final" in lowered and "r" in lowered:
        return {
            "classification": "anomaly_final_cosmological_ratio",
            "numerator_role": "C_Cosmo",
            "denominator_role": "C_Final",
            "explicit_roles": True,
        }

    if "causal" in lowered and "ctp" in lowered and "ratio" in lowered:
        return {
            "classification": "causal_ctp_response_ratio",
            "numerator_role": None,
            "denominator_role": None,
            "explicit_roles": False,
        }

    if "r log" in lowered and "weyl" in lowered and "ratio" in lowered:
        return {
            "classification": "curvature_anomaly_ratio",
            "numerator_role": None,
            "denominator_role": None,
            "explicit_roles": False,
        }

    return {
        "classification": "undefined_or_ambiguous",
        "numerator_role": None,
        "denominator_role": None,
        "explicit_roles": False,
    }


def _extract_explicit_r_ratio(text: str) -> List[str]:
    patterns = [
        r"R\s*=\s*\|?C_Cosmo\s*/\s*C_Final\|?",
        r"R\s*=\s*C_Cosmo\s*/\s*C_Final",
        r"R\s*=\s*C_Final\s*/\s*C_Cosmo",
    ]
    matches: List[str] = []
    for pattern in patterns:
        for match in re.findall(pattern, text):
            matches.append(match)
    return matches


def load_physical_intent_sources() -> List[Dict[str, object]]:
    statements: List[Dict[str, object]] = []

    for source in _PRIMARY_SOURCES:
        content = _read_text(source)
        if not content:
            continue

        for snippet in _extract_explicit_r_ratio(content):
            classification = _classify_statement(snippet)
            statements.append(
                {
                    "source": str(source),
                    "statement": snippet,
                    **classification,
                    "promotes_claims": False,
                }
            )

        if "ratio of forward and backward anomaly coefficients" in content:
            classification = {
                "classification": "anomaly_final_cosmological_ratio",
                "numerator_role": "C_Cosmo",
                "denominator_role": "C_Final",
                "explicit_roles": True,
            }
            statements.append(
                {
                    "source": str(source),
                    "statement": "ratio of forward and backward anomaly coefficients",
                    **classification,
                    "promotes_claims": False,
                }
            )

    if not statements:
        statements.append(
            {
                "source": "none",
                "statement": "no_explicit_intent_found",
                "classification": "undefined_or_ambiguous",
                "numerator_role": None,
                "denominator_role": None,
                "explicit_roles": False,
                "promotes_claims": False,
            }
        )

    return statements
