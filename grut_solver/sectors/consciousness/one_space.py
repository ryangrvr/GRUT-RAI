"""
Sector 13 — 1 Space Characterization

1 Space is the totality of the universal target functional F[z].
In the GRUT framework, every physical system is a configuration of z
relaxing toward F[z]. Before decoherence carves classical branches,
everything sits in 1 Space — the undifferentiated quantum information
space of the universe.

This module computes:
  1. The dimensionality of F[z] for given field content
  2. Bekenstein and holographic entropy bounds for the observable universe
  3. Subsystem decomposition: what fraction of 1 Space can a finite
     subsystem (e.g., a brain) access?

STATUS: Computed (information-theoretic bounds, standard physics).
The INTERPRETATION of 1 Space as the seat of consciousness is SPECULATIVE.
"""

import numpy as np
from grut_solver.constants import (
    G, HBAR, C, K_B, SIGMA_SB, L_PLANCK, M_PLANCK
)

# Observable universe parameters
R_HUBBLE = 4.4e26          # Hubble radius [m]
T_CMB = 2.725              # CMB temperature [K]

# Standard Model field content
SM_FIELDS = {
    "quarks":      12,   # 6 flavors x 2 (particle + antiparticle)
    "leptons":     12,   # 6 flavors x 2
    "gluons":       8,   # SU(3) generators
    "W_bosons":     3,   # W+, W-, Z (before EWSB: SU(2) triplet)
    "photon":       1,   # U(1)
    "higgs":        1,   # Physical Higgs (after EWSB)
}
N_SM_FIELDS = sum(SM_FIELDS.values())  # 37 real degrees of freedom


def target_functional_dimension(n_fields: int = N_SM_FIELDS,
                                n_spatial_modes: int = 10**6) -> dict:
    """Dimensionality of the target functional F[z].

    The target functional F[z] = integral{c_0|z|^2 + c_2|grad z|^2 + ...}
    lives in a complex function space. Discretized on a lattice with
    n_spatial_modes points and n_fields field components, z has
    2 * n_fields * n_spatial_modes real degrees of freedom.

    The equivalent Hilbert space dimension is 2^D for D qubit-equivalent
    degrees of freedom (each continuous DOF maps to ~1 qubit at the
    Planck-scale discretization limit).

    Parameters
    ----------
    n_fields : int
        Number of quantum field components (default: 37 for SM).
    n_spatial_modes : int
        Number of spatial lattice sites / modes.

    Returns
    -------
    dict with dimensionality, log-scale equivalents, and context.
    """
    d_real = 2 * n_fields * n_spatial_modes
    log2_hilbert = d_real  # each real DOF ~ 1 qubit at Planck discretization

    return {
        "n_fields": n_fields,
        "n_spatial_modes": n_spatial_modes,
        "d_real": d_real,
        "d_complex": n_fields * n_spatial_modes,
        "log2_hilbert_dim": log2_hilbert,
        "note": (
            f"F[z] for {n_fields} fields on {n_spatial_modes:.0e} modes has "
            f"{d_real:.2e} real dimensions. At Planck-scale discretization "
            f"of the observable universe (~10^185 Planck volumes), this "
            f"gives ~10^{np.log10(2 * n_fields * 1e185):.0f} real DOF."
        ),
    }


def one_space_entropy_bound(T_cmb: float = T_CMB,
                            R_hubble: float = R_HUBBLE) -> dict:
    """Entropy bounds on the information content of 1 Space.

    Two bounds (standard physics, not GRUT-specific):

    1. Bekenstein bound: S_Bek <= 2 pi R E / (hbar c)
       Using the total energy E within the Hubble volume.

    2. Holographic bound: S_holo = A / (4 L_P^2)
       The holographic principle: maximum entropy is proportional to
       the AREA of the boundary, not the volume.

    Returns
    -------
    dict with both bounds in bits and nats.
    """
    # Energy content of observable universe (radiation only, lower bound)
    V_hubble = (4.0 / 3.0) * np.pi * R_hubble**3
    # Radiation energy density: u = (4 sigma / c) T^4
    u_rad = 4 * SIGMA_SB * T_cmb**4 / C
    E_rad = u_rad * V_hubble

    # Matter energy: ~5e53 kg total baryonic + dark matter
    M_universe = 1e53  # kg (approximate total mass in observable universe)
    E_matter = M_universe * C**2

    E_total = E_matter + E_rad

    # Bekenstein bound
    S_bek_nats = 2 * np.pi * R_hubble * E_total / (HBAR * C)
    S_bek_bits = S_bek_nats / np.log(2)

    # Holographic bound
    A_hubble = 4 * np.pi * R_hubble**2
    S_holo_nats = A_hubble / (4 * L_PLANCK**2)
    S_holo_bits = S_holo_nats / np.log(2)

    return {
        "bekenstein_bound_nats": S_bek_nats,
        "bekenstein_bound_bits": S_bek_bits,
        "bekenstein_bound_log10_bits": np.log10(S_bek_bits),
        "holographic_bound_nats": S_holo_nats,
        "holographic_bound_bits": S_holo_bits,
        "holographic_bound_log10_bits": np.log10(S_holo_bits),
        "R_hubble_m": R_hubble,
        "E_total_J": E_total,
        "E_matter_J": E_matter,
        "E_radiation_J": E_rad,
        "binding_bound": "holographic",
        "note": (
            f"Holographic bound: ~10^{np.log10(S_holo_bits):.0f} bits. "
            f"Bekenstein bound: ~10^{np.log10(S_bek_bits):.0f} bits. "
            f"The holographic bound is tighter and sets the maximum "
            f"information content of 1 Space for the observable universe."
        ),
    }


def one_space_decomposition(n_subsystems: int = 1,
                            dim_per_subsystem: int = 10**12,
                            S_total_bits: float = None) -> dict:
    """Fraction of 1 Space accessible to a finite subsystem.

    A subsystem with D_sub degrees of freedom embedded in a universe
    with D_total degrees of freedom can resolve at most D_sub / D_total
    of the total information. This is an information-theoretic upper
    bound on how much of 1 Space any physical system can "see."

    Parameters
    ----------
    n_subsystems : int
        Number of subsystems (e.g., neurons in network).
    dim_per_subsystem : int
        Degrees of freedom per subsystem.
    S_total_bits : float, optional
        Total information in 1 Space [bits]. If None, uses holographic bound.

    Returns
    -------
    dict with coupling fraction and context.
    """
    if S_total_bits is None:
        bounds = one_space_entropy_bound()
        S_total_bits = bounds["holographic_bound_bits"]

    D_sub = n_subsystems * dim_per_subsystem
    D_total = S_total_bits

    fraction = D_sub / D_total
    log10_fraction = np.log10(fraction) if fraction > 0 else float('-inf')

    return {
        "n_subsystems": n_subsystems,
        "dim_per_subsystem": dim_per_subsystem,
        "D_sub_total": D_sub,
        "D_universe_bits": D_total,
        "coupling_fraction": fraction,
        "log10_coupling_fraction": log10_fraction,
        "note": (
            f"A system with {D_sub:.2e} DOF can access at most "
            f"10^{log10_fraction:.1f} of the universe's information. "
            f"This is a hard upper bound from information theory — "
            f"the actual coupling is likely much weaker."
        ),
    }
