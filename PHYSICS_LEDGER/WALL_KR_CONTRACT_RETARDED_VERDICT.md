# TIER 4 — THE CONTRACT-LEVEL RETARDED K_R: VERDICT

**Date:** 2026-09-01 · **Authorization:** owner (retarded assembly only;
noise α = −2 never enters; ω ≪ H forbidden) · **Instrument:**
`wall_kr_tier4_retarded.py` · **Artifact:**
`WALL_KR_CONTRACT_RETARDED_RESULT.json` (sha `5bad5574…`) ·
**Manifest:** `WALL_KR_CONTRACT_RETARDED_MANIFEST.json` (input hash
provenance). **Battery: 34/34, zero failures, all controls detecting —
after a two-lens adversarial review whose findings were all adopted
(below).** Final artifact sha `d916ef32…`.
**W-0: computed-and-reported, NOT banked. HARD STOP.**

## PRIMARY QUESTION — ANSWERED

*"Does the validated TT-TT-TT gravitational interaction plus the
validated massless TT bath produce a well-defined contract-level
retarded K_R in the declared k → 0-first regime?"*

**YES — within the declared validity domain ω ≫ H, with the local
(scheme) slot carried symbolically and every boundary of the claim
enforced by the instrument itself.** The gravitational vacuum's own
retarded kernel, at contract scope:

    K_R(omega) = Sigma_R(omega)   [(1/2 kappa^2)-weighted probe units]

    Sigma_R(omega > 0) =
        -(3/1280 pi^2) omega^4 [log(mu^2/omega^2) + i pi]
        + H^2 * ( -(13/480 pi^2) omega^2 [log(mu^2/omega^2) + i pi] )
        + [ c0 + c2 omega^2 + c4 omega^4 + H^2 (c0p + c2p omega^2) ]

with the H¹ sector identically zero (frozen T3 structural result). The
bracketed real polynomial is the **undetermined D5/scheme slot** —
carried symbolically, never chosen (the frozen renormalization
conditions are deferred; μ is absorbable into c4/c2p). The absorptive
content is EXACT and frozen-input-loaded, not re-derived:
Im Σ_R^{H⁰} = −(3/1280π)ω⁴, Im Σ_R^{H²} = −(13/480π)H²ω².

## WHAT WAS BUILT

- **Retarded completion (the tier's only new analytic content):** the
  unique upper-half-plane completion of each frozen scale-free
  absorptive law, gated two ways: (i) its Im part equals the frozen
  values exactly; (ii) an INDEPENDENT numeric 5×-subtracted
  principal-value Kramers–Kronig transform of the absorptive law
  reproduces the log-form's polynomial-free fifth derivative
  (rel 7×10⁻³, finite-difference-limited).
- **Both Dyson objects, kept separate:** G₁ = G₀ + G₀ΣG₀ and
  G_R = 1/(G₀⁻¹ − Σ), with the exact symbolic identity
  G_R − G₁ = G₀³Σ² + O(Σ³) gated, and the agreement domain |λ| ≪ 1
  (λ = 2κ²Σ/ω² ~ (κω)²·logs) reported per the frozen charter's
  resummation-validity mandate.
- **The validity domain, hard-wired:** ε_H = (104/9)H²/ω².
  ε_H ≤ 0.1 CONTROLLED; 0.1–1 returned only with an explicit BOUNDARY
  flag; **ε_H ≥ 1 REFUSED by the evaluator** — and the refusal is
  itself a gated control (an attempted ω = H evaluation raises
  DomainRejected; the truncated H series is never extrapolated).
- **Influence-action normalization (T4-6):** K_R = Σ_R derived from the
  SK r–a quadratic structure (executable identity chain, not an
  import); passivity Im G_R(ω>0) < 0 verified in-domain as an external
  consistency check of the Tier-2 orientation chain.

## ANALYTIC STRUCTURE (T4-8) — classified, nothing assumed

- **Branch structure (unconditional):** a branch point at ω = 0 with a
  real-axis cut — the gapless two-graviton continuum; present in both
  Dyson forms; one-loop in origin.
- **Poles:** the massless graviton's double zero of G₀⁻¹ at ω = 0
  survives iff c0 = 0 — a D5 renormalization condition, DEFERRED,
  recorded parametrically (c0 ≠ 0 shifts it; no choice made).
  **No additional zeros of the resummed denominator on the real
  controlled segment**, established by a pointwise grid bound PLUS an
  executable interval sup bound (with the controlled-band H²
  contribution included) — **triply conditional and frozen as such:
  reference slice c = 0, κ = 0.1 units, μ = 1** (the local slot is
  undetermined, so no slice-independent claim is possible; the review
  demanded and received this conditionality in the artifact itself).
  This is NOT a Rouché/contour statement: the complex-plane and
  general-slice statements remain parametric prose. Pole-from-cut
  candidates require (κω)²|log| ~ 1 — outside the EFT domain; **no
  pole claim is made**, and the matter-K_R pole result is neither
  imported nor assumed.
- **Second sheet:** the log continuation L → L − 2πi is declared; no
  in-domain second-sheet content; no certification attempted (no
  in-domain candidate exists to certify).

## WARD (T4-9)

The frozen T3 record's nonzero gauge-image contraction is carried:
classification **same class** (the graviton-loop analogue of the
Class-B structure persists). K_R is TT-scoped by the frozen charter
(§6): the residual is EXCLUDED by construction — not resolved, not
repaired, and K_R was not altered to change it.

## CHECKS AND CONTROLS (T4-7)

Flat limit == frozen T3 exactly (#1); H² == frozen IR-check exactly
(#2); isotropy and routing cited as executed T3 gates with artifact
pins (#3, #5); retarded/advanced conjugate pair (#4); vertex/bath
normalization through the dimensions gate and the κ-power chain (#6);
first-order/resummed distinction exact (#7); wrong-retarded-sign
detected by passivity (#8); wrong-symmetry-factor detected by the flat
anchor (#9); **the ω/H extrapolation control is REJECTED by the
instrument as required (#10)**; numeric evaluator-chain integrity at
ω/H = 130 (#11). Noise fence: nothing reads nk_wigner or any
Σ_> + Σ_< object — the α = −2 finding remains a separate SK-state
record, untouched.

## DEFECT HISTORY AND REVIEW DISPOSITIONS (all adopted, disclosed)

Run 1: six failures from ONE bug — the frozen-artifact loader mapped
positive-assumed symbols while sympify produces plain ones (the
campaign's recurring identical-printing-symbols trap, fourth
appearance). Drafting catches: a missing factor 2 in the KK stencil; a
principal-value window the first quadrature would have entered.

**Adversarial review (two lenses) before this freeze — physics all
NOT-REFUTED** (the completion re-derived independently; the SK factor
chain re-derived; passivity shown structural: Im G_R = Im Σ/|D|²).
**Four MAJOR instrument findings, all repaired in the frozen run:**
(1) domain enforcement was per-site — |λ| < 1 is now enforced INSIDE
the evaluator and every production flag is asserted, never discarded;
(2) the "Rouché-class" language overclaimed and the artifact's poles
summary had dropped its conditionality — the campaign's known
κ-conditional-verdict defect class — renamed to the honest
pointwise+interval real-axis bound with all conditions frozen into the
artifact (and the first interval draft wrongly called H = 0 the worst
case; the H² band adds and is now included); (3) check #7 had proven
the Dyson identity on a parallel toy — it now ties the toy to the
SHIPPED objects and exercises G₁ numerically (G₁ no longer ships
uncertified); (4) a provenance hole — the file actually read for the
H⁰ datum and the Ward record was unpinned — both files are now
hard-pinned and the Ward string is provenance-locked through two
independently hashed artifacts.

## SCOPE LIMITATIONS

k_ext = 0 evaluation point of the D1 limit (Σ's O(k²) not computed —
T3 scope, disclosed; the dressing's own k → 0 continuity is gated
here). Base-time independence through O(H²) (review-verified on the
frozen cone data). The local slot is symbolic: every numeric statement
uses the DECLARED reference slice c = 0 and says so. ω ≲ H is not
covered and the instrument refuses it. The benchmark consequence, the
J(ω) comparison, D5's conditions, the Ward repair, and the noise-sector
fork decision all remain downstream and owner-held.

## HARD STOP

No benchmark consequence, no J(ω), no Ward/Bardeen work, no bridge, no
added operators, no sign changes, no ω ≪ H, no noise import. **The
retarded contract K_R record is frozen pending owner adjudication.**
