# Gate 3 Hminus-Derivative-Regularized Branch Specification

**Date:** May 15, 2026  
**Status:** Specification phase (no code yet)  
**Motivation:** massive_regulated branch exhausted; derivative regularization is the primary target candidate.

---

## Purpose

Extract the Euler-channel 3-loop coefficient $C_{\text{Euler}}^{(3)}$ from the massless/IR-sensitive Allen-Jacobson branch without triggering the boundary singularities and endpoint pathologies observed in massive_regulated.

The branch must define a mathematically coherent and physically defensible prescription for taking $h_- \to 0$ (the zero-mode limit) while preserving finite, interpretable Laurent coefficients.

---

## AJ Parameter Definition

### Full Parameter Specification

The Allen-Jacobson hypergeometric kernel is:

$$K(u,\epsilon) = {}_2F_1\left(h_+, h_-; \frac{D}{2}; u\right)$$

where:
- $u = \frac{1+Z}{2}$, with $Z \in [-1, 1]$ (integration variable)
- $D = 4 - 2\epsilon$ (dimension-regularized)
- $\epsilon \to 0$ is the expansion parameter
- $h_\pm(\mu^2, D)$ are the branch parameters

For the **massive_regulated branch** (failed), we had:
$$h_\pm = \frac{D-1}{2} \pm \sqrt{\frac{(D-1)^2}{4} - \frac{m^2}{H^2}}$$

For the **hminus_derivative_regularized branch** (this spec):
- $h_+ = D - 1$ (massless minimally-coupled, non-renormalized)
- $h_- = \alpha \to 0$ (treated as a regulator parameter, not a mass)

The choice $h_+ = D-1$ follows from standard CTP/Keldysh conventions for minimally coupled scalars without massive deformation.

---

## The Integral Object

### Full Cube Integral

The Euler-channel 3-loop coefficient is encoded in:

$$I(h_-, \epsilon) = \int_{-1}^{1} \left[{}_2F_1(h_+, h_-; D/2; u)\right]^3 (1-Z^2)^{(D-3)/2} dZ$$

where $u = (1+Z)/2$, $Z = 2u-1$, and $(1-Z^2)^{(D-3)/2} = [4u(1-u)]^{(D-3)/2}$.

In the $u$ variable, $u \in [0, 1]$:

$$I(h_-, \epsilon) = 2 \cdot 4^{(D-3)/2} \int_0^1 {}_2F_1(h_+, h_-; D/2; u)^3 \, u^{(D-3)/2} (1-u)^{(D-3)/2} du$$

### Expected Behavior

As $h_- \to 0$ with $D = 4 - 2\epsilon$ held fixed:

1. The hypergeometric function reduces: ${}_2F_1(D-1, h_-; D/2; u) \to {}_2F_1(D-1, 0; D/2; u) = (1-u)^{-(D-1)}$
2. **But** the integral in the full form exhibits singularities. The Laurent expansion in $h_-$ is expected to have the structure:

$$I(h_-,\epsilon) = \frac{A_{-p}(\epsilon)}{h_-^p} + \cdots + \frac{A_{-1}(\epsilon)}{h_-} + A_0(\epsilon) + A_1(\epsilon) h_- + A_2(\epsilon) h_-^2 + \cdots$$

for some finite $p \geq 1$. The coefficients $A_k(\epsilon)$ depend on $\epsilon$ and must each be expanded in powers of $\epsilon$.

---

## Pole Structure Analysis

### Why Direct $h_- \to 0$ Fails

Setting $h_- = 0$ directly in the integrand produces:

$${}_2F_1(D-1, 0; D/2; u) = (1-u)^{-(D-1)} = (1-u)^{-(4-2\epsilon-1)} = (1-u)^{-(3-2\epsilon)}$$

Combined with the measure $(1-u)^{(D-3)/2} = (1-u)^{(1/2 - \epsilon)}$, the full integrand behaves as:

$$(1-u)^{-(3-2\epsilon)} \cdot (1-u)^{3(1/2-\epsilon)} \cdot (1-u)^{1/2-\epsilon} = (1-u)^{-(3-2\epsilon) + 3/2 - 3\epsilon + 1/2 - \epsilon} = (1-u)^{-2-2\epsilon}$$

This integral **diverges** at $u \to 1$:

$$\int_0^1 (1-u)^{-2-2\epsilon} du = \frac{(1-u)^{-1-2\epsilon}}{-1-2\epsilon}\bigg|_0^1 \to \infty$$

**Physical meaning:** The zero-mode / IR divergence is real. Direct substitution is not valid.

### Laurent Expansion Strategy

Instead of direct substitution, we expand in $h_-$ as a formal parameter:

1. For each power of $h_-$, compute the coefficient function $A_k(\epsilon)$ by extracting the $h_-^k$ term from the Taylor expansion of $I(h_-, \epsilon)$ around $h_- = 0$.
2. Each $A_k(\epsilon)$ will itself have a Laurent expansion in $\epsilon$.
3. The **pole in $h_-$** must be present due to the zero-mode structure; the question is **which coefficient** after pole subtraction represents the physical Euler coefficient.

---

## Three Candidate Prescriptions

### Prescription 1: Finite-Part Prescription

**Definition:**

Expand $I(h_-, \epsilon) = h_-^{-p} A_{-p}(\epsilon) + \cdots + h_-^{-1} A_{-1}(\epsilon) + A_0(\epsilon) + \cdots$

Extract the coefficient:

$$C_{\text{Euler}}^{(3), \text{FP}} = A_0(\epsilon) \bigg|_{\epsilon \to 0}$$

**Interpretation:** The finite part after subtracting all poles in $h_-$. Analogous to dimensional-regularization finite-part prescriptions in standard QFT.

**Pros:**
- Straightforward pole subtraction
- Analog to familiar FP prescription in renormalization
- Removes zero-mode singularity by construction

**Cons:**
- Loses information about the residues (the $A_k$ for $k < 0$)
- May yield zero or numerically small results if the true physics resides in the pole structure
- Requires tracking all pole orders; ambiguous if multiple pole structures compete

---

### Prescription 2: Derivative-Response Prescription

**Definition:**

Compute the finite part after pole subtraction:

$$I_{\text{FP}}(h_-, \epsilon) = A_0(\epsilon) + A_1(\epsilon) h_- + A_2(\epsilon) h_-^2 + \cdots$$

Then extract the linear response to $h_-$ deformation:

$$C_{\text{Euler}}^{(3), \text{DR}} = A_1(\epsilon) \bigg|_{\epsilon \to 0}$$

Equivalently:

$$C_{\text{Euler}}^{(3), \text{DR}} = \frac{\partial}{\partial h_-} I_{\text{FP}}(h_-, \epsilon) \bigg|_{h_-=0, \epsilon=0}$$

**Interpretation:** The coefficient that measures how the finite-part integral responds to small deformations in $h_-$. Probes the sensitivity of the regulator.

**Pros:**
- Captures dynamical feedback from the regularization parameter
- Non-trivial even if $A_0 = 0$ or very small
- Directly measures the "derivative regularization" aspect

**Cons:**
- May pick up artificial sensitivity if $A_1$ is determined by regularization artifacts rather than physics
- Requires computing the full Taylor series in $h_-$
- No standard precedent in anomaly calculations or loop-integral theory

---

### Prescription 3: Pole-Stripped Derivative Prescription

**Definition:**

If the pole structure is $h_-^{-p}$, define:

$$I_{\text{stripped}}(h_-, \epsilon) = h_-^p I(h_-, \epsilon)$$

This removes the leading pole. Then:

$$C_{\text{Euler}}^{(3), \text{PSD}} = \frac{\partial}{\partial h_-}\left[h_-^{p-1} I(h_-, \epsilon)\right] \bigg|_{h_-=0}$$

Or, more conservatively, if the pole order $p$ is uncertain:

$$C_{\text{Euler}}^{(3), \text{PSD}} = \lim_{h_- \to 0} h_-^{-1} \frac{d}{dh_-}\left[\operatorname{FP} I(h_-, \epsilon)\right]$$

**Interpretation:** The derivative of the pole-normalized integral, capturing the "residue rate" — how quickly the physical content emerges from the zero-mode singularity.

**Pros:**
- Directly probes residue structure
- Invariant under rescaling of $h_-$ (natural for a regulator)
- Connects to Feynman-parameter derivative tricks

**Cons:**
- Most abstract; hardest to compute
- Introduces an additional derivative, multiplying per-term complexity
- Ambiguous if $p$ is not cleanly determined

---

## Acceptance Criteria

Any successful branch must satisfy:

1. **Finiteness:** The extracted coefficient is finite after $\epsilon \to 0$. No divergences, no spurious infinities.

2. **Pole characterization:** The pole order $p$ in $h_-$ is determined and consistent across the integration interval. Document the exact pole structure.

3. **Epsilon expansion:** The result has a well-defined expansion in $\epsilon$. At minimum, the $\epsilon^0$ (finite) and $\epsilon^{-1}$ (pole) terms must be accessible.

4. **Universality check:** Re-compute with a different conformal frame (e.g., variable change $w = 1 - u$) or parametrization. The coefficient must be invariant or transform predictably.

5. **Known-limit consistency:** If any subcase reduces to a known formula (e.g., conformal scalar at massless limit, or tree-level), verify the coefficient.

6. **Sign and scale consistency:** The coefficient must have a sign compatible with physical loop corrections (e.g., not absurdly small or absurdly large relative to tree-level or other loop contributions). Avoid outputs like $10^{160}$ without physical justification.

7. **Stability under D variation:** Compute at $D = 4 - 2\epsilon$ for multiple small $\epsilon$ values (e.g., $\epsilon = 10^{-2}, 10^{-3}, 10^{-4}$). The extracted coefficient should vary smoothly, not jump or oscillate.

8. **Endpoint-singularity absence:** The integration over $u \in [0, 1]$ must not exhibit the boundary pathologies (precision loss, overflow, slow convergence, global-error growth) observed in massive_regulated Route D.

---

## Non-Claim

**This specification is NOT tuned to land a specific value for $C_{\text{Euler}}^{(3)}$ or $R_{\text{3-loop}}$.**

In particular:
- We do not choose the prescription to yield $R = 1.15428$ or any other predetermined answer.
- We do not select among the three candidate prescriptions based on which one produces the "desired" output.
- If all three prescriptions fail the acceptance criteria, that is an honest result: hminus_derivative_regularized does not exist or requires further theoretical work.
- If the prescriptions succeed but yield conflicting answers, that conflict is documented and interpreted, not hidden.

---

## Implementation Guardrails

**These guardrails prevent specification drift and ensure honest evaluation. They are binding commitments, not guidelines.**

### 1. Freeze Spec Hash Before Coding

- Commit this specification document to git with a signed tag: `gate3-hminus-dr-spec-v1.0`
- Include hash in Mathematica/Python harness code comments
- Any changes to the specification (acceptance criteria, prescription definitions, test cases) require:
  - New spec version tag (v1.1, etc.)
  - Explicit recorded rationale in git log
  - Re-testing under the new spec before promotion
- **Purpose:** Prevent accidental drift if one prescription starts looking numerically attractive during implementation

### 2. Blind Classification Protocol

**Phase A: Extraction (output only coefficients and pole structure)**
- Mathematica harness outputs: $(h_-, I(h_-, \epsilon))$ pairs, Laurent fit quality, pole order $p$
- No reference to desired $R$ value, no statements about "good" or "bad" outputs
- File: `gate3_hminus_dr_laurent_extraction.json`

**Phase B: Prescription Application (blind to iteration context)**
- Python script reads extraction JSON
- Computes all three prescriptions: $C^{(3), \text{FP}}$, $C^{(3), \text{DR}}$, $C^{(3), \text{PSD}}$
- Outputs results with labels: "prescription_1", "prescription_2", "prescription_3" (not by name)
- File: `gate3_hminus_dr_prescription_coefficients.json`

**Phase C: Classification (acceptance criteria check)**
- Separate harness reads prescription JSON
- For each prescription, checks all eight criteria independently
- Outputs: 3-tuple of pass/fail per criterion, with evidence
- No comparison to desired $R$ until classification complete
- File: `gate3_hminus_dr_classification_report.md`

**Only after classification complete:** compare final values to known targets and interpret

### 3. Separation of Concerns: Three Sequential Outputs

```
gate3_hminus_dr_laurent_extraction.json
  ├── h_minus_values: [0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001]
  ├── epsilon_values: [0.01, 0.005, 0.002, 0.001]
  ├── I_samples: { (h_minus, epsilon): value, ... }
  ├── laurent_fit_quality: MSE, R²
  ├── pole_order: p (determined empirically)
  └── coefficients: { A_k(ε): [ c_{k,0}, c_{k,1}, ... ] }

gate3_hminus_dr_prescription_coefficients.json
  ├── prescription_1: { epsilon_to_0: X, epsilon_to_minus_1: Y, ... }
  ├── prescription_2: { epsilon_to_0: X, epsilon_to_minus_1: Y, ... }
  ├── prescription_3: { epsilon_to_0: X, epsilon_to_minus_1: Y, ... }
  └── extraction_metadata: hash, date, harness_version

gate3_hminus_dr_classification_report.md
  ├── prescription_1: { criterion_1: pass, criterion_2: fail, ... | reason: ... }
  ├── prescription_2: { criterion_1: fail, criterion_2: pass, ... | reason: ... }
  ├── prescription_3: { criterion_1: pass, criterion_2: pass, ... | reason: ... }
  └── summary: which prescriptions pass all 8 criteria
```

### 4. Robustness Test: "No Landing by Construction"

**If a prescription looks numerically attractive, test whether it's robust or fragile:**

Perturbation suite:
- Vary sample spacing: $h_-$ grid from $(10^{-3}, 10^{-1})$ with different densities
- Vary numerical precision: Working precision 60, 100, 150
- Vary integration method: NIntegrate settings (precision goal, accuracy goal)
- Vary normalization: multiply $I(h_-, \epsilon)$ by $(1 \pm 10^{-2})$
- Vary endpoint regulator: if any small regulator added near boundaries, how stable is fit?

**Test result:** Do all perturbations land the same prescription, or only one fragile configuration?
- All perturbations → robust branch
- Single fragile config → likely artifact; classify as "numerical accident"
- Each perturbation gives different prescription → ill-posed problem

### 5. Failure as a Success Condition

**If all three prescriptions fail the eight acceptance criteria:**

This is not a disaster. It is a **valuable negative result**:

- Gate 3 does NOT have a viable Euler-channel extraction route via Allen-Jacobson / S⁴ regularization
- The problem is not numerical; it is mathematical
- The next step is deeper theory (alternative integral representations, contour deformations, Mellin transforms, etc.)
- GRUT's loop-corrected R derivation via this route is blocked
- Alternative routes (tree-level R = 4/3, Osborn route, decoherence sector) remain open

**Document this failure explicitly:**
```markdown
# Gate 3 Negative Result (Date)

The hminus_derivative_regularized branch, tested under three candidate prescriptions,
failed to produce finite, universal, and physically interpretable coefficients.

Prescriptions 1, 2, 3 failed criteria [list specific failures].

**Implication:** The Allen-Jacobson / S⁴ / Euler-channel route to loop-corrected R
does not have a tractable implementation with standard regularization methods.

**Recommended alternatives:**
- Fourier/Mellin methods on alternative integral representations
- Complex-plane contour deformations
- Dispersion relations
- Numerical conformal bootstrap

GRUT's zero-parameter chain remains viable; this gate is architecturally independent.
```

---

## Implementation Plan (Guardrail-Compliant)

### Step 1: Spec Commit & Tag

```bash
git add theory/hard_theory/GATE3_HMINUS_DERIVATIVE_REGULARIZED_SPEC.md
git commit -m "SPEC: Gate 3 hminus_derivative_regularized with three prescriptions and eight criteria"
git tag -s gate3-hminus-dr-spec-v1.0 -m "Gate 3 hminus_derivative_regularized specification, frozen before implementation"
```

Include spec hash in all harness code:
```python
# Specification hash: git tag gate3-hminus-dr-spec-v1.0
# If this code runs against a newer spec version, analysis is invalid.
SPEC_VERSION = "1.0"
```

### Step 2: Phase A – Laurent Extraction Harness

**Output file:** `gate3_hminus_dr_laurent_extraction.json`

Build Mathematica/HypExp script:
1. Implement $I(h_-, \epsilon)$ as full cube integral with $h_- = \alpha$ free parameter
2. Loop over $h_-$ values: $[0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001]$
3. For each $(h_-, \epsilon)$ pair, numerically integrate using HypExp
4. Collect raw samples: $(h_-, \epsilon, I_{\text{value}})$
5. Fit Laurent expansion: $I(h_-, \epsilon) = \sum_k A_k(\epsilon) h_-^k$
6. Determine pole order $p$ empirically (where coefficients $A_{-p}, ..., A_{-1}$ are nonzero and $A_0$ is first regular term)
7. Extract final Laurent coefficients: $A_{-p}, ..., A_0, A_1, A_2, ...$
8. Record fit quality: MSE, $R^2$ of polynomial fit

**Output schema:**
```json
{
  "spec_version": "1.0",
  "date": "2026-05-15",
  "h_minus_values": [0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001],
  "epsilon_values": [0.01, 0.005, 0.002, 0.001],
  "I_samples": {
    "(0.1, 0.01)": 1.2345,
    "(0.1, 0.005)": 1.2367,
    ...
  },
  "laurent_fit": {
    "pole_order": 1,
    "coefficients": {
      "A_{-1}": [coeff_0, coeff_1, ...],
      "A_0": [coeff_0, coeff_1, ...],
      "A_1": [coeff_0, coeff_1, ...],
      ...
    },
    "fit_quality_mse": 1.2e-6,
    "fit_quality_r2": 0.99998
  }
}
```

### Step 3: Phase B – Prescription Application (Blind)

**Input:** `gate3_hminus_dr_laurent_extraction.json`  
**Output file:** `gate3_hminus_dr_prescription_coefficients.json`

Python script (no reference to desired $R$ or $C_{\text{Euler}}$):
1. Load extraction JSON
2. For each prescription:
   - **Prescription 1 (FP):** Extract $C^{(3), \text{FP}} = A_0(\epsilon=0)$
   - **Prescription 2 (DR):** Extract $C^{(3), \text{DR}} = A_1(\epsilon=0)$
   - **Prescription 3 (PSD):** Compute derivative of pole-stripped integral (implement as specified in Candidates section)
3. For each prescription, expand in small $\epsilon$ to extract $\epsilon^0$ (finite) and $\epsilon^{-1}$ (pole)
4. Output coefficients with generic labels (not names)

**Output schema:**
```json
{
  "spec_version": "1.0",
  "extraction_date": "2026-05-15",
  "prescriptions": {
    "prescription_1": {
      "definition": "finite-part: A_0(epsilon=0)",
      "epsilon_to_0_finite": 1.2345,
      "epsilon_to_0_pole": 0.0123,
      "expansion_terms": [1.2345, 0.0123, -0.00045, ...],
      "fit_residual": 1e-8
    },
    "prescription_2": {
      "definition": "derivative-response: A_1(epsilon=0)",
      "epsilon_to_0_finite": 2.3456,
      "epsilon_to_0_pole": -0.0234,
      "expansion_terms": [2.3456, -0.0234, ...],
      "fit_residual": 2e-8
    },
    "prescription_3": {
      "definition": "pole-stripped-derivative: d/dh_- [FP I] at h_-=0",
      "epsilon_to_0_finite": 0.9876,
      "epsilon_to_0_pole": 0.00567,
      "expansion_terms": [0.9876, 0.00567, ...],
      "fit_residual": 3e-8
    }
  }
}
```

### Step 4: Phase C – Blind Classification

**Input:** `gate3_hminus_dr_prescription_coefficients.json`  
**Output file:** `gate3_hminus_dr_classification_report.md`

Python script evaluates each prescription against the eight criteria:

1. **Finiteness:** Does $\epsilon^{-1}$ coefficient vanish or is it small relative to finite part?
2. **Pole characterization:** Is pole order $p$ consistent? Does it match mathematical expectation?
3. **Epsilon expansion:** Are higher-order $\epsilon$ terms well-defined? No divergence patterns?
4. **Universality check:** (If available) does coefficient match known limits?
5. **Known-limit consistency:** Compare to conformal scalar or tree-level where possible
6. **Sign and scale:** Is magnitude reasonable? Not $10^{160}$ or $10^{-160}$?
7. **Stability under D variation:** Recompute at slightly perturbed $D$ values; does coefficient vary smoothly?
8. **Endpoint singularity absence:** NIntegrate warnings? Precision loss? Global error growth?

**Report format:**
```markdown
# Gate 3 Hminus-Derivative-Regularized Classification Report

Date: 2026-05-15
Spec version: 1.0

## Prescription 1: Finite-Part

| Criterion | Result | Evidence |
|-----------|--------|----------|
| Finiteness | PASS | ε^{-1} term = 0.0123, finite part = 1.2345; ratio 0.01 < threshold 0.1 |
| Pole characterization | PASS | Pole order p=1 confirmed across all h_- samples; consistent |
| Epsilon expansion | PASS | Terms [1.2345, 0.0123, -0.00045, ...] show smooth decay; no divergence |
| Universality check | INCONCLUSIVE | No available conformal comparison |
| Known-limit consistency | PASS | Matches conformal scalar at h_+ = D/2, h_- = (D-2)/2 to 2% |
| Sign and scale | PASS | Magnitude 1.2345; physically reasonable for loop correction |
| Stability under D variation | FAIL | Coefficient jumps from 1.2 to 1.8 as D moves from 4-ε to 4-1.2ε; unstable |
| Endpoint singularity absence | FAIL | NIntegrate warnings at u→1: "Slow convergence in dimension 4-0.02" |

**Overall:** 5/8 criteria pass; 2 failures (stability, endpoint); 1 inconclusive

## Prescription 2: Derivative-Response

[Same format...]

**Overall:** 6/8 criteria pass; 1 failure (universality); 1 inconclusive

## Prescription 3: Pole-Stripped Derivative

[Same format...]

**Overall:** 7/8 criteria pass; 1 failure (endpoint singularity); 0 inconclusive

## Summary

No prescription passes all eight criteria. Prescriptions 2 and 3 come closest.

Recommend: Further mathematical investigation required.
```

### Step 5: Robustness Testing (if any prescription passes ≥ 7 criteria)

Perturbation suite:
1. **Sample density:** Increase $h_-$ samples to 20+ values; does fitted coefficient change?
2. **Precision:** Recompute with WorkingPrecision 100 and 150; stable?
3. **Integration settings:** Vary NIntegrate MaxRecursion and precision goals; robust?
4. **Normalization shock:** Multiply $I(h_-, \epsilon)$ by $(1 + 0.01)$ and $(1 - 0.01)$; coefficient robust?
5. **Endpoint regulator:** Add small $\delta(1-u)^k$ term for $k = 0.1, 0.01$; coefficient unchanged?

Report: "Robust across 5 perturbation classes" or "fragile: only survives in configuration X"

### Step 6: Final Interpretation

**Only after classification complete**, compare results to:
- Known $R = 4/3$ (tree level)
- Osborn decoherence route outputs
- Desired loop-corrected targets (if any)

Interpretation: Which prescription, if any, produces physically consistent results? Is it the "best" because it lands near a target, or because it passes criteria independently?

---

## References

- [GATE3_AJ_PARAMETER_BRANCHES.md](GATE3_AJ_PARAMETER_BRANCHES.md) — Branch table and conformal benchmark
- [GATE3_MASSIVE_REGULATED_REDUCTION.md](GATE3_MASSIVE_REGULATED_REDUCTION.md) — Why massive_regulated does not work
- [GATE3_EULER_3LOOP_STATUS.md](GATE3_EULER_3LOOP_STATUS.md) — Overall Gate 3 status and next steps
- [GRUT_TOE.md](../GRUT_TOE.md) — Context on the role of the Euler-channel coefficient in the broader GRUT chain

---

## Status

**Date created:** May 15, 2026  
**Author:** Gate 3 Specification Phase  
**Approval:** Specification complete; ready for implementation.  
**Next step:** Implement Mathematica/HypExp harness to measure $I(h_-, \epsilon)$ for multiple $h_-$ values.
