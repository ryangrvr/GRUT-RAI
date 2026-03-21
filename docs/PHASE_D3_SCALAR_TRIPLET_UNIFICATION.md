# Phase D3 — Scalar/Triplet Unification and Symmetry-Breaking Trigger

This is a taxonomy and narrowing phase, not locked canon.

---

## A. Mission & Context

D1 formulated the O(3) triplet hedgehog defect as a provisional candidate. D2 showed it is numerically viable. The next critical question:

**What is the mathematical relation between the original scalar-memory field Phi and the O(3) triplet vec(Phi)?**

**What triggers the symmetry breaking?**

| Prior Phase | Status |
|-------------|--------|
| Phase 6: f(R_eq) | LOCKED (-17.71) |
| Phase 6B: A_crit | LOCKED (1.062) |
| Phase 6C: deficit | LOCKED (Component A + Component B) |
| Route C (all kernels) | LOCKED (insufficient) |
| Route B (all channels) | LOCKED (closed) |
| Source-Law Program I | LOCKED (partially viable, no GRUT-native) |
| Defect D1 | LOCKED (provisional candidate formulated) |
| Defect D2 | LOCKED (defect_candidate_numerically_viable) |

**Goal**: Narrow the unification architecture and trigger mechanism space for the next phase.

---

## B. Relation-Type Taxonomy

Four architectures assessed:

### 1. Embedding (radial-mode identification)

Phi = |vec(Phi)|. The scalar-memory field is identified with the radial modulus of the O(3) triplet. Angular modes carry the hedgehog structure.

- Coherence: 0.90 (standard field-theory construction)
- Compatibility: 0.85 (preserves scalar-memory as radial sector in principle)
- Explanatory: 0.75 (candidate route for both A and B, not yet derived)
- Ad hoc: 0.15 (reinterpretation, no new fields)
- **Overall: 0.7929** — strong candidate

### 2. Companion sector (coupled but distinct)

Phi and vec(Phi) are distinct fields coupled via a portal term g*Phi*|vec(Phi)|^2.

- Coherence: 0.80
- Compatibility: 0.70 (both sectors preserved but coupling must be consistent)
- Explanatory: 0.60 (explains both but does not unify)
- Ad hoc: 0.45 (two new parameters)
- **Overall: 0.5714** — moderate

### 3. Emergent reorganization (from lag/doubled structure)

vec(Phi) arises effectively from the CTP doubled-field structure.

- Coherence: 0.35 (speculative, no explicit construction)
- Compatibility: 0.40 (unknown)
- Explanatory: 0.85 (would be deep if constructible)
- Ad hoc: 0.30 (potentially low, but undemonstrated)
- **Overall: 0.4286** — weak

### 4. Replacement (scalar is truncation of triplet)

Old scalar-memory field is a truncation of a more fundamental triplet.

- Coherence: 0.85
- Compatibility: 0.30 (destroys prior scalar-memory interpretation)
- Explanatory: 0.80
- Ad hoc: 0.35
- **Overall: 0.5000** — moderate

---

## C. Trigger Taxonomy

Five trigger classes assessed:

| ID | Trigger | GRUT-native | Score | Verdict |
|----|---------|-------------|-------|---------|
| 1 | Explicit SSB (mu^2 by hand) | NO | 0.40 | moderate |
| 2 | Curvature-triggered (xi*R) | YES | 0.80 | strong candidate |
| 3 | Source-density-triggered | NO (partially) | 0.45 | moderate |
| 4 | Lag-/processing-triggered | YES | 0.60 | moderate |
| 5 | Hybrid (curvature + density) | YES (partially) | 0.50 | moderate |

**Curvature-triggered SSB** is structurally attractive because strong-field curvature provides an environment-dependent trigger using existing GRUT geometric structure. The sign and regime must still be checked in the actual coupled model.

**Lag-/processing-triggered SSB** is also GRUT-native (tau is the fundamental GRUT parameter) but requires careful treatment as a mathematical hypothesis only, with no metaphysical or observer-based claims.

---

## D. Canon Preservation

This is the hardest filter. For each architecture:

| Architecture | Comp A intact | Comp B produced | Sigma additive | Locked stable | ALL PASS |
|-------------|--------------|----------------|----------------|---------------|----------|
| Embedding | YES | YES | YES | YES | **YES** |
| Companion | YES | YES | YES | YES | **YES** |
| Emergent | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | **NO** |
| Replacement | NO (rederive) | YES | YES | NO (disrupts) | **NO** |

Only embedding and companion pass all canon-preservation checks. Emergent fails because no explicit construction exists. Replacement fails because it disrupts prior locked results.

---

## E. Minimal Couplings

Five minimal coupling candidates:

| ID | Formula | Relation | Trigger | New params |
|----|---------|----------|---------|------------|
| 1 | Phi = \|vec(Phi)\| | Embedding | — | 0 |
| 2 | g * Phi * \|vec(Phi)\|^2 | Companion | — | 1 |
| 3 | xi * R * \|vec(Phi)\|^2 | Embedding | Curvature | 1 |
| 4 | alpha_d * rho(r) * \|vec(Phi)\|^2 | Embedding | Source-density | 1 |
| 5 | beta * (1/tau^2) * \|vec(Phi)\|^2 | Embedding | Lag/processing | 1 |

---

## F. Candidate Ranking

Ten architecture+trigger pairings ranked by combined score:

| Rank | Architecture | Score | Canon |
|------|-------------|-------|-------|
| 1 | Embedding + curvature trigger | 0.8215 | PASS |
| 2 | Embedding + lag/processing trigger | 0.7615 | PASS |
| 3 | Embedding + hybrid trigger | 0.6815 | PASS |
| 4 | Companion + curvature trigger | 0.6807 | PASS |
| 5 | Embedding + source-density trigger | 0.6664 | PASS |
| 6 | Embedding + explicit SSB | 0.6415 | PASS |
| 7 | Companion + explicit SSB | 0.5007 | PASS |
| 8 | Emergent + curvature trigger | 0.4993 | FAIL |
| 9 | Replacement + explicit SSB | 0.4050 | FAIL |
| 10 | Replacement + curvature trigger | 0.4950 | FAIL |

Canon-passing candidates: 7/10.

---

## G. Classification

**Classification**: `scalar_triplet_embedding_most_promising`

This means:
- The embedding architecture (Phi = |vec(Phi)|) is the top-ranked candidate
- Curvature-triggered SSB (mu_eff^2 = mu_0^2 + xi*R) is the top-ranked trigger
- This pairing passes all canon-preservation checks
- The ranking is earned through structural scoring, not predetermined

### What this classification does NOT mean:
- The embedding is not yet derived or proven
- The radial mode has not yet been shown to reproduce Component A in detail
- The curvature trigger sign and regime have not been computed in the coupled system
- This is the leading candidate for D4, not a concluded theory

### Phase lock update

| Phase | Status |
|-------|--------|
| Phase 6: f(R_eq) | LOCKED (-17.71) |
| Phase 6B: A_crit | LOCKED (1.062) |
| Phase 6C: deficit | LOCKED (Component A + Component B) |
| Route C (all kernels) | LOCKED (insufficient) |
| Route B (all channels) | LOCKED (closed) |
| Source-Law Program I | LOCKED (partially viable, no GRUT-native) |
| Defect D1 | LOCKED (provisional candidate formulated) |
| Defect D2 | LOCKED (defect_candidate_numerically_viable) |
| **Unification D3** | **ASSESSED (scalar_triplet_embedding_most_promising)** |

---

## H. Numerical Validation Summary

- Benchmark: **57/57 checks PASSED**
- Pytest: **57/57 tests PASSED** (0.22s)
- 4 relation types assessed
- 5 trigger types assessed
- 4 canon-preservation checks
- 5 minimal coupling candidates
- 10 architecture pairings ranked

---

## I. Nonclaims (10)

1. This phase does NOT prove the final unified field theory.
2. This phase does NOT derive the defect sector uniquely from the locked GRUT core.
3. This phase does NOT justify metaphysical or observer-based symmetry breaking.
4. A top-ranked architecture is not yet canon; it is a next-phase target.
5. This phase only narrows the candidate unification architecture and trigger mechanism.
6. The embedding model is a strong candidate, not a predetermined conclusion.
7. The claim that the radial mode preserves Component A is a candidate hypothesis, not derived.
8. Curvature-triggered SSB is a candidate trigger; the sign and magnitude have not been computed.
9. The ranking reflects structural assessment within the tested taxonomy only.
10. The classification is within the D3 framework only. D4 may revise the ranking.

---

## J. Assumptions (10)

1. The O(3) triplet hedgehog defect sector is provisionally numerically viable (D2).
2. The original scalar-memory field produces Component A ~ 1/r^4.
3. The defect sector produces Component B ~ eta^2/r^2 asymptotically.
4. Four relation-type architectures are assessed.
5. Five trigger-type classes are assessed.
6. Canon preservation is the hardest filter.
7. Scoring is deterministic and structural.
8. The embedding model is assessed as a candidate, not assumed correct.
9. Curvature-triggered SSB is structurally attractive but needs coupled-model verification.
10. This phase narrows the space; it does not derive the final theory.

---

## K. Recommended Next Move

Phase D4 should implement the top-ranked architecture:

1. **Embedding + curvature trigger**: Construct the explicit Lagrangian L(vec(Phi), g_mu_nu) with non-minimal coupling xi*R*|vec(Phi)|^2.
2. **Radial-mode verification**: Derive the effective equation for the radial mode |vec(Phi)| and check whether it reproduces the scalar-memory equation.
3. **Curvature sign check**: Compute R in the GRUT interior and verify that xi*R can flip the effective mass sign.
4. **Coupled BVP**: Solve the coupled triplet + metric system numerically.
5. **Component A recovery**: Verify that the radial sector of the embedding reproduces Component A ~ 1/r^4.
