# U3_COUPLING_ADJUDICATION_03 — the "Cherenkov no-go" verdict, adjudicated: REFUTED

**Date:** 2026-09-24. **Object:** the 19:13 rebuild of
`u3_resistive_graviton_coupling.py` + RESULT (builder tree), verdict
`DISDERIVED_for_acoustic_chain_cherenkov_no_go`, decisive branch V1b.
**Adjudication instruments:** the sealed ledger (T2_…_01, d2da3a5, three blinded
routes + two adversarial numerical verifications) and a fresh independent checker
written for this adjudication, `calc/adjudication_03_channel_check.py` (my copy,
committed with this file; no code shared with the builder's).

**Verdict on the verdict: REFUTED.** The acoustic two-phonon graviton channel is
OPEN, not kinematically empty. The no-go rests on one false inequality and one
inverted control. Reality has veto power and a true no-go would have been a welcome
result — this one fails on instrument logic, not on direction.

## F1 — The kinematic inequality is false for the channel that matters

The verdict_detail's load-bearing sentence: "omega_q + omega_q' < |q + q'| = k_par
<= omega_k **for every pair**." The step |q| + |q′| = |q + q′| holds **only for
same-sign (co-propagating) pairs**. For opposite-sign (counter-propagating) pairs
|q| + |q′| > |q + q′| — arbitrarily so — and the pair energy reaches any ω ≤ band
top while the pair momentum stays at the graviton's small k∥. The sealed ledger
derived exactly this split: same-sign closed at all ω (by that inequality),
opposite-sign OPEN at every graviton angle with roots a = ω(1+μ)/2 + O(ω³),
b = ω(1−μ)/2 + O(ω³). The builder's own first kinematic report ("oblique modes
resonate via the graviton's transverse momentum") had it right; the new verdict
over-generalized the aligned/same-sign closure into a full no-go by dropping the
same-sign hypothesis while keeping the conclusion.

**Direct demonstration (T1 of the checker, no tolerance anywhere):** Brent
root-finding on 2sin((k∥+b)/2) + 2sin(b/2) = ω across ω ∈ {0.3, 0.6, 1.0, 1.5},
μ ∈ {0, 0.3, 0.6, 0.9}: **16/16 exact interior on-shell roots at machine-precision
residual (≤ 2e-16)**, matching the sealed analytic root formulas (e.g. ω = 1,
μ = 0.3: a = 0.6568, b = 0.3568 vs predicted 0.65/0.35 + curvature).

## F2 — V1b's null logic is inverted: it reads the OPEN-channel signature as emptiness

`onshell_pair_weights` contains **no 1/dω normalization**; V1b then treats
"W scales ~linearly in dω and extrapolates to zero" as proof of emptiness. But a
windowed δ-approximant without its 1/dω factor scales linearly in dω **precisely
when the shell is a continuous open curve** (count in window ∝ dω). The physical
golden-rule object is the density W/dω. From V1b's own recorded numbers
(1.503e-6 / 7.522e-7 / 3.790e-7 / 2.018e-7 at dω = 0.06/0.03/0.015/0.0075):
W/dω = 2.51e-5, 2.51e-5, 2.53e-5, 2.69e-5 — **constant to ~7% over an 8× tolerance
range. V1b's own data demonstrates a finite, convergent golden-rule density — the
opposite of its interpretation.** Checker T2 reproduces this independently (W/dω
drift 1.27× over 16×, with sparse-count noise at the smallest window).

**What true emptiness looks like in this very instrument** is on the builder's own
record: V9's gapped chain below threshold — weight **identically 0.000e+00 at
finite dω** (gap > window ⇒ zero count), not weight halving with the window. The
same-sign channel likewise: zero roots at every ω. Halving ratios of 0.50 are the
fingerprint of an open channel measured without δ-normalization; V1b as built
returns "empty" for every open continuous channel in physics.

## F3 — Consequences for the exponents, and between-run instability

The 18:49 run's J ~ ω^5.03 — which matched the sealed blinded prediction mapped
through that run's conventions (ω⁸ − 2 − 1 = ω⁵; ADJUDICATION_02) — is the physics,
now relabeled "tolerance leakage": an inverted attribution. Separately, the 19:13
run reports V2 ω^2.11 / V3 ω^2.38 where the 18:49 run measured 4.88 / 5.03 with
nominally the same object — an undocumented instrument change between runs. No
exponent from the 19:13 instrument is bankable until the normalization is declared
(G1), the coefficient is mapped (G6), and the counterfactual nulls are run (G8).

## F4 — The FDT check remains tautological, now at machine precision

The "de-tautologized" check builds N = πJ(2n_B+1)/2 from Bose–Einstein occupation
and matches it to the coth form at 3.09e-16. But coth(ω/2T) ≡ 2n_B(ω) + 1 is an
algebraic identity — machine-precision agreement is the signature of comparing an
expression to itself. (The previous run's π/2 bookkeeping slip was fixed; the
non-independence was not.) F4 of ADJUDICATION_01 stays open: a genuine FDT check
derives the noise kernel from the microscopic symmetrized correlator and compares
it to χ″coth. Detailed balance (1.75e-16) is likewise an identity, not a sub-test.

## What genuinely stands from the 19:13 run

The pre-registration culture (predictions with tolerances fixed in-file before
measurement); V4's box limitation kept as FAIL; V9's van Hove fit honestly failed
and only the exact below-threshold zero banked; the aligned/same-sign closure
itself (true, and doubly redundant with e_xx = 0); the gapped threshold at exactly
2Ω; tidal +2 pointwise linearity; passivity. The verdict-from-the-run discipline
was followed — the run's error is upstream, in the control's null logic, not in
narrative drift. (Precision note for the record: on the lattice even the aligned
channel reopens at a curvature-scale root b ~ ω³/24 — TT-dead, physically
irrelevant, but "no interior solution at aligned incidence" is exact only at
strictly linear dispersion.)

## Prescribed repairs (priority order)

1. **V1b′ — replace the control's null:** test the DENSITY W/dω for convergence to
   a finite limit (open) vs collapse to zero (empty), with the two true-emptiness
   positive controls run alongside: same-sign-only count (0 at every dω) and the
   gapped chain below threshold (0 at every dω). V1b's current form must be
   retired; its recorded data already passes the corrected test as OPEN.
2. **Exact-root production cross-check (sealed G10):** a tolerance-free instrument
   (root-finding on the shell equation, Jacobian-weighted) as the second instrument
   class; the windowed sum then only needs to agree with it.
3. **Declare the normalization (G1), map the coefficient (G6), run the
   counterfactual nulls (G8):** kinetic-only vertex, linear-dispersion switch,
   lattice-sine vertex — with their pre-computed outcomes under the declared
   convention. This also resolves the 5.03 → 2.38 between-run shift.
4. **Rewrite the verdict:** the acoustic channel is open; the coupling line returns
   to ADJUDICATION_02's standing — first two-sided exponent-class agreement,
   coefficient level pending.
5. **FDT from the microscopic symmetrized correlator** (F4, still open).

## Correction of an attribution in circulation

The no-go was relayed as "matching the reviewer's predicted fork." For the record:
the sealed fork predicted **open channel with J ~ ω⁸ task-literal (ω⁵ under the
18:49 conventions), or else the derivation falls**; the Cherenkov closure was
sealed as a side-prediction for the **same-sign channel specifically** ("exactly
zero on-shell roots at every ω — the builder's Cherenkov closure"), never as a
no-go for the coupling. The next-question proposed under the no-go ("which sectors
satisfy ω_pair ≥ ω_k") dissolves: the acoustic sector already satisfies it at
every oblique angle.
