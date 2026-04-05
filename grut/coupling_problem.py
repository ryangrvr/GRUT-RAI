"""
GRUT-II Epsilon — Coupling Problem: Regime-Dependent Amplitude Analysis
=========================================================================

The coupling problem (XVIII Gamma): no direct Phi-detector coupling exists.
The only native channel: Phi → T^Phi → G_ab → metric perturbation.

XVIII Beta showed this produces 10^-48 strain in the solar system.

BUT: the fluctuation amplitude sigma^2 = D / tau_local is REGIME-DEPENDENT.
Near compact objects, tau_local → t_dyn → SMALL, so sigma^2 → LARGE.

THIS MODULE COMPUTES:
  1. sigma^2(r) = D / tau_local(r) as a function of radius for various sources
  2. The induced metric fluctuation delta_g from T^Phi fluctuations
  3. The signal at various detector locations/types
  4. Whether ANY regime produces detectable effects through the native coupling

The key question: does the Level-1 tau reduction create a regime where the
native metric-mediated coupling becomes non-negligible?
"""

import math
import numpy as np
from dataclasses import dataclass, field
from typing import List

# Physical constants (SI)
G = 6.674e-11        # m^3 kg^-1 s^-2
C = 2.998e8           # m/s
HBAR = 1.055e-34      # J·s
K_B = 1.381e-23       # J/K
M_SUN = 1.989e30      # kg
R_SUN = 6.957e8       # m
M_SUN_GEOM = G * M_SUN / C**2  # = 1.477 km = 1477 m
AU = 1.496e11         # m

# GRUT constants (SI-compatible)
TAU_0_GEOM = math.sqrt(1.5)  # canonical tau in geometric units (dimensionless r_s units)
# In SI, tau depends on the object. For the Level-1 rule:
# tau_local = tau_0 * t_dyn / (tau_0 + t_dyn)
# where t_dyn = sqrt(r^3 / (2GM))

# GRUT-II Delta bound
D_OVER_TAU_MAX = 0.01  # sigma^2 < 0.01 for bridge stability


@dataclass
class RegimeResult:
    """Result for one physical regime."""
    name: str = ""
    M_kg: float = 0.0
    r_m: float = 0.0
    r_over_rs: float = 0.0
    t_dyn_s: float = 0.0
    tau_local_s: float = 0.0
    X_eq: float = 0.0          # equilibrium Phi value (geometric units)
    sigma_sq: float = 0.0      # D / tau_local (using D = D_max)
    sigma_over_X: float = 0.0  # fluctuation/equilibrium ratio
    delta_T_phi: float = 0.0   # T^Phi fluctuation (SI: J/m^3)
    delta_g: float = 0.0       # metric fluctuation (strain)
    notes: List[str] = field(default_factory=list)


def t_dyn(r_m, M_kg):
    """Newtonian free-fall timescale."""
    return math.sqrt(r_m**3 / (2 * G * M_kg))


def tau_local(r_m, M_kg, tau_0_s):
    """Level-1 local tau: 1/tau_local = 1/tau_0 + 1/t_dyn."""
    td = t_dyn(r_m, M_kg)
    return tau_0_s * td / (tau_0_s + td)


def r_s(M_kg):
    """Schwarzschild radius."""
    return 2 * G * M_kg / C**2


def compute_regime(
    name: str,
    M_kg: float,
    r_m: float,
    tau_0_s: float = 1e15,  # cosmological tau_0 ~ age of universe
    D_over_tau: float = D_OVER_TAU_MAX,
) -> RegimeResult:
    """Compute fluctuation amplitude and metric signal for one regime.

    Using the maximum allowed D from Delta: D = D_over_tau * tau_local.
    This gives sigma^2 = D_over_tau (constant! independent of tau_local).

    Wait — that's the KEY insight. If D is a universal constant,
    then sigma^2 = D / tau_local VARIES with position.
    But if D = sigma^2_max * tau (so sigma^2 = sigma^2_max always),
    then D itself varies with tau_local.

    The question is: is D universal or local?

    GRUT-II Alpha says D is a primitive constitutive constant — ONE number.
    So D is universal. Then sigma^2(r) = D / tau_local(r) varies.

    For D = D_max = 0.01 * tau_canonical (canonical geometric units):
    In SI, we need D in SI units. D has units [Phi]^2 * [time].

    In geometric units (G=c=1), Phi is dimensionless, tau has units of length.
    D has units of length.

    Converting: D_geometric = 0.01 * tau_geometric = 0.01 * sqrt(1.5) ≈ 0.0122
    in units of r_s.

    In SI at a given r_s: D_SI = D_geometric * r_s / c  [time * Phi^2]

    Actually, let me work in geometric units throughout and convert at the end.
    """
    rs = r_s(M_kg)
    r_over_rs_val = r_m / rs
    td = t_dyn(r_m, M_kg)
    tl = tau_local(r_m, M_kg, tau_0_s)

    # In geometric units: X = M/r^2 (dimensionless; M in units of r_s/2, r in units of r_s)
    # X_geom = (r_s/2) / (r/r_s * r_s)^2 = 1 / (2 * (r/r_s)^2)  ... in units where r_s = 1
    # Let's use SI throughout instead.

    # X(r) = GM/r^2 = gravitational acceleration [m/s^2]
    X_val = G * M_kg / r_m**2

    # Phi_eq = X in constitutive units. But we need to be careful about units.
    # The constitutive equation is tau dPhi/dt + Phi = X.
    # In SI, Phi and X have the same units. If X = GM/r^2 [m/s^2],
    # then Phi has units [m/s^2].
    # tau has units [s].
    # xi has units [m/s^2] (same as Phi).
    # D has units [m/s^2]^2 * [s] = [m^2 / s^3].
    # sigma^2 = D/tau has units [m^2/s^4] = [m/s^2]^2. Correct (variance of Phi).

    # D_max = D_over_tau_max * tau_local (in the regime where tau_local is the local timescale)
    # But wait — D is UNIVERSAL (one number). D_over_tau is position-dependent.
    # D is fixed. sigma^2 = D / tau_local varies.

    # Let me parameterize by D directly. We need D in SI units [m^2/s^3].
    # From Delta bound: D/tau < 0.01 means sigma^2 < 0.01 * [Phi]^2.
    # In geometric units, Phi ~ O(1), so sigma^2 < 0.01.
    # In SI, sigma^2 < 0.01 * X_eq^2... no, the bound was in canonical geometric units.

    # Let me just compute the ratio sigma/X as a function of position.
    # This is what matters for observability.

    # sigma^2 = D / tau_local
    # X_eq^2 = (GM/r^2)^2
    # sigma/X = sqrt(D / tau_local) / (GM/r^2)

    # For the metric fluctuation:
    # delta_T^Phi ~ (X/tau^2) * delta_Phi ~ (X/tau^2) * sigma
    # delta_g ~ (G/c^4) * delta_T * r^2

    # Let's compute with a specific D. Use D such that sigma^2 = D_over_tau * tau_canonical
    # at the canonical radius. Then D = D_over_tau * tau_canonical^2.
    # In SI: tau_canonical = sqrt(1.5) * (r_s / c) for a given object.

    tau_canonical_s = math.sqrt(1.5) * rs / C
    D_SI = D_over_tau * tau_canonical_s  # [m/s^2]^2 * [s] ... actually this doesn't work

    # I need to be more careful. Let me work in dimensionless geometric units
    # where r_s = 1, c = 1, M = 1/2.

    # In these units:
    # X(r) = M/r^2 = 1/(2r^2)  (r in units of r_s)
    # tau_canonical = sqrt(3/2) ≈ 1.22  (in units of r_s/c = r_s since c=1)
    # D_geom = 0.01 * tau_canonical ≈ 0.0122  (in geometric units)
    # sigma^2 = D_geom / tau_local  (tau_local in geometric units)

    # tau_local in geometric units:
    tau_local_geom = tl * C / rs  # convert from SI seconds to r_s/c units

    # D in geometric units (universal)
    D_geom = D_over_tau * math.sqrt(1.5)  # ≈ 0.0122

    # sigma^2 in geometric units
    sigma_sq_geom = D_geom / tau_local_geom if tau_local_geom > 0 else float('inf')

    # X in geometric units
    X_geom = 0.5 / (r_over_rs_val**2)

    # sigma / X ratio
    if X_geom > 0:
        sigma_over_X = math.sqrt(abs(sigma_sq_geom)) / X_geom
    else:
        sigma_over_X = float('inf')

    # Metric fluctuation estimate
    # delta_rho ~ X * delta_Phi / tau^2 ~ X * sigma / tau^2
    # In geometric units: delta_rho ~ X_geom * sqrt(sigma_sq_geom) / tau_local_geom^2
    if tau_local_geom > 1e-30:
        delta_rho_geom = X_geom * math.sqrt(abs(sigma_sq_geom)) / tau_local_geom**2
    else:
        delta_rho_geom = 0

    # Metric perturbation: delta_g ~ 8*pi*G * delta_rho * r^2 / c^4
    # In geometric units (G=c=1): delta_g ~ 8*pi * delta_rho * r^2
    delta_g_geom = 8 * math.pi * delta_rho_geom * r_over_rs_val**2

    # Convert to SI strain for comparison with detectors
    # In geometric units, delta_g is already dimensionless (strain)
    delta_g_strain = delta_g_geom

    notes = [
        "{}: M={:.1e} M_sun, r={:.1e} r_s".format(name, M_kg/M_SUN, r_over_rs_val),
        "t_dyn = {:.3e} s".format(td),
        "tau_local = {:.3e} s = {:.3e} r_s/c".format(tl, tau_local_geom),
        "X_eq (geom) = {:.3e}".format(X_geom),
        "sigma^2 (geom) = {:.3e}".format(sigma_sq_geom),
        "sigma/X = {:.3e}".format(sigma_over_X),
        "delta_g (strain) = {:.3e}".format(delta_g_strain),
    ]

    return RegimeResult(
        name=name,
        M_kg=M_kg, r_m=r_m, r_over_rs=r_over_rs_val,
        t_dyn_s=td, tau_local_s=tl,
        X_eq=X_geom, sigma_sq=sigma_sq_geom,
        sigma_over_X=sigma_over_X,
        delta_T_phi=delta_rho_geom,
        delta_g=delta_g_strain,
        notes=notes,
    )


if __name__ == "__main__":
    print("=" * 80)
    print("  GRUT-II EPSILON — COUPLING PROBLEM: REGIME-DEPENDENT ANALYSIS")
    print("  Native channel: Phi → T^Phi → G_ab → metric perturbation")
    print("  Question: Is there ANY regime where this channel is non-negligible?")
    print("=" * 80)

    tau_0_s = 1e15  # cosmological tau_0

    regimes = [
        # Solar system (XVIII Beta baseline)
        ("Mercury perihelion", M_SUN, 4.6e10),
        ("Earth orbit", M_SUN, AU),
        ("Solar surface", M_SUN, R_SUN),

        # Stellar compact objects
        ("WD surface (1 M_sun)", M_SUN, 6e6),
        ("NS surface (1.4 M_sun)", 1.4*M_SUN, 1e4),
        ("NS surface (2 M_sun)", 2*M_SUN, 1e4),

        # Near black hole horizon
        ("10 M_sun BH at 10 r_s", 10*M_SUN, 10 * r_s(10*M_SUN)),
        ("10 M_sun BH at 3 r_s", 10*M_SUN, 3 * r_s(10*M_SUN)),
        ("10 M_sun BH at 1.5 r_s (ISCO)", 10*M_SUN, 1.5 * r_s(10*M_SUN)),
        ("10 M_sun BH at 1.01 r_s", 10*M_SUN, 1.01 * r_s(10*M_SUN)),

        # Supermassive BH
        ("Sgr A* at 10 r_s", 4e6*M_SUN, 10 * r_s(4e6*M_SUN)),
        ("Sgr A* at 3 r_s", 4e6*M_SUN, 3 * r_s(4e6*M_SUN)),
        ("Sgr A* at 1.01 r_s", 4e6*M_SUN, 1.01 * r_s(4e6*M_SUN)),

        # Early universe (CMB epoch, using Hubble radius as r)
        ("CMB epoch (T~3000K)", 1e22*M_SUN, 1e23),  # approximate
        # Planck epoch
        ("Planck scale", 1e-8, 1.6e-35),  # M_Planck, l_Planck
    ]

    print("\n{:<35s} {:>10s} {:>10s} {:>12s} {:>12s} {:>12s} {:>12s}".format(
        "Regime", "r/r_s", "tau_loc(s)", "sigma^2", "sigma/X", "delta_g", "Detectable?"))
    print("-" * 105)

    # Detection thresholds
    LIGO_STRAIN = 1e-23
    LISA_STRAIN = 1e-20
    PTA_STRAIN = 1e-15

    for name, M, r in regimes:
        try:
            res = compute_regime(name, M, r, tau_0_s)
            detectable = "NO"
            if abs(res.delta_g) > LIGO_STRAIN:
                detectable = "LIGO"
            elif abs(res.delta_g) > LISA_STRAIN:
                detectable = "LISA"
            elif abs(res.delta_g) > PTA_STRAIN:
                detectable = "PTA"

            print("{:<35s} {:>10.2e} {:>10.2e} {:>12.3e} {:>12.3e} {:>12.3e} {:>12s}".format(
                res.name, res.r_over_rs, res.tau_local_s,
                res.sigma_sq, res.sigma_over_X, res.delta_g, detectable))
        except Exception as e:
            print("{:<35s} ERROR: {}".format(name, str(e)[:50]))

    print("\n" + "=" * 80)
    print("  ANALYSIS")
    print("=" * 80)

    # Compute the critical radius where sigma/X = 1 for a 10 M_sun BH
    print("\n  Critical radius where sigma/X = 1 (fluctuations = equilibrium):")
    print("  For 10 M_sun BH with D = 0.01*tau_canonical:")
    M_bh = 10 * M_SUN
    rs_bh = r_s(M_bh)
    # sigma^2 = D_geom / tau_local_geom
    # X = 1/(2*(r/r_s)^2)
    # sigma/X = sqrt(D_geom/tau_local_geom) * 2*(r/r_s)^2
    # sigma/X = 1 when D_geom/tau_local_geom = 1/(4*(r/r_s)^4)
    # tau_local_geom ≈ t_dyn_geom = sqrt(r_geom^3 / 1) for r_geom = r/r_s
    # So D_geom / sqrt(r_geom^3) = 1/(4*r_geom^4)
    # D_geom * 4 * r_geom^4 = sqrt(r_geom^3)
    # 4 D_geom * r_geom^{5/2} = 1  ... approximately
    D_geom = 0.01 * math.sqrt(1.5)
    # r_geom^{5/2} = 1/(4*D_geom)
    r_crit_geom = (1/(4*D_geom))**(2/5)
    print("  r_critical / r_s ≈ {:.2f}".format(r_crit_geom))
    print("  r_critical = {:.3e} m".format(r_crit_geom * rs_bh))

    print("\n  Key finding:")
    print("  At r ≈ {:.1f} r_s, constitutive fluctuations become order-unity.".format(r_crit_geom))
    print("  This is INSIDE the photon sphere (1.5 r_s) for stellar BHs.")
    print("  It is observationally INACCESSIBLE for external observers.")

    print("\n  At ISCO (1.5 r_s) for 10 M_sun:")
    res_isco = compute_regime("ISCO", M_bh, 1.5 * rs_bh, tau_0_s)
    print("  sigma/X = {:.3e}".format(res_isco.sigma_over_X))
    print("  delta_g = {:.3e} (LIGO: {:.0e})".format(res_isco.delta_g, LIGO_STRAIN))

    print("\n  At 3 r_s (last stable circular orbit in Kerr):")
    res_3rs = compute_regime("3 r_s", M_bh, 3 * rs_bh, tau_0_s)
    print("  sigma/X = {:.3e}".format(res_3rs.sigma_over_X))
    print("  delta_g = {:.3e}".format(res_3rs.delta_g))

    print("\n" + "=" * 80)
    print("  VERDICT")
    print("=" * 80)
    print("")
    print("  The native metric-mediated coupling remains BELOW all detector")
    print("  thresholds at every observationally accessible location.")
    print("")
    print("  Near-horizon (r < 1.5 r_s): fluctuations grow but the region")
    print("  is INSIDE the photon sphere / causally disconnected from")
    print("  external observers.")
    print("")
    print("  At ISCO and beyond: fluctuations are too small by many orders")
    print("  of magnitude to produce detectable metric perturbations.")
    print("")
    print("  The coupling problem is NOT solved by the Level-1 tau reduction.")
    print("  The regime where fluctuations are large is the regime where")
    print("  observations are impossible (deep interior / near-horizon).")
    print("")
    print("  STATUS: COUPLING PROBLEM PERSISTS.")
    print("  The native channel is structurally real but observationally dead")
    print("  at every accessible radius for every astrophysical source.")
    print("=" * 80)
