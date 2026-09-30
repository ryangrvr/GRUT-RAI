# S2-1 — NOISE-ORIGIN DISCRIMINATOR CHARTER 01 (C-B; DRAFT)

**STATUS: DRAFT FOR OWNER REVIEW. NOT FROZEN. NOT RUN. NOT EXECUTABLE.**
- **Authority:** `S2_CAMPAIGN_OWNER_DIRECTION_01.md` §11. The charter is drafted only because the S2-0
  gate proposes MINIMAL-CLASS-FOUND (`S2_NOISE_ORIGIN_HARD_DDET_01.md` §5).
- **Execution needs:**
  - owner review and freeze;
  - a **campaign-specific v4 exception** (none is granted);
  - a ruling on flag F-1.
- **Date:** 2026-09-30 · **Branch:** `master-w25bu9`.

## §0 Target

Confirm, at exact (theorem/rational) grade on the declared C-B members, the S2-0 discriminator:

> the retained mean response map m₁(t; a) of dx = [−Kx − 4βx^{∘3}]dt + B dW differs from that of every
> deterministic flow of the same drift with preparation-independent hidden initial data. The leading
> difference is −12βT₁a·t².

The charter also produces the exact higher Taylor coefficients, without claiming any finite-time
magnitude.

## §1 Parent and members (all declared; no new ingredient)

- **K = K_b** (sealed, 23 sites, rational).
- **Drift:** f_β = −Kx − 4βx^{∘3}.
- **Noise:** Q = 2·diag(T_i), additive, so the result is convention-free.
- **Members:**
  - β ∈ {0 (control), 0.03, 0.1, 0.3, 1.0, 3.0};
  - T-profiles **F** (T_i ≡ 1; primary) and **G(∞)** (T₁ = 0; a higher-order control, where the t²
    coefficient must vanish);
  - preparations a ∈ {±0.001, ±1.0, ±3.0}, which are the declared values and their negatives, at
    least 5 distinct and nonzero.

## §2 Execution (exact; deterministic; no simulation, no RNG)

- **E-1: exact Dynkin coefficients.** For n ≤ n_max, compute, in exact rational arithmetic:
  - c_n^𝒮(a) := (𝓛ⁿx₁)(a·e₁), with 𝓛 = f·∇ + ½Q:∇∇;
  - c_n^φ(a) := ((f·∇)ⁿx₁)(a·e₁).

  Here n_max = 6 is proposed (OR-2). By locality (K is tridiagonal), 𝓛ⁿx₁ involves only sites
  1 … n + 1. Report Δ_n(a) = c_n^𝒮 − c_n^φ, as exact rationals.
- **E-2: the M2 no-go at declared generality.**
  - A formal proof, restated with explicit moment conditions (verifier: finite 7th moments suffice
    for orders ≤ 2 plus the remainder).
  - Extended symbolically to the order at which the first nonzero Δ_n appears for each T-profile.
  - Include the Dirac-shift single-preparation counter-construction, to document that a single
    preparation is not decisive.
- **E-3: theorem obligation T-HT** (mandatory only if F-1(b) is ruled). Either close or refute the
  no-go for hidden laws ν with 𝔼|ξ| < ∞ but infinite higher moments.
- **E-4: controls** (integrity):
  - β = 0 ⇒ Δ_n ≡ 0 for every n (Theorem LD instantiated).
  - G(∞) ⇒ Δ₂ = 0 exactly. The first nonzero order is reported. (The T4 correction predicts a
    higher-order separation through coupling; this is not assumed.)
  - A re-derivation on the verifier's generic 2- and 4-site symbolic chain reproduces
    Δ₂ = −12βT₁a·(t²-normalized) and Δ₃ = 4βT₁a(44βa² + 5K₁₁).

## §3 Outcomes (proposed; to freeze at freeze)

1. **RUN VOID:** an integrity failure (E-4, or an arithmetic or locality check). Preserve the defect;
   no re-run without a ruling.
2. **DISCRIMINATOR-CONFIRMED:**
   - Δ₂(a) = −24βT₁a (in the coefficient-of-t²/2 normalization) exactly, for every declared (β > 0,
     F, a);
   - the M2 no-go is proved at the admissibility class ruled under F-1;
   - the controls pass.
3. **DISCRIMINATOR-CONFIRMED-FINITE-MOMENT:** as item 2, but under F-1(b) with T-HT left open.
4. **DISCRIMINATOR-REFUTED:** the exact coefficients contradict the S2-0 identity, or an M2 ν
   reproducing the response map is exhibited.

**No finite-time magnitude, sign-over-a-window or "size of the effect" claim** is made unless a
rigorous remainder bound is separately chartered (OR-3).

## §4 Fences

- **First-gate comparison only.** The Hamiltonian-bath (enlarged deterministic) comparison is
  deferred, and becomes eligible only if S2-1 confirms.
- **Conditional on the declared L0-1c drift**, a supplied premise (S-5).
- **The claim** is only that primitive forcing leaves response structure that
  preparation-independent initial uncertainty cannot reproduce in C-B. It is **not** "noise is
  primitive".
- **Not authorized:**
  - simulation or RNG;
  - S-3, S-6, S5-WB/OD;
  - gravity, Π₀ or cosmology.

## §5 Open items for owner review

- **OR-1 (= S2-0 F-1):** hidden-law admissibility: finite moments (a), or arbitrary with T-HT (b).
- **OR-2:** n_max (6 is proposed), and whether E-1 runs on all members or only on the adjudicating
  set (β ∈ {1.0, 3.0}; a ∈ {±1, ±3}).
- **OR-3:** whether to add a rigorous finite-time remainder bound (Lyapunov-moment-based) so that a
  finite-window statement becomes possible, or to stay at Taylor grade.
- **OR-4:** whether to include G(∞) and GR(∞) as the T₁ = 0 / T₁ > 0 profile controls.

**Artifacts at execution:**
- `calc/s2_noise_origin.py`, exact rational and sympy only;
- `S2_NOISE_ORIGIN_RESULT.json`;
- `S2_NOISE_ORIGIN_VERDICT_01.md`.

Then **HARD STOP.**
