# GRUT v3 — The Corrected Physical Picture

**Version 3.0.0.dev0 · June 2026 · branch `main_v3`**
**Status:** foundation / corrected physical picture. *Not a complete program* — the spine from
which the v3 Theory-of-Everything path continues. Operative module: `grut/v3/picture.py`.

v3 **inherits the verified v2 backend** (frozen at tag `v2-final`) and builds forward from the
foundation that survived every adversarial attack. The v2 over-claims — chiefly the linear
modified-gravity enhancement — are removed; what remains is what the theory actually earned.

---

## The picture in one line

> **GRUT is general relativity's long-wavelength rescaling redundancy, broken in a controlled way
> by exactly one scale `L₀ = c·τ₀ ≈ 12.85 Mpc`** — the same shape by which a particle mass breaks
> scale invariance. A theory is defined by *which* symmetry it breaks and by *how much*; GRUT
> breaks the adiabatic-rescaling redundancy by one memory length.

Two pillars carry it, and one relation binds them:

| | | Standing |
|---|---|---|
| **Q** | CTP / in-in unitarity — physics is the response to *realized differences* (`S_IF[φ₊=φ₋]=0`) | **proven** |
| **F** | finite single-pole memory `χ(ω)=1/(1−iωτ₀)` — causal, bounded, GR-recovering | **postulated** (one scale, τ₀) |
| **D** | the adiabatic-dilatation redundancy | **bridge** — *F breaks D* |

"The vacuum responds only to physically distinguishable structure" is the *name* for the
conjunction Q∩F∩D — not a separate axiom.

---

## The forward build (the v3 spine)

Read top to bottom: each step is what the previous one entails. This is the order the v3 ToE is
constructed in, and the order `grut/v3/picture.forward_chain()` returns.

1. **The responsive vacuum (Q).** Physics is the response to realized differences. The
   closed-time-path action vanishes on the classical diagonal; the physical response is
   `δS_IF/δφ_q|_{q=0}`. *Proven (theorem of the formalism).*
2. **Finite memory (F).** A single-pole susceptibility gives a causal, bounded response that
   recovers general relativity at high frequency. One dimensionful input: `τ₀ ≈ 41.9 Myr`.
   *Postulated (τ₀ anchored).*
3. **The boundary operator (the no-gos).** What the vacuum is *forbidden* to respond to:
   pure-gauge/adiabatic modes (⇒ `μ_linear = 1`), the bare gauge-dependent density,
   unbounded/infinite response. The no-gos are not failures — they map the shape of the allowed
   solution space. *Derived constraints.*
4. **The organizing principle (F breaks D).** The adiabatic spatial-dilatation redundancy is exact
   only in the memoryless `L₀→0` limit; finite memory breaks it for every `k≠0` at `O((L₀k_phys)²)`,
   *non-anomalously* (the trace-anomaly coefficient α does **not** enter). *Theorem — outcome B,
   independently verified.*
5. **The emergent universe.** Linear cosmology = **ΛCDM** (`μ_linear=1`, derived). Certified:
   gravitational decoherence (~689 Hz plateau), `R=√(4/3)`, `η_B≈6.6×10⁻¹⁰`, background `H(z)`/BAO,
   the cosmological constant as a terminal velocity. The dark-sector enhancement is *relocated* out
   of the linear channel. *Derived/certified.*
6. **The open frontiers — where the ToE path continues.** The dark sector lives **only** in
   nonlinear/tensor channels — C5a (W² second-order), C5b (orbital-ω bound systems), C5c (TT/GW).
   Also open: the first-principles value of α (4th-order Riegert), the `L₀→0` underlying-redundancy
   proof. Flavor (incl. Koide) is **hosted** Standard-Model input. *Open — the live v3 targets.*

---

## What stands (certified, inherited)

| Quantity | Value | Status |
|---|---|---|
| α (vacuum impedance) | 1/3 | single dimensionless **axiom** (genuine trace-anomaly result under one identification; 4th-order Riegert closure open) |
| R (deep-IR refractive index) | √(4/3) ≈ 1.1547 | derived |
| τ₀ (relaxation time) | 41.9 Myr | single dimensionful scale (anchored) |
| L₀ (memory length) | c·τ₀ ≈ 12.85 Mpc | the symmetry-breaking scale |
| μ_linear | 1 | **linear cosmology = ΛCDM (derived requirement)** |
| η_B (baryon asymmetry) | ≈ 6.6×10⁻¹⁰ | derived (CTP path asymmetry) |
| decoherence plateau | ~689 Hz | primary tabletop falsifier |

---

## What was corrected from v2 (do not reintroduce)

- **Linear modified-gravity enhancement (μ→4/3, "μ−1=1/3"): RULED OUT** — by the low-ℓ CMB ISW
  (≈2.8×/32σ) and by consistency (`μ_linear=1`). σ₈/fσ₈/S₈ are ΛCDM-level, not distinctive.
- **α = 1/3** is an axiom, not "derived/Gate-R-closed."
- **The k_eq equality filter** has no derivable basis — retired.
- **Flavor/Koide** is hosted (fixed-point no-go: the impedance gives 4/9, not 2/3).
- The default `camb` is the GRUT fork (μ always-on = the ruled-out enhancement); v3 baselines
  ΛCDM against **stock CAMB**.

---

## Honest precision note

v3 is precise where it earned it — the decoherence plateau, R, η_B, the background `H(z)`/BAO, and
the *derived requirement* that linear cosmology is ΛCDM. It is **honest-but-open** exactly where
the dark sector now lives: the **nonlinear/tensor channels (C5a–c) are uncomputed.** The first real
test of v3's precision is whether that channel produces a dark sector at all. That is the frontier,
not a solved result — and v3 states it as such rather than overclaiming.

---

## Continuing the ToE path

The v3 ToE is built forward from this spine. The immediate, load-bearing target is **the nonlinear
/tensor dark sector (C5a–c)** — the only surviving home for GRUT deviations after the linear channel
closed. Everything needed to start is inherited and verified; `grut/v3/picture.py` is the operative
entry point, and `theory/V2_TO_V3_SYNTHESIS.md` records how the foundation was reached.

---

## Standing V3 methodology rules

These are the working rules of the v3 audit, alongside the v2 selected/permitted/hosted/anchored
terrain taxonomy.

1. **Every surviving sector must identify its controlling frequency.** A GRUT prediction is a
   response of a finite-memory medium, so it is meaningless until the dimensionless `ωτ₀` of the
   relevant physical regime is named. Test 01 succeeded *because* it compared `ωτ₀` across regimes —
   cosmological linear modes (`k·c_s·τ₀ ≪ 1`), bound-system orbital modes (`ω_dyn·τ₀ ~ 1`), and the
   DC/terminal limit — which exposed that the "dielectric Ω_dm" was secretly the ruled-out linear
   (`ωτ₀≪1`) branch. The frequency-domain classification is as load-bearing to v3 as the terrain
   taxonomy: *no sector is audited until its controlling frequency is on the table.*

2. **The mathematics often survives; the ontology changes.** The recurring v3 signature: a v2
   *calculation* is usually correct, but the *thing it was claimed to be* is not. Koide survived as a
   compatibility identity but lost its status as a prediction; the linear enhancement survived as a
   possibility but lost selection; `Ω_dm = 1/3` survived as a (correct) integral but lost its
   interpretation as a dark-sector mechanism. **A v3 audit asks not "is the number right?" but "which
   surviving structure is this number actually a consequence of?"**

3. **No major v2 claim is assumed safe until it survives a v3 audit** under rules (1)–(2). After
   Test 01, the standing re-audit queue is: flavor sector, α=1/3 provenance, the constitutive-law
   hierarchy, and the decoherence sectors.
