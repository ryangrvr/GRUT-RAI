# S-2 CAMPAIGN — OWNER DIRECTION 01 (hard D-DET / noise-origin discriminator)

**Date:** 2026-09-30 · **Recorded by the owner on Issue #2, comment `5904589246`**, after review
through `3024b3b`. The comment is authoritative; this file records it.

## Decision

- **The next campaign is S-2, the hard D-DET stochastic-class gate.**
- The framing question stays S-1: **is noise primitive or derived?**
- S-1 is blocked in the linear additive Gaussian class by the recorded observational-equivalence
  theorem, so S-2 moves to a class where that equivalence provably breaks.
- **Do not open S-3, S-4, S-6, S-7 or S-8 first.**

## Why S-2 (the ruling's §1)

- **In the linear additive class:** for dx = −Kx dt + B dW, d⟨x⟩/dt = −K⟨x⟩ independently of B (F-5).
  Primitive forcing, a Gaussian initial ensemble and a Hamiltonian bath are equivalent at the tested
  second-order level.
- **The hard class:** nonlinear drift, multiplicative, colored or non-Gaussian noise. There, noise can
  alter the mean or the response law itself.

## Phase: S2-0, formulation / class-selection gate

- **Output:** `S2_NOISE_ORIGIN_HARD_DDET_01.md`.
- **Not authorized yet:** a physics run, stochastic simulation, or a v4 exception.

**Central question:**

> Is there a minimal declared stochastic extension of the Level-0 substrate for which primitive
> stochastic forcing changes a retained observable in a way that cannot be reproduced by
> deterministic evolution with only randomized initial data, while holding the deterministic
> drift/substrate fixed?

- **Target distinction:** primitive stochasticity ≠? deterministic dynamics + uncertain initial state.
- **Comparison scope:** compare only against the deterministic-initial-ensemble alternative. A
  Hamiltonian-bath comparison comes later, and only if the first discriminator survives.

## Candidates (§4; inspected without computation)

| Candidate | Form | Question or note |
|---|---|---|
| **C-A** | multiplicative noise, linear drift: dx = −Kx dt + Σ_a G_a x dW_a (Itô and Stratonovich kept distinct) | Does the mean acquire a noise-dependent drift term? |
| **C-B** | nonlinear drift + additive noise, reusing the L0-1c drift: dx = [−Kx − 4βx^{∘3}]dt + B dW | Does noise alter ⟨x(t)⟩ through moment coupling in a way that initial uncertainty cannot reproduce? |
| **C-C** | colored noise | An auxiliary state or correlation time is added; higher price. |
| **C-D** | non-Gaussian additive noise | May distinguish only higher cumulants; weaker for the first gate. |

## Itô / Stratonovich firewall (§5, mandatory)

- **State in advance:** the calculus used, whether the other convention is physically distinct or a
  representation, and what is held fixed.
- **A drift-conversion identity is not evidence.** f + ½Σ(G_a·∇)G_a with Itô noise and f with
  Stratonovich noise are **one** model.

## Comparison (§6, frozen before any run)

- The stochastic member 𝒮 and the deterministic member 𝒟 share the **same vector field f**, the
  **same initial distribution P₀**, and differ only in having **no forcing after t = 0** (𝒟).
- **The primary discriminator must be a multi-time or response quantity that cannot be matched merely
  by choosing P₀.**
- **Observable hierarchy:**
  1. m₁(t) = 𝔼[x₁(t)];
  2. C₁₁(t, s);
  3. third/fourth cumulants;
  4. linear response to an already-declared probe.
- **Prefer the lowest order.** No exotic readouts.

## Grades (§7)

- **IDENTITY-DISTINGUISHABLE:** a theorem shows they differ for every nonzero noise strength.
- **PARAMETER-REGIME-DISTINGUISHABLE:** they differ only in a parameter region.
- **SECOND-ORDER-EQUIVALENT:** mean and covariance are reproducible; only higher orders distinguish.
- **OBSERVATIONALLY-EQUIVALENT-IN-CLASS.**
- **SECTOR-SMUGGLED:** drift, readout, convention or another ingredient changed.
- **UNFORMULABLE.**

## Theorem-first obligations (§8)

- **T1: mean equation.** Say where noise enters. Do not *assume* that multiplicative noise changes the
  mean.
- **T2: deterministic-ensemble closure.** Find the first frozen observable where the hierarchies
  differ.
- **T3:** prove or kill: *if S and D have identical one-time distributions for all t, the
  discriminator is impossible.* If true, move to multi-time statistics.
- **T4: Fokker–Planck vs Liouville.** The diffusion term itself is **not yet** a discriminator.

## Relations (§§9–10)

- **S-1 is consumed as the control class.** A success must say *"the S-1 equivalence breaks here"* and
  name the structural change. Do not credit "stochasticity itself" unless the controls support it.
- **S-5 stays closed.** Do not use G-D as derived. The campaign is conditional on its adopted drift
  class, and for C-B it must say so explicitly.

## Outcomes (§11, frozen)

| Outcome | Meaning |
|---|---|
| **MINIMAL-CLASS-FOUND** | one declared or minimally extended class supports a clean discriminator |
| **CLASS-SPLIT** | some hard classes are distinguishable, others equivalent |
| **ONLY-HIGHER-ORDER-DISTINGUISHABLE** | |
| **NO-DISCRIMINATOR-IN-DECLARED-CLASSES** | |
| **REQUIRES-NEW-PARENT** | |
| **UNFORMULABLE** | |

**If and only if** the outcome is MINIMAL-CLASS-FOUND, or CLASS-SPLIT with a clean executable
candidate: draft `S2_NOISE_ORIGIN_CHARTER_01.md`, then HARD STOP.

## Priority and governance (§§12–13)

- **Held:** S-3 (crossed cell) and S-6 (coarse-grained arrow).
- **Not authorized:**
  - a v4 exception;
  - simulation, RNG or a sweep;
  - S-3, the reversal diagnostic, S-6;
  - S5-WB or S5-OD;
  - gravity, Π₀ or cosmology.
- **Sequence:**
  1. record the direction;
  2. create the S2-0 file;
  3. **freeze the definitions, candidates, observables, equivalence relation and outcomes before
     evaluation**;
  4. theorem-first audit of C-A … C-D;
  5. mechanical outcome;
  6. the charter only if executable;
  7. HARD STOP.

> **Objective:** find the first stochastic class in which "noise after t = 0" leaves observable
> structure that cannot be replaced by uncertainty only in the initial condition.
