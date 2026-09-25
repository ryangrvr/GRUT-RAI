# P-3 — THE NONCOMMUTATIVE LIFT: CHARTER + PRE-REGISTRATION (frozen before evaluation)

**Date:** 2026-09-25 · **Authorized by:** owner, GitHub **Issue #2**
(title: "P-3 authorization: quantum/noncommutative lift of influence cone
and counting law") + its ten-point working-guidance comment — **the issue
text is the authority; this charter freezes the implementation.** Binding
posture from the issue: **attack, do not confirm**; do not assume the
scalar cone lifts; do not assume the counting law survives; do not turn
P-3 into a proof of quantum mechanics; a clean failure identifying the
first genuinely noncommutative/non-Gaussian obstruction is a successful
outcome. Fences carried: Λ_R, Matsubara, Π₀, U5; ω⁷/class-4 untouched
(guidance point 8); type-III as extension map only (point 9).

## 0. THE TWO QUESTIONS (issue verbatim, compressed)

**A.** Does the Gaussian admissibility geometry lift to genuinely
noncommutative finite type-I systems **without collapsing into a
restatement of ordinary uncertainty/positivity**?
**B.** Does locality + symmetry counting survive matrix/channel structure
and higher non-Gaussian cumulants?

Outcome taxonomy per question (frozen; point 1): **SURVIVES / MODIFIED /
CLASS-SPLIT / FAILS-NULL**, with the redundancy rule (point 4) overriding:
a found constraint reducible to (a) state positivity or (b) complete
positivity is recorded **NULL-AS-NEW-PRINCIPLE** even where it survives as
geometry. A failed derivation is never collapsed into a modified
hypothesis.

## 1. THE MODEL BATTERY (frozen; all exactly solvable, finite type I)

- **Q1 (matrix admissibility):** bath = 3 spins, H_B = Σ ωᵢσ_zⁱ/2 with
  ω = (0.7, 1.0, 1.6), thermal state β = 2.0. TWO noncommuting coupling
  operators (deliberately off-diagonal channels, point 3):
  B₁ = Σ gᵢσ_xⁱ, g = (0.6, 0.5, 0.4); B₂ = Σ hᵢσ_yⁱ, h = (0.3, 0.7, 0.2)
  ([B₁,B₂] ≠ 0, verified in-run). Exact spectral matrices
  C_ab(ω) = Σ_{n,m:E_m−E_n=ω} p_n⟨n|B_a|m⟩⟨m|B_b|n⟩ by direct
  computational-basis summation (H_B diagonal; no approximation).
  Definitions frozen: ν(ω) ≡ (C(ω)+C̄ᵀ(−ω))/2, J(ω) ≡ C(ω)−C̄ᵀ(−ω).
  **Candidate lift (hypothesis only, point 3):**
  **ν(ω) ± J(ω)/2 ⪰ 0 as Hermitian matrices**, Hermiticity of ν and J,
  covariance under ω-independent invertible channel mixing B → RB
  ((J,ν) → RJR†, RνR†; truth-value invariance under congruence).
  Tests: (i) the candidate holds at every discrete frequency of the
  noncommuting-channel model (eigenvalue check); (ii) covariance verified
  under a declared non-orthogonal R; (iii) noncommutativity of the
  spectral matrices across frequencies verified ([·,·] ≠ 0);
  (iv) **strictness over the scalar theory:** the declared pair
  ν = [[1, .9],[.9, 1]], J = diag(1.8, 1.8) passes every channelwise
  scalar check (ν_aa ≥ J_aa/2) yet ν − J/2 has a negative eigenvalue —
  it must be certified NON-REALIZABLE (no Gram/state representation);
  (v) **redundancy adjudication (point 4):** exhibit the Gram
  decomposition showing C(±ω) ⪰ 0 IS bath-state positivity — if that
  succeeds, Q1's verdict is "SURVIVES-AS-GEOMETRY / NULL-AS-NEW-PRINCIPLE"
  and never a new foundational claim; (vi) commuting restriction: the
  single-channel diagonal reduces to the scalar ν ≥ |J|/2.
- **Q2 (CP separation, point 4b):** probe qubit + Q1 bath,
  H = μσ_x^p + σ_z^p⊗B₁ + H_B, μ = 0.4, λ-scale 1; the reduced map's
  Choi matrix at t ∈ {0.7, 2.1} must be PSD (tolerance 1e-9) — recorded
  as the dilation-guaranteed (b) leg: CP adds no data constraint beyond
  (a); any Choi negativity HALTS (instrument bug, not physics).
- **Q3 (non-Gaussian control, point 5):** matched-two-point pair —
  bath A = two spins (ω₀ = 1, coupling g = 0.5 each, ground state);
  bath B = one spin (ω₀ = 1, coupling g√2, ground state). Frozen claims
  to verify: C_A(t) = C_B(t) = 2g²e^{−iω₀t} exactly; equal-time connected
  fourth cumulants differ, κ₄(A) = −4g⁴ vs κ₄(B) = −8g⁴ (analytic,
  verified numerically); third cumulants vanish by symmetry (checked).
  Probe pure-dephasing coherence (σ_z^p⊗B, λ = 1, t ∈ [0, 10], 400 pts):
  **detection** = max|ρ₀₁^A − ρ₀₁^B| > 1e-3 with the matched control
  (A vs A under a bath-local relabeling) < 1e-12. If detected: the
  Gaussian pair (K, N) is a **projection** — CLASS-SPLIT, first
  obstruction = κ₄; higher cumulants are NOT forced into (K, N).
- **Q4 (counting in noncommuting channels, point 6):** two-channel,
  two-species golden-rule battery with linear dispersion and rank-2
  noncommuting J(ω) (species vertices v = (q, 0.3q²)/√(2ω),
  w = (0.3q², q³)/√(2ω)); eigen-exponents by exact roots + log-slope on
  the S-1 window [0.02, 0.2]. Frozen hypotheses at INCREMENT level:
  H1-matrix — multiplying all vertices by q shifts BOTH eigen-slopes by
  +2 ± 0.1; H3-matrix — a near-cancelling two-term vertex (the B4-class
  bracket) in one species adds +4 ± 0.2 to the eigenvalue it dominates;
  **null control (convention laundering):** an ω-dependent channel
  rescaling diag(1, ω) visibly shifts apparent slopes — demonstrated and
  EXCLUDED by the ω-independent-basis freeze, so no exponent claim may
  ride a basis convention.
- **Q5 (representation invariance, point 7):** bath-local z-rotations
  (commuting with H_B and the state) give a microscopically re-labeled
  realization with identical FULL influence data → probe trajectories
  identical (< 1e-12) — representational, D-1 extended to matrix level.
  The distinguishing pair is Q3's (identical 2-point, different κ₄):
  the influence-data quantity carrying the distinction is **named** (κ₄).
- **Q6 (type-III extension map, point 9):** derivational section of the
  verdict only — which finite-I conclusions must generalize or fail at
  the boundary (discrete Gram sums → spectral measures; factorized
  preparations unavailable without the split-property collar; normal-state
  tomography for CP; the operator-order cone as Bochner-type positivity).
  No claims.

## 2. CONTROLS (halt on miss)

Exact-model controls: Hermiticity of every C(ω) (1e-12); Gram-PSD of
every C(±ω) (min eig ≥ −1e-10); scalar-restriction recovery; Q3's
two-point match (< 1e-12) BEFORE the coherence comparison; Q2 Choi PSD;
Q4's S-1 scalar limit (single channel reproduces +2/+4 exactly).
NO-PROOF-OF-QM fence: every positivity used is CITED as quantum-mechanical
input, never presented as derived; the ℏ floor stays located-not-generated.

## 3. COMPOSITE VERDICT RULE (mechanical)

Question A: SURVIVES-AS-GEOMETRY iff Q1(i,ii,iii,vi) pass and (iv)
detects; AND-ed with NULL-AS-NEW-PRINCIPLE iff (v) exhibits the
positivity reduction. Question B: SURVIVES iff Q4's two increments hold;
CLASS-SPLIT (for the influence-data structure) iff Q3 detects with its
controls clean. FAILS-NULL wherever a leg's construction fails; MODIFIED
where a condition holds only in altered form (reported per leg; never
averaged).

## 4. DELIVERABLES AND STOP

1. `calc/p3_nc_lift.py` (pure stdlib; emits `P3_NC_LIFT_RESULT.json`,
   sha-hashed).
2. `P3_NC_LIFT_VERDICT_01.md` — per-leg verdicts, the composite, the
   type-III map, and a closing comment posted to Issue #2.
3. **HARD STOP at the verdict** (waiting decision: the owner rules on
   what the lift's outcome does to 𝒯). Fences stand throughout.
