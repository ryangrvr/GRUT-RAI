# Instrument-layer design — reproduction runners & source-verification queue

**Date:** 2026-08-23 · Design only; runners not yet implemented. Per brief: extractor first
(done, `prose_extractor.py`), runners second, source verification as workflow design only.

## 1. Plant-and-recover runner design ([A-3])

**Principle:** a runner that rejects absurd plants demonstrates nothing. Plants must be close
enough that only the actual physics separates them.

**The model case:** axial-coefficient rival `6ℓ−8` matched incumbent `ℓ(ℓ+1)−2` at ℓ=2,3 and
diverged at ℓ=4. Someone could have believed it. Recovery of the plant made "18" a measurement.

| target node | incumbent | planted rival | distance | source |
|---|---|---|---|---|
| mu_linear | linear-in-μ payoff | quadratic-in-μ (nearest defensible) | small; both fit low-μ data | nearest alternative |
| kk_static_transfer | computed transfer | single-pole approx to same kernel | same family | internal variant |
| x_no_pin_theorem | no-pin result | weakened pin (ε-pin) | parameterised | natural weakening |

Runner spec per target:
1. compute incumbent value;
2. inject plant as alternative hypothesis in the SAME harness;
3. require the harness to recover BOTH values and report which fits;
4. **report plant-vs-incumbent distance**; if distance is large, record runner as WEAK not PASS.

## 2. Source-verification queue — workflow design only

Not fully automatable (paywalls). Build the QUEUE and VOCABULARY:

- **queue:** every BORROWED-evidence claim → its primary source → status (open / paywalled / obtained)
- **vocabulary:** VERIFIED-SAYS · MISMATCH · UNREACHABLE · PARTIAL
- precedent: 2107.13905 "square of e-foldings" retired after source check killed premise twice
- priority order: rung2_kms_gate (KMS textbook) > founding_h1_zeta_casimir > rung1 SK lineage

## 3. Interleave contract ([A-1]) — restated on this artifact

Physics track declares every quarantined/unbanked consumed result in ONE named block with
provenance (`AGENT_COORDINATION.md`, 2026-08-22). Audit feeds physics via declared blocks only;
physics feeds audit via banked results only. Neither reads the other's drafts. A later correction
is then a one-line recomputation from the declared block.

## 4. Extractor self-report (emitted)

`prose_extractor.py` emits: live edges 46 · inactive 1 · negation 4 (excluded) · substring
collisions 0 · corpus 28 files. False-positive rate: NOT YET MEASURED — hand-check of a random
sample is required before prose blast radii support the load-bearing map. Logged as blocker.

