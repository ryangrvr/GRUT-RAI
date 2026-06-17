# GRUT v3 — Audit-Phase Checkpoint (Tests 01–04)

**Date:** June 2026 (2026-06-17) · branch `main_v3` · tag `v3-audit-checkpoint`
**Purpose:** freeze the coherent falsification map produced by the v3 dark-sector audit before the
constructive phase (Test 05) begins changing the landscape. This is the **phase boundary between the
audit phase and the constructive phase of v3.**

---

## The organizing statement

> **GRUT-ToE v3 is organized around constraint auditing, not mechanism accumulation.** The audit
> reduced the dark sector from four candidate mechanisms to **one surviving nonlinear channel (C5a)**,
> **one surviving scale (`a₀`)**, and **one decisive open computation (the second-order CTP kernel
> `K⁽²⁾`)**. That is a far stronger statement than any specific `Ω_dm` claim ever was.

The dark-sector question is no longer "how does GRUT explain dark matter?" It is now the single,
well-posed question: **what is the explicit second-order CTP kernel `K⁽²⁾`?**

---

## The compression (the actual accomplishment)

```
BEFORE the audit (mechanisms spread across the dark sector):
    dielectric Ω_dm = α
    linear enhancement (μ → 4/3)
    orbital-frequency gating
    a₀-scale emergence
    Weyl/tidal (W²) response

AFTER the audit:
    Linear branch    -> dead   (μ_linear = 1; 32σ low-ℓ ISW)
    Dielectric Ω_dm  -> dead   (= the ruled-out linear branch)
    Orbital gate     -> dead   (realized structure ~1/√N, negligible magnitude)
    a₀ scale         -> SURVIVES (derived from τ_Λ = 1/H₀)
    W² response (C5a)-> SURVIVES (undetermined: sign ✓, scaling ✓, magnitude open)
```

An enormous compression of uncertainty: four candidate mechanisms → one surviving channel + one
scale + one computation.

---

## The clean v3 state (frozen here)

**Proven / surviving**
- Q pillar — CTP/in-in response structure (proven)
- F pillar — finite-memory postulate (`τ₀ = 41.9 Myr`)
- `μ_linear = 1` — linear cosmology = ΛCDM (derived requirement)
- derived `a₀ = cH₀/(2π)` scale

**Refuted**
- dielectric `Ω_dm = α = 1/3` (Test 01)
- linear modified-gravity enhancement (Test 01)
- orbital-gate dark-matter mechanism (Test 03)

**Open**
- C5a — the W² second-order kernel (Test 04: not refuted; magnitude undetermined)
- the underlying `L₀→0` redundancy status of D beyond the current derivation
- α-selection closure (the 4th-order Riegert a/c)

---

## The four tests, and the failure-mode shift

| Test | Channel | Mode | Verdict |
|---|---|---|---|
| 01 | dielectric / linear | mechanism → theorem → **dead** | refuted |
| 02 | C5b gate (frequency) | mechanism → derivation gap | assumed |
| 03 | C5b gate (magnitude) | mechanism → theorem → **dead** | refuted (`~1/√N`) |
| 04 | C5a (W²) | mechanism → theorem → **survives**; magnitude → **unknown** | undetermined |

Tests 01–03 were **eliminations**: each mechanism met a theorem (the No-Go / separate-universe
invariance) and died. **Test 04 is qualitatively different** — it is the first result *not killed by
a theorem*. The sign survived; the scaling survived; only an *uncomputed parameter* (the `K⁽²⁾`
length scale + prefactor) stands between it and a verdict. C5a is the first dark-sector channel that
**earned the right to exist** — not because it works, but because it was not eliminated.

---

## The phase boundary

Tests 01–04 stress-tested *existing* claims. **Test 05 must produce *new mathematics*** — the
explicit second-order variation `Φ⁽²⁾_μν = δ²S_CTP/δh_a δh_r|_{O(2)}`, yielding `K⁽²⁾`, its coupling
length scale (`L₀` → C5a dies; local `r` → galaxy-marginal), and its dimensionless prefactor.

> **Test 05 is no longer "another test." It is the single computation that determines whether GRUT
> possesses a derived dark-sector mechanism at all.**

This checkpoint freezes the audit phase.

**UPDATE (Test 05 run, 2026-06-17):** the audit phase now **ENDS at Test 05** (its endpoint), which
reduced the dark sector to the single `K⁽²⁾` symbolic computation (`undetermined_needs_symbolic`).
The audit phase (Tests 01–05) is frozen at tag `v3-audit-complete`. The **constructive phase** is the
`K⁽²⁾` derivation itself — its flagship problem and the dark-sector moratorium are defined in
`GRUT_V3_CONSTRUCTIVE_PHASE.md`.

**Test records:** `GRUT_V3_TEST_01_DARK_SECTOR.md`, `..._02_C5B_GATE.md`, `..._03_C5B_DISCHARGE.md`,
`..._04_C5A_WEYL.md`, `..._05_K2_KERNEL.md`. **Foundation:** `GRUT_V3.md`,
`GRUT_V3_ORGANIZING_STRUCTURE.md`, `V2_TO_V3_SYNTHESIS.md`.
