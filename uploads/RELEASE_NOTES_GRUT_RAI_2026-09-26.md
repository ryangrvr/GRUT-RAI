# GRUT-RAI — public-record release (26 September 2026)

This release is the repository snapshot behind the GRUT program's
consolidated public record. It is the archival companion of the paper, not
a claim of its own.

**The paper.** *GRUT — Grand Responsive Universe Theory: Consolidated
Theory, Formal Architecture, Results, Limits, and Completion Program*,
D. Ryan Grover, 26 September 2026.
DOI: [10.5281/zenodo.22983638](https://doi.org/10.5281/zenodo.22983638)
(all versions of the theory record:
[10.5281/zenodo.19803663](https://doi.org/10.5281/zenodo.19803663)).
The paper's authoritative Markdown source, its conversion-only LaTeX/PDF
build, and its figure are in `uploads/`.

**This software record.** GRUT-RAI, all versions:
[10.5281/zenodo.18993689](https://doi.org/10.5281/zenodo.18993689). This
release carries its own version DOI, minted on deposit. GRUT-RAI is the
computational and provenance infrastructure of the program — instruments,
pre-registration charters, results, verdicts, and the dependency ledger.
It is not the physical theory, and it is not an authority that can make a
physical claim true.

**Source boundary.** The paper consolidates `master-w25bu9` through commit
`6abbf316` (26 September 2026, 02:54 UTC). The foundations record of the
unmerged `adjudicator-track` branch (tip `90218f5`) is archived byte-exact,
with SHA-256 sums, in `archive/adjudicator-track_90218f5/` (51 files), so
this snapshot contains every source the paper cites. Files committed after
the boundary are the manuscript, its build, this release's metadata, and
the archive itself; they add no computation and change no status.

## What this release contains, relative to the v5.0 Program Record (7 September 2026)

- **Program closure and reopening.** The program was formally closed on
  23 September 2026 (`GRUT_PROGRAM_CLOSURE_01.md`) and reopened by owner
  ruling on 25 September 2026 (`GRUT_PROGRAM_REOPEN_01.md`) as a
  theory-development effort. Reopening is not rehabilitation: every
  standing negative grading carries over, including zero GRUT-specific
  derived predictions and the twice-failed distinctive-theory
  adjudication.
- **The foundations record (24 September 2026).** GRUT Skeleton v02.1, the
  `u3_*` instruments with their results, the sealed T2 analytic ledger,
  the rebuilt on-shell coupling instrument (20/20; the ω⁷ result, graded
  within-class occupancy evidence), and the coupling adjudications,
  including the same-evening refutation of the "Cherenkov no-go". Archived
  under `archive/adjudicator-track_90218f5/`.
- **The dependency campaign (25 September 2026).** Twenty-four chartered
  forks — P-1 through P-6, D-1, S-1, G-1, G-2, GS-1, GR-1, CP-1, EQ-1,
  S4-1, FS-1, CC-1, U-1, RS-1, CA-1, SX-1, TT-1, C1-a, and C1-a2 — each
  with its charter committed before its run, its instrument and SHA-hashed
  result committed with its verdict, and an owner ruling. Seventeen failed
  frozen gates are preserved in ten red-register entries, none
  reinterpreted.
- **The first domain extension.** C1-a extends the core construction, in
  class, to finite stepped nonstationary dynamics (exact to 10⁻¹²), and
  C1-a2 certifies, at its stated scope and with its calibration disclosed,
  that no single spectral measure or Δt-only kernel packages the resulting
  two-time memory.
- **The synthesis and formal layer.** GRUT Working Theory 01, Theory Paper
  Working Drafts 01–02, and Formalizations 01–02 with their dated
  amendments.
- **The public record itself** (`uploads/`): the consolidated paper
  (Markdown and PDF), Figure 1, the LaTeX build (`uploads/build/`), the
  owner's draft preserved as received, the editorial changelog, and the
  Zenodo description. The edition passed an in-house multi-agent factual
  audit, a readability review by simulated outside readers, and a final
  three-pass fact-check of the complete text against the repository
  (~860 claims re-verified). All passes were AI-operated; none is external
  review.
- **Deposit metadata:** `.zenodo.json` (this software record) and
  `CITATION.cff` (with the paper as preferred citation).

## Scope statement

This is an in-house research record.

- No external peer review is claimed, and external review is deferred by
  owner direction (paper, §29.4).
- No experimental validation is claimed.
- No confirmed novel quantitative prediction is claimed; the GRUT-specific
  prediction ledger stands at zero.
- It is not a completed theory of everything.

Earlier releases in this lineage carried stronger claims that the current
record has demoted; where they conflict, the paper's scoped statements
govern (paper, §29). The June 2026 "GRUT ToE v4.0" deposit
(10.5281/zenodo.20783057) is withdrawn by its author, and nothing in it
should be cited as a result.

## How to verify a result

```
git clone https://github.com/ryangrvr/GRUT-RAI
cd GRUT-RAI && git checkout public-record-2026-09-26
cp -r calc /tmp/grut_calc && cd /tmp/grut_calc
python3 c1a2_packaging.py     # prints "7/7 gated checks passed"
```

The campaign instruments are pure Python 3 standard library and
deterministic or fixed-seed; run them from a copy, as shown, because each
writes its result file into the parent directory. The foundations
instruments are in `archive/adjudicator-track_90218f5/calc/`; six are pure
standard library, and the rest need `numpy` (two also `scipy`), with
Python 3.12 recorded as the tested environment. Paper §28 and Appendix G
give the full verification map, commit by commit.

## License and citation

- Source code: MIT License (`LICENSE`).
- The deposit and the paper: CC BY 4.0. © 2026 D. Ryan Grover.
- Cite the paper as: Grover, D. Ryan (2026). *GRUT — Grand Responsive
  Universe Theory: Consolidated Theory, Formal Architecture, Results,
  Limits, and Completion Program.* Zenodo.
  https://doi.org/10.5281/zenodo.22983638
- Cite this software as: Grover, D. Ryan (2026). *GRUT-RAI: research and
  provenance infrastructure for the GRUT program.* Zenodo.
  https://doi.org/10.5281/zenodo.18993689

AI agents (Claude, Anthropic) were used as computational, drafting, and
audit instruments under the author's direction; the author issued every
status ruling. If a future result changes a status, the change enters
through a new dated source boundary and a new record — this snapshot is
never silently rewritten.
