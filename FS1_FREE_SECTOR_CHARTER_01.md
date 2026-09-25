# FS-1 — CAN THE UNIT-CHANGE RESULT BE SELECTED FOR A GENUINELY FREE GAPLESS SECTOR? CHARTER + PRE-REGISTRATION (frozen before evaluation)

**Date:** 2026-09-25 · **Authority:** owner ruling recorded in
`S41_FS1_OWNER_RULING_01.md`. **Question (owner):** *Can the
constant-probe/unit-change result be selected for a genuinely free
gapless sector?* Also: can **full influence data plus G-2-recovered
spectral geometry distinguish O = H from genuinely independent conserved
O ≠ f(H)**? **Outcomes:** DERIVED · CONSTRAINED-NONUNIQUE · CLASS-SPLIT ·
IRREDUCIBLE INPUT · FAILS/NULL.

**Standing status carried in (binding):** C_cons is an **unresolved
import**. FS-1 works inside the owner-specified candidate family
(conserved local couplings), so every result below is **conditional on
C_cons**. No result here promotes it.

**Two questions, kept separate:**
- **DISTINGUISH:** can the declared data *tell apart* O = H from an
  independent conserved charge? That is an observational question.
- **SELECT:** does anything *earned* forbid the independent charge?
  That is a constraint question.

A charge can be distinguishable and still unselected. Distinguishing
two options is not selecting one of them.

**Fences:** ω⁷ occupancy only; ℏ located; GR-1 3D red; retained-sector
choice supplied (FS-1 studies its free class, it does not explain it);
D = 4 TT/ξ, operator ordering and geometry selection separate;
non-interacting universality deferred; no Einstein equations.

## 1. THE SECTOR (the exact phonon situation, frozen)

Harmonic ring, N = 20, periodic, unpinned (gapless, ω_k = 2|sin(k/2)|),
with H = ½Σpᵢ² + ½Σ(uᵢ₊₁ − uᵢ)². Quadratic operators are
Q = ½zᵀMz with z = (u, p) and symplectic J. Conservation means
AJM_H − M_HJA = 0. The dynamics is ż = JMz.

The translation-invariant local basis of range ≤ R has 4R + 3 elements:
- **pp_r** = the p-block (Sʳ + S⁻ʳ)/2, for r = 0..R;
- **uu_r**, the same u-block, for r = 0..R;
- **up_r**: uᵀSʳp, for r = −R..R.

Mode-space check: H = Σ_{k≠0} ω_k(a_k†a_k + ½).

Named members:
- **H**;
- **Q_n = ½[pᵀF_n p + uᵀF_n K u]**, with F_n = (Sⁿ + S⁻ⁿ)/2 (the even
  tower, f(k) = cos nk);
- **P_n = Σ(uᵢpᵢ₊ₙ − uᵢ₊ₙpᵢ)** (the odd tower).

## 2. THE LEGS (frozen, predictions written before any number)

- **L-T (is the free exception structural?):** the conserved subspace
  of the range-≤R basis, for R = 1, 2, 3, 4. **Prediction: dim = 2R
  exactly.** That is H, Q₁ … Q_{R−1} and P₁ … P_R. The dimension grows
  without bound with range. Explicit Q₂ and P₁ lie in it (residual
  < 1e-10). Frozen consequence: the extra local charges are a
  structural property of the free phonon sector itself, not an artifact
  of S4-1's spin models.
- **L-P (𝔠_full as selector):** H + hO with h = 0.05, for O ∈ {H, Q₂,
  P₁}. **Prediction:** M′ is positive semidefinite (min eigenvalue
  ≥ −1e-10), so the Hamiltonian is bounded below and 𝔠_full admits
  each one (NULL).
- **L-I (DISTINGUISH via influence data):**
  - (a) *Dynamic.* For any conserved O, the probe's connected two-time
    correlator is time-independent, so J(ω ≠ 0) ≡ 0. In vacuum it is
    identically zero: the mode-sum variance Σ w_k² n̄(n̄+1) has n̄ = 0.
    **Prediction (halt-grade identity):** the vacuum variance is 0.0
    for H, Q₁ and P₁. Frozen consequence: dynamic influence data cannot
    distinguish O = H from any conserved charge (UNDERDETERMINED), and
    conserved clock couplings contribute **nothing** to GR-1's
    zero-momentum pair channel.
  - (b) *Static, multi-temperature, amplitude-free.* R_O =
    Var_O(T₁)/Var_O(T₂) with T₁ = 0.5 and T₂ = 2.0. **Predictions:**
    |R_Q₁/R_H − 1| > 1e-2 and |R_P₁/R_H − 1| > 1e-2 (distinguishable);
    R(λO) = R(O) exactly (amplitude drops out).
- **L-G (DISTINGUISH via G-2 spectral geometry of the probe-modified
  sector):** G-2's hop estimator applied to the retarded response. After
  an impulse on p_j, compute u_i(t) by exact series. d̂ = (s − 1)/2,
  where s is the Richardson log-slope at t = 0.02, 0.04, 0.08.
  **Predictions:**
  - O = H: |d̂(0,d) − d| < 0.3 for d = 1..4 (a unit change preserves
    hop geometry);
  - O = Q₂: d̂(0,2) < 0.5 (a shortcut: the recovered geometry is
    rewired);
  - O = P₁: d̂(0,1) < 0.8.

  Reported only: the static resistance R(0,8) for each probe (IR
  stiffness).
- **L-S (SELECT: what would it take?):** on the R = 3 tower (six
  charges), impose the candidate **GeoInv**, *"a constant probe
  preserves the G-2-recovered hop geometry."* Operationally: for
  d = 1..4 and m ≤ 2d, the first-order-in-h coefficient of tᵐ in
  u_d(t) vanishes. This is computed by exact product-rule
  differentiation of (JM)ᵐ. **Prediction:** null space dim **1**, with
  the H direction's residual < 1e-8. GeoInv is **not earned**: it is
  chartered here as a candidate, exactly as Sel-4 was in EQ-1.

## 3. OUTCOME RULE (frozen, mechanical)

- **STRUCTURAL** if L-T holds (dim = 2R for all R).
- **DISTINGUISH:**
  - dynamic influence: NO (L-I(a)), recorded as UNDERDETERMINED;
  - static multi-T influence: YES/NO per L-I(b);
  - G-2 geometry: YES/NO per L-G.
- **SELECT:**
  - DERIVED only if an EARNED element (𝔠_full, influence data,
    G-2 geometry, as constraints) excludes every independent charge.
  - If none does (L-P admits all; the L-I and L-G signals observe
    differences without forbidding them), the verdict is **IRREDUCIBLE
    INPUT**, reduced to GeoInv when L-S gives dim 1.
  - CONSTRAINED-NONUNIQUE if earned constraints cut the tower but leave
    dim ≥ 2.
- Components are reported separately. Everything is conditional on
  C_cons.

## 4. CONTROLS

- Halt-grade: [H, H] = 0 in the quadratic algebra (the AJM − MJA
  residual < 1e-12).
- Halt-grade: the vacuum variances of conserved charges (exact zero).
- Halt-grade: the amplitude-invariance identity for R.
- Cross-check: explicit Q₂ and P₁ lie in the L-T null space.
- The series truncation for u(t) is m ≤ 40 at t ≤ 0.08
  (‖JM‖t < 0.4).
- The null-space tolerance is 1e-10 × max eigenvalue.

## 5. DELIVERABLES AND STOP

1. `calc/fs1_free.py` (pure stdlib; emits `FS1_FREE_RESULT.json`,
   sha-hashed).
2. `FS1_FREE_VERDICT_01.md` and a closing comment on Issue #2.
3. **HARD STOP at the verdict.**
