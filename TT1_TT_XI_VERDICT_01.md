# TT-1 — THE PHYSICAL D = 4 TT CHANNEL AND ξ: VERDICT

**Date:** 2026-09-25 · **Charter:** `TT1_TT_XI_CHARTER_01.md` (frozen at
`b4a2f33` before the run) · **Authority:** owner ruling on SX-1, given
in-session · **Instrument:** `calc/tt1_channel.py` · **Artifact:**
`TT1_CHANNEL_RESULT.json` (sha `8d3f508e72e28e99…`) · **Gated battery
9/10, one frozen red (L-F(b)), zero halts, single run.**

Halt-grade identities held:
- the L-ξ improvement identity, to 2.0e-15;
- the per-point TT rank 1, with λ₂/λ₁ = 1.8e-16;
- the L-K(a) collinear zero, to 2.3e-16;
- the on-shell condition on every sample, to 4.4e-16.

No absolute exponent was computed. There is no ω⁷ comparison. None of
the excluded selectors appears.

## VERDICT

> | Question | Outcome |
> |---|---|
> | **Q1** Is ξ (and its tower) visible in the physical TT channel? | **DERIVED-IN-CLASS: no.** ξ is irrelevant on-shell TT. |
> | **Q2** Is the coupling form forced once higher derivatives are allowed? | **TT tensor FORCED** (rank 1 per point). **Leading IR coupling forced**, with the higher-derivative form factor suppressed. **Form factor beyond leading order CONSTRAINED-NONUNIQUE.** One frozen red: the rank count was predicted 4 and measured 3. |
> | **Q3** When does the TT pair channel exist? | **CLASS-SPLIT** by the retained sector's light cone relative to the probe's: dead / open ∝ subluminality / closed. |

**1. The D = 4 ξ ambiguity dissolves in the physical TT channel.**
Every improvement structure ξ(η^{ij}k² − k^ik^j)·f, for f = 1, p₁·p₂ and
|p₁|² + |p₂|², has a TT image at most 2e-15 of the canonical vertex. The
reason is structural, not numerical:
- Λ(k k) = 0 because P k = 0;
- Λ(𝟙) = 0 because tr P = 2;
- on shell k² = 0.

The whole tower is therefore projected out. ξ remains visible
off-shell/in the trace, where a sensitivity note shows the improvement
trace is 0.754 ≠ 0 at static strain kinematics. So CP-1's strain-class
finding is **retained, not contradicted**. The ξ question was a question
about the *probe class*, and on the physical graviton channel it has no
content.

**2. The tensor is forced; the form factor is not.** For each on-shell
point, the TT images of all five couplings T₁…T₅ are collinear. In the
transverse plane each image is ∝ (q q − ½P q²) with q = P p₁, and
P p₂ = −q. T₂ ∝ T₁ exactly (ratio −1). Across points, the scalar form
factors are **not** a single function, so the momentum dependence of
the vertex is not fixed by the channel. The higher-derivative piece T₃
relative to T₁ grows exactly ×4.000 from p = 0.2 to p = 0.4, which is
IR suppression ∝ p². The **leading IR coupling is forced**. What lies
beyond leading order is choice, and it inherits the supplied
geometric-coupling/Sel-4x premise that SX-1 classified.

**3. The channel's existence is a light-cone relation.**

| Retained-sector dispersion | Locus | TT vertex | Channel |
|---|---|---|---|
| ω = \|p\| (v = c exactly) | collinear, cos θ = 1 | 2.3e-16 (identically 0) | **dead** (aligned death) |
| ω = 0.8\|p\| | non-collinear | min 0.032 over 200 pairs | **open** |
| ω = \|p\| − α\|p\|³ | slightly opened | 1.77e-3 (α = 0.01), 3.53e-3 (α = 0.02); ratio 1.9975 | **open ∝ α** |
| ω = \|p\| + 0.01\|p\|³ | none (cos θ ≥ 1 + 1.6e-3) | — | **closed** |

With RS-1's per-sector v = c units choice, **the channel lives only on
dispersion curvature**. That curvature is microscopic retained-sector
content, not something the channel supplies. The cross-sector light-cone
relation (probe c vs. sector c) is U-1 territory and stays supplied.

## THE FROZEN RED (kept red)

**L-F(b)** predicted a form-factor rank of **4** across points. The
measured rank is **3**: the Gram eigenvalues are 4.57, 0.370, 0.0557,
then 7e-16.

**Labeled diagnostic, written into the instrument before the run.** The
on-shell identity was recognized while building the instrument, after
the charter was frozen. The frozen gate was left unchanged, and it went
red as anticipated.
- For a linear sector, the on-shell condition itself gives
  p₁·p₂ = ½(v² − 1)(a² + b²) + ω₁ω₂. This holds to 4.4e-16.
- So T₄'s form factor is a fixed combination of T₃'s and T₅'s. The
  count 4 was an overcount.
- With dispersion curvature (ω = 0.8|p| − 0.1|p|³), the identity breaks
  and the rank is 4. The fourth eigenvalue is 2e-4, well above the
  1e-10 cut.

**Effect on the outcome: none.** The frozen rule reads
CONSTRAINED-NONUNIQUE for any rank > 1, and the rank is 3 or 4
depending on class. The red stays attached to the rank *count*.
Incidentally, the on-shell condition does some of the constraining the
charter attributed to nothing.

## STRENGTH AND LIMITS (stated plainly)

- **Q1 is projector algebra.** Λ kills k k and 𝟙, and that is textbook
  transversality. Its value here is classification: the ξ ambiguity that
  CP-1 left open is a property of off-shell/trace probes, not of the
  physical channel.
- **Q2 covers a finite family.** Five structures of up to four
  derivatives were tested. "Rank 1 per point" is general for symmetric
  tensors built from p₁, p₂ and k, because every such tensor projects
  onto the single TT structure q q − ½P q². The form-factor
  non-uniqueness is a lower bound.
- **Q3 is tree-level, 2 → 1 kinematics.** It covers single-graviton
  emission from a pair with one isotropic dispersion per sector. It
  says nothing about loop, medium or multi-graviton channels, and it
  computes no rate exponent.
- **The existence split needs the probe/sector light-cone comparison,
  which is supplied.** TT-1 classifies what follows from it; it does
  not earn it.

## LEDGER

- **κ:** discharged.
- **C_cons:** irreducible, reduced to the supplied massless
  gauge/Lorentz probe.
- **Universality:** derived under exchange; universal reach supplied.
- **Retained sector:** conditional on CARRIER plus the supplied probe;
  the class is selected.
- **CARRIER:** access-seed coincidence, supplied.
- **Geometry:** CLASS-SPLIT / access-relative (GS-1).
- **Sel-4x:** IRREDUCIBLE, reduced to the co-stretch declaration;
  inherited here, not re-decided.
- **ξ (new):** irrelevant in the physical TT channel (DERIVED-IN-CLASS);
  visible only off-shell/in the trace.
- **TT coupling (new):** tensor forced; leading IR form factor forced;
  subleading form factor CONSTRAINED-NONUNIQUE.
- **TT channel existence (new):** CLASS-SPLIT by the relative light
  cone. Under v = c per sector it rides on dispersion curvature alone.
- GeoInv unearned. **Class-4 OPEN.**

ω⁷ not used; the v3 record is not reopened. GR-1 3D red. ℏ located.
Operator ordering fenced.

## HARD STOP

Hard stop after the TT/ξ verdict, as chartered. The physical graviton
channel is now classified:
- ξ has no content there;
- the tensor and the leading coupling are forced;
- whether the channel exists at all is a property of the retained
  sector's dispersion relative to the probe's light cone. That comes
  down to curvature, which is microscopic content the program has not
  yet earned.
