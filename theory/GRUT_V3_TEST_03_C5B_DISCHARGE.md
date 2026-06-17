# GRUT v3 — Test 03: The C5b Discharge (Controlling-Frequency Magnitude)

**Date:** June 2026 (2026-06-17) · branch `main_v3`
**Status:** COMPLETE — **verdict B (REFUTED), route to C5a**; adversarially verified, **read-only**
workflow (`wj098m5xz`; 5/5 agents converge).
**Question (Test 02's open discharge):** does a virialized halo present GRUT's medium a realized
(Weyl/tidal) source that varies at `ω_dyn = v/r` with **O(1) magnitude** (→ promote C5b) — or is it
DC / negligible (→ route to C5a)?

---

## Verdict: refuted on MAGNITUDE (not frequency)

Decompose the realized gravitational structure of a virialized halo:

- **Mean field (O(1)):** the equilibrium potential `Φ̄(r)` is time-independent (DC) by virialization.
  At linear scalar order the tracefree `P^TT` kernel annihilates it (`μ_linear=1`) — the medium gives
  **no linear response** to the static mean. (Responding to the O(1) mean Weyl field at all requires
  the **nonlinear W² channel — C5a**, since `δ(W²)=2W̄·δW=0` on the background makes it genuinely
  second-order.)
- **Granular fluctuations (what's left at `ω_dyn`):** the deviations from the mean are N-body Poisson
  noise, amplitude `δΦ/Φ̄ ~ 1/√N`. For a galactic halo `N~10¹¹` → **`~10⁻⁶`**. Their autocorrelation
  frequency is `~ω_dyn=v/r` (kinematically correct), but their amplitude is negligible.

So the controlling frequency `ω_dyn` is *dimensionally right but applied to a `~10⁻⁶` source*; the
gate `1/(1+X²)` (correct constitutive form) gates near-zero amplitude. Required for flat curves /
`Ω_dm`: `~15–25%` (O(1)). Delivered by the gated realized structure: `~10⁻⁶`. **C5b's discharge
condition is NOT cleared — it fails on magnitude.**

## Scrutiny (don't over-claim a negative)

I checked whether the agents over-applied the No-Go to the galaxy's *inhomogeneous* mean tidal field
(which is realized Weyl structure, not the homogeneous separate-universe mode). Resolution: the O(1)
mean Weyl field **is** a real source — but responding to it is the **nonlinear W² channel (C5a)**, not
the linear C5b gate. The *linear* C5b mechanism is genuinely refuted; the O(1) dark sector survives
only in C5a. The negative is sound.

## The big picture — after three v3 tests

| Test | Channel | Verdict |
|---|---|---|
| 01 | linear dielectric `Ω_dm=1/3` | RULED OUT (linear branch; `μ_linear=1`) |
| 02 | C5b orbital gate — frequency | ASSUMED, not derived |
| 03 | C5b orbital gate — magnitude | **REFUTED** (realized structure `~10⁻⁶`, not O(1)) |

**The entire dark sector now routes to the single uncomputed nonlinear channel C5a (W²).** The
No-Go is more corrosive than Tests 01–02 suggested: it undercuts the bound-system mechanism for the
*same* reason it undercut the linear one — the O(1) structure (the mean potential) is the
locally-absorbable/linear-scalar mode the medium cannot respond to, and what's left is negligible.
**GRUT retains a derived `a₀` *scale* but has no derived dark-matter *mechanism*.** Galactic rotation
curves, in v3, are *adopted-MOND `ν(y)` × a phenomenological gate* with a GRUT-derived `a₀` —
MOND-compatible, not GRUT-generated.

## Banked

- `mond_a_0_emergence`: **HELD at `computed`** (the `a₀` scale is genuinely derived and tested), but
  the statement now records that the **gate is refuted as a dark-sector mechanism** (Test 03).
- C5b: refuted as a standalone dark-sector source; **not** a structural channel.

## Next — C5a (W²), the sole remaining dark-sector channel

The decisive v3 dark-sector computation is now unavoidable and singular: **does the second-order
Weyl-squared (W²) constitutive response to the O(1) mean tidal field of a bound/collapsed system
produce an O(1) effective source — and of the right sign/magnitude/scaling for the dark sector?**
This is genuinely uncomputed (a 2nd-order CTP computation; `PROJECTOR_CONSISTENCY_NOGO.md §8 C5a`).
If C5a fails, GRUT has no dark-matter mechanism and the dark sector is a hosted input; if it
succeeds, it is GRUT's *only* derived dark-sector physics. Either outcome is decisive.
