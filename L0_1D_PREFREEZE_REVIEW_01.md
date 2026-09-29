# L0-1d — PRE-FREEZE DESIGN REVIEW 01 (analytic-only; nothing to quarantine)

**Date:** 2026-09-29 · **Object:** the L0-1d (D-HERM-a) charter draft
(`b27e559`) · **Authority:** the owner's authorization of the analytic
pre-freeze review under the adopted floor boundary
(`L0_1_FLOOR_TERMINATION_ADOPTION_01.md`).

**Method.** Three independent reviewer agents, each with one lens:
(1) method, prohibition, and termination-condition compliance;
(2) correctness of every mathematical identity; (3) predicate-registry
fidelity, vacuity, and identity-versus-prediction honesty. **Hard rule
for all three: analytic only.** No member dynamics were integrated, and
no member kernel, Gram matrix, moment sequence, or member spectrum was
computed. **Unlike L0-1c, this review previewed nothing, so this
record quarantines nothing.** The charter author (the operator)
verified each finding by hand before incorporating it. The owner's
setup authorized "a smaller set of reviewer agents", so there was no
separate machine-verifier pass. Revision 2's new mathematics gets one
focused analytic verification before freeze, recorded in §4.

**Yield:** 44 findings in total (20 + 10 + 14), with heavy overlap.
They collapse to the themes below. Every theme was confirmed and
incorporated, except where §3 notes a refinement.

## 1. The findings that changed the fork

| Theme | Raised by | What was wrong | Disposition in revision 2 |
|---|---|---|---|
| **F-1 misstated** (blocker, all three) | 1, 2, 3 | The draft said zero-affinity asymmetry leaves the retained-site kernel *unchanged* ("invisible"). F-1 says only that it equals a *different* symmetric chain's kernel, so it changes with γ, which is certain. A mechanized Outcome A would have HALTed a correct run. | Outcome A is now "leaves the reciprocal (CM) class", which is identity-impossible. L-1 is renamed to *reducible to a reciprocal twin*. The faces state that the kernels change. |
| **Circulant estimate qualitatively wrong** (major, two reviewers independently) | 2, 3 | The draft ignored the e₁e₁ᵀ defect. The ring has a reflection R fixing site 1 with RKR = Kᵀ, so the generator is self-adjoint in an indefinite form. The odd modes are invisible at γ = 0 and the spectrum is simple. **The spectrum therefore stays real for small γ, and CM breaks through negative real weights (−O(γ²)), not complex pairs,** until exceptional points appear. | §3.5 is rewritten with the pseudo-Hermitian analysis and both breach mechanisms. The claim is labeled analytic-leaning, not theorem. |
| **Outcome C conflated a blind instrument with a falsified hypothesis** (blocker) | 1, 3 | The draft recorded "falsified" when the operational Gram failed to see a breach that is exact by theorem. That contradicts the owner's O-2 ruling principle. It also invoked a re-charter after a terminal label, which T3 forbids. | **Resolved at the root.** The adjudicating CM battery is now **exact**: a moment-Hankel test in exact rational arithmetic (R-3 scope). Outcome C is now a genuine exact falsification. The operational Gram becomes an ungated map measuring what a trajectory battery can see. |
| **Gram tolerance not tied to integration error** (major) | 1, 3 | Weyl bound ≈ 2×10⁻⁸ against a −10⁻¹⁰ tolerance. The draft's justification borrowed L0-1c's measured previews. | Dissolved: the adjudicating test is exact. The operational Gram is ungated, reported full and halved. |
| **X-1 confounded** (major) | 1, 2, 3 | Holding K_s fixed also shrinks each edge product to 1 − γ², so X-1 against γ = 0 mostly measured zero-affinity renormalization. | **Reciprocal twins S(γ)** were added, with the same edge products and zero affinity. Their moments agree with C(γ) through order 22, since only winding walks see affinity. X-1′ compares C(0.9) with S(0.9). A **balanced ring** B(γ) was added: zero affinity, **same K_s**, the asymmetry-without-affinity control. The limitation is disclosed: K_s and the edge products cannot both be held. |
| **Identity controls not halt-grade** (blocker) | 1, 2, 3 | The γ = 0 CM check sat inside a response gate, so its failure routed to PARTIAL. This is the L01C-2 defect class again. | RC-8 now requires exact CM at every zero-affinity member, and a failure is HALT. |
| **F-7 over-generalized** (major, all three) | 1, 2, 3 | Diagonal similarity to a normal matrix needs a **uniform diagonal** for a directed cycle. The record's own attachment convention breaks that, so F-7 does not cover the natural O-2 candidate. "Invisible" was too strong: F-7 excludes only growth. | §3.8 is rewritten. F-7 is an observability/identity result (the owner's ruling) with its correct scope. **O-2 is not deferred on F-7 grounds; the attached directed ring is a live O-2 candidate.** |
| **M-1 failure routing undefined** (major) | 1, 3 | A clean M-1 failure had no line and could be masked by precedence. | M-1 failure with RC-6 clean is recorded as **COMPARATOR-LIMITATION**, because the exponential bound is identity-held. It is never "affinity load-bearing for memory". This is reviewer 3's reading. Reviewer 1's alternative, issuing a load-bearing line, was rejected: it would record a comparator misgrade of a kernel with a proven exponential bound as physics, the prohibition-3 direction. |
| **No outcome → terminal-label map** (major) | 1, 3 | Outcome B could read as either DISCHARGED or CLASS-SPLIT after the run. | A frozen table was added (§5): B supports CLASS-SPLIT; C supports FALSIFIED; PARTIAL and HALT are non-terminal and use the single re-charter. The owner assigns the label. |
| **Relative tolerances infeasible at kernel minima** (major) | 1, 2 | An RK4 relative error scales with k⁽⁵⁾/k, which blows up at the troughs of an oscillating kernel. | RC-1, RC-2, and RC-3 are now envelope-normalized (·e^{μτ}), at 10⁻⁶ per the reviewer's analytic RK4 bound. |
| **Vacuity / open content ungated** (major) | 3 | Every gate was identity or analytic. The only open content was ungated, and part of it is predictable. | Following the reviewer's recommendation, γ* stays ungated (movable by tuning). **Labeled analytic expectations are recorded** in §3.6, where the maps can confirm or refute them. §0 now states plainly what theorems fix and what the run certifies. |

## 2. Minor findings (all incorporated)

- Instrument contract now authorizes `jacobi_eig` on the symmetric data Gram.
- The E envelope is defined discretely.
- RC-7 names the eigen-form anchor.
- Orientation and edge conventions are written out.
- "Symmetrized chain" is replaced by an explicit S_T(γ), so it cannot be confused with K_s.
- Member/leg vocabulary is fixed.
- Stale references to the *draft* termination condition are updated.
- The canonical label UNFORMULABLE-WITH-DOCUMENTED-REASON is used.
- The scope clause names the declared members and covers PARTIAL and HALT.
- The re-charter budget is stated.
- Component (a)/(b)/(c) disclosure is on the certificate face.
- The real reason (b) is not gated is given: H-HERM-1 makes no claim about it.
- X-1′ is classified as not banded.
- M-1 on T(γ ≠ 0) is reclassified as analytic-leaning.

## 3. Refinements to reviewer proposals

- **Reviewer 1, D-1** offered two options for Outcome C: (i) an operational FALSIFIED, or (ii) non-terminal INSENSITIVE with a pre-named re-charter battery. Revision 2 does neither. It makes the primary battery exact, which removes the insensitivity case altogether. (Reviewer 1's suggested re-charter battery, a static R-3 reading, is in effect promoted to the primary battery.)
- **Reviewer 1, D-5** (matched twin) and **reviewer 3, D-4** (balanced ring on the same K_s) are both adopted. They answer different questions: the twin isolates affinity from edge renormalization; the balanced ring is the asymmetry-without-affinity control.
- **Reviewer 3, D-6's** open question, where the exceptional points are, becomes an **exact ungated map**: a Sturm real-root count on the retained-site recurrence polynomial, together with H₀ inertia.

## 4. Focused verification of revision 2 (pending)

Revision 2 introduces the exact-CM theorem (§3.4), the pseudo-Hermitian analysis (§3.5), the twin moment agreement, the balanced pattern, and RC-9. One analytic-only verifier is checking these before freeze. Its findings and their disposition will be appended here.
