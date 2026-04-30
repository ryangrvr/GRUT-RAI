# Crystallization Temperature Schedule for SM Species — Investigation

**Status: HELD (Stages 2-4 suspended) — blocked by `t_c_provenance_inconsistency_open_negative`.**

**Started:** 2026-04-28.
**Trigger:** Ch 13.5 of the GRUT ToE document carries a `[CLAUDE CODE INPUT REQUIRED]` marker for the per-species crystallization schedule. The Λ_grav infrastructure exists in `grut/foundation/noise_kernel.py`; this investigation applies it to thermal SM cosmology.

**Methodological constraint:** Surface multiple plausible options explicitly. Don't pick one silently. The pattern from the A_s investigation: definitional choices that the framework hasn't pinned should be reported as conditional results, not steered.

---

## Suspension notice (2026-04-28)

This investigation is HELD pending closure of
`t_c_provenance_inconsistency_open_negative` (registry, Ch 12). The
T_c provenance audit (`theory/foundations_audit/T_C_PROVENANCE.md`)
surfaced a foundational issue: the framework has been using one
symbol (τ_0) and one formula (T_c = 1/(τ_0 k_B)) for two distinct
physical scales — the macroscopic gravitational relaxation time
τ_0 = 41.9 Myr and an implicit microscopic plasma relaxation time
τ_micro ≈ 1.4×10⁻¹⁹ s.

The crystallization investigation's Stage 1.5 finding — that Λ_grav-
based crystallization fails for elementary SM species at any natural
choice of length scale, and the heavy-first cosmic-cooling order
emerges only from cosmic thermal decoupling at T = mc²/k_B — is
orthogonal to the T_c question and remains valid. But Ch 13.5's
mechanism conflation (using Λ_grav language for what is actually
thermal-decoupling physics) should not be revised in the document
until T_c is resolved, because Ch 13.5's "T_c crossing at 1 hour
post-BB" framing depends on T_c provenance closure.

The draft module `grut/derived/cosmology/sm_crystallization_schedule.py`
stays quarantined: NO tests, NO registry-claim registration, NO
chapter revision proposal until T_c resolves. After T_c closes, the
crystallization investigation can complete cleanly with the
disambiguated τ scales.

**Stage 1 and Stage 1.5 findings below are preserved as the
investigation log up to the suspension point.** They document what
was learned; they don't drive any framework change yet.

---

## Stage 1 — Define the calculation precisely

### The crystallization condition

The framework's regime classification (Ch 4): crystallinity X = max(ω, Λ_grav) × τ₀.

For a thermal species, the dominant dynamical frequency is ω_T = k_B T / ℏ (the thermal-fluctuation frequency). Gross crystallinity X > 1 holds either via thermal (ω_T τ₀ > 1, i.e., T > T_c = ℏ/(k_B τ₀) = 54.7 MK) OR via gravitational (Λ_grav τ₀ > 1).

Two physically distinct conditions one could call "crystallization":

| Condition | Formula | Physical meaning |
|:---|:---|:---|
| **(1) Gross crystallinity** | Λ_grav × τ₀ = 1 | Below T_c, when does the species drop out of (or into) crystal regime? |
| **(2) Gravity-thermal balance** | Λ_grav = ω_T = k_B T / ℏ | When does gravitational decoherence overtake thermal motion? |

These are different physical questions. Ch 13.5's prose mixes them: "Particles whose Λ_grav exceeds their thermal fluctuation frequency cross the crystalline boundary" reads like (2), but the chapter's overall narrative ("heaviest crystallize first as universe cools") fits (1).

**Stage 2 commits to condition (1)** — gross crystallinity Λ_grav × τ₀ = 1 — because:
- It's the framework-native X = max(ω, Λ_grav) × τ₀ regime boundary
- Below T_c, ω_T τ₀ < 1 so X = Λ_grav τ₀ exclusively
- Condition (2) gives ridiculously low T_cryst (10⁻⁵¹ K for top quark, 10⁻⁸⁰ K for electron) — never relevant cosmologically

### The thermal length scale l_thermal

This is the load-bearing definitional choice. For a thermal SM particle, three scales are physically defensible:

| Scale | Formula | Physical meaning |
|:---|:---|:---|
| **(A) Compton wavelength** | λ_C = ℏ/(mc) | Relativistic-particle localization; T-independent; m-dependent |
| **(B) Thermal de Broglie wavelength** | λ_th = ℏ/√(2π m k_B T) | Quantum coherence length at temperature T; T- and m-dependent |
| **(C) Inter-particle separation** | l_inter ≈ ℏc/(k_B T) (relativistic) | Mean separation between plasma constituents; T-dependent; m-independent |

**The framework does NOT natively pin which is correct for cosmological thermal particles.** The decoherence-rate formula Λ_grav was derived for a body at distance l from another body. For a single particle in cosmic plasma, the "other body" is ambiguous:

- (A) Compton: treats the particle as a point object at its own intrinsic quantum scale. Natural for a particle in vacuum.
- (B) Thermal de Broglie: the particle's quantum extent at finite T. Natural if "decoherence" means decoherence of the particle's own wavefunction.
- (C) Inter-particle: distance to nearest neighbor in plasma. Natural for "decoherence between two particles in plasma."

Each gives a different T_cryst, with different mass-ordering. This sensitivity is the central Stage-1 finding to report in Stage 2.

### The screening factor S(l/R)

S(l/R) = min(1, (l/R)³/6) appears in Λ_grav for extended bodies. For point particles (R → 0), the ratio l/R → ∞ and S = 1 trivially.

**For elementary SM species, S = 1.** This is unambiguous — there's no screening for point particles. (The screening factor matters for composite objects like the gold-benchmark nanoparticle, not for single quarks/leptons.)

### Pre-Stage-2 algebraic predictions

For each scale choice, I can derive T_cryst symbolically and check the mass-ordering:

**Scale (A) — Compton.** l = ℏ/(mc), so:

    Λ_grav = Gm² × mc / ℏ² = G c m³ / ℏ²

This is T-independent. Setting Λ_grav × τ₀ = 1:

    G c m³ τ₀ / ℏ² = 1
    m_critical = (ℏ² / (G c τ₀))^(1/3)

This gives a critical *mass*, not a critical temperature. Λ_grav × τ₀ > 1 iff m > m_critical (mass-only condition). For arbitrary T with Compton scale, the calculation has no T-dependence — the T_cryst is undefined.

Numerically: m_critical = (1.10×10⁻⁶⁸ / (6.67×10⁻¹¹ × 3×10⁸ × 1.32×10¹⁵))^(1/3) = (4.16×10⁻⁵⁹ kg³)^(1/3) ≈ 3.5×10⁻²⁰ kg ≈ 2×10¹⁰ GeV.

**No SM particle is anywhere near 2×10¹⁰ GeV.** Top quark (173 GeV) is 8 orders of magnitude below. Electron is 13 orders of magnitude below.

So under Scale (A), NO SM species is in the gross-crystal regime via gravity at the Compton scale. All SM species are in the gravity-fluid regime at Compton scale, regardless of T.

**Scale (B) — Thermal de Broglie.** l = ℏ/√(2π m k_B T), so:

    Λ_grav = Gm² × √(2π m k_B T) / ℏ²

Setting Λ_grav × τ₀ = 1 and solving for T:

    T_cryst(B) = ℏ⁴ / (2π G² m⁵ k_B τ₀²) ∝ 1/m⁵

**Mass-ordering (B):** lighter species → HIGHER T_cryst. As universe cools through this T_cryst, lighter species cross the boundary at higher T (heavy species cross at lower T).

This is BACKWARDS from Ch 13.5's narrative. The chapter says heavy species crystallize first as universe cools; the calculation under (B) says light species cross the gravity-boundary first.

Pre-Stage-2 numerical estimates:
- Top quark: T_cryst(B) ≈ 0.006 K (very cold — way below CMB)
- Electron: T_cryst(B) ≈ 3×10²⁶ K (way above T_c, near Planck)

**Scale (C) — Inter-particle separation.** l = ℏc/(k_B T), so:

    Λ_grav = Gm² × k_B T / (ℏ² c)

Setting Λ_grav × τ₀ = 1:

    T_cryst(C) = ℏ² c / (G m² k_B τ₀) ∝ 1/m²

**Mass-ordering (C):** lighter species → HIGHER T_cryst. Same direction as (B) but milder slope (1/m² vs 1/m⁵).

Pre-Stage-2 numerical estimates:
- Top quark: T_cryst(C) ≈ 2.8×10⁷ K ≈ T_c/2 (just below T_c — physically interesting)
- Electron: T_cryst(C) ≈ 3.3×10¹⁸ K (above T_c, well below Planck)

### Stage-1 honest read

The calculation IS computable per species under any of the three scale choices, but:

1. **Scale (A) Compton:** Reduces to a mass condition with critical mass ~10¹⁰ GeV. No SM species qualifies. The "crystallization temperature" is undefined under this choice.

2. **Scale (B) Thermal de Broglie:** Gives T_cryst ∝ 1/m⁵ with mass-ordering OPPOSITE to Ch 13.5's narrative. Top quark: 0.006 K. Electron: 3×10²⁶ K.

3. **Scale (C) Inter-particle separation:** Gives T_cryst ∝ 1/m² with mass-ordering OPPOSITE to Ch 13.5's narrative. Top quark: 2.8×10⁷ K (near T_c). Electron: 3.3×10¹⁸ K.

**Critical methodological observation:** Ch 13.5's qualitative narrative ("heaviest crystallize first as universe cools") doesn't match what the framework actually computes under any of the three scales. Either:

- (i) The narrative is wrong and the chapter needs revision to match the framework's actual prediction;
- (ii) The narrative is right but it's about a DIFFERENT crystallization mechanism (e.g., thermal-frequency mechanism, where heavy species have higher ω_T = m c²/ℏ relativistically, but ω_T = k_B T/ℏ for any thermal mode — so this doesn't help);
- (iii) The narrative refers to crystallization-by-internal-dynamics (heavy particles have higher rest-mass-frequency m c²/ℏ → ω·τ₀ = m c² τ₀/ℏ which IS m-dependent and IS heavier-first), not gravitational decoherence.

**Reading (iii) is most likely physically correct.** A particle with rest mass m has an intrinsic frequency ω_rest = m c²/ℏ from its Compton scale. This is the "internal clock" of the particle. ω_rest × τ₀ = m c² τ₀ / ℏ:
- Top quark: 173 GeV × τ₀ / ℏ = 5.55×10²⁵ × 1.32×10¹⁵ / (in correct units) ≈ very large
- Electron: 0.511 MeV × τ₀ / ℏ ≈ smaller but still large

Heavy species have larger ω_rest, hence larger ω_rest × τ₀, crystallize first by this metric. **This is heavier-first, matching Ch 13.5's narrative.**

So a *fourth* scale interpretation surfaces: what Ch 13.5 actually means is the **rest-mass frequency** mechanism, not gravitational decoherence at any scale. Crystallization happens when ω_rest × τ₀ > 1, which is m c² > ℏ/τ₀ = k_B T_c, i.e., when the particle's rest-mass energy exceeds the thermal energy at T_c.

### Refined Stage-1 conclusion

There are FOUR plausible interpretations of Ch 13.5's "crystallization":

| Scale | Formula | T_cryst range | Mass-ordering |
|:---|:---|:---|:---|
| (A) Compton — Λ_grav | Mass condition only | undefined (no SM species qualifies) | N/A |
| (B) Thermal de Broglie — Λ_grav | T ∝ 1/m⁵ | 0.006 K (top) to 10²⁶ K (electron) | Light species cross boundary first |
| (C) Inter-particle — Λ_grav | T ∝ 1/m² | 2.8×10⁷ K (top) to 10¹⁸ K (electron) | Light species cross boundary first |
| **(D) Rest-mass frequency — ω_rest** | mc² > k_B T (at T_c boundary) | varies per species | **Heavy species cross boundary first** |

Ch 13.5's narrative is consistent with interpretation (D) — rest-mass-frequency mechanism. Interpretations (A), (B), (C) all use Λ_grav (gravitational decoherence) and all give mass-orderings inconsistent with the chapter.

**The honest Stage-2 deliverable** therefore should compute the schedule under all four interpretations and document which (if any) matches the chapter's narrative. The framework's actual prediction depends on which interpretation is the intended one — that's the central finding to report.

---

## Stage 1.5 — Numerical comparison across all four interpretations

Per refined Stage-1 prompt: compute T_cryst under all four interpretations
for representative SM species, apply sanity checks, surface explicit
sensitivity to scale choice. Don't pick silently.

### Per-species results (T_cryst in Kelvin)

| Species | mass (kg) | (A) Compton | (B) thermal de Broglie | (C) inter-particle | (D) rest-mass T = mc²/k_B |
|:---|:---|:---|:---|:---|:---|
| top quark    | 3.08×10⁻²⁵ | crystal (T-indep) | 0.066 K | 2.88×10⁷ K | 2.01×10¹⁵ K |
| Higgs        | 2.23×10⁻²⁵ | crystal (T-indep) | 0.333 K | 5.51×10⁷ K | 1.45×10¹⁵ K |
| Z boson      | 1.63×10⁻²⁵ | crystal (T-indep) | 1.6 K | 1.04×10⁸ K | 1.06×10¹⁵ K |
| W boson      | 1.43×10⁻²⁵ | crystal (T-indep) | 3.0 K | 1.33×10⁸ K | 9.33×10¹⁴ K |
| bottom quark | 7.45×10⁻²⁷ | crystal (T-indep) | 7.97×10⁶ K | 4.93×10¹⁰ K | 4.85×10¹³ K |
| tau          | 3.17×10⁻²⁷ | crystal (T-indep) | 5.74×10⁸ K | 2.73×10¹¹ K | 2.06×10¹³ K |
| charm quark  | 2.26×10⁻²⁷ | crystal (T-indep) | 3.08×10⁹ K | 5.34×10¹¹ K | 1.47×10¹³ K |
| strange quark| 1.69×10⁻²⁸ | **fluid** (Λτ_0=1.16×10⁻²) | 1.31×10¹⁵ K | 9.54×10¹³ K | 1.10×10¹² K |
| muon         | 1.88×10⁻²⁸ | **fluid** (Λτ_0=1.59×10⁻²) | 7.71×10¹⁴ K | 7.71×10¹³ K | 1.23×10¹² K |
| down quark   | 8.38×10⁻³⁰ | fluid (Λτ_0=1.40×10⁻⁶) | 4.44×10²¹ K | 3.90×10¹⁶ K | 5.45×10¹⁰ K |
| up quark     | 3.92×10⁻³⁰ | fluid (Λτ_0=1.43×10⁻⁷) | 1.97×10²³ K | 1.78×10¹⁷ K | 2.55×10¹⁰ K |
| electron     | 9.11×10⁻³¹ | fluid (Λτ_0=1.80×10⁻⁹) | 2.92×10²⁶ K | 3.30×10¹⁸ K | 5.93×10⁹ K |
| neutrino     | 1.78×10⁻³⁷ | fluid (Λτ_0=1.35×10⁻²⁹) | 1.02×10⁶⁰ K | 8.61×10³¹ K | 1.16×10³ K |
| photon       | 0           | N/A (Λ=0)         | N/A (Λ=0) | N/A (Λ=0) | N/A (m=0) |

### Sanity checks (per the user's protocol)

| Check | (A) Compton | (B) de Broglie | (C) inter-particle | (D) rest-mass |
|:---|:---|:---|:---|:---|
| Monotonic in mass | binary yes/no by mass | descending: light→high T | descending: light→high T | **ascending: heavy→high T** ✓ |
| Heavy-first cosmic cooling | undefined (T-indep) | ✗ light first | ✗ light first | **✓ heavy first** |
| Brackets T_c = 54.7 MK sensibly | undefined | most species way off | top/Higgs/Z near T_c ✓ | most species above; lightest below |
| Photons never crystallize | ✓ | ✓ | ✓ | ✓ |

### Honest read

**Only interpretation (D) — rest-mass equivalent temperature mc²/k_B —
gives the heavy-first cosmic-cooling order that Ch 13.5 narrates.**
Interpretations (A), (B), and (C) all use Λ_grav and all give either
no temperature schedule (A) or wrong-direction orderings (B, C).

**But (D) doesn't actually use Λ_grav.** The "crystallization" under
interpretation (D) is just standard cosmic-thermal-decoupling: a
species' rest-mass-equivalent temperature is when the thermal plasma
can no longer create/destroy that species through pair production. This
is standard cosmology, not a GRUT-specific prediction.

The chapter's prose ("Particles whose Λ_grav exceeds their thermal
fluctuation frequency cross the crystalline boundary") implies a Λ_grav
mechanism, but no Λ_grav-based interpretation reproduces the heavy-first
schedule.

**Diagnosis:** Ch 13.5's qualitative narrative is using the LANGUAGE
of gravitational decoherence (Λ_grav) but actually relies on the
PHYSICS of standard cosmic thermal decoupling (T ~ mc²/k_B). The two
mechanisms are conflated in the chapter.

This is consistent with the framework's broader pattern: gravitational
decoherence dominates only for COMPOSITE objects (gold benchmark, lab
nanoparticles) where m² is large enough. For elementary particles,
gravitational decoherence rates are dwarfed by other dynamical
frequencies (thermal, electromagnetic, strong-interaction). Crystallization
of SM species in cosmic plasma is set by those non-gravitational rates,
not Λ_grav.

### Implications for Ch 13.5

Three honest options for revising the chapter:

(i) **Drop the per-species crystallization-via-gravity narrative.**
Replace with a description of cosmic thermal decoupling at T ~ mc²/k_B
(standard cosmology). The framework reproduces this; it's not GRUT-
specific. Chapter 13.5 becomes shorter and more honest.

(ii) **Recast the crystallization narrative as about COMPOSITE objects,
not elementary particles.** Atoms, molecules, dust grains have
m² × G/(ℏl) values that DO produce non-trivial Λ_grav. These crystallize
via gravity at temperatures the framework can compute. Elementary
particles crystallize via thermal frequency (already discussed in Ch 4
for atoms).

(iii) **Document the conflation explicitly as a framework finding.**
The Λ_grav mechanism doesn't crystallize SM species at any cosmologically
relevant temperature. Ch 13.5's narrative is a qualitative description
of cosmic history; the GRUT-specific quantitative content is at
COMPOSITE scales, not elementary-particle scales.

---

## Separate finding — T_c units discrepancy

While running the numerical comparison, I tripped over a potential
framework-internal inconsistency that deserves separate flagging:

**The framework's T_c = 54.7 MK does NOT follow from τ_0 = 41.9 Myr
via the formula T_c = ℏ/(τ_0 k_B).**

- Codebase: `T_C_KELVIN = 1.0 / (TAU_0_SEC * K_B)` in
  `grut/foundation/closure_protocol.py:315`, gives 5.49×10⁷ K.
- SI-correct formula: `T_c = ℏ/(τ_0 × k_B)` with τ_0 = 41.9 Myr =
  1.32×10¹⁵ s and k_B = 1.38×10⁻²³ J/K gives 5.77×10⁻²⁷ K.
- The codebase's formula is missing a factor of ℏ.
- Test `test_T_c_is_54p7_MK` pins the (potentially wrong) 54.7 MK value.

The discrepancy is a factor of ℏ ≈ 1.05×10⁻³⁴ J·s. Either:
- (i) The framework has a units bug — the actual T_c should be
  5.77×10⁻²⁷ K, far below CMB. Most predictions involving T_c (like
  "BBN at T > T_c so vacuum is memoryless") would still hold but with
  a vastly different T_c value.
- (ii) The framework intends a DIFFERENT τ_0 for the thermal
  transition (~10⁻¹⁹ s instead of 41.9 Myr), but this τ_0 isn't in
  the codebase's TAU_0_SEC.
- (iii) The "natural-units" comment in the docstring is meant to
  paper over the missing ℏ, in which case the value 54.7 MK is
  conventional rather than dimensional.

**This is OUTSIDE the crystallization-schedule investigation's scope
but should be added to the framework's open-question / correction
ledger separately.** The pattern "T_c = 54.7 MK" appears in multiple
places (closure_protocol.py, dashboard.py, document Ch 2 and Ch 13.5),
so the consistency or correction question affects multiple chapters.

Surfacing here for visibility; not chasing further in this investigation.

---

## Stage 2 — Compute the schedule (REVISED PLAN)

For each SM species (top, b, c, s, u, d quarks; tau, mu, e leptons; W, Z, H bosons; neutrinos):

1. Compute Λ_grav under scales (A), (B), (C) as a function of T.
2. Compute ω_rest × τ₀ for scale (D).
3. Solve for T_cryst under each scale.
4. Report the per-species table with all four columns.
5. Identify which scale (if any) gives a sensible cosmic-history schedule (heavy-first, photons-never, T_c-bracketed).

**Photons:** m = 0, so Λ_grav = 0 for all scales (A)-(C). Under (D), ω_rest = 0. Photons never crystallize under any of these mechanisms — consistent with Ch 13.5.

**Neutrinos:** very light (~0.1 eV mass), so very low T_cryst under all scales.

---

## Stage 3 — Verify physical plausibility (PENDING)

Three sanity checks per the user's prompt:
1. Schedule monotonic in mass.
2. Schedule brackets T_c = 54.7 MK in some sensible way.
3. Photons never crystallize.

These checks may rule out scales (A), (B), (C) decisively (since their mass-ordering is wrong direction). If only (D) passes, the chapter's narrative is correct but the mechanism is rest-mass frequency, not gravitational decoherence.

---

## Stage 4 — Document and update (PENDING)

Three possible outcomes:

(a) **Sensible schedule under one interpretation (likely (D)).** New registry claim. Update Ch 13.5 to clarify the mechanism (rest-mass frequency, not gravitational decoherence). Tier-promote.

(b) **Schedule with structural issues under all interpretations.** Document as honest negative. The framework's qualitative narrative in Ch 13.5 doesn't match any computable schedule.

(c) **Multiple interpretations all give defensible schedules.** Document conditional results, similar to A_s rescaling sensitivity.

---

## End of Stage 1

Four physical interpretations of "crystallization" identified, with pre-Stage-2 numerical estimates. The mass-ordering varies across interpretations. Ch 13.5's narrative consistent only with interpretation (D) — rest-mass frequency, not gravitational decoherence.

The chapter's current text mixes mechanisms: it describes a per-species crystallization schedule using the language of gravitational decoherence (Λ_grav) but the actual mass-ordering only works under rest-mass frequency (ω_rest = mc²/ℏ).

**Stage-2 recommendation:** compute all four interpretations, surface the sensitivity, and let Stage 3's sanity checks select which (if any) is the framework's natural schedule.

Pausing for review per investigation protocol.
