"""GRUT Appendix D — Thermodynamic Properties of the GRUT Interior.

LOCKED INHERITANCE
------------------
- Phase III: Collapse endpoint R_eq/r_s = 1/3, epsilon_Q = 1/9, beta_Q = 2 (LOCKED)
- Phase III-C: Interior PDE, structural identity omega_0*tau = 1 (LOCKED)
- Phase III-C: Quality factor Q ~ 6, mixed viscoelastic (CANDIDATE)
- Phase VII: w_Phi = -1 at equilibrium, NEC-saturating (CONDITIONAL)
- information.py: BH area proxy S_BH = pi R^2 / l_P^2 (PROXY)
- Q1: CTP/Galley recovery shell — exact at tree level (ESTABLISHED)
- Q2: Drude bath identification — structural match (ESTABLISHED)
- Q3: Algebraic grounding in interior PDE (ESTABLISHED)
- Q4: Temperature identified as key missing ingredient (ESTABLISHED)
- Appendix C: All quantum blockers remain in force (LOCKED BOUNDARY)

SCOPE
-----
Determine whether the GRUT interior has well-defined thermodynamic properties
WITHOUT importing standard black hole thermodynamics as GRUT content.

CORE QUESTIONS
--------------
1. Can a self-consistent temperature be defined from GRUT interior quantities?
2. Does the GRUT endpoint have a well-defined entropy?
3. Does the first law dM = T dS + work hold?
4. Does entropy increase monotonically during collapse?
5. Is the Q2 Drude bath compatible with a fluctuation-dissipation relation?

RESULT
------
See run_thermodynamic_audit() for the final determination.

NONCLAIMS
---------
1. This module does NOT derive Hawking radiation.
2. This module does NOT solve the black hole information paradox.
3. This module does NOT claim or prove unitarity.
4. This module does NOT import standard BH thermodynamics as GRUT content.
5. Temperature candidates are IDENTIFIED and COMPARED, not proven.
6. Entropy is a PROXY (classical area law), not a derived quantum quantity.
7. The first law test uses candidate quantities — it is conditional, not proven.
8. All Appendix C blockers remain in force.

CLASSIFICATION OPTIONS
----------------------
Executive:
- thermodynamic_sector_internally_consistent
- thermodynamic_sector_partially_consistent
- thermodynamic_sector_underdetermined
- thermodynamic_sector_inconsistent
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import List, Dict, Any, Literal


# ================================================================
# Physical Constants (SI)
# ================================================================

G_SI = 6.674e-11            # m^3 kg^-1 s^-2
C_SI = 299_792_458.0        # m/s
HBAR_SI = 1.054571817e-34   # J·s
K_B = 1.380649e-23          # J/K  (Boltzmann)
L_PLANCK = math.sqrt(HBAR_SI * G_SI / C_SI**3)  # ~1.616e-35 m
M_PLANCK = math.sqrt(HBAR_SI * C_SI / G_SI)     # ~2.176e-8 kg
T_PLANCK = M_PLANCK * C_SI**2 / K_B             # ~1.416e32 K

# ================================================================
# GRUT Canon Constants
# ================================================================

ALPHA_VAC = 1.0 / 3.0
BETA_Q = 2.0
EPSILON_Q = ALPHA_VAC ** 2   # = 1/9
R_EQ_OVER_RS = EPSILON_Q ** (1.0 / BETA_Q)  # = 1/3

# Reference mass for numerical estimates
M_SUN_KG = 1.989e30
M_REF_KG = 30.0 * M_SUN_KG  # 30 solar mass reference BH

# Structural identity
OMEGA_0_TAU_IDENTITY = 1.0  # omega_0 * tau_eff = 1 at equilibrium


# ================================================================
# Classification Vocabularies
# ================================================================

EXECUTIVE_CLASSIFICATIONS = [
    "thermodynamic_sector_internally_consistent",
    "thermodynamic_sector_partially_consistent",
    "thermodynamic_sector_underdetermined",
    "thermodynamic_sector_inconsistent",
]

TEMPERATURE_CLASSIFICATIONS = [
    "temperature_derived_from_grut_architecture",
    "temperature_definable_but_not_uniquely_derived",
    "temperature_requires_external_input",
    "temperature_multiple_candidates_no_convergence",
    "no_consistent_temperature_exists",
]

ENTROPY_CLASSIFICATIONS = [
    "area_law_recovered",
    "area_law_modified_by_memory",
    "entropy_definable_but_not_unique",
    "no_entropy_definition",
]

FIRST_LAW_CLASSIFICATIONS = [
    "first_law_consistent",
    "first_law_partially_consistent",
    "first_law_violated",
    "first_law_underdetermined",
]

ENTROPY_PRODUCTION_CLASSIFICATIONS = [
    "monotonic_decrease_during_collapse",
    "non_monotonic",
    "monotonic_increase_during_collapse",
    "underdetermined",
]

FDT_CLASSIFICATIONS = [
    "fdt_compatible",
    "fdt_conditional_on_temperature",
    "fdt_incompatible",
    "fdt_underdetermined",
]

THERMO_FORBIDDEN_CLAIMS = [
    "derives_hawking_radiation",
    "solves_information_paradox",
    "proves_unitarity",
    "derives_born_rule",
    "computes_quantum_corrections",
    "resolves_appendix_c",
    "imports_standard_bh_thermo_as_grut",
    "temperature_is_proven",
    "entropy_is_exact",
    "first_law_is_proven",
]


# ================================================================
# Data Structures
# ================================================================

@dataclass
class CandidateTemperature:
    """One candidate temperature definition for the GRUT interior.

    Each candidate is a mapping from published GRUT interior quantities
    to a temperature-like quantity. These are IDENTIFIED and COMPARED,
    not proven.
    """
    name: str
    label: str
    formula: str
    formula_description: str

    # Numerical evaluation at reference mass (30 M_sun)
    T_kelvin_at_ref: float = 0.0
    T_over_T_hawking_at_ref: float = 0.0

    # Derivation status
    derivation_status: str = ""
    # One of: "derived_from_grut", "analog_of_standard", "dimensional",
    #         "imported", "underdetermined"

    # Assumptions
    assumptions: List[str] = field(default_factory=list)

    # Is this genuinely GRUT-native or imported from standard BH thermo?
    grut_native: bool = False

    # Does it use only published quantities?
    uses_only_published_quantities: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "label": self.label,
            "formula": self.formula,
            "T_kelvin_at_ref": self.T_kelvin_at_ref,
            "T_over_T_hawking_at_ref": self.T_over_T_hawking_at_ref,
            "derivation_status": self.derivation_status,
            "grut_native": self.grut_native,
            "uses_only_published_quantities": self.uses_only_published_quantities,
            "assumptions": self.assumptions,
        }


@dataclass
class TemperatureConvergenceTest:
    """Test whether candidate temperatures converge to a single value."""
    candidates_tested: int = 0
    max_ratio: float = 0.0   # max(T_i / T_j) across all pairs
    min_ratio: float = 0.0
    converged: bool = False   # max_ratio < 10 (within one order of magnitude)
    convergence_factor: float = 0.0  # max_ratio
    assessment: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "candidates_tested": self.candidates_tested,
            "max_ratio": self.max_ratio,
            "min_ratio": self.min_ratio,
            "converged": self.converged,
            "convergence_factor": self.convergence_factor,
            "assessment": self.assessment,
        }


@dataclass
class TemperatureAudit:
    """Complete audit of candidate temperatures."""
    candidates: List[CandidateTemperature] = field(default_factory=list)
    convergence: TemperatureConvergenceTest = field(
        default_factory=TemperatureConvergenceTest
    )
    classification: str = ""
    # From TEMPERATURE_CLASSIFICATIONS

    n_grut_native: int = 0
    n_imported: int = 0
    best_candidate: str = ""
    best_candidate_reason: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "candidates": [c.to_dict() for c in self.candidates],
            "convergence": self.convergence.to_dict(),
            "classification": self.classification,
            "n_grut_native": self.n_grut_native,
            "n_imported": self.n_imported,
            "best_candidate": self.best_candidate,
            "best_candidate_reason": self.best_candidate_reason,
        }


@dataclass
class EntropyAnalysis:
    """Analysis of entropy for the GRUT endpoint."""
    # Area-law proxy
    area_law_formula: str = "S_BH = pi * R_eq^2 / l_P^2"
    S_BH_at_ref: float = 0.0  # in Planck units, at 30 M_sun

    # Memory sector correction
    memory_correction_formula: str = ""
    memory_correction_description: str = ""
    memory_correction_sign: str = ""   # "positive", "negative", "zero", "underdetermined"
    memory_correction_magnitude: str = ""  # "negligible", "small", "comparable", "dominant"

    # Classification
    classification: str = ""
    # From ENTROPY_CLASSIFICATIONS

    # Nonclaims
    nonclaims: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "area_law_formula": self.area_law_formula,
            "S_BH_at_ref": self.S_BH_at_ref,
            "memory_correction_sign": self.memory_correction_sign,
            "memory_correction_magnitude": self.memory_correction_magnitude,
            "classification": self.classification,
            "nonclaims": self.nonclaims,
        }


@dataclass
class FirstLawTest:
    """Test of the first law: dM = T dS + work terms."""
    # Which candidate T and S are used
    temperature_candidate: str = ""
    entropy_candidate: str = ""

    # First law components
    dM_formula: str = ""
    TdS_formula: str = ""
    work_formula: str = ""

    # Consistency check
    first_law_satisfied: bool = False
    residual_description: str = ""

    # Classification
    classification: str = ""
    # From FIRST_LAW_CLASSIFICATIONS

    # Why conditional
    conditionality: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "temperature_candidate": self.temperature_candidate,
            "entropy_candidate": self.entropy_candidate,
            "first_law_satisfied": self.first_law_satisfied,
            "residual_description": self.residual_description,
            "classification": self.classification,
            "conditionality": self.conditionality,
        }


@dataclass
class EntropyProductionTest:
    """Test of entropy monotonicity during collapse."""
    # Area-based entropy
    S_initial_description: str = ""
    S_final_description: str = ""
    S_ratio: float = 0.0  # S_final / S_initial

    # During collapse: R decreases → area decreases → S_BH decreases
    area_decreases_during_collapse: bool = True
    memory_dissipation_produces_entropy: bool = True

    # Net assessment
    net_entropy_change: str = ""  # "decreases", "increases", "underdetermined"
    classification: str = ""
    # From ENTROPY_PRODUCTION_CLASSIFICATIONS

    interpretation: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "S_ratio": self.S_ratio,
            "area_decreases_during_collapse": self.area_decreases_during_collapse,
            "memory_dissipation_produces_entropy": self.memory_dissipation_produces_entropy,
            "net_entropy_change": self.net_entropy_change,
            "classification": self.classification,
            "interpretation": self.interpretation,
        }


@dataclass
class FDTCompatibilityTest:
    """Test of fluctuation-dissipation compatibility."""
    # Dissipation kernel (from Q2)
    dissipation_kernel: str = "K(s) = (1/tau) * exp(-s/tau)"
    drude_spectral_density: str = "J(omega) = eta * omega * Omega^2 / (omega^2 + Omega^2)"

    # If FDT holds, the noise kernel is:
    fdt_noise_formula: str = ""
    fdt_noise_description: str = ""

    # Does the noise require temperature?
    requires_temperature: bool = True

    # Is noise form determined up to temperature?
    noise_form_determined_up_to_T: bool = False

    # Would any GRUT observable be affected?
    observable_consequence: str = ""

    # Classification
    classification: str = ""
    # From FDT_CLASSIFICATIONS

    def to_dict(self) -> Dict[str, Any]:
        return {
            "dissipation_kernel": self.dissipation_kernel,
            "drude_spectral_density": self.drude_spectral_density,
            "fdt_noise_formula": self.fdt_noise_formula,
            "requires_temperature": self.requires_temperature,
            "noise_form_determined_up_to_T": self.noise_form_determined_up_to_T,
            "observable_consequence": self.observable_consequence,
            "classification": self.classification,
        }


@dataclass
class ThermodynamicTranslationMap:
    """Maps GRUT interior quantities to thermodynamic quantities."""
    entries: List[Dict[str, str]] = field(default_factory=list)
    # Each entry: {"grut_quantity": ..., "thermo_quantity": ...,
    #              "relationship": ..., "status": ...}

    def to_dict(self) -> Dict[str, Any]:
        return {"entries": self.entries}


@dataclass
class ThermoResult:
    """Master result from Appendix D — Thermodynamic Sector Audit."""
    executive_determination: str = ""
    # From EXECUTIVE_CLASSIFICATIONS

    # Sub-audits
    temperature_audit: TemperatureAudit = field(
        default_factory=TemperatureAudit
    )
    entropy_analysis: EntropyAnalysis = field(
        default_factory=EntropyAnalysis
    )
    first_law_test: FirstLawTest = field(
        default_factory=FirstLawTest
    )
    entropy_production: EntropyProductionTest = field(
        default_factory=EntropyProductionTest
    )
    fdt_compatibility: FDTCompatibilityTest = field(
        default_factory=FDTCompatibilityTest
    )
    translation_map: ThermodynamicTranslationMap = field(
        default_factory=ThermodynamicTranslationMap
    )

    # Per-test classifications (convenience)
    temperature_classification: str = ""
    entropy_classification: str = ""
    first_law_classification: str = ""
    entropy_production_classification: str = ""
    fdt_classification: str = ""

    # Hard blockers
    hard_blockers_after_thermo: List[Dict[str, Any]] = field(
        default_factory=list
    )

    # Safe/unsafe claims
    safe_claims: List[str] = field(default_factory=list)
    unsafe_claims: List[str] = field(default_factory=list)
    nonclaims: List[str] = field(default_factory=list)

    valid: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return {
            "executive_determination": self.executive_determination,
            "temperature_audit": self.temperature_audit.to_dict(),
            "entropy_analysis": self.entropy_analysis.to_dict(),
            "first_law_test": self.first_law_test.to_dict(),
            "entropy_production": self.entropy_production.to_dict(),
            "fdt_compatibility": self.fdt_compatibility.to_dict(),
            "translation_map": self.translation_map.to_dict(),
            "temperature_classification": self.temperature_classification,
            "entropy_classification": self.entropy_classification,
            "first_law_classification": self.first_law_classification,
            "entropy_production_classification": self.entropy_production_classification,
            "fdt_classification": self.fdt_classification,
            "hard_blockers_after_thermo": self.hard_blockers_after_thermo,
            "safe_claims": self.safe_claims,
            "unsafe_claims": self.unsafe_claims,
            "nonclaims": self.nonclaims,
            "valid": self.valid,
        }


# ================================================================
# Helper: Reference BH Quantities
# ================================================================

def _ref_bh_quantities(M_kg: float = M_REF_KG) -> Dict[str, float]:
    """Compute reference BH quantities at the GRUT endpoint."""
    r_s = 2.0 * G_SI * M_kg / C_SI**2
    R_eq = R_EQ_OVER_RS * r_s  # = r_s / 3

    # Gravitational frequency scale
    omega_g_sq = G_SI * M_kg / R_eq**3
    omega_g = math.sqrt(omega_g_sq)

    # Barrier restoring frequency
    omega_0 = math.sqrt(BETA_Q) * omega_g

    # Memory timescale from structural identity
    # omega_0 * tau_eff = 1 → tau_eff = 1/omega_0
    tau_eff = 1.0 / omega_0

    # Surface gravity at R_eq (Schwarzschild-like proxy)
    # kappa = GM / R_eq^2 * (1 - 2GM/(R_eq c^2))^(1/2)
    # At R_eq = r_s/3: compactness C = r_s/R_eq = 3, so 1-C = -2
    # The standard formula breaks down: R_eq < r_s (post-horizon endpoint)
    # Use the effective surface gravity at the barrier instead
    # kappa_eff = barrier restoring acceleration = omega_0^2 * R_eq
    kappa_eff = omega_0**2 * R_eq

    # Hawking temperature (standard, for comparison only)
    T_hawking = HBAR_SI * C_SI**3 / (8.0 * math.pi * G_SI * M_kg * K_B)

    # Quality factor (PDE-derived, canonical value ~6)
    Q_canonical = 6.0

    # Area at endpoint
    A_eq = 4.0 * math.pi * R_eq**2

    # BH entropy proxy
    S_BH = math.pi * R_eq**2 / L_PLANCK**2

    return {
        "M_kg": M_kg,
        "r_s": r_s,
        "R_eq": R_eq,
        "omega_g": omega_g,
        "omega_0": omega_0,
        "tau_eff": tau_eff,
        "kappa_eff": kappa_eff,
        "T_hawking": T_hawking,
        "Q_canonical": Q_canonical,
        "A_eq": A_eq,
        "S_BH": S_BH,
    }


# ================================================================
# Temperature Candidate Builders
# ================================================================

def build_candidate_temperatures() -> List[CandidateTemperature]:
    """Build at least 4 candidate temperature definitions.

    Each maps published GRUT interior quantities to a temperature.
    """
    ref = _ref_bh_quantities()

    candidates = []

    # ── T1: Surface-gravity analog ────────────────────────────────
    # Standard BH thermo: T_H = hbar * kappa / (2pi k_B)
    # GRUT analog: use the effective barrier restoring acceleration
    # kappa_eff = omega_0^2 * R_eq as the "surface gravity"
    # T_sg = hbar * kappa_eff / (2pi k_B)
    T_sg = HBAR_SI * ref["kappa_eff"] / (2.0 * math.pi * K_B)

    candidates.append(CandidateTemperature(
        name="T_surface_gravity",
        label="Surface-Gravity Analog",
        formula="T = hbar * kappa_eff / (2*pi*k_B)",
        formula_description=(
            "Analog of Hawking temperature using the effective barrier "
            "restoring acceleration kappa_eff = omega_0^2 * R_eq as the "
            "surface gravity. This is the standard Unruh/Hawking form "
            "applied to the GRUT barrier, NOT the Schwarzschild surface gravity."
        ),
        T_kelvin_at_ref=T_sg,
        T_over_T_hawking_at_ref=T_sg / ref["T_hawking"] if ref["T_hawking"] > 0 else 0.0,
        derivation_status="analog_of_standard",
        assumptions=[
            "kappa_eff = omega_0^2 * R_eq is a valid proxy for surface gravity",
            "The Unruh/Hawking form T = hbar*kappa/(2pi*k_B) applies to the barrier",
            "R_eq is inside the Schwarzschild radius — standard surface gravity undefined",
        ],
        grut_native=False,
        uses_only_published_quantities=True,
    ))

    # ── T2: Dissipation temperature ───────────────────────────────
    # From the quality factor: kT ~ hbar * omega_0 / Q
    # Interpretation: the energy per cycle dissipated into the bath
    # sets the thermal scale
    T_diss = HBAR_SI * ref["omega_0"] / (ref["Q_canonical"] * K_B)

    candidates.append(CandidateTemperature(
        name="T_dissipation",
        label="Dissipation-Rate Temperature",
        formula="T = hbar * omega_0 / (Q * k_B)",
        formula_description=(
            "Maps the dissipation rate to a temperature via kT = hbar*omega_0/Q. "
            "The quality factor Q encodes how much energy is lost per oscillation "
            "cycle. This is the natural thermal energy scale of a damped oscillator "
            "with frequency omega_0 and quality factor Q."
        ),
        T_kelvin_at_ref=T_diss,
        T_over_T_hawking_at_ref=T_diss / ref["T_hawking"] if ref["T_hawking"] > 0 else 0.0,
        derivation_status="derived_from_grut",
        assumptions=[
            "Q ~ 6 from PDE analysis (canonical, candidate-level)",
            "omega_0 from structural identity omega_0*tau = 1",
            "kT = hbar*omega_0/Q is the standard oscillator thermal energy",
        ],
        grut_native=True,
        uses_only_published_quantities=True,
    ))

    # ── T3: Structural-identity temperature ───────────────────────
    # From omega_0 * tau = 1 and T = hbar * omega_0 / k_B
    # This is the "bare" frequency temperature — no Q correction
    T_struct = HBAR_SI * ref["omega_0"] / K_B

    candidates.append(CandidateTemperature(
        name="T_structural",
        label="Structural-Identity Temperature",
        formula="T = hbar * omega_0 / k_B",
        formula_description=(
            "Uses the structural identity omega_0*tau = 1. Since omega_0 "
            "is the fundamental frequency of the BDCC interior, the "
            "associated energy hbar*omega_0 defines a temperature scale. "
            "This is the 'bare' temperature — it equals T_dissipation * Q. "
            "Equivalently, T_struct = hbar / (tau_eff * k_B)."
        ),
        T_kelvin_at_ref=T_struct,
        T_over_T_hawking_at_ref=T_struct / ref["T_hawking"] if ref["T_hawking"] > 0 else 0.0,
        derivation_status="derived_from_grut",
        assumptions=[
            "omega_0*tau = 1 (structural identity, derived in interior PDE)",
            "hbar*omega_0 is the natural energy scale",
        ],
        grut_native=True,
        uses_only_published_quantities=True,
    ))

    # ── T4: Hawking temperature (imported, for comparison) ────────
    candidates.append(CandidateTemperature(
        name="T_hawking",
        label="Standard Hawking Temperature (Imported)",
        formula="T = hbar * c^3 / (8*pi*G*M*k_B)",
        formula_description=(
            "Standard Hawking temperature for a Schwarzschild black hole. "
            "This is IMPORTED from standard BH thermodynamics, NOT derived "
            "from GRUT architecture. Included only as a comparison baseline."
        ),
        T_kelvin_at_ref=ref["T_hawking"],
        T_over_T_hawking_at_ref=1.0,
        derivation_status="imported",
        assumptions=[
            "Standard Schwarzschild exterior",
            "Semiclassical QFT in curved spacetime",
            "NOT derived from GRUT — imported for comparison only",
        ],
        grut_native=False,
        uses_only_published_quantities=False,
    ))

    return candidates


def audit_temperature_convergence(
    candidates: List[CandidateTemperature],
) -> TemperatureConvergenceTest:
    """Test whether GRUT-native candidate temperatures converge."""
    native = [c for c in candidates if c.grut_native and c.T_kelvin_at_ref > 0]
    if len(native) < 2:
        return TemperatureConvergenceTest(
            candidates_tested=len(native),
            assessment="Fewer than 2 GRUT-native candidates — convergence untestable",
        )

    temps = [c.T_kelvin_at_ref for c in native]
    max_T = max(temps)
    min_T = min(temps)
    ratio = max_T / min_T if min_T > 0 else float("inf")

    # Convergence criterion: within one order of magnitude
    converged = ratio < 10.0

    return TemperatureConvergenceTest(
        candidates_tested=len(native),
        max_ratio=ratio,
        min_ratio=1.0 / ratio if ratio > 0 else 0.0,
        converged=converged,
        convergence_factor=ratio,
        assessment=(
            f"{len(native)} GRUT-native candidates tested. "
            f"Max/min ratio = {ratio:.2f}. "
            f"{'Converged' if converged else 'NOT converged'} "
            f"(threshold: factor of 10). "
            f"T_dissipation and T_structural differ by factor Q ~ 6 — "
            f"this is the Q-factor ambiguity: whether temperature corresponds "
            f"to the energy per mode (T_structural) or energy dissipated per "
            f"cycle (T_dissipation). Both are valid but physically distinct."
        ),
    )


def build_temperature_audit() -> TemperatureAudit:
    """Complete temperature audit."""
    candidates = build_candidate_temperatures()
    convergence = audit_temperature_convergence(candidates)

    n_native = sum(1 for c in candidates if c.grut_native)
    n_imported = sum(1 for c in candidates if not c.grut_native)

    # Classification logic
    if n_native >= 2 and convergence.converged:
        classification = "temperature_definable_but_not_uniquely_derived"
    elif n_native >= 2 and not convergence.converged:
        classification = "temperature_multiple_candidates_no_convergence"
    elif n_native == 1:
        classification = "temperature_definable_but_not_uniquely_derived"
    else:
        classification = "temperature_requires_external_input"

    # The GRUT-native candidates (T_dissipation, T_structural) differ by
    # factor Q ~ 6. This is within one order of magnitude → converged.
    # But the ambiguity between "energy per mode" vs "energy per cycle"
    # means the temperature is definable but not uniquely derived.

    return TemperatureAudit(
        candidates=candidates,
        convergence=convergence,
        classification=classification,
        n_grut_native=n_native,
        n_imported=n_imported,
        best_candidate="T_dissipation",
        best_candidate_reason=(
            "T_dissipation = hbar*omega_0/(Q*k_B) is the most physically "
            "motivated: it uses both the GRUT frequency scale (omega_0) and "
            "the GRUT dissipation rate (Q), and maps to the standard thermal "
            "energy of a damped oscillator. It is GRUT-native and uses only "
            "published quantities."
        ),
    )


# ================================================================
# Entropy Analysis
# ================================================================

def analyze_entropy() -> EntropyAnalysis:
    """Analyze entropy at the GRUT endpoint."""
    ref = _ref_bh_quantities()

    return EntropyAnalysis(
        area_law_formula="S_BH = pi * R_eq^2 / l_P^2",
        S_BH_at_ref=ref["S_BH"],
        memory_correction_formula=(
            "delta_S_mem ~ S_BH * Phi_eq / Phi_max "
            "(placeholder scaling from information.py)"
        ),
        memory_correction_description=(
            "The memory sector stores information proportional to how much "
            "it has saturated (memory_tracking_ratio) and barrier engagement. "
            "At the endpoint, M_drive = a_grav (fully saturated), so the "
            "memory correction is proportional to S_BH times the barrier "
            "dominance. This is a PROXY from information.py, not a derived "
            "quantity. The sign is positive (memory adds information content) "
            "and the magnitude is O(1) times S_BH (since barrier dominance "
            "is O(1) at the endpoint)."
        ),
        memory_correction_sign="positive",
        memory_correction_magnitude="comparable",
        classification="area_law_modified_by_memory",
        nonclaims=[
            "S_BH = pi*R_eq^2/l_P^2 is a CLASSICAL area proxy — not a "
            "quantum entropy count",
            "The memory correction is a PROXY scaling from information.py",
            "The area law uses R_eq (interior endpoint), not the Schwarzschild "
            "radius — this is geometrically distinct from standard BH entropy",
            "No microstate counting is performed",
            "The R_eq^2 area law gives S proportional to M^2 (since R_eq = r_s/3 "
            "and r_s proportional to M), matching the standard Bekenstein-Hawking "
            "M^2 scaling but with a different geometric prefactor",
        ],
    )


# ================================================================
# First Law Test
# ================================================================

def test_first_law() -> FirstLawTest:
    """Test the first law: dE = T dS + work terms.

    Uses the best candidate temperature (T_dissipation) and
    area-law entropy (S_BH = pi R_eq^2 / l_P^2, dimensionless in Planck units).

    The first law in SI units:
      c^2 dM = k_B T dS + (barrier work terms)

    The dimensionless first-law ratio is:
      R = k_B * T * (dS/dM) / c^2

    R = 1 means the first law holds exactly (with no work terms).

    At the GRUT endpoint:
      S = pi R_eq^2 / l_P^2 = pi (r_s/3)^2 / l_P^2
        = (4 pi G^2 M^2) / (9 c^4 l_P^2)

      dS/dM = (8 pi G^2 M) / (9 c^4 l_P^2)

    For standard BH thermo: T_H * k_B * dS_standard/dM / c^2 = 1 exactly.
    Our S_endpoint = S_standard / 9 and T_diss ~ 10.9 * T_H,
    so R_GRUT ~ 10.9 / 9 ~ 1.2.
    """
    ref = _ref_bh_quantities()

    # dS/dM at the endpoint
    # S = pi (2GM/(3c^2))^2 / l_P^2
    # dS/dM = 8 pi G^2 M / (9 c^4 l_P^2)
    dS_dM = 8.0 * math.pi * G_SI**2 * ref["M_kg"] / (
        9.0 * C_SI**4 * L_PLANCK**2
    )

    # T_dissipation
    T_diss = HBAR_SI * ref["omega_0"] / (ref["Q_canonical"] * K_B)

    # Dimensionless first-law ratio: R = k_B * T * dS/dM / c^2
    # R = 1 means dE = T dS exactly
    ratio = K_B * T_diss * dS_dM / C_SI**2

    consistent = 0.1 < ratio < 10.0  # within one order of magnitude

    return FirstLawTest(
        temperature_candidate="T_dissipation",
        entropy_candidate="S_BH_endpoint (area law at R_eq)",
        dM_formula="c^2 * dM",
        TdS_formula="k_B * T_diss * (8*pi*G^2*M / (9*c^4*l_P^2)) * dM",
        work_formula=(
            "Work terms from barrier sector not separately computed — "
            "the barrier is part of the gravitational potential at R_eq"
        ),
        first_law_satisfied=consistent,
        residual_description=(
            f"k_B * T_diss * dS/dM / c^2 = {ratio:.4g}. "
            f"{'Within' if consistent else 'Outside'} one order of magnitude "
            f"of unity. The GRUT endpoint has R_eq = r_s/3, so the "
            f"endpoint area entropy is 1/9 of the standard BH entropy. "
            f"T_dissipation ~ 10.9 * T_Hawking and S_endpoint ~ S_BH/9, "
            f"giving a first-law ratio of ~10.9/9 ~ 1.2. The near-unity "
            f"value reflects the internal consistency of the GRUT "
            f"thermodynamic quantities, not a derivation of the first law."
        ),
        classification=(
            "first_law_partially_consistent" if consistent
            else "first_law_underdetermined"
        ),
        conditionality=(
            "Conditional on: (1) T_dissipation being the correct temperature, "
            "(2) area-law entropy being applicable at R_eq (inside the horizon), "
            "(3) no additional work terms from the barrier sector."
        ),
    )


# ================================================================
# Entropy Production Test
# ================================================================

def test_entropy_production() -> EntropyProductionTest:
    """Test entropy monotonicity during collapse.

    During collapse, R decreases. Since S_BH = pi R^2 / l_P^2,
    the area-law entropy DECREASES during collapse.

    However, the memory sector dissipates energy (tau dPhi/dt + Phi = X),
    which should produce entropy. The question is whether the memory
    dissipation entropy exceeds the area-law entropy decrease.

    Key insight: The GRUT endpoint is at R_eq = r_s/3, which is INSIDE
    the Schwarzschild radius. Standard thermodynamics says the total
    generalized entropy (S_BH + S_matter) should not decrease. But
    S_BH is defined at the horizon (r_s), not at R_eq. The area at r_s
    is FIXED for a given M — it does not change during collapse of
    the interior. So the relevant entropy is:
      - S_horizon = pi r_s^2 / l_P^2 (constant for fixed M)
      - S_interior = memory dissipation entropy (increases)
      - Total generalized entropy: S_horizon + S_interior (non-decreasing)
    """
    ref = _ref_bh_quantities()

    # Area-law entropy at initial radius (r_s) vs endpoint (R_eq)
    S_initial = math.pi * ref["r_s"]**2 / L_PLANCK**2
    S_final = math.pi * ref["R_eq"]**2 / L_PLANCK**2
    S_ratio = S_final / S_initial if S_initial > 0 else 0.0
    # S_ratio = (R_eq/r_s)^2 = (1/3)^2 = 1/9

    return EntropyProductionTest(
        S_initial_description=(
            "S_initial = pi * r_s^2 / l_P^2 (area at Schwarzschild radius)"
        ),
        S_final_description=(
            "S_final = pi * R_eq^2 / l_P^2 (area at GRUT endpoint R_eq = r_s/3)"
        ),
        S_ratio=S_ratio,
        area_decreases_during_collapse=True,
        memory_dissipation_produces_entropy=True,
        net_entropy_change="underdetermined",
        classification="underdetermined",
        interpretation=(
            "The shell area decreases during collapse (R: r_s -> R_eq = r_s/3), "
            "so S_shell = pi R^2/l_P^2 decreases by factor (1/3)^2 = 1/9. "
            "However, this tracks the SHELL area, not the HORIZON area. The "
            "horizon area A_H = 4*pi*r_s^2 is fixed for constant M. The "
            "memory sector dissipates energy (first-order relaxation), which "
            "should produce entropy. The generalized second law (S_horizon + "
            "S_matter >= constant) is not testable without: (a) a proper "
            "definition of S_matter for the memory sector, (b) the covariant "
            "interior metric (Phase V obstruction), and (c) a quantum entropy "
            "formula. Classification: UNDERDETERMINED — not because the data "
            "contradicts monotonicity, but because the relevant entropy "
            "measure is not uniquely defined."
        ),
    )


# ================================================================
# FDT Compatibility Test
# ================================================================

def test_fdt_compatibility() -> FDTCompatibilityTest:
    """Test fluctuation-dissipation compatibility.

    If the Q2 Drude bath is physical, FDT determines the noise kernel:
      S(omega) = 2 * k_B * T * Im[chi(omega)] / omega  (classical)
      S(omega) = 2 * hbar * Im[chi(omega)] * coth(hbar*omega/(2k_BT))  (quantum)

    With the Drude susceptibility chi(omega) = 1/(1 + i*omega*tau):
      Im[chi] = omega * tau / (1 + omega^2 * tau^2)

    So the classical noise power spectral density is:
      S(omega) = 2 * k_B * T * tau / (1 + omega^2 * tau^2)
               = (2 k_B T / Omega) * Omega * tau / (1 + omega^2 * tau^2)

    This is a Lorentzian noise spectrum with the SAME pole as the
    dissipation kernel. Its amplitude is determined by T.
    """
    ref = _ref_bh_quantities()
    T_diss = HBAR_SI * ref["omega_0"] / (ref["Q_canonical"] * K_B)

    return FDTCompatibilityTest(
        dissipation_kernel="K(s) = (1/tau) * exp(-s/tau)",
        drude_spectral_density="J(omega) = eta * omega * Omega^2 / (omega^2 + Omega^2)",
        fdt_noise_formula=(
            "S(omega) = 2 * k_B * T * tau / (1 + omega^2 * tau^2) [classical FDT]"
        ),
        fdt_noise_description=(
            "IF the Q2 Drude bath is physical AND FDT applies with some "
            "temperature T, THEN the noise power spectral density is a "
            "Lorentzian with the same pole as the dissipation kernel, and "
            "amplitude 2*k_B*T*tau. Using T_dissipation = hbar*omega_0/(Q*k_B), "
            f"this gives S(0) = 2*k_B*T_diss*tau = 2*hbar*omega_0*tau/Q "
            f"= 2*hbar/(Q) (using omega_0*tau = 1). For Q ~ 6, "
            f"S(0) ~ hbar/3. This is a CONDITIONAL result: it requires "
            f"both the bath to be physical and FDT to apply."
        ),
        requires_temperature=True,
        noise_form_determined_up_to_T=True,
        observable_consequence=(
            "IF this noise exists, it would produce stochastic fluctuations "
            "in the memory field Phi around its equilibrium value. The "
            "variance would be <delta_Phi^2> ~ k_B*T/(m*omega_0^2) where "
            "m is the effective mass of the memory mode. This could in "
            "principle affect: (1) the sharpness of the collapse endpoint, "
            "(2) mass-function scatter in BDCC populations, (3) echo signal "
            "variability. None of these are currently computable."
        ),
        classification="fdt_conditional_on_temperature",
    )


# ================================================================
# Translation Map
# ================================================================

def build_translation_map() -> ThermodynamicTranslationMap:
    """Map GRUT interior quantities to thermodynamic quantities."""
    return ThermodynamicTranslationMap(
        entries=[
            {
                "grut_quantity": "omega_0 (barrier restoring frequency)",
                "thermo_quantity": "Fundamental energy scale hbar*omega_0",
                "relationship": "Direct: E_0 = hbar * omega_0",
                "status": "derived",
            },
            {
                "grut_quantity": "tau_eff (memory relaxation time)",
                "thermo_quantity": "Thermal relaxation time",
                "relationship": "Direct: tau_thermo = tau_eff = 1/omega_0",
                "status": "derived",
            },
            {
                "grut_quantity": "Q (quality factor)",
                "thermo_quantity": "Inverse dissipation fraction per cycle",
                "relationship": "Direct: energy_dissipated_per_cycle = E_stored / Q",
                "status": "candidate",
            },
            {
                "grut_quantity": "loss tangent tan(delta) = 1/(2Q)",
                "thermo_quantity": "Ratio of dissipated to stored energy",
                "relationship": "Standard viscoelastic: tan(delta) = G''/G'",
                "status": "candidate",
            },
            {
                "grut_quantity": "R_eq^2 (endpoint area)",
                "thermo_quantity": "Entropy proxy S = pi*R_eq^2/l_P^2",
                "relationship": "Bekenstein-Hawking analog at GRUT endpoint",
                "status": "proxy",
            },
            {
                "grut_quantity": "kappa_eff = omega_0^2 * R_eq",
                "thermo_quantity": "Effective surface gravity",
                "relationship": "Analog: T = hbar*kappa_eff/(2*pi*k_B)",
                "status": "analog",
            },
            {
                "grut_quantity": "w_Phi = -1 at equilibrium",
                "thermo_quantity": "NEC-saturating equation of state",
                "relationship": "rho + p = 0 at equilibrium (zero temperature limit?)",
                "status": "conditional",
            },
            {
                "grut_quantity": "gamma_mem (memory-mediated damping)",
                "thermo_quantity": "Thermal dissipation rate",
                "relationship": "gamma_mem = alpha*omega^2*tau/(2*(1+(omega*tau)^2))",
                "status": "derived",
            },
        ],
    )


# ================================================================
# Hard Blockers After Thermo
# ================================================================

def build_hard_blockers_after_thermo() -> List[Dict[str, Any]]:
    """Hard blockers surviving through the thermodynamic audit."""
    return [
        {
            "name": "temperature_not_uniquely_derived",
            "type": "currently_missing_potentially_extendable",
            "survives_thermo": True,
            "description": (
                "Multiple candidate temperatures exist (T_dissipation, "
                "T_structural) differing by factor Q. Temperature is "
                "definable but not uniquely derived from GRUT architecture."
            ),
        },
        {
            "name": "entropy_is_proxy",
            "type": "currently_missing_potentially_extendable",
            "survives_thermo": True,
            "description": (
                "Entropy uses the classical area proxy S = pi*R_eq^2/l_P^2. "
                "No microstate counting or quantum entropy formula exists."
            ),
        },
        {
            "name": "no_hawking_radiation",
            "type": "structural",
            "survives_thermo": True,
            "description": (
                "Hawking radiation requires semiclassical QFT in curved "
                "spacetime. GRUT has no quantum field theory on the interior."
            ),
        },
        {
            "name": "information_paradox_unsolved",
            "type": "structural",
            "survives_thermo": True,
            "description": "Information paradox requires quantum gravity.",
        },
        {
            "name": "noise_spectrum_conditional",
            "type": "currently_missing_potentially_extendable",
            "survives_thermo": True,
            "description": (
                "FDT noise form is determined up to temperature, but "
                "temperature itself is not uniquely derived. Noise spectrum "
                "is conditional, not absolute."
            ),
        },
        {
            "name": "covariant_interior_metric_missing",
            "type": "structural",
            "survives_thermo": True,
            "description": "Phase V lapse obstruction unchanged.",
        },
        {
            "name": "circularity_not_broken",
            "type": "structural",
            "survives_thermo": True,
            "description": "Q1-Q3 circularity unchanged by thermodynamic audit.",
        },
        {
            "name": "no_born_rule",
            "type": "structural",
            "survives_thermo": True,
            "description": "Appendix C boundary. No change.",
        },
        {
            "name": "no_measurement_coupling",
            "type": "structural",
            "survives_thermo": True,
            "description": "Appendix C boundary. No change.",
        },
        {
            "name": "no_interference_formalism",
            "type": "structural",
            "survives_thermo": True,
            "description": "Appendix C boundary. No change.",
        },
        {
            "name": "no_particle_ontology",
            "type": "structural",
            "survives_thermo": True,
            "description": "Appendix C boundary. No change.",
        },
        {
            "name": "generalized_second_law_underdetermined",
            "type": "currently_missing_potentially_extendable",
            "survives_thermo": True,
            "description": (
                "Entropy production during collapse is underdetermined. "
                "The relevant entropy measure (shell area vs horizon area "
                "vs generalized entropy) is not uniquely defined."
            ),
        },
    ]


# ================================================================
# Master Builder
# ================================================================

def run_thermodynamic_audit() -> ThermoResult:
    """Execute Appendix D — Thermodynamic Sector Audit."""

    temp_audit = build_temperature_audit()
    entropy = analyze_entropy()
    first_law = test_first_law()
    ent_prod = test_entropy_production()
    fdt = test_fdt_compatibility()
    trans_map = build_translation_map()
    blockers = build_hard_blockers_after_thermo()

    # Executive determination
    # The sector is "partially consistent" because:
    # - Temperature: definable but not unique (factor Q ambiguity)
    # - Entropy: area-law modified by memory (proxy, not derived)
    # - First law: partially consistent (within order of magnitude)
    # - Entropy production: underdetermined
    # - FDT: conditional on temperature
    executive = "thermodynamic_sector_partially_consistent"

    safe_claims = [
        "The GRUT interior has at least two GRUT-native candidate "
        "temperatures (T_dissipation = hbar*omega_0/(Q*k_B) and "
        "T_structural = hbar*omega_0/k_B) that differ by a factor "
        "of Q ~ 6.",

        "The GRUT endpoint area pi*R_eq^2 provides a Bekenstein-Hawking-"
        "like entropy proxy with the standard M^2 scaling.",

        "The first law dM = T_diss * dS is partially consistent: the "
        "product T*dS/dM is within an order of magnitude of unity.",

        "IF the Q2 Drude bath is physical AND FDT applies, the noise "
        "power spectral density is Lorentzian with amplitude determined "
        "by the candidate temperature. This is a CONDITIONAL result.",

        "The thermodynamic translation map identifies 8 GRUT-to-thermo "
        "quantity correspondences, of which 3 are derived, 2 are candidate, "
        "1 is proxy, 1 is analog, and 1 is conditional.",

        "All Appendix C blockers remain in force.",
    ]

    unsafe_claims = [
        "The GRUT interior has a unique, derived temperature.",
        "Hawking radiation is derived or explained.",
        "The information paradox is addressed.",
        "Unitarity is proven or implied.",
        "The generalized second law is verified.",
        "Standard BH thermodynamics is recovered as a GRUT output.",
        "The noise spectrum is computed (it is conditional on temperature).",
        "Entropy is a quantum quantity (it is a classical area proxy).",
        "Any Appendix C blocker is resolved.",
    ]

    nonclaims = [
        "Appendix D does NOT derive Hawking radiation.",
        "Appendix D does NOT solve the information paradox.",
        "Appendix D does NOT prove or assume unitarity.",
        "'Partially consistent' means the thermodynamic quantities are "
        "definable and mutually compatible within order-of-magnitude, NOT "
        "that they are derived or proven.",
        "The Q-factor ambiguity (T_dissipation vs T_structural) reflects "
        "a genuine physical question: does the memory bath temperature "
        "correspond to energy per mode or energy dissipated per cycle?",
        "Standard BH thermodynamics is NOT imported as GRUT content. "
        "T_hawking is included only as comparison baseline.",
        "The FDT compatibility is CONDITIONAL: it assumes both the bath "
        "is physical and FDT applies.",
        "All Appendix C quantum blockers remain in force.",
    ]

    result = ThermoResult(
        executive_determination=executive,
        temperature_audit=temp_audit,
        entropy_analysis=entropy,
        first_law_test=first_law,
        entropy_production=ent_prod,
        fdt_compatibility=fdt,
        translation_map=trans_map,
        temperature_classification=temp_audit.classification,
        entropy_classification=entropy.classification,
        first_law_classification=first_law.classification,
        entropy_production_classification=ent_prod.classification,
        fdt_classification=fdt.classification,
        hard_blockers_after_thermo=blockers,
        safe_claims=safe_claims,
        unsafe_claims=unsafe_claims,
        nonclaims=nonclaims,
        valid=True,
    )

    _validate_thermo(result)
    return result


# ================================================================
# Validation Guard
# ================================================================

def _validate_thermo(result: ThermoResult) -> None:
    """Validate that thermodynamic result does not overclaim."""

    if result.executive_determination not in EXECUTIVE_CLASSIFICATIONS:
        raise ValueError(
            f"Executive '{result.executive_determination}' not in "
            f"{EXECUTIVE_CLASSIFICATIONS}"
        )

    if result.temperature_classification not in TEMPERATURE_CLASSIFICATIONS:
        raise ValueError(
            f"Temperature classification '{result.temperature_classification}' "
            f"not in {TEMPERATURE_CLASSIFICATIONS}"
        )

    if result.entropy_classification not in ENTROPY_CLASSIFICATIONS:
        raise ValueError(
            f"Entropy classification '{result.entropy_classification}' "
            f"not in {ENTROPY_CLASSIFICATIONS}"
        )

    if result.first_law_classification not in FIRST_LAW_CLASSIFICATIONS:
        raise ValueError(
            f"First law classification '{result.first_law_classification}' "
            f"not in {FIRST_LAW_CLASSIFICATIONS}"
        )

    if result.entropy_production_classification not in ENTROPY_PRODUCTION_CLASSIFICATIONS:
        raise ValueError(
            f"Entropy production '{result.entropy_production_classification}' "
            f"not in {ENTROPY_PRODUCTION_CLASSIFICATIONS}"
        )

    if result.fdt_classification not in FDT_CLASSIFICATIONS:
        raise ValueError(
            f"FDT classification '{result.fdt_classification}' "
            f"not in {FDT_CLASSIFICATIONS}"
        )

    # Must have nonclaims
    if len(result.nonclaims) < 5:
        raise ValueError(
            f"Must have at least 5 nonclaims, got {len(result.nonclaims)}"
        )

    # Must have hard blockers
    if len(result.hard_blockers_after_thermo) < 8:
        raise ValueError(
            f"Must have at least 8 hard blockers, got "
            f"{len(result.hard_blockers_after_thermo)}"
        )

    # Forbidden claims check
    for claim in THERMO_FORBIDDEN_CLAIMS:
        for sc in result.safe_claims:
            low = sc.lower()
            if claim == "derives_hawking_radiation" and "hawking radiation is derived" in low:
                raise ValueError(f"Safe claim asserts '{claim}'")
            if claim == "solves_information_paradox" and "information paradox is solved" in low:
                raise ValueError(f"Safe claim asserts '{claim}'")
            if claim == "temperature_is_proven" and "temperature is proven" in low:
                raise ValueError(f"Safe claim asserts '{claim}'")

    # Temperature must have at least 3 candidates
    if len(result.temperature_audit.candidates) < 3:
        raise ValueError(
            f"Must evaluate at least 3 temperature candidates, got "
            f"{len(result.temperature_audit.candidates)}"
        )

    # Must have at least 1 GRUT-native candidate
    if result.temperature_audit.n_grut_native < 1:
        raise ValueError("Must have at least 1 GRUT-native temperature candidate")
