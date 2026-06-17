# GRUT RAI — Status

**Branch `v3` · version 3.0.0.dev0 · June 2026**

This repository is now running on **v3 physics**. GRUT **Version 2 is retired** and frozen at
the git tag **`v2-final`** (commit on branch `v2`): the v2.8 Final Edition book
(`uploads/GRUT_TOE.pdf`, with the V2→V3 Synthesis foreword) plus the v3-readiness-audited backend.
v3 **inherits that verified backend** and builds forward from the corrected foundation.

---

## What v3 physics is (the operative foundation)

GRUT is a **theory of permissible vacuum response**: general relativity's long-wavelength
rescaling redundancy, broken in a controlled way by exactly one scale — the memory length
`L₀ = c·τ₀ ≈ 12.85 Mpc`. (Full statement: `theory/GRUT_V3_ORGANIZING_STRUCTURE.md`;
derivation trail: `theory/V2_TO_V3_SYNTHESIS.md`.)

- **Two pillars:** **Q** = CTP/in-in unitarity (proven); **F** = finite single-pole memory
  (postulated). **D** = adiabatic-dilatation redundancy is a conjectured bridge whose *breaking*
  is established — **F breaks D** (dilatation theorem, outcome B; verified).
- **Robust theorem:** `μ_linear = 1` — **linear cosmology = ΛCDM, a derived requirement.**
- Backend recorded in `grut/foundation/organizing_structure.py` (+ tests).

## Corrected from v2 (do not reintroduce)

- The **linear modified-gravity enhancement** (μ→4/3, "μ−1 = 1/3") is **RULED OUT** — by the
  low-ℓ CMB ISW (≈2.8×/32σ) and by consistency (μ_linear = 1). Registry claims
  `cmb_boltzmann_case_a_structural` and `camb_grut_power_spectrum_prediction` are `open_negative`.
- **σ₈ / fσ₈ / S₈** are ΛCDM-level, not distinctive predictions.
- The **k_eq equality filter** has no derivable basis — retired.
- **α = 1/3** is the single dimensionless **axiom** (a genuine trace-anomaly result under one
  identification; 4th-order Riegert closure open) — not "derived/closed."
- **Flavor / Koide** is hosted Standard-Model input (fixed-point no-go) — outside the scheme.
- The **default `camb` is the GRUT fork** (μ always-on = the ruled-out enhancement); v3 must
  baseline ΛCDM against **stock CAMB**.

## What stands (inherited clean)

Gravitational decoherence (~689 Hz plateau, isotope discriminator, BMV); `R = √(4/3)`;
`η_B ≈ 6.6×10⁻¹⁰`; background `H(z)` and BAO; the CTP/constitutive foundation; the no-go skeleton.
Suite: **3209 passed, 2 xfailed** (the documented camb-fork ΛCDM baseline).

## Open v3 frontiers (named, not closed)

First-principles α (4th-order Riegert); the **nonlinear/tensor dark sector** (C5a W², C5b
orbital-ω, C5c TT) — the only surviving home for GRUT deviations; nonlinear structure-formation
self-consistency; Koide/flavor closure; the τ_micro/τ₀ hierarchy; stock-CAMB ΛCDM baselining.
