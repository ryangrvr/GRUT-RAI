# REALITY AUDIT — operational brief

*The owner's brief (2026-08-23) is carried in full. This document adds seven items that would
otherwise distort the result, marked **[ADDED]**. Read `REALITY_AUDIT_CHARTER.md` first.*

---

## [ADDED-0] The framing fence — read before anything else

This has been described as a "hail mary" and an "ultimate answer" exercise. **That framing is
itself the largest hazard in the audit**, and it is named here so it cannot operate silently.

An audit run under the expectation that it will deliver a verdict on GRUT will deliver one,
whether or not the evidence supports it. **It will not produce 42.** The most likely honest
outcome, given everything already computed, is: most nodes hold at a *narrower* scope than the
register states; a handful of tier-vs-reality mismatches; and a load-bearing map showing two or
three nodes carrying most of the structure. That is a genuinely valuable result and it is not an
ultimate answer.

**The deliverable is a MAP, not a verdict.** §15 already forbids concluding GRUT is right because
many nodes hold, or wrong because some fail. This clause extends that to the audit's own framing:
do not write a conclusion the map does not contain.

## [ADDED-1] Three claim TYPES — and grading across them is a category error

GRUT's claims are mostly **not** about nature. Most are about a formalism. Classify every item
BEFORE applying Q1, because the wrong question produces a meaningless verdict:

| type | what makes it true | what "reality" means for it |
|---|---|---|
| **MATHEMATICAL** | true or false as mathematics, full stop | re-derive it; no experiment is relevant |
| **FRAMEWORK** | true *within* a stated formalism, given its assumptions | check the derivation AND whether the formalism's conditions hold |
| **PHYSICAL** | true of nature | world-check per §10 |

**Grading a MATHEMATICAL claim as UNRESOLVED "because no experiment bears on it" is a category
error, and it would be the single most common way this audit produces noise.** The Blaschke
pole-free result, the Wronskian identities, the l(l+1)−2 coefficient, the free spectral zeros —
these are mathematics. They are settled or not settled by calculation alone.

Report the type distribution. **[INFERENCE] If the audit finds very few PHYSICAL claims, that is a
finding in itself** — it would say the program is further from empirical contact than its prose
implies.

## [ADDED-2] The actual product is a MISMATCH MATRIX, not a verdict list

A verdict list restates the register. The register's own tiers are: `shown` 10, `assumed` 16,
`postulate` 14, `to-derive` 20, `derived-pending` 4, `measured` 3, `heuristic` 2, `open` 2 —
**and zero at `derived`.**

So: **an ASSERTED verdict on a node already tiered `assumed` or `postulate` is a NULL RESULT, not a
finding.** It is the register agreeing with itself. If the audit returns "40 nodes ASSERTED" it has
restated the tier column and discovered nothing.

**Build the matrix: register tier (rows) × reality verdict (columns). The findings are the
off-diagonal entries.** Pre-registered as informative:

- tiered **`shown`** → reality ASSERTED / BORROWED-SCOPE-MISMATCH / DERIVATION-FAIL → **the register
  over-states**. Highest-value finding class.
- tiered **`derived-pending`** → derivation reproduces cleanly at stated scope → **the register
  under-states**. Also a finding, and one this program's directional-optimism rule makes it
  unlikely to notice unprompted.
- tiered **`shown`** → HOLDS-NARROWER → **scope creep**, the recurrent pattern.
- any tier → DOES-NOT-HOLD → self-explanatory.

Report the matrix in full. **A fully diagonal matrix means the register describes itself accurately,
which is a real and publishable result.**

## [ADDED-3] Calibration batch BEFORE the fragile eight

The owner's §7 says start with the eight known-fragile items. **Do the opposite first, for one
batch only.**

Audit a **random sample of 10 ordinary nodes** and record their verdict distribution *before*
touching the fragile eight. This establishes your baseline severity. Then audit the eight, then the
remainder.

Reason: starting with items pre-labelled fragile anchors the whole sweep on defect-hunting, and §5
forbids manufacturing findings. With a calibration batch you can **measure** whether the fragile
eight scored harsher than baseline, and report that comparison. Without it, there is no way to tell
severity drift from real defects — which is exactly what the consequence-map symmetry audit had to
reconstruct after the fact.

Seed the random sample from a fixed list written down before you look at any node.

## [ADDED-4] Uniform per-node budget, with escalation as a recorded decision

71 nodes × 4 questions × source-opening is unbounded. Unbounded audits go deep early and shallow
late, producing depth asymmetry as an artifact of ordering — the consequence-map audit measured
exactly this (longest/shortest branch ≈ 1.28×, and the thinnest branches were the last-considered
ones).

**Set a fixed default effort per node. Escalate only on a stated trigger, and RECORD the escalation
as a decision with its reason.** Triggers that justify escalation: high blast radius; a tier-vs-
reality mismatch; a `shown` tier; a source that appears to say something different. Report at the
end how many nodes were escalated and why. **A node that got the default treatment is not a
failure of the audit; an unrecorded escalation is.**

## [ADDED-5] SOURCE-UNAVAILABLE is a distinct verdict, and it is not a failure

The brief says open the primary source. Some sources will be paywalled, offline, or otherwise
unreachable (precedent: `mizar-items`' host no longer resolves). **Do not silently grade these as
HOLDS, and do not grade them as SOURCE-MISMATCH.**

Add: **SOURCE-UNAVAILABLE** — the claim's evidentiary route is borrowed and the source could not be
independently opened in this pass. State what *was* checked (abstract, secondary citation, the
program's own note) and mark the verification as **owed**. This is an honest null and it belongs in
the summary counts.

## [ADDED-6] The self-screen (§13) must be run by a separate pass

§13 asks the audit to screen itself against the known failure patterns. **An auditor checking its
own output is the exact conflict-of-interest §6 names**, applied one level up.

Run §13 as a **separate pass over the finished output**, ideally in a fresh context that has not
seen the audit being produced — only its results. Its specific charge:

1. Did the fragile eight score harsher than the calibration batch? By how much?
2. Are HOLDS verdicts thinner than DOES-NOT-HOLD verdicts? (Depth asymmetry, measured.)
3. Was any MATHEMATICAL claim graded UNRESOLVED for want of experiment? (Category error per ADDED-1.)
4. Was any ASSERTED-on-`assumed` reported as a finding? (Null dressed as signal per ADDED-2.)
5. Is there a node the audit was reluctant to grade DOES-NOT-HOLD because of what it carries?
   **Name it.** Blast radius must not influence verdict — ADDED-2 and §3 are separate axes.

## [ADDED-7] The blocker log — a required output, and a success mode

The owner's stated expectation for this run: *"I don't expect to actually get an answer right now,
I'm sure we'll find where software needs updating to even attempt the answer."*

**Take that literally. It changes what a successful run is.** If the tooling cannot answer a
question, that is a RESULT, and it is the result this run most likely produces. Do not work around
a gap silently, do not approximate past it, and do not let a node quietly receive a weaker verdict
because the instrument to grade it properly does not exist.

**Emit `REALITY_AUDIT_BLOCKERS.md`**, and treat it as co-equal with the results file. One entry per
blocker:

| field | content |
|---|---|
| what I could not do | the specific question left unanswered |
| for which nodes | ids |
| why | missing tool / unreachable source / uncomputable object / undecided owner ruling / cost |
| what would unblock it | the concrete thing that has to exist |
| verdict consequence | what verdict the node received *because* of the blocker, and what it might have received otherwise |

**The last row is the one that matters.** A node graded UNRESOLVED because the instrument is
missing is a different fact from a node graded UNRESOLVED because nature is ambiguous, and the
summary counts must not merge them. Add the suffix **-BLOCKED** to any verdict caused by a blocker
rather than by evidence (e.g. `UNRESOLVED-BLOCKED`), and count them separately.

**An audit that returns few verdicts and a precise blocker log has succeeded.** An audit that
returns 71 confident verdicts by quietly lowering its standard where the tooling ran out has
failed, and it will be indistinguishable from success in the summary table — which is exactly why
this section exists.

---

## Everything below is the owner's brief, unchanged and in force

§0 prerequisite (adjudicate ω_c, `rung7_wz` +2/+3, the `rung1` finite-memory clause, and the 6-vs-7
enumeration; emit a clean register checkpoint before sweeping) · §1 what this is not · §2 the four
questions with evidence classes BORROWED / DERIVED / ASSERTED / EMPIRICAL / MIXED · §3 the
load-bearing map as primary deliverable · §4 the controlled verdict vocabulary · §5 "everything
holds" pre-registered · §6 the external-validation firewall · §7 the eight fragile items (now
after the calibration batch, per ADDED-3) · §8 primary-source verification · §9 reproduction ·
§10 empirical world-checking · §11 the formal delete-one test on a sandbox graph · §12 the output
package · §13 the self-screen (now a separate pass, per ADDED-6) · §14 do not mutate the live
register · §15 the final question.

**The two clauses from the owner's brief worth repeating because everything else fails without
them:** *"Do not treat 'consistent' as 'confirmed'"* and *"Do not treat 'asserted' as defective by
definition."*
