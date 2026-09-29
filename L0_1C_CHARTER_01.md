# L0-1c — LINEARITY (D-LIN): CHARTER + PRE-REGISTRATION (frozen before evaluation)

**STATUS: DRAFT REVISION 2 — NOT YET FROZEN. EXECUTION BLOCKED.** All
findings confirmed by the pre-freeze review to date are incorporated;
four verifier verdicts (honesty lens F4–F7) are still outstanding and
will be reconciled before freeze. The charter freezes at the commit
that removes this banner. No instrument exists and no gate binds until
then.

**Fork:** L0-1c, the third fork of the Level-0 necessity sweep.
**Authority:** `L0_1B_OWNER_RULING_01.md` (D-LIN authorized next per
the frozen descent order; the pin-free locality fork queued separate,
not interrupting); design basis `L0_1_NECESSITY_SWEEP_DESIGN_01.md` §4
D-LIN and §2 (the predicate registry: P_exact-reduction ≠
P_emergence). The owner's four prohibitions bind.

**Pre-freeze review provenance.** A draft of this charter (commit
`ab9108a`, banner-marked, execution blocked) underwent an adversarial
pre-freeze design review — four lenses, every finding adversarially
verified — recorded in `L0_1C_PREFREEZE_REVIEW_01.md`. All confirmed
findings are incorporated below and the material ones are disclosed
in §3. In verifying feasibility, the review **numerically exercised
the frozen schedule and previewed gate-relevant magnitudes** (the
X-1 deficits, the minimum gated response, the hardest leg's comparator
grade). Per the review's own discipline ruling, this frozen text
carries **analytic derivations and bands only**; the measured preview
values are quarantined to the review record and adjudicate nothing.
Consequence, stated before the run: the previewed gates are
**certification-grade** for this fork — the verdict must grade them as
disclosed-foreknowledge certifications, never as discoveries. The
genuinely unpreviewed live content is named in §3.5.

## 0. The frozen question, the frozen hypothesis, and the two named outcomes

> **Is linearity necessary for the phenomena, or only for the
> instrument?**

**H3 (frozen in the design, under attack here, not protection):**
linearity certifies for P_exact-reduction and does **not** certify for
P_memory / P_positivity, once the phenomenon batteries are
instrument-separated per the registry.

- **Outcome A (phenomenon failure, per-property):** an adjudicating
  leg of a deleted member loses the declared decay grade, monotone
  decrease, or the trajectory-Gram positivity reading on the gated
  window — recorded per property and per failing (β, a) set, never as
  a composed "the phenomena"; H3 is thereby falsified at the fork's
  full declared scope (§5). Outcome A is live in this fork through
  the gates §3 marks attackable — not through sign breaches, which
  §3.2's theorem forecloses.
- **Outcome B (the instrument split, the H3 target):** the
  eigen-reduction dies exactly where its defining premise
  (superposition) dies, while the phenomena survive — *linearity
  belongs to the instrument, not to the emergence class* — under the
  §3.4 transient-limited qualifier.

**The deletion touches linearity ONLY.** Every member keeps the pin
(0.3), the chain couplings (+1), and a convex potential, so
∇²V(0) = K_b **exactly, for every β** — the spectral gap at the
unique fixed point and passivity (V bounded below, strictly convex)
are held by construction. β < 0 (softening) would conflate the
linearity deletion with a passivity deletion and is **out of scope**
(noted; it belongs to a future conflated-deletion fork if ever
chartered — where §3.2's sign identity would NOT hold).

## 1. Members, legs, and the probe (frozen; N = 24; the C1-a bath block)

Substrate: the committed anchor stiffness `build_K(24, 0)` (pin 0.3,
unit chain springs); **bath block** K_b = its (1:, 1:) block
(dimension 23). Potential and dynamics:

> V(x) = ½ xᵀ K_b x + β Σᵢ xᵢ⁴  ·  **ẋ = −∇V(x) = −K_b x − 4β x³**
> (componentwise cube)

The first-order gradient-flow convention **is the record's kernel
convention**: at β = 0 it reproduces the sealed kernel
k(τ) = Σu²e^{−λτ} = e₁ᵀe^{−K_b τ}e₁ identically, and the β > 0
normalized response is this convention's kernel object by the same
declaration. Second-order (Newtonian) dynamics are a different fork,
out of scope, noted.

**Vocabulary (frozen; resolves the draft's collision):** a **member**
is a β value; a **leg** is a (β, a) pair.

- **Members:** β ∈ {0 (anchor), 0.03, 0.1, 0.3, 1.0, 3.0} — five
  deleted members plus the anchor.
- **Probe amplitudes:** x(0) = a·e₁ with a ∈ {0.001, 1.0, 3.0} —
  **18 legs**. The **normalized response** r(τ; a, β) = x₁(τ)/a is
  the kernel object: at β = 0, r ≡ k for every a (linearity); for
  β > 0 its a-dependence *is* the deletion made visible.
- **Leg roles (frozen):** the three β = 0 legs are **replication
  legs** (sealed-known); the a = 0.001 legs of deleted members are
  **linear-regime control legs**; the a ∈ {1.0, 3.0} legs of deleted
  members are the **adjudicating legs** (10 of them); the **strong
  legs** are (β = 1, a = 3) and (β = 3, a = 3). Only adjudicating
  legs can carry Outcome A (§5); replication and control legs are
  identity-protected — an M-battery failure there is HALT, never
  physics.

## 2. The two instruments, the batteries, the grids, the integrator (frozen)

**Instrument A — the eigen-reduction (P_exact-reduction).** The
committed eigen machinery (`jacobi_eig`, the eigen-form kernel). Its
defining premise is superposition: r independent of a. Instrument A's
verdict is **definitional and stated as such** (§3.1): X-1
*instantiates numerically* that the premise fails on the deleted
members; it discovers nothing.

**Instrument B — the phenomenon battery (P_memory, P_positivity;
substrate-eigen-free).** Direct time-domain integration of the
gradient flow. No eigendecomposition of the substrate enters
Instrument B; the eigen-form appears only as RC-1/RC-6's sealed
reference. (M-3 applies `jacobi_eig` to a **data** Gram matrix built
from the recorded trajectory — instrument mathematics on measured
values, presupposing nothing about the dynamics that produced them.)

- **P_memory battery:** the L0-1a grade comparator, carried as a
  **textual copy** of `fit_residuals` together with its TAUS grid
  (the carrying mechanism the draft lacked), certified against the
  sealed record by RC-6 before any deletion is read. Grade per leg on
  the gated window; never a threshold on a single number.
- **P_positivity battery (the registry substitution, disclosed —
  §3.3):** (i) monotone decrease of r on the gated window (M-2);
  (ii) the **trajectory-Gram PSD reading** (M-3): the record's
  operationalization J(w) ≥ 0 is, by Bernstein, complete monotonicity
  of the kernel, whose declared-grid form is positive
  semidefiniteness of G_ij = r(τ_i + τ_j) on the frozen sub-grid
  τ_i ∈ {1.0, 1.5, …, 20.0} (39 points; every sum τ_i + τ_j lands on
  the gated grid ≤ 40). Nonnegativity of r itself is identity-held
  (§3.2) and lives in RC-5, not in the battery.

**Grids (frozen; all ungated grids diagnostic-only).** Gated window:
τ ∈ [1, 40] step 0.5 (79 points — the registry's declared P_memory
window, carried from L0-1a/b). Early diagnostic grid: τ ∈ [0.05,
0.95] step 0.05 (19 points). Early-early diagnostic grid:
τ ∈ {0.0005, 0.001, 0.002, 0.005, 0.01, 0.02, 0.045} — anchored about
a decade below the strongest member's collapse timescale, so the
deletion-specific collapse is actually mapped (most of the amplitude
action precedes τ = 0.05, while the nonlinear-dominant regime itself
extends to τ ~ 0.25–0.5 inside the existing grids).

**Integrator (frozen; the mechanism is mandated, not just the
schedule).** Classical RK4, two-phase fixed steps h₁ = 10⁻⁴ on
[0, 1], h₂ = 2.5×10⁻³ on (1, 40]. The integrator advances by integer
step counts (10000 steps of h₁, then 15600 steps of h₂); recordings
trigger at step indices, never at accumulated-time tests —
early-early grid at h₁ steps {5, 10, 20, 50, 100, 200, 450}, early
grid at every 500th h₁ step (j = 1…19), gated grid at h₁ step 10000
and then every 200th h₂ step (i = 1…78); the halved-schedule audit
(h₁/2, h₂/2) switches phase at step 20000 and records the gated grid
at that step and every 400th h₂/2 step thereafter (early grid at
every 1000th h₁/2 step); τ labels are taken from the nominal grid
lists and τ is never accumulated in floating point.

**Trajectory inventory (frozen): 38.** The 18 legs; a
halved-schedule audit of every leg (RC-2 is per-leg); and two
**linear-continuation runs** (X-diag): from each strong leg's
recorded full-precision state x(τ = 1), integrate the pure linear
flow ẋ = −K_b x on (1, 40] under the identical h₂ stepping —
diagnostic-only, no halved audit, RC-3 with the quadratic V.

## 3. Honesty note, stated before the run (incorporating the verified review)

1. **Definitional content:** the P_exact-reduction line. "The
   eigen-reduction requires linearity" is true by what the reduction
   *is*; X-1 measures the premise's failure, it does not test a
   hypothesis. Recorded with this status on its face.
2. **The sign identity (theorem; forecloses one Outcome A branch).**
   The flow is cooperative: the Jacobian's off-diagonal entries are
   −(K_b)_ij = +w_ij ≥ 0 (Kamke condition; the −4βx³ term is
   diagonal), the vector field on each face xᵢ = 0 points inward
   (ẋᵢ = Σⱼ wᵢⱼxⱼ ≥ 0), and V is coercive with global solutions — so
   the nonnegative orthant is forward-invariant from x(0) = a·e₁,
   and Grönwall on ẋ₁ ≥ −(K₁₁ + 4βx₁²)x₁ gives **x₁(t) > 0 strictly,
   for every leg**. Scope conditions, stated so the identity is never
   over-generalized: off-diagonals of K_b nonpositive (cooperativity),
   β ≥ 0, x(0) = a·e₁ with a > 0 — all three fail in other forks
   (e.g. the fenced β < 0 fork). Consequence: **a recorded r ≤ 0
   anywhere, on any grid, at any leg, is an integrator artifact —
   HALT (RC-5), never adjudicating.** The nonnegativity half of the
   positivity battery is therefore identity-held; only monotone
   decrease and the Gram reading are tested.
3. **The registry substitution, disclosed (the draft's silent
   weakening, corrected):** the substrate-spectral construction of
   J(w) is Instrument-A-definitional and dies with the
   eigen-reduction; the *property* has the exact eigen-free reading
   of §2 (Bernstein/Gram), which M-3 gates. The §5 positivity line is
   scoped to this operationalization on its face — never
   UNFORMULABLE-YET (the battery is formulable, and a false entry
   would corrupt the formulability floor the D-ORD/D-HERM/D-DET queue
   keys on).
4. **The deletion is transient-limited on the declared window
   (analytic; the structural cap).** With the 0.3 pin on every site,
   at any maximizer of m(t) = maxᵢ xᵢ(t) the linear part contributes
   ≤ −0.3m, so D⁺m ≤ −4βm³ and hence x₁(t)² ≤ m(t)² ≤ 1/(8βt) for
   every β > 0 member and every amplitude. The cap is **uniform in β
   and a**: by the gated window the nonlinear stiffness 12βx₁² sits
   below λ_min at every leg. In-class re-chartering can push the
   amplitude-collapse defect toward 1 but can **never** produce
   in-window-dominant nonlinearity; a future fork seeking that
   stronger deletion sense must name a structurally different
   deletion (nonlinearity in the couplings, or a convex
   non-self-limiting potential). Outcome B, if it lands, carries this
   qualifier on its face.
5. **Classification of the live content (the review's central
   product).** *Certification-grade (previewed or analytically
   banded):* X-1 — its direction is forced on the orthant (r ≤ k by
   comparison with the linear flow; r nonincreasing in a by
   subhomogeneity, both resting on cooperativity + forward-invariance,
   and making X-1's |·| one-sided at the declared legs), its
   magnitude sits in an analytic band ≈ 0.6–0.85 against the frozen
   0.1 margin, and its persistence is forced — the burned slow-mode
   amplitude accumulates monotonically, so an early-dying transient
   *freezes* the deficit at the loss factor rather than erasing it.
   (The `ab9108a` draft carried the opposite mechanism — "could fail
   if the transient dies before τ = 1" — which is backwards; recorded
   here per the disclosure obligation.) Likewise M-1 at replication
   and control legs (sealed-known / linear-regime). *Analytic-leaning:*
   M-1 at adjudicating legs — the transient is exhausted before the
   window opens even at the strongest leg (its own x₁ ≳ 0.3
   criterion puts the crossover near t ≈ 0.26), so what the
   window-global fit actually sees is the transient-deformed launch
   state, early-window higher-mode content, and an envelope-derived
   in-window distortion budget of ≲ 0.2 nats against the sealed
   comparator's multi-nat discriminant (R_alg − R_exp ≈ 2.8 on the
   anchor), drifting in the passing direction — never in-window
   nonlinear dominance, which §3.4 caps; M-2 (componentwise monotone decrease of a nonlinear
   cooperative flow on a finite window is unproven — only eventual
   monotonicity is forced — but the structure makes a rebound
   remote). *Genuinely unpreviewed:* **M-3, the trajectory-Gram PSD
   gate — no identity forces near-complete-monotonicity of the
   nonlinear response, and no preview touched the Gram spectrum; this
   is the fork's sharpest live content** — plus the D_act activation
   map, the early-early collapse map, and the M-diag fine structure.
6. **Diagnostic honesty (two corrections carried from the review):**
   (i) X-1's margin is carried overwhelmingly by pre-window
   depletion; in-window deletion activity is measured by D_act (§4
   X-diag), recorded ungated per the design's magnitudes-reported
   rule, and both NOT-LOAD-BEARING lines are scoped to a deletion
   whose in-window action is at the recorded D_act level. (ii) The
   late-slope M-diag compares each leg against the **anchor leg's own
   fitted window-tail slope**, not against λ_min = 0.304, which is
   asymptotic-only — the window tail reads a mode-mixture value above
   it for every leg including β = 0, and misreading that as a
   deletion effect is the exact artifact this line forecloses.

## 4. The gates (frozen, mechanical)

**Controls and identities (halt-grade; a breach anywhere is HALT):**
- RC-1 replication: eigen-form k(0) − 1 within 10⁻¹²; eigen k(40)
  matches L0-1a's recorded 6.8195192260507686×10⁻⁹ (|rel Δ| < 10⁻⁹);
  the time-domain (β = 0, a = 0.001) leg matches the eigen form on
  the gated grid, sup |r/k − 1| < 10⁻⁶.
- RC-2 integrator self-consistency, **per leg** (all 18): full
  schedule vs halved schedule, sup over the gated grid of
  |rel Δ| < 10⁻⁹ (tolerance set from the review's independent
  two-implementation feasibility measurements at the binding leg,
  with ~30× margin; the audit exists at every leg so §5's Outcome A
  needs no post-result battery addition).
- RC-3 the Lyapunov identity: along every recorded trajectory, V
  non-increasing across consecutive recorded points (all three
  grids), tolerance ΔV ≤ 10⁻¹²·(V_prev + 10⁻³⁰); quadratic V on the
  two linear-continuation runs.
- RC-4 superposition at β = 0: sup over the gated grid of
  |r(τ; a)/r(τ; 0.001) − 1| < 10⁻⁹ for a ∈ {1.0, 3.0}.
- RC-5 the sign identity (§3.2): r > 0 at every recorded point of
  every grid at every leg; any r ≤ 0 anywhere is HALT — never an
  M-line failure, never Outcome A. (M-1's comparator therefore always
  operates on positive data or the run has halted; the guard executes
  before the comparator.)
- RC-6 comparator certification: the textual copy of `fit_residuals`
  + TAUS, applied to the eigen-form anchor kernel, reproduces the
  sealed L0-1a anchor values R_exp = 1.9809889100368165 and
  R_alg = 4.7907669413552245 with |Δ| < 10⁻¹² each, and the grade
  string "EXPONENTIAL-GRADE" exactly.

**X — the deletion is real (conditions every NOT-LOAD-BEARING line):**
- X-1 (gate; certification-grade per §3.5): at both strong legs,
  sup over the gated grid of |r(τ; 3)/r(τ; 0.001) − 1| > 0.1
  (within-member comparison; the a = 0.001 leg is the member's own
  linear regime).
- X-diag (ungated): **D_act**, the linear-continuation activation
  defect at each strong leg — sup over the gated grid of
  |x₁_full(τ)/x₁_lin(τ) − 1| against the §2 linear-continuation run
  (same initial state, same integrator, only the deletion term
  differs; zero iff the deletion is inert in-window) — plus the
  collapse-defect map over all 18 legs and sup |r(τ; 0.001, β)/k − 1|
  per member.

**M — the phenomena under the deletion (Instrument B only; all 18 legs):**
- M-1 (gate) P_memory: the certified comparator classifies r
  EXPONENTIAL-GRADE on the gated window at every leg.
- M-2 (gate) P_positivity, monotone half: steps ≤ +10⁻¹² on the
  gated window at every leg.
- M-3 (gate) P_positivity, Gram half (**the unpreviewed live gate**):
  the 39×39 data Gram G_ij = r(τ_i + τ_j) has minimum eigenvalue
  ≥ −10⁻¹⁰ at every leg (`jacobi_eig` on the data matrix; the
  tolerance clears integration-noise perturbation of the Gram by an
  order of magnitude while leaving genuine violations readable).
- M-diag (ungated): per-leg R_exp/R_alg and grade map; late-slope per
  leg vs the anchor leg's fitted window-tail slope (§3.6.ii); the
  early and early-early transient maps (undershoot status is RC-5's
  domain; shape is mapped here); min Gram eigenvalue per leg.

## 5. Outcome rule (frozen, mechanical; per-property lines, never composed)

**Scope declaration, on the face of every recorded line, under every
outcome including VACUOUS, PARTIAL, and HALT:** *within the declared
background mathematics (real symmetric matrices, exact
eigendecomposition, the frozen RK4 schedule), the convex quartic
on-site class on the C1-a bath (N = 24), the declared amplitudes
a ∈ {0.001, 1.0, 3.0}, window, grids, and comparator.* This sentence
is "the recorded scope" wherever a line names it.

- **LINEARITY: NECESSITY-CERTIFIED for P_exact-reduction** iff RC-4
  and X-1 hold — definitional status on the face (§3.1).
- **LINEARITY: NOT-LOAD-BEARING for P_memory** (at the declared
  amplitudes; the deletion's in-window action recorded at the D_act
  level) iff M-1 holds at every leg AND X-1 holds.
- **LINEARITY: NOT-LOAD-BEARING for P_positivity, as operationalized
  by the declared window-cone battery and the trajectory-Gram PSD
  reading** (at the declared amplitudes; nonnegativity identity-held
  per §3.2, monotone decrease and Gram PSD tested; D_act recorded)
  iff M-2 AND M-3 hold at every leg AND X-1 holds.
- **H3 / Outcome B is certified** iff all three lines land — with the
  §3.4 transient-limited qualifier on the face, citing the scope
  clause above.
- **Outcome A (mechanical):** iff no RC breach anywhere (else HALT),
  X-1 holds, and M-1, M-2, or M-3 fails on the gated window at an
  **adjudicating leg** (a ∈ {1.0, 3.0} of a deleted member).
  Recorded per property and per failing (β, a) set: "linearity is
  load-bearing for P_memory [resp. P_positivity as operationalized]
  at the failing legs, at the recorded scope" — never a composed
  "the phenomena"; the other property's line may still issue. One
  clean gated failure falsifies H3 at the fork's full declared scope;
  the surviving (β, a) set is mapped ungated (M-diag), never issued
  as per-leg certificates. An M-battery failure at a replication or
  control leg is HALT (identity-protected), never Outcome A.
- **L01C-VACUOUS** iff X-1 fails at **both** strong legs (the
  deletion never bit at the tested amplitudes: no NOT-LOAD-BEARING
  line may issue; the honest product is the maps plus a re-charter
  obligation — noting per §3.4 that an in-class re-charter can raise
  the collapse defect but never in-window dominance).
- X-1 failing at one strong leg but not the other →
  **L01C-PARTIAL**, with the collapse map reported, naming which
  strong leg the deletion bit; no NOT-LOAD-BEARING line may issue
  (X-1 is a single conjunction — survival at a leg where the deletion
  never bit certifies nothing), and the re-charter obligation
  attaches at the leg where it failed to bite.
- **L01C-PARTIAL** for any other gate failure; **HALT** on any RC
  breach.
- **Precedence (run-level labels only):** HALT > L01C-VACUOUS >
  Outcome A > L01C-PARTIAL. This orders run-level labels; it neither
  composes nor suppresses the per-property lines. VACUOUS and Outcome
  A are mutually exclusive by construction (X-1 fails-at-both vs
  X-1 holds), so their relative order is inert — recorded to prevent
  a future reader from inferring a live co-fire.

Under every outcome: no v4 channel moves; no red gate is touched;
GR2, L0-1a, L0-1b, and the public paper untouched. **HARD STOP**
after the verdict, pending owner ruling (which decides the
formulability floor — D-ORD / D-HERM / D-DET — and the queued
pin-free locality fork).

## 6. Instrument contract

`calc/l01c_linearity.py`: pure stdlib; imports `build_K` unchanged
(it supplies K_b to both instruments) and `jacobi_eig` unchanged
(Instrument A / RC-1 / RC-6's eigen reference, and M-3's data-Gram
PSD test per §2); carries the certified textual copy of
`fit_residuals` + TAUS (RC-6); RK4 exactly as §2, integer-count
stepping mandated; deterministic, no RNG; single run; the 38
trajectories of §2; writes `L0_1C_RESULT.json` (sha-hashed) with
`defect_history`; runtime minutes. Scope: the §5 scope clause;
nothing else.
