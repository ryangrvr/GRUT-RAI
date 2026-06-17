# GRUT v3 — Test 01: The Dark-Sector Channel Reconciliation

**Date:** June 2026 (2026-06-17) · branch `main_v3`
**Status:** COMPLETE — finding holds (adversarially verified, workflow `w1zl9ecij`).
**Question:** Now that v3 has ruled out the linear modified-gravity enhancement, *where can a
dark sector live* — and does the existing "Ω_dm = α = 1/3" result survive?

---

## The test

GRUT's existing dark-matter result (`omega_dm_equals_alpha`, `dielectric_dm_reframing`, both
formerly `tier="computed"`) computes a **bandwidth integral**
`Ω_dm,eff = ∫ E(k) Δ²(k) dk / ∫ Δ²(k) dk`, with `E(k) = α/(1+(ω(k)τ₀)²)` and `ω(k)=k·c_s`
(`c_s≈200 km/s`, a *linear-theory* velocity dispersion), over the **linear** power spectrum `P(k)`.
At the `P(k)` peak (`k≈0.02 h/Mpc`), `ωτ₀ ≈ 10⁻⁴ ≪ 1`, so `E(k) ≈ α` across the whole support →
`Ω_dm,eff ≈ α = 1/3`.

**That is the DC saturation of exactly the conformal `μ → 4/3` enhancement on linear modes** —
the one v3 ruled out (`PROJECTOR_CONSISTENCY_NOGO.md §5`: `μ_linear=1` forced; `CMB_ISW_EQUALITY_FILTER.md §0.1`:
MGCAMB `D_ℓ^GRUT/D_ℓ^ΛCDM = 2.79× at ℓ=15`, ~32σ). The integral is correct code; its
surviving-mechanism *interpretation* is dead.

## Verified verdict (all four claims hold)

1. **The dielectric `Ω_dm = 1/3` is the ruled-out linear branch.** The velocity-dispersion frequency
   is *not* an escape: it is integrated over the *linear* `P(k)` at `ωτ₀≪1`, which is precisely the
   linear-scalar response the No-Go forbids and the data falsify.
2. **The surviving channel is bound-system C5b** (`X = ω_dyn·τ₀`, `ω_dyn = v/r` orbital). Galaxies sit
   at `X ~ 0.3–1.3` → frequency-gated enhancement `E ~ 0.13–0.31` (matches the module's "~0.19").
   Genuinely distinct from the linear FRW scalar; not killed by the No-Go.
3. **But C5b is bounded** (`n_g² ≤ 4/3`, ~19% at galactic scales): it sets the MOND scale
   `a₀ = cH₀/(2π)` and a falsifiable high-ω deviation, but **cannot flatten rotation curves** (the
   shape `ν(y)` is *adopted* from MOND). And it is **partial** — the orbital Lorentzian is
   *extrapolated* from the DC `χ_eq`, not yet CTP-derived at bound-system frequencies.
4. **Full `Ω_dm` is open**, routed to the uncomputed nonlinear **C5a (W² second-order)**.

## The honest outcome

> **GRUT does not have a derived dark sector that produces `Ω_dm` today.** It has a *ruled-out*
> linear branch (the dielectric `Ω_dm=1/3`), a *real-but-partial* bound-system result (C5b: a derived
> `a₀` + a falsifiable high-ω MOND deviation, bounded and not-yet-CTP-derived), and an *open*
> nonlinear program (C5a, W²). The first v3 test cleanly splits the dark sector along the frequency
> axis and tells us precisely where precision is — and isn't — currently possible.

## Banked (re-tiering)

| Claim | Was | Now | Why |
|---|---|---|---|
| `omega_dm_equals_alpha` | computed | **open_negative** | the linear dielectric; its falsifier has fired (+ ledger entry added) |
| `dielectric_dm_reframing` | computed | **conjectural** | splits into a dead linear part + a surviving partial C5b part + a separate Bullet-Cluster part |
| `mond_a_0_emergence` | (unchanged) | preserved | the legitimate surviving C5b `a₀` result lives here — **not** over-demoted |

Suite green after re-tiering: `tests/toe` 224 passed; tiers computed 60 / open_negative 22 (≡ ledger).

## Next v3 test → C5b (a₀), then C5a (W²)

The linear fork is closed by consistency + data; nothing more to test there. Of the two open forks,
**C5b is the next test** because it has a concrete, dischargeable assumption: derive (or refute) the
orbital-frequency susceptibility `χ(ω_dyn) = 1/(1−iω_dyn τ₀)` *directly from the CTP action for a
bound system* — confirming the Lorentzian gate is continuous from the cosmological DC limit to
orbital frequencies rather than assumed — then push the falsifiable high-ω deviation from MOND
(wide binaries / orbital-phase) to a quantitative prediction. If C5b's gate is confirmed derived,
`mond_a_0_emergence` promotes. **Only then** is C5a (W², the route to full `Ω_dm`) the well-posed
next front.
