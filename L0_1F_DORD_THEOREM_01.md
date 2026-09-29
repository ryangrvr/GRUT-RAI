# L0-1f — D-ORD-a THEOREM DOCUMENT 01 (obligation O-5: ordering in the dissipative classes)

**STATUS: REVISION 2, reviewed; one owner ruling pending (§6).**
Revision 1 (`314f2c3`) was reviewed by two analytic reviewers (proofs;
scope and honesty). Their findings are all confirmed and incorporated,
and they are recorded in `L0_1F_REVIEW_01.md`. Two were genuine
mathematical errors in revision 1, each with a counterexample, both
fixed below. No computation on any record member was run. The
reviewers' toy checks used generic small matrices and are disclosed
in the review record.

**Authority:** `L0_1E_OWNER_RULING_02.md` (D-ORD/O-5 authorized);
design basis `L0_1_FLOOR_DESIGN_01.md` §3 D-ORD; registry R-3 (static
readings are theorem-equivalent **at declared linear-class scope
only**; the owner's qualification binds: *not every time-domain
predicate is interchangeable with a static one*); the no-`t` rule of
`LEVEL0_DIRECTION_01.md` §2 (any ordering in a Layer-0 instrument must
be derived and labeled).

## §0 The obligation, the classes, and what is presupposed

> **Can the substrate be formulated without a primitive time
> parameter, with every ordering the batteries use derived from
> substrate data and labeled?**

**Stated first, because the review showed it is where the question
lives. The formulation removes a primitive time *parameter*. It does
not derive the generator.**
- In every class below, the substrate datum includes the generator:
  the vector field f, or K, or (V, metric g).
- The **magnitude** of f is exactly what the derived clock reads.
- The **sign** of f (and, in D-1, the choice of the one-sided
  transform) is what fixes which direction along an orbit is "later".
- **The generator is therefore a presupposition on this document's
  face, not something it derives.** The design's §0 names "a
  generator" as one of the floor's three primitive-looking assumptions.
  Deriving the generator itself is **not** in O-5's scope (T1: "the
  formulability proof for the dissipative classes: Lyapunov ordering;
  the linear-class static presentation"). It is added to the successor
  list as S-5.

**Classes in scope** (corrected per the review; members named):
- **𝒞₁, linear relaxational, ẋ = −Kx with −K Hurwitz:**
  - symmetric positive definite K: the sealed chain; L0-1b members;
    L0-1a's anchor and pin > 0 D-GAP members;
  - accretive non-normal K, K_s ≻ 0: the L0-1d ring members;
  - spectrally stable but non-accretive K: this covers O-2's named
    candidate, the attached directed ring.
- **Excluded from 𝒞₁ by name:**
  - L0-1a's D-GAP pin = 0 member (K positive semidefinite and singular:
    not Hurwitz);
  - L0-1a's D-PASS members with a negative spring (K indefinite: not
    dissipative).
- **𝒞₂, nonlinear gradient, ẋ = −∇_g V:** the L0-1c convex quartic,
  with data (V, the Euclidean metric g, x₀).
- **𝒞₃, the stationary linear-Gaussian class,**
  dx = −Kx dt + B dW with −K Hurwitz: L0-1e. **All variables are even
  under time reversal** (no momentum-like coordinates); that hypothesis
  is required by D-5.

**Out of scope (O-6):** conservative classes. Their boundary appears
in §3 only.

## §1 Static presentations (R-3; 𝒞₁ and 𝒞₃ only, since 𝒞₂ is nonlinear and outside R-3)

**Theorem D-1 (response, 𝒞₁).** The retained-site response
k(τ) = e₁ᵀe^{−Kτ}e₁ is determined uniquely by any of the following:
- (i) the resolvent G(z) = e₁ᵀ(K + zI)⁻¹e₁, defined by the static
  constraint (K + z)y = e₁;
- (ii) the moments s₀ … s_{2N−1} (N = dim K), where the McMillan
  degree is d = rank H_N and the first 2d moments determine G;
- (iii) for symmetric K, the Jacobi matrix from Lanczos on (K, e₁).

*Proof.* G is the Laplace transform of k on Re z > −min Re λ(K).
Laplace is injective, and G is rational, so it extends by continuation.
The expansion (K + z)⁻¹ = Σₙ(−1)ⁿKⁿz^{−n−1} gives
G = Σₙ(−1)ⁿsₙz^{−n−1}. By Kronecker, finite Hankel rank d ⟺ G is
rational of degree d. By partial realization (Ho–Kalman), 2d Markov
parameters determine G. d ≤ r ≤ N, so moments up to 2N−1 suffice to
find d. (iii) is the Lanczos factorization, which for symmetric K has
no breakdown (H₀ is a Gram matrix, so d = r). ∎

**Theorem D-1′ (correlation, 𝒞₃; added per the review).** The
stationary autocorrelation C(τ) = e₁ᵀe^{−Kτ}Σe₁ (τ ≥ 0) has Laplace
transform e₁ᵀ(K + z)⁻¹Σe₁. Σ is fixed by the static Lyapunov equation
KΣ + ΣKᵀ = Q. So C is determined by static data (K, Q, e₁) exactly as
in D-1, with moments e₁ᵀKⁿΣe₁. **Scope: second-order statistics.**
These are complete for this class, because the stationary process is
Gaussian and zero-mean and so is determined by its covariance function
(ties to successor item S-1).

**In both, τ is only the dual variable of a one-sided inverse
transform.** The half-line [0, ∞) that transform uses is where D-1
carries the orientation (§0). It is named here, not hidden.

**Theorem D-2 (static readings of the registry batteries, 𝒞₁; 𝒞₃ via
D-1′), component by component:**

| Battery | Static reading | Grade |
|---|---|---|
| P_positivity (c), CM | H₀ ≻ 0 (size d) on the moment Hankel; H₁ ≻ 0 is then automatic under accretivity. Exact on all of 𝒞₁, including non-symmetric K: complex pairs and Jordan blocks make H₀ indefinite. **On the symmetric subclass CM is identity-held** (the spectral measure is |⟨e₁, v_j⟩|² ≥ 0), so it is not a test there. | **Exact.** Used on the record for the response (L0-1d) and, via D-1′, for the correlation (L0-1e). |
| The asymptotic exponential class (**not a registry battery**) | \|k(τ)\| ≤ Ce^{−cτ} ⟺ every pole of the reduced G has Re z < −c, **or** Re z = −c and is simple. Existence of some c > 0 ⟺ every pole has Re z < 0, which is identity-held on 𝒞₁. | **Exact.** Revision 1's "no pole with nonzero residue" was **false**: see the counterexamples in the review record, including a double pole with zero residue in an accretive 3×3 K. |
| **P_memory, the registry battery** (the comparator's grade on the envelope over a declared τ window) | **None.** | **Stays τ-indexed.** Its τ is derived under D-3, which ties it to the Lyapunov-ordered orbit from e₁, not under D-1. |
| P_positivity (a), nonnegativity; (b), monotone decrease | Sufficient static conditions: −K Metzler for (a); CM for both. A necessary static condition: the dominant pole is real with a positive coefficient. | **No exact finite static test is known in general.** Continuous-time positivity of exponential polynomials is an open problem (Ouaknine–Worrell). It is decidable in special cases, e.g. real commensurate exponents without Jordan terms (via u = e^{−τ/q} and Sturm). **None is claimed here.** |
| P_geometry | The resistance metric from L⁺ (L0-1b). | **Exact.** It never contained τ. |
| P_exact-reduction | The eigen-reduction. | Definitional. |

**R-3, restated on the face:** these equivalences hold within the
declared linear classes under the stated hypotheses. **Not every
time-domain predicate has a static counterpart:** P_memory's window
grade has none, and (a) and (b) have only sufficient conditions.

## §2 Derived order on relaxing orbits (𝒞₁, 𝒞₂)

**Theorem D-3 (strict-Lyapunov order).** Let ẋ = f(x) be locally
Lipschitz, with V ∈ C¹ and V̇ = ∇V·f < 0 off equilibria. On a
non-equilibrium forward half-orbit from x₀:
- (i) V strictly decreases, so **V totally orders the orbit's states;**
- (ii) with σ = V(x₀) − V(x) ∈ [0, σ*), where
  σ* = V(x₀) − lim_{t→∞} V(x(t)), the orbit solves the σ-ODE
  dx/dσ = f(x)/(−V̇(x));
- (iii) the derived clock τ(σ) = ∫₀^σ dσ′/(−V̇(x(σ′))) reproduces t
  exactly on [0, σ*). As σ → σ*, V̇ → 0 and τ(σ) → ∞: the equilibrium
  is approached only asymptotically and is never reached.

*Proof.* (i) is immediate. For (ii) and (iii), dσ/dt = −V̇ > 0, so
t ↦ σ is a C¹ bijection onto [0, σ*), and the chain rule gives both.
**Uniqueness** (revised per the review, because revision 1's
Lipschitz argument needed V ∈ C^{1,1}): any solution y of the σ-ODE
has dV(y)/dσ = −1. Define t(σ) = ∫dσ/(−V̇(y)). Then y∘σ(t) solves
ẋ = f, so uniqueness for f transfers to y. ∎

**Instances.** Every V is exhibited, not inferred:

| Class | Strict Lyapunov function V | σ-ODE |
|---|---|---|
| 𝒞₁, K symmetric positive definite | ½xᵀKx (V̇ = −\|Kx\|²), or ½\|x\|² (V̇ = −xᵀKx) | −Kx/\|Kx\|² (first choice) |
| 𝒞₁, K accretive (K_s ≻ 0) | ½\|x\|² (V̇ = −xᵀK_s x) | −Kx/(xᵀK_s x) |
| **𝒞₁, K spectrally stable, non-accretive** (e.g. O-2's candidate) | **xᵀPx, with P ≻ 0 solving KᵀP + PK = I (Lyapunov's theorem)**, so V̇ = −\|x\|² | −Kx/\|x\|² |
| 𝒞₂, gradient in metric g | V (V̇ = −\|∇_g V\|²_g) | −∇_g V/\|∇_g V\|²_g |

(In the gradient rows the data are (V, g, x₀). The rate information
lives in g, as the design's F-3 wrote it. The ring and non-accretive
rows need the raw vector field, because those generators are not
gradients in any metric.)

**What is derived and what is not (corrected per the review):**
- The **order** is derived.
- **Which direction is "later" is carried by the sign of the
  generator f, not by the static data alone.** Reversing f forces
  V → −V.
- The two ends of an orbit are always *distinguishable* (V differs),
  but naming one of them "later" is equivalent to reading "along f" as
  forward in time. That is the one bit the design called a convention
  at F-3. It is **not** a free bit: once f is given it is fixed. It is
  the generator's sign.

**The batteries under D-3.** Take x₀ = e₁. Every τ-indexed reading on
these classes is k(τ) = x₁(σ(τ)), where σ(·) is the inverse of the
clock map τ(·). That covers the comparator's window grade and the L0-1c
trajectory batteries. Since the derived clock equals the original
parametrization, every certified reading is unchanged.

## §3 A boundary on the design's hypothesis (recorded for O-7 and the successor list; no result claimed)

**Theorem D-4 (recurrence obstruction).** Let γ be an orbit of a
continuous flow with **α(γ) ∩ ω(γ) ≠ ∅.** This includes every
recurrent orbit (x(tₙ) → x(0) with tₙ → +∞ or −∞), and every homoclinic
orbit. Then **no continuous function of state is strictly monotone
along γ.**

*Proof (monotone function written F).* Let F be continuous and
strictly increasing along γ, and let p ∈ α(γ) ∩ ω(γ). Then
F(x(t)) → F(p) both as t → −∞ and as t → +∞. A strictly increasing
function cannot have equal limits at both ends. ∎

**Corrections to revision 1** (errors, now fixed, not wording):
- **"Strict Lyapunov function, equivalently non-recurrent" was
  false.** A homoclinic orbit to a saddle is non-recurrent and still
  obstructed (by D-4 as corrected).
- The accurate statement: **D-3 is sufficient; D-4 is necessary.**
  The general boundary is Conley's fundamental theorem: a continuous
  Lyapunov function exists that strictly decreases off the
  **chain-recurrent set**. This is cited, not used here.
- The limit-cycle example needs the cycle to be **stable** (attracting).
  Orbits spiralling onto it can still be ordered; the cycle itself
  cannot.

**Scoped statements:**
- **Every dissipative *relaxational* class on the record (𝒞₁ as
  enumerated in §0, and 𝒞₂) has an exhibited global strict Lyapunov
  function** (the §2 table).
- **𝒞₃ does not order its sample paths.** Stationary OU paths are
  almost surely neighbourhood-recurrent, so by D-4's argument no state
  function strictly orders a sample path. Its ordering question is
  therefore posed at the level of law (D-5), not paths.
- **Conservative classes:** every orbit is recurrent for
  positive-definite quadratic Hamiltonians (quasi-periodicity) and for
  finite-dimensional unitary dynamics. Almost every orbit is recurrent
  on compact energy shells (Poincaré). Not every conservative system
  is recurrent (a free particle is not), so the statement is scoped,
  as the design's F-4 wrote it.

**Relation to the frozen hypothesis (DORD-5 fix).** The design's H-ORD
says ordering is derivable "*exactly* in the dissipative classes". The
stable-limit-cycle case shows that wording **fails for general
dissipative systems**. Within the record's tested classes it holds (the
§2 table). **The frozen hypothesis wording for O-7 is unchanged.**
Revision 1's proposed re-reading ("dissipation → non-recurrence";
"detailed balance → stationary orientation") is **withdrawn from this
document** and recorded as successor item **S-4**, for O-7 or the
Level-0 synthesis to consider. Re-wording a frozen hypothesis requires
an owner ruling (T4).

## §4 The stationary class 𝒞₃: when can the lag directions be told apart?

**Theorem D-5 (OU, all variables even under time reversal).** Let
C(τ) = E[x(t+τ)x(t)ᵀ] = e^{−Kτ}Σ for τ ≥ 0, with C(−τ) = C(τ)ᵀ.
- (i) Every autocorrelation C_ii is even. Moreover, **any scalar
  linear readout cᵀx is reversible in law:** a stationary zero-mean
  Gaussian scalar process is determined by its autocovariance, which is
  even. So **no single-channel observation can tell the lag directions
  apart. At least two jointly observed channels are needed.**
- (ii) C(τ) = C(τ)ᵀ for all τ ⟺ KΣ = ΣKᵀ ⟺ the process is reversible
  in law (detailed balance for even variables).

*Proof.* (i) follows from stationarity plus Gaussian determinacy. For
(ii): C(τ) − C(τ)ᵀ = −τ(KΣ − ΣKᵀ) + O(τ²), which gives necessity.
KΣ = ΣKᵀ implies KⁿΣ = Σ(Kᵀ)ⁿ by induction, hence e^{−Kτ}Σ is
symmetric, which gives sufficiency. For a Gaussian stationary Markov
process, reversibility in law ⟺ C(−τ) = C(τ). ∎

**Framing aligned with §2 (DORD-2 fix).** D-5 decides whether the two
lag directions are **statically distinguishable**: exactly when
KΣ ≠ ΣKᵀ, a static datum. **Naming one of them "forward" is the same
one-bit reading as in §2.** The real contrast between the classes is
this. On a relaxing orbit (𝒞₁, 𝒞₂) the two directions are *always*
distinguishable. In a reversible stationary process (𝒞₃ with
KΣ = ΣKᵀ) they are distinguishable *by nothing at all*.
- **On the record:** L0-1e's F member is indistinguishable in both lag
  directions. Its FDT-broken members are distinguishable only through
  cross-correlations. The retained-site autocorrelation L0-1e studied
  is even at every member, by (i).
- **Scope:** if momentum-like (odd) variables are present, detailed
  balance becomes C(τ) = εC(τ)ᵀε, and (ii) changes. This must be
  restated before any reuse beyond even variables.

## §5 What O-5 establishes, and what it hands on

- **Formulable without a primitive time parameter, for 𝒞₁, 𝒞₂, 𝒞₃ as
  scoped:**
  - static presentations: D-1 for 𝒞₁, D-1′ for 𝒞₃;
  - derived order on relaxing orbits: D-3, for 𝒞₁ (every spectrally
    stable member) and 𝒞₂;
  - static distinguishability of the lag directions in 𝒞₃: D-5.
- **Presupposed, on the face:**
  - **the generator** (f, K, or (V, g)), whose magnitude gives the
    derived clock;
  - **the orientation bit** ("later" = along f; the one-sided
    transform), which the generator's sign carries.
  - Named residual: P_memory's comparator window, τ-indexed through
    D-3's derived clock.
- **Handed to O-6 (reworded per the review; nothing prejudged):** by
  D-4 plus quasi-periodicity or Poincaré, no continuous function of the
  full state is strictly monotone along the conservative classes'
  orbits. So at finite N any state-derived monotonicity is at best
  window-limited. **Whether emergent dissipation through the
  system/bath split supplies an ordering, and how, is H-ORD, O-6's
  hypothesis, untested here.**
- **Reversal diagnostic (DORD-8 fix):**
  - D-3 and D-5 are theorems about **substrate data** (V, g, K, Σ,
    KΣ − ΣKᵀ), not certified property nodes.
  - Cross-correlation antisymmetry is **not** a registry predicate.
  - **Owner acceptance of O-5 may not be cited as certifying any edge**
    in the diagnostic's graph. The graph stays acyclic, and the
    diagnostic is neither supported nor refuted.

## §6 The ruling O-5's label depends on (put to the owner explicitly)

> **Does an order that is derived from substrate data, with its
> orientation carried by the sign of the (presupposed) generator and
> labeled as such, satisfy the no-`t` rule's "derived and labeled"?**

- **If yes: O-5 = DISCHARGED** for 𝒞₁, 𝒞₂, 𝒞₃ as scoped. The face
  carries the generator presupposition and the orientation carrier.
  The question of deriving the generator itself is S-5.
- **If no: O-5 = UNFORMULABLE-WITH-DOCUMENTED-REASON.** The documented
  reason: *the orientation of the derived order is carried by the sign
  of the generator, not by static substrate data; within these classes
  no generator-free presentation fixes it* (D-3 and D-5 framing).

**Operator's recommendation: yes, and so DISCHARGED.** Two reasons:
- The no-`t` rule targets a **primitive time parameter**, and D-1, D-3
  and D-5 remove it.
- The generator is not a time parameter. It is substrate structure, of
  the same kind the floor has been deleting and holding throughout
  (D-HERM tested its self-adjointness; it did not dispense with it).

What the "no" branch would really be recording is the absence of a
**generator-free** formulation. That is a deeper and separate question
(S-5), not a failure of O-5 as T1 posed it. Either ruling is honest.
What would *not* be honest is leaving the generator unmentioned, as
revision 1 did.
