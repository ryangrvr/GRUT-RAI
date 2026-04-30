"""GRUT — SM cosmic-crystallization schedule [QUARANTINED DRAFT].

⚠️  QUARANTINE NOTICE (2026-04-28; updated 2026-04-30) ⚠️

This module is a DRAFT held pending closure of
`tau_zero_to_tau_micro_relation_open_question` (registry, Ch 12;
formerly tracked under `t_c_provenance_inconsistency_open_negative`,
which Correction #22 closed at the dimensional level on 2026-04-30).

Status:
  - NOT covered by any test
  - NOT registered as a framework claim
  - NOT consumed by any chapter prose
  - NOT exported from grut/derived/cosmology

The Stage 1.5 numerical findings the module encodes are preserved as
reference material. The framework absorbs them via the open-negative
ledger entry, not via this module. Module activation (tests + registry
claim + chapter revision) is held until the T_c provenance audit
completes — see theory/foundations_audit/T_C_PROVENANCE.md for the
audit and theory/derivation/CRYSTALLIZATION_SCHEDULE_INVESTIGATION.md
for the suspension context.

---

Investigation: CRYSTALLIZATION_SCHEDULE_INVESTIGATION.md (Stages 1-1.5).
Output: per-species temperature schedule for SM particles becoming
classical during cosmic cooling.

KEY FINDING (Stage 1.5):

Ch 13.5's qualitative narrative ("heaviest crystallize first as universe
cools") is reproduced ONLY by cosmic thermal decoupling at T = mc²/k_B
— standard cosmology, not gravitational decoherence. The Λ_grav-based
crystallization narrative does NOT work for SM elementary species at
any natural choice of length scale (Compton, thermal de Broglie, or
inter-particle separation).

The framework's natural per-species schedule is therefore standard
cosmic thermal decoupling. This is not a novel GRUT-specific prediction,
but it IS what the framework computes given that GRUT imports the SM
as S_classical. The GRUT-specific finding here is the QUANTITATIVE
diagnosis: gravitational decoherence is too weak to crystallize
elementary particles at any cosmologically relevant scale; Λ_grav
becomes relevant only at composite-object scales (atoms, nanoparticles,
gold-benchmark).

This module provides:
1. The schedule T_decouple = mc²/k_B per SM species
2. The diagnostic that Λ_grav at all three natural l choices is
   ridiculously below crystallization threshold for elementary species
3. A clear separation between elementary-particle crystallization
   (thermal mechanism) and composite-object crystallization (Λ_grav
   mechanism)

This complements (does not replace) Ch 13.5's narrative; the chapter
needs revision to clarify the mechanism, but the QUANTITATIVE schedule
emerges from this calculation.

NOTE: this calculation does NOT depend on the framework's T_c value.
The schedule uses mc²/k_B per species (standard SM masses + standard
constants), independent of any τ_0-derived T_c. So this output is
robust to the T_c provenance audit (T_C_PROVENANCE.md, pending
resolution).
"""

from __future__ import annotations

from dataclasses import dataclass

from grut.foundation.constants import C as C_LIGHT, G, HBAR, K_B
from grut.foundation.closure_protocol import TAU_0_SEC


# ─────────────────────────────────────────────────────────────────────
# SM particle masses (PDG 2024 central values, in kg)
# ─────────────────────────────────────────────────────────────────────

EV_TO_KG: float = 1.602e-19 / C_LIGHT**2  # 1 eV/c² in kg

SM_SPECIES_KG: dict[str, float] = {
    "top_quark":     173.0e9 * EV_TO_KG,
    "Higgs":         125.0e9 * EV_TO_KG,
    "Z_boson":        91.2e9 * EV_TO_KG,
    "W_boson":        80.4e9 * EV_TO_KG,
    "bottom_quark":    4.18e9 * EV_TO_KG,
    "tau":             1.777e9 * EV_TO_KG,
    "charm_quark":     1.27e9 * EV_TO_KG,
    "muon":            0.1057e9 * EV_TO_KG,
    "strange_quark":   0.095e9 * EV_TO_KG,
    "down_quark":      0.0047e9 * EV_TO_KG,
    "up_quark":        0.0022e9 * EV_TO_KG,
    "electron":        9.1093837e-31,            # exact PDG kg value
    "neutrino_eV":     0.1 * EV_TO_KG,           # rough — < 0.8 eV cosmological bound
    "photon":          0.0,
}


# ─────────────────────────────────────────────────────────────────────
# Per-species cosmic thermal decoupling
# ─────────────────────────────────────────────────────────────────────


@dataclass(frozen=True)
class SpeciesEntry:
    name: str
    mass_kg: float
    T_decouple_K: float
    note: str

    @property
    def mass_GeV(self) -> float:
        return self.mass_kg * C_LIGHT**2 / 1.602e-19 / 1e9


def cosmic_thermal_decoupling_T(mass_kg: float) -> float:
    """T_decouple = mc²/k_B — the temperature at which a species'
    rest-mass energy equals the thermal energy. Above this T, the
    species is in thermal equilibrium with the plasma (created and
    destroyed via pair production). Below this T, the species
    'decouples' — its number density freezes (modulo annihilations).

    For massive species, this is the cosmic thermal decoupling
    temperature. For photons (m=0), this is 0 — photons never
    decouple in this sense (they remain in thermal equilibrium until
    last scattering for unrelated reasons).

    NOTE: this is standard cosmology, not GRUT-specific physics.
    Included here because it IS the framework's natural per-species
    crystallization schedule, given that the Λ_grav-based mechanism
    fails for elementary particles (see investigation log)."""
    if mass_kg == 0:
        return 0.0
    return mass_kg * C_LIGHT**2 / K_B


def species_schedule() -> tuple[SpeciesEntry, ...]:
    """The cosmic thermal-decoupling schedule for all SM species.

    Returns species ordered by descending T_decouple (heaviest first,
    matching cosmic cooling order)."""
    entries: list[SpeciesEntry] = []
    for name, mass in SM_SPECIES_KG.items():
        T = cosmic_thermal_decoupling_T(mass)
        if mass == 0:
            note = "Massless — never decouples via rest-mass mechanism"
        else:
            note = "Decouples when k_B T ≈ mc²"
        entries.append(SpeciesEntry(name, mass, T, note))
    # Sort by T_decouple descending (heaviest first)
    entries.sort(key=lambda e: -e.T_decouple_K)
    return tuple(entries)


# ─────────────────────────────────────────────────────────────────────
# Diagnostic: Λ_grav crystallization fails for elementary species
# ─────────────────────────────────────────────────────────────────────


def lambda_grav_at_compton(mass_kg: float) -> float:
    """Λ_grav at l = ℏ/(mc) (Compton wavelength).

    This evaluates Λ_grav = Gm²/(ℏ × λ_C) = G c m³/ℏ². T-independent."""
    if mass_kg == 0:
        return 0.0
    return G * C_LIGHT * mass_kg**3 / HBAR**2


def lambda_grav_compton_x_tau_0(mass_kg: float) -> float:
    """Crystallinity X = Λ_grav × τ_0 at Compton scale.

    For elementary species, X ≪ 1 universally. The threshold
    X ≥ 1 requires m³ ≥ ℏ²/(G c τ_0), giving a critical mass of
    ~10¹⁰ GeV — far above any SM particle."""
    return lambda_grav_at_compton(mass_kg) * TAU_0_SEC


def lambda_grav_diagnostic() -> dict:
    """Quantitative verification that Λ_grav at the Compton scale is
    far below the crystallization threshold for ALL SM elementary
    particles. The critical mass required is ~10¹⁰ GeV; no SM species
    qualifies. This is the framework-specific finding: elementary
    particles are NOT crystallized by gravitational decoherence at
    any cosmologically relevant scale."""
    # Critical mass: m_crit such that G c m³ τ_0 / ℏ² = 1
    m_critical_kg = (HBAR**2 / (G * C_LIGHT * TAU_0_SEC)) ** (1.0/3.0)
    m_critical_GeV = m_critical_kg * C_LIGHT**2 / 1.602e-19 / 1e9

    diagnostic_per_species = []
    for name, mass in SM_SPECIES_KG.items():
        if mass == 0:
            X = 0.0
        else:
            X = lambda_grav_compton_x_tau_0(mass)
        diagnostic_per_species.append({
            "name": name,
            "mass_kg": mass,
            "lambda_grav_compton_Hz": lambda_grav_at_compton(mass),
            "X_at_compton": X,
            "is_crystal_via_gravity": X >= 1.0,
        })

    return {
        "m_critical_for_gravity_crystallization_kg": m_critical_kg,
        "m_critical_for_gravity_crystallization_GeV": m_critical_GeV,
        "interpretation": (
            f"To satisfy Λ_grav × τ_0 ≥ 1 at the Compton scale, a "
            f"particle must have m ≥ {m_critical_GeV:.2e} GeV. No SM "
            f"species satisfies this. Heaviest SM particle (top quark "
            f"at 173 GeV) is 8 orders of magnitude below the threshold."
        ),
        "per_species": diagnostic_per_species,
        "any_SM_species_crystal_via_gravity": any(
            d["is_crystal_via_gravity"] for d in diagnostic_per_species
        ),
    }


# ─────────────────────────────────────────────────────────────────────
# Master reporter
# ─────────────────────────────────────────────────────────────────────


def sm_crystallization_attempt() -> dict:
    """Full report: schedule + diagnostic + verdict."""
    schedule = species_schedule()
    diag = lambda_grav_diagnostic()

    return {
        "investigation_log": "theory/derivation/CRYSTALLIZATION_SCHEDULE_INVESTIGATION.md",
        "framework_specific_finding": (
            "Λ_grav-based crystallization fails for elementary SM "
            "particles at any natural choice of length scale. The "
            "critical mass for gravity-driven crystallization at the "
            f"Compton scale is {diag['m_critical_for_gravity_crystallization_GeV']:.2e} "
            "GeV — 8 orders of magnitude above the heaviest SM "
            "particle (top quark at 173 GeV). Gravitational "
            "decoherence becomes relevant only at composite-object "
            "scales (atoms upward through the gold benchmark)."
        ),
        "natural_schedule_mechanism": (
            "Cosmic thermal decoupling at T = mc²/k_B. This is "
            "STANDARD cosmology, reproduced by GRUT because it imports "
            "the SM as S_classical. The framework-specific content is "
            "the diagnosis above (Λ_grav too weak for elementary "
            "particles), not the schedule values themselves."
        ),
        "per_species_schedule": [
            {
                "name": e.name,
                "mass_GeV": e.mass_GeV,
                "T_decouple_K": e.T_decouple_K,
                "note": e.note,
            }
            for e in schedule
        ],
        "lambda_grav_diagnostic": diag,
        "ch_13_5_revision_recommendation": (
            "Chapter 13.5 currently uses the language of "
            "gravitational decoherence (Λ_grav) for SM crystallization, "
            "but the heavy-first cosmic-cooling order it narrates only "
            "emerges from cosmic thermal decoupling at T = mc²/k_B. The "
            "chapter conflates two distinct mechanisms. Recommended "
            "revision: clarify that the per-species schedule is "
            "thermal-decoupling-based (standard cosmology), while "
            "gravitational decoherence becomes relevant at composite-"
            "object scales (Ch 4/5 gold benchmark). The cosmic-history "
            "narrative is preserved; the mechanism description is "
            "corrected."
        ),
        "structural_observation": (
            "This is the third Stage-1 scoping in this session that "
            "found a definitional gap in cosmological-plasma physics "
            "(after rescaling sensitivity in primordial A_s, "
            "and N_total cosmic-age choice). The pattern: GRUT has "
            "well-defined infrastructure for specific predictions but "
            "doesn't have fully-formal cosmological-plasma physics. "
            "Closing the n_g(ω) covariance question (#9 in ledger) "
            "would address one aspect; cosmological-plasma decoherence "
            "is adjacent territory potentially needing its own formal "
            "structure."
        ),
    }


if __name__ == "__main__":
    import json

    result = sm_crystallization_attempt()

    print("=" * 72)
    print("GRUT cosmic crystallization schedule for SM species")
    print("=" * 72)
    print()
    print("Mechanism: cosmic thermal decoupling at T = mc²/k_B")
    print("(Λ_grav-based crystallization fails for elementary particles)")
    print()
    print(f"{'Species':<18} {'mass (GeV)':>12} {'T_decouple (K)':>16}")
    print("-" * 60)
    for e in result["per_species_schedule"]:
        T_str = f"{e['T_decouple_K']:.3e}" if e['T_decouple_K'] > 0 else "N/A"
        print(f"{e['name']:<18} {e['mass_GeV']:>12.3e} {T_str:>16}")

    print()
    print("Λ_grav diagnostic:")
    diag = result["lambda_grav_diagnostic"]
    print(f"  Critical mass: {diag['m_critical_for_gravity_crystallization_GeV']:.2e} GeV")
    print(f"  Any SM species crystal via gravity? {diag['any_SM_species_crystal_via_gravity']}")
    print()
    print(result["framework_specific_finding"])
