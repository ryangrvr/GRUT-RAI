# L0-1g — D-ORD-b (O-6) DESIGN 01: ordering on a conservative substrate through its bath

**Status: DESIGN REVISION 2 — NOT A CHARTER.**

**Revision 2 note (the focused verification's findings are all
incorporated).** I-1 … I-4 are confirmed, with fixes:
- I-1 now cites D-4's *non-strict* form.
- I-2 is extended from quadratic functionals to all C¹ functionals, on
  classes containing C₀.
- I-3 is worded for E₁ and E_B specifically.
- I-4's caveat is added.

The verifier also found a **new identity, I-5 (the initial slip)**. It
shows that §3's "no identity decides the ensemble question" was
**false for half of the proposed batteries**. §3 and §4 are rewritten
accordingly.

**Verifier toy checks (disclosed):** a symbolic small-t expansion on a
generic N = 4 chain with free-symbol entries, and a numerical N = 3
toy (entries 3.1/2.7/1.9, couplings −0.7/−0.5). Nothing was evaluated
on the declared chain, and no L1 or L2 curve on the window was
computed.

**Original status line:** no computation was run by the operator. The
identities below are theorems with proofs. **One operationalization choice belongs to the owner
(§4) before any charter is frozen**, because it decides what the
question *means*.

**Authority:** `L0_1F_OWNER_RULING_01.md` (O-6 authorized, with the
owner's framing: can temporal ordering arise on a conservative,
recurrent substrate through its coupling to a bath, rather than from a
primitive clock or an assumed dissipative structure?). The termination
condition's O-6 row reads "window-relative ordering in one conservative
substrate via the system/bath split".

## §1 The substrate (proposed)

**𝒦_N: the record's pinned chain, made conservative.**
- Dynamics: q̈ = −K_N q, with K_N the N-site tridiagonal (pin 0.3, unit
  springs, a wall spring at site 1, a free far end). **K₂₃ = K_b, the
  sealed bath block**, so the record's substrate is literally the
  N = 23 member.
- Phase space x = (q, p) ∈ ℝ^{2N}, with ẋ = Ax and
  H = ½|p|² + ½qᵀK_N q conserved.
- Closed form, from L0-1f's T-1: λ_k = 2.3 − 2cos((2k−1)π/(2N+1)),
  ω_k = √λ_k, and v_k(i) ∝ sin((2k−1)iπ/(2N+1)).
- **Split:** the retained system is site 1 (z₁ = (q₁, p₁)); the bath is
  sites 2 … N.
- **Emergent dissipation:** as N → ∞ the site-1 spectral lines merge
  into a band [√0.3, √4.3], and the retained response decays. At
  finite N it recurs, with a recurrence time T_rec(N) ∝ N (a round trip
  at the maximal group velocity).

## §2 The identities that constrain *any* O-6 design (front-run; proofs given)

**I-1 (window-ordering for all initial states is global, so conserved
here).** Let F be C¹ on the phase space of an autonomous flow. If F is
non-increasing on [0, T] (T > 0) along the trajectory from **every**
initial state, then dF/dt ≤ 0 **everywhere**, because every point is
an initial state. On 𝒦_N every orbit is a translation on a torus
(frequencies ω_k > 0), so it is recurrent in both time directions. By
**D-4's argument in its non-strict form**, F is constant on every
orbit, so **F is conserved.** The non-strict form: a monotone function
along an orbit with α∩ω ≠ ∅ has equal limits at ±∞, and so is constant.
Only continuity of F is needed.

**Consequence:** a *nontrivial* window-relative ordering exists **only
relative to a restricted class of initial conditions.** O-6 must
therefore declare one: the bath at rest, or the bath thermal and
uncorrelated with the system (a product state). **The "past hypothesis"
is forced by the mathematics, not chosen for convenience.**

**I-2 (the system's own state cannot carry the ordering, even with the
bath at rest).**
- **Class:** C₀ = {bath at rest (q_B = p_B = 0), z₁(0) arbitrary}.
- **Candidates:** quadratic reduced functionals V_P = z₁ᵀPz₁, P ≻ 0.
- **Step (a): only the system energy survives t = 0.** At t = 0 on C₀,
  q₂ = 0, so ż₁ = A₀z₁ exactly, with A₀ = [[0, 1], [−K₁₁, 0]].
  Non-increase at 0⁺ for all z₁ requires PA₀ + A₀ᵀP ⪯ 0, which forces
  P ∝ P_E = diag(K₁₁, 1) (computation in the design notes). **The only
  candidate is the retained site's energy E₁ = ½p₁² + ½K₁₁q₁².**
- **Step (b): even that fails immediately.** dE₁/dt = p₁q₂. On C₀,
  p₁ = uᵀz₁(0) and q₂ = vᵀz₁(0), with u = (ċ, ṡ) and v = (c₂, s₂) the
  retained and next-site response functions. The quadratic form
  p₁q₂ = z₁ᵀ sym(uvᵀ) z₁ has **det sym(uvᵀ) = −¼W², where
  W = u₁v₂ − u₂v₁**. So **it is indefinite whenever W ≠ 0**: one
  eigenvalue is positive and one negative, whatever their size.
- Taylor on C₀ gives u = (−K₁₁t, 1) + O(t²) and v = (t²/2, t³/6) +
  O(t⁴), so **W(t) = −t²/2 + O(t⁴) ≠ 0 for small t > 0.** W is
  analytic, so its zeros are isolated.
- **So on every window (0, T], some system initial state sends energy
  *back into* site 1.** No quadratic functional of the system's own
  state orders trajectories there, at any N. The argument uses only
  local structure, so it holds equally at N = ∞.

**Extension to every C¹ functional G(z₁), on any class containing C₀
(verifier).**
- Step (a) forces ∇G·A₀z ≤ 0 for all z. The isolated oscillator's flow
  is periodic, so G is constant on its ellipses: G = g(E₁).
- Then dG/dt = g′(E₁)·p₁q₂, and the indefinite cone of step (b), scaled
  to any energy level, forces g′ ≡ 0.
- **So no C¹ function of the system's state orders trajectories on any
  window, over any initial class containing C₀.** (For classes *not*
  containing C₀, step (a)'s argument does not apply, and none is
  claimed.)
- A concrete backflow instance: with q₁₀ = 0, p₁q₂ ≈ (t³/6)p₁₀² > 0,
  sourced by the negative interaction energy −q₁q₂.

**Reading:** this is non-Markovianity at the level of identities. The
reduced dynamics of a conservative split is not autonomous in z₁, so
z₁ alone cannot carry an arrow. That holds even where the bath is
infinite and genuinely dissipative.

**I-3 (the bath's energy fails the same way).** With
E_B = ½|p_B|² + ½q_BᵀK_BB q_B, dE_B/dt = p₂q₁. On C₀ this is again a
rank-one symmetric form. With (c, s) = (1, t) + O(t²) and
(ċ₂, ṡ₂) = (t, t²/2) + O(t³), **W(t) = −t²/2 + O(t⁴) ≠ 0**, so the form
is indefinite (same determinant argument): some initial state makes the
bath *lose* energy on every window. **Energy partition functions do not
order pointwise over the class either.**

**I-5 (the initial slip; new, from the verifier; symbolic on a generic
chain, valid for every N ≥ 2 and any coupling g = −K₁₂, including
N = ∞).**
- **Setup:** a product Gaussian initial state ρ_S(T_s) ⊗ ρ_B(T_b). The
  interaction energy starts at 0 and the system–bath correlations start
  at 0.
- **Bath-energy current:**
  d⟨E_B⟩/dt = g²(T_s/K₁₁)·t − g²(2T_bK₁₁ + T_sK₁₁ + T_sK₂₂)/(6K₁₁)·t³
  + O(t⁵).
  **Its leading term is positive for every T_s > 0, whatever T_b is.**
  (Operator check: ⟨p₂q₁⟩(0) = 0 and d⟨p₂q₁⟩/dt|₀ = −K₂₁⟨q₁²⟩ =
  gT_s/K₁₁.) **So when the system is colder than the bath, the bath
  still first *gains* energy from it.** That is the coupling
  switch-on: the interaction energy goes negative as correlations
  build.
- **Reduced relative entropy** against any reference state with
  ⟨p₁²⟩ = T_b (the local Gibbs state, or the reduced global Gibbs
  state):
  D(t) − D(0) = ½g²(K_BB⁻¹)₂₂(1 − T_b/T_s)·t² + O(t³).
  Bath noise reaches ⟨p₁²⟩ at order t². The system's own dissipation
  enters only at order t⁴. **So when the system is hotter than the
  bath, the reduced relative entropy first *rises*.**
- **Consequence:** under the textbook past hypothesis (a product
  state), **the switch-on transient runs *against* the relaxation arrow
  at t = 0⁺ for half of the temperature orderings, by identity, at
  every N.** It fails on every window, so it is not a finite-size
  effect.

**I-4 (trivial orderings exist and must be excluded).** On any orbit
segment before its first return, the orbit map is injective, so "time
since leaving C₀" is a function of state there. It orders trivially.
It is also **the dynamics itself read backwards**: a clock by
construction. It is well defined per orbit, or as "time since the most
recent visit to C₀", since an orbit can re-enter C₀. So **the ordering functional must come from a declared
structural class** (energies, entropies, locality-defined quantities),
fixed before evaluation. Otherwise the question is vacuous.

## §3 What remains open after the identities (REVISED by I-5; the original text below is superseded where it conflicts)

**After I-5, exactly two ensemble directions remain open under a
product initial state:**

| Battery | Temperature ordering | Status |
|---|---|---|
| L1: mean bath energy **non-decreasing** | hot system, cold bath (T_s > T_b) | **Open.** The leading slope is positive; later sign changes are not decided. |
| L2: reduced relative entropy **non-increasing** | cold system, hot bath (T_s < T_b) | **Open.** The leading slope is negative; later backflow is not decided. |
| L1 read as "heat flows the right way" | cold system, hot bath (T_s < T_b) | **Fails at t = 0⁺ by identity (I-5).** |
| L2 | hot system, cold bath (T_s > T_b) | **Fails at t = 0⁺ by identity (I-5).** |

**The L2 reference state must be pinned before any charter.** The
local Gibbs state is **not** the N → ∞ limit of the reduced state: by
the Schur complement, (K⁻¹)₁₁ > 1/K₁₁. So D measured against the local
Gibbs state tends to a nonzero limit, and the natural reference is the
**reduced global Gibbs state** at T_b.

**Corrected overclaim:** "beyond T_rec, D-4 guarantees failure" should
read: D-4, applied to the recurrent covariance flow in its non-strict
form, guarantees **non-monotonicity somewhere on [0, ∞)** at every
finite N. It does not guarantee failure in any particular interval
after T_rec.

---

**(Original §3 text, superseded where it conflicts with the table
above.)**

I-1 through I-4 close the pointwise, all-state and reduced-state
routes. **What is left is genuinely open: ordering at the level of
ensembles, given a declared product initial state.**
- **Initial state (the declared past hypothesis):** ρ₀ = ρ_S(T_s) ⊗
  ρ_B(T_b), Gaussian thermal, with T_s ≠ T_b.
- **Why this is not yet identity-decided:** averaging over the
  system's thermal initial phases kills the phase-sensitive backflow
  terms of I-2 and I-3. What remains is scalar functions of t, whose
  sign is **not** fixed by any identity above.

**Candidate structural batteries (Gaussian; closed form from the
2N-dimensional covariance flow X(t) = e^{At}X₀e^{Aᵀt}):**
- **L1, the mean bath energy ⟨E_B⟩(t):** is it monotone on the window
  (non-decreasing if T_s > T_b)? This is heat flow without backflow.
- **L2, the reduced relative entropy D(ρ₁(t) ‖ ρ₁^eq(T_b)):** is it
  non-increasing on the window? That would be a second law for the
  split. In the open-systems literature, non-monotonicity of such
  distinguishability measures is the standard signature of
  non-Markovian information backflow.
- **The window:** [0, T_rec(N)) as N grows; T_rec is frozen as a
  formula before evaluation. Beyond T_rec, D-4 guarantees failure at
  every finite N (recurrence), and that is an identity control.

**Pre-registrable hypotheses:**
- **H-ORD (as frozen in the design):** ordering arises only through
  emergent dissipation, window-relatively.
- **Its ensemble operationalization:** L1 and L2 are monotone on
  [0, T_rec(N)) for all large N at the record's coupling, and fail
  beyond T_rec.
- **The live alternative:** **non-Markovian backflow**. L2 or L1
  fails *inside* the window even as N → ∞, because the pinned chain's
  band edges give the bath a memory kernel with algebraic tails
  (van Hove). In that case emergent *dissipation* would not imply
  emergent *ordering*.
- **Neither outcome is predicted by an identity here.**

## §4 REVISED — the owner's decision after I-5

The dead routes are now: A (I-1); B for every C¹ system-state
functional on classes containing C₀ (I-2 as extended); B′ for E₁ and
E_B (I-3); and **half of C under a product initial state (I-5).**
Two ways remain to ask O-6's question:

- **C1 (the narrowed product-state version).** Keep the textbook past
  hypothesis (a product state). Charter only the two open directions:
  L1 for T_s > T_b, and L2 for T_s < T_b against the **reduced global
  Gibbs state**. Record I-5's two identity failures as findings.
  *What it tests:* whether the arrow, once past the switch-on slip,
  holds throughout the window, or is spoiled later by memory
  (band-edge backflow).
- **C2 (the correlated version).** Replace the product state with a
  **local perturbation of the coupled system's global Gibbs state**:
  heat or displace the system's marginal while keeping the equilibrium
  system–bath correlations. That removes the switch-on artifact at its
  source, since the interaction energy is already equilibrated. It
  needs a fresh identity check before chartering, because its t = 0⁺
  behavior is not yet derived.

**Operator's recommendation: C1**, with I-5 recorded as a first-class
finding. C1 keeps the standard past hypothesis the record has been
circling, and its open content is sharp. **The I-5 finding is already
an O-7 input:** *the textbook past hypothesis produces an
identity-forced anti-arrow at switch-on, so any arrow in this class
emerges only after a slip.* C2 is a legitimate alternative, and could
go to the successor list if the owner prefers C1.

---

**(Original §4, superseded where it conflicts.)**

## §4 (original) The owner's decision: what counts as "ordering arising through the bath"

| Option | Operationalization | Status after §2 |
|---|---|---|
| **A** | A structural state function, monotone for **all** initial states on a window | **Dead by identity (I-1):** it reduces to a conserved quantity. |
| **B** | A structural function of the **system's** state, monotone over a restricted initial class | **Dead by identity (I-2)**, even with the bath at rest, and even at N = ∞. |
| **B′** | **Partition energies** of the full state over the restricted class, pointwise | **Dead by identity (I-3).** |
| **C** | **Ensemble level:** declared product initial state (the past hypothesis made explicit as a datum), with structural batteries L1 and L2 on the window, over a growing N family | **Open.** No identity decides it. |

**Operator's recommendation: charter C, and record A, B, B′ as
identity results inside it.** The identity results are themselves
substantive for O-7:
- in a conservative split, the arrow can live **neither** in the
  system's state **nor** in pointwise energy bookkeeping;
- it can only live at the **ensemble** level, relative to a declared
  **low-correlation initial condition**.

That is the textbook thermodynamic picture, but here it is *derived*
as a constraint rather than assumed. Whether it then holds on the
window (L1, L2), or is spoiled by memory, is the one genuinely
unpredicted question left.

**Scope, if C is chosen:** one conservative harmonic class, Gaussian
ensembles, the record's coupling, the declared T_s/T_b pairs, and the
N family. **Not in scope:** anharmonic substrates, quantum chains (the
record's 7-site unitary chains), coupling-strength families
(weak-coupling/Markov limit). Those go to the successor list if the
owner wants them.

## §5 Standing

This design changes no status, touches no channel, and creates no edge
in the reversal diagnostic. Its identities are about substrate data and
initial classes, not certified property nodes. **O-2 remains open.**
