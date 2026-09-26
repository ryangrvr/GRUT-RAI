# Archived foundations record: `adjudicator-track` @ `90218f5`

This directory is a byte-exact copy of every file that exists on the
repository branch `adjudicator-track` (tip
`90218f53fff6a659a6c65dcbb1dfc0606696b6c1`, 24 September 2026, 23:19:57 UTC−5)
and is absent from the publication branch `master-w25bu9`. There are 51
files in total.

**Why it exists.** The public record
(`uploads/GRUT_Consolidated_Theory_PUBLIC_RECORD.md`) relies on these files
for its Layer-I foundations (Section 4) and for the ω⁷ coupling result
(Section 17). A Zenodo snapshot of `master-w25bu9` would otherwise leave
them out. The branch itself is not merged; its history remains on the
remote.

**Integrity.**
- Every file was extracted with `git show origin/adjudicator-track:<path>`.
- Each file's git blob hash was then checked against the branch
  (`git hash-object` = `git rev-parse origin/adjudicator-track:<path>`).
  All 51 matched.
- `SHA256SUMS` lists the SHA-256 of every archived file.
- Paths below this directory are the original repository paths.

**Nothing here was edited.** Several of these files are internally stale
or carry known defects, and they are archived exactly as they were
committed. The public record discloses the defects that matter, among
them:
- the Skeleton §3.1 and §5 lines that predate its own repairs;
- the spectral-match result JSON that still reads t⁻³;
- the coarse-graining-universality result at 2/7.

**Reproduction.** Most `calc/u3_*.py` instruments here need `numpy`, and
two also need `scipy`. The recorded environment is
`"python": "3.12 (pinned; 3.15 numpy broken)"`. They write their results
into `calc/`. Six are pure stdlib:
- `u3_spectrum`
- `u3_realization_dimension`
- `u3_geometry_spectral_selection`
- `u3_kernel_minimality`
- `u3_kms_spectral_constraint`
- `u3_scale_origin`

Run them from a copy, not in place, to avoid overwriting the archived
results.
