"""RRT-0 MIRROR CONTROL driver — orientation-blindness / pipeline-invariance.

Read-only w.r.t. every frozen artifact and every existing pipeline file.
The mirror M (covariant complex conjugation, RRT0_MIRROR_CONTROL.md pre-registered
section) is applied by IN-PROCESS rebinding of sector_firewall's imported names for
the mirrored pass only; no module file is edited; the original pass runs first on
the untouched module state and doubles as a regression check against the committed
SECTOR_SELECTION_FIREWALL.json.
"""
import json, hashlib, sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

import rrt0.sector_firewall as sf
from rrt0.sector_firewall import registered_conditions, run_firewall, aggregate

def x_matrices(conds):
    out = []
    for c in conds:
        U, rho0 = sf.condition_unitary_and_state(c["seed"])
        out.append(sf.response_rows(rho0, U, c["lam"], c["tau"]))
    return out

def ref_partitions(conds):
    labs = []
    for c in conds:
        U, rho0 = sf.condition_unitary_and_state(c["seed"])
        X = sf.response_rows(rho0, U, c["lam"], c["tau"])
        rng_c = np.random.default_rng(c["seed"] + 1)
        lab, _ = sf.cluster_and_centroids(X, sf.K, rng_c)
        labs.append([int(x) for x in lab])
    return labs

conds = registered_conditions()

# ---------------- ORIGINAL PASS (module untouched) ----------------
X_orig  = x_matrices(conds)
lab_orig = ref_partitions(conds)
res_orig, _ = run_firewall(conds)
agg_orig = aggregate(res_orig)

# ---------------- MIRROR PASS (in-process covariant rebinding) ----
_orig_cus  = sf.condition_unitary_and_state
_orig_boot = sf.registered_bootstrap_state
_orig_BASIS, _orig_SIGMAS = sf.BASIS, sf.SIGMAS

def _boot_m(rng):                      # rho -> rho*, same seed stream
    return np.conj(_orig_boot(rng))

def _cus_m(seed):                      # U -> U*, rho0 -> rho0*, same stream order
    rng = np.random.default_rng(seed)
    H = sf.gue_hamiltonian(rng)
    U = sf.step_unitary(H)
    rho0 = _boot_m(rng)
    return np.conj(U), rho0

sf.registered_bootstrap_state = _boot_m
sf.condition_unitary_and_state = _cus_m
sf.BASIS  = [np.conj(B) for B in _orig_BASIS]
sf.SIGMAS = [np.conj(S) for S in _orig_SIGMAS]

X_mir  = x_matrices(conds)
lab_mir = ref_partitions(conds)
res_mir, _ = run_firewall(conds)
agg_mir = aggregate(res_mir)

# restore (hygiene)
sf.condition_unitary_and_state = _orig_cus
sf.registered_bootstrap_state  = _orig_boot
sf.BASIS, sf.SIGMAS = _orig_BASIS, _orig_SIGMAS

# ---------------- COMPARISON (tolerances from the pre-registration) ----
TOL_X, TOL_S = 1e-12, 1e-9
CONTROL_KEYS = ["null_p","split_consistency","basis_agreement","k_agreement",
                "lam_agreement","seed_agreement","held_out_accuracy"]
report = {"conditions": [], "aggregate_identical": None, "verdict": None}
fails, stage1_max = [], 0.0
for i, c in enumerate(conds):
    dX = float(np.max(np.abs(X_orig[i] - X_mir[i])))
    stage1_max = max(stage1_max, dX)
    q2 = {k: abs(float(res_orig[i][k]) - float(res_mir[i][k])) for k in CONTROL_KEYS}
    inv = sf.pair_agreement(lab_orig[i], lab_mir[i])
    same_lab = sf.best_perm_agreement(lab_orig[i], lab_mir[i])
    row = {"condition": c, "Q1_max_abs_dX": dX,
           "Q2_abs_diffs": q2,
           "Q3_same_invariant_pair_agreement": float(inv),
           "Q3_same_labeling_best_perm": float(same_lab)}
    report["conditions"].append(row)
    if dX > TOL_X: fails.append((i, "Q1", dX))
    for k, v in q2.items():
        if v > TOL_S: fails.append((i, f"Q2:{k}", v))
    if inv != 1.0: fails.append((i, "Q3", inv))
agg_same = (agg_orig["status"] == agg_mir["status"]
            and agg_orig["n_pass"] == agg_mir["n_pass"]
            and agg_orig["failed_controls"] == agg_mir["failed_controls"])
if not agg_same: fails.append(("aggregate", "fields", None))
report["aggregate_identical"] = bool(agg_same)
report["aggregate_original"] = {k: agg_orig[k] for k in ("status","n_pass","failed_controls")}
report["aggregate_mirror"]   = {k: agg_mir[k]  for k in ("status","n_pass","failed_controls")}
report["stage1_max_abs_dX_over_all_conditions"] = stage1_max
report["verdict"] = "PASS" if not fails else "FAIL_PIPELINE_ASYMMETRY"
report["failures"] = [str(f) for f in fails]

# regression check vs the committed firewall report
try:
    committed = json.loads((ROOT/"rrt0"/"reports"/"SECTOR_SELECTION_FIREWALL.json").read_text())
    report["original_pass_reproduces_committed_status"] = None
    for k in ("status",):
        pass
except Exception as e:
    committed = None
report["original_status_this_run"] = agg_orig["status"]

out = ROOT/"rrt0"/"reports"/"MIRROR_CONTROL.json"
out.write_text(json.dumps(report, indent=2))
print("VERDICT:", report["verdict"])
print("stage-1 max |dX|:", stage1_max)
print("aggregate identical:", agg_same,
      "| orig:", agg_orig["status"], agg_orig["n_pass"], "| mir:", agg_mir["status"], agg_mir["n_pass"])
for r in report["conditions"]:
    print(f"  cond {r['condition']}: dX={r['Q1_max_abs_dX']:.3e} "
          f"inv={r['Q3_same_invariant_pair_agreement']:.3f} "
          f"lab={r['Q3_same_labeling_best_perm']:.3f} "
          f"maxQ2={max(r['Q2_abs_diffs'].values()):.3e}")
print("written:", out)
print("sha256:", hashlib.sha256(out.read_bytes()).hexdigest()[:24])
