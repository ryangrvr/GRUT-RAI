# S3 — OWNER RULING 01 (S3-0 accepted; D-1 … D-6; REV-0 opened)

**Date:** 2026-09-30 · **Recorded by the owner on Issue #2, comment `5909891161`**, after review of
the pre-registration `febc3f6`, the audit `b2b8f8b`, the reversal diagnostic, and the L0-1d / L0-1e
source records. The comment is authoritative; this file records it.

## 1. Terminal: ACCEPTED

**S3-0 = FORMULABLE-ONLY-WITH-CHANGE**, under both declared FDT-like readings.

> **Binding reading:** The missing crossed cell is not available from the current declared record at
> fixed invariants. Constructing it would require changing at least the substrate and the noise rule.
> Moving from the symmetric chain to a non-symmetric affinity generator would also change the
> correlation/Lyapunov definition.

**Not authorized:** an S3 physics run, a hybrid, a v4 exception, or any claim about the crossed cell's
physical answer.

**The audit stopped correctly**, when the invariant-preserving cell failed to exist.

## 2. Changed invariants: ACCEPTED

| Invariant | Why it changes |
|---|---|
| **I-1 substrate** | The affinity lives on the 23-site ring. P^corr_CM lives on the symmetric chain K_b, and a tree has no cycle to carry affinity. |
| **I-4 noise rule** | The L0-1e FDT point is declared only in the symmetric class. Extending it is not declared. The rule Q = K + Kᵀ is a different rule. |
| **I-5 / X-c** | KΣ + ΣK = Q → KΣ + ΣKᵀ = Q is mathematically necessary, but it is still a change at the declared-object level. It is recorded, not silently generalized. |

## 3–8. Rulings on D-1 … D-6

| Item | Ruling |
|---|---|
| **D-1** | **Absence is not identity.** An invariant that is absent on one parent and supplied from another record is not "identical on the two sides". Importing it is a change unless a home record supplies the combined structure. This is recorded as the adjudicated interpretation; the frozen text is unchanged. |
| **D-2** | A third-record rule may be audited as a declared reading, but by itself it cannot satisfy invariant-preserving formulability. **R₂ is a valid declared reading, but an off-invariant construction.** |
| **D-3** | "Any accretive K" is a **declared extension** to non-symmetric accretive generators. R₂ may be evaluated algebraically on the ring as a report-only reading. |
| **D-4** | **Identity-forced is adjudicative only at the frozen invariants.** The R₂ chain Q = T(K + Kᵀ) ⇒ Σ = T·I ⇒ C = T·k is a **report-only conditional identity**. It does not trigger CELL-IDENTITY-FORCED. |
| **D-5** | READING-DEPENDENT refers to the frozen predicate, not to the report-only tags. Both readings give O-4, so it is **not assigned**. The notes (R₁ OPEN, R₂ CM-LOST) are still reported. |
| **D-6** | "As declared on the N side" means the actual L0-1e object and its covariance equation. The general Lyapunov form is correct, but it is a generalization, so it counts as a changed X-c/I-5 ingredient. No category error occurred. |

## 9. The R₁ and R₂ readings (strictly fenced)

**R₂.** Q = T(K + Kᵀ) gives Σ = T·I and C = T·k. So **P^corr_CM ≡ P^resp_CM** under this reading. It
is structurally trivial and gives **no independent reversal evidence.**

**R₁.** The ring with Q = 2T·I leaves the correlation-CM question genuinely open. But that
construction changes the substrate and extends the rule beyond its declared class, so **no execution
is authorized.**

## 10. What S3-0 establishes

| Comparison | Status |
|---|---|
| generator affinity → response-CM loss | on one substrate (the ring) |
| noise / detailed-balance variation → correlation-CM behavior | on another substrate (the chain) |
| generator affinity → P^corr_CM, with every other axis fixed | **not currently in the theory** |

> **The apparent response/correlation inversion remains confounded.**

This is a useful negative result. **Do not build the ring-plus-noise hybrid automatically.**

## 11. Relationship to the reversal diagnostic

- S3-0 does not assign the diagnostic's terminal.
- S-3 was preserved to remove the largest confound before the diagnostic was evaluated. **That confound
  cannot be removed without inventing a hybrid.**
- **The next step is therefore not S3-1.** It is a separate read-only evaluation of the
  already-pre-registered reversal diagnostic at the current recorded scope:
  `L0_STRUCTURAL_DIAGNOSTIC_REVERSAL_EVALUATION_01.md`.
- No new definitions, no new physics, and no v4 exception.

## 12. REV-0 procedure

Use the frozen criteria of `L0_STRUCTURAL_DIAGNOSTIC_REVERSAL_01.md` **without reinterpretation**.
Audit the entire accepted Level-0 and post-floor record through S3-0.

- **R-1:** list every certified ingredient → property and property → ingredient edge. An edge exists
  only where an accepted owner ruling meets the frozen certification rule.
- **R-2:** does 𝒢 contain a directed cycle? For each proposed cycle, identify every edge. Reject the
  cycle if any edge is merely:
  - an interpretation, analogy or "suggests" statement;
  - the FDT identity;
  - an F-5-type identity;
  - an off-invariant S3 construction.
- **R-3:** search only for an **explicit record-certified map** that exchanges two subgraphs and
  preserves their edges. Do not infer one from visual similarity.
- **R-4:** consume S3-0:
  - the crossed cell is not available at fixed invariants;
  - R₂'s off-invariant answer is identity-forced, so it is disqualified as reversal evidence;
  - R₁ stays open only in an undeclared hybrid.

  **Do not create an edge from either note.**
- **R-5:** apply the frozen outcomes mechanically:
  - a qualifying nontrivial reversal;
  - a qualifying self-duality;
  - or the frozen death criterion, **NOT SUPPORTED at recorded scope**.

  **No new outcome labels.**

## 13. Governance

**Do not assume the diagnostic dies** merely because the original file said no property → ingredient
edge existed at that earlier date.

**Scan the later accepted campaigns too:**
- the access/lift chain;
- SF/SFG;
- S5;
- S2;
- S3.

Include any later owner ruling that truly certified a property as constructing, or becoming a
required ingredient at, another level. If none did, say so *after* the audit. **That makes the death
criterion earned rather than inherited.**

## 14. Actions

**Create:**
- this ruling;
- the accepted banner in `S3_CROSSED_CELL_01.md`;
- the CURRENT_STATE update (S3-0 CLOSED / ACCEPTED).

**For REV-0:** pre-register nothing new, because the criteria are already frozen. Create only the
evaluation file, run the read-only graph audit, and **HARD STOP.**

**Not authorized:**
- an S3 physics run;
- a hybrid;
- S-4 or S-6;
- S5-WB or S5-OD;
- gravity, Π₀ or cosmology.
