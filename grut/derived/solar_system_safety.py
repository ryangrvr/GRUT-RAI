"""Solar-system safety — quantitative multi-test demonstration.

The closure_protocol's `solar_system_safety` claim asserts that GRUT
reduces to GR at solar-system frequencies (ωτ_0 ≫ 1 → α_eff → 0). The
basic assertion is anchored in Saturn's orbital frequency. This module
extends the demonstration to eight independent precision tests of GR
spanning six orders of magnitude in frequency, showing that the
constitutive correction α_eff is below the measurement precision of
each test by factors of 10⁵ to 10³⁵.

The eight tests:

    1. Saturn orbit ranging (Cassini)
    2. Mercury perihelion advance
    3. Lunar laser ranging (Earth-Moon, G_dot/G)
    4. GPS orbital relativity (Earth-bound atomic clocks)
    5. Hulse-Taylor binary pulsar (B1913+16)
    6. Cassini Shapiro delay (post-Newtonian γ)
    7. LIGO GW propagation
    8. Earth orbital ranging (Astronomical Unit)

For each: compute the natural angular frequency ω of the test, the
dimensionless regime parameter X = ωτ_0, the constitutive correction
α_eff(ω) = α / (1 + X²), and the safety factor (current observational
precision) / α_eff. Any safety factor > 1 means the framework's
prediction is below detection precision; > 100 means safety with
substantial margin.

References
----------
- Will, C.M. (2014). "The Confrontation between General Relativity and
  Experiment," Living Rev. Relativity 17, 4. arXiv:1403.7377.
- Bertotti, Iess, Tortora (2003). Cassini test of γ. Nature 425, 374.
- Williams et al. (2004). Lunar laser ranging tests. PRL 93, 261101.
- Weisberg & Huang (2016). Hulse-Taylor B1913+16. ApJ 829, 55.
- Abbott et al. LIGO Scientific (2017). GW170817 + GRB170817A.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from grut.foundation.closure_protocol import ALPHA_VAC, TAU_0_SEC


YEAR_SEC: float = 3.156e7
DAY_SEC: float = 86400.0
HOUR_SEC: float = 3600.0


# ─────────────────────────────────────────────────────────────────────
# Test record
# ─────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class SolarSystemTest:
    """One precision test of GR with its associated frequency and
    observational precision."""
    short_id: str
    name: str
    period_seconds: float
    period_human: str           # e.g. "30 yr", "12 hr"
    omega_basis: str            # what physical timescale ω represents
    obs_precision: float        # current measurement precision
    obs_precision_basis: str    # what the precision describes
    citation: str
    notes: str = ""

    @property
    def omega_Hz(self) -> float:
        return 2 * math.pi / self.period_seconds

    @property
    def omega_tau_0(self) -> float:
        return self.omega_Hz * TAU_0_SEC

    @property
    def alpha_eff(self) -> float:
        return ALPHA_VAC / (1.0 + self.omega_tau_0 ** 2)

    @property
    def safety_factor(self) -> float:
        """obs_precision / α_eff. > 1 means GRUT below detection."""
        if self.alpha_eff <= 0:
            return float("inf")
        return self.obs_precision / self.alpha_eff


# ─────────────────────────────────────────────────────────────────────
# The eight tests
# ─────────────────────────────────────────────────────────────────────

SOLAR_SYSTEM_TESTS: tuple[SolarSystemTest, ...] = (

    SolarSystemTest(
        short_id="SS01",
        name="Saturn orbit (Cassini ranging)",
        period_seconds=30 * YEAR_SEC,
        period_human="30 yr",
        omega_basis="orbital angular frequency",
        obs_precision=1e-9,
        obs_precision_basis="Cassini ranging fractional precision on Saturn position",
        citation="Folkner et al. 2014 (DE430 ephemeris)",
    ),

    SolarSystemTest(
        short_id="SS02",
        name="Mercury perihelion advance",
        period_seconds=88 * DAY_SEC,
        period_human="88 days",
        omega_basis="orbital angular frequency",
        obs_precision=3e-3,
        obs_precision_basis=(
            "fractional precision on the GR contribution (43 arcsec/century) "
            "from MESSENGER and INPOP ephemerides"
        ),
        citation="Park et al. 2017 (AJ 153 121); Verma et al. 2014",
    ),

    SolarSystemTest(
        short_id="SS03",
        name="Lunar laser ranging",
        period_seconds=27.3 * DAY_SEC,
        period_human="27.3 days",
        omega_basis="Earth-Moon orbital frequency",
        obs_precision=1e-13,
        obs_precision_basis="G_dot/G constraint per year (Williams et al. 2004)",
        citation="Williams, Turyshev, Boggs 2004 (PRL 93 261101)",
    ),

    SolarSystemTest(
        short_id="SS04",
        name="GPS orbital relativity",
        period_seconds=12 * HOUR_SEC,
        period_human="12 hours",
        omega_basis="GPS satellite orbital frequency",
        obs_precision=1e-13,
        obs_precision_basis="atomic clock fractional stability (~10⁻¹³/day)",
        citation="Ashby 2003 (Living Rev. Rel. 6, 1)",
    ),

    SolarSystemTest(
        short_id="SS05",
        name="Hulse-Taylor binary pulsar B1913+16",
        period_seconds=7.75 * HOUR_SEC,
        period_human="7.75 hours",
        omega_basis="orbital angular frequency",
        obs_precision=1.6e-3,
        obs_precision_basis=(
            "ratio of observed to GR-predicted period decay rate "
            "(precision ~0.16%)"
        ),
        citation="Weisberg & Huang 2016 (ApJ 829 55)",
    ),

    SolarSystemTest(
        short_id="SS06",
        name="Cassini Shapiro delay",
        period_seconds=500.0,
        period_human="500 s (≈ 1 AU/c)",
        omega_basis="photon transit time across Sun's gravitational field",
        obs_precision=2.3e-5,
        obs_precision_basis="post-Newtonian γ measurement (γ - 1 = (2.1 ± 2.3) × 10⁻⁵)",
        citation="Bertotti, Iess, Tortora 2003 (Nature 425 374)",
    ),

    SolarSystemTest(
        short_id="SS07",
        name="LIGO/Virgo GW propagation (GW170817)",
        period_seconds=1.0 / 100.0,
        period_human="≈10 ms (100 Hz GW)",
        omega_basis="gravitational-wave angular frequency",
        obs_precision=7e-2,
        obs_precision_basis=(
            "constraint on GW group velocity vs. c at 7% level "
            "(GW170817 + GRB170817A coincidence)"
        ),
        citation="Abbott et al. (LIGO+Virgo) 2017 (ApJL 848 L13)",
    ),

    SolarSystemTest(
        short_id="SS08",
        name="Earth orbit (AU ranging)",
        period_seconds=YEAR_SEC,
        period_human="1 yr",
        omega_basis="Earth orbital frequency",
        obs_precision=1e-9,
        obs_precision_basis="AU determination precision from radar/pulsar timing",
        citation="DE430 / IAU 2009 nominal AU value",
    ),
)


# ─────────────────────────────────────────────────────────────────────
# Aggregate analysis
# ─────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class SafetyReport:
    n_tests: int
    n_safe: int
    """Tests with safety_factor > 1 (GRUT below detection)."""
    n_safe_with_margin: int
    """Tests with safety_factor > 100 (substantial margin)."""
    min_safety_factor: float
    max_safety_factor: float
    median_safety_factor: float
    smallest_alpha_eff: float
    largest_alpha_eff: float


def safety_report() -> SafetyReport:
    factors = sorted(t.safety_factor for t in SOLAR_SYSTEM_TESTS)
    alphas = sorted(t.alpha_eff for t in SOLAR_SYSTEM_TESTS)
    n_safe = sum(1 for f in factors if f > 1.0)
    n_safe_margin = sum(1 for f in factors if f > 100.0)
    median = factors[len(factors) // 2]
    return SafetyReport(
        n_tests=len(SOLAR_SYSTEM_TESTS),
        n_safe=n_safe,
        n_safe_with_margin=n_safe_margin,
        min_safety_factor=factors[0],
        max_safety_factor=factors[-1],
        median_safety_factor=median,
        smallest_alpha_eff=alphas[0],
        largest_alpha_eff=alphas[-1],
    )


# ─────────────────────────────────────────────────────────────────────
# Markdown rendering
# ─────────────────────────────────────────────────────────────────────

def render_table() -> str:
    """Render the multi-test safety table for the ToE document."""
    out = []
    out.append("| ID | Test | Period | ωτ_0 | α_eff | Obs precision | Safety factor |")
    out.append("|:---|:---|:---|---:|---:|---:|---:|")
    for t in SOLAR_SYSTEM_TESTS:
        out.append(
            f"| {t.short_id} | {t.name} | {t.period_human} | "
            f"{t.omega_tau_0:.2e} | {t.alpha_eff:.2e} | "
            f"{t.obs_precision:.1e} | {t.safety_factor:.1e} |"
        )
    return "\n".join(out)


def render_full_report() -> str:
    out = []
    rep = safety_report()
    out.append("# GRUT — Solar-System Safety Multi-Test Demonstration")
    out.append("")
    out.append(
        "*Auto-generated from `grut/derived/solar_system_safety.py`. "
        "Re-run to regenerate.*"
    )
    out.append("")
    out.append(
        "Eight independent precision tests of GR span six orders of "
        "magnitude in frequency. For each test, GRUT's predicted "
        "constitutive correction α_eff(ω) = α/(1 + (ωτ_0)²) is "
        "compared to the observational measurement precision. The "
        "safety factor (obs precision / α_eff) is the margin by which "
        "GRUT's prediction sits below detection threshold."
    )
    out.append("")
    out.append("## Aggregate")
    out.append("")
    out.append(f"- Total tests: {rep.n_tests}")
    out.append(f"- Tests with safety factor > 1 (GRUT below detection): {rep.n_safe}/{rep.n_tests}")
    out.append(f"- Tests with safety factor > 100 (substantial margin): {rep.n_safe_with_margin}/{rep.n_tests}")
    out.append(f"- Smallest safety factor: {rep.min_safety_factor:.2e}")
    out.append(f"- Largest safety factor: {rep.max_safety_factor:.2e}")
    out.append(f"- Median safety factor: {rep.median_safety_factor:.2e}")
    out.append("")
    out.append("## Per-test breakdown")
    out.append("")
    out.append(render_table())
    out.append("")
    out.append("## Detailed entries")
    out.append("")
    for t in SOLAR_SYSTEM_TESTS:
        out.append(f"### {t.short_id} — {t.name}")
        out.append("")
        out.append(f"- **Period:** {t.period_human} ({t.period_seconds:.2e} s)")
        out.append(f"- **Frequency basis:** {t.omega_basis}")
        out.append(f"- **ω = 2π/period:** {t.omega_Hz:.2e} Hz")
        out.append(f"- **ωτ_0:** {t.omega_tau_0:.2e}")
        out.append(f"- **α_eff(ω):** {t.alpha_eff:.2e}")
        out.append(f"- **Observational precision:** {t.obs_precision:.1e} ({t.obs_precision_basis})")
        out.append(f"- **Safety factor:** {t.safety_factor:.2e} ({'safe' if t.safety_factor > 1 else 'CHECK'})")
        out.append(f"- **Citation:** {t.citation}")
        if t.notes:
            out.append(f"- **Notes:** {t.notes}")
        out.append("")
    return "\n".join(out)


# ─────────────────────────────────────────────────────────────────────
# Verification harness
# ─────────────────────────────────────────────────────────────────────

def verify() -> dict:
    rep = safety_report()
    return {
        "all_tests_safe":             rep.n_safe == rep.n_tests,
        "all_tests_substantial_margin": rep.n_safe_with_margin == rep.n_tests,
        "median_safety_above_1e6":    rep.median_safety_factor > 1e6,
        "min_safety_above_1e4":       rep.min_safety_factor > 1e4,
        "all_alpha_eff_under_1e_minus_10": all(
            t.alpha_eff < 1e-10 for t in SOLAR_SYSTEM_TESTS
        ),
        "tests_span_six_orders_of_magnitude_in_omega": (
            max(t.omega_Hz for t in SOLAR_SYSTEM_TESTS)
            / min(t.omega_Hz for t in SOLAR_SYSTEM_TESTS)
            > 1e10
        ),
    }


if __name__ == "__main__":
    print(render_full_report())
    print()
    print("Verify:")
    for k, v in verify().items():
        mark = "PASS" if v else "FAIL"
        print(f"  [{mark}] {k}")
