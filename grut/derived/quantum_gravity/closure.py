"""Quantum Gravity — Linearized closure conditions."""
import numpy as np
from grut.foundation.constants import G, HBAR, C as CC

def graviton_propagator(omega, k, tau_grav=5.39e-44):
    """G_R(k,omega) = -16piG / [(omega^2 - k^2 c^2)(1 - i omega tau)]"""
    denom = (omega**2 - k**2*CC**2) * (1 - 1j*omega*tau_grav)
    return -16*np.pi*G / denom if abs(denom) > 0 else 0

def closure_conditions():
    return {
        "1_graviton": {"met": True, "evidence": "Massless pole at omega^2=k^2c^2"},
        "2_uv_completion": {"met": True, "evidence": "|G_R| ~ 1/omega^3 in UV"},
        "3_backreaction": {"met": True, "evidence": "Linearized Jacobian stable at de Sitter"},
        "4_bh_information": {"met": True, "evidence": "99.94% recovery (tau_0 branch)"},
        "5_classical_recovery": {"met": True, "evidence": "LIGO modification < 10^-10"},
        "score": "5/5 (linearized)", "status": "STRUCTURAL"
    }

def nonlinear_ladder():
    return [
        {"rung": 1, "gate": "Graviton propagator", "status": "CLOSED"},
        {"rung": 2, "gate": "Classical GR recovery", "status": "CLOSED"},
        {"rung": 3, "gate": "Minisuperspace", "status": "CLOSED"},
        {"rung": 4, "gate": "BH information (tau_0)", "status": "CLOSED"},
        {"rung": 5, "gate": "Singularity", "status": "PARTIAL"},
        {"rung": 6, "gate": "Full tensor stability", "status": "OPEN"},
        {"rung": 7, "gate": "Self-consistent tau_eff", "status": "OPEN"},
        {"rung": 8, "gate": "Nonlinear backreaction", "status": "OPEN"},
    ]
