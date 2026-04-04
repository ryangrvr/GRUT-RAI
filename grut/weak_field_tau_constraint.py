"""
Book XVI Beta — Weak-Field Exterior Correction and Tau-Constraint Computation
==============================================================================

Derives the weak-field metric correction from the GRUT equilibrium
stress-energy T^Phi, computes PPN-relevant deviations, and constrains
tau from precision gravity observations.

GOVERNING RESULT (Phase 4, xAct-verified):
  At equilibrium (Phi = X), the scalar energy-momentum has:
    rho_eq = -X^2 / (2 tau^2)
    p_r = +X^2 / (2 tau^2)
    w = -1, NEC-saturated

IDENTIFICATION (weak-field Schwarzschild exterior):
  X(r) = M/r^2  (Newtonian gravitational acceleration)
  => rho_eq(r) = -M^2 / (2 tau^2 r^4)

WHAT THIS MODULE COMPUTES:
  1. Modified mass function m(r) from integrating rho_eq
  2. Exterior metric correction delta_f(r) = -4*pi*M^2/(tau^2 * r^2)
  3. Effective PPN deviation: delta_beta = 4*pi / tau^2 (geometric units)
  4. Tau constraints from Mercury precession, Cassini bound, binary pulsars
  5. Irreducibility comparison: GRUT vs GR + massive scalar

UNITS: Geometric (G = c = 1). Lengths in km. Times in km (= seconds * c).
  M_sun = 1.477 km
  1 AU = 1.496e8 km
  c = 3.0e5 km/s
"""

from __future__ import annotations
import math
from dataclasses import dataclass, field
from typing import List, Dict


# ================================================================
# Physical Constants (geometric units: G = c = 1)
# ================================================================

C_LIGHT = 2.998e5        # km/s
M_SUN_KM = 1.477         # km (GM_sun/c^2)
R_SUN_KM = 6.957e5       # km
AU_KM = 1.496e8          # km
MERCURY_PERI_KM = 4.60e7 # km (Mercury perihelion)
R_EARTH_ORBIT = AU_KM

# Experimental bounds
CASSINI_GAMMA_BOUND = 2.3e-5     # |gamma - 1| < 2.3e-5
MERCURY_PRECESSION_BOUND = 1e-3  # fractional; precession known to ~0.1%
NORDTVEDT_BETA_BOUND = 1e-4      # |beta - 1| < ~1e-4 (LLR)


# ================================================================
# Dataclasses
# ================================================================

@dataclass
class WeakFieldCorrection:
    """Result of weak-field metric correction computation."""
    r_km: float = 0.0
    M_km: float = M_SUN_KM
    tau_km: float = 0.0        # tau in geometric units (km)
    tau_seconds: float = 0.0

    # Mass correction
    delta_m_km: float = 0.0    # excess enclosed mass at r

    # Metric correction
    delta_f: float = 0.0       # correction to g_tt component
    f_schwarzschild: float = 0.0
    f_total: float = 0.0

    # PPN comparison
    U: float = 0.0             # Newtonian potential M/r
    U_squared: float = 0.0
    delta_beta_effective: float = 0.0  # delta_f / U^2

    notes: List[str] = field(default_factory=list)


@dataclass
class TauConstraint:
    """Tau constraint from a specific observation."""
    observation: str = ""
    r_km: float = 0.0
    M_km: float = M_SUN_KM
    bound_on_delta_f: float = 0.0    # |delta_f| must be < this
    bound_on_delta_beta: float = 0.0 # |delta_beta| must be < this
    tau_lower_bound_km: float = 0.0  # tau must be > this (km)
    tau_lower_bound_s: float = 0.0   # tau must be > this (seconds)
    notes: List[str] = field(default_factory=list)


@dataclass
class IrreducibilityTest:
    """Result of irreducibility comparison."""
    comparison: str = ""
    matches: List[str] = field(default_factory=list)
    differs: List[str] = field(default_factory=list)
    irreducible: bool = False
    verdict: str = ""
    notes: List[str] = field(default_factory=list)


@dataclass
class WeakFieldAuditResult:
    """Master result for XVI Beta weak-field audit."""
    corrections: List[WeakFieldCorrection] = field(default_factory=list)
    constraints: List[TauConstraint] = field(default_factory=list)
    irreducibility: List[IrreducibilityTest] = field(default_factory=list)

    # Global tau bound
    tau_min_km: float = 0.0
    tau_min_s: float = 0.0
    controlling_observation: str = ""

    # Verdict
    observationally_distinct: bool = False
    observationally_silent: bool = False
    tau_collapse: bool = False
    verdict: str = ""
    notes: List[str] = field(default_factory=list)


# ================================================================
# Core Computations
# ================================================================

def compute_weak_field_correction(
    r_km: float,
    M_km: float = M_SUN_KM,
    tau_s: float = 1.0,
) -> WeakFieldCorrection:
    """Compute the weak-field metric correction at radius r.

    The equilibrium energy density:
      rho_eq(r) = -M^2 / (2 tau^2 r^4)  [geometric units]

    Integrating dm/dr = 4*pi*r^2 * rho_eq from r to infinity:
      delta_m(r) = 2*pi*M^2 / (tau^2 * r)

    Metric correction:
      delta_f(r) = -2*delta_m(r)/r = -4*pi*M^2 / (tau^2 * r^2)

    In PPN comparison:
      U = M/r (Newtonian potential)
      delta_f / U^2 = -4*pi / tau^2
    """
    tau_km = tau_s * C_LIGHT  # convert seconds to km

    # Newtonian potential
    U = M_km / r_km
    U_sq = U * U

    # Schwarzschild metric
    f_schw = 1.0 - 2.0 * M_km / r_km

    # GRUT correction
    delta_m = 2.0 * math.pi * M_km**2 / (tau_km**2 * r_km)
    delta_f = -4.0 * math.pi * M_km**2 / (tau_km**2 * r_km**2)

    # PPN comparison
    delta_beta = -4.0 * math.pi / tau_km**2 if tau_km > 0 else float('inf')

    return WeakFieldCorrection(
        r_km=r_km,
        M_km=M_km,
        tau_km=tau_km,
        tau_seconds=tau_s,
        delta_m_km=delta_m,
        delta_f=delta_f,
        f_schwarzschild=f_schw,
        f_total=f_schw + delta_f,
        U=U,
        U_squared=U_sq,
        delta_beta_effective=delta_beta,
        notes=[
            "r = {:.3e} km".format(r_km),
            "tau = {:.3e} s = {:.3e} km".format(tau_s, tau_km),
            "U = M/r = {:.6e}".format(U),
            "delta_f = {:.6e}".format(delta_f),
            "|delta_f/U^2| = {:.6e}".format(abs(delta_f / U_sq) if U_sq > 0 else 0),
            "|delta_beta| = 4*pi/tau^2 = {:.6e}".format(abs(delta_beta)),
        ],
    )


def compute_tau_constraint(
    observation: str,
    r_km: float,
    M_km: float,
    bound_on_delta_beta: float,
) -> TauConstraint:
    """Compute lower bound on tau from a precision-gravity observation.

    The effective PPN deviation: |delta_beta| = 4*pi / tau^2 [geometric units]
    Requiring |delta_beta| < bound:
      tau^2 > 4*pi / bound
      tau > sqrt(4*pi / bound)  [km]
    """
    if bound_on_delta_beta <= 0:
        tau_min_km = float('inf')
    else:
        tau_min_km = math.sqrt(4.0 * math.pi / bound_on_delta_beta)

    tau_min_s = tau_min_km / C_LIGHT

    # Also compute the direct delta_f bound at this radius
    # |delta_f| < bound * U^2 where U = M/r
    U = M_km / r_km
    bound_delta_f = bound_on_delta_beta * U * U

    return TauConstraint(
        observation=observation,
        r_km=r_km,
        M_km=M_km,
        bound_on_delta_f=bound_delta_f,
        bound_on_delta_beta=bound_on_delta_beta,
        tau_lower_bound_km=tau_min_km,
        tau_lower_bound_s=tau_min_s,
        notes=[
            "Observation: {}".format(observation),
            "Bound on |delta_beta|: {:.1e}".format(bound_on_delta_beta),
            "tau > {:.6e} km = {:.6e} s".format(tau_min_km, tau_min_s),
            "|delta_f| at r = {:.3e} km: < {:.3e}".format(r_km, bound_delta_f),
        ],
    )


def test_irreducibility_scalar(
) -> IrreducibilityTest:
    """Test whether GRUT equilibrium T^Phi reduces to GR + massive scalar.

    GRUT action at equilibrium:
      S = integral[(1/2)(nabla Phi)^2 + Phi^2/(2tau^2) - Phi*X/tau]

    This IS the action of a massive scalar field:
      mass: m_phi = 1/tau
      potential: V(Phi) = Phi^2/(2tau^2)
      external source coupling: J = X/tau

    At equilibrium (Phi = X, nabla Phi = 0):
      rho = V - Phi*J = -X^2/(2tau^2)

    This is EXACTLY what a massive scalar field sourced by gravity produces.
    """
    return IrreducibilityTest(
        comparison="GR + minimally coupled massive scalar",
        matches=[
            "Action form: S = (1/2)(nabla Phi)^2 + V(Phi) - Phi*J is standard",
            "V(Phi) = Phi^2/(2tau^2) is a standard mass term with m_phi = 1/tau",
            "J = X/tau is a standard external source coupling",
            "Equilibrium rho = -X^2/(2tau^2) follows from standard scalar T_{mu nu}",
            "Equation of state w = -1 at equilibrium: standard for sourced massive scalar",
            "NEC saturation: standard for scalar at static equilibrium with this V",
            "Weak-field correction: same 1/r^4 energy density as sourced massive scalar",
        ],
        differs=[
            "DYNAMICS: GRUT is first-order (tau dPhi/dt + Phi = X); scalar is second-order (Box Phi + V' = J)",
            "TIME-REVERSAL: GRUT breaks T natively; scalar preserves T",
            "APPROACH TO EQUILIBRIUM: GRUT has Lyapunov monotone; scalar has oscillatory approach",
            "TRANSIENT BEHAVIOR: GRUT is overdamped relaxation; scalar has wave propagation",
        ],
        irreducible=False,
        verdict=(
            "AT EQUILIBRIUM: REDUCIBLE. The static T^Phi is identical to GR + massive scalar. "
            "The equilibrium energy density, equation of state, and metric correction are "
            "indistinguishable from a standard massive scalar field sourced by gravity. "
            "AWAY FROM EQUILIBRIUM: IRREDUCIBLE. The first-order dynamics, Lyapunov stability, "
            "and native time-reversal breaking have no standard scalar counterpart."
        ),
    )


def test_irreducibility_r_squared(
) -> IrreducibilityTest:
    """Test whether GRUT equilibrium reduces to R^2 / curvature-squared correction."""
    return IrreducibilityTest(
        comparison="GR + R^2 curvature-squared correction",
        matches=[
            "Both produce corrections to Schwarzschild exterior",
            "Both are sourced by curvature (ultimately from mass)",
        ],
        differs=[
            "SCALING: GRUT rho ~ M^2/r^4 (from X = M/r^2 squared); R^2 correction rho ~ M^2/r^6",
            "The radial dependence is different: 1/r^4 vs 1/r^6",
            "GRUT correction comes from scalar equilibrium, not from higher-derivative gravity",
            "R^2 corrections modify the gravitational equations themselves; GRUT adds matter",
            "GRUT has a free parameter tau; R^2 has a coupling constant",
        ],
        irreducible=True,
        verdict=(
            "NOT EQUIVALENT. Different radial scaling (1/r^4 vs 1/r^6) means the theories "
            "are distinguishable in principle. GRUT's correction comes from scalar matter, "
            "not from modified gravity. However, both are observationally negligible in "
            "the weak field."
        ),
    )


def test_irreducibility_semiclassical(
) -> IrreducibilityTest:
    """Test whether GRUT equilibrium reduces to semiclassical vacuum polarization."""
    return IrreducibilityTest(
        comparison="Semiclassical vacuum polarization (<T_{mu nu}> on curved background)",
        matches=[
            "Both produce negative energy densities in vacuum",
            "Both are sourced by curvature/gravitational field",
            "Both produce corrections to the classical metric",
        ],
        differs=[
            "SCALING: GRUT rho ~ M^2/(tau^2 r^4); semiclassical ~ hbar*(curvature)^2 ~ hbar*M^2/r^6",
            "PARAMETER: GRUT has tau (classical); semiclassical has hbar (quantum)",
            "MAGNITUDE: semiclassical is Planck-suppressed; GRUT is tau-suppressed",
            "ORIGIN: GRUT from classical constitutive equation; semiclassical from quantum vacuum fluctuations",
            "SIGN: Both negative, but different functional forms",
        ],
        irreducible=True,
        verdict=(
            "NOT EQUIVALENT. Different physical origin, different scaling, different "
            "suppression parameters. GRUT is classical; semiclassical is quantum. "
            "Both are negligible in the weak field but for different reasons."
        ),
    )


# ================================================================
# Master Computation
# ================================================================

def run_full_audit(
) -> WeakFieldAuditResult:
    """Run the complete XVI Beta weak-field audit."""

    # ---- Weak-field corrections at key locations ----
    corrections = []

    # Solar system locations with tau = 1 second (aggressive lower bound)
    for label, r_km, tau_s in [
        ("Mercury perihelion (tau=1s)", MERCURY_PERI_KM, 1.0),
        ("Earth orbit (tau=1s)", AU_KM, 1.0),
        ("Mercury perihelion (tau=t_dyn)", MERCURY_PERI_KM,
         math.sqrt(MERCURY_PERI_KM**3 / (2 * M_SUN_KM)) / C_LIGHT),
        ("Earth orbit (tau=t_dyn)", AU_KM,
         math.sqrt(AU_KM**3 / (2 * M_SUN_KM)) / C_LIGHT),
        ("Solar surface (tau=t_dyn)", R_SUN_KM,
         math.sqrt(R_SUN_KM**3 / (2 * M_SUN_KM)) / C_LIGHT),
    ]:
        c = compute_weak_field_correction(r_km, M_SUN_KM, tau_s)
        c.notes.insert(0, label)
        corrections.append(c)

    # ---- Tau constraints from precision gravity ----
    constraints = []

    # Nordtvedt / LLR bound on beta
    constraints.append(compute_tau_constraint(
        "Nordtvedt/LLR (beta)", AU_KM, M_SUN_KM, NORDTVEDT_BETA_BOUND,
    ))

    # Cassini bound on gamma (using as proxy for general PPN)
    constraints.append(compute_tau_constraint(
        "Cassini (gamma proxy)", AU_KM, M_SUN_KM, CASSINI_GAMMA_BOUND,
    ))

    # Mercury precession
    constraints.append(compute_tau_constraint(
        "Mercury precession", MERCURY_PERI_KM, M_SUN_KM, MERCURY_PRECESSION_BOUND,
    ))

    # Find strongest constraint (largest tau_min)
    strongest = max(constraints, key=lambda c: c.tau_lower_bound_km)
    tau_min_km = strongest.tau_lower_bound_km
    tau_min_s = strongest.tau_lower_bound_s

    # ---- Irreducibility tests ----
    irreducibility = [
        test_irreducibility_scalar(),
        test_irreducibility_r_squared(),
        test_irreducibility_semiclassical(),
    ]

    # ---- Check observational distinctness ----
    # At the tau lower bound, what is the correction at Mercury?
    c_at_bound = compute_weak_field_correction(MERCURY_PERI_KM, M_SUN_KM, tau_min_s)

    # Is the correction detectable?
    # Detectable means |delta_f/U^2| > ~10^-5 (Cassini-level precision)
    detectable_threshold = 1e-5
    observable = abs(c_at_bound.delta_beta_effective) > detectable_threshold

    # ---- Determine verdict ----
    if not observable:
        if abs(c_at_bound.delta_beta_effective) < 1e-20:
            verdict = "A_OBSERVATIONALLY_SILENT"
            observationally_silent = True
            observationally_distinct = False
            tau_collapse = True
        else:
            verdict = "A_EFFECTIVELY_SILENT"
            observationally_silent = True
            observationally_distinct = False
            tau_collapse = True
    else:
        verdict = "C_OBSERVATIONALLY_DISTINCT"
        observationally_silent = False
        observationally_distinct = True
        tau_collapse = False

    notes = [
        "Strongest tau constraint: {} (tau > {:.3e} s)".format(
            strongest.observation, tau_min_s),
        "|delta_beta| at tau bound: {:.3e}".format(
            abs(c_at_bound.delta_beta_effective)),
        "Detectable (|delta_beta| > {:.0e})? {}".format(
            detectable_threshold, observable),
        "Verdict: {}".format(verdict),
        "",
        "STRUCTURAL REASON for observational silence:",
        "  delta_beta = 4*pi/tau^2 [geometric units: km^2]",
        "  Even at tau = 1 second = {:.0e} km: delta_beta = {:.3e}".format(
            C_LIGHT, 4 * math.pi / C_LIGHT**2),
        "  This is {:.1e} times smaller than Cassini precision".format(
            4 * math.pi / (C_LIGHT**2 * CASSINI_GAMMA_BOUND)),
        "",
        "The correction is STRUCTURALLY SUPPRESSED by c^2 in the denominator",
        "of tau^2 (geometric) = (tau_seconds * c)^2. Even tau = 1 second gives",
        "tau_geometric = 3e5 km, and 4*pi/tau^2 ~ 1.4e-11.",
        "This is below Cassini (2.3e-5) by factor ~6e5.",
        "",
        "To achieve delta_beta > 2.3e-5 would require:",
        "  tau < sqrt(4*pi/2.3e-5) = {:.1f} km = {:.3e} seconds".format(
            math.sqrt(4 * math.pi / CASSINI_GAMMA_BOUND),
            math.sqrt(4 * math.pi / CASSINI_GAMMA_BOUND) / C_LIGHT),
        "  That is {:.1f} km, or {:.1e} Schwarzschild radii of the Sun".format(
            math.sqrt(4 * math.pi / CASSINI_GAMMA_BOUND),
            math.sqrt(4 * math.pi / CASSINI_GAMMA_BOUND) / (2 * M_SUN_KM)),
    ]

    return WeakFieldAuditResult(
        corrections=corrections,
        constraints=constraints,
        irreducibility=irreducibility,
        tau_min_km=tau_min_km,
        tau_min_s=tau_min_s,
        controlling_observation=strongest.observation,
        observationally_distinct=observationally_distinct,
        observationally_silent=observationally_silent,
        tau_collapse=tau_collapse,
        verdict=verdict,
        notes=notes,
    )


# ================================================================
# Main
# ================================================================

if __name__ == "__main__":
    print("=" * 75)
    print("  BOOK XVI BETA — WEAK-FIELD EXTERIOR CORRECTION AND TAU CONSTRAINT")
    print("=" * 75)

    result = run_full_audit()

    print("\n--- Weak-Field Corrections ---")
    hdr = "{:<35s} {:>12s} {:>12s} {:>14s} {:>14s}".format(
        "Location", "tau (s)", "|delta_f|", "|delta_f/U^2|", "|delta_beta|")
    print(hdr)
    print("-" * 90)
    for c in result.corrections:
        print("{:<35s} {:>12.3e} {:>12.3e} {:>14.3e} {:>14.3e}".format(
            c.notes[0] if c.notes else "",
            c.tau_seconds,
            abs(c.delta_f),
            abs(c.delta_f / c.U_squared) if c.U_squared > 0 else 0,
            abs(c.delta_beta_effective),
        ))

    print("\n--- Tau Constraints from Precision Gravity ---")
    hdr = "{:<30s} {:>12s} {:>14s} {:>14s}".format(
        "Observation", "Bound", "tau_min (km)", "tau_min (s)")
    print(hdr)
    print("-" * 75)
    for tc in result.constraints:
        print("{:<30s} {:>12.1e} {:>14.3e} {:>14.3e}".format(
            tc.observation, tc.bound_on_delta_beta,
            tc.tau_lower_bound_km, tc.tau_lower_bound_s))

    print("\n--- Irreducibility Tests ---")
    for ir in result.irreducibility:
        print("\n  vs {}:".format(ir.comparison))
        print("    Irreducible: {}".format(ir.irreducible))
        print("    Verdict: {}".format(ir.verdict[:120]))

    print("\n--- Global Result ---")
    print("  Strongest constraint: {}".format(result.controlling_observation))
    print("  tau_min = {:.3e} km = {:.3e} s".format(
        result.tau_min_km, result.tau_min_s))
    print("  Observationally distinct: {}".format(result.observationally_distinct))
    print("  Observationally silent: {}".format(result.observationally_silent))
    print("  Tau collapse: {}".format(result.tau_collapse))
    print("  Verdict: {}".format(result.verdict))

    print("\n--- Structural Analysis ---")
    for n in result.notes:
        print("  {}".format(n))

    print("\n" + "=" * 75)
    print("  CRITICAL FINDING")
    print("=" * 75)
    print("  The equilibrium T^Phi correction to the Schwarzschild metric is:")
    print("    delta_f = -4*pi*M^2 / (tau^2 * r^2)  [geometric units]")
    print("")
    print("  Relative to the PPN U^2 term:")
    print("    delta_beta = 4*pi / tau^2  [geometric: tau in km]")
    print("    delta_beta = 4*pi / (tau_s * c)^2")
    print("")
    print("  At tau = 1 second:")
    print("    delta_beta = 4*pi / (3e5)^2 = {:.3e}".format(
        4 * math.pi / C_LIGHT**2))
    print("    Cassini bound: 2.3e-5")
    print("    Ratio: {:.1e} (below detection by 6 orders)".format(
        4 * math.pi / (C_LIGHT**2 * CASSINI_GAMMA_BOUND)))
    print("")
    print("  To reach Cassini precision requires:")
    tau_crit = math.sqrt(4 * math.pi / CASSINI_GAMMA_BOUND)
    print("    tau < {:.1f} km = {:.3e} seconds".format(
        tau_crit, tau_crit / C_LIGHT))
    print("    = {:.1f} Schwarzschild radii of the Sun".format(
        tau_crit / (2 * M_SUN_KM)))
    print("")
    print("  This means tau must be SHORTER than ~2 milliseconds to produce")
    print("  a detectable PPN deviation. No physical tau in the GRUT program")
    print("  is this small. The local dynamical time t_dyn is always >> 1 ms")
    print("  at any astrophysically relevant radius.")
    print("")
    print("  VERDICT: THE WEAK-FIELD CONSTITUTIVE GRAVITY CLAIM IS")
    print("  OBSERVATIONALLY SILENT. The metric correction is structurally")
    print("  suppressed by c^2 in tau_geometric. No precision-gravity test")
    print("  can detect it.")
    print("=" * 75)
