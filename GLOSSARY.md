# GRUT — Glossary

*Working definitions of the program's load-bearing objects. Entries here are **stipulations, not results**: each is a provisional referent that makes the register's claims well-posed. Under the **`u0` charter** (`CHARTER.md` §8) every V2 object is provisional — **revising a definition is expected; defending it is forbidden.** A definition that has to be defended has become an ontology, which u0 prohibits.*

---

## Constitutive organization
> **(provisional, revisable — not a defended ontology):** the **equivalence class of response functionals χ(ω,k) that produce identical observable transport under admissible coarse-grainings.**

**Why it is the central object.** The `u4`→(`u5`,`u6`) classification tree asks to *classify / order-parameter / derive* something — this is the *what*. Without a referent, "classify the universality classes of constitutive response" is a slogan; with it, the tree is well-posed:
- **`u4_constitutive_origin`** — asks why nature admits *this object at all* (why coarse-graining yields a response form); it **derives / interrogates the existence** of constitutive organization.
- **`u5_constitutive_phases`** — **classifies the classes**: the admissible equivalence classes, their morphisms (RG flows = the class-preserving vs class-changing maps), stability, observable distinctions.
- **`u6_constitutive_order`** — seeks an **order parameter that labels** the classes (with the RG monotone as a corollary, not the theorem).

**Why it is a *usable* working definition, not a slogan.** It is **operationally grounded**: "identical observable transport" is measurable, and "admissible coarse-grainings" is the same conditions U1/U4 already name (locality, causality, the near-equilibrium/weak-coupling regime). The definition therefore has empirical teeth (two χ's are in the same class iff no admissible experiment distinguishes their transport) rather than resting on an ontological posit.

**Fence (u0).** This entry *will* be revised as `u5`/`u6` sharpen "admissible coarse-grainings" and "observable transport". That revision is the program working. If a future pass finds itself *defending* the definition against a counterexample rather than *revising* it, that is the u0 line being crossed — stop and revise.

---

## The translation layer (added 2026-08-09; MAINTAINED AS PART OF BANKING)

*One line of plain English per dialect term. The dialect has a real cause — every wave named a new
failure mode, which is why the terms are precise — but precision that can't be translated is
private language. **Rule: any banking that coins a term adds its line here in the same commit.***

| term | plain English |
|---|---|
| **the register** | the machine-checked JSON file of claims that IS the program's product; everything else is commentary on it |
| **banked** | written into the register after review — the program's word for "we now stand behind this" |
| **tier** | a claim's declared epistemic grade (proven / derived / assumed / open …); no claim enters untiered |
| **ledger_delta / net +13** | each claim's signed count of assumptions it adds or removes; the net is the program's total admitted assumption count, currently 13 |
| **laundering** | selling something as a derivation while it quietly adds assumptions; the gate blocks it |
| **laundering_ok / waiver** | a declared exception: "yes this adds assumptions and says so openly" — must carry a written justification |
| **rung** | one step of the framework's build-out, each with its own claims and price |
| **wave** | one work session with a defined goal, ending in a relay to the human overseer |
| **FLAG / firewall** | a substantive change is surfaced and adversarially attacked before a human accepts it; nothing substantive lands silently |
| **same-wave firewall** | the attack happens in the same session that produced the result — errors die before they can travel |
| **bank-gate** | the live diff-checker: any edit to the register is audited against the last accepted state before it can land |
| **KC (kill-condition)** | a pre-registered way the current work would be wrong, written down before doing the work |
| **prereg / seal** | expectations written and hashed BEFORE an analysis runs, so results can't be read back onto them; results live in a separate file citing the hash |
| **blind-safe** | a sealed prereg guaranteed to contain no result numbers, so agents directed to read it stay blind |
| **fence** | a recorded boundary on how far a result may be used ("valid only under X; do not quote beyond it") |
| **F-MAP fence** | a specific fence: the data's fitted deviation-shape differs from ours in time-dependence, so amplitude comparisons carry an unresolved conversion — direction currently undetermined |
| **derived-pending** | derived modulo a named open input — honest middle grade between proven and assumed |
| **no-go export** | a negative result packaged for use elsewhere: "this route is closed, here is exactly what closed it" |
| **settled-negative** | a hoped-for derivation that failed on named obstructions and is frozen as a result, not left as "pending" |
| **earned-under-determined** | a quantity whose value is fixed only conditional on an axiom the program itself marks as chosen, not derived |
| **horn-conditional forward-only** | a result valid on one branch of an open fork, usable downstream only if that branch is later established — never as evidence for the branch |
| **armed trigger** | a pre-written consequence that EXECUTES when a named event occurs (no re-litigation) — e.g. "if X resolves against us, this claim demotes" |
| **retire / strike** | remove a number or claim from service while keeping the record of it (append-and-mark, never rewrite history) |
| **insertion-contaminated** | a computed number that depends on a modeling insertion the register never priced; consumers must declare the insertion, not inherit it |
| **held-at-flag** | reviewed by the overseer and awaiting formal acceptance — as opposed to never-looked-at |
| **compound (node)** | one registered claim secretly carrying two separately-dischargeable commitments — repair: split it |
| **omission** | a presupposition several claims rest on that is booked nowhere — repair: add it |
| **edge-not-vertex** | an open question booked as if it were an input; must never be counted in an inventory |
| **separate-universe (check)** | the consistency requirement that super-horizon patches evolve like independent universes; kills modifications that act on scales they shouldn't |
| **quotable** | the one number/statement from a calculation that may be cited downstream; everything else is diagnostic |
| **D3 deposit** | the pre-defined honorable ending: publish the ontology + derived boundaries + method, and stop |
| **the dispatch** | the one-page external question (pole vs cut of the vacuum's tensor response) that only an outside specialist can answer |

---

## "Specialist" — what the register has actually meant (added 2026-08-12, B0.2 audit)

> **Standing rule for any public-facing document: the word "specialist" never appears unqualified.
> Either name the modality in the same sentence ("an AI-relayed adversarial pass," "an in-house
> screen") or do not use the word. In a public document "specialist" says *human expert* to every
> reader, and on this program's record that reading would be false.**

**The audit.** `provenance/claims.json` contains **41 occurrences of "specialist"/"specialists"
across 15 of 70 claims** (verified by Python `re` over the raw file at every commit in the repo's
history — the count has never differed). Classified by which sense is in force:

| sense | count | what it denotes | risk |
|---|---|---|---|
| **A — prospective / reserved** | **17** | *"frontier-reserved (specialist, not in-house)," "escalate to a … specialist," "reserve for specialist," "the specialist dispatch."* A **future** human expert. Asserts that nobody has done this. | Low — these are honest statements of what is owed. |
| **B — a pass that was RUN, and whose output was banked** | **22** | *"finite-T CONFIRMED 2026-06-25 by open-systems specialist," "RESOLVED 2026-06-26 (specialist)," "EXTERNAL CHECK 2026-07-04 … an independent specialist … INDEPENDENTLY reconstructed the identical disposition," "the verified specialist deliverable," "CEILING-CHECK ANSWERED by the specialist."* | **High — this is the dangerous class.** |
| **C — collective/generic** | **2** | *"three specialists conflict"* — shorthand for three analytical positions. | Low. |

**What the record does and does not establish about class B.**

The register **never records the modality** of any class-B pass — not once, in 22 occurrences. It
does not say "human expert," and it does not say "AI-relayed." That silence is itself the finding.

What the record *does* establish, checkably:

- **No transmission to any external human expert is logged at any date.** The event log states the
  one drafted ask "remains unsent," and a later entry confirms "no entry since records a send to
  either author group."
- **The one time a class-B-style entry was examined, it was an in-house instrument.** The event log
  entry of 2026-08-10 records that words previously logged as a reply were "output of an AI
  literature-research tool operated by the owner — an in-house instrument," and rules the general
  case: such output "is in-house work product, recordable as a research note … and is not a reply
  from the audience of record."

So the honest statement is: **class-B "specialist" denotes an adversarial or literature pass run by
the owner — presumptively AI-relayed on the one precedent the record contains — and no occurrence
of the word anywhere in this register is backed by a logged communication with an outside human.**

**The concentration matters.** 13 of the 22 class-B occurrences sit in one node,
`rung3_single_pole` — the framework's load-bearing structural conjecture — including the sentence
*"the FIRST external check logged in this register."* That is the single most misreadable line in
the register, in the single most load-bearing node.

**Why the register text is NOT being mass-renamed.** The register is a historical record and
rewriting it would destroy the evidence of what was believed when. The fix is this entry, plus the
standing rule above, plus the enforcement test in `provenance/test_doc_sync.py`.
