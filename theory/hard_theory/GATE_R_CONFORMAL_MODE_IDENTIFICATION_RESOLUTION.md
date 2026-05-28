# Gate R: Conformal Mode Identification — C4 and C5 Resolution

Date: 2026-05-27
Spec: gate-r-conformal-mode-identification-resolution-v1.0
Resolves: C4 (NEEDS_THEORY → SUPPORTED), C5 (TENSION → RESOLVED)
Upstream: `GATE_R_CONFORMAL_MODE_IDENTIFICATION.md`

---

## Purpose

The conformal mode identification gate left two criteria open:

- **C4** (NEEDS_THEORY): Fermion/gauge alternatives excluded on spin/statistics
  grounds, not by R-matching
- **C5** (TENSION): How does a scalar anomaly coefficient $\alpha_{\rm vac}$
  enter a kernel $K^R = \alpha_{\rm vac}\,\chi(\omega)\,P^{TT}$ that projects
  onto transverse-tracefree modes?

This document closes both in the forward direction:
physics → identification → $\alpha_{\rm vac} = 1/3$ → $R = \sqrt{4/3}$.

**Neither argument uses $R = \sqrt{4/3}$ as input.**

---

## 1. C4 — Spin/Statistics Exclusion (Forward Direction)

### The mode

The GRUT vacuum conformal response is encoded in the gravitational conformal
factor $\sigma$, defined by the Weyl decomposition of the metric:

$$g_{\mu\nu} = e^{2\sigma}\,\hat{g}_{\mu\nu}$$

where $\hat{g}_{\mu\nu}$ is a reference metric (Fubini–Study metric on $S^4$)
and $\sigma$ is a real scalar function on the manifold.

**$\sigma$ is a real scalar by construction.** It is a single real-valued function.
This is not a choice — it is a consequence of the Weyl decomposition of the
Riemannian metric tensor in four dimensions.

### Why not a Weyl fermion

A Weyl fermion is a spinor-valued field transforming in the $(1/2, 0)$
representation of $\mathrm{Spin}(4)$. The conformal factor $\sigma$ transforms
as a scalar under all diffeomorphisms and local Lorentz transformations:

$$\sigma \longrightarrow \sigma - \omega(x) \quad \text{under } g_{\mu\nu} \to e^{2\omega}g_{\mu\nu}$$

This is the transformation law of a spin-0 field, not a spinor. A Weyl fermion
cannot represent the conformal factor because the conformal factor is a scalar
under the spin group. **Fermionic identification is excluded by representation
theory, not by numerical matching.**

### Why not a gauge field

A gauge field is a Lie-algebra-valued 1-form with gauge redundancy under
$A_\mu \to A_\mu + \partial_\mu\lambda$. The conformal factor $\sigma$ carries
no gauge index, no internal symmetry, and no 1-form index. It has no Yang–Mills
charge and participates in no gauge transformation. **Vector/gauge identification
is excluded by representation content.**

### Summary of C4

| Alternative | Exclusion mechanism | Uses R? |
|---|---|---|
| Weyl fermion | $\sigma$ transforms as spin-0 scalar, not spinor | **No** |
| Gauge field | $\sigma$ carries no gauge index or 1-form structure | **No** |
| Complex scalar | $\sigma$ is a real-valued function; one real DOF | **No** |
| Graviton TT polarizations | $\sigma$ is the trace sector; TT is the complement | **No** |

> **The real conformally coupled scalar is the only admissible effective field
> for the gravitational conformal response channel because $\sigma$ is selected
> by the representation content of the Weyl decomposition, not by numerical
> matching to $R$.**

**C4 status: SUPPORTED.**

---

## 2. C5 — Scalar Anomaly / $P^{TT}$ Compatibility (R5b)

### The apparent tension

The constitutive kernel is:

$$K^R_{\mu\nu\rho\sigma}(\omega) = \alpha_{\rm vac}\,\chi(\omega)\,P^{TT}_{\mu\nu\rho\sigma}$$

- $\alpha_{\rm vac} = a/c = 1/3$ is derived from the trace anomaly of a real
  conformally-coupled scalar — a property of the *scalar sector*
- $P^{TT}_{\mu\nu\rho\sigma}$ is the transverse-tracefree projector, which
  projects *out* the scalar/trace sector of metric perturbations

The question: how can a scalar-sector quantity ($\alpha_{\rm vac}$) appear inside
a tensor kernel that actively removes the scalar sector?

### The resolution: two independent roles in $K^R$

The kernel $K^R$ contains two structurally independent pieces with distinct
physical roles:

| Factor | Type | Role |
|---|---|---|
| $\alpha_{\rm vac}\,\chi(\omega)$ | Scalar | Vacuum response *amplitude*: how strongly the medium responds |
| $P^{TT}_{\mu\nu\rho\sigma}$ | Rank-4 tensor | Response *geometry*: which external perturbations excite the response |

These pieces answer different questions and are not redundant:

- $P^{TT}$ answers: **which external metric perturbation $h_{\mu\nu}$ is a
  physical source?** Answer: only the TT part. Longitudinal and trace modes are
  pure gauge or unphysical on-shell.

- $\alpha_{\rm vac}\,\chi(\omega)$ answers: **given that a physical TT perturbation
  is present, how does the vacuum respond?** The vacuum is characterized by its
  susceptibility, whose normalization comes from the conformal anomaly of the
  mode that carries the vacuum's internal conformal degrees of freedom.

$\alpha_{\rm vac}$ is a property of **the vacuum itself**, not of the
perturbation. $P^{TT}$ is a property of **the perturbation**, not of the vacuum.
They act on different objects.

### The dielectric analogy

In classical electrodynamics, the constitutive relation in a dielectric medium is:

$$\mathbf{D}(\omega) = \varepsilon(\omega)\,\mathbf{E}(\omega)$$

where $\varepsilon(\omega)$ is a **scalar** dielectric constant and $\mathbf{E}$
is a **transverse** electromagnetic wave (in the Coulomb gauge, $\nabla \cdot \mathbf{E} = 0$).

Nobody concludes from this that $\varepsilon$ is a transverse quantity, or that
the transversality of $\mathbf{E}$ contradicts the scalar nature of $\varepsilon$.
The scalar $\varepsilon$ characterizes the medium's response *strength*; the
transversality condition on $\mathbf{E}$ is a constraint on the *source*.

The GRUT constitutive kernel has the same structure:

$$K^R = \underbrace{\alpha_{\rm vac}\,\chi(\omega)}_{\varepsilon(\omega)\text{-analogue}}\;
        \underbrace{P^{TT}}_{\text{transversality constraint}}$$

$\alpha_{\rm vac}$ characterizes the vacuum; $P^{TT}$ constrains the perturbation.
They are not in tension.

### Why $\alpha_{\rm vac}$ carries the conformal scalar anomaly

On the $S^4$ background, the gravitational vacuum has a specific conformal
structure. The mode that carries the internal conformal degrees of freedom of
this vacuum is $\sigma$, the conformal factor. When a TT graviton perturbation
$h_{\mu\nu}^{TT}$ propagates through this vacuum, it encounters a medium whose
susceptibility is determined by the conformal properties of $\sigma$.

The heat kernel expansion for the TT graviton propagator on $S^4$ involves the
Seeley–DeWitt coefficient $a_2$, which depends on curvature invariants of the
background. For a conformally flat $S^4$ background, the dominant contribution
to $a_2$ in the vacuum sector is set by the conformal anomaly of the scalar mode
$\sigma$ — which gives $a/c = 1/3$.

In other words: $P^{TT}$ filters the *input* perturbation; the background $\sigma$
determines the *output* susceptibility. These are independent steps in the
scattering problem.

### Summary of C5

> $\alpha_{\rm vac}$ normalizes the scalar vacuum susceptibility $\chi(\omega)$:
> it quantifies how strongly the $S^4$ conformal vacuum responds to any
> perturbation. $P^{TT}$ projects the external metric perturbation onto the
> physical transverse-tracefree channel: it determines which perturbations are
> admissible sources. These are independent roles. The scalar nature of
> $\alpha_{\rm vac}$ is not in tension with the TT nature of $P^{TT}$, for the
> same reason that a scalar dielectric constant is not in tension with the
> transversality of electromagnetic waves.

**C5 status: RESOLVED (R5b — anomaly as background property).**

---

## Updated Gate Table

| Criterion | Was | Now | Notes |
|---|---|---|---|
| C1 Scalar mode isolated | PARTIAL | PARTIAL | Weyl decomposition established; full path-integral derivation deferred |
| C2 Conformal coupling | PARTIAL | PARTIAL | $\xi_c = 1/6$ by symmetry; Lagrangian derivation deferred |
| C3 One real species | PARTIAL | PARTIAL | GHP instability handling deferred |
| **C4 Fermion/gauge excluded** | NEEDS_THEORY | **SUPPORTED** | Spin-0 / uncharged by representation; non-circular |
| **C5 $P^{TT}$ compatibility** | TENSION | **RESOLVED** | R5b: anomaly = vacuum property; $P^{TT}$ = perturbation filter |
| C6 R-independence | SUPPORTED | SUPPORTED | Route 2 forward direction confirmed |

**Overall gate status: C4 and C5 closed. C1–C3 remain PARTIAL (deferred to full
Weyl decomposition chapter).**

---

## The Forward Chain (Complete)

With C4 and C5 resolved, the R-chain can be written in the forward direction
without circular steps:

```
1. Metric Weyl decomposition: g_μν = e^{2σ} ĝ_μν
   → σ is one real scalar (not spinor, not gauge, not complex)  [C1, C3, C4]

2. σ transforms as a conformally-coupled scalar (ξ_c = 1/6 in 4D)  [C2]

3. From Duff 1994 / KS 2011: (a,c) = (1,3) for real conformally-coupled scalar
   → a/c = 1/3  [PUBLISHED]

4. Identification: conformal mode σ ≡ real conformally-coupled scalar
   → alpha_vac = a/c = 1/3  [C4 exclusion ensures non-circularity]

5. alpha_vac enters as vacuum susceptibility normalization in K^R
   P^TT independently filters which perturbations excite the response  [C5]
   K^R = alpha_vac · chi(omega) · P^TT

6. DC limit: n_g(0)^2 = 1 + alpha_vac = 1 + 1/3 = 4/3

7. R = n_g(0) = sqrt(4/3)  [EXACT]
```

---

## What Remains for Full Book-Readiness

C1–C3 are PARTIAL and need one additional chapter:

| Remaining item | Content |
|---|---|
| Weyl decomposition on $S^4$ | Explicit derivation $g = e^{2\sigma}\hat{g}$; functional measure; single real DOF |
| GHP conformal instability | State how GRUT treats the Gibbons–Hawking–Perry instability of Euclidean $S^4$ |
| Conformal coupling derivation | Show $(\Box - R/6)\sigma = 0$ on $S^4$; confirm $\xi_c = 1/6$ |

These three items are mathematical formalization of what is already implicitly
used in the GRUT framework. They do not introduce new physical assumptions.
C4 and C5 — the conceptually new steps — are now resolved.

---

## Book-Ready Status Sentence

> The canonical GRUT R-chain is closed at the constitutive-action level,
> conditional on the standard identification of the gravitational conformal
> response mode with one real conformally-coupled scalar. This identification
> is supported by: (i) the Weyl decomposition of the metric, which selects
> $\sigma$ as a real scalar by representation theory; (ii) the $P^{TT}$
> compatibility argument, which shows that the scalar anomaly coefficient
> $\alpha_{\rm vac}$ normalizes the vacuum susceptibility independently of the
> TT projector acting on external perturbations. The remaining formalization
> (C1–C3: full Weyl decomposition derivation) does not introduce new physical
> assumptions. The old anomaly-quotient route remains diagnostic/honest-negative;
> the canonical value is refractive/constitutive: $R = \sqrt{4/3}$.

---

## Files

| File | Contents |
|---|---|
| `theory/hard_theory/GATE_R_CONFORMAL_MODE_IDENTIFICATION_RESOLUTION.md` | This document |
| `theory/hard_theory/GATE_R_CONFORMAL_MODE_IDENTIFICATION.md` | Gate spec with six criteria |
| `theory/hard_theory/GATE3_ALPHA_VAC_PROVENANCE.md` | $\alpha_{\rm vac}$ five Q&A |
| `theory/hard_theory/GATE3_CTP_ACTION_TERM_AUDIT.md` | Constitutive kernel structure |

---

## Spec ID

`gate-r-conformal-mode-identification-resolution-v1.0`
Frozen: 2026-05-27
