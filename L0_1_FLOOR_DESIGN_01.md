# L0-1 — THE FORMULABILITY FLOOR: DESIGN 01 (D-ORD / D-HERM / D-DET)

**Status: DESIGN — NOT A CHARTER. No instrument exists; no gate binds;
nothing here banks.** Authority: `L0_1C_OWNER_RULING_01.md` (the floor
authorized *as obligations to formulate, not as ordinary deletion
tests*), under `L0_1_NECESSITY_SWEEP_DESIGN_01.md` §4 (the three
formulability obligations) and §2 (the predicate registry). The
owner's four prohibitions bind.

**Preview discipline (the L0-1c lesson, applied at design stage):**
**no computation was run to write this document.** Every claim below
is a theorem, a definition, or a labeled hypothesis. The charters this
design feeds therefore start clean, with nothing to quarantine.

**Scope of every statement here, unless marked otherwise:** the
linear relaxational class ẋ = −Kx on a finite substrate, with kernel
k(τ) = e₁ᵀe^{−Kτ}e₁ — the record's kernel convention. Unitary quantum
generators (H Hermitian) are a different object; their non-Hermitian
and open-system (Lindblad) extensions are noted, deferred, not
designed here.

---

## §0 The question the floor asks (the owner's)

> **Can the system even be formulated without already assuming
> ordering, a generator, and determinism?**

The four certified deletions deleted properties *of a formulated system*.
The floor asks whether the formulation itself — a time parameter, a
self-adjoint generator, a deterministic update — is primitive or
derivable. The honest verdict class for any of them, until a
non-presupposing presentation *and* a battery mapping exist, is
UNFORMULABLE-YET; the design's job is to discharge that class where it
can, and to show *why* it cannot where it cannot.

## §1 The central design-stage finding: identities first

Every fork so far has found part of its content to be an identity —
L0-1a *after* its run (the exact factorization), L0-1b *before* it
(the pin-held M-lines), L0-1c at *pre-freeze review* (the
cooperativity theorem). The discovery point has been moving earlier
each time. This design moves it to the earliest point possible: before any charter,
it records the identities that would make a naive floor fork vacuous.
Six are found. Each is standard mathematics, cited, not derived by us.

**F-1 · Tree transparency (kills a naive D-HERM on the C1 chain).**
A real matrix whose off-diagonal pairs satisfy K_ij·K_ji > 0 is
similar, by a positive diagonal D, to a symmetric matrix **iff** the
products of couplings around every cycle are equal in both directions
(the Kolmogorov cycle criterion; the symmetrizability theorem). A
chain is a tree — it has no cycles — so **every** sign-consistent
non-reciprocal coupling on the C1 chain is diagonally similar to a
symmetric chain with couplings √(K_ij K_ji). Because D is diagonal,
e₁ᵀD⁻¹e^{−K′τ}De₁ = e₁ᵀe^{−K′τ}e₁: **the retained-site kernel of a
non-reciprocal chain is exactly a Hermitian chain's kernel.**
Consequence: a D-HERM fork on the C1 chain would certify survival of
every single-site predicate *by identity*. A live D-HERM requires a
substrate **with cycles carrying nonzero cycle affinity** — the ring,
or L0-1b's weighted all-pairs networks. (Sign-inconsistent pairs,
K_ij·K_ji < 0, are a separate route: they produce effectively
imaginary couplings and can make the spectrum complex; noted.)

**F-2 · The chain is its own Jacobi matrix (makes the static
positivity battery identity-grade on the anchor).** The Lanczos
recursion from e₁ tridiagonalizes K; the resulting Jacobi matrix J
encodes the spectral measure μ of the retained site, and by Favard's
theorem μ is a positive measure iff the recursion's off-diagonal
products are positive, with support in [c, ∞) iff J − cI ⪰ 0. The C1
bath is *already* tridiagonal with e₁ at its end, so J = K up to signs:
the static positivity battery, on the anchor, reads K's own couplings.
Identity-grade there; live only on substrates where Lanczos does real
work.

**F-3 · Lyapunov ordering (makes D-ORD identity-grade in gradient
classes).** For a gradient flow ẋ = −∇V (the L0-1c class and the
linear class with V = ½xᵀKx), V is strictly decreasing off
equilibria, so V **totally orders** the points of every orbit. The
orbit can be computed without a time parameter: with σ = V(x₀) − V(x),
dx/dσ = −∇V/|∇V|², and the clock is *derived*,
τ(σ) = ∫ dσ/|∇V|² — a reparametrization theorem guarantees derived τ
equals the original t exactly. So in dissipative gradient classes,
ordering is derivable from static data (V, the metric, x₀) **by
theorem**; a numerical D-ORD fork there would only instantiate it.
What is *not* derived: the orientation. V distinguishes the two ends
of the orbit structurally; calling the low-V end "later" is a one-bit
convention.

**F-4 · The recurrence obstruction (makes D-ORD genuinely hard in
conservative classes).** In a finite conservative system (the record's
Hamiltonian oscillator chains; the 7-site unitary quantum chains),
almost every orbit is recurrent (Poincaré recurrence, for the
invariant finite measure on an energy shell), and in the linear and
finite-dimensional unitary cases *every* orbit is (quasi-periodicity);
**no continuous function of state can be strictly monotone along a
recurrent orbit** —
continuity plus recurrence contradicts strict monotonicity. So in
those classes ordering is not merely unformulated but **not derivable
from state at all**; it must come from somewhere else. The record
already names where dissipation comes from in those classes: the
system/bath split and the large-N / finite-window limit (frontier F2).
Consequence, stated as a hypothesis for attack (§3): *in conservative
substrates, derived ordering is only as good as the emergent
dissipation — window-relative, and inheriting the split's derivational
status.*

**F-5 · Noise-blindness of the mean response (makes the naive D-DET
identity-grade).** For dx = −Kx dt + B dW with additive noise, the mean
obeys d⟨x⟩/dt = −K⟨x⟩ exactly: **the response kernel is independent
of the noise, whatever its strength or structure.** Deleting
determinism therefore leaves every response-kernel predicate intact
by identity. The live content of D-DET lives only in the
**correlation** object, C(τ) = e₁ᵀe^{−Kτ}Σe₁ / e₁ᵀΣe₁, where the
stationary covariance Σ is fixed by the *static* Lyapunov equation
KΣ + ΣKᵀ = Q, Q = BBᵀ.

**F-6 · The FDT-held member is identity-grade.** If Q = 2T·I and K is
symmetric, Σ = T·K⁻¹, so C(τ) ∝ Σ_k (u_k²/λ_k) e^{−λ_k τ} — positive
weights, completely monotone by identity. Primitive noise *with* the
fluctuation–dissipation relation intact certifies survival of
correlation positivity by identity; primitive noise *without* it
(e.g. site-dependent temperatures, Q = 2·diag(T_i)) makes the weights
u_k·(v_kᵀΣe₁) sign-indefinite — **that** is live.

## §2 What the identities imply — the floor's structure (a design-stage observation, not a certificate)

Stripping the identities away, the three obligations stop looking like
three unrelated questions:

| Obligation | Naive deletion | Identity that makes it vacuous | What remains genuinely live |
|---|---|---|---|
| D-HERM | non-symmetric K | F-1 (trees), F-2 | **nonzero cycle affinity** |
| D-DET | add noise | F-5, F-6 | **noise–dissipation mismatch** |
| D-ORD | remove t | F-3 (gradient classes) | **conservative/recurrent classes** (F-4) |

In the stochastic (Ornstein–Uhlenbeck) reading of the relaxational
class, cycle affinity in the generator and noise–dissipation mismatch
are the two textbook ways to break **detailed balance**; and F-3/F-4
make derivable ordering a question of **dissipation**. So the design
stage suggests — and only suggests; it is a hypothesis the charters
must attack — that **the floor's three formulability obligations reduce
to two deeper structural properties: dissipation (for ordering) and
detailed balance (for the generator and noise structure).** If that
survives, the Level-0 ledger's next rows would read against those two
properties rather than against "time," "Hermiticity," and
"determinism" as named.

## §3 The obligations, fork by fork

### D-HERM — the generator (closest to chartable)

**Formulation.** Formulable now: L0-1c's Instrument B (time-domain,
substrate-eigen-free) never presupposed symmetry. **Substrate:** a
cycle-bearing class (per F-1) — a pinned ring, or L0-1b's weighted
networks with a circulation added. **Deletion:** add an antisymmetric
circulation of strength γ around cycles, holding the symmetric part
fixed — so K_s = (K + Kᵀ)/2 is unchanged and accretivity is held.

**Identity to front-run:** with K_s ⪰ c·I held, every eigenvalue
satisfies Re λ ≥ c (numerical-range bound), and |k(τ)| ≤ ‖e^{−Kτ}‖ ≤
e^{−cτ}. **The finite-memory envelope survives by identity.** P_memory
survival would be certification-grade, like L0-1b's M-lines.

**Registry obligations (owner rulings needed before charter):**
- **R-1, the envelope comparator.** An oscillating kernel has no ln k;
  the frozen comparator would record UNDEFINED — an instrument
  artifact masquerading as necessity (prohibition 3). Proposed: apply
  the frozen comparator to E(τ) = max_{τ′ ∈ [τ, 40]} |k(τ′)|. For any
  positive decreasing k, E = k exactly, so R-1 is a **conservative
  extension** — identical on every kernel the record has certified.
- **R-4, the passivity split.** For non-normal K, "passive" splits
  into two inequivalent notions: *accretive* (K_s ⪰ 0, numerical
  range; forbids transient growth) and *spectrally stable* (Re spec ≥
  0; permits it). They coincide for symmetric K, which is why the
  record never had to choose. D-HERM must declare which one the
  passivity certificate of L0-1a referred to — the answer is
  accretive (L0-1a's K was symmetric; both hold), but the registry
  should say so before a non-normal member is read.

**Hypotheses to attack (labeled; predictions, not results):**
- **H-HERM-1:** cycle affinity — not asymmetry per se — is
  load-bearing for P_positivity (complete monotonicity); it is not
  load-bearing for P_memory (identity-held by accretivity).
- **H-HERM-2:** on a second leg that holds spectral stability but
  drops accretivity, transient growth breaks P_positivity's monotone
  half inside the window — i.e. of the two passivity notions, it is
  *accretivity* that carries positivity.

### D-DET — determinism (chartable after one registry ruling)

**Formulation.** The substrate's microscopic update carries primitive
noise; Q is a **declared substrate datum**, never constructed from K,
and **never set by importing rung2's KMS lock** — that is the design's
anti-circularity rule: the fluctuation–dissipation relation becomes a
*consistency check* on declared data, not a derivation input.
**Substrate:** the C1 chain is fine here (the deletion is in the
noise, and F-1 is irrelevant).

**Registry obligation:** **R-2, the object split.** Under determinism
the response kernel and the (normalized) correlation kernel coincide
up to FDT; without it they separate. The registry must split each
predicate into P^resp and P^corr before a stochastic member is read.
By F-5, every P^resp line is identity-grade; by F-6, every P^corr
line on an FDT-held member is identity-grade. The live members are
FDT-broken.

**Hypotheses to attack:**
- **H-DET-1:** determinism is not load-bearing for any tested
  predicate on either object while FDT holds (identity-grade — to be
  recorded as such, never as a discovery).
- **H-DET-2:** the noise–dissipation match is load-bearing for
  P_positivity^corr: site-temperature gradients make the correlation
  kernel sign-indefinite, beyond a threshold the fork maps.
  (P_memory^corr's envelope is fixed by K and survives.)

**Deferred:** multiplicative noise and nonlinear stochastic classes,
where F-5 fails (noise-induced drift moves the mean response) — the
genuinely hard D-DET, noted for a later fork.

### D-ORD — ordering (the deepest; predominantly a theorem fork)

**Formulation, three presentations:**
1. *Linear class, fully static:* the resolvent G(z) = e₁ᵀ(K+z)⁻¹e₁,
   defined by the constraint (K + z)y = e₁ — no τ anywhere. The kernel
   is recovered as G's inverse Laplace transform; τ appears only as a
   derived, labeled dual variable. The batteries have static
   counterparts: P_memory ↔ the analyticity of G for Re z > −c (gap);
   P_positivity ↔ G is a Stieltjes function ↔ positivity of the
   Jacobi/Lanczos data (Favard; F-2), numerically stable where raw
   moment-Hankel tests are not (Gershgorin bounds the spectral radius
   by 2.3 + 2 = 4.3, so the moments s_n = e₁ᵀKⁿe₁ out to the order ~46
   a 23-atom Hankel test needs span ~29 decades — useless in floating
   point, an instrument trap the charter must avoid by construction).
2. *Nonlinear gradient class:* the (V, metric, x₀) presentation with
   the σ-parametrized orbit and derived clock of F-3.
3. *Conservative class:* no static order exists (F-4); the only
   candidate route derives ordering from emergent dissipation via the
   system/bath split — inheriting that frontier's status.

**Registry obligation:** **R-3, static readings.** Accept the static
(resolvent / Jacobi) readings as theorem-equivalent operationalizations
for the linear class, alongside the trajectory-Gram reading L0-1c
used — so that a D-ORD verdict can be issued without any battery
touching τ.

**Hypothesis to attack:**
- **H-ORD:** ordering is derivable from static substrate data exactly
  in the dissipative classes; in conservative classes it is derivable
  only through emergent dissipation, and then only window-relatively.
  The "dissipative ⇒ derivable" half is F-3 (theorem); the
  "conservative ⇒ not from state" half is F-4 (theorem); the open,
  attackable content is **the window-relative derivation in a
  conservative substrate** — the one numerical fork D-ORD needs.

**Honest consequence:** most of D-ORD is a *written formulability
proof* (F-3, F-4, the resolvent presentation), not an instrument. That
proof is a legitimate floor product — it discharges UNFORMULABLE-YET
for the dissipative classes on theorem grade — and should be recorded
as a theorem document, never dressed as a run.

## §4 Proposed sequence (a recommendation; the order is the owner's)

1. **Registry rulings R-1 … R-4** (owner). All four are conservative
   extensions or disclosures; none changes any certified line.
2. **D-HERM charter** on a cycle-bearing substrate — the only floor
   fork chartable now, with its identity (the memory envelope)
   declared in advance and its live content (H-HERM-1/2) named.
3. **D-DET charter** — FDT-held member (identity) plus site-temperature
   members (live).
4. **D-ORD theorem document** for the dissipative classes, then the
   one conservative-class numerical fork (window-relative ordering via
   the split).

Each charter inherits the full house method: pre-freeze adversarial
review, frozen before instrument, single run, per-property lines never
composed, scope clause on every face, HARD STOP.

## §5 Standing

Nothing here changes a status, touches a channel, or adds to the
register. **The pin-free locality fork remains a separate unresolved
branch** (L0-1b's Outcome A undecided, not refuted). **The successor
program still owes its own termination condition** — flagged again,
because the floor is where an open-ended descent could start to run
without a stopping rule; the owner may want that condition in place
before the first floor charter freezes.
