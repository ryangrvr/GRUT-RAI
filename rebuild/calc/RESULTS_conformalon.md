# The conformalon does double duty? — joint rung-7 / rung-9 result

**Date:** 2026-06-26 · **Code:** `calc/two_scale_desitter.py`, `calc/conformalon_joint.py` +
7-agent workflow (Starobinsky–Yokoyama / de Sitter dynamical-mass, primary-verified).
**Status:** the first *potentially additive* lead of the rebuild — a decidable hypothesis, not
an established result. Reported with the workflow critic's corrections folded in.

## The hypothesis
The two open back-half items might be one object. Rung 9: does the **conformalon** (the contested
dynamical conformal mode of the trace anomaly) go dynamical and de-anchor α? Rung 7: where does
the cosmological relaxation scale τ₂ ∼ 1/H come from? The conformalon is a light, self-interacting
conformal scalar; the relaxation needs a light, self-interacting scalar that gets a de Sitter
dynamical mass. *Same job description.* If true, one anomaly-fixed number Q² (= field content)
governs both, and the conformalon flips from a *threat* to α into the *feature* that supplies w(z).

## The conformalon's action (what the self-coupling actually is)
g_μν = e^{2σ}ĝ_μν. The Riegert / Antoniadis–Mottola anomaly-induced action gives σ:
- a **fourth-order** Paneitz kinetic term σΔ₄σ (higher-derivative, not an ordinary scalar);
- coefficient **Q² = −2b′ fixed by field content** (b′ ∝ N_S + 11N_F + 62N_V) — *why α can anchor*;
- **Liouville self-interactions** e^{2nσ}, the dominant being Λ∫√ĝ e^{4σ}.
So the "λ" is really Q², one number set by the Standard-Model field content.

## What is grounded vs what is inserted (critic-corrected)
**Forced by the de Sitter horizon** (primary-verified): the noise amplitude H/2π = T_dS, and the
*existence* of a stochastic relaxation toward the Starobinsky–Yokoyama equilibrium. τ_relax = 3H/m²
(SY 1994), m²_eff ∼ √λ H² for a self-coupled field (Beneke–Moch; Rajaraman; Serreau), and m_eff/H
fixed at every epoch by the dS-invariant attractor ("re-equilibrates to whatever H is").

**NOT forced — inserted:** the timescale τ₂ ∼ 1/H.
- *Free-field horn:* needs a tuned m ∼ H₀ (unprotected relevant operator, η-problem). Inserted.
- *Self-coupled horn:* **relocates** the insertion from one tuned number to a structural bundle —
  a light scalar IR mode + an O(1) self-coupling + broken shift symmetry. More natural, **not
  forced**. And τ ∼ 1/(√λ H) equals a Hubble time only for λ ∼ O(1), exactly where the SY √λH
  attractor (derived at weak coupling) is **unverified** — the magnitude and the mechanism are
  required in mutually unverified regimes. This is the load-bearing caveat.

The coincidence is **partially discharged, not eliminated**: tracking removes the mass-tuning, but
the onset coincidence (why ρ_φ ≈ ρ_m now) is relocated, not solved.

## The two computations that decide it
1. **Prefactor ratio (compatibility):** α-shift = k_α⟨σ²⟩, w-deviation = k_w⟨σ²⟩. α "held twice"
   (δα/α ≲ 0.03) and DESI (1+w₀ ∼ 0.2) are compatible **iff k_w/k_α ≥ 7**. One number from the
   Antoniadis–Mottola action: ≥ 7 → one Q² does both; < 7 → mirage, cleanly. (α responds to the
   UV/horizon moment of ⟨σ²⟩, w to the superhorizon IR moment — different moments of one field, so
   the ratio is the whole ballgame.)
2. **Stress sign (shape):** the lag-driven w(z) (m_eff chasing a dropping H through matter→DE) gives
   **w₀ ≈ −0.87, w_a ≈ −0.08 — DESI's quintom sign** (w₀>−1, w_a<0), unlike the passive relaxor's
   wrong-sign w_a>0. Toy magnitude is small; the *sign* is the result. If the real conformalon
   stress tensor preserves it, GRUT predicts a w(z) shape from one coupling.

## Gates on the conformalon (unverified — the honest fence)
(a) its IR self-coupling is O(1) and the sign gives m²_eff > 0 (not tachyonic);
(b) **does the 4th-order conformal mode actually get a SY-type √λH attractor, or does conformal
   symmetry protect/gap it differently?** (conformal symmetry is double-edged) — the deepest gate;
(c) the anomaly coefficient maps to an effective λ of the right sign and magnitude;
(d) the weak-coupling SY attractor survives to O(1) coupling under full in-in resummation.

## Verdict
A real, economical, **decidable** hypothesis: one anomaly-fixed number could collapse rung 7 and
rung 9 into one, and the w(z) sign comes out right for the first time. It is **not** forced and
**not** established — it relocates an insertion to a more natural bundle and rests on gates (a)–(d).
But it is the first lead that could *add* rather than recover, and it is decided by two concrete
calculations, not by taste.

## Next concrete step
Compute, from the anomaly-induced action in de Sitter: (1) k_w/k_α, and (2) the conformalon stress
sign. Two numbers decide whether two open rungs collapse into one.

## Quantitative update — the actual Q²_SM (calc/conformalon_q2_band.py, 2026-06-26)
Q² is **fixed by SM field content, not fit**: N_S=4, N_WF=45 (48 with ν_R), N_V=12 →
**Q²_SM ≈ 5.53** (positive, stable; a_SM ≈ 2.77, Q² ≈ 2a). So ⟨σ²⟩ = K_σ/Q²_SM ≈ **0.18·K_σ**.

**GROUNDED RESULT (prefactors pinned against primaries; supersedes the "near-hit"):** Q²_SM ≈ 5.53
is confirmed (AMM PRD 55; Mottola 1008.5006). But the mode is **not** protected — Weyl-covariant Δ₄
makes σ a *free* massless 4th-order field, ⟨σ²⟩ = K_σ/Q² with **K_σ ~ (1/4π²)·N** (loop-sized per
e-fold, growing *secularly*, not an O(1) equilibrium). The connection closes for three independent,
primary-verified reasons:
1. **Wrong equation of state.** The pinned conformal-mode fluctuation stress is **w = +1/3**
   (radiation-like, redshifts a⁻⁴; Anderson–Molina-Paris–Mottola 0907.0823 eqs 8.14/8.16) — not a
   dark-energy deviation near −1 at all.
2. **Magnitude, with the prefactor carried on both legs.** k_w and k_α both carry the same
   1/(2Q²) ≈ 0.09; the w-deviation is then ~0.024, **~8× below** DESI's 0.2 (at N=60; the ratio rises toward ~11× at fewer e-folds, since ⟨σ²⟩ grows with N).
3. **k_α plausibly zero.** The b′/a anomaly coefficient is one-loop-exact (Wess–Zumino/Riegert), so
   the α self-shift is plausibly protected to zero — protection bites at the *anomaly-coefficient*
   level, not the mode level.

**The "near-hit" was a dropped-prefactor artifact.** Setting ⟨σ²⟩ = 1/Q² ≈ 0.18 (K_σ ~ O(1)) and
comparing to DESI's 0.2 silently dropped the 1/(2Q²) on the w-leg — flagged by the grounding's
anti-laundering critic as the exact laundering this project forbids. With the prefactor restored,
there is no near-hit and no window. Outcome **C — closed.**

## Banking notes (2026-06-27, consolidated relay)
- **The killer is leg-2, not Wess–Zumino.** The shift/WZ symmetry forbids only a *Lagrangian* m²σ²
  mass term (leg-1) — it is **not** the protector. The Starobinsky–Yokoyama obstruction is **leg-2**:
  the Liouville potential e^{4σ} has **no bounded-below minimum** (a monotone runaway), so there is
  no stationary O(1) equilibrium for a √λH dynamical mass to form around. Carry the secular factor
  explicitly — ⟨σ²⟩ ~ N/((4π)²Q²), K_σ loop-sized and growing per e-fold — and state the result as
  **"too small at realistic N," not "never O(1)."**
- **One-point ≠ two-point — §8 stays OPEN.** This closure controls **one-point** objects (⟨σ²⟩ and
  the one-point stress ⟨T_μν⟩, w=+1/3). It does **not** bound the gauge-invariant **two-point**
  ⟨T_ab T_cd⟩: **⟨σ²⟩ ≠ ⟨T_ab T_cd⟩.** The two-point secular-growth tension is untouched and remains
  **OPEN** (writeup §8). Closing the phenomenological sub-thread does **not** close §8.
- **Magnitude recompute (grounded, supersedes the relay's "~1e-4").** The relay's illustrative
  "⟨σ²⟩ ~ 1e-4 at N=60, Q²~3000" used a loose "Q²~thousands" prose figure; the workspace's grounded
  **Q²_SM ≈ 5.53** (computed; AMM/Mottola) is authoritative, so ~3000 is dropped. Recomputing fresh
  in the workspace formula ⟨σ²⟩ = N/(4π²·Q²_SM):
    - N=60 → ⟨σ²⟩ ≈ **0.27** — only ~3.6× below O(1) (**~0.6 orders**, **NOT** the ~4 orders the
      1e-4 framing implied);
    - O(1) reached only at **N ≈ 4π²·Q²_SM ≈ 218 e-folds** (hundreds); it grows secularly with N.
  So the honest magnitude buffer is **modest — sub-O(1) at realistic N, reaching O(1) only at
  ~hundreds of e-folds** — materially weaker reassurance than the relay carried.
- **Outcome C does not depend on the magnitude.** The closure **leads on the equation of state**
  (w = +1/3, radiation-like a⁻⁴ — the **wrong** EoS for a DE deviation near −1; magnitude-independent),
  with the w-deviation leg (k_w⟨σ²⟩ = [1/(2Q²)]·⟨σ²⟩ ≈ **0.025 at N=60, ~8× below DESI's 0.2**,
  computed with the **same** grounded Q²≈5.53) as support. The weakened ⟨σ²⟩ magnitude therefore does
  **not** reopen the thread — Outcome **C (closed)** rests on the EoS argument, which is exactly why
  we lead with it. (Reproduce: `python3 -c "import math;Q2=5.53;f=4*math.pi**2;print([round(N/f/Q2,3) for N in (60,)],round(f*Q2))"`.)

## One-line question for the specialist
> For the 4th-order anomaly-induced conformal mode in de Sitter, does it acquire a Starobinsky–
> Yokoyama-type dynamical mass m²_eff ∼ √λ H² (so it relaxes on ∼1/H and supplies w(z)), or does
> the conformal symmetry of the Paneitz action protect/gap it so the SY attractor does not apply —
> and is its coupling to the cosmological stress ≳ 7× its coupling to the running of the a-anomaly?
