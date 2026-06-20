# GRUT α-ANTECEDENT FEASIBILITY — can GRUT establish the IR-carrier identification?

**Verdict: NOT-YET-FORMULATED** (kinematic identification candidate-selected; the carrier-vs-source
gap is unclosed) **+ STRUCTURALLY-BLOCKED** (the only dynamical completion route inherits the UV
no-go). Tier: **[fact]** on every load-bearing leg. The bottom-line label corrects an earlier
internal assessment's "REFUTED" *down* to the repo's own audited posture. The conditional theorem
(IF conformal mode = IR carrier THEN a/c = 1/3, Komargodski–Schwimmer / Duff) remains **proven and
untouched**. α = 1/3 stands exactly as the repo books it: the single adopted dimensionless **AXIOM**,
conditional-theorem-verified, antecedent-open.

---

## 1. Purpose & charter — the narrow question

GRUT's vacuum impedance **α = 1/3** is an **adopted axiom** resting on a **proven conditional
theorem**:

> **IF** the gravitational conformal mode is the IR carrier of the vacuum's response (the
> susceptibility χ), **THEN** a/c = 1/3 (Komargodski–Schwimmer / Duff, one real conformally-coupled
> scalar — Fraction-exact, proven). `grut/foundation/conformal_mode_scalar.py:70-91` (a/c =
> Fraction(1,3), 9/9 verify).

The **antecedent** — "the gravitational conformal mode IS the IR carrier of χ" — is **OPEN**
(`theory/GRUT_V4_CORE_CHAIN.md:116-117`, verbatim). This pass asks **only**:

> Can GRUT **establish** (or **refute**) that antecedent **from its own structure**, without
> reverse-fitting to a/c = 1/3?

NOT "is α = 1/3 right" (the conditional is proven). ONLY whether the **IR-carrier identification**
is reachable.

**Why it is the #1 gap.** α is the single open premise with the **widest fan-out** in the core chain
(`theory/GRUT_V4_CORE_CHAIN.md:118-120`). R = √(1+α), S = 12π/α², Ω_Λ = (2−R)², H_inf = (2−R)/(Sτ₀)
all carry `deps=(alpha_vac_derivation, …)`; ±0.07 in α moves Ω_Λ by ~one order. The registry books
`alpha_vac_derivation` tier=**open_negative** — *"the most load-bearing open gap in v3"*
(`grut/toe/registry.py:274`).

**The four legitimate verdicts** (and the four fail conditions that disqualify a route):

1. **REVERSE-FITTING** to a/c = 1/3 or α = 1/3 (choosing the carrier so the ratio comes out 1/3).
2. **ASSUMING THE CONCLUSION** (positing "σ is the IR carrier" as an axiom and calling it
   established).
3. **IMPORTED STRUCTURE** with no GRUT origin.
4. **SILENTLY NEEDING THE BLOCKED DYNAMICS** (using the propagating/Riegert conformal mode the UV
   no-go forbids while claiming a kinematic result).

---

## 2. The kinematic-vs-dynamic distinction — and why it decides which no-go applies

The UV-sector construction (`theory/GRUT_UV_SECTOR_CONSTRUCTION.md`, structural NO) blocked the
conformal mode as a **dynamical / propagating** field: the Riegert action's 1/k⁴ matter→metric pole
violates the locality / no-halo theorem, and the 4th-order Paneitz ghost violates Q. But the α
antecedent is a **kinematic / identification** question (is σ the IR carrier of χ?), logically
**prior to and distinct from dynamics**. The make-or-break crux:

> Does establishing "σ is the IR carrier of χ" **require** the conformal mode to be **dynamical**
> (and so inherit the UV no-go), or can it stand on a **non-dynamical / kinematic** footing (σ as
> the IR degree of freedom of the metric *response*, not a propagating excitation)?

**Resolution: there is no non-dynamical footing on which σ *carries* χ.** σ is the metric trace.
Its only **kinematic** role in GRUT's kernel is the one the tracefree projector P^TT *annihilates*
(§4, TEST A). To **carry** the matter→metric response, σ must couple to the stress trace T via the
conformal Ward identity δS_m/δσ = √g T^μ_μ (`theory/PROJECTOR_CONSISTENCY_NOGO.md` §5 step 2,
lines 163-165). That is no longer kinematically inert — it is a propagating channel, and it
reinstates the blocked Riegert dynamics (§4, Route D). **So the *dynamical-completion* route to the
identification inherits the UV no-go in full.** What that block does **not** license is the stronger
word REFUTED for the *kinematic identification itself*: the identification is currently a
**candidate** (monopole dominance), and its outstanding **non-dynamical** test — the 4th-order S⁴
Riegert/Paneitz a/c — has simply **not been computed**. That is the textbook signature of
**NOT-YET-FORMULATED with a named missing piece**, not a refutation.

---

## 3. Inventory — where χ is built, what carries it, GRUT's current α justification

**Where χ is constructed.** The CTP variation δS_CTP/δh_a yields G^(1)_μν − Φ_μν = 8πG T_μν with the
retarded constitutive kernel (`grut/derivation/phi_munu/linearized_ctp_action.py:53`, eq. 4):

> **K^R_μνρσ(ω) = α_vac · χ(ω) · P^TT_μνρσ**,  with  χ(ω) = 1/(1 − iωτ₀).

This factorizes into a **temporal** carrier χ(ω) and an **index** carrier P^TT. The IR carrier of χ
is whatever DOF P^TT projects onto.

**What carries it.** P^TT is the transverse-**tracefree** (spin-2) projector: η^μν P^TT_μνρσ = 0
(`linearized_ctp_action.py:443`), trace = 5 (the 5 tensor modes; `:477`). The conformal/trace mode
(η^μν h_μν) is **exactly what P^TT projects OUT**. This is the load-bearing kinematic fact.

**How α enters.** χ(0) = α (sympy-verified); n_g²(0) = 1 + α = 4/3 at α = 1/3. α is a **free
multiplicative DC normalization** on the tracefree kernel — an *input*, not the output of an
IR-carrier identification (`closure_protocol.py:507-524`). The conformal mode appears in the
operative χ algebra **only** in docstring/provenance comments.

**GRUT's current α justification = an explicit postulate.** The identification lives in exactly one
place, stated verbatim as a **Postulate**: `conformal_mode_scalar.py:82-108` —
*"Postulate: the gravitational conformal mode is the IR carrier of the vacuum's responsive
susceptibility"* — and then returns 1/3 *under* it. As written, that is fail-condition 2 (assuming
the conclusion). The value 1/3 is then wired into the tracefree kernel as a scalar marker
`conformal_mode_amplitude = 1/3` (`linearized_ctp_action.py:464`): the trace-sector a/c is **glued by
adoption** onto a projector that annihilates the trace mode.

**The repo's own audited posture** (the decisive context the bottom-line label must match):

| Source | Booking |
|---|---|
| `GRUT_V4_CORE_CHAIN.md:116-117` | antecedent **"OPEN"** (verbatim) |
| `GRUT_V4_CORE_CHAIN.md:168` (E4) | α→HUB **COMPUTED**, *"Inherits α's open antecedent (IR-carrier)"* |
| `GRUT_V4_CORE_CHAIN.md:172` (E8) | HUB→μ_linear=1 **SOLID** — *"P^TT annihilates the linear-scalar **response**"* (distinct edge) |
| `GRUT_SELECTION_PRINCIPLE.md:212` | conformal mode = IR carrier — **candidate-SELECTED** (monopole dominance) |
| `GRUT_SELECTION_PRINCIPLE.md:216, §6` | α value **OPEN** — *"the 4th-order S⁴ Riegert a/c (the one computation, not faked)"* |
| `registry.py:274` | `alpha_vac_derivation` tier=**open_negative**; falsifier = *"Demonstration that the gravitational conformal mode is not the IR carrier"* (**as-yet-UNMET**) |
| `closure_protocol.py:128-136` | dual-outcome fork: **derived-under-postulate OR adopted-axiom** — there is **no "refuted" branch** |

---

## 4. The routes assessed — the trace-vs-TT crux

| Route | Establishes antecedent? | Tier | Status |
|---|---|---|---|
| **K — kinematic** (σ as IR dof of metric response) | **Not yet.** Candidate-SELECTED by **monopole dominance** (`SELECTION_PRINCIPLE.md` §2: σ is the unique metric mode sourced by the stress *trace* via δS_m/δσ = T^μ_μ; TT couples to quadrupole+, IR-subdominant), then **self-demoted** to *necessary-not-sufficient* (§2 lines 35-40: *"conflates source-dominance with carrier-identity … does NOT select the carrier"*). The carrier-vs-source gap is **named and open**; the closing computation (4th-order S⁴ Riegert a/c) is **not done**. | [fact] | **NOT-YET-FORMULATED** — no reverse-fit (TEST B: 1/3 is normalization-independent, so it cannot pick the carrier); no fail-condition tripped *as a candidate*. |
| **D — dynamical** (Riegert/Paneitz σ propagates, couples to T) | **No.** σ-couples-to-T ⇒ σ(k) = T/(Q²k⁴): a 1/k⁴ matter→metric pole, strictly **worse** than the forbidden 1/k² (TEST C = ∞), in the class the locality/no-halo theorem bans (`locality_no_halo.py:7-14`); plus the 4th-order Paneitz ghost = Q-violation. The only ghost-free/locality-safe home (E₄/a) is **Lovelock-null / dormant** (`second_order_kernel.py:16-22`); the live channel is c/W² (TT). | [fact] | **STRUCTURALLY-BLOCKED** — fail-condition 4; inherits the UV no-go in full. |
| **A — anomaly-matching** (pin the carrier by anomaly equality) | **No.** Fixes the *coefficient* a/c = 1/3 (normalization-independent, TEST B) — **silent on which mode carries χ.** If pushed to a *live* carrier it collapses to Route D. | [fact] | Silent; collapses to D if made dynamical. |

**The crux, stated plainly.** The tension the charter flagged — *Φ_μν = α·χ·P^TT uses the TT
projector, which tensions with a trace-mode carrier* — is real and is the **internal inconsistency
the repo already flags** (`PROJECTOR_CONSISTENCY_NOGO.md` §3 Fact 3): the kernel multiplies a
*conformal* susceptibility by a *tracefree* projector. It does **not** by itself establish that
"χ's IR carrier is TT." What P^TT annihilates is the **linear-scalar RESPONSE to a matter source**
(edge **E8**, μ_linear=1) — a *different* proposition from "which mode is the IR carrier of χ" (edge
**E4**). The repo keeps E4 ≠ E8 deliberately. The kinematic identification therefore stands as a
**candidate**, with one named **non-dynamical** closure computation outstanding, and with its
**dynamical** completion **blocked**.

---

## 5. Adversarial results

All load-bearing algebra was re-derived from scratch in `.venv`/sympy and every file:line confirmed
by direct read. Four results:

- **TEST A — P^TT annihilates the pure-trace conformal mode.** The spin-2 TT projector applied to a
  pure-trace source δ_kl·H returns the **identically-zero matrix**. ✓ Confirms `:443` (η^μν P^TT = 0).
  *Bears on:* this is the kinematic fact behind E8 (the linear-scalar response is killed) — it is
  **not** the same as "χ's IR carrier is TT."
- **TEST B — a/c = 1/3 is normalization-independent.** (N·a)/(N·c) = 1/3 for any N; Birrell–Davies
  |Euler/Weyl| = 1/3 = KS a/c (conventions differ by 360). ✓ The value is therefore **silent on the
  carrier** and **cannot be used to pick it** — fail-condition 1 (reverse-fitting) is structurally
  **clean** on every route.
- **TEST C — the Riegert pole is strictly worse than the forbidden one.** lim_{k→0}(1/k⁴)/(1/k²) =
  ∞. ✓ The dynamical-completion route is more singular than the locality-forbidden 1/k² —
  STRUCTURALLY-BLOCKED leg confirmed.
- **TEST D — α is a free DC multiplier.** χ(0) = α; n_g²(0) = 1 + α = 4/3 at α = 1/3. ✓ α is an
  input normalization, not the output of an identification.

**The decisive adjudication (why REFUTED over-reaches).** The earlier internal assessment reached
REFUTED via: *K^R = α·χ·P^TT; P^TT annihilates the trace mode (TEST A); therefore χ's IR carrier is
TT; therefore the antecedent is false.* Steps 1–2 are correct (TEST A). The inference to REFUTED is
not — it **equivocates E8 with E4**:

- **E8 (SOLID, `:172`):** P^TT annihilates the linear-scalar **RESPONSE to matter** ⇒ μ_linear = 1
  ⇒ linear cosmology = ΛCDM. α-free, τ₀-free, structural; over-determined ~32σ by low-ℓ ISW.
- **E4 (COMPUTED-on-open-antecedent, `:168`):** which mode is the **IR carrier of χ** whose DC
  amplitude χ(0) = α drives R, S, Ω_Λ, H_inf.

"P^TT appears in the linear matter→metric kernel" entails E8. It does **not** entail "χ's IR carrier
is TT." The No-Go that does the heavy lifting (`PROJECTOR_CONSISTENCY_NOGO.md` §5 step 1, lines
160-161) **presupposes** the conformal reading: *"GRUT's foundational object is the conformal
refractive enhancement n_g²=1+α … a conformal-mode (trace) response."* It then proves only that this
conformal response cannot **also** be separate-universe invariant on linear scalars (forcing
μ_linear = 1), and **relocates the same conformal/anomaly response** to the orbital-ω χ(ω), TT, and
nonlinear W²/c-anomaly channels (§6.4). **It never identifies TT as χ's carrier.** Promoting the two
code-comment over-claims (§6 below) to a structural refutation would invert the framework's #1
load-bearing OPEN gap into a closed negative against the repo's own univocal booking
(`CORE_CHAIN:116` OPEN, `SELECTION_PRINCIPLE:212` candidate-SELECTED, `registry:274` open_negative
with an **as-yet-unmet** falsifier, and `closure_protocol:128-136` whose own fork has **no refuted
branch**).

---

## 6. Verdict & diagnosis

**Kinematic identification — NOT-YET-FORMULATED [fact].** The antecedent is *candidate-selected* by
monopole dominance, self-demoted to *necessary-not-sufficient* (the source-dominance ≠
carrier-identity trap is named in-repo), with the carrier-vs-source gap open. The single outstanding
piece is the **4th-order S⁴ Riegert/Paneitz a/c value** (`SELECTION_PRINCIPLE.md` §6, lines 243-247).
No reverse-fit is used or possible (TEST B). This is the attackable front.

**Dynamical completion — STRUCTURALLY-BLOCKED [fact].** The only route to *compute* that a/c via a
propagating σ trips the 1/k⁴ pole (TEST C) + Paneitz ghost = Q-violation; ghost-free only as a
Lovelock-null inert mode. "σ is the IR carrier" **silently needs the blocked dynamics**
(fail-condition 4) on its only completion route. The block tells you the closure computation must be
done **non-dynamically** — as an a/c *ratio* on S⁴ (the anomaly coefficient), not as a propagating
EOM. It does not say the computation is hopeless.

**Genuine, actionable findings that survive (inert — they change no computed result, because
`conformal_mode_scalar.verify()` checks the *value* 1/3, never that P^TT *yields* it):**

1. `grut/hard_theory/s4_ctp_solver/gate3_ctp_action_term_audit.py:317` — *"K^R = alpha_vac * P^TT
   projects onto S^4 conformal mode"* is **internally self-contradictory**: a tracefree P^TT
   projects onto the spin-2 sector, the **orthogonal complement** of the conformal/trace mode
   (TEST A). Reword to: P^TT carries the *tensor* response; the conformal-mode IR-carrier identity
   is a candidate postulate, not something P^TT yields.
2. `grut/foundation/closure_protocol.py:55, :108, :130` — *"the conformal mode is identified as the
   IR carrier"* asserts the antecedent more strongly than the registry/core-chain book it
   (candidate/open). Soften to the postulate standing.
3. `grut/derivation/phi_munu/linearized_ctp_action.py:85-88` docstring — claims the trace
   contraction η^μν η^ρσ P^TT *"reproduces α_vac = 1/3 / gives the 4/3 enhancement."* A tracefree
   projector's double trace is identically 0; the 1/3 at `:464` is a **hand-attached label**, not a
   contraction the kernel produces. Same internal inconsistency the No-Go already flags
   (`PROJECTOR_CONSISTENCY_NOGO.md` §3 Fact 3). Reword to surface that the trace-anomaly a/c is glued
   by adoption onto a TT kernel.

**Framing note (kept from the most careful adversary):** the situation is best described as the
**internal inconsistency** (a conformal susceptibility wired onto a tracefree projector), which the
repo *already flags* — **not** as "the carrier is provably TT." The No-Go's genuine content is that
the conformal response is **forbidden where it would be linearly testable** (μ_linear = 1), not that
χ's IR carrier is TT.

**What it means for α and the core chain.**

- **α = 1/3 keeps its conditional-theorem support.** KS/Duff is untouched; α stays the single
  adopted dimensionless **AXIOM** (`closure_protocol.py:128-136` — no "refuted" branch exists,
  consistent with this verdict). The verdict forecloses moving α **up** to "established"; it does
  **not** move it **down**.
- **The #1 gap NARROWS to one computation.** Kinematic identification candidate-selected; the single
  outstanding piece is the 4th-order S⁴ Riegert/Paneitz a/c. If = 1/3 → the keystone closes
  (monopole dominance + a/c = 1/3 + realized-structure coupling); if ≠ 1/3 → the conformal-scalar
  identification is *then* falsified.
- **The gap HARDENS into a no-go on its dynamical completion.** The *propagating* route to that same
  computation is STRUCTURALLY-BLOCKED (1/k⁴ + Paneitz ghost) — which is precisely **why** the
  closure must be done as a kinematic a/c ratio on S⁴, not a dynamical EOM.

**Net:** the #1 foundation gap does **not** close (the assessment's REFUTED over-reaches) and does
**not** stay merely open-and-undifferentiated. It resolves into: **kinematic identification =
NOT-YET-FORMULATED (candidate-selected, one named closure computation), dynamical completion =
STRUCTURALLY-BLOCKED, α = adopted axiom (unchanged).** A clean negative on the dynamical leg; an
honest open on the kinematic leg. No reverse-fitting was used or needed at any point.

---

## 7. Charge / next step

1. **Compute the 4th-order S⁴ Riegert/Paneitz a/c as a kinematic anomaly ratio** (a curved-space-QFT
   calculation, *not* a propagating EOM — that form is what dodges the STRUCTURALLY-BLOCKED leg).
   `SELECTION_PRINCIPLE.md` §6 names this exactly. Outcome = 1/3 closes the keystone; ≠ 1/3 falsifies
   the conformal-scalar identification and frees α's value. This is the single decisive front.
2. **Close the carrier-vs-source gap** in `SELECTION_PRINCIPLE.md` §2: turn monopole dominance from
   *necessary* into *sufficient*, or document why it cannot be — the named obstacle is that
   source-dominance ≠ carrier-identity.
3. **Reword the three inert over-claims** (§6 findings 1–3) to the candidate/postulate standing they
   actually hold; they currently contradict the tracefree kernel they cite, though they change no
   computed result.
4. **Keep the registry/closure_protocol booking as-is** — `alpha_vac_derivation` open_negative with
   the unmet falsifier, and the dual-outcome fork (derived-under-postulate OR adopted-axiom) are the
   correct, honest postures and match this verdict precisely.
