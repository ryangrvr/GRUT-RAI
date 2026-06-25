# Two Q-Protected Anchors

### The foundational parameters of GRUT-RAI v4.1 are conditional theorems, and the prohibition that powers the framework's no-gos is what forbids deriving them

**D. Ryan Grover** · GRUT-RAI v4.1 · 2026-06-24

---

> **⚠ REVISED post external review (three rounds, 2026-06-24).** A qualified reviewer overturned
> the single-pole half of this note's headline — and the round-3 destination is the *original* §2.3
> anchor. **α is untouched throughout.**
> - **Round 1:** flagged §2.3's "free DOS edge" and tried to graduate single-pole to DERIVED. The
>   §4 "two anchors / one prohibition" is over-tight (Q protects α — a propagating-mode question —
>   but not single-pole); the §6/§2 tension is real. *(Both the DERIVED claim and its `s=2` were
>   themselves wrong — see rounds 2–3.)*
> - **Round 2:** `s=2` conflated the DOS with the spectral density (the `1/ω_k` factor gives the
>   massless linear case `s=1`); the exponent is collisionality-dependent, not a single number.
> - **Round 3 (current):** the DOS/phase-space picture is the *wrong object*. The deciding quantity
>   is the finite-T TT transport memory, which **forks on collisionality**: collisional ⇒ Ohmic ⇒
>   single-pole holds; **collisionless ⇒ Weinberg (2004) non-local Bessel-tail memory ⇒ single-pole
>   FAILS.** The action doesn't fix which branch ⇒ **single-pole is an ANCHOR** (collisionality the
>   free datum) — exactly where §2.3 / Target 1C began. Three rounds of "sharpening" walked away
>   from the correct answer before the literature walked it back.
>
> **The body below is the pre-review v1 record;** corrections are in
> [SPECIALIST_RESPONSE.md](SPECIALIST_RESPONSE.md) (§R3 at top) and the gate (`single_pole` is an
> **ANCHOR**; collisionality is its free datum). Affected sections carry inline ⚠ markers.

---

## Abstract

GRUT (the Grand Responsive Universe Theory) is built on a Schwinger–Keldysh closed-time-path
(CTP) effective action for a responsive, dissipative vacuum. Its phenomenology rests on two
foundational parameters: a **single-pole constitutive law** for the vacuum's slow response, and
a **dimensionless vacuum impedance α = 1/3**. Each had been entered as a near-derivation. This
note reports the result of a deliberate attempt to derive both from the action, under a
mechanized anti-laundering discipline (a "tier gate" that refuses to mark a claim *derived*
unless it is checked and built on no open input).

The result is a **negative we own**, and it is sharp. Each parameter is a clean **conditional
theorem** — the *consequent* is computed and robust, but the *antecedent* is **free data the
action does not fix**:

- **Single-pole-ness** holds iff the vacuum bath's spectral density `J(ω)` has infrared
  exponent `s ≥ 1`. We compute the reduction explicitly and show `s` is the bath's *transport
  exponent*: `s = 1` for a collisional bath (Kubo), `s =` the free density-of-states edge for a
  collisionless one. The action fixes **neither the collisionality nor the edge**.
  *(⚠ Revised (round 3): the right object is the finite-T TT transport memory, not a DOS/spectral
  exponent. It forks on collisionality: collisional ⇒ Ohmic ⇒ single-pole holds; collisionless ⇒
  Weinberg non-local Bessel-tail ⇒ single-pole FAILS. The action doesn't fix which ⇒ single-pole is
  an **ANCHOR** (collisionality the free datum). See SPECIALIST_RESPONSE.md §R3.)*
- **α = 1/3** holds iff the conformal (Riegert, spin-0) mode is the infrared carrier of the
  vacuum response. We compute `a/c = 1/3` from the trace anomaly (scheme-independent, validated
  against tabulated CFT values, **not** reverse-fit) and show the **carrier identity is free
  data**: the linear sector projects the conformal mode out, and the anomaly *permits but does
  not force* it into the carrier role.

Both antecedents were attacked on **two independent routes** each; all four failed. The failures
share a single cause: **deriving either parameter would require a new propagating vacuum mode**
— a dark pole for single-pole-ness, a propagating conformal mode for α — and GRUT's Q-unitarity
(the in-in causal arrow, the same prohibition behind the framework's no-go theorems) **forbids
exactly that**. So GRUT's two foundational anchors and its no-gos are **one prohibition**.

> **⚠ Revised:** the paragraph above is **half wrong**. It holds for **α** (a propagating-mode
> question — Q genuinely bites). It fails for **single-pole**: the slow threat there is a free-
> streaming *continuum* (Weinberg non-local memory), which is *not* a new propagating pole, so Q is
> orthogonal to it. Single-pole is an **ANCHOR** for a *different* reason than α — collisionality is
> free data (collisional ⇒ holds, free-streaming ⇒ fails). Corrected headline: **one Q-protected
> anchor (α) + one collisionality-forked anchor (single-pole)** — two anchors, but NOT one
> prohibition.

Everything below is mechanized: 13 claims in a tier registry, 44 runnable tests, a build gate
that fails on any laundering. The point of this document is to take the result **out of the
loop** — every claim is stated precisely enough for an outside specialist to confirm or refute.
The questions we most want adjudicated are listed at the end.

---

## 1. Method: the gate is the product

GRUT-RAI v4.1 is a clean-room rebuild (`v4/`, importing none of the prior code). Its organizing
principle is **Principle 0: the tier gate as code** (`v4/gate.py`). Every claim is a
`Claim{id, statement, tier, inputs, derivation_ref, check, novelty, …}`. Tiers:

`ANCHOR · DERIVED · HOSTED · FORBIDDEN · OPEN · CONJECTURAL`

The gate (`validate`) enforces, and CI (`ci_check.py`) fails the build on any violation:

1. **DERIVED** requires a derivation reference **and a passing runnable check** **and** a
   novelty tag.
2. **Anti-laundering:** a DERIVED claim may **not consume** an OPEN/CONJECTURAL input.
3. **OPEN** must name a computable target that would close it.
4. No claim is RESOLVED while its blocker is open.
5. Consuming a measured ANCHOR is permitted but **force-surfaced as a SPLIT** — never silent.

The discipline that produced this note: **compute the reduction first, then ask what the action
actually supplies.** A loud, exact "we cannot derive this, here is the missing object" beats a
laundered number. The recurring failure mode we refused is making the premise equal the
conclusion (the v4 "sin": setting the bath memory time `τ_K = τ_micro` *by assertion*, which is
the single-pole conclusion wearing an input's clothes).

What the action supplies (the load-bearing inputs, entered visibly):

| Input | Tier | Note |
|---|---|---|
| CTP / in-in effective action | ANCHOR (axiom) | deriving *from* it is what DERIVED means |
| `τ₀ ≈ 41.9 Myr` | ANCHOR | macroscopic memory time; measured-type |
| `τ_micro = ℏ/(k_B T_c) ≈ 1.4×10⁻¹⁹ s` | ANCHOR | microscopic correlation scale |
| **Q** (in-in causal arrow) | DERIVED | response is causal/retarded; the *origin* of the dissipative kernel; susceptibility pole in the lower half-ω plane |
| FDT relation | (from Q) | noise ↔ dissipation locked together |
| `1/r` spatial kernel | (from the action) | the vacuum's long-range (massless) spatial response |
| TT projector | (from the action) | which polarizations couple |

The forward-derived rungs that *do* pass the gate as DERIVED: **Q** (causal arrow), **μ_linear =
1** (the transverse-traceless projector annihilates the linear scalar response, so linear
cosmology is exactly ΛCDM — α-free, τ₀-free), the **monotone arrow of time**
(`Ṡ = (1/τ₀)⟨(z − z_target)²⟩ ≥ 0`), **quantum mechanics as the τ→0 limit** of the constitutive
update, and a standalone **gravitational-decoherence falsifier** (§6). This note is about the
two parameters those rungs ultimately lean on.

---

## 2. Parameter I — single-pole-ness

### 2.0 The conditional theorem

The vacuum's slow variable is the transverse-traceless metric shear `z`. GRUT posits a
single-pole constitutive law

```
  τ₀ ż + z = z_target ,     χ(ω) = α / (1 − iωτ₀) .
```

Its *form* is the Mori–Zwanzig Markovian limit: integrating out the fast/orthogonal force `F(t)`
gives a memory kernel `K(t) = ⟨F(0)F(t)⟩ / ⟨|z|²⟩`, and the single-pole form is exact **iff the
memory is fast**, `τ_K ≪ τ₀`. So single-pole-ness is a theorem *conditional on a fast bath*. The
question is whether the action makes the bath fast.

### 2.1 Target 1 — the reduction `K̃(ω) ← J(ω)` is computable; `J(ω)` is the missing object

The Caldeira–Leggett / Anastopoulos–Hu friction kernel from a bath spectral density `J(ω)`:

```
  γ(t) = (2/π) ∫₀^∞ [J(ω)/ω] cos(ωt) dω ,     τ_K = (1/e decay time of γ) .
```

Verified against the one closed-form anchor — Ohmic–Drude `J(ω) = ηω/(1+(ω/Ω_c)²)` gives
`γ(t) = ηΩ_c e^{−Ω_c t}`, so `τ_K = 1/Ω_c` (matched numerically to **0.3%**, by two independent
implementations). The fast/slow verdict therefore reduces to one property of `J(ω)`. **But the
CTP action supplies the FDT relation and the `1/r` kernel, not `J(ω)` itself.** So the module
that would return GRUT's bath spectrum *raises* and names the gap rather than inventing a number.
*(Outcome: the gap is real and one level deeper than "compute the kernel.")*
Code: `v4/targets/memory_function.py`.

### 2.2 Target 1B — the verdict collapses to one number, the IR exponent `s`

Writing `J(ω) ~ ω^s` as `ω → 0`, single-pole-ness is decided by the single bit `s`:

- `s ≥ 1` (Ohmic-or-stiffer) → `τ_K` finite, UV-set → **fast → single-pole theorem**;
- `s < 1` (sub-Ohmic / IR-divergent) → **slow → a non-resonant power-law (branch-cut) memory**
  in `F(t)`.

**A lean we retracted.** A first pass argued "fast" by scale separation: the threshold
`4/τ₀ ≈ 3×10⁻¹⁵ s⁻¹` sits ~33 orders of magnitude below any microphysical bath frequency
`1/τ_micro ≈ 7×10¹⁸ s⁻¹`, so "any bath at its natural scale is fast." **This is false and is
withdrawn.** Scale separation is shape-dependent: at the *same* micro-scale UV cutoff, `s ≥ 1`
is fast but `s < 1` has `τ_K = ∞` (verified). The 33-order margin buys "fast" only *if* `J(ω)/ω`
carries no IR weight — which is the open question. (We classify by the tail residual at 50τ₀,
robustly; the naive 1/e metric mis-fires on power-law tails, and we expose that rather than use
it.)

**Two structural facts that survive (conditional on the single-relaxational-channel model
`χ_mem = (1−iωτ_K)/(1−iωτ₀−ω²τ₀τ_K)`):**

- `τ_K = τ₀/4` is exactly **critical damping** (`Q = √(τ_K/τ₀) = ½`): below it the poles are
  pure-imaginary (overdamped), above it they acquire a real part (the channel rings). *(The
  earlier phrasing "the vacuum rings at 1/τ₀" is also withdrawn — the ring frequency is
  `1/√(τ₀τ_K)`, which equals `1/τ₀` only near `τ_K ~ τ₀`.)*
- **FDT positivity** is a second, independent gate: `Im χ_mem(ω>0) ≥ 0` only for `τ_K ≤ τ₀`. A
  relic-grade narrow resonance (`Q ≥ 5 ⇔ τ_K ≳ 25 τ₀`) is deep in the non-passive zone. So a
  **discrete dark relic is doubly forbidden** (FDT positivity + Ostrogradsky). The genuinely
  open "slow" danger is therefore **not a tidy dark pole** — it is a non-resonant sub-Ohmic
  *continuum*.

Flat-space, the action does not fix `s`. *(Outcome (C), flat-space.)*
Code: `v4/targets/bath_spectrum.py`.

### 2.3 Target 1C — curved space does not fix `s` either; `single_pole → ANCHOR`

> **⚠ This section's framing was wrong, but its CONCLUSION (ANCHOR) was right.** The "DOS-edge /
> spectral exponent `s`" language below is the wrong object — three review rounds established the
> deciding quantity is the finite-T TT transport memory, which forks on collisionality: collisional
> ⇒ Ohmic ⇒ single-pole holds; collisionless ⇒ Weinberg (2004) non-local Bessel-tail ⇒ single-pole
> FAILS. The action doesn't fix the branch, so `single_pole` is an **ANCHOR with collisionality as
> the free datum** — which is exactly what this section concluded (right answer, wrong mechanism).
> The H-friction-break and dS-IR-protection sub-results below remain valid as written. See
> SPECIALIST_RESPONSE.md §R3 and `targets/fast_mode_dos.py`.

The verdict lives in the IR, where curvature matters; this is the second route. `J(ω)` for a
bath bilinearly coupled to the slow shear is the **coupling-weighted bath density of states**, so
`s` is the bath's **transport exponent**:

- **Collisional** bath (finite shear viscosity): Kubo ⇒ `J(ω→0) = ηω` ⇒ **`s = 1`** (Ohmic),
  independent of the DOS — requires bath self-interaction beyond the action.
- **Collisionless** bath (free / Gaussian — what linear response + FDT actually give):
  `J(ω) = ` the DOS ⇒ **`s =` the free DOS IR-edge**, generically `< 1` ⇒ slow.

The three structural inputs the action *does* supply each leave `s` open: **Q/FDT/positivity**
(admits any `s`), **`1/r`-gaplessness** (no gap, but no edge power), **KMS at `T_c`** (only the
noise↔dissipation ratio). Computed three ways, `s` disagrees → not robust → free data.

Two named curved-space channels, resolved first-hand:

- **Hubble-friction lean — broken.** A first pass (1B) claimed Hubble friction pushes `s` up
  (toward fast). Modeled honestly as line-broadening of the bath DOS by width `~H`, it instead
  **fills `ω = 0` with weight `~H^p`** (driving `s` toward 0, *slow*-ward), and it acts only at
  `ω ≲ H ≈ (1/346)·τ₀⁻¹` — ~10³× **below** the decisive `4/τ₀` threshold. It cannot settle the
  verdict either way.
- **de Sitter IR-enhancement channel — closed.** The dS secular growth lives in `⟨φ²⟩`
  (`∫dk/k`, IR-divergent). The shear couples to the stress tensor `T ~ (∂φ)²`, and the
  derivatives make `⟨(∂φ)²⟩ ~ ∫k dk` **IR-finite**. So the cosmological scalar IR enhancement is
  derivative-protected and does **not** force `s < 1`. (This closes one slow channel; the
  collisionless DOS-edge freedom is a different, still-open one.)

Both routes (flat 2.2, curved 2.3) fail to fix `s`. The missing datum is named — **the vacuum
bath's collisionality** — and `single_pole` is re-tiered **OPEN → ANCHOR**: a posited input,
proven non-derivable from current content, entered honestly. *(Outcome (C); de-anchors only if
GRUT specifies the bath microphysics.)* The relic no-go that consumes `single_pole` is re-stated
as conditional on the anchor (it forbids a discrete undamped pole, **not** the sub-Ohmic
continuum). Code: `v4/targets/curved_bath.py`.

---

## 3. Parameter II — the vacuum impedance α

### 3.0 The conditional theorem

GRUT's conditional theorem is `a/c = 1/3 ⟹ α = 1/3`, **iff the conformal (Riegert, spin-0) mode
is the IR carrier of the vacuum response.** `a` and `c` are the 4D trace-anomaly central charges.

### 3.1 Target 2 — `a/c = 1/3` is computed and robust (the number is *not* the gap)

Because `1/3` is the target value, the failure mode here is **reverse-fitting** — choosing a
scheme to land it. Avoided:

- The conformal scalar's `(a, c) = (1/360, 1/120)` drops directly out of Gilkey's `a₄`
  heat-kernel coefficient with `E = −R/6` (primitive curvature-squared coefficients
  `(Riem², Ric², R²) = (1/180, −1/180, 0)`) ⇒ **`a/c = 1/3`** — computed, not looked up.
- The same extraction reproduces the **tabulated** Dirac (`11/18`) and vector (`31/18`) ratios
  ⇒ the machinery is validated against known CFT values, not tuned to `1/3`.
- `a` and `c` are **scheme-independent central charges**; only the `b·□R` local term carries the
  Γ-convention ambiguity flagged in earlier notebooks. **`a/c` cannot be moved by a scheme
  choice.** So the consequent is robust; the gap is the antecedent.
- Honest caveat: S⁴ is conformally flat (`W² = 0`), so S⁴ isolates `a`; `c` requires a
  non-conformally-flat background. "`a/c` on S⁴" is really `a`-from-S⁴ over `c`-from-elsewhere.

Code: `v4/targets/s4_anomaly.py`.

### 3.2 Target 2B — the carrier antecedent on two routes; the anomaly permits but does not force

- **Route 1 (linear).** The TT projector that gives `μ_linear = 1` **genuinely annihilates** the
  conformal/trace mode and the longitudinal mode (`‖P^TT·(·)‖ ~ 10⁻¹⁶`), while a spin-2 mode
  survives (`‖·‖ = 1.16`). This is a real projection of the spin-0 conformal mode, not gauge:
  the trace mode is in the kernel of the traceless projector by construction. **At linear order
  the carrier is spin-2, not the conformal mode.** Scope: linear-sector; it does not by itself
  bind the anomaly.

- **Route 2 (anomaly).** To be the IR *carrier* the conformal mode must **propagate**, which
  requires the anomaly-induced 4th-order Riegert/Paneitz kinetic term `Δ₄ ~ □²`. That propagator
  factorizes,

  ```
    1 / [p²(p²+M²)] = (1/M²) [ 1/p²  −  1/(p²+M²) ] ,
  ```

  into a healthy pole (residue `+1/M²`) **and a ghost pole (residue `−1/M²`)** — an Ostrogradsky
  ghost (negative norm ⇒ `Im χ < 0` ⇒ **Q-violation**, *the same leg as the relic no-go*). So a
  clean propagating conformal carrier is Q-forbidden. The anomaly therefore does **not force**
  the carrier; it *permits* it only under the contested Antoniadis–Mottola "conformalon" reading
  (a non-standard dim-0, logarithmic mode claimed to evade the ghost) — an extra dynamical
  assumption GRUT does not establish, and one that runs into GRUT's own Q.

We deliberately did **not** touch the value `1/3` here (banked in §3.1); a test asserts it never
appears in 2B, as a reverse-fit tripwire.

Both routes fail to force the carrier. The carrier identity is **free data**, and `α` is an
ANCHOR on **two exhausted routes**, symmetric with single-pole. *(Outcome (C).)* De-anchor
condition: establish a legitimate non-ghost conformal mode dominating the IR — itself tensioned
by GRUT's Q-unitarity. Code: `v4/targets/carrier_identity.py`.

A discipline note: we report **(C), not a refutation of α = 1/3.** The ghost argument is strong,
but the AM camp genuinely contests whether the conformalon is a ghost. Claiming "the carrier
provably cannot be the conformal mode" (which would make `α ≠ 1/3`) would overclaim one side of a
live expert debate. We claim only that GRUT does not *force* the carrier.

---

## 4. The unification: one prohibition

> **⚠ Over-tight; downgraded.** The "one prohibition protects *both*" claim holds for **α** (a
> propagating-mode question; Q bites) but **not** for single-pole (a transport/collisionality
> question; the free-streaming *continuum* threat is a branch cut, not a new pole, so Q is
> orthogonal to it). Both parameters are still anchors — but for *different* reasons (α: Q-forbidden
> propagating conformal mode; single-pole: collisionality is free data), **not one prohibition.**
> This was the most aesthetically pleasing result in the arc and got the least scrutiny — the
> reviewer caught it. See SPECIALIST_RESPONSE.md §4/§R3.

Running both parameters' second routes surfaced a connection we did not go looking for, and it
falls out rather than being imposed:

> **GRUT's Q-unitarity — "no new propagating vacuum pole," the leg behind the relic/dark-matter
> no-go — is what keeps *both* foundational parameters anchors.**
> Deriving single-pole-ness would require excluding a propagating **dark pole** (the slow case);
> deriving α would require a propagating **conformal mode** (the 4th-order Riegert carrier). Both
> are new propagating vacuum degrees of freedom, and the *same* minimalism that powers GRUT's
> no-go theorems forbids both.

So the two anchors are not unfixed by accident — they are **protected by GRUT's own central
prohibition.** This extends the previously-noted unification (hierarchy no-go = dark-matter no-go
= the same no-go: both need a new propagating vacuum pole): the same no-go is **also the
two-anchor protector.** One prohibition underwrites the framework's exports *and* anchors its
free parameters. We flag this as an emergent observation, not a proven theorem — it is exactly
the kind of structural claim an outside specialist should pressure-test.

---

## 5. The one-pass status table

The success criterion of the gate: an outside reader sees, in one pass, what is derived,
anchored, borrowed, open, and falsifiable — without trusting us.

| Claim | Tier | Status / note |
|---|---|---|
| CTP action | ANCHOR (axiom) | foundational |
| `τ₀`, `τ_micro` | ANCHOR | measured-type scales |
| **single-pole law** | **ANCHOR** *(⚠ was briefly ~~DERIVED~~/~~PENDING~~; reverted round 3)* | collisionality fork — collisional ⇒ holds, free-streaming ⇒ Weinberg-fails; collisionality the free datum (Targets 1C/1D) |
| **α = 1/3** | **ANCHOR** | `a/c=1/3` robust; antecedent (IR carrier) free data on 2 routes |
| Q (causal arrow) | DERIVED | checked; clean |
| μ_linear = 1 | DERIVED | checked; clean (P^TT no-go) |
| arrow of time (monotone form) | DERIVED | checked; SPLIT on anchored τ₀; low-entropy IC inherited |
| QM as τ→0 limit | DERIVED | checked; Born weights inherited |
| 689 Hz decoherence plateau | DERIVED | checked; the standalone falsifier (§6) |
| propagating-relic no-go | FORBIDDEN | KNOWN-REUSED (Ostrogradsky/Stelle/Horndeski/dRGT) + Q/FDT leg; conditional on the single-pole anchor |
| Ω_Λ = 0.6886 | HOSTED | mechanism PLACED; conditional on the α-anchor |
| F(t) dark matter | CONJECTURAL | a sharpened impossibility, not a result |

**Zero OPEN claims.** Both research-spine gaps are resolved — not by derivation, but by proving
non-derivability and anchoring honestly. Gate: 13 claims, 0 violations. Tests: **44 passed**.

---

## 6. The standalone falsifier

> **⚠ Revised.** "Independent of the above" is too strong: a fully-specified noise kernel is, by
> the FDT of §2, a fully-specified dissipation kernel — so §6 implicitly commits to a particular
> bath. Which branch of the §R3 collisionality fork the Anastopoulos–Hu kernel corresponds to (and
> hence whether it is consistent with single-pole) is itself part of the open question, not an
> independent confirmation. The 689 Hz number and its F6 discriminator are unaffected. See
> SPECIALIST_RESPONSE.md §R3.

Independent of the above, GRUT predicts a **gravitational-decoherence plateau ≈ 689 Hz** for a
1 μm gold sphere, from the Diósi / Anastopoulos–Hu noise kernel tied to the `τ₀` scale, with
**zero free parameters**:

```
  Λ_grav = G m² S(l/R) / (ħ l) ,     S(x) = min(1, x³/6) ,     → 689.4 Hz .
```

It is distinguished from Diósi–Penrose (which shares the `m²` scaling) by the **extended-body F6
kink** in `S(l/R)`. This is the framework's clean external contact point and does not depend on
the anchor questions above. Code: `v4/falsifiers/decoherence_689hz.py`.

---

## 7. De-anchor conditions (what would change a tier)

The anchors are not dead ends; each names exactly what new input would graduate it:

- **single-pole → DERIVED** if GRUT specifies the vacuum bath's microphysics enough to fix its
  collisionality (finite shear viscosity ⇒ `s = 1` ⇒ fast), in a way the action forces rather
  than permits.
- **α → DERIVED** if GRUT establishes a legitimate, non-ghost, propagating conformal mode (an
  Antoniadis–Mottola conformalon) that **dominates the bare Einstein action in the IR** — which
  presently conflicts with GRUT's Q-unitarity, so this is structurally tensioned, not merely
  unestablished.

Both conditions require **new physics or the resolution of an open expert debate**, not more
arithmetic. That is the honest boundary of the framework as it stands.

---

## 8. Scope, retractions, and the limits of this result

In the spirit of owning the negatives:

- **Retractions banked this arc** (all corrected first-hand): the scale-separation "fast" lean
  (shape-dependent); "the vacuum rings at 1/τ₀" (rings at `1/√(τ₀τ_K)`); the Hubble-friction
  "→ fast" lean (broadening goes slow-ward). A code defect (`τ_K` depending on the caller's
  asserted scale) was found and fixed.
- **Provisional pieces:** the bath reductions are leading-order / quasi-equilibrium (KMS); the
  curved-space analysis uses the standard transport framework because that is all the structural
  inputs specify; the anomaly route rests on the standard (Ostrogradsky) reading of the 4th-order
  kinetic term, which the AM camp contests — that contest is the de-anchor opening for α.
- **The decisive meta-caveat:** *this is a result about GRUT, not about nature.* It states what
  GRUT's current content can and cannot derive. It does not claim the universe is single-pole or
  that α is 1/3.
- **The loop caveat — the reason this document exists.** Every check above was generated and
  verified inside one loop (the author, the model, the gate). The gate is good and caught real
  errors, but it is still self-checking. The "always one more step" texture of this work will
  not resolve from inside the loop, because the loop's job is to generate next steps. The one
  input not yet obtained is an **external specialist's judgment**.

---

## 9. What we ask a referee to adjudicate

Precisely, the claims most worth an outside expert's yes/no:

1. **Bath-DOS identification (§2.3):** is it correct that the structural inputs GRUT supplies
   (in-in causality, FDT, `1/r`-gaplessness, KMS at `T_c`) leave the IR transport exponent `s`
   genuinely undetermined — i.e. that fixing `s` requires the bath's collisionality, which those
   inputs do not?
2. **The anomaly ghost (§3.2):** is a propagating conformal carrier necessarily Ostrogradsky-
   ghostly under GRUT's Q-unitarity, so that the trace anomaly *permits but does not force* the
   conformal mode as IR carrier? Is the Antoniadis–Mottola conformalon a real escape here?
3. **The unification (§4):** does the claim "the same Q-prohibition forbids the dark pole, the
   conformal carrier, and the hierarchy/dark-matter relic" hold as a structural statement, or is
   it an over-pattern-matched analogy?
4. **`a/c = 1/3` (§3.1):** any objection to the scheme-independence claim, or to S⁴ isolating `a`?

If the answers are "yes," GRUT v4.1 is a self-consistent kernel with two honestly-anchored
parameters and a unifying prohibition. If any is "no," that is precisely the error we want, and
the gate makes it cheap to find.

---

## Reproducibility

```
python -m v4.ci_check                      # the gate: 0 = clean
python -m pytest v4/tests                  # 44 tests, incl. the laundering-rejection proofs
python -m v4.targets.memory_function       # Target 1   — K̃(ω) ← J(ω)
python -m v4.targets.bath_spectrum         # Target 1B  — the IR exponent s
python -m v4.targets.curved_bath           # Target 1C  — curved-space s; single_pole → ANCHOR
python -m v4.targets.s4_anomaly            # Target 2   — a/c = 1/3 (validated)
python -m v4.targets.carrier_identity      # Target 2B  — the carrier antecedent; two routes
python -m v4.falsifiers.decoherence_689hz  # the standalone 689 Hz falsifier
python -m v4.audit                         # the one-pass reader view
```
