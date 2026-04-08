#!/usr/bin/env python3
"""
GRUT Double-Slit Derivation

What the GRUT framework actually predicts for the double slit.

The setup:
  A particle of mass m passes through two slits separated by d.
  It propagates distance L to a detection screen.
  Standard QM predicts interference fringes with spacing lambda_fringe = lambda_dB * L / d.

GRUT adds:
  The particle propagates through a fluctuating METRIC (not just empty space).
  The metric fluctuations have two sources:
    1. Newtonian gravitational self-energy (tree-level USL)
    2. Anomaly-induced 1/k^4 noise (3-loop, coefficient C_Final)

  These fluctuations introduce a RANDOM PHASE between the two paths.
  The random phase REDUCES the visibility of the interference fringes.

The GRUT double-slit prediction:
  P(x) = |psi_1|^2 + |psi_2|^2 + 2 V(d,m,t) Re[psi_1* psi_2]

  where V is the VISIBILITY (fringe contrast), modified by gravitational decoherence.

This derivation imports:
  - The superposition principle (quantum: NOT derived from GRUT)
  - The de Broglie wavelength lambda = h/p (quantum: NOT derived)
  - The Born rule |psi|^2 (quantum: NOT derived, per N3)
  - The CTP influence functional (GRUT-derived: Iota-Prime)
  - The gravitational decoherence rate (GRUT: USL + anomaly)

What GRUT ADDS to the standard double slit:
  The mass-dependent, separation-dependent VISIBILITY FUNCTION V(d, m, t)
  that determines when and how the fringes disappear.
"""

import numpy as np
from scipy.special import zeta

# ============================================================
# CONSTANTS
# ============================================================
G = 6.67430e-11       # m^3 kg^-1 s^-2
hbar = 1.05457e-34    # J s
h = 2 * np.pi * hbar
c = 2.99792e8         # m/s
k_B = 1.38065e-23     # J/K
m_e = 9.10938e-31     # electron mass, kg
amu = 1.66054e-27     # kg

# C_Final (from M0/M3)
pi = np.pi
z3 = zeta(3)
ln2 = np.log(2)
C_Final = 3*(99 + 2*pi**2 + 576*ln2*z3) / (16384*pi**6)
kappa = np.sqrt(32 * pi * G / c**4)
C_0_anomaly = C_Final * kappa**4 / (4*pi*hbar**2)

print("=" * 90)
print("THE GRUT DOUBLE-SLIT PREDICTION")
print("=" * 90)

# ============================================================
# PART 1: THE STANDARD DOUBLE SLIT (what QM gives)
# ============================================================
print(f"\n{'='*90}")
print("PART 1: STANDARD QUANTUM MECHANICS (imported, not derived)")
print("=" * 90)

print(f"""
  A particle of mass m, momentum p = m v, passes through two slits
  separated by distance d, then hits a screen at distance L.

  de Broglie wavelength: lambda = h / p
  Fringe spacing: Delta_x = lambda * L / d
  Intensity pattern:

    I(x) = I_0 [1 + cos(2 pi d x / (lambda L))]

  This comes from the superposition of two spherical waves:
    psi_total = psi_1 + psi_2
    |psi_total|^2 = |psi_1|^2 + |psi_2|^2 + 2 Re[psi_1* psi_2]

  The cross term 2 Re[psi_1* psi_2] produces the fringes.
  Without it: uniform illumination (classical).
  With it: interference pattern (quantum).

  GRUT does NOT derive this. It imports it from quantum mechanics.
  The superposition principle, the complex amplitudes, and the Born rule
  are UPSTREAM of the constitutive sector (N3).
""")

# ============================================================
# PART 2: WHAT GRUT ADDS — GRAVITATIONAL VISIBILITY
# ============================================================
print(f"{'='*90}")
print("PART 2: WHAT GRUT ADDS — THE VISIBILITY FUNCTION")
print("=" * 90)

print(f"""
  In GRUT, the particle does not propagate through empty space.
  It propagates through a fluctuating metric — the gravitational
  vacuum has stochastic fluctuations from two sources:

  SOURCE 1 (Newtonian, tree-level):
    The particle's own gravitational field creates a self-energy
    difference Delta_E between the two paths (through slit 1 vs slit 2).
    This produces a dephasing rate:
      Gamma_N = G m^2 / (hbar d)   [for d > 2R, point-mass regime]

  SOURCE 2 (Anomaly, 3-loop):
    The 1/k^4 gravitational noise kernel (from C_Final) produces
    additional metric fluctuations that decohere the two paths:
      Gamma_A = C_0 m^2 d   [from the noise integral]

  The TOTAL gravitational decoherence rate:
    Gamma_total(d, m) = G m^2 / (hbar d) + C_0 m^2 d

  The VISIBILITY (fringe contrast) after propagation time t:
    V(d, m, t) = exp(-Gamma_total * t)

  The GRUT double-slit intensity pattern:
    I(x) = I_0 [1 + V(d,m,t) cos(2 pi d x / (lambda L))]

  When V = 1: full quantum interference (standard QM)
  When V = 0: no fringes (classical, fully decohered)
  When 0 < V < 1: partial fringes (GRUT regime)
""")

def Gamma_Newtonian(m, d):
    """Newtonian gravitational dephasing rate."""
    return G * m**2 / (hbar * d)

def Gamma_anomaly(m, d):
    """Anomaly-induced noise decoherence rate."""
    return C_0_anomaly * m**2 * d

def Gamma_total(m, d):
    """Total gravitational decoherence rate."""
    return Gamma_Newtonian(m, d) + Gamma_anomaly(m, d)

def Visibility(m, d, t):
    """Fringe visibility after time t."""
    return np.exp(-Gamma_total(m, d) * t)

def fringe_spacing(m, v, d, L):
    """Interference fringe spacing on screen."""
    lam = h / (m * v)
    return lam * L / d

# ============================================================
# PART 3: COMPUTE FOR SPECIFIC EXPERIMENTS
# ============================================================
print(f"{'='*90}")
print("PART 3: PREDICTIONS FOR SPECIFIC EXPERIMENTS")
print("=" * 90)

experiments = [
    ("Electron (Tonomura 1989)",
     m_e, 1e6, 0.5e-6, 1.0, 0.35e-3,
     "Classic electron double slit"),
    ("C60 fullerene (Arndt 1999)",
     60*12*amu, 200, 100e-9, 1.25, 1e-3,
     "First large-molecule interference"),
    ("25 kDa molecule (Fein 2019)",
     25000*amu, 10, 266e-9, 2.0, 7e-3,
     "Current record: large organic molecules"),
    ("170 kDa Na cluster (Arndt 2026)",
     170000*amu, 5, 100e-9, 1.0, 10e-3,
     "Current macroscopicity record"),
    ("1 fg nanosphere (proposed)",
     1e-18, 0.1, 500e-9, 0.5, 0.1,
     "Near-future levitated nanoparticle"),
    ("196 fg nanodiamond (GRUT target)",
     196e-18, 0.01, 474e-9, 0.1, 5.0,
     "GRUT corrected operating point (Mu-Prime)"),
    ("1 ug dust grain (thought experiment)",
     1e-9, 0.001, 1e-6, 1.0, 1.0,
     "Macroscopic regime"),
]

print(f"\n  {'Experiment':<35s} {'m (kg)':>12s} {'d (nm)':>8s} {'Gamma_N':>12s} {'Gamma_A':>12s} {'V (t)':>10s} {'Fringes?':>10s}")
print(f"  {'-'*35} {'-'*12} {'-'*8} {'-'*12} {'-'*12} {'-'*10} {'-'*10}")

for name, m, v, d, L, t, desc in experiments:
    GN = Gamma_Newtonian(m, d)
    GA = Gamma_anomaly(m, d)
    V = Visibility(m, d, t)
    lam_dB = h / (m * v)

    if V > 0.99:
        fringes = "FULL"
    elif V > 0.5:
        fringes = "PARTIAL"
    elif V > 0.01:
        fringes = "FADING"
    else:
        fringes = "GONE"

    print(f"  {name:<35s} {m:12.2e} {d*1e9:8.0f} {GN:12.4e} {GA:12.4e} {V:10.6f} {fringes:>10s}")

# ============================================================
# PART 4: THE FULL PATTERN
# ============================================================
print(f"\n{'='*90}")
print("PART 4: THE GRUT DOUBLE-SLIT INTENSITY PATTERN")
print("=" * 90)

# Compute and display the pattern for key cases
print(f"\n  The GRUT intensity pattern:")
print(f"    I(x) = I_0 [1 + V(d,m,t) cos(2 pi d x / (lambda L))]")
print(f"    where V = exp(-[G m^2/(hbar d) + C_0 m^2 d] t)")
print()

# For each case, show the key numbers
for name, m, v, d, L, t, desc in experiments[:4]:
    GN = Gamma_Newtonian(m, d)
    V = Visibility(m, d, t)
    lam_dB = h / (m * v)
    dx_fringe = lam_dB * L / d

    print(f"  {name}:")
    print(f"    lambda_dB = {lam_dB:.4e} m")
    print(f"    fringe spacing = {dx_fringe:.4e} m = {dx_fringe*1e6:.2f} um")
    print(f"    Gamma_total = {Gamma_total(m, d):.4e} s^-1")
    print(f"    Visibility V = {V:.8f}")
    print(f"    Gravitational fringe reduction: {(1-V)*100:.2e}%")
    print()

# ============================================================
# PART 5: WHAT GRUT UNIQUELY PREDICTS
# ============================================================
print(f"{'='*90}")
print("PART 5: WHAT GRUT UNIQUELY PREDICTS")
print("=" * 90)

print(f"""
  Standard QM predicts: perfect interference for any mass (V = 1 always).
  Environmental decoherence (gas, photons) reduces V depending on environment.

  GRUT predicts: an IRREDUCIBLE gravitational visibility reduction that depends
  ONLY on the mass, slit separation, and propagation time — not on the environment.

  The GRUT visibility function:
    V(d, m, t) = exp(-[G m^2/(hbar d) + C_0 m^2 d] t)

  This has a MINIMUM in d (maximum decoherence) at:
    d_min = sqrt(G / (hbar C_0)) = {np.sqrt(G/(hbar*C_0_anomaly)):.2e} m

  For d < d_min: Newtonian dephasing dominates (V decreases as d decreases)
  For d > d_min: anomaly noise dominates (V decreases as d increases)

  THE THREE REGIMES OF THE GRUT DOUBLE SLIT:

  1. QUANTUM REGIME (V ~ 1):
     m << m_threshold(d, t). Gravitational decoherence is negligible.
     Full interference fringes. Standard QM applies.
     Example: electrons, atoms, molecules up to ~10^5 amu.

  2. TRANSITION REGIME (0.01 < V < 0.99):
     m ~ m_threshold. Gravitational decoherence is MEASURABLE.
     Fringes are present but REDUCED in contrast.
     This is where GRUT makes a TESTABLE prediction that differs
     from standard QM (which predicts V = 1 with no gravitational effect).
     Example: nanoparticles in the 10^6 - 10^10 amu range.

  3. CLASSICAL REGIME (V ~ 0):
     m >> m_threshold. Gravitational decoherence destroys all fringes.
     No interference. Classical behavior.
     Example: dust grains, baseballs, planets.
""")

# Compute the threshold mass for V = 0.5 at various d and t
print(f"  THRESHOLD MASS for V = 0.5 (50% visibility):")
print(f"  (Newtonian channel only: m_threshold = sqrt(ln(2) hbar d / (G t)))")
print()
print(f"  {'d (nm)':>8s} {'t (s)':>8s} {'m_thresh (kg)':>14s} {'m_thresh (amu)':>14s}")
print(f"  {'-'*8} {'-'*8} {'-'*14} {'-'*14}")

for d_nm in [100, 500, 1000]:
    for t_val in [0.001, 0.01, 0.1, 1.0]:
        d_val = d_nm * 1e-9
        # Gamma_N * t = ln(2) for V = 0.5
        # G m^2 t / (hbar d) = ln(2)
        m_thresh = np.sqrt(np.log(2) * hbar * d_val / (G * t_val))
        print(f"  {d_nm:8d} {t_val:8.3f} {m_thresh:14.4e} {m_thresh/amu:14.2e}")

# ============================================================
# PART 6: THE COMPLETE GRUT DOUBLE-SLIT EQUATION
# ============================================================
print(f"\n{'='*90}")
print("PART 6: THE COMPLETE GRUT DOUBLE-SLIT EQUATION")
print("=" * 90)

print(f"""
  THE GRUT DOUBLE-SLIT EQUATION:

  I(x, d, m, t) = I_0 {{ 1 + exp(-Gamma(d,m) t) cos(2 pi d x / (lambda L)) }}

  where:
    Gamma(d, m) = G m^2 / (hbar d) + C_0 m^2 d

  with:
    G = {G:.5e} m^3 kg^-1 s^-2  (Newton)
    hbar = {hbar:.5e} J s  (Planck, imported)
    C_0 = C_Final * kappa^4 / (4 pi hbar^2) = {C_0_anomaly:.4e} kg^-2 m^-1 s^-1  (anomaly)
    C_Final = {C_Final:.6e}  (3-loop SM+gravity anomaly coefficient)
    lambda = h / (m v)  (de Broglie, imported)

  WHAT IS DERIVED FROM GRUT:
    1. The Gamma(d,m) decoherence rate — from the CTP influence functional
       (Iota-Prime: tree-level gravitational self-energy dephasing)
    2. The C_0 anomaly correction — from C_Final (M0: 3-loop anomaly)
    3. The extended-body correction for d < 2R — from the Diosi integral
       (Kappa-Prime)
    4. The visibility function V = exp(-Gamma t) — from the CTP noise sector

  WHAT IS IMPORTED FROM QUANTUM MECHANICS:
    1. The superposition principle (psi = psi_1 + psi_2)
    2. The Born rule (I = |psi|^2)
    3. The de Broglie wavelength (lambda = h/p)
    4. The value of hbar (irreducible input, per L1)

  WHAT IS UNIQUELY GRUT:
    The GRAVITATIONAL decoherence function Gamma(d,m) is the GRUT-specific
    contribution. It predicts that interference fringes have a mass-dependent,
    separation-dependent contrast that is IRREDUCIBLE — it cannot be removed
    by improving the vacuum, lowering the temperature, or shielding the
    experiment. It is a consequence of the particle's own gravitational
    self-interaction through the CTP influence functional.

    This is the GRUT prediction for the double slit:
    gravity sets a fundamental limit on quantum interference.
""")

print("=" * 90)
print("END")
print("=" * 90)
