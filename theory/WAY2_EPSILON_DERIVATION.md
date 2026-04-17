# Way 2 — ε as the Natural CTP Asymmetry on S⁴

## Status

**Numerical headline:** `ε_combined(SM, M_Z) = 1.1537` → via GRUT's already-derived
`f(R) = 2-R` structure → `Ω_Λ = 0.6918`, within **0.42% of Planck**.

The hand-constructed `R_anomaly = 1.15428` in the original framework and the
SM-derived `ε_combined = 1.1537` differ by 0.05%. If the identification R = ε is
correct, the cosmological sector becomes SM-grounded with zero free parameters
in the anomaly sector.

## The claim

> The 3-loop CTP effective action on Euclidean S⁴ with SM matter and running
> couplings at the electroweak scale produces a forward/backward anomaly-
> coefficient asymmetry `R = |C_Cosmo / C_Final|` that coincides with the
> coupling-corrected trace-anomaly coefficient ε from Osborn 2003 eq (36),
> evaluated at the scale where SM matter becomes massive.

## Why the identification is natural

### 1. Both live on the same footing

- **R in GRUT** is a ratio of 3-loop anomaly coefficients appearing in the
  CTP action on S⁴, with forward path carrying `C_Final` and backward path
  carrying `C_Cosmo = R × C_Final`.
- **ε in Osborn 2003 eq (36)** is the coupling-dependent correction to the
  trace-anomaly coefficient multiplying `G` (Euler density) when local
  couplings `g(x)` are allowed on curved backgrounds.

Both are **curved-space anomaly coefficients with coupling-dependent
corrections**. The question is whether GRUT's R, when derived from first
principles with SM matter, equals ε.

### 2. S⁴ selects the Euler-density sector

On S⁴ (maximally symmetric), the Weyl tensor `C_μνρσ = 0` identically. The
trace anomaly reduces to:

```
⟨T^μ_μ⟩|_{S⁴} = b × E_4 + c × □R
             = b × 24H⁴ + 0      (constant curvature kills □R)
```

Only the Euler-density coefficient contributes dynamically. The `a`-coefficient
(Weyl²) is invisible on S⁴. This is exactly the sector Osborn 2003 eq (36)
parameterizes via ε.

### 3. CTP asymmetry is a coupling-dependent phenomenon

In equilibrium CTP at flat space, the forward and backward effective actions
are identical (Keldysh symmetry). The asymmetry `C_Cosmo ≠ C_Final` comes from:

- **Time-dependence of the background** (inflation, H > 0)
- **Coupling-dependence of the trace anomaly** (ε ≠ 1 when interactions on)

At free-field level (ε = 1): forward and backward anomaly coefficients are
identical, R = 1, f(R) = 1, and the cosmological formula gives the maximum
vacuum response. This is the GRUT boundary condition f(1) = 1.

**With interactions:** ε ≠ 1 and the forward/backward asymmetry is driven
precisely by the coupling-dependent correction that Osborn 2003 eq (36)
computes.

### 4. Scale selection at M_Z

The SM matter content has all particles massless in the Lagrangian. Physical
masses come from the Higgs VEV at the EW scale. Below the EW scale, the
effective theory has fewer massless degrees of freedom (top decouples first).
Above the EW scale, all SM fermions and bosons are effectively massless.

**The natural scale at which the SM trace anomaly is fully manifested is the
EW scale**, where all SM particles are simultaneously in the massless regime
relative to H_inf ~ 10¹³ GeV. At lower scales, decoupling kicks in. At higher
scales, the couplings are running but the matter content is unchanged.

This gives a physical argument for why ε(M_Z), not ε(H_inf) or ε(Λ_QCD), is
the natural object.

## What remains to be derived

### The specific technical question

> **Compute the 3-loop CTP effective action on Euclidean S⁴ with SM matter
> and running couplings. Extract the coefficient ratio `C_Cosmo / C_Final`
> that appears in the CTP doubled action. Verify that this ratio equals
> `ε_combined(SM, M_Z) = 1.1537` at leading order in α_s.**

This is not a new loop calculation — the 3-loop anomaly coefficients for
general gauge-Yukawa-scalar theory are in the literature (Jack-Osborn 1990
eq 5.12 for gauge sector, Chetyrkin-Zoller 2012 for SM 3-loop β-functions).
It is a **reassembly** of existing 3-loop results in the CTP framework on S⁴.

### Three specific sub-questions

**Q1: Why does the CTP asymmetry take the form R = (ε forward)/(ε backward)?**

On S⁴ with inflation, the CTP contour has forward time (expanding) and
backward time (contracting). The anomaly coefficient on each branch is a
function of the running coupling evaluated at that branch's kinematic scale.
If the forward branch evaluates at `g(H_inf)` and backward branch at `g(M_Z)`
(matter decoupling scale), the asymmetry is:

```
R = ε(g_backward) / ε(g_forward) = ε(M_Z) / ε(H_inf)
```

At H_inf ~ 10¹³ GeV, α_s ≈ 0.04 → ε_SU3(H_inf) ≈ 1.05. So:

```
R ≈ 1.160 / 1.05 ≈ 1.10
```

That doesn't reproduce 1.154. So the simple "backward at M_Z, forward at
H_inf" doesn't work. **A more careful analysis of which scale each CTP
branch evaluates at is needed.**

**Alternative:** if BOTH branches evaluate at M_Z but with opposite sign
conventions, R could be exactly ε(M_Z). This would require:
- Forward branch: anomaly coefficient = b_free (free-field value at scale)
- Backward branch: anomaly coefficient = b_free × ε(M_Z) (coupling-corrected)

Then R = ε(M_Z) directly. This is the Way 2 conjecture in its simplest form.

**Q2: Why M_Z specifically and not another scale?**

The SM matter content has the property that below M_Z, particles start
decoupling (top first, then bottom, etc.). Above M_Z, the matter content
is "complete" in the sense that all SM particles contribute. M_Z is
therefore the **matching scale** where the full SM is realized.

For a CTP calculation on S⁴ with SM matter, the natural evaluation scale
for the effective action's anomaly coefficients is where the SM is
"fully on" — which is M_Z. Below, decoupling suppresses contributions.
Above, the couplings run but the field content is the same.

**This needs to be checked against a decoupling analysis: at what scale
does the full SM anomaly coefficient "stabilize" for a curved-space
calculation on S⁴ of radius 1/H with H ~ 10¹³ GeV?**

**Q3: What are the higher-order corrections?**

At leading order in α_s, ε_SU3 = 1 + (17/3) α_s/π. Higher-order corrections:

- 2-loop: α_s² × (group-theory coefficient)
- Mixed: α_s × α_2, α_s × y_t² (Yukawa)
- Non-perturbative: exp(-8π²/g²) — suppressed

The 0.4% residual match could be absorbed into these higher-order
corrections. Explicit calculation would either:
- Confirm the residual is within perturbative uncertainty → framework solid
- Produce a shift that changes Ω_Λ by > 1% → framework needs revision

## The calculation path

### Step 1: Reassemble Jack-Osborn 1990 / Osborn 2003 / 3-loop SM in CTP form

Take the 3-loop trace anomaly for SM matter (Jack-Osborn 1990 eq 5.12 + 5.15
for gauge, Chetyrkin-Zoller 2012 for Yukawa). Place this on CTP contour with
forward/backward doubling. Evaluate on Euclidean S⁴ of radius 1/H.

### Step 2: Identify the forward/backward asymmetry structurally

Determine which coupling value enters the forward branch vs the backward
branch. The answer depends on:
- The CTP i-ε prescription for S⁴ with de Sitter boundary conditions
- The analytic continuation Euclidean → Lorentzian
- The decoupling structure of SM matter at scales relevant to S⁴

### Step 3: Extract R = C_Cosmo / C_Final

Compute the ratio. If R = ε(M_Z) at leading order, Way 2 is confirmed and
GRUT's cosmological sector is SM-derived.

### Step 4: Verify 0.4% residual

Compute the next-order correction to ε (2-loop, Yukawa, mixed). If the
correction shifts Ω_Λ within 1-2% of Planck, the framework is consistent.
If it shifts by 10%+, something is wrong.

## Who can do this

Curved-space CTP specialists. Named in §26 of the main doc:
- Bei-Lok Hu (Maryland)
- Enric Verdaguer (Barcelona)
- Albert Roura

This is not a Feynman-diagram calculation — it's a structural reassembly of
existing 3-loop SM anomaly results in the CTP framework on S⁴. Estimated
effort: 2-4 weeks for a specialist, longer for someone new to curved-space
CTP.

## What this closes

If Way 2 is confirmed:

- **R_anomaly is replaced by ε_combined(SM, M_Z) = 1.1537.**
- The hand-constructed function that produced R = 1.15428 in the original
  Mathematica notebook is retired.
- GRUT's cosmological sector is SM-grounded with zero free parameters.
- Ω_Λ = 0.6918 is a derived prediction, matching Planck at 0.42%.
- The framework becomes genuinely predictive: given measured α_s, α_2, α_Y
  at M_Z, GRUT predicts Ω_Λ with 0.4% residual.

If Way 2 is NOT confirmed (CTP calculation gives a different R):

- R_anomaly remains hand-constructed. ε(M_Z) proximity is coincidence.
- The 12.5% gap between Birrell-Davies |b/a| and what GRUT needs is not
  the right framing (R was never |b/a|), but the specific value of R
  remains unexplained from SM physics.
- Avenue 6 (honest negative, ship decoherence-only) becomes appropriate.

## Current status

**Way 2 is the highest-leverage remaining lead.** The numerical match
`ε_combined(M_Z) = 1.1537 → Ω_Λ = 0.6918` (Planck 0.42%) is too close to
dismiss as coincidence but too unexplained to claim as a derivation. The
specific technical question — does 3-loop CTP on S⁴ with SM matter produce
this ratio — is well-defined and executable by a curved-space CTP specialist.

Until that calculation is performed, the cosmological-sector status is:

> **Structurally plausible, numerically consistent at 0.4%, pending explicit
> 3-loop CTP calculation on S⁴ with SM matter to confirm the identification
> R_anomaly = ε_combined(SM, M_Z).**
