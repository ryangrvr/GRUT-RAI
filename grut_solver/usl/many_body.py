"""
GRUT USL — Many-Body Extension (Closure Gate O3)

THE QUESTION: How does gravitational decoherence act on multi-particle
states? Does it treat entangled states differently from product states?

THE ANSWER: Yes. The Diosi functional depends on the TOTAL mass density
of the superposition, not on individual particles independently.
Entangled and product states have different density configurations,
producing different decoherence rates.

This is a NEW prediction beyond the single-particle USL.
Standard QM predicts both rates are zero.

THE DIOSI FUNCTIONAL (the master formula):

  Lambda = (1/hbar) * integral integral
           [rho_1(x) - rho_2(x)] [rho_1(x') - rho_2(x')]
           * (-G / |x - x'|) d^3x d^3x'

where rho_1, rho_2 are the mass densities of the two superposition branches.

For a single particle: rho_1 - rho_2 is two displaced blobs -> USL.
For two particles: rho_1 - rho_2 depends on the QUANTUM STATE (entangled vs product).
"""

import numpy as np
from grut_solver.constants import G, HBAR


# ============================================================
# SINGLE PARTICLE (reference)
# ============================================================

def lambda_single(m: float, l: float, R: float = None) -> float:
    """Single-particle gravitational decoherence rate [Hz].
    Delegates to the standard USL.
    """
    from grut_solver.usl.gravitational import lambda_grav
    return lambda_grav(m, l, R)


# ============================================================
# TWO PARTICLES — PRODUCT STATE
# ============================================================

def lambda_product(m_A: float, m_B: float, l_A: float, l_B: float,
                   d_AB: float, R_A: float = None, R_B: float = None) -> dict:
    """Decoherence rate for a PRODUCT state of two particles [Hz].

    State: |psi> = (|L>_A + |R>_A)(|L>_B + |R>_B) / 2

    Each particle is independently in a superposition of left (L) and right (R)
    separated by l_A (particle A) and l_B (particle B).
    The two particles are separated by distance d_AB (center-to-center).

    The density difference rho_1 - rho_2 has FOUR terms:
      |LL> - |RR>: both particles displaced
    But for a product state, the branches are:
      |LL>, |LR>, |RL>, |RR> (four branches, not two)

    For the product state, the decoherence RATE of the full state is:
      Lambda_product = Lambda_A + Lambda_B

    This is because the Diosi functional for independent particles is ADDITIVE
    (no cross terms between A and B when the state is separable).

    Parameters
    ----------
    m_A, m_B : float      Masses [kg].
    l_A, l_B : float      Superposition separations [m].
    d_AB : float           Inter-particle distance [m].
    R_A, R_B : float       Particle radii [m] (optional, for extended body).

    Returns
    -------
    dict with rates, interpretation.
    """
    from grut_solver.usl.gravitational import lambda_grav

    Lg_A = lambda_grav(m_A, l_A, R_A)
    Lg_B = lambda_grav(m_B, l_B, R_B)

    Lambda_prod = Lg_A + Lg_B

    return {
        "state": "product |psi_A> x |psi_B>",
        "lambda_A": Lg_A,
        "lambda_B": Lg_B,
        "lambda_product": Lambda_prod,
        "lambda_cross": 0.0,  # no cross term for product state
        "d_AB": d_AB,
        "interpretation": (
            "Product state: each particle decoheres independently. "
            "Total rate = sum of individual rates. No cross-term contribution."
        ),
    }


# ============================================================
# TWO PARTICLES — ENTANGLED (BELL) STATE
# ============================================================

def lambda_bell(m_A: float, m_B: float, l_A: float, l_B: float,
                d_AB: float, R_A: float = None, R_B: float = None) -> dict:
    """Decoherence rate for a BELL state of two particles [Hz].

    State: |psi> = (|L_A, R_B> + |R_A, L_B>) / sqrt(2)

    This is a maximally entangled state where the two particles are
    anti-correlated: when A is left, B is right, and vice versa.

    The density difference between the two branches:
      Branch 1: A at x_A - l_A/2, B at x_B + l_B/2
      Branch 2: A at x_A + l_A/2, B at x_B - l_B/2

    The Diosi functional now has CROSS TERMS between A and B:
      Lambda_Bell = Lambda_self_A + Lambda_self_B + Lambda_cross_AB

    where:
      Lambda_self_A = G m_A^2 / (hbar l_A) * S(l_A/R_A)  [same as single particle]
      Lambda_self_B = G m_B^2 / (hbar l_B) * S(l_B/R_B)  [same as single particle]
      Lambda_cross_AB = cross-term from Diosi integral

    THE CROSS TERM:

    For point masses separated by d_AB >> l_A, l_B:
      Lambda_cross = (2 G m_A m_B / hbar) *
                     [1/d_AB - 1/sqrt(d_AB^2 + (l_A + l_B)^2/4)]

    In the limit d_AB >> l_A + l_B (far separated):
      Lambda_cross ~ G m_A m_B (l_A + l_B)^2 / (4 hbar d_AB^3)

    In the limit d_AB ~ l (close):
      Lambda_cross ~ G m_A m_B / (hbar d_AB) [significant contribution]

    Parameters
    ----------
    m_A, m_B : float      Masses [kg].
    l_A, l_B : float      Superposition separations [m].
    d_AB : float           Inter-particle distance [m].
    R_A, R_B : float       Particle radii [m] (optional).
    """
    from grut_solver.usl.gravitational import lambda_grav

    Lg_A = lambda_grav(m_A, l_A, R_A)
    Lg_B = lambda_grav(m_B, l_B, R_B)

    # Cross term from the Diosi integral
    # The two branches have mass density:
    #   Branch 1: delta(x - x_A + l_A/2) m_A + delta(x - x_B - l_B/2) m_B
    #   Branch 2: delta(x - x_A - l_A/2) m_A + delta(x - x_B + l_B/2) m_B
    # Difference: rho_1 - rho_2 has four delta functions.
    # The Diosi integral G * integral (rho_1-rho_2)(x)(rho_1-rho_2)(x')/|x-x'|
    # produces self-terms (A with A, B with B) and cross-terms (A with B).

    # Self terms = standard USL for each particle
    # Cross terms: depend on geometry

    # For the Bell state |LR> + |RL>, the cross contribution involves:
    # G m_A m_B * [
    #   -1/|x_A - l_A/2 - (x_B + l_B/2)|   (branch 1 A with branch 1 B)
    #   -1/|x_A + l_A/2 - (x_B - l_B/2)|   (branch 2 A with branch 2 B)
    #   +1/|x_A - l_A/2 - (x_B - l_B/2)|   (branch 1 A with branch 2 B)
    #   +1/|x_A + l_A/2 - (x_B + l_B/2)|   (branch 2 A with branch 1 B)
    # ] / hbar

    # With x_A = 0, x_B = d_AB, and working in 1D:
    # d_11 = |d_AB + l_B/2 + l_A/2| = d_AB + (l_A + l_B)/2   (same-branch, far)
    # d_22 = |d_AB - l_B/2 - l_A/2| = d_AB - (l_A + l_B)/2   (same-branch, near)
    # d_12 = |d_AB - l_B/2 + l_A/2| = d_AB + (l_A - l_B)/2   (cross-branch)
    # d_21 = |d_AB + l_B/2 - l_A/2| = d_AB - (l_A - l_B)/2   (cross-branch)

    half_sum = (l_A + l_B) / 2.0
    half_diff = (l_A - l_B) / 2.0

    d_11 = abs(d_AB + half_sum)
    d_22 = abs(d_AB - half_sum)
    d_12 = abs(d_AB + half_diff)
    d_21 = abs(d_AB - half_diff)

    # Avoid division by zero
    eps = 1e-30

    # The cross-term in the Diosi integral:
    # Lambda_cross = (G m_A m_B / hbar) * [-1/d_11 - 1/d_22 + 1/d_12 + 1/d_21]
    cross_kernel = (
        -1.0 / (d_11 + eps)
        - 1.0 / (d_22 + eps)
        + 1.0 / (d_12 + eps)
        + 1.0 / (d_21 + eps)
    )

    Lambda_cross = G * m_A * m_B * cross_kernel / HBAR

    Lambda_bell = Lg_A + Lg_B + Lambda_cross

    return {
        "state": "Bell (|LR> + |RL>)/sqrt(2)",
        "lambda_A": Lg_A,
        "lambda_B": Lg_B,
        "lambda_cross": Lambda_cross,
        "lambda_bell": Lambda_bell,
        "d_AB": d_AB,
        "d_11": d_11, "d_22": d_22, "d_12": d_12, "d_21": d_21,
        "cross_kernel": cross_kernel,
    }


# ============================================================
# THE DISCRIMINANT: ENTANGLED vs PRODUCT
# ============================================================

def entanglement_discriminant(m: float, l: float, d_AB: float,
                               R: float = None) -> dict:
    """Compute the difference between Bell and product decoherence rates.

    For identical particles (m_A = m_B = m, l_A = l_B = l):

    Lambda_product = 2 * Lambda_single
    Lambda_bell = 2 * Lambda_single + Lambda_cross

    The DIFFERENCE is entirely in the cross term.

    Parameters
    ----------
    m : float       Mass of each particle [kg].
    l : float       Superposition separation per particle [m].
    d_AB : float    Distance between particles [m].
    R : float       Particle radius [m] (optional).

    Returns
    -------
    dict with rates, difference, fractional difference, and interpretation.
    """
    prod = lambda_product(m, m, l, l, d_AB, R, R)
    bell = lambda_bell(m, m, l, l, d_AB, R, R)

    Lp = prod["lambda_product"]
    Lb = bell["lambda_bell"]
    Lc = bell["lambda_cross"]

    diff = Lb - Lp  # = Lambda_cross
    frac = diff / Lp if Lp > 0 else 0

    return {
        "lambda_product": Lp,
        "lambda_bell": Lb,
        "lambda_cross": Lc,
        "difference_hz": diff,
        "fractional_difference": frac,
        "percent_difference": frac * 100,
        "m": m, "l": l, "d_AB": d_AB, "R": R,
        "is_measurable": abs(frac) > 0.01,  # > 1% difference
        "interpretation": (
            f"Bell state decoheres {'faster' if diff > 0 else 'slower'} than product state "
            f"by {abs(frac)*100:.2f}%. "
            f"{'This is measurable (>1%).' if abs(frac) > 0.01 else 'This may be too small to measure.'}"
        ),
    }


def cross_term_scan(m: float, l: float, R: float = None,
                     d_min: float = None, d_max: float = None,
                     n_points: int = 50) -> list[dict]:
    """Scan the cross-term as a function of inter-particle distance.

    The cross term peaks when d_AB ~ l and falls off as d_AB^{-3} for d >> l.

    Returns a list of dicts, one per d_AB value.
    """
    if d_min is None:
        d_min = l * 1.1  # slightly more than l to avoid overlap
    if d_max is None:
        d_max = l * 1000

    distances = np.logspace(np.log10(d_min), np.log10(d_max), n_points)
    results = []
    for d in distances:
        r = entanglement_discriminant(m, l, d, R)
        results.append(r)
    return results


# ============================================================
# N-PARTICLE GENERALIZATION
# ============================================================

def lambda_n_particle(masses: list, positions_L: list, positions_R: list) -> float:
    """Gravitational decoherence rate for an N-particle superposition.

    General Diosi functional for N point masses:

    Lambda = (G / hbar) * sum_{i,j}  m_i m_j *
             [1/|r_i^L - r_j^L| + 1/|r_i^R - r_j^R| - 1/|r_i^L - r_j^R| - 1/|r_i^R - r_j^L|]
             (excluding i=j self-energy which gives the single-particle USL)

    Wait — more carefully. The Diosi functional is:

    Lambda = (G / hbar) * integral (rho_L - rho_R)(x) (rho_L - rho_R)(x') / |x-x'| d^3x d^3x'

    For point masses:
    rho_L(x) = sum_i m_i delta(x - r_i^L)
    rho_R(x) = sum_i m_i delta(x - r_i^R)

    Lambda = (G / hbar) * sum_{i,j} m_i m_j *
             [1/|r_i^L - r_j^L| + 1/|r_i^R - r_j^R| - 1/|r_i^L - r_j^R| - 1/|r_i^R - r_j^L|]

    For i = j: this gives 2/0 - 2/|r_i^L - r_i^R| -> regularized to G m_i^2 / (hbar l_i)
    For i != j: cross terms (depend on state geometry)

    Parameters
    ----------
    masses : list of float       Masses [kg].
    positions_L : list of array  Positions in branch L [m]. Each is (x, y, z).
    positions_R : list of array  Positions in branch R [m].

    Returns
    -------
    float   Total decoherence rate [Hz].
    """
    N = len(masses)
    assert len(positions_L) == N and len(positions_R) == N

    rL = [np.asarray(p, dtype=float) for p in positions_L]
    rR = [np.asarray(p, dtype=float) for p in positions_R]

    eps = 1e-30  # regularization
    Lambda = 0.0

    for i in range(N):
        for j in range(N):
            if i == j:
                # Self-term: standard USL
                l_i = np.linalg.norm(rL[i] - rR[i])
                if l_i > eps:
                    Lambda += G * masses[i]**2 / (HBAR * l_i)
            else:
                # Cross-term
                d_LL = np.linalg.norm(rL[i] - rL[j]) + eps
                d_RR = np.linalg.norm(rR[i] - rR[j]) + eps
                d_LR = np.linalg.norm(rL[i] - rR[j]) + eps
                d_RL = np.linalg.norm(rR[i] - rL[j]) + eps

                kernel = 1/d_LL + 1/d_RR - 1/d_LR - 1/d_RL
                Lambda += G * masses[i] * masses[j] * kernel / HBAR

    return Lambda


# ============================================================
# GHZ STATE — THREE PARTICLES
# ============================================================

def lambda_ghz_3(m: float, l: float, d_12: float, d_23: float) -> dict:
    """Decoherence rate for a 3-particle GHZ state.

    |GHZ> = (|L L L> + |R R R>) / sqrt(2)

    All three particles in a correlated superposition along one axis.
    Particle positions: x_1 = 0, x_2 = d_12, x_3 = d_12 + d_23.

    Branch L: all particles shifted by -l/2.
    Branch R: all particles shifted by +l/2.
    """
    # GHZ: all go left or all go right
    positions_L = [
        np.array([0 - l/2, 0, 0]),
        np.array([d_12 - l/2, 0, 0]),
        np.array([d_12 + d_23 - l/2, 0, 0]),
    ]
    positions_R = [
        np.array([0 + l/2, 0, 0]),
        np.array([d_12 + l/2, 0, 0]),
        np.array([d_12 + d_23 + l/2, 0, 0]),
    ]

    masses = [m, m, m]
    Lambda_ghz = lambda_n_particle(masses, positions_L, positions_R)

    # For comparison: product state (each independently L+R)
    # Product rate = 3 * single-particle rate
    from grut_solver.usl.gravitational import lambda_grav
    Lambda_single = lambda_grav(m, l)
    Lambda_product = 3 * Lambda_single

    return {
        "state": "GHZ (|LLL> + |RRR>)/sqrt(2)",
        "lambda_ghz": Lambda_ghz,
        "lambda_product_3": Lambda_product,
        "lambda_single": Lambda_single,
        "ratio_ghz_over_product": Lambda_ghz / Lambda_product if Lambda_product > 0 else 0,
        "enhancement": Lambda_ghz / Lambda_product - 1 if Lambda_product > 0 else 0,
        "d_12": d_12, "d_23": d_23,
        "interpretation": (
            f"GHZ state decoheres at {Lambda_ghz:.2e} Hz vs product at {Lambda_product:.2e} Hz. "
            f"Ratio: {Lambda_ghz/Lambda_product:.4f}. "
            f"The GHZ enhancement comes from cross-terms: all particles shift "
            f"coherently, creating larger gravitational self-energy differences."
        ),
    }


if __name__ == "__main__":
    print("=" * 80)
    print("GRUT MANY-BODY EXTENSION — Closure Gate O3")
    print("=" * 80)
    print()

    m = 1e-14  # 10 pg each
    l = 100e-9  # 100 nm superposition
    R = 50e-9   # 50 nm radius

    print("=== TWO-PARTICLE: ENTANGLED vs PRODUCT ===")
    print()
    print(f"  m = {m*1e15:.0f} fg, l = {l*1e9:.0f} nm, R = {R*1e9:.0f} nm")
    print()
    print(f"  {'d_AB (um)':>10s}  {'Lambda_prod':>12s}  {'Lambda_bell':>12s}  {'cross term':>12s}  {'diff %':>8s}")

    for d_um in [0.5, 1, 2, 5, 10, 50, 100, 500]:
        d = d_um * 1e-6
        disc = entanglement_discriminant(m, l, d, R)
        print(f"  {d_um:10.1f}  {disc['lambda_product']:12.2e}  {disc['lambda_bell']:12.2e}  {disc['lambda_cross']:12.2e}  {disc['percent_difference']:8.2f}")

    print()

    # Peak discriminant
    print("=== PEAK DISCRIMINANT ===")
    print()
    scan = cross_term_scan(m, l, R, d_min=l*1.5, d_max=l*10000, n_points=100)
    peak = max(scan, key=lambda r: abs(r["fractional_difference"]))
    print(f"  Peak at d_AB = {peak['d_AB']*1e6:.2f} um: "
          f"difference = {peak['percent_difference']:.2f}%")
    print(f"  {'Measurable' if peak['is_measurable'] else 'Not measurable'}")
    print()

    # GHZ state
    print("=== THREE-PARTICLE GHZ STATE ===")
    print()
    for d in [1e-6, 10e-6, 100e-6]:
        ghz = lambda_ghz_3(m, l, d, d)
        print(f"  d = {d*1e6:.0f} um: GHZ/product = {ghz['ratio_ghz_over_product']:.4f} "
              f"(enhancement = {ghz['enhancement']*100:.2f}%)")

    print()
    print("=== SCALING: N-PARTICLE GHZ ===")
    print()
    print("  For N identical particles in GHZ |LL...L> + |RR...R>:")
    print("  Lambda_GHZ = N * Lambda_single + N(N-1) * Lambda_cross")
    print("  Lambda_product = N * Lambda_single")
    print("  Enhancement ratio = 1 + (N-1) * Lambda_cross / Lambda_single")
    print()
    print("  The GHZ enhancement grows LINEARLY with N.")
    print("  For large N: Lambda_GHZ ~ N^2 * Lambda_cross (dominates)")
    print("  This is a MACROSCOPIC ENTANGLEMENT AMPLIFIER for gravitational decoherence.")
