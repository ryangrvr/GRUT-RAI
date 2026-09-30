# S5-1 — ANALYTIC DERIVATION 01 (the single authorized execution, steps 1–5 of the frozen sequence)

- **Charter:** `S5_CONSERVATIVE_ORIGIN_01.md`, frozen at `d603db5`.
- **Authority:** `S5_OWNER_RULING_02.md`, with the S5-1-only v4 exception.
- **What this document is:**
  - It is the analytic execution.
  - It was written and committed **before** any numerical cross-check (§7 X-1…X-5) was run.
  - Symbolic re-verification of the displayed identities, and the non-adjudicating cross-checks,
    follow in `calc/s5_conservative_origin.py`.
- **Notation:**
  - ω_s := √K₁₁ = √2.3.
  - A₀ = [[0, 1], [−K₁₁, 0]].
  - For the retained site: C := cos(√K t), S := K^{−1/2}sin(√K t).

## §0 Common preliminaries

**P-1: the reduced map on C₀.** With the bath at rest (q₀ = q₁(0)e₁, p₀ = p₁(0)e₁), the exact modal
solution q(t) = Cq₀ + Sp₀, p(t) = −KSq₀ + Cp₀ (`L0_1G_CHARTER_01.md` §1) gives

  Φ(t) = [[φ, ψ], [φ′, φ]],  with φ := C₁₁ = e₁ᵀcos(√K t)e₁ and ψ := S₁₁,

using d/dt C = −KS. By the spectral theorem, with μ the spectral measure of K at e₁:

  φ(t) = ∫cos(√λ t)dμ(λ),  ψ(t) = ∫λ^{−1/2}sin(√λ t)dμ(λ),  ψ′ = φ.

**P-2: the reference operator.** T denotes the semi-infinite free Jacobi operator on ℓ²(ℕ):
(Tu)_n = u_{n−1} + u_{n+1}, with u₀ := 0.
- **Standard facts (proved in the literature and re-verified symbolically in the script):**
  - σ(T) = [−2, 2] is purely absolutely continuous;
  - T has no eigenvalues;
  - its spectral measure at e₁ is the semicircle ν(dx) = (1/2π)√(4 − x²)dx;
  - its Stieltjes function m(ζ) = ⟨e₁, (T − ζ)⁻¹e₁⟩ = (−ζ + √(ζ² − 4))/2 solves m² + ζm + 1 = 0.
- **Why T has no eigenvalues:** a formal eigenvector with u₀ = 0 is u_n = U_{n−1}(x/2) (Chebyshev),
  which is not in ℓ² for any real x.
- **The parent in these terms:**
  - K_∞ = 2.3·I − T, the N → ∞ member with g = 1.
  - The bath block of every member at N = ∞ is again 2.3·I − T, a copy of K_∞ on sites 2, 3, ….

## §1 Step 1: finite-N theorem

**Theorem 1 (finite N, 0 < g ≤ 1).** For every finite member (N ≥ 2), including the K(g) family:

- **(a) Positive definiteness.**
  - Gershgorin gives λ_min(K_N(g)) ≥ min_i(K_ii − Σ_{j≠i}|K_ij|) = min(2.3 − g, 2.3 − g − 1, 0.3,
    1.3 − 1) = 0.3 > 0. The rows are, in order: row 1; row 2; bulk rows; row N.
  - K_N(g) is a Jacobi matrix with non-zero off-diagonals, so its spectrum is **simple** and every
    eigenvector has v_k(1) ≠ 0. (If v(1) = 0, the three-term recursion forces v ≡ 0.)
  - Hence φ_N(t) = Σ_{k=1}^{N} w_k cos(ω_k t), with w_k = v_k(1)² > 0 and N ≥ 2 distinct
    ω_k = √λ_k > 0.
- **(b) No decay, almost periodic.**
  - Φ_N is almost periodic, and (1/T)∫₀ᵀφ_N² dt → ½Σw_k² > 0.
  - So Φ_N(t) does not tend to 0. **No strictly dissipative semigroup e^{−Mt} (Re σ(M) > 0), which
    decays to 0, equals Φ_N.**
- **(c) No exact semigroup of any kind on R1.**
  - Suppose Φ_N(t + s) = Φ_N(t)Φ_N(s). Φ_N is C^∞, so Φ_N(t) = e^{Φ_N′(0)t}.
  - From P-1: Φ_N′(0) = [[φ′(0), ψ′(0)], [φ″(0), φ′(0)]] = [[0, 1], [−K₁₁, 0]] = A₀. This uses
    φ′(0) = 0, ψ′(0) = φ(0) = 1, and φ″(0) = −∫λdμ = −(K)₁₁ = −K₁₁.
  - Then φ_N = cos(ω_s t), so μ = δ_{K₁₁}, which contradicts N ≥ 2 atoms of positive weight.
  - **Conclusion:** the retained map is not a semigroup. The only exact first-order generator of the
    parent is the full conservative A (spectrum ±iω_k), which is G-W in first-order form.
- **(d) R2 short-time obstruction.**
  - φ_N(0) = 1, φ_N′(0) = −∫√λ·sin(0)dμ = 0, and φ_N″(0) = −K₁₁ = −2.3.
  - A nontrivial scalar law e^{−γt} with γ > 0 has derivative −γ ≠ 0 at t = 0. **Exact equality is
    impossible.**
  - Complete monotonicity requires f″(0) ≥ 0, so **φ_N is not CM.** This holds for every N and every
    g, because φ″(0) = −K₁₁ does not depend on g.

∎ Consumes O-6 I-1 (recurrence) and T_rec.

## §2 Step 2: infinite-N spectral theorem (g = 1, the L-N member)

**Theorem 2.**
- **(a) The operator.** K_∞ = 2.3 − T is bounded, self-adjoint and positive:
  σ(K_∞) = 2.3 − [−2, 2] = [0.3, 4.3].
  - Its spectral measure at e₁ is purely absolutely continuous:
    μ(dλ) = (1/2π)√(4 − (2.3 − λ)²)dλ on [0.3, 4.3].
  - **Bound-state audit: none**, because T has no eigenvalues.
  - Finite sections converge strongly (K_N → K_∞ strongly on finitely supported vectors, uniformly
    bounded). So Φ_N(t) → Φ_∞(t) pointwise, uniformly on compact t-sets.
- **(b) Laplace structure (branch cut, not poles).**
  - The retained Stieltjes function is F(z) := ⟨e₁, (K_∞ − z)⁻¹e₁⟩ = −m(2.3 − z)
    = (w − √(w² − 4))/2, with w := 2.3 − z.
  - It satisfies **F² − wF + 1 = 0.** The discriminant w² − 4 is not the square of a polynomial, so
    **F is not rational**. It has square-root branch points at z = 0.3 and z = 4.3.
  - The Laplace transform of φ_∞ is ℒ[φ_∞](s) = ∫s/(s² + λ)dμ = s·F(−s²). This is not rational, with
    branch points at s = ±i√0.3 and ±i√4.3.
  - Every entry of e^{−Mt} (finite M) is an exponential polynomial, whose Laplace transform is
    rational. **Hence φ_∞ is not a matrix element of any finite-dimensional semigroup.**
- **(c) No semigroup on R1 at N = ∞.** The argument of Theorem 1(c) applies verbatim: Φ_∞′(0) = A₀,
  so a semigroup would force μ = δ_{2.3}, which contradicts absolute continuity.
- **(d) Decay and long-time class.**
  - With ω = √λ, φ_∞(t) = ∫_{ω₋}^{ω₊}cos(ωt)ρ̃(ω)dω, where
    ρ̃(ω) = (ω/π)√((ω² − 0.3)(4.3 − ω²)), ω₋ = √0.3 and ω₊ = √4.3.
  - Riemann–Lebesgue gives Φ_∞(t) → 0: **effective dissipation emerges.**
  - At the endpoints, ρ̃ ≈ c_∓·|ω − ω_∓|^{1/2}, with c₋ = (ω₋/π)√(8ω₋) and c₊ = (ω₊/π)√(8ω₊).
  - The standard endpoint (Erdélyi) asymptotics, using
    ∫_a e^{iωt}(ω − a)^{1/2}… ~ Γ(3/2)e^{iat}e^{i3π/4}t^{−3/2} and the upper-end analogue with
    e^{−i3π/4}, give

    **φ_∞(t) = Γ(3/2)·t^{−3/2}·[c₋cos(ω₋t + 3π/4) + c₊cos(ω₊t − 3π/4)] + O(t^{−5/2}).**

  - This is **algebraic and sign-alternating**, so it is neither exponential-grade nor CM. It is
    consistent with O-6 D-1, since bilinear currents are products of two t^{−3/2} factors, giving
    t^{−3}. ψ_∞ and φ_∞′ share the t^{−3/2} class.
- **Scope fence.** This concerns the declared local parent only. Abstract unitary dilations of
  contraction semigroups (Sz.-Nagy) are outside it and are not addressed.

∎

## §3 Step 3: kernel-class theorem

**K-L0 on the retained response φ** (the primary object):
- **Finite N:** φ_N is almost periodic, pole-only with purely imaginary poles, and non-decaying.
  φ_N″(0) = −K₁₁ < 0, so it is **not CM**.
- **N = ∞:** φ_∞ has a branch cut, a t^{−3/2} sign-alternating tail, and φ_∞″(0) = −2.3 < 0. It is
  **not CM and not pole-only.**
- **K(g) family:** φ_g″(0) = −K₁₁ for every g, so it is **not CM.**

⇒ **K-L0 FAILS** at every declared N, at N = ∞, and for every member of the admitted family. The
failure shows in the local short-time structure and, at N = ∞, also in the long-time branch
structure.

**Memory diagnostic** (categorically separate; never identified with k_D):
- **Derivation.** For sites i ≥ 2, q̈_i = −(K_BB q_B)_i + gδ_{i2}q₁. With the bath at rest,
  q_B(t) = g∫₀ᵗS_B(t − s)f q₁(s)ds, where f = e₂ and S_B = K_BB^{−1/2}sin(√K_BB t).
- **Self-energy (sine) form:** q̈₁ = −K₁₁q₁ + g²∫₀ᵗΣ(t − s)q₁(s)ds, with Σ(t) = fᵀS_B(t)f.
- **Friction form.** Define Γ_fric(t) := g²fᵀK_BB⁻¹cos(√K_BB t)f. Then Γ_fric′ = −g²Σ, and
  integrating by parts gives the exact GLE

  **q̈₁ = −(K₁₁ − Γ_fric(0))q₁ − ∫₀ᵗΓ_fric(t − s)q̇₁(s)ds − Γ_fric(t)q₁(0),**

  with Γ_fric(0) = g²(K_BB⁻¹)₂₂.
- **Local CM test (exact normalization):** Γ_fric″(0) = −g²fᵀK_BB⁻¹K_BB f = **−g² < 0**, so it is
  **not CM**.
- **At N = ∞:** Γ_fric(t) = g²∫λ⁻¹cos(√λ t)dμ(λ), over the same a.c. measure. It is an oscillatory
  memory kernel with a branch cut and t^{−3/2} tails.
- **Reading.** The friction is never white: Γ_fric ∝ δ(t) is impossible, because the band is bounded
  and the density is smooth. This **explains** why the retained response is non-Markovian at every
  fixed g.

∎

## §4 Step 4: weak-coupling theorem (L-vH; the admitted K(g) family; conditional)

**(a) Validity of the family.**
- The family is K(g) = 2.3·I − T_g, where T_g is T with its first off-diagonal entry replaced by g
  (0 < g ≤ 1).
- By the Schur test, ‖T_g‖ ≤ max row-sum = max(g, g + 1, 2) = 2, so **K(g) ≥ 0.3·I > 0 for every
  0 < g ≤ 1.** The finite members are covered by Theorem 1(a).
- K₁₁ = 2.3 and K_BB = 2.3 − T are fixed, as frozen.

**(b) Retained resolvent (Schur complement):**

  F_g(z) = ⟨e₁, (K(g) − z)⁻¹e₁⟩ = 1/(2.3 − z − g²F(z)),

where F is the §2 function; the bath block is a copy of K_∞. Check at g = 1: w − F = 1/F, so
F₁ = F. ✓

**(c) Bound-state audit for the whole family.**
- Real eigenvalues outside [0.3, 4.3] are zeros of D_g = w − g²F with |w| > 2.
- Write w = y + 1/y with |y| > 1. Then F = 1/y, and D_g = y + (1 − g²)/y = 0 ⟺ y² = g² − 1 ≤ 0.
  There is no solution with |y| > 1.
- **So there are no bound states for 0 < g ≤ 1.** (They would appear only for g² > 2.)
- μ_g is therefore purely a.c. on [0.3, 4.3], with mass 1.

**(d) Exact spectral density.**
- Parametrize the band by w = 2.3 − λ = 2cos θ, θ ∈ (0, π). Then F(λ + i0) = e^{iθ} (the Herglotz
  branch, Im > 0), and

  **ρ_g(λ) = (1/π)·Im F_g(λ + i0) = (1/π)·g²·sin θ / [(2 − g²)²cos²θ + g⁴sin²θ].**

- **Check at g = 1:** ρ₁ = sin θ/π = (1/2π)√(4 − w²). ✓
- ρ_g is **symmetric about θ = π/2, i.e. about λ = K₁₁ = 2.3.** The isolated system frequency squared
  sits exactly at **band centre**, so ω_s = √2.3 ∈ (ω₋, ω₊).
- There is **no level shift at any g**: the resonance centre is exactly λ = 2.3.
- At every fixed g > 0, ρ_g has √-edges, because the denominator is (2 − g²)² ≠ 0 at θ = 0, π. So
  **every fixed-g member keeps the branch cut and the t^{−3/2} tails.** It is non-Markovian at fixed
  g, like §2.

**(e) The van Hove limit, proved via Scheffé.**
- In the ω-variable, ρ̃_g(ω) := 2ωρ_g(ω²) on [ω₋, ω₊], and 0 outside.
- Put ω = ω_s + g²x. Then 2.3 − λ = −2ω_s g²x − g⁴x², so cos θ = −ω_s g²x − g⁴x²/2 and sin θ → 1.
- Pointwise in x, as g → 0:

  g²·ρ̃_g(ω_s + g²x) → (2ω_s/π)·1/(4ω_s²x² + 1) = (1/π)·κ/(x² + κ²),  **κ := 1/(2ω_s).**

- Both sides are probability densities in x. The left side has mass 1 by (c); the right side is
  Cauchy.
- By **Scheffé's lemma**, the convergence is in L¹. Equivalently, with ℓ_g the Cauchy density of
  centre ω_s and half-width κg²,

  **‖ρ̃_g − ℓ_g‖_{L¹(ℝ)} → 0.**

  In particular ρ̃_g → δ_{ω_s} weakly.
- **Golden-rule reading of the rate (derived, not inserted):** κg² = πg²ρ_B(λ_s)/(2ω_s). Here
  ρ_B(λ_s) = 1/π is the bath spectral density at λ_s = 2.3, the semicircle value at the centre.

**(f) Uniform approximation in the physical variables.**
- Let E_g(t) := e^{−κg²t}[[cos ω_s t, sin(ω_s t)/ω_s], [−ω_s sin ω_s t, cos ω_s t]] = e^{(A₀ − κg²I)t}.
  This holds because [A₀, I] = 0 and ∫_ℝ e^{iωt}ℓ_g dω = e^{iω_s t − κg²|t|} (the Cauchy
  characteristic function).
- For each entry, with weights ω^j (j ∈ {0, ±1}) continuous and bounded on the band:

  |∫cos or sin(ωt)·ω^j·ρ̃_g − ω_s^j∫cos or sin(ωt)·ℓ_g| ≤ ∫|ω^j − ω_s^j|ρ̃_g dω + ω_s^j‖ρ̃_g − ℓ_g‖₁.

  - The first term tends to 0 by weak convergence to δ_{ω_s}.
  - The second tends to 0 by (e).
  - For the sine entries, the odd extension of ℓ_g to (0, ∞) differs from ℓ_g by the Cauchy mass
    on ω < 0, which is O(κg²/ω_s) → 0.
- **Hence, uniformly in t ≥ 0:**

  **sup_{t≥0} ‖Φ_g(t) − e^{(A₀ − κg²I)t}‖ → 0 as g → 0.**

**(g) The frozen interaction-picture statement.**
- In the coordinates (q₁, p₁/ω_s), e^{−A₀t} is an orthogonal rotation, so it has norm 1.
- Therefore Ψ_g(τ) = e^{−A₀τ/g²}Φ_g(τ/g²) = e^{−κτ}I + O(o(1)), and

  **Ψ_g(τ) → e^{Bτ}, B = −κI,**

  **uniformly on τ ≥ 0**, which is stronger than the frozen compact-uniform requirement. B is derived
  from the parent spectral measure.

**(h) Physical reconstruction (ruling S5-02 §1).**
- **The effective generator in the physical variables (q₁, p₁)** is A_eff(g) = A₀ + g²B = A₀ − κg²I.
  - It is time-homogeneous and closed on R1.
  - Its spectrum is σ = {−κg² ± iω_s}, so it is **strictly dissipative** (Re σ = −κg² < 0).
  - Restartability holds in the limit: sup_{t,s}‖Φ_g(t + s) − Φ_g(t)Φ_g(s)‖ → 0, from (f) and
    boundedness.
  - Equivalently, it is the **damped oscillator** q̈ + 2κg²q̇ + (ω_s² + κ²g⁴)q = 0. It is
    underdamped for every admitted g (κg² ≤ 0.33 < ω_s ≈ 1.52).
- **M-1 (PHYSICAL MARKOV): YES**, as a controlled limit with vanishing uniform error and a derived
  rate. This is **conditional on the weak-coupling deformation.**
- **M-2 (G-D-PROPER): NO.**
  - The spectrum is complex (±iω_s), not real.
  - The scalar response e^{−κg²t}cos(ω_s t) is **not CM.**
  - There is **no autonomous first-order law for q₁**, because the effective generator couples q₁
    and p₁ through A₀.
  - **R2 closure fails:** there is no slaving relation for p₁. Slaving would need a damping scale
    ≳ ω_s, but damping is O(g²) → 0 in the only admitted limit.
- **The free oscillation is not discarded:** A₀ remains in A_eff and fixes the class.

∎

## §5 Step 5: no-insertion audit (NI)

| Step | Friction coefficient | Noise | Markov assumption | Reservoir / Lindblad | μ | Exponential ansatz | K change |
|---|---|---|---|---|---|---|---|
| §1 | none | none | none | none | none | none | none |
| §2 | none | none | none | none | none | none | none (N → ∞, admitted) |
| §3 | none. Γ_fric is **derived** by eliminating the bath. | none | none | none | none | none | none |
| §4 | none. κ is **derived** from ρ_g (golden-rule form). | none | none. The Markov form is a **theorem** (Scheffé L¹ convergence of the exact density), not an assumption. | none | none | none. The exponential **arises** as the Cauchy characteristic function of the limiting spectral shape. | only g (admitted L-vH) |

**The NI audit passes.**

## §6 Consequences for the frozen terminal (charter §8; applied in the verdict)

1. **UNFORMULABLE:** no. Every object is defined.
2. **EXACT-GENERATOR-DERIVED:** no. Theorems 1 and 2 give no exact semigroup at finite N or at
   N = ∞, and K-L0 fails.
3. **MARKOV-LIMIT-DERIVED (M-2):** no, by §4(h).
4. **MARKOV-LIMIT-OTHER-CLASS:** **yes.**
   - L-vH is admitted.
   - A controlled, time-homogeneous, strictly dissipative physical-variable generator is derived:
     A₀ − κg²I, with κ = 1/(2√2.3).
   - Its type is an underdamped oscillator, not first-order CM/real-spectrum G-D.

**Sub-findings reported with it:**
- **L-N (native, g = 1):** the parent yields **non-Markovian dissipation only** (branch cut,
  t^{−3/2}).
- **K-L0:** fails everywhere.
- **Γ_fric:** oscillatory, never white.
- **Missing ingredients for M-2 (indicated, not established as necessary):**
  - an overdamped/slaving scale (L-OD) for a first-order, real-spectrum law;
  - a wide-band limit (L-WB) for white friction.
