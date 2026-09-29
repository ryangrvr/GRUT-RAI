# L0-1f — D-ORD-a THEOREM DOCUMENT 01 (obligation O-5: ordering in the dissipative classes)

**STATUS: DRAFT — pending analytic review (termination condition T1:
O-5 is a "theorem document, reviewed, not a run").** No computation was
run to write it. Every statement is a theorem (proof or standard
citation given), a definition, or a labeled hypothesis.

**Authority:** `L0_1E_OWNER_RULING_02.md` (D-ORD/O-5 authorized);
design basis `L0_1_FLOOR_DESIGN_01.md` §3 D-ORD (F-3, F-4, the
resolvent presentation); registry R-3 (static readings, theorem-
equivalent **at declared linear-class scope only**, with the owner's
qualification binding); the no-`t` rule of `LEVEL0_DIRECTION_01.md` §2
(any ordering in a Layer-0 instrument must be derived and labeled).

## §0 The obligation, and what "formulated without ordering" means here

> **Can the substrate be formulated without a primitive time
> parameter, with every ordering the batteries use *derived* from
> static substrate data and labeled as derived?**

**Two distinctions are kept separate throughout:**
- **Order vs orientation.** A *total order* on the states of an orbit
  says which state is between which. An *orientation* says which end is
  "later". The design (F-3) already noted that the orientation may be
  only a one-bit convention even when the order is derived.
- **Relaxational vs stationary.** A relaxing trajectory, whose state
  changes, is a different object from a stationary process, whose
  state statistics do not. The stationary class needs its own theorem
  (§4).

**Classes in scope (O-5):** the dissipative classes on the record.
- **𝒞₁**, the linear relaxational class ẋ = −Kx. This covers:
  - K symmetric positive definite: the sealed chain and L0-1a/b;
  - K accretive non-normal (K_s ≻ 0): the L0-1d ring members.
- **𝒞₂**, the nonlinear gradient class ẋ = −∇V (the L0-1c convex
  quartic).
- **𝒞₃**, the stationary linear-Gaussian stochastic class (L0-1e).

**Out of scope (O-6 and beyond):** the conservative classes (Hamiltonian
and unitary). Only their boundary is stated here (§5).

## §1 The static presentation of 𝒞₁ (R-3 scope)

**Theorem D-1 (static substrate data suffice for the response).** For
K ∈ 𝒞₁, the retained-site response k(τ) = e₁ᵀe^{−Kτ}e₁ is determined
uniquely by static data in any of these forms, none of which contains
a time parameter:
- (i) the resolvent G(z) = e₁ᵀ(K + zI)⁻¹e₁, defined by the linear
  constraint (K + z)y = e₁, for z outside −spec(K);
- (ii) the moments sₙ = e₁ᵀKⁿe₁, n ≤ 2d − 1, where d is the McMillan
  degree;
- (iii) for symmetric K, the Jacobi matrix from Lanczos on (K, e₁).

*Proof.* G is the Laplace transform of k on Re z > −min Re λ, and the
Laplace transform is injective, so G determines k. G is rational of
McMillan degree d, and is determined by its first 2d Taylor
coefficients at ∞, which are (−1)ⁿsₙ (Kronecker). (iii) is the Lanczos
factorization of (ii). ∎

Here τ enters only as the **dual variable of an inverse transform.** It
is a derived, labeled coordinate, not substrate data.

**Theorem D-2 (static readings of the registry batteries on 𝒞₁).**
Stated component by component, including where **no** exact static
reading exists:

| Battery | Static reading | Grade |
|---|---|---|
| P_positivity (c), CM | H₀ ≻ 0 and H₁ ≻ 0 on the moment Hankel of size d. For symmetric K, equivalently a positive Jacobi measure (Favard). | **Exact.** Already *used* on the record: L0-1d and L0-1e adjudicated CM with no τ anywhere. |
| P_positivity (a), nonnegativity | Sufficient static conditions only: −K Metzler (sign pattern), or CM. | **Sufficient only.** No exact finite static test in general. |
| P_positivity (b), monotone decrease | Sufficient static condition only: CM. | **Sufficient only.** |
| P_memory: the exponential *class* | G has no pole with nonzero residue in Re z > −c ⟺ \|k(τ)\| ≤ Ce^{−cτ}. The rate is read from the poles of G. | **Exact** for the asymptotic class. |
| P_memory: the comparator's *window grade* | **None.** It is a statement about a fit on a declared τ window. | **Stays a τ-battery**, now using a *derived* τ (D-1). |
| P_geometry | The resistance metric R_ij from L⁺ (L0-1b). | **Exact.** It never contained τ. |
| P_exact-reduction | The eigen-reduction itself. | Definitional. |

*Proof sketches.* The CM row is the finite Hamburger/Hermite and
Bernstein argument recorded in the L0-1d/e charters. The memory-class
row holds because k is a finite sum of polynomial-times-exponential
terms, whose exponents are exactly the poles of G. The (a) and (b)
rows are sufficiency only: nonnegativity of an exponential polynomial
on [0, ∞) has no finite algebraic characterization in general, and
none is claimed. ∎

**Consequence.** In 𝒞₁ the record's batteries split three ways: two
are **fully static** (CM, geometry); one is **static in its asymptotic
content** (the memory class); and two have **only sufficient static
readings** ((a), (b)). The comparator's window grade is the one reading
that stays irreducibly τ-indexed. Under D-1 its τ is derived, not
primitive, so it complies with the no-`t` rule, and its presence is
recorded.

## §2 Derived ordering on relaxing orbits (𝒞₁ and 𝒞₂)

**Theorem D-3 (strict-Lyapunov ordering).** Let ẋ = f(x) be locally
Lipschitz, with a C¹ function V satisfying V̇ = ∇V·f < 0 off equilibria
(a *strict Lyapunov function*). Then along every non-equilibrium orbit:
- (i) V is strictly decreasing, so **V totally orders the orbit's
  states**;
- (ii) the orbit is the solution of the **σ-ODE**
  dx/dσ = f(x)/(−V̇(x)), with σ = V(x₀) − V(x). This uses only static
  data (f, V, x₀) and no time parameter;
- (iii) the **derived clock** τ(σ) = ∫₀^σ dσ′/(−V̇(x(σ′))) reproduces
  the original parametrization exactly.

*Proof.* (i) is immediate. For (ii) and (iii), dσ/dt = −V̇ > 0 on the
orbit, so t ↦ σ is a C¹ diffeomorphism onto its image, and the chain
rule gives the σ-ODE and τ(σ) = t. Uniqueness for the σ-ODE follows
from local Lipschitz continuity of f/(−V̇) away from equilibria. ∎

**Instances on the record** (each V is static substrate data):

| Class | Strict Lyapunov function | Resulting σ-ODE |
|---|---|---|
| 𝒞₁, K symmetric positive definite | V = ½xᵀKx or ½\|x\|² | — |
| 𝒞₁, K accretive non-normal (the L0-1d ring) | V = ½\|x\|², since V̇ = −xᵀK_s x < 0 | dx/dσ = −Kx/(xᵀK_s x) |
| 𝒞₂, gradient flow (L0-1c) | V itself, V̇ = −\|∇V\|² | dx/dσ = −∇V/\|∇V\|²; τ = ∫dσ/\|∇V\|² |

**What is derived, and what is not.** The **order** is derived. The
**orientation** is a one-bit convention: V distinguishes the two ends
of the orbit structurally, and calling the low-V end "later" is a
labeling choice. The design recorded this at F-3, and it is restated
here as part of the theorem's face.

**The batteries under D-3 (no primitive t).** Every τ-indexed reading
used on these classes can be taken on the derived clock, because
k(τ) = x₁(σ⁻¹(τ)) along the orbit from x₀ = e₁. That includes the
comparator's window grade and the L0-1c trajectory batteries. The
derived clock is exactly the original parametrization (D-3(iii)), so
every certified reading on these classes is unchanged.

## §3 The sharpened boundary: non-recurrence, not "dissipation"

**Theorem D-4 (recurrence obstruction, general).** Let x(t) be an
orbit of a continuous flow that is **recurrent**: there exist tₙ → ∞
with x(tₙ) → x(0). Then **no continuous function of state is strictly
monotone along it.**

*Proof.* Suppose f is continuous and strictly increasing along the
orbit. For tₙ > t₁ > 0, f(x(tₙ)) > f(x(t₁)) > f(x(0)). But
f(x(tₙ)) → f(x(0)) by continuity, which contradicts the strict gap
f(x(t₁)) − f(x(0)) > 0. ∎

**Consequence (this sharpens the design's hypothesis, and is recorded
as such).** The design (§2) paired *dissipation* with derivable
ordering. D-3 and D-4 show that the property doing the work is **the
existence of a strict Lyapunov function along the orbit, equivalently
the orbit being non-recurrent.** Two cases show why:
- **A dissipative system can be obstructed.** A limit cycle attracts
  its neighbourhood and is dissipative, yet on the cycle itself the
  orbit is periodic, so D-4 forbids any state-derived order there. The
  dissipative class is therefore *not* uniformly ordering.
- **Every class currently on the record is safe.** Each has a global
  strict Lyapunov function (§2), because each is linear-accretive or
  gradient, and neither admits a limit cycle.

**Hypothesis refinement, carried to O-7 (labeled, not a result):** the
floor's "dissipation" property should be read as **"non-recurrence /
strict-Lyapunov structure"**. This matters for O-6 and O-7:
- a conservative substrate is recurrent (Poincaré);
- a dissipative substrate with recurrent attractors would be obstructed
  on them too.

## §4 The stationary class 𝒞₃: orientation exists iff detailed balance is broken

A stationary process has no relaxing orbit, so D-3 gives it nothing.
The question becomes whether the **lag** τ of its stationary
correlations carries a derivable orientation.

**Theorem D-5 (stationary arrow ⟺ broken detailed balance, OU
class).** Take the stationary Ornstein–Uhlenbeck process
dx = −Kx dt + B dW, Q = BBᵀ, with stationary covariance Σ, and its
cross-correlation matrix C(τ) = e^{−Kτ}Σ for τ ≥ 0, C(−τ) = C(τ)ᵀ.
- (i) **Every autocorrelation C_ii(τ) is even in τ.** No
  single-coordinate statistic of the stationary process can orient the
  lag.
- (ii) **C(τ) = C(τ)ᵀ for all τ ⟺ KΣ = ΣKᵀ ⟺ the process is
  reversible (detailed balance).** So the lag carries an
  observationally derivable orientation, the sign of the antisymmetric
  part of C, **if and only if detailed balance is broken.**

*Proof.* (i) C_ii(−τ) = C_ii(τ) by stationarity. For (ii):
C(τ) − C(τ)ᵀ = e^{−Kτ}Σ − Σe^{−Kᵀτ}. At first order in τ this is
−τ(KΣ − ΣKᵀ), so symmetry for all τ forces KΣ = ΣKᵀ. Conversely,
KΣ = ΣKᵀ gives Kⁿ Σ = Σ(Kᵀ)ⁿ for all n, hence e^{−Kτ}Σ = Σe^{−Kᵀτ}.
For the OU process, KΣ = ΣKᵀ is the standard detailed-balance
(reversibility) condition. ∎

**On the record:** at L0-1e's F member (KΣ = I = ΣK, reversible), the
lag is **unorientable**. At every FDT-broken member (T-11: KΣ ≠ ΣK) it
**is** orientable, but **only through cross-correlations**: the
retained-site autocorrelation L0-1e studied is even at every member,
by D-5(i).

**Consequence for the two-property hypothesis (labeled; this is O-7's
input, not a result):**
- **Relaxational order** is carried by **non-recurrence / strict
  Lyapunov structure** (D-3, D-4).
- **Stationary orientation** is carried by **broken detailed balance**
  (D-5).

These are the two properties the design named, but D-5 attaches
detailed balance to *orientation in stationarity*, not to ordering
generally. The scope is the OU class only: linear drift, additive
Gaussian noise.

## §5 What O-5 establishes, and what it hands on

- **Formulability is discharged for 𝒞₁, 𝒞₂, and 𝒞₃ as scoped.**
  - 𝒞₁ and 𝒞₂: the substrate is formulable from static data; the order
    of relaxing states is derived (D-3); every battery reading is
    either static (D-1, D-2) or taken on a derived clock (D-3).
  - 𝒞₃: whether an orientation exists is decided by a static datum,
    KΣ − ΣKᵀ (D-5). The single-site battery cannot see it (D-5(i)).
- **Where a primitive-looking element survives, it is named:**
  - the one-bit orientation convention on relaxing orbits;
  - the τ-window of the comparator grade, which is derived under D-1
    and D-3 but still a window.
- **Handed to O-6:** conservative substrates are recurrent (D-4), so no
  state-derived order exists there. Any ordering must come through
  emergent dissipation (the system/bath split, frontier F2), and would
  be **window-relative at best**. That is the one numerical question
  O-6 exists to ask.
- **Handed to O-7:** the refinement "dissipation → non-recurrence"
  (§3), and the split "order ↔ non-recurrence; stationary orientation
  ↔ broken detailed balance" (§4). Both are hypotheses for the
  synthesis.
- **Reversal diagnostic:** no property → ingredient edge is created
  here. The graph stays acyclic, and the diagnostic is neither
  supported nor refuted.

**Proposed terminal label for O-5, for the owner to assign after
review:** **DISCHARGED** for 𝒞₁, 𝒞₂, 𝒞₃ as scoped. It carries the
named residuals (orientation convention; comparator window) and the
explicit boundary (D-4) on its face.
