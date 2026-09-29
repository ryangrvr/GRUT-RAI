# L0-1e — PRE-FREEZE DESIGN REVIEW 01 + OWNER DECISION MEMO (freeze held)

**Date:** 2026-09-29 · **Object:** the L0-1e (D-DET) charter draft
(`5c71374`) · **Method:** three independent analytic-only reviewers
(method/termination compliance; mathematics; registry/honesty). No
member covariance, weight, moment, kernel, Hankel matrix, or spectrum
was computed by any reviewer or by the operator. The toy numerics were
on non-member matrices of size ≤ 4, and are disclosed. **Nothing is
quarantined.**

**Status: FREEZE HELD.** The review changed what this fork *is*. Two
framing decisions now belong to the owner (§3), so the charter stays
draft until the owner rules. Mechanical fixes are listed in §2, and
they will be applied in whichever form the owner chooses.

## 1. The findings that change the fork

**(A) The fork is decidable in closed form. Nothing in it is
genuinely unpredicted; it is "not pre-evaluated, by discipline".**
(Mathematics reviewer; confirmed by operator derivation.)
- K_b = 0.3I plus a Dirichlet–Neumann path, so
  **λ_k = 2.3 − 2cos((2k−1)π/47)** and v_k(i) ∝ sin((2k−1)iπ/47).
  Every correlation weight w_k(T) = 2u_k Σ_j T_j v_k(j)[(K+λ_k)⁻¹]_{j1}
  is a closed-form trig sum. Every member's CM status is therefore
  analytically decidable.
- **The odd-moment hierarchy (a new identity).** The Lyapunov equation
  gives m_{2j+1} as an exact linear form in T₁ … T_{j+1}. The
  coefficient on the farthest temperature is (−1)ʲ·ΠK²_{i,i+1}:
  - m₁ = T₁
  - m₃ = (a² + 2b²)T₁ − b²T₂
  - m₅ = (a⁴ + 8a²b² + 5b⁴)T₁ − (2a²b² + 4b⁴)T₂ + b⁴T₃

  All three were toy-verified. CM requires every odd moment to be
  positive. **Physically: correlation CM at a site is gated by a
  near-to-far hierarchy of temperature conditions; the retained site's
  own temperature enters first, and distant sites enter only at high
  order.**
- **Consequence: D-3 is vacuous.** On the ramp,
  m₃ = s₂ − b²(R−1)/22 < 0 at R = 1000, so G(1000) breaches **by
  identity**. My second attackable gate turned out to be as vacuous as
  the first-draft gate I had already disclosed.
- **Perron (identity):** w₁(T) > 0 for every nonzero T ≥ 0. Breaches
  can only occur in modes k ≥ 2, so the slow tail is always positive.
- **Retained-site heating (identity):** T = e₁ gives
  C(τ) = 2∫k(τ+s)k(s)ds, which lies in the cone interior. Every profile
  aU + bδ₁ is CM at every strength.
- **GR(∞) = U − G(∞) = G(0).** The reversed ramp is the ramp line
  continued below R = 1, so "orientation" is **not** a second axis.
  D-1 and D-3 are the two exit points of one line through the cone.
  D-1 passes every odd-moment necessary condition and is still open,
  but it is decidable in closed form. A sufficient route: GR(∞) is in
  the cone if every step profile 1_{[1..m]} is.

**(B) The fork cannot test whether noise is *primitive*.** (Registry
reviewer.) In the linear-Gaussian class, C(τ) = e₁ᵀe^{−Kτ}Σe₁ also
arises from:
- a **deterministic** linear flow started from a Gaussian initial
  ensemble N(0, Σ);
- a deterministic Hamiltonian dilation: a Ford–Kac–Mazur-type bath
  with thermal initial data at per-site temperatures.

So **no second-order battery in this class can separate primitive
stochasticity from derived stochasticity.** The lines certify
properties of the declared (K, Q) pair, not of noise being primitive.
RC-7, which checks KΣ ≠ ΣK, tests the FDT / detailed-balance break,
not the removal of determinism: determinism is equally absent at F,
where KΣ = ΣK.

**(C) O-4's terminal label is fixed by identities before the run.**
(Registry and method reviewers.) RC-6 (F interior) and RC-12 (the
T₁ = 0 shapes, and now G(1000)) already imply CLASS-SPLIT. No run
outcome can change the label; the run moves only face text.

**(D) The O-7 input that matters most is already theorem-grade.**
(Registry reviewer.) The cone interior means **broken detailed balance
via the noise is not sufficient to break correlation CM.** It survives
an open neighbourhood of FDT, and response CM is untouched (F-5). In
O-1, generator-side affinity broke response CM at every declared
γ > 0. That contrast holds **across object (correlation vs response),
substrate (chain vs ring), and route (Q vs K)**. It is not a universal
statement, and it must not be phrased as "detailed balance is not
fundamental".

## 2. Mechanical defects (confirmed; applied in any chosen form)

| # | Defect | Fix |
|---|---|---|
| Routing (blocker, 2 reviewers) | PARTIAL ("any other non-RC failure") swallowed the D-outcomes and outranked them. An M-1 comparator note would have used up both re-charters. | PARTIAL is defined exhaustively and never triggered by a D-gate. An M-1 failure is a per-member COMPARATOR-LIMITATION note on the memory line only. "Composes no lines **and suppresses none**" is restored. |
| Label table (blocker) | The O-3 rows overlapped, so the table was not a function. | O-3 is keyed only to F's controls and RC-1. What happens under a HALT caused elsewhere is stated. |
| Cone consistency | The identity ordering along each ray (the CM set is an interval [1, R*]) was not halt-grade. | RC-13: exact statuses are monotone along each ray, and the limit shape fails ⇒ large R fails. Exact prevails over the float R*. |
| Boundary / interval | "CM for R < R*" should read **R ≤ R***. The THRESHOLD-SHIFTED face stated its interval backwards. | Corrected. |
| Scaling | mₙ(K) was undefined while the moments are M-scaled; a literal implementation would HALT a correct run. | Both forms stated: m₁(M) = 10·T₁ and mₙ(M) = 10·s_{n−1}(M). s₀ … s₄₆ are computed. |
| O-3 coverage | P_memory^corr at F was routed to an O-4 line; component (b) at F was unnamed; "FDT relation" was listed as a component. | M-1 at F moves to an O-3 line. (b) at F is identity (CM ⇒ monotone). The FDT relation becomes a consistency note, not a component. |
| Overreach | The L-4 headline generalized one shape to "heating preserves at every strength"; the table's subclass wording depended on the result. | Scoped to the declared shapes. The subclasses are outcome-independent and name their certifying members. |
| L-3 attribution | The identity breach is caused by a noise-free *retained coordinate*, a determinism-flavoured mechanism, not by "mismatch". | Both readings go on the face. "Mismatch" is reserved for breaches with T₁ > 0. |
| Battery compliance | It was not shown that Instrument B does not presuppose determinism. | Cite the regression theorem: the conditional mean of a linear drift with additive noise equals e^{−Kτ}x. |
| Minor | RC-1 is not an "instantiation" of F-5; §3.8 misfiled numerical controls as identities; the anti-circularity rule is unenforced; no RC for the exponential bound; the timing record was not auditable. | All fixed. The timing script is archived as `calc/feasibility/l01e_lyapunov_timing_nonmember.py`, with its only output (residual, wall time, digits). It **preceded the first draft** and printed no weight, CM status, or kernel. |

Reviewer question answered: the timing *was* a 276-unknown elimination
with sparse-row skipping, about 1 s. The claim stands.

## 3. The two decisions that belong to the owner

**Decision 1: what O-3 records.**
- **(1a) DISCHARGED, at identity-grade, for the predicate question.**
  Determinism is not load-bearing for any tested predicate on either
  object while FDT holds (theorem F-5 plus the FDT identities). The
  **primitivity** question goes on the successor list as a documented
  limit of the linear-Gaussian class. In nonlinear or multiplicative
  classes, noise-induced drift can separate primitive from derived
  noise.
- **(1b) UNFORMULABLE-WITH-DOCUMENTED-REASON**, with the dilation /
  initial-ensemble equivalence as the documented impossibility: *in
  the linear-Gaussian class, primitive stochasticity is observationally
  equivalent to deterministic dynamics at second order.*

**Operator's recommendation: (1a).** The floor obligation O-3 was
written as a predicate question ("determinism with FDT held"), and
(1a) answers exactly that. (1b)'s content is real, but it belongs to a
*different* question: whether determinism is primitive, which the
design routed to D-ORD's style of formulability treatment. Recording
it as UNFORMULABLE would close O-3 on a question it was never asked.
It should be preserved on the successor list with the equivalence
theorem attached.

**Decision 2: how O-4 is completed.**
- **(2a) Theorem document with an exact computational appendix.** The
  cone theorem, the odd-moment hierarchy, the zero-temperature and
  G(1000) identities, and the closed-form weights are all stated. The
  appendix then **evaluates** the closed-form statuses of all declared
  shapes exactly: GR(∞), G(2), G(10), G(100), the thresholds R* per
  family, and H(1000). **Nothing is gated, because nothing is open in
  the adjudicative sense;** every number is an exact evaluation of a
  declared formula. The appendix's list of quantities is frozen before
  evaluation. That preserves pre-registration without pretending to an
  uncertainty that does not exist.
- **(2b) Keep the run form.** Re-gate on the still-unevaluated items
  (D-1 GR(∞); a threshold gate at G(100) or G(10)), labeled honestly as
  "decidable in closed form, not pre-evaluated by discipline."

**Operator's recommendation: (2a).** After two rounds of identity
front-running, every gate this fork could hold is either already an
identity or a closed-form evaluation someone has chosen not to do yet.
Gating "not yet evaluated" would dress arithmetic up as prediction,
the prohibition-4 pattern. The honest product is a theorem document
whose exact appendix gives the maps. This mirrors O-5, the model the
owner already set for D-ORD. The appendix's instrument is the exact
machinery already built for L0-1d, so nothing new is needed.

**Either way:** the O-4 label (CLASS-SPLIT) is identity-determined and
is recorded as such. The O-7 input in §1(D) is carried forward,
scoped.

## 4. Standing

No channel moves. L0-1e is not frozen, not run, and banks nothing.
O-1 is terminal (CLASS-SPLIT); O-2, O-5, O-6 and O-7 are unchanged.
