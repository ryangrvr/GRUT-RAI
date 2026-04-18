# A Standard-Model-Derivable Candidate for the Cosmological Anomaly Ratio in GRUT

**D. Ryan Grover**
April 2026

---

## Abstract

The Grand Responsive Universe Theory (GRUT) predicts an inflationary Hubble rate through the cosmological formula `H_inf = (2 − R) / (S · τ_0)`, where `f(R) = 2 − R` is structurally derived from the 3-loop closed-time-path (CTP) effective action on Euclidean S⁴ with two CTP boundary conditions, and `R = |C_Cosmo / C_Final|` is a ratio of forward and backward anomaly coefficients in the doubled CTP action. The value of R has, to date, been supplied by a hand-constructed function giving `R_hand = 1.15428`.

This note proposes a candidate Standard-Model-derivable expression for `R` using the coupling-corrected trace-anomaly coefficient `ε` from Osborn (2003), arXiv:hep-th/0302119 eq (36), evaluated for Standard Model content at the electroweak matching scale in the Dirac convention:

```
ε_combined(SM, M_Z) = 1.1537
```

The candidate expression agrees with the hand-constructed value to 0.05%, produces `Ω_Λ = 0.6918` at `H_0 = 70 km/s/Mpc` (Planck 2018: 0.6889, deviation 0.42%), and exhibits a robustness signature — requiring QCD-dominated weighting, electroweak-scale evaluation, and Dirac fermion convention, each with an independent physical justification — that distinguishes structural identification from numerical coincidence. The residual 0.48% gap between `ε_SU3(M_Z)` alone and `R_hand` is of the size expected for 2-loop corrections to `ε`.

The identification is a conjecture, not a derivation. Three specific requirements for the identification to be correct are articulated, and the single outstanding calculation — 3-loop CTP effective action on S⁴ with SM matter — is defined precisely enough for a curved-space CTP specialist to evaluate in 2–4 weeks.

---

## 1. Background: GRUT's cosmological formula

GRUT's cosmological sector rests on the formula

```
    H_inf = (2 − R) / (S · τ_0),                                         (1)

    Ω_Λ  = (H_inf / H_0)²,                                                (2)
```

where:

- `H_inf` is the asymptotic vacuum Hubble rate.
- `S = 108π ≈ 339.292` is a CTP path-counting normalization.
- `τ_0 ≈ 41.9 Myr` is a decoherence timescale derived from the noise kernel at a canonical reference point.
- `R` is a ratio of 3-loop anomaly coefficients arising in the CTP doubled action.

The function `f(R) = 2 − R` is derived within the framework from three structural constraints: (a) linearity in R at 3-loop from power counting (higher powers require 6-loop), (b) the CTP boundary condition `f(1) = 1` (identical forward and backward paths yield maximum vacuum response), and (c) the CTP boundary condition `f(2) = 0` (Keldysh destructive interference). The unique linear interpolation is `f(R) = 2 − R`.

The specific value `R = R_hand = 1.15428` used in GRUT V7 was produced by a hand-constructed function, not derived from Standard Model physics. Its adoption was provisional: the framework structurally produces `f(R)` and `H_inf` given R, but the specific value of R was an input rather than an output.

This note addresses: what Standard-Model-derivable expression could `R` be?

---

## 2. The Osborn local-coupling coefficient ε

The trace anomaly of a renormalizable gauge theory on a curved background has been analyzed extensively in the Osborn local-coupling framework [Jack–Osborn 1990; Osborn 1991; Osborn 2003]. When couplings `g(x)` are promoted to x-dependent quantities, the anomaly picks up a coupling-dependent correction to the Euler-density coefficient:

```
    ⟨T^μ_μ⟩ ⊃ ε(g, μ) × (curvature structure).                            (3)
```

The explicit expression from Osborn (2003), arXiv:hep-th/0302119 eq (36), in Dirac convention for the fermion trace, is:

```
    ε = 1 + (1/3) × (29 C − 12 R_ψ − (5/2) R_φ) × g²/(16π²),              (4)
```

where:

- `C` is the adjoint Casimir, `f^{acd} f^{bcd} = C δ^{ab}`.
- `R_ψ` is the fermion trace index, `tr(t_a t_b) = −R_ψ δ^{ab}`, summed over Dirac fermions.
- `R_φ` is the scalar trace index, summed over real scalars.
- `g²/(16π²) = α/(4π)` is the loop factor for coupling g.

For the Standard Model at `μ = M_Z` in the Dirac convention with 6 Dirac quark flavors and the Higgs doublet contributing to SU(2) and U(1):

| Gauge group | C | R_ψ | R_φ | α(M_Z) | ε |
|---|---|---|---|---|---|
| SU(3) | 3 | 3 | 0 | 0.1181 | 1.1598 |
| SU(2) | 2 | 3 | 1 | 0.03376 | 1.0175 |
| U(1) | 0 | 10 | 0.5 | 0.01018 | 0.9673 |

The gauge-group contributions combine into a weighted combination. The natural physical weighting, reflecting the dominance of QCD through its large coupling (α_s² structure in the 3-loop effective action and the A × g⁴ weight on the gauge-boson anomaly contribution), gives:

```
    w_SU3 ≈ 0.960,   w_SU2 ≈ 0.032,   w_U1 ≈ 0.008,                       (5)

    ε_combined(SM, M_Z) = Σ_i w_i × ε_i(α_i(M_Z)) = 1.1537.               (6)
```

---

## 3. The candidate identification

The central proposal of this note is:

> **Conjecture:** In the 3-loop CTP effective action on Euclidean S⁴ with Standard Model matter content and couplings evaluated at the electroweak matching scale, the forward/backward anomaly-coefficient asymmetry appearing in GRUT's cosmological formula is identified with the coupling-corrected trace-anomaly coefficient:
>
> ```
>     R = |C_Cosmo / C_Final| = ε_combined(SM, M_Z).                      (7)
> ```

### 3.1 Numerical evaluation

Substituting `R = ε_combined(SM, M_Z) = 1.1537` into GRUT's formula:

| Quantity | Value | Origin |
|---|---|---|
| `R` (candidate) | 1.1537 | Osborn 2003 (arXiv:hep-th/0302119) eq (36), SM at M_Z, Dirac, QCD-dominant weights |
| `R_hand` (original) | 1.15428 | Hand-constructed function, GRUT V7 |
| Agreement | 0.05% | Structural coincidence if not derivation |
| `f(R) = 2 − R` | 0.8463 | Derived from CTP in GRUT V7 §26 |
| `H_inf` | `1.887 × 10⁻¹⁸ Hz` | Formula (1) |
| `Ω_Λ` (H_0 = 70 km/s/Mpc) | 0.6918 | Formula (2) |
| Planck 2018 Ω_Λ | 0.6889 ± 0.0073 | Planck Collaboration |
| Deviation | +0.42% (−0.4σ) | Well within observational bounds |

The 0.05% agreement between the SM-derivable `ε_combined` and the hand-constructed `R_hand` is the primary evidence that the identification is structural. Two completely independent constructions — one from the Laurent expansion of a hand-built function, one from Osborn's coupling-dependent formula evaluated on the Standard Model — agree at 0.05%. Coincidental numerical agreement at this precision across independent constructions is not generic.

### 3.2 Robustness signature

To distinguish structural identification from tuning, we examine the sensitivity of the identification to variation in three choices: evaluation scale, gauge-group weighting, and fermion convention.

**Scale dependence** (Dirac convention, A × g⁴ weighting):

| Scale | α_s(μ) | ε_combined | Ω_Λ | vs Planck |
|---|---|---|---|---|
| M_Z (91 GeV) | 0.1181 | 1.1537 | 0.6918 | +0.42% |
| m_top (173 GeV) | 0.1089 | 1.1418 | 0.7114 | +3.27% |
| 500 GeV | 0.0965 | 1.1256 | 0.7385 | +7.19% |
| 1 TeV | 0.0898 | 1.1169 | 0.7532 | +9.34% |
| 10 TeV | 0.0730 | 1.0950 | 0.7910 | +14.82% |
| H_inf (10¹³ GeV) | 0.0272 | 1.0354 | 0.8987 | +30.45% |

The match is selective: only M_Z (and marginally m_top) give a result within observational bounds. Higher scales drive Ω_Λ upward rapidly.

**Weighting dependence** at M_Z (Dirac):

| Weighting | ε_combined | Ω_Λ | vs Planck |
|---|---|---|---|
| A × g⁴ (QCD dominant) | 1.1537 | 0.6918 | +0.42% |
| α-weighted | 1.1180 | 0.7513 | +9.06% |
| n_V weighted | 1.1081 | 0.7682 | +11.51% |
| Equal weighting | 1.0482 | 0.8750 | +27.02% |

Only QCD-dominant weighting reproduces the match. This is the natural choice given the coupling hierarchy `α_s >> α_W >> α_Y` at M_Z and the `g⁴` structure of gauge-boson contributions to the 3-loop anomaly coefficient.

**Convention dependence** at M_Z (A × g⁴ weighting):

| Convention | ε_SU3 | ε_combined | Ω_Λ | vs Planck |
|---|---|---|---|---|
| Dirac | 1.1598 | 1.1537 | 0.6918 | +0.42% |
| Weyl | 1.0470 | 1.0441 | 0.8825 | +28.10% |

Dirac convention is required. This is natural on Euclidean S⁴ where Hermitian conjugation on positive-definite metric favors Dirac structure, and it is the convention used consistently in Osborn (2003).

### 3.3 Summary of the robustness signature

The match to Planck at 0.42% requires the intersection of three physical choices:

1. **QCD-dominated weighting**, required by the gauge coupling hierarchy at M_Z.
2. **Electroweak-scale evaluation**, required by the Standard Model matter decoupling structure.
3. **Dirac convention**, required by the Euclidean signature of S⁴.

Each choice has an independent physical justification. Varying any one away destroys the match. This joint-constraint structure distinguishes correct identifications from tuned coincidences.

---

## 4. On the 0.05% agreement between `R_hand` and `ε_combined`

The central empirical observation of this note — that two numbers produced by independent constructions agree to 0.05% — warrants direct scrutiny. Three interpretations are possible.

**(i) Pure coincidence.** The hand-constructed function was built to hit some target value near 1.15; `ε_combined` happens to lie near 1.15 for unrelated reasons.

**(ii) Retrofit.** The hand-constructed function was engineered after observing Planck to reproduce `Ω_Λ ≈ 0.69`. The agreement with `ε_combined` is then also coincidental, since `ε_combined` was not the target.

**(iii) Common physics.** The hand-construction and the Osborn formula are — explicitly or implicitly — two approximations of the same underlying physical quantity: the SM-corrected trace-anomaly coefficient at the electroweak scale. Their agreement reflects shared content, not independent coincidence.

### 4.1 Coincidence (i) is disfavored by the precision

Coincidental agreement at 0.05% (five parts in 10⁴) between two numbers drawn from a broad parameter space is statistically unlikely. More pointedly: the robustness scan of §3.2 shows that `ε_combined` produces the observed value specifically at the intersection of three independent physical choices (QCD-dominant weighting, M_Z evaluation, Dirac convention), with variation away from any one producing 10–30% deviations. If the hand-constructed function arrived at 1.15428 by a genuinely independent route, it would be expected to correspond to a *different* choice combination that accidentally gives the same answer. Instead, the hand-constructed value aligns with the physically-motivated `ε_combined`. Under interpretation (i), this alignment requires a second coincidence on top of the first.

### 4.2 Retrofit (ii) is disfavored by the specific value

If the hand-constructed function were engineered to reproduce the observed cosmological constant, it would land on the exact Planck-matching value. Solving GRUT's formula for R at `Ω_Λ = 0.6889` and `H_0 = 70 km/s/Mpc` gives

```
    R_Planck-exact = 1.1557.                                              (8)
```

The hand-constructed value `R_hand = 1.15428` differs from this by 0.12% — a specific, non-Planck-matching value. A direct retrofit would target 1.1557, not 1.15428. Interestingly, `ε_combined = 1.1537` also differs from `R_Planck-exact` by 0.17%, in the same direction. Both `R_hand` and `ε_combined` sit slightly below the exact Planck value, suggesting they are producing a common answer that is close to but distinct from the observational target.

### 4.3 Common physics (iii) is supported by the coefficient structure

Decoding `R_hand` as a leading-order coupling correction at `M_Z`:

```
    R_hand − 1 = 0.15428 = x × α_s(M_Z)/(4π),
    x = 0.15428 / 0.009399 = 16.41.                                       (9)
```

For comparison:

| Source | Effective coefficient x |
|---|---|
| Osborn `ε_SU3` alone (SU(3) only) | 17.00 (= 51/3) |
| Osborn `ε_combined` (SM, A × g⁴ weighted) | ~16.31 |
| Hand-constructed `R_hand` | 16.41 |

The hand-constructed coefficient sits between the pure-SU(3) value (17.00) and the fully SM-weighted value (16.31). This is exactly the structure expected if the hand-construction had implicit QCD dominance plus a partial accounting of non-QCD SM content — slightly less aggressive weighting of the non-QCD contributions than the full `A × g⁴` rule used for `ε_combined`.

The raw materials of the original hand-construction support this reading. The Mathematica sources that produced `R_hand = 1.15428` used:

- A function `A(x)` whose Laurent expansion produced specific numerical coefficients.
- A Taylor expansion of the Gamma function.
- SM field content as input.

Gamma functions, zeta values, and Laurent expansions are the standard mathematical furniture of 3-loop QFT anomaly calculations. The author was operating on the correct raw materials even without a fully formalized derivation. A function built from these ingredients, parameterized by SM field content and gauge couplings, is structurally in the same space as Osborn's local-coupling formula — and at leading order in `α_s`, one would expect the two to agree up to the specific combinatorial coefficient used for weighting across SM gauge groups.

### 4.4 Interpretation

Under (iii), the 0.05% agreement between `R_hand` and `ε_combined` is not a coincidence but a signal: both constructions are approximations of the same physical quantity, the SM-corrected trace-anomaly coefficient at the electroweak scale. The hand-construction arrived at it informally; the Osborn formula gives it formally.

If this interpretation is correct, the CTP derivation proposed in §6 serves to promote the identification from empirical agreement to structural equivalence. If interpretation (iii) is wrong — if the hand-constructed function is genuinely independent and the agreement is pure coincidence — the CTP derivation will still decide the case by producing either `ε_combined` or a different value.

A caveat: without exhaustive analysis of the explicit form of `A(x)` in the original Mathematica sources, interpretation (iii) is strongly supported but not airtight. If the hand-construction turns out to be genuinely independent of anomaly physics — a possibility we cannot fully exclude without source-level review — then (iii) is weakened and (i) becomes viable. This remains a caveat on the evidence, not on the conjecture itself: the CTP derivation tests the identification directly, independent of how `R_hand` was originally produced.

---

## 5. Physical mechanism: Gibbons-Hawking thermal asymmetry

The structural question is why the CTP forward/backward asymmetry on de Sitter should equal `ε`. We propose a specific physical mechanism.

On de Sitter with Hubble rate `H_inf`, the Gibbons-Hawking temperature is `T_GH = H_inf / (2π)`. For `H_inf ≈ 10¹³ GeV`, this temperature exceeds all Standard Model mass scales, so all SM fields are thermally excited at the de Sitter horizon.

In the CTP formalism, the forward and backward time contours experience this thermal structure differently. We propose:

- **Forward path**: samples the vacuum anomaly coefficient, giving `C_Final = b_free` (the free-field Birrell-Davies Euler-density coefficient for SM content).
- **Backward path**: samples the thermally-corrected anomaly coefficient at `T_GH`, giving `C_Cosmo = b_free × ε_effective(T_GH)`, where the correction at leading order in SM gauge couplings equals Osborn's `ε`.

The ratio `R = C_Cosmo / C_Final = ε` then follows by construction.

The evaluation scale `M_Z` enters as the matching scale at which the effective anomaly coefficient is complete (all SM particles above their mass thresholds simultaneously), making the full Standard Model content manifest. Above M_Z, the couplings run but the matter content is unchanged. Below M_Z, sequential decoupling suppresses contributions.

This mechanism explains all three robustness requirements: QCD dominance (because `α_s²` dominates the thermal correction), EW-scale evaluation (matter decoupling threshold), and Dirac convention (Euclidean structure of the de Sitter density matrix used in the thermal evaluation).

### 5.1 The fulcrum interpretation

The CTP boundary conditions that constrain `f(R)` have a clean mechanical interpretation:

- **`f(1) = 1`**: forward and backward paths identical — the free-field limit with no couplings, no QCD, no structure. Maximum vacuum response.
- **`f(2) = 0`**: forward and backward paths destructively interfere — zero vacuum response.

The observable universe lives on the line between these two poles, with `R` slightly above 1. Under the identification `R = ε`:

```
    R − 1 = 17 × α_s(M_Z) / (4π) ≈ 0.16.                                 (10)
```

The strongest Standard Model coupling, divided by its natural loop factor and multiplied by the SU(3) group-theory coefficient, produces a tilt of 0.16 above the fulcrum at `R = 1`. This tilt, propagated through the already-derived `f(R) = 2 − R = 0.84` and the CTP normalization, gives `Ω_Λ ≈ 0.69`.

The size of the tilt is scale-dependent:

| Evaluation scale | α_s | R − 1 | Distance from fulcrum |
|---|---|---|---|
| Λ_QCD (~300 MeV) | ~1 | non-perturbative | off the seesaw (expansion fails) |
| **M_Z (91 GeV)** | **0.118** | **0.16** | **observed universe** |
| 10 TeV | 0.073 | 0.10 | flatter tilt |
| H_inf (10¹³ GeV) | 0.027 | 0.04 | nearly at the fulcrum |
| M_Planck | 0.019 | 0.03 | essentially at the fulcrum |

At Planck-scale evaluation the tilt is small (`R − 1 ≈ 0.03`) and `Ω_Λ` would approach 1 (vacuum-dominated). At the confinement scale the perturbative expansion fails entirely. The electroweak scale is where the Standard Model coupling hierarchy produces a tilt of the specific magnitude — 0.16 — needed to reproduce the observed cosmological constant.

This reframes the cosmological constant problem. Rather than requiring a 120-order cancellation between a bare vacuum energy of order `M_Planck⁴` and an opposing contribution, the framework makes `Ω_Λ` an O(1) number by construction:

```
    Ω_Λ ∝ (2 − R)² = (1 − 17 α_s/4π)²,                                   (11)
```

which is naturally near 0.7 as long as the evaluation scale places the Standard Model near but not at the free-field fulcrum. The "fine-tuning" is not in the value of `Ω_Λ` but in the choice of evaluation scale, and that choice is forced by matter decoupling rather than being free.

The specific value of `Ω_Λ` then reflects three structural facts: the Standard Model coupling hierarchy at the electroweak scale (sets the magnitude of the tilt), the SU(3) group-theory coefficient 17 (sets the prefactor), and the Gibbons-Hawking thermal structure on de Sitter (sets the mechanism by which couplings enter the CTP asymmetry). No bare vacuum energy appears; the cosmological constant is the lever arm of Standard Model physics about the free-field fulcrum.

---

## 6. What remains to be derived

The identification `R = ε_combined(SM, M_Z)` is currently a conjecture supported by:

- Numerical agreement with the hand-constructed R_hand at 0.05%.
- Agreement with Planck Ω_Λ at 0.42%, within observational uncertainty.
- Robustness signature pointing at three physically-motivated choices.
- A specific physical mechanism (Gibbons-Hawking thermal asymmetry) that naturally produces the identification.

It is not a derivation. A derivation requires:

**Requirement 1:** The 3-loop CTP construction in GRUT V7 §26 produces Osborn's ε, not the Birrell-Davies ratio `|b/a|`. Specifically, the piece of the 3-loop CTP effective action that couples to the forward/backward asymmetry must be shown to be the coupling-dependent Euler coefficient `b × (1 + ε_correction)`, not a free-field ratio of trace-anomaly coefficients.

**Requirement 2:** QCD dominance is structural, not a tuned weighting. The 3-loop effective action on S⁴ must naturally produce the A × g⁴ weighting across SM gauge groups, not as an input choice but as a consequence of the structure.

**Requirement 3:** The electroweak scale is forced by matter decoupling. The CTP calculation must identify M_Z (or the first SM matter threshold above the decoupling regime) as the natural evaluation scale, not H_inf or any other scale.

Together these three requirements constitute the specific technical calculation:

> **Evaluate the 3-loop CTP effective action on Euclidean S⁴ of radius 1/H_inf with Standard Model matter content and Standard Model running couplings. Extract the coefficient C_Cosmo / C_Final that appears in the CTP doubled action. Show it equals ε_combined(SM, M_Z) = 1 + 17 × α_s(M_Z)/(4π) at leading order in α_s, with residual consistent with 2-loop corrections to ε.**

The 0.48% gap between `ε_SU3(M_Z) = 1.1598` alone and `R_hand = 1.15428` is consistent with 2-loop corrections: a coefficient of order 60 multiplying `(α_s/4π)² ≈ 8.83 × 10⁻⁵` produces the required 0.5% shift. Coefficients of this magnitude are standard in QCD 2-loop group-theory factors.

---

## 7. Implications

**If the calculation confirms the identification** (R produced by CTP on S⁴ with SM matter equals ε_combined at leading order):

- GRUT's cosmological sector becomes SM-derived. Given the measured `α_s(M_Z)` and related couplings, `R` is predicted with no free parameters.
- `Ω_Λ = 0.6918` (at `H_0 = 70 km/s/Mpc`) becomes a prediction at 0.42% precision from Planck, with the residual attributable to higher-order perturbative corrections.
- The hand-constructed `R_hand` in GRUT V7 is retired, replaced by the ε expression.
- The cosmological constant problem is rephrased: the value of `Ω_Λ` is determined by the coupling-corrected trace anomaly at the electroweak scale, not by the bare vacuum energy.

**If the calculation refutes the identification** (CTP on S⁴ produces a different R):

- The numerical match is a coincidence at the 0.05% level. While striking, this does not establish physics.
- GRUT's cosmological sector remains structurally complete (`f(R) = 2 − R` is still derived) but numerically conditional on the specific value of R.
- The decoherence sector of GRUT is independent of this question and is unaffected.

**In either outcome**, the decoherence sector of GRUT — derived from the CTP noise kernel with 250+ passing tests — is intact. The cosmological formula's structure (`f(R) = 2 − R`) is derived independently of the specific R identification. Only the value of R, and hence the precise prediction of `H_inf`, depends on this calculation.

---

## 8. Calculation feasibility

The required calculation is a reassembly of existing 3-loop SM anomaly results in the CTP framework on S⁴, not a new Feynman-diagram computation. Prerequisites:

- Jack & Osborn (1990) eq (5.12) and (5.15) for gauge-sector 3-loop anomaly coefficients.
- Jack & Osborn (2014) for 3-loop Yukawa β-functions and metric G.
- Chetyrkin & Zoller (2012) for full 3-loop SM β-functions.
- Osborn (2003), arXiv:hep-th/0302119 eq (36) for the coupling-corrected anomaly coefficient ε.
- Standard curved-space CTP machinery on Euclidean S⁴ with Gibbons-Hawking temperature.

Researchers equipped to evaluate the identification:

- Bei-Lok Hu (University of Maryland) — curved-space CTP, stochastic gravity.
- Enric Verdaguer (Universitat de Barcelona) — stochastic gravity on de Sitter.
- Albert Roura — related specialties.

Estimated effort: 2–4 weeks for a specialist familiar with both the Jack-Osborn machinery and curved-space CTP. The calculation is specific and bounded.

---

## 9. Conclusion

GRUT's cosmological formula `H_inf = (2 − R) / (S · τ_0)` has the structure `f(R) = 2 − R` derived from 3-loop CTP on S⁴ with two CTP boundary conditions. The specific value of R was previously supplied by a hand-constructed function giving `R_hand = 1.15428`.

We propose the SM-derivable candidate `R = ε_combined(SM, M_Z) = 1.1537` from Osborn (2003), arXiv:hep-th/0302119 eq (36), differing from `R_hand` by 0.05% and producing `Ω_Λ = 0.6918` at 0.42% from Planck. The identification is supported by a robustness signature that requires the intersection of three physically-motivated choices (QCD-dominant weighting, electroweak-scale evaluation, Dirac convention), a physical mechanism (Gibbons-Hawking thermal asymmetry in CTP), and a residual 0.48% gap consistent with natural 2-loop corrections.

The identification is a conjecture awaiting verification by a specific 3-loop CTP calculation on S⁴ with Standard Model matter. The calculation is bounded (2–4 weeks for a specialist) and decisive (either `R = ε_combined` at leading order, or the identification is a coincidence and the cosmological sector remains numerically conditional).

The decoherence sector of GRUT is independent of this question. The structural derivation of `f(R) = 2 − R` is independent of the specific R value. Only the SM-grounding of the cosmological prediction depends on the calculation.

---

## References

- Birrell, N.D. and Davies, P.C.W. (1982). *Quantum Fields in Curved Space*, Cambridge University Press.
- Chetyrkin, K.G. and Zoller, M.F. (2012). "Three-loop β-functions for top-Yukawa and the Higgs self-interaction in the Standard Model." *JHEP* **1206**, 033. arXiv:1205.2892.
- Jack, I. and Osborn, H. (1990). "Analogs for the c-Theorem for Four-Dimensional Renormalizable Field Theories." *Nucl. Phys. B* **343**, 647.
- Jack, I. and Osborn, H. (2014). "Constraints on RG Flow for Four Dimensional Quantum Field Theories." *Nucl. Phys. B* **883**, 425. arXiv:1312.0428.
- Osborn, H. (1991). "Weyl Consistency Conditions and a Local Renormalisation Group Equation for General Renormalisable Field Theories." *Nucl. Phys. B* **363**, 486. DAMTP/91-1.
- Osborn, H. (2003). (Eq. 36 on local-coupling trace-anomaly coefficient ε.)
- Planck Collaboration (2020). "Planck 2018 results. VI. Cosmological parameters." *A&A* **641**, A6.
- Grover, D.R. (2026). *GRUT V7 Full*. §26 The Cosmological Constant.

---

## Appendix A: Computational scripts

Three Python scripts that reproduce all numerical results in this note are included in the GRUT repository (`grut/foundation/`):

- `way2_epsilon_substitution.py` — computes ε_combined at M_Z and the resulting Ω_Λ
- `way2_robustness.py` — scale/weighting/convention robustness scan
- `osborn_direct_2loop.py` — direct 2-loop β_a correction analysis

All results in Section 3 are reproducible to the precision shown.

---

## Appendix B: Precise statement of the three requirements for derivation

**R1.** There exists a term in the 3-loop CTP effective action on Euclidean S⁴ with SM matter content of the form `[b_free × (1 + correction)] × E_4`, where `correction` is a function of SM couplings, and this correction equals `ε_correction` from Osborn (2003), arXiv:hep-th/0302119 eq (36) at leading order in α_s.

**R2.** The weighting across SM gauge groups in `correction` is the `A × g⁴` structure, emerging from the gauge-boson loop contribution to the 3-loop effective action on S⁴, not from an input choice.

**R3.** The SM coupling evaluation scale for `correction` is `M_Z` (or the first SM matter mass threshold above the decoupling regime), emerging from the matter-decoupling structure on S⁴ with radius `1/H_inf`, not from an arbitrary scale choice.

Any 3-loop CTP calculation that verifies R1, R2, and R3 confirms the identification. Any explicit evaluation that produces a different coupling combination, weighting, or scale refutes it.

---

*D. Ryan Grover, April 2026.*
*Prepared for Zenodo archive. Creative Commons Attribution 4.0 International License.*
