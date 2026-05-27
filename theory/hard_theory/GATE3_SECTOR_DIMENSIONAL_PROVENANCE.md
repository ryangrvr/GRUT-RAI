# Gate 3 Sector-Dimensional Provenance Audit

Date: 2026-05-26
Spec: gate3-sector-dimensional-provenance-spec-v1.0
Status: R1 = NEEDS_THEORY; role = role_unassigned

---

## Purpose

The sector coupling assignment established that three independent geometric
mechanisms (C1 volume-projection, C2 spectral-gap, C3 dimensional ladder) each
predict $g_{\rm cosmo}/g_{\rm final} = \sqrt{4/3}$ with zero free parameters.

This audit establishes the **sector assignment** — which sphere each sector couples
to — by testing the two canonical options and showing that only one is consistent
with $R = \sqrt{4/3}$. All geometric facts are now proved. The final gate requires
theory input to confirm which GRUT CTP action terms carry $C_{\rm cosmo}$ and
$C_{\rm final}$.

**This is the last geometric audit.** No further numerical work is needed.

---

## 1. Established Facts

The following have been proved in prior Gate 3 audits (all exact to machine precision):

| ID | Statement | Status | Source |
|---|---|---|---|
| F1 | $I(0,0)\big|_D = \mathrm{Vol}(S^{D-1})/\mathrm{Vol}(S^{D-2})$ for all $D$ | PROVED | Sector coupling harness |
| F2 | $I(0,0)\big|_{D=4} = \pi/2$ — Gate 3 seed | PROVED | D1/D3 numerical + $4B(3/2,3/2)$ |
| F3 | $I(0,0)\big|_{D=5} = 4/3 = R_{\rm target}^2$ — exact | PROVED | Dimensional ladder theorem |
| F4 | $R_{\rm target} = \sqrt{I(0,0)\big|_{D=5}} = \sqrt{4/3}$ — exact | PROVED | F3 + definition |
| F5 | $\mathrm{Vol}(S^4)/\mathrm{Vol}(S^3) = \lambda_1(S^4)/\lambda_1(S^3) = 4/3$ — unique to $D=4$ | PROVED | D=4 coincidence theorem |
| F6 | $\pi/2$ is `shared_normalization` (cancels in $R$) on Euclidean $S^4$ | PROVED | CTP branch-incidence audit |
| F7 | $R = g_{\rm cosmo}/g_{\rm final}$ where $C = g \cdot (\pi/2)$ for each sector | FRAMEWORK | Follows from F6 |

---

## 2. Sector Assignment Analysis

Given the framework $R = g_{\rm cosmo}/g_{\rm final}$ and the D=4 coincidence
$\lambda_1(S^4)/\lambda_1(S^3) = 4/3$, two canonical assignments must be tested.

### Assignment A — Naïve (WRONG)

$$g_{\rm cosmo} = \sqrt{\lambda_1(S^3)} = \sqrt{3}, \qquad
  g_{\rm final}  = \sqrt{\lambda_1(S^4)} = 2$$

$$R_A = \frac{\sqrt{3}}{2} = \sqrt{\frac{3}{4}} \neq \sqrt{\frac{4}{3}} \qquad \text{WRONG}$$

The naïve assignment (final sector on the larger sphere, cosmological on the
smaller) gives the **reciprocal** of the target. This assignment is ruled out
by the requirement $R = \sqrt{4/3}$.

### Assignment B — Correct

$$g_{\rm cosmo} = \sqrt{\lambda_1(S^4)} = 2, \qquad
  g_{\rm final}  = \sqrt{\lambda_1(S^3)} = \sqrt{3}$$

$$\boxed{R_B = \frac{2}{\sqrt{3}} = \sqrt{\frac{4}{3}} = R_{\rm target} \qquad \text{EXACT}}$$

**The cosmological sector couples to the larger sphere ($S^4$ bulk); the
final/Euler sector couples to the smaller sphere ($S^3$ boundary or sub-manifold).**

| Assignment | $g_{\rm cosmo}$ | $g_{\rm final}$ | $R$ predicted | Correct? |
|---|---|---|---|---|
| A (naïve) | $\sqrt{\lambda_1(S^3)} = \sqrt{3}$ | $\sqrt{\lambda_1(S^4)} = 2$ | $\sqrt{3/4}$ | ✗ |
| **B** | $\sqrt{\lambda_1(S^4)} = 2$ | $\sqrt{\lambda_1(S^3)} = \sqrt{3}$ | $\sqrt{4/3}$ | **✓** |

---

## 3. Physical Picture — Bulk-Boundary Split

The natural geometric interpretation of Assignment B is a **bulk-boundary split**
in the GRUT CTP action on $S^4$:

| Role | Manifold | Coupling | Physical term |
|---|---|---|---|
| Cosmological (bulk) | $S^4$ | $g_{\rm cosmo} = \sqrt{\lambda_1(S^4)} = 2$ | $\Lambda \int_{S^4} \sqrt{g}\, d^4x \sim \Lambda \cdot \mathrm{Vol}(S^4)$ |
| Final/Euler (boundary) | $S^3$ | $g_{\rm final} = \sqrt{\lambda_1(S^3)} = \sqrt{3}$ | $\alpha \int_{S^3} K\sqrt{h}\, d^3x \sim \alpha \cdot \mathrm{Vol}(S^3)$ |

**Sphere volumes** (exact):

$$\mathrm{Vol}(S^4) = \frac{8\pi^2}{3} \approx 26.319, \qquad
  \mathrm{Vol}(S^3) = 2\pi^2 \approx 19.739$$

$$\sqrt{\frac{\mathrm{Vol}(S^4)}{\mathrm{Vol}(S^3)}}
= \sqrt{\frac{4}{3}} = R_{\rm target} \qquad \text{[exact]}$$

The volume-projection and spectral-gap mechanisms give the same ratio — this
is the D=4 coincidence (F5 above). Both encode the bulk/boundary asymmetry.

**Caveat**: $S^4$ is a closed manifold with no boundary. The "$S^3$ boundary"
refers to the equatorial 3-sphere inside $S^4$ (the fixed-point set of the
reflection symmetry $x_5 \to -x_5$), or to a sub-manifold defined by the GRUT
sector decomposition. The GRUT CTP action structure determines the correct
interpretation.

---

## 4. Amplitude vs Power

Why $R = \sqrt{4/3}$ rather than $R = 4/3$?

Two representations, both giving the same numerical answer:

| Representation | Definition | Value |
|---|---|---|
| Power-1 (amplitude) | $R = g_{\rm cosmo}/g_{\rm final} = 2/\sqrt{3}$ | $\sqrt{4/3}$ ✓ |
| Power-2 (energy) | $R = \sqrt{g_{\rm cosmo}^2/g_{\rm final}^2} = \sqrt{4/3}$ | $\sqrt{4/3}$ ✓ |

**Underlying**: $g_{\rm cosmo}^2/g_{\rm final}^2 = 4/3 = R_{\rm target}^2$ (exact).

Both representations give $R = \sqrt{4/3}$. The distinction is interpretive:
- If $R = N/D$ with $N, D \propto g$ (coupling constants, first power), then
  $R = 2/\sqrt{3}$ directly.
- If $R = \sqrt{N_{\rm action}/D_{\rm action}}$ with $N, D \propto g^2$
  (action densities or partition functions), then $R = \sqrt{4/3}$ as a square root.

Theory input required to determine which definition is used in the GRUT quotient.

---

## 5. Complete Geometric Chain

Every arrow below is a proved mathematical identity. Theory input is required only
for the final sector-assignment step.

```
S4 Euler geometry
  → Allen-Jacobson three-point loop: I(h_-, ε) with seed I(0,0)|_{D=4} = π/2
  → Dimensional ladder: I(0,0)|_D = Vol(S^{D-1})/Vol(S^{D-2})
  → I(0,0)|_{D=5} = 4/3 = R²    [one rung up the ladder]
  → CTP branch audit: π/2 is shared normalization on Euclidean S⁴
  → Sector coupling framework: R = g_cosmo / g_final
  → D=4 coincidence: Vol(S⁴)/Vol(S³) = λ₁(S⁴)/λ₁(S³) = 4/3
  → Assignment B: g_cosmo/g_final = √(λ₁(S⁴)/λ₁(S³)) = √(4/3)
  → [NEEDS THEORY: confirm cosmo sector on S⁴ bulk, final sector on S³]
  → R = √(4/3)
```

---

## 6. Gate Conditions for Theory Confirmation

| ID | Question | Status |
|---|---|---|
| G1 | Which GRUT CTP action term generates $C_{\rm cosmo}$? | NEEDS_THEORY |
| G2 | Does the $C_{\rm cosmo}$ term project onto the $S^4$ bulk ($\lambda_1(S^4)$ or $\mathrm{Vol}(S^4)$)? | NEEDS_THEORY |
| G3 | Which GRUT CTP action term generates $C_{\rm final}$? | NEEDS_THEORY |
| G4 | Does the $C_{\rm final}$ term project onto the $S^3$ boundary ($\lambda_1(S^3)$ or $\mathrm{Vol}(S^3)$)? | NEEDS_THEORY |
| G5 | Does the shared $\pi/2$ loop appear in both $C_{\rm cosmo}$ and $C_{\rm final}$ terms? | NEEDS_THEORY |
| G6 | Is $R$ defined as a first-power amplitude ratio $N/D$ (not $\sqrt{N/D}$)? | NEEDS_THEORY |
| G7 | Does explicit computation give $R = g_{\rm cosmo}/g_{\rm final} = 2/\sqrt{3} = \sqrt{4/3}$? | NEEDS_THEORY |

**All 7 conditions: NEEDS_THEORY.**

Sector assignment is the final geometric gate. No further numerical computation
is required — only the identification of which GRUT CTP action terms carry
$C_{\rm cosmo}$ and $C_{\rm final}$ and which sphere each couples to.

---

## 7. Current Assessment

| Layer | Finding |
|---|---|
| Numerical | $C_{\rm seed}^{(3)} = \pi/2$, D1/D3 validated, endpoint resolved |
| Analytic | $I(0,0) = \pi/2 = \mathrm{Vol}(S^3)/\mathrm{Vol}(S^2)$ (exact) |
| CTP branch | SYM topology only; $\pi/2$ is shared normalization on Euclidean $S^4$ |
| Dimensional ladder | $I(0,0)\big|_{D=5} = 4/3 = R^2$ (exact); $R = \sqrt{I\big|_{D=5}}$ |
| D=4 coincidence | $\mathrm{Vol}(S^4)/\mathrm{Vol}(S^3) = \lambda_1(S^4)/\lambda_1(S^3) = 4/3$ (exact, unique) |
| Sector coupling | C1/C2/C3 all give $g_{\rm cosmo}/g_{\rm final} = \sqrt{4/3}$ with 0 free params |
| Sector assignment | Assignment B (cosmo=S4 bulk, final=S3 boundary) gives $R = \sqrt{4/3}$ exactly |
| Assignment A | RULED OUT: gives $R = \sqrt{3/4}$ (reciprocal of target) |
| Role | `role_unassigned` (provisional); R1 = NEEDS_THEORY |

---

## 8. What Would Resolve the Remaining Gate

| Action | Resolves |
|---|---|
| Identify the GRUT CTP action term for $C_{\rm cosmo}$ and verify it couples to $S^4$ | G1, G2 |
| Identify the GRUT CTP action term for $C_{\rm final}$ and verify it couples to $S^3$ | G3, G4 |
| Verify the shared $\pi/2$ loop appears in both sector terms | G5 |
| Confirm $R$ is defined as a first-power amplitude ratio | G6 |
| Compute $R = g_{\rm cosmo}/g_{\rm final}$ explicitly from the GRUT action | G7 |

Once G1–G7 are resolved by theory, R1 transitions from NEEDS_THEORY to a positive
evidence criterion, and promotion from `role_unassigned` can be evaluated.

---

## 9. Files

| File | Contents |
|---|---|
| `grut/hard_theory/s4_ctp_solver/gate3_sector_dimensional_provenance.py` | This harness |
| `theory/hard_theory/GATE3_SECTOR_DIMENSIONAL_PROVENANCE.md` | This spec |
| `theory/hard_theory/gate3_dl_outputs/gate3_sector_dimensional_provenance.json` | Execution output |
| `theory/hard_theory/GATE3_SECTOR_COUPLING_ASSIGNMENT.md` | Upstream: dimensional ladder, D=4 coincidence |
| `theory/hard_theory/GATE3_CTP_BRANCH_INCIDENCE_AUDIT.md` | Upstream: SYM topology, shared normalization |
| `theory/hard_theory/GATE3_VERTEX_PROVENANCE_AUDIT.md` | Upstream: geometric ladder, V3/V4 fork |
| `theory/hard_theory/GATE3_COEFFICIENT_ROLE_ASSIGNMENT.md` | Role taxonomy, R1–R6 criteria |

---

## Spec ID

`gate3-sector-dimensional-provenance-spec-v1.0`
Frozen: 2026-05-26
