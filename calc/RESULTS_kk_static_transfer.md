# RESULTS — kk_static_transfer: the dissipative-to-static transfer question, answered

*Calc: `calc/kk_static_transfer.py` (pure stdlib, selftest green, four-mutant battery in
`provenance/mutation_registry.py`, all verified killed). Pre-registered:
`provenance/prereg/PREREG_KK_STATIC_2026-08-09.txt` (sha256 `1f9c3bf6f2954087…`, sealed before
the calc existed); scored in `provenance/prereg/RESULT_KK_STATIC_2026-08-09.txt`. This is the
register node `kk_static_transfer`'s owed calc — the load-bearing gap between "the family has a
floor" (`x_no_pin_theorem`) and "μ has a floor" (the claim any reader actually wants). Outcomes
**(b) and (c) jointly** — the pre-stated expected landing and the default-broken set; the
flattering outcome (a) did not bank.*

## The identity that decides everything

For a retarded channel coefficient χ(ω) with real high-frequency (instantaneous/contact) part
χ_∞ and convergent dispersion integral:

> χ(0) = χ_∞ + (2/π) ∫₀^∞ dω · Im χ(ω)/ω

Passivity makes the integral **nonnegative** — so the dissipative floor pushes the static
modulus up *from χ_∞*, and never below it. The entire transfer question collapses onto the sign
of χ_∞: a **reactive contact datum that passivity, causality, and the KMS lock are all
structurally blind to** (verified: the counterexample's Im χ and KMS noise are bit-identical
with and without its contact term). Verified to machine precision (10⁻¹⁵) against closed forms.

## (b) — Unconditional transfer REFUTED, permanently

The counterexample, pre-named by form in the sealed prereg: χ(ω) = −1.0 + 0.4/(1 − iω).
Machine-verified: retarded-analytic (only pole at ω = −i, lower half-plane), passive at every
probed frequency, consistent with the two-point KMS/FDT lock (the only KMS content rung2
banks; no many-body-realization claim) — and **χ(0) = −0.6 < 0**. A passive kernel with a negative
static response exists inside the declared structure. **No artifact may ever quote an
unconditional "μ has a floor."**

Context, analogy-grade per the prereg (transfers nothing): the register already banks that
linearized EH's own scalar-channel coefficient is a *negative ω-independent contact structure*
(`p_tt_ansatz`, exact arithmetic) — negative real contact terms in gravity's scalar sector are
not exotic; the counterexample class is not a pathology.

## (c) — The transfer criterion, at its exact edge

*(Precision-corrected in-wave by the adversarial verification pass: the first draft's headline —
"exactly as strong as the single-pole conjecture" — was a false equivalence; sufficiency was
proven, not equivalence.)* Given passivity, the identity makes the criterion exact:

> **Passivity gives χ(0) ≥ χ_∞.** Therefore χ_∞ ≥ 0 is **sufficient** for χ(0) ≥ 0. It is
> **not necessary** — the dissipative integral can lift a negative χ_∞ above zero — and
> passivity alone supplies **no necessary condition on χ_∞ whatsoever**. What is exact is that
> χ_∞ ≥ 0 is the **tightest premise on the instantaneous part that yields the guarantee across
> the whole admissible class** (for any χ_∞ < 0 there is an admissible kernel with χ(0) < 0 —
> the counterexample family). The vanishing class (χ_∞ = 0) gives the equality form, and
> `rung3_single_pole`'s Debye family is in it — so **conditional on rung3's conjecture,
> x_static ≥ 0**; the floor does not die if single-pole falls; **unconditionally, nothing**.

*Editorial note, recorded so the third editor knows why this sentence keeps going wrong: this
headline has now been wrong twice, in two different ways — first as a false equivalence
("exactly as strong as the single-pole conjecture"), then as a false biconditional ("χ(0) ≥ 0
iff χ_∞ ≥ 0", true only at class level, false of an individual kernel — a passive kernel with
χ_∞ < 0 can still land χ(0) ≥ 0 if its dissipative integral is large enough). Both caught by
review, neither by the author on first pass. The sentence is hard because it is a claim about a
CLASS being quoted as a claim about a KERNEL, and English collapses the two. Edit accordingly.*

Whether GRUT's vacuum kernel has χ_∞ ≥ 0 is bath/UV structure — rung3's domain, priced there,
never decided here. (If the admissible class's UV behavior forces further subtractions,
additional unconstrained constants enter and the condition only tightens — also rung3's.)

## The firewall event of this wave

The first quadrature (uniform Simpson on a truncated half-line) under-resolved relaxor features
narrower than its step; the selftest rejected the reconstruction against closed forms (errors to
the percent level) and FAILED before any prose existed. Fix: the tan substitution ω = tan θ maps
the half-line to a finite interval where the transformed integrand is smooth and finite at both
ends — a fix of the method, not a loosening of the tolerance. Machine precision after; stability
verified under n-doubling on the widest-timescale sample, which is the case the broken version
actually failed on.

## Fences

No TT-channel or ceiling statement; no Israel–Stewart number; no kernel-class assertion about
GRUT's actual vacuum; the KC4 guard carried (a floor licenses no channel's vanishing); ledger 0
(structural mathematics on priced inputs — the conditional hypothesis is priced at rung3,
counted once, there). Register disposition: the answer is staged onto `kk_static_transfer`
(to-derive → derived-pending, pending exactly the sign of the vacuum kernel's instantaneous
part — rung3's UV/contact domain) and refines
`x_no_pin_theorem`'s fence — **held at the bank gate's TIER-OR-LEDGER flag for the overseer;
not self-accepted.**
