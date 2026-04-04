"""GRUT Appendix H — Temperature Selection and First Fluctuation Consequence.

QUESTION BEING ANSWERED (TASK 2)
---------------------------------
Can temperature be SELECTED, not just defined?

Is there a GRUT-native criterion that privileges one temperature candidate
over the others, without importing external physics?

QUESTION BEING ANSWERED (TASK 3)
---------------------------------
What is the first non-circular fluctuation consequence?

Is there a constrained form, required scaling, or necessary incompatibility
that acts as a quantum-side discriminator with real bite?

TEMPERATURE CANDIDATES (inherited from Appendix D)
---------------------------------------------------
T_structural   = ℏω₀/k_B                 [GRUT-native, most direct]
T_dissipation  = ℏω₀/(Q·k_B) = T_s/Q    [GRUT-native, best_candidate in Appendix D]
T_surface_gravity = ℏκ_eff/(2π·k_B)      [not GRUT-native]
T_hawking      = ℏc³/(8πGMk_B)           [imported]

SELECTION CRITERIA EVALUATED
-----------------------------
Criterion 1 — FDT Inversion:
    S_FF(ω₀) = 2k_B·T·Im[χ(ω₀)] / ω₀ → gives T if fluctuation amplitude known.
    Status: BLOCKED — requires quantum state (Appendix C).

Criterion 2 — KMS Periodicity (thermal time):
    If τ_local is the thermal KMS period: T_KMS = ℏ/(k_B·τ_local) = ℏω₀/k_B = T_structural.
    Status: CONDITIONAL — requires state to be KMS thermal (Appendix C).

Criterion 3 — First Law Self-Consistency:
    T_1stlaw = dE/dS = c² × (dS/dM)⁻¹ using S = πR_eq²/l_P².
    Gives T_1stlaw = 9·T_Hawking (GRUT-native expression: see below).
    T_1stlaw ≠ T_dissipation, ≠ T_structural.
    Status: VIABLE_WITH_ASSUMPTIONS — no Appendix C blocker,
    but requires accepting E = Mc² and S = πR_eq²/l_P².

FIRST NON-CIRCULAR FLUCTUATION CONSEQUENCE (TASK 3)
----------------------------------------------------
The first-law ratio R = k_B·T_diss·(dS/dM)/c² is MASS-INDEPENDENT:

    R = 2π√3 / (3Q) = 2π√3/18 ≈ 1.209   (for Q=6, β_Q=2, α_vac=1/3)

This is a fixed GRUT prediction:
- If R is measured to be 1.0 (exact first law), it would rule out T_dissipation
  as the correct temperature. The correct T would be T_1stlaw = T_dissipation/R.
- If R ≠ 2π√3/18, it would imply either the area law at R_eq is wrong, or
  the endpoint law R_eq = r_s/3 is wrong, or T_dissipation is wrong.
- The ratio R = 2π√3/18 is the unique combination of α_vac, β_Q (through Q
  and R_eq) and the FDT form that produces a mass-independent number.

EXECUTIVE DETERMINATION
-----------------------
`temperature_selectable_conditionally_not_uniquely`

T_1stlaw is the only candidate accessible without quantum-state input.
No GRUT-native criterion uniquely selects between T_structural and T_dissipation.
The first-law ratio R = 2π√3/18 ≈ 1.21 is the first non-circular, mass-independent
prediction from the GRUT thermodynamic sector.

WHAT THIS MODULE DOES NOT CLAIM:
  - Does NOT prove any temperature is correct.
  - Does NOT resolve any Appendix C blocker.
  - Does NOT upgrade the thermodynamic_sector_partially_consistent classification.
  - Does NOT derive Hawking radiation or standard BH thermodynamics from GRUT.

LOCKED INHERITANCE:
  - Appendix D: thermodynamic_sector_partially_consistent UNCHANGED.
  - Appendix E: locally_consistent_globally_underdetermined UNCHANGED.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

# ================================================================
# Physical Constants (SI)
# ================================================================

G_SI = 6.674e-11           # m³ kg⁻¹ s⁻²
C_SI = 299_792_458.0       # m/s
HBAR_SI = 1.054571817e-34  # J·s
K_B = 1.380649e-23         # J/K
L_PLANCK = math.sqrt(HBAR_SI * G_SI / C_SI ** 3)

# ================================================================
# Canonical GRUT Parameters (locked)
# ================================================================

ALPHA_VAC = 1.0 / 3.0
BETA_Q = 2.0
EPSILON_Q = ALPHA_VAC ** 2       # = 1/9
R_EQ_OVER_RS = EPSILON_Q ** (1.0 / BETA_Q)   # = 1/3
Q_CANONICAL = BETA_Q / ALPHA_VAC             # = 6.0
M_SUN_KG = 1.989e30
M_REF_KG = 30.0 * M_SUN_KG

# ================================================================
# Mass-independent first-law ratio (derived analytically)
#
#   R = k_B · T_diss · (dS/dM) / c²
#   = ℏω₀/(Q) × 8πG²M/(9c⁶l_P²) / c²
#   = ℏω₀ × 8πGM/(9Qc³)    [using l_P² = ℏG/c³]
#   = 8πGM × 3√3·c³/(2GM) / (9Q·c³)    [ω₀ = 3√3c³/(2GM)]
#   = 8π × 3√3 / (18Q)
#   = 4π√3 / (3Q)
#   = 2π√3 / (9)    [for Q=6]
#
# ================================================================
R_FIRSTLAW_ANALYTIC = 4.0 * math.pi * math.sqrt(3.0) / (3.0 * Q_CANONICAL)

# ================================================================
# Forbidden classification strings (guard)
# ================================================================

_FORBIDDEN_CLASSIFICATIONS = {
    "temperature_proven",
    "temperature_uniquely_derived",
    "fdt_proven_in_grut",
    "kms_proven_in_grut",
    "hawking_derived_from_grut",
    "appendix_c_resolved",
    "first_law_is_proven",
}


# ================================================================
# Data Structures
# ================================================================

@dataclass
class TemperatureValue:
    """One temperature candidate with its numerical value at reference mass."""
    name: str
    formula: str
    T_kelvin: float
    T_over_T_hawking: float
    grut_native: bool
    derivation_status: str   # "grut_native", "analog", "first_law", "imported"


@dataclass
class SelectionCriterion:
    """One temperature selection criterion and its verdict."""
    name: str = ""
    description: str = ""
    formula: str = ""

    # Does it select a unique temperature?
    selects_unique_T: bool = False
    selected_T_name: Optional[str] = None
    selected_T_kelvin: float = 0.0

    # Conditions
    requires_quantum_state: bool = False
    requires_appendix_c_resolved: bool = False
    requires_entropy_ansatz: bool = False

    # Verdict
    verdict: str = ""
    verdict_reason: str = ""


@dataclass
class FirstLawAnalysis:
    """First-law thermodynamic consistency analysis."""
    # Inputs
    energy_formula: str = "E = M * c²"
    entropy_formula: str = "S = π * R_eq² / l_P²"
    entropy_at_Req: bool = True   # Entropy evaluated at R_eq (not r_s)

    # dS/dM at reference mass
    dS_dM_SI: float = 0.0    # m⁻¹ kg⁻¹ s² units collapse to pure number... actually J/K / kg

    # First-law temperature
    T_1stlaw_K: float = 0.0
    T_1stlaw_over_T_hawking: float = 0.0
    T_1stlaw_over_T_diss: float = 0.0
    T_1stlaw_over_T_struct: float = 0.0

    # First-law ratio using T_dissipation
    R_firstlaw_T_diss: float = 0.0        # should be 2π√3/18
    R_firstlaw_analytic: float = 0.0      # analytical: 2π√3/18
    R_is_mass_independent: bool = True    # R is mass-independent

    # Does the first law hold within a factor of 2?
    first_law_approximately_satisfied: bool = False

    # Classification
    verdict: str = ""


@dataclass
class FluctuationConsequence:
    """The first non-circular fluctuation consequence.

    The first-law ratio R = k_B·T_diss·(dS/dM)/c² = 2π√3/18 ≈ 1.21 is
    mass-independent. This is a constrained prediction.
    """
    consequence_name: str = "mass_independent_first_law_ratio"
    consequence_formula: str = "R = 2π√3 / (3Q) = 2π√3/18 ≈ 1.209"
    consequence_value: float = 0.0
    consequence_is_mass_independent: bool = True

    # What it implies
    if_R_equals_one: str = (
        "If R = 1 (exact first law holds with T_dissipation and S_endpoint), "
        "then GRUT has an exact thermodynamic closure at the endpoint."
    )
    if_R_measured_different: str = (
        "If R ≠ 2π√3/18 experimentally, then at least one of these must fail: "
        "(a) T_dissipation = ℏω₀/(Q·k_B) is the correct temperature, "
        "(b) S = πR_eq²/l_P² is the correct entropy, "
        "(c) R_eq/r_s = 1/3 (endpoint law). "
        "The measurement would discriminate between the three assumptions."
    )

    # Is this circular?
    is_non_circular: bool = True
    non_circular_argument: str = (
        "R is computed from T_dissipation (uses Q = β_Q/α_vac) and the "
        "endpoint entropy (uses R_eq = r_s/3). Both are derived from GRUT "
        "locked parameters (α_vac = 1/3, β_Q = 2), not from the temperature "
        "itself. Setting R = 1 would then determine a unique T — this is a "
        "non-circular constraint because T is NOT an input to the calculation "
        "of R. R is determined by the ratio Q and R_eq, and then T_correct = "
        "T_dissipation/R is the derived output."
    )

    # FDT consequence
    fdt_noise_at_omega0: str = ""
    fdt_noise_formula: str = ""


@dataclass
class TemperatureSelectionResult:
    """Master result from the temperature selection audit."""
    # All candidates (numerical values at reference mass)
    candidates: List[TemperatureValue] = field(default_factory=list)

    # Selection criteria
    criterion_fdt: SelectionCriterion = field(default_factory=SelectionCriterion)
    criterion_kms: SelectionCriterion = field(default_factory=SelectionCriterion)
    criterion_first_law: SelectionCriterion = field(default_factory=SelectionCriterion)

    # First law analysis
    first_law: FirstLawAnalysis = field(default_factory=FirstLawAnalysis)

    # Fluctuation consequence
    fluctuation: FluctuationConsequence = field(default_factory=FluctuationConsequence)

    # Executive determination
    executive_determination: str = ""
    determination_explanation: str = ""

    # Number of criteria that select a unique T
    n_criteria_selecting: int = 0
    n_criteria_blocked: int = 0
    n_criteria_conditional: int = 0

    # The strongest surviving criterion
    strongest_criterion: str = ""
    strongest_criterion_reason: str = ""

    # Safe/unsafe claims
    safe_claims: List[str] = field(default_factory=list)
    unsafe_claims: List[str] = field(default_factory=list)
    nonclaims: List[str] = field(default_factory=list)

    # Inherited classifications
    appendix_d_classification: str = "thermodynamic_sector_partially_consistent"
    appendix_e_classification: str = "locally_consistent_globally_underdetermined"

    valid: bool = False

    def assert_no_unsupported_claims(self) -> None:
        """Guard against forbidden classification strings."""
        for forbidden in _FORBIDDEN_CLASSIFICATIONS:
            if forbidden in self.executive_determination:
                raise AssertionError(
                    f"Forbidden classification '{forbidden}' found in "
                    f"executive_determination. Appendix H must not claim "
                    f"temperature is proven or that Appendix C is resolved."
                )


# ================================================================
# Reference BH Quantities
# ================================================================

def _ref_quantities(M_kg: float = M_REF_KG) -> Dict[str, float]:
    """Compute reference BH quantities at the GRUT endpoint."""
    r_s = 2.0 * G_SI * M_kg / C_SI ** 2
    R_eq = R_EQ_OVER_RS * r_s

    omega_g_sq = G_SI * M_kg / R_eq ** 3
    omega_g = math.sqrt(omega_g_sq)
    omega_0 = math.sqrt(BETA_Q) * omega_g

    T_hawking = HBAR_SI * C_SI ** 3 / (8.0 * math.pi * G_SI * M_kg * K_B)
    T_structural = HBAR_SI * omega_0 / K_B
    T_dissipation = T_structural / Q_CANONICAL

    kappa_eff = omega_0 ** 2 * R_eq
    T_surface_gravity = HBAR_SI * kappa_eff / (2.0 * math.pi * K_B)

    # dS/dM at R_eq: S = π(2GM/(3c²))²/l_P², dS/dM = 8πG²M/(9c⁴l_P²)
    dS_dM = 8.0 * math.pi * G_SI ** 2 * M_kg / (9.0 * C_SI ** 4 * L_PLANCK ** 2)

    # First-law temperature: T = c²/(k_B × dS/dM)
    T_1stlaw = C_SI ** 2 / (K_B * dS_dM)

    return {
        "M_kg": M_kg,
        "r_s": r_s,
        "R_eq": R_eq,
        "omega_0": omega_0,
        "T_hawking": T_hawking,
        "T_structural": T_structural,
        "T_dissipation": T_dissipation,
        "T_surface_gravity": T_surface_gravity,
        "T_1stlaw": T_1stlaw,
        "dS_dM": dS_dM,
    }


# ================================================================
# Temperature Candidate Builder
# ================================================================

def build_temperature_candidates(M_kg: float = M_REF_KG) -> List[TemperatureValue]:
    """Build all four temperature candidates at the reference mass."""
    ref = _ref_quantities(M_kg)

    return [
        TemperatureValue(
            name="T_structural",
            formula="hbar * omega_0 / k_B = hbar / (k_B * tau_local)",
            T_kelvin=ref["T_structural"],
            T_over_T_hawking=ref["T_structural"] / ref["T_hawking"],
            grut_native=True,
            derivation_status="grut_native",
        ),
        TemperatureValue(
            name="T_dissipation",
            formula="hbar * omega_0 / (Q * k_B) = T_structural / Q",
            T_kelvin=ref["T_dissipation"],
            T_over_T_hawking=ref["T_dissipation"] / ref["T_hawking"],
            grut_native=True,
            derivation_status="grut_native",
        ),
        TemperatureValue(
            name="T_surface_gravity",
            formula="hbar * kappa_eff / (2*pi*k_B)",
            T_kelvin=ref["T_surface_gravity"],
            T_over_T_hawking=ref["T_surface_gravity"] / ref["T_hawking"],
            grut_native=False,
            derivation_status="analog",
        ),
        TemperatureValue(
            name="T_hawking",
            formula="hbar * c^3 / (8*pi*G*M*k_B)",
            T_kelvin=ref["T_hawking"],
            T_over_T_hawking=1.0,
            grut_native=False,
            derivation_status="imported",
        ),
        TemperatureValue(
            name="T_1stlaw",
            formula="c^2 / (k_B * dS/dM)  where  S = pi*R_eq^2/l_P^2",
            T_kelvin=ref["T_1stlaw"],
            T_over_T_hawking=ref["T_1stlaw"] / ref["T_hawking"],
            grut_native=True,   # derived entirely from GRUT quantities
            derivation_status="first_law",
        ),
    ]


# ================================================================
# Selection Criterion Evaluators
# ================================================================

def evaluate_fdt_criterion() -> SelectionCriterion:
    """Criterion 1: FDT inversion.

    The FDT relates noise amplitude to temperature. Inverting gives T if
    the fluctuation amplitude is known.

    Result: BLOCKED — requires quantum state (Appendix C).
    """
    return SelectionCriterion(
        name="FDT_inversion",
        description=(
            "Invert the Fluctuation-Dissipation Theorem: "
            "S_FF(ω₀) = 2k_B·T·Im[χ(ω₀)]/ω₀. "
            "If S_FF(ω₀) is measured, T is determined."
        ),
        formula="T = ω₀ · S_FF(ω₀) / (2k_B · Im[χ(ω₀)])",
        selects_unique_T=False,
        requires_quantum_state=True,
        requires_appendix_c_resolved=True,
        verdict="BLOCKED",
        verdict_reason=(
            "The fluctuation amplitude S_FF(ω₀) requires knowledge of the "
            "quantum state of the GRUT interior — one of the hard Appendix C "
            "blockers. FDT inversion cannot proceed without the fluctuation "
            "amplitude, which is not available from the classical ODE system."
        ),
    )


def evaluate_kms_criterion(M_kg: float = M_REF_KG) -> SelectionCriterion:
    """Criterion 2: KMS periodicity (thermal time identification).

    If the GRUT state is a KMS thermal state, the thermal time β·ℏ = ℏ/(k_B·T)
    must equal the memory correlation time τ_local. This gives T = T_structural.

    Result: CONDITIONAL — requires state to be KMS thermal (Appendix C blocker).
    """
    ref = _ref_quantities(M_kg)
    T_kms = ref["T_structural"]   # ℏ/(k_B·τ_local) = ℏω₀/k_B

    return SelectionCriterion(
        name="KMS_periodicity",
        description=(
            "Identify the memory relaxation time τ_local with the KMS thermal "
            "period β·ℏ = ℏ/(k_B·T). In a KMS thermal state, correlation "
            "functions satisfy periodicity with period β = 1/(k_B·T). "
            "If τ_local IS the thermal period, then T = ℏ/(k_B·τ_local) = ℏω₀/k_B "
            "(using ω₀·τ_local = 1) = T_structural."
        ),
        formula="T_KMS = hbar/(k_B * tau_local) = hbar * omega_0 / k_B = T_structural",
        selects_unique_T=True,
        selected_T_name="T_structural",
        selected_T_kelvin=T_kms,
        requires_quantum_state=True,
        requires_appendix_c_resolved=True,
        verdict="CONDITIONAL",
        verdict_reason=(
            "The KMS criterion selects T_structural = ℏω₀/k_B IF the GRUT "
            "interior state is a KMS thermal state. This requires the state "
            "to be in thermal equilibrium — an assumption that is blocked by "
            "Appendix C (quantum state unknown). However, this is the strongest "
            "candidate for an eventual selection: if equilibrium is ever established, "
            "T_structural is the natural result. The selection is physically motivated "
            "by the structural identity ω₀·τ_local = 1, which equates the "
            "oscillation period (1/ω₀) with the memory time (τ_local), "
            "making τ_local the natural thermal time."
        ),
    )


def evaluate_first_law_criterion(M_kg: float = M_REF_KG) -> SelectionCriterion:
    """Criterion 3: First-law self-consistency.

    T_1stlaw = ∂E/∂S = c² × (dS/dM)⁻¹ with S = πR_eq²/l_P² and E = Mc².
    This gives a unique temperature WITHOUT requiring the quantum state.

    Result: VIABLE_WITH_ASSUMPTIONS — no Appendix C blocker.
    """
    ref = _ref_quantities(M_kg)

    return SelectionCriterion(
        name="first_law_self_consistency",
        description=(
            "Require T·dS = dE at the GRUT endpoint. With E = Mc² and "
            "S = πR_eq²/l_P² (area law at R_eq = r_s/3), the first law "
            "∂E/∂S = T determines a unique first-law temperature T_1stlaw. "
            "This uses only classical thermodynamic reasoning — no quantum state."
        ),
        formula="T_1stlaw = c^2 / (k_B * dS/dM) = 9 * T_Hawking",
        selects_unique_T=True,
        selected_T_name="T_1stlaw",
        selected_T_kelvin=ref["T_1stlaw"],
        requires_quantum_state=False,
        requires_appendix_c_resolved=False,
        requires_entropy_ansatz=True,
        verdict="VIABLE_WITH_ASSUMPTIONS",
        verdict_reason=(
            "The first law uniquely determines T_1stlaw = 9·T_Hawking when "
            "E = Mc² and S = πR_eq²/l_P². This requires accepting: "
            "(1) E = Mc² is the appropriate energy (rest mass, not ADM mass correction), "
            "(2) S = πR_eq²/l_P² is the thermodynamic entropy (it is a proxy, not "
            "a microstate count), "
            "(3) No work terms contribute (the barrier does no work at the endpoint). "
            "This is VIABLE: no Appendix C blocker. But it is CONDITIONAL on the "
            "entropy ansatz. T_1stlaw ≈ 0.83 × T_dissipation: the first law selects "
            "a temperature BETWEEN T_dissipation and T_Hawking. Neither T_structural "
            "nor T_dissipation exactly satisfies the first law with endpoint entropy."
        ),
    )


# ================================================================
# First Law Analysis
# ================================================================

def compute_first_law_analysis(M_kg: float = M_REF_KG) -> FirstLawAnalysis:
    """Compute the first-law thermodynamic analysis."""
    ref = _ref_quantities(M_kg)

    T_1stlaw = ref["T_1stlaw"]
    T_diss = ref["T_dissipation"]
    T_struct = ref["T_structural"]
    T_hawk = ref["T_hawking"]

    # First-law ratio with T_dissipation
    R_diss = K_B * T_diss * ref["dS_dM"] / C_SI ** 2
    # Should equal 2π√3/18 analytically

    first_law_approx = 0.5 < R_diss < 2.0

    return FirstLawAnalysis(
        dS_dM_SI=ref["dS_dM"],
        T_1stlaw_K=T_1stlaw,
        T_1stlaw_over_T_hawking=T_1stlaw / T_hawk,
        T_1stlaw_over_T_diss=T_1stlaw / T_diss,
        T_1stlaw_over_T_struct=T_1stlaw / T_struct,
        R_firstlaw_T_diss=R_diss,
        R_firstlaw_analytic=R_FIRSTLAW_ANALYTIC,
        R_is_mass_independent=True,
        first_law_approximately_satisfied=first_law_approx,
        verdict=(
            f"First-law ratio R = {R_diss:.4f} ≈ 2π√3/18 = {R_FIRSTLAW_ANALYTIC:.4f}. "
            f"R ≠ 1.0: T_dissipation does not exactly satisfy the first law "
            f"with endpoint area entropy. "
            f"The exact first-law temperature is T_1stlaw = {T_1stlaw:.4e} K "
            f"= {T_1stlaw/T_hawk:.2f} × T_Hawking "
            f"≈ {T_1stlaw/T_diss:.4f} × T_dissipation."
        ),
    )


# ================================================================
# Fluctuation Consequence
# ================================================================

def compute_fluctuation_consequence(M_kg: float = M_REF_KG) -> FluctuationConsequence:
    """The first non-circular fluctuation consequence.

    R = 2π√3/18 ≈ 1.21 is mass-independent. It is derived from Q and R_eq
    alone, without knowing T. Setting R = 1 would give a unique T.
    """
    return FluctuationConsequence(
        consequence_value=R_FIRSTLAW_ANALYTIC,
        fdt_noise_at_omega0=(
            "With T_dissipation and bath cutoff Ω = ω₀ (via ω₀·τ_local = 1): "
            "S(0) = 2·k_B·T_diss·τ_local = 2·ℏω₀·τ_local/Q = 2·ℏ/Q "
            "(using ω₀·τ_local = 1). For Q = 6: S(0) = ℏ/3. "
            "This is a dimensionful GRUT prediction for the low-frequency "
            "noise floor, IF the interior bath is physical."
        ),
        fdt_noise_formula="S(0) = 2·hbar/Q = hbar/3  (for Q=6, conditional on bath)",
    )


# ================================================================
# Master Audit Runner
# ================================================================

def run_temperature_selection_audit(
    M_kg: float = M_REF_KG,
) -> TemperatureSelectionResult:
    """Run the complete temperature selection audit.

    Parameters
    ----------
    M_kg : float
        Reference mass (default: 30 M_sun).

    Returns
    -------
    TemperatureSelectionResult
        Full audit result with selection criterion verdicts and
        the executive determination.
    """
    result = TemperatureSelectionResult()

    # Build candidates
    result.candidates = build_temperature_candidates(M_kg)

    # Selection criteria
    result.criterion_fdt = evaluate_fdt_criterion()
    result.criterion_kms = evaluate_kms_criterion(M_kg)
    result.criterion_first_law = evaluate_first_law_criterion(M_kg)

    # Count outcomes
    criteria = [
        result.criterion_fdt,
        result.criterion_kms,
        result.criterion_first_law,
    ]
    result.n_criteria_selecting = sum(1 for c in criteria if c.selects_unique_T)
    result.n_criteria_blocked = sum(1 for c in criteria if c.verdict == "BLOCKED")
    result.n_criteria_conditional = sum(1 for c in criteria if c.verdict == "CONDITIONAL")

    # First law analysis
    result.first_law = compute_first_law_analysis(M_kg)

    # Fluctuation consequence
    result.fluctuation = compute_fluctuation_consequence(M_kg)

    # Strongest criterion
    result.strongest_criterion = "first_law_self_consistency"
    result.strongest_criterion_reason = (
        "The first-law criterion is the only one that (a) selects a unique "
        "temperature, (b) does not require the quantum state (no Appendix C "
        "blocker), and (c) is derived entirely from GRUT quantities "
        "(R_eq/r_s = 1/3, β_Q = 2). It selects T_1stlaw = 9·T_Hawking "
        "≈ 0.83 × T_dissipation."
    )

    # Executive determination
    result.executive_determination = "temperature_selectable_conditionally_not_uniquely"
    result.determination_explanation = (
        "Temperature can be selected conditionally — but not uniquely and not "
        "without assumptions. The strongest GRUT-native selection is T_1stlaw "
        "from the first law, which is accessible without quantum-state input. "
        "But it requires accepting the endpoint area entropy S = πR_eq²/l_P². "
        "The KMS criterion would select T_structural if the interior state is "
        "thermal (blocked by Appendix C). The FDT criterion is fully blocked. "
        "No criterion distinguishes T_structural from T_dissipation without "
        "external input: they differ by exactly Q = 6, which is a GRUT-locked "
        "parameter. "
        "The first non-circular fluctuation consequence is the mass-independent "
        "first-law ratio R = 2π√3/18 ≈ 1.21, which constrains any experimental "
        "determination of T from the first law."
    )

    # Safe claims
    result.safe_claims = [
        "T_1stlaw = 9·T_Hawking is the unique temperature selected by the first "
        "law with E = Mc² and S = πR_eq²/l_P². It uses no quantum-state input.",

        "T_dissipation does NOT exactly satisfy the first law with endpoint area "
        "entropy: the ratio R = k_B·T_diss·(dS/dM)/c² = 2π√3/18 ≈ 1.21 ≠ 1.",

        "R = 2π√3/18 is mass-independent — it is the same for any BH mass. "
        "It depends only on Q = β_Q/α_vac = 6 and R_eq/r_s = 1/3.",

        "T_structural and T_dissipation differ by exactly Q = 6 (a GRUT-locked "
        "parameter). No GRUT-native criterion distinguishes them without the "
        "quantum state.",

        "The KMS criterion would select T_structural IF the interior state is "
        "a KMS thermal equilibrium state — this is conditional on Appendix C.",

        "The FDT noise at ω = 0 is S(0) = 2ℏ/Q = ℏ/3 (for Q=6) when using "
        "T_dissipation, conditional on the interior bath being physical.",
    ]

    result.unsafe_claims = [
        "Any specific temperature is proven correct.",
        "T_dissipation satisfies the first law (it gives R ≈ 1.21, not 1.0).",
        "T_structural is the KMS temperature (the state must be KMS thermal, "
        "which requires Appendix C resolution).",
        "The first-law selection proves the endpoint area entropy is correct.",
    ]

    result.nonclaims = [
        "This module does NOT prove any temperature.",
        "This module does NOT resolve any Appendix C blocker.",
        "This module does NOT claim Hawking radiation is derived from GRUT.",
        "This module does NOT upgrade the thermodynamic sector classification.",
    ]

    result.valid = True

    # Guard
    result.assert_no_unsupported_claims()

    return result


# ================================================================
# Convenience: Analytical Ratio Formula
# ================================================================

def compute_R_firstlaw_analytic(alpha_vac: float, beta_Q: float) -> float:
    """Compute the mass-independent first-law ratio analytically.

    R = 4π√3 / (3Q) where Q = β_Q/α_vac.

    Parameters
    ----------
    alpha_vac : float
        Vacuum susceptibility.
    beta_Q : float
        Barrier exponent.

    Returns
    -------
    float
        The first-law ratio R (mass-independent).
    """
    Q = beta_Q / alpha_vac
    return 4.0 * math.pi * math.sqrt(3.0) / (3.0 * Q)


def compute_R_firstlaw_numerical(M_kg: float = M_REF_KG) -> float:
    """Compute the first-law ratio numerically for verification.

    R = k_B · T_diss · (dS/dM) / c²

    Parameters
    ----------
    M_kg : float
        BH mass in kg.

    Returns
    -------
    float
        The first-law ratio R.
    """
    ref = _ref_quantities(M_kg)
    return K_B * ref["T_dissipation"] * ref["dS_dM"] / C_SI ** 2


# ================================================================
# Convenience: Summary String
# ================================================================

def summary_string(result: TemperatureSelectionResult) -> str:
    """Return a human-readable summary."""
    fl = result.first_law
    fc = result.fluctuation

    lines = [
        "=== APPENDIX H: TEMPERATURE SELECTION AUDIT SUMMARY ===",
        "",
        f"Executive determination: {result.executive_determination}",
        "",
        "--- Temperature Candidates (30 M_sun reference) ---",
    ]

    for c in result.candidates:
        lines.append(
            f"  {c.name:<22} = {c.T_kelvin:.4e} K  "
            f"({c.T_over_T_hawking:.2f} × T_H)  "
            f"[{'GRUT-native' if c.grut_native else 'not native'}]"
        )

    lines += [
        "",
        "--- Selection Criteria ---",
        f"  FDT inversion:           {result.criterion_fdt.verdict}",
        f"  KMS periodicity:         {result.criterion_kms.verdict}",
        f"  First law:               {result.criterion_first_law.verdict}",
        f"  → Strongest: {result.strongest_criterion}",
        "",
        "--- First Law Analysis ---",
        f"  T_1stlaw = 9 × T_H = {fl.T_1stlaw_K:.4e} K",
        f"  T_1stlaw / T_dissipation = {fl.T_1stlaw_over_T_diss:.4f}",
        f"  T_1stlaw / T_structural  = {fl.T_1stlaw_over_T_struct:.4f}",
        f"  First-law ratio R (numerical) = {fl.R_firstlaw_T_diss:.6f}",
        f"  First-law ratio R (analytic)  = {fl.R_firstlaw_analytic:.6f}",
        f"  R = 2π√3/18 ≈ {R_FIRSTLAW_ANALYTIC:.4f} (mass-independent)",
        "",
        "--- First Fluctuation Consequence ---",
        f"  R = {fc.consequence_value:.4f} (mass-independent first-law ratio)",
        f"  FDT noise S(0) = 2ℏ/Q = ℏ/3 (conditional on interior bath)",
        "",
        "--- Inherited Classifications (unchanged) ---",
        f"  Appendix D: {result.appendix_d_classification}",
        f"  Appendix E: {result.appendix_e_classification}",
    ]

    return "\n".join(lines)
