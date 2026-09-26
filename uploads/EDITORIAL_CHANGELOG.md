# Editorial changelog — public-record edition of the Consolidated Theory

- **Input:** `GRUT_Consolidated_Theory_2026-09-25_DRAFT_as_received.md`
  (the owner-supplied draft of 25 September 2026, preserved verbatim).
- **Output:** `GRUT_Consolidated_Theory_PUBLIC_RECORD.md` (26 September
  2026) and the PDF typeset from it.
- **Rule:** editing adds no physics and moves no status. No gate was
  re-graded, no input was promoted, and no red gate was turned green.

The edition was produced in two passes. Pass 1 corrected the owner's draft
against the repository. Pass 2 is a full revision: it applies every finding
of an in-house factual audit (each flagged discrepancy re-checked by an
adversarial agent), the findings of a readability review by three simulated
outside readers (a physicist, a generalist, and a referee), and five
research packs that re-verified the foundations record, the definitions,
the methods, the release history, and the references against the
repository. A final fact-check of the complete text followed. All of these
passes were AI-operated and in-house; none is external review.

---

## Pass 1 — corrections to the owner's draft

1. **CP-1 and CC-1 were conflated (§13.1).** The four-parameter coupling
   family and the finding that the +4 locus is a plane belong to CP-1, not
   CC-1. CC-1's result is that a non-conserved coupling passes every earned
   constant-level selector, and conservation follows only for a supplied
   massless probe. The two are attributed separately.
2. **ρ in the datum is a state (§20),** not "spectral/influence content".
   (Pass 2 writes it ϱ to keep ρ for the spectral measure.)
3. **The continuum-origin record was misdescribed (§4.2).** It has six
   checks, (i)–(vi), not "four principal branches". Check (vi) is an
   order-of-magnitude estimate. *Pass 1 also wrote that the $t^{-d/2}$ law
   holds only for d ≥ 2 and that d = 1 is recurrent; that reading was wrong
   and is corrected in pass 2 (item 12).*
4. **Undisclosed provenance.** The Layer-I results come from branch
   `adjudicator-track` (`affdf52`, `90218f5`); this is disclosed, and the
   branch's files are now archived in `archive/adjudicator-track_90218f5/`.
5. **~~A nonexistent branch was cited.~~ WITHDRAWN.** Pass 1 wrongly said
   the draft's `v4` branch does not exist, having checked only locally
   fetched branches. The public repository has `v4`, `main`,
   `physics-final`, `v2`, `v1-retired`, and `testingi-rrt`; the disclosure
   is restored.
6. **Red-register descriptions** for EQ-1, P-6, and RS-1 were replaced with
   the recorded measured value, threshold, and diagnostic.
7. **Unsourced non-selectors** in §6.1 were removed.
8. **The ω⁷ convention caveat** was added.
9. **Omissions filled:** the two permanent C1-a reds; the standing negative
   gradings; the three certified closure statuses; the formalization's
   findings; the EQ-1 and CP-1 links; C1-a's numbers; C1-a2's calibration
   disclosure; the T3 anchor's status; the campaign index; the concept DOI;
   the AI-role and no-outside-review disclosures.

## Pass 2 — full revision

### Corrections of fact (audit and critic findings)

10. **Source boundary (header, §28).** `master` is not a separate line: it
    is the base of the publication branch, which forks from it at
    `a2dcb02`. The RRP records are in the source history and enter only by
    adjudication.
11. **The finite reduction formula (§4.1, Appendix A).** The draft's
    $\dot q=-\int K_R\,q+\text{drive}$ had the wrong sign and omitted the
    instantaneous term. The instruments implement
    $\dot q=-K_{SS}q+\int k\,q+\eta$ with $k(\tau)=\sum u_l^2e^{-\lambda_l\tau}$.
    The notation note reconciles the older form.
12. **Continuum origin (§4.2).** The checks were run on conservative
    (class (b)) lattices, whose kernels oscillate, not on the completely
    monotone class. The recorded slopes show $t^{-d/2}$ in all three
    dimensions, with the d = 1 fit window below the finite-size floor.
    Checks (iv) and (vi) are asserted in code; check (i) reflects finite
    propagation speed.
13. **Irreversibility (§4.3).** The positive result comes from the
    infinite-bath battery (4/4), which the draft never cited; the
    irreversibility-origin battery (3/4) is the negative half.
14. **"Both directions were checked (P1 and P2)"** was wrong: P1 and P2 are
    the necessity direction; the constructive converse is P3, P4, E4a.
15. **Grades brought to the binding vocabulary.** Formalization 01 §0 lists
    exactly five grades, including [UNDEFINED]; other labels are
    distinguished from it (§1). Continuum emergence and irreversibility are
    [FAMILY-FACT], not DERIVED-IN-CLASS (§31). The retained-sector class is
    conditionally DERIVED-IN-CLASS, not CONSTRAINED. Spectral *content* is
    SUPPLIED, while recovery of ρ is CONSTRAINED.
16. **Scope qualifiers restored** where the draft or pass 1 dropped them:
    the abstract's geometry sentence; C1-a and C1-a2 "in class"; the
    stationarity measurement (grid-scoped, per Correction 01) and the
    transport ruling (tested family only); P-1 (toy class, one testbed per
    regime); D-1 (Gaussian class, factorized state); S-1 (branch-level
    counting; a null over three functionals, not all); G-1 (in class, at
    these scales); GS-1 (selected *in class*; boundary access leaves the
    interior CONSTRAINED); U-1 (derived conditional on the supplied probe);
    §32 (in class; "certified at the stated scope", not "provably").
17. **Numbers corrected:** probe-routed observables agree to 6.3×10⁻¹⁵ (not
    4.5×10⁻¹⁵); single-site heat data agree to 4.4×10⁻¹⁶ (not 2.2×10⁻¹⁶); the
    inhomogeneous deformation is 0.180 (not 0.181); the U-1 figures 0.13 and
    9×10⁻¹⁶ are the soft-emission gauge variation, not the discriminator
    (0.049 against 1.8×10⁻¹⁴); +3.999 is measured on the cancelled branch,
    not on each branch.
18. **The ω⁷ account (§17).** The ±0.15 is the instrument's tolerance; the
    sealed ledger's figure is 7.00 ± 0.05. The instrument's pre-registration
    was committed with its result; its coefficient ratio is against its own
    asymptote; several sealed gates were never implemented; two-sided
    blindness holds only for an earlier run; both sides were AI-operated
    roles. The Cherenkov episode and the unimplemented gates are stated.
19. **Universal reach (§21, §31)** is supplied; *clock universality* is what
    U-1 derives given reach.
20. **"Each attack reduced or refuted" (§12)** was wrong; several rows record
    derived-in-class or class-split outcomes.
21. **Carving (§20).** Only some constraints remove assignments; the others
    partition. "Provable" became "demonstrated in class".
22. **Amendment numbering (§20).** The C1-a extension is Formalization 01
    Amendment 02 and Formalization 02 Amendment 01.
23. **Appendix B #13** is the exact-light-cone *death* of the TT channel, not
    its closure.
24. **Appendix G.** The counting rule was misstated: through SX-1 the
    battery counts every line; TT-1, C1-a, and C1-a2 count gated checks
    only. The continuum-origin computation had no committed charter.
25. **Record integrity (§29).** The codified response to the asymmetric
    error budget is the N1–N10 negative-control standard (partially
    repaired), which the red-gate discipline complements.
26. **The distinctive-theory adjudication failed twice**, and the founding
    bet is negated "at the computed order".
27. **Red register (§23)** is scoped: ten entries contain seventeen failed
    gates. Foundations-record failures are listed in §23.1.
28. **DESI (§25).** "Armed but not sealed" conflated two senses of "sealed":
    a DESI DR3 falsification threshold *was* pre-registered and sealed on
    18 August 2026. The channel is now stated in plain terms, with its grade
    and the prereg's own caveats.
29. **The withdrawn June 2026 deposit** (10.5281/zenodo.20783057) is named
    in a supersession notice and in §29.
30. **The T3 anchor** is located (`physics-final` @ `310101f`) and
    positioned against its literature.

### Additions for comprehension

31. A plain-language overview, reading routes, and a note that
    "prediction" and "theory" are used narrowly.
32. §0 (origin and why this record is narrower); the gravitational
    identification defined (§12) with a plain-language upshot.
33. §2.1 relation to existing work; §3.3 the admitted model classes;
    Figure 1 (the architecture, typeset in TikZ).
34. Definitions at first use: the kernels $K,N,J,\nu$ with ℏ restored by
    declaration; access, seed, and closure; CARRIER; C_cons; Sel-4 and its
    parts; the probe; the Class-4 gate; occupancy evidence; ξ and the TT
    projector; R1–R7.
35. Worked examples: one hidden node (§4.1); the two-time kernel across a
    step (§5.1); a thermal bath inside the cone (§6.1).
36. Every headline number given its observable and scale.
37. The foundations scorecard (§4.5), with the checks re-executed during
    preparation.
38. Named obstructions (§22): Weinberg–Witten as a named exit, soft-graviton
    universality, Lorentz recovery, energy bookkeeping.
39. §29 rebuilt: release history, closure and reopening, governance (D-1,
    the signed termination condition, the DESI prereg), record integrity.
40. §31 ledger with a column separating standard ingredients from
    program-specific findings.
41. Appendix D (methods): what pre-registration here does and does not
    establish, with the charter-to-verdict timings; the role of AI agents;
    battery counting; author, funding, competing interests.
42. Appendix G with charter commits, gaps, and times; G.2 for the other
    instruments. Appendix H (glossary). Appendix I (notation and symbol
    collisions). References with verification tiers; entries marked † are
    supplied for this edition and not register-verified.

### Tone and labels

43. Advocacy sentences replaced with neutral statements.
44. Colliding labels resolved: C1-a2's charter gates are renamed A2-1 to
    A2-6; the state is written ϱ; the correlation length is written ℓ_c.

### Typesetting

45. The PDF is typeset by pandoc and XeLaTeX (`build/make_pdf.sh`), with
    LaTeX mathematics, a hyperlinked table of contents, PDF bookmarks, and
    the vector figure. Conversion only: the Markdown file is the source of
    truth.
