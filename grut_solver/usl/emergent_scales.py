"""
Emergent timescales from the GRUT scaling hierarchy.

The USL gives t_coh = hbar * l / (G m^2 S(l/R)).
At different (m, l), this produces timescales spanning 10^-67 s to 10^+26 s.
The original GRUT "41.9 million year relaxation time" is NOT fundamental —
it is an emergent crossover timescale at a specific mass-separation scale.

This module computes where that timescale sits in the hierarchy and what
physical systems live there.
"""

import numpy as np
from grut_solver.constants import G, HBAR, AMU, K_B

TAU_COSMIC_S = 41.9e6 * 3.1557e7  # 41.9 Myr in seconds = 1.322e15 s
TAU_COSMIC_YR = 41.9e6


def mass_at_timescale(t_target: float, l: float) -> float:
    """What mass gives t_coherence = t_target at separation l?

    From t_coh = hbar l / (G m^2):
      m = sqrt(hbar l / (G t_target))

    Parameters
    ----------
    t_target : float   Target coherence time [s].
    l : float          Superposition separation [m].

    Returns
    -------
    float   Mass [kg] where the USL coherence time equals t_target.
    """
    if t_target <= 0 or l <= 0:
        return 0.0
    return np.sqrt(HBAR * l / (G * t_target))


def separation_at_timescale(t_target: float, m: float) -> float:
    """What separation gives t_coherence = t_target at mass m?

    From t_coh = hbar l / (G m^2):
      l = G m^2 t_target / hbar
    """
    if t_target <= 0 or m <= 0:
        return 0.0
    return G * m**2 * t_target / HBAR


def timescale_hierarchy() -> dict:
    """Compute the full hierarchy of emergent timescales from the USL.

    Returns a dict mapping physical regime -> (m, l, t_coh, description).
    """
    hierarchy = {}

    scales = [
        ("Planck",           np.sqrt(HBAR * G / 3e8**3) * 3e8 / G,  # ~Planck mass
                             np.sqrt(HBAR * G / 3e8**3)),              # Planck length
        ("proton",           1.67e-27, 1e-15),
        ("atom",             1e-25, 1e-10),
        ("small molecule",   1e-24, 1e-9),
        ("large molecule",   1e-22, 1e-7),
        ("protein",          1e-20, 1e-6),
        ("virus",            1e-17, 1e-7),
        ("nanoparticle",     1e-14, 1e-7),
        ("microsphere",      1e-9, 1e-5),
        ("dust grain",       1e-6, 1e-4),
        ("raindrop",         1e-3, 1e-3),
        ("baseball",         0.15, 0.01),
        ("human",            70, 0.1),
        ("Earth",            6e24, 1e7),
    ]

    for name, m, l in scales:
        t_coh = HBAR * l / (G * m**2) if m > 0 else float('inf')
        t_yr = t_coh / 3.1557e7

        if t_yr > 1e15:
            t_str = f"{t_yr:.1e} yr"
        elif t_yr > 1e6:
            t_str = f"{t_yr/1e6:.1f} Myr"
        elif t_yr > 1:
            t_str = f"{t_yr:.1f} yr"
        elif t_coh > 1:
            t_str = f"{t_coh:.1f} s"
        elif t_coh > 1e-3:
            t_str = f"{t_coh*1e3:.1f} ms"
        else:
            t_str = f"{t_coh:.1e} s"

        hierarchy[name] = {
            "m_kg": m, "m_amu": m/AMU, "l_m": l,
            "t_coh_s": t_coh, "t_coh_yr": t_yr, "t_str": t_str,
        }

    return hierarchy


def locate_41_9_myr() -> dict:
    """Where does the original GRUT 41.9 Myr timescale live in the USL?

    Computes the mass-separation locus where t_coh = 41.9 Myr.
    This is NOT a fundamental parameter — it is the crossover point
    where gravitational decoherence takes cosmological time.

    Returns
    -------
    dict with:
      - mass_at_various_l: mass needed at each separation to get 41.9 Myr
      - separation_at_various_m: separation needed at each mass
      - physical_interpretation: what lives at this scale
    """
    t_target = TAU_COSMIC_S

    # Mass at various separations
    l_values = [1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1.0]
    mass_table = []
    for l in l_values:
        m = mass_at_timescale(t_target, l)
        mass_table.append({
            "l_m": l,
            "m_kg": m,
            "m_amu": m / AMU,
        })

    # Separation at various masses
    m_values = [1e-25, 1e-23, 1e-21, 1e-19, 1e-17, 1e-15, 1e-13, 1e-11]
    sep_table = []
    for m in m_values:
        l = separation_at_timescale(t_target, m)
        sep_table.append({
            "m_kg": m,
            "m_amu": m / AMU,
            "l_m": l,
        })

    # The "sweet spot" at l ~ 1 um
    m_sweet = mass_at_timescale(t_target, 1e-6)

    return {
        "t_target_s": t_target,
        "t_target_yr": TAU_COSMIC_YR,
        "mass_at_l": mass_table,
        "l_at_mass": sep_table,
        "sweet_spot": {
            "l": 1e-6,
            "m_kg": m_sweet,
            "m_amu": m_sweet / AMU,
            "description": (
                f"At l = 1 um, the 41.9 Myr timescale corresponds to "
                f"m = {m_sweet/AMU:.0f} amu (~{m_sweet*1e23:.1f}×10^-23 kg). "
                f"This is the mass of a large protein or small virus — "
                f"the scale where gravitational decoherence takes geological time. "
                f"Below this mass: quantum coherence persists for longer than the "
                f"age of the universe. Above it: decoherence is rapid."
            ),
        },
        "interpretation": (
            "The 41.9 Myr timescale is NOT fundamental. It is the emergent "
            "crossover where gravitational decoherence transitions from "
            "'effectively never' (quantum regime) to 'fast' (classical regime) "
            "at the macromolecular scale. It marks the boundary between "
            "systems that can maintain quantum coherence on cosmological "
            "timescales and those that cannot."
        ),
    }


if __name__ == "__main__":
    print("=" * 80)
    print("EMERGENT TIMESCALE HIERARCHY FROM THE USL")
    print("=" * 80)
    print()

    hierarchy = timescale_hierarchy()
    print(f"  {'System':>18s}  {'m (kg)':>12s}  {'m (amu)':>12s}  {'l (m)':>10s}  {'t_coh':>16s}")
    print(f"  {'-'*18}  {'-'*12}  {'-'*12}  {'-'*10}  {'-'*16}")
    for name, data in hierarchy.items():
        print(f"  {name:>18s}  {data['m_kg']:12.2e}  {data['m_amu']:12.2e}  {data['l_m']:10.2e}  {data['t_str']:>16s}")

    print()
    print("=" * 80)
    print("WHERE IS THE 41.9 MILLION YEAR TIMESCALE?")
    print("=" * 80)
    print()

    result = locate_41_9_myr()

    print(f"  t_target = {result['t_target_yr']:.1f} Myr = {result['t_target_s']:.3e} s")
    print()
    print(f"  Mass needed for t_coh = 41.9 Myr at various l:")
    print(f"  {'l (m)':>10s}  {'m (kg)':>12s}  {'m (amu)':>12s}  {'equivalent':>20s}")
    for entry in result["mass_at_l"]:
        m_amu = entry["m_amu"]
        if m_amu < 1e3:
            equiv = f"~{m_amu:.0f} amu (atom)"
        elif m_amu < 1e6:
            equiv = f"~{m_amu:.0f} amu (molecule)"
        elif m_amu < 1e9:
            equiv = f"~{m_amu/1e6:.1f} MDa (protein)"
        elif m_amu < 1e12:
            equiv = f"~{m_amu/1e9:.1f} GDa (virus)"
        else:
            equiv = f"~{m_amu/1e12:.1f} TDa (cell)"
        print(f"  {entry['l_m']:10.0e}  {entry['m_kg']:12.2e}  {m_amu:12.0f}  {equiv:>20s}")

    print()
    print(f"  SWEET SPOT:")
    print(f"  {result['sweet_spot']['description']}")
    print()
    print(f"  INTERPRETATION:")
    print(f"  {result['interpretation']}")
    print()

    # The hierarchy of tau
    print("=" * 80)
    print("THE COMPLETE tau HIERARCHY")
    print("=" * 80)
    print()
    print("  Scale              | tau                | Meaning")
    print("  -------------------|--------------------|---------------------------------")
    print(f"  Planck             | {5.39e-44:.2e} s     | Minimum meaningful time")
    print(f"  tau_I = hbar/2     | {HBAR/2:.2e} s     | Quantum phase oscillation")
    print(f"  Atomic t_coh       | ~10^+18 yr         | Grav decoh of atom (unobservable)")
    print(f"  41.9 Myr crossover | {TAU_COSMIC_S:.2e} s | Macro-molecular boundary")
    print(f"  Lab t_coh (10pg)   | ~1.6 ms            | Current experimental target")
    print(f"  Human t_coh        | ~3×10^-29 s        | Instantly classical")
    print(f"  Earth t_coh        | ~4×10^-67 s        | Overwhelmingly classical")
    print()
    print("  The 41.9 Myr sits precisely at the boundary between:")
    print("    'quantum coherence persists on cosmological timescales'")
    print("    'gravitational decoherence is fast enough to matter'")
    print("  It is the EMERGENCE SCALE — not fundamental, but structurally meaningful.")
