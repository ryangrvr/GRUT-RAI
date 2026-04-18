# V8 Roadmap Note — Torsion and the CTP z_a Sector

**Date:** April 2026
**Status:** Framework-level observation flagged for V8. Quantitatively
Planck-suppressed for the cosmological sector; potentially relevant for the
4/8 closure ladder at near-Planck H.

## The structural observation

In the Palatini (first-order) formulation of gravity, the spin connection
ω_μ^ab is independent of the metric. CTP-doubling in the Palatini
formulation produces (ω_+, ω_-) → (ω_r, ω_a) alongside the metric doubling.

**Claim:** ω_a is the natural home for torsion in GRUT's CTP. Einstein-Cartan
torsion couples directly to fermion spin through the spin connection; the
antisymmetric CTP channel ω_a is where torsion-like gravitational
decoherence of spinning matter naturally lives.

**Why it's structural rather than cosmetic:**
- Fermion stress-energy includes ψ̄γ^μω_μψ
- CTP noise kernel on spinning matter already includes this contribution
- Torsion in Einstein-Cartan is algebraically the same operator structure
- The decoherence channel for quantum angular momentum IS torsion-coupled

## Where the parallel is loose

- z_a is antisymmetric under CTP branch swap; torsion T^λ_μν is
  antisymmetric under lower-index swap. These are different index spaces.
  The structural tightening requires Palatini CTP, not metric-only CTP.
- Standard metric CTP with induced Levi-Civita connection carries no
  torsion, because no torsion exists to begin with.
- The claim "torsion + CTP parallel" is therefore conditional on using
  the Palatini formulation. Metric CTP does not force the identification.

## Quantitative irrelevance for the cosmological sector

The Hehl-Datta torsion contact term in Einstein-Cartan gives a
contribution of order G × H² to dimensionless observables when integrated
over S^4 (volume ~1/H^4 cancels the H^6 from spin density squared
times the G prefactor):

| H [GeV] | G H² = (H/M_Pl)² | vs Planck-match 4×10⁻⁴ |
|:---:|:---:|:---:|
| 10¹⁰ | 7 × 10⁻¹⁹ | 15 orders below |
| 10¹³ | 7 × 10⁻¹³ | 9 orders below |
| 10¹⁶ | 7 × 10⁻⁷ | 3 orders below |
| 10¹⁸ | 7 × 10⁻³ | ~order of magnitude above |

**Conclusion for cosmology:** torsion does not shift R_GRUT at any
precision we can observe. The framework's Ω_Λ = 0.6886 prediction is
robust against torsion contributions by 9+ orders of magnitude.

## Where it might actually matter

The 4/8 closure ladder in GRUT operates in the near-Planck regime. At
H ~ 10¹⁸ GeV, torsion corrections reach the percent level. **This is the
regime where the Palatini-CTP observation could have real computational
consequences.**

Specifically:
- Quantum gravity corrections to the anomaly coefficients at H near M_Pl
  need Palatini-CTP treatment to capture spin-connection doubling.
- The 4/8 closure conditions on the Keldysh contour may have non-trivial
  consistency requirements when ω_a is included alongside g_a.
- Spinor-gravity entanglement generation could have torsion-channel
  contributions that metric-only CTP misses.

None of this changes the cosmological constant prediction. It's a
completeness issue for the quantum gravity sector.

## What this does NOT establish

The suggestion that torsion corrections could explain "why K₁ ≈ K₂" in
the ratio analysis lacks a clear mechanism. K₁ and K₂ are 3-loop CTP
tensor projection coefficients for specific operators; torsion adds a
different class (4-fermion contact). There's no structural argument for
why torsion would equalize the two dressings rather than shift them both
uniformly. Flagged as speculation, not a structural argument.

## Recommended framing in V8

One paragraph in the theory document:

> GRUT's CTP formalism, when formulated in the Palatini (first-order)
> variables, naturally doubles the spin connection alongside the metric.
> The antisymmetric CTP channel ω_a is the locus where Einstein-Cartan
> torsion would live. For current cosmological observables this channel
> contributes at order G × H² ~ 10⁻¹² at inflationary scales, far below
> observational precision. In the near-Planck regime relevant to the 4/8
> closure ladder (H ~ M_Pl), torsion becomes a percent-level correction
> and requires explicit Palatini-CTP treatment. The noise kernel for
> spinning matter already carries the torsion-coupled decoherence channel
> at leading order; the full Einstein-Cartan completion is a V8 frontier
> direction.

## Follow-up if pursued

A concrete computation would compare the fermion noise kernel on S^4
with and without the spin-connection terms that torsion would modify.
If the spin-connection contribution is a significant fraction of the
total fermion noise kernel at H ~ M_Pl, Palatini-CTP becomes mandatory
for the closure ladder. If suppressed at all relevant scales, metric-CTP
is complete.

## Priority

**Not urgent.** The cosmological sector is robust against torsion by
construction (Planck-suppression dominates). The V8 completion of the
quantum gravity sector is a natural place to do this work. Can be
deferred until the 3-loop tensor projection specialist task is resolved.

## Bottom line

The torsion-CTP connection is genuine at the framework level when
Palatini formulation is adopted. Numerically it's irrelevant for the
cosmological constant prediction. It's a frontier item for the quantum
gravity / closure-ladder sector, noted here so it isn't lost, but not
on the critical path for current work.
