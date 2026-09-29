# L0-1e — D-DET (DETERMINISM / NOISE–DISSIPATION): CHARTER + PRE-REGISTRATION (frozen before evaluation)

**STATUS: DRAFT — NOT YET FROZEN. EXECUTION BLOCKED** pending the
analytic-only pre-freeze review. The charter freezes at the commit that
removes this banner. No instrument exists and no gate binds until then.

**Fork:** L0-1e, the second floor fork. It works on obligations **O-3**
(determinism deleted, fluctuation–dissipation held) and **O-4**
(noise–dissipation mismatch), with separate lines and separate
terminal-label mappings. **Authority:** `L0_1D_OWNER_RULING_01.md`
(D-DET authorized); registry rulings R-1 … R-4 (R-2: every stochastic
predicate splits into P^resp and P^corr); design basis
`L0_1_FLOOR_DESIGN_01.md` §3 D-DET. The owner's four prohibitions bind.

**Anti-circularity rule (design §3):** every noise profile is a
**declared substrate datum**. None is constructed from K, and none is
set by importing rung2's KMS lock. The fluctuation–dissipation relation
is a consistency check on declared data, never a derivation input.

**Preview discipline:** no member covariance, kernel, weight, or
spectrum was computed to write this charter. The only computation was
a feasibility timing of the exact Lyapunov solve on a **non-member**
matrix (pin 0.7, arbitrary temperatures): 276 unknowns, about 1 s,
exact residual 0.

**A self-correction made during drafting, disclosed.** The first draft
gated "at least one limit shape breaches correlation CM" as the fork's
real content. Two of those shapes put zero temperature on the retained
site, so they breach **by identity** (§3.5). The gate was vacuous. It
was replaced before any review or computation, and the attackable
content moved to orientation and threshold location (§0).

## 0. The frozen question, the hypotheses, the outcomes

> **Does primitive noise in the microscopic update bear on the tested
> response properties, and if the fluctuation–dissipation match is
> broken, what does it take to break them?**

- **H-DET-1 (O-3):** determinism is not load-bearing for any tested
  predicate on either object while the fluctuation–dissipation
  relation (FDT) holds. **Identity-grade by design (§3.1, §3.2),
  recorded as such, never as a discovery.**
- **H-DET-2 (O-4):** the noise–dissipation match is load-bearing for
  P_positivity^corr component (c), complete monotonicity (CM), beyond
  a threshold. **Its existence half is now identity-grade in this
  class** (§3.5): a retained site at zero temperature cannot carry a
  CM correlation. By the cone theorem (§3.4), that forces a finite
  threshold in every family whose limit shape cools the retained site
  to zero. **This fork cannot falsify it**, and it says so.
- **H-DET-3 (O-4; the attackable content, pre-registered):**
  **orientation matters.** A gradient that makes the retained site the
  *hottest* site (the reversed ramp) keeps correlation CM for every
  gradient strength: GR(∞) lies inside the cone. **And the ramp
  family's threshold is interior to the declared range:** G(2) keeps
  CM and G(1000) loses it.

## 1. Substrate, noise, members (frozen)

**Substrate:** the sealed C1 bath K = K_b, the (1:, 1:) block of
`build_K(24, 0)`: symmetric, irreducible tridiagonal, simple spectrum,
positive definite. It is built exactly as M = 10K from integers.

**Stochastic update (the deleted axiom is determinism):**
dx = −Kx dt + B dW, Q = BBᵀ = 2·diag(T_i), T_i ≥ 0 declared. The
process is linear with additive Gaussian noise, so it is **Gaussian and
fully characterized by its mean and covariance** (a theorem).
Stochasticity is therefore represented **exactly** through the unique
stationary covariance Σ solving KΣ + ΣK = Q. **No sampling and no
RNG.** Non-Gaussian, multiplicative, colored, and nonlinear stochastic
classes are out of scope.

**Objects (R-2):**
- **Response:** k_resp(τ) = e₁ᵀe^{−Kτ}e₁.
- **Correlation:** C(τ) = e₁ᵀe^{−Kτ}y, y = Σe₁; normalized
  c = C/C(0).

**Temperature profiles** (exact rationals):

| Member | T_i (i = 1 … 23) | Role |
|---|---|---|
| **F** | 1 | O-3; FDT held; cone interior |
| **G(R)**, R ∈ {2, 10, 100, 1000} | 1 + (R−1)(i−1)/22 (hot far end) | O-4 ramp family |
| **G(∞)** | (i−1)/22 (T₁ = 0) | ramp limit shape; **identity breach** (§3.5) |
| **GR(10)**, **GR(1000)** | 1 + (R−1)(23−i)/22 (hot retained site) | O-4 reversed family |
| **GR(∞)** | (23−i)/22 (T₁ = 1, T₂₃ = 0) | reversed limit shape; **attackable** |
| **H(1000)** | 1 + 999·δ_{i,12} | hot-spot member |
| **H(∞)** | δ_{i,12} (T₁ = 0) | hot-spot limit shape; **identity breach** |

Eleven stochastic members, plus the deterministic anchor D (the sealed
kernel). **Roles:** D and F are identity-protected. G(∞) and H(∞) are
identity-breach members (RC-12). G(2), G(1000), GR(∞) are the
**adjudicating** members. G(10), G(100), GR(10), GR(1000), H(1000) are
mapped.

## 2. Instruments and batteries (frozen)

**Instrument E (exact, static; R-3 at declared linear-class scope).**
For each stochastic member, exactly:
- Σ from the Lyapunov equation with rational K = M/10: 276 symmetric
  unknowns, exact Gaussian elimination;
- y = Σe₁;
- the M-scaled correlation moments mₙ = e₁ᵀMⁿy (n = 0 … 47);
- d_c, the exact rank of the 24×24 Hankel [m_{i+j}];
- H₀ = [m_{i+j}] and H₁ = [m_{i+j+1}] at size d_c.

The response moments are sₙ = e₁ᵀMⁿe₁. **Exact CM test:** H₀ ≻ 0 by
exact Sylvester pivots (no pivoting; stop at the first pivot ≤ 0).

**Instrument B (time-domain, eigen-free):** RK4 of ẋ = −Kx from
x(0) = y/y₁ (float of the exact y), giving c(τ) = x₁(τ). It uses the
L0-1c/d integer-count schedule verbatim, with a halved-schedule audit.
22 trajectories.
- **P_memory^corr:** the RC-10-certified textual copy of
  `fit_residuals` + TAUS on E(τ_i) = max_{j≥i} |c(τ_j)| (R-1).

**Eigen references (`jacobi_eig`, symmetric only):** K's
eigendecomposition. It gives the float weights w_k = u_k(v_kᵀy) for the
**ungated** threshold map and RC-3's eigen-form c, and it serves the
symmetric data Gram of the operational map.

**Grids:** gated τ ∈ [1, 40] step 0.5; early τ ∈ [0.05, 0.95] step
0.05.

## 3. Honesty note, stated before the run (identities first)

1. **Response is noise-blind (F-5; theorem).** d⟨x⟩/dt = −K⟨x⟩
   exactly, so k_resp is the sealed kernel for every member. Every
   P^resp line is identity-grade, instantiated by RC-1.
2. **The FDT member (identity).** Q = 2I gives Σ = K⁻¹ uniquely. Then
   mₙ(K) = s_{n−1}(K) for n ≥ 1, C(τ) = Σ_k (u_k²/λ_k)e^{−λ_kτ} is
   exactly CM, and −C′ = k_resp exactly. **O-3 is identity-grade in
   its entirety.**
3. **Correlation nonnegativity, component (a) (identity).** −K is
   Metzler, so e^{−Kt} ≥ 0 entrywise. Then Σ ≥ 0 entrywise for
   diagonal Q ≥ 0, so y ≥ 0 and C ≥ 0. C is strictly positive because
   y₁ > 0 at every member: every profile heats some site and K is
   irreducible. **Noise mismatch cannot make the correlation
   negative.**
4. **The cone theorem (the organizing identity).**
   - K is symmetric with simple spectrum and every u_k ≠ 0, so
     C = Σ_k w_k e^{−λ_kτ} with w_k = u_k v_kᵀΣe₁, and C is CM ⟺ every
     w_k ≥ 0.
   - Σ is linear in Q, so **each w_k is linear in the profile T**, and
     the CM set 𝒦 is a **convex polyhedral cone**.
   - The uniform profile U lies in its **interior** (weights
     u_k²/λ_k > 0), so **CM survives every sufficiently mild FDT
     violation** (a theorem, with "sufficiently" unbounded).
   - For a family T(R) = U + (R−1)·S:
     - if S ∈ 𝒦, CM holds for **every** R ≥ 1;
     - if S ∉ 𝒦, CM holds exactly for R < R* = 1 + min_{k: w_k(S)<0}
       w_k(U)/|w_k(S)|, and fails beyond.
5. **The zero-temperature obstruction (identity; new; it removed the
   first draft's vacuous gate).**
   - The (1,1) entry of the Lyapunov equation gives
     **m₁(K) = e₁ᵀKΣe₁ = T₁ exactly**, so −C′(0) = T₁.
   - A nonzero CM function of the form Σw_k e^{−λ_kτ} with λ_k > 0 and
     w_k ≥ 0 has −C′(0) = Σw_kλ_k > 0.
   - **So T₁ = 0 with y₁ > 0 means C is not CM.** G(∞) and H(∞) are
     outside 𝒦 by identity. By §3.4, **the ramp and hot-spot families
     each have a finite threshold R*, by theorem.** Only its location
     is unknown.
   - Physically: *a retained site that is not itself thermally driven
     cannot carry a completely monotone autocorrelation; it only
     echoes what arrives from elsewhere.* That is a structural fact
     about the class, not a finding of this run.
6. **Further exact controls:**
   - the Lyapunov residual is exactly zero;
   - Σ is exactly symmetric;
   - **KΣ ≠ ΣK** at every FDT-broken member, so the deletion is real.
     KΣ = ΣK would force Σ = K⁻¹Q/2 to be symmetric, which fails for a
     nonuniform diagonal Q and an irreducible tridiagonal K.
7. **McMillan degree (the L0-1d lesson).**
   - d_c is the number of nonzero weights, and the test is sized by
     d_c.
   - H₀ ≻ 0 at size d_c ⟺ every nonzero weight is positive.
   - Given H₀ ≻ 0, H₁ ≻ 0 is identity-held because every λ_k > 0.
8. **Classification.**
   - *Identity-grade:* every P^resp line; all of O-3; component (a);
     the G(∞) and H(∞) breaches; the existence of the ramp and
     hot-spot thresholds; RC-1 … RC-12.
   - *Theorem, with an unbounded constant:* mild-violation survival.
   - *Analytic-leaning:* D-2, survival at G(2).
   - **Genuinely unpredicted, attackable:**
     - **D-1, GR(∞) inside the cone.** Orientation: does heating the
       retained site preserve CM for every strength?
     - **D-3, G(1000) breaches.** Does the ramp threshold fall inside
       the declared range?
   - *Not banded:* M-1.
   - *Mapped:* the other members' exact status, R* per family,
     monotonicity (b), commutator size, FDT-deviation ratios, the
     operational Gram, E(40).
9. **Scope.** One substrate (the tree bath), diagonal additive Gaussian
   noise, and declared profiles. Not tested: the generator sector
   (O-1), colored or multiplicative noise, or nonlinear stochastic
   dynamics.

## 4. The gates (frozen, mechanical)

**Controls and identities (halt-grade; a breach anywhere is HALT):**
- **RC-1 sealed replication (the P^resp instantiation):** the
  eigen-form k_resp(40) = 6.8195192260507686×10⁻⁹ (|rel Δ| < 10⁻⁹).
- **RC-2 halved audit:** every trajectory, sup |c_full − c_half|·e^{λ₁τ}
  < 10⁻⁶ on the gated grid.
- **RC-3 eigen-form cross-check:** the time-domain c matches
  Σw_k e^{−λ_kτ}/y₁, sup |Δ|·e^{λ₁τ} < 10⁻⁶.
- **RC-4 exact Lyapunov:** KΣ + ΣK − Q = 0 exactly, and Σ = Σᵀ
  exactly, at every member.
- **RC-5 exact m₁ identity:** m₁(K) = T₁ exactly at every member.
- **RC-6 FDT member:** KΣ = I exactly at F. Also mₙ(K) = s_{n−1}(K)
  exactly for n = 1 … 47. And H₀ ≻ 0 with d_c = 23.
- **RC-7 the deletion is real:** KΣ ≠ ΣK exactly at every FDT-broken
  member.
- **RC-8 sign:** y ≥ 0 entrywise exactly with y₁ > 0 at every member,
  and c > 0 at every recorded point.
- **RC-9 exact construction:** M = 10K from integers, and the sealed
  `build_K` bath equals float(M/10) entry by entry.
- **RC-10 comparator certification:** the textual copy on the
  eigen-form sealed anchor gives E = k exactly, and reproduces
  R_exp = 1.9809889100368165 and R_alg = 4.7907669413552245
  (|Δ| < 10⁻¹²) and "EXPONENTIAL-GRADE".
- **RC-11 H₁ identity:** wherever H₀ ≻ 0, H₁ ≻ 0.
- **RC-12 zero-temperature identity:** G(∞) and H(∞) fail the exact CM
  test.

**The response properties (O-4):**
- **D-1 (H-DET-3, orientation; attackable):** GR(∞) passes the exact
  correlation CM test.
- **D-2 (mild survival; analytic-leaning):** G(2) passes.
- **D-3 (threshold in range; attackable):** G(1000) fails.
- **M-1, P_memory^corr (R-1 envelope; not banded):** EXPONENTIAL-GRADE
  on E at every stochastic member.
- **Maps (ungated):**
  - exact CM status and d_c at every member;
  - R* per family from the float weights (§3.4);
  - monotone-decrease (b) status;
  - the commutator ratio ‖KΣ − ΣK‖_F / ‖KΣ‖_F;
  - FDT-deviation ratios mₙ(K)/(T₁·s_{n−1}(K)), n = 2 … 5, wherever
    T₁ > 0;
  - the operational Gram minimum eigenvalue, full and halved;
  - E(40).

## 5. Outcome rule (frozen, mechanical; lines never composed)

**Scope clause, on the face of every recorded line under every
outcome, including PARTIAL and HALT:** *within the declared background
mathematics (exact rational arithmetic for Instrument E, the frozen RK4
schedule for Instrument B, exact symmetric eigendecomposition for the
references), the sealed C1 bath with linear additive Gaussian noise of
diagonal intensity 2·diag(T_i), the eleven declared profiles, and the
declared window, grids, and comparator. Family verdicts extend to every
R ≥ 1 only through the cone theorem (§3.4).*

**The lines:**
- **L-1 (O-3, P^resp):** DETERMINISM: NOT-LOAD-BEARING for P^resp.
  **Theorem (F-5);** instantiated by RC-1.
- **L-2 (O-3, P^corr, FDT held):** DETERMINISM: NOT-LOAD-BEARING for
  P^corr (components (a), (c), and the FDT relation) when FDT holds.
  **Identity-grade;** issued iff RC-6.
- **L-3 (O-4, existence; identity):** NOISE–DISSIPATION MISMATCH:
  LOAD-BEARING for P_positivity^corr (c) in the ramp and hot-spot
  families, **beyond a finite threshold that exists by theorem**
  (§3.4, §3.5). Issued iff RC-12. The face states that this is an
  identity, not a finding.
- **L-4 (O-4, orientation; the finding):** issued per D-1.
  - If D-1 holds: "HEATING THE RETAINED SITE PRESERVES CORRELATION CM
    AT EVERY GRADIENT STRENGTH (reversed-ramp family; cone theorem)".
  - If D-1 fails: "ORIENTATION DOES NOT PROTECT: the reversed ramp also
    breaks correlation CM beyond a finite threshold".
- **L-5 (O-4, threshold location):** records D-2 and D-3 exactly, with
  the ramp family's float R* from the map, labeled ungated.
- **L-6 (O-4, P_memory^corr):** NOISE–DISSIPATION MISMATCH:
  NOT-LOAD-BEARING for P_memory^corr (R-1 envelope). Issued iff M-1
  holds. An M-1 failure is **COMPARATOR-LIMITATION**: the exponential
  bound is identity-held, so a failure is never recorded as
  load-bearing.

**Run labels:**
- **HALT:** any RC breach.
- **OUTCOME-ORIENTED:** D-1, D-2, and D-3 all hold (the pre-registered
  picture).
- **OUTCOME-UNORIENTED:** D-1 fails. Both orientations break;
  H-DET-3's orientation half is refuted.
- **OUTCOME-THRESHOLD-SHIFTED:** D-1 holds, but D-2 or D-3 fails. The
  ramp threshold lies outside (1, 2] ∪ [1000, ∞) as pre-registered.
- **L01E-PARTIAL:** an M-1 comparator limitation, or any other non-RC
  failure.
- **Precedence:** HALT > L01E-PARTIAL > the D-outcomes. This orders run
  labels only and composes no lines.

**Mapping to terminal labels** (proposed; the owner assigns, per T2):

| Obligation | Run result | Supports | Re-charter used? |
|---|---|---|---|
| **O-3** | RC-1 and RC-6 clean (any non-HALT run) | **DISCHARGED** (identity-grade; recorded as such) | no |
| **O-4** | OUTCOME-ORIENTED | **CLASS-SPLIT:** the cone divides the profile space. The FDT and hot-retained-site directions keep correlation CM at every strength; cold-retained-site directions lose it beyond a threshold. Same substrate. | no |
| **O-4** | OUTCOME-UNORIENTED or OUTCOME-THRESHOLD-SHIFTED | **CLASS-SPLIT** (the near-FDT interior vs the identity-breach shapes still divides the class). The refuted part of H-DET-3 is recorded **on the L-4 / L-5 faces**, never as a label. The termination condition permits exactly four terminal labels, and this fork adds none. | no |
| O-3 / O-4 | HALT / L01E-PARTIAL | non-terminal | **yes, one each** |

Under every outcome: no v4 channel moves; no red gate is touched;
L0-1a … d, GR2, and the public paper are untouched. **HARD STOP** after
the verdict, pending owner ruling on the lines and on the O-3 and O-4
labels.

## 6. Instrument contract

`calc/l01e_noise_dissipation.py`: pure stdlib. Instrument E uses exact
integers and `fractions`, on M = 10K built from integers. The code
imports `build_K` and `jacobi_eig` unchanged; `jacobi_eig` is used for
symmetric references and the data Gram only. It carries the
RC-10-certified textual copy of `fit_residuals` + TAUS. It is
deterministic, with **no RNG anywhere**, and runs once: 11 exact
Lyapunov solves plus 22 trajectories. It writes `L0_1E_RESULT.json`
(sha-hashed) with `defect_history`. Scope: the §5 clause, nothing else.
