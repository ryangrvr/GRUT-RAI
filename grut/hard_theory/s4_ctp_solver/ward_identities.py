"""Ward identity placeholders for the S4 CTP scaffold."""

from typing import Dict


def ward_identity_status(name: str) -> Dict[str, str]:
    return {
        "name": name,
        "status": "not_evaluated",
        "detail": "Stage 1 scaffold only; no computation executed.",
    }


def diffeomorphism_ward_identity() -> Dict[str, str]:
    return ward_identity_status("diffeomorphism")


def transversality_check() -> Dict[str, str]:
    return ward_identity_status("transversality")


def trace_anomaly_consistency() -> Dict[str, str]:
    return ward_identity_status("trace_anomaly")


def ctp_unitarity_placeholder() -> Dict[str, str]:
    return {
        "name": "ctp_unitarity",
        "status": "not_evaluated",
        "detail": "Requires Gamma[g,g] = 0; placeholder only.",
        "Gamma_g_g": 0.0,
    }


def causality_retarded_support() -> Dict[str, str]:
    return ward_identity_status("causality_retarded_support")
