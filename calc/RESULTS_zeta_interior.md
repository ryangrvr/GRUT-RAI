# The {shear, bulk} interior — first pass (the window computation)


> **ANCHOR CORRECTION (2026-08-03, `calc/isw_exclusion.py`):** the ~32σ anchor underlying every window number below was computed and **not confirmed** — cross-channel N(1) ~ 2.0σ (Σ-corrected); **binding inversion** (DESI Σ₀ lensing binds, x < ~0.59 loose-upper per F-MAP); the numbers below stand as the first-pass historical record only.

*The first exploration of the region the p_tt interrogation opened: the admissible two-moduli family K = c₂·P^TT + c₀·P0s between the banked endpoints. Code: `calc/zeta_interior.py` (pure stdlib, self-tested). Register: `zeta_interior_family` (`to-derive`, ledger 0). Default-BROKEN. **Framing corrected by the firewall:** under linear scaling with N(0)=0, non-emptiness is *structurally guaranteed* (no finite bound can empty the window — a 32× stronger bound gives x < 1/512); the first-class computed content is the window **edge** and the **binding structure**, not non-emptiness.*

---

## Inputs (banked only — no new external numbers)

- **The family**: admissibility from `eft_operator_basis` (CHOSEN verdict: the interior is not excluded by any declared symmetry); endpoints banked in `mu_linear` — x=0 (TT-only) → μ=1 exactly; x=1 (trace-only) → μ=4/3, excluded **~32σ** by the low-ℓ ISW (+ separate-universe no-go).
- **The interpolation** (toy/scaling): μ(x) = 1 + x·α with α=1/3 — linear in the scalar coupling at leading order; endpoints exact. **Fence:** the precise x↔c₀ map inherits `mu_linear`'s conventions, not derived here.
- **Anchor-softness fence:** the window edge inherits **O(1) uncertainty in both directions** from the linear reading — endpoint-variance inflation would *shrink* the true window; a quadratic response component would *widen* it — and the ~32σ anchor is an in-house-derived exclusion significance (`calc/isw_exclusion.py` owed), not an in-repo computation; every number here is a linear rescaling of it.
- **The data**: the banked 32σ endpoint anchor with **linear amplitude-significance scaling** N_σ(x) ≈ 32x (leading-order reading of an amplitude-over-error statistic); the banked μ₀ = 0.05 ± 0.22 and Σ₀ = 0.009 ± 0.045 (SIGNATURE_AUDIT, overseer-verified) as cross-checks.

## The result — the window EDGE and the BINDING STRUCTURE, computed

| quantity | value |
|---|---|
| ISW-allowed admixture (2σ) | **x < 1/16 = 0.0625** |
| μ−1 ceiling | **α/16 ≈ 0.0208** (percent level) |
| μ₀ growth bound (2σ) | \|μ−1\| < 0.44 — weaker by ~21× |
| Σ₀ lensing bound (2σ, conservative Σ−1≈(μ−1)/2) | \|μ−1\| < 0.18 — weaker by ~9× |

**The ISW anchor binds; the window is set by it alone at current data** (and robustly: Σ−1 = (μ−1)/2 is *exact* in the inherited bookkeeping, η = 1/(1+α), and ISW binds for **any** slip in [1/μ, 1] — the Σ bound stays 4–9× weaker). The interior 0 < x < 1/16 is the **first region of GRUT's family whose observables are allowed up to the percent level — at the edge of current low-ℓ ISW sensitivity — rather than 20+ orders below any measurement** (a contrast of *ceilings* with the c₀=0 branch; the family **allows**, it does not predict — x has no lower observable floor). Non-emptiness itself was structurally guaranteed and is not claimed as a finding; what would *move* the result: the rigorous μ(c₀)/slip computation shifting the edge materially, or a derivation forcing x=0 (the interrogation showed none exists).

**The GRUT-natural-point map** (coherence note, u5/rung9a-facing — *not* a claim): the interrogation located α's legitimate linear-response carrier in the scalar channel — exactly the channel the interior opens. If the scalar coupling were α-normalized: x=α → ~10.7σ, **excluded**; x=α² ≈ 0.11 → ~3.6σ nominal (within the anchor fence's O(1) band, but disfavored). For scale, the 2σ window edge is x = α/16 in α units — a *data-derived* factor, not an α-normalization. No normalization is banked; this maps where GRUT-natural points fall, nothing more — and it is *testable structure*: the two simplest α-normalizations are already data-disfavored.

## What this does NOT do (fences, both directions)

- Does **not** demote `mu_linear` (that screen is open, separately — this calc *feeds* it: the interior is now computed, not hidden).
- Does **not** touch the TT channel (rung4's suppression stands) and does **not** rescue DESI (one passive channel — the no-crossing export `rung7_w3` untouched; any w(z) leg rides the already-booked rung7 dials, not recomputed).
- Banks **no new ledger input**: x is the c₀ modulus the admissible basis already carries; the *choice* c₀=0 is what `p_tt_ansatz`'s +1 books. Exploring the family it forecloses adds no dial.
- **Toy/scaling throughout**: linear interpolation; linear significance scaling off the banked anchor; the Σ leg conservative (slip not recomputed — owed); "future growth surveys reach σ(μ₀)~0.02" is an external number, owed, not asserted.

## Why this matters (the honest framing)

Until 2026-08-02 the program's empirical story was: every observable either equals ΛCDM exactly or is suppressed 20+ orders. That story is now known to be **conditional on c₀=0 — a chosen constitutive assertion**. This calc is the first look past that choice, and the answer is: the family has a **small but real viable interior**, its edge pinned by exactly one measurement (the low-ℓ ISW), with percent-level μ deviations inside. The next honest steps it sets up: the slip/Σ(x) computation (closing the conservative fence), the μ_linear demotion screen (now with the interior computed), and the u5 classification of what kernel *dynamics* (Debye vs other) live in the window.

## Independent firewall (2026-08-02) — amber → green after corrections

Two lenses + adjudicator; **all arithmetic independently verified exact** (window 1/16, ceiling α/16 = 1/48, cross-check ratios, natural points). **No red-class defect**: no stealth demotion of `mu_linear`, no unbooked input (x is the already-carried c₀ modulus), prediction-shading contained. The binding catch — **the horn-(b) framing was structurally dead on arrival**: under N_σ(x)=32x with N(0)=0 no finite bound can empty the window, so "non-empty window: LANDED" overstated the result's contingency; corrected everywhere to the honest content (the *edge* + the *binding structure*). Also corrected: "observables sit at percent level" → "allowed up to" (ceiling, not region); the anchor-softness fence added (O(1) both directions; the 32σ anchor is literature-level, not in-repo); the Σ reading upgraded from "conservative guess" to *exact-in-inherited-bookkeeping* with the all-slip robustness statement; the α/16 point relabeled data-derived; the 2σ convention unified; the ledger_note gains the collapse-not-a-dial sentence (nothing result-tier rests on the linear path — it is the to-derive content itself).
