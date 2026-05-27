# Gate 3 Coefficient-Role Assignment Specification

Date: 2026-05-26
Branch: v2
Seed: C_seed^(3) = π/2  (exact analytic value, 4·B(3/2,3/2))
Status: role_unassigned  (default until all criteria resolve)

---

## Purpose

The Allen–Jacobson S⁴ integral has produced an exact analytic seed:

$$C_{\mathrm{seed}}^{(3)} = \frac{\pi}{2}$$

This gate determines what role that seed plays in the GRUT quotient system.
A coefficient is only "promoted" when its role is unambiguously assigned —
not when the number is elegant.

---

## Role Taxonomy

| Status | Code | Meaning |
|---|---|---|
| Role unassigned | `role_unassigned` | Default; evidence incomplete |
| Final coefficient candidate | `final_coefficient_candidate` | Can enter C_Euler,final |
| Cosmo coefficient candidate | `cosmo_coefficient_candidate` | Can enter C_Euler,cosmo |
| Shared normalization | `shared_normalization` | Appears in N and D; cancels in R |
| Branch normalization | `branch_normalization` | Validates branch extraction; not quotient-bearing |
| Benchmark seed | `benchmark_seed` | Useful cross-check; no direct R implication |
| Rejected | `rejected` | Cannot enter quotient; evidenced disqualification |

Only one status may be assigned at a time. The default is `role_unassigned`.

---

## Six Evidence Criteria

All six must be assessed before a non-default status can be assigned.

### Criterion R1 — Operator Source

**Question**: Which term in the CTP effective action produces the S⁴ Allen–Jacobson integral?

**Required evidence**:
- Identify the vertex in the CTP action that generates the three-loop S⁴ diagram
- Confirm the integral is a loop contribution, a tree-level normalization, or a topological term
- Record the field content of the source vertex (graviton, matter, gauge)

**Disqualifying findings**:
- If the source vertex is not present in the CTP action, the seed is `benchmark_seed` only
- If the source is a contact term, it may be `branch_normalization`

**Current status**: NEEDS_THEORY

---

### Criterion R2 — Projection Target

**Question**: What geometric/topological object does the S⁴ seed project onto in the effective action?

**Candidate targets**:

| Target | Code | Role implication |
|---|---|---|
| Euler density $\mathcal{E}_4$ | `euler_density` | Strong candidate for C_Euler |
| Pontryagin density | `pontryagin` | Different coefficient family |
| $R \log \Box R$ term | `log_nonlocal` | Non-local; different gate |
| Cosmological constant | `cosmo_const` | C_Euler,cosmo candidate |
| Overall normalization | `normalization` | May cancel in quotient |
| Unknown | `unknown` | Cannot assign role |

**Partial evidence available**:
- S⁴ is the round 4-sphere: $\chi(S^4) = 2$, so S⁴ is a natural test manifold for Euler-class invariants
- The Euler density on S⁴ integrates to $8\pi^2 \chi(S^4) = 16\pi^2$ (normalized)
- The prefactor $4 = 2 \cdot 4^{1/2}$ in $I(0,0)$ suggests the coefficient is measuring a density, not a topological index directly

**Current status**: PARTIAL — S⁴ topology consistent with Euler density, but projection operator not confirmed

---

### Criterion R3 — Quotient Position

**Question**: Does $C_{\mathrm{seed}}^{(3)}$ appear in the numerator $N$, denominator $D$, both, or neither of the GRUT quotient $R = N/D$?

**Sub-questions**:
- Is the quotient $R$ defined with C_Euler in the numerator (cosmological side)?
- Is C_Euler in the denominator (gravitational/metric side)?
- Does the quotient structure predict a specific ratio between the two sides?

**Blocking dependency**: Criterion R2 (projection target) must be resolved first. If the seed projects onto the Euler density, its position in the quotient depends on which side of R the Euler density belongs to.

**Current status**: BLOCKED — requires R2 resolution

---

### Criterion R4 — Scheme Behavior

**Question**: Is the seed protected under regularization-scheme changes, or scheme-fragile?

**Available numerical evidence**:

| Evidence | Value | Interpretation |
|---|---|---|
| D3 c-independence (universality) | spread = 1.97e-4 (< 1%) | Path-independent; suggests protection |
| D1 vs D3 agreement | Δ = 2.9e-5 | Consistent across independent prescriptions |
| D2 vs D1 discrepancy | Δ = 1.3e-3 | Scheme-order-dependent; non-commutativity |
| Stage-2 ε-expansion residual (D1) | 2.32e-5 | Smooth ε-dependence |

**Interpretation**: The D1/D3 agreement at the 3e-5 level, combined with D3 c-independence, suggests the seed is protected under path-direction changes. However, D2's order-of-limits sensitivity shows a non-trivial regularization dependence in the ε-first direction. The protected value is the D1/D3 consensus at $\pi/2$; D2 indicates this protection requires taking $h_- \to 0$ before (or simultaneously with) $\varepsilon \to 0$.

**Current status**: PARTIAL — universality and prescription-independence support protection; order-of-limits sensitivity noted as structural (not disqualifying)

---

### Criterion R5 — Cancellation Check

**Question**: If the seed appears in both numerator and denominator of R, does it cancel?

**Method**: Compute R with and without the seed and compare.

**Blocking dependency**: Cannot evaluate until R3 (quotient position) is resolved.

**Current status**: BLOCKED — requires R3 resolution

---

### Criterion R6 — Landing Eligibility

**Question**: Does the seed satisfy the Gate 3 coefficient landing interface conditions?

**Sub-conditions**:
- [ ] Seed was produced by a pre-registered, blinded protocol (yes — Phase A/B/C)
- [ ] At least two independent prescriptions agree (yes — D1 and D3)
- [ ] Endpoint objection resolved (yes — endpoint-split validation)
- [ ] No R promotion made prematurely (yes — R not promoted)
- [ ] Coefficient-role gate opened before landing (yes — this document)
- [ ] Role assigned before landing (NO — role_unassigned; gate open)

**Current status**: PARTIALLY SATISFIED — numerical side complete; role assignment pending

---

## Preliminary Assessment

| Criterion | Status | Blocking? |
|---|---|---|
| R1 Operator source | NEEDS_THEORY | Yes — must identify CTP vertex |
| R2 Projection target | PARTIAL | Yes — must confirm Euler density projection |
| R3 Quotient position | BLOCKED | Yes — blocked by R2 |
| R4 Scheme behavior | PARTIAL | No — supports candidate status |
| R5 Cancellation check | BLOCKED | No — blocked by R3 |
| R6 Landing eligibility | PARTIAL | Yes — role must be assigned first |

**Current role assignment**: `role_unassigned`

**Promotion-review eligible**: Yes (D1/D3 numerical evidence complete; endpoint validation done)

**Blocking path to role assignment**: R1 → R2 → R3 → R5

---

## Decision Tree

```
Start: C_seed^(3) = π/2, role_unassigned
  │
  ├─ R1: Identify CTP vertex
  │    Not found → benchmark_seed
  │    Found → continue
  │
  ├─ R2: Identify projection target
  │    euler_density → continue
  │    cosmo_const   → cosmo_coefficient_candidate (pending R3)
  │    normalization → shared_normalization (pending R5)
  │    unknown       → role_unassigned
  │
  ├─ R3: Determine quotient position
  │    numerator only → cosmo_coefficient_candidate
  │    denominator only → final_coefficient_candidate
  │    both → check R5
  │    neither → branch_normalization
  │
  ├─ R5: Cancellation check (if both sides)
  │    cancels → shared_normalization
  │    does not cancel → role determined by relative weight
  │
  └─ R6: Landing eligibility
       all sub-conditions met → role landing approved
       sub-conditions unmet → role_unassigned
```

---

## Output Format

The harness `gate3_coefficient_role_assignment.py` produces:

```json
{
  "spec": "gate3-coefficient-role-assignment-spec-v1.0",
  "date": "...",
  "seed_value": 1.5707963268,
  "seed_exact": "pi/2",
  "seed_source": "Allen-Jacobson S4 integral, direct-limit D1/D3",
  "current_role": "role_unassigned",
  "promotion_review_eligible": true,
  "criteria": { ... per-criterion evidence and status ... },
  "blocking_questions": [ ... ],
  "next_action": "Resolve R1 (operator source) to unlock R2 and R3"
}
```

---

## What Would Change the Assessment

| Finding | Role assigned |
|---|---|
| S⁴ vertex is a loop normalization that appears only in D | `final_coefficient_candidate` |
| S⁴ vertex is a loop normalization that appears only in N | `cosmo_coefficient_candidate` |
| S⁴ vertex is the same in N and D (common-mode) | `shared_normalization` |
| S⁴ diagram is a contact term, not a loop | `branch_normalization` |
| S⁴ integral is not present in the CTP action at all | `benchmark_seed` |
| Explicit R computation produces R = f(π/2) with no cancellation | `final_coefficient_candidate` or `cosmo_coefficient_candidate` |

---

## Spec ID

`gate3-coefficient-role-assignment-spec-v1.0`  
Frozen: 2026-05-26
