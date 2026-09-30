# S6-1 — ANALYTIC THEOREM BLOCK 01 (LS-0 … LS-5)

**Status: VERIFIED.**
- An independent adversarial verification passed after corrections VC-1 and VC-2; see the verification record at
  the end.
- The draft was committed at `303d3f3`/`303a216`.
- This verified version is committed **before** the certification script (charter
  `S6_1_COARSEGRAINED_ARROW_CHARTER_01.md` §2 and §5.1). The charter was frozen at `fbd15c8`.

**Authority:** `S6_OWNER_RULING_01.md` §9.

**Conventions:**
- Units: g = 1 and K₁₁ = 2.3.
- The objects are the confirmed O-6 record objects (ruling §2).
- **Primary object:** N = ∞.
- **J** is the bath self-energy flux (ruling A-3).

## LS-0 Spectral representation

**0.1 The operator.** K_∞ = 2.3·I − T on ℓ²(ℕ), where T is the half-line adjacency (T_{i,i+1} = T_{i+1,i} = 1).
- K_∞ is bounded and self-adjoint, with spectrum [0.3, 4.3].
- This is the strong limit of the finite sections K_N used by S5 (`S5_CONSERVATIVE_ORIGIN_DERIVATION_01.md:36-37,
  73-79`; L-N admitted, `S5_CONSERVATIVE_ORIGIN_01.md:50`). The last-site modification (1.3) moves to infinity.

**0.2 The spectral map.** The map e_n ↦ U_{n−1}(x/2), where U is the Chebyshev polynomial of the second kind, is
unitary from ℓ²(ℕ) onto L²(ρ dx). Here ρ(x) = (1/2π)√(4 − x²) on [−2, 2].
- Under this map, T becomes multiplication by x, and K_∞ becomes multiplication by λ = 2.3 − x.
- The e₁-spectral measure of K_∞ is therefore

  > dμ(λ) = (1/2π)√(4 − (λ − 2.3)²) dλ on [0.3, 4.3],

  which is **purely absolutely continuous**, with a bounded continuous density and no atoms. This is consistent
  with S5's "no bound state" (`S5_…_DERIVATION_01.md:74-77`; accepted `S5_OWNER_RULING_03.md:33-36`).
- **Matrix elements:** ⟨e_i, h(K)e₁⟩ = ∫ h(λ) w_i(λ) dμ, with w₁ = 1 and w₂ = U₁(x/2) = x = 2.3 − λ.
- **Angle parametrization:** with λ = 2.3 − 2cosθ, dμ = (2/π) sin²θ dθ on [0, π], and the total mass is 1.

**0.3 Families.** For k ∈ ℤ and w ∈ {w₁, w₂}:

> I^c_{k,w}(t) = ∫ w λ^{k/2} cos(√λ t) dμ,  I^s_{k,w}(t) = ∫ w λ^{k/2} sin(√λ t) dμ.

- **Derivatives:** d/dt I^c_{k,w} = −I^s_{k+1,w} and d/dt I^s_{k,w} = I^c_{k+1,w}.
- **Integrability:** the weights w λ^{k/2} are continuous on [0.3, 4.3], because λ ≥ 0.3 > 0. They are therefore
  bounded, so the integrands lie in L¹(μ).

**Named families.**

| Name | Family (w₁ / w₂) |
|---|---|
| c0 / c0₂ | I^c_{0,·} |
| cm / cm₂ | I^c_{−2,·} |
| sm / sm₂ | I^s_{−1,·} |
| sp / sp₂ | I^s_{1,·} |

**0.4 The constant r.** r := (K_∞⁻¹)₁₁ = ∫λ⁻¹dμ = m(2.3), where m(z) = ∫ρ(x)dx/(z − x) = (z − √(z² − 4))/2 for z > 2
(the branch with m(z) → 0 as z → ∞). Hence

> **r = (2.3 − √1.29)/2 ≈ 0.5821**, and r² − 2.3r + 1 = 0.

Also (K⁻¹)₁₂ = ∫(2.3 − λ)λ⁻¹dμ = 2.3r − 1 = r².

**0.5 Dynamics.**
- **Equations of motion:** q̈ = −Kq, i.e. ż = Az with A = [[0, I], [−K, 0]].
- **Propagator:** e^{At} = [[C, S], [−KS, C]], where C = cos(√K t) and S = K^{−1/2} sin(√K t). These are bounded,
  because K ≥ 0.3.
- **Covariance evolution:** a Gaussian (quasi-free) state with covariance Σ evolves as Σ(t) = e^{At}Σe^{Aᵀt}.

## LS-1 Return to equilibrium

**1.1 Gibbs invariance.** Take Σ_G = T_b·diag(K⁻¹, I). Then AΣ_G = T_b[[0, I], [−I, 0]] and
Σ_GAᵀ = T_b[[0, −I], [I, 0]], so AΣ_G + Σ_GAᵀ = 0. Hence e^{At}Σ_Ge^{Aᵀt} = Σ_G for all t.

**1.2 A finite-rank perturbation.**

*Setup.* Split K by site 1 and the bath {2, 3, …}:
- K = [[2.3, −e₁ᵀ], [−e₁, K_BB]], where K_BB ≅ K_∞ (the bath half-line is the same operator).
- Set v = K_BB⁻¹e₁ and s = 2.3 − (K_BB⁻¹)₁₁ = 2.3 − r.

*The Schur complement.*
- K⁻¹ = (0 ⊕ K_BB⁻¹) + s·u uᵀ, with u := K⁻¹e₁ = s⁻¹[1; v].
- Since (K⁻¹)₁₁ = 1/s = r, we have s = 1/r. This is consistent with r = 1/(2.3 − r).

*Declared initial covariance.* Σ₀ = diag(Q₀, P₀), with:
- Q₀ = (T_s/2.3)e₁e₁ᵀ ⊕ T_bK_BB⁻¹;
- P₀ = T_s e₁e₁ᵀ + T_b(I − e₁e₁ᵀ).

*The deviation.* Therefore Σ₀ = Σ_G + Δ₀, where Δ₀ = diag(Δ_Q, Δ_P) with:
- Δ_Q = (T_s/2.3) e₁e₁ᵀ − (T_b/r) u uᵀ;
- Δ_P = (T_s − T_b) e₁e₁ᵀ.

Δ₀ has **rank ≤ 3**, on the directions (e₁, 0), (u, 0) and (0, e₁).

**1.3 Exact deviation.** The deviation evolves as Σ(t) = Σ_G + e^{At}Δ₀e^{Aᵀt}. Using ⟨q_iq_j⟩ = (CΔ_QC + SΔ_PS)_{ij},
⟨p_ip_j⟩ = (KSΔ_QSK + CΔ_PC)_{ij} and ⟨p_iq_j⟩ = (−KSΔ_QC + CΔ_PS)_{ij}, with LS-0 matrix elements, the deviations are:

| Deviation | Expression |
|---|---|
| ΔQ₁₁ | (T_s/2.3)·c0² − (T_b/r)·cm² + (T_s − T_b)·sm² |
| ΔP₁₁ | (T_s/2.3)·sp² − (T_b/r)·sm² + (T_s − T_b)·c0² |
| ΔC₁₁ := Δ⟨q₁p₁⟩ | −(T_s/2.3)·sp·c0 + (T_b/r)·sm·cm + (T_s − T_b)·c0·sm |
| ΔQ₁₂ | (T_s/2.3)·c0·c0₂ − (T_b/r)·cm·cm₂ + (T_s − T_b)·sm·sm₂ |
| J = ⟨p₂q₁⟩ | −(T_s/2.3)·sp₂·c0 + (T_b/r)·sm₂·cm + (T_s − T_b)·c0₂·sm |

The Gibbs part of J is 0. This uses (KSu)_i = (Se₁)_i = sm_i, (Cu)_i = cm_i and (KSe₁)_i = sp_i.

**Checks at t = 0.** Here c0 = 1, cm = r, cm₂ = r², c0₂ = 0 and every sine is 0. Hence:
- Q₁₁ = T_br + T_s/2.3 − T_br = T_s/2.3;
- P₁₁ = T_s;
- Q₁₂ = T_br² − T_br² = 0;
- C₁₁ = 0;
- J = 0.

These are the declared values.

**1.4 The limit.**

*Theorem LS-1.* S₁(t) = [[Q₁₁, C₁₁], [C₁₁, P₁₁]](t) → S_ref = T_b·diag(r, 1), and Q₁₂(t) → T_br², as t → ∞.

*Proof.*
- Each family is I(t) = ∫ G(λ) e^{±i√λ t} dμ, with G continuous on [0.3, 4.3].
- Substituting ω = √λ gives I(t) = ∫ g(ω) e^{±iωt} dω, with g(ω) = G(ω²) ρ̃(ω²)·2ω. Here ρ̃ is the μ-density,
  continuous and bounded, supported on [√0.3, √4.3].
- So **g ∈ L¹(ℝ)**. This rests on μ being absolutely continuous (LS-0.2). A point mass (bound state) would give a
  non-decaying term.
- By the Riemann–Lebesgue lemma, I(t) → 0.
- Every deviation entry is a finite sum of products of two such I's with bounded coefficients, so every deviation
  tends to 0.
- The Gibbs part is invariant (1.1). ∎

## LS-2 Closed forms

**2.1 Local energy identity.** Take E₁ = ½(2.3q₁² + p₁²) and E_int = −q₁q₂. With ṗ₁ = −2.3q₁ + q₂:
- dE₁/dt = p₁q₂;
- dE_int/dt = −(p₁q₂ + q₁p₂).

Hence **d(E₁ + E_int)/dt = −q₁p₂**, and in expectation this equals −J. Since ⟨E_int⟩(0) = 0:

> X_J(T) := ∫₀ᵀ J = ⟨E₁⟩(0) − ⟨E₁⟩(T) − ⟨E_int⟩(T)
> = 1.15(Q₁₁(0) − Q₁₁(T)) + ½(P₁₁(0) − P₁₁(T)) + Q₁₂(T).

**2.2 The limits, via LS-1.**
- X_J(∞) = 1.15(T_s/2.3 − T_br) + ½(T_s − T_b) + T_br² = T_s − ½T_b(2.3r + 1) + T_br².
- Using 2.3r = 1 + r²:

> **X_J(∞) = (T_s − T_b) + ½T_b r²**  (record convention, i.e. bath self-energy gained).

- **Forward orientation:** X_f = +X_J on L1 and −X_J on L2.
- **Equal-temperature offset:** ½T_br² ≈ 0.1694·T_b, reported with every J result (A-3).

**Deviation form.** X_J(T) − X_J(∞) = −1.15·ΔQ₁₁(T) − ½·ΔP₁₁(T) + ΔQ₁₂(T).

**2.3 Entropy.** With R = S_ref:

> D(S₁) = ½[Q₁₁/(T_br) + P₁₁/T_b − 2 − ln((Q₁₁P₁₁ − C₁₁²)/(T_b² r))].

- D is continuous at S₁ = R, where it equals 0. So by LS-1, D(∞) = 0 and **X_σ(∞) = D(0)**.
- The initial value is D(0) = ½[T_s/(2.3T_br) + T_s/T_b − 2 − ln(T_s²/(2.3T_b²r))].
- **D(0) > 0**, because S₁(0) ≠ R: P₁₁ = T_s ≠ T_b at every member, and KL > 0 for distinct Gaussians.

**2.4 Initial derivatives** (by direct differentiation of moments):
- **Value and slope at 0:** X_f(0) = 0, and X_f′(0) = f(0) = 0. For J this is ⟨p₂q₁⟩(0) = 0. For σ it is −Ḋ(0) = 0,
  because Ṡ₁(0) = 0:
  - d⟨q₁²⟩ = 2⟨q₁p₁⟩ = 0;
  - d⟨p₁²⟩ = −2⟨p₁(Kq)₁⟩ = 0;
  - d⟨q₁p₁⟩ = ⟨p₁²⟩ − ⟨q₁(Kq)₁⟩ = T_s − 2.3·T_s/2.3 = 0.
- **J′(0):** J′ = ⟨ṗ₂q₁⟩ + ⟨p₂p₁⟩ = ⟨(q₁ − 2.3q₂ + q₃)q₁⟩ = T_s/2.3 at t = 0. So X_J''(0) = T_s/2.3.
- **D''(0):** at t = 0 all first derivatives of S₁ vanish, and ∂D/∂C₁₁ = 0 at C₁₁ = 0. Hence
  D''(0) = ∂_QD·Q₁₁''(0) + ∂_PD·P₁₁''(0), where:
  - Q₁₁''(0) = 2⟨p₁²⟩ − 2⟨q₁(Kq)₁⟩ = 0;
  - P₁₁''(0) = 2⟨(Kq)₁²⟩ − 2⟨p₁(Kp)₁⟩ = 2T_b(K_BB⁻¹)₁₁ = 2T_br;
  - ∂_PD = ½(1/T_b − 1/T_s).

  Therefore D''(0) = r(1 − T_b/T_s).

**The oriented second derivatives** (L1 means T_s > T_b; L2 means T_s < T_b):

| Pair | X_f''(0) | Role |
|---|---|---|
| J, L1 | +T_s/2.3 > 0 | target |
| J, L2 | −T_s/2.3 < 0 | control |
| σ, L2 | r(T_b/T_s − 1) > 0 | target |
| σ, L1 | r(T_b/T_s − 1) < 0 | control |

## LS-3 Entropy tail (A-5)

**3.1 Band-edge asymptotics.**

*Definition.* I^e_{k,w}(t) = ∫₀^π H(θ)e^{itω(θ)}dθ, where H = (2/π)wλ^{k/2}sin²θ and ω = √(2.3 − 2cosθ).

*The phase.* ω′(θ) = sinθ/ω vanishes only at θ = 0 and θ = π.
- Near θ = 0: ω = ω₋ + θ²/(2ω₋) + O(θ⁴), with ω₋ = √0.3.
- Near θ = π: ω = ω₊ − φ²/(2ω₊) + O(φ⁴), with φ = π − θ and ω₊ = √4.3.

*The amplitude.* H vanishes to second order at both ends, and H/θ² and H/φ² are smooth.

*Endpoint stationary phase.* Using ∫₀^∞ x²e^{±iαx²}dx = (√π/4)α^{−3/2}e^{±3πi/4}:

> **I^e_{k,w}(t) = t^{−3/2}[A₋e^{i(ω₋t + 3π/4)} + A₊e^{i(ω₊t − 3π/4)}] + O(t^{−5/2})**,
> with A_± = (1/(2√π))·w(λ_±) λ_±^{k/2}(2ω_±)^{3/2}.

The lower edge carries +3π/4 and the upper edge −3π/4 (verification correction VC-1).

**Consistency with S5.** For k = 0, w = 1, A₋ = Γ(3/2)c₋, which is S5's retained-response tail for
⟨e₁, cos(√K t)e₁⟩ = c0.

Here λ₋ = 0.3, λ₊ = 4.3, w₂(λ₋) = 2 and w₂(λ₊) = −2. Take I^c = Re I^e and I^s = Im I^e.

*Derivatives.* The derivative of a family is again a family (LS-0.3). So derivatives obey the same expansion,
with the remainder O(t^{−5/2}).

**3.2 The quadratic expansion.**
- Let E = R^{−1/2}(S₁ − R)R^{−1/2}, and let μ_i be the eigenvalues of I + E. Then D = ½Σ(μ_i − 1 − ln μ_i).
- Since μ − 1 − ln μ = ½(μ − 1)² + O((μ − 1)³), we get **D = ¼‖E‖_F² + O(‖E‖³)**.
- By 1.3 and 3.1, E = t⁻³M(t) + O(t⁻⁴), where M is a quasi-periodic, real-symmetric, trig-polynomial matrix. Its
  frequencies lie in {0, 2ω₋, 2ω₊, ω₊ ± ω₋}.
- Hence:

> **D(t) = t⁻⁶P(t) + O(t⁻⁷)**, with P := ¼‖M‖_F² ≥ 0.

**3.3 The derivative.**
- Ḋ = ½tr[(R⁻¹ − S₁⁻¹)Ṡ₁] = ½tr[(E − E² + …)Ė], where Ė = R^{−1/2}Ṡ₁R^{−1/2} = d/dt(t⁻³M) + O(t⁻⁴) (by 3.1).
- Hence ½tr(EĖ) = t⁻⁶·½tr(MM′) + O(t⁻⁷). With O(‖E‖²‖Ė‖) = O(t⁻⁹), this gives:

> **Ḋ(t) = t⁻⁶P′(t) + O(t⁻⁷)**.

**3.4 Non-degeneracy and sign reversal.**
- P is almost periodic, so P′ has mean zero.
- **If P is not constant**, then P′ ≢ 0. On unbounded sets of t it takes values ≥ η > 0, and on other unbounded
  sets values ≤ −η.
- Therefore **Ḋ changes sign on an unbounded set of t, with magnitude of order t⁻⁶.**

**Non-degeneracy (analytic; verification correction VC-2, replacing an invalid argument in the draft).**
- ω₊/ω₋ = √(43/3) is irrational, so the frequencies mω₋ + nω₊ (m, n ∈ ℤ) are pairwise distinct.
- P is a trigonometric polynomial in ψ₋ = ω₋t + 3π/4 and ψ₊ = ω₊t − 3π/4.
- Its coefficient of e^{4iψ₋} depends only on the lower-edge amplitudes. It equals

  > p₄,₀ = [(21414449 + 1879537√129)T_b² + (7929480 + 687240√129)T_bT_s + (752400 + 61200√129)T_s²] / (16π²·3174000·T_b²).

  Every coefficient is positive, so **p₄,₀ > 0 for all T_s, T_b > 0.**
- It was derived symbolically for generic T_s and T_b by the independent verifier. The verifier cross-checked it
  by a 2-D FFT at the non-member pairs (3,2), (0.3,0.7), (5,0.2) and (0.01,5), agreeing to machine precision.
- **Hence P is non-constant for every positive temperature pair, and the sign reversal of Ḋ holds unconditionally
  on the declared family.**
- The charter P-8 two-point evaluation is kept as a cross-check only.

**3.5 Answer on the O-6 wording.**
- The accepted D-1 text reads "t⁻³ sign-alternating ripples in both heat current and entropy derivative"
  (`L0_1G_OWNER_RULING_02.md:36-38`; `PREFREEZE:31`).
- **For J**, it is consistent: J = O(t⁻³) is proved as an upper bound, since J is bilinear. The non-vanishing of
  J's t⁻³ coefficient is not examined here.
- **For Ḋ**, it is a **valid upper bound but not the leading power.** The leading class is **t⁻⁶**.
- The qualitative sign-reversal claim for Ḋ **survives unconditionally** (3.4, non-degeneracy).
- The correction is **additive only**. It is recorded after owner acceptance, and **no O-6 terminal changes.**

## LS-4 Tail bound

**4.1 The single-family bound.**
- In the angle variable, write I = ∫₀^π H(θ)·trig(tω(θ))dθ.
- Since dω/dθ = sinθ/ω, we have cos(tω) = (ω/(t sinθ))·d/dθ sin(tω), and similarly for sin.
- Set g := Hω/sinθ = (2/π)·w·λ^{(k+1)/2}·sinθ. It is smooth and satisfies g(0) = g(π) = 0.
- Integrating by parts, the boundary terms vanish, and so:

> **|I^{c,s}_{k,w}(t)| ≤ V_{k,w}/t** for all t > 0, where V_{k,w} := ∫₀^π |g′(θ)| dθ.

- Here g′ = (2/π)[w′λ^{(k+1)/2}sinθ + w·(k+1)λ^{(k−1)/2}sin²θ + wλ^{(k+1)/2}cosθ], with w′ = 0 (for w₁) or −2sinθ (for w₂).
- **Computation:** V is bounded rigorously by Σ_i (π/256)·sup_{θ∈box_i}|g′| over 256 equal θ-boxes, using
  interval arithmetic.

**4.2 The constants.** Write V_{k} := V_{k,w₁} and V_{k,2} := V_{k,w₂}. From 1.3:
- C_Q11 = (T_s/2.3)V₀² + (T_b/r)V₋₂² + |T_s − T_b|V₋₁²
- C_P11 = (T_s/2.3)V₁² + (T_b/r)V₋₁² + |T_s − T_b|V₀²
- C_C11 = (T_s/2.3)V₁V₀ + (T_b/r)V₋₁V₋₂ + |T_s − T_b|V₀V₋₁
- C_Q12 = (T_s/2.3)V₀V₀,₂ + (T_b/r)V₋₂V₋₂,₂ + |T_s − T_b|V₋₁V₋₁,₂

These give, for all T > 0:
- **|X_J(T) − X_J(∞)| ≤ C_J T⁻²**, with C_J = 1.15·C_Q11 + ½·C_P11 + C_Q12;
- **‖E(T)‖_F ≤ C_E T⁻²**, with C_E = √((C_Q11/(T_br))² + (C_P11/T_b)² + 2(C_C11/(T_b√r))²).

## LS-5 Entropy tail inequality

- **The two scalar inequalities.** For x ≥ 0, x − ln(1+x) ≤ x²/2. For −1 < x < 0, x − ln(1+x) ≤ x²/(2(1+x)).
- **The case ‖E‖_F ≤ ½.** Then ‖E‖₂ ≤ ½, so each μ_i ∈ [½, 3/2] and μ_i − 1 − ln μ_i ≤ (μ_i − 1)².
- **Conclusion:** summing gives D ≤ ½Σ(μ_i − 1)² = ½‖E‖_F². ∎

**Consequence (charter P-5).** For T ≥ T\*_σ = √(C_E/min(½, √D(0))):
- ‖E‖_F ≤ min(½, √D(0));
- hence D(T) ≤ ½D(0), and X_σ(T) ≥ ½D(0) > 0.

For J, T ≥ T\*_J = √(2C_J/|X_J(∞)|) gives |X_f(T) − X_f(∞)| ≤ ½|X_f(∞)|.

## Summary

| Item | Result |
|---|---|
| **LS-1** | Return to equilibrium (Gibbs invariance + rank-≤3 perturbation + absolute continuity + L¹ weights + Riemann–Lebesgue). **Proved.** |
| **LS-2** | X_J(∞) = (T_s − T_b) + ½T_br² (record convention), with offset ½T_br². X_σ(∞) = D(0) > 0. Exact X_f''(0), with X_f(0) = X_f′(0) = 0. **Proved.** |
| **LS-3** | D = t⁻⁶P + O(t⁻⁷) and Ḋ = t⁻⁶P′ + O(t⁻⁷). O-6's "t⁻³" for Ḋ is a loose upper bound, and the leading class is t⁻⁶. P is non-constant analytically (p₄,₀ > 0), so the sign reversal of Ḋ holds unconditionally. |

## Verification record

The block was verified by an independent adversarial verifier, read-only with respect to the repository. It used
symbolic checks and finite-chain exact evolution at non-member temperatures only.

| Item | Verdict |
|---|---|
| V1 LS-0; V2 LS-1.1/1.2; V3 LS-1.3 (five deviation formulas, matched to ~1e-40 on N = 6–10); V4 LS-1.4 (L¹ step); V5 LS-2.1/2.2; V6 LS-2.3/2.4 (D''(0) finite-difference check); V8 LS-4 (IBP, and t\|I\| ≤ V for all eight families); V9 LS-5 | **CONFIRMED** |
| V7 LS-3 | Two defects were corrected: **VC-1**, the edge phase signs; **VC-2**, the invalid non-degeneracy argument, replaced by the analytic p₄,₀ > 0. Minor wording was also fixed. |
| V10 completeness against charter §2 / ruling §9 | **CONFIRMED** after VC-2 |

**Overall: PASS after VC-1 and VC-2.** No LS-1 or LS-2 conclusion changed, and T-1 and T-2 are unaffected.
| **LS-4 / LS-5** | Explicit tail constants, and the entropy tail inequality. |

**Consequence of LS-2 for T-1 and T-2** (theorem-grade once these pass verification and the run's integrity
identities hold):

| Pair (T_s, T_b) | X_f(∞) for J (forward) |
|---|---|
| (2, 1) | 1 + ½r² > 0 |
| (10, 1) | 9 + ½r² > 0 |
| (1/2, 1) | ½ − ½r² > 0 (since r < 1) |
| (1/10, 1) | 0.9 − ½r² > 0 |

For σ, X_σ(∞) = D(0) > 0 at all four members.
