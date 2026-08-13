# How to verify this repository

Everything below is Python 3 stdlib — no dependencies, no network. From a clean checkout:

## 1. The register gates (the product)

```bash
python3 provenance/validate.py
```
Blocking validator: every claim tiered, sourced, falsifiable; the anti-laundering discipline; the
blind ledger sum. Expect `PASS`, the net ledger (**+13**), and the waived-by-stance disclosure
(+8 behind 4 justified waivers) printed on its face.

```bash
python3 provenance/validate_scoped.py
```
The scoped gate: one register, several ledgers (GRUT vs the physics-cluster maps), plus the
cluster typed inventory. GRUT's net must be +13 regardless of cluster contents.

```bash
python3 provenance/bankgate.py
```
The bank-time gate: diffs the working register against the last accepted baseline. `CLEAN` means
no unaccepted change; any edit shows as a flag with severity.

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
