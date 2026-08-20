# Register-edit drafts — 2026-08-20

> **NOTHING HERE IS APPLIED.** `provenance/claims.json` is untouched by this file. These are drafts
> for the owner to run through the bank-gate / firewall, per CHARTER §1.3 and §5.3. Each is stated
> with what was verified, by whom, and what it does NOT license.
>
> **Applied separately today (calc layer only, unconditional, no register edit):** the corrected
> regime check and KK scope fence in `calc/gw_dissipation_bounds.py`; the `orders`-vs-`factor`
> unit slip in `calc/RESULTS_gw.md`, `provenance/harness.py`, `GRUT_ToE.md`, `SIGNATURE_AUDIT.md`,
> `README.md`, `SPECIALIST_BRIEF.md`; and the retraction of `PRIMITIVE_INVERSION_SCOPE.md` §9.

---

## EDIT 1 — `rung4_love_kk`: mark the 22–62 orders CONDITIONAL (do NOT change the number)

**What was found.** `calc/gw_dissipation_bounds.py`'s regime check claimed the IR horizon pole
(τ₂ ~ 1/H₀) is "invisible" in the LIGO band because ω ≫ H₀. That is false: a Lorentzian pole does
not switch off above its own frequency. Im χ_UV rises as A·ω·τ_c while Im χ_IR falls as B/(ω·τ₂),
so they cross at the geometric mean √((B/A)·ω_c·H₀). **Independently verified**: with this corpus's
own ω_c = 1e40·H₀ and B/A = 0.4, Im χ_IR/Im χ_UV = 1.0e-2 at 100 Hz and the crossover is ~63 rad/s
(~10 Hz) — inside the LIGO band.

**What this does NOT do — read this before amending anything downstream.** It does **not** falsify
the filed 22–62 orders. That number is a *dephasing* figure computed from Re χ, and the IR pole's
Re part, B/(1+(ωτ₂)²), *is* negligible at LIGO frequencies. An earlier draft of this finding
compared an Im-χ attenuation exponent in nepers against a radian phase threshold; that was a
category error and it is withdrawn.

**What is actually exposed** is an *uncovered channel*: achromatic friction Γ = B·H₀/2, degenerate
with the coalescence phase (so the matched-filter test is blind to it by construction), appearing
instead in standard-siren amplitude. At B = 0.4 that is 0.2·H₀ — inside the |Γ_T| ≲ few × H₀ slot
bound this program already quotes at `SIGNATURE_AUDIT.md:62`.

**Two reasons it is not settled in either direction.** B = 0.4 is a *staked illustrative* amplitude
whose own source disclaims the form (`wz_dark_energy.py:18-25`); and the conformalon rate leg
(EDIT 4) would put B ~ 2.4e-4, returning the channel to invisibility. These two results were
produced in the same pass and were never composed.

**Proposed `differentiator` amendment** (append; do not alter the existing sentence):

> CONDITIONAL-SCOPE MARKER 2026-08-20: the "~22-62 orders below detectability" is a DEPHASING
> statement (computed from Re[chi]) and is NOT a statement about the standard-siren AMPLITUDE
> channel. calc/gw_dissipation_bounds.py's regime check asserted the IR pole tau_2~1/H0 is
> invisible at LIGO frequencies; that assertion was FALSE (the poles cross at the geometric mean,
> not at omega~H0) and is corrected in the calc file. The amplitude channel carries achromatic
> friction Gamma = B*H0/2, which at the staked B=0.4 is 0.2*H0 -- inside the |Gamma_T| <~ few x H0
> slot bound, not below it. NOT SETTLED: B is a staked illustrative constant, and the conformalon
> rate leg would put B ~ 2.4e-4 (invisible again). The forward calculation is
> calc/gw_tensor_friction.py, specified at SIGNATURE_AUDIT.md:68 and CONFIRMED ABSENT 2026-08-20.
> The SECTOR question decides it: does the tau_2 pole appear in P^TT at all, or only in the scalar
> channel that p_tt_ansatz excludes? Until that runs, this node's differentiator verdict stands
> for dephasing and is UNCOVERED for amplitude.

**Tier: unchanged (`shown`). Ledger: unchanged (0).** The KK structure claim itself is untouched.

**Downstream that must NOT be amended yet** (all still correct as dephasing statements):
`NO_GO_LEDGER.md` entry 5, `RESULTS_gw.md:23-24,44`, `GRUT_ToE.md:149,166`,
`GRUT_V1_PLAIN.md:68,168`, `docs/WHERE_IT_STOPS.md:285`.

---

## EDIT 2 — `rung7_wz.boundary_condition`: the ~40-orders reconciliation clause

**Current text**, verbatim: *"BUT they coexist by ~40-orders scale separation (UV cutoff omega_c
for the tabletop where omega>>H0; IR horizon scale for cosmology where omega~H)."*

**Status: true for Re χ, false for Im χ.** The reconciliation as written implies the two poles do
not both operate in one band. They do — in the dissipative part. The separation of *scales* is
real; the separation of *effects* is not.

**Verified negative, worth recording so it is not re-opened:** the ~40-orders ratio itself is
**clock-invariant** — a ratio of two times at one event is invariant under reparametrisation. Redone
in five corpus clocks the full spread is 0.477 orders out of 40. **The clock audit found no defect
here.** The real defect is EDIT 3.

**Proposed amendment** (replace the clause):

> ...BUT they coexist by ~40-orders scale separation IN THE STORAGE (Re) CHANNEL ONLY. CORRECTED
> 2026-08-20: this clause previously read as a general invisibility claim. It is FALSE for the
> dissipative (Im) channel, where the two Lorentzian contributions cross at the geometric mean
> sqrt((B/A)*omega_c*H0), not at omega~H0 -- inside the LIGO band for this corpus's own omega_c.
> See rung4_love_kk's 2026-08-20 conditional-scope marker.

**Also flagged, not proposed:** this node's `statement` says the τ₂ mode is *"booked in this
claim's +2"* while `ledger_delta` is **3**. Internal inconsistency, unresolved here — it needs an
owner ruling on which is right, and it touches the net.

---

## EDIT 3 — pin ω_c (this is an adjudication, not an edit)

Three in-corpus values, spanning **39.6 orders**, inside a quantity filed as "~40 orders":

| value | source | log₁₀(ω_c/H₀) |
|---|---|---|
| 2π·689 rad/s | `rung8_falsifier.ledger_note` ("what '689 Hz' really was") | 21.30 |
| 1e40·H₀ | `wz_dark_energy.py:61` — a round literal with a bare comment | 40.00 |
| ω_Planck = 1.855e43 rad/s | `gw_dissipation_bounds.py:28` | 60.93 |

**Why this is now load-bearing rather than bookkeeping.** The EDIT 1 crossover goes as √ω_c, so the
choice moves it ~10 orders and decides whether it lands *inside* the LIGO band (1e40·H₀ → ~10 Hz)
or far above it (Planck → ~0.64 THz). Two independent passes computed the crossover and got
different answers **for this reason alone**. The number is not free.

Propagates to: `rung7_wz.boundary_condition`, `README.md:86`, `RESULTS_wz.md:24`,
`wz_dark_energy.py:87,141`. If 689 Hz is the answer, "~40 orders" becomes 21.3 in four documents.

---

## EDIT 4 — the conformalon epoch is declared nowhere

`⟨σ²⟩ = D·N`, `D = 1/(4π²Q²)`, is de Sitter IR secular growth **per e-fold**, and *what epoch N
counts* is stated in neither `delta4_stability.py`, nor `RESULTS_conformalon.md`, nor the register.
The filed "~8× below DESI at N=60" is arithmetically correct at N=60 (verified: 60/2414.57 =
0.024849; 0.2/0.024849 = 8.05). The defect is that N=60 is an *inflationary* e-fold count used for
a *z=0* observable, with no declaration.

**The epoch-free leg, which nobody computed and which is the better statement:** since 1+w(N) is
linear in N, `w_a = dw/dz|₀ = −1/(8π²Q⁴) = −4.14e-04` with **no free parameter and no epoch**.
Against DESI's |w_a| ~ 0.6–1.0 that is ~1500–2400×, not 8×.

**Direction: this runs AGAINST the framework's interest** — it makes the conformalon closure safer,
not weaker. Labelling defect, not laundering.

**Do not quote the companion "shape fixes N" argument** ((1+w₀)/|w_a| = N ≈ 0.29 vs ln(1.3057) =
0.267). It is near-circular — DESI's ratio just encodes that dark energy evolves over ~one e-fold —
and it should not be presented as independent convergence.

---

## EDIT 5 — `method_novelty`: the prior-art screen against formal methods

**The falsifier does NOT fire.** Verbatim: *"REFUTED as even WEAKLY-novel IF the full assembly …
is shown to be an existing named/deployed system rather than a fresh synthesis."* It fails on two
grounds only: every screened system presupposes a **decidable checker** and can price only what a
kernel sees — essentially none of this register's 71 entries could enter one, because they are
natural-language physical claims carrying an **empirical** falsifying computation, a field no
screened system has; and "deployed" is doing real work.

**Tier stays `to-derive`. Ledger stays 0. The node is NOT retracted.**

**But three findings cut against the node and belong in `tier_note`:**

1. **Metamath set.mm collapses four of the five components into one artifact** — running since
   1992, 47,736 theorems, per-theorem transitive axiom closure published, six independent verifiers
   in CI that must all pass, a 21,406-line `discouraged` ledger diffed on every PR. The node's line
   attributing the consistency engine to "build-lineage / W3C-PROV / truth-maintenance" is
   materially understated, and its ledger line ("Lakatos + double-entry accounting +
   parameter-counting") likewise. Reverse mathematics does the ledger job with a **reversal**, which
   proves the price *exact* where this ledger asserts a heuristic sum.
2. **On component 3 this program is strictly WEAKER than the prior art, not differentiated from
   it.** This repo has no CI and no git hooks; `../claimledger` has none either. The engine is a
   142-line auditor invoked by hand. Metamath's gate exits nonzero.
3. **The closest single system is CONTEMPORANEOUS and in physics.** M.R. Douglas (Harvard CMSA):
   `math-commons/formalization-assurance` created **2026-06-15 — two weeks before this node was
   banked** — plus `seiberg-witten` / arXiv:2607.06379 and the Palomar Registry. It implements all
   five components in substance, aimed at AI-generated physics, with cross-model adversarial vetting
   carrying sha256 statement hashes. **The falsifier as armed cannot distinguish "fresh synthesis"
   from "independent simultaneous reinvention." RE-ARM IT.** Note also that this is a *different
   team* on a *different problem* catching real errors — which discharges nothing here, because the
   errors it caught were its own. It is competition, not validation.

**The surviving delta, stated after the screen, as what survived — narrow but real:**
(1) an **empirical** falsifying computation per claim (no formal system has this or could — a proved
theorem is not defeasible); (2) a scalar price — **also the least defensible surviving element**: a
declared human integer that nothing verifies, and "signed" means the arithmetic sign of a blind sum,
not a cryptographic signature; (3) the **tier × price cross-rule** (result-tier claim + positive
`ledger_delta` = BLOCKED), for which four independent screens found **no counterpart anywhere**.
That third item is the only genuinely unprecedented mechanism.

**Also: component (4) is a symptom, not a contribution.** Formal systems need no adversarial agents
because the kernel *is* the adversary. The default-BROKEN subagent layer exists here because these
claims are not machine-checkable — and it should be described that way rather than as an innovation.

**Sources to add:** `metamath_setmm`, `lean_print_axioms`, `simpson_reverse_math`, `rmzoo`,
`alama_mizaritems_2011`, `kohlhase_rabe_viewfinder_2018` (cross-foundation theory-morphism search —
prior art for the *cross-cluster shared input* operation specifically), `douglas_sw_2607.06379`,
`formalization_assurance`, `palomar_registry`, `carcassi_reverse_physics` (a published two-axis
tier vocabulary for underived PHYSICAL inputs, genuinely prior to this node's vocabulary).

> **Verification status: these citations have NOT been checked against primaries by the owner.**
> Per CHARTER §2 they are not sources until they have been. Add only what verifies.

---

## EDIT 6 — the `claimledger` pointer, and the unbooked Nowak run

**Verified 2026-08-20:** `../claimledger` exists as its own repository — the correct arrangement for
a domain-free package — with two commits: `6853b78` "claimledger 0.1.0: the discipline engine, split
out domain-free" and `61c0a3e` "cold-corpus run: Nowak arXiv:2608.06147, selection rule
pre-committed". It was never committed into this tree because it is a separate repo, not because it
was lost. `method_novelty.boundary_condition` already names the path; what it lacks is the commit
hashes and the note that verification requires a second checkout.

**The substantive gap: the register books only the Du et al. run, and the Nowak run is the stronger
one.** Per `examples/COLD_RUN_PROTOCOL.md`, the Nowak run committed its selection rule *before any
fetch* — field q-bio.PE (never touched by any wave), first paper in the recent listing with a
quantitative headline claim, **no substitutions permitted after reading**, and the encoder's first
read of the paper *was* the encoding read. The Du et al. file states plainly that its own encoder
"had already read the paper closely for other reasons, so it demonstrates only the tool's first
value proposition (recording DECLARED posits)."

The Nowak run tests the second proposition and reports honestly in both directions: the tool found
**no error** (the paper prices its assumptions well), and what it surfaced was that the headline
"maximum payoff" is defined as *efficiency*, so for u+v > 1 the resolved dilemma resolves by
**anti-coordinated alternation, not mutual cooperation** — the gap a downstream quotation falls into.

**Why this matters more than a pointer fix:** it is the only run designed to answer the standing
objection that the engine was tuned on its own corpus, and it is the strongest single piece of
evidence for the "the instrument travels" reading of the program. **Leaving it unbooked is an
omission of FAVOURABLE evidence** — not directional optimism, an incomplete record — and it should
be closed for the same reason the ledger exists.

---

## What this pass could not determine

- Whether the corrected `kk_static_transfer` treatment on FRW moves χ(0) by 1% or by O(1). Needs a
  calculation this pass was read-only for.
- What epoch the conformalon's N counts. The repository never says. A defence that ⟨σ²⟩ is an
  inflationary condensate surviving into the late universe is not obviously wrong — it is merely
  nowhere written down, and the growth formula it would need is a de Sitter formula.
- **Q2(e), the cosmic-time/foliation candidate, remains owed since 2026-08-04.** It went missing in
  two consecutive waves and the second disappearance was itself ruled a method defect. Every ω in
  this corpus is written at a frequency whose conjugate time Q2(e) was supposed to settle. This pass
  points at it and does not close it.
