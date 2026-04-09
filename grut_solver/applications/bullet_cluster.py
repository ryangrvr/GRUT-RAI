"""
Application 3: Bullet Cluster Lensing Analysis

THE QUESTION: Does GRUT's constitutive field produce any detectable
lensing signature beyond standard GR + dark matter in the Bullet Cluster?

THE HONEST ANSWER (from Sector 4): The weak-field correction is
delta_beta ~ 10^-16 (observationally silent at all physical tau).
So: NO detectable GRUT-specific lensing modification.

WHAT THIS APPLICATION DOES:
1. Computes the GRUT gravitational decoherence rate for Bullet-Cluster-scale masses
2. Computes the quantum-classical boundary at cluster scales
3. Shows that cluster-scale objects are overwhelmingly classical
4. Documents the null result: GRUT adds nothing to cluster lensing beyond GR
"""

import numpy as np
from grut_solver.constants import G, HBAR, AMU
from grut_solver.usl.gravitational import lambda_grav, boundary_mass


# ── Bullet Cluster parameters ───────────────────────────────

# 1E 0657-56 "Bullet Cluster" (Clowe et al. 2006)
M_SUN = 1.989e30  # kg

BULLET_CLUSTER = {
    "name": "1E 0657-56 (Bullet Cluster)",
    "ref": "Clowe et al., ApJ 648, L109 (2006)",
    "M_main_cluster": 1.5e15 * M_SUN,      # ~1.5 x 10^15 solar masses
    "M_sub_cluster": 1.5e14 * M_SUN,       # ~1.5 x 10^14 solar masses
    "separation_Mpc": 0.72,                  # ~720 kpc projected
    "separation_m": 0.72 * 3.086e22,        # in meters
    "R_main_Mpc": 1.0,                      # ~1 Mpc virial radius
    "R_main_m": 1.0 * 3.086e22,
    "R_sub_Mpc": 0.3,
    "R_sub_m": 0.3 * 3.086e22,
    "v_collision_km_s": 4700,                # ~4700 km/s
    "z_redshift": 0.296,
}

# Individual galaxy parameters (for sub-cluster galaxy)
TYPICAL_GALAXY = {
    "name": "Typical cluster galaxy",
    "M_kg": 1e11 * M_SUN,                   # ~10^11 solar masses
    "R_m": 30e3 * 3.086e16,                 # ~30 kpc in meters
    "l_superposition_m": 1.0,                # hypothetical 1 m superposition
}


def cluster_decoherence_rates() -> dict:
    """Compute gravitational decoherence rates at cluster scales.

    These are formal USL evaluations. At cluster masses, the decoherence
    rate is enormous — these objects are overwhelmingly classical.
    """
    bc = BULLET_CLUSTER
    results = {}

    # Main cluster
    m = bc["M_main_cluster"]
    l = bc["separation_m"]
    R = bc["R_main_m"]
    Lg = lambda_grav(m, l, R)
    results["main_cluster"] = {
        "m_kg": m, "m_solar": m / M_SUN,
        "l_m": l, "R_m": R,
        "lambda_grav_hz": Lg,
        "t_decoherence_s": 1/Lg if Lg > 0 else float('inf'),
        "regime": "overwhelmingly classical",
    }

    # Sub-cluster
    m2 = bc["M_sub_cluster"]
    R2 = bc["R_sub_m"]
    Lg2 = lambda_grav(m2, l, R2)
    results["sub_cluster"] = {
        "m_kg": m2, "m_solar": m2 / M_SUN,
        "l_m": l, "R_m": R2,
        "lambda_grav_hz": Lg2,
        "t_decoherence_s": 1/Lg2 if Lg2 > 0 else float('inf'),
    }

    # Typical galaxy
    gal = TYPICAL_GALAXY
    Lg3 = lambda_grav(gal["M_kg"], gal["l_superposition_m"], gal["R_m"])
    results["galaxy"] = {
        "m_kg": gal["M_kg"], "m_solar": gal["M_kg"] / M_SUN,
        "l_m": gal["l_superposition_m"],
        "lambda_grav_hz": Lg3,
        "t_decoherence_s": 1/Lg3 if Lg3 > 0 else float('inf'),
    }

    return results


def cluster_quantum_classical_boundary() -> dict:
    """Compute the quantum-classical boundary at cluster scales.

    For the Bullet Cluster separation (~720 kpc) and observation time (~1 Gyr):
    m* = sqrt(hbar l / (G t)). Any mass above m* is classical.
    """
    l = BULLET_CLUSTER["separation_m"]
    t_obs = 1e9 * 3.156e7  # 1 Gyr in seconds

    m_star = boundary_mass(l, t_obs)

    return {
        "l_m": l,
        "t_obs_s": t_obs,
        "m_boundary_kg": m_star,
        "m_boundary_solar": m_star / M_SUN,
        "m_boundary_amu": m_star / AMU,
        "note": (
            f"Any object heavier than {m_star:.2e} kg ({m_star/M_SUN:.2e} solar masses) "
            f"is gravitationally classical at this separation over 1 Gyr. "
            f"Galaxy clusters are ~10^15 solar masses. They are classical by "
            f"a factor of ~10^{np.log10(BULLET_CLUSTER['M_main_cluster']/m_star):.0f}."
        ),
    }


def lensing_modification() -> dict:
    """Assess whether GRUT modifies Bullet Cluster lensing.

    From Sector 4: weak-field correction delta_beta ~ 10^-16.
    """
    return {
        "weak_field_correction": 1e-16,
        "detectable": False,
        "lensing_modified": False,
        "note": (
            "GRUT's constitutive field produces a weak-field metric correction "
            "of order 10^-16 at all physical tau values. This is completely "
            "undetectable in any lensing observation. The Bullet Cluster's "
            "mass-light offset remains a standard GR + dark matter result. "
            "GRUT adds nothing to cluster lensing beyond GR."
        ),
        "dark_matter_status": (
            "The Bullet Cluster's separation of baryonic mass (X-ray gas) "
            "from total mass (lensing) is evidence for dark matter or a "
            "modification of gravity. GRUT does not provide either: it has "
            "no dark-matter candidate (Sector 9: Open) and no gravity "
            "modification (Sector 4: matter within GR)."
        ),
    }


def full_analysis() -> dict:
    """Complete Bullet Cluster analysis."""
    return {
        "decoherence": cluster_decoherence_rates(),
        "boundary": cluster_quantum_classical_boundary(),
        "lensing": lensing_modification(),
        "verdict": (
            "The Bullet Cluster is overwhelmingly classical by GRUT's "
            "quantum-classical boundary. GRUT predicts no detectable "
            "modification to cluster lensing. The dark-matter inference "
            "from the mass-light offset stands unchanged. This is a "
            "NULL RESULT for GRUT at cluster scales."
        ),
    }


if __name__ == "__main__":
    print("=" * 80)
    print("APPLICATION 3: BULLET CLUSTER LENSING ANALYSIS")
    print("=" * 80)

    # Decoherence rates
    print("\n1. GRAVITATIONAL DECOHERENCE AT CLUSTER SCALES")
    print("-" * 60)
    rates = cluster_decoherence_rates()
    for name, r in rates.items():
        print(f"  {name:>15s}: m = {r['m_solar']:.1e} M_sun, "
              f"Lambda = {r['lambda_grav_hz']:.2e} Hz, "
              f"t_decoh = {r['t_decoherence_s']:.2e} s")

    # Boundary
    print("\n2. QUANTUM-CLASSICAL BOUNDARY")
    print("-" * 60)
    b = cluster_quantum_classical_boundary()
    print(f"  At l = {BULLET_CLUSTER['separation_Mpc']} Mpc, t = 1 Gyr:")
    print(f"  m* = {b['m_boundary_kg']:.2e} kg = {b['m_boundary_solar']:.2e} M_sun")
    print(f"  Cluster mass / m* = {BULLET_CLUSTER['M_main_cluster']/b['m_boundary_kg']:.0e}")
    print(f"  -> Cluster is classical by {np.log10(BULLET_CLUSTER['M_main_cluster']/b['m_boundary_kg']):.0f} orders of magnitude")

    # Lensing
    print("\n3. LENSING MODIFICATION")
    print("-" * 60)
    lens = lensing_modification()
    print(f"  Weak-field correction: {lens['weak_field_correction']:.0e}")
    print(f"  Lensing modified: {lens['lensing_modified']}")
    print(f"  {lens['note']}")

    # Dark matter
    print("\n4. DARK MATTER IMPLICATION")
    print("-" * 60)
    print(f"  {lens['dark_matter_status']}")

    # Verdict
    print("\n5. VERDICT")
    print("-" * 60)
    analysis = full_analysis()
    print(f"  {analysis['verdict']}")
