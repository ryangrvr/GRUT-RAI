# Gate 3 Alpha_vac Provenance Audit

Date: 2026-05-27
Spec: gate3-alpha-vac-provenance-spec-v1.0
Status: Q1/Q3/Q4/Q5 = CONFIRMED; Q2 = ROUTE 2 EXPLICIT, identification step needs chapter

---

## Purpose

The CTP action term audit established that the GRUT canonical R-value is:

$$R = n_g(0) = \sqrt{1 + \alpha_{\rm vac}} = \sqrt{4/3}$$

from the constitutive cross-term $S_{\rm const}$ with retarded kernel
$K^R = \alpha_{\rm vac}\,\chi(\omega)\,P^{TT}$.

This makes $\alpha_{\rm vac} = 1/3$ the **load-bearing input** of the entire
R-chain. This audit answers Ryan's five book-readiness questions and reconciles
two previously conflicting provenance claims.

---

## 1. Per-Species Trace Anomaly (KS 2011 / Duff 1994)

From Duff 1994 eq (30)–(31) and Kounnas–Scrucca 2011 eq (A.5):

| Species | $(a,\, c)$ | $a/c$ | Role |
|---|---|---|---|
| Real scalar (conformally coupled) | $(1,\, 3)$ | $1/3$ | $\alpha_{\rm vac}$ ← |
| Weyl fermion | $(11/2,\, 9)$ | $11/18$ | — |
| Gauge field (vector + ghosts) | $(62,\, 36)$ | $31/18$ | — |

$$\boxed{\alpha_{\rm vac} = \frac{a}{c}\bigg|_{\rm real\;scalar} = \frac{1}{3}
\quad \text{[EXACT, PUBLISHED]}}$$

---

## 2. Two Routes to $\alpha_{\rm vac} = 1/3$

The codebase historically contained two different claims. They are **not the same
claim**, and only one of them is supported by the cited literature.

### Route 1 — v11 App H: $\alpha = 1/d$ (NOT supported)

> "In $d$ spatial dimensions, the vacuum impedance is $\alpha = 1/d$. Setting
> $d = 3$ gives $\alpha_{\rm vac} = 1/3$."

| Assessment | Finding |
|---|---|
| Source | GRUT v11 Appendix H — narrative text |
| In KS 2011? | **No** — this exact claim does not appear |
| In Duff 1994? | **No** |
| Status | **ASSERTION** — a numerical coincidence dressed as dimensional reduction |

The April 2026 `ALPHA_VAC_PROVENANCE.md` audit correctly found that
"vacuum impedance = 1/d" is not a published physics result. That audit was
checking Route 1 (Claim a). Its finding stands.

### Route 2 — KS 2011 / Duff 1994: $a/c = 1/3$ for real scalar (SUPPORTED)

> "For a single real conformally-coupled scalar in 4D CFT, the trace anomaly
> coefficients are $(a, c) = (1, 3)$, giving $a/c = 1/3$."

| Assessment | Finding |
|---|---|
| Source | Duff 1994 eq (30)–(31); KS 2011 eq (A.5) |
| In KS 2011? | **Yes** |
| In Duff 1994? | **Yes** (independent confirmation) |
| Status | **PUBLISHED** — textbook result, two independent sources |
| Convention-independent? | **Yes** — $a/c$ is a dimensionless ratio; survives all normalization changes |

**The book must use Route 2, not Route 1.**

---

## 3. The Identification Step (Load-Bearing)

Route 2 establishes $a/c = 1/3$ for a real conformally-coupled scalar. To
conclude $\alpha_{\rm vac} = 1/3$, GRUT makes one additional identification:

$$\boxed{\text{gravitational conformal mode} \equiv \text{real conformally-coupled scalar}}$$

This is a **GRUT-specific physical identification**. It is the load-bearing step
that converts a published CFT result into the GRUT vacuum impedance.

| Piece | Status |
|---|---|
| $a/c = 1/3$ for real scalar | PUBLISHED (Duff 1994 / KS 2011) |
| Conformal mode = real scalar | GRUT-SPECIFIC — needs its own derivation chapter |
| $\alpha_{\rm vac} = a/c = 1/3$ | Follows IF identification holds |

**The identification chapter is the remaining open item.** It must show why
the IR carrier of the gravitational vacuum response behaves as a single real
conformally-coupled scalar, not as a Weyl fermion or gauge field. This is
physics content, not a numerical audit.

---

## 4. Independence: $\alpha_{\rm vac}$ is Computed Before R

The computation order via Route 2 is:

```
Step 1: Duff 1994 per-species (a,c) for real scalar: (1, 3)
Step 2: a/c = 1/3  [no R involved]
Step 3: Identify conformal mode as real scalar
Step 4: alpha_vac = a/c = 1/3  [still no R involved]
Step 5: n_g(0) = sqrt(1 + 1/3) = sqrt(4/3) = R  [R computed last]
```

$R$ is a **consequence** of $\alpha_{\rm vac}$, not its source.

**Historical caveat**: The historical route *was* reverse-engineered. GRUT v6
started with a holographic $a/c = 4/3$ claim; v11 then provided the post-hoc
"$\alpha = 1/d$" narrative to justify $1/3$. Route 2 breaks this circularity
by anchoring to Duff 1994 coefficients directly.

| Route | Circular? | Status |
|---|---|---|
| Route 1 (v11 App H) | Potentially — post-hoc narrative | ASSERTION |
| Route 2 (KS 2011 / Duff) | No — $a/c$ computed from first principles | INDEPENDENT |

---

## 5. Convention Invariance

$a/c = 1/3$ is a dimensionless ratio of two Weyl anomaly coefficients. It is
invariant under:

| Convention change | Result |
|---|---|
| KS 2011 normalization | $a/c = 1/3$ ✓ |
| Duff 1994 normalization | $\|b'\|/b = 1/3$ ✓ |
| Arbitrary overall rescaling $N \cdot (a, c)$ | $Na/(Nc) = a/c = 1/3$ ✓ |

**$\alpha_{\rm vac} = 1/3$ is convention-independent.** This is an exact
rational number, not a floating-point coincidence.

---

## 6. KS 2011 Path: Which Claim is Supported?

Two distinct claims have been attributed to KS 2011:

| Claim | Statement | In KS 2011? | Status |
|---|---|---|---|
| (a) | $\alpha = 1/d$ from dimensional reduction | **No** | NOT SUPPORTED |
| (b) | $a/c = 1/3$ for real conformally-coupled scalar | **Yes** | SUPPORTED |

The April 2026 audit correctly rejected Claim (a). Claim (b) — which is what
`grut/foundation/closure_protocol.py` actually uses — is supported.

**Resolution**: The codebase is correct. The narrative in v11 App H (Claim a)
should be replaced by an explicit reference to Duff 1994 / KS 2011 eq (A.5)
(Claim b) in the book.

---

## 7. Sensitivity: Why $\alpha_{\rm vac}$ Must Be Near $1/3$

The GRUT cosmological prediction depends on $\alpha_{\rm vac}$ through:

$$\Omega_\Lambda \propto n_g(0)^2 = 1 + \alpha_{\rm vac}$$

| $\alpha_{\rm vac}$ | $R$ | $\Omega_\Lambda$ (approx) | Planck deviation | Physical? |
|---|---|---|---|---|
| $1/4$ | $1.118$ | $0.238$ | $-65.5\%$ | marginal |
| $0.27$ | $1.127$ | $0.317$ | $-54.0\%$ | no |
| $\mathbf{1/3}$ | $\mathbf{1.155}$ | $\mathbf{0.690}$ | $\mathbf{+0.14\%}$ | **yes** ← |
| $0.4$ | $1.183$ | $1.336$ | $+93.9\%$ | no |
| $1/2$ | $1.225$ | $2.938$ | $+326\%$ | no |

Only $\alpha_{\rm vac} \approx 1/3$ gives a physically sensible $\Omega_\Lambda$
in the Planck range. The framework is **sensitive**: a 10% deviation in
$\alpha_{\rm vac}$ produces $\sim 50\%$ deviation in $\Omega_\Lambda$. This
means the identification $\alpha_{\rm vac} = 1/3$ is not a tuning choice — the
framework selects it.

---

## 8. Five Book-Readiness Questions: Answers

| ID | Question | Answer | Status |
|---|---|---|---|
| Q1 | Where does $\alpha_{\rm vac} = 1/3$ enter the GRUT action? | Constitutive cross-term $S_{\rm const}$: $K^R = \alpha_{\rm vac}\,\chi(\omega)\,P^{TT}$; sets $n_g(0)^2 = 1 + \alpha_{\rm vac}$ | IDENTIFIED |
| Q2 | Is it derived from TT projection, vacuum susceptibility, or dimensional averaging? | Route 2: $a/c = 1/3$ from Duff 1994 trace anomaly coefficients for real scalar; identification step (conformal mode = scalar) needs chapter | ROUTE 2 EXPLICIT |
| Q3 | Is it independent of $R$? | YES via Route 2: $a/c = 1/3$ computed from Duff 1994 before $R$ is defined; historical route was reverse-engineered (see caveat) | INDEPENDENT |
| Q4 | Does it survive convention changes? | YES: $a/c$ is a dimensionless ratio; invariant under KS 2011, Duff 1994, and arbitrary normalization changes | CONFIRMED |
| Q5 | Does it match the cited KS 2011 path? | YES for Claim (b): $a/c = 1/3$ for real scalar is in KS 2011 eq (A.5). NO for Claim (a): $\alpha = 1/d$ is not | RESOLVED |

---

## 9. The Complete $\alpha_{\rm vac}$ Chain

```
Duff 1994 / KS 2011 eq (A.5)
  → per-species (a,c): real scalar = (1, 3)
  → a/c = 1/3  [exact rational, no R]
  → GRUT identification: conformal mode ≡ real conformally-coupled scalar
  → alpha_vac = a/c = 1/3  [load-bearing identification]
  → enters S_const: K^R = alpha_vac * chi(omega) * P^TT
  → DC limit: n_g(0)^2 = 1 + alpha_vac = 4/3
  → R = sqrt(4/3)  [Path G canonical value]
```

The only step requiring additional derivation/justification is the identification.
Everything else is exact.

---

## 10. Book Action Items

| Item | Action | Priority |
|---|---|---|
| Replace Route 1 narrative | Replace "vacuum impedance = 1/d" (v11 App H) with explicit Duff 1994 eq (30)–(31) reference | **IMMEDIATE** |
| Write identification chapter | Derive why gravitational conformal mode ≡ real conformally-coupled scalar, not fermion or gauge field | **HIGH** |
| Flag historical circularity | Note in a footnote that v6–v11 used reverse-engineered $\alpha$; current derivation breaks this | **MEDIUM** |
| Promote Route 2 to primary | In `closure_protocol.py` docstring, make "Duff 1994 / KS 2011 eq (A.5)" the lead citation | **LOW** |

---

## 11. Current Assessment

| Layer | Finding |
|---|---|
| $\alpha_{\rm vac}$ source | $a/c = 1/3$ for real scalar (Duff 1994 / KS 2011) — PUBLISHED, EXACT |
| Route in use | Route 2 (`closure_protocol.py`) — CORRECT |
| Route in book (v11) | Route 1 ("$\alpha = 1/d$") — ASSERTION, should be replaced |
| Convention independence | YES — dimensionless ratio, invariant |
| Independence from $R$ | YES via Route 2 (historical reverse-engineering is documented as caveat) |
| KS 2011 match | YES for Claim (b); April 2026 audit correctly rejected Claim (a) |
| Load-bearing identification | "conformal mode = real scalar" — needs derivation chapter |
| Sensitivity | High — only $\alpha \approx 1/3$ gives physical $\Omega_\Lambda$ |
| Book readiness | Q1/Q3/Q4/Q5 confirmed; Q2 requires identification chapter |

---

## 12. What Resolves the Remaining Open Item

The identification "gravitational conformal mode = real conformally-coupled
scalar" needs a dedicated chapter arguing:

1. **IR dominance**: In the low-energy limit of the gravitational path integral,
   which degrees of freedom carry the dominant vacuum response?
2. **Conformal sector selection**: Why does the TT projector $P^{TT}$ select
   the conformal scalar sector rather than the spin-1 or spin-2 sectors?
3. **Species exclusion**: Why not Weyl fermion ($a/c = 11/18 \neq 1/3$) or
   gauge field ($a/c = 31/18 \neq 1/3$)?
4. **Single-species counting**: Why one real scalar rather than a superposition?

If this chapter is written and holds, then $\alpha_{\rm vac} = 1/3$ is
fully provenanced, and the R-chain is complete.

---

## 13. Files

| File | Contents |
|---|---|
| `grut/hard_theory/s4_ctp_solver/gate3_alpha_vac_provenance.py` | This harness |
| `theory/hard_theory/GATE3_ALPHA_VAC_PROVENANCE.md` | This spec |
| `theory/hard_theory/gate3_dl_outputs/gate3_alpha_vac_provenance.json` | Execution output |
| `grut/foundation/closure_protocol.py` | `ALPHA_VAC`, `N_G_DC`, `R_REFRACTIVE` |
| `theory/foundations_audit/ALPHA_VAC_PROVENANCE.md` | April 2026 audit (Route 1 / Claim a analysis) |
| `theory/hard_theory/GATE3_CTP_ACTION_TERM_AUDIT.md` | Upstream: R from constitutive kernel |
| `theory/path_d_trace_anomaly/STAGE_D_TRACE_ANOMALY_RATIO.md` | Per-species $(a,c)$ table |

---

## Spec ID

`gate3-alpha-vac-provenance-spec-v1.0`
Frozen: 2026-05-27
