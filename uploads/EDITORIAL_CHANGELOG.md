# Editorial changelog — public-record edition of the Consolidated Theory

- **Input:** `GRUT_Consolidated_Theory_2026-09-25_DRAFT_as_received.md`
  (the owner-supplied draft, preserved verbatim).
- **Output:** `GRUT_Consolidated_Theory_PUBLIC_RECORD.md`.
- **Rule:** this edit adds no physics and moves no status.

Every factual change below was checked against the repository before it
was made, as follows:

- commit hashes were verified with `git rev-parse` or `git log`;
- the GR-1 diagnostic digits were checked in `GR1_GRAVITY_RESULT.json`;
- the continuum-origin checks were checked in
  `U3_CONTINUUM_ORIGIN_RESULT.json` on `adjudicator-track` @ `affdf52`;
- all other numbers come from the frozen verdicts and commit records.

## Corrections of fact

1. **CP-1 and CC-1 were conflated (§13.1).**
   - The draft attributed the four-parameter coupling family, and the
     finding that the +4 locus is a plane, to CC-1. Both belong to CP-1.
   - CC-1's actual result is different: a non-conserved coupling passes
     every earned constant-level selector, and conservation follows only
     for a supplied massless probe (exchange residues −10.6 and −17.8).
   - The two are now attributed separately.
2. **ρ in the datum is a state, not "spectral/influence content" (§20).**
   The formalization defines 𝔇 = (M, 𝔞, ρ, ι) with ρ a state on M's
   algebra.
3. **The continuum-origin record was misdescribed (§4.2).**
   - The draft said "four principal branches C1–C4" and "6/6". The artifact
     actually has six checks, (i)–(vi).
   - Check (v) is universality. Check (vi) is an order-of-magnitude
     viability estimate, not a derivation.
   - For d = 1 the kernel is recurrent; the t^(−d/2) law holds for d ≥ 2.
     The measured d = 3 slope is −1.36 against −1.5 in theory.
   - The labels were renamed (i)–(vi) because the draft's "C1–C4" collided
     with completion problems C1–C7 and with C1-a.
4. **Undisclosed provenance (header, §4, §28, Appendix G).**
   - The Layer-I results come from branch `adjudicator-track` (commits
     `affdf52` and `90218f5`), not from the stated source branch.
   - This is now disclosed explicitly.
5. **~~A nonexistent branch was cited.~~ WITHDRAWN (correction, 26
   September 2026).** This item originally said the draft's "older `v4`
   branch" does not exist, and the reference was removed. That was wrong.
   The check looked only at the branches fetched into the editing
   environment. The public repository has `v4`, `main`, `physics-final`,
   `v2`, `v1-retired`, and `testingi-rrt`. The draft's disclosure was
   accurate, and the public-record edition restores it.
6. **The EQ-1, P-6, and RS-1 red-register descriptions were imprecise
   (§23).** They were replaced with the recorded content: the measured
   value, the frozen threshold, and the labeled diagnostic.
7. **The §6.1 list of non-selectors was overstated.** Unsourced items
   ("covariance/Ward identities", "equivalence-principle-type constraints")
   were removed. The list is now what P-2 established: KMS, FDT,
   stationarity, and single-pole memory are states inside the cone.
8. **The ω⁷ convention caveat was missing (§17).** Added: "in the
   program's declared convention; absolute exponents never compared across
   conventions."

## Omissions filled (required for an honest public record)

9. **The two C1-a red gates were missing from the red register.** L-B(a)
   (0.0498 against 0.1) and L-B(b) (0.0494 against 0.05) are the owner's
   "permanent reds." They have been added, with an explicit note that C1-a2
   did not turn them green.
10. **Standing negative gradings added (§29, the glance table, §26, §31,
    §32).** The owner's program-reopening ruling says these still stand:
    - GRUT-specific derived predictions stand at zero, and the signature
      audit reads EMPTY;
    - the distinctive-theory adjudication of 4–5 September 2026 failed as
      scoped;
    - the finite single-pole founding bet is negated (de Sitter forces
      scale-free memory);
    - the earlier no-go results stand.
11. **The completion criterion was updated to the three certified statuses
    (§24).** These are derived section, irreducible primitive, and domain
    datum, per Formalization 01 Amendment 01. The draft listed only two
    routes.
12. **The formalization's findings were added (§20).** These are:
    - the R1–R7 relations;
    - "one theory on the core" as a checked property, not a theorem;
    - the domain extension from C1-a;
    - the earned-carved base 𝕀_adm and the refuted sections;
    - termination points as content.
13. **The EQ-1 and CP-1 links in the gravity chain were missing.** They
    have been added as a reduction table in §12.
14. **C1-a's numerical results were added (§5.1).** These are: the
    reduction exact to 1e-12, continuity 1.9968 and 7.8e-16, and the Gram
    PSD result with its tamper detection.
15. **The C1-a2 calibration disclosure was added (§5.2).** The C1-a2
    charter itself states it.
16. **The T3 anchor was described as standard QFT, not a GRUT claim
    (§24).**
17. **The irreversibility-origin battery score (3/4) was added**, together
    with the existence/direction split (§4.3).
18. **Appendix G was added:** a campaign index giving each fork's question,
    verdict, battery score, and commit.
19. **The GRUT concept DOI 10.5281/zenodo.19803663 was added** to the
    header and the citation, as recorded in the program-reopening ruling.
20. **An AI-agent role disclosure and a no-outside-human-review statement
    were added.**

## Editorial

- Section numbering was repaired: "28.0" before "28" was merged, and
  "30.5" was renamed 30.1.
- Numbers were added wherever the draft said "approximately" or "a
  measurable difference" without a value.
- Dates now separate the record date (25 September 2026, the source
  boundary) from the date prepared for deposit (26 September 2026).
- The manuscript's own later commit is declared as adding no physics.
