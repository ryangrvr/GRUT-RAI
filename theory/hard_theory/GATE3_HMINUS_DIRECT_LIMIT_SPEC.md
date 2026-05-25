# Gate 3: hminus_direct_limit — Specification (v2)

**Date:** May 24, 2026
**Status:** PROVISIONAL (frozen upon commit)
**Motivation:**
Gate 3 hminus_derivative_regularized identified a structural incompatibility between the derivative-regularization probe family and the medium's IR threshold response. To determine if this is a family-specific or IR-limit-general barrier, we now specify the direct limit route.

---

## 1. Objective

Extract the three-loop Euler coefficient $C_\text{Euler}^{(3)}$ via the Allen-Jacobson closed-S⁴ integral, using direct limit procedures that do not rely on derivative regularization.

---

## 2. Prescriptions (Blind Protocol)

**Three candidate prescriptions (sealed until Phase C):**

- **D1: Sequential limit (h_- first):**
  1. Take $h_- \to 0$ at fixed $\varepsilon$
  2. Then $\varepsilon \to 0$
- **D2: Sequential limit (epsilon first):**
  1. Take $\varepsilon \to 0$ at fixed $h_-$
  2. Then $h_- \to 0$
- **D3: Diagonal limit:**
  1. Take $h_- = c \cdot \varepsilon$ for $c \in \mathbb{R}^+$
  2. Then $\varepsilon \to 0$

All three are implemented as independent code paths. Labels D1/D2/D3 are not revealed to the classifier until after acceptance gating.

---

## 3. Acceptance Criteria (Frozen)

Eight pre-registered, blind-sealed criteria (must pass all to promote $C_\text{Euler}^{(3)}$):

1. **Laurent fit quality:** $R^2 > 0.99999$ for all samples
2. **Epsilon expansion smoothness:** Residual $< 0.0001$ in $\varepsilon \to 0$ extrapolation
3. **Prescription universality:** All three limits yield consistent $C_\text{Euler}^{(3)}$ within 1%
4. **Numerical stability:** No sample fails with error $> 10^{-6}$
5. **Analytic continuation:** No pole or branch cut ambiguity in $h_-$ or $\varepsilon$
6. **Blind protocol integrity:** Classifier receives only generic labels until after gating
7. **Specification compliance:** All code, data, and results traceable to this spec
8. **Reproducibility:** All scripts and data archived in repo

---

## 4. Implementation Guardrails

1. **No tuning to target:** No post-hoc adjustment of prescriptions or thresholds
2. **No code modification after freeze:** Harness and scripts are frozen at commit
3. **Independent code paths:** Each prescription implemented separately
4. **Blind protocol enforced:** Classifier and implementer roles separated
5. **Full traceability:** All results, failures, and decisions documented and committed

---

## 5. Motivation and Decision Tree

- If all three prescriptions fail epsilon_expansion uniformly: **IR limit itself is the barrier** (not just derivative family)
- If one or more succeed: **Derivative family is specifically incompatible**; direct limit is viable

---

## 6. Specification Status

**This document is the canonical citation target for all future work on the hminus_direct_limit route.**

**Status:** PROVISIONAL until committed and all implementation guardrails are verified.
