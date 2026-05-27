# Gate 3 CTP Branch-Incidence Audit

Date: 2026-05-26
Spec: gate3-ctp-branch-incidence-spec-v1.0
Status: R1 = NEEDS_THEORY; role = role_unassigned

---

## Purpose

The vertex provenance audit identified the key fork:

> **V3 (shared normalization)** vs **V4 (CTP branch-response)**: both have high
> structural scores. Theory must distinguish them.

This audit resolves the fork by analyzing the CTP branch-incidence of the three-point
$S^4$ scalar loop using the Schwinger–Keldysh (Keldysh $r/a$) basis.

The central question:

$$\text{Does the loop } I(h_-, \varepsilon) \text{ appear symmetrically on both CTP}$$
$$\text{branches (shared normalization) or on one branch only (quotient-bearing)?}$$

**Key guardrail** (from Ryan): Do not assign V4 because it produces $R = \sqrt{4/3}$.
Assign V4 only if the CTP branch structure demands it.

---

## 1. Keldysh-Basis Machinery

The Schwinger–Keldysh $r/a$ (retarded/advanced, or classical/quantum) basis is defined by:

$$\varphi_r = \frac{\varphi_+ + \varphi_-}{2}, \qquad \varphi_a = \varphi_+ - \varphi_-$$

The rotation matrix $R$ with rows indexed by $(r, a)$ and columns by $(+, -)$:

$$R = \begin{pmatrix} 1/2 & 1/2 \\ 1 & -1 \end{pmatrix}, \qquad \det(R) = -1$$

The $a$-row $[1, -1]$ is the discrete alternating sum. This is the key to CTP causality.

**CTP causality constraint** ($V_{aaa} = 0$): For any physical loop contribution to
the effective action in the Schwinger–Keldysh formalism, the all-quantum component
of the effective vertex must vanish:

$$V_{aaa} = \sum_{i,j,k \in \{+,-\}} (-1)^{i+j+k} I[i,j,k] = 0$$

This follows from the CTP normalization $Z[J_+, J_+] = 1$ (the closed time path
returns to the initial state). It holds to all orders in perturbation theory.

---

## 2. Three-Point Loop Topologies

For a triangle diagram with three scalar propagators on $S^4$, the eight CTP index
combinations $I[i, j, k]$ with $i, j, k \in \{+, -\}$ determine the branch structure.

### Topology SYM: Euclidean $S^4$ (all propagators equal)

$$I[i,j,k] = 1 \text{ for all } (i,j,k)$$

| r/a component | Value |
|---|---|
| $V_{rrr}$ | 1.000 |
| all others | 0 |

**CTP causality**: $V_{aaa} = 1-1-1-1+1+1+1-1 = 0$ ✓ **PASSES**

**Physical meaning**: On compact Euclidean $S^4$, the scalar propagator has a real
discrete spectrum (eigenvalues $\lambda_l = l(l+3)$, $l = 0, 1, 2, \ldots$).
This means:

$$G^{++} = G^{--} = G^{+-} = G^{-+} = G_E$$

All four CTP components are equal to the Euclidean Green function. The loop
integral is **identical on both branches**. Result: pure noise kernel ($V_{rrr}$
only), no response component.

**Role implication**: `shared_normalization` — loop appears identically in $N$ and
$D$, so it cancels in $R = N/D$.

---

### Topology ANTISYM: Branch sign flip

$$I[+,+,+] = +1, \quad I[-,-,-] = -1, \quad \text{rest} = 0$$

| r/a component | Value |
|---|---|
| $V_{rra} = V_{rar} = V_{arr}$ | 0.500 |
| $V_{aaa}$ | **2.000** |

**CTP causality**: $V_{aaa} = 2 \neq 0$ ✗ **FAILS**

The antisymmetric topology violates CTP causality. This branch structure is not
allowed by the Schwinger–Keldysh effective action at any loop order.

---

### Topology RESP1: One-response (one backward vertex)

$$I[+,+,-] = I[+,-,+] = I[-,+,+] = 1, \quad \text{rest} = 0$$

| r/a component | Value |
|---|---|
| $V_{rrr}$ | 0.375 |
| $V_{rra} = V_{rar} = V_{arr}$ | 0.250 |
| $V_{raa} = V_{ara} = V_{aar}$ | −0.500 |
| $V_{aaa}$ | **−3.000** |

**CTP causality**: $V_{aaa} = -3 \neq 0$ ✗ **FAILS**

The one-response topology also violates CTP causality. Simple cross-branch
propagator insertions are not consistent with the Schwinger–Keldysh constraint.

---

### Result: Only SYM passes CTP causality

| Topology | $V_{aaa}$ | CTP causality | Role implication |
|---|---|---|---|
| SYM (Euclidean $S^4$) | 0 | **PASS** | `shared_normalization` |
| ANTISYM (branch sign flip) | 2 | FAIL | – |
| RESP1 (one backward vertex) | −3 | FAIL | – |
| Sector-asymmetric | 0.21 | FAIL | – |

**The SYM topology is the only three-point loop topology consistent with CTP
causality for a compact Euclidean background.**

---

## 3. Euclidean $S^4$ Propagator Equality

The result is rigorous: on compact Euclidean $S^4$, the scalar propagator
$G_{h_-}(u) = {}_2F_1(D-1, h_-; D/2; u)$ has eigenvalues

$$\lambda_l = l(l+3), \qquad d_l = \frac{(2l+3)(l+1)(l+2)}{6}$$

for $l = 0, 1, 2, \ldots$ These are **real** and **discrete**, with no Lorentzian
time ordering. Therefore:

$$G^{++} = G^{--} = G^{+-} = G^{-+} = G_E \qquad \text{(all four CTP components)}$$

The three-point loop integral satisfies $I^{ijk}(h_-, \varepsilon) = I(h_-, \varepsilon)$
for all $(i,j,k)$. This is the SYM topology. The loop is **identically present on
both CTP branches**.

**Corollary**: On pure Euclidean $S^4$, $\pi/2$ is a **shared normalization** that
cancels in $R = N/D$.

---

## 4. Two Scenarios for $R = \sqrt{4/3}$

Since the Euclidean $S^4$ analysis supports $\pi/2$ as a shared normalization,
two distinct scenarios can produce $R = \sqrt{4/3}$:

---

### Scenario A — $\pi/2$ cancels (shared normalization)

$$R = \frac{C_{\rm Euler, cosmo} \cdot \pi/2}{C_{\rm Euler, final} \cdot \pi/2}
= \frac{C_{\rm Euler, cosmo}}{C_{\rm Euler, final}} = \sqrt{\frac{4}{3}}$$

The $\pi/2$ loop normalization is **common to both sectors**. The physics of $R$
comes from the **ratio of sector-specific Euler couplings**, not from $\pi/2$ itself.

| Quantity | Status |
|---|---|
| $\pi/2$ role | `shared_normalization` |
| $R$ origin | $C_{\rm Euler,cosmo} / C_{\rm Euler,final}$ |
| CTP consistency | Yes — SYM topology, $V_{aaa} = 0$ |
| Supported by Euclidean $S^4$ argument | Yes |

---

### Scenario B — $\pi/2$ is quotient-bearing

$$R = \frac{\pi/2}{\pi\sqrt{3}/4} = \frac{2}{\sqrt{3}} = \sqrt{\frac{4}{3}}$$

The $N$ sector uses the $S^4$ scalar loop with normalization $\pi/2$; the $D$ sector
uses a different loop (or different coupling) with normalization $\pi\sqrt{3}/4$. The
asymmetry between $N$ and $D$ is a **sector-level** difference, not a CTP branch-level
difference.

| Quantity | Status |
|---|---|
| $\pi/2$ role | `final_coefficient_candidate` (in $N$) or `cosmo_coefficient_candidate` (in $D$) |
| $R$ origin | $(pi/2) / (\pi\sqrt{3}/4)$ |
| CTP consistency | Only if sector asymmetry mechanism identified |
| Supported by Euclidean $S^4$ argument | No — requires additional structure |

---

### Current assessment

| Criterion | Scenario A | Scenario B |
|---|---|---|
| CTP causality on pure $S^4$ | ✓ SYM topology | ✗ Requires sector asymmetry |
| Euclidean $S^4$ propagator equality | ✓ All components equal | ✗ Requires Lorentzian or sector structure |
| Geometric ladder connection | ✓ Consistent | ✓ Consistent (projection factor $\pi\sqrt{3}/4$) |
| Blocked by theory input | Yes — need sector decomposition | Yes — need CTP action structure |

**Supported scenario**: A ($\pi/2$ cancels; $R$ from sector prefactor ratio).
**Not excluded**: B ($\pi/2$ quotient-bearing with sector-level asymmetry mechanism).

---

## 5. Decision Table

| Finding | CTP causality | Role |
|---|---|---|
| Loop appears identically on both branches (SYM) | PASSES | `shared_normalization` |
| Loop appears only on one branch (RESP) | FAILS for simple topologies | `final_coefficient_candidate` or `cosmo_coefficient_candidate` — only with Lorentzian structure |
| Loop in both branches with unequal weights | Unchecked — needs sector decomposition | `branch_normalization_candidate` |
| Loop absent from CTP action | N/A | `benchmark_seed` |
| Branch placement undetermined | Unknown | `role_unassigned` |

**Current state**: R1 = NEEDS_THEORY; all topologies evaluated; SYM is CTP-consistent.
Role remains `role_unassigned` until the GRUT sector decomposition is identified.

---

## 6. The Sharpened Blocking Question

The vertex provenance audit established:

> Which CTP vertex produces $I(h_-, \varepsilon)$?

The CTP branch-incidence audit sharpens this to:

> Does the GRUT CTP action assign **equal** $S^4$ scalar loop coefficients to both
> the cosmological ($N$) sector and the gravitational ($D$) sector, or does it assign
> **different** sector-specific couplings?

| Answer | Consequence |
|---|---|
| Equal coefficients (Scenario A) | $\pi/2$ is `shared_normalization`; $R = C_{\rm cosmo}/C_{\rm final}$ |
| Different coefficients (Scenario B) | $\pi/2$ is quotient-bearing; projection factor $\pi\sqrt{3}/4$ required |
| $S^4$ loop absent from CTP action | $\pi/2$ is `benchmark_seed` |

---

## 7. What Would Resolve the Branch-Incidence Question

| Action | Result |
|---|---|
| Write down the GRUT CTP action and identify which term generates the $S^4$ scalar three-point loop | R1 → resolved |
| Identify whether that term appears in the cosmological sector, gravitational sector, or both | R2 → resolved |
| Check whether the sector-specific coupling is the same or different | distinguishes Scenario A from B |
| Verify $V_{aaa} = 0$ for the identified term using the GRUT action Feynman rules | CTP causality confirmed |
| Compute $R$ explicitly with the identified coupling | confirms or refutes $R = \sqrt{4/3}$ |

---

## 8. Files

| File | Contents |
|---|---|
| `grut/hard_theory/s4_ctp_solver/gate3_ctp_branch_incidence.py` | This harness |
| `theory/hard_theory/GATE3_CTP_BRANCH_INCIDENCE_AUDIT.md` | This spec |
| `theory/hard_theory/gate3_dl_outputs/gate3_ctp_branch_incidence.json` | Execution output |
| `grut/hard_theory/s4_ctp_solver/gate3_vertex_provenance_audit.py` | Upstream audit (V1–V5 scoring) |
| `theory/hard_theory/GATE3_VERTEX_PROVENANCE_AUDIT.md` | Upstream spec (geometric ladder) |
| `grut/hard_theory/s4_ctp_solver/gate3_coefficient_role_assignment.py` | Role assignment gate |
| `theory/hard_theory/GATE3_COEFFICIENT_ROLE_ASSIGNMENT.md` | Role taxonomy (R1–R6 criteria) |

---

## Spec ID

`gate3-ctp-branch-incidence-spec-v1.0`
Frozen: 2026-05-26
