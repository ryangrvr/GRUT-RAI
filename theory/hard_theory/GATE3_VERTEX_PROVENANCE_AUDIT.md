# Gate 3 Vertex Provenance Audit

Date: 2026-05-26
Spec: gate3-vertex-provenance-audit-spec-v1.0
Status: R1 = NEEDS_THEORY; role = role_unassigned

---

## Purpose

The coefficient-role assignment gate established that:

$$C_{\mathrm{seed}}^{(3)} = \frac{\pi}{2}$$

is a validated, promotion-review-eligible seed — but its role in the GRUT quotient
system remains `role_unassigned` because Criterion R1 (Operator Source) is unresolved.

This audit sharpens the R1 question by:

1. Computing the **projection-factor hypothesis** exactly.
2. Identifying a **geometric dimensional ladder** connecting the seed to $R_{\rm target}$.
3. Documenting a **Green-function structural observation** that constrains which
   CTP vertices can produce the Allen–Jacobson integral.
4. Scoring five **candidate vertex sources** for structural consistency.
5. Stating the **blocking question** that must be answered to unlock R2 and R3.

---

## 1. The Projection-Factor Hypothesis

If $C_{\mathrm{seed}}^{(3)} = \pi/2$ is a quotient-bearing coefficient entering
exactly one side of $R = N/D$, then the other side must supply a projection factor
$\mathcal{N}$ such that:

$$R = \frac{\pi/2}{\mathcal{N}} = \sqrt{\frac{4}{3}} = \frac{2}{\sqrt{3}}$$

Solving:

$$\boxed{\mathcal{N} = \frac{\pi\sqrt{3}}{4}}$$

Numerical values (all exact to floating-point precision):

| Quantity | Value |
|---|---|
| $C_{\mathrm{seed}}^{(3)} = \pi/2$ | 1.5707963268… |
| $R_{\rm target} = \sqrt{4/3}$ | 1.1547005384… |
| $\mathcal{N} = \pi\sqrt{3}/4$ | 1.3603495232… |
| $(\pi/2) / (\pi\sqrt{3}/4)$ | 1.1547005384… ✓ |

**The projection factor is $\pi\sqrt{3}/4$.** If $\pi/2$ cancels as a shared
normalization instead, $R$ comes from other structure and this factor is irrelevant.

---

## 2. Geometric Dimensional Ladder

A striking exact identity connects the seed to the sphere-volume sequence:

$$\mathrm{Vol}(S^n) = \frac{2\pi^{(n+1)/2}}{\Gamma\!\left(\tfrac{n+1}{2}\right)}$$

| $n$ | $\mathrm{Vol}(S^n)$ |
|---|---|
| 2 | $4\pi$ |
| 3 | $2\pi^2$ |
| 4 | $8\pi^2/3$ |
| 5 | $\pi^3$ |

**Identity 1** (exact):
$$I(0,0) = \frac{\pi}{2} = \frac{\mathrm{Vol}(S^3)}{\mathrm{Vol}(S^2)}
= \frac{2\pi^2}{4\pi}$$

**Identity 2** (exact):
$$R_{\rm target} = \sqrt{\frac{4}{3}} = \sqrt{\frac{\mathrm{Vol}(S^4)}{\mathrm{Vol}(S^3)}}
= \sqrt{\frac{8\pi^2/3}{2\pi^2}}$$

These are not numerical coincidences — they are exact consequences of the
$\Gamma$-function recurrence. The dimensional ladder reads:

$$\frac{\mathrm{Vol}(S^3)}{\mathrm{Vol}(S^2)} = \frac{\pi}{2}
\qquad\longrightarrow\qquad
\sqrt{\frac{\mathrm{Vol}(S^4)}{\mathrm{Vol}(S^3)}} = \frac{2}{\sqrt{3}}$$

with the projection factor:
$$\mathcal{N} = \frac{\pi/2}{2/\sqrt{3}}
= \frac{\mathrm{Vol}(S^3)}{\mathrm{Vol}(S^2) \cdot \sqrt{\mathrm{Vol}(S^4)/\mathrm{Vol}(S^3)}}$$

**Interpretation**: $C_{\rm seed}^{(3)}$ is the ratio of adjacent sphere volumes
$S^3/S^2$, and $R_{\rm target}$ is the square root of the next ratio $S^4/S^3$.
Whether this dimensional-ladder structure has a physical origin in the GRUT CTP
action — or is a numerical property of dim-reg on $S^4$ — is the open question.

---

## 3. Green-Function Structural Observation

The Allen–Jacobson integral is:

$$I(h_-, \varepsilon) = 2 \cdot 4^{(D-3)/2}
\int_0^1 {}_2F_1(D-1,\, h_-;\, D/2;\, u)^3 \cdot [u(1-u)]^{(D-3)/2}\, du$$

with $D = 4 - 2\varepsilon$.

**Mathematical fact**: The function ${}_2F_1(D-1, h_-; D/2; u)$ is the
chordal-distance spectral function of the massive scalar propagator on $S^D$.
For a scalar field of dimensionless mass parameter $h_-$ on the unit $D$-sphere,
the two-point function in the coordinate $u = \sin^2(d/2)$ (where $d$ is geodesic
distance) takes the form:

$$G_{h_-}(u) = C \cdot {}_2F_1(D-1,\, h_-;\, D/2;\, u)$$

This identification is exact at any $h_-$ and $D$. Therefore:

- The integrand of $I(h_-, \varepsilon)$ is a **three-point function** of massive
  scalar propagators on $S^D$.
- The parameter $h_-$ is literally the mass of the scalar (in units of inverse
  sphere radius), and the limit $h_- \to 0$ is the massless limit.
- At $h_- = 0$: ${}_2F_1(a, 0; c; u) = 1$ exactly (series terminates at
  the zeroth term), so $I(0,0) = 4 \int_0^1 [u(1-u)]^{1/2}\, du = \pi/2$.

In the GRUT CTP context, $h_-$ parameterizes the **CTP branch split**
($h_- = h_+ - h_-$ in CTP notation). The $h_- \to 0$ limit is therefore the
**symmetric CTP point** where both branches coincide.

**Consequence for vertex identification**:

- **V1** ($R \log\Box R$): ruled out as the primary source of the triple-$_2F_1$
  structure. A non-local 2-point kernel does not naturally produce a 3-point function.
- **V3** (shared $S^4$ Green kernel): the propagators ARE the ${}_2F_1$ Green
  functions, making this the most structurally natural source.
- **V4** (CTP branch-response): the $h_-$ parameter explicitly encodes CTP branch
  structure, making this a natural source if the AJ integral is a CTP-specific loop.

---

## 4. Five Candidate Vertex Sources

| ID | Candidate | Role if confirmed | Triple-$_2F_1$ | Proj-factor plausibility |
|---|---|---|---|---|
| V1 | $R \log\Box R$ nonlocal Euler kernel | `final_coefficient_candidate` | LOW | LOW |
| V2 | Cosmological/Euler projection term | `cosmo_coefficient_candidate` | MODERATE | MODERATE |
| V3 | Shared $S^4$ Green kernel normalization | `shared_normalization` | HIGH | N/A (cancels in R) |
| V4 | CTP branch-response vertex | `final_coefficient_candidate` | MODERATE–HIGH | MODERATE |
| V5 | Pure benchmark Allen–Jacobson scalar seed | `benchmark_seed` | HIGH (by construction) | N/A (no quotient implication) |

### V1: $R \log\Box R$ nonlocal Euler kernel

The one-loop effective action of quantum gravity on curved backgrounds contains
the non-local term $R \log(\Box/\mu^2) R$, which on $S^4$ reduces to a finite
Euler-type coefficient. However, this term generates a **two-point** kernel
structure. The triple-${}_2F_1$ product in $I(h_-, \varepsilon)$ — three propagator
insertions — is not natural for a one-loop, two-point operator.

- **Theory input needed**: Compute the one-loop $R \log\Box R$ coefficient on $S^4$.
  Does its spectral function have the form ${}_2F_1(D-1, h_-; D/2; u)$? If three
  such factors appear in the loop: reconsider. Otherwise: V1 is disfavored.

### V2: Cosmological/Euler projection term

A three-loop matter correction to the cosmological constant, projected onto the
Euler density via the Gauss–Bonnet identity, would produce a three-loop vacuum
bubble. If each matter propagator on $S^4$ has the ${}_2F_1$ form, the triple
product would arise naturally. The matter field content would determine whether
$\sqrt{3}$ appears in the coupling.

- **Theory input needed**: Identify the matter sector in the GRUT CTP action
  contributing the three-loop cosmological-sector bubble on $S^4$.

### V3: Shared $S^4$ Green kernel normalization

The $S^4$ scalar Green function is $G_{h_-}(u) \propto {}_2F_1(D-1, h_-; D/2; u)$.
A triangle diagram of three such propagators on $S^4$ would produce exactly
$I(h_-, \varepsilon)$. If this diagram appears symmetrically in both the numerator
$N$ and denominator $D$ of the GRUT quotient, it cancels in $R$ and $\pi/2$ is a
shared normalization.

- **Theory input needed**: Verify that the GRUT CTP propagator on $S^4$ has the
  ${}_2F_1(D-1, h_-; D/2; u)$ form. Check whether the triangle diagram appears
  on both CTP branches or only one.

### V4: CTP branch-response vertex

In the Schwinger–Keldysh formalism, the branch-response vertex couples three
fields across the two CTP branches. The parameter $h_-$ in $I(h_-, \varepsilon)$
directly measures the CTP branch separation, making this a structurally natural
identification. If the branch-response vertex appears asymmetrically (only in $N$
or only in $D$), $\pi/2$ enters the quotient on one side and requires the
projection factor $\pi\sqrt{3}/4$ on the other.

- **Theory input needed**: Identify the three-point CTP vertex in the GRUT action
  that depends on $h_-$ as a branch-split parameter. Determine whether it appears
  in $N$, $D$, or both.

### V5: Pure benchmark Allen–Jacobson scalar seed

The AJ integral validates the extraction route and endpoint-split methodology but
is not a vertex in the GRUT CTP action. In this case $\pi/2$ is a `benchmark_seed`:
it confirms the numerical infrastructure but has no direct implication for $R$.

- **Theory input needed**: Verify that no CTP action term generates $I(h_-, \varepsilon)$.
  If no vertex is found: $\pi/2$ is benchmark only.

---

## 5. Structural Consistency Scores

Scores are **structural plausibility priors**, not evidence. They measure how
naturally each candidate produces the observed integral structure. High structural
score is necessary but not sufficient for R1 identification.

| ID | Composite | Triple-$_2F_1$ | GF-consistency | $S^4$-fit | Prefactor | Proj-factor |
|---|---|---|---|---|---|---|
| V5 | 1.000 | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 |
| V3 | 0.968 | 0.95 | 1.00 | 1.00 | 0.90 | 0.00 |
| V4 | 0.780 | 0.80 | 0.85 | 0.70 | 0.70 | 0.50 |
| V2 | 0.623 | 0.55 | 0.55 | 0.80 | 0.70 | 0.60 |
| V1 | 0.398 | 0.15 | 0.30 | 0.90 | 0.50 | 0.20 |

**Score weights**: triple-$_2F_1$ match (0.35), GF-consistency (0.30),
$S^4$-fit (0.20), prefactor (0.15).

**Projection-factor plausibility** (rightmost column) is a separate track:
it measures whether the vertex can be **quotient-bearing** rather than cancelling.
V3 and V5 score highest on structural consistency but have zero
projection-factor plausibility because they either cancel in $R$ (V3) or are
outside the quotient entirely (V5).

**The key fork**: V3 (highest structural score, cancels in $R$) vs V4 (high
structural score, potentially quotient-bearing, CTP-motivated). Theory must
distinguish them.

---

## 6. Current Assessment

| Criterion | Status | Reason |
|---|---|---|
| R1 Operator source | NEEDS_THEORY | No CTP vertex yet identified |
| R2 Projection target | BLOCKED | Requires R1 |
| R3 Quotient position | BLOCKED | Requires R2 |
| R4 Scheme behavior | PARTIAL | D1/D3 agreement supports protection |
| R5 Cancellation check | BLOCKED | Requires R3 |
| R6 Landing eligibility | PARTIAL | Role must be assigned first |

**Current role**: `role_unassigned`

**Promotion-review eligible**: Yes

---

## 7. Blocking Question

$$\boxed{
\text{Which CTP action vertex produces } I(h_-, \varepsilon)?
\text{ Does it appear on both CTP branches or only one?}
}$$

Two resolutions:

| Finding | Consequence |
|---|---|
| Vertex appears symmetrically on both CTP branches | `shared_normalization` — $\pi/2$ cancels in $R$; $R$ comes from other structure |
| Vertex appears asymmetrically (one branch only) | `final_coefficient_candidate` or `cosmo_coefficient_candidate`; projection factor $\pi\sqrt{3}/4$ required on the other side |
| Vertex is absent from CTP action entirely | `benchmark_seed`; $\pi/2$ validates numerics only |

---

## 8. What Would Resolve This Audit

| Action | Result |
|---|---|
| Identify the GRUT CTP action term generating $I(h_-,\varepsilon)$ on $S^4$ | R1 resolved → unlocks R2 |
| Show the term appears in both $N$ and $D$ | R1→R2→R3 → `shared_normalization` |
| Show the term appears only in $D$ | R1→R2→R3 → `final_coefficient_candidate` |
| Show the term appears only in $N$ | R1→R2→R3 → `cosmo_coefficient_candidate` |
| Show no such term exists in the GRUT CTP action | R1 → `benchmark_seed` |
| Explicit $R$ computation with $\pi/2$ as input gives $R = \sqrt{4/3}$ with no cancellation | confirms `final_coefficient_candidate` or `cosmo_coefficient_candidate` |

---

## 9. Output Format

The harness `gate3_vertex_provenance_audit.py` produces:

```json
{
  "spec": "gate3-vertex-provenance-audit-spec-v1.0",
  "date": "...",
  "seed_value": 1.5707963268,
  "R_target": 1.1547005384,
  "projection_factor": 1.3603495232,
  "projection_factor_exact": "pi*sqrt(3)/4",
  "geometric_ladder": { ... identity_1_seed, identity_2_R, projection_factor ... },
  "green_function_observation": { ... structural match, massless limit verification ... },
  "candidate_vertices_ranked": [ ... five candidates with scores ... ],
  "provisional_r1_assessment": {
    "r1_status": "NEEDS_THEORY",
    "provisional_role": "role_unassigned",
    "key_fork": "V3 (shared_normalization) vs V4 (final_coefficient_candidate)",
    "blocking_question": "...",
    "what_would_resolve_r1": [ ... three items ... ]
  },
  "current_role": "role_unassigned",
  "r1_status": "NEEDS_THEORY"
}
```

---

## Spec ID

`gate3-vertex-provenance-audit-spec-v1.0`
Frozen: 2026-05-26
