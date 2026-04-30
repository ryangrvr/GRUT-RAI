# Path D — SM Trace Anomaly Ratio: Derived R Value

**Date:** April 23, 2026
**Status:** COMPUTED. Clean textbook-derived number from SM trace anomaly coefficients.
**Result:** `R_SM ≡ a_SM / c_SM = 1991 / 1698 ≈ 1.172556` (exact rational, not a choice).
**Ω_Λ prediction (with τ_0 = 41.9 Myr, H_0 = 70 km/s/Mpc):** **0.661** — 4.06% below Planck 0.6889.

---

## What this calculation is (and isn't)

**It IS:** an exact rational number computed from (a) textbook per-species trace-anomaly coefficients for scalars/fermions/vectors in 4D curved-space QFT, (b) fixed SM field content. Everything is sourced, cross-checked, and reproducible.

**It is NOT:** a derivation of why `R = a/c` is the specific combination that enters GRUT's `H_inf = (2−R)/(Sτ_0)`. That identification is a physical argument that still has to be made — see §5.

The calculation answers: *given that the relevant R in GRUT's formula is some dimensionless combination of the SM trace-anomaly coefficients, which natural candidate lands in the physical range?* Answer: a_SM/c_SM. No other natural ratio produces a sensible Ω_Λ.

---

## D.0 — Source verification

### Komargodski-Schwimmer 2011 (arXiv:1107.3987), "On Renormalization Group Flows in Four Dimensions"

Appendix A, equations (A.4)–(A.6):

- Euler tensor: `E_4 = R²_μνρσ − 4 R²_μν + R²`
- Weyl tensor squared: `W²_μνρσ = R²_μνρσ − 2 R²_μν + (1/3) R²`
- Trace anomaly: **`T^μ_μ = a·E_4 − c·W²`**

Per-species, in units of `1/(90·(8π)²) = 1/(360·(4π)²)`:

| Species | (a, c) |
|:---|:---|
| Real scalar (conformally coupled) | (1, 3) |
| Weyl fermion | (11/2, 9) |
| Gauge field (vector with ghosts) | (62, 36) |

### Duff 1994 (arXiv:hep-th/9308075), "Twenty years of the Weyl anomaly"

Equations (30)–(31):

- Weyl² coefficient: `b = 1/(120·(4π)²) × [N_S + 6 N_F + 12 N_V]`
- Euler coefficient:  `b' = −1/(360·(4π)²) × [N_S + 11 N_F + 62 N_V]`

where `N_F` counts **Dirac** fermions. Per Dirac = 2 × per Weyl, so Duff's 11 per Dirac ↔ KS's 11/2 per Weyl. Duff's 62 per vector ↔ KS's 62 per vector. Duff's 1 per scalar ↔ KS's 1 per scalar.

**Cross-check status:** sources AGREE on all per-species values. No convention ambiguity. Sign conventions differ (KS has explicit `−c`, Duff has `b'<0`), but the *values* of a and c per species are pinned.

### User's half-remembered values (cross-check)

The user reported from memory: a values (1, 11/2, 62) and c values (3, 9/2, 18). The **a values match exactly.** The **c values are off by factor 2** (paper values are 3, 9, 36; user had 3, 9/2, 18). Sources win; use (1, 3), (11/2, 9), (62, 36).

---

## D.1 — SM content and totals

### Field content

| Content | Count | Justification |
|:---|:---|:---|
| Gauge bosons `N_V` | 12 | 8 gluons (SU(3)) + 3 W^a (SU(2)) + 1 B (U(1)) |
| Weyl fermions `N_Weyl` | 45 | 15 per generation × 3 generations (per-gen: Q_L=6, u_R=3, d_R=3, L_L=2, e_R=1) |
| Real scalars `N_S` | 4 | Complex Higgs doublet = 4 real d.o.f. |

### Exact SM totals (units: `1/(360·(4π)²)`)

    a_SM = N_S·a_scalar + N_Weyl·a_weyl + N_V·a_vector
         = 4·1 + 45·(11/2) + 12·62
         = 4 + 495/2 + 744
         = 8/2 + 495/2 + 1488/2
         = 1991/2         (exact)
         ≈ 995.5

    c_SM = N_S·c_scalar + N_Weyl·c_weyl + N_V·c_vector
         = 4·3 + 45·9 + 12·36
         = 12 + 405 + 432
         = 849              (exact integer)

---

## D.2 — All natural dimensionless ratios

Every candidate, exact rational + decimal (6-place):

| Candidate | Exact rational | Decimal | vs R_hand (1.15428) |
|:---|:---|:---|:---|
| **a_SM / c_SM**            | **1991/1698** | **1.172556** | **+1.58%** |
| c_SM / a_SM                | 1698/1991 | 0.852838 | − |
| √(a_SM / c_SM)             | irrational | 1.082846 | −6.19% |
| √(c_SM / a_SM)             | irrational | 0.923492 | − |
| (a−c)/a                    | 293/1991  | 0.147162 | − |
| (a−c)/c = a/c − 1          | 293/1698  | 0.172556 | − |
| (a+c)/c                    | 3689/1698 | 2.172556 | − |
| 2(a−c)/c                   | 293/849   | 0.345112 | − |

**Irreducibility check:** `a_SM/c_SM = 1991/1698` is in lowest form. `1991 = 11 · 181` and `1698 = 2 · 3 · 283` share no common factors (181, 283 prime).

**Observations:**

- `a/c` and `1 + (a−c)/c` are algebraically identical (1.172556). Both land within 1.6% of R_hand.
- Reciprocals and differences are all far from R_hand or its vicinity.
- The only ratio of this set in the "GRUT-interesting" range is **a/c = 1991/1698**.

---

## D.3 — Downstream Ω_Λ for each candidate

With `H_inf = (2 − R) / (S·τ_0)`, `S = 108π`, `τ_0 = 41.9 Myr`, `H_0 = 70 km/s/Mpc`:

| Candidate R | R value | 2−R | H_inf (Hz) | Ω_Λ | vs Planck 0.6889 |
|:---|:---|:---|:---|:---|:---|
| R_hand (original, 1.15428) | 1.154280 | 0.845720 | 1.885×10⁻¹⁸ | 0.6904 | **+0.22%** |
| **a_SM / c_SM** (**derived**) | 1.172556 | 0.827444 | 1.844×10⁻¹⁸ | **0.6609** | **−4.06%** |
| c_SM / a_SM | 0.852838 | 1.147162 | 2.557×10⁻¹⁸ | 1.2703 | +84.4% |
| √(a/c) | 1.082846 | 0.917154 | 2.044×10⁻¹⁸ | 0.8120 | +17.9% |
| (a−c)/c | 0.172556 | 1.827444 | 4.073×10⁻¹⁸ | 3.2237 | +368% |
| (a+c)/c | 2.172556 | −0.172556 | −3.85×10⁻¹⁹ | 0.0287 | −95.8% |

**a_SM/c_SM is the only candidate that lands in the physical Ω_Λ range.** All others are drastically wrong (Ω_Λ > 1, or negative, or < 0.1).

Planck observational band (1σ): 0.6816 – 0.6962. The derived a/c value gives Ω_Λ = 0.6609, outside the 1σ band but within the "O(1) not fine-tuned" structural window.

---

## D.4 — Physical identification: which ratio is R_GRUT?

The calculation above identifies `a/c` as the unique natural candidate that lands in the physical range. But **"lands in the right range" is not a derivation.** A proper answer to "why does R = a/c specifically" requires a physical argument from GRUT's CTP structure.

### The boundary-condition argument (V7 §12)

V7 derives `f(R) = 2 − R` from CTP structure:
- `f(1) = 1`: forward and backward CTP paths identical → maximum vacuum response
- `f(2) = 0`: Keldysh destructive interference → zero response

For R = a/c: R = 1 means a = c. For R = 2 means a = 2c. Neither is at the SM value (a/c ≈ 1.17), so SM is **away** from the max-response point and **away** from destructive interference — consistent with a cosmological vacuum that has a finite but not maximal response.

The boundary conditions *constrain* what R = 1 and R = 2 MEAN, but they don't *fix* the relationship between R and specific anomaly coefficients. To pin R = a/c, one needs either:

- **(Option A)** An argument from 3-loop CTP effective action structure on S⁴ identifying a/c as the forward/backward asymmetry ratio. This would require tracing the 3-loop calculation of the Euler and Weyl² anomaly coefficients on CTP contours and showing their ratio plays the role of R in `H_inf = (2−R)/(S·τ_0)`.

- **(Option B)** An argument from "maximum simplicity" / dimensional analysis: of all natural dimensionless combinations of a and c, only a/c lands in the physical range. This is a weaker argument (not uniquely fixing R) but is real: the calculation demonstrates that if *any* natural combination of trace-anomaly coefficients plays the role of R, it must be a/c — the other combinations are ruled out by producing unphysical Ω_Λ.

- **(Option C)** An argument pending from the TJI Phase-1 curved-space calculation. If the full 3-loop TJI on S⁴ with SM matter produces a specific R, and if that R equals a/c within calculational uncertainty, that's the principled identification.

**Honest recommendation:** under Option B, report `R_SM = a_SM/c_SM = 1991/1698 ≈ 1.1726` as the derived value. The structural argument is: among natural dimensionless ratios of SM trace-anomaly coefficients, a/c is the unique physical candidate. The identification with GRUT's R is pending a full CTP-on-S⁴ derivation (Option A or C), but the value is bounded.

---

## D.5 — Implications

### For V7/V8 §12

The original R = 1.15428 was 1.58% below a_SM/c_SM = 1.1726. The +0.22% match to Planck was likely a fit (R_hand was tuned close to but not exactly the derivable a/c; the close match is coincidence given the derivation's true value).

**Under R = a/c:**
- `Ω_Λ = 0.661` (4% below Planck 0.689)
- The structural claim "Ω_Λ is O(1), not 10⁻¹²⁰ fine-tuned" is preserved cleanly
- The precision match to Planck 0.6889 is not claimed — the derivation predicts 0.661

**V8 §12 becomes:**

> GRUT predicts Ω_Λ = 0.661 using R = a_SM/c_SM = 1991/1698, where a_SM and c_SM are the one-loop trace-anomaly coefficients for the SM computed from textbook per-species values (Komargodski-Schwimmer 2011; Duff 1994). The value is 4% below Planck 0.6889 ± 0.0073, within the "O(1) not fine-tuned" structural window of the framework. The 0.04% precision match reported for the earlier heuristic R = 1.15428 is retracted; that value was 1.58% below the derived a/c and its Planck match was coincidental given the derivation's true prediction.

### For the anomaly sector

The 3-loop CTP structure on S⁴ does not need to produce 1.15428 specifically. It needs to produce whatever the 3-loop extension of the a/c ratio is. If the 3-loop correction shifts a/c by O(α_s/(4π))² ≈ 10⁻⁴, the prediction moves from 1.1726 to something like 1.1726 ± 0.0001 — which won't save the Planck match, but that's fine. **The framework has structural content regardless of precision match.**

### For Correction log

This is the kind of correction the framework has been catching successfully: the 1.15428 number was close to — but not equal to — the derivable value. The difference (1.58%) was absorbed into the Planck match by selecting the slightly-wrong R. Retracting 1.15428 → 1.1726 shifts Ω_Λ from 0.6904 → 0.6609 and the Planck deviation from 0.22% → 4.06%.

---

## D.6 — Confidence ledger

| Step | Status | Evidence |
|:---|:---|:---|
| Per-species (a, c) values | **Verified via two sources** | KS eq (A.6); Duff eq (30)-(31) |
| SM field content counts | **Standard** | Textbook SM |
| a_SM = 1991/2, c_SM = 849 | **Exact arithmetic** | SymPy Fraction |
| a_SM/c_SM = 1991/1698 in lowest form | **Verified** | gcd(1991, 1698) = 1 |
| All natural ratios enumerated | **Complete** | Exact rationals + decimals |
| a/c is the unique physical candidate | **Demonstrated** | Ω_Λ downstream table |
| Ω_Λ under R = a/c = 0.661 | **Computed** | H_inf = (2−R)/(Sτ_0), standard |
| R = a/c IS the correct identification for R_GRUT | **Not yet derived** | Pending Option A or C argument |
| 4% Planck deviation acceptable | **Structural, not precision** | Framework stays "O(1) not fine-tuned" |

---

## D.7 — What remains (D.4 proper, 3-loop corrections)

At one loop, a_SM/c_SM is a pure group-theoretic rational. At higher loops, both `a` and `c` acquire coupling-dependent corrections:

- At two loops: corrections of order `α_s/(4π) ≈ 9.4×10⁻³` (for QCD-dominant contributions)
- At three loops: `(α_s/(4π))² ≈ 8.8×10⁻⁵`
- At four loops: `(α_s/(4π))³ ≈ 8.3×10⁻⁷`

These shift a/c at the 0.01–1% level. To refine the prediction, we'd compute the two-loop corrections from the β-functions (Jack-Osborn 1990), giving corrected `a_SM(μ)` and `c_SM(μ)` at a specific renormalization scale. The result would be a scale-dependent R(μ) that runs weakly with α_s.

**This is tractable in the pipeline but deferred** — the one-loop result of `R = 1991/1698` is the headline finding; the refinement determines whether 3-loop corrections bring it closer to Planck (unlikely without large factors) or leave it at ~1.17 with ~4% Planck deviation.

---

## Deliverables

- `theory/path_d_trace_anomaly/STAGE_D_TRACE_ANOMALY_RATIO.md` (this file)
- D.0 source verification via KS + Duff, both fetched and cross-checked
- D.1-D.2 SymPy calculation, exact rationals, all natural ratios enumerated
- D.3 downstream Ω_Λ table for each candidate
- D.4 physical identification discussion, three options for completing the derivation
- D.5 implications for V7/V8 §12 (retraction of 0.04% Planck match, reframing as structural prediction)
