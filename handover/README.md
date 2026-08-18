# Hand-overs for Wave 7 — prepared, unwired, not executed

Two artifacts live here. **Neither is connected to anything**, by design:

- `zenodo_draft.json` — a DRAFT of the metadata a future deposit would carry. It is **not**
  `.zenodo.json` and must not be renamed to that path by anyone but the owner, at the moment of
  deposit. The repository's live `.zenodo.json` still carries the prior lineage's v2.2.0 metadata
  ("candidate Theory of Everything", "Zero free parameters in the gravitational predictive core"),
  and the Zenodo hook is **server-side**: creating a tag or a GitHub release would publish that
  stale text as a new deposit automatically. That is why no tag, no release, and no deposit has
  been created, and why this draft sits under a different filename.
- `SUPERSEDING_NOTE.md` — the one-page note to deposit as a new version under the prior work's
  **concept** DOI, so that every existing citation resolves forward to the correction.

**The owner performs both acts.** Nothing here fires on its own; nothing here has been sent,
tagged, released, or deposited.
