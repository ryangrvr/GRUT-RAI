# Gate R: Conformal Mode Identification

Date: 2026-05-27
Spec: gate-r-conformal-mode-identification-spec-v1.0
Status: C1 = PARTIAL; C2 = PARTIAL; C3 = PARTIAL; C4 = SUPPORTED; C5 = RESOLVED; C6 = SUPPORTED

---

## Purpose

The alpha_vac provenance audit established that $\alpha_{\rm vac} = 1/3$ follows
from the published trace anomaly ratio $a/c = 1/3$ for a real conformally-coupled
scalar (Duff 1994 / KS 2011), provided one identification holds:

$$\boxed{\text{gravitational conformal mode} \equiv \text{real conformally-coupled scalar}}$$

This is the **last load-bearing step** in the GRUT R-chain. Everything upstream
is either proved or published. This gate determines whether that identification
is justified from first principles, or is a post-hoc assignment chosen to produce
$R = \sqrt{4/3}$.

**The identification must be made before R is calculated.**

---

## The R-Chain Dependency

```
Duff 1994 / KS 2011: a/c = 1/3 for real conformally-coupled scalar
                              ↓
[THIS GATE] conformal mode ≡ real scalar  ←  load-bearing identification
                              ↓
alpha_vac = a/c = 1/3  (exact, convention-independent)
                              ↓
K^R = alpha_vac · chi(omega) · P^TT  (constitutive kernel)
                              ↓
n_g(0)^2 = 1 + alpha_vac = 4/3  (DC limit)
                              ↓
R = sqrt(4/3)  (canonical GRUT R)
```

If this gate fails, $\alpha_{\rm vac} = 1/3$ loses its published anchor. If it
passes, the R-chain is complete from first principles.

---

## Six Criteria

All six must reach PASS before the identification is book-ready.

---

### C1 — Scalar Mode Isolated

**Question**: Is the relevant gravitational vacuum-response mode a scalar, not a
tensor or spinor?

**Required evidence**:
- Show that the Weyl decomposition of the metric in 4D yields a scalar conformal
  factor $\sigma$ as the IR carrier of vacuum response
- Confirm that the GRUT CTP action on $S^4$ couples to $\sigma$ (not the full
  tensor $h_{\mu\nu}$) at the level of the constitutive kernel
- Identify which component of the gravitational path integral measure corresponds
  to $\sigma$

**What we have**:
- `grut/foundation/closure_protocol.py` docstring states: "the gravitational
  conformal mode is identified as the IR carrier of vacuum response" — but this
  is a declaration, not a derivation
- Weyl decomposition $g_{\mu\nu} = e^{2\sigma}\tilde{g}_{\mu\nu}$ makes $\sigma$
  a natural scalar candidate; in 4D this is a single real degree of freedom
- The S⁴ background is conformally flat, which singles out $\sigma$ as the
  dynamically relevant mode in the conformal sector

**Disqualifying findings**:
- If the dominant IR mode is a spin-2 TT graviton rather than a scalar, C1 fails
- If the Weyl decomposition on $S^4$ does not isolate a single scalar mode, C1 fails

**Current status**: PARTIAL — natural from Weyl decomposition, not derived from
the GRUT path integral

---

### C2 — Conformal Coupling Justified

**Question**: Does the scalar mode $\sigma$ couple as a conformally-coupled scalar
(coupling $\xi_c = 1/6$ in 4D), rather than minimally coupled ($\xi = 0$) or
with some other coupling?

**Required evidence**:
- Show that the transformation $\sigma \to \sigma - \omega$ under conformal rescaling
  $g_{\mu\nu} \to e^{2\omega}g_{\mu\nu}$ matches the conformal weight of a
  conformally-coupled scalar
- Confirm that the Weyl anomaly coefficients $(a,c)$ cited by Duff 1994 apply to
  $\xi = \xi_c = (D-2)/[4(D-1)] = 1/6$ in 4D, not to $\xi = 0$

**What we have**:
- Duff 1994 and KS 2011 quote $(a,c)$ for "conformally coupled scalar" — this
  specifies $\xi_c = 1/6$ explicitly in 4D CFT
- The conformal transformation law of $\sigma$ is identical to that of a
  conformally-coupled scalar field under Weyl rescaling
- On $S^4$ (maximally symmetric), the conformally-coupled scalar equation
  $(\Box - R/6)\phi = 0$ reduces to the eigenvalue equation for $\sigma$

**Disqualifying findings**:
- If $\sigma$ has minimal coupling ($\xi = 0$), the relevant $(a,c)$ would differ
  and $a/c \neq 1/3$
- If the GRUT kernel couples to $\sigma$ with an arbitrary $\xi$, the anomaly
  coefficient would be $\xi$-dependent and not pinned to $1/3$

**Current status**: PARTIAL — the coupling type matches by symmetry argument; no
explicit Lagrangian derivation in the GRUT codebase

---

### C3 — One Real Species Justified

**Question**: Is the effective mode count one real scalar, not a complex scalar
(2 DOF), not a vector (4 DOF), not the five graviton TT polarizations?

**Required evidence**:
- Show that the Weyl decomposition on $S^4$ yields exactly one real scalar DOF
  in the conformal sector ($\sigma$ is a single real function)
- Confirm that the functional determinant in the gravitational path integral
  counts $\sigma$ as one real scalar degree of freedom
- Exclude the possibility that the GRUT vacuum response is a sum over multiple
  species or polarizations

**What we have**:
- $\sigma$ in $g_{\mu\nu} = e^{2\sigma}\tilde{g}_{\mu\nu}$ is a single real
  scalar function — one real DOF by construction
- The S⁴ gravitational path integral in the conformal gauge has a well-defined
  conformal factor sector; functional measure is that of one real scalar
- No instability or additional zero-modes from the conformal sector on compact
  $S^4$ (Gibbons–Hawking–Perry; GHP 1978)

**Disqualifying findings**:
- If the gravitational conformal sector on $S^4$ counts as $N > 1$ effective
  scalars (e.g., due to ghost contributions or gauge-fixing multipliers), $a/c$
  would be shifted by $N$ and $\neq 1/3$
- If the GHP conformal instability of the gravitational path integral on $S^4$
  alters the species count, C3 is compromised

**Current status**: PARTIAL — one-DOF counting natural from Weyl decomposition;
GHP instability handling in GRUT context needs explicit statement

---

### C4 — Fermion/Gauge Alternatives Excluded

**Question**: Is the identification to a real scalar preferred over a Weyl fermion
or gauge field on physical grounds, not because those give the wrong R?

**Required evidence**:
- Show that the gravitational conformal mode has integer spin (spin-0), ruling
  out Weyl fermion (spin-1/2) on symmetry grounds
- Show that the mode is uncharged and not a gauge degree of freedom, ruling out
  vector species
- The exclusion argument must not use $R = \sqrt{4/3}$ as input

**What we have**:
- $\sigma$ is a real scalar field — spin-0 by construction. Fermionic exclusion
  follows from spin statistics (no fermionic conformal factor)
- The conformal factor is not a gauge field; it carries no Yang–Mills charge
- The trace anomaly table shows: Weyl fermion gives $a/c = 11/18$, gauge field
  gives $a/c = 31/18$ — only real scalar gives $1/3$

**Critical warning**: The observation "only real scalar gives $a/c = 1/3$ and
$a/c = 1/3$ is needed for the correct $\Omega_\Lambda$" is observationally
supported but cannot serve as the *primary* exclusion argument without circularity.
The *primary* exclusion must come from the spin/statistics of $\sigma$.

**Disqualifying findings**:
- If the primary exclusion argument relies on "$a/c$ must be $1/3$ to give the
  right R" rather than on the spin and gauge properties of $\sigma$, C4 fails
  as circular

**Current status**: NEEDS_THEORY — spin/gauge exclusion is physically obvious but
not explicitly formalized in the GRUT codebase; circularity guard needed

---

### C5 — $P^{TT}$ Compatibility

**Question**: How does $\alpha_{\rm vac} = a/c$ for a *scalar* mode enter a
kernel $K^R = \alpha_{\rm vac}\,\chi(\omega)\,P^{TT}$ that **projects onto
transverse-tracefree modes** (which exclude scalar/trace degrees of freedom)?

**Required evidence**:
- Show that even though $P^{TT}$ removes the trace, the susceptibility $\chi(\omega)$
  of the TT modes to vacuum fluctuations carries $a/c$ from the conformal scalar
  sector
- Alternatively, show that the conformal anomaly coefficient $(a,c)$ appears in
  the heat kernel expansion for *TT graviton* propagation on $S^4$, not only in
  the scalar sector
- Identify the mechanism by which the conformal scalar anomaly enters the TT
  graviton response

**What we have**:
- On $S^4$, the heat kernel for TT gravitons has a Seeley–DeWitt expansion whose
  $a_2$ coefficient depends on the curvature — and for a conformally flat background
  the scalar conformal factor $\sigma$ contributes to curvature invariants seen
  by TT modes
- The Schwinger–DeWitt approach shows that the graviton propagator in a curved
  background receives contributions from the conformal anomaly of all species,
  including the conformal factor; $P^{TT}$ filters the polarizations but does not
  filter the anomaly

**Tension**:
- $P^{TT}$ projects *out* the scalar/trace component of $h_{\mu\nu}$; the
  conformal mode $\sigma$ lives in the *complement* of the TT sector
- If $K^R$ is purely TT, then $\alpha_{\rm vac}$ cannot come from the scalar-sector
  anomaly without a cross-coupling mechanism
- **This tension has no explicit resolution in the current GRUT codebase**

**Disqualifying findings**:
- If $P^{TT}$ strictly prevents scalar-sector anomaly from entering $K^R$, then
  the identification "conformal mode → $\alpha_{\rm vac}$" is incompatible with
  the kernel structure, and C5 fails

**Current status**: TENSION — the $P^{TT}$ / scalar-anomaly cross-coupling
mechanism must be explicitly derived; this is the most technically demanding
criterion

---

### C6 — R-Independence

**Question**: Is the identification of $\sigma$ as a real conformally-coupled scalar
made independently of the requirement that it produce $R = \sqrt{4/3}$?

**Required evidence**:
- The argument for C1–C4 must be constructible without knowing or using $R$
- The identification chapter must read: "Here is what $\sigma$ is, by the following
  physical arguments $\to$ therefore $a/c = 1/3$ $\to$ therefore $\alpha_{\rm vac} = 1/3$
  $\to$ therefore $R = \sqrt{4/3}$"
- It must NOT read: "We need $R = \sqrt{4/3}$, so we look for a species with
  $a/c = 1/3$, so we choose real scalar"

**What we have**:
- Via Route 2, $a/c = 1/3$ comes from Duff 1994 before $R$ is defined — the
  published value is not derived from $R$
- The spin/statistics argument for C4 (scalar vs. fermion vs. gauge) is independent
  of $R$
- The Weyl decomposition argument for C1 is independent of $R$
- Historical caveat (v6 → v11 reverse-engineering) is documented in
  `GATE3_ALPHA_VAC_PROVENANCE.md`; the Route 2 derivation breaks this circularity

**Disqualifying findings**:
- If C4 exclusion relies primarily on the R-observation (only $a/c = 1/3$ gives
  the right $\Omega_\Lambda$), then C6 is compromised — observational fit is a
  consistency check, not the primary exclusion argument

**Current status**: SUPPORTED for the published $a/c$ step; the identification
argument (C1–C4) must be written in the forward direction to fully close C6

---

## Pass/Fail Summary

| Criterion | Required result | Current status |
|---|---|---|
| C1 Scalar mode isolated | $\sigma$ (conformal factor) is the IR response mode | PARTIAL |
| C2 Conformal coupling justified | $\xi_c = 1/6$; matches Duff 1994 species | PARTIAL |
| C3 One real species | One real DOF; GHP instability handled | PARTIAL |
| C4 Fermion/gauge alternatives excluded | Spin-0 / uncharged; non-circular exclusion | **SUPPORTED** |
| C5 $P^{TT}$ compatibility | Cross-coupling mechanism scalar → TT response | **RESOLVED** |
| C6 R-independence | Forward-direction argument (physics → $a/c$ → $R$) | SUPPORTED |

**Gate status: C4 and C5 closed. C1–C3 remain PARTIAL — deferred to full Weyl
decomposition chapter (no new physical assumptions required).** See
`GATE_R_CONFORMAL_MODE_IDENTIFICATION_RESOLUTION.md` for C4/C5 arguments.

---

## The Critical Open Problem: C5

C5 is the most technically demanding criterion. The tension is:

- $K^R = \alpha_{\rm vac}\,\chi(\omega)\,P^{TT}$ is a TT kernel
- $\alpha_{\rm vac} = a/c$ is a scalar-sector anomaly coefficient
- $P^{TT}$ projects *out* the scalar sector

**Three possible resolutions** (one must be argued explicitly):

| Resolution | Mechanism | Plausibility |
|---|---|---|
| R5a: Off-diagonal coupling | The gravitational conformal factor $\sigma$ couples off-diagonally to TT gravitons via the background curvature of $S^4$; the anomaly leaks into the TT susceptibility | Plausible on curved background |
| R5b: Anomaly is background property | $a/c$ is a property of the background CFT, not a dynamical field; it modifies $\chi(\omega)$ for TT modes without requiring a TT-sector scalar mode | Standard in holographic literature |
| R5c: Effective species | The conformal scalar is an effective description of the TT graviton vacuum response; the "scalar" label refers to the species in the anomaly calculation, not a physical field propagating in the TT sector | Needs precise statement |

R5b is the most natural in the GRUT context: $\alpha_{\rm vac}$ enters $\chi(\omega)$
as a vacuum susceptibility, while $P^{TT}$ controls which modes the kernel
*acts on*. These are independent objects. The anomaly determines *how strongly*
the vacuum responds; the projector determines *which perturbations* trigger that
response.

**This must be made explicit in the identification chapter.**

---

## What the Identification Chapter Must Contain

A book-ready identification chapter needs:

1. **Weyl decomposition on $S^4$**: Derive $\sigma$ as the scalar conformal factor;
   show it is one real DOF; confirm conformal coupling $\xi_c = 1/6$ on $S^4$
2. **GHP conformal instability**: Acknowledge the Gibbons-Hawking-Perry instability
   of the Euclidean gravitational path integral on $S^4$; state how GRUT handles it
3. **Spin exclusion**: One paragraph showing $\sigma$ is spin-0, uncharged — fermion
   and gauge-field identification ruled out on spin/statistics grounds
4. **P^TT / anomaly decoupling**: Explicit argument (most likely R5b above) showing
   $\alpha_{\rm vac}$ enters $\chi(\omega)$ independently of $P^{TT}$
5. **Forward derivation**: Present the full chain in forward order:
   $\sigma$ is spin-0 conformal scalar → $(a,c) = (1,3)$ → $a/c = 1/3$ →
   $\alpha_{\rm vac} = 1/3$ → $n_g(0)^2 = 4/3$ → $R = \sqrt{4/3}$

---

## Gate Promotion Criteria

The gate passes when:

| Condition | Requirement |
|---|---|
| C1–C3 closed | Written derivation of Weyl decomposition → scalar mode on $S^4$ |
| C4 closed | Explicit spin/statistics exclusion of fermionic and gauge alternatives |
| C5 resolved | Written resolution of $P^{TT}$ / scalar-anomaly mechanism (R5a, R5b, or R5c) |
| C6 confirmed | Identification chapter reads forward: physics → $\alpha_{\rm vac}$ → $R$ |

When all four conditions are met, $\alpha_{\rm vac} = 1/3$ is fully provenanced
and the R-chain is complete.

---

## Current Status of the R-Chain

| Step | Status |
|---|---|
| $K^R = \alpha_{\rm vac}\,\chi(\omega)\,P^{TT}$ enters $S_{\rm const}$ | LOCKED |
| $\alpha_{\rm vac} = 1/3$ from published $a/c$ | SUPPORTED (Duff 1994 / KS 2011) |
| $R = \sqrt{4/3}$ from $n_g(0)^2 = 4/3$ | EXACT once $\alpha_{\rm vac} = 1/3$ is accepted |
| Old $\alpha = 1/d$ route | DEMOTED to assertion/history |
| KS/Duff route | CANONICAL route |
| Conformal mode $\equiv$ real conformal scalar | **THIS GATE — not passed** |

---

## Files

| File | Contents |
|---|---|
| `theory/hard_theory/GATE_R_CONFORMAL_MODE_IDENTIFICATION.md` | This spec |
| `theory/hard_theory/GATE_R_CONFORMAL_MODE_IDENTIFICATION_RESOLUTION.md` | C4/C5 resolution (2026-05-27) |
| `theory/hard_theory/GATE3_ALPHA_VAC_PROVENANCE.md` | Upstream: five Q&A for $\alpha_{\rm vac}$ |
| `theory/hard_theory/GATE3_CTP_ACTION_TERM_AUDIT.md` | Upstream: constitutive kernel structure |
| `grut/foundation/closure_protocol.py` | `ALPHA_VAC`, `N_G_DC`, `R_REFRACTIVE` |
| `theory/foundations_audit/ALPHA_VAC_PROVENANCE.md` | April 2026: Route 1 / Claim (a) audit |
| `theory/path_d_trace_anomaly/STAGE_D_TRACE_ANOMALY_RATIO.md` | Per-species $(a,c)$ table |

---

## Spec ID

`gate-r-conformal-mode-identification-spec-v1.0`
Frozen: 2026-05-27
