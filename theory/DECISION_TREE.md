# Decision Tree: What to Execute When the Brother Answers

## Purpose

When the three-sentence email arrives, this doc tells you exactly which
branch to run. No re-deriving, no guessing — just map his letters to the
right action.

---

## Q1: Does CTP select ε (local-coupling) or b/a (constant-coupling)?

### Q1 = A (yes, ε)
**Action:** Plug ε_SU3(M_Z) = 1.1603 directly into the cosmological formula.

```python
from grut.foundation.osborn_assembly import compute_omega_lambda_from_inputs
# Skip the integrated calculation entirely
# Treat 1.1603 as the framework's R directly
R_eff = 1.1603
f_R = 2 - R_eff
H_inf = f_R / (S * tau_0)
Omega_Lambda = (H_inf / H_0)**2
```
Expected: Ω_Λ ≈ 0.6915 (vs Planck 0.6889, +0.4% deviation — well within 2σ)

### Q1 = B (no, b/a)
**Action:** Return to integrated w_g route. Wait for brother's c_w values.

```python
from grut.foundation.osborn_integrated import run_rg_flow
# Use his c_w values, not the inverted one
result = run_rg_flow(c_w_gauge=<brother's value>, n_steps=5000)
```

### Q1 = C (complicated/combination)
**Action:** He specifies the exact combination (e.g., "ε - 0.5·b/a" or
"ε × scheme_factor"). Evaluate whatever formula he writes.

---

## Q2: Does the chain simplify at single-group dominance?

### Q2 = A (yes, R_eff = ε_SU3)
**Action:** QCD alone gives Ω_Λ. EW sectors are 1% correction.

```python
R_eff = 1.1603  # QCD dominant
# Optional: apply the 1% EW correction
eps_SU2 = 1.0186
eps_U1 = 0.9834
# If the combination is additive (uncertain without brother's Q2 answer):
# R_eff_full = R_eff × (1 + 0.01 × some_combo)
```

### Q2 = B (need full sum)
**Action:** Brother provides combination rule. Evaluate all three groups.

If rule is multiplicative: R = ε_SU3 × ε_SU2 × ε_U1 = 1.1596 × 1.0186 × 0.9834 = 1.1622
If rule is summed: R = ε_SU3 + (ε_SU2 − 1) + (ε_U1 − 1) = 1.1596 + 0.0186 − 0.0166 = 1.1616
If rule is weighted by g²: use the 25.3 : 2.9 : −2.6 ratios we already have

Ryan plugs in the formula and reports Ω_Λ.

### Q2 = C (additional factors in the chain)
**Action:** Brother gives the factor X. Multiply:

```python
R_eff = X × 1.1603  # X could be a loop factor, normalization, scheme factor
```

---

## Q3: Is there a known identity?

### Q3 = A (yes, published)
**Action:** Cite it. The derivation is complete from published literature.
Ryan updates v7 appendices to reference the identity and remove
"CONDITIONAL" status from cosmological predictions.

### Q3 = B (derivable, not published)
**Action:** Brother derives it. That's a **new physics result worth
co-authoring**. Ryan offers authorship and writes it up with him.

### Q3 = C (unclear)
**Action:** Document the 0.46% as an observation pending further work.
Integrated w_g route remains available as the longer path.

---

## Combined outcomes

### Best case: A, A, A
**Meaning:** Ω_Λ is derived in one line of algebra from Osborn 2003 eq (36)
+ SM field content + the cosmological formula.

**Action:**
1. Update osborn_assembly.py: set R_eff = ε_SU3(M_Z) = 1.1603
2. Run it. Confirm Ω_Λ ≈ 0.69.
3. Update v7 appendices:
   - Remove "R = 1.15428 asserted" and "CONDITIONAL" labels
   - Replace with "R = ε_SU3(M_Z) from Osborn 2003 eq (36)"
   - Status: DERIVED (zero free parameters)
4. Write paper.

### Middle cases: mixed answers
**Action:** Run the specific branch he indicates. Report whatever Ω_Λ
comes out. Update documentation to reflect the actual derivation path,
honestly.

### Worst case: C, C, C
**Meaning:** Striking numerical coincidence, documented with full honesty.

**Action:**
1. Keep the 0.46% proximity documented in EPSILON_VS_R_QUESTION.md
2. Continue with the integrated w_g route (needs brother's c_w)
3. Treat the ε lead as "further work" — not dismissed, not claimed

---

## Hard rules for whichever branch we land in

1. **No adjusting to hit 0.6889.** Whatever Ω_Λ the pipeline produces
   is the answer. If it's 0.72 or 0.65 instead of 0.69, document the
   deviation. Don't refit.

2. **No quietly changing conventions after the fact.** Dirac counting
   for R_ψ is settled; don't switch to Weyl because it would change
   the answer.

3. **No branching to a different formula mid-calculation.** Pick the
   branch from the brother's answer, run it, report the result. If the
   number looks wrong, the framework is wrong — not the branch choice.

4. **No inversions.** The osborn_integrated.py inversion section is
   commented out or deleted if anyone runs it. Fit-to-target is exactly
   what we spent today removing.

---

## The single-line summary for each outcome

- **A,A,A:** Ω_Λ = (2 − 1.1603)² / (S·τ_0·H_0)² = 0.6915 (**publishable as derived**)
- **A,A,C:** Same number, flagged as "pending confirmation of identity" (**publishable with caveat**)
- **Any B:** Integrated calculation with brother's w_g values (**depends on his number**)
- **C,C,C:** 0.46% coincidence documented; integrated route still open (**publishable as open problem**)

---

## Why this tree is final

Each branch terminates in either a number (with whatever error bars
follow from its provenance) or a labeled open problem. There is no
branch that requires further derivation from us on this side — Ryan's
Python infrastructure already handles every formula. The only missing
inputs are the brother's three yes/no answers.

Once those arrive: one branch executes, one number comes out, paper gets
written (either as "derived" or as "here's the specific open question").

Nothing else is waiting on anything.
