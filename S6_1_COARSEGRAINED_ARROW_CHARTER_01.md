# S6-1 — COARSE-GRAINED ARROW CHARTER 01

**STATUS: FROZEN FOR EXECUTION.** This charter was amended per `S6_OWNER_RULING_01.md` (Issue #2 comment `5914432316`,
§§8–12).
- **Frozen commit:** the commit that introduces this revision; CURRENT_STATE records its hash.
- **Draft history:** `a9017e8`. The amendment log is in §9.
- **Authorization:** **ONE S6-1 analytic / certified execution** under a campaign-specific v4 exception for S6-1 only.
- **Date:** 2026-09-30 · **Branch:** `master-w25bu9`.

## §0 Targets

| Target | Statement | Members (T_s, T_b) |
|---|---|---|
| **T-1** | Net bath self-energy transfer: the sign of X_J(∞) = ∫₀^∞ f_J dt, forward-oriented | (2,1), (10,1), (1/2,1), (1/10,1) |
| **T-2** | Net entropy-reference approach: X_σ(∞) = D(0) − D(∞) | the same four |
| **T-3** | No erasure for J: X_J(T) > 0 for all T > 0 | L1: (2,1), (10,1) |
| **T-4** | No erasure for σ: X_σ(T) > 0 for all T > 0 | L2: (1/2,1), (1/10,1) |

- **Controls, not targets:** the K-2 members already DECIDED FALSE by I-5 (J on L2, σ on L1). The run reports them, and
  also re-certifies their small-T negativity as a control.
- **Excluded:** K-3, which is ARBITRARY.
- **Orientation** (S6-0 §1.2 and §4.2 Q5):
  - f_J = +J on L1 and −J on L2;
  - σ = −Ḋ on all members.
- **J is the bath self-energy flux** (ruling A-3). Every J conclusion is reported with the equal-temperature offset
  ½T_b r².

## §1 Parent and objects (confirmed record objects only; ruling §2)

**The chain.**
- The O-6 pinned chain, with g = 1 and system site 1 (K₁₁ = 2.3).
- **Primary object:** N = ∞, with K_∞ = 2.3·I − T (T is the half-line adjacency) and the L-N limit.

**The initial state.**
- A product of uncoupled Gibbs states:
  - site 1: ⟨q₁²⟩ = T_s/2.3, ⟨p₁²⟩ = T_s;
  - bath: ⟨q_Bq_Bᵀ⟩ = T_b K_BB⁻¹, ⟨p_Bp_Bᵀ⟩ = T_b I;
  - all cross terms zero.

**The observables.**
- J = ⟨p₂q₁⟩.
- **E₁** = ½(2.3 q₁² + p₁²).
- **E_int** = −q₁q₂.
- **D(t)** = KL(𝒩(0, S₁(t)) ‖ 𝒩(0, S_ref)), where S_ref = T_b·diag(r, 1) and r = (K_∞⁻¹)₁₁.

**Integrals start at t = 0** (ruling A-4).

**Finite-N cross-checks.** N = 95 (declared), for T < T_rec(95) only. They are **never adjudicating**.

## §2 Mandatory analytic theorem block

The block is written in `S6_1_THEOREM_01.md`. It is committed and independently verified **before** the script is
committed.

| Item | Content |
|---|---|
| **LS-0 (spectral representation)** | μ = the e₁-spectral measure of K_∞, dμ = (1/2π)√(4 − (λ − 2.3)²) dλ on [0.3, 4.3]. Equivalently λ = 2.3 − 2cosθ with dμ = (2/π) sin²θ dθ on [0, π]. The exact covariance evolution of the declared state is written in terms of the families I_{k,w,m}(t) = ∫ w(λ) λ^{k/2} cos(√λ t + mπ/2) dμ, with w ∈ {1, 2.3 − λ}. |
| **LS-1 (return to equilibrium)** | S₁(t) → S_ref. The proof covers the Gibbs covariance T_b·diag(K⁻¹, I) and its invariance; the rank-≤3 perturbation; LS-0; absolute continuity with no bound state (consumed from S5); the L¹ property of the spectral weights; and Riemann–Lebesgue. |
| **LS-2 (closed forms)** | X_J(∞) = (T_s − T_b) + ½T_b r² (record convention; the sign flips for L2), and X_σ(∞) = D(0), with r = (2.3 − √1.29)/2. It also gives the exact X_f''(0) and the property X_f(0) = X_f′(0) = 0. |
| **LS-3 (entropy tail)** | The leading asymptotic class of D and Ḋ, via: the quadratic expansion D = ¼‖E‖_F² + O(‖E‖³) with E = S_ref^{-1/2}(S₁ − S_ref)S_ref^{-1/2}; the band-edge stationary-phase leading terms; and the non-degeneracy condition for sign reversal. It states whether the O-6 "t⁻³" wording for Ḋ is a loose upper bound or an incorrect leading power. |
| **LS-4 (tail bound)** | By integration by parts in θ, |I_{k,w,m}(t)| ≤ V_{k,w}/t, where V_{k,w} = ∫₀^π |d/dθ[(2/π) w λ^{(k+1)/2} sinθ]| dθ. The deviations are bilinear in the I's, which gives |X_f(T) − X_f(∞)| ≤ C_f T⁻² (for J) and ‖E(T)‖_F ≤ C_E T⁻² (for σ), with C_f and C_E given by explicit formulas in the V's. |
| **LS-5 (entropy tail inequality)** | If ‖E‖_F ≤ ½, then D ≤ ½‖E‖_F². |

**T-1 and T-2 are theorem-grade only if LS-1 and LS-2 pass verification**, and the run confirms their integrity
identities.

## §3 Deterministic certification protocol (frozen)

### P-1 Arithmetic

- **Package:** `mpmath.iv` interval arithmetic, with `mp.prec = 128` bits.
- **Constants:** every constant (√1.29, r, π, …) is an interval enclosure.
- **Excluded:** floating-point values never enter an adjudicating quantity.

### P-2 Spectral quadrature

Use the θ-trapezoid rule on the even, 2π-periodic integrand F(θ) = w λ^{k/2} cos(√λ t + mπ/2)·(2/π) sin²θ:

> ∫₀^π F dθ = (π/N) Σ_{j=0}^{N−1} F(2πj/N) + ℰ

**Rigorous error bound** (Trefethen–Weideman), with strip half-width a = 1/5:

> |ℰ| ≤ 2πB/(e^{aN} − 1)

The constants are as follows:

| Constant | Value |
|---|---|
| α_min | 2.3 − 2cosh a |
| ν | sinh a / √α_min |
| Λ_max | 2.3 + 2cosh a |
| B | (2/π)·cosh²a · W · Λ_k · cosh(ν t_max) |
| W | 1 for w = 1, and 2cosh a for w = 2.3 − λ |
| Λ_k | α_min^{k/2} for k < 0, and Λ_max^{k/2} for k ≥ 0 |

**Analyticity:** the integrand is analytic for |Im θ| < 1/4, because 2.3 − 2cosh(1/4) > 0.

**Node count:** N(t_max) = ⌈(ν t_max + 100)/a⌉. ℰ enters as an interval ±bound.

### P-3 Small-T region

**Taylor argument.** Since X_f(0) = X_f′(0) = 0 (LS-2),

> X_f(T) = X_f''(0)T²/2 + X_f'''(ξ)T³/6.

**Resolving T₀:**
- For k = 0, 1, …, 20:
  - set T₀ = 2^{−k}·min(1, T\*);
  - take M₃ = the upper bound of |X_f'''| over the box [0, T₀], from order-3 interval Taylor jets.
  - **Accept the first T₀ with T₀·M₃ ≤ 1.5·lower(X_f''(0))**, which is a safety factor of 2.
- If no k succeeds, the small-T region is **UNRESOLVED**.

**The controls use the mirror test:** on (0, T₀], X_f < 0 when X_f''(0) < 0, with the same rule applied to −X_f.

### P-4 Main region [T₀, T\*]

**Enclosure.** A mean-value enclosure of each box [a, b]:

> X_f([a, b]) ⊂ X_f(a) + [0, b − a]·X_f′([a, b])

where X_f(a) is a point enclosure (a jet of order 0), and X_f′([a, b]) comes from an order-1 jet over the box.

**Boxes.** The initial box width is h₀ = 1/16, processed left to right.

**Per-box rules:**
- **Certified:** lower > 0.
- **Otherwise:** evaluate the point enclosures at a and at the midpoint.
  - If either upper bound is < 0 → **FALSE** is certified at that point.
  - Otherwise bisect, up to **depth 16**.
  - A box still unresolved at depth 16 is **UNRESOLVED**.

**Resource cap:** 400,000 box evaluations per member. If the cap is exceeded, the member is **UNRESOLVED** and
processing of that member stops.

### P-5 Tail region T ≥ T\*

**For f = J (T\* is fixed by formula from LS-4 and the proven margin):**
- T\*_J = √(2C_J / lower|X_f(∞)|), rounded up.
- Then |X_f(T) − X_f(∞)| ≤ X_f(∞)/2 for all T ≥ T\*.

**For f = σ:**
- T\*_σ = √(C_E / min(½, √lower D(0))), rounded up.
- Then ‖E‖_F ≤ min(½, √D(0)), so D(T) ≤ ½D(0) (LS-5), and X_σ(T) ≥ D(0)/2.

**Precondition:** X_f(∞) > 0 must first be certified. If X_f(∞) < 0 is certified instead, K-2 is FALSE via the tail.

### P-6 Per-member verdict (T-3 and T-4)

| Verdict | Condition |
|---|---|
| **FALSE** | any certified negative point |
| **TRUE** | the small-T region, every main box and the tail region are all certified positive |
| **UNRESOLVED** | otherwise |

**The resources are fixed.** No rerun with increased resources without an owner ruling.

### P-7 Integrity checks (implementation; a failure gives RUN VOID)

- **(i)** Quadrature reproduces the exact moments m₀ = 1, m₁ = 2.3, m₂ = 6.29 (∫λ^j dμ, at t = 0) and ∫λ⁻¹dμ = r.
- **(ii)** At t = 0, the jets reproduce:
  - the declared initial covariances;
  - ΔQ₁₂(0) = −T_b r², so that Q₁₂(0) = 0;
  - X_f''(0) as given by LS-2.
- **(iii)** Consistency of the derivative: the enclosure of the order-1 jet of X_J contains ±J evaluated from its
  independent formula, at the box endpoints.
- **(iv)** The tail constants are finite and positive.
- **(v)** The closed forms of LS-2 lie in the enclosures of X_f(T\*) ± C_f T\*⁻².

### P-8 Cross-checks (report-only)

- N = 95, float64 eigen-evolution, at T ∈ {0.5, 1, 2, 4, 8}, compared with the midpoints of the N = ∞
  enclosures.
- The leading LS-3 amplitude P(t) is evaluated at two points to certify that it is non-constant (non-degeneracy).

## §4 Outcomes (ruling §11)

**Primary outcome (T-1 and T-2):**

| Outcome | Condition |
|---|---|
| **NET-ARROW-CONFIRMED** | T-1 and T-2 are TRUE for every member |
| **NET-ARROW-PARTIAL** | the result splits by observable or by member |
| **NO-NET-ARROW** | neither observable carries the forward sign on the family |
| **RUN VOID** | an integrity (P-7) or theorem-implementation failure |

**Secondary outcome (T-3 and T-4):**

| Outcome | Condition |
|---|---|
| **NO-ERASURE-ON-OPEN-MEMBERS** | all four open members are TRUE |
| **ERASURE-OCCURS-ON-OPEN-MEMBER** | any open member is FALSE |
| **NO-ERASURE-UNRESOLVED** | otherwise |

**Always reported separately:** the decided switch-on failures (J-L2, σ-L1).

## §5 Execution sequence (ruling §14)

1. `S6_1_THEOREM_01.md`: written, independently verified, committed.
2. `calc/s6_1_certify.py`: committed before its run.
   - Unit tests of the primitives on **non-member** mathematical controls only (quadrature moments, jet algebra
     against series) are permitted before the run and are disclosed.
3. **ONE execution.**
4. Result JSON, then the verdict.
5. **HARD STOP.**

## §6 Fences (ruling §13)

**The strongest statement allowed:**

> In the declared infinite conservative pinned chain, the integrated bath-self-energy transfer and the reduced-state
> entropy measure retain a net direction despite arbitrarily late band-edge-memory backflow.

**Not allowed:**
- "monotonicity is restored";
- "O-6 is repaired";
- "microscopic reversibility is gone";
- "a fundamental thermodynamic arrow";
- "J is a unique heat current".

**O-6 stays FALSIFIED.** Any correction to O-6's Ḋ-tail wording is additive, after LS-3 is accepted.

## §7 Not authorized

- RNG or simulation;
- an ordinary-grid sign gate;
- a second run;
- S-4, S-7 or S-8;
- S5-WB or S5-OD;
- a new reversal diagnostic;
- gravity, Π₀ or cosmology.

## §8 Owner rulings consumed

- A-1 (family aggregation);
- A-2 (K-1 EXECUTABLE until banked here);
- A-3 (the J name and offset);
- A-4 (integration from 0);
- A-5 (Ḋ tail derived here).

## §9 Amendment log (draft `a9017e8` → frozen)

| # | Change | Source |
|---|---|---|
| AM-1 | The targets are renamed precisely (T-1 is net bath self-energy transfer; T-2 is net entropy-reference approach). The opposite-direction K-2 members become controls. | ruling §8 |
| AM-2 | The analytic block LS-0 … LS-5 is mandatory before the script, including the explicit proof elements of LS-1 and the LS-3 non-degeneracy. | ruling §9 |
| AM-3 | The protocol is frozen: interval arithmetic at 128 bits; trapezoid with a rigorous strip bound; the formula for N(t_max); small-T Taylor with a jet bound; mean-value boxes with h₀ = 1/16, depth 16 and a cap of 400k; T\* by formula; the stopping rule; UNRESOLVED. | ruling §10 |
| AM-4 | The outcome map is split into primary (K-1) and secondary (K-2), with NO-ERASURE-UNRESOLVED added. | ruling §§10–11 |
| AM-5 | One execution is authorized under the S6-1 v4 exception. | ruling §12 |
