# CORPUS_SCHEMA v0 — machine-readable established-physics corpus (RRP Stage 1)

One JSON file per domain under `rrp/corpus/domains/`. The corpus is the inventory of
"structures physics demonstrably has"; it is data, never argument. Any rendered counts or
summaries are emitted from the JSON, never hand-typed (`HOW_TO_VERIFY.md` discipline).

## Per-domain record fields (all required; empty allowed, absence is content)

`domain` · `phenomena` · `formalism` · `primitives` · `derived_objects` · `empirical_inputs`
· `constants` · `symmetries` · `limits` · `known_connections` · `known_disconnects` ·
`open_problems` · `observables` · `alternative_formulations` · `domain_of_validity` ·
`notes`

Each entry inside a field is an object:

```json
{
  "claim": "<one statement>",
  "provenance": "OBSERVED | COMMUNITY-DERIVED | PROGRAM-RESULT | ABSENCE",
  "verification": "VERIFIED | TO-VERIFY",
  "source": "<citation, archive ref:path, or the named verification pass>",
  "caveat": "<scope/strength qualifier, if any>"
}
```

## Rules

1. **Provenance classes are firewalled.** OBSERVED = experimental fact, citable.
   COMMUNITY-DERIVED = standard theory, citable. PROGRAM-RESULT = in-house, unreviewed,
   carries its recorded limitations, and can never upgrade to the other classes by
   repetition. ABSENCE = a recorded not-observed / not-derived — first-class content
   (negated edges, empty tiers).
2. **No fabricated bibliography.** An entry without a checked citation carries
   `verification: TO-VERIFY` and names what would verify it. Stage 2 converts or deletes;
   TO-VERIFY entries may not be load-bearing for any requirement claim.
3. **Correspondence edges live in `known_connections`/`known_disconnects`** and will carry
   the seven-class typing (IDENTITY · MATHEMATICAL_ANALOGY · STRUCTURAL_ISOMORPHISM ·
   LIMIT_RELATION · EFFECTIVE_CORRESPONDENCE · EMPIRICAL_CORRELATION · VOCABULARY_ONLY ·
   UNRESOLVED) from Stage 3 on; until then edges carry the `REALITY_PICTURE_01` vocabulary
   they inherit.
4. **Requirement relativity.** Nothing in a corpus record asserts that a structure is
   *required* — extraction is Stage 4's job, under M/D/P/O stamps. The corpus only records
   what is there, at what strength, on whose authority.
5. **PILOT grade** (Stage 1): records marked `"grade": "PILOT"` bank nothing and exist to be
   attacked; the schema itself is frozen only at the Stage-2 owner gate.
