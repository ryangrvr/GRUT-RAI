# Where the Responsive Vacuum Stops

*A negative-results report on a program that modelled the gravitational vacuum as a medium with memory, priced every assumption it took, and pushed until it stopped.*

D. Ryan Grover · {{STAMP_DATE}}

---

## Abstract

**This is a negative-results report.** Between early and mid-2026 a single author, working with AI collaborators under a machine-checked discipline, built a framework treating the gravitational vacuum as a responsive medium with finite memory, and pushed it until it stopped. This document states where it stopped.

The framework produced **no novel positive predictions**: the register's `derived` tier is empty and has always been empty. What it produced instead is a map of boundaries — results about what the framework *cannot* do, several of them refutations of its own hopes: it cannot derive its own coupling normalization; its central projector is a choice rather than a theorem; and the calculation meant to fix its one free parameter returned, when finally run, that no value is fixed. The single decisive question it identified — whether the vacuum's tensor response has a relaxation pole or a branch cut at low frequency — was drafted as a one-page ask for outside experts, **and never sent**; subsequent in-house work suggests the question may be ill-posed in the formalism its intended readers use.

Two inflations are refused here. The program's physics is not presented as a theory; and its method, though it is the more transferable output, is not presented as validated — it carries a published negative self-assessment and remains unexamined by any independent team. A prior book by the same author, with a live DOI, describes a **different** framework and is largely superseded; a note below states what in it is wrong and why the correction is owed rather than done.

Every count in this document is emitted from the claim register by script on the date shown. The register, the calculations, and the audit tooling are public.

---

## If you read nothing else

1. The framework makes **no novel positive prediction**, and its own register says so in a machine-checkable field.
2. Its real output is **boundaries** — including several the program proved *against itself*, after wanting the opposite.
3. Its one decisive external question was **drafted, held, and never sent**; the program's later reading is that the question may be **ill-posed as posed**.
4. **No outside physicist has answered any physics question put by this program** — see fixed point 2 below, which states this in the specific, checkable form rather than as a denial.
5. The method — a claim register that prices assumptions and refuses to let derivations quietly acquire them — is the more useful output, and it is **unvalidated by anyone but its author**.
6. A previous book by this author, still live under its own DOI, is **not this framework** and is substantially wrong; the correction to it is **owed, not done**.

---

## Six fixed points

These are the load-bearing negatives. Each is checkable against the public register in minutes.

**1 — Zero novel positive predictions; the `derived` tier is empty.** Of {{n_grut}} claims in the framework's scope, the tier reserved for "follows from the foundation, derivation exhibited and checked" contains **{{tier_derived}}**. The tiers that are populated are `shown` ({{tier_shown}}, standard physics verified against primary sources), `derived-pending` ({{tier_derived_pending}}, derived modulo a named open input), `assumed` ({{tier_assumed}}), and `to-derive` ({{tier_to_derive}}). A test in the repository fails if this ever changes without the headline being rewritten.

**2 — No outside physicist has answered any physics question put by this program.** Stated in the specific form, because the general denial is unfalsifiable-sounding and this one is checkable: the register contains **{{spec_B}} records phrased as an external pass having run** — including **six, across {{n_spec_2026_06_25_nodes}} nodes**, written as *SPECIALIST CONFIRMED* and *SPECIALIST-CORRECTED* and dated 2026-06-25. All trace to sessions the author ran himself. **No transmission to any outside human is logged at any date**, and the one log entry that recorded a reply was corrected the same day: the quoted words were output of an AI literature tool the author operated. Appendix D carries the full {{spec_total}}-of-{{spec_total}} classification, including the {{spec_A}} that correctly denote a *future* expert and the {{spec_D}} that are filenames.

**3 — A prior book with a live DOI describes a different theory.** Concept DOI `10.5281/zenodo.19803663`, seven versions, latest v4.0 at `10.5281/zenodo.20783057`. See the note below.

**4 — Every count here is generated, not typed.** See the next section.

**5 — This is not the program's final deposit.** The program carries a signed termination condition that schedules a closing document *after* a stop condition fires. **No stop condition has fired.** This document exists to correct a wrong live DOI — a different obligation — and changes nothing about what fires or when.

**6 — The name contains "Theory of Everything."** It does, on the prior deposit's own title page. What that reaches for, and why it is not what this document claims, is addressed at the end, in the author's own voice, placed last deliberately.

---

## The one-number rule

No count in this document was typed by hand. Every figure above and below is emitted by `provenance/emit_public_numbers.py`, which reads the claim register and writes a dated block; this document is rendered from a source file in which each number is a named placeholder, and a test fails if the rendered text disagrees with a fresh run. The rule exists because this program has twice published counts that were wrong — once by a mis-scoped audit pattern that silently dropped every capitalized instance of the word it was counting, and once in the prior book, at scale.

Two honest exceptions, both marked where they occur: numbers **quoted from the prior deposit** are quoted, not generated — they are that record's claims about itself, not this register's; and numbers **cited from published literature** carry their source. Everything else comes from the script.

---

## A note on the prior deposit

A book by this author is live on Zenodo: *Grand Responsive Universe Theory GRUT ToE v4.0 — The Emergence of Everything — Candidate Framework*, deposited 2026-06-21, resource type **preprint**, seventh in a series under concept DOI `10.5281/zenodo.19803663`. **It is not the framework described here, and it is substantially wrong.**

It was not sloppy, and that is the point worth making. Its own public description reads:

> *"Fully machine-checked. 121 registered claims across six tiers, over 3,000 gating tests, falsifiers attached — every reader-facing claim mapped to a registry tier, no HOSTED or OPEN result dressed as DERIVED."*

That is this document's pitch, made first, by the same author, about a body of work that a later verification pass scored **1-of-18 on its verifiable numbers, 0-of-7 on its falsifiers, and 1-of-11 on its scorecard rows**. A reader who notices that I am promising machine-checked rigor twice is right to notice it, and is owed the mechanism rather than an assurance.

**Here is the mechanism.** The tests tested the code. The register graded itself. Nothing in the loop was charged with trying to break a result before it was banked. Three thousand tests can pass against a register whose entries were written by the same process that wrote the claims, and a tier label is only worth the adversarial pressure applied before it is assigned — which in that program was none. The count of tests measured coverage of the machinery, not scrutiny of the physics. The present program's difference is not more tests; it is that a result is attacked, by an independent pass defaulting to *broken*, before it may be banked — and the record of this document's own construction contains four occasions on which that pressure removed a claim its author wanted.

What died with that book: an entire dark-matter substrate line; a two-anchor hierarchy ledger; a claimed unified no-go; and the whole `FORBIDDEN-BY-THEOREM` tier, which asserted impossibility results the framework had not established.

Four things are wrong in public right now, and two can be quoted from the book against itself. Its key-points list advertises a **32σ** exclusion; the present register's own computation of that quantity returned roughly **2σ**, and found the mechanism it rested on had the wrong sign. The same list advertises a falsifier at **"689 Hz, zero free parameters"**; that observable was later found to be energy-basis rather than position-basis, which is not a free-parameter question at all — the falsifier as advertised does not exist.

**The remedy, stated as owed.** A version DOI is permanent by design: `10.5281/zenodo.20783057` will retrieve that text forever, and nothing said here changes it. What *can* be done is to deposit a superseding note as a new version under the concept DOI, so that every citation of `10.5281/zenodo.19803663` resolves to the correction and points onward to this document. **That has not been done.** It is owed, it is the author's to do, and until it is, the prior record stands uncorrected in the place most readers will meet it.

---
