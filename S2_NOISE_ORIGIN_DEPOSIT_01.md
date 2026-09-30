# S-2 NOISE ORIGIN — DEPOSIT 01 (through S2-1; no new analysis)

- **Authority:** `S2_OWNER_RULING_03.md` (Issue #2 comment `5909019588`).
- **What this file is:** accepted terminals only. **It contains no new analysis.**
- **Date:** 2026-09-30 · **Branch:** `master-w25bu9`.

## The chain

| Gate | Terminal | Records |
|---|---|---|
| **S-1** (control; floor successor) | Linear additive Gaussian ⇒ **initial-uncertainty equivalence** on the tested second-order objects | `L0_1_FLOOR_SUCCESSOR_LIST.md` (S-1), L0-1e (F-5) |
| **S2-0** | **CLASS-SPLIT** | `S2_NOISE_ORIGIN_HARD_DDET_01.md` (pre-registered `8e1c8e7`, audit `47a9a7b`); `S2_OWNER_RULING_01.md` |
| **S2-1** | **FULL-DISCRIMINATOR-CONFIRMED** | charter `227dd09`; verified derivation `32645cc`; first run **RUN VOID** (`81b4f8f`, preserved); corrective run `64d9cc9` → `de6eb46`; `S2_OWNER_RULING_02.md`, `S2_OWNER_RULING_03.md` |

## Accepted results

1. **Theorem LD.** A linear canonical drift plus a true-martingale noise gives 𝔼[x(t) | x₀] = e^{−Mt}x₀.
   Multiplicative, colored (on the enlarged state) and non-Gaussian noise are equivalent on the frozen
   O-1/O-2, **read narrowly at the audited scope.**
2. **The C-B coefficient theorem:**
   - Δc₂ = −24βT₁a, so m₁^𝒮 − m₁^𝒟 = **−12βT₁a·t²** + O(t³);
   - Δc₃ = 24βT₁a(44βa² + 5K₁₁).
3. **HT-B (T-HT closed).** No preparation-independent hidden initial law on the **same deterministic
   state space**, of arbitrary tails, reproduces the C-B retained mean-response map when β > 0 and
   T₁ > 0.
4. **The accepted statement:**

   > **Within the declared nonlinear C-B class, ongoing stochastic forcing is observationally
   > distinguishable in the retained mean-response map from uncertainty confined to the initial
   > condition on the same deterministic state space.**

5. **Mechanism:** noise-generated spread + drift curvature → mean-response structure.
6. **Class split:**
   - **Linear canonical drift:** ongoing martingale noise is invisible to the frozen mean-response
     object.
   - **Nonlinear curved drift:** it can become visible already in the retained mean.

   **The S-1 linear equivalence is not structurally stable under nonlinear drift.**
7. **Diagnostics (report-only):**
   - G(∞) (T₁ = 0): Δc₄ = −(48/11)aβ, the first nonzero order.
   - F vs GR(∞): they first differ at Δc₄.
   - The earliest correction is local; remote structure enters later. This is not a finite-time
     dominance claim.

## Not established

- ontological noise, or that GRUT requires primitive randomness;
- that deterministic physics cannot reproduce the process;
- **that an enlarged hidden environment cannot reproduce the reduced law (open: S2-HB)**;
- quantum outcomes, Born probabilities or collapse;
- a derived L0-1c drift.

## Status

- **S-2 is open at the S2-HB boundary** (audit only).
  - Same-state-space uncertainty: **NO.**
  - Enlarged deterministic physical bath: **?**
