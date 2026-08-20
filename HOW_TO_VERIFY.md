# How to verify this repository

Everything below is Python 3 stdlib — no dependencies, no network. From a clean checkout:

## 1. The register gates (the product)

```bash
python3 provenance/validate.py
```
Blocking validator: every claim tiered, sourced, falsifiable; the anti-laundering discipline; the
blind ledger sum. Expect `PASS`, the net ledger as the validator prints it, and the waived-by-stance disclosure
(the waived total the validator prints) printed on its face.

```bash
python3 provenance/validate_scoped.py
```
The scoped gate: one register, several ledgers (GRUT vs the physics-cluster maps), plus the
cluster typed inventory. GRUT's net is whatever the validator prints for grut scope, and must not move when cluster contents change (2026-08-17: this line carried a hand-typed +13 that had gone stale once the fourth rung1 input was booked — the same defect the standing docs' sync stamps exist to prevent).

```bash
python3 provenance/bankgate.py
```
The bank-time gate: diffs the working register against the last accepted baseline. `CLEAN` means
no unaccepted change; any edit shows as a flag with severity.

## Verify before any irreversible act

**The rule, and what it cost to learn it.** On 2026-08-18 two pre-registrations were sealed and
manifested, and the suite ran afterwards. The guard that governs blind-safe seals fired
immediately — against a file that could no longer be edited, because sealing it was the point.
The artifact was repaired by supersession; **seal-then-verify is an ordering defect, and in a
class where the act is irreversible an ordering defect simply recurs.**

So: **the guard suite is a precondition of any irreversible act, not something done near one.**
That covers sealing, manifesting, tagging, releasing, and depositing — everything a working tree
cannot undo.

For sealing, the rule is mechanized:

```
python3 provenance/seal.py <prereg filename>
```

It refuses when an **undeclared** failure is open, when the file is already manifested, and — the
whole point — when a blind-safe file fails **any** blind-safe guard, *before* the hash exists,
where the answer can still change. Declared adjudications (`provenance/expected_red.py`) do not
block; a new red does.

**Why the candidate is checked twice.** The suite's blind-safe guards are *set-valued* — one test
over every sealed pre-registration — and they are currently declared reds. A declared red does not
block, so a new file carrying the very defect those guards exist to catch would have sealed
cleanly **on the strength of the record of that defect**. Two fixes, both in force: declarations
are made at *(test, case)* granularity so a new member of a declared set is a new red, and
`seal.py` runs every blind-safe guard against the **candidate directly**, where no declaration can
speak for it.

For tagging, releasing and depositing there is no local tool, because the act happens elsewhere.
The rule is the same and is the operator's to keep.


## The open adjudications, and what a declared red is allowed to mean

`provenance/expected_red.py` gives a known failure a third state between green and broken. Every
declaration names **the specific cases it covers** and, for each case, **the open adjudication it
waits on** — an id in `provenance/OPEN_PASSES.txt`.

Two properties the file enforces, both learned the hard way:

- **A new member of a declared set is a new red.** The runner diffs the live case set, produced by
  the same enumerator the test asserts on, against the declared one.
- **A declaration citing a closed or unknown adjudication fails in its own right.** Otherwise a
  pass closes, the test keeps failing for an unrelated reason, and the runner prints green while
  citing a ruling that already happened — which staleness cannot catch, because stale fires only
  when a test starts *passing*.

**Closing a pass is a human act**: set `STATUS: CLOSED` in `OPEN_PASSES.txt` with the ruling, then
remove every declaration resting on it. If a test still fails afterwards, that failure is new and
the runner says so.


## Adding a calculation

`calc/` is enumerated from a **committed manifest**, not from the directory — a gitignored mutant
left by a mutation battery once inserted itself as a row in the published calculation index, and a
count another clone cannot reproduce is not a verifiable number. So adding a calculation is two
acts:

```
python3 provenance/build_calc_manifest.py --write
python3 provenance/build_public_doc.py --write
```

The manifest is not trusted on its word: `test_public_doc.py` derives the calculation set from
`git ls-files` and fails if the manifest disagrees.


## Keeping the book current with the register

The public document is a **derived artifact in four ways, and all four are checked**:

| what | how it stays true | what fails |
|---|---|---|
| counts | emitted from the register; never typed | `emit_public_numbers.py --check`, and a guard whose coverage derives from the emitter |
| tables | generated at build time | `build_public_doc.py --check` |
| figures | generated from the register and the map | `build_figures.py --check` |
| **prose** | **pinned to the register nodes it cites** | **`doc_register_pins.py`** |

The fourth was unguarded until 2026-08-18. A tier moving, a claim retiring, a price changing —
every sentence describing it would go stale and nothing would fail. Now the fields prose depends
on (`tier`, `ledger_delta`, `sub_status`, `grut_standing`) are pinned for every node the document
names, along with the standing artifacts it vouches for.

**When the register moves, the check fails and names the node.** That is a prompt, not a lock:
re-read the sentences citing it, reconcile them, then

```
python3 provenance/doc_register_pins.py --accept
```

Re-pinning is a human act and it is a claim: *the prose about this node has been re-read and still
says what the register says.* Refresh it without reading and the machinery is intact while the
book is not — which is the failure this program convicts its own prior deposit of.


## Any claim about the public repository is checked against the public repository

**The trap, recorded because this program fell into it (2026-08-18).** The rebuild tree is the
*source* of a `git subtree` contribution. `git subtree add` rewrites the contributed history into
**new commit objects in the destination**, and the source repository has no knowledge of them. So
a commit hash that is perfectly valid in `github.com/ryangrvr/GRUT-RAI` returns
`fatal: Not a valid object name` when checked from the rebuild tree — and both answers are
correct, because they are answers about different repositories.

What this cost, in full: a verification run in the wrong repository was reported as proof that the
public document cited a nonexistent commit; the "correction" then deleted a true statement and
published a confession to an error that had not occurred. An audit hunting over-claims waved the
resulting *under*-claim straight through.

**The rule:** to check anything the document says about `github.com/ryangrvr/GRUT-RAI` — a commit
hash, a file's presence, a count over the published tree — clone or fetch **that** repository and
run the check there. Naming a repository in a sentence and testing a different one is not a check.


## 2. The full test suite

```bash
cd provenance && python3 -m pytest -q
```
All test files, including the mutation batteries, the prereg seal checks, the consumed-by
trigger, the emergence-chain drift check, and the doc-sync markers. One test is skipped by design
without `GRUT_RUN_SLOW=1`, and it says so.

**The batteries, stated honestly — the earlier wording here was a coverage claim it could not
support.** A mutation battery is a set of pre-registered wrong answers that must make the calc's
own selftest fail. The figures are emitted from `provenance/mutation_registry.py`, never typed
(see `PUBLIC_NUMBERS.md`, and `test_public_doc.py` fails if they drift):

| | |
|---|---|
| mutation batteries | **14** |
| **mutants that run by default** | **33 of 54** |
| cited calcs still owing a battery | **15** |

So *"guards proven to fail on wrong answers"* is true of the batteries that run, and the honest
form of the claim is: **every cited calc ships a battery or is declared owed, and every battery
that exists has been executed at least once.** The second half became true only on 2026-08-19 —
before that, 21 of the 54 mutants had never fired, and one of them had been mis-classified since
the day it was written.

**TWO different environment variables, which this file previously conflated into one:**

```bash
GRUT_FULL_MUTATION=1 python3 -m pytest -q test_mutation_battery.py   # runs the 21 slow mutants
GRUT_RUN_SLOW=1      python3 -m pytest -q                           # the falsifier-execution layer
```

The earlier text said `GRUT_RUN_SLOW=1` ran the slow mutants. It does not. A reader following that
instruction would have left 39% of the mutants unexecuted while the same sentence told them the
guards were proven — the documented procedure could not reproduce the claim beside it. The full
mutation run takes about 50 minutes.

## 3. The seals

```bash
cd provenance && python3 -c "
import hashlib
man=[l.split('  ') for l in open('prereg/MANIFEST.txt') if '  ' in l and not l.startswith('MANIFEST')]
bad=[n.strip() for s,n in man if hashlib.sha256(open('prereg/'+n.strip(),'rb').read()).hexdigest()!=s.strip()]
print('ALL SEALS VERIFY' if not bad else bad)"
```
Every pre-registration is immutable once hashed; results live in separate files citing the seal in
the pinned `sha256 = <64hex>` format. Editing any sealed file breaks this check.

## 4. What a green run does and does not mean

Green means the **discipline** holds: declarations complete, prices summed, seals intact, guards
firing on their mutation batteries. It does **not** certify physical truth — a
wrong-but-well-provenanced claim passes, and the register says so about itself. The claims'
epistemic grades are in their `tier` fields; read those, not the color of the gate.
