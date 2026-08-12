# Kill-shot #2 — falsifier recomputed in the energy basis: result

**Date:** 2026-06-25 · **Code:** `calc/energy_basis_decoherence.py` (stdlib, <1 s)
**Status:** lead computed; **awaiting specialist sign-off.** Built on the kill-shot-#1 working
assumption (short, cutoff-set memory → S(ω) keeps its #1 shape). The *qualitative wedge*
below is **independent of #1**; only the spectral *shape* rides on it.

## What was wrong (the miscast)
The old crown jewel — "689 Hz, parameter-free, cleanly distinct from Diósi-Penrose/CSL" —
was wrong three ways, confirmed against Anastopoulos-Hu 2013:
1. **Wrong axis.** AH decoheres in the **energy basis**; DP/CSL localize in **position**. Not
   competing numbers on one observable — different observables.
2. **Not parameter-free.** AH's rate depends on free "textures of spacetime" parameters.
3. **689 Hz is an input**, an added τ_c/cutoff scale, not a kernel output.

## The relocation (the firmer ground)
Born-Markov reduction of the in-in influence action gives, for coherence between energy
eigenstates split by ΔE:

> **Γ(ΔE) = (1/ħ²) |A_nm|² S(ΔE/ħ)** — the rate samples the vacuum noise spectrum at the
> **Bohr frequency of the energy gap**.

Two consequences:

**(A) The decoherence "bandwidth feature" — correctly located in energy-gap space.**
g(x)=S(xω_c)/peak rises as x³ (quantum) / x² (thermal IR, contingent on #1), **peaks at
ΔE = 1.22 ħω_c**, FWHM ΔE ∈ [0.69, 1.85] ħω_c, then cuts off. Because S(0)=0, **small energy
gaps are suppressed** — decoherence grows with the gap, then falls past the cutoff. This is
the "finite-bandwidth feature," but in ΔE, not a fixed lab frequency.

**(B) The wedge — independent of #1, the real differentiator.**

| knob | GRUT-AH (energy basis) | DP / CSL (position basis) |
|---|---|---|
| vary ΔE at fixed Δx | Γ ∼ S(ΔE/ħ) | Γ ≈ const (no ΔE dep) |
| vary Δx at fixed ΔE | Γ ≈ const (no Δx dep) | Γ ∝ (Δx)² |

Orthogonal. A molecular / clock-state interferometer that varies ΔE and Δx independently
discriminates the families directly: same Δx + two energy splittings → GRUT responds, DP/CSL
flat; same ΔE + two separations → DP/CSL responds, GRUT flat.

## Honest accounting
- **Predicted (parameter-free up to one normalization):** the energy-basis structure, the
  shape g(ΔE), the orthogonal ΔE-vs-Δx wedge.
- **Staked inputs (on the ledger, +2):** the amplitude κ (must survive MICROSCOPE/Donadi
  bounds); the cutoff scale ω_c that places the peak (what "689 Hz" really was).
- **"689 Hz parameter-free" is retired.** **BMV backup is withdrawn** — an energy-basis
  decoherer may not degrade a position-basis entanglement witness; recompute or drop.

## New tension surfaced (report straight)
The wedge is **sharp but possibly faint**:
- If gravity couples to the *static* energy H_S, small-gap decoherence samples **S(0)=0 →
  suppressed** (the responsive vacuum is a *quiet* bath for static energy superpositions).
- If ω_c sits near **sub-kHz** (what "689 Hz" implied), atomic/molecular gaps
  (ω=ΔE/ħ ≫ ω_c) are **exponentially cutoff-suppressed**.
Either way the predicted magnitude could be small — a clean differentiator that is hard to
*see*. That is the next thing to resolve before staking the program here.

## Open items for the specialist
1. The exact coupling operator A and |A_nm| (gravity couples to the full stress tensor, not
   exactly H_S) — decides suppressed (samples S(0)) vs transition-driven (samples S(ΔE/ħ)).
2. The physical value of ω_c — is the vacuum-memory scale really sub-kHz, and if so what
   experiment has access?
3. The BMV witness under an energy-basis decoherer.

## One-line question for the specialist
> For gravity coupling to the stress tensor (not exactly H_S), does the energy-basis
> decoherence of a ΔE superposition sample S(ω=ΔE/ħ) (transition-driven, nonzero) or S(0)=0
> (pure-dephasing, suppressed) — is the responsive vacuum a decohering or a quiet bath for
> static energy superpositions?

## Consequence for the ladder
Rung 8 stays **to-derive**, ledger now **+2** (amplitude + ω_c), differentiator = energy-basis
ΔE-scaling (PASS, #1-independent). The single-point-of-failure structural risk is **unchanged**:
diversify (rung 7 low-parameter w(z); a second finite-τ_c observable) before staking.
