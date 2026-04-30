"""GRUT-vs-CSL discriminator via isotope-pair decoherence ratios.

The framework's m² scaling vs CSL's linear-in-mass (or linear-in-N)
scaling can be tested cleanly by comparing decoherence rates of
isotope pairs of the same element. Same chemistry, same nanoparticle
geometry, same surface — only nuclear mass differs.

Why this is the cleanest discriminator
--------------------------------------

Most decoherence experiments compare different materials (gold vs
silica), where chemistry and geometry differ. CSL/GRUT predictions
depend on multiple parameters and are easily confounded with
environmental systematics.

Isotope substitution holds everything constant EXCEPT:
    - Total nuclear mass (different per atom)
    - Nucleon count (different)
    - Mass density (slightly different)
Atom count, surface chemistry, optical response, and geometry are
identical.

Predictions for the decoherence rate ratio Λ(heavier) / Λ(lighter):

    GRUT:       (m_heavier / m_lighter)²
                Quadratic in mass. Zero free parameters.

    CSL (linear-in-nucleons, large-system regime):
                N_heavier / N_lighter ≈ m_heavier / m_lighter
                Linear in nucleon count. λ-dependent for absolute rate;
                λ CANCELS in the ratio.

    CSL (Adler mass-proportional):
                m_heavier / m_lighter
                Linear in mass. Same ratio as standard CSL.

    CSL (small-system / coherent regime, l < r_C ~ 100 nm):
                ≈ 1 (rate scales with N² but for matched-atom-count
                samples, both N's are equal)
                Note: Most matter-wave interferometry experiments
                operate at l > r_C, so this regime is rare.

Discriminator framing
---------------------

GRUT's prediction is parameter-free at this scale:
    Λ_grav = G m² S(l/R) / (ℏl)
Every input is known.

CSL's prediction has the localization parameter λ as a free input.
Different published λ values (GRW λ ≈ 10⁻¹⁶ s⁻¹, Adler enhanced,
Bassi-Pearle range) span orders of magnitude. But:
    - The CSL ratio between isotopes is λ-INDEPENDENT (cancels)
    - The structural form (linear vs quadratic in mass) doesn't depend
      on λ either

So the CSL-vs-GRUT discriminator is purely structural:
    GRUT/CSL ratio factor = (m_heavier / m_lighter)¹
                         = mass ratio itself

For ²⁸Si/³⁰Si:    7.1% discriminator
For ¹⁰⁶Ag/¹⁰⁸Ag:  1.9% discriminator
For ¹⁸²W/¹⁸⁴W:   1.1% discriminator

Experimental precision needed to detect the discriminator:
    Si pair: <5% precision on rate ratio
    Ag pair: <1% precision on rate ratio
    W pair:  <0.5% precision on rate ratio

MAQRO and matter-wave-interferometry programs target precisions in
the ~1-10% range over the next decade, putting the Ag and Si
discriminators within experimental reach.

References
----------
- Bassi, Lochan, Satin, Singh, Ulbricht (2013), Rev. Mod. Phys. 85, 471.
- Pearle (1989), Phys. Rev. A 39, 2277.
- Ghirardi, Pearle, Rimini (1990), Phys. Rev. A 42, 78.
- Adler (2007), J. Phys. A 40, 2935.
- IUPAC 2021 atomic masses.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


# ─────────────────────────────────────────────────────────────────────
# Isotope data (IUPAC 2021)
# ─────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class Isotope:
    name: str          # e.g. "106Ag"
    element: str
    Z: int             # atomic number (proton count)
    A: int             # mass number (nucleon count)
    mass_amu: float    # accurate atomic mass in amu


# Selected isotopes — all stable, IUPAC 2021 atomic masses
ISOTOPES: dict[str, Isotope] = {
    # Silicon — large mass-ratio discriminator (~7%)
    "28Si":   Isotope("28Si", "Si",  14,  28,  27.9769265),
    "29Si":   Isotope("29Si", "Si",  14,  29,  28.9764947),
    "30Si":   Isotope("30Si", "Si",  14,  30,  29.9737702),
    # Silver — moderate discriminator (~2%); tractable for nanoparticle synthesis
    "107Ag":  Isotope("107Ag", "Ag", 47, 107, 106.905097),
    "109Ag":  Isotope("109Ag", "Ag", 47, 109, 108.904752),
    # Approximate "106Ag/108Ag" as 107Ag/109Ag (closest naturally-stable pair).
    # 106Ag and 108Ag are radioactive; experiments use 107/109.
    # Tungsten — small discriminator (~1%); high-mass for stronger absolute signal
    "182W":   Isotope("182W", "W",  74, 182, 181.948205),
    "184W":   Isotope("184W", "W",  74, 184, 183.950932),
    "186W":   Isotope("186W", "W",  74, 186, 185.954362),
}


# ─────────────────────────────────────────────────────────────────────
# Isotope pair predictions
# ─────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class IsotopePair:
    """A pair (lighter, heavier) of isotopes of the same element."""
    light: Isotope
    heavy: Isotope

    def __post_init__(self) -> None:
        # Sanity: same element, light < heavy in mass
        assert self.light.element == self.heavy.element, (
            f"isotope pair must be same element: "
            f"{self.light.element} vs {self.heavy.element}"
        )
        assert self.light.mass_amu < self.heavy.mass_amu

    @property
    def name(self) -> str:
        return f"{self.heavy.name}/{self.light.name}"

    @property
    def mass_ratio(self) -> float:
        """heavy/light, > 1."""
        return self.heavy.mass_amu / self.light.mass_amu

    @property
    def nucleon_ratio(self) -> float:
        return self.heavy.A / self.light.A


# ─────────────────────────────────────────────────────────────────────
# Predicted decoherence-rate ratios
# ─────────────────────────────────────────────────────────────────────

def grut_predicted_ratio(pair: IsotopePair) -> float:
    """GRUT: Λ ∝ m² → Λ_heavy/Λ_light = (m_heavy/m_light)².

    Zero free parameters. Direct consequence of the noise kernel
    N_grav(x,x') = G/(ℏ|x-x'|) producing Λ_grav = Gm²S(l/R)/(ℏl)
    when the geometry factor S(l/R) is held fixed by isotope
    substitution (identical chemistry → identical R, identical l).
    """
    return pair.mass_ratio ** 2


def csl_predicted_ratio_linear_n(pair: IsotopePair) -> float:
    """Standard CSL (large-system regime, l > r_C ≈ 100 nm):
    Λ_CSL ∝ λ × N → ratio = N_heavy/N_light ≈ mass ratio.

    λ cancels in the ratio. The ratio depends only on the structural
    linear-in-N scaling, which is shared across CSL formulations
    (Pearle 1989, Bassi-Pearle 2013).
    """
    return pair.nucleon_ratio


def csl_predicted_ratio_mass_proportional(pair: IsotopePair) -> float:
    """Adler mass-proportional CSL: Λ_CSL ∝ λ × m → ratio = m_heavy/m_light."""
    return pair.mass_ratio


def csl_predicted_ratio_coherent_small_system(pair: IsotopePair) -> float:
    """Small-system regime (l ≪ r_C): coherent enhancement scales as N².
    For matched-atom-count nanoparticles, this ratio ≈ (N_heavy/N_light)².

    NOT typical for matter-wave interferometry (l ≈ μm > r_C ≈ 100 nm).
    Listed for completeness — predicts the same quadratic scaling as
    GRUT in this regime, BUT only in the small-system limit which is
    not the experimental regime."""
    return pair.nucleon_ratio ** 2


# ─────────────────────────────────────────────────────────────────────
# Discriminator analysis
# ─────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class DiscriminatorReport:
    pair_name: str
    grut_ratio: float
    csl_linear_n_ratio: float
    csl_mass_prop_ratio: float
    csl_coherent_ratio: float
    """CSL coherent (small-system) — listed for completeness, not experimentally relevant."""
    grut_minus_csl_linear_pct: float
    """% difference between GRUT and CSL-linear predictions."""
    discriminating_precision_required: float
    """Experimental precision (in fractional units) needed to detect the
    GRUT-vs-CSL-linear discriminator at 1σ."""


def discriminator_report(pair: IsotopePair) -> DiscriminatorReport:
    grut = grut_predicted_ratio(pair)
    csl_n = csl_predicted_ratio_linear_n(pair)
    csl_m = csl_predicted_ratio_mass_proportional(pair)
    csl_coh = csl_predicted_ratio_coherent_small_system(pair)
    diff_pct = (grut - csl_n) / csl_n * 100.0
    # Required precision: difference / 2 for 2σ-level discrimination
    # (i.e., experiment must resolve the gap between predictions)
    precision = abs(grut - csl_n) / 2.0
    return DiscriminatorReport(
        pair_name=pair.name,
        grut_ratio=grut,
        csl_linear_n_ratio=csl_n,
        csl_mass_prop_ratio=csl_m,
        csl_coherent_ratio=csl_coh,
        grut_minus_csl_linear_pct=diff_pct,
        discriminating_precision_required=precision,
    )


# ─────────────────────────────────────────────────────────────────────
# Canonical pairs
# ─────────────────────────────────────────────────────────────────────

CANONICAL_PAIRS: tuple[IsotopePair, ...] = (
    IsotopePair(ISOTOPES["28Si"], ISOTOPES["30Si"]),
    IsotopePair(ISOTOPES["107Ag"], ISOTOPES["109Ag"]),
    IsotopePair(ISOTOPES["182W"], ISOTOPES["184W"]),
)


def all_reports() -> tuple[DiscriminatorReport, ...]:
    return tuple(discriminator_report(p) for p in CANONICAL_PAIRS)


# ─────────────────────────────────────────────────────────────────────
# Markdown rendering
# ─────────────────────────────────────────────────────────────────────

def render_table() -> str:
    """Render the discriminator table for the ToE document."""
    out = []
    out.append("| Pair | mass ratio | GRUT (m²) | CSL linear-N | "
               "Discriminator | Precision needed |")
    out.append("|:---|---:|---:|---:|---:|---:|")
    for r in all_reports():
        # Find the pair to get mass ratio for display
        pair = next(
            p for p in CANONICAL_PAIRS if p.name == r.pair_name
        )
        out.append(
            f"| {r.pair_name} | {pair.mass_ratio:.4f} | "
            f"{r.grut_ratio:.4f} | {r.csl_linear_n_ratio:.4f} | "
            f"{r.grut_minus_csl_linear_pct:+.2f}% | "
            f"{r.discriminating_precision_required*100:.2f}% |"
        )
    return "\n".join(out)


def render_full_report() -> str:
    out = []
    out.append("# GRUT-vs-CSL Isotope-Pair Discriminator")
    out.append("")
    out.append(
        "*Auto-generated from `grut/derived/decoherence/csl_discriminator.py`.*"
    )
    out.append("")
    out.append(
        "GRUT predicts decoherence rate Λ ∝ m² (quadratic in mass). "
        "CSL predicts Λ ∝ λN (or λm), linear in nucleon count or mass. "
        "Isotope substitution within the same element holds geometry "
        "and chemistry constant, isolating the mass-scaling difference "
        "as a clean, parameter-cancelling discriminator (λ drops out "
        "of the ratio)."
    )
    out.append("")
    out.append("## Predictions")
    out.append("")
    out.append(render_table())
    out.append("")
    out.append("## Discriminator framing")
    out.append("")
    out.append(
        "GRUT is parameter-free at this scale. The prediction "
        "Λ_grav = Gm² S(l/R) / (ℏl) has every input known. "
        "Isotope substitution at fixed geometry gives "
        "ratio = (m_heavy/m_light)² with no free parameter."
    )
    out.append("")
    out.append(
        "CSL has localization parameter λ as a free input. Different "
        "published λ values (GRW λ ≈ 10⁻¹⁶ s⁻¹, Adler enhanced, "
        "Bassi-Pearle range) span orders of magnitude. The CSL-"
        "predicted ABSOLUTE rate is λ-dependent. But the CSL ratio "
        "between isotopes is λ-INDEPENDENT — λ cancels."
    )
    out.append("")
    out.append(
        "So the GRUT-vs-CSL discriminator is purely STRUCTURAL: "
        "quadratic vs linear scaling. The discriminator factor is "
        "approximately the mass ratio itself (1-7% across the "
        "isotope pairs above)."
    )
    out.append("")
    out.append("## Experimental program")
    out.append("")
    out.append(
        "Matter-wave interferometry programs (MAQRO, MAGIS-100, "
        "atom interferometers, optomechanical levitation) target "
        "decoherence-rate precisions in the ~1-10% range over the "
        "next decade. The Si pair is detectable at <5% precision; "
        "the Ag pair at <1%; the W pair at <0.5%. MAQRO's design "
        "sensitivity puts the Si and Ag discriminators within reach."
    )
    out.append("")
    out.append("## Detailed entries")
    out.append("")
    for r in all_reports():
        pair = next(p for p in CANONICAL_PAIRS if p.name == r.pair_name)
        out.append(f"### {r.pair_name}")
        out.append("")
        out.append(f"- **Element:** {pair.heavy.element}")
        out.append(f"- **Light isotope:** {pair.light.name} "
                   f"(m = {pair.light.mass_amu:.6f} amu)")
        out.append(f"- **Heavy isotope:** {pair.heavy.name} "
                   f"(m = {pair.heavy.mass_amu:.6f} amu)")
        out.append(f"- **Mass ratio (heavy/light):** {pair.mass_ratio:.6f}")
        out.append(f"- **GRUT predicted ratio (m²):** {r.grut_ratio:.6f}")
        out.append(f"- **CSL predicted ratio (linear-N):** {r.csl_linear_n_ratio:.6f}")
        out.append(f"- **CSL predicted ratio (Adler mass-prop):** "
                   f"{r.csl_mass_prop_ratio:.6f}")
        out.append(f"- **GRUT − CSL difference:** {r.grut_minus_csl_linear_pct:+.3f}%")
        out.append(f"- **Discriminating precision required:** "
                   f"{r.discriminating_precision_required*100:.3f}% "
                   f"(2σ-level)")
        out.append("")
    return "\n".join(out)


# ─────────────────────────────────────────────────────────────────────
# Verification harness
# ─────────────────────────────────────────────────────────────────────

def verify() -> dict:
    reports = all_reports()
    return {
        # (1) GRUT predictions are quadratic — always larger than CSL linear
        "grut_predicts_larger_than_csl_for_heavy_isotope": all(
            r.grut_ratio > r.csl_linear_n_ratio for r in reports
        ),
        # (2) Si pair has the largest discriminator (~7%)
        "si_discriminator_above_5_pct": (
            abs(reports[0].grut_minus_csl_linear_pct) > 5.0
        ),
        # (3) Ag pair has moderate discriminator (~2%)
        "ag_discriminator_around_2_pct": (
            1.0 < abs(reports[1].grut_minus_csl_linear_pct) < 3.0
        ),
        # (4) W pair has the smallest discriminator (~1%)
        "w_discriminator_around_1_pct": (
            0.5 < abs(reports[2].grut_minus_csl_linear_pct) < 2.0
        ),
        # (5) The discriminator factor is approximately the mass ratio
        # (since GRUT/CSL = m²/m = m, structural relation)
        "discriminator_matches_mass_ratio_minus_one": all(
            abs(
                r.grut_minus_csl_linear_pct / 100.0
                - (CANONICAL_PAIRS[i].mass_ratio - 1.0)
            ) < 0.005
            for i, r in enumerate(reports)
        ),
        # (6) λ-independence: CSL linear-N and Adler mass-prop give nearly
        # the same ratio (since N ≈ m in amu) — both are λ-independent in ratio
        "csl_variants_agree_to_0p1_pct": all(
            abs(r.csl_linear_n_ratio - r.csl_mass_prop_ratio)
            / r.csl_linear_n_ratio < 0.001
            for r in reports
        ),
    }


if __name__ == "__main__":
    print(render_full_report())
    print()
    print("Verify:")
    for k, v in verify().items():
        mark = "PASS" if v else "FAIL"
        print(f"  [{mark}] {k}")
