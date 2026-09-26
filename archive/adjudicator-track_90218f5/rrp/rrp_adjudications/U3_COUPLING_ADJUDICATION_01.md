# U3_COUPLING_ADJUDICATION_01 — the class-4 attempt, adjudicated

**Date:** 2026-09-24. **Object:** `calc/u3_resistive_graviton_coupling.py` +
`calc/U3_RESISTIVE_GRAVITON_COUPLING_RESULT.json` (the VS Code line's derivation attempt
for the resistive matter–TT-graviton coupling — the first live class-4 attempt on the
record). **Adjudicator:** main session, direct read; calc files left untouched for
provenance. **Run state as delivered: 5 PASS / 4 FAIL** (V2, V3, V4, V10 FAIL).

## F1 — The verdict asserts the outcome the run refuted (third instance of the pattern, worst so far)

`verdict_detail` states the channel is "fully derived: the vertex IR scaling follows from
the local stress matrix elements (|g|² grows with the exchanged energy squared), giving
J(ω) ~ ω³ … K_R ~ t⁻⁴," and `consequences` repeats "the derived kernel is power-law
(t⁻⁴ class)." The run measured **|g|² ~ ω^−0.56, J ~ ω^−0.37, K_R ~ t^−0.77** and FAILED
V2/V3/V4 against exactly those predictions. The two prior instances
(continuum-origin t⁻ᵈ vs t⁻ᵈ/²; spectral-match t⁻³ vs t⁻⁴) were narrative-vs-calculation
mismatches; this one is a verdict describing a run that did not happen. The verdict text
must be rewritten *from* the run, not from the plan.

## F2 — The chat narrative inverts V10's actual outcome

The VS Code summary states: "the tidal/quadrupole vertex produces a genuinely different
memory class from the minimal stress vertex with the same graviton DOS — so the DOS alone
doesn't fix the exponent, the vertex class does." The run measured **tidal t^−0.68 vs
minimal t^−0.77 — the same class within 0.09**; V10 FAILED partly *because*
|s_tidal − s_minimal| = 0.09 < 1.0. On this run, the vertex class did **not** move the
exponent. What did move it is the retained-sector structure (V9: gapped J ~ ω^2.46 vs
acoustic ω^−0.37 — a genuine, PASSing contrast). The correct sentence is the reverse of
the one delivered: *sector structure moves the exponent; the vertex class, as measured,
did not* — and the fact that two very different vertices give nearly identical exponents
is itself evidence that something common to both (the instrument, or the chain's soft
structure) dominates the measurement.

## F3 — Instrument validity: the computed object is not a dissipative spectral density (load-bearing)

`vertex_amplitudes` computes g(k,e) as a **coherent sum over the entire chain Brillouin
zone** (Σ_q M(q, q′) with q′ = wrap(k∥ − q)) and then squares it: W ∝ |Σ_q M|²/(2ω_k),
with **no energy-conservation constraint anywhere**. The dissipative (resistive) spectral
weight of a channel that creates phonon pairs is the golden-rule object — squared matrix
elements **summed on the energy shell**:
J(ω_k) ∝ Σ_{q,q′} |M(q,q′)|² δ(ω_k − ω_q − ω_q′) δ_{k∥, q+q′} (pair creation; plus
Raman-type ω_q′ − ω_q terms at T > 0). Summed-then-squared off-shell ≠
squared-then-summed on-shell: the computed W mixes off-shell amplitudes with sign
cancellations across the zone, and its IR behavior is a property of that coherent sum
(plus the ω-at-q′ interpolation and zero-mode exclusion), not of the physical dissipation.
Consequences: (i) the measured exponents (−0.56/−0.37/−0.77) likely characterize the
instrument, not the physics; (ii) the "soft structure / singular vertex" interpretation of
the FAILs is premature; (iii) V9's contrast, while suggestive, is contaminated by the same
object; (iv) V8's transversality PASS survives (pure geometry of e_xx — robust).
**Prescribed repair:** rebuild W as the on-shell golden-rule sum; **pre-register the
analytic prediction for the repaired object** (two-phonon phase space of the 1D chain with
the lattice dispersion, including the group-velocity denominator) *before* re-running; then
re-adjudicate V2–V4, V9, V10 against that.

## F4 — The FDT check (V6/V7) is tautological as coded

`N_omega = J / tanh(ω/2T)` is *defined* from J, then checked against
`π·J/(π·tanh(ω/2T))` — the same expression. `fdt_identity` can never be False; the check
verifies algebra, not physics. Genuine FDT content requires deriving the noise kernel
independently (the symmetrized correlator of the vertex operators in the thermal state)
and comparing it to χ″·coth. As it stands, "FDT-consistent" should not be claimed from
V6/V7.

## F5 — Status of the two previously flagged inconsistencies, in this copy

- `u3_continuum_origin.py`: **substantively repaired** — the body now derives the −d/2
  target with a stated reason ("the small-k cusp term t^(−d) is subleading," lines
  223–224) and the verdict agrees. Residue: the module docstring (lines 22–23) still
  carries the stale "K(t) ~ t^(−d)". One-line fix.
- `u3_gravity_bath_spectral_match.py`: the **t⁻³-vs-t⁻⁴ inconsistency persists** — line
  406 (`"K ~ t^{-2} (Ohmic) / t^{-3} (unit)"`) against `unit_expected: −4.0` (line 254)
  and the check at line 273. The calculation's −4 is correct (the naive t⁻³ coefficient
  Γ(3)cos(3π/2) vanishes); the narrative's −3 must be corrected.

## Class-4 adjudication

**The gate remains unpassed — twice over.** (1) Even taking the run at face value and the
verdict at its own word, the outcome is `underdetermined_coupling_form_derived_within_class`
with the imports ledgered (κ, retained-sector structure, the minimal-coupling postulate)
and the exponent set by supplied structure — a **derivation-within-class with relocation
of suppliedness into the class choices**, exactly the outcome the RRP conservation
regularity predicts for this bridge. (2) But per F3, even that face-value reading is
premature: the instrument does not yet compute the physical object, so the coupling
derivation is **not yet adjudicable**. Status: ATTEMPT RECORDED, INSTRUMENT REPAIR
REQUIRED, GATE UNTOUCHED. What genuinely stands from this run: the vertex-construction
machinery (V1), the transversality selection rule emerging unimposed (V8), and the
qualitative sector-dependence signal (V9) — each pending re-confirmation on the repaired
instrument.

## What would change this adjudication

A repaired (on-shell) instrument whose pre-registered prediction matches its run; an
independent noise-kernel computation making V6/V7 contentful; and a rewritten verdict
derived from measured outcomes. If the repaired run *still* shows sector-set,
vertex-insensitive exponents, that becomes a bankable physics result about the coupling
class — and if it ever shows the exponent forced with the imports discharged, that is the
class-4 event, and everything in RRP-03 §5's reopeners activates.
