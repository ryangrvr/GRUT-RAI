# GRUT ToE v4 — The Elastic Vacuum (research program)

**Opened:** June 2026 · branch `main_v3` · the first *foundational extension* beyond v3.

> **⚠️ DEMOTED by the v4 founding derivation (see `GRUT_V4_FOUNDING_CHARTER.md`, June 2026).** The
> inverse-problem analysis found the elastic-**SOLID** thesis below is **not forced** and is in *tension*
> with v3: v3's memory F is a Maxwell **FLUID** (static TT shear modulus G_TT(ω→0)→0), so a solid with the
> "forced" G₀ ≈ 10¹⁶ Pa would propagate shear waves at all frequencies and contradict v3's diffusive
> memory. The solid is therefore ONE of ≥4 degenerate medium classes and G₀ > 0 is an **unpaid postulate**,
> not a v3 output. Read this document as a *candidate* within the founding charter's program, not the
> settled v4 thesis. The charter's paid-for content is the unification (v3's 7 targets → 4 inputs) and the
> coarse-graining language; the elastic-solid/dark-sector direction is still owed a justification.

v3 closed its dark-sector question by theorem: the responsive vacuum is single-mode (Phase III,
Mori–Zwanzig), so dark matter is a **hosted input**, not vacuum-derived. v4 asks the only question that
can change that: **does a microscopic medium beneath the vacuum host a genuine new mode?** This document
is the charter + the first results + the roadmap. It does *not* enter the v3 registry; v4 becomes real
only if the make-or-break calculation (§5) succeeds.

---

## 1. The postulate (minimal)

> **The gravitational vacuum is a viscoelastic SOLID (Standard-Linear-Solid / Zener), i.e. its
> transverse-traceless response retains a nonzero static shear rigidity G₀ > 0** — replacing v3's Maxwell
> FLUID (static shear modulus = 0). Mechanically: one spring k_E in parallel with v3's Maxwell arm.

v3 is recovered exactly as the **G₀ → 0 corner**: the Zener modulus → G_∞·iωτ₀/(1−iωτ₀), whose
compliance is v3's χ(ω)=α/(1−iωτ₀), single relaxational pole, n_g(0)=√(4/3), n_g(∞)=1. The name was
always "viscoelastic vacuum"; v3 used only the *viscous* half, v4 activates the *elastic* half.

**The dark candidate:** a gapped, propagating, transverse (shear) phonon / topological defect of the
elastic vacuum (Kleinert world-crystal dislocation, or a Nielsen–Olesen string/vorton) — **not** a bolt-on
dark U(1). It is HEALTHY (ghost-free): a first-order auxiliary internal-strain variable (τ₀ė+e=e_target)
with positive propagator residue (Im χ≥0, N≥0), so it escapes the Ostrogradsky+Q pincer that kills every
*vacuum-derived* higher-derivative pole. It is the imported-but-healthy new DOF that v3 left as the one
open door, and the genuine new k=0 pole that `locality_no_halo` says a halo requires.

**Consistency with v3 (verified, no result broken; two improved):**
single-pole/Markovian (G₀→0 recovery) ✅ · locality–no-halo (phonon *is* the required new pole) ✅
improved · ghost-freedom (first-order internal strain, not Ostrogradsky) ✅ · μ_linear=1 / Ω_Λ from τ₀
(hosted relic gravitates as ordinary CDM; G₀ is a high-ω modulus that doesn't move τ₀) ✅.

---

## 2. The forced result — the rigidity G₀ (a real win)

The Debye / Kleinert world-crystal identity (modulus = energy-quantum per cell), applied to a vacuum
lattice of spacing ℓ_micro = c·τ_micro with one quantum ℏ/τ_micro per cell, FORCES the static shear
rigidity from {ℏ, c, τ_micro} alone — **no dark-sector observable injected, no dial**:

```
G₀ = ℏ / (c³ τ_micro⁴) = 1.03×10¹⁶ Pa          (verified, repo constants, .venv)
ρ_v = G₀/c²            = 0.115 kg/m³
```

This partially fills `tau_hierarchy_decision.py` **Path 2** (vacuum rigidity), previously marked
UNDEFINED/research-tier. Tier: **derived-modulo-one-anchored-input** (τ_micro is anchored, Option B, not
itself derived). It is mechanism-backed, NOT numerology (no digit-coincidence; the rejected α/(1+α)=1/4
does not appear).

---

## 3. The honest miss — a falsifiable refuted prediction

That same forced G₀ predicts the **wrong** dark sector:

| Quantity | Value | Verdict |
|---|---|---|
| c_s = √(G₀/ρ_v) | **= c exactly** | single-velocity inventory ⇒ stiff *relativistic* solid, no slow phonon |
| gap mass m_φ = ℏ/(τ_micro c²) | **4.71 keV** | WARM — at the Lyman-α WDM floor (~3 keV), borderline-disfavored |
| Ω (elastic energy) = ρ_v/ρ_crit | **1.25×10²⁵** | the Λ-catastrophe |
| Ω (4.71 keV hot relic) ~ m/94eV | **~50** (Ωh²) | overcloses ~**418×** |
| Ω (Kibble–Zurek defects) | ~1.5×10³ | overcloses ~**5800×** |

**GRUT's natural elastic dark sector is warm and massively *overcloses*** (the opposite of Track VII's
~31× deficit). Matching Ω_dm = 0.265 needs a ~400–5800× *suppression*, which G₀ does not supply. This is
banked as a **derived-but-refuted prediction** — a falsifiable miss, which is more scientific than a free
dial.

**Numerology casualties (rejected):** α/(1+α)=1/4 (no abundance mechanism); G₀=ρ_Λc² (tautological
scale-match, c_s→c by construction); Ω_eff=α=1/3 (refractive, not particulate, +26%). The other principles
(trace-anomaly fixes only the dimensionless ratio n_g²=1+α; marginal-stability is under-determined, 13
orders; reverse-check finds no natural scale within 5 orders) do **not** force G₀ to the abundance.

---

## 4. The reframe (why the static hunt was the wrong tool)

The static hunt asked "is G₀ a combination of today's constants?" and answered: the *rigidity* is forced,
but the *abundance* is not — and **the abundance was never a static-constant question**. G₀ is the order
parameter of a **rigidity transition**; its dark-matter yield is set by the **quench dynamics** of that
transition (Kibble–Zurek), i.e. by the early-universe history, not by present-day constants. The free knob
did not vanish — it **moved**, from G₀ (now forced) to the **abundance-suppression / transition-scale
dynamics**. That is the development-stage question.

Crucially, the development stage can fix *both* failures of §3: the warm gap (4.71 keV assumes the
transition sits at τ_micro — the *actual* transition scale may differ → possibly cold) and the overclosure
(a forced dilution / defect-annihilation epoch could supply the missing ~10³×).

---

## 5. Roadmap — determining the abundance from the development stage

The arrow of time runs back to *before* the vacuum was rigid. Each stage ends in a computable, falsifiable
number; the postulate boundary (where we leave "computed from GRUT" for "new postulate") is marked in red.

- **Stage 0 — static route (DONE).** G₀ forced (§2); abundance not static (§3). ⇒ the dynamical route is
  necessary.
- **Stage 1 — comprehend the transition. ✅ COMPLETE (see §7).** The rigidity onset is forced (given
  τ_micro) to the **micro/thermal scale** (T_c = 54.7 MK), gap **4.71 keV → WARM**, with **no cold window**
  in current GRUT. The *scale* is GRUT's existing thermal transition; the order parameter (static TT-shear
  G₀) is genuinely new. The prior Genesis crystallization-DM falsification does NOT kill v4 but names its
  three holes (no derived order parameter, no derived dispersion, no derived dilution).
- **Stage 2 — the quench (Kibble–Zurek; mostly existing machinery).** τ_Q from H(t_c) (we have the
  expansion history, N_ERAS=329) → ξ_KZ → defect density → Ω_dm; needs the universality class (ν, z) of
  the TT-shear transition (`kibble_zurek.py:scan_critical_exponents`). **This is where a forced dilution
  either appears or doesn't.**
- 🟥 **Stage 3 — the development stage. ✅ Step 1 COMPLETE → `theory/GRUT_GENESIS.md`.** The backward walk
  (re-framed per the no-bias methodology: catalog necessary transitions blind, test DM downstream) DERIVED
  the **emergence of responsiveness** as spontaneous scale-symmetry breaking (L₀: 0→finite breaking D),
  unmasked by the 34-order slow/fast gap, with **Q the unique invariant surviving the loss of memory**.
  Dark-sector test (blind): **no viable cold DM falls out** — the only forced particulate relic is the warm
  shear phonon (Option B, refuted); Option C (predates responsiveness) is empty within current GRUT (a cold
  relic would need the microscopic bath beneath the vacuum). Auditor: PASS, no forbidden move. The single
  decisive open falsifier: is the dilatation T_λ a genuine gauge redundancy of the full bare CTP action
  (`GRUT_V3_ORGANIZING_STRUCTURE.md` §6)?
- **Stage 4 — close the loop (decision gate).** Compute G₀ and Ω_dm together: forced-and-right
  (derivation), forced-but-wrong (falsifiable miss), or still-free (the development stage hid a knob).

**The single make-or-break calculation:** does the early-universe rigidity transition supply a *forced*
~10³× suppression (and the right transition scale) such that the cold/abundance prediction lands without a
dial? If yes, v4 is a derivation. If no, v4 is an honest one-parameter (or refuted) model and v3's clean
boundary stands.

**The honesty rail:** no step counts unless it ends in a computable, falsifiable consequence; every input
must be mechanism-fixed, not tuned to 0.265; the 🟥 boundary is where v4 stops being v3-derived.

---

## 6. Status

- **Bankable now:** the forced rigidity G₀ = ℏ/(c³τ_micro⁴) ≈ 10¹⁶ Pa (partially fills Path 2); the
  refuted warm/overclosing prediction; full consistency with v3.
- **NOT a derivation of dark matter** — it is a derivation of the *wrong* (warm, overclosing) dark matter,
  plus a recorded miss. v4 becomes a derivation only if Stage 2–3 supplies a forced transition-scale +
  dilution. Until then v3's boundary holds: dark matter is hosted.

---

## 7. Stage 1 result — the rigidity transition (COMPLETE, June 2026)

**Verdict: WARM (m_φ = 4.71 keV), no cold window in current GRUT. Status: WOUNDED — not refuted, not on
track.** Every number verified in `.venv` against repo constants.

**The transition scale (forced given τ_micro).** The fluid→solid rigidity onset is the **same scale** as
GRUT's existing thermal T_c "boiling point of gravity" transition (`thermal_transition.py`: above T_c
local GR, below T_c the memory kernel activates) — NOT the rheological crossover X=ωτ₀=1 (a frequency gate
on v3's *viscous* response, a late matter-era label z≈71 that never makes a static modulus). The order
parameter (static TT-shear G₀: 0→>0) is genuinely new.

```
τ_micro = 1.396×10⁻¹⁹ s ⇔ Δ=1/τ_micro=7.16×10¹⁸ rad/s ⇔ T_c=ℏ/(τ_micro k_B)=54.7 MK ⇔ k_B T_c=ℏ/τ_micro=4.71 keV
epoch: radiation era, t_c ≈ 16.5 hr post-BB, H(t_c) ≈ 8.4×10⁻⁶ /s, τ_Q = 1/H ≈ 1.19×10⁵ s   [Stage-2 inputs]
```

**No cold window — robust.** GRUT contains exactly two transition scales at opposite ends of a 34-order
τ-gap: WARM τ_micro (4.71 keV, the *only* clustering-capable scale) and FUZZY τ₀ (4.98×10⁻³¹ eV). A cold
clustering gap (100 keV–1 GeV) needs τ ≈ 6.6×10⁻²¹–6.6×10⁻²⁵ s — strictly inside the empty gap GRUT does
not populate. All four `tau_hierarchy_decision.py` bridging paths fail (Option B). **A cold scale is
new-postulate territory GRUT does not currently contain.**

**T_c units issue — RESOLVED** (Correction #22, `t_c_provenance_inconsistency_resolved`): 54.7 MK is the
real T_c (τ_micro side); the 5.8×10⁻²⁷ K is the *separate* τ₀-side noise-kernel spectral peak, not a
transition temperature.

**Postulate boundary (drawn one step earlier, per the skeptic):**
- 🟩 forced from GRUT: **only G₀** (given τ_micro).
- 🟨 postulate #1: τ_micro is *anchored* (Option B, BBN chronology), not derived.
- 🟨 postulate #2: m_φ = ℏ/τ_micro is a **Debye one-quantum-per-cell ansatz** (a guessed dispersion), not
  derived. The headline ℏ/τ_micro = k_B T_c is a *definitional tautology* (`closure_protocol.py:407`
  defines τ_micro ≡ ℏ/(k_B T_c)) — the "warm" rests on this ansatz, not on a derivation.
- 🟥 Stage-3 territory: deriving τ_micro (Path 2), a temperature→bandwidth bridge to replace the ad-hoc
  sigmoid `memory_activation_fraction(T)`, and any cold transition scale — none in current GRUT.

**Prior falsification — does NOT kill v4.** The Genesis crystallization-DM log killed a binding-energy
buffer and a refractive/dielectric DM (n_g²−1=α/3); v4's particulate KZ-sourced phonon sidesteps both. But
its lesson carries over: GRUT has **no temperature→bandwidth bridge** (only the frequency classifier X), so
v4's "rigidity turns on at T_c" is still an ad-hoc sigmoid, not a derived order parameter.

**Sharpened Stage-2 question:** since the only clustering-capable scale is warm, Stage 2 must fix **both**
the regime (warm→cold) *and* the abundance, or neither — strictly harder than "supply a 10³× dilution."
The cold scale required lives in the empty 34-order gap, so Stage 2 cannot reach it without Stage 3's new
postulate.
