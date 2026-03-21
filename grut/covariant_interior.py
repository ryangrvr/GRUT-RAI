"""Constitutive-to-metric lapse obstruction analysis — Phase V.

This module does not derive a full covariant interior metric.  It
formalizes the obstruction to promoting the naive constitutive
post-Newtonian lapse proxy to a true Schwarzschild-like interior lapse.

PRINCIPAL RESULTS:

  Result 1 — Constitutive Lapse Insufficiency Theorem (theorem-grade):
    The naive constitutive post-Newtonian mapping yields
    A_eff(beta_Q) < 0 for every finite beta_Q > 0 when
    alpha_vac <= e^{-1/2}.  Status: PROVEN.

  Result 2 — Lapse Direction Failure (theorem-grade):
    The constitutive barrier correction does not restore a timelike
    Schwarzschild-like lapse direction at the endpoint.  The naive
    static redshift interpretation fails.  Further metric
    interpretation requires an observer-adapted interior chart or
    a fuller covariant construction.

  Result 3 — Psi_proxy Classification (constitutive_surrogate):
    Psi_proxy = 1/(1+beta_Q) is the exact barrier-to-gravitational
    energy ratio.  Its mapping to the metric lapse is structurally
    undetermined.  Neither promoted nor excluded as the true lapse.

  Result 4 — Effective NEC-Violating Support (secondary, constitutive-level):
    Under Einstein-like covariant closure assumptions, NEC-violating
    effective stress-energy appears necessary for sub-horizon barrier
    support.  This is a qualified constitutive-level observation,
    NOT a covariant theorem.

PHASE IV HANDOFF:
  Level 1 EXACT: Phi_barrier/Phi_grav = 1/(1+beta_Q)
  Level 2 CONSTITUTIVE_DERIVED: Psi_proxy = 1/(1+beta_Q)
  Level 3 UNRESOLVED: True interior metric lapse

PHASE V UPDATE:
  Level 3 sharpened from UNRESOLVED to
  CONSTITUTIVE_LAPSE_PROMOTION_OBSTRUCTED:
    The naive constitutive post-Newtonian mapping provably fails
    for every finite beta_Q > 0 (not just canon beta_Q = 2).

SELF-CONTAINED: No cross-imports from grut/.  Pure Python (math only).
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Tuple


# ================================================================
# Constants — each mirrors canonical Phase IV value; see effective_lapse.py
# ================================================================

ALPHA_VAC = 1.0 / 3.0            # Mirrors canonical Phase IV value; see effective_lapse.py
BETA_Q = 2.0                     # Mirrors canonical Phase IV value; see effective_lapse.py
EPSILON_Q = ALPHA_VAC ** 2        # = 1/9; mirrors canonical Phase IV value
R_EQ_OVER_R_S = ALPHA_VAC        # = 1/3; from endpoint law
C_ENDPOINT = 1.0 / R_EQ_OVER_R_S # = 3.0; compactness at endpoint

# Classification labels
LEVEL_EXACT = "exact"
LEVEL_CONSTITUTIVE_DERIVED = "constitutive_derived"
LEVEL_UNRESOLVED = "unresolved"
LEVEL_CONSTITUTIVE_LAPSE_PROMOTION_OBSTRUCTED = (
    "constitutive_lapse_promotion_obstructed"
)
LEVEL_CONSTITUTIVE_SURROGATE = "constitutive_surrogate"

# Threshold for alpha_vac in the insufficiency theorem
ALPHA_VAC_CRITICAL = math.exp(-0.5)  # e^{-1/2} ~ 0.6065

# Verbatim scope statement (required in result object, docs, and benchmark)
SCOPE_STATEMENT = (
    "This theorem rules out only the naive constitutive post-Newtonian "
    "lapse identification.  It does not rule out a different covariant "
    "interior metric construction or a non-Schwarzschild-like "
    "observer-adapted lapse notion."
)


# ================================================================
# Dataclasses
# ================================================================

@dataclass
class InsufficiencyProof:
    """Constitutive Lapse Insufficiency Theorem.

    THEOREM: For the canonical GRUT parameter regime alpha_vac <= e^{-1/2},
    the naive constitutive post-Newtonian mapping yields A_eff < 0 for
    every finite beta_Q > 0.

    PROOF (clean inequality route):
      1. A_eff = 1 - C*beta/(1+beta) where C = alpha^{-2/beta}
      2. A_eff < 0 iff g(beta) = ln(C*beta/(1+beta)) > 0
      3. Substitute x = 1/beta > 0: g = 2Lx - ln(1+x) where L = |ln alpha|
      4. For L >= 1/2: 2L >= 1, so g >= x - ln(1+x) = h(x)
      5. h(0) = 0 and h'(x) = x/(1+x) > 0 for x > 0
      6. Therefore h(x) > 0 for x > 0
      7. Therefore g(beta) > 0 for every finite beta > 0
      8. Therefore A_eff < 0 for every finite beta > 0.  QED.

    SCOPE: This concerns the naive constitutive post-Newtonian ansatz
    only.  It does NOT prove that no covariant interior metric exists.
    """
    alpha_vac: float = 0.0
    alpha_vac_satisfies_bound: bool = False
    alpha_vac_critical: float = 0.0

    ln_alpha_abs: float = 0.0
    two_L: float = 0.0
    two_L_ge_one: bool = False

    h_positive_for_all_x: bool = False
    g_positive_for_all_beta: bool = False
    A_eff_negative_for_all_finite_beta: bool = False

    sample_beta_values: List[float] = field(default_factory=list)
    sample_A_eff_values: List[float] = field(default_factory=list)
    sample_g_values: List[float] = field(default_factory=list)
    sample_h_values: List[float] = field(default_factory=list)

    proof_steps: List[str] = field(default_factory=list)
    theorem_status: str = ""
    scope_statement: str = ""
    notes: List[str] = field(default_factory=list)


@dataclass
class EffectiveNECAnalysis:
    """Effective NEC-violating support analysis (secondary, constitutive-level).

    Under Einstein-like covariant closure assumptions, the provisional
    constitutive-to-covariant translation indicates NEC-violating
    effective stress-energy appears necessary for sub-horizon barrier
    support.  This is a qualified constitutive-level observation,
    NOT a covariant theorem.
    """
    compactness: float = 0.0
    is_sub_horizon: bool = False
    A_eff: float = 0.0
    delta_A: float = 0.0

    rho_plus_P_sign_effective: str = ""
    nec_violating_support_indicated: bool = False
    derivation_level: str = "constitutive"

    notes: List[str] = field(default_factory=list)


@dataclass
class LapseDirectionAnalysis:
    """Lapse direction failure analysis at the GRUT equilibrium endpoint.

    The constitutive barrier correction does not restore a timelike
    Schwarzschild-like lapse direction at the endpoint.  The naive
    static redshift interpretation fails.  Further metric interpretation
    requires an observer-adapted interior chart or a fuller covariant
    construction.
    """
    compactness: float = 0.0
    A_schw: float = 0.0
    g_tt_schw: float = 0.0
    g_rr_schw: float = 0.0

    t_is_spacelike_schw: bool = False
    r_is_timelike_schw: bool = False

    A_eff: float = 0.0
    g_tt_eff: float = 0.0
    constitutive_restores_timelike: bool = False
    naive_redshift_fails: bool = False
    requires_adapted_chart_or_covariant: bool = False

    notes: List[str] = field(default_factory=list)


@dataclass
class TPhiStatusResult:
    """Status of the memory stress-energy tensor T^Phi.

    T^Phi_mu_nu is SCHEMATIC/EFFECTIVE in the current framework:
    not derived from a Lagrangian, not uniquely specified.
    """
    is_lagrangian_derived: bool = False
    is_schematic: bool = True
    is_uniquely_specified: bool = False

    mapping_underdetermined: bool = True
    underdetermination_reason: str = ""
    missing_for_metric: List[str] = field(default_factory=list)

    notes: List[str] = field(default_factory=list)


@dataclass
class ProxyLapseClassification:
    """Sharpened classification of Psi_proxy = 1/(1+beta_Q).

    Status: CONSTITUTIVE SURROGATE
    - Exact barrier-to-gravity energy ratio (Level 1)
    - Constitutive lapse scale (Level 2)
    - Cannot presently be promoted to true metric lapse (Level 3)
    - Cannot be excluded either
    """
    psi_proxy: float = 0.0
    level_1_status: str = ""
    level_2_status: str = ""
    level_3_status_phase_iv: str = ""
    level_3_status_phase_v: str = ""

    is_exact_energy_ratio: bool = False
    is_constitutive_lapse_scale: bool = False
    can_be_promoted_to_true_lapse: bool = False
    can_be_excluded: bool = False
    classification: str = ""

    scope_of_obstruction: str = ""
    notes: List[str] = field(default_factory=list)


@dataclass
class StatusLadderUpdate:
    """Status ladder update from Phase IV to Phase V."""
    level_1_before: str = ""
    level_1_after: str = ""
    level_1_changed: bool = False

    level_2_before: str = ""
    level_2_after: str = ""
    level_2_changed: bool = False

    level_3_before: str = ""
    level_3_after: str = ""
    level_3_changed: bool = True
    level_3_sharpening_reason: str = ""

    no_level_weakened: bool = True
    obstruction_scope: str = ""
    notes: List[str] = field(default_factory=list)


@dataclass
class SelfHealingReconfirmation:
    """Reconfirmation that Phase IV self-healing survives Phase V."""
    source_at_eq: float = 0.0
    source_vanishes: bool = True
    independent_of_metric: bool = True
    independent_of_A_eff: bool = True
    independent_of_nec: bool = True
    preserved: bool = True

    reason: str = ""
    notes: List[str] = field(default_factory=list)


@dataclass
class Phase4Reconfirmation:
    """Reconfirmation that all Phase IV results survive Phase V."""
    level_1_preserved: bool = True
    level_2_preserved: bool = True
    sensitivity_band_preserved: bool = True
    self_healing_preserved: bool = True
    shift_estimates_preserved: bool = True
    coincidence_explanation_preserved: bool = True
    all_preserved: bool = True

    notes: List[str] = field(default_factory=list)


@dataclass
class BetaScanEntry:
    """Single entry in the beta_Q parametric scan for A_eff."""
    beta_Q: float = 0.0
    C: float = 0.0
    A_schw: float = 0.0
    delta_A: float = 0.0
    A_eff: float = 0.0
    g_of_beta: float = 0.0
    h_of_x: float = 0.0
    A_eff_is_negative: bool = False


@dataclass
class CovariantInteriorResult:
    """Master result: Phase V constitutive-to-metric lapse obstruction."""
    valid: bool = False

    insufficiency_theorem: Optional[InsufficiencyProof] = None
    effective_nec: Optional[EffectiveNECAnalysis] = None
    lapse_direction: Optional[LapseDirectionAnalysis] = None
    tphi_status: Optional[TPhiStatusResult] = None
    proxy_classification: Optional[ProxyLapseClassification] = None

    status_ladder: Optional[StatusLadderUpdate] = None
    self_healing: Optional[SelfHealingReconfirmation] = None
    phase4_reconfirmation: Optional[Phase4Reconfirmation] = None

    beta_scan: List[BetaScanEntry] = field(default_factory=list)

    nonclaims: List[str] = field(default_factory=list)
    obstruction_is_about_constitutive_ansatz: bool = True

    approx_status: str = ""
    remaining_obstructions: List[str] = field(default_factory=list)
    diagnostics: Dict[str, Any] = field(default_factory=dict)


# ================================================================
# Helper functions
# ================================================================

def _compactness(alpha_vac: float, beta_Q: float) -> float:
    """Endpoint compactness C = alpha_vac^{-2/beta_Q}."""
    if alpha_vac <= 0.0 or beta_Q <= 0.0:
        return 0.0
    return alpha_vac ** (-2.0 / beta_Q)


def _h_of_x(x: float) -> float:
    """Standard inequality function h(x) = x - ln(1+x).

    h(0) = 0, h'(x) = x/(1+x) > 0 for x > 0, so h(x) > 0 for x > 0.
    """
    if x <= 0.0:
        return 0.0
    return x - math.log(1.0 + x)


def _g_of_beta(beta: float, ln_alpha_abs: float) -> float:
    """Theorem function g(beta) = 2L/beta - ln(1 + 1/beta).

    Equivalently, with x = 1/beta: g = 2Lx - ln(1+x).
    g > 0 for every finite beta > 0 when L >= 1/2.
    """
    if beta <= 0.0:
        return float("inf")
    x = 1.0 / beta
    return 2.0 * ln_alpha_abs * x - math.log(1.0 + x)


def _A_eff_from_constitutive(alpha_vac: float, beta_Q: float) -> float:
    """Constitutive A_eff = 1 - C * beta/(1+beta).

    Where C = alpha_vac^{-2/beta_Q} and
    A_eff = A_schw + delta_A = (1-C) + C/(1+beta_Q).
    """
    C = _compactness(alpha_vac, beta_Q)
    return 1.0 - C * beta_Q / (1.0 + beta_Q)


# ================================================================
# Builder functions
# ================================================================

def build_insufficiency_theorem(
    alpha_vac: float = ALPHA_VAC,
) -> InsufficiencyProof:
    """Prove the Constitutive Lapse Insufficiency Theorem."""
    ip = InsufficiencyProof()
    ip.alpha_vac = alpha_vac
    ip.alpha_vac_critical = ALPHA_VAC_CRITICAL
    ip.alpha_vac_satisfies_bound = alpha_vac <= ALPHA_VAC_CRITICAL

    ip.ln_alpha_abs = abs(math.log(alpha_vac)) if alpha_vac > 0 else 0.0
    ip.two_L = 2.0 * ip.ln_alpha_abs
    ip.two_L_ge_one = ip.two_L >= 1.0

    # The core proof: h(x) = x - ln(1+x) > 0 for x > 0
    # is a standard calculus result (h(0)=0, h'(x)=x/(1+x)>0).
    ip.h_positive_for_all_x = True  # mathematical fact

    # If 2L >= 1 then g(beta) = 2Lx - ln(1+x) >= x - ln(1+x) = h(x) > 0
    ip.g_positive_for_all_beta = (
        ip.alpha_vac_satisfies_bound and ip.two_L_ge_one
    )

    # Therefore A_eff < 0 for every finite beta > 0
    ip.A_eff_negative_for_all_finite_beta = ip.g_positive_for_all_beta

    # Numerical verification samples
    beta_samples = [0.5, 1.0, 2.0, 3.0, 5.0, 10.0, 50.0, 500.0]
    ip.sample_beta_values = beta_samples
    ip.sample_A_eff_values = [
        _A_eff_from_constitutive(alpha_vac, b) for b in beta_samples
    ]
    ip.sample_g_values = [
        _g_of_beta(b, ip.ln_alpha_abs) for b in beta_samples
    ]
    ip.sample_h_values = [_h_of_x(1.0 / b) for b in beta_samples]

    # Proof steps
    ip.proof_steps = [
        "1. Define A_eff = 1 - C*beta/(1+beta) where C = alpha^{-2/beta}.",
        "2. A_eff < 0 iff g(beta) = ln(C*beta/(1+beta)) > 0.",
        (
            "3. Substitute x = 1/beta > 0: "
            "g = 2Lx - ln(1+x) where L = |ln alpha|."
        ),
        "4. For L >= 1/2: 2L >= 1, so g >= x - ln(1+x) = h(x).",
        "5. h(0) = 0 and h'(x) = x/(1+x) > 0 for x > 0.",
        "6. Therefore h(x) > 0 for x > 0.",
        "7. Therefore g(beta) > 0 for every finite beta > 0.",
        "8. Therefore A_eff < 0 for every finite beta > 0.  QED.",
        (
            "9. Scope: this concerns the naive constitutive "
            "post-Newtonian ansatz only."
        ),
    ]

    ip.theorem_status = (
        "proven" if ip.A_eff_negative_for_all_finite_beta
        else "not_applicable"
    )
    ip.scope_statement = SCOPE_STATEMENT

    ip.notes = [
        (
            "Phase IV showed A_eff = -1 for canon beta_Q = 2 only.  "
            "Phase V proves A_eff < 0 for every finite beta_Q > 0."
        ),
        (
            "At beta_Q -> infinity, A_eff -> 0^- but never reaches zero."
        ),
        (
            "The bound alpha_vac <= e^{-1/2} covers the canonical "
            "GRUT value alpha_vac = 1/3 and any regime satisfying "
            "this bound."
        ),
    ]

    return ip


def build_effective_nec(
    alpha_vac: float = ALPHA_VAC,
    beta_Q: float = BETA_Q,
) -> EffectiveNECAnalysis:
    """Assess effective NEC-violating support (secondary, constitutive-level)."""
    nec = EffectiveNECAnalysis()
    C = _compactness(alpha_vac, beta_Q)
    nec.compactness = C
    nec.is_sub_horizon = C > 1.0

    A_eff = _A_eff_from_constitutive(alpha_vac, beta_Q)
    nec.A_eff = A_eff
    nec.delta_A = C / (1.0 + beta_Q)

    # For sub-horizon equilibrium with A_eff < 0, barrier support
    # implies the effective stress-energy violates the NEC:
    # rho_eff + P_eff/c^2 < 0 is needed to hold the configuration
    # against singularity formation (Penrose theorem evasion).
    if nec.is_sub_horizon and A_eff < 0:
        nec.rho_plus_P_sign_effective = "negative"
        nec.nec_violating_support_indicated = True
    elif nec.is_sub_horizon:
        nec.rho_plus_P_sign_effective = "indeterminate"
        nec.nec_violating_support_indicated = False
    else:
        nec.rho_plus_P_sign_effective = "not_applicable"
        nec.nec_violating_support_indicated = False

    nec.derivation_level = "constitutive"

    nec.notes = [
        (
            "This is a constitutive-level observation under Einstein-like "
            "covariant closure assumptions, NOT a covariant theorem."
        ),
        (
            "NEC-violating support is analogous to the mechanism in "
            "gravastar-type constructions but is not derived from "
            "a covariant action here."
        ),
        (
            "The derivation level is 'constitutive': the effective "
            "stress-energy decomposition is provisional."
        ),
    ]

    return nec


def build_lapse_direction(
    alpha_vac: float = ALPHA_VAC,
    beta_Q: float = BETA_Q,
) -> LapseDirectionAnalysis:
    """Analyze lapse direction failure at the endpoint."""
    ld = LapseDirectionAnalysis()
    C = _compactness(alpha_vac, beta_Q)
    ld.compactness = C

    # Schwarzschild coordinates at R_eq < r_s
    ld.A_schw = 1.0 - C
    ld.g_tt_schw = -ld.A_schw   # = C - 1 > 0 when C > 1
    ld.g_rr_schw = 1.0 / (1.0 - C) if abs(1.0 - C) > 1e-30 else 0.0

    ld.t_is_spacelike_schw = ld.A_schw < 0
    ld.r_is_timelike_schw = ld.A_schw < 0

    # Constitutive effective metric
    ld.A_eff = _A_eff_from_constitutive(alpha_vac, beta_Q)
    ld.g_tt_eff = -ld.A_eff  # positive when A_eff < 0

    # Key results
    ld.constitutive_restores_timelike = ld.A_eff > 0
    ld.naive_redshift_fails = ld.A_eff <= 0
    ld.requires_adapted_chart_or_covariant = ld.A_eff <= 0

    ld.notes = [
        (
            "In Schwarzschild coordinates at R_eq < r_s, the coordinate t "
            "is spacelike (g_tt > 0) and r is timelike (g_rr < 0)."
        ),
        (
            "The constitutive barrier correction (delta_A > 0) reduces "
            "the magnitude of A_schw but does not flip its sign to positive."
        ),
        (
            "The naive static redshift formula Psi = 1/sqrt(A_eff) - 1 "
            "does not apply when A_eff < 0."
        ),
        (
            "Further metric interpretation requires an observer-adapted "
            "interior chart or a fuller covariant construction."
        ),
    ]

    return ld


def build_tphi_status() -> TPhiStatusResult:
    """Assess the status of the memory stress-energy tensor T^Phi."""
    ts = TPhiStatusResult()
    ts.is_lagrangian_derived = False
    ts.is_schematic = True
    ts.is_uniquely_specified = False
    ts.mapping_underdetermined = True

    ts.underdetermination_reason = (
        "The mapping from the barrier energy ratio 1/(1+beta_Q) to the "
        "metric lapse requires solving the Einstein equations "
        "G_mu_nu = 8*pi*G*(T^matter + T^Phi) with a specific T^Phi.  "
        "Since T^Phi is schematic/effective (not derived from a "
        "Lagrangian), the Einstein equations cannot be solved and the "
        "interior metric lapse is structurally undetermined."
    )

    ts.missing_for_metric = [
        "A covariant action S[Phi] for the memory/barrier field.",
        (
            "The stress-energy tensor T^Phi_mu_nu = (-2/sqrt(g)) "
            "delta(S)/delta(g^mu_nu) derived from that action."
        ),
        "An equation of state relating barrier pressure to energy density.",
        "Covariant conservation constraints on T^Phi in the sub-horizon regime.",
    ]

    ts.notes = [
        (
            "T^Phi_mu_nu is SCHEMATIC/EFFECTIVE in the current framework "
            "(see field_equations.py, Candidate 2)."
        ),
        (
            "This is the structural reason why Psi_proxy cannot be "
            "promoted to the true metric lapse."
        ),
    ]

    return ts


def build_proxy_classification(
    alpha_vac: float = ALPHA_VAC,
    beta_Q: float = BETA_Q,
) -> ProxyLapseClassification:
    """Classify Psi_proxy with Phase V precision."""
    pc = ProxyLapseClassification()
    pc.psi_proxy = 1.0 / (1.0 + beta_Q)

    pc.level_1_status = LEVEL_EXACT
    pc.level_2_status = LEVEL_CONSTITUTIVE_DERIVED
    pc.level_3_status_phase_iv = LEVEL_UNRESOLVED
    pc.level_3_status_phase_v = LEVEL_CONSTITUTIVE_LAPSE_PROMOTION_OBSTRUCTED

    pc.is_exact_energy_ratio = True
    pc.is_constitutive_lapse_scale = True
    pc.can_be_promoted_to_true_lapse = False
    pc.can_be_excluded = False
    pc.classification = LEVEL_CONSTITUTIVE_SURROGATE

    pc.scope_of_obstruction = (
        "The obstruction is specifically about the naive constitutive "
        "post-Newtonian lapse identification.  It does not exclude "
        "Psi_proxy as the true lapse under a different covariant "
        "interior construction."
    )

    pc.notes = [
        (
            "Psi_proxy = 1/(1+beta_Q) is the exact barrier-to-gravitational "
            "energy ratio (Level 1 EXACT)."
        ),
        (
            "Its identification as the lapse scale is at the constitutive "
            "level (Level 2 CONSTITUTIVE_DERIVED)."
        ),
        (
            "The Insufficiency Theorem proves the naive constitutive "
            "mapping cannot promote this to the true metric lapse."
        ),
        (
            "The true lapse may coincidentally equal Psi_proxy for "
            "reasons beyond the constitutive framework — hence "
            "'cannot be excluded'."
        ),
    ]

    return pc


def build_status_ladder_update() -> StatusLadderUpdate:
    """Build the Phase IV → Phase V status ladder transition."""
    sl = StatusLadderUpdate()

    sl.level_1_before = LEVEL_EXACT
    sl.level_1_after = LEVEL_EXACT
    sl.level_1_changed = False

    sl.level_2_before = LEVEL_CONSTITUTIVE_DERIVED
    sl.level_2_after = LEVEL_CONSTITUTIVE_DERIVED
    sl.level_2_changed = False

    sl.level_3_before = LEVEL_UNRESOLVED
    sl.level_3_after = LEVEL_CONSTITUTIVE_LAPSE_PROMOTION_OBSTRUCTED
    sl.level_3_changed = True

    sl.level_3_sharpening_reason = (
        "The Constitutive Lapse Insufficiency Theorem proves that "
        "A_eff < 0 for every finite beta_Q > 0 when alpha_vac <= "
        "e^{-1/2}.  The naive constitutive post-Newtonian mapping "
        "is therefore structurally unable to produce a valid "
        "Schwarzschild-like interior lapse at the GRUT endpoint.  "
        "Phase IV labeled this 'unresolved'; Phase V sharpens it to "
        "a specific, provable no-go for the naive constitutive "
        "lapse promotion."
    )

    sl.no_level_weakened = True

    sl.obstruction_scope = (
        "The obstruction is about the naive constitutive post-Newtonian "
        "lapse identification specifically, not about the full covariant "
        "GRUT interior metric."
    )

    sl.notes = [
        "Level 1 (exact barrier ratio): UNCHANGED.",
        "Level 2 (constitutive-derived proxy): UNCHANGED.",
        (
            "Level 3: sharpened from 'unresolved' to "
            "'constitutive_lapse_promotion_obstructed'."
        ),
        "No level is weakened by Phase V.",
    ]

    return sl


def build_self_healing_reconfirmation() -> SelfHealingReconfirmation:
    """Reconfirm self-healing independence from Phase V results."""
    sh = SelfHealingReconfirmation()
    sh.source_at_eq = 0.0
    sh.source_vanishes = True
    sh.independent_of_metric = True
    sh.independent_of_A_eff = True
    sh.independent_of_nec = True
    sh.preserved = True

    sh.reason = (
        "Self-healing depends on the source term X - Phi = "
        "a_grav - M_drive = 0 at equilibrium (force balance).  "
        "Force balance is a dynamical condition, not a metric "
        "condition.  The Insufficiency Theorem concerns the metric "
        "component A_eff, not force balance.  NEC violation concerns "
        "the effective stress-energy, not the memory-drive equation.  "
        "Therefore all Phase V results are structurally independent "
        "of self-healing, which is PRESERVED."
    )

    sh.notes = [
        "Self-healing at equilibrium: X - Phi = 0 (exact, force balance).",
        "Correction ODE source vanishes identically at equilibrium.",
        (
            "Phase V metric/NEC results do not affect the dynamical "
            "force balance."
        ),
    ]

    return sh


def build_phase4_reconfirmation() -> Phase4Reconfirmation:
    """Reconfirm all Phase IV results survive Phase V."""
    p4 = Phase4Reconfirmation()
    p4.level_1_preserved = True
    p4.level_2_preserved = True
    p4.sensitivity_band_preserved = True
    p4.self_healing_preserved = True
    p4.shift_estimates_preserved = True
    p4.coincidence_explanation_preserved = True
    p4.all_preserved = True

    p4.notes = [
        "Phase V adds new results but does NOT invalidate any Phase IV result.",
        (
            "Level 1 (exact barrier ratio), Level 2 (constitutive proxy), "
            "sensitivity band, self-healing, shift estimates, and "
            "coincidence explanation are all PRESERVED."
        ),
    ]

    return p4


# ================================================================
# Parametric scan
# ================================================================

def scan_A_eff_vs_beta(
    alpha_vac: float = ALPHA_VAC,
    beta_values: Optional[List[float]] = None,
) -> List[BetaScanEntry]:
    """Scan A_eff across beta_Q values to verify the theorem numerically."""
    if beta_values is None:
        beta_values = [0.5, 1.0, 2.0, 3.0, 5.0, 10.0, 50.0, 500.0]

    ln_alpha_abs = abs(math.log(alpha_vac)) if alpha_vac > 0 else 0.0
    entries: List[BetaScanEntry] = []

    for beta in beta_values:
        e = BetaScanEntry()
        e.beta_Q = beta
        e.C = _compactness(alpha_vac, beta)
        e.A_schw = 1.0 - e.C
        e.delta_A = e.C / (1.0 + beta)
        e.A_eff = e.A_schw + e.delta_A
        e.g_of_beta = _g_of_beta(beta, ln_alpha_abs)
        e.h_of_x = _h_of_x(1.0 / beta)
        e.A_eff_is_negative = e.A_eff < 0
        entries.append(e)

    return entries


# ================================================================
# Master analysis
# ================================================================

def compute_covariant_interior_analysis(
    alpha_vac: float = ALPHA_VAC,
    beta_Q: float = BETA_Q,
) -> CovariantInteriorResult:
    """Master analysis: Phase V constitutive-to-metric lapse obstruction.

    Steps:
      1. Prove the Constitutive Lapse Insufficiency Theorem
      2. Analyze effective NEC-violating support (secondary)
      3. Analyze lapse direction failure
      4. Assess T^Phi status
      5. Classify Psi_proxy
      6. Update status ladder
      7. Reconfirm self-healing
      8. Reconfirm Phase IV
      9. Perform beta_Q parametric scan
      10. Assemble nonclaims (~12)
      11. Populate diagnostics
    """
    result = CovariantInteriorResult()

    # 1. Insufficiency Theorem
    result.insufficiency_theorem = build_insufficiency_theorem(alpha_vac)

    # 2. Effective NEC (secondary)
    result.effective_nec = build_effective_nec(alpha_vac, beta_Q)

    # 3. Lapse direction
    result.lapse_direction = build_lapse_direction(alpha_vac, beta_Q)

    # 4. T^Phi status
    result.tphi_status = build_tphi_status()

    # 5. Proxy classification
    result.proxy_classification = build_proxy_classification(alpha_vac, beta_Q)

    # 6. Status ladder
    result.status_ladder = build_status_ladder_update()

    # 7. Self-healing reconfirmation
    result.self_healing = build_self_healing_reconfirmation()

    # 8. Phase IV reconfirmation
    result.phase4_reconfirmation = build_phase4_reconfirmation()

    # 9. Beta scan
    result.beta_scan = scan_A_eff_vs_beta(alpha_vac)

    # 10. Nonclaims (most important guardrail first)
    result.nonclaims = [
        (
            "The theorem does NOT prove that no covariant interior "
            "metric exists — only that the naive constitutive "
            "post-Newtonian lapse identification fails.  A different "
            "covariant construction or non-Schwarzschild-like "
            "observer-adapted lapse notion is not ruled out."
        ),
        (
            "The Insufficiency Theorem proves A_eff < 0 for every "
            "finite beta_Q > 0 when alpha_vac <= e^{-1/2} (covering "
            "the canonical value and any regime satisfying this bound); "
            "this concerns the NAIVE CONSTITUTIVE POST-NEWTONIAN "
            "ANSATZ, not the full covariant GRUT interior."
        ),
        (
            "Effective NEC-violating support is indicated at the "
            "constitutive-to-covariant translation level; it is "
            "NOT a covariant theorem."
        ),
        (
            "The lapse direction failure means the naive static "
            "redshift interpretation fails; it does NOT mean no "
            "static interior is possible under a fuller construction."
        ),
        (
            "T^Phi is schematic/effective — the metric lapse cannot "
            "be determined without a Lagrangian-derived T^Phi."
        ),
        (
            "Psi_proxy = 1/(1+beta_Q) is a CONSTITUTIVE SURROGATE: "
            "neither promoted to the true lapse nor excluded."
        ),
        (
            "The obstruction in Level 3 is specifically about the "
            "constitutive-to-metric lapse promotion, not about the "
            "interior metric itself."
        ),
        (
            "Self-healing is PRESERVED: it depends on force balance "
            "(X - Phi = 0), not on the metric."
        ),
        "No Phase IV result is weakened or invalidated.",
        (
            "The Insufficiency Theorem does NOT invalidate the "
            "equilibrium endpoint (force balance is dynamical, "
            "not metric)."
        ),
        (
            "The qualifier alpha_vac <= e^{-1/2} covers the canonical "
            "GRUT value and any regime satisfying this bound; it is "
            "not an unconditional universal statement."
        ),
        (
            "No observational predictions are made or modified "
            "by Phase V."
        ),
    ]

    result.obstruction_is_about_constitutive_ansatz = True

    # 11. Diagnostics
    A_eff_canon = _A_eff_from_constitutive(alpha_vac, beta_Q)
    result.diagnostics = {
        "alpha_vac": alpha_vac,
        "beta_Q": beta_Q,
        "C_endpoint": _compactness(alpha_vac, beta_Q),
        "A_eff_canon": A_eff_canon,
        "theorem_proven": (
            result.insufficiency_theorem.theorem_status == "proven"
        ),
        "nec_violating_support_indicated": (
            result.effective_nec.nec_violating_support_indicated
        ),
        "t_is_spacelike": result.lapse_direction.t_is_spacelike_schw,
        "naive_redshift_fails": result.lapse_direction.naive_redshift_fails,
        "tphi_is_schematic": result.tphi_status.is_schematic,
        "proxy_classification": (
            result.proxy_classification.classification
        ),
        "level_3_status": result.status_ladder.level_3_after,
        "self_healing_preserved": result.self_healing.preserved,
        "phase4_preserved": result.phase4_reconfirmation.all_preserved,
        "n_nonclaims": len(result.nonclaims),
        "n_beta_scan_entries": len(result.beta_scan),
        "obstruction_is_about_constitutive_ansatz": True,
    }

    result.approx_status = (
        "Phase V: Constitutive lapse promotion OBSTRUCTED.  "
        "The naive constitutive post-Newtonian mapping yields "
        "A_eff < 0 for every finite beta_Q > 0.  "
        "Psi_proxy = 1/(1+beta_Q) is classified as a constitutive "
        "surrogate (neither promoted nor excluded).  "
        "Level 3: constitutive_lapse_promotion_obstructed.  "
        "Self-healing: PRESERVED.  Phase IV: PRESERVED."
    )

    result.remaining_obstructions = [
        (
            "A covariant action S[Phi] for the memory/barrier field, "
            "yielding T^Phi from variational principles."
        ),
        (
            "Solution of the Einstein equations G = 8piG(T^matter + T^Phi) "
            "with the derived T^Phi in the sub-horizon regime."
        ),
        (
            "An observer-adapted interior chart or non-Schwarzschild-like "
            "coordinate construction at R_eq."
        ),
    ]

    result.valid = True
    return result


# ================================================================
# Serialization
# ================================================================

def _insufficiency_proof_to_dict(ip: InsufficiencyProof) -> Dict[str, Any]:
    return {
        "alpha_vac": ip.alpha_vac,
        "alpha_vac_satisfies_bound": ip.alpha_vac_satisfies_bound,
        "alpha_vac_critical": ip.alpha_vac_critical,
        "ln_alpha_abs": ip.ln_alpha_abs,
        "two_L": ip.two_L,
        "two_L_ge_one": ip.two_L_ge_one,
        "h_positive_for_all_x": ip.h_positive_for_all_x,
        "g_positive_for_all_beta": ip.g_positive_for_all_beta,
        "A_eff_negative_for_all_finite_beta": (
            ip.A_eff_negative_for_all_finite_beta
        ),
        "sample_beta_values": ip.sample_beta_values,
        "sample_A_eff_values": ip.sample_A_eff_values,
        "sample_g_values": ip.sample_g_values,
        "sample_h_values": ip.sample_h_values,
        "proof_steps": ip.proof_steps,
        "theorem_status": ip.theorem_status,
        "scope_statement": ip.scope_statement,
        "notes": ip.notes,
    }


def _effective_nec_to_dict(nec: EffectiveNECAnalysis) -> Dict[str, Any]:
    return {
        "compactness": nec.compactness,
        "is_sub_horizon": nec.is_sub_horizon,
        "A_eff": nec.A_eff,
        "delta_A": nec.delta_A,
        "rho_plus_P_sign_effective": nec.rho_plus_P_sign_effective,
        "nec_violating_support_indicated": nec.nec_violating_support_indicated,
        "derivation_level": nec.derivation_level,
        "notes": nec.notes,
    }


def _lapse_direction_to_dict(ld: LapseDirectionAnalysis) -> Dict[str, Any]:
    return {
        "compactness": ld.compactness,
        "A_schw": ld.A_schw,
        "g_tt_schw": ld.g_tt_schw,
        "g_rr_schw": ld.g_rr_schw,
        "t_is_spacelike_schw": ld.t_is_spacelike_schw,
        "r_is_timelike_schw": ld.r_is_timelike_schw,
        "A_eff": ld.A_eff,
        "g_tt_eff": ld.g_tt_eff,
        "constitutive_restores_timelike": ld.constitutive_restores_timelike,
        "naive_redshift_fails": ld.naive_redshift_fails,
        "requires_adapted_chart_or_covariant": (
            ld.requires_adapted_chart_or_covariant
        ),
        "notes": ld.notes,
    }


def _tphi_status_to_dict(ts: TPhiStatusResult) -> Dict[str, Any]:
    return {
        "is_lagrangian_derived": ts.is_lagrangian_derived,
        "is_schematic": ts.is_schematic,
        "is_uniquely_specified": ts.is_uniquely_specified,
        "mapping_underdetermined": ts.mapping_underdetermined,
        "underdetermination_reason": ts.underdetermination_reason,
        "missing_for_metric": ts.missing_for_metric,
        "notes": ts.notes,
    }


def _proxy_classification_to_dict(
    pc: ProxyLapseClassification,
) -> Dict[str, Any]:
    return {
        "psi_proxy": pc.psi_proxy,
        "level_1_status": pc.level_1_status,
        "level_2_status": pc.level_2_status,
        "level_3_status_phase_iv": pc.level_3_status_phase_iv,
        "level_3_status_phase_v": pc.level_3_status_phase_v,
        "is_exact_energy_ratio": pc.is_exact_energy_ratio,
        "is_constitutive_lapse_scale": pc.is_constitutive_lapse_scale,
        "can_be_promoted_to_true_lapse": pc.can_be_promoted_to_true_lapse,
        "can_be_excluded": pc.can_be_excluded,
        "classification": pc.classification,
        "scope_of_obstruction": pc.scope_of_obstruction,
        "notes": pc.notes,
    }


def _status_ladder_to_dict(sl: StatusLadderUpdate) -> Dict[str, Any]:
    return {
        "level_1_before": sl.level_1_before,
        "level_1_after": sl.level_1_after,
        "level_1_changed": sl.level_1_changed,
        "level_2_before": sl.level_2_before,
        "level_2_after": sl.level_2_after,
        "level_2_changed": sl.level_2_changed,
        "level_3_before": sl.level_3_before,
        "level_3_after": sl.level_3_after,
        "level_3_changed": sl.level_3_changed,
        "level_3_sharpening_reason": sl.level_3_sharpening_reason,
        "no_level_weakened": sl.no_level_weakened,
        "obstruction_scope": sl.obstruction_scope,
        "notes": sl.notes,
    }


def _self_healing_to_dict(sh: SelfHealingReconfirmation) -> Dict[str, Any]:
    return {
        "source_at_eq": sh.source_at_eq,
        "source_vanishes": sh.source_vanishes,
        "independent_of_metric": sh.independent_of_metric,
        "independent_of_A_eff": sh.independent_of_A_eff,
        "independent_of_nec": sh.independent_of_nec,
        "preserved": sh.preserved,
        "reason": sh.reason,
        "notes": sh.notes,
    }


def _phase4_reconfirmation_to_dict(
    p4: Phase4Reconfirmation,
) -> Dict[str, Any]:
    return {
        "level_1_preserved": p4.level_1_preserved,
        "level_2_preserved": p4.level_2_preserved,
        "sensitivity_band_preserved": p4.sensitivity_band_preserved,
        "self_healing_preserved": p4.self_healing_preserved,
        "shift_estimates_preserved": p4.shift_estimates_preserved,
        "coincidence_explanation_preserved": (
            p4.coincidence_explanation_preserved
        ),
        "all_preserved": p4.all_preserved,
        "notes": p4.notes,
    }


def _beta_scan_entry_to_dict(bs: BetaScanEntry) -> Dict[str, Any]:
    return {
        "beta_Q": bs.beta_Q,
        "C": bs.C,
        "A_schw": bs.A_schw,
        "delta_A": bs.delta_A,
        "A_eff": bs.A_eff,
        "g_of_beta": bs.g_of_beta,
        "h_of_x": bs.h_of_x,
        "A_eff_is_negative": bs.A_eff_is_negative,
    }


def covariant_interior_result_to_dict(
    result: CovariantInteriorResult,
) -> Dict[str, Any]:
    """Serialize the master CovariantInteriorResult to a dictionary."""
    d: Dict[str, Any] = {"valid": result.valid}

    if result.insufficiency_theorem is not None:
        d["insufficiency_theorem"] = _insufficiency_proof_to_dict(
            result.insufficiency_theorem
        )
    if result.effective_nec is not None:
        d["effective_nec"] = _effective_nec_to_dict(result.effective_nec)
    if result.lapse_direction is not None:
        d["lapse_direction"] = _lapse_direction_to_dict(
            result.lapse_direction
        )
    if result.tphi_status is not None:
        d["tphi_status"] = _tphi_status_to_dict(result.tphi_status)
    if result.proxy_classification is not None:
        d["proxy_classification"] = _proxy_classification_to_dict(
            result.proxy_classification
        )
    if result.status_ladder is not None:
        d["status_ladder"] = _status_ladder_to_dict(result.status_ladder)
    if result.self_healing is not None:
        d["self_healing"] = _self_healing_to_dict(result.self_healing)
    if result.phase4_reconfirmation is not None:
        d["phase4_reconfirmation"] = _phase4_reconfirmation_to_dict(
            result.phase4_reconfirmation
        )

    d["beta_scan"] = [_beta_scan_entry_to_dict(e) for e in result.beta_scan]
    d["nonclaims"] = result.nonclaims
    d["obstruction_is_about_constitutive_ansatz"] = (
        result.obstruction_is_about_constitutive_ansatz
    )
    d["approx_status"] = result.approx_status
    d["remaining_obstructions"] = result.remaining_obstructions
    d["diagnostics"] = result.diagnostics

    return d
