# rung7 — the dark-energy w(z) and the SIGN of wa (in-house attempt + verdict)

*Closes the loop the forward-model harness opened: the harness ASSERTED `forward_wz` per rung7's to-derive status; this is the in-house attempt to DERIVE the sign of wa and whether w(z) crosses the phantom divide. Default-BROKEN: the win is the honest verdict, not a forced sign. Code: `calc/wz_sign.py`. Register: `rung7_w1_wz_map` (shown-generic), `rung7_w2_wa_sign` / `rung7_w3_nocrossing_export` (to-derive, default-BROKEN). Scope, held throughout: a SIGN / NO-GO, NOT a magnitude — the w(z) magnitude rides on the open late-time vacuum-energy anchor.*

---

## The claim (default-BROKEN)

For the passive (Im χ ≥ 0), causal (KK), KMS-consistent **single-pole** vacuum the shown spine supplies (rung1 memory + rung2 detailed balance + rung3 single-pole + rung4 KK), w(z) cannot cross the phantom divide w=−1, so DESI's evolving wa<0 (a quintom **crossing**) is reachable only by breaking passivity / inserting an off-equilibrium DOF = laundering.

## Decomposition

- **W1 — the map exists (generic).** A relaxing causal χ(ω) defines an effective T_μν and w(a)=p/ρ=−1+(w+1), with the deviation (w+1)=Π/ρ off the de Sitter equilibrium w_eq=−1. Standard EFT-of-dark-energy (Gubitosi–Piazza–Vernizzi) — **`shown`, flagged not-uniquely-GRUT** (names neither a sign nor a GRUT structure).
- **W2 — the crux (the SIGN).** From the passive-causal-KMS single-pole spine: (i) can w cross −1? (ii) the sign of wa? (iii) is an evolving w(z) sourced or inserted?
- **W3 — the payoff.** IF W2's no-crossing graduates, does it export a falsifiable-direction no-go and convert the harness's *asserted* w(z) negative into a *derived* one?

## The in-house attempt (W2) — `calc/wz_sign.py`

A two-framing comparison on the background H(a)²/H0²=Ω_m a⁻³+Ω_Λ, with the vacuum's equilibrium pinned at w=−1 and a single passive dissipative deviation (w+1)=±ε·(H/H0) that shrinks toward the de Sitter attractor:

| framing | w0 | wa | crosses w=−1? |
|---|---|---|---|
| bulk-viscosity (ζ≥0, second law) | −1.05 | **−0.0225** | False |
| phase-lag / energy-loss (banked rung7 v5) | −0.95 | **+0.0225** | False |

**(i) NO-CROSSING — ROBUST (within the spine).** The equilibrium is exactly w=−1; a SINGLE passive channel's (w+1) is **one-signed** (one relaxation time, one coupling sign → monotone, not oscillatory) and → 0 as H → 0. So w approaches −1 from one side and **never crosses**. A crossing (DESI's quintom: w<−1 past → w>−1 now) needs the equilibrium itself off −1 (a real quintessence/phantom DOF) **or** a sign-changing kernel (≥2 modes / oscillatory poles) — exactly the inserted structure banked rung7 already names as the cost of matching DESI. Consistent with banked rung7 Q2 ("single passive relaxor ⇒ no phantom-divide crossing") and Vikman 2005 (a single non-ghost DOF cannot dynamically cross).

**(ii) the SIGN of wa — INDETERMINATE in-house.** Passivity fixes the dissipation **positive** (Im χ ≥ 0) but NOT the **wa slope sign**. The standard second-law **bulk-viscosity** reading (ζ=lim Im χ/ω ≥ 0 ⇒ Π=−3ζH ≤ 0) fixes the **side** w ≤ −1 (the phantom side); but its **wa slope** is a modeling choice — ζ=const/Eckart gives **wa ≤ 0**, ζ(a)∼1/H² gives **wa > 0**, both with Π≤0 and σ=Π²/(ζT)≥0 at every epoch. The banked **phase-lag** (reactive Re χ) reading sits on the w ≥ −1 side. So the wa sign rides on the **trace-sector coupling and the ζ(a) scaling**, which the frequency-space spine does not supply — genuinely **open** (two non-theorem arguments lean it wa<0; see the amended boundary below).

**(iii) SOURCED — w=−1 FLAT.** The shown response is pure spin-2 TT (`p_tt_ansatz` / `mu_linear`): the spin-0/trace sector that carries a bulk response is annihilated, so ζ_bulk=0 ⇒ (w+1)=0 ⇒ w=−1 at **background** order. Any evolving w(z) requires the trace sector `mu_linear`'s no-go EXCLUDES — an inserted input.

## Verdict (default-BROKEN, honest)

- **Robust derived-candidate:** the **NO-CROSSING no-go** — the passive single-pole spine forbids DESI's phantom-divide crossing without laundering. (Held at to-derive, relay-gated; NOT banked as derived in-house.)
- **Frontier:** the **sign of wa** is contested — bulk-viscosity ⇒ wa ≤ 0, phase-lag ⇒ wa > 0. Resolving it needs the full de Sitter **trace-sector effective stress tensor**. Escalate to a dark-energy-EFT specialist.
- **Sole fully-sourced prediction:** **w=−1 flat** (pure-TT / mu_linear).
- **W3:** converts the harness's *asserted* w(z) negative into a *derived* no-go **on the crossing** (not on the wa sign); the wa magnitude/sign stay open. Not a ToE-completion, not a precise w(z) curve.

## Independent firewall (2026-06-29) — HOLDS, both directions clean, two sharpenings

A both-directions screen (steelman the no-go / refute / scope) confirmed the verdict and sharpened it — no manufactured proof (the no-crossing stays to-derive), no over-dismissal:

1. **No-crossing is CONDITIONAL on rung3 (open).** The "monotone one-signed Π" argument is the **single-real-pole** (collisional/analytic) regime. If GRUT's bath is collisionless free-streaming (rung3's live Class-B branch cut, not a single pole), the kernel is power-law and the no-crossing needs re-derivation. The no-go inherits rung3's openness (W2 `depends_on` rung3, which is `derived-pending`).
2. **The wa "indeterminate" leans toward DESI.** The *natural* EFT reading (passive second-law bulk viscosity, ζ≥0) gives **wa ≤ 0** — the DESI sign — making the banked rung7 **wa > 0** the *less* natural of the two branches. This SHARPENS (does not overturn) exactly the "explicit proof owed in GRUT's effective stress tensor" caveat the banked rung7 specialist (Q2) already attached to wa>0.

## Overseer rulings (2026-06-29) — both adjudicated, then (a) self-corrected (verify-the-verifier)

**(a) The wa-sign softening — APPROVED, then AMENDED.** The overseer ran an independent workflow on their *own* sharpening and **retracted it**: "wa≤0 is second-law-fixed" was an over-claim in the *toward-DESI* direction — the mirror of the banked "wa>0, wrong sign" (away-from-DESI). **Both are now retracted; the honest middle is open-slope** (the machine caught the overseer — the verify-the-verifier principle working on the verifier).

**The amended boundary** *(replaces the prior sharpening):*
- **The second law fixes the SIDE, not the SLOPE.** ζ≥0 ⇒ Π=−3ζH≤0 ⇒ the dissipative branch sits at w≤−1 (phantom side), the reactive (Re χ) branch at w≥−1; σ=Π²/(ζT)≥0 forbids a *within-branch* crossing of −1 — **this is the robustly-supported piece, exactly what supports the no-crossing.** But σ is *quadratic* in Π, blind to dΠ/dt, so the wa slope rides on sign[d(ζH)/da], which the inequality never touches: ζ=const → wa<0, ζ∼1/H² → wa>0, both fully passive (Π≤0, σ≥0 throughout). **The wa sign is genuinely OPEN.**
- **Two non-theorem arguments lean the slope toward wa<0 (DESI's sign) — flagged as ARGUMENTS, not constraints; banked as notes, not tiered claims:** (i) the de Sitter-attractor / entropy-max boundary excludes the strongest wa>0 profiles (ζ∼1/H² gives ζH↛0); (ii) thermal naturalness — ζ tracks the *cooling* Gibbons-Hawking bath, so it falls with a, making wa<0 the natural reading. Neither is a constraint.
- **Side-tension with DESI.** The w≤−1 floor is in mild tension with DESI's present-day w₀>−1 — so the dissipative branch matches DESI's slope-*sign* (on the natural reading) but sits on the *wrong side* for w₀ today, and can't cross without an inserted mode. The lean lost not just its theorem but, on the side axis, its direction.
- **Net: sourced = w=−1 FLAT; wa OPEN (soft DESI-ward lean, argument-not-theorem); no clean DESI match** — carried by the `evolving ⇒ needs_unsourced_input` invariant, not the sign. The **no-crossing is the robustly-supported piece** (the second law genuinely forbids a within-branch crossing); still `to-derive`, still rung3-gated, now clearly the solid part while the slope-sign is the open part.
- **Harness showcase (stronger, not weaker).** `forward_wz`'s passive 2-scale representative was flipped to the dissipative **DESI-sign** (wa≤0) branch: it now *matches DESI's sign within precision and is still refused* — on inserted-input grounds alone. The no-clean-match guarantee never rested on the sign; it rests on the `evolving ⇒ needs_unsourced_input` **invariant**, so the correction makes the machine a stronger demonstration. `n_data_consistent_clean` is **unchanged** (one clean: the single-scale ΛCDM); two regression tests pin it.

**(b) The no-crossing no-go: HELD at `to-derive` (does NOT graduate).** Two decisive reasons: (1) it is **generic** (Vikman — any single non-ghost DOF can't dynamically cross; GRUT content is only "the single-pole spine lands in that class"); (2) it is **conditional on rung3, which is open** — *a no-go cannot outrank its anchor*. **Strategic:** rung3 (single real pole vs free-streaming branch cut) is **the bottleneck** for graduation and for the whole w(z) story; likely specialist-reserved, not a quick in-house win.

## Scope and honesty

- **A SIGN / NO-GO, not a magnitude.** The w(z) magnitude rides on the open vacuum-energy anchor and stays open. Do not inflate the no-crossing into a w(z) prediction.
- **The no-crossing is generic-flavored** (Vikman applies to any single non-ghost DOF); the GRUT-specific content is only that the *spine* (rung2 equilibrium-at-−1 + rung3 single-pole) lands in the no-crossing class. Not a brand-new no-go.
- **Banked at honest tiers**, ledger 0 each: W1 `shown`-generic, W2/W3 `to-derive` default-BROKEN. The resident FLAGs W3 (BUILDS-ON-CLOSED: mu_linear), passes W1/W2; `validate.py` GREEN at net **+12**, 32 claims. Relayed before anything graduates above `to-derive`.
- **A resident bug was found and fixed en route** (not part of the physics): `_is_closed` substring-matched the bare token "refuted" inside rung3's *negation* "neither derived nor refuted", falsely flagging the OPEN rung3 (and its dependents rung5 / rung7_wz) as closed. Now negation-guarded; 2 regression tests added. See `RESULTS_resident.md`.

## Reproducibility
```
python3 calc/wz_sign.py            # the two-framing sign comparison + the no-crossing verdict
python3 provenance/validate.py     # the gate: GREEN, net +12, 32 claims
```
Pure stdlib; runs in well under a second.
