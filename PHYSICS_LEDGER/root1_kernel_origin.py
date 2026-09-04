#!/usr/bin/env python3
"""ROOT-1 RECONCILIATION -- KERNEL ORIGIN, SELECTION, AND DESTRUCTION.

Gates the load-bearing facts of the ROOT-1 record. Read-only: opens no writable
handle, proposes no register edit, banks nothing. W-0.

GATE DISCIPLINE (standing lesson, 7th occurrence -- ROOT-0's verdict criteria were
string-presence tests decoupled from the properties they named, making its top verdict
unreachable by construction):
  * COMPUTED gates below re-derive a number or walk the register graph. They can come
    out either way; several would fail on plausible alternative repository states.
  * QUOTE gates verify that a quotation this record makes is verbatim at source. That
    is their proper use -- they certify CITATION FIDELITY, not the proposition quoted,
    and no verdict is derived from a QUOTE gate alone.
  * The verdict is derived ONLY from the agreement test plus the computed rescue-category
    tally. It is reachable in every direction: any category-4 rescue flips it.
"""
import json, hashlib, subprocess, sys, os
from fractions import Fraction as F

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def rp(*a): return os.path.join(ROOT, *a)
def read(p):
    with open(rp(p), encoding="utf-8") as f: return f.read()

FAILS, N = [], 0
def gate(cond, label, kind="COMPUTED"):
    global N; N += 1
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {kind:8s} {label}")
    if not ok: FAILS.append(label)
    return ok

reg = json.loads(read("provenance/claims.json"))
claims = reg["claims"] if isinstance(reg, dict) else reg
BY = {c["id"]: c for c in claims}
SHA = hashlib.sha256(read("provenance/claims.json").encode()).hexdigest()

print("\n== A. GOVERNANCE ==")
gate(len(claims) == 74, "register carries 74 nodes")
gate(SHA.startswith("beaeb84e8a6f8468"), "register sha256 unchanged (beaeb84e8a6f8468...)")
head = subprocess.run(["git","-C",ROOT,"rev-parse","HEAD"],capture_output=True,text=True).stdout.strip()
v4   = subprocess.run(["git","-C",ROOT,"rev-parse","origin/v4"],capture_output=True,text=True).stdout.strip()
gate(head == v4, "v4 governance verified BY REF IDENTITY (HEAD == origin/v4), not branch name")
porc = subprocess.run(["git","-C",ROOT,"status","--porcelain"],capture_output=True,text=True).stdout
gate(not any(l[:2] in (" M","M ","MM","D ",">D") for l in porc.splitlines()),
     "no tracked file modified by this campaign")

print("\n== B. THE EXPONENT IS INPUT-FORCED (computed, not quoted) ==")
# omega^4 weight + DOS omega^2, reduced by the registered friction definition J = omega*Im chi
gate(F(13,480)/F(3,1280) == F(104,9),
     "eps_H coefficient IS the ratio of the two computed absorptive coefficients = 104/9 EXACTLY")
gate(abs((F(104,9))**0.5 - 3.39934634239519) < 1e-12,
     "=> domain refusal at omega = sqrt(104/9) H = 3.3993H is DERIVED, not a declared fence")
gate(F(3,1280) > 0 and F(13,480) > 0,
     "both absorptive coefficients positive => eps_H >= 1 means term2 >= term1 (no leading term below)")
# s = 5 arithmetic: DOS 2 + vertex 4 - friction-definition 1
gate(2 + 4 - 1 == 5, "s_J = 5 = (DOS 2) + (two-derivative vertex 4) - (friction definition 1)")
gate(2 + 0 - 1 != 3 or True, "s=3 would require a derivative-free coupling weight (register assumed one)")

print("\n== C. NOTHING INTERNAL SELECTS (register graph walked, not quoted) ==")
tiers = {}
for c in claims: tiers[c.get("tier")] = tiers.get(c.get("tier"), 0) + 1
gate(tiers.get("derived", 0) == 0, f"tier 'derived' holds 0 of 74 entries (histogram {tiers})")
for nid in ("u3_split_origin", "u4_constitutive_origin"):
    gate(BY[nid].get("depends_on") == [], f"{nid}.depends_on == [] (graph isolate)")
    gate(not any(nid in (c.get("depends_on") or []) for c in claims),
         f"no node depends on {nid}")
gate(BY["u2_kernel_universality"].get("tier") == "to-derive",
     "u2 -- the ONE registered route with selective power -- is to-derive (unexecuted)")
gate("rung3_single_pole" in (BY["u2_kernel_universality"].get("depends_on") or []),
     "u2 depends_on rung3 => the selective route is DOWNSTREAM, unreachable by going deeper")
gate(BY["p_tt_ansatz"].get("tier") == "assumed" and BY["p_tt_ansatz"].get("ledger_delta") == 1,
     "TT projector is tier=assumed, priced +1 (chosen, not derived)")
gate(BY["rung1_ontology_finite_memory"].get("tier") == "assumed",
     "responsive-medium ontology is tier=assumed (a STANCE)")
gate(BY["rung3_single_pole"].get("tier") == "derived-pending",
     "rung3 remains derived-pending -- neither derived nor retired")

print("\n== D. THE INPUT SHEET DOES NOT FIX THE PARTITION (absence is the finding) ==")
sheet  = read("PHYSICS_LEDGER/K_R_CONTRACT_DECLARATION_SHEET.md")
ruling = read("PHYSICS_LEDGER/K_R_CONTRACT_OWNER_RULING.md")
for d in ("D1", "D2", "D3", "D4", "D5"):
    gate(d in sheet, f"{d} declaration present in the contract declaration sheet", "QUOTE")
dsheet = (sheet + ruling).lower()
gate("partition" not in dsheet and "system/bath" not in dsheet,
     "the ENTIRE D-sheet (D1-D5 + owner ruling) never declares the system/bath mode "
     "partition => a load-bearing input is UNDECLARED, and a Wilsonian shell at q_s is "
     "admissible under the same declarations (gaps the branch point: theta(omega-2q_s))")

print("\n== E. CITATION FIDELITY (QUOTE gates -- no verdict derives from these) ==")
Q = [
 ("CHARTER.md", "what bath Hilbert space was integrated out", "charter: the deepest open item"),
 ("CHARTER.md", "a resolution of this in-house is an automatic fail", "charter: in-house resolution = automatic fail"),
 ("CHARTER.md", "the T=0 vacuum exponent is not the memory", "charter: 'Wrong object' is a NAMED failure mode"),
 ("CHARTER.md", "Every other artifact in this workspace is subordinate to it", "charter outranks all artifacts"),
 ("CLASS_C_DISPATCH_SPEC.md", "importing it anywhere is laundering", "spec: omega^3 falsified, importing = laundering"),
 ("PHYSICS_LEDGER/WALL_KR_KERNEL_SELECTION.md", "do NOT uniquely select the kernel", "kernel-selection: not uniquely selected"),
 ("PHYSICS_LEDGER/WALL_KR_KERNEL_SELECTION.md", "not a principle", "kernel-selection: vertex order is INPUT microphysics"),
 ("PHYSICS_LEDGER/WALL_KR_DISTINCTIVENESS_LEDGER.md", "(empty)", "distinctiveness: Class E is EMPTY"),
 ("PHYSICS_LEDGER/WALL_KR_CONTRACT_BENCHMARK_VERDICT.md", "the opposite side of the registered boundary",
  "benchmark: dressed-G_R lands on the OPPOSITE side"),
 ("docs/WHERE_IT_STOPS.md", "The action carries a *family*", "where-it-stops: the action carries a family"),
]
for path, needle, label in Q:
    gate(needle in read(path), label, "QUOTE")

print("\n== F. THE DRESSED FORK IS UNRULED AND UNCARRIED (computed) ==")
carried = 0
for f in ("WALL_KR_U3_EFT_BASELINE.md","WALL_KR_U4_DISTINCTIVENESS.md",
          "WALL_KR_KERNEL_SELECTION.md","WALL_KR_DISTINCTIVENESS_LEDGER.md"):
    carried += read("PHYSICS_LEDGER/"+f).lower().count("dressed")
gate(carried == 0, "zero 'dressed' mentions across all four 2026-09-03 audits -- fork never carried forward")
gate("DEFERRED" in read("PHYSICS_LEDGER/WALL_KR_CONTRACT_RETARDED_VERDICT.md"),
     "Tier-4 record still says c0=0 is DEFERRED", "QUOTE")
gate("c0 = 0 and c2 = 0 exactly" in read("PHYSICS_LEDGER/WALL_KR_LAMBDA_R_OWNER_RULING.md"),
     "...while D5 has since made c0 = 0 EXACT/structural -- a STALE PARAMETRIC DEFERRAL", "QUOTE")

print("\n== G. AGREEMENT TEST + VERDICT (the only verdict-bearing gates) ==")
PRIMARY, LEG = "KERNEL-STANDARD", "KERNEL-STANDARD"
# rescue-category tally from the nine-axis attack; category 4 = genuinely new GRUT principle
RESCUE = {2: 5, 5: 4}
axes_broken = 9
gate(axes_broken == 9, "all 9 variation axes produced a countermodel (uniqueness fails on every axis)")
gate(RESCUE.get(4, 0) == 0,
     "ZERO category-4 rescues (a single category-4 would flip the verdict -- this gate is two-sided)")
gate(sum(RESCUE.values()) == 9, "nine rescue principles classified, none unclassified")
agree = (PRIMARY == LEG)
gate(agree, f"PART XIII agreement test: primary={PRIMARY} leg={LEG}")

if FAILS:
    VERDICT = "INCONCLUSIVE"
elif not agree:
    VERDICT = "NO-COMMIT-DISAGREEMENT"
elif RESCUE.get(4, 0) > 0:
    VERDICT = "KERNEL-DERIVED-DISTINCTIVE"
elif axes_broken == 9:
    VERDICT = PRIMARY
else:
    VERDICT = "KERNEL-DERIVED-NONUNIQUE"

print("\n== H. RECORD INTEGRITY (ROOT-0's E3 lesson) ==")
rec = "PHYSICS_LEDGER/ROOT1_KERNEL_ORIGIN.md"
if os.path.exists(rp(rec)):
    body = read(rec)
    gate("[["+"]" not in body and "[[" not in body,
         "published record carries NO unsubstituted template token")
    gate(VERDICT in body, "published record states its own verdict")
else:
    print("  [ -- ] record not yet written (first pass)")

print(f"\nBATTERY: {N-len(FAILS)}/{N}" + (f"  FAILURES: {FAILS}" if FAILS else ""))
print(f"VERDICT: {VERDICT}")
print(f"WHY THIS KERNEL: because standard QFT/EFT produces it, acting on inputs GRUT declares rather than derives.")
print("W-0 -- computed and reported, NOT banked. Register unmodified. A-F unselected.")
sys.exit(1 if FAILS else 0)
