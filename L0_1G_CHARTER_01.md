# L0-1g — D-ORD-b (O-6): CHARTER + PRE-REGISTRATION (frozen before evaluation)

**STATUS: DRAFT — NOT YET FROZEN. EXECUTION BLOCKED** pending
analytic-only pre-freeze review. The charter freezes at the commit
that removes this banner.

**Fork:** L0-1g, obligation **O-6**. **Authority:** owner ruling
`L0_1G_OWNER_RULING_01.md` (option C1). Design basis:
`L0_1G_DORD_B_DESIGN_01.md` revision 2. **I-1 … I-5 are identity-grade
constraints carried in as-is and not rerun as findings.** The only
exception is I-5's instantiation, which appears as a halt-grade control
(RC-6). The owner's four prohibitions bind.

**Preview discipline:** no quantity on the declared substrate was
computed to write this charter. The design's verifier used only
non-member toy chains (archived in `calc/feasibility/`).

## 0. The frozen question and hypothesis

> **After the initial slip and before recurrence, does an
> ensemble-level ordering emerge robustly from the coupled
> conservative system**, as a property of a restricted ensemble (an
> uncorrelated product initial state) plus a system–bath partition,
> despite conservative full dynamics?

**H-ORD (ensemble operationalization; under attack).** For the two
directions I-5 leaves open:
- the heat current into the bath is non-negative when the system is
  hotter (L1);
- the reduced relative entropy to equilibrium is non-increasing when
  the system is colder (L2);

both throughout the post-slip, pre-recurrence window, at every declared
N and temperature pair.

**The live alternative:** non-Markovian backflow. Memory in the bath,
from band edges with algebraic tails, reverses the heat current or the
entropy trend *inside* the window, so emergent dissipation does not
imply emergent ordering.

**Neither outcome is forced by any identity** (design §3 as revised).

## 1. Substrate, split, initial ensemble (frozen)

- **𝒦_N:** q̈ = −K_N q, where K_N is the N × N tridiagonal with
  diagonal 2.3 (sites 1 … N−1) and 1.3 (site N), and off-diagonal −1.
  - K₂₃ = K_b exactly (the sealed bath block).
  - The spectrum is closed form: λ_k = 2.3 − 2cos((2k−1)π/(2N+1)) and
    v_k(i) ∝ sin((2k−1)iπ/(2N+1)).
- **N ∈ {23, 47, 95}.**
- **Split:** the retained system is site 1, with K₁₁ = 2.3 and coupling
  g = −K₁₂ = 1. The bath is sites 2 … N, and K_BB has the same
  structure at size N − 1.
- **Initial ensemble** (the declared past hypothesis): a zero-mean
  Gaussian product of the uncoupled Gibbs states.
  - System: ⟨q₁²⟩ = T_s/K₁₁, ⟨p₁²⟩ = T_s.
  - Bath: ⟨q_Bq_Bᵀ⟩ = T_b K_BB⁻¹, ⟨p_Bp_Bᵀ⟩ = T_b I.
  - All cross terms are zero.
- **Temperature pairs:**
  - L1: (T_s, T_b) ∈ {(2, 1), (10, 1)};
  - L2: (T_s, T_b) ∈ {(1/2, 1), (1/10, 1)}.
- **Evolution (exact modal form):** q(t) = C(t)q₀ + S(t)p₀ and
  p(t) = −KS(t)q₀ + C(t)p₀, with C = cos(√K t) and
  S = K^{−1/2}sin(√K t). All second moments are evaluated from the
  closed-form modes. **No integrator, no RNG.**

## 2. The window, the slip, the grid (frozen before evaluation)

- **Slip end (frozen, substrate-derived):** t_s = 2π/√K₁₁ ≈ 4.143, one
  natural period of the isolated retained oscillator.
- **Recurrence horizon (frozen formula):** T_rec(N) = 2(N−1)/v_max,
  where v_max = max over k ∈ (0, π) of sin k/√(2.3 − 2cos k). That is
  the maximal group velocity of the infinite pinned chain, computed by
  a dense scan with 10⁵ points plus golden-section refinement.
- **Gated window:** 𝒲_N = [t_s, T_rec(N)), on the grid t = 0.05·j.
- **Mapped, never gated:** the slip interval [0, t_s), and
  [T_rec, 2T_rec) at N = 23 (recurrence onset).

## 3. The batteries (exact moment formulas; no finite differences in the gates)

- **L1, heat current into the bath:**
  J(t) = d⟨E_B⟩/dt = g⟨p₂q₁⟩(t). Here E_B = ½|p_B|² + ½q_BᵀK_BB q_B is
  the bath's self-energy.
- **L2, reduced relative entropy:**
  D(t) = KL(𝒩(0, S₁(t)) ‖ 𝒩(0, S_ref)).
  - S₁ is the 2×2 (q₁, p₁) covariance.
  - **S_ref = T_b·diag((K_N⁻¹)₁₁, 1)**, the reduced *global* Gibbs state
    at T_b (design §3: the local Gibbs state is not the N → ∞ limit).
  - The gate uses the **exact derivative**
    Ḋ = ½tr[(S_ref⁻¹ − S₁⁻¹)Ṡ₁], with
    - d⟨q₁²⟩/dt = 2⟨q₁p₁⟩;
    - d⟨p₁²⟩/dt = −2K₁₁⟨q₁p₁⟩ + 2g⟨p₁q₂⟩;
    - d⟨q₁p₁⟩/dt = ⟨p₁²⟩ − K₁₁⟨q₁²⟩ + g⟨q₁q₂⟩.

## 4. The gates (frozen, mechanical)

**Controls (halt-grade; a breach is HALT):**
- **RC-1:** the closed-form spectrum of K₂₃ agrees with `jacobi_eig`
  (max |Δλ| < 10⁻¹²), and K₂₃ equals the sealed `build_K(24,0)` bath
  block entry by entry.
- **RC-2 energy conservation:** ⟨H⟩(t) = T_s + (N−1)T_b at every grid
  point, with relative error < 10⁻⁹. (Equipartition gives the initial
  value.)
- **RC-3 covariance validity:** S₁(t) is symmetric positive definite at
  every grid point.
- **RC-4 derivative consistency:** at 20 declared points, the exact
  moment derivatives match centered differences (h = 10⁻⁴) to a
  relative error of 10⁻⁵.
- **RC-5 I-5 instantiation (surviving directions):**
  - J(t)/t → g²T_s/K₁₁ at t = 10⁻³ (relative error < 10⁻³);
  - (D(t) − D(0))/t² → ½g²(K_BB⁻¹)₁₁(1 − T_b/T_s) at t = 10⁻³
    (relative error < 10⁻²; the bath's first site is index 1 of K_BB).
- **RC-6 I-5 instantiation (the wrong directions; the owner's recorded
  distinction):**
  - for T_s < T_b, J(10⁻²) > 0: the bath gains energy from the colder
    system at switch-on;
  - for T_s > T_b, Ḋ(10⁻²) > 0: relative entropy rises for the hotter
    system at switch-on.

**The attackable gates (H-ORD, ensemble):**
- **G-1 (L1):** J(t) ≥ −ε_J at every grid point of 𝒲_N, for every N and
  both L1 pairs. ε_J = 10⁻¹⁰·max_{𝒲_N}|J|.
- **G-2 (L2):** Ḋ(t) ≤ +ε_D at every grid point of 𝒲_N, for every N and
  both L2 pairs. ε_D = 10⁻¹⁰·max_{𝒲_N}|Ḋ|.

**Maps (ungated):**
- per N and pair: the minimum of J (and maximum of Ḋ) on 𝒲_N, the
  first violation time if any, and the fraction of the window in
  violation;
- the full behavior on the slip interval [0, t_s);
- recurrence onset on [T_rec, 2T_rec) at N = 23;
- convergence of J and D across N on the common window.

## 5. Honesty note (stated before the run)

- **Identity-grade:** RC-1 … RC-6. RC-5 and RC-6 *instantiate* I-5;
  they discover nothing.
- **Genuinely attackable:** G-1 and G-2. No identity fixes the sign of
  J or Ḋ after the slip. The leading small-t slopes favor the H-ORD
  directions, but I-5's own t³ term in J is negative:
  −g²(2T_bK₁₁ + T_sK₁₁ + T_sK₂₂)/(6K₁₁). So the sign at larger t is
  genuinely open.
- **Choices that bound the claim, frozen here:**
  - t_s (one retained period). Any backflow inside the slip is mapped,
    never gated.
  - The grid step of 0.05. Sub-grid backflow shorter than the step is
    not tested; this is disclosed.
  - N ≤ 95 (compute budget, pure stdlib). The window grows about 4.2×
    across the family.
  - One coupling, g = 1, the record's own. Weak-coupling (Markov)
    families are not tested.
- **Scope:** one conservative harmonic class, Gaussian ensembles, the
  declared pairs. No anharmonic or quantum substrates.

## 6. Outcome rule (frozen; lines never composed)

**Scope clause, on every line under every outcome:** *within the
conservative pinned harmonic chain 𝒦_N for N ∈ {23, 47, 95}, the
record's coupling, zero-mean Gaussian product initial states at the
declared temperature pairs, the frozen slip end, recurrence horizon and
grid, and exact modal evaluation; I-1 … I-5 as identity-grade
constraints.*

- **L-1 (identity; from the design, restated):** in this class there is
  **no pointwise ordering by state functions** (I-1 … I-3), and **the
  past hypothesis produces an anti-arrow at switch-on** (I-5,
  instantiated by RC-6). *past hypothesis ≠ arrow at t = 0.*
- **L-2 (heat):** issued iff G-1 holds: "after the slip and before
  recurrence, heat flows one way from the hotter system into the
  bath". If G-1 fails: "heat backflow inside the window" (memory).
- **L-3 (entropy):** issued iff G-2 holds: "after the slip and before
  recurrence, the colder system's relative entropy to global
  equilibrium decreases monotonically". If G-2 fails: "information
  backflow inside the window".

**Run labels and the O-6 terminal-label mapping** (proposed; the owner
assigns):

| Run outcome | Supports |
|---|---|
| G-1 and G-2 both hold | **DISCHARGED:** H-ORD (ensemble) holds at scope. An arrow emerges from restricted ensemble plus partition, after the slip, before recurrence. |
| both fail | **FALSIFIED:** H-ORD (ensemble) is refuted at scope; memory spoils ordering within the window. |
| one holds, one fails | **CLASS-SPLIT:** heat ordering and entropy ordering diverge. |
| HALT | non-terminal (re-charter budget: one) |

An N-dependent status, where a gate holds at some N but not others, is
reported per N. The gate as frozen requires **every** N and pair.

Under every outcome, nothing else on the record moves. **HARD STOP**
after the verdict.

## 7. Instrument contract

`calc/l01g_bath_arrow.py`: pure stdlib. It imports `build_K` and
`jacobi_eig` (RC-1 only) unchanged. The modes are closed form. The
moment formulas are exact and modal, with precomputed initial-covariance
matrices in mode space. It is deterministic, with no RNG, and runs once.
It writes `L0_1G_RESULT.json` (sha-hashed) with `defect_history`.
