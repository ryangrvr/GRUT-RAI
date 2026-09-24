# CAPABILITY_CONTRACT_01 — the unified capability-contract rule (RRP Stage 3)

**Date:** 2026-09-23. **Status:** codification of existing enforced practice into one rule —
not a new invention. Sources codified: the freeze stopping rule (`GRUT_PROGRAM_FREEZE.md` §1,
the why-needed gate), instrument discipline (`program/REALITY_PROGRAM.md` §4: mutation
batteries, plants-that-must-detect, negative controls; RC-05's frozen calibration protocol),
and the cannot-establish face-statement pattern (`REALITY_AUDIT_CHARTER.md` §7;
`RESULTS_auditor.md`; the RAI capability certifications).

## The rule

No computational or methodological module is built, and no existing module is extended, in
the RRP without a contract stating, before construction:

```
WHY NEEDED               — the registered question that cannot be answered without it
WHAT QUESTION IT ENABLES — stated so that failure to enable it is checkable afterwards
INPUTS                   — everything it consumes, with provenance classes
OUTPUTS                  — everything it produces, with the vocabulary that grades them
VALIDATION               — how it is shown to work BEFORE use (calibration cases; a
                           mutation/plant battery where numeric; two-sided: it must be able
                           to fail, and a legitimate negative must be recognizable)
FAILURE MODES            — the known ways it can mislead, written down in advance
DEPENDENCIES             — modules, data, and external tools it relies on
WHAT IT CANNOT ESTABLISH — stated in the module's own output, not left implied
```

**Binding corollaries:** needed capability ≠ evidence — building a tool proves nothing about
any theory; a module that cannot be validated under its contract stops its question rather
than shipping unvalidated; contracts are written before construction and frozen with the
module; a module reused for a new question gets a contract addendum, not silent reuse.

## Contract instance 1 — `rrp/tools/corpus_validate.py`

- WHY NEEDED: Stage 2 produces ten machine-readable domain records from parallel builders;
  the Stage-4 extraction may only consume schema-conformant, provenance-classed entries.
  Hand-checking ten JSON files repeatedly is the defect-prone path the archive's
  emitted-never-typed rule exists to prevent.
- WHAT IT ENABLES: mechanical admission of corpus records into Stage 4; mechanical counts
  (VERIFIED vs TO-VERIFY per record) that can be quoted without hand-typing.
- INPUTS: `rrp/corpus/domains/*.json` (data, untrusted), `CORPUS_SCHEMA.md` field list
  (mirrored as constants).
- OUTPUTS: per-file PASS/FAIL with named violations; per-file entry counts by provenance and
  verification class. Nothing else.
- VALIDATION: run against the known-good QM pilot (must PASS) and against three deliberate
  mutants (missing field; illegal provenance enum; entry that asserts a requirement via
  "must"/"required" in a corpus claim) — all three must FAIL. Battery run at first use and
  after any edit.
- FAILURE MODES: string-level requirement-language detection can false-positive on quoted
  material (reported as WARN, not FAIL); schema drift if CORPUS_SCHEMA.md changes without
  updating the mirrored constants (mitigation: version string checked).
- DEPENDENCIES: Python 3 stdlib only.
- WHAT IT CANNOT ESTABLISH: truth of any entry; adequacy of any citation; completeness of
  any record. It validates form and counts, never physics — a wrong-but-well-formed entry
  passes, and this line travels in its output.
