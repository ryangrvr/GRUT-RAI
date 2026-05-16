"""Extract nonlocal form markers from prior stage payloads."""

from __future__ import annotations

from typing import Dict, Iterable, Iterator, List, Tuple


def _normalize(text: str) -> str:
    return "".join(text.lower().split())


def _iter_strings(value: object, path: str = "") -> Iterator[Tuple[str, str]]:
    if isinstance(value, str):
        yield path, value
        return
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}" if path else str(key)
            yield from _iter_strings(child, child_path)
        return
    if isinstance(value, list):
        for index, child in enumerate(value):
            child_path = f"{path}[{index}]" if path else f"[{index}]"
            yield from _iter_strings(child, child_path)


def _build_marker_map() -> Dict[str, List[str]]:
    return {
        "log_minus_box_i_epsilon_placeholder": [
            "log_minus_box_i_epsilon_placeholder",
            "im log(-box - i epsilon)",
            "im log(-box - i\\epsilon)",
            "im log(-box - iε)",
        ],
        "Im_log_box_placeholder": [
            "im_log_box_placeholder",
            "im log(-box)",
            "imaginary log(-box)",
        ],
        "R_log_box_R": [
            "r_log_box_r",
            "r log(box) r",
        ],
        "Weyl_log_box_Weyl": [
            "weyl_log_box_weyl",
            "weyl log(box) weyl",
        ],
        "causal_response_kernel_placeholder": [
            "causal_response_kernel_placeholder",
            "causal response kernel",
            "ctp keldysh",
            "keldysh",
        ],
    }


def extract_nonlocal_markers(
    stage_p2: Dict[str, object],
    stageN2: Dict[str, object],
    stage9c: Dict[str, object],
    stage11b: Dict[str, object],
) -> Dict[str, object]:
    payloads = {
        "P2": stage_p2,
        "N2": stageN2,
        "9C": stage9c,
        "11B": stage11b,
    }

    marker_map = _build_marker_map()
    normalized_tokens = {
        marker: [_normalize(token) for token in tokens]
        for marker, tokens in marker_map.items()
    }

    marker_hits: Dict[str, List[Dict[str, str]]] = {
        marker: [] for marker in marker_map
    }

    for stage_name, payload in payloads.items():
        for path, text in _iter_strings(payload):
            normalized = _normalize(text)
            for marker, tokens in normalized_tokens.items():
                if any(token and token in normalized for token in tokens):
                    marker_hits[marker].append(
                        {"stage": stage_name, "path": path, "value": text}
                    )

    markers: List[Dict[str, object]] = []
    for marker, hits in marker_hits.items():
        markers.append({"marker": marker, "found": bool(hits), "sources": hits})

    return {
        "markers": markers,
        "marker_map": {marker: bool(hits) for marker, hits in marker_hits.items()},
        "promotes_claims": False,
    }
