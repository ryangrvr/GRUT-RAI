# Path B Stage 0 — Osborn (2003) Equation (36) Verification

**Date:** April 23, 2026
**Status:** COMPLETE. Paper retrieved, eq. (36) transcribed directly. Two FINDINGS (one positive, one critical) documented below.
**Purpose:** Before any calculation of ε_combined, verify what the paper actually says.
**Honesty protocol:** No calculations performed in Stage 0. No choices made. Only transcription and comparison.

---

## 1. Paper identity

| Field | Value |
|:---|:---|
| Title | **Local Couplings and Sl(2,R) Invariance for Gauge Theories at One Loop** |
| Author | H. Osborn (DAMTP Cambridge; email ho@damtp.cam.ac.uk) |
| arXiv | hep-th/0302119v1 (16 Feb 2003) |
| DAMTP number | DAMTP/03-11 |
| PACS | 11.10.Gh, 11.15.-q, 11.30.Pb |
| Keywords | local couplings, Sl(2,R) symmetry |

**Abstract (verbatim):**

> The response of the one loop effective action for a gauge theory with local couplings g(x), θ(x) under a local Weyl rescaling of the background metric is calculated. Apart from terms which may be removed by local contributions to the effective action the result is compatible with Sl(2, R) symmetry acting on g, θ. Two loop effects are also discussed.

**Note on scope:** The paper is *one-loop* with some two-loop extensions. The GRUT ZENODO document's characterization of this as "Osborn (2003)" eq. 36 applied to the 3-loop CTP context is a re-use of the two-loop result in a different context — not a 3-loop calculation from this paper.

---

## 2. Equation (36) — direct transcription from the PDF

**Preceding text (eq. 34 and 35):** The paper places the calculation in the general Weyl-rescaling response:

> For local couplings g^i, with corresponding β-functions β^i, and where L, Z^μ, Y depend on their derivatives:
>
>     16π² D_σ W = ∫ d⁴x √γ σ ( cF − aG − h∇²R − (1/9)bR² + L − ∇_μ Z^μ + ∇² Y )    (34)
>     D_σ = ∫ d⁴x σ ( −2γ_μν δ/δγ_μν + β^i δ/δg^i )
>
> For a simple gauge coupling g, with θ = 0, we may write:
>
>     L = n_V { (1/g²) [ α(∇²g)² − 2δ G_μν ∂^μg ∂^νg − (1/3) ε R ∂_μg ∂^μg ]
>             − 2κ (1/g³) ∂_μg ∂^μg ∇²g
>             + 2λ (1/g⁴) ∂_μg ∂^μg ∂_νg ∂^νg }                                   (35)

**Equation (36) verbatim (paper's exact form), "to two loop order using dimensional regularisation, for ĝ² = g²/(16π²), extending the results in [5]":**

    α = δ = 1 + (1/3) ( 51 C − 20 R_ψ − (7/2) R_φ ) ĝ²

    ε     = 1 + (1/3) ( 29 C − 12 R_ψ − (5/2) R_φ ) ĝ²                          (36)

    κ     = 1 + (4/3) ( 11 C −  4 R_ψ − (1/2) R_φ ) ĝ²

    λ     = 1 + (1/18) ( 323 C − 76 R_ψ − (25/2) R_φ ) ĝ²

**Text immediately following eq. (36) (definitions and caveats):**

> where `t^φ_a, t^ψ_a` are the gauge group generators acting on scalar, fermion fields, `tr(t^φ_a t^φ_b) = −δ_ab R_φ`, `tr(t^ψ_a t^ψ_b) = −δ_ab R_ψ`. **The results are scheme dependent.** For supersymmetric theories it is more natural to transform to a dimensional reduction scheme by letting `1/ĝ² → 1/ĝ² + (1/3) C`. [...]

**Symbol definitions (as given in the paper):**

| Symbol | Definition in paper | Notes |
|:---|:---|:---|
| `C` | Adjoint Casimir: `f^{acd} f^{bcd} = C δ^{ab}` (convention from earlier in paper) | For SU(N): C = N |
| `R_ψ` | Fermion trace index: `tr(t^ψ_a t^ψ_b) = −δ_ab R_ψ` (note minus sign in Osborn's convention) | Summed over all fermion representations |
| `R_φ` | Scalar trace index: `tr(t^φ_a t^φ_b) = −δ_ab R_φ` | Summed over all scalar representations |
| `ĝ²` | `g²/(16π²)` | Dimensionless loop factor |
| `g` | Single gauge coupling (scalar; θ = 0 case) | Promoted to g(x) locally |
| `n_V` | Number of gauge bosons (dimension of adjoint representation) | `n_V` prefactor in eq. (35) |

---

## 3. What ε physically computes — critical clarification

**ε is NOT a trace anomaly coefficient.**

Reading eq. (34)-(36) in context:

- Equation (34) is the Weyl-rescaling response `D_σ W` of the effective action. The coefficients of `F` (Weyl² density) and `G` (Euler density) are `c` and `a` — these are the standard *trace anomaly coefficients* of the constant-coupling theory.
- `L` in eq. (34) is the local-coupling-dependent piece: terms built from derivatives of `g(x)`. When `g` is constant (`∂_μ g = 0`), `L = 0`.
- Equation (35) expands `L` for a single simple gauge coupling into five independent terms with coefficients `α, δ, ε, κ, λ`.
- **ε specifically multiplies `R ∂_μg ∂^μg`** — the scalar-curvature-weighted kinetic term for the spatially-varying coupling.

So: `ε` is the coefficient of the `R · (∂g)²` term in the local-coupling-dependent part of the Weyl response. It has physical meaning only when one promotes the gauge coupling to a spacetime-varying function `g(x)`. For standard field theory with constant `g`, ε does not enter the trace anomaly at all.

The *trace anomaly Euler coefficient* of this theory is `a` (see eq. 34) — a *different* object from ε.

---

## 4. Comparison to the GRUT ZENODO document's quote

The GRUT document `theory/ZENODO_EPSILON_IDENTIFICATION.md` (line 27-29) quotes:

    ε_combined(SM, M_Z) = 1 + (1/3) × (29 C − 12 R_ψ − (5/2) R_φ) × g²/(16π²)
                        = 1.1537

**Comparison:**

| Item | ZENODO doc claim | Paper's eq. (36) | Match? |
|:---|:---|:---|:---|
| Formula for ε | `1 + (1/3)(29C − 12R_ψ − (5/2)R_φ) × g²/(16π²)` | Same | **✓ EXACT** |
| Coefficient of C | 29 | 29 | ✓ |
| Coefficient of R_ψ | 12 (with minus sign) | 12 (with minus sign) | ✓ |
| Coefficient of R_φ | 5/2 (with minus sign) | 5/2 (with minus sign) | ✓ |
| Overall prefactor | 1/3 | 1/3 | ✓ |
| Loop factor | g²/(16π²) = ĝ² | ĝ² = g²/(16π²) | ✓ |

**The formula as quoted is EXACTLY the ε-line of eq. (36). This is not a misremembered equation; it is a real equation from the paper.**

---

## 5. Critical finding — physical identification

The ZENODO document (line 82-95) claims:

> The trace anomaly of a renormalizable gauge theory on a curved background has been analyzed extensively in the Osborn local-coupling framework [...]. When couplings g(x) are promoted to x-dependent quantities, the anomaly picks up a coupling-dependent correction to the Euler-density coefficient: ⟨T^μ_μ⟩ ⊃ ε(g, μ) × (curvature structure). The explicit expression from Osborn (2003), arXiv:hep-th/0302119 eq (36), in Dirac convention for the fermion trace, is: `ε = 1 + (1/3)(29C − 12R_ψ − (5/2)R_φ) × g²/(16π²)`

**This physical identification is NOT what Osborn's paper says.**

Per Section 3 above:
- Osborn's paper: ε is the coefficient of `R ∂_μg ∂^μg` in the local-coupling Lagrangian `L`, where `L` is the portion of the Weyl response that depends on *derivatives* of the coupling.
- ZENODO document: ε is claimed to be "a coupling-dependent correction to the Euler-density coefficient" in the trace anomaly.

These are **different objects**. The Euler-density coefficient in the Weyl response is `a` (eq. 34). ε is in `L`, not beside `G` (the Euler density) in eq. (34).

The ε → trace-anomaly-ratio identification used by GRUT's ZENODO document **does not match Osborn's paper**. This may be a misattribution, a loose paraphrase that obscures the meaning, or a genuine physical argument that requires its own derivation (i.e. why should the coefficient of `R(∂g)²` in the local-coupling Lagrangian be numerically identified with the trace-anomaly ratio of a CTP effective action on S⁴?).

**Either way: identifying ε with the GRUT quantity R = |C_Cosmo/C_FINAL| is NOT a result of Osborn's paper. It is a separate physical identification that the ZENODO document makes but does not derive.**

---

## 6. Combining contributions across gauge groups

**The paper does NOT discuss combining ε contributions across multiple gauge groups (e.g. SU(3) × SU(2) × U(1)).**

Eq. (35)-(36) is explicitly written "For a simple gauge coupling g, with θ = 0" — a *single* gauge group, single coupling. The paper extends to SUSY (N=1, 2, 4) in subsequent equations (37, 38), but never to semi-simple groups.

The ZENODO document's combination rule:

    ε_combined(SM, M_Z) = w_SU3 × ε_SU3 + w_SU2 × ε_SU2 + w_U1 × ε_U1
    w_SU3 ≈ 0.960, w_SU2 ≈ 0.032, w_U1 ≈ 0.008

with justification "reflecting the dominance of QCD through its large coupling" **has no basis in the Osborn paper**. The weights are not derived from the formula. They appear to be chosen such that the combined result equals ~1.15.

This is the **fitted-weights concern** raised by the user's Path B instruction. Osborn provides no mechanism for combining ε across gauge groups. The 0.960/0.032/0.008 numbers are not derived from Osborn (2003); they are a GRUT-side choice.

---

## 7. Other caveats from the paper

1. **"The results are scheme dependent."** Osborn's explicit statement. The values of α, δ, ε, κ, λ depend on the regularization scheme. In dimensional-reduction (DRED) vs. dimensional-regularization (DREG), the results differ by a finite shift `1/ĝ² → 1/ĝ² + (1/3)C`.

2. **Two-loop result, not one-loop.** The paper's main calculation is one-loop. Eq. (36) is labeled as the *two-loop* extension of earlier results [ref 5 in Osborn]. The one-loop analog would have different (smaller) coefficients. The ZENODO document's implicit assumption is that the two-loop form applies to the SM at M_Z — which is a choice, not a derivation.

3. **Appendix A caveat** (from paper): "The coefficient of C in λ is corrected from [5]" — i.e. eq. (36)'s numerical coefficient for λ (323) is an erratum for a prior paper's value. This flags that the Osborn group re-derived these coefficients and found errors in earlier references. Dependence on the published form requires care.

---

## 8. Stage 0 findings summary

| Finding | Status |
|:---|:---|
| Osborn (2003) arXiv:hep-th/0302119 exists and is accessible | ✓ **Verified** |
| Equation (36) exists and matches the GRUT ZENODO quote for ε | ✓ **Verified exactly** |
| Symbol definitions (C, R_ψ, R_φ) match | ✓ **Verified** |
| ε is a trace-anomaly coefficient as claimed in ZENODO doc | ✗ **CRITICAL MISATTRIBUTION**: ε is the coefficient of `R(∂g)²` in the local-coupling Lagrangian L, not the Euler coefficient of the trace anomaly. The Euler coefficient is `a`, a different symbol in eq. (34). |
| Paper discusses combining ε across SU(3) × SU(2) × U(1) | ✗ **Paper does NOT discuss this**. The 0.960/0.032/0.008 weights have no basis in Osborn (2003). |
| Paper's result is scheme-independent | ✗ Paper explicitly states "The results are scheme dependent." |
| Paper is 3-loop (as ZENODO doc implies when paired with GRUT V7's 3-loop CTP claim) | ✗ Paper is **one-loop with some two-loop results**. Eq. (36) is the two-loop form. |

---

## 9. Implications for Stage 1 and beyond

The user's Path B plan (STAGE_0 → STAGE_1-SM_content → STAGE_2-per_gauge_group_ε → STAGE_3-combination_rule → STAGE_4-final_evaluation) faces a **load-bearing obstacle revealed at Stage 0**:

**Stage 3 (deriving the combination rule) cannot be executed from Osborn (2003).**

The paper contains no combination rule for SU(3) × SU(2) × U(1). Any Stage 3 that produces specific weights (0.960/0.032/0.008 or otherwise) must derive them from *some other source* — Yukawa hierarchy arguments, the 3-loop CTP amplitude structure on S⁴, dimensional analysis, or fitting. Since the user's honesty protocol explicitly forbids fitting, the allowable sources are derivations from GRUT's own structure (not Osborn) and would require their own verification step.

**Additionally: the physical identification ε ↔ R needs separate justification.** Osborn's ε is not the object GRUT needs. Even if Stage 1-2 produces a number from the formula, that number is the coefficient of `R(∂g)²` in a local-coupling Lagrangian — not the trace-anomaly ratio `|C_Cosmo/C_FINAL|` that enters `H_inf = (2−R)/(Sτ_0)`. The ZENODO document bridges these with a verbal argument ("the anomaly picks up a coupling-dependent correction to the Euler-density coefficient") that is not supported by the paper.

---

## 10. Recommended next steps

Three options for the user's decision:

**Option A — Stop Path B here.** Stage 0 has revealed that the Osborn identification is not what the ZENODO document claims it is. Proceeding through Stages 1-4 would compute a number from an un-justified physical identification, which would not constitute a derivation of R. The ZENODO document's 1.1537 claim should be retracted or re-framed as "a formula from Osborn's paper whose numerical value happens to be near 1.15 when specific SM content and specific fitted weights are plugged in; its identification with the GRUT trace-anomaly ratio is not established."

**Option B — Continue Path B, but with a revised Stage 3.** Derive the combination rule from GRUT's own CTP structure on S⁴ (not from Osborn). If such a derivation produces specific weights as an OUTPUT, apply them and see what ε_combined produces. If the derivation fails to produce unique weights, report that as an honest negative and stop at Stage 3. This would take Path B from "verify Osborn claim" to "build a new derivation chain inside GRUT that happens to use Osborn's formula as a sub-input."

**Option C — Pivot to a different Path.** Path A (commission or run the full 3-loop graviton self-energy calculation) or Path C (stochastic-inflation A_s prediction) is more likely to produce a genuinely derived number. Path B's attractiveness was that it was supposed to be "pipeline-tractable via a published formula," but Stage 0 reveals that the published formula doesn't compute what we need. Pipeline-tractability is partially preserved under Option B, but Option C may be cleaner.

**I recommend surfacing this finding to the user before executing Stages 1-4.** The honest thing is to STOP here, report Stage 0's findings, and let the user decide whether Path B as originally framed can still produce a defensible result.

---

## Deliverable

- This file: `theory/path_b_osborn/STAGE_0_PAPER_VERIFICATION.md`
- PDF source: retrieved via WebFetch to `/Users/mpg/.claude/projects/...webfetch-*.pdf` (11 pages, 154 KB)
- Raw extracted text: `/tmp/osborn_0302119_full.txt` (via `pypdf`)

No calculations performed. No weights chosen. No identifications made beyond what the paper explicitly says.
