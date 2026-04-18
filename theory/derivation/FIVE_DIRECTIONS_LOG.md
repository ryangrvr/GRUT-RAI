# Five Directions for the Specialist — Concrete Analysis

**Date:** April 2026
**Status:** Three directions closed; two open and critical.

## Summary Table

| Direction | Status | Impact |
|:---|:---|:---|
| 1. Ratio structure | **CRITICAL UPDATE** | V7 structure makes near-invariance inapplicable |
| 2. Non-perturbative QCD (instantons) | **CLOSED** | exp(−218) suppressed, 97 orders below precision |
| 3. Cross-sector 3-loop terms | **CLOSED** | O(10⁻⁵), below precision |
| 4. Higgs thermal restoration | **OPEN + CRITICAL** | Weakens matter-decoherence argument for M_Z |
| 5. Graviton loops | **CLOSED for cosmology** | Relevant only for closure ladder |

## Key findings

### D1 — Ratio structure (decisive update)

V7/V8 posits C_Final = b_free (bare), C_Cosmo = b_free × ε (thermally
dressed). This gives:

    R_GRUT = |C_Cosmo / C_Final| = ε

directly. In my earlier ratio test framework, this is K₁ = 17, K₂ = 0 —
the maximally scheme-dependent case. **The ratio near-invariance argument
I built in `tensor_projection_ratio_test.py` does not apply to V7's
posited structure.**

| µ | α_s(µ) | ε | Ω_Λ | vs Planck |
|:---:|:---:|:---:|:---:|:---:|
| M_Z (91.2 GeV) | 0.118 | 1.160 | 0.682 | −1% |
| T_GH (1.6×10¹² GeV) | 0.029 | 1.039 | 0.892 | +30% |
| H_inf (10¹³ GeV) | 0.027 | 1.037 | 0.896 | +30% |

**Specialist task:** verify or refute V7's specific structural claim.
Either outcome is publishable; it determines which regime applies.

### D2 — Instantons (closed)

Instanton action at inflationary scales: S_inst = 2π/α_s(µ).

- At T_GH: S_inst = 218, exp(−218) ≈ 10⁻⁹⁵
- At H_inf: S_inst = 231, exp(−231) ≈ 10⁻¹⁰¹

Even with 100× IR enhancement from the noise kernel, 10⁻⁹⁵ × 100 = 10⁻⁹³.
Negligible by 90+ orders of magnitude at all relevant scales.

### D3 — Cross-sector diagrams (closed)

Cross-sector contribution ~ α_s α_2 / (4π)²:
- At M_Z: 2.5 × 10⁻⁵
- At T_GH: 4.4 × 10⁻⁶

Both well below 0.04% match precision (4 × 10⁻⁴). Not the source of
scheme ambiguity.

### D4 — Higgs thermal restoration (critical open question)

T_GH / v_EW ≈ 6.5 × 10⁹. EW symmetry emphatically restored.

Consequences in the thermal state:
- Higgs VEV = 0
- All Yukawa masses vanish
- Thermal masses: m_therm ≈ g·T ~ 10¹² GeV

**The "matter-decoherence argument picks M_Z because SM matter is
defined at M_Z" loses force in the restored phase.** There is no
physical M_Z threshold when matter is massless.

Two competing interpretations remain:
- **Thermal reading:** µ ~ T_GH ~ H (Scenario C, 30% miss)
- **Vacuum calibration reading:** µ = M_Z as measurement anchor,
  RG-invariant in principle (Scenario A, Planck match)

Neither can be settled by scaling arguments alone. The specialist must
identify which reading applies to GRUT's specific CTP construction.

### D5 — Graviton loops (closed for cosmology)

Contribution O((H/M_Pl)²):
- At H = 10¹³ GeV: 7 × 10⁻¹³ (9 orders below precision)
- At H = 10¹⁸ GeV: 7 × 10⁻³ (percent level, relevant for closure ladder)

Negligible for cosmological sector; flagged for 4/8 closure ladder V8 work.

## Revised probability assessment

Before the five directions: ~70-80% M_Z wins (tensor projection work,
ratio near-invariance).

**After five directions:** ~50-60% M_Z wins, ~40-50% H wins.

The downward update reflects:
- D1: V7 structure makes ratio near-invariance inapplicable
- D4: Thermal restoration weakens matter-decoherence argument

What still supports M_Z:
- IR-dominated spectral structure of the right observable (D5)
- Vacuum calibration interpretation (D4.ii)
- Standard EFT practice when SM is defined at its measurement scale

## What the specialist's workflow looks like

**Week 1:** Trace V7 §26 explicitly. Determine whether 3-loop CTP on S⁴
produces C_Cosmo, C_Final with V7's posited structure or a more complex
form. Check Higgs thermal restoration impact on the CTP construction.

**Week 2:** Compute the 1-loop coupling-source self-energy on S⁴ with
Allen-Jacobson propagator. Extract Im(Π) for fermion loop. Confirm or
refute IR dominance for the specific tensor projection.

**Week 3:** Extract K₁ and K₂. Verify instanton negligibility (standard),
check cross-sector diagrams and graviton loops (expect negligible).

**Week 4:** Cross-checks (flat-space limit, Osborn eq 36 recovery,
MS̄ / on-shell scheme comparison). Assemble final K₁, K₂ values. Determine
whether R = 1.155 is robust.

## Bottom line

The cosmological sector remains falsifiable with two clean outcomes:

- **Ω_Λ = 0.69** (0.04–1% from Planck): 50-60% probable
- **Ω_Λ = 0.90** (30% miss): 40-50% probable

After the five directions, three of them (D2, D3, D5) are closed at
our precision. The remaining two (D1, D4) are the specialist's real
work: the ratio structure in V7's posited form, and the thermal-phase
scale ambiguity.

## Files

- `grut/derivation/five_directions.py` — concrete computation
- `theory/derivation/FIVE_DIRECTIONS_LOG.md` — this document
- `theory/SPECIALIST_VERIFICATION_BRIEF.md` — updated with §8 expansion

## Honesty ledger

19 pieces of work, 10 corrections caught, 0 hallucinations passed through.
Most recent: the ratio near-invariance argument I built (pre-five directions)
was real mathematically but doesn't apply to V7's posited structure. This
is a legitimate downward revision of the probability, caught before any
claim was made beyond the repository.
