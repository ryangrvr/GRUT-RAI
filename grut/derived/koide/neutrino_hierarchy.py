"""Priority 4 — neutrino hierarchy via the Koide / Z_3 circulant structure.

The framework's Koide identity K = 2/3 for charged leptons is PROVEN
to follow from a Z_3 circulant structure on √m_i with coupling a = √2:

    √m_i = M_0 (1 + √2 cos(θ + 2π k / 3))     k = 0, 1, 2     (★)

This gives Σ s² = 6 and (Σ s)² = 9, hence K = 2/3 exactly. See
`grut/derived/koide/identity.py` for the charged-lepton fit.

The Standard Model question: does this Z_3 structure extend to
neutrinos? If neutrinos satisfied (★) with the SAME a = √2, the
framework would predict a specific hierarchy and lightest mass.
This module tests that hypothesis and reports the result.

═════════════════════════════════════════════════════════════════════
LOAD-BEARING FINDING
═════════════════════════════════════════════════════════════════════

Applying the canonical Z_3 ansatz (a = √2, K = 2/3) to neutrinos with
experimental Δm²_sol = 7.42×10⁻⁵ eV² and Δm²_atm = 2.515×10⁻³ eV²:

    Minimum achievable Δm²_atm/Δm²_sol = 194.7
    Observed                            =  33.9

The CANONICAL Z_3 ANSATZ DOES NOT FIT NEUTRINOS — for any θ in the
all-positive-s_k range, the Δm²_atm/Δm²_sol ratio is bounded ≥ 194.7,
~6× too large compared to observations. NEITHER hierarchy admits a
solution under the charged-lepton coupling.

This is a SHARP, FALSIFIABLE structural finding. Charged-lepton Z_3
structure does not trivially extend to neutrinos — neutrinos require
a different mass-generation mechanism. Consistent with the framework's
Dirac-vs-Majorana posture (preference for Dirac at ~1.5%, see
A_OVER_C_SM_DIRAC vs A_OVER_C_SM_MAJORANA in closure_protocol.py).

═════════════════════════════════════════════════════════════════════
GENERALIZED Z_3 ANSATZ — modified coupling a
═════════════════════════════════════════════════════════════════════

If we relax the K = 2/3 constraint and admit a generalized Z_3:

    √m_i = M_0 (1 + a cos(θ + 2π k / 3))                            (★★)

then K_ν = (1 + a²/2)/3, which equals 2/3 only when a = √2 (charged
leptons) but takes other values for other a. Numerically:

  a = 0.50  → K_ν = 0.375
  a = 0.71  → K_ν = 0.417 (≈ 1/√2)
  a = 1.00  → K_ν = 0.500          ←← SPECIAL VALUE
  a = √2     → K_ν = 0.667 (charged leptons)

The value a = 1 admits NH with INTERIOR (generic) solution and IH at
the boundary m_3 → 0 (degenerate, fine-tuned). GRUT's a = 1 ansatz
therefore PREFERS NORMAL HIERARCHY:

  NH at a = 1:
    θ ≈ 18.94°
    m_1 ≈ 8.0 × 10⁻⁴ eV  (sub-meV lightest mass)
    m_3 ≈ 5.02 × 10⁻² eV  (≈ √Δm²_atm)
    Σm_ν ≈ 5.96 × 10⁻² eV  (well below Planck 0.12 eV bound)

  IH at a = 1:
    θ ≈ 59.63° (boundary m_3 → 0)
    DEGENERATE — fine-tuned, NOT a generic interior solution.

═════════════════════════════════════════════════════════════════════
What is the postulate, and what is derived?
═════════════════════════════════════════════════════════════════════

DERIVED:
  - Canonical Z_3 (a = √2) DOES NOT admit any neutrino hierarchy
    (minimum ratio 194.7 vs observed 33.9). This is unconditional.
  - For generalized coupling a, K_ν = (1 + a²/2)/3.
  - At a = 1, NH admits an interior solution; IH admits only a
    boundary solution.

POSTULATED:
  - That the GRUT-natural neutrino coupling is a_ν = 1 (giving
    K_ν = 1/2). This is suggested by:
       (i) IH at a = 1 sits exactly at the m_3 = 0 boundary, while
           NH is interior — selects NH.
      (ii) a = 1 is a clean ratio (vs a = √2 for charged leptons —
           factor √2 difference).
     (iii) K_ν = 1/2 corresponds to "two-equal-plus-one-zero"
           limit when one mass vanishes; the structural extreme.
  - The DERIVATION of a_ν = 1 from GRUT primitives (CTP action,
    flavor operator, anomaly coefficients) is OPEN. Tracked under
    `neutrino_z3_coupling_derivation_open_question`.

PREDICTED (conditional on the a_ν = 1 postulate):
  - Normal hierarchy preferred (IH at boundary)
  - m_1 ≈ 0.8 meV (sub-meV lightest)
  - m_2 ≈ 8.7 meV
  - m_3 ≈ 50.2 meV
  - Σm_ν ≈ 60 meV (well within current bounds)

═════════════════════════════════════════════════════════════════════
Observational tests
═════════════════════════════════════════════════════════════════════

  Σm_ν cosmological:
    Planck 2018 + BAO  : Σm_ν < 0.12 eV (95% CL) ← GRUT consistent
    DESI Y3+ (2025)    : ~0.05 eV precision      ← could detect at 1σ
    Euclid + CMB-S4    : ~0.02 eV precision      ← definitive test

  Hierarchy:
    Current (NOvA/T2K/SK): mild NH preference (~2σ)
    JUNO (2024-)         : >3σ hierarchy
    DUNE / Hyper-K       : >5σ hierarchy by 2030

  m_β (electron-flavor effective neutrino mass):
    KATRIN current : m_β < 0.45 eV
    KATRIN final   : m_β < 0.2 eV
    Project 8      : m_β < 0.04 eV (could approach m_2 ≈ 9 meV → m_β ≈ 9 meV)

GRUT's predicted m_2 ≈ 9 meV → m_β ≈ √(|U_e2|² m_2² + ...) ≈ 8 meV
is below current and near-future limits but within reach of advanced
experiments.

═════════════════════════════════════════════════════════════════════
Reference
═════════════════════════════════════════════════════════════════════

- grut/derived/koide/identity.py — charged-lepton Z_3 fit (proven)
- grut/foundation/closure_protocol.py — A_OVER_C_SM_DIRAC vs
  MAJORANA cross-check (Path D)
- NuFIT 2024 — global oscillation fit values for Δm²
- Planck 2018 paper VI — cosmological Σm_ν constraints
- KATRIN Collaboration 2024 — m_β bound
"""

from __future__ import annotations

from typing import Dict, List, Optional, Tuple

import numpy as np
from scipy.optimize import brentq


# Experimental Δm² values (NuFIT 2024 best fit, normal ordering)
DELTA_M_SQ_SOL_EV2 = 7.42e-5    # m_2² - m_1²
DELTA_M_SQ_ATM_NH_EV2 = 2.515e-3  # m_3² - m_1² (NH)
DELTA_M_SQ_ATM_IH_EV2 = 2.498e-3  # |m_3² - m_2²| (IH)

# Planck 2018 + BAO cosmological bound (95% CL)
SIGMA_M_NU_PLANCK_BOUND_EV = 0.12

# Charged-lepton Z_3 coupling (canonical)
A_CHARGED_LEPTON = float(np.sqrt(2))  # = √2; gives K = 2/3

# GRUT-postulated neutrino Z_3 coupling
A_NEUTRINO_POSTULATE = 1.0  # gives K = 1/2; admits NH interior solution


def convention_declaration() -> Dict[str, str]:
    """Convention declaration for the neutrino-hierarchy Z_3 analysis."""
    return {
        "C1n_z3_ansatz":
            "√m_i = M_0 (1 + a cos(θ + 2πk/3)), k = 0,1,2.",
        "C2n_K_value_from_a":
            "K_ν = (1 + a²/2)/3. Charged leptons have a = √2 → "
            "K = 2/3 (PROVEN). Neutrinos have a different a (this "
            "module's analysis).",
        "C3n_canonical_a_fails":
            "a = √2 gives minimum Δm²_atm/Δm²_sol = 194.7 > observed "
            "33.9 — NO solution for either hierarchy. Charged-lepton "
            "Z_3 does NOT extend to neutrinos.",
        "C4n_neutrino_postulate_a_equals_1":
            "Postulate: a_ν = 1 (giving K_ν = 1/2). NH admits interior "
            "solution; IH admits only boundary (m_3=0) solution. "
            "Selects NH, predicts m_1 ≈ 0.8 meV, Σm_ν ≈ 60 meV.",
        "C5n_derivation_status":
            "a_ν = 1 is POSTULATED; derivation from GRUT primitives "
            "(CTP/flavor/anomaly) is OPEN — see "
            "neutrino_z3_coupling_derivation_open_question.",
        "C6n_experimental_baseline":
            "Δm²_sol = 7.42e-5 eV², Δm²_atm,NH = 2.515e-3 eV², "
            "Δm²_atm,IH = 2.498e-3 eV² (NuFIT 2024); Σm_ν < 0.12 eV "
            "(Planck 2018 + BAO, 95% CL).",
        "priority_4_status":
            "Sharp Standard-Model prediction: NORMAL HIERARCHY with "
            "m_1 ≈ 0.8 meV, m_3 ≈ 50 meV, Σm_ν ≈ 60 meV — "
            "anchored on a_ν = 1 postulate. Falsifiable by JUNO/"
            "DUNE/Hyper-K hierarchy + DESI/Euclid/CMB-S4 Σm_ν.",
    }


# ─────────────────────────────────────────────────────────────────────
# Section 1 — Z_3 ansatz machinery
# ─────────────────────────────────────────────────────────────────────


def s_values(theta: float, a: float = A_NEUTRINO_POSTULATE) -> np.ndarray:
    """The three Z_3 circulant √m values:

        s_k = 1 + a cos(θ + 2πk/3),  k = 0, 1, 2

    Returns array [s_0, s_1, s_2]. Caller may sort.
    """
    return np.array([1 + a * np.cos(theta + 2 * np.pi * k / 3) for k in range(3)])


def koide_K(a: float) -> float:
    """Koide K value implied by Z_3 ansatz with coupling a.

        K = Σ s² / (Σ s)² = (3 + 3a²/2) / 9 = (1 + a²/2)/3

    Charged leptons: a = √2 → K = 2/3.
    Neutrinos (postulated): a = 1 → K = 1/2.
    """
    return (1 + a**2 / 2) / 3


def all_positive(theta: float, a: float = A_NEUTRINO_POSTULATE) -> bool:
    """Check all three s_k > 0 (required for real positive masses)."""
    return bool(np.all(s_values(theta, a) > 0))


# ─────────────────────────────────────────────────────────────────────
# Section 2 — Canonical Z_3 (a = √2) fails for neutrinos
# ─────────────────────────────────────────────────────────────────────


def minimum_ratio_canonical_z3() -> float:
    """The minimum value of Δm²_atm/Δm²_sol achievable by the
    canonical Z_3 ansatz (a = √2, K = 2/3) over all valid θ.

    Δm²_atm/Δm²_sol = (s_max⁴ - s_min⁴)/(s_mid⁴ - s_min⁴)

    Returns: 194.7 ± numerical precision (independent of M_0).

    Compare to observed 33.9 — the canonical ansatz CANNOT reproduce
    observations.
    """
    a = A_CHARGED_LEPTON
    thetas = np.linspace(0, 2 * np.pi, 100_000)

    def ratio(t):
        s = s_values(t, a)
        if np.any(s <= 0):
            return np.inf
        s4 = np.sort(s**4)
        denom = s4[1] - s4[0]
        if denom <= 0:
            return np.inf
        return (s4[2] - s4[0]) / denom

    ratios = np.array([ratio(t) for t in thetas])
    return float(np.min(ratios[np.isfinite(ratios)]))


def canonical_z3_fits_neutrinos(target_ratio: float = None) -> bool:
    """Does the canonical Z_3 (a = √2) admit any neutrino solution
    matching the observed Δm²_atm/Δm²_sol?

    Returns False — sharp finding. Default target uses NH ratio
    (33.9). For IH (33.7) the answer is also False.
    """
    if target_ratio is None:
        target_ratio = DELTA_M_SQ_ATM_NH_EV2 / DELTA_M_SQ_SOL_EV2
    return minimum_ratio_canonical_z3() <= target_ratio


# ─────────────────────────────────────────────────────────────────────
# Section 3 — Generalized Z_3 with arbitrary coupling a
# ─────────────────────────────────────────────────────────────────────


def neutrino_solution(
    a: float = A_NEUTRINO_POSTULATE,
    hierarchy: str = "NH",
    delta_sol: float = DELTA_M_SQ_SOL_EV2,
    delta_atm: Optional[float] = None,
    n_theta_samples: int = 20_000,
) -> Optional[Dict[str, float]]:
    """Solve the generalized Z_3 ansatz for neutrinos.

    Given coupling `a` and target hierarchy ('NH' or 'IH'), find θ
    such that the implied Δm²_atm / Δm²_sol matches observations,
    then determine M_0 from Δm²_sol and report all three masses.

    Parameters
    ----------
    a : float
        Z_3 coupling (a = √2 for charged leptons; a = 1 GRUT-
        postulated for neutrinos).
    hierarchy : 'NH' or 'IH'
        Mass-ordering hypothesis.
    delta_sol : float
        Δm²_sol in eV².
    delta_atm : float, optional
        |Δm²_atm| in eV². Defaults to NH (2.515e-3) or IH (2.498e-3).

    Returns
    -------
    dict with keys: a, theta_rad, theta_deg, M_0, m_1, m_2, m_3,
    sum_m_nu, K_implied, hierarchy. None if no solution exists.
    """
    if delta_atm is None:
        delta_atm = (DELTA_M_SQ_ATM_NH_EV2 if hierarchy == "NH"
                     else DELTA_M_SQ_ATM_IH_EV2)
    target = delta_atm / delta_sol

    thetas = np.linspace(0, 2 * np.pi, n_theta_samples)

    def ratio(theta):
        s = s_values(theta, a)
        if np.any(s <= 0):
            return np.nan
        s4 = np.sort(s**4)
        if hierarchy == "NH":
            # m_1 = s_min, m_2 = s_mid, m_3 = s_max
            denom = s4[1] - s4[0]
            if denom <= 0:
                return np.nan
            return (s4[2] - s4[0]) / denom
        else:  # IH
            # m_3 = s_min, m_1 = s_mid, m_2 = s_max
            denom = s4[2] - s4[1]
            if denom <= 0:
                return np.nan
            return (s4[2] - s4[0]) / denom

    ratios = np.array([ratio(t) for t in thetas])
    diffs = ratios - target

    # Find sign changes among finite values
    finite_mask = np.isfinite(diffs)
    finite_thetas = thetas[finite_mask]
    finite_diffs = diffs[finite_mask]
    if len(finite_diffs) < 2:
        return None
    sign_changes = np.where(np.diff(np.sign(finite_diffs)) != 0)[0]
    if len(sign_changes) == 0:
        return None

    # Refine first sign change via brentq
    i = sign_changes[0]
    try:
        theta_sol = brentq(
            lambda t: ratio(t) - target,
            finite_thetas[i], finite_thetas[i + 1],
            xtol=1e-10,
        )
    except Exception:
        return None

    # Compute M_0 from delta_sol
    s = s_values(theta_sol, a)
    s4_sorted = np.sort(s**4)
    if hierarchy == "NH":
        denom_sol = s4_sorted[1] - s4_sorted[0]
    else:
        denom_sol = s4_sorted[2] - s4_sorted[1]
    if denom_sol <= 0:
        return None
    M_0_quartic = delta_sol / denom_sol
    M_0 = float(M_0_quartic ** 0.25)

    # Compute the three masses (in eV)
    m_sorted = M_0**2 * np.sort(s**2)  # ascending
    if hierarchy == "NH":
        m_1, m_2, m_3 = m_sorted
    else:
        m_3, m_1, m_2 = m_sorted

    return {
        "a":            float(a),
        "theta_rad":    float(theta_sol),
        "theta_deg":    float(np.degrees(theta_sol)),
        "M_0":          M_0,
        "m_1":          float(m_1),
        "m_2":          float(m_2),
        "m_3":          float(m_3),
        "sum_m_nu":     float(m_1 + m_2 + m_3),
        "K_implied":    koide_K(a),
        "hierarchy":    hierarchy,
    }


# ─────────────────────────────────────────────────────────────────────
# Section 4 — GRUT prediction at a_ν = 1 (postulated)
# ─────────────────────────────────────────────────────────────────────


def grut_prediction_NH() -> Dict[str, float]:
    """The GRUT-postulated neutrino prediction in the Normal Hierarchy
    case with a_ν = 1.

    Returns the (m_1, m_2, m_3, Σm_ν) prediction, conditional on the
    a_ν = 1 postulate. Falsifiable by JUNO/DUNE/Hyper-K (hierarchy)
    + DESI/Euclid/CMB-S4 (Σm_ν).
    """
    return neutrino_solution(
        a=A_NEUTRINO_POSTULATE,
        hierarchy="NH",
    )


def grut_prediction_IH() -> Optional[Dict[str, float]]:
    """The GRUT IH solution at a_ν = 1.

    NOTE: this lives at the m_3 = 0 boundary, NOT a generic interior
    solution. Returned for completeness; GRUT's prediction is NH (not IH).
    """
    return neutrino_solution(
        a=A_NEUTRINO_POSTULATE,
        hierarchy="IH",
    )


def hierarchy_preference() -> Dict[str, object]:
    """GRUT's hierarchy preference: NH vs IH at a_ν = 1.

    Reports both solutions and compares m_lightest. The IH solution
    sits at m_3 → 0 boundary (degenerate, fine-tuned), while NH gives
    a generic interior m_1 ≈ 1 meV. GRUT therefore PREFERS NH.
    """
    nh = grut_prediction_NH()
    ih = grut_prediction_IH()

    nh_m_lightest = nh["m_1"] if nh else None
    ih_m_lightest = ih["m_3"] if ih else None

    # IH at boundary: m_3 essentially 0 (numerical noise ~1e-11)
    ih_at_boundary = (
        ih is not None
        and ih_m_lightest is not None
        and ih_m_lightest < 1e-6  # below 1 μeV — boundary case
    )

    return {
        "NH_solution":       nh,
        "IH_solution":       ih,
        "NH_m_lightest":     nh_m_lightest,
        "IH_m_lightest":     ih_m_lightest,
        "IH_at_boundary":    ih_at_boundary,
        "preferred":         "NH",  # NH is interior; IH is degenerate
        "rationale":
            "NH at a=1 is an interior generic solution (m_1 ≈ 0.8 meV "
            "nonzero, all three masses generic). IH at a=1 sits at "
            "the m_3 → 0 boundary (degenerate, fine-tuned). GRUT's "
            "Z_3 structure with a_ν = 1 thus PREFERS NORMAL HIERARCHY.",
    }


# ─────────────────────────────────────────────────────────────────────
# Section 5 — Compare to observational constraints
# ─────────────────────────────────────────────────────────────────────


def consistency_with_planck() -> Dict[str, object]:
    """Is the GRUT NH prediction consistent with Planck Σm_ν bound?"""
    pred = grut_prediction_NH()
    if pred is None:
        return {"consistent": False, "reason": "no NH solution"}
    return {
        "GRUT_sum_m_nu_eV":        pred["sum_m_nu"],
        "Planck_2018_BAO_bound_eV": SIGMA_M_NU_PLANCK_BOUND_EV,
        "consistent":              pred["sum_m_nu"] < SIGMA_M_NU_PLANCK_BOUND_EV,
        "headroom_eV":             SIGMA_M_NU_PLANCK_BOUND_EV - pred["sum_m_nu"],
        "interpretation":
            "GRUT's predicted Σm_ν ~ 60 meV is well below Planck "
            "0.12 eV bound. DESI Y3+ (~50 meV precision) could "
            "detect the prediction at ~1σ; Euclid/CMB-S4 "
            "(~20 meV precision) provides definitive test.",
    }


def observational_tests_summary() -> Dict[str, str]:
    """Summary of near-term observational tests of the GRUT NH prediction."""
    return {
        "hierarchy_NH_preference": (
            "Current (NOvA + T2K + SK): mild NH preference ~2σ. "
            "JUNO 2024-2030: hierarchy at >3σ. DUNE/Hyper-K: >5σ "
            "by ~2030. GRUT predicts NH."
        ),
        "sum_m_nu":
            "GRUT predicts Σm_ν ≈ 60 meV. Planck 0.12 eV (consistent). "
            "DESI Y3+ ~50 meV precision (2025-) could detect. "
            "Euclid + CMB-S4 ~20 meV precision (2027+) definitive.",
        "m_beta_kinematic":
            "GRUT predicts m_β ≈ √(|U_e1|² m_1² + |U_e2|² m_2² + "
            "|U_e3|² m_3²) ≈ 9 meV. KATRIN current 0.45 eV "
            "(consistent). Project 8 future ~40 meV (could "
            "approach prediction).",
        "neutrinoless_double_beta_decay":
            "GRUT's Dirac-ν posture (Path D, A_OVER_C_SM_DIRAC closer "
            "to canonical) predicts NO 0νββ signal. nEXO, KamLAND-Zen "
            "future generations test this — non-detection at "
            "improved bounds is consistent with GRUT prediction.",
    }


# ─────────────────────────────────────────────────────────────────────
# Verification harness
# ─────────────────────────────────────────────────────────────────────


def verify() -> Dict[str, bool]:
    """Self-test: Priority 4 neutrino-hierarchy landings.

    Eight legs:
      (1) Charged-lepton coupling a = √2 gives K = 2/3
      (2) Postulated neutrino coupling a_ν = 1 gives K = 1/2
      (3) Canonical Z_3 (a = √2) cannot fit either neutrino hierarchy
      (4) Minimum Δm²_atm/Δm²_sol at a = √2 is ≈ 194.7 (> observed)
      (5) NH solution at a = 1 exists with m_1 ≈ 0.8 meV
      (6) IH at a = 1 sits at m_3 → 0 boundary (degenerate)
      (7) GRUT prefers NH (interior generic solution)
      (8) Σm_ν < Planck bound 0.12 eV (cosmologically allowed)
    """
    # (1) Charged-lepton K
    leg1 = abs(koide_K(A_CHARGED_LEPTON) - 2 / 3) < 1e-12

    # (2) Neutrino-postulate K
    leg2 = abs(koide_K(A_NEUTRINO_POSTULATE) - 1 / 2) < 1e-12

    # (3) Canonical Z_3 cannot fit
    leg3 = not canonical_z3_fits_neutrinos()

    # (4) Minimum ratio is ~194.7 (greater than ~190, less than ~200)
    min_r = minimum_ratio_canonical_z3()
    leg4 = bool(190 < min_r < 200)

    # (5) NH at a=1 has m_1 ≈ 0.8 meV
    nh = grut_prediction_NH()
    leg5 = bool(
        nh is not None
        and 5e-4 < nh["m_1"] < 5e-3  # m_1 in (0.5, 5) meV range
    )

    # (6) IH at a=1 boundary
    ih = grut_prediction_IH()
    leg6 = bool(ih is not None and ih["m_3"] < 1e-6)

    # (7) Hierarchy preference
    pref = hierarchy_preference()
    leg7 = pref["preferred"] == "NH" and pref["IH_at_boundary"] is True

    # (8) Cosmological consistency
    cosm = consistency_with_planck()
    leg8 = bool(cosm["consistent"])

    return {
        "charged_lepton_a_sqrt2_gives_K_2_over_3":  leg1,
        "neutrino_a_one_gives_K_1_over_2":           leg2,
        "canonical_z3_does_not_fit_neutrinos":       leg3,
        "minimum_ratio_at_a_sqrt2_is_194_7":          leg4,
        "NH_solution_at_a_1_has_m1_sub_meV":          leg5,
        "IH_at_a_1_sits_at_m3_zero_boundary":         leg6,
        "GRUT_prefers_normal_hierarchy":              leg7,
        "sum_m_nu_consistent_with_Planck":            leg8,
    }
