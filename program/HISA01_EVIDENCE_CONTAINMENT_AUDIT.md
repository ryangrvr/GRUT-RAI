# HISA-01 — Evidence Containment Audit

Mechanical citation/containment audit. Exact byte/string containment
only; no normalization, no fuzzy matching, no reconstruction.

## Integrity

- frozen package sha256 `a0fd00c03b16e9a232ffe4fd19b95138e972527fe747ad7f0c34498a834b8343` — UNCHANGED
- adjudication sha256 `a2968bae465fd2f93b6c0383f835738332746a82feb648dd8849643ff2197617` — UNCHANGED
- term occurrences examined: **62** (expected 62)

## Summary

| class | count |
|---|---|
| PASS_EXACT_SOURCE_CONTAINMENT | 18 |
| PASS_CONTEXT_CONTAINMENT | 1 |
| FAIL_SOURCE_NOT_CONTAINED | 19 |
| FAIL_CONTEXT_NOT_CONTAINED | 1 |
| FAIL_WRONG_EVIDENCE_SCOPE | 3 |
| FAIL_TERM_EVIDENCE_MISMATCH | 1 |
| FAIL_MISSING_EVIDENCE_REFERENCE | 0 |
| FAIL_MALFORMED_REFERENCE | 19 |
| REQUIRES_HUMAN_REVIEW | 0 |

## Failed occurrences

- **stmt 0** (`55`) term `gauge` — FAIL_MALFORMED_REFERENCE
  quote: (no quote)
  evidence_reference does not begin with an exact_source_line: or bounded_context_window: scope tag; no mechanically verifiable citation exists.
- **stmt 1** (`79`) term `Mori-Zwanzig` — FAIL_MALFORMED_REFERENCE
  quote: (no quote)
  evidence_reference does not begin with an exact_source_line: or bounded_context_window: scope tag; no mechanically verifiable citation exists.
- **stmt 1** (`79`) term `inner product` — FAIL_MALFORMED_REFERENCE
  quote: (no quote)
  evidence_reference does not begin with an exact_source_line: or bounded_context_window: scope tag; no mechanically verifiable citation exists.
- **stmt 1** (`79`) term `cutoff` — FAIL_MALFORMED_REFERENCE
  quote: (no quote)
  evidence_reference does not begin with an exact_source_line: or bounded_context_window: scope tag; no mechanically verifiable citation exists.
- **stmt 1** (`79`) term `correlator` — FAIL_SOURCE_NOT_CONTAINED
  quote: the FREE bath correlator (super-Ohmic, collisionless-AT-FREE-LEVEL) ... the TRANSPORT SELF-ENERGY Sigma controlling G_R = 1/(G0^-1 - Sigma)
  Quote does not occur verbatim in the cited frozen exact_source_line.
- **stmt 2** (`269`) term `GAUGE` — FAIL_SOURCE_NOT_CONTAINED
  quote: INTERROGATION RESULT 2026-08-02 ... VERDICT = CHOSEN, unanimous. THE PHYSICS IN ONE LINE: diffeomorphism invariance gets you to TRANSVERSE
  Quote does not occur verbatim in the cited frozen exact_source_line.
- **stmt 2** (`269`) term `response kernel` — FAIL_TERM_EVIDENCE_MISMATCH
  quote: K^R = alpha*chi(omega)*P^TT, with the projector P^TT chosen (not derived)
  Quote is contained in the frozen context window, but neither quote nor window mentions the candidate term 'response kernel'.
- **stmt 4** (`201`) term `projector` — FAIL_CONTEXT_NOT_CONTAINED
  quote: K^R = alpha*chi*P^TT ... Structural obstruction (projector-orthogonality PRIMARY / Ward / UV-IR no-RG-protection)
  Quote does not occur verbatim in the frozen context window for term 'projector'.
- **stmt 5** (`274`) term `projection P` — FAIL_SOURCE_NOT_CONTAINED
  quote: B system/bath partition · C the Mori-Zwanzig projection P
  Quote does not occur verbatim in the cited frozen exact_source_line.
- **stmt 5** (`274`) term `Mori-Zwanzig` — FAIL_SOURCE_NOT_CONTAINED
  quote: B system/bath partition · C the Mori-Zwanzig projection P
  Quote does not occur verbatim in the cited frozen exact_source_line.
- **stmt 5** (`274`) term `system/bath` — FAIL_SOURCE_NOT_CONTAINED
  quote: B system/bath partition
  Quote does not occur verbatim in the cited frozen exact_source_line.
- **stmt 6** (`275`) term `cutoff` — FAIL_SOURCE_NOT_CONTAINED
  quote: F cutoff/separation scale
  Quote does not occur verbatim in the cited frozen exact_source_line.
- **stmt 6** (`275`) term `inner product` — FAIL_SOURCE_NOT_CONTAINED
  quote: D inner-product choice
  Quote does not occur verbatim in the cited frozen exact_source_line.
- **stmt 7** (`22`) term `system/bath` — FAIL_SOURCE_NOT_CONTAINED
  quote: declared inputs: system/bath split ... STANCE, not derivation
  Quote does not occur verbatim in the cited frozen exact_source_line.
- **stmt 7** (`22`) term `GAUGE` — FAIL_MALFORMED_REFERENCE
  quote: (no quote)
  evidence_reference does not begin with an exact_source_line: or bounded_context_window: scope tag; no mechanically verifiable citation exists.
- **stmt 7** (`22`) term `correlator` — FAIL_MALFORMED_REFERENCE
  quote: (no quote)
  evidence_reference does not begin with an exact_source_line: or bounded_context_window: scope tag; no mechanically verifiable citation exists.
- **stmt 8** (`1637`) term `gauge` — FAIL_MALFORMED_REFERENCE
  quote: (no quote)
  evidence_reference does not begin with an exact_source_line: or bounded_context_window: scope tag; no mechanically verifiable citation exists.
- **stmt 9** (`87`) term `susceptibility` — FAIL_SOURCE_NOT_CONTAINED
  quote: if the vacuum susceptibility contains a second dynamical scale (e.g. J~omega^3/(1+omega^2 tau^2) ...), a second slow pole appears and short-memory breaks
  Quote does not occur verbatim in the cited frozen exact_source_line.
- **stmt 10** (`18`) term `KUBO` — FAIL_SOURCE_NOT_CONTAINED
  quote: Mori-Zwanzig projection for a quantum system conventionally uses the KUBO-MORI (canonical) inner product, and the Kubo correlation function carries
  Quote does not occur verbatim in the cited frozen exact_source_line.
- **stmt 10** (`18`) term `Mori-Zwanzig` — FAIL_MALFORMED_REFERENCE
  quote: (no quote)
  evidence_reference does not begin with an exact_source_line: or bounded_context_window: scope tag; no mechanically verifiable citation exists.
- **stmt 11** (`180`) term `projector` — FAIL_MALFORMED_REFERENCE
  quote: (no quote)
  evidence_reference does not begin with an exact_source_line: or bounded_context_window: scope tag; no mechanically verifiable citation exists.
- **stmt 11** (`180`) term `gauge` — FAIL_MALFORMED_REFERENCE
  quote: (no quote)
  evidence_reference does not begin with an exact_source_line: or bounded_context_window: scope tag; no mechanically verifiable citation exists.
- **stmt 11** (`180`) term `Green's function` — FAIL_MALFORMED_REFERENCE
  quote: (no quote)
  evidence_reference does not begin with an exact_source_line: or bounded_context_window: scope tag; no mechanically verifiable citation exists.
- **stmt 12** (`36`) term `gauge` — FAIL_WRONG_EVIDENCE_SCOPE
  quote: inserted the gauge image WITHOUT the bath projector the loop actually applies
  Quote occurs in the frozen bounded_context_window but NOT in the cited exact_source_line; a context quote may not be presented as exact-line evidence.
- **stmt 13** (`216`) term `gauge` — FAIL_SOURCE_NOT_CONTAINED
  quote: gauge-transforming the internal line moves no TT amplitude ... does NOT establish that the TT-bath DECLARATION itself is the unique admissible gauge choice -- t
  Quote does not occur verbatim in the cited frozen exact_source_line.
- **stmt 14** (`223`) term `projection P` — FAIL_MALFORMED_REFERENCE
  quote: (no quote)
  evidence_reference does not begin with an exact_source_line: or bounded_context_window: scope tag; no mechanically verifiable citation exists.
- **stmt 14** (`223`) term `system/bath` — FAIL_MALFORMED_REFERENCE
  quote: (no quote)
  evidence_reference does not begin with an exact_source_line: or bounded_context_window: scope tag; no mechanically verifiable citation exists.
- **stmt 15** (`639`) term `response function` — FAIL_MALFORMED_REFERENCE
  quote: (no quote)
  evidence_reference does not begin with an exact_source_line: or bounded_context_window: scope tag; no mechanically verifiable citation exists.
- **stmt 17** (`660`) term `coarse-grain` — FAIL_WRONG_EVIDENCE_SCOPE
  quote: ENUMERATE the universality classes chi(omega,k) can occupy
  Quote occurs in the frozen bounded_context_window but NOT in the cited exact_source_line; a context quote may not be presented as exact-line evidence.
- **stmt 19** (`28`) term `gauge` — FAIL_SOURCE_NOT_CONTAINED
  quote: the synchronous-gauge computation reproduces the gauge-invariant content of the gauge-unfixed computation ... the difference of the two computations is the orbi
  Quote does not occur verbatim in the cited frozen exact_source_line.
- **stmt 20** (`513`) term `Mori-Zwanzig` — FAIL_MALFORMED_REFERENCE
  quote: (no quote)
  evidence_reference does not begin with an exact_source_line: or bounded_context_window: scope tag; no mechanically verifiable citation exists.
- **stmt 21** (`559`) term `Mori-Zwanzig` — FAIL_SOURCE_NOT_CONTAINED
  quote: rung3's "Mori-Zwanzig kernel" does not denote a unique object, and the two candidates answer oppositely
  Quote does not occur verbatim in the cited frozen exact_source_line.
- **stmt 22** (`250`) term `gauge` — FAIL_MALFORMED_REFERENCE
  quote: (no quote)
  evidence_reference does not begin with an exact_source_line: or bounded_context_window: scope tag; no mechanically verifiable citation exists.
- **stmt 22** (`250`) term `correlator` — FAIL_MALFORMED_REFERENCE
  quote: (no quote)
  evidence_reference does not begin with an exact_source_line: or bounded_context_window: scope tag; no mechanically verifiable citation exists.
- **stmt 23** (`351`) term `coarse-grain` — FAIL_SOURCE_NOT_CONTAINED
  quote: renormalization/coarse-graining is an information-projection' with 'Wilsonian coarse-graining as information loss
  Quote does not occur verbatim in the cited frozen exact_source_line.
- **stmt 24** (`28`) term `gauge` — FAIL_WRONG_EVIDENCE_SCOPE
  quote: the D4-C test BYPASSED the projector that defines the declared bath. Routes A and B show that projector annihilates the orbit direction exactly
  Quote occurs in the frozen bounded_context_window but NOT in the cited exact_source_line; a context quote may not be presented as exact-line evidence.
- **stmt 25** (`210`) term `gauge` — FAIL_SOURCE_NOT_CONTAINED
  quote: gauge-transforming the internal line moves no TT amplitude ... NOT D3(iii)
  Quote does not occur verbatim in the cited frozen exact_source_line.
- **stmt 26** (`43`) term `gauge` — FAIL_SOURCE_NOT_CONTAINED
  quote: the D4-C test BYPASSED the projector ... projector annihilates the orbit direction exactly
  Quote does not occur verbatim in the cited frozen exact_source_line.
- **stmt 27** (`109`) term `Mori-Zwanzig` — FAIL_SOURCE_NOT_CONTAINED
  quote: Mori-Zwanzig: choosing a projector P IS the partition (coarse-graining -> split), while Zurek's approach assumes factorization
  Quote does not occur verbatim in the cited frozen exact_source_line.
- **stmt 28** (`76`) term `projector` — FAIL_SOURCE_NOT_CONTAINED
  quote: Mori-Zwanzig: choosing a projector P IS the partition (coarse-graining -> split)
  Quote does not occur in the cited frozen exact_source_line (it occurs in some other frozen record; that does not validate the citation).
- **stmt 28** (`76`) term `Mori-Zwanzig` — FAIL_MALFORMED_REFERENCE
  quote: (no quote)
  evidence_reference does not begin with an exact_source_line: or bounded_context_window: scope tag; no mechanically verifiable citation exists.
- **stmt 29** (`530`) term `inner product` — FAIL_SOURCE_NOT_CONTAINED
  quote: on the CONVENTIONAL Mori-Zwanzig inner product there is no ladder to inherit, and the friction kernel does not contain T at all
  Quote does not occur verbatim in the cited frozen exact_source_line.
- **stmt 29** (`530`) term `Mori-Zwanzig` — FAIL_MALFORMED_REFERENCE
  quote: (no quote)
  evidence_reference does not begin with an exact_source_line: or bounded_context_window: scope tag; no mechanically verifiable citation exists.
