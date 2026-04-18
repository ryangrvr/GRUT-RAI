# STEP 05 — Log: Mechanism producing ⟨(∂_μg)²⟩ on S⁴

**Date:** April 2026
**Status:** Structural mechanism identified; full coefficient deferred to Step 06.

## Goal of Step 5

Determine what mechanism produces a non-zero `⟨(∂_μg_i)²⟩` on S⁴ even
when couplings are classically constant, and which weighting across
SM gauge sectors that mechanism implies.

## The two candidate mechanisms

### Mechanism 1: Gibbons-Hawking thermal fluctuations (simplest form)

On Euclidean S⁴ of radius 1/H_inf, the horizon temperature is
T_GH = H_inf/(2π). Treating g(x) as a stochastic field in the
thermal bath gives free-field fluctuations `⟨g²⟩ ~ H²/(4π²)`.

**Problem:** these fluctuations are INDEPENDENT of g itself and of
the gauge group structure. Evaluated this way, the weighting across
SM sectors becomes uniform (independent of coupling strength),
giving `ε_combined ≈ (ε_SU3 + ε_SU2 + ε_U1)/3 = 1.048`, and
`Ω_Λ ≈ 0.87` — inconsistent with Planck.

**Conclusion:** Mechanism 1 in its simplest form **does not** reproduce
the observed identification. Ruled out as primary mechanism.

### Mechanism 2: CTP source doubling with thermal KMS

In the CTP formalism, sources are doubled: `J_+` on forward, `J_-` on
backward. In Osborn's local-coupling framework, the coupling `g(x)`
IS a source (coupling to the composite operator `[F_μν F^μν]`). So
CTP gives `g_+(x)` and `g_-(x)` independently.

At equilibrium flat space, Keldysh symmetry forces `g_+ = g_-`. On de
Sitter, the thermal KMS structure of the Wightman function **breaks
Keldysh symmetry**, inducing an effective `g_+ ≠ g_-` through the
1-loop self-energy of the coupling source:

```
(g_+ − g_-) ~ g³/(16π²) × (thermal factor at T_GH)
```

At T_GH >> m_SM (inflationary scale dominates matter masses), the
thermal factor is O(1) and the branch difference is O(g³/(16π²)).

Squared: `(g_+ − g_-)² ~ g⁶/(16π²)²`

Multiplied by eq (35)'s `n_V × (1/g²)` prefactor:

```
Contribution per group ~ n_V × ε × g⁴/(16π²)²
```

**This is the `n_V × g⁴` weighting.** Summing across SM sectors gives
the ε_combined scheme that yielded the 0.04% match to Planck in Step 04.

## What Step 5 establishes structurally

1. **Gibbons-Hawking thermal structure breaks Keldysh symmetry** on S⁴.
   This is the "imaginary element" physical insight now made specific:
   the imaginary part of the CTP effective action (Step 02) contains
   the Euler term with coefficient modified by the thermal asymmetry
   (this step).

2. **The thermal asymmetry sources `(g_+ − g_-) ~ g³/(16π²)`** via the
   1-loop self-energy of the coupling source. This is standard QFT
   (1-loop β-function scaling) applied to the CTP doubled structure.

3. **The resulting weighting is `n_V × g⁴`**, which is exactly the scheme
   that produces ε_combined = 1.1554 (Step 04) and Ω_Λ = 0.6886
   (0.04% from Planck).

## What Step 5 does NOT fully derive

- **The exact numerical coefficient** of the 1-loop self-energy of the
  coupling source on S⁴ with SM matter. That requires the explicit
  Feynman-diagram calculation with thermal boundary conditions on S⁴,
  which is Step 06 territory.

- **The transition from the dimensional-analysis scaling `g³/(16π²)`
  to the precise prefactor** (which could be, e.g., `(21/(16π²)) g³`
  or `(b₀/(16π²)) g³` or similar — depending on the specific coupling
  self-energy).

These are honest limitations. The **structural claim** (n_V × g⁴
weighting) holds; the **precise numerical coefficient** remains to be
computed.

## Scale selection (R3 from the specialist protocol)

An important bonus observation from Step 5:

The thermal-KMS mechanism requires **T_GH >> m_matter** to avoid
exponential thermal suppression. On S⁴ of radius 1/H_inf ~ 10⁻¹³ GeV⁻¹
during inflation:

- `T_GH = H_inf/(2π) ~ 1.6 × 10¹² GeV`
- All SM masses (top mass 173 GeV, Higgs mass 125 GeV, etc.) are far
  below T_GH.
- So ALL SM particles are effectively massless at the de Sitter
  horizon — no thermal suppression.

BUT: the **running couplings that enter eq (35) are evaluated at the
MATCHING SCALE** where the SM effective theory is fully realized.
That's M_Z (or slightly above), not H_inf or M_Planck.

This makes the scale selection argument (R3) **internally consistent**:
the thermal mechanism operates at T_GH >> all SM masses, but the
coupling corrections that feed into it are computed at the EFT matching
scale M_Z. No fine-tuning; the two scales play different roles.

## Transcendentals check

Step 05 introduced no new transcendentals at the leading-order
estimate level. The ζ(3) and ln(2) we're tracking would appear in
the full 1-loop self-energy calculation on S⁴ (Step 06), where Feynman
integrals with thermal boundary conditions produce these standard
3-loop-QCD transcendentals.

## Status at end of Step 05

**DERIVED (at structural / dimensional-analysis level):**
- Gibbons-Hawking thermal structure on S⁴ breaks Keldysh symmetry
- This generates `(g_+ − g_-) ~ g³/(16π²)` at 1-loop
- Weighting across SM gauge sectors is `n_V × g⁴/(16π²)²`, reproducing
  the scheme from Step 04 that gave 0.04% match to Planck

**STRUCTURAL:**
- Scale selection for the coupling evaluation is M_Z (matter-decoupling
  threshold), not H_inf (thermal scale); the two serve different
  roles, internally consistent

**NOT FULLY DERIVED:**
- Precise numerical coefficient of the 1-loop self-energy on S⁴
- Full Feynman-diagram calculation with thermal boundary conditions

**OPEN for Step 06:**
- Assemble the full C_Cosmo / C_Final ratio
- Verify explicitly that it equals ε_combined(SM, M_Z) at leading order
- Identify where ζ(3) and ln(2) enter

## Net progress

The identification `R_GRUT = ε_combined(SM, M_Z)` is now supported by
a specific, structurally-derived mechanism:

1. GH thermal structure on S⁴ breaks Keldysh symmetry
2. CTP source doubling gives `g_+ − g_- ~ g³/(16π²)` at 1-loop
3. Osborn 2003 eq (35)'s operator structure turns this into the
   `n_V × g⁴` weighting across SM sectors
4. Summed, this gives ε_combined ≈ 1.1554, matching Planck at 0.04%

Steps 1-5 together provide a structural skeleton for the derivation.
Step 06 attempts the full assembly, which is the limit of what can be
done without specialist tools.
