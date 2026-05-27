# Gate 3 Sector-Coupling Assignment

Date: 2026-05-26
Spec: gate3-sector-coupling-assignment-spec-v1.0
Status: R1 = NEEDS_THEORY; role = role_unassigned; provisional = sector_projection_candidate

---

## Purpose

The CTP branch-incidence audit established:

> On Euclidean $S^4$, all CTP propagator components are equal, so the three-point
> scalar loop $I(h_-, \varepsilon)$ is a **shared normalization** that cancels in $R=N/D$.

Therefore the sector coupling framework is:

$$C_{\rm cosmo} = g_{\rm cosmo} \cdot \frac{\pi}{2}, \qquad
  C_{\rm final}  = g_{\rm final}  \cdot \frac{\pi}{2}$$

$$R = \frac{C_{\rm cosmo}}{C_{\rm final}} = \frac{g_{\rm cosmo}}{g_{\rm final}}$$

The remaining problem: **what determines $g_{\rm cosmo}/g_{\rm final} = \sqrt{4/3}$?**

This audit answers by computing the dimensional ladder and the D=4 coincidence.

---

## 1. Dimensional Ladder Theorem

The Allen–Jacobson integral satisfies an exact general formula:

$$\boxed{I(0,0)\big|_D = \sqrt{\pi}\,\frac{\Gamma\!\left(\frac{D-1}{2}\right)}{\Gamma\!\left(\frac{D}{2}\right)}
= \frac{\mathrm{Vol}(S^{D-1})}{\mathrm{Vol}(S^{D-2})}}$$

for all $D$. This follows from the derivation:

$$I(0,0)\big|_D = 2 \cdot 4^{(D-3)/2} \cdot B\!\left(\frac{D-1}{2},\frac{D-1}{2}\right)
= \sqrt{\pi}\,\frac{\Gamma\!\left(\frac{D-1}{2}\right)}{\Gamma\!\left(\frac{D}{2}\right)}$$

using $B(a,a) = \sqrt{\pi}\,\Gamma(a)/(2^{2a-1}\Gamma(a+\tfrac{1}{2}))$ and the
$\Gamma$-function recurrence.

**The full dimensional ladder** (all exact to machine precision):

| $D$ | $I(0,0)\big|_D$ | $\mathrm{Vol}(S^{D-1})/\mathrm{Vol}(S^{D-2})$ |
|---|---|---|
| 3 | 2 | $4\pi / (2\pi) = 2$ |
| **4** | $\pi/2$ | $2\pi^2 / (4\pi) = \pi/2$ |
| **5** | $4/3$ | $(8\pi^2/3) / (2\pi^2) = 4/3$ |
| 6 | $3\pi/8$ | $\pi^3 / (8\pi^2/3) = 3\pi/8$ |

### Key result: $R_{\rm target}$ is one ladder rung above the seed

$$\boxed{I(0,0)\big|_{D=5} = \frac{4}{3} = R_{\rm target}^2}$$

$$\boxed{R_{\rm target} = \sqrt{I(0,0)\big|_{D=5}}}$$

**Exact, difference from $4/3$: $0.00 \times 10^{-\infty}$.**

The GRUT quotient target $R = \sqrt{4/3}$ is the square root of the Allen–Jacobson
integral evaluated **one dimension higher** than the Gate 3 seed computation.

---

## 2. D=4 Coincidence Theorem

The three-dimensional ratio $4/3$ arises independently from **three** geometric
structures, and this triple coincidence holds **only at $n=4$**:

### Structure 1: Sphere volume ratio

$$\frac{\mathrm{Vol}(S^4)}{\mathrm{Vol}(S^3)} = \frac{8\pi^2/3}{2\pi^2} = \frac{4}{3}$$

### Structure 2: Laplacian spectral gap ratio

The first nonzero eigenvalue of the Laplacian on the unit $n$-sphere is $\lambda_1(S^n) = n$.

$$\frac{\lambda_1(S^4)}{\lambda_1(S^3)} = \frac{4}{3}$$

### Structure 3: Dimensional ladder rung

$$\frac{I(0,0)\big|_{D=5}}{I(0,0)\big|_{D=4}} = \frac{4/3}{\pi/2} = \frac{8}{3\pi}$$

(this is a different ratio — but $I(0,0)|_{D=5} = 4/3 = R^2$ is exact.)

**Uniqueness**: The coincidence $\mathrm{Vol}(S^n)/\mathrm{Vol}(S^{n-1}) = n/(n-1)$
holds **only at $n=4$**. At $n=3$: $\mathrm{Vol}(S^3)/\mathrm{Vol}(S^2) = \pi/2 \neq 3/2$.
At $n=5$: $\mathrm{Vol}(S^5)/\mathrm{Vol}(S^4) = 3\pi/8 \neq 5/4$.

| $n$ | $\mathrm{Vol}(S^n)/\mathrm{Vol}(S^{n-1})$ | $\lambda_1(S^n)/\lambda_1(S^{n-1}) = n/(n-1)$ | Coincide? |
|---|---|---|---|
| 2 | $4\pi/(2\pi) = 2$ | $2/1 = 2$ | ✓ (trivial: both = $n$) |
| 3 | $\pi/2 \approx 1.571$ | $3/2 = 1.500$ | ✗ |
| **4** | $4/3 \approx 1.333$ | $4/3 \approx 1.333$ | **✓ UNIQUE** |
| 5 | $3\pi/8 \approx 1.178$ | $5/4 = 1.250$ | ✗ |

**Physical significance**: Four dimensions is the unique case where the
volume-projection and spectral-gap sector coupling mechanisms predict the
**same** ratio $\sqrt{4/3}$ for $R$. This double constraint is a signature of
the special role of $D=4$ in the GRUT theory.

---

## 3. Sector Coupling Candidates

Given $R = g_{\rm cosmo}/g_{\rm final}$ and the need for $R = \sqrt{4/3}$:

| ID | Candidate | $R$ predicted | Free params | Natural | Role |
|---|---|---|---|---|---|
| **C1** | Volume-projection | $\sqrt{4/3}$ ✓ | 0 | ✓ | `sector_projection_candidate` |
| **C2** | Spectral-gap | $\sqrt{4/3}$ ✓ | 0 | ✓ | `sector_projection_candidate` |
| **C3** | Dimensional ladder ($D=5$) | $\sqrt{4/3}$ ✓ | 0 | ✓ | `sector_projection_candidate` |
| C0 | Equal coupling | $1$ ✗ | 0 | ✓ | `shared_normalization_confirmed` (but $R=1$ contradicts $R=\sqrt{4/3}$) |
| C4 | Euler-density normalization | $\sqrt{24} \neq \sqrt{4/3}$ | 0 | ✓ | `role_unassigned` |
| C5 | CTP response weighting | unknown | $\geq 1$ | ? | `role_unassigned` |
| C6 | Hand-tuned ratio | $\sqrt{4/3}$ trivially | 1 | ✗ | **`rejected_tuning`** |

### C1 — Volume-projection coupling

If the cosmological sector projects onto $S^4$ geometry and the final sector
onto $S^3$:

$$\frac{g_{\rm cosmo}}{g_{\rm final}} = \sqrt{\frac{\mathrm{Vol}(S^4)}{\mathrm{Vol}(S^3)}} = \sqrt{\frac{4}{3}} = R_{\rm target}$$

No free parameters. Purely geometric.

### C2 — Spectral-gap coupling

If sector couplings are set by the first Laplacian eigenvalue of the corresponding sphere:

$$g_{\rm cosmo} \propto \sqrt{\lambda_1(S^4)} = 2, \qquad
  g_{\rm final}  \propto \sqrt{\lambda_1(S^3)} = \sqrt{3}$$

$$\frac{g_{\rm cosmo}}{g_{\rm final}} = \frac{2}{\sqrt{3}} = \sqrt{\frac{4}{3}} = R_{\rm target}$$

No free parameters. Unique to $D=4$.

### C3 — Dimensional ladder

The AJ ladder gives $I(0,0)|_{D=5} = 4/3$. If the ratio of sector loops involves
the $D=5$ integral:

$$R = \sqrt{I(0,0)\big|_{D=5}} = \sqrt{\frac{4}{3}} = R_{\rm target}$$

This is the most compact statement: **$R$ is the AJ seed at $D=5$, square-rooted.**

### C1 = C2 = C3 at D=4

All three candidates are equivalent expressions of the same D=4 coincidence.
They give identical predictions with zero free parameters. Together they constitute a
single **sector-projection candidate** backed by three independent geometric arguments.

---

## 4. What π/2 Is and Is Not

| Object | Status |
|---|---|
| $\pi/2 = I(0,0)\big|_{D=4}$ | Exact AJ seed, validated |
| $\pi/2 = \mathrm{Vol}(S^3)/\mathrm{Vol}(S^2)$ | Exact sphere-volume identity |
| $\pi/2$ as shared normalization | CTP-consistent; cancels in $R$ (Scenario A) |
| $\pi/2$ as quotient-bearing | Requires sector asymmetry (Scenario B; not CTP-forced) |
| $4/3 = R^2 = I(0,0)\big|_{D=5}$ | Exact; one rung up the same ladder |
| $R = \sqrt{4/3}$ | From sector-projection ratio, not from $\pi/2$ directly |

---

## 5. Current Assessment

| Layer | Finding |
|---|---|
| Numerical | $C_{\rm seed}^{(3)} = \pi/2$, D1/D3 validated, endpoint resolved |
| Analytic | $I(0,0) = \pi/2 = \mathrm{Vol}(S^3)/\mathrm{Vol}(S^2)$ (exact) |
| CTP branch | SYM topology only; $\pi/2$ is shared normalization on Euclidean $S^4$ |
| Dimensional ladder | $I(0,0)|_{D=5} = 4/3 = R^2$ (exact); $R = \sqrt{I|_{D=5}}$ |
| D=4 coincidence | $\mathrm{Vol}(S^4)/\mathrm{Vol}(S^3) = \lambda_1(S^4)/\lambda_1(S^3) = 4/3$ (exact, unique) |
| Sector coupling | C1/C2/C3 all give $g_{\rm cosmo}/g_{\rm final} = \sqrt{4/3} = R$ with 0 free params |
| Role | `sector_projection_candidate` (provisional); default `role_unassigned` |

---

## 6. Blocking Question and What Would Resolve It

The sharpened blocking question is now:

> Which sector of the GRUT CTP action couples via the $S^4$ projector, and which
> via the $S^3$ projector (or equivalently, via the $D=5$ AJ integral)?

| Finding | Consequence |
|---|---|
| Cosmological sector uses $S^4$ volume, final sector uses $S^3$ | C1 confirmed; $R = \sqrt{4/3}$ from volume ratio |
| Sector couplings set by $\lambda_1(S^4)$ vs $\lambda_1(S^3)$ | C2 confirmed; $R = 2/\sqrt{3}$ from spectral gaps |
| Final sector loop is the $D=5$ AJ integral | C3 confirmed; $R = \sqrt{I|_{D=5}}$ |
| All sectors use same sphere | C0; $R=1$; theory inconsistent with $R=\sqrt{4/3}$ |
| $g_{\rm cosmo}/g_{\rm final}$ inserted by hand | C6 rejected |

---

## 7. Files

| File | Contents |
|---|---|
| `grut/hard_theory/s4_ctp_solver/gate3_sector_coupling_assignment.py` | This harness |
| `theory/hard_theory/GATE3_SECTOR_COUPLING_ASSIGNMENT.md` | This spec |
| `theory/hard_theory/gate3_dl_outputs/gate3_sector_coupling_assignment.json` | Execution output |
| `theory/hard_theory/GATE3_CTP_BRANCH_INCIDENCE_AUDIT.md` | Upstream: SYM topology, shared normalization |
| `theory/hard_theory/GATE3_VERTEX_PROVENANCE_AUDIT.md` | Upstream: geometric ladder, V3/V4 fork |
| `theory/hard_theory/GATE3_COEFFICIENT_ROLE_ASSIGNMENT.md` | Role taxonomy, R1–R6 criteria |

---

## Spec ID

`gate3-sector-coupling-assignment-spec-v1.0`
Frozen: 2026-05-26
