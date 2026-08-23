# Reality audit — correction

> Corrects two findings in `REALITY_AUDIT_RESULTS.md`. That file is left untouched: it is the
> record of what the audit concluded, and the correction is a separate citing file, per this
> program's pre-registration discipline (`grut-prereg-discipline`: results live in a separate file
> that cites the sealed instrument).
>
> **NOTHING BANKED.** `claims.json` untouched, `validate.py` PASS. Both corrections make the audit
> STRONGER, not weaker. The 65 UNRESOLVED-BLOCKED verdicts are upheld and defended in §3.

---

## 1. The load-bearing map: one nested chain, not two independent pillars

**Reported:** *"1. `background_time_translation_flow` — carries 28. 2. `rung1_inin_action` — carries
27. 3. `rung2_kms_gate` — carries 20. Two nodes carry ~55 of 71."*

**The three sets are NESTED.** Computed from `claims.json` by transitive closure over `depends_on`:

| node | reach | subset of `background_time_translation_flow`'s reach? |
|---|---|---|
| `background_time_translation_flow` | 28 | — |
| `rung1_inin_action` | 27 | **YES** |
| `rung2_kms_gate` | 20 | **YES** |
| **union of all three** | **28** | |

`rung1_inin_action.depends_on` contains `background_time_translation_flow` (verified). Therefore
every node downstream of rung1 is also downstream of background, and **28 + 27 = 55 double-counts
27 of the 28.** Pairwise overlaps: A∩B = 27, A∩C = 20, B∩C = 20.

**The corrected fact is SHARPER than the reported one.** It is not two pillars — it is **one chain**:

    background_time_translation_flow  ->  rung1_inin_action  ->  rung2_kms_gate  ->  (25 more)

**28 of 71 nodes — 39% of the register — hang off a single root.** That root is
`background_time_translation_flow`: booked **2026-08-18, five days before this audit**, as an
OMISSION (a presupposition booked nowhere), tier `assumed`, Δ+1, and its own `sub_status` reads
*"NOT a physics claim about de Sitter -- the claim is only that the framework HAS BEEN USING such a
flow."*

**That is the single most consequential structural fact this audit produced**, and it is stronger
stated correctly. A program whose largest dependency root is a presupposition discovered last week
is a different object from one with two independent pillars.

*Method note for the next pass:* blast radii must be reported as **sets with their overlaps**, or as
a chain, never as addable integers. Summing reach counts over nodes on a common path is the same
arithmetic error class as summing a blind ledger — and this register already carries a gloss added
after an external reviewer misread exactly that.

## 2. `rung1_inin_action`: the right node, the wrong verdict — and the real finding is better

**Reported:** `DOES-NOT-HOLD`, reason *"finite-memory clause contradicted by 4/7 Class-C outcome
branches; tier shown over-states."*

### 2.1 Why DOES-NOT-HOLD is not earned

The Class-C outcome branches are **hypothetical**. The calculation has not been run: walls A (no
graviton-probe assembly exists), B (the RG half undischarged) and C (the TTW premise is in-out, not
retarded) all stand, and the consequence map is by construction *"if it came back this way, here is
what it would mean."* **No branch has been realised.**

Grading a claim `DOES-NOT-HOLD` because four of seven possible future results would contradict it
converts *"exposed under several branches"* into *"contradicted."* That is scope inflation — the
exact defect class `REALITY_AUDIT_BRIEF.md` §3 (Q3) names as the program's recurrent pattern —
committed by the audit, in the direction of finding a defect, on the highest-blast-radius node in
the register. `REALITY_AUDIT_CHARTER.md` §4 pre-registers that findings must not be manufactured;
this is that fence firing on the audit's own output.

### 2.2 What the REALISED evidence supports

The class-A pair does bear on the finite-memory clause and is adverse — but at a fenced scope, in
the results files' own words:

- `RESULTS_worldline_reduction.md`: the dS worldline reduction gives a horizon-forced **white
  floor**, folded s_eff → 0; *"a white floor is zero-memory, contradicting the FINITE-memory claim
  as much as it contradicts s = 3."* And: *"the registered kernel and the reduced proxy kernel are
  DIFFERENT OBJECTS"*, *"NOT a verdict on class C."*
- `RESULTS_tt_worldline.md`: the free TT-graviton geodesic kernel is **non-stationary**.

Both are **class-A proxy scope**, both are **unbanked pending adjudication**. That supports
**HOLDS-NARROWER** or **UNRESOLVED**. It does not support DOES-NOT-HOLD.

### 2.3 The real finding — and it is the highest-value class the brief named

The statement, verbatim:

> *"The gravitational vacuum **is a responsive medium with finite memory**, described by **a single
> Schwinger-Keldysh influence action** S_IF with retarded dissipation kernel K_R and noise kernel N
> (doubled x_r/x_a fields)."*

**That is two claims at one tier.**

| part | content | honest status |
|---|---|---|
| **A — ontology** | the gravitational vacuum *is* a responsive medium with finite memory | a STANCE. The node's own `ledger_note` says so: *"STANCE, not derivation."* |
| **B — formalism** | it is described by a single SK influence action with K_R and N | genuinely **shown** — Schwinger 1961, Keldysh 1964, Feynman-Vernon 1963, Calzetta-Hu |

Run `CHARTER.md` §4's compound test — *can one part discharge alone?* **Yes.** The Feynman-Vernon
structure holds whether or not the vacuum is in fact a responsive medium. Part B is established
physics; part A is the program's founding bet. **The candidate appears in the node's own statement,
which by the charter's own tell makes this a SPLIT question, not an omission.**

So the finding is: **a `shown`-tier, Δ4 node carries an ontological stance welded to a borrowed
formalism.** That is precisely the *"tiered `shown` → reality ASSERTED"* over-statement class that
`REALITY_AUDIT_BRIEF.md` ADDED-2 pre-registered as the highest-value finding available. **The audit
found the right node. It reached for a stronger verdict than the evidence carried, and in doing so
reported a weaker finding than the one actually present** — a compound at the register's largest
dependency root.

### 2.4 Corrected entry

| field | value |
|---|---|
| verdict | **HOLDS-NARROWER** |
| basis | part B holds at `shown`; part A is a stance and does not |
| repair | **SPLIT** the node per CHARTER §4 — owner adjudication, not an agent edit |
| Class-C branches | recorded as **EXPOSURE**, not contradiction (4/7 branches, none realised) |
| class-A pair | **ADVERSE AT PROXY SCOPE**, fenced by its own results files, unbanked |
| blast radius | 27 (subset of background's 28 — see §1) |

**Note against my own correction:** splitting a Δ4 node is not free. Which part carries the +4, and
whether the split changes the net, is a register decision with ledger consequences. This file
proposes the split; it does not price it.

## 3. What is UPHELD — the 65 UNRESOLVED-BLOCKED

**Defended without qualification.** The audit reported that the instruments to grade 65 nodes at
full strength — source-verification harness, reproduction runners, prose-graph extractor — do not
exist, and it declined to lower its standard to fill the table.

That is `REALITY_AUDIT_BRIEF.md` ADDED-7 working exactly as written: *"An audit that returns few
verdicts and a precise blocker log has succeeded. An audit that returns 71 confident verdicts by
quietly lowering its standard where the tooling ran out has failed, and it will be indistinguishable
from success in the summary table."*

The owner pre-registered this outcome before the run. **It is the result, not a shortfall.** The
blocker log is now the program's build queue.

## 4. The pattern, recorded

Ninth and tenth defects in this stretch; **still zero physics errors.** Both of today's are in the
*audit* rather than in the physics: an addition over sets that overlap, and a verdict stronger than
its evidence. Both were caught by recomputing the claim rather than by reading the reasoning —
consistent with every prior instance.

The specific lesson for the next pass: **the audit needs the same treatment it gives the register.**
Its numbers should be emitted from the graph, not typed; its verdicts should carry the evidence
class that licenses them; and a verdict resting on unrealised hypotheticals should be structurally
unable to render as `DOES-NOT-HOLD`.
