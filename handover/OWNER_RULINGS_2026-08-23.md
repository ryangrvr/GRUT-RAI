# Owner rulings — 2026-08-23 (PENDING BANK GATE)

> **NOT APPLIED.** `claims.json` untouched. These are the owner's rulings, recorded for the bank
> gate and the adversarial pre-screen (CHARTER §1.3, §5.3). One checker flag on Ruling B, §B.4.

## RULING A — no universal ω_c; validity domain declared

**There is no presently derived universal ω_c.** The symbol is **sector-dependent** unless a
microscopic calculation establishes a common scale. Three incompatible meanings exist in the
record; selecting one globally would itself be a new assumption.

| use | value | ruling |
|---|---|---|
| tabletop / `rung8_falsifier` | 2π×689 rad/s | **RETAIN** as the staked tabletop cutoff |
| GW dissipation calc | ω_Planck | **RETAIN** as that GW EFT's UV cutoff |
| `wz_dark_energy.py` | 1e40·H₀ | **NOT a pinned universal cutoff** — model/ratio placeholder until derived |

**Every calculation must identify which cutoff it uses rather than inheriting a global ω_c by
notation.**

**Validity domain — closes the §8 gap (classification (c)):**

> All spectral claims based on the registered effective response are scoped to the low-frequency
> regime ω ≪ ω_c. The vicinity ω ~ ω_c is OUTSIDE the declared validity domain and cannot be used
> as an infrared/macroscopic prediction without a separate UV-complete derivation.

Operational screening window 0 < ω/ω_c ≤ 0.3. **Not elevated to a physical boundary** unless a
derivation establishes it.

*This directly closes the gap that let the cutoff-edge zero masquerade as an IR phenomenon.*
**Checker note:** `wz_dark_energy.py` is already self-flagged SUPERSEDED, so the reclassification
of 1e40·H₀ appears to carry no live downstream consequence — confirm at bank time.

## RULING B — split rung1; all Δ4 to the formalism half

    rung1_inin_formalism          SK / Feynman-Vernon influence-action structure
                                  tier: shown (borrowed, established)      delta: +4
    rung1_ontology_finite_memory  the gravitational vacuum IS a responsive medium with
                                  finite / single-pole memory
                                  tier: assumed (stance, explicitly not derived)   delta: 0

**Net unchanged.**

**Rationale (checker-verified):** the four priced ingredients — system/bath split · Gaussian /
linear-response truncation · Lorentzian causal background · 4d-covariant Ward gauge-orbit-zero
availability — are each prerequisites for *writing S_IF at all*. **None of them is the proposition
that the vacuum physically possesses finite memory.** The allocation is correct on the register's
own itemisation.

### B.4 — CHECKER FLAG, raised before banking, not an objection to the ruling

Under this allocation the register will carry **GRUT's entire distinctive content at Δ0**. This
session established that `rung1_ontology_finite_memory` carries `rung3` and the whole `rung7`
family, and that three of them collapse without it. A reader — especially an outside referee —
will see four *formal prerequisites* priced and the *ontological bet* free.

**The ledger's stated purpose is pricing underived inputs, and an un-derived ontological stance is
an underived input.** There is direct precedent: `background_time_translation_flow` was booked as a
**new +1** in August precisely because it was a presupposition doing work while unpriced. The
ontology is arguably the same shape.

**Three options, the owner's to choose:**

1. **As ruled — ontology Δ0, net unchanged.** Then the node should carry an explicit
   `ledger_note` saying the price is *not separately booked because the stance is the framework's
   founding commitment rather than an added input* — so the Δ0 is a recorded decision rather than
   an apparent oversight.
2. **Ontology +1, net moves +15 → +16.** Prices the stance honestly and matches the
   `background_time_translation_flow` precedent. Costs a net change.
3. **Re-examine whether any of the four belongs to the ontology rather than the formalism.**
   Checker's reading is that none does, so this likely returns option 1 or 2.

**Recommendation: option 1 with the explicit note, or option 2 — but not option 1 silently.** A Δ0
on the program's most load-bearing un-derived claim needs its reason on the node's own face.

## RULING C — rung7_wz stays Δ3; the "+2" wording is fixed

**Arithmetic verified:** three declared inputs — the free out-of-equilibrium amplitude ε · the IR
two-scale relaxation commitment τ₂ ~ 1/H₀ (**2 units**) · the single-departure-shape closure
(**1 unit**). Total **+3**, matching `ledger_delta`. **The defect is textual, not arithmetic.**

Replace *"the IR relaxation mode τ₂ ~ 1/H₀ booked in this claim's +2"* with:

> the IR relaxation mode τ₂ ~ 1/H₀, which constitutes **two of this claim's three declared inputs
> (+2 of the +3 total)**; the remaining +1 is the single-departure-shape closure.

**No net change.**

## Effect on Wall A

The microscopic calculation is no longer asked to rediscover an undefined cutoff or carry an
ambiguous composite rung1 price. Its task is unchanged and now unencumbered:

> **Does the gravitational response itself generate the finite-memory / low-ω structure that
> rung3 currently assumes?**

Entry gates unchanged: **G0** mode-counting declaration · **G1** Ohmic plant (a *precondition*, not
a check — if the machinery cannot recover a planted Ohmic bath, the s=3 vs s≤1 conflict is not
adjudicated whatever it returns) · **G2** Σ → G_R^TT → K_R · **G3** actual IR functional form, with
classifications s≥2 / s≤1 / NOT-A-POWER-LAW / UNRESOLVED and the convergence integral
Re χ(0) = (2/π)∫ Im χ(ω′)/ω′ dω′ computed and reported in **every** case.

**And the solver is blind to which outcome favours GRUT.**
