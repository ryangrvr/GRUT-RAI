# GRUT UV-Sector Construction — Scoping the Missing Dynamics

**Status: POSTULATED-CONSTRUCTION SCOPING DOCUMENT. Verdict: structural NO.**
This is not a derivation. It is the honest scoping of whether a UV-dynamical
sector can be *built* inside GRUT, and the answer it reaches is negative. That
negative is the deliverable.

Companion to: `theory/GRUT_UV_ANCHOR_FEASIBILITY.md` (commit 11aae02,
"NOT-YET-FORMULATED"), `theory/GRUT_HIERARCHY_LEDGER.md`. This document upgrades
that "not-yet-formulated" to a *structural* NO: the missing machinery cannot be
supplied from GRUT's own content without fracturing the framework.

Tiering used throughout: **[fact]** = in the repo / standard QFT, verified;
**[reading]** = interpretation of repo intent; **[open]** = genuinely
unresolved. Every load-bearing claim is anchored to a file:line that was Read,
and every algebraic step was re-checked in `.venv` (sympy).

---

## 1. PURPOSE & CHARTER

### 1.1 What is being scoped

The hierarchy ledger establishes that GRUT's 34-order τ₀/τ_micro gap reduces to
exactly two anchored numbers (τ₀, T_c) plus the orthogonal α = 1/3. The charge
to a future derivation was: force `ln(τ_micro/t_P) = 56.21` from GRUT structure
via Coleman–Weinberg / dimensional transmutation — **never** by tuning, never
through 8π². The feasibility pass returned NOT-YET-FORMULATED because GRUT lacks
three dynamical ingredients:

  (a) a condensing scale-invariant scalar,
  (b) a GRUT-origin running coupling g(μ) anchored at t_P,
  (c) the dynamics to deploy its anomaly coefficient.

This document scopes **building that machinery as a postulated extension**: write
down the minimal UV-dynamical sector — a scale-invariant action for the conformal
mode σ (or a minimal new micro scalar), a GRUT-origin running coupling with a
β-function, and a t_P boundary condition — and determine whether such a sector
can be **constructed self-consistently within GRUT**.

### 1.2 The success standard (unusual — read carefully)

**SUCCESS = a self-consistent postulated sector**, one that simultaneously:

  - respects **Q** (CTP/in-in unitarity: the influence action must vanish on the
    Keldysh diagonal, S_IF[φ₊=φ₋]=0 — a proven theorem of the formalism,
    non-negotiable);
  - respects the **LOCALITY / NO-HALO theorem** (`locality_no_halo.py`): a local,
    causal kernel cannot contain a 1/∇² inverse-Laplacian — the same locality
    that fixes L₀;
  - does **NOT break banked v3** (μ_linear = 1 / D = 1.0 ΛCDM linear growth; the
    single-pole finite memory F; Ω_Λ = (2−R)²; the τ₀ scale RG-protected in the
    IR);
  - is **Ostrogradsky-stable** (any higher-derivative action must be shown
    ghost-free, or the ghost must be addressed);
  - uses **ONLY GRUT-origin structure** (the genuine trace-anomaly coefficients
    a, c; the conformal mode; the CTP action) — not imported / tuned numbers.

**SUCCESS IS NOT "we got 56.21."** The number 56.21 (equivalently k_B T_c = 4.71
keV, τ_micro, T_c) is **forbidden as a target.**

### 1.3 The four fail conditions (still in force, non-negotiable)

A construction is **disqualified** if it trips any of:

  1. **Reverse-engineering from 56.21** — choosing a coupling/coefficient so the
     log comes out ~56. Forbidden.
  2. **Any appearance of 78.23 / ln(τ₀/τ_micro) / 8π² ≈ 78.96 / the ratio
     9.47e33** as input or result. Forbidden.
  3. **Any use of τ₀ / L₀ = cτ₀ / H₀ / τ_Λ / μ₀ / a₀** — the construction must be
     BLIND to the gravitational-IR scale; it lives entirely in the UV/micro
     sector. (α = 1/3 and the anomaly coefficients a, c are micro/structural and
     ALLOWED.) Forbidden to use τ₀.
  4. **Imported coefficients** with no GRUT origin (8π², arbitrary instanton
     actions, tuned β-coefficients, PDG SM couplings as the mechanism).
     Forbidden.

A clean negative — "no self-consistent sector can be built without violating
locality or Q" — is a **first-class result**. This document reaches it.

---

## 2. THE SUBSTRATE — what GRUT structures the sector is built from

### 2.1 The conformal mode and its anomaly coefficients (the legitimate source) [fact]

GRUT computes the genuine trace-anomaly coefficients but only as **numbers, not
yet as dynamics.**

  - `grut/foundation/conformal_mode_scalar.py:47-63` — per-species
    Knizhnik–Polyakov–Zamolodchikov / Christensen–Duff coefficients: real scalar
    (a, c) = (1, 3). The module computes ratios only; there is no σ field, no σ
    action, no propagator. It is a fraction calculator.
  - `grut/foundation/anomaly_derived.py:46` — the same physics in
    Birrell–Davies normalization, verbatim:
    `<T^mu_mu> = (1/16pi^2) [ a F + b G + c Box R ]`, with scalar
    (a, b, c) = (1/120, −1/360, 1/180) at lines 55-59 (`COEFF_SCALAR`).

**The ratio a/c = 1/3 is convention-independent** (verified, sympy):

```
KS a/c = 1/3 ;  BD |Euler/Weyl| = |(−1/360)/(1/120)| = 1/3
KS_a == 360·|BD_euler| : True ;  KS_c == 360·BD_weyl : True
```

The two normalizations differ only by a common factor of 360 — so 1/3 is the
**strongest GRUT-origin number available**, and the legitimate non-imported
source for a Riegert/Wess–Zumino σ action. This is the route the charter names.

The normalization 1/(16π²) (anomaly_derived.py:46) is the **standard QFT anomaly
prefactor**, genuine GRUT structure, and is explicitly *not* the forbidden
8π² ≈ 78.96. (Verified: 16π² = 157.91, 8π² = 78.96 — distinct objects.)

### 2.2 The decisive structural seam: where the Riegert action lives vs. where GRUT has dynamics [fact]

This is the single most important fact in the substrate, and it determines the
verdict. From `grut/derivation/phi_munu/second_order_kernel.py:16-22` (STAGE A,
verbatim):

  - **W² (the c-anomaly) is the UNIQUE dynamically-active O(2) operator**
    (W̄ = 0 on FRW ⇒ δW² = O(h²) escapes the linear-scalar No-Go).
  - **E₄ (the a-anomaly / Euler density) is "TOPOLOGICALLY DORMANT —
    Lovelock-null in 4D (no local dynamics)."**
  - R², R_μν², □R are **FORBIDDEN** because they "couple to the T-trace ⇒
    first-order scalar response ⇒ violate μ_linear = 1."

The Riegert / Antoniadis–Mottola conformal-mode action is built on **E₄ and the
a-coefficient** — exactly the dormant one — while every *live* GRUT dynamic (the
dark sector, the kernel) lives in the **c / W² channel.** This is the **locality–
dynamics fork**, and it is internal to GRUT, not an imported limitation.

### 2.3 The exact locality / no-halo theorem and its scope [fact]

`grut/derivation/phi_munu/locality_no_halo.py:7-14`, verbatim:

> "THEOREM (spectral). A GRUT dark-sector response that is covariant, local in
> the matter fields (a kernel analytic — entire, pole-free — in k² near k=0),
> and nonlinear (No-Go) is no more spatially extended than its baryon source. An
> extended halo … requires the response to be SINGULAR at k=0 (a pole /
> inverse-Laplacian 1/∇²). Locality forbids that singularity. Hence … a derived
> dark sector requires a NEW POLE in the vacuum spectrum (a new propagating
> mode), not a new operator."

**Exact scope** (not a blanket ban on all nonlocality): it forbids one specific
object — a 1/k² pole at k = 0 **in the matter→metric response kernel**
(`g = ∇(1/∇²)ρ`, line 19-20). It permits a kernel analytic (polynomial) in k²
near k = 0. GRUT's actual kernel σ·α·χ(ω)·P^TT is on the permitted side
(lines 78-89). The theorem says nothing, a priori, about a pole in a sector's
*internal* propagator that never feeds a matter-source response — that is the
narrow window any construction must try to exploit.

`second_order_kernel.py:67-70` already states the prior verbatim: "Shallowing
1/r⁴ → 1/r² would REQUIRE 1/∇², which the same locality result that fixes L = L₀
forbids."

### 2.4 The RG-protection / firewall statement and its scope [fact]

`grut/derived/cmb/boltzmann_consistency.py:43-45`, verbatim:

> "the modification is entirely IR (τ_0 c ≈ 12.85 Mpc). UV RG flow cannot
> generate operators at this IR scale from UV physics without a new UV
> threshold."

**Two-edged for the construction. [reading]** Favorable: it is a *directional*
firewall — UV physics cannot reach down and generate the IR τ₀ operator, so by
the same logic the IR τ₀ scale does not constrain a UV sector. The UV/micro
sector is left **free to run**, and the required blindness to τ₀ (fail-3) is
*implied by*, not merely consistent with, this firewall. A UV sector that
respected τ₀ would *violate* the firewall by introducing the forbidden shared
threshold. Teeth: the new sector must **decouple above the IR** and introduce **no
new UV threshold** that lets UV flow regenerate τ₀-scale operators, or it breaks
banked v3.

### 2.5 The Q / S_IF-diagonal constraint applied to a new σ action [fact + standard CTP]

`grut/derivation/phi_munu/linearized_ctp_action.py:304-309` — the existing
influence terms `S_const = −½ h_a K^R h_r` and `S_noise = (i/2) h_a N h_a` are
each built on `h_a = h₊ − h₋`, so `S_IF[h₊=h₋] = 0` holds by antisymmetric
construction, for any sign of N. A new σ sector must be writable in the same
Keldysh-doubled, h_a/σ_a-anchored form. **The Ostrogradsky/ghost issue is a Q
issue, not a separate one:** a non-unitary (ghost-carrying) kernel cannot be cast
as a valid CTP influence action with an FDT-positive noise kernel. "Address the
ghost" and "respect Q" are the **same gate.** [reading, tightly grounded]

The 4th-order Riegert/Paneitz closure is **flagged OPEN** in the repo:
`grut/foundation/closure_protocol.py:131-133`, verbatim — "the gravitational
conformal mode is 4th-order (Riegert/Paneitz) and that closure is OPEN."

---

## 3. THE CONSTRUCTION(S) — the candidate sectors and the three angles tried

Three independent design angles were worked, each fully, each verified in sympy.
All three reach `honest_tier = fails`.

### 3.1 Angle 1 — the Riegert / Antoniadis–Mottola conformal mode (the genuine GRUT-origin route)

Make the gravitational conformal mode σ dynamical via the anomaly-induced
Wess–Zumino (Riegert) action; physical metric g_μν = e^{2σ} ḡ_μν. Flat-background
reduction:

```
S_anom = −(Q²/16π²) ∫ √ḡ [ σ Δ₄ σ + (E₄ − (2/3)□R) σ ]
```

where Δ₄ is the 4th-order Paneitz operator (flat-space symbol □² → k⁴, verified
in sympy). **The coefficient Q² is the genuine GRUT-origin number** — built from
the per-species anomaly coefficients GRUT already computes (a/c = 1/3,
convention-independent; §2.1). This is the one part of the construction that is
legitimately, non-importedly GRUT-sourced.

**Critical structural defect:** the action is **Gaussian** (free, 4th-order) in
σ at leading order. There is no scale-invariant potential V(σ) (no λσ⁴, no
condensing direction). The Wess–Zumino structure is fixed by anomaly matching; it
contains no self-interaction that could condense. The shape required for
Coleman–Weinberg is absent.

  - **Running coupling: NONE.** The coefficient Q² ∝ (GRUT's anomaly number) is
    one-loop-exact (a cohomological Wess–Zumino-consistency quantity), so β = 0
    for it by construction. The σ kinetic term is Gaussian — no self-coupling to
    run. Fabricating a g(μ) + β-coefficient to drive transmutation would be an
    imported coefficient (fail-4) and, if tuned to make the log ~56,
    reverse-engineering (fail-1). **GRUT's anomaly structure does not contain a
    running coupling.**
  - **t_P boundary:** formally statable — σ(t_P) = 0 (physical metric = bare
    metric at Planck time), blind to τ₀/L₀/H₀ (fail-3 respected, and *natural*
    under the firewall, §2.4). But **inert**: a Gaussian 4th-order free field with
    no running coupling has no RG trajectory to integrate from t_P. Well-posed,
    vacuous.

### 3.2 Angle 2 — a minimal new local scalar (the foil)

A new local 2nd-order scalar φ with classically scale-invariant λφ⁴ and conformal
coupling ξφ²R, ξ = 1/6:

```
S[φ] = ∫ √−g [ −½(∂φ)² − (λ/4!)φ⁴ ],   β(λ) = 3λ²/16π²
```

This sidesteps both hard obstacles by being local and 2nd-order: its propagator
is analytic at k = 0 (locality-clean) and it is manifestly ghost-free
(Ostrogradsky-clean). **But it fails GRUT-origin:** λ, its t_P value, and the
β-coefficient 3 have **no GRUT source.** It is a bolt-on (fail-4). Offered only
to demonstrate that the two hard obstacles and the GRUT-origin requirement are in
tension: the object that evades locality + Ostrogradsky is precisely the object
GRUT cannot source.

### 3.3 Angle 3 — CTP/KMS thermal-field condensation

Test whether GRUT's existing FDT noise kernel
`N(ω) = (2/τ)ℏω·coth(ℏω/2k_BT)` (`noise_kernel.py:31-48`) and KMS time
`τ_KMS = ℏ/2πk_BT` can serve as a condensation engine — the micro scale emerging
from a gap/condensation in the noise sector.

**It cannot.** The FDT kernel's only parameters are {τ, T} — both **dimensionful
scales**; the coth argument ℏω/2k_BT is ω/scale, **not** a dimensionless coupling
g(μ). A gap exp(−1/bg²) has no g to evaluate. There is no β-function, no order
parameter, no condensing potential. The thermal "anchor" is a **circular
identity** (verified in sympy: τ_micro := ℏ/k_BT_c, then T_c := ℏ/(τ_micro k_B)
returns T_c exactly), with T_c an empirical cosmological-chronology pin
(`closure_protocol.py` thermal anchor, status POSITED). The only running coupling
anywhere in the repo is the **imported SM** (`d4_thermal_restoration.py`: PDG
α_s, y_t, g_2, g_Y, λ, 16π²), which trips fail-4, and it uses H_inf / τ₀ → fail-3.
Stripped of imports, Angle 3 is a static thermal anchor wearing a condensation
costume — circular, exactly the failure mode the charter warned of. It passes
locality / Ostrogradsky / Q / v3 **by vacuity** — it carries no propagating UV
degree of freedom, so it has nothing to run.

---

## 4. THE TWO HARD OBSTACLES

### 4.1 Obstacle (i): NONLOCALITY vs the LOCALITY / NO-HALO THEOREM

The Riegert action is intrinsically nonlocal — it contains the inverse Paneitz
operator 1/Δ₄, a 1/□²-type kernel. **Leading symbol: 1/k⁴ — a k = 0 pole of
order 4.** Verified in sympy:

```
lim_{k→0} (1/k⁴)/(1/k²) = ∞
```

So the Riegert pole is **strictly MORE singular** than the 1/k² inverse-Laplacian
the theorem already forbids — not less. It is unambiguously in the singular-at-
k = 0 class the theorem (§2.3) bans.

**How each construction fares:**

  - **Angle 1 — BREAKS.** The scope-defense ("the pole lives in σ's *internal*
    propagator, decoupled from matter, so the matter→metric theorem does not
    apply") fails because σ **is the conformal/trace mode of the metric**, tied to
    the matter trace T by the trace-anomaly Ward identity. To do any dynamical
    work σ must couple to T — which is exactly a matter→metric channel,
    reinstating a 1/k⁴ matter-sourced response. Solving the Riegert EOM
    Q²□²σ = (1/2)T in momentum space gives σ(k) = T/(Q²k⁴): a 4th-order matter→
    metric pole, ~|r| in 3D position space (it *grows* with separation —
    maximally delocalized). The repo states the verdict directly
    (`second_order_kernel.py:67-70`). The **only** locality-safe confinement is
    into the E₄/a-anomaly channel — which `second_order_kernel.py:19-20` proves
    is Lovelock-null / dynamically dormant. **Locality is saved only by killing
    the dynamics.** There is no window where σ is both locality-safe and
    dynamically live.
  - **Angle 2 — passes locality** (local 2nd-order, analytic at k = 0), but at
    the cost of GRUT-origin (it is a bolt-on).
  - **Angle 3 — passes locality by vacuity** (no Riegert action, no inverse
    Paneitz; the noise kernels are the permitted single-pole-in-ω OU response and
    the analytic Diósi kernel). The same emptiness that makes it locality-safe
    makes it dynamically dead.

### 4.2 Obstacle (ii): OSTROGRADSKY / GHOST (= Q)

The Riegert/Paneitz action is 4th-order → a generic Ostrogradsky ghost. Verified
in sympy:

```
1/(s(s+m²)) = +1/(m²s) − 1/(m²(s+m²))      [s = k²]
```

— opposite-sign residues +1/m², −1/m²: one healthy pole, one propagating
negative-norm (ghost) pole. The degenerate Riegert case (pure 1/k⁴) is a double
pole / dipole ghost.

**Ghost = Q-violation (same gate), verified in sympy:** GRUT's healthy
susceptibility χ(ω) = 1/(1−iωτ) has Im χ = ωτ/(1+ω²τ²) > 0 (FDT-positive
baseline, `linearized_ctp_action.py:240-249`). A ghost flips the sign:
Im χ_ghost < 0 ⇒ FDT noise N(ω) = coth(ω/2T)·2 Im χ < 0 (coth > 0). With N < 0,
the influence weight Im S_IF = ½ h_a N h_a is **not** positive-semidefinite, so
exp(−Im S_IF) is a non-normalizable Gaussian — the in-in path integral has no
valid stochastic-noise realization and is not unitary evolution. **Q is
violated.**

*(Precision note, for honesty: the failure is the OFF-diagonal noise positivity,
not "S_IF cannot vanish on the diagonal." S_IF[h₊=h₋] = 0 still holds by h_a
antisymmetry regardless of N's sign — every influence term carries h_a. The Q
failure is that N < 0 makes the off-diagonal noise weight non-normalizable. Same
gate, same conclusion — ghost = Q failure — more precise mechanism.)*

**How each construction fares:**

  - **Angle 1 — BREAKS.** The Antoniadis–Mottola resolution renders the
    conformal-mode dipole a zero-norm / cohomological (gauge, non-propagating)
    state — but **only if σ is the global conformal factor, non-propagating.**
    That is the **same confinement** as the locality fix: ghost-free ⇔
    dynamically inert. The repo flags this exact closure OPEN
    (`closure_protocol.py:131-133`). Ghost-freedom is not achieved for a *live*
    sector; it is bought by deleting the degrees of freedom. Importing AM's
    external spectral machinery as the resolution would itself trip fail-4.
  - **Angle 2 — passes** (2nd-order, manifestly ghost-free), again at the cost of
    GRUT-origin.
  - **Angle 3 — passes by vacuity** (relaxational single-pole OU dynamics, no
    4th-order operator, no new propagating mode).

---

## 5. VERDICT

**Can a self-consistent postulated UV-dynamical sector be built from GRUT's own
structure? NO — at the structural tier.**

All three angles reach `honest_tier = fails`. The convergent, decisive obstacle
is the **LOCALITY–DYNAMICS FORK**, internal to GRUT:

> The anomaly number that would source the conformal-mode (Riegert) action —
> a / E₄ — is **precisely the one GRUT's own second-order analysis proves is
> dynamically dormant** (Lovelock-null in 4D, `second_order_kernel.py:19-20`).
> The channel that has live dynamics — c / W² — is **not** the channel the
> Riegert action is built from.

The fork is exact and triple-locked:

  - **To respect locality + Q**, σ must be confined to the matter-decoupled
    E₄/a-channel as a global / zero-norm (AM cohomological) mode — but that
    channel is Lovelock-null with no local 4D dynamics, so it carries **no
    β-function and no running coupling.** Locality and Q are saved by killing the
    dynamics.
  - **To do dynamical work**, σ must couple to the matter trace (it *is* the
    metric trace, tied to T by the Ward identity), producing a 1/k⁴ matter→metric
    response — which trips the locality / no-halo theorem (a pole strictly worse
    than the forbidden 1/k²) **and** threatens μ_linear = 1.

There is **no window** where σ is simultaneously locality-safe, ghost-free
(Q-safe), and dynamically live.

### 5.1 The existence question, answered both ways (honestly)

  - **The reference CLASS generically makes large Planck-referenced logs from
    O(1) inputs.** [fact, verified] With the genuine 1/(16π²) anomaly
    normalization, b₀ ~ O(1)/16π² ≈ 0.0063, so L = 1/(b₀g²) for g ∈ {0.5, 1, 2,
    3} gives L ≈ {632, 158, 39, 18} — tens-to-hundreds, naturally. The smallness
    of b₀ (forced by 1/16π², **not** the forbidden 8π²) is exactly why a large
    hierarchy is generic. This is a legitimate, valuable **existence** statement.
  - **But it cannot be realized inside GRUT.** That large log requires a *live*
    running coupling. GRUT's only GRUT-origin coupling (the anomaly coefficient)
    is one-loop-exact (β = 0) and lives in the dormant E₄ channel. **The class
    makes large logs; GRUT's own structure cannot supply the engine.** Reporting
    "and it equals 56" would be reverse-engineering and is explicitly *not* done —
    g_P is left free throughout; the g that would hit 56.21 (≈ 1.676) is not in
    the sampled set {0.5, 1, 2, 3} and is never targeted.

### 5.2 What new postulate would GRUT have to accept — and is it compatible or fracturing?

In order of increasing damage:

  1. **A new propagating vacuum pole** (a genuinely new micro degree of freedom),
     not a new operator. `locality_no_halo.py:13-14` states the only escape
     verbatim: "a derived dark sector requires a NEW POLE in the vacuum spectrum
     (a new propagating mode), not a new operator." This is the minimal honest
     postulate. **Verdict: it FRACTURES GRUT's minimalism** — a bolt-on degree of
     freedom with no anomaly origin, carrying its own un-GRUT-sourced running
     coupling and β-coefficient (fail-4 territory). It is new *content*, not a
     re-reading of existing structure; it constitutes a different theory, not
     GRUT.
  2. **Tolerated UV nonlocality** — accept that the locality / no-halo theorem
     constrains only the matter→metric IR response and permit the Riegert 1/k⁴
     pole in the σ-*internal* propagator, decoupled from matter. **Verdict: the
     decoupling required is exactly the E₄-confinement that makes the sector
     dynamically inert** — so even this relaxation buys no working sector. It does
     not fracture v3 (the firewall keeps UV blind to τ₀; μ_linear = 1, single-pole
     F, Ω_Λ = (2−R)² untouched), but it also produces nothing.
  3. **Abandon either Q or the locality theorem.** Both are proven results of the
     formalism (Q = in-in unitarity; locality = the same result that fixes L₀).
     **Verdict: this fractures the framework's foundations** and is ruled out by
     the charter's non-negotiables.

**Bottom line.** The honest, grounded answer is **NO**: no self-consistent
postulated UV-dynamical sector can be built from GRUT's own anomaly structure
without either (a) tripping the locality / no-halo theorem (the Riegert 1/k⁴
matter→metric pole), (b) violating Q via the unresolved Paneitz ghost, or (c)
being dynamically inert because the only locality-safe and ghost-free home — the
E₄/a-anomaly channel — is the one GRUT itself proves is Lovelock-null. The class
makes large logs; GRUT cannot supply the live coupling to realize one. The
feasibility pass's NOT-YET-FORMULATED is upgraded to a structural **NO**.

---

## 6. ADVERSARIAL RESULTS — which attacks broke which construction

Five independent adversarial passes were run; four conclude `breaks_construction
= true` (i.e. confirm the negative), one `false` (a number-smuggling audit that
found the negative clean). Each re-Read the cited files and re-ran the algebra.

| Attack axis | Target | Result |
|---|---|---|
| **Nonlocality vs locality theorem** | Angle 1 (Riegert σ) | **BREAKS** — 1/k⁴ matter→metric pole, strictly worse than forbidden 1/k²; scope-defense fails because σ = metric trace, tied to T by Ward identity; only locality-safe confinement (E₄) is Lovelock-null. |
| **Ostrogradsky ghost** | Angle 1 | **BREAKS** — opposite-sign residues +1/m², −1/m² = propagating dipole ghost; ghost-freedom only via AM zero-norm confinement = the same inert E₄ channel; closure_protocol.py:131-133 flags OPEN. |
| **Q / CTP unitarity** | Angle 1 | **BREAKS** — ghost ⇒ Im χ < 0 ⇒ FDT noise N < 0 ⇒ off-diagonal noise weight non-normalizable ⇒ in-in path integral non-unitary. (Precision correction to earlier wording: the failure is off-diagonal noise positivity, not diagonal vanishing.) |
| **v3-breakage + bolt-on** | Angles 1–3 | **CONFIRMS NEGATIVE** — v3 is NOT broken precisely *because* the sector fails to be built; v3 breaks only if σ is forced to do work (the disqualifying configuration). The only escape (new propagating pole) is a non-anomaly-origin bolt-on that fractures minimalism. |
| **Number-smuggling audit** | all | **CLEAN (no fail tripped)** — no coupling tuned to 56.21 (the g that would, ≈1.676, absent from sampled set); b₀ uses standard 1/16π² not 8π²; no τ₀/L₀/H₀ as inputs (τ₀ only via the firewall that *guarantees* UV blindness); no imported coefficient as the mechanism in the GRUT-origin route. The construction dies at the locality/ghost/dynamics fork *before* any forbidden number is reached. |

Convergence: the locality failure and the Q/ghost failure are **two independent
gates**, either of which is fatal to Angle 1; the v3 and number-smuggling audits
confirm the negative is clean and load-bearing. The strongest single statement,
true across all three designs and all five attacks: **the anomaly number that
would source the conformal-mode action (a / E₄) is precisely the one GRUT has
shown is dynamically dormant; the channel that has live dynamics (c / W²) is not
the channel the Riegert action is built from.**

---

## 7. CHARGE / NEXT STEP

The negative is the deliverable. What would have to be settled to revisit it:

  1. **Harden the Ostrogradsky leg from "conditionally passed" to "proven."** The
     AM zero-norm / cohomological ghost resolution and the claim that a
     topological E₄ sector carries strictly zero local β-flow are stated at the
     [reading] / [reference-class] tier. A dedicated covariant CAS (xAct)
     treatment of the Paneitz BRST cohomology would convert "ghost-free ⇔ inert"
     from a strong argument into a theorem. **[open]** This does not change the
     verdict — locality already kills Angle 1 independently — but it closes the
     last gap.

  2. **If GRUT chooses to accept a new postulate**, the *only* one that yields a
     working sector is **a new propagating vacuum pole** (option 5.2.1) — and the
     framework must then openly book it as a fracture of minimalism: a new degree
     of freedom with no anomaly origin, requiring its own running coupling. That
     coupling, having no GRUT source, lands in fail-4 territory; deriving its
     β-coefficient from anything other than GRUT structure would not count as a
     GRUT derivation of the hierarchy. **The honest framing: this is a different
     theory, not GRUT v-next.**

  3. **The four fail conditions remain in force** for any future attempt: no
     reverse-engineering from 56.21 (fail-1); no 78.23 / 8π² ≈ 78.96 / 9.47e33
     (fail-2); no τ₀ / L₀ / H₀ / τ_Λ / μ₀ / a₀ as inputs (fail-3); no imported /
     tuned coefficient as the mechanism (fail-4). The hierarchy ledger's standing
     charge is unchanged: existence is FORCED, magnitude UNKNOWN; force
     ln(τ_micro/t_P) from GRUT structure, never c, never 8π² — and, per this
     document, **not from the conformal mode, because its anomaly home is
     dormant.**

---

### Files Read (absolute paths, all confirmed verbatim)

- `/Users/mpg/Library/Mobile Documents/com~apple~CloudDocs/Ryans Projects/GRUT-RAI-v2/grut/derivation/phi_munu/locality_no_halo.py` (theorem 7-14; walls 16-21; 1/k² pole 19-20)
- `/Users/mpg/Library/Mobile Documents/com~apple~CloudDocs/Ryans Projects/GRUT-RAI-v2/grut/derivation/phi_munu/second_order_kernel.py` (W² unique active / E₄ dormant 16-22; 1/r⁴→1/r² forbidden 67-70)
- `/Users/mpg/Library/Mobile Documents/com~apple~CloudDocs/Ryans Projects/GRUT-RAI-v2/grut/foundation/anomaly_derived.py` (anomaly normalization 1/16π² 44-50; COEFF_SCALAR 55-59)
- `/Users/mpg/Library/Mobile Documents/com~apple~CloudDocs/Ryans Projects/GRUT-RAI-v2/grut/foundation/conformal_mode_scalar.py` (per-species (a,c) 47-63)
- `/Users/mpg/Library/Mobile Documents/com~apple~CloudDocs/Ryans Projects/GRUT-RAI-v2/grut/foundation/closure_protocol.py` (Riegert/Paneitz 4th-order closure OPEN 131-133)
- `/Users/mpg/Library/Mobile Documents/com~apple~CloudDocs/Ryans Projects/GRUT-RAI-v2/grut/derived/cmb/boltzmann_consistency.py` (RG firewall 43-45)
- `/Users/mpg/Library/Mobile Documents/com~apple~CloudDocs/Ryans Projects/GRUT-RAI-v2/grut/derivation/phi_munu/linearized_ctp_action.py` (single-pole χ 240-249; h_a-anchored influence terms 304-309)

### Sympy verifications (re-run in `.venv`)

- Riegert pole strictly more singular: lim_{k→0}(1/k⁴)/(1/k²) = ∞
- Dipole ghost: 1/(s(s+m²)) = +1/(m²s) − 1/(m²(s+m²)), opposite-sign residues
- a/c = 1/3 convention-independent: KS a/c = 1/3 = BD |Euler/Weyl|; KS = 360·BD (both coeffs)
- FDT sign: healthy Im χ = ωτ/(1+ω²τ²) > 0; ghost flips → N < 0
- Generic large log: b₀ = 1/16π² = 0.00633; L = 1/(b₀g²) = {632, 158, 39, 18} for g = {0.5, 1, 2, 3}; g→56.21 ≈ 1.676 (absent from sampled set, never targeted)
