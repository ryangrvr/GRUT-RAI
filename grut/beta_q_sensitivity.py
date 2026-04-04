"""β_Q Sensitivity Analysis.

β_Q = 2 is a canon assumption of the GRUT architecture — it sets the
barrier steepness exponent and determines the equilibrium endpoint.

STATUS: assumed, not derived.
  stability_consistency_audit.py:
    "BETA_Q = 2.0  # dimensionless — barrier exponent (ASSUMED, not derived)"

β_Q DETERMINES:
  1. Endpoint law:      (R_eq/r_s)^β_Q = ε_Q  →  R_eq/r_s = 1/3 at β_Q = 2
  2. Barrier frequency: ω₀² = β_Q · GM/R_eq³  →  ω₀ shifts with both β_Q and R_eq
  3. Lapse proxy:       Ψ_proxy = 1/(1+β_Q) = 1/3 = α_vac  (coincidence at β_Q = 2)
  4. Quantum pressure:  a_Q = a_grav · ε_Q · (r_s/R)^β_Q

CANON ASSUMPTION ENCODING
--------------------------
  ε_Q(β_Q) follows from a SELF-CONSISTENCY CONDITION on the endpoint law.
  At the canonical endpoint: Ψ_proxy = 1/(1+β_Q) = α_vac.
  If α_vac is fixed (= 1/3), then β_Q = 1/α_vac − 1.
  For α_vac = 1/3: β_Q = 2.  ← This is the self-consistency that selects β_Q = 2.

  The canon ε_Q = (R_eq/r_s)^β_Q is therefore the DERIVED consequence:
    ε_Q = α_vac^β_Q = (1/3)^2 = 1/9.

  So the assumption chain is:
    α_vac = 1/3  (vacuum fraction, set by the equilibrium sector)
    ↓ (via Ψ_proxy = α_vac = 1/(1+β_Q))
    β_Q = 2  (DERIVED from α_vac IF the Ψ_proxy coincidence is exact)
    ↓
    ε_Q = (1/3)^2 = 1/9
    ↓
    R_eq/r_s = ε_Q^(1/β_Q) = (1/9)^(1/2) = 1/3  (consistent)

  BUT: the Ψ_proxy coincidence itself is not derived — it is observed.
  The derivation Ψ_proxy = α_vac requires a separate justification
  (why the barrier-to-gravity lapse ratio exactly equals the vacuum fraction).
  This justification is currently absent.

SENSITIVITY SWEEP
-----------------
For each test β_Q, fixing α_vac = 1/3 and ε_Q = α_vac^β_Q:

  R_eq/r_s = α_vac  (independent of β_Q if ε_Q = α_vac^β_Q)
  ω₀² = β_Q · GM/R_eq³  (scales linearly with β_Q)
  Ψ_proxy = 1/(1+β_Q)  (moves away from α_vac if β_Q ≠ 2)
  α_vac − Ψ_proxy = coincidence gap

For the downstream locked results (A_crit, κ_ratio = 3/5, T_Killing/T_Hawking = 3/5,
first-law gap R = 1.209), these all depend on R_eq, τ², and M through the
deficit chain.  If ε_Q = α_vac^β_Q (self-consistent encoding), then R_eq = α_vac · r_s
is β_Q-INDEPENDENT.  However τ² = C_eq/2 may depend on β_Q through the
equilibrium condition.  The locked ratios are therefore:
  - FORM-PRESERVED if τ² and R_eq are held fixed
  - VALUE-SHIFTED if τ² changes with β_Q

BLAST RADIUS CLASSIFICATION
----------------------------
  β_Q-INVARIANT (form preserved regardless of β_Q):
    - Self-healing condition: X - Φ = 0 at equilibrium (independent of β_Q)
    - ω₀·τ_eff = 1 structural identity (by definition at equilibrium)
    - Galley CTP structure (not β_Q-dependent)

  β_Q-SENSITIVE (values shift with β_Q, forms may also change):
    - ω₀ = sqrt(β_Q · GM/R_eq³): scales as √β_Q (at fixed R_eq)
    - Ψ_proxy = 1/(1+β_Q): moves away from α_vac
    - ε_Q = α_vac^β_Q: changes if α_vac fixed, β_Q varies
    - τ_eff_canon = 1/ω₀: inversely proportional to √β_Q
    - All quantities depending on τ_eff_canon: A_crit, κ_GRUT, T_Killing, R (first-law)

  CONDITIONALLY β_Q-SENSITIVE (depend on τ²(β_Q)):
    - κ_GRUT/κ_Schw = 3/5: exact at β_Q=2; shifts if τ² shifts
    - T_Killing/T_Hawking = 3/5: same
    - First-law gap R = 1.209: same

STATUS: working canon hypothesis.
  Classification: "working_hypothesis__derived_from_observed_Psi_proxy_coincidence__"
                  "coincidence_not_independently_justified"

References
----------
  effective_lapse.py          — Ψ_proxy = 1/(1+β_Q); endpoint law
  collapse.py                 — a_Q = a_grav · ε_Q · (r_s/R)^β_Q
  interior_pde.py             — ω₀² = β_Q · GM/R_eq³
  stability_consistency_audit.py — explicit "ASSUMED, not derived"
  interior_metric_closure.py  — A_crit, κ_GRUT, T_Killing (locked at β_Q = 2)
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

# ---------------------------------------------------------------------------
# Canon constants (β_Q = 2)
# ---------------------------------------------------------------------------
BETA_Q_CANON: float = 2.0
ALPHA_VAC: float = 1.0 / 3.0
EPSILON_Q_CANON: float = ALPHA_VAC ** BETA_Q_CANON   # = 1/9
R_EQ_OVER_RS: float = ALPHA_VAC                      # = 1/3 (self-consistent)
M_EXT: float = 0.5
R_S: float = 2.0 * M_EXT                             # = 1.0
R_EQ: float = R_EQ_OVER_RS * R_S                     # = 1/3
TAU_SQ_CANON: float = 1.5                            # τ² = 3/2 (locked at β_Q = 2)

# ψ_proxy coincidence (observed, not derived)
PSI_PROXY_CANON: float = 1.0 / (1.0 + BETA_Q_CANON)  # = 1/3 = α_vac ← coincidence
COINCIDENCE_GAP_CANON: float = ALPHA_VAC - PSI_PROXY_CANON  # = 0.0

# ω₀ at canon β_Q
OMEGA_0_SQ_CANON: float = BETA_Q_CANON * M_EXT / (R_EQ ** 3)   # = 13.5
OMEGA_0_CANON: float = math.sqrt(OMEGA_0_SQ_CANON)             # ≈ 3.674

# Locked downstream results (from interior_metric_closure.py, β_Q = 2)
KAPPA_RATIO_LOCKED: float = 3.0 / 5.0        # κ_GRUT/κ_Schw = 3/5
T_KILLING_RATIO_LOCKED: float = 3.0 / 5.0   # T_Killing/T_Hawking = 3/5
A_CRIT_LOCKED: float = math.sqrt(1.0 + 2.0 / (5.0 * math.pi))  # ≈ 1.062
FIRST_LAW_GAP_LOCKED: float = 1.209          # R = dS/dM · T/(dS/dR · dR/dM)


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class BetaQAssumption:
    """Formal declaration of the β_Q = 2 canon assumption."""
    value: float              # 2.0
    status: str               # "working_hypothesis__not_derived"
    derivation_chain: str     # how β_Q = 2 is selected in the current architecture
    blocking_gap: str         # why the derivation is incomplete
    psi_proxy_coincidence: float    # Ψ_proxy = 1/(1+β_Q) = α_vac at β_Q = 2
    coincidence_justified: bool     # False: coincidence is observed, not derived
    notes: List[str] = field(default_factory=list)


@dataclass
class SensitivityPoint:
    """Results at a single test β_Q value."""
    beta_q: float
    epsilon_q: float              # α_vac^β_Q (self-consistent encoding)
    r_eq_over_rs: float           # = α_vac (β_Q-independent if ε_Q = α_vac^β_Q)
    omega_0_sq: float             # β_Q · GM/R_eq³
    omega_0: float                # sqrt(ω₀²)
    tau_eff_canon: float          # 1/ω₀  (from ω₀·τ_eff = 1)
    psi_proxy: float              # 1/(1+β_Q)
    coincidence_gap: float        # α_vac − Ψ_proxy
    coincidence_holds: bool       # |gap| < tol
    # Conditionally sensitive (depend on τ²(β_Q), set to NaN if τ² unknown)
    kappa_ratio: float            # κ_GRUT/κ_Schw (NaN if τ² not known)
    a_crit: float                 # critical amplitude (NaN if τ² not known)


@dataclass
class BlastRadiusClassification:
    """Classification of which results are β_Q-invariant vs sensitive."""
    invariant: List[str]          # results unchanged regardless of β_Q
    sensitive_value: List[str]    # values shift with β_Q
    sensitive_form: List[str]     # algebraic structure also changes
    conditional: List[str]        # depend on τ²(β_Q), which is not yet computed


@dataclass
class BetaQSensitivityResult:
    """Master result of the β_Q sensitivity analysis."""
    assumption: BetaQAssumption
    sensitivity_points: List[SensitivityPoint]
    blast_radius: BlastRadiusClassification
    beta_q_canon: float
    r_eq_independent_of_beta_q: bool  # True (under self-consistent ε_Q encoding)
    omega_0_scales_as_sqrt_beta_q: bool  # True (at fixed R_eq)
    psi_proxy_coincidence_breaks: bool   # True (for β_Q ≠ 2)
    verdict: str
    nonclaims: List[str]
    diagnostics: Dict[str, Any]


# ---------------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------------

def _compute_sensitivity_point(beta_q: float) -> SensitivityPoint:
    """Compute sensitivity metrics at a given β_Q.

    Uses self-consistent encoding: ε_Q = α_vac^β_Q, so R_eq/r_s = α_vac
    is β_Q-independent.  ω₀ scales as sqrt(β_Q) at fixed R_eq.
    """
    epsilon_q = ALPHA_VAC ** beta_q
    r_eq_over_rs = ALPHA_VAC        # invariant under self-consistent ε_Q encoding
    r_eq_local = r_eq_over_rs * R_S

    omega_0_sq = beta_q * M_EXT / (r_eq_local ** 3)
    omega_0 = math.sqrt(omega_0_sq)
    tau_eff_c = 1.0 / omega_0       # from ω₀·τ_eff = 1

    psi_proxy = 1.0 / (1.0 + beta_q)
    gap = ALPHA_VAC - psi_proxy
    coincidence = abs(gap) < 1e-10

    # For downstream results (κ_ratio, A_crit), we would need τ²(β_Q).
    # τ² is locked at 3/2 at β_Q = 2 from the equilibrium condition.
    # How τ² scales with β_Q is not yet established.
    # We mark these as NaN for β_Q ≠ β_Q_canon.
    tol = 1e-10
    if abs(beta_q - BETA_Q_CANON) < tol:
        kappa_ratio = KAPPA_RATIO_LOCKED
        a_crit = A_CRIT_LOCKED
    else:
        # Cannot compute without τ²(β_Q) formula
        kappa_ratio = float("nan")
        a_crit = float("nan")

    return SensitivityPoint(
        beta_q=beta_q,
        epsilon_q=epsilon_q,
        r_eq_over_rs=r_eq_over_rs,
        omega_0_sq=omega_0_sq,
        omega_0=omega_0,
        tau_eff_canon=tau_eff_c,
        psi_proxy=psi_proxy,
        coincidence_gap=gap,
        coincidence_holds=coincidence,
        kappa_ratio=kappa_ratio,
        a_crit=a_crit,
    )


def build_assumption() -> BetaQAssumption:
    """Document the β_Q = 2 assumption."""
    return BetaQAssumption(
        value=BETA_Q_CANON,
        status="working_hypothesis__derived_from_observed_Psi_proxy_coincidence__coincidence_not_independently_justified",
        derivation_chain=(
            "Observed coincidence: Ψ_proxy = 1/(1+β_Q) = α_vac = 1/3 at β_Q = 2.  "
            "If this coincidence is imposed as a constraint, then β_Q = 1/α_vac − 1 = 2.  "
            "This selects β_Q = 2 GIVEN α_vac = 1/3.  "
            "But the coincidence Ψ_proxy = α_vac is not derived — it is observed in the "
            "effective_lapse.py output and taken as a structural fact."
        ),
        blocking_gap=(
            "The coincidence Ψ_proxy = α_vac is not derived from first principles.  "
            "Ψ_proxy = 1/(1+β_Q) is the barrier-to-gravity lapse ratio (effective_lapse.py).  "
            "α_vac = 1/3 is the vacuum fraction from the equilibrium sector.  "
            "Why these should be equal is unestablished.  "
            "Without this justification, β_Q = 2 remains an observed coincidence, not a derivation."
        ),
        psi_proxy_coincidence=PSI_PROXY_CANON,
        coincidence_justified=False,
        notes=[
            f"β_Q = {BETA_Q_CANON}  (ASSUMED — stability_consistency_audit.py)",
            f"Ψ_proxy = 1/(1+β_Q) = {PSI_PROXY_CANON:.4f}  (barrier-to-gravity lapse ratio)",
            f"α_vac = {ALPHA_VAC:.4f}  (vacuum fraction)",
            f"coincidence gap = {COINCIDENCE_GAP_CANON:.6f}  (exact zero at β_Q = 2)",
            "If α_vac were not 1/3, the same logic would select a different β_Q.",
            "The self-consistency of the canon selection depends on α_vac = 1/3 being exact.",
        ],
    )


def build_sensitivity_sweep(
    test_values: List[float] = None,
) -> List[SensitivityPoint]:
    """Compute sensitivity at test β_Q values."""
    if test_values is None:
        test_values = [1.0, 1.5, 2.0, 2.5, 3.0, 4.0]
    return [_compute_sensitivity_point(b) for b in test_values]


def build_blast_radius() -> BlastRadiusClassification:
    """Classify which results are β_Q-invariant vs sensitive."""
    return BlastRadiusClassification(
        invariant=[
            "Self-healing condition X - Phi = 0 at equilibrium (ODE fixed point, β_Q-independent)",
            "ω₀ · τ_eff = 1 structural identity (holds at equilibrium by definition)",
            "R_eq/r_s = α_vac = 1/3  (under self-consistent ε_Q = α_vac^β_Q encoding)",
            "Galley CTP doubled-field structure (not β_Q-dependent)",
            "rho_eq profile shape ~ 1/r⁴ (from Phi_eq = M/r² form, independent of β_Q)",
        ],
        sensitive_value=[
            "ω₀ = sqrt(β_Q · GM/R_eq³): scales as √β_Q (value changes, form preserved)",
            "τ_eff_canon = 1/ω₀: inversely proportional to √β_Q (value changes)",
            "ε_Q = α_vac^β_Q: changes with β_Q (even at fixed α_vac)",
            "Ψ_proxy = 1/(1+β_Q): moves away from α_vac for β_Q ≠ 2",
            "rho_eq magnitude at R_eq: -M²/(2τ²R_eq⁴) shifts if τ² depends on β_Q",
        ],
        sensitive_form=[
            "ω₀² = β_Q · GM/R_eq³: form changes (linear in β_Q)",
            "a_Q = a_grav · ε_Q · (r_s/R)^β_Q: exponent in radial power law changes",
            "Coincidence Ψ_proxy = α_vac: breaks for β_Q ≠ 2 (form change: gap ≠ 0)",
        ],
        conditional=[
            "κ_GRUT/κ_Schw = 3/5: exact at β_Q = 2; requires τ²(β_Q) formula to compute elsewhere",
            "T_Killing/T_Hawking = 3/5: same (depends on κ_GRUT)",
            "A_crit = sqrt(1 + 2/(5π)): locked at β_Q = 2; requires τ²(β_Q) for general β_Q",
            "First-law gap R = 1.209: depends on R_eq and T (β_Q-sensitive via τ_eff)",
            "rho_eq at R_eq = -6.75: the specific value requires τ² = 3/2 (β_Q = 2 only)",
        ],
    )


def assign_verdict(assumption: BetaQAssumption, points: List[SensitivityPoint]) -> str:
    """Compute verdict from assumption status and sweep results."""
    if assumption.coincidence_justified:
        return "beta_q_derived__coincidence_justified__full_closure"
    else:
        # Check: does R_eq remain invariant across sweep?
        r_eq_values = [p.r_eq_over_rs for p in points]
        r_eq_invariant = all(abs(r - ALPHA_VAC) < 1e-10 for r in r_eq_values)

        # Check: does Ψ_proxy coincidence break for β_Q ≠ 2?
        coincidence_breaks = any(
            not p.coincidence_holds for p in points if abs(p.beta_q - BETA_Q_CANON) > 1e-6
        )

        if r_eq_invariant and coincidence_breaks:
            return (
                "beta_q_assumed__Psi_proxy_coincidence_unverified__"
                "R_eq_invariant_under_self_consistent_encoding__"
                "omega0_and_downstream_ratios_beta_q_sensitive"
            )
        else:
            return "beta_q_assumed__sensitivity_undetermined"


def run_beta_q_sensitivity(
    test_values: List[float] = None,
) -> BetaQSensitivityResult:
    """Run the β_Q sensitivity analysis."""
    if test_values is None:
        test_values = [1.0, 1.5, 2.0, 2.5, 3.0, 4.0]

    assumption = build_assumption()
    points = build_sensitivity_sweep(test_values)
    blast = build_blast_radius()
    verdict = assign_verdict(assumption, points)

    # Derived summaries from sweep
    r_eq_invariant = all(abs(p.r_eq_over_rs - ALPHA_VAC) < 1e-10 for p in points)

    omega_0_at_canon = next(p.omega_0 for p in points if abs(p.beta_q - BETA_Q_CANON) < 1e-6)
    omega_0_at_half = next(
        (p.omega_0 for p in points if abs(p.beta_q - 1.0) < 1e-6), None
    )
    omega_0_scales_as_sqrt = (
        omega_0_at_half is not None and
        abs(omega_0_at_half / omega_0_at_canon - math.sqrt(1.0 / BETA_Q_CANON)) < 1e-6
    )

    psi_proxy_breaks = any(
        not p.coincidence_holds for p in points if abs(p.beta_q - BETA_Q_CANON) > 1e-6
    )

    nonclaims = [
        "NOT claiming β_Q = 2 is wrong — it is the self-consistent canon value.",
        "NOT claiming the κ_ratio = 3/5 and T_Killing ratio are incorrect — they are "
        "exact at β_Q = 2 and remain locked unless β_Q and τ² both shift.",
        "NOT claiming A_crit formula changes form — it changes value if τ² changes.",
        "NOT claiming R_eq/r_s = 1/3 is β_Q-sensitive — under self-consistent ε_Q encoding, "
        "R_eq/r_s = α_vac is invariant.",
        "The NaN entries for κ_ratio and A_crit at β_Q ≠ 2 reflect missing τ²(β_Q), "
        "not a failure of the computation.",
    ]

    diagnostics: Dict[str, Any] = {
        "BETA_Q_CANON": BETA_Q_CANON,
        "ALPHA_VAC": ALPHA_VAC,
        "EPSILON_Q_CANON": EPSILON_Q_CANON,
        "R_EQ_OVER_RS": R_EQ_OVER_RS,
        "TAU_SQ_CANON": TAU_SQ_CANON,
        "OMEGA_0_CANON": OMEGA_0_CANON,
        "PSI_PROXY_CANON": PSI_PROXY_CANON,
        "COINCIDENCE_GAP_CANON": COINCIDENCE_GAP_CANON,
        "KAPPA_RATIO_LOCKED": KAPPA_RATIO_LOCKED,
        "A_CRIT_LOCKED": A_CRIT_LOCKED,
        "FIRST_LAW_GAP_LOCKED": FIRST_LAW_GAP_LOCKED,
        "r_eq_invariant_across_sweep": r_eq_invariant,
        "omega_0_scales_as_sqrt_beta_q": omega_0_scales_as_sqrt,
        "psi_proxy_coincidence_breaks_for_beta_q_ne_2": psi_proxy_breaks,
        "coincidence_justified": assumption.coincidence_justified,
        "verdict": verdict,
    }

    return BetaQSensitivityResult(
        assumption=assumption,
        sensitivity_points=points,
        blast_radius=blast,
        beta_q_canon=BETA_Q_CANON,
        r_eq_independent_of_beta_q=r_eq_invariant,
        omega_0_scales_as_sqrt_beta_q=omega_0_scales_as_sqrt,
        psi_proxy_coincidence_breaks=psi_proxy_breaks,
        verdict=verdict,
        nonclaims=nonclaims,
        diagnostics=diagnostics,
    )
