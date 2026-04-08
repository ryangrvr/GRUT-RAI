"""Experimental platform catalog.

Named experimental configurations with all parameters specified.
Each platform is a complete specification for solver.decoherence().
"""

from dataclasses import dataclass
from grut_solver.constants import AMU, RHO_DIAMOND, RHO_SILICA
import numpy as np


@dataclass
class Platform:
    """An experimental platform with all parameters."""
    name: str
    m: float          # mass [kg]
    R: float          # radius [m]
    l: float          # superposition separation [m]
    T_env: float      # environment temperature [K]
    P: float          # gas pressure [Pa]
    t_flight: float   # free evolution time [s]
    status: str       # OPERATIONAL, IN_DEVELOPMENT, PROPOSED, FUTURE
    description: str = ""


# ============================================================
# PLATFORM CATALOG
# ============================================================

OTIMA = Platform(
    name="OTIMA (Vienna)",
    m=1e4 * AMU,
    R=1e-9,
    l=100e-9,
    T_env=300.0,
    P=1e-7,
    t_flight=0.1,
    status="OPERATIONAL",
    description="Talbot-Lau near-field interferometry with gold clusters.",
)

MAQRO = Platform(
    name="MAQRO (ESA proposed)",
    m=1e9 * AMU,
    R=100e-9,
    l=100e-9,
    T_env=20e-3,
    P=1e-12,
    t_flight=100.0,
    status="PROPOSED",
    description="Space-based matter-wave interferometry. Free-fall in microgravity.",
)

NANODIAMOND = Platform(
    name="Levitated nanodiamond",
    m=1e-14,
    R=50e-9,
    l=100e-9,
    T_env=10e-3,
    P=1e-10,
    t_flight=1.0,
    status="IN_DEVELOPMENT",
    description="Optically levitated nanodiamond with NV center spin readout.",
)

MICROSPHERE = Platform(
    name="Microsphere (next-gen)",
    m=1e-12,
    R=500e-9,
    l=1e-6,
    T_env=1e-3,
    P=1e-12,
    t_flight=10.0,
    status="FUTURE",
    description="Silica microsphere, magnetically or optically levitated.",
)

# Mu-Prime operating point from GRUT-II hardware audit
MU_PRIME = Platform(
    name="Mu-Prime (GRUT-II reference)",
    m=196e-18,                                        # 196 fg
    R=(3 * 196e-18 / (4*np.pi*RHO_DIAMOND))**(1/3),  # diamond sphere
    l=474e-9,                                          # 474 nm (= 2R, point-mass boundary)
    T_env=4.0,                                         # 4 K (cryogenic)
    P=1e-13,                                           # 10^-13 Pa (extreme UHV)
    t_flight=10.0,
    status="REFERENCE",
    description=(
        "The Mu-Prime hardware-verified operating point from GRUT-II. "
        "196 fg diamond sphere at l = 2R (the point-mass boundary). "
        "USL/gas ratio ~ 2.9. T2 gap 125x, mass gap 700x from current tech. "
        "Timeline: 5-15 years."
    ),
)

# Bose-Marletto-Vedral (BMV) entanglement witness
BMV = Platform(
    name="BMV (entanglement witness)",
    m=1e-14,
    R=50e-9,
    l=200e-6,   # 200 um separation between two particles
    T_env=10e-3,
    P=1e-11,
    t_flight=2.0,
    status="PROPOSED",
    description=(
        "Bose-Marletto-Vedral: two nanoparticles in adjacent traps. "
        "Tests whether gravity can entangle — not the USL directly, "
        "but probes quantum gravity at low energies."
    ),
)


# All platforms as a dict for easy lookup
ALL_PLATFORMS = {
    "OTIMA": OTIMA,
    "MAQRO": MAQRO,
    "NANODIAMOND": NANODIAMOND,
    "MICROSPHERE": MICROSPHERE,
    "MU_PRIME": MU_PRIME,
    "BMV": BMV,
}


def get_platform(name: str) -> Platform:
    """Look up a platform by name."""
    key = name.upper().replace(" ", "_").replace("-", "_")
    if key in ALL_PLATFORMS:
        return ALL_PLATFORMS[key]
    raise KeyError(f"Unknown platform: {name}. Available: {list(ALL_PLATFORMS.keys())}")
