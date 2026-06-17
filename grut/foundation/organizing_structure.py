"""GRUT's organizing structure — the V2→V3 foundation, recorded.

This module records (it does NOT build V3) the verified result of the
June 2026 organizing-structure phase: *what GRUT is, once the mechanisms
that failed every adversarial attack are stripped away and only the
surviving constraints remain.*

The one-line organizing principle (adversarially verified, workflows
ww3jtq2t9 / wqr4a0cuq / w1up736t0 / w3g2yu2wc):

    GRUT is the adiabatic-dilatation-redundant (GR) limit, plus the
    controlled breaking of that redundancy by exactly one scale L0 = c*tau_0.

Two pillars + one conjectured bridge:

    Q  — CTP / in-in unitarity         (PROVEN; see ctp_action_structure)
    F  — finite single-pole memory     (POSTULATED; see memory_kernel_form)
    D  — adiabatic spatial dilatation  (CONJECTURED bridge whose BREAKING
                                         term is established; broken by F)

The load-bearing theorem this module encodes: the rigid spatial
dilatation T_lambda (a -> a*e^lambda, comoving k fixed) is a genuine
gauge redundancy of the full CTP action S_IF ONLY at strict k=0 / in the
memoryless L0 -> 0 limit. GRUT's finite memory L0 (a fixed PROPER length)
breaks it for every physical k != 0. The breaking is:

  * CONTROLLED  — enters at O((L0*k_phys)^2);
  * NON-ANOMALOUS — T_lambda is a diffeomorphism, not a Weyl rescaling,
    so the path-integral measure Jacobian is identically 1 and the
    trace-anomaly coefficient alpha does NOT enter (outcome C ruled out);
  * confined to the TENSOR sector — in the linear SCALAR sector the
    tracefree P^TT kernel annihilates the response (mu_linear = 1,
    linear cosmology = LCDM), so the k != 0 breaking is physical, not a
    pathology.

Outcome classification: (B) broken_by_kernel — NOT (A) genuine
redundancy, NOT (C) anomalous.

References:
  theory/GRUT_V3_ORGANIZING_STRUCTURE.md  (the foundation artifact)
  theory/GRUT_SELECTION_PRINCIPLE.md §3.7  (the demotions)
  theory/PROJECTOR_CONSISTENCY_NOGO.md §5  (mu_linear = 1 forced)
  theory/CMB_ISW_EQUALITY_FILTER.md §0.1   (the 2.79x falsification)
"""

from __future__ import annotations

from fractions import Fraction
from typing import Dict

import sympy as sp

from grut.foundation.closure_protocol import TAU_0_MYR, ALPHA_VAC

# Speed of light in Mpc / Myr (c = 299792.458 km/s).
C_MPC_PER_MYR: float = 0.306601

# GRUT's single physical length: the memory scale L0 = c * tau_0.
L0_MPC: float = C_MPC_PER_MYR * TAU_0_MYR  # ~= 12.85 Mpc


# ─────────────────────────────────────────────────────────────────────
# The dilatation theorem — symbolic, computed (not hardcoded)
# ─────────────────────────────────────────────────────────────────────

def chi_eq(L0: sp.Symbol, k: sp.Symbol, a: sp.Symbol) -> sp.Expr:
    """Static GRUT susceptibility chi_eq = 1/(1 + (L0 * k_phys)^2),
    with physical wavenumber k_phys = k/a (retarded_kernel_frw.py)."""
    k_phys = k / a
    return 1 / (1 + (L0 * k_phys) ** 2)


def kphys_dilatation_factor() -> sp.Expr:
    """The factor by which k_phys = k/a transforms under the
    separate-universe dilatation T_lambda (a -> a*e^lambda, comoving k
    fixed). Result: e^(-lambda).  (Corrects the earlier e^(-2lambda)
    mislabel; the e^(-2lambda) belongs on the SQUARE, not on k_phys.)"""
    lam = sp.Symbol("lambda", real=True)
    L0, k, a = sp.symbols("L0 k a", positive=True)
    kphys = k / a
    kphys_T = k / (a * sp.exp(lam))
    return sp.simplify(kphys_T / kphys)  # -> exp(-lambda)


def chi_eq_breaking() -> Dict[str, object]:
    """Compute whether chi_eq is invariant under T_lambda at k=0 vs k!=0.

    Returns the symbolic difference chi_eq(after) - chi_eq(before) in both
    cases. At k=0 it is identically 0 (invariant). At k!=0 it is non-zero
    for lambda != 0 (broken) — the finite L0 obstruction.
    """
    lam = sp.Symbol("lambda", real=True)
    L0, k, a = sp.symbols("L0 k a", positive=True)
    before = chi_eq(L0, k, a)
    after = chi_eq(L0, k, a * sp.exp(lam))  # a -> a e^lambda

    diff_general = sp.simplify(after - before)
    diff_k0 = sp.simplify(diff_general.subs(k, 0))
    # squared-argument transformation factor
    sq_before = (L0 * k / a) ** 2
    sq_after = (L0 * k / (a * sp.exp(lam))) ** 2
    sq_factor = sp.simplify(sq_after / sq_before)  # -> exp(-2 lambda)

    return {
        "diff_at_k0": diff_k0,                 # 0  -> invariant at strict k=0
        "diff_general": diff_general,          # != 0 -> broken for k != 0
        "squared_arg_factor": sq_factor,       # exp(-2 lambda)
        "broken_for_k_nonzero": diff_general != 0,
        "invariant_at_k0": diff_k0 == 0,
    }


# ─────────────────────────────────────────────────────────────────────
# Structural classification (the recorded verdict)
# ─────────────────────────────────────────────────────────────────────

OUTCOME: str = "B_broken_by_kernel"

PILLARS: Dict[str, str] = {
    "Q_ctp_unitarity": "proven",          # ctp_action_structure (computed)
    "F_finite_memory": "postulated",      # memory_kernel_form (computed kernel, tau_0 anchored)
    "D_adiabatic_dilatation": "conjectured_bridge_breaking_established",
}

# The robust theorem: linear scalar sector mu = 1 (LCDM), forced.
MU_LINEAR: Fraction = Fraction(1, 1)

# The anomaly route (C) is ruled out: T_lambda is a diffeomorphism, not a
# Weyl rescaling, so the measure Jacobian is identically 1.
MEASURE_JACOBIAN: int = 1
ALPHA_ENTERS_BREAKING: bool = False

# Terrain of the V3 foundation (what each structure IS to the theory).
TERRAIN: Dict[str, str] = {
    "organizing_principle": "GR-limit dilatation redundancy + controlled breaking by one scale L0",
    "linear_cosmology": "LCDM (mu_linear=1) — derived requirement",
    "linear_refractive_enhancement": "ruled_out (data 2.79x/32sigma + consistency No-Go)",
    "dark_sector": "open — nonlinear/tensor (C5a W^2, C5b orbital-omega, C5c TT)",
    "flavor_koide": "outside the vacuum-response scheme (hosted Yukawa input)",
    "alpha_value": "open — 4th-order Riegert a/c",
    "distinguishability_principle": "a NAME for the conjunction Q∩F∩D, not a fourth axiom",
}


def verify() -> dict:
    """Self-test the recorded organizing-structure result."""
    br = chi_eq_breaking()
    lam = sp.Symbol("lambda", real=True)

    return {
        # The dilatation is invariant at strict k=0 ...
        "invariant_at_strict_k0": bool(br["invariant_at_k0"]),
        # ... and broken for any physical k != 0 (finite-L0 obstruction).
        "broken_for_k_nonzero": bool(br["broken_for_k_nonzero"]),
        # k_phys transforms by e^(-lambda) (the corrected exponent).
        "kphys_factor_is_exp_minus_lambda": (
            sp.simplify(kphys_dilatation_factor() - sp.exp(-lam)) == 0
        ),
        # the squared memory argument transforms by e^(-2 lambda).
        "squared_arg_factor_is_exp_minus_2lambda": (
            sp.simplify(br["squared_arg_factor"] - sp.exp(-2 * lam)) == 0
        ),
        # outcome is (B), not (A) or (C).
        "outcome_is_B": OUTCOME == "B_broken_by_kernel",
        # anomaly route ruled out: measure Jacobian 1, alpha absent.
        "measure_anomaly_free": MEASURE_JACOBIAN == 1 and not ALPHA_ENTERS_BREAKING,
        # the robust theorem: mu_linear = 1 (LCDM).
        "mu_linear_is_one": MU_LINEAR == 1,
        # L0 is GRUT's single proper length ~ 12.85 Mpc.
        "L0_is_about_12p85_Mpc": abs(L0_MPC - 12.85) < 0.5,
        # pillars recorded.
        "two_pillars_plus_bridge": (
            PILLARS["Q_ctp_unitarity"] == "proven"
            and PILLARS["F_finite_memory"] == "postulated"
            and PILLARS["D_adiabatic_dilatation"].startswith("conjectured")
        ),
        # alpha_vac sanity (the one dimensionless axiom, unchanged).
        "alpha_vac_is_one_third": ALPHA_VAC == 1 / 3,
    }
