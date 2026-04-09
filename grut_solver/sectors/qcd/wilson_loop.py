"""
Module 4: Wilson loop — toy-level 2D lattice proxy.

Status: EXPLORATORY. This is a minimal demonstration scaffold,
not a full lattice QCD computation.

The Wilson loop W(C) = (1/N) Tr P exp(i g_s oint A_mu dx^mu)
is the order parameter for confinement:
  area law: W ~ exp(-sigma * Area) => confined
  perimeter law: W ~ exp(-mu * Perimeter) => deconfined
"""

import numpy as np
from grut_solver.sectors.qcd.su3_structure import T_GEN, N_GEN, N_C, I3


def random_su3_link(g_s: float, eps: float = 0.1) -> np.ndarray:
    """Generate a random SU(3) link variable near the identity.

    U = exp(i eps g_s theta^a T^a), theta^a ~ random.
    """
    theta = eps * np.random.randn(N_GEN)
    generator = sum(theta[a] * T_GEN[a] for a in range(N_GEN))
    from scipy.linalg import expm
    return expm(1j * g_s * generator)


def wilson_loop_2d(Nx: int = 8, Ny: int = 8, g_s: float = 1.0,
                    eps: float = 0.3, R: int = 3, T: int = 3) -> dict:
    """Compute a Wilson loop on a 2D toy lattice.

    Parameters
    ----------
    Nx, Ny : int    Lattice dimensions.
    g_s : float     Coupling constant.
    eps : float     Fluctuation amplitude for link variables.
    R, T : int      Loop dimensions (spatial x temporal extent).

    Returns
    -------
    dict with W (loop value), area, perimeter, and diagnostic info.

    NOTE: This is EXPLORATORY. A real lattice QCD computation requires
    Monte Carlo importance sampling, proper action weighting, and
    thermalization. This is a deterministic toy model.
    """
    np.random.seed(0)

    # Generate random link variables U_mu(x) for mu = 0 (x), 1 (y)
    U = np.zeros((2, Nx, Ny, N_C, N_C), dtype=complex)
    for mu in range(2):
        for x in range(Nx):
            for y in range(Ny):
                U[mu, x, y] = random_su3_link(g_s, eps)

    # Compute Wilson loop W(R, T) starting at origin
    # Path: right R steps, up T steps, left R steps, down T steps
    # W = Tr(U_x(0,0) U_x(1,0) ... U_y(R,0) U_y(R,1) ... U_x^dag(R-1,T) ... U_y^dag(0,T-1) ...)

    path_product = np.eye(N_C, dtype=complex)

    # Right: mu=0, (x, 0) for x = 0..R-1
    for x in range(R):
        path_product = path_product @ U[0, x % Nx, 0]

    # Up: mu=1, (R, y) for y = 0..T-1
    for y in range(T):
        path_product = path_product @ U[1, R % Nx, y % Ny]

    # Left: mu=0 dagger, (x, T) for x = R-1..0
    for x in range(R-1, -1, -1):
        path_product = path_product @ U[0, x % Nx, T % Ny].conj().T

    # Down: mu=1 dagger, (0, y) for y = T-1..0
    for y in range(T-1, -1, -1):
        path_product = path_product @ U[1, 0, y % Ny].conj().T

    W = np.real(np.trace(path_product)) / N_C
    area = R * T
    perimeter = 2 * (R + T)

    return {
        "W": W,
        "area": area,
        "perimeter": perimeter,
        "R": R, "T": T,
        "g_s": g_s, "eps": eps,
        "Nx": Nx, "Ny": Ny,
        "note": "EXPLORATORY: deterministic toy lattice, not Monte Carlo QCD.",
    }


def area_law_scan(Nx: int = 12, Ny: int = 12, g_s: float = 1.0,
                   eps: float = 0.5, R_max: int = 5) -> dict:
    """Scan Wilson loop vs area to test for area-law behavior.

    If ln|W| ~ -sigma * A (linear in area), this suggests confinement.
    If ln|W| ~ -mu * P (linear in perimeter), this suggests deconfinement.
    """
    results = []
    for R in range(1, R_max + 1):
        for T_val in range(1, R_max + 1):
            w = wilson_loop_2d(Nx, Ny, g_s, eps, R, T_val)
            if abs(w["W"]) > 1e-15:
                results.append({
                    "R": R, "T": T_val,
                    "area": R * T_val,
                    "perimeter": 2*(R + T_val),
                    "W": w["W"],
                    "ln_W": np.log(abs(w["W"])),
                })

    if len(results) < 3:
        return {"results": results, "fit": None,
                "note": "Insufficient data for area/perimeter fit."}

    areas = np.array([r["area"] for r in results])
    ln_W = np.array([r["ln_W"] for r in results])
    perimeters = np.array([r["perimeter"] for r in results])

    # Fit: ln|W| = -sigma * A + const (area law)
    area_fit = np.polyfit(areas, ln_W, 1)
    area_residual = np.sqrt(np.mean((ln_W - np.polyval(area_fit, areas))**2))

    # Fit: ln|W| = -mu * P + const (perimeter law)
    perim_fit = np.polyfit(perimeters, ln_W, 1)
    perim_residual = np.sqrt(np.mean((ln_W - np.polyval(perim_fit, perimeters))**2))

    return {
        "results": results,
        "area_fit_slope": area_fit[0],   # -sigma if area law
        "area_fit_residual": area_residual,
        "perim_fit_slope": perim_fit[0],  # -mu if perimeter law
        "perim_fit_residual": perim_residual,
        "area_law_preferred": area_residual < perim_residual,
        "note": "EXPLORATORY: toy lattice results, not physical QCD.",
    }
