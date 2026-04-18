# Direction 4 — Higgs Thermal Restoration at T_GH

**Date:** April 2026
**Status:** Confirmed restoration, sharpened scale ambiguity, weakened M_Z argument.

## Confirmed

**EW symmetry is emphatically restored at T_GH.**

Using Dolan-Jackiw leading-order thermal effective potential:

    c_SM = 3 y_t² + (9/4) g_2² + (3/4) g_Y² + 6 λ_H = 4.786

    T_c² = 24 m_H² / (2 c_SM)
    T_c  = 198 GeV

At T_GH = 1.59 × 10¹² GeV:
- **T_GH / T_c = 8 × 10⁹** (restoration by 10 orders of magnitude)
- Higgs VEV = 0
- All Yukawa masses vanish: m_f = y_f × ⟨φ⟩ = 0
- Thermal masses: m_therm ≈ g·T_GH ~ 10¹² GeV

## Key structural finding: Osborn ε is phase-independent in form

Osborn's K coefficients (R_ψ, R_φ) are **group-theoretic sums** over matter
multiplicity — they do NOT depend on Higgs VEV. So in both phases:

- SU(3): K = 17 (6 Dirac quarks, T_F=1/2)
- SU(2): K = 6.5 (fermion doublets + Higgs doublet)
- U(1)_Y: K = −40.4

The only thing that changes between phases is **which α to use**. This
reduces the phase question to the scale question.

## The scale scan under V7 structure (R = ε)

| Scale | µ [GeV] | α_s | ε_SU3 | Ω_Λ | vs Planck |
|:---|:---:|:---:|:---:|:---:|:---:|
| M_Z (vacuum calibration) | 91 | 0.118 | 1.160 | 0.682 | −1.0% |
| T_c (EW transition) | 198 | 0.107 | 1.145 | 0.706 | +2.5% |
| **T_GH (thermal)** | 1.6 × 10¹² | 0.029 | 1.039 | 0.892 | **+30%** |
| π·T_GH (HTL optimal) | 5.0 × 10¹² | 0.028 | 1.037 | 0.898 | +30% |
| H_inf (curvature) | 10¹³ | 0.027 | 1.037 | 0.899 | +30% |

Standard thermal field theory practice (Braaten-Pisarski hard thermal loop
scheme) picks µ = π·T. All three thermal/curvature scales give the same
answer (Ω_Λ ≈ 0.90) because they're within a factor of 2 of each other.

## The author's subtlety: CTP fluctuations probe all scales?

The argument raised: CTP is out-of-equilibrium; the forward/backward
asymmetry is a departure from the thermal state; long-wavelength modes
could probe broken-phase physics even on a restored-phase background.

**The geometric fact that refutes this on S⁴:**

On S⁴ of radius 1/H at H = 10¹³ GeV:

| Field type | Min eigenvalue | Min energy |
|:---|:---:|:---:|
| Fermion | λ_0 = (3/2)² H² = 2.25 H² | **1.5 H = 1.5 × 10¹³ GeV** |
| Scalar | λ_0 = 0 (zero mode) | 0 (needs thermal mass regulator) |
| Vector | λ_0 > 0 | > H |

**There are no fermion modes on S⁴ below ~H ≈ 10¹³ GeV.** The minimum
fermion energy is 6 × 10¹⁰ times the EW scale. The "broken-phase at
long-wavelength" intuition relies on arbitrarily-low-energy modes
existing, which is a property of flat infinite space, not compact S⁴.

The noise kernel's "IR-dominant" mode from our spectral test was at n ≈ 12.
Energy scale: √((12+3/2)²) H = 13.5 H = 1.4 × 10¹⁴ GeV. That's higher
than H, not lower. The "IR" of the noise kernel is IR with respect to the
S⁴ spectrum, but it's at energies vastly above the EW scale.

**Consequence:** the IR-dominance argument does NOT rescue µ = M_Z. The
IR-dominant modes are at thermal/curvature scales.

The scalar (Higgs) zero mode IS at sub-EW effective energy in the broken
phase (m_H = 125 GeV < H). But:
- In the restored phase, m_Higgs_thermal ~ H/7, no longer sub-EW
- ε depends on R_φ (scalar multiplicity, = 1 for Higgs), NOT on Higgs
  propagator magnitude
- So the scalar IR enhancement doesn't directly enter ε

## What survives as M_Z arguments (after D4 sharpening)

1. **Vacuum calibration interpretation:** M_Z is the observational input
   where α_s = 0.118 is measured. The CTP asymmetry (g_+ − g_-) measures
   a difference between external classical coupling sources — not a
   thermal quantity. This COULD justify µ = M_Z, but it requires the
   CTP observable to be formally a "vacuum-structure functional" rather
   than "thermal physics at T_GH."

2. **V7 specifies it:** if V7 §26 explicitly says R = ε(SM, M_Z), that's
   a definition to accept and verify, not a scale to re-derive.

3. **Thermal correction: ε(µ, T) may have structural T-dependence that
   effectively returns the M_Z-value** in some resummation scheme.
   Speculative.

What no longer works:
- "Matter is defined at M_Z" — NO, matter is massless in the restored phase
- "IR dominance picks sub-EW scales" — NO, IR modes on S⁴ are at scale ~H
- "Broken-phase physics at long wavelength" — NO, no sub-EW modes exist on S⁴

## Revised probability

Before D4 analysis: 50-60% M_Z wins.
After Part 1-5 of D4: 45-55%.
**After the S⁴ minimum-energy analysis:** 35-45% M_Z wins.

The drop from 45% to 35% reflects: the IR-dominance argument, which was
one of the main supports for M_Z, is weaker than I previously represented.
The IR-dominant modes on compact S⁴ are at ENERGIES comparable to H, not
at sub-EW energies. "IR of the S⁴ spectrum" ≠ "low physical energy."

The 35-45% range is what remains when we take seriously:
- V7's structural claim (§12) making R = ε directly (K₂ = 0 case)
- Standard thermal QFT favoring µ ~ πT_GH
- No physical S⁴ mode below the EW scale
- But still the vacuum-calibration argument on the other side
- And the fact that V7 MAY specify M_Z as a definitional choice

## What the specialist now needs specifically

**Q_D4_primary:** Does GRUT's CTP construction in §26 formally identify
the observable as a "vacuum-structure functional" (where µ = M_Z is
natural) or as "thermal physics at T_GH" (where µ ~ πT_GH is natural)?

If the latter, the 30% miss from Planck is the honest prediction and the
framework's cosmological sector needs retirement or refinement.

If the former, we need an explicit structural argument that survives
scrutiny of standard thermal QFT practice.

## Tenth correction tally

10 corrections caught, 0 hallucinations passed through. The ratio
near-invariance argument (correction 10 walked it back) was real but
inapplicable to V7's posited structure. The IR-dominance argument is
now also weaker than I previously claimed when the S⁴ minimum-energy
structure is accounted for.

The framework's cosmological sector prediction at 0.04% Planck match
remains ON THE TABLE but is now supported by fewer independent
arguments than I had stacked. It reduces to:

- V7's structural claim R = ε(SM, M_Z) [to be verified by specialist]
- Vacuum calibration interpretation [needs rigorous argument]

That is an honest, falsifiable, narrow claim. It's the result of 10
corrections of self-check, not the original optimistic picture.

## Files

- `grut/derivation/d4_thermal_restoration.py` — computation (Parts 1-5)
- `theory/derivation/D4_THERMAL_RESTORATION_LOG.md` — this document

## Next steps

Direction 1: trace V7 §26 explicitly. Does it SPECIFY µ = M_Z as a
definitional choice, or does it leave µ ambiguous? If specified, we
accept the definition and present it to the specialist as GRUT's
particular construction. If ambiguous, the thermal reading wins by
default and the 30% miss is the prediction.
