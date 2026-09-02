# TIER-4 FORMAL ACCEPTANCE / BANK PRE-SCREEN

**Date:** 2026-09-01 · **Instrument:** `wall_kr_t4_bank_and_cell.py` ·
**Machine-readable:** `WALL_KR_T4_BANK_AND_CELL_RESULT.json` ·
**Battery: 35/35 (shared with Part II).** · **No frozen scientific
artifact modified; register byte-identical; auditor suite green.**

## STATUS: **T4-BANK-A — FORMALLY BANKABLE AS WRITTEN**

The frozen Tier-4 result (artifact `d916ef32…`, commits
`2d3f514`/`41811ff`) can move from *computed-and-reported / NOT
BANKED* to *BANKABLE* with every condition, scope limit, and unresolved
quantity preserved exactly. **Scientific content: UNCHANGED.** The bank
MOVE itself remains the owner's act — this record is the adversarial
pre-screen; the relay is yours. The delta is **PROPOSED ONLY**
(`WALL_KR_T4_BANK_DELTA_PROPOSED.json`); `provenance/claims.json`
was not touched.

## SCOPE, VERIFIED AGAINST THE FROZEN ARTIFACT (not broadened)

TT scope with the Ward Class-B residual **excluded by construction, not
repaired**; noise fence intact (α = −2 never consumed); ε_H validity
rule exercised at all three levels in the frozen record (CONTROLLED /
explicit BOUNDARY flag / REJECTED extrapolation control) — ω ≪ H is
refused, not interpreted; local slot recorded UNDETERMINED; k → 0 and
isotropy carried as executed T3 gates; no J(ω) input anywhere. The
frozen validation record carries 33 checks, all passing (the terminal
"34/34" included the final artifact-rehash gate, which necessarily
post-dates the artifact write — bookkeeping, not validation).

## THE CONDITIONALITY TABLE (banked exactly as stated)

| claim | status | condition |
|---|---|---|
| branch point at ω = 0 + real-axis cut | **UNCONDITIONAL** | none |
| frozen absorptive coefficients; H¹ = 0 | **UNCONDITIONAL/FROZEN** | none |
| retarded analyticity of the +iπ completion | **UNCONDITIONAL** | none (review Cauchy-verified) |
| no additional real-axis zero of the resummed denominator | CONDITIONAL | c = 0 slice, κ = 0.1, μ = 1, CONTROLLED band |
| ω = 0 graviton pole survives | CONDITIONAL | iff c0 = 0 (D5; later certified c0 = 0 at H⁰ under Option β — carried in this wrapper, bytes preserved) |
| resummed/first-order agreement | CONDITIONAL | |λ| ≪ 1 |
| anything at ω ≲ H | OUT OF SCOPE | refused by the evaluator |

**Upgrade control:** a conditions-stripped wrapper text *fails* the same
qualifier-presence gate the frozen artifact passes — "no zero on the
reference slice" cannot be silently upgraded to "no poles."

## LATER CERTIFIED RESULTS (wrapper only — historical bytes preserved)

H⁰: c0 = 0, c2 = 0 (exact, structural); c4 represented through the
RG-invariant Λ_R (symbolic by owner ruling). H²: c0′, c2′ unresolved;
IR fork gated by owner decision. Gate-E-A and NOISE-A were established
separately and afterward — cited as corroboration, never retro-fitted.
The Tier-4 artifact hash is unchanged.

## PROPOSED BANK DELTA (NOT EXECUTED)

Node `kr_contract_retarded_tier4`: W-0 → BANKED as a scoped computed
record; **ledger_delta 0**; conditions carried verbatim; unresolved
dependencies listed (Λ_R; c0′/c2′; D4 at contract scope; the
certificate-vs-manifest face adjudication). Requires owner/overseer
relay per the map's bank procedure.
