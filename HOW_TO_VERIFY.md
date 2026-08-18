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
All test files, including: the mutation batteries (guards proven to FAIL on wrong answers —
`GRUT_RUN_SLOW=1` runs the slow ones and the falsifier-execution layer), the prereg seal checks,
the consumed-by trigger, the emergence-chain drift check, and the doc-sync markers. One test is
skipped by design without `GRUT_RUN_SLOW=1`, and it says so.

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
