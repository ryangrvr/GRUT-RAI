# S5-1 — CONSERVATIVE-ORIGIN VERDICT 01

**Mechanical terminal: MARKOV-LIMIT-OTHER-CLASS**, conditional on the admitted weak-coupling
deformation L-vH.

**Status:** proposed for owner adjudication. **HARD STOP.**

## Provenance

| Item | Value |
|---|---|
| Frozen charter | `S5_CONSERVATIVE_ORIGIN_01.md` at `d603db5` |
| Authority | `S5_OWNER_RULING_02.md`, one analytic execution, S5-1-only v4 exception |
| Analytic execution | `S5_CONSERVATIVE_ORIGIN_DERIVATION_01.md`, committed at `6170129` **before any numerical check** |
| Verification / cross-check script | `calc/s5_conservative_origin.py`, committed at `ed2bbe3` before its single run |
| Result | `S5_CONSERVATIVE_ORIGIN_RESULT.json` (sha256 `8e0683fc…`) |
| Executions | One (2 s). No re-run. |

**Disclosed before the run (charter):**
- the auditor's prior expectation that a damped-oscillator Markov law was likely;
- a mental sketch of the problem's structure while preparing the freeze. No member was computed.
  The cross-check g-values and windows were fixed by rule.

## 1. The analytic results (frozen order; each theorem proved in the derivation document)

| Step | Result |
|---|---|
| **1. Finite N** (0 < g ≤ 1) | K_N(g) ≥ 0.3·I (Gershgorin). The spectrum is simple and every weight w_k > 0. Φ_N is almost periodic and does not decay. Φ_N′(0) = A₀, so a semigroup would force φ = cos ω_s t, which is false for N ≥ 2. **There is no exact semigroup of any kind on R1.** The only exact first-order generator is the conservative A. **R2 short-time obstruction:** φ(0) = 1, φ′(0) = 0, φ″(0) = −K₁₁ = −2.3, so e^{−γt} (γ > 0) is impossible at t = 0, and φ is not CM. |
| **2. N = ∞** (g = 1, L-N) | K_∞ = 2.3 − T, with σ = [0.3, 4.3], purely a.c., and a semicircle-type retained measure. **No bound states.** The Stieltjes function F solves F² − wF + 1 = 0 and is irrational, with √ branch points at λ = 0.3 and 4.3. The Laplace transform of φ_∞ is not rational, so it is not a matrix element of any finite semigroup. Φ_∞ → 0 (effective dissipation emerges), with a **t^{−3/2} sign-alternating tail** from the two band edges. This is consistent with O-6 D-1 (t^{−3} in bilinears). |
| **3. Kernel class** | **K-L0 fails** on the retained response at every N, at N = ∞, and for every g, locally (φ″(0) = −K₁₁ < 0) and, at N = ∞, through the branch cut. **Memory diagnostic:** the exact GLE friction kernel is Γ_fric(t) = g²fᵀK_BB⁻¹cos(√K_BB t)f, with Γ_fric″(0) = −g² < 0. It is oscillatory and never white. It is kept separate from k_D. |
| **4. Weak coupling** (L-vH, admitted K(g)) | **PD for all 0 < g ≤ 1** (Schur test). **No bound states** (y² = g² − 1 ≤ 0). The exact density is ρ_g(λ) = g²sin θ/(π[(2 − g²)²cos²θ + g⁴sin²θ]), with 2.3 − λ = 2cos θ. The system frequency sits **at band centre**, and there is no level shift. **Scheffé:** g²ρ̃_g(ω_s + g²x) → Cauchy(κ), with **κ = 1/(2√2.3) = πρ_B(λ_s)/(2ω_s)** (derived). Hence **sup_{t≥0}‖Φ_g(t) − e^{(A₀ − κg²I)t}‖ → 0**, and **Ψ_g(τ) → e^{−κτ}I uniformly in τ ≥ 0.** |
| **Physical reconstruction** | A_eff(g) = A₀ − κg²I on (q₁, p₁). It is time-homogeneous, closed, and restartable in the limit. Its spectrum is **−κg² ± iω_s**, so it is **strictly dissipative (M-1)**. It is the **underdamped oscillator** q̈ + 2κg²q̇ + (ω_s² + κ²g⁴)q = 0. **It is not M-2:** the spectrum is complex, the scalar response e^{−κg²t}cos ω_s t is not CM, there is no autonomous first-order law for q₁, and no slaving (R2 closure fails). |
| **5. NI audit** | Passes. κ, Γ_fric and the exponential are all **derived.** The only K change is g in L-vH. |

## 2. Non-adjudicating checks (all after the analytic results)

**Symbolic re-verification:** S-1, S-2, S-3, S-4, S-6 and S-7 pass.
- S-6 confirms mass 1 for ρ_g at g ∈ {1, 0.5, 0.25}.
- S-7 confirms Γ_fric″(0) = −g² at every N and g.

**S-5 (Scheffé pointwise limit) is flagged FALSE. This is a defect in the pass criterion, preserved and
not re-run.**
- The substantive checks agree:
  - the **sympy limit matches the Cauchy target exactly** (`sympy_limit_matches: true`);
  - the mpmath deviations fall as O(g²) at every x (for example, at x = 0.5: 2.3e-5 → 2.3e-7 →
    2.3e-9).
- **What went wrong:** my criterion demanded *strictly* decreasing deviations at every sampled x. At
  x = 0 the deviation is **identically 0 to working precision** (1.1e-41) for every g, so it cannot
  strictly decrease.
- **Why no re-run:** per ruling S5-02 §2, the analytic terminal is wholly independent of this
  supplementary re-verification. S-5 is not one of the frozen X-checks, and the derivation is the
  proof.

**Frozen cross-checks X-1 … X-5:**

| # | Result |
|---|---|
| X-1 | Closed-form spectra agree to ≤ 2.7e-15 (N = 23, 47, 95). **Pass.** |
| X-2 | Every eigenvalue of K_95(g), for g ∈ {1, 0.5, 0.25}, lies in [0.3, 4.3], with minimum 0.3003 > 0. This is consistent with the no-bound-state theorem. |
| X-3 | Σw_k = 1 and Σw_kλ_k = 2.3, so φ″(0) = −2.3 at all 9 (N, g) members. **Pass.** |
| X-4 | T_rec(95) = 246.41 (v_max = 0.76296). On t ∈ [82.15, 221.75], the derived t^{−3/2} asymptotic formula agrees with φ_95 to a maximum of 6.4% of the local envelope (absolute 7.4e-5). The residual is consistent with the O(t^{−5/2}) correction. |
| X-5 | The sup-deviation of Φ_{95,g} from e^{(A₀ − κg²I)t} over [0, 221.75] is **0.113 at g = 0.5 and 0.035 at g = 0.25**. It decreases, as the theorem requires. |

## 3. Mechanical terminal (charter §8)

1. **UNFORMULABLE:** no.
2. **EXACT-GENERATOR-DERIVED:** no (Steps 1 and 2).
3. **MARKOV-LIMIT-DERIVED (M-2):** no (complex spectrum, not CM, no slaving).
4. **MARKOV-LIMIT-OTHER-CLASS:** **yes.** The admitted L-vH limit derives a genuine, controlled,
   time-homogeneous Markov effective generator for the retained physical variables, A₀ − κg²I. Its
   type is an **underdamped oscillator**, not the Level-0 first-order CM/real-spectrum G-D class.

> **S5-1 = MARKOV-LIMIT-OTHER-CLASS**, conditional on the admitted weak-coupling deformation.
> *The declared local conservative parent derives a genuine Markov effective law, but a different
> one: a damped oscillator, not the Level-0 first-order dissipative generator.*

**Sub-findings carried with the terminal:**
- **Native parent (L-N, g = 1): non-Markovian dissipation only.** There is effective decay, but with
  a branch cut and t^{−3/2} algebraic, sign-alternating memory. At **every fixed g > 0** the dynamics
  keeps the branch cut. Markovianity appears **only in the g → 0 limit.**
- **K-L0 fails everywhere.** The obstruction is already local (φ″(0) = −K₁₁), not only a late-time
  one.
- **Γ_fric** is oscillatory and never white.
- **Missing ingredients for M-2** (indicated, **not** established as necessary, so item 5 does not
  fire):
  - an **overdamped/slaving scale (L-OD)**, which the first-order real-spectrum law needs, whereas the
    admitted damping is O(g²) ≪ ω_s;
  - a **wide-band limit (L-WB)**, which white friction needs.

## 4. Scope and fences

- **SL-1:** the result concerns the **retained site's** reduced law. It says nothing about deriving
  the multi-site Level-0 net ẋ = −Kx.
- **SL-3:** it is conditional on the conservative parent **and** on the weak-coupling deformation.
  O-6 was evaluated at g = 1, where only non-Markovian dissipation holds.
- Nothing here addresses abstract unitary dilations, other spectral densities, L-WB/L-OD as
  derivation routes, S5-2, SF-2, gravity, Π₀ or cosmology.

**Reading.**
- The conservative parent **can derive Markovian dissipation**, as a genuine theorem rather than a
  fit.
- The Markov law it derives is **second-order/inertial** (A₀ survives in the generator).
- The Level-0 **first-order** real-spectrum generator is **not** derived. Its inertia-free,
  completely monotone structure would need a separate slaving/overdamped ingredient that the
  admitted parent does not supply.

## 5. HARD STOP

- Result, verdict and derivation are committed. CURRENT_STATE is updated.
- **Awaiting owner adjudication.**
- No second run, no S5-2, no L-WB/L-OD route, no new parent.
