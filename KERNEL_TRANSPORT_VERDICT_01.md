# KERNEL-TRANSPORT INSTRUMENT — VERDICT

**Date:** 2026-09-25 · **Charter:** `KERNEL_TRANSPORT_CHARTER_01.md`,
pre-registration frozen at commit `c30f18e` before the run · **Instrument:**
`calc/kernel_transport_rule.py` (pure stdlib) · **Artifact:**
`KERNEL_TRANSPORT_RESULT.json` (sha `95f0f2a71dfce6a2…`) · **Battery: 11/11,
zero failures; integrator controls at machine precision** (dS closed form
reproduced to rel 1.4e-14; Wronskian drift 7.6e-13; SL(2,R)
state-independence 1.1e-13; superhorizon freezing 0.03%; wrong-sign mutant
detected at 80%). Register untouched; ledger 0.

## THE ANSWER TO THE OWNER'S QUESTION, IN ITS OWN THREE PARTS

**1. Can GRUT derive a dS→FRW transport rule from already admitted inputs?**

**Partially — and the boundary is now computed, not conjectured.**

- **What IS derivable: the transport exists as recomputation.** The exact
  free TT retarded/commutator kernel on the declared ΛCDM background is
  computable from admitted inputs alone (the C1-validated tensor primitive
  A4 + the declared background A7) — the instrument computed it on the full
  frozen grid. At free level, nothing further is needed to *have* the FRW
  kernel; what does not survive is the idea that it is the dS kernel locally
  re-rated.
- **What is NOT derivable: any local substitution rule.** No member of the
  declared family (rate chosen at observation, midpoint, or emission) stays
  within 10% of the exact kernel over the grid — best worst-case 34%
  (emission-rate member), worst 130% (the H₀-frozen member). And the premise
  every local rule assumes has **no small parameter in the real universe**:
  ε = −Ḣ/H² ≥ 0.4725 at every epoch z ≥ 0 of the declared background
  (0.75 at z_Λ, 1.18 at z = 1, 1.45 at z = 3).

**2. What additional structure would be required (derive-or-price, each item
typed):**

- **For a LOCAL/stationary description of the retarded kernel:** none exists
  beyond the derived validity domain below; outside it the kernel is a
  functional of the expansion history, and the instrument's O-MISSING
  co-occurrence records that at long lags NO local-rate evaluation
  reproduces it.
- **For the noise/KMS side (the Matsubara ladder)** — three named items, all
  RELOCATION-class (each a new priced input, none derivable from A1–A8):
  (i) a **state choice** on FRW — no Bunch–Davies analog; adiabatic vacua
  form an order-indexed family; (ii) a **temperature/KMS structure** — the
  matter+Λ background has no timelike Killing field, so T = H/2π (defined on
  the dS flows, A2/D6) has no derivation there; a "local temperature"
  T(t) = H(t)/2π is exactly the D6-class transport assumption the record
  already calls unpaid; (iii) a **proved stationary reduction** — the exact
  kernel is a two-time object; asserting a Δt-only form in any clock is the
  same unproved reduction Decision C's prerequisite 3 demands at contract
  scope, independently re-encountered here at free level.

**3. The nonuniqueness, as the structural result the owner named:** the
"apply the dS kernel with a local rate" prescription is **a family, not a
rule**, and its size is now measured: internal spread 0.003 of the kernel
scale at emission z_Λ, 0.04–0.10 at z = 1, up to **1.64 at z = 3**. The
members are equivalent exactly where none of them is needed and inequivalent
everywhere the cosmological comparison actually probes.

## THE DERIVED POSITIVE CONTENT — a validity domain, with numbers

At emission z′ = z_Λ = 0.296 (cosmic lag 0.241/H₀), **every** family member
matches the exact kernel to ≤ 0.3% at all three k. By z′ = 1 (lag 0.548/H₀)
the best member is at ~3%; by z′ = 3 (lag 0.803/H₀) all members are off by
34–130%. So the local dS transport is **derived-with-domain**: licensed at
the stated accuracy for lags ≲ 0.25/H₀, degrading through lag ~0.55/H₀, dead
before lag ~0.8/H₀ — at free level, from admitted inputs, with the exact
kernel as ground truth.

**Consequence for the demoted conditional calculation** (owner ruling §3):
its premises are now shown to be **disjoint**. Single-pole dominance needs a
kernel lag ≥ 4.33/H_*; the local dS transport that would carry the ladder
onto the real background is valid only for lags ≲ 0.25/H₀ and is O(1) wrong
by 0.8/H₀. **Any lag long enough to test the dominance claim lies far outside
the domain where the dS kernel is a licensed description of the FRW kernel.**
As posed, the old adverse comparison has no reachable physical content on
the declared background at free level — not because it was refuted, but
because its two requirements cannot hold at once.

## EFFECT ON THE FOUR UPSTREAM QUESTIONS (owner ruling §4)

- *Does the Matsubara ladder survive on the evolving background?* Not
  answerable until T-III items (i)–(ii) are priced: without a state and a
  KMS structure there is no ladder to transport. The ~367× temperature
  variation already priced the naive version.
- *How should the memory kernel be defined in cosmology?* As the two-time
  object K(t, t′; k) the instrument computed — exact, state-independent,
  admitted-inputs-only at free level. Stationary language is licensed only
  inside the derived domain.
- *Does low-ω K_R have a legitimate stationary limit?* The free-level answer
  reproduces Decision C's own prerequisite: only with a proved reduction;
  the exact kernel is not Δt-only, and the domain where it approximately is
  cannot reach low ω (lags ≳ 1/H₀ are outside it).
- *Does the old adverse finding have physical content?* See above: as posed,
  none reachable. A future re-filing must construct the comparison inside a
  licensed domain or bank the structure that extends one.

## PROPOSED REGISTER ANNOTATION (drafted, not applied)

EDIT 4 appended to `handover/REGISTER_EDITS_DRAFT_2026-09-25_clock.md`:
`background_time_translation_flow` gains the instrument's outcome (transport
= recomputation at free level; local rule derived-with-domain lag ≲ 0.25/H₀;
nonuniqueness measured; KMS-side structure named as three relocation-class
inputs). No tier moves; no ledger delta.

## DEFECT HISTORY (disclosed)

One drafting defect caught before any run: the cosmic-time accumulator was
mis-written (netted to a half-weight step) and was repaired to the plain
trapezoid before execution. No in-run failures; no post-run edits to any
verdict-bearing quantity. The orientation of the closed-form members against
the real unit-Wronskian basis is a single global sign convention, fixed once
and disclosed on the artifact face.

## HARD STOP

The transport verdict is recorded. The decision this stop waits on: **the
owner reads it and either selects the next instrument or reopens the
prediction/uniqueness tree.** Λ_R, Matsubara-inheritance, Π₀, and U5 remain
fenced. One computable follow-up is named (not opened): the exact kernel's
non-stationarity can be measured directly from the stored solutions
(same-lag/different-endpoint comparison), which would put a number on the
D3b obstruction the same way this instrument put numbers on the transport.
