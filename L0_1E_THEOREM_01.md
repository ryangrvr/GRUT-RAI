# L0-1e — D-DET THEOREM DOCUMENT 01 (O-3 lines; O-4 completion) + FROZEN APPENDIX LIST

**Date:** 2026-09-29 · **Authority:** owner ruling `5888965691`
(`L0_1E_OWNER_RULING_01.md`). O-3 is DISCHARGED at identity-grade. O-4
is completed as a theorem document with an exact computational
appendix, not a gated run. **This commit freezes the appendix's
quantity list (§6) before any of it is evaluated.** Nothing that is
unevaluated here is presented as a prediction.

**Sources:** the L0-1e draft charter (`5c71374`) and its analytic-only
review (`L0_1E_PREFREEZE_REVIEW_01.md`). The theorems below were
derived or confirmed there by three reviewers and the operator, with
toy checks on non-member matrices only. The mechanical fixes that
review listed are applied here. **No member quantity has been computed
at any point.**

**Setting (the class; every statement is scoped to it).**
- K = K_b is the sealed C1 bath, the (1:, 1:) block of `build_K(24, 0)`:
  23×23, symmetric, irreducible tridiagonal, positive definite. It is
  built exactly as M = 10K from integers.
- The dynamics are dx = −Kx dt + B dW with Q = BBᵀ = 2·diag(T_i),
  T_i ≥ 0 declared rationals, **never constructed from K and never set
  from rung2's KMS lock.**
- The objects (R-2):
  - response: k_resp(τ) = e₁ᵀe^{−Kτ}e₁;
  - correlation: C(τ) = e₁ᵀe^{−Kτ}y, with y = Σe₁ and Σ the unique
    solution of KΣ + ΣK = Q;
  - correlation moments mₙ = e₁ᵀKⁿy; response moments sₙ = e₁ᵀKⁿe₁
    (both in K units; the appendix computes in M units and converts,
    mₙ(M) = 10ⁿmₙ).

## §1 Foundations

**T-0 (Gaussian completeness; regression theorem).** The process is
Gaussian. Its stationary law N(0, Σ) exists and is unique because −K
is Hurwitz, and Cov(x(t+τ), x(t)) = e^{−Kτ}Σ. The conditional mean is
E[x(t+τ) | x(t)] = e^{−Kτ}x(t), and that follows *from* the stochastic
model. **So the correlation battery does not presuppose the deleted
structure (determinism);** it relies on linear drift and additive
noise, both held. This is the registry compliance the review asked to
be shown.

**T-1 (closed-form spectrum).** K = 0.3I + L, where L is the path
Laplacian on 23 sites, Dirichlet at site 1 (the spring to the removed
system site) and Neumann at site 23 (the free end). Therefore
**λ_k = 2.3 − 2cos((2k−1)π/47)** and v_k(i) ∝ sin((2k−1)iπ/47),
k = 1 … 23. The spectrum is simple, and u_k = v_k(1) ≠ 0 for every k.
λ₁ ≈ 0.30447, matching the record's μ.

**T-2 (the weight formula).**
C(τ) = Σ_k w_k e^{−λ_kτ}, with

> w_k(T) = 2·u_k·Σ_j T_j·v_k(j)·[(K + λ_k I)⁻¹]_{j1}.

**C is completely monotone (CM) ⟺ every w_k ≥ 0**, by Bernstein and
the uniqueness of the Laplace representation over distinct positive
λ_k.

## §2 O-3 — determinism with FDT held (DISCHARGED, identity-grade)

**T-3 (F-5, noise-blindness).** d⟨x⟩/dt = −K⟨x⟩ exactly, so k_resp is
the sealed kernel under every noise profile.

> **Line O3-L1:** DETERMINISM: NOT-LOAD-BEARING for P^resp, every
> component, at every declared profile. *Theorem.* The appendix's
> sealed replication is a control, not an instantiation.

**T-4 (the FDT member).** Q = 2I gives Σ = K⁻¹ uniquely. Then
mₙ = s_{n−1} for n ≥ 1; w_k = u_k²/λ_k > 0, so C is exactly CM and
hence monotone decreasing; and −C′ = k_resp exactly. P_memory^corr at
F: the exponential bound C ≤ e^{−λ₁τ}·(K⁻¹)₁₁ is identity-held. The
comparator's grade is *evaluated* in the appendix (B4); it is not a
theorem.

> **Line O3-L2:** DETERMINISM: NOT-LOAD-BEARING for P^corr when FDT
> holds. **Components (a), (b), (c): identity. P_memory^corr:** the
> exponential bound is identity-held and the comparator reading is
> reported in the appendix. *The FDT relation −C′ = k_resp is a
> consistency note, not a registry component.*

**Scope and limit, carried on O-3's face.** This answers the predicate
posed. Whether noise is **primitive** is not decided in this class: the
linear-Gaussian observational-equivalence theorem makes primitive and
derived noise indistinguishable at second order. That question is
successor item S-1.

## §3 O-4 — noise–dissipation mismatch: the theorems

**T-5 (nonnegativity, strict).** −K + cI ≥ 0 entrywise and K is
irreducible, so e^{−Ks} > 0 entrywise for s > 0. Hence y > 0 entrywise
for every nonzero profile, and C(τ) > 0. **Component (a) is
identity-held. Mismatch never makes the correlation negative.**

**T-6 (the cone).** Each w_k is linear in T, so the CM set 𝒦 is a
**convex polyhedral cone**. The uniform profile U lies in its interior
(T-4), so **CM survives every sufficiently mild FDT violation**, with
"sufficiently" unbounded. For a family T(R) = U + (R−1)·S, R ≥ 1:
- if S ∈ 𝒦, CM holds for every R;
- otherwise CM holds **exactly for R ≤ R***, with
  R* = 1 + min_{k: w_k(S)<0} w_k(U)/|w_k(S)|. At R* one weight is zero
  and C is still CM.

**T-7 (the odd-moment hierarchy).** Let G_ab = (Kᵃe₁)ᵀΣ(Kᵇe₁) and
q_ab = (Kᵃe₁)ᵀQ(Kᵇe₁). The Lyapunov equation gives
G_{a+1,b} + G_{a,b+1} = q_ab, and G is symmetric, so

> m_{2j+1} = Σ_{a=0}^{j−1}(−1)ᵃ q_{2j−a,a} + (−1)ʲ q_{jj}/2,

which is linear in T₁ … T_{j+1}. With a = K₁₁ = 2.3 and b = |K₁₂| = 1:
- **m₁ = T₁**
- m₃ = (a² + 2b²)T₁ − b²T₂
- m₅ = (a⁴ + 8a²b² + 5b⁴)T₁ − (2a²b² + 4b⁴)T₂ + b⁴T₃

**CM requires every m_{2j+1} > 0** (for a nonzero CM C,
m_{2j+1} = Σw_kλ_k^{2j+1} > 0). *Reading: correlation CM at the
retained site is gated by a near-to-far hierarchy of temperature
conditions; the retained site's own temperature enters first.*

**T-8 (the identity breaches).**
- **Zero retained-site temperature:** T₁ = 0 gives m₁ = 0 while
  y₁ > 0, so C is not CM. **G(∞) and H(∞) breach by identity.**
- **The ramp, via m₃:** on G(R), T₁ = 1 and T₂ = 1 + (R−1)/22, so
  m₃ = s₂ − b²(R−1)/22 with s₂ = a² + b² = 6.29. That is negative for
  **R > 1 + 22·s₂ ≈ 139.4**. **G(1000) breaches by identity, with
  T₁ > 0.** This is a genuine *mismatch* breach: the retained site is
  thermally driven, and it still breaches.
- By T-6, **the ramp and hot-spot families each have a finite
  threshold.** On the ramp, R* ≤ 139.4 (from m₃).

**T-9 (identity-interior directions).**
- **Perron:** w₁(T) > 0 for every nonzero T ≥ 0. The slowest mode's
  weight is always positive, so breaches live only in modes k ≥ 2.
- **Retained-site heating:** T = δ₁ gives
  w_k = 2u_k²[(K+λ_k)⁻¹]₁₁ > 0, which is interior.
- **Every profile aU + bδ₁ (a, b ≥ 0, not both zero) is CM at every
  strength.**

**T-10 (one line, not two axes).** GR(∞) = U − G(∞) = G(0): the
reversed ramp is the ramp line continued to R = 0. GR(∞) ∈ 𝒦 ⟺ the
ramp line's lower exit R₋ satisfies R₋ ≤ 0. **Sufficient route:**
GR(∞) = (1/22)·Σ_{m=1}^{22} 1_{[1..m]}, so if every step profile
1_{[1..m]} is in 𝒦, then so is GR(∞).

**T-11 (the deletion is real).** For a nonuniform diagonal Q and an
irreducible tridiagonal K, **KΣ ≠ ΣK.** Commuting would force
Σ = K⁻¹Q/2 to be symmetric, but [Q, K]_{i,i+1} = 2(Tᵢ − T_{i+1})K_{i,i+1}
≠ 0 for some adjacent pair. This is the Ornstein–Uhlenbeck
**detailed-balance break**, not the removal of determinism:
determinism is equally absent at F, where KΣ = ΣK.

## §4 O-4 — the lines (theorem-grade; the appendix instantiates and maps)

**Scope clause (every line):** *the sealed C1 bath; linear additive
Gaussian noise with diagonal intensity 2·diag(T_i); declared rational
profiles; exact rational arithmetic; family statements extend to every
R only through T-6.*

- **O4-L1 (existence and location; theorem):** NOISE–DISSIPATION
  MISMATCH: LOAD-BEARING for P_positivity^corr (c) beyond a finite
  threshold in the ramp and hot-spot families. **Two readings, both on
  the face:**
  - at T₁ = 0 (G(∞), H(∞)), the breach is a *noise-free retained
    coordinate*, a determinism-flavoured mechanism;
  - at T₁ > 0, G(1000) breaches through m₃: a *genuine mismatch*
    breach, with the retained site driven.

  Ramp threshold: R* ≤ 139.4 by T-8. Its exact value is evaluated in
  the appendix (B2).
- **O4-L2 (survival; theorem):** NOISE–DISSIPATION MISMATCH:
  NOT-LOAD-BEARING for P_positivity^corr (c) in an open neighbourhood
  of FDT, and in the directions aU + bδ₁ at every strength (T-6, T-9).
  **Component (a) is identity-held at every profile (T-5).**
  Component (b) is reported per profile in the appendix (B4).
- **O4-L3 (P_memory^corr):** the exponential bound is identity-held at
  every profile. The envelope-comparator grade is *evaluated* per
  profile in the appendix (B4). An ALGEBRAIC reading would be recorded
  as COMPARATOR-LIMITATION, never as mismatch load-bearing for memory.
- **Proposed O-4 terminal label: CLASS-SPLIT, identity-determined, and
  recorded as such.** No evaluation can change it. The subclasses are
  outcome-independent and name their certifying members:
  - the **cone-interior class**: F (T-4) and δ₁ (T-9);
  - the **breach class**: G(∞), H(∞) (T-8, zero retained temperature)
    and G(1000) (T-8, m₃ < 0 at T₁ > 0).

  All of these are identity members; the appendix confirms them. The
  owner assigns the label.

## §5 The O-7 input (theorem-grade; scoped, not universal)

By T-6, T-11 and T-3: **detailed balance broken through the noise is
not sufficient to break correlation CM**, since it survives an open
neighbourhood of FDT, **and it cannot touch response CM at all.** In
O-1, generator-side cycle affinity broke *response* CM at every
declared γ > 0.

This contrast differs across object (correlation vs response),
substrate (chain vs ring), and route (Q vs K). It is **not** a
universal statement, and must not be phrased as "detailed balance is
not fundamental". Separating the axes needs successor item S-3. The
reversal diagnostic's cautions apply: one arm is F-5 (an identity) and
another is FDT.

## §6 THE APPENDIX — frozen quantity list (evaluated exactly, once, after this commit)

**Instrument:** `calc/l01e_appendix.py`. Pure stdlib; exact integers
and `fractions`; `build_K` and `jacobi_eig` imported unchanged; the
textual copy of `fit_residuals` + TAUS. **No RNG.** A single evaluation
writes `L0_1E_APPENDIX_RESULT.json` (sha-hashed). Nothing is gated
except identity verifications.

**Profiles (all exact rationals):**

| Profile | T_i (i = 1 … 23) |
|---|---|
| F | 1 |
| δ₁ | δ_{i,1} |
| G(R), R ∈ {2, 10, 100, 1000} | 1 + (R−1)(i−1)/22 |
| G(∞) | (i−1)/22 |
| GR(R), R ∈ {10, 1000} | 1 + (R−1)(23−i)/22 |
| GR(∞) | (23−i)/22 |
| H(1000) | 1 + 999·δ_{i,12} |
| H(∞) | δ_{i,12} |
| S_m, m = 1 … 22 | 1_{[1..m]} (the step profiles of T-10) |

**Part A — identity verifications (halt-grade).** A failure here
means **a defect in this document, disclosed and HALT**, never a
finding.

| # | Verification |
|---|---|
| A1 | Sealed replication: eigen-form k_resp(40) = 6.8195192260507686×10⁻⁹ (|rel Δ| < 10⁻⁹). Sealed `build_K` bath equals float(M/10) entry by entry. |
| A2 | T-1: closed-form λ_k agrees with `jacobi_eig`, max |Δ| < 10⁻¹². |
| A3 | Exact Lyapunov at every profile: KΣ + ΣK − Q = 0 and Σ = Σᵀ, exactly. |
| A4 | T-7: m₁ = T₁, and m₃ and m₅ equal their closed forms, exactly, at every profile. |
| A5 | T-4 (O-3's instantiation): KΣ = I at F; mₙ = s_{n−1} exactly for n = 1 … 47; exact H₀ ≻ 0 with d_c = 23. |
| A6 | T-11: KΣ ≠ ΣK exactly at every nonuniform profile. |
| A7 | T-5: y > 0 entrywise, exactly, at every profile. |
| A8 | T-8: G(∞), H(∞) and G(1000) fail the exact CM test. T-9: F and δ₁ pass it. |
| A9 | T-9 Perron: float w₁ > 0 at every profile. |
| A10 | T-6 cone consistency along each ray. Exact CM statuses are monotone in R (the CM set is [1, R*]). A failing limit shape implies failure at large R. The float R* is consistent with the exact statuses; **exact prevails**, and any disagreement is recorded as a float-instrument defect. |
| A11 | Comparator certification: the textual copy on the eigen-form sealed anchor reproduces R_exp = 1.9809889100368165 and R_alg = 4.7907669413552245 (|Δ| < 10⁻¹²) and the grade string "EXPONENTIAL-GRADE". |

**Part B — the evaluated quantities (reported; not gated; not
predictions).**

| # | Quantity |
|---|---|
| B1 | The exact correlation-CM status, d_c, and H₀ inertia of **every** profile above, including GR(∞) and every S_m. |
| B2 | Float thresholds from T-2 weights: R* for the ramp, reversed-ramp, and hot-spot families; the ramp line's lower exit R₋; and the consistency R₋ ≤ 0 ⟺ GR(∞) ∈ 𝒦. |
| B3 | The signs of m₃ and m₅ at every profile (the T-7 necessary conditions). |
| B4 | From the closed-form weights, on the gated grid τ ∈ [1, 40] step 0.5, per profile: normalized c(τ); the P_memory^corr envelope-comparator grade (R-1); component (b), monotone decrease; the operational Gram minimum eigenvalue (G_ij = c(τ_i + τ_j), τ_i ∈ {1.0 … 20.0}); and E(40). |
| B5 | FDT-deviation ratios mₙ/(T₁·s_{n−1}), n = 2 … 5, wherever T₁ > 0. Those at n = 3 and 5 are identity-determined by T-7 and labeled so. |
| B6 | The commutator ratio ‖KΣ − ΣK‖_F / ‖KΣ‖_F per profile. |

**After evaluation:** the appendix record `L0_1E_APPENDIX_01.md`
reports Part A's pass/fail and Part B's values. It adds no line and
changes no label. **HARD STOP** pending the owner's assignment of O-4's
terminal label.
