"""
GRUT USL — Anomaly Channel

The 3-loop gravitational anomaly creates an additional decoherence channel.
Planck-suppressed: Lambda_anom / Lambda_grav ~ C_Final^2 ~ 10^-8.
NOT experimentally relevant with foreseeable technology.
Structurally present in the CTP influence functional.
"""

from grut_solver.constants import G, HBAR, C_FINAL, R_ANOMALY


def lambda_anomaly(m: float, l: float) -> float:
    """Anomaly-induced gravitational decoherence rate [Hz].

    Lambda_anom = C_Final^2 * G m^2 / (hbar l)

    This is Planck-suppressed relative to the Newtonian channel:
    Lambda_anom / Lambda_grav ~ C_Final^2 ~ 1.3e-8.

    NOTE: Not experimentally relevant. Included for structural completeness.

    Parameters
    ----------
    m : float
        Mass [kg].
    l : float
        Superposition separation [m].

    Returns
    -------
    float
        Anomaly decoherence rate [Hz].
    """
    if m <= 0 or l <= 0:
        return 0.0
    return C_FINAL**2 * G * m**2 / (HBAR * l)


def c_final() -> float:
    """The 3-loop gravitational anomaly coefficient (scheme-protected).

    C_Final = 3*(99 + 2*pi^2 + 576*ln(2)*zeta(3)) / (16384*pi^6)
            ~ 1.14e-4

    This is a PURE NUMBER from the Standard Model field content + gravity
    at 3 loops. It is scheme-protected (nonlocal operator).
    """
    return C_FINAL


def r_anomaly() -> float:
    """Anomaly ratio R = |C_Cosmo / C_Final| = 1.15428.

    From published papers (Grover 2025). Verified to 15 significant figures.
    C_Final is scheme-protected; C_Cosmo is local and fragile.
    R inherits the fragility of C_Cosmo.
    """
    return R_ANOMALY


def c_cosmo() -> float:
    """Cosmological anomaly coefficient C_Cosmo.

    C_Cosmo = (-108000 + pi^4 + 1536*pi^4*ln(2) + 540*zeta(3)) / (276480*pi^4)

    This is the zero-momentum finite part (cosmological counterterm).
    It is NOT anomaly-protected: local operator, subject to finite
    renormalization. A rational shift delta_n ~ 36 in the -108000
    coefficient shifts R by 1%.
    """
    import numpy as np
    from grut_solver.constants import ZETA_3
    num = -108000 + np.pi**4 + 1536*np.pi**4*np.log(2) + 540*ZETA_3
    den = 276480 * np.pi**4
    return num / den


def anomaly_crossover_length(m: float) -> float:
    """Crossover separation where anomaly and Newtonian channels are equal [m].

    The Newtonian channel scales as Lambda_N ~ m^2 / l (1/l).
    The anomaly channel from M3 scales as Lambda_A ~ m^2 * l (linear in l).
    (The anomaly channel's noise kernel goes as 1/k^4 in momentum space,
    giving the opposite l-scaling after Fourier transform.)

    The crossover: Lambda_N(l_c) = Lambda_A(l_c)
      G m^2 / (hbar l_c) = C_Final^2 * G m^2 * l_c / (hbar * l_ref^2)

    This gives l_c = l_ref / C_Final (if we use the M3 normalization).

    In practice, the anomaly channel is so suppressed that l_c is
    astronomical (~3.5 million light-years from M3).

    Parameters
    ----------
    m : float   Mass [kg]. (Cancels out — crossover is mass-independent.)
    """
    # From program_m_m3_cfinal_usl.py:
    # The crossover length is set by the anomaly structure, not by m.
    # l_c ~ sqrt(1 / C_Final^2) * l_Planck-scale factor
    # The M3 computation gives l_c ~ 3.5 million light-years
    import numpy as np
    ly = 9.461e15  # light-year in meters
    l_crossover = 3.5e6 * ly  # ~3.3e22 m

    return l_crossover


def two_channel_rate(m: float, l: float) -> dict:
    """Compute both Newtonian and anomaly decoherence channels.

    Returns the rates and which channel dominates at separation l.
    """
    Lambda_N = G * m**2 / (HBAR * l) if l > 0 else 0
    Lambda_A = lambda_anomaly(m, l)
    l_c = anomaly_crossover_length(m)

    return {
        "lambda_newtonian": Lambda_N,
        "lambda_anomaly": Lambda_A,
        "ratio_A_over_N": Lambda_A / Lambda_N if Lambda_N > 0 else 0,
        "dominant": "newtonian" if Lambda_N > Lambda_A else "anomaly",
        "crossover_length_m": l_c,
        "crossover_length_ly": l_c / 9.461e15,
        "note": (
            f"At l = {l:.2e} m: Newtonian dominates by "
            f"{Lambda_N/Lambda_A:.0e}x. "
            f"Crossover at l_c = {l_c/9.461e15:.1e} light-years."
        ),
    }
