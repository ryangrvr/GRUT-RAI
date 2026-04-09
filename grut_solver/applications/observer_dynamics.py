"""
Application 4: Observer Dynamics — Decoherence as Measurement

THE QUESTION: When does a quantum superposition become "measured"?

GRUT ANSWER: When the total decoherence rate Lambda_total exceeds
the inverse observation time: Lambda * t > 1. This is not a new
measurement postulate — it is the standard decoherence program
with GRUT providing the gravitational channel that standard QM lacks.

THE DOUBLE-SLIT CONNECTION: In a double-slit experiment, "which-path
information" is acquired when the environment (or gravity) decoheres
the particle faster than the interference pattern forms. The fringe
visibility V = exp(-Lambda * t_flight) quantifies this.

This application computes: for any object mass, what is the decoherence
time from gravity alone? From environment? When does "measurement" occur?
"""

import numpy as np
from grut_solver.constants import G, HBAR, AMU, K_B, M_ELECTRON
from grut_solver.usl.gravitational import lambda_grav, boundary_mass


def measurement_timescale(m: float, l: float, R: float = None,
                           T_env: float = 300.0, P: float = 1e5) -> dict:
    """Compute all decoherence timescales for an object.

    Returns the time at which each channel "measures" the superposition
    (i.e., Lambda * t ~ 1 => t ~ 1/Lambda).
    """
    from grut_solver.budget.gas import lambda_gas
    from grut_solver.budget.blackbody import lambda_bb_scatter

    Lg = lambda_grav(m, l, R)
    Lgas = lambda_gas(m, R if R else 1e-10, l, T_env, P)
    Lbb = lambda_bb_scatter(R if R else 1e-10, l, T_env)
    L_total = Lg + Lgas + Lbb

    def safe_inv(x):
        return 1.0/x if x > 0 else float('inf')

    return {
        "m_kg": m,
        "l_m": l,
        "t_grav": safe_inv(Lg),
        "t_gas": safe_inv(Lgas),
        "t_bb": safe_inv(Lbb),
        "t_total": safe_inv(L_total),
        "lambda_grav": Lg,
        "lambda_gas": Lgas,
        "lambda_total": L_total,
        "fastest_channel": (
            "gravity" if Lg > max(Lgas, Lbb)
            else "gas" if Lgas > Lbb
            else "blackbody"
        ),
        "gravity_dominant": Lg > (Lgas + Lbb),
    }


def observer_hierarchy() -> list[dict]:
    """Compute measurement timescales for objects from electrons to planets.

    This IS the quantum-classical boundary — computed, not postulated.
    At each scale, the fastest decoherence channel determines when
    "measurement" (loss of coherence) occurs.
    """
    M_SUN = 1.989e30
    systems = [
        ("Electron",         M_ELECTRON,   1e-10,  1e-15,  300, 1e5),
        ("Hydrogen atom",    1.67e-27,     1e-10,  5.3e-11, 300, 1e5),
        ("C60 molecule",     1.2e-24,      1e-9,   3.5e-10, 300, 1e-7),
        ("Protein (100 kDa)", 1.66e-22,    1e-6,   5e-9,   310, 1e5),
        ("Virus",            1e-17,        1e-7,   50e-9,  300, 1e5),
        ("Bacterium",        1e-15,        1e-6,   500e-9, 300, 1e5),
        ("Dust grain",       1e-12,        1e-5,   1e-6,   300, 1e5),
        ("Grain of sand",    1e-6,         1e-4,   50e-6,  300, 1e5),
        ("Baseball",         0.145,        0.01,   0.037,  300, 1e5),
        ("Human",            70,           0.1,    0.25,   300, 1e5),
        ("Earth",            5.97e24,      1e7,    6.37e6, 2.7, 0),
        ("Sun",              M_SUN,        1e9,    6.96e8, 2.7, 0),
    ]

    results = []
    for name, m, l, R, T, P in systems:
        r = measurement_timescale(m, l, R, T, P)
        r["name"] = name
        results.append(r)

    return results


def double_slit_which_path(m: float, l_slit: float, R: float,
                            v_particle: float) -> dict:
    """The double-slit as an observer problem.

    A particle passing through a double slit acquires a spatial
    superposition of size l_slit. The "which-path" information is
    acquired when decoherence destroys the interference pattern.

    In vacuum (no gas, no photons): only gravitational decoherence acts.
    The fringe contrast is V = exp(-Lambda_grav * t_transit)
    where t_transit ~ l_slit / v_particle (time to cross one fringe).
    """
    t_transit = l_slit / v_particle if v_particle > 0 else float('inf')
    Lg = lambda_grav(m, l_slit, R)

    V_grav = np.exp(-Lg * t_transit)

    return {
        "m_kg": m,
        "l_slit_m": l_slit,
        "v_m_s": v_particle,
        "t_transit_s": t_transit,
        "lambda_grav_hz": Lg,
        "V_grav": V_grav,
        "which_path_acquired": V_grav < 0.5,
        "interpretation": (
            f"Gravitational which-path: V = {V_grav:.6f}. "
            f"{'Fringes destroyed by gravity.' if V_grav < 0.5 else 'Fringes preserved — gravity too slow.'}"
        ),
    }


def schrodinger_cat_decoherence() -> dict:
    """The Schrodinger cat thought experiment, computed.

    A cat (m ~ 4 kg) in a superposition of "alive" (position A) and
    "dead" (position B) separated by l ~ 10 cm.

    How fast does each channel "measure" the cat?
    """
    m_cat = 4.0
    l_cat = 0.1  # 10 cm
    R_cat = 0.15  # ~15 cm radius

    r = measurement_timescale(m_cat, l_cat, R_cat, T_env=300, P=1e5)
    r["name"] = "Schrodinger's Cat"
    r["interpretation"] = (
        f"Gravitational decoherence time: {r['t_grav']:.2e} s. "
        f"Air collision decoherence time: {r['t_gas']:.2e} s. "
        f"The cat is 'measured' (decohered) in {r['t_total']:.2e} s — "
        f"far faster than any biological process. The superposition "
        f"is destroyed essentially instantaneously."
    )
    return r


if __name__ == "__main__":
    print("=" * 80)
    print("APPLICATION 4: OBSERVER DYNAMICS — DECOHERENCE AS MEASUREMENT")
    print("=" * 80)

    # Observer hierarchy
    print("\n1. THE MEASUREMENT HIERARCHY")
    print("-" * 70)
    print(f"  {'System':>20s}  {'m (kg)':>10s}  {'t_grav':>12s}  {'t_gas':>12s}  "
          f"{'t_total':>12s}  {'fastest':>10s}")

    hierarchy = observer_hierarchy()
    for r in hierarchy:
        def fmt_time(t):
            if t > 3.15e16:
                return f"{t/3.15e7:.0e} yr"
            elif t > 1:
                return f"{t:.2e} s"
            elif t > 1e-3:
                return f"{t*1e3:.1f} ms"
            elif t > 1e-6:
                return f"{t*1e6:.1f} us"
            else:
                return f"{t:.2e} s"

        print(f"  {r['name']:>20s}  {r['m_kg']:10.2e}  {fmt_time(r['t_grav']):>12s}  "
              f"{fmt_time(r['t_gas']):>12s}  {fmt_time(r['t_total']):>12s}  "
              f"{r['fastest_channel']:>10s}")

    # Schrodinger's cat
    print("\n2. SCHRODINGER'S CAT")
    print("-" * 70)
    cat = schrodinger_cat_decoherence()
    print(f"  {cat['interpretation']}")

    # Double-slit which-path
    print("\n3. DOUBLE-SLIT WHICH-PATH (gravitational only, perfect vacuum)")
    print("-" * 70)

    for name, m, l, R, v in [
        ("Electron",     M_ELECTRON,  1e-6,  1e-15,  1e6),
        ("Neutron",      1.67e-27,    1e-6,  1e-15,  1e3),
        ("C60",          1.2e-24,     1e-7,  3.5e-10, 200),
        ("10^6 amu",     1.66e-21,    1e-7,  5e-9,    10),
        ("10^9 amu",     1.66e-18,    1e-7,  1e-7,    1),
        ("10 pg",        1e-14,       1e-7,  5e-8,    0.1),
    ]:
        ds = double_slit_which_path(m, l, R, v)
        print(f"  {name:>12s}: V = {ds['V_grav']:.6f}  "
              f"Lambda = {ds['lambda_grav_hz']:.2e} Hz  "
              f"{'FRINGES GONE' if ds['which_path_acquired'] else 'fringes OK'}")

    # The key point
    print("\n4. THE KEY INSIGHT")
    print("-" * 70)
    print("""
  GRUT computes WHEN a system loses coherence. This IS the measurement
  problem in the decoherence framework:

  - For electrons: gravity is irrelevant (t_grav ~ 10^26 yr)
  - For molecules: gravity is negligible (t_grav ~ 10^15 yr)
  - For nanoparticles (10 pg): gravity acts in milliseconds
  - For cats: gravity acts in 10^-28 s (and air acts even faster)

  The "observer" is the fastest decoherence channel.
  At microscopic scales: the environment is the observer.
  At macroscopic scales: gravity alone would suffice.

  There is no sharp boundary — the transition is smooth, computed
  from the USL and environmental channels, with zero free parameters.
""")
