# The load-bearing number, computed: the ISW exclusion of μ(x) = 1 + xα

*Code: `calc/isw_exclusion.py` (pure stdlib; imports `mu_slip_interior.py` as the banked source of truth; self-tested). Pre-registered kill-conditions KC1–KC4 and the directional guard (default-broken toward the ~32σ being inflated) in the module docstring. Outcome: **(b) SUBSTANTIALLY WEAKER — the banked ~32σ is retired.** All numbers below are the **post-firewall** record (the same-wave firewall's Σ-correction B1 applied; see the firewall section).*

---

## The verdict

| quantity | banked (pre-wave) | computed (2026-08-03, Σ-corrected) |
|---|---|---|
| endpoint exclusion, **cross-correlation channel** (the observable the register cites) | ~32σ (asserted) | **N(1) ~ 2.0σ** (1.97 central; KC3 band ~0.6–4.8) — and at central inputs the cross channel alone no longer 2σ-excludes *any* x ≤ 1 (band-hi corners still do) |
| mechanism | "μ>1 enhances potential decay → ISW excess" | **backwards**: μ>1 *strengthens growth* → decay suppressed; potential *grows* for z > z* ≈ 0.81; the model suppresses the signal to **~0.57× the template** (A(1) = +0.57 with the Weyl-source Σ factor) |
| 2σ window edge | x < 1/16 (= 2/32), "ISW binds alone (growth ~21×, lensing 4–9× weaker)" | **binding inversion** (band-robust vs the retired 1/16): DESI Σ₀ lensing binds at **x < ~0.59** — *central-inputs and loose-upper per the named F-MAP fence*; μ−1 ≤ ~0.20, Σ−1 ≤ ~0.10 (loose-upper ceilings). Channel identity is central-inputs-grade (mid-band corners let the cross channel co-bind ~0.44–0.56) |
| the channel where a 32-class number could live | — | the **low-ℓ TT auto-power**: estimate-grade, order-10²σ-class at x=1; estimate-grade 2σ edge **band x ~ 0.03–0.14** (filter/normalization-sensitive; 98% of the unfiltered integrand sits at z>3 at near/super-horizon k where PART E's own logic forbids μ-modified growth on adiabatic modes). **NOT BANKED**; its rigorous calc is the **owed gate** for interior viability above x ~ 0.06 and the natural-point discriminator |

**The structural cap (KC1, why 32σ was never possible here):** for a signal-suppressing model (A ∈ [−1, 1]) the cross exclusion is capped at (A_obs + |A|)/σ_A — **~9σ central, ~12σ at band extremes**. Detection (~4.5σ, definitional = A_obs/σ_A) and exclusion computed separately; their proximity for a suppressed-signal model is physics, not conflation.

**KC2 (linearity):** the N(x) curve is computed; deviation from N(1)·x was −1.8% at the pre-B1 cross edge — the scaling assumption was fine; the *anchor value* was the problem.

**KC3 (no anchor-shopping):** A_obs = 1.00 ± 0.22 central (combined ~4.5σ, consistent-with-ΛCDM); swept A_obs ∈ [0.85, 1.40], σ_A ∈ [0.20, 0.32], ℓ_eff ∈ {10, 20, 40}, kernels z_med ∈ {0.15, 0.45, 1.1} (joint-fit combination; per-kernel A(1) = {+0.79, +0.54, −0.06} with Σ — the sign flip with depth is the growing-potential regime). A survey-S/N-weighted joint fit lands inside the band; the worst single-kernel cherry-pick reaches only ~7σ — the verdict class is safe. Radiation ignored from a=10⁻⁴ (growing-mode attractor → ratio-irrelevant for the z<4 cross integrand).

**KC4 (leg accounting):** the endpoint exclusion is **multi-leg**: ISW-cross **~2.0σ** (computed) + DESI Σ₀ **~3.5σ** (independent; joint ~4σ-class) + the **separate-universe structural leg** (EdS-quantified: p(4/3) − p_SU = +0.186 ≠ 0; comoving-gauge identification; conditional on adiabaticity + the presupposed dilatation bridge). The TT-auto channel is a **prospect, not a leg**. No single ~32σ kill exists in the computed record.

## The separate-universe leg (Part 3 — dated assessment, 2026-08-03)

EdS-level demonstration (PART E): a super-horizon adiabatic mode is a shifted FRW background whose comoving-gauge growing mode (δ ∝ a) is fixed by the Friedmann equation; super-horizon μ=4/3 forces δ ∝ a^1.186 — **inconsistent**. **Establishes:** the trace-only branch *as banked* is internally inconsistent, dataset-independent. **Does not:** constrain a strictly sub-horizon modification. **Score: USABLE-BUT-CONDITIONAL** (owed residue: adiabaticity + the dilatation bridge the L0 screen scored "relocated, not derived"). **Load-bearing map:** the structural leg carries the endpoint-as-banked; the empirical legs (~4σ-class joint) back it independently.

**Reopening-trigger status (relayed, no tier edit):** condition 1 **FIRED** (~2.0σ < the ~4–5σ headline); condition 2 **NOT FIRED** (leg scored usable). Conjunction fails → **no demotion**; `mu_linear`'s statement re-weakened to the computed record.

## Independent firewall (2026-08-03) — AMBER → fixed, all lenses converged

Four lenses (two physics adversaries with replication rights, KC-compliance, propagation sweep) + adjudicator; every disputed number independently re-derived. **B1 (physics, confirmed by adjudicator rerun):** the Weyl-source Σ(x) factor was omitted from the cross amplitude — constant Σ cancels in decay *rates* but not in the template-relative *amplitude* (the register's own banked lensing line puts Σ in the Weyl potential); corrected A(1) = +0.566, N(1) = 1.97, no in-family 2σ cross edge at central inputs; the headline (32-retirement, ~2σ-class, binding inversion) **survived and slightly strengthened**. **B2 (named fence added):** DESI's Σ₀ multiplies an Ω_Λ(a)/Ω_Λ0 shape while the family's Σ−1 is constant-in-a — the direct identification makes x < ~0.59 **loose-upper** (shape-weighted mapping plausibly 2–3× tighter; direction TIGHTER); natural points de-symmetrized (x=α² survives everything; x=α's un-disfavoring is F-MAP-fragile). **B3:** four stale headline sites re-propagated. Tightenings applied: auto estimate banded (~0.03–0.14 edge, point value never quoted), TT-auto demoted from "leg" to "prospect" in all statement fields, KC1 cap quoted as a band (~9–12σ), gauge caveat on the SU leg, the superseded ToE changelog tag, `p_tt_ansatz` pointer, partial-discharge mark on the separate-universe owed item. Rejected findings recorded in the workflow journal (incl. the x=α "re-disfavoring" as computed — held at plausible-grade).

## Propagation applied (same wave, post-firewall numbers)

`mu_slip_interior.py` anchor constants (N_CROSS_ENDPOINT = 2.0 banked, computed 1.97; EDGE_CROSS retired; EDGE = lensing formula ~0.594 with F-MAP fence; AUTO_EDGE_EST banded) — drift-pinned both directions by the harness regression and the calc selftest; harness `OBSERVATIONS mu_window_edge_x` + `forward_mu` 2.0x; register (`mu_linear` statement/BC/overturning/tier_note, `zeta_interior_family` statement/BC/differentiator, `p_tt_ansatz` BC pointer, `sources.json isw_lowl`) and docs (ToE §2.8 + no-go list + changelog, NO_GO_LEDGER entry 2 + hybrid strength label, What_Survived, SIGNATURE_AUDIT, STATE) all carry the Σ-corrected record; "ISW binds alone / ~21× / 4–9×" and "natural points data-disfavored" overturned or de-symmetrized everywhere live; historical first-pass records preserved under dated correction marks.
