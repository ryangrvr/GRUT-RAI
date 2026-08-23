# CLASS_C_PROVENANCE_LEDGER — repeated verification vs independent confirmation

> **Phase 11 artefact** (owner brief 2026-08-21). Classifies every decisive
> class-C-era result by its provenance. The distinction is load-bearing:
>
>     SAME_CODE_RERUN            !=  INDEPENDENT_IMPLEMENTATION  !=  EXTERNAL_REPRODUCTION
>     (regression check)             (different code, same math)    (outside reproduction)
>
> Multiple correlated AI/code checks are REPEATED VERIFICATION and must never
> be described as independent confirmation.

## Ledger

| result / guarantee | provenance | notes |
|---|---|---|
| Manifest contract: fail-closed require() semantics | SAME-CODE RERUN (gate selftest + solver refusal selftest + benchmark matrix row) | three executions of one implementation; no independent implementation exists yet |
| Dependency closure: 8 bypass mutants caught, clean source passes | SAME-CODE RERUN | mutants are data of one detector; a second detector would be needed for independence |
| Contamination audit verdict CLEAN (active surface) | SAME-CODE RERUN | single scanner; independent verification would require a differently-built scanner or human review |
| Proxy worldline spectrum (conformal BD geodesic): floored, non-super-Ohmic | SINGLE_IMPLEMENTATION (numeric) + FALSIFIED closed forms | the two hand-derived closed forms disagree with it; numerics converge under ε-refinement; NO independent implementation yet |
| Flat T=0 origin of ω³ (fold identity) | SAME-CODE RERUN + INDEPENDENT-CODE (fresh Simpson, rel.err 0.0e+00) | the one genuinely independently-coded confirmation to date |
| TT-graviton channel non-stationarity (>130% shape drift) | SINGLE_IMPLEMENTATION (mode-sum quadrature) | validated only against its own flat-limit pipeline; no independent implementation |
| [R_wl, R_IR] ≠ 0 | CLOSED FORM + SAME-CODE RERUN of the numeric integral | closed form is analytic; numeric confirms at 0.2% |
| D3a/D3b stationarity split (keystone map) | NUMERIC (embedding invariants) + ANALYTIC derivation | two methods agree |
| Everything older (rung1–rung12 register content) | see register tiers/sources | outside this ledger's scope |

## Rules going forward

1. Any result promoted toward the register must carry its provenance class from this table.
2. A class-C physics result requires AT MINIMUM one INDEPENDENT_IMPLEMENTATION agreement
   (Route B per the brief) plus one benchmark-limit agreement before banking.
3. EXTERNAL_REPRODUCTION (dispatch return) outranks everything and supersedes.
4. "The AI checked it twice" is always the first row's class, whatever the wording.
