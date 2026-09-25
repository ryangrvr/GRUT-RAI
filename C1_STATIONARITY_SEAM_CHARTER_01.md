# C1 — THE STATIONARITY SEAM: DOMAIN-EXTENSION ATTACK ON ε. CHARTER + PRE-REGISTRATION (frozen before evaluation)

**Date:** 2026-09-25 · **Authority:** owner ruling accepting
Formalization 02: *"the next fork is authorized: C1 — Stationarity
Seam … frozen as a domain-extension attack on ε, with no C2 work
mixed into it and no reopening of ω⁷, Class-4, GR-1, or the
already-closed forks."* **This is the program's first completion
attack** (a test of whether the formal domain extends), not another
exploratory fork.

**The question (owner, verbatim):**

> Can the constructive map ε : (M, 𝔞) ↦ 𝒞_continuum be extended from
> stationary microscopic dynamics to genuinely nonstationary
> backgrounds while preserving the already-earned finite reduction,
> spectral/influence structure, and positivity properties?

**Outcomes (owner-fixed, mechanical):**
1. **DERIVED EXTENSION** — a nonstationary construction exists and
   connects continuously to the stationary one
   (K_R(t,t′) → K_R(t−t′) when time-translation invariance is
   restored).
2. **PRINCIPLED DOMAIN BOUNDARY** — the extension requires a priced
   additional structure, named exactly; S1 becomes a certified
   boundary.
3. **FAILURE** — the extension violates an earned constraint
   (positivity, passivity, locality, exact finite reduction);
   preserved as a structural failure.

Components are reported separately (an extension may be DERIVED for
the map and BOUNDARY for the packaging).

**Binding cautions (owner):**
- **The FRW cosmological kernel is NOT the microscopic nonstationary
  model.** This instrument *generates* K_R(t,t′) from a declared
  microscopic M(t) and then measures its properties. The
  kernel-transport / non-stationarity record is motivation only; no
  cosmological object is consumed.
- The attack tests the extension of the map M(t) → K_R(t,t′); it
  never replaces K(t−t′) by an arbitrary two-time function.
- No C2 content (no light cones, no sectors, no causal data). No
  reopening of ω⁷ (occupancy fence carried), Class-4, GR-1's reds, or
  any closed fork. ℏ located; operator ordering fenced. No absolute
  exponents.

**Scope (declared, frozen).** Class: finite first-order passive local
networks 𝕆_G, ẋ = −K(t)x with K(t) symmetric PSD and local;
nonstationarity protocol: **stepped (piecewise-stationary)
modulation**, which genuinely breaks time-translation invariance
while keeping every propagator exact (eigendecomposition per epoch).
This charter is **C1-a, the finite core of C1**. Named successors,
not opened here: **C1-b** (the infinite-volume nonstationary limit)
and **C1-c** (smooth modulation). A verdict here claims nothing about
either.

## 1. THE MODEL (frozen)

- Chain of N = 24 sites (site 0 retained, 23 bath), springs 1.0
  between neighbors, pins 0.3 on every site (K PSD, min eig ≥ 0.3).
- Epochs [0,4), [4,8), [8,12]: K_A, K_B, K_A, with K_B = K_A except
  the four bath-internal springs (1,2), (2,3), (3,4), (4,5) scaled by
  (1 + ε_m). The system–bath coupling row K_SB (spring (0,1)) is
  **never modulated**, so the coupling datum is constant and the
  nonstationarity lives strictly in the bath.
- ε_m ∈ {0 (stationary control), 0.01, 0.02 (continuity), 0.5
  (working point)}.
- Initial condition x₀ = e₀ (retained excited, bath empty), so the
  inhomogeneous term vanishes exactly.
- Exact machinery: per-epoch propagators e^{−K_e Δ} = V_e e^{−λΔ} V_eᵀ
  by cyclic Jacobi; the exact two-time kernel
  k(t,s) = v ᵀ U_B(t,s) v (v = bath-side coupling vector), with
  U_B the time-ordered product of per-epoch bath exponentials.
- The reduced dynamics is solved **using only S-level data** (the
  per-epoch spectral data {λ_e, u_e = V_eᵀv} and the mixing matrices
  C_{e′e} = V_{e′}ᵀV_e): memory modes ṁ_l = −λ_l m_l + u_l q within an
  epoch, m ↦ V_newᵀV_old m at boundaries,
  q̇ = −K_SS q + Σ_l u_l m_l. RK4, h = 0.002, halved for the
  convergence control; steps never cross an epoch boundary.

## 2. THE LEGS (frozen, predictions written before any number)

- **L-E (exact finite reduction extends — the map).**
  *Prediction:* max_t |q_reduced(t) − x_S,full(t)| < 1e-6 at
  ε_m = 0.5 over t ∈ [0,12], with the h → h/2 error ratio in
  [8, 32] (4th order). Bath-propagator composition identity
  U_B(t,s)U_B(s,r) = U_B(t,r) to < 1e-10 (halt-grade).
  Frozen consequence: **the exact finite reduction is not a
  stationary accident; ε extends constructively to stepped
  nonstationary M(t) in-class.**
- **L-S (stationary restoration — outcome-1 continuity clause).**
  - (a) ε_m = 0: kernel anchored in different epochs identical,
    max_τ |k(t₁+τ,t₁) − k(t₂+τ,t₂)| < 1e-10 (halt-grade): K(t,s)
    collapses to K(t−s) exactly when TTI is restored.
  - (b) continuity: dev(ε_m) = max over the cross-boundary grid of
    |k_{ε_m} − k₀|; ratio dev(0.02)/dev(0.01) ∈ [1.8, 2.2] (linear
    response of the kernel to the TTI-breaking amplitude).
- **L-P (earned structure preserved).**
  - Passivity: min eig K(t) > 0 in both epochs; ‖x(t)‖ monotone
    nonincreasing (tolerance 1e-12).
  - Hierarchy positivity (the stationarity-independent formulation of
    admissibility): the multi-time Gram G_ij = [U(t_i,0)U(t_j,0)ᵀ]₀₀
    at t_i = 0.4i, i = 1…8, ε_m = 0.5, has min eigenvalue ≥ −1e-10
    (halt-grade). Tamper control: off-diagonal inflation ×1.5 must be
    detected (min eig < −1e-8).
  - Bernstein form per epoch: every frozen-epoch kernel weight
    u_l² ≥ −1e-12 (each snapshot stays in the earned completely
    monotone class).
- **L-B (what does NOT extend — the boundary component).**
  - (a) Same-lag drift at ε_m = 0.5: D = max_{τ∈[0,3]}
    |k(2+τ,2) − k(6+τ,6)| / max_τ |k(2+τ,2)| **> 0.1** — the
    generated kernel is genuinely two-time (measured, from the
    microscopic side, with no cosmological input).
  - (b) The local-anchor family k_frozen(a)(t−s), a ∈ {s, t,
    (t+s)/2}: worst relative error on cross-boundary samples
    (t−s ∈ [0.5, 3]) **> 0.05 for every member** — no single-frozen-
    spectral-measure rule reproduces the crossing kernel.
  - Frozen consequence: the **map** extends, but the **stationary
    spectral packaging does not**: no single spectral measure ρ(τ)
    and no single-frequency pair (J, ν)(ω) represents K(t,s). The
    priced additional structure is **exhibited constructively by the
    solver itself**: the per-epoch spectral data PLUS the mixing
    datum C = V_{e′}ᵀV_e (equivalently, the bath propagator family) —
    a two-time spectral datum. This names the S1 boundary instead of
    leaving it a hole.
- **L-D (labeled diagnostics, no gates).** N ∈ {12, 24} reduction
  residuals (scale check); the separable rank of the sampled k(t,s)
  (SVD) against bath size — reported only.

## 3. OUTCOME RULE (frozen, mechanical)

- **Map:** DERIVED EXTENSION (in-class) iff L-E and L-S(a) hold.
- **Continuity:** established iff L-S(b) holds.
- **Structure preservation:** established iff all L-P gates hold;
  any L-P failure = **FAILURE** (outcome 3), preserved.
- **Packaging:** PRINCIPLED DOMAIN BOUNDARY for (ρ, (J,ν)(ω)) iff
  L-B(a) and L-B(b) hold, with the priced datum named as above; if
  either fails red, it stays red with a labeled diagnostic.
- **Composite (predicted shape, frozen):** DERIVED EXTENSION for the
  map + structures, PRINCIPLED DOMAIN BOUNDARY for the stationary
  packaging — i.e. **S1 is crossed constructively at finite level
  in-class, and the seam's remainder is relocated to C1-b/C1-c plus
  the certified packaging boundary.**
- No absolute exponent is computed anywhere; nothing here touches
  ω⁷, Class-4, GR-1, or any closed fork.

## 4. CONTROLS

- Halt-grade: composition identity; ε_m = 0 exact stationarity;
  Gram PSD; Bernstein weights.
- Detecting controls: the Gram tamper (×1.5 off-diagonal); the
  RK4 h → h/2 convergence ratio.
- Exactness anchors: propagators via cyclic Jacobi (reused
  `jacobi_eig`); reconstruction identity e^{−K·0} = 1 to 1e-12.
- Seed-free: the instrument is deterministic.

## 5. DELIVERABLES AND STOP

1. `calc/c1_seam.py` (pure stdlib; emits `C1_SEAM_RESULT.json`,
   sha-hashed).
2. `C1_STATIONARITY_SEAM_VERDICT_01.md` and a closing comment on
   Issue #2.
3. **HARD STOP after the C1-a verdict.** C1-b and C1-c are named,
   not opened. No C2 content.
