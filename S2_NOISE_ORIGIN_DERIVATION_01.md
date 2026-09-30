# S2-1 — ANALYTIC DERIVATION 01 (coefficients; finite-moment M2; T-HT)

> **STATUS: DRAFT, PENDING INDEPENDENT ADVERSARIAL VERIFICATION of §1 and §3 (HT-B).**
> - No script has been written or run.
> - Any correction will be applied in a later commit, **before** `calc/s2_noise_origin.py` is
>   committed.
> - This status line will then be updated.

- **Charter:** `S2_NOISE_ORIGIN_CHARTER_01.md`, frozen at `227dd09`.
- **Authority:** `S2_OWNER_RULING_01.md` (one analytic/exact execution; S2-1-only v4 exception).
- **Order:** this document is written and committed **before** `calc/s2_noise_origin.py`. The
  script only instantiates and verifies; it is not the source of any theorem here.
- **Grade:** exact and analytic. No RNG, no simulation.

## §0 Setting and structural facts

**The C-B model.**
- Stochastic: dx = f(x)dt + B dW, with f(x) = −Kx − 4βx^{∘3}, β > 0, and Q = BBᵀ = 2·diag(T_i).
- K = K_b (23 sites): K_ii = 23/10 for i < 23 and 13/10 for i = 23; K_{i,i±1} = −1.
- Generator: 𝓛 = A + D, where A = f·∇ and D = Σ_i T_i∂_i².
- Deterministic flow: φ_t of ẋ = f(x). N = 23.

**Structural facts:**

| Fact | Statement | Reason |
|---|---|---|
| **F1** | K is symmetric positive definite, with λ_min(K) ≥ 0.3 and off-diagonals ≤ 0 | Gershgorin: the rows give 2.3 − 1, 2.3 − 2, and 1.3 − 1 |
| **F2 (cooperative)** | The flow is order-preserving: y ≤ y′ componentwise ⇒ φ_t(y) ≤ φ_t(y′) for all t ≥ 0 | ∂f_i/∂x_j = −K_ij ≥ 0 for i ≠ j (Kamke–Müller) |
| **F3 (contraction)** | \|φ_t(y) − φ_t(y′)\| ≤ e^{−0.3t}\|y − y′\| | Df = −K − 12β·diag(x²) ⪯ −λ_min·I |
| **F4 (coming down from infinity)** | For u = \|x\|²: u̇ = −2xᵀKx − 8βΣx_i⁴ ≤ −(8β/N)u², using Σx_i⁴ ≥ u²/N. Hence \|φ_t(y)\|² ≤ min(\|y\|², N/(8βt)) for every y and t > 0. Solutions exist globally. | |
| **F5 (oddness)** | f(−x) = −f(x), so φ_t(−y) = −φ_t(y). With symmetric additive noise, the law of x under −x₀ is the image of the law under x₀. | |
| **F6 (stochastic regularity)** | 𝓛\|x\|^{2p} ≤ c_p(1 + \|x\|^{2p}), because x·f ≤ 0. So every moment of 𝒮 is bounded on compact time intervals, and Dynkin's expansion holds to every finite order with a remainder of the next order. | |

From F5: m^𝒮(t; −a) = −m^𝒮(t; a).
From F6: m^𝒮(t; a) = Σ_{n≤4} c_n tⁿ/n! + O(t⁵).

## §1 Coefficient identities (general Q; evaluated at a·e₁)

- **Orders 0 and 1:** Dx₁ = 0, so Δc₀ = Δc₁ = 0.
- **Order 2:**
  - 𝓛²x₁ = Af₁ + Df₁, where Df₁ = T₁∂₁²f₁ = −24βT₁x₁. (Other ∂_i²f₁ vanish, because f₁ is linear in
    x₂.)
  - **Δc₂ = −24βT₁a**, so the coefficient of t² is **−12βT₁a**.
- **Order 3:**
  - 𝓛³x₁ − A³x₁ = DAf₁ + ADf₁ + D²f₁.
  - D²f₁ = T₁²∂₁⁴f₁ = 0.
  - ADf₁ = f·∇(−24βT₁x₁) = −24βT₁f₁, which at a·e₁ is 24βT₁a(K₁₁ + 4βa²).
  - DAf₁ = Σ_i T_i∂_i²(f·∇f₁), with f·∇f₁ = f₁·(−K₁₁ − 12βx₁²) + f₂·(−K₁₂).
    - **The i = 1 term.** Put u = f₁ and v = −K₁₁ − 12βx₁². At a·e₁: u = −K₁₁a − 4βa³,
      u′ = v = −K₁₁ − 12βa², u″ = v′ = −24βa, v″ = −24β. Then
      (uv)″ = u″v + 2u′v′ + uv″ = 24βa(4K₁₁ + 40βa²). The f₂ part is linear in x₁, so it contributes
      nothing.
    - **The i = 2 term.** ∂₂²(f₁v) = 0, and ∂₂²(−K₁₂f₂) = 24βK₁₂x₂ = 0 at x₂ = 0.
    - **The terms i ≥ 3** vanish, because f₂ is linear in x₃.
    - **So DAf₁ = 24βT₁a(4K₁₁ + 40βa²), with no T₂ dependence at a·e₁.**
  - **Δc₃ = 24βT₁a(44βa² + 5K₁₁)**, so the coefficient of t³ is **4βT₁a(44βa² + 5K₁₁)**.
- **Order 4:** Δc₄ is computed exactly by the script. Its sign and value are **not pre-registered**.
- **Linear-drift control (β = 0):** Aⁿx₁ and 𝓛ⁿx₁ coincide, because every ∂²f vanishes. So Δc_n ≡ 0
  (Theorem LD).
- **G(∞):** T₁ = 0 gives Δc₂ = 0.

## §2 The finite-moment M2 no-go (restated; S2-0 §4.2, verifier-confirmed)

- **Hypotheses:** ν is independent of a, with finite 7th moments, and matching holds for two
  distinct a.
- **Steps:**
  - O(t⁰) gives 𝔼ξ₁ = 0.
  - The O(t) difference, −12βa𝔼ξ₁² − 4β𝔼ξ₁³ − K₁₂𝔼ξ₂, is affine in a. This forces ξ₁ = 0 a.s. and
    𝔼ξ₂ = 0.
  - The O(t²) difference, K₁₂(4β𝔼ξ₂³ + K₂₃𝔼ξ₃), does not depend on a, whereas 𝒮 needs −24βT₁a.
- **Conclusion:** no such ν exists. ∎ (Subsumed by §3, which needs no moments.)

## §3 T-HT: HT-B, a moment-free no-go

**Theorem HT-B.** Let β > 0, and let the profile have T₁ > 0 (F, or GR(∞)). Suppose the frozen
preparation set A contains a pair a > a′ and a symmetric pair ±a with a ≠ 0. The frozen
A = {±1/1000, ±1, ±3} does.

Let ν be **any** law on ℝ²³, independent of the preparation, with 𝔼|ξ₁| < ∞. That is exactly the
charter's admissibility: the O-1 mean is defined at t = 0.

Then there is **no ε > 0** such that m^𝒟(t; a) := 𝔼[φ_t(a·e₁ + ξ)₁] = m^𝒮(t; a) for all a ∈ A and
all 0 ≤ t < ε.

**Well-posedness of m^𝒟 (no moments needed).**
- By F4, |φ_t(y)₁| ≤ √(N/(8βt)) for t > 0, so m^𝒟(t; a) is finite for every t > 0 and every ν.
- For t ≥ t₀ > 0, f₁(φ_t(y)) is bounded uniformly in y, again by F4. So m^𝒟 is differentiable on
  (0, ∞), with (m^𝒟)′(t) = 𝔼[f₁(φ_t(a·e₁ + ξ))], by dominated convergence.
- At t = 0, m^𝒟 = a + 𝔼ξ₁.

Suppose, for contradiction, that matching holds on [0, ε).

**Step A: matching forces ξ₁ = 0 a.s., with no moment assumption.**
- **Setting.** At t = 0, a + 𝔼ξ₁ = a, so 𝔼ξ₁ = 0. Fix a > a′ in A. Write X := φ_t(a·e₁ + ξ),
  X′ := φ_t(a′·e₁ + ξ), and g_j := X_j − X′_j.
- **Signs and bounds.**
  - By F2, g ≥ 0 componentwise.
  - By F3, |g| ≤ a − a′.
  - Put h_t := 4β(X₁³ − X′₁³) ≥ 0 (a monotone difference).
- **Rewriting the derivative identity.** Matching on (0, ε) gives, for t ∈ (0, ε),

  (m^𝒮)′(t; a) − (m^𝒮)′(t; a′) = 𝔼[f₁(X) − f₁(X′)] = −K₁₁𝔼g₁ − K₁₂𝔼g₂ − 𝔼h_t.

- **Limits as t → 0⁺.**
  - The left side tends to f₁(a·e₁) − f₁(a′·e₁) = −K₁₁(a − a′) − 4β(a³ − a′³), because m^𝒮 is C¹
    (F6).
  - 𝔼g₁ → a − a′ and 𝔼g₂ → 0, by dominated convergence (bounded by a − a′; pointwise continuity of
    φ_t at t = 0).
  - Hence **lim_{t→0⁺}𝔼h_t exists and equals 4β(a³ − a′³).**
- **Fatou.** h_t ≥ 0 and h_t → h₀ := 4β((a + ξ₁)³ − (a′ + ξ₁)³) pointwise. So

  𝔼h₀ ≤ liminf 𝔼h_t = 4β(a³ − a′³).

- **Evaluating 𝔼h₀.** h₀ = 4β(a − a′)[a² + aa′ + a′² + 3(a + a′)ξ₁ + 3ξ₁²] ≥ 0. With 𝔼ξ₁ = 0 this
  gives, in the extended reals, 𝔼h₀ = 4β(a³ − a′³) + 12β(a − a′)𝔼ξ₁².
- **Conclusion.** 12β(a − a′)𝔼ξ₁² ≤ 0. So **𝔼ξ₁² = 0 and ξ₁ = 0 a.s.** ∎(A)

**Step B: the symmetric pair (a, −a), a > 0, with ξ₁ = 0 a.s.**

*Definitions.*
- X^± := φ_t(±a·e₁ + ξ) and X^{±0} := φ_t(±a·e₁), the bath at rest.
- By F5, X^{−0} = −X^{+0}. Write p := X₁^{+0}.
- g := X⁺ − X⁻ (componentwise) and g⁰ := X^{+0} − X^{−0}. Note g⁰₁ = 2p.
- e := g₁ − g⁰₁ and δ^± := X₁^± − X₁^{±0}, so e = δ⁺ − δ⁻.
- Fix t₀ ∈ (0, 1]. All constants C below depend only on (a, β, K, N, t₀). **They do not depend on ξ.**

*Bounds that hold for every ξ, for 0 ≤ s ≤ t₀:*
- **(i)** |X_j^±(s)| ≤ √(N/(8βs)) (F4). Moreover |X₁^±(s)| ≤ |a| + ∫₀^s|X₂^±| ≤ |a| + √(Ns/(2β)).
  This is because ẋ₁ = −K₁₁x₁ + x₂ − 4βx₁³ satisfies sgn(x₁)·ẋ₁ ≤ |x₂|. Also |X₁^{±0}| ≤ |a|.
- **(ii)** |δ̇^±| ≤ C|δ^±| + |X₂^±| + |X₂^{±0}|, with |X₂^{±0}(u)| ≤ Cu. By Gronwall,
  **|δ^±(s)| ≤ C√s.**
- **(iii)** By F2 and F3: 0 ≤ g_j ≤ |g| ≤ 2a for every j.
- **(iv)** ġ₂ = −K₂₁g₁ − K₂₂g₂ − K₂₃g₃ − 4β(X₂⁺³ − X₂⁻³) ≤ g₁ + g₃ ≤ 4a. Here K₂₁ = K₂₃ = −1, and
  the dropped terms are ≤ 0 because g₂ ≥ 0. With g₂(0) = 0, this gives 0 ≤ g₂(s) ≤ 4as. The same
  bound holds for g⁰₂. So **|g₂ − g⁰₂| ≤ 4as.**
- **(v) The equation for e.**
  - Write q := X₁⁺² + X₁⁺X₁⁻ + X₁⁻². Then q⁰ = p², and **q − q⁰ = p·e + ρ**, where
    ρ := δ⁺² + δ⁺δ⁻ + δ⁻² ∈ [0, Cs].
  - Since ġ₁ = −K₁₁g₁ + g₂ − 4βq·g₁ (K₁₂ = −1), we get

    ė = −(K₁₁ + 4βp² + 4βp·g₁)e + (g₂ − g⁰₂) − 4βρ·g₁.

  - The coefficient of e is bounded, and the remaining terms are ≤ Cs.

*Lemma B1 (uniform).* |e(t, ξ)| ≤ Ct² for all ξ and t ∈ [0, t₀]. This follows by Gronwall from (v),
with e(0) = 0.

*Lemma B2 (pointwise).* For each fixed ξ, e(·, ξ) is C^∞ (polynomial ODE), and:
- e(0) = 0.
- ė(0) = 0, because g₂(0) = g⁰₂(0) = 0 and ρ(0) = 0.
- ë(0) = ġ₂(0) − ġ⁰₂(0) − 4βρ̇(0)g₁(0) = 2a − 2a − 0 = 0. Here ġ₂(0) = −K₂₁·2a (since
  g₂(0) = g₃(0) = 0), and ρ̇(0) = 0 because δ^±(0) = 0.
- Hence e(t, ξ) = O(t³), so **e/t² → 0.**

**Conclusion.**
- By dominated convergence (B1 gives the uniform bound; B2 gives pointwise convergence),
  𝔼e(t, ξ)/t² → 0. That is:

  **m^𝒟(t; a) − m^𝒟(t; −a) = g⁰₁(t) + o(t²),** for **every** ν with ξ₁ = 0.

- On the stochastic side, by F5, F6 and §1:

  m^𝒮(t; a) − m^𝒮(t; −a) = 2m^𝒮(t; a) = 2φ_t(a·e₁)₁ − 24βT₁a·t² + O(t³) = g⁰₁(t) − 24βT₁a·t² + O(t³).

- Matching would force −24βT₁a·t² + O(t³) = o(t²). **So βT₁a = 0, a contradiction.** ∎

**Scope and reading.**
- **T-HT closes by HT-B for profiles F and GR(∞).** It holds for **every** preparation-independent
  hidden law with a defined O-1 mean. No higher moment is assumed. Step A *derives* ξ₁ = 0, and
  Step B needs no moment of any bath component.
- **What the proof uses:**
  - the cooperativity, contraction and coming-down properties of the declared L0-1c drift (F2–F4);
  - its oddness (F5);
  - one ordered pair and one symmetric pair of frozen preparations.
- **G(∞) (T₁ = 0):** HT-B is not claimed. The leading discriminator vanishes there, and its
  higher-order Δc_n are reported only.
- **Mechanism, in words.**
  - Hidden initial uncertainty in the bath reaches the retained site only through a push of size
    O(√s), because F4 caps the bath amplitude.
  - For the ± pair it enters the retained difference only **quadratically** (ρ), and through the
    downstream difference g₂ − g⁰₂ = O(s).
  - Both effects are o(t²) after averaging, **whatever the tails.**
  - Primitive noise instead injects variance 2T₁t **directly at the retained site**, which the cubic
    curvature converts into an O(t²) drift.

## §4 Consequences for the frozen terminal (applied in the verdict after the script)

If the script's I-1 … I-5 pass:
1. The finite-moment M2 no-go is reproduced (§2, and its symbolic algebra in E-2).
2. **T-HT closes by HT-B** (§3).
3. **No arbitrary preparation-independent ν reproduces O-1 across the frozen preparations.**

⇒ **FULL-DISCRIMINATOR-CONFIRMED** (charter §5, item 3), for β > 0 and the T₁ > 0 profiles F and
GR(∞). It is subject to the §6 fence, and G(∞) is reported only.
