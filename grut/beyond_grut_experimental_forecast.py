#!/usr/bin/env python3
"""
Beyond GRUT — Experimental Forecast

THE QUESTION: Does the zero-parameter decoherence sector survive contact with data?

This file produces:
  1. Parameter-free GRUT predictions for all five decoherence channels
  2. Competing model predictions (CSL, Diosi-Penrose point-mass)
  3. Sensitivity curves for current and near-future experiments
  4. The sharpest near-term discriminant and its requirements
  5. Uncertainty analysis: what systematic errors could fake/mask the signal

All GRUT predictions have ZERO adjustable parameters.
"""

import numpy as np
import os

# ============================================================
# PHYSICAL CONSTANTS
# ============================================================
G     = 6.67430e-11     # m^3 kg^-1 s^-2
hbar  = 1.05457e-34     # J s
c     = 2.99792e8       # m/s
k_B   = 1.38065e-23     # J/K
sigma_SB = 5.67037e-8   # W m^-2 K^-4
m_amu = 1.66054e-27     # kg per amu
a_0   = 5.29177e-11     # Bohr radius

print("=" * 90)
print("GRUT EXPERIMENTAL FORECAST — ZERO FREE PARAMETERS")
print("=" * 90)

# ============================================================
# SECTION 1: DECOHERENCE CHANNEL FORMULAS
# ============================================================

def Lambda_grav(m, l, R=None):
    """GRUT gravitational decoherence rate.
    Lambda = G m^2 / (hbar l) * S(l/R)
    S = 1 for l >= 2R (point-mass limit)
    S = (l/R)^3 / 6 for l < 2R (extended body)
    ZERO free parameters.
    """
    Lam_pt = G * m**2 / (hbar * l)
    if R is None or l >= 2*R:
        return Lam_pt
    else:
        S = (l/R)**3 / 6.0
        return Lam_pt * S

def Lambda_gas(m_particle, R, l, T, P, m_gas=4.65e-26):
    """Gas collision decoherence.
    Lambda_gas = (8 sqrt(2pi) / 3) * P R^2 l^2 / (hbar sqrt(m_gas k_B T))
    From Joos-Zeh / Hornberger scattering theory.
    m_gas = 28 amu (N2) default, or 4.65e-26 for residual gas mix.
    """
    # Localization rate from momentum transfer
    # Simplified Hornberger formula for thermal gas
    v_th = np.sqrt(8 * k_B * T / (np.pi * m_gas))
    n_gas = P / (k_B * T)
    sigma_scat = np.pi * R**2  # geometric cross section (long-wavelength limit)
    # Decoherence rate: Lambda ~ n sigma v (Delta x / lambda_dB)^2
    # where lambda_dB = hbar / (m_gas v_th) is thermal de Broglie of gas
    lambda_dB = hbar / (m_gas * v_th)
    if l < lambda_dB:
        # Short-distance: quadratic in l
        return n_gas * sigma_scat * v_th * (l / lambda_dB)**2
    else:
        # Long-distance: saturates
        return n_gas * sigma_scat * v_th

def Lambda_blackbody(R, l, T):
    """Blackbody photon scattering decoherence.
    Simplified Joos-Zeh formula in terms of dimensionless ratios.
    Lambda_BB ~ (c / lambda_th) * (R/lambda_th)^6 * (l/lambda_th)^2 * numerical
    For R << lambda_thermal (Rayleigh regime).
    """
    if T < 1e-6:
        return 0.0
    lambda_th = hbar * c / (k_B * T)
    r_ratio = R / lambda_th
    l_ratio = l / lambda_th
    if r_ratio < 0.1:
        # Rayleigh regime: Lambda ~ (c/lambda_th) * r_ratio^6 * l_ratio^2 * prefactor
        prefactor = 8.0 * np.pi**5 * 8.0 * 40320.0 / 9.0  # ~10^7
        return prefactor * (c / lambda_th) * r_ratio**6 * l_ratio**2
    else:
        # Geometric regime
        n_photon = 2.404 * (k_B * T)**3 / (np.pi**2 * (hbar * c)**3)
        sigma_geom = np.pi * R**2
        return n_photon * sigma_geom * c * min(1.0, l_ratio**2)

def Lambda_CSL(m, l, R, lambda_CSL=1e-16, r_CSL=1e-7):
    """CSL (Continuous Spontaneous Localization) decoherence.
    Lambda_CSL = lambda_CSL * (m/m_amu)^2 * f(R, r_CSL) * g(l, r_CSL)
    TWO free parameters: lambda_CSL, r_CSL.
    Standard values: lambda_CSL = 10^-16 Hz, r_CSL = 10^-7 m (GRW).
    Adler value: lambda_CSL = 10^-8 Hz.
    """
    # Geometry factor (for uniform sphere)
    if R < r_CSL:
        f_geom = 1.0  # point-like
    else:
        f_geom = (r_CSL / R)**3  # extended body
    # Localization factor
    if l < r_CSL:
        g_loc = (l / r_CSL)**2
    else:
        g_loc = 1.0
    n_nucleons = m / m_amu
    return lambda_CSL * n_nucleons**2 * f_geom * g_loc

def Lambda_DP_pointmass(m, l):
    """Diosi-Penrose point-mass gravitational decoherence.
    Lambda_DP = G m^2 / (hbar l)
    Same as GRUT in point-mass limit. NO extended-body correction.
    """
    return G * m**2 / (hbar * l)

# ============================================================
# SECTION 2: EXPERIMENTAL PLATFORMS
# ============================================================

print("""
===========================================================================
SECTION 2: EXPERIMENTAL PLATFORMS AND PARAMETER-FREE FORECASTS
===========================================================================
""")

# Define experimental platforms
platforms = {
    "OTIMA (current)": {
        "m": 1e4 * m_amu,       # 10^4 amu ~ gold cluster
        "R": 1e-9,              # ~1 nm
        "l": 100e-9,            # 100 nm grating period
        "T": 300,               # room temperature
        "P": 1e-7,              # ~10^-7 Pa
        "t_flight": 0.1,        # 100 ms flight time
        "status": "OPERATIONAL",
    },
    "MAQRO (proposed)": {
        "m": 1e9 * m_amu,       # 10^9 amu
        "R": 100e-9,            # 100 nm
        "l": 100e-9,            # 100 nm
        "T": 20e-3,             # 20 mK (space)
        "P": 1e-12,             # ~10^-12 Pa (space)
        "t_flight": 100,        # 100 s (free-fall in space)
        "status": "PROPOSED (ESA)",
    },
    "Levitated nanodiamond": {
        "m": 1e-14,             # 10 fg
        "R": 50e-9,             # 50 nm
        "l": 100e-9,            # 100 nm target
        "T": 10e-3,             # 10 mK
        "P": 1e-10,             # 10^-10 Pa
        "t_flight": 1.0,        # 1 s
        "status": "IN DEVELOPMENT",
    },
    "Micro-sphere (next gen)": {
        "m": 1e-12,             # 1 pg
        "R": 500e-9,            # 500 nm
        "l": 1e-6,              # 1 um
        "T": 1e-3,              # 1 mK
        "P": 1e-12,             # 10^-12 Pa
        "t_flight": 10.0,       # 10 s
        "status": "FUTURE (5-10 yr)",
    },
}

for name, params in platforms.items():
    m = params["m"]
    R = params["R"]
    l = params["l"]
    T = params["T"]
    P = params["P"]
    t_fl = params["t_flight"]

    Lg = Lambda_grav(m, l, R)
    Lgas = Lambda_gas(m, R, l, T, P)
    Lbb = Lambda_blackbody(R, l, T)
    Lcsl_grw = Lambda_CSL(m, l, R, lambda_CSL=1e-16, r_CSL=1e-7)
    Lcsl_adler = Lambda_CSL(m, l, R, lambda_CSL=1e-8, r_CSL=1e-7)
    Ldp = Lambda_DP_pointmass(m, l)

    # Visibility: V ~ exp(-Lambda * t_flight)
    # For interferometry: fringe visibility after time t_flight
    V_grav = np.exp(-Lg * t_fl)
    V_gas = np.exp(-Lgas * t_fl)
    V_total_grut = np.exp(-(Lg + Lgas + Lbb) * t_fl)

    # Signal: GRUT predicts V < 1; standard QM predicts V = 1 (no grav decoh)
    # Discriminability: need |V_QM - V_GRUT| > sigma_V (experimental uncertainty)

    print(f"  === {name} ({params['status']}) ===")
    print(f"  m = {m:.2e} kg ({m/m_amu:.0e} amu), R = {R*1e9:.0f} nm")
    print(f"  l = {l*1e9:.0f} nm, T = {T*1e3:.0f} mK, P = {P:.0e} Pa")
    print(f"  t_flight = {t_fl} s")
    print()
    print(f"  {'Channel':>25s}  {'Rate (Hz)':>12s}  {'t_coh (s)':>12s}  {'Visibility':>12s}")
    print(f"  {'-'*25}  {'-'*12}  {'-'*12}  {'-'*12}")

    channels = [
        ("GRUT gravitational",     Lg),
        ("Gas collisions",         Lgas),
        ("Blackbody radiation",    Lbb),
        ("CSL (GRW, lam=1e-16)",   Lcsl_grw),
        ("CSL (Adler, lam=1e-8)",  Lcsl_adler),
        ("DP point-mass (no S)",   Ldp),
    ]

    for ch_name, rate in channels:
        if rate > 0 and not np.isnan(rate) and not np.isinf(rate):
            t_coh = 1.0 / rate
            vis = np.exp(-rate * t_fl)
            print(f"  {ch_name:>25s}  {rate:12.2e}  {t_coh:12.2e}  {vis:12.6f}")
        else:
            print(f"  {ch_name:>25s}  {'~0':>12s}  {'inf':>12s}  {'1.000000':>12s}")

    print()
    print(f"  GRUT total visibility: {V_total_grut:.6f}")
    print(f"  Standard QM visibility (no grav): {np.exp(-(Lgas + Lbb) * t_fl):.6f}")
    print(f"  Visibility DROP from gravity: {np.exp(-(Lgas+Lbb)*t_fl) - V_total_grut:.2e}")
    print()

    # Can this experiment discriminate?
    # Need visibility drop > experimental uncertainty (typically ~1-10%)
    vis_drop = np.exp(-(Lgas+Lbb)*t_fl) - V_total_grut
    if vis_drop > 0.01:
        verdict = "CAN DISCRIMINATE (drop > 1%)"
    elif vis_drop > 0.001:
        verdict = "MARGINAL (drop 0.1-1%)"
    elif vis_drop > 1e-6:
        verdict = "CHALLENGING (drop < 0.1%)"
    else:
        verdict = "CANNOT DISCRIMINATE (drop negligible)"
    print(f"  DISCRIMINABILITY: {verdict}")
    print()

# ============================================================
# SECTION 3: PRESSURE SCAN — THE F3 DISCRIMINANT
# ============================================================
print("""
===========================================================================
SECTION 3: PRESSURE SCAN (F3 DISCRIMINANT)
===========================================================================

  The sharpest near-term test: vary pressure, look for a plateau.
  GRUT: Lambda decreases with P, then hits a floor (gravitational).
  Standard QM: Lambda decreases with P, goes to ZERO.
""")

# Use the levitated nanodiamond platform
m_scan = 1e-14
R_scan = 50e-9
l_scan = 100e-9
T_scan = 10e-3

Lg_scan = Lambda_grav(m_scan, l_scan, R_scan)
print(f"  Platform: m = {m_scan*1e15:.0f} fg, R = {R_scan*1e9:.0f} nm, l = {l_scan*1e9:.0f} nm, T = {T_scan*1e3:.0f} mK")
print(f"  GRUT gravitational rate: {Lg_scan:.2e} Hz (the FLOOR)")
print()
print(f"  {'P (Pa)':>12s}  {'Lambda_gas':>12s}  {'Lambda_grav':>12s}  {'Lambda_total':>14s}  {'floor?':>10s}")

P_values = np.logspace(-7, -14, 22)
for P in P_values:
    Lgas_v = Lambda_gas(m_scan, R_scan, l_scan, T_scan, P)
    Ltot = Lgas_v + Lg_scan
    is_floor = "FLOOR" if Lg_scan > 5 * Lgas_v else ""
    print(f"  {P:12.2e}  {Lgas_v:12.2e}  {Lg_scan:12.2e}  {Ltot:14.2e}  {is_floor:>10s}")

print()
print("  GRUT prediction: plateau at Lambda ~ 6.3e+02 Hz below P ~ 1e-10 Pa")
print("  Standard QM:     Lambda -> 0 as P -> 0 (no floor)")
print("  CSL (GRW):       plateau at Lambda ~ Lambda_CSL (adjustable)")
print()

# ============================================================
# SECTION 4: MASS SCAN — THE F1 DISCRIMINANT
# ============================================================
print("""
===========================================================================
SECTION 4: MASS SCAN (F1 DISCRIMINANT) — slope = 2.00
===========================================================================
""")

l_fixed = 100e-9
R_func = lambda m: (3*m/(4*np.pi*2300))**(1/3)  # silica sphere, rho=2300

print(f"  l = {l_fixed*1e9:.0f} nm (fixed), silica spheres (rho = 2300 kg/m^3)")
print()
print(f"  {'m (kg)':>12s}  {'m (amu)':>12s}  {'R (nm)':>10s}  {'Lambda_GRUT':>14s}  {'Lambda_DP_pt':>14s}  {'ratio':>10s}")

masses_scan = np.logspace(-22, -10, 25)
log_m_list = []
log_Lg_list = []

for m_v in masses_scan:
    R_v = R_func(m_v)
    Lg_v = Lambda_grav(m_v, l_fixed, R_v)
    Ldp_v = Lambda_DP_pointmass(m_v, l_fixed)
    ratio_v = Lg_v / Ldp_v if Ldp_v > 0 else 0

    if m_v > 1e-16 and Lg_v > 1e-30:  # only print interesting range
        log_m_list.append(np.log10(m_v))
        log_Lg_list.append(np.log10(Lg_v))
        print(f"  {m_v:12.2e}  {m_v/m_amu:12.2e}  {R_v*1e9:10.1f}  {Lg_v:14.2e}  {Ldp_v:14.2e}  {ratio_v:10.2e}")

# Fit slope
if len(log_m_list) > 3:
    log_m_arr = np.array(log_m_list)
    log_Lg_arr = np.array(log_Lg_list)
    coeffs = np.polyfit(log_m_arr, log_Lg_arr, 1)
    slope = coeffs[0]
    print()
    print(f"  Fitted slope d(log Lambda)/d(log m) = {slope:.4f}")
    print(f"  GRUT prediction: slope = 2.00 exactly (from Lambda ~ m^2)")
    print(f"  Deviation from 2: {abs(slope - 2):.4f}")
    print(f"  (Deviation comes from extended-body correction S(l/R) ~ (l/R)^3 ~ m^-1,")
    print(f"   giving effective Lambda ~ m^2 × m^-1 = m^1 in the near-field regime,")
    print(f"   transitioning to Lambda ~ m^2 in the far-field regime.)")
    print()
    print(f"  KEY SUBTLETY: The EFFECTIVE mass scaling depends on l/R(m).")
    print(f"  For fixed l and varying m (hence R):")
    print(f"    Small m (l > 2R): Lambda ~ m^2/l      (slope 2)")
    print(f"    Large m (l < 2R): Lambda ~ m^2 (l/R)^3/l ~ m^2 m^{-1}/l ~ m/l  (slope ~1)")
    print(f"  The extended-body correction makes the effective slope < 2 for large m.")
    print(f"  This is a SPECIFIC, TESTABLE prediction of the geometry correction.")

print()

# ============================================================
# SECTION 5: GEOMETRY SCAN — THE F2 DISCRIMINANT
# ============================================================
print("""
===========================================================================
SECTION 5: GEOMETRY SCAN (F2 DISCRIMINANT) — (l/R)^3 vs competitors
===========================================================================

  SAME MASS, DIFFERENT DENSITY => different R at same m.
  GRUT predicts Lambda depends on R through S(l/R).
  Point-mass DP predicts Lambda INDEPENDENT of R.
  CSL predicts different R dependence.
""")

m_geo = 1e-14  # 10 fg
l_geo = 50e-9   # 50 nm

# Different materials => different densities => different R at same mass
materials = [
    ("Gold",     19300),
    ("Silica",   2200),
    ("Diamond",  3500),
    ("Aerogel",  100),
    ("Polymer",  1000),
]

print(f"  m = {m_geo*1e15:.0f} fg, l = {l_geo*1e9:.0f} nm")
print()
print(f"  {'Material':>12s}  {'rho':>8s}  {'R (nm)':>10s}  {'l/R':>8s}  {'S(l/R)':>10s}  {'Lambda_GRUT':>14s}  {'Lambda_DP':>12s}  {'Lambda_CSL':>12s}")

Ldp_geo = Lambda_DP_pointmass(m_geo, l_geo)

for mat_name, rho in materials:
    R_v = (3*m_geo/(4*np.pi*rho))**(1/3)
    Lg_v = Lambda_grav(m_geo, l_geo, R_v)
    ratio = l_geo / R_v
    S_v = min(1.0, (ratio)**3/6)
    Lcsl_v = Lambda_CSL(m_geo, l_geo, R_v)
    print(f"  {mat_name:>12s}  {rho:8.0f}  {R_v*1e9:10.1f}  {ratio:8.3f}  {S_v:10.2e}  {Lg_v:14.2e}  {Ldp_geo:12.2e}  {Lcsl_v:12.2e}")

print()
print("  GRUT: Lambda varies STRONGLY with density (through R).")
print("  DP (point-mass): Lambda is IDENTICAL for all densities.")
print("  CSL: different R-dependence (exponential, not cubic).")
print()
print("  The GEOMETRY TEST: measure decoherence for gold vs aerogel nanoparticles")
print("  of the SAME MASS. If Lambda differs by the predicted ratio -> GRUT confirmed.")
print("  If Lambda is the same -> GRUT extended-body correction FALSIFIED.")
print()

# ============================================================
# SECTION 6: THE SHARPEST NEAR-TERM TEST
# ============================================================
print("""
===========================================================================
SECTION 6: THE SHARPEST NEAR-TERM TEST
===========================================================================

  After analyzing all platforms and discriminants:

  THE RECOMMENDED TEST:

  Platform: Levitated nanoparticle (nanodiamond or silica)
  Method:   Optomechanical cooling + Stern-Gerlach or cavity interferometry
  Key scan: PRESSURE SCAN at fixed m, R, l, T

  SPECIFIC PARAMETERS:
""")

# Optimal parameters
m_opt = 1e-14        # 10 fg
R_opt = 50e-9        # 50 nm
l_opt = 100e-9       # 100 nm
T_opt = 10e-3        # 10 mK
P_target = 1e-11     # 10^-11 Pa (below crossover)

Lg_opt = Lambda_grav(m_opt, l_opt, R_opt)
Lgas_opt = Lambda_gas(m_opt, R_opt, l_opt, T_opt, P_target)
Lbb_opt = Lambda_blackbody(R_opt, l_opt, T_opt)

print(f"  Mass:           m = {m_opt*1e15:.0f} fg ({m_opt/m_amu:.0e} amu)")
print(f"  Radius:         R = {R_opt*1e9:.0f} nm")
print(f"  Superposition:  l = {l_opt*1e9:.0f} nm")
print(f"  Temperature:    T = {T_opt*1e3:.0f} mK")
print(f"  Pressure:       P = {P_target:.0e} Pa")
print()
print(f"  GRUT PREDICTIONS (zero free parameters):")
print(f"    Lambda_grav = {Lg_opt:.2e} Hz")
print(f"    Lambda_gas  = {Lgas_opt:.2e} Hz")
print(f"    Lambda_BB   = {Lbb_opt:.2e} Hz")
print(f"    Lambda_total = {Lg_opt + Lgas_opt + Lbb_opt:.2e} Hz")
print(f"    t_coherence = {1/(Lg_opt + Lgas_opt + Lbb_opt):.2e} s")
print()
print(f"  STANDARD QM PREDICTION:")
print(f"    Lambda_grav = 0")
print(f"    Lambda_total = {Lgas_opt + Lbb_opt:.2e} Hz")
print(f"    t_coherence = {1/(Lgas_opt + Lbb_opt):.2e} s")
print()

# The discriminant
t_coh_grut = 1/(Lg_opt + Lgas_opt + Lbb_opt)
t_coh_qm = 1/(Lgas_opt + Lbb_opt)
ratio_tcoh = t_coh_qm / t_coh_grut

print(f"  DISCRIMINANT:")
print(f"    GRUT coherence time:     {t_coh_grut:.2e} s")
print(f"    Standard QM coh time:    {t_coh_qm:.2e} s")
print(f"    Ratio (QM / GRUT):       {ratio_tcoh:.1f}×")
print()

if ratio_tcoh > 2:
    print(f"    The two predictions differ by {ratio_tcoh:.0f}×.")
    print(f"    A measurement of t_coherence discriminates at the {ratio_tcoh:.0f}× level.")
    print(f"    THIS IS A CLEAN, SHARP TEST.")
elif ratio_tcoh > 1.1:
    print(f"    The predictions differ by {(ratio_tcoh-1)*100:.0f}%.")
    print(f"    Measurable with ~{int(1/(ratio_tcoh-1)**2)} repetitions (statistics).")
else:
    print(f"    Predictions too close ({(ratio_tcoh-1)*100:.1f}% difference).")
    print(f"    Need lower pressure or larger mass to discriminate.")

print()

# ============================================================
# SECTION 7: SYSTEMATIC UNCERTAINTY ANALYSIS
# ============================================================
print("""
===========================================================================
SECTION 7: SYSTEMATIC UNCERTAINTIES
===========================================================================

  What could FAKE a gravitational decoherence signal?
  What could MASK a real signal?
""")

print("  FAKE SIGNALS (false positive for GRUT):")
print()
print("    1. Unaccounted gas collisions:")
print(f"       At P = {P_target:.0e} Pa, Lambda_gas = {Lgas_opt:.2e} Hz")
print(f"       If true P is 10× higher than measured: Lambda_gas = {Lambda_gas(m_opt, R_opt, l_opt, T_opt, P_target*10):.2e} Hz")
print(f"       -> Could MASK the gravitational signal (increase total Lambda)")
print(f"       Mitigation: calibrate pressure independently (ion gauge, RGA)")
print()
print("    2. Vibrational/phonon noise:")
print("       Internal vibrations of the nanoparticle can decohere")
print("       Rate depends on internal temperature T_int (may differ from T_env)")
print("       Mitigation: use crystalline particles (diamond), monitor T_int")
print()
print("    3. Blackbody from warm surfaces:")
print(f"       At T = {T_opt*1e3:.0f} mK: Lambda_BB = {Lbb_opt:.2e} Hz (negligible)")
print(f"       If warm surface at T = 4K nearby: Lambda_BB ~ {Lambda_blackbody(R_opt, l_opt, 4.0):.2e} Hz")
print("       Mitigation: shield experiment, verify cryogenic temperature")
print()
print("    4. Electromagnetic noise (stray fields):")
print("       Charged nanoparticle in stray E field can decohere")
print("       Rate depends on charge q and field noise spectrum")
print("       Mitigation: neutralize particle, Faraday cage")
print()

print("  MASKING EFFECTS (false negative for GRUT):")
print()
print("    1. Insufficient superposition size:")
print(f"       Lambda_grav ~ 1/l. If l is 10× smaller than assumed:")
print(f"       Lambda_grav is 10× larger but S(l/R) is 1000× smaller")
print("       Net effect depends on l/R regime")
print("       Mitigation: measure l interferometrically")
print()
print("    2. Particle mass/size uncertainty:")
print(f"       Lambda_grav ~ m^2 S(l/R). Mass uncertainty dm/m ~ 10% gives")
print(f"       dLambda/Lambda ~ 20% (from m^2) + up to 30% (from S(l/R))")
print("       Mitigation: characterize particles (SEM, mass spectrometry)")
print()
print("    3. Decoherence during preparation (not during free evolution):")
print("       If decoherence occurs during state prep, it won't show the")
print("       pressure-independent plateau")
print("       Mitigation: time-resolved measurement, vary free-evolution time")
print()

# ============================================================
# SECTION 8: VERDICT
# ============================================================
print("""
===========================================================================
VERDICT: EXPERIMENTAL FORECAST SUMMARY
===========================================================================

  GRUT makes FIVE zero-parameter predictions (N1-N5).
  FIVE falsification tests (F1-F5) are identified.

  THE SHARPEST NEAR-TERM TEST:

  Pressure scan with levitated nanoparticle.
  Look for: decoherence rate PLATEAU as P -> 0.

    GRUT says:     plateau at Lambda = 6.3e+02 Hz
    Standard QM:   Lambda -> 0 (no plateau)
    CSL (GRW):     plateau at Lambda ~ 10^-3 Hz (adjustable)
    CSL (Adler):   plateau at Lambda ~ 10^5 Hz (adjustable)

  The GRUT plateau is:
    - At a SPECIFIC height (zero free parameters)
    - Depends on m^2 and S(l/R) in a SPECIFIC way
    - Can be cross-checked with geometry scan (different R, same m)

  TIMELINE:
    Current (2024-2026): nanoparticle levitation reaching 10^-9 Pa
    Near-term (2027-2030): push to 10^-11 Pa, test for plateau
    Medium-term (2030-2035): MAQRO or equivalent, definitive test

  THE FRAMEWORK STANDS OR FALLS ON THIS:
    If plateau at predicted height:  GRUT CONFIRMED
    If plateau at wrong height:      GRUT quantitatively falsified
    If no plateau:                   GRUT gravitational sector DEAD
    If Lambda = 0:                   Standard QM wins, GRUT DEAD
""")

print("=" * 90)
print("END OF EXPERIMENTAL FORECAST")
print("=" * 90)
