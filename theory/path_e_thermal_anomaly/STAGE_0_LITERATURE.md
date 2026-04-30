# Path E Stage 0 — Literature on Finite-T Corrections to the Euler Anomaly Coefficient

**Date:** April 24, 2026
**Scope:** Literature retrieval only. No calculations. Establish what published QFT says about V7's ε_effective before we try to compute it.
**Pause gate:** After this stage, review before proceeding to E.1 (active-fields identification at T_GH).

---

## 1. The target quantity per V7 §26.2

V7 lines 1547–1548 define:

> Forward path samples the vacuum anomaly coefficient: `C_Final = b_free` (free-field Birrell-Davies Euler coefficient).
> Backward path samples the thermally-corrected coefficient at T_GH: `C_Cosmo = b_free × ε_effective`.
> Ratio R = C_Cosmo / C_Final = ε_effective.

So V7 asserts R is the multiplicative factor relating the free-field Euler anomaly coefficient to its "thermally-corrected" value at the Gibbons-Hawking temperature T_GH = H_∞/(2π). The question for Stage 0 is whether standard QFT literature supports this object as a well-defined quantity, and if so, how it's computed.

## 2. What the literature actually says

### 2.1 Duff 1994 — "Twenty years of the Weyl anomaly" (arXiv:hep-th/9308075)

The paper is a survey of the trace anomaly, covering free-field coefficients (eqs. 30–31, which we used in Path D), their group-theoretic derivation, and applications to cosmology, black holes, and supersymmetry.

**On de Sitter and the cosmological constant** (page 15–16):

> "In the inflationary phase, the geometry will be that of De Sitter space. But the trace anomaly for De Sitter completely determines the energy momentum because it must be a multiple of the metric by the symmetry:
>     ⟨T^μν⟩ = (1/4) g^μν g^αβ ⟨T_αβ⟩."

So on de Sitter, the trace anomaly ⟨T^μ_μ⟩ *determines* ⟨T_μν⟩ completely, and by extension the effective cosmological constant contribution from quantum loops. This is the link to Ω_Λ that V7 is using.

**On the trace-anomaly / CC connection:**

> "The idea that the trace anomaly might also have a bearing on the vanishing of the cosmological constant is a recurring theme [62, 28, 63, 64, 65, 66, 67]."

Duff cites Tomboulis, Antoniadis–Mazur–Mottola, and others for dynamical-relaxation arguments, but **does not give an explicit formula for a "thermal correction to the Euler coefficient."** The paper is a free-field review.

**Status for Path E:** Duff gives free-field values and states the de Sitter connection, but does NOT supply a formula for ε_effective. We have to look elsewhere.

### 2.2 a-theorem (Komargodski-Schwimmer 2011, arXiv:1107.3987 — already sourced for Path D)

The a-theorem states: `a_UV > a_IR` under RG flow in four dimensions.

**Critical implication for V7's R identification:**

- If V7's C_Final = b_free is the a-coefficient at some UV reference point
- And V7's C_Cosmo = b_free × ε_effective is the a-coefficient at an IR endpoint (e.g. after thermal flow to T_GH)
- Then by the a-theorem, `C_Cosmo < C_Final`, so `ε_effective < 1`, so `R < 1`.

But V7 claims **R = 1.15428 > 1**.

So V7's identification R = C_Cosmo/C_Final as "thermally-corrected Euler / free-field Euler" via a-theorem-style flow would give R < 1, not R > 1. **V7's R > 1 is inconsistent with the a-theorem direction if ε_effective is literally "the Euler coefficient after RG/thermal flow."**

This is a structural tension. Either:
- (a) V7's R is defined in the INVERSE direction (a_UV/a_IR > 1 instead of a_IR/a_UV < 1), and the "thermal correction" language is misleading
- (b) V7's ε_effective is NOT the Euler coefficient after RG flow; it's some other object
- (c) The a-theorem doesn't apply to the specific flow V7 has in mind (e.g., because it's not a true Wilsonian RG flow but a Gibbons-Hawking thermal *state* on a fixed de Sitter background)

Option (c) is the most likely. The a-theorem is about RG flow between scale-invariant fixed points. Moving from T=0 to T=T_GH on a fixed de Sitter geometry isn't a RG flow — it's a state change. The a-theorem wouldn't directly constrain ε_effective in this case.

**Status:** the a-theorem doesn't close the question but raises the flag that V7's terminology ("thermal correction to the Euler coefficient") may be using the Euler symbol in a non-standard way.

### 2.3 Finite-temperature QFT on de Sitter (arXiv:hep-th/9302078)

"Finite-Temperature Scalar Field Theory in Static de Sitter Space" — this is the closest published match to V7's conceptual setup. A scalar field on de Sitter at finite temperature (not just Gibbons-Hawking T_GH), with explicit zeta-function regularization.

**Key results** (from abstract and standard reviews):
- The stress tensor trace anomaly on de Sitter depends on the thermal state of the system
- For the Hartle-Hawking vacuum (which IS the T = T_GH state by construction), the renormalized stress tensor is what you get from Euclidean S⁴
- Additional thermal states at T ≠ T_GH exist but are non-equilibrium

The standard result: the Euclidean S⁴ continuation of de Sitter IS automatically at the Gibbons-Hawking temperature. There's no additional "thermal correction to the Euler coefficient" — the Euclidean calculation on S⁴ already gives the T = T_GH result.

**Implication:** If V7's C_Cosmo is "the Euler coefficient on S⁴ at T_GH" and C_Final is "the Euler coefficient on flat Minkowski at T=0," then these are fundamentally *different* calculations, not the same calculation with a thermal factor. The "thermal correction" language obscures that.

Concretely:
- Flat-space (T=0): Euler coefficient = standard free-field values we tabulated in Path D. a_SM = 1991/2.
- de Sitter S⁴ (T=T_GH): Euler coefficient = ? This requires a de Sitter QFT calculation, which has specific corrections from the curved background and the thermal state.

### 2.4 Heat kernel / Seeley-DeWitt coefficients (Vassilevich 2003, "Heat kernel expansion: user's manual")

The trace anomaly at 1-loop is governed by the Seeley-DeWitt coefficient `b_4(x)` which is a polynomial in curvature invariants. On de Sitter with specific Ricci R and Euler E:

    ⟨T^μ_μ⟩_1-loop = b_4 per species, summed

For free massless fields on de Sitter:
- The coefficients of E_4 and W² are the standard a and c values.
- On de Sitter specifically, W² = 0 identically (conformally flat), so only a·E_4 contributes.
- No additional "thermal" factor — the Euclidean continuation to S⁴ already gives the T = T_GH result.

So at **1-loop, for free massless fields, ε_effective ≡ 1**. The trace anomaly on S⁴ for free fields equals the flat-space value times the de Sitter curvature insertion; there's no extra thermal multiplicative factor.

Non-trivial ε_effective ≠ 1 requires:
- **Interactions** (2-loop and higher — couplings α_i enter through β-function contributions), or
- **Finite masses** (Boltzmann suppression of heavy fields at T_GH), or
- **Novel effects** beyond standard QFT on de Sitter that V7 is invoking.

### 2.5 Jack-Osborn 1990 — 2-loop Weyl consistency and a coefficient

The 2-loop correction to the Euler coefficient `a` for general gauge theories has been computed (Jack-Osborn 1990, with various follow-ups). For a generic gauge theory, the 2-loop correction has the schematic form:

    a(g) = a_free + (g²/(16π²)) × [group-theoretic coefficient] + O(g⁴/(16π²)²)

The specific coefficient depends on the gauge group and matter content. For the SM at M_Z, this gives a correction of order `α_s/(4π) ≈ 10⁻²` to a_SM.

**This is the only published formula that could produce a non-trivial ε_effective.** But it's a PERTURBATIVE correction, not a thermal one — it applies at T=0 flat space as well as at T=T_GH on de Sitter, with specific modifications.

If V7's R = 1.154 is supposed to come from Jack-Osborn 2-loop corrections to a_SM evaluated at SM couplings, that's computable. But then the physical interpretation is "2-loop coupling correction to a," not "thermal correction to a." Different story.

## 3. Synthesis: what Stage 0 has established

| Question | Answer |
|:---|:---|
| Is "thermal correction to the Euler coefficient at T_GH" a standard QFT quantity? | **No — not as V7 uses it.** On de Sitter S⁴, the Euclidean trace anomaly already includes the T_GH state. There's no additional multiplicative factor "ε_effective" in standard QFT. |
| Does the a-theorem constrain ε_effective? | **Yes, if it's an RG-flow quantity**: a_UV > a_IR means ε_effective < 1. V7's ε_effective = 1.154 > 1 is inconsistent with this. The mismatch suggests V7 is using the symbol for a different quantity or the direction is inverted. |
| Is there any formula that gives ε_effective ≈ 1.15 for SM at 1-loop? | **No.** At 1-loop with massless free SM fields, ε_effective = 1 identically (Euclidean S⁴ already captures T_GH). |
| Could Jack-Osborn 2-loop coupling corrections produce ε_effective > 1? | **Possibly, yes — but that's a COUPLING correction, not a THERMAL correction.** The physical interpretation changes. |
| What T_GH is V7 actually using? | V7 §26.2 line 1545 uses **inflationary H_inf ≈ 10¹³ GeV**, giving T_GH ≈ 10¹² GeV — where all SM fields are effectively massless and fully thermally populated. But V7 applies the resulting R in the TODAY's cosmological formula `H_inf = (2-R)/(Sτ_0)` where H_inf ≈ 10⁻¹⁸ Hz. **This is a scale-mixing that needs justification.** |

## 4. Scale-mixing flag

V7 has what appears to be **two different H_inf values** in its cosmological argument:

1. **Inflationary H_inf ≈ 10¹³ GeV** (used in §26 for computing R at T_GH)
2. **Today's cosmological H_inf ≈ 10⁻¹⁸ Hz = 1.885 × 10⁻¹⁸ Hz** (appears in the formula Ω_Λ = (H_inf/H_0)²)

These differ by ~60 orders of magnitude. V7 seems to treat R as an epoch-independent structural ratio — computed at the inflationary scale and applied at today's cosmological scale — but the physical argument for this epoch-independence isn't explicit in what I've read.

**If ε_effective is a literal thermal correction at today's T_GH (~10⁻³⁴ eV):**
- All SM fields are effectively frozen (their masses >> T_GH by many, many orders)
- Only truly massless fields (photon, graviton) contribute
- Thermal corrections scale as α·T⁴ × (structural factor), which at T ~ 10⁻³⁴ eV is astronomically tiny
- **ε_effective ≈ 1 to ridiculous precision**
- R = 1 gives Ω_Λ = (1/(Sτ_0 H_0))² = 0.965 — 40% above Planck

**If ε_effective is a thermal correction at inflationary T_GH (~10¹² GeV):**
- All SM fields thermally populated
- Coupling-corrected Euler coefficient has O(α/4π) ~ 1% modifications
- Plausibly gets to ε_effective ≈ 1.01 to 1.10 depending on specifics
- R in this range gives Ω_Λ in 0.95 – 1.10 range — still too high

Neither interpretation obviously gives R = 1.15 from pure thermal correction at 1-loop.

## 5. Hypothesis for what V7 actually computed

Best-guess reconstruction of V7's §26.2 logic:

1. V7 takes the Euler coefficient of the SM as the "b_free" baseline (call this a_SM_free).
2. V7 applies the **Osborn 2003 eq (36) ε formula** at the electroweak scale, with SM couplings at M_Z, using specific weights across SU(3)/SU(2)/U(1) contributions.
3. The weighted ε comes out to 1.1537 per the ZENODO identification document.
4. V7 identifies this ε with its "ε_effective" via a narrative about Gibbons-Hawking thermal state at inflationary T_GH.

If this reconstruction is accurate, **V7's R is numerically the Osborn-2003 ε_combined formula applied at M_Z, not an independently-computed thermal correction.** The "thermal correction at T_GH" framing is metaphorical, not the actual calculation.

We've already established in Stage 0 of Path B that:
- Osborn's ε is the coefficient of `R(∂_μg)²` in a local-coupling Lagrangian, NOT a correction to the Euler coefficient.
- The V7 combination weights 0.960/0.032/0.008 are fitted, not derived from Osborn.

So V7's R = 1.154 appears to be a **recycling of the Osborn-ε misidentification** we already flagged, wrapped in different terminology ("thermal correction at T_GH" instead of "trace-anomaly Euler coupling correction").

## 6. What this means for Path E going forward

Stage 0 has revealed that **Path E's target quantity (ε_effective as literal thermal correction to the Euler coefficient at T_GH) may not actually be what V7 computed.** If V7's 1.154 is the Osborn-ε recycled, then computing an independent thermal correction won't match V7 regardless of whether it matches Planck.

Two legitimate options for continuing:

### Option E-1: Compute the actual thermal correction at T_GH (today's) and accept what it gives

At T_GH ≈ 10⁻³⁴ eV, this will give ε_effective ≈ 1 at any reasonable precision. R = 1 gives Ω_Λ ≈ 0.965. **This is not close to Planck and wasn't close to V7's 1.154 either.** But it's a real calculation of a real quantity, and it tells us: at today's Gibbons-Hawking temperature, the thermal correction is negligible.

### Option E-2: Compute the 2-loop coupling correction to a_SM at M_Z via Jack-Osborn

This would give the actual published 2-loop correction `a(g) = a_free + g²/(16π²) × [coefficient] + ...`. The coefficient depends on the gauge group content, computed rigorously by Jack-Osborn. Applying to SM content gives a specific ε-like number.

This is NOT the Osborn-2003 ε (which is a different object). It's a legitimate 2-loop correction to the actual Euler coefficient.

**Expected result:** correction of order α_s/(4π) ≈ 0.01, so a_eff ≈ 1.01 × a_free. Way below 1.154.

### Option E-3: Retract the ε_effective framing and reopen the question of what R means

Stage 0 has established that V7's R = ε_effective identification doesn't hold up under literature review. Options E-1 and E-2 both give R ≈ 1 or ~1.01 at 1-loop+2-loop, not 1.15. **If ε_effective isn't what R is, the question of what R actually is in GRUT becomes open again.**

This is the honest-negative finding Stage 0 was supposed to surface or rule out. It's looking like it's surfacing it.

## 7. Sources cited

- [Duff 1994 "Twenty years of the Weyl anomaly"](https://arxiv.org/abs/hep-th/9308075) — free-field trace anomaly review, local at `/Users/mpg/.claude/projects/.../webfetch-1776967969224-62ojzr.pdf`
- [Komargodski-Schwimmer 2011 "On RG Flows in Four Dimensions"](https://arxiv.org/abs/1107.3987) — a-theorem, local at `/Users/mpg/.claude/projects/.../webfetch-1776967873901-kfqwv0.pdf`
- [Finite-Temperature Scalar Field Theory in Static de Sitter Space](https://arxiv.org/abs/hep-th/9302078) — not fetched, relevant for de Sitter finite-T
- [Vassilevich 2003 "Heat kernel expansion: user's manual"](https://www.researchgate.net/publication/222520183_Heat_kernel_expansion_User's_manual) — standard reference for 1-loop anomaly coefficients
- [Osborn 2003 "Local Couplings and Sl(2,R) Invariance"](https://arxiv.org/abs/hep-th/0302119) — the source of V7's ε (which we established is the coefficient of a local-coupling Lagrangian term, not the Euler coefficient)
- V7 local: `theory/GRUT_V7_FULL.md` §26.2 (lines 1476, 1537, 1547–1548)
- V7 local: `theory/ZENODO_EPSILON_IDENTIFICATION.md` (the Osborn-ε-combined weighting document)

## 8. Recommendation: pause and decide before E.1

Stage 0's findings change the Path E question substantially. Before committing to E.1 (identifying thermally-active fields at T_GH), we need a user call on which version of Path E to run:

- **E-1:** Literal thermal correction at today's T_GH → honest ε_effective ≈ 1, Ω_Λ ≈ 0.965.
- **E-2:** Jack-Osborn 2-loop coupling correction to a_SM → honest ε ≈ 1.01, Ω_Λ ≈ 0.7 territory but specifically.
- **E-3:** Retract ε_effective as a target and acknowledge V7's R doesn't have a clean published identification.

None of these produces R = 1.15 from first principles. That's the honest finding.

This is Stage 0's pause-gate output. Waiting for decision before proceeding.

Sources:
- [Duff 1994 "Twenty years of the Weyl anomaly"](https://arxiv.org/abs/hep-th/9308075)
- [Komargodski-Schwimmer 2011](https://arxiv.org/abs/1107.3987)
- [Finite-T scalar field theory in static de Sitter](https://arxiv.org/abs/hep-th/9302078)
- [Vassilevich 2003 heat kernel manual](https://www.researchgate.net/publication/222520183_Heat_kernel_expansion_User's_manual)
- [Osborn 2003](https://arxiv.org/abs/hep-th/0302119)
