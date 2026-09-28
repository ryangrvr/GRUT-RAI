# L0-1c — LINEARITY (D-LIN): CHARTER + PRE-REGISTRATION (frozen before evaluation)

**STATUS: DRAFT — NOT YET FROZEN. EXECUTION BLOCKED.** An adversarial
pre-freeze design review (four lenses; findings verified before
incorporation) is in progress; confirmed findings will be incorporated
here and disclosed, and the charter freezes at the commit that removes
this banner. No instrument exists and no gate binds until then.

**Fork:** L0-1c, the third fork of the Level-0 necessity sweep.
**Authority:** `L0_1B_OWNER_RULING_01.md` (D-LIN authorized next per
the frozen descent order; the pin-free locality fork queued separate,
not interrupting); design basis `L0_1_NECESSITY_SWEEP_DESIGN_01.md` §4
D-LIN and §2 (the predicate registry: P_exact-reduction ≠
P_emergence). The owner's four prohibitions bind.

## 0. The frozen question, the frozen hypothesis, and the two named outcomes

> **Is linearity necessary for the phenomena, or only for the
> instrument?**

**H3 (frozen in the design, under attack here, not protection):**
linearity certifies for P_exact-reduction and does **not** certify for
P_memory / P_positivity, once the phenomenon batteries are
instrument-separated per the registry.

- **Outcome A (phenomenon collapse):** the anharmonic members lose
  finite-memory-grade decay or the positivity structure on the
  declared window — linearity is load-bearing for the phenomena, H3
  falsified. **Unlike L0-1b, Outcome A is genuinely live in this
  fork:** the nonlinear transient enters the gated window at the
  strong members, and no identity forbids an M-gate failure there.
- **Outcome B (the instrument split, the H3 target):** the
  eigen-reduction dies exactly where its defining premise
  (superposition) dies, while the phenomena survive — *linearity
  belongs to the instrument, not to the emergence class.*

**The deletion touches linearity ONLY.** Every member keeps the pin
(0.3), the chain couplings (+1), and a convex potential, so:
∇²V(0) = K_bath **exactly, for every β** — the spectral gap at the
unique fixed point and passivity (V bounded below, strictly convex)
are held by construction. β < 0 (softening) would conflate the
linearity deletion with a passivity deletion and is **out of scope**
(noted for the record; it belongs to a future conflated-deletion fork
if ever chartered).

## 1. Members (frozen; N = 24; the C1-a bath block)

Substrate: the L0-1a/b anchor stiffness `build_K(24, 0)` (pin 0.3,
unit chain springs); **bath block** K_b = the (1:, 1:) block
(dimension 23), exactly the committed machinery. Potential and
dynamics:

> V(x) = ½ xᵀ K_b x + β Σᵢ xᵢ⁴  ·  **ẋ = −∇V(x) = −K_b x − 4β x³**
> (componentwise cube)

The first-order gradient-flow convention **is the record's kernel
convention**: at β = 0 it reproduces the sealed kernel
k(τ) = Σu²e^{−λτ} = e₁ᵀe^{−K_b τ}e₁ identically. Second-order
(Newtonian) dynamics are a different fork, out of scope, noted.

- **Deletion members:** β ∈ {0 (anchor), 0.03, 0.1, 0.3, 1.0, 3.0}.
- **Probe amplitudes (declared):** x(0) = a·e₁ with
  a ∈ {0.001 (linear-regime control), 1.0, 3.0}. The **normalized
  response** r(τ; a, β) = x₁(τ)/a is the fork's kernel object:
  at β = 0, r ≡ k for every a (linearity); for β > 0 its
  a-dependence *is* the deletion made visible.

## 2. The two instruments (by construction, per design §4; never conflated)

**Instrument A — the eigen-reduction (P_exact-reduction).** The
committed eigen machinery (`jacobi_eig`, the eigen-form kernel). Its
defining premise is superposition: r independent of a. Instrument A's
verdict is **definitional and is stated as such** (§3): the gate
X-1 *instantiates numerically* that the premise fails on the deleted
members; it discovers nothing.

**Instrument B — the phenomenon battery (P_memory, P_positivity;
eigen-free).** Direct time-domain integration of the gradient flow;
r(τ; a, β) read on the declared grids; decay-grade classified by the
**L0-1a comparator carried verbatim** (max-abs-residual linear fits of
ln r vs τ against ln r vs ln τ on the gated window — never a threshold
on a single number); positivity read as nonnegativity + monotone
decrease on the gated window. **No eigendecomposition enters
Instrument B's battery**; the eigen-form appears only inside RC-1's
β = 0 replication control, where it is the sealed reference.

**Grids (frozen).** Gated window: τ ∈ [1, 40] step 0.5 (79 points —
the registry's declared P_memory window, carried from L0-1a/b).
Early diagnostic grid: τ ∈ [0.05, 0.95] step 0.05 (19 points),
**ungated** — the transient is mapped, never adjudicated (§3).

**Integrator (frozen).** Classical RK4, deterministic two-phase fixed
steps: h₁ = 10⁻⁴ on [0, 1], h₂ = 2.5×10⁻³ on (1, 40]. Every grid
point lands exactly on a step boundary; no interpolation anywhere.

## 3. Honesty note, stated before the run (the L0-1a/b precedent)

1. **Definitional content:** the P_exact-reduction line. "The
   eigen-reduction requires linearity" is true by what the reduction
   *is*; X-1 measures the premise's failure, it does not test a
   hypothesis. The line is recorded with this status on its face.
2. **Analytic-leaning content:** ∇²V(0) = K_b exactly for all β, so
   the *late-time* decay rate at every member is the anchor's
   λ_min = 0.304 (linearization at the held fixed point). By late
   window, amplitudes are ~10⁻⁸ — deep in the linear regime. A late-
   window M failure would therefore be identity-suspect (instrument
   first). What is **not** protected by any identity: the strong
   members' transients persist into the *early gated window*
   (at β = 3, a = 3: 4βx₁² ≳ the spectral scale until x₁ ≲ 0.3), so
   the window-global comparator and the monotonicity battery can
   genuinely fail there.
3. **The genuinely attackable content:** M-1 at the strong members
   (does the transient's curvature flip the frozen comparator's
   grade?); M-2 everywhere (componentwise monotonicity of a nonlinear
   cooperative flow is *not* proven — an undershoot/rebound inside the
   gated window would fail the gate honestly); and the size of X-1's
   collapse defect (frozen margin, could fail if the transient dies
   before τ = 1).
4. **Vacuity protection (frozen rule):** a NOT-LOAD-BEARING
   certificate may be issued **only if X-1 passes** — survival under a
   deletion that never bit certifies nothing (the L0-1a G-3 lesson:
   first prove the deletion is real, then read survival).

## 4. The gates (frozen, mechanical)

**Controls and identities (halt-grade):**
- RC-1 replication: eigen-form k(0) − 1 within 10⁻¹²; eigen k(40)
  matches L0-1a's recorded 6.8195192260507686×10⁻⁹ (|rel Δ| < 10⁻⁹);
  and the time-domain run at (β = 0, a = 0.001) matches the eigen form
  on the gated grid: sup |r/k − 1| < 10⁻⁶ (Instrument B is certified
  against the sealed machinery before any deletion is read).
- RC-2 integrator self-consistency at the hardest member (β = 3,
  a = 3): the full schedule against the halved schedule (h₁/2, h₂/2):
  sup over the gated grid of |rel Δ| < 10⁻⁷.
- RC-3 the Lyapunov identity: along every recorded trajectory,
  V(x) is non-increasing across consecutive recorded grid points
  (early + gated), tolerance ΔV ≤ 10⁻¹²·(V_prev + 10⁻³⁰) — gradient
  flow descends; a rise is an integrator bug, never physics.
- RC-4 superposition at β = 0 (the linear identity): sup over the
  gated grid of |r(τ; a)/r(τ; 0.001) − 1| < 10⁻⁹ for a ∈ {1.0, 3.0}.

**X — the deletion is real (gate; conditions every NOT-LOAD-BEARING line):**
- X-1 amplitude collapse fails at the strong members: at (β = 1,
  a = 3) and (β = 3, a = 3), sup over the gated grid of
  |r(τ; 3)/r(τ; 0.001) − 1| > 0.1 (within-member comparison; the
  small-amplitude leg is the member's own linear regime).
- X-diag (ungated): the collapse-defect map over the full (β, a)
  lattice; and sup |r(τ; 0.001, β)/k − 1| per member (the small-
  amplitude legs should hug the linear kernel — reported).

**M — the phenomena under the deletion (Instrument B only):**
- M-1 (gate) P_memory: the frozen comparator classifies r(τ; a, β)
  EXPONENTIAL-GRADE on the gated window for **all 18 members**
  (every β × every a). The comparator requires r > 0 across the
  window; a member with any gated r ≤ 0 records grade UNDEFINED and
  **fails M-1** (a sign-changing kernel has no decay grade under this
  comparator — recorded as such, never skipped, never crashed).
- M-2 (gate) P_positivity: on the gated window, r ≥ −10⁻¹² and steps
  ≤ +10⁻¹² at **all 18 members**.
- M-diag (ungated): per-member late-slope fit vs the analytic 0.304;
  the early-grid transient map (undershoot/rebound status per member);
  the comparator's R_exp/R_alg per member.

## 5. Outcome rule (frozen, mechanical; per-property lines, never composed)

- **LINEARITY: NECESSITY-CERTIFIED for P_exact-reduction** iff RC-4
  holds AND X-1 holds — recorded with its definitional status on the
  face (§3.1).
- **LINEARITY: NOT-LOAD-BEARING for P_memory** iff M-1 holds at every
  member AND X-1 holds.
- **LINEARITY: NOT-LOAD-BEARING for P_positivity** iff M-2 holds at
  every member AND X-1 holds.
- **H3 / Outcome B is certified** iff all three lines land as above —
  recorded as: *linearity is necessary for the exact-reduction
  instrument and not load-bearing for the tested response phenomena —
  within the declared background mathematics, the convex quartic
  on-site class on the C1-a bath (N = 24), the declared amplitudes,
  window, and comparator.*
- **Outcome A** is recorded iff X-1 holds and M-1 or M-2 fails at a
  deleted member with the failure surviving instrument audit
  (RC-2/RC-3 clean at that member) — H3 falsified at recorded scope,
  a finding, not a defect.
- **L01C-VACUOUS** iff X-1 fails (the deletion never bit at the tested
  amplitudes: no NOT-LOAD-BEARING line may issue; the honest product
  is the map plus a re-charter obligation at stronger deletion).
- **L01C-PARTIAL** for any other gate failure; **HALT** on any RC
  breach.

Under every outcome: no v4 channel moves; no red gate is touched; GR2,
L0-1a, L0-1b, and the public paper untouched. **HARD STOP** after the
verdict, pending owner ruling (which decides the formulability floor —
D-ORD / D-HERM / D-DET — and the queued pin-free locality fork).

## 6. Instrument contract

`calc/l01c_linearity.py`: pure stdlib; imports `build_K` and
`jacobi_eig` unchanged (Instrument A / RC-1 only); RK4 exactly as §2;
deterministic, no RNG; single run; writes `L0_1C_RESULT.json`
(sha-hashed) with `defect_history`; runtime minutes (the 19
trajectories: 18 members + one halved-schedule audit). Scope: the
convex quartic on-site class above; the declared grids and comparator;
nothing else.
