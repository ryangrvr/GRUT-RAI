#!/usr/bin/env python3
"""Benchmark — Phase D8: Coupled Action Closure.

60 checks across 11 sections verifying the coupled action closure analysis.
"""

import sys
import json

from grut.coupled_action_closure import (
    compute_coupled_action,
    coupled_action_result_to_dict,
    CoupledActionParams,
    N_SECTORS,
    N_D7_CHANNELS,
    N_INTERACTION_CANDIDATES,
    N_EL_FIELDS,
    RECOVERY_STATUSES,
    CLOSURE_STATUSES,
    CLASSIFICATION_OPTIONS,
    COUPLED_ACTION_ASSUMPTIONS,
    COUPLED_ACTION_NONCLAIMS,
)

# ---- Harness ----
_passed = 0
_failed = 0


def check(label: str, condition: bool) -> None:
    global _passed, _failed
    if condition:
        _passed += 1
        print(f"  [PASS] {label}")
    else:
        _failed += 1
        print(f"  [FAIL] {label}")


# ---- Compute ----
print("=" * 60)
print("Benchmark — Phase D8: Coupled Action Closure")
print("=" * 60)

params = CoupledActionParams()
result = compute_coupled_action(params)

# ---- Section 1: Constants & Parameters (5 checks) ----
print("\n--- Section 1: Constants & Parameters (5 checks) ---")
check("N_SECTORS = 4", N_SECTORS == 4)
check("N_D7_CHANNELS = 2", N_D7_CHANNELS == 2)
check("N_INTERACTION_CANDIDATES = 4", N_INTERACTION_CANDIDATES == 4)
check("N_EL_FIELDS = 3", N_EL_FIELDS == 3)
check("RECOVERY_STATUSES has 4 values", len(RECOVERY_STATUSES) == 4)

# ---- Section 2: Sector Action Definitions (6 checks) ----
print("\n--- Section 2: Sector Action Definitions (6 checks) ---")
sectors = result.sector_actions
check("Sector actions exist", sectors is not None)
check("4 sectors defined", len(sectors) == 4)
sector_names = [s.name for s in sectors]
check("Gravity sector present", "gravitational" in sector_names)
check("Macro sector present", "macro_scalar_memory" in sector_names)
check("Defect sector present", "defect_triplet" in sector_names)
check("Trigger sector present", "curvature_trigger" in sector_names)

# ---- Section 3: Interaction Candidate Set (5 checks) ----
print("\n--- Section 3: Interaction Candidate Set (5 checks) ---")
interactions = result.interaction_candidates
check("Interaction candidates exist", interactions is not None)
check("4 candidates assessed", len(interactions) == 4)
int_names = [t.name for t in interactions]
check("Gravitational coupling present", "stress_energy_gravitational_coupling" in int_names)
check("Portal coupling present", "scalar_triplet_portal" in int_names)
check("Each has target channel", all(t.target_d7_channel != "" for t in interactions))

# ---- Section 4: Action Assembly (6 checks) ----
print("\n--- Section 4: Action Assembly (6 checks) ---")
action = result.action_candidate
check("Action candidate exists", action is not None)
check("4 sectors in action", action.n_sectors == 4)
check("4 interaction terms assessed", action.n_interaction_terms == 4)
check("6 free parameters", action.n_free_parameters == 6)
check("Action symbolic contains S_grav", "S_grav" in action.full_action_symbolic)
check("Action symbolic contains S_portal", "S_portal" in action.full_action_symbolic)

# ---- Section 5: Euler-Lagrange Derivation (6 checks) ----
print("\n--- Section 5: Euler-Lagrange Derivation (6 checks) ---")
els = result.el_derivations
check("EL derivations exist", els is not None)
check("3 field equations", len(els) == 3)
el_fields = [el.field_name for el in els]
check("Metric EL present", "metric" in el_fields)
check("Macro scalar EL present", "macro_scalar" in el_fields)
check("Defect triplet EL present", "defect_triplet" in el_fields)
metric_el = [el for el in els if el.field_name == "metric"][0]
check("Metric EL identifies back-reaction", "back_reaction_gravitational_penalty" in metric_el.terms_identified)

# ---- Section 6: D7 Channel Recovery Map (6 checks) ----
print("\n--- Section 6: D7 Channel Recovery Map (6 checks) ---")
cr = result.channel_recovery
check("Channel recovery exists", cr is not None)
check("2 channels mapped", cr.n_channels == 2)
check("1 action-derived", cr.n_action_derived == 1)
check("1 derived after approximation", cr.n_derived_after_approximation == 1)
check("0 effective closure", cr.n_effective_closure == 0)
check("Recovery fraction = 0.75", abs(cr.d7_recovery_fraction - 0.75) < 0.01)

# ---- Section 7: Closure Inventory (6 checks) ----
print("\n--- Section 7: Closure Inventory (6 checks) ---")
ci = result.closure_inventory
check("Closure inventory exists", ci is not None)
check("10 items inventoried", ci.n_total == 10)
check("4 action-derived", ci.n_action_derived == 4)
check("3 effective-but-disciplined", ci.n_effective == 3)
check("3 still open", ci.n_open == 3)
check("All statuses valid", all(
    e.status in CLOSURE_STATUSES for e in ci.entries
))

# ---- Section 8: Classification (6 checks) ----
print("\n--- Section 8: Classification (6 checks) ---")
cl = result.classification
check("Classification exists", cl is not None)
check("Classification is valid string", cl.classification in CLASSIFICATION_OPTIONS)
check("Phase lock has D8", "coupled_action_D8" in cl.phase_lock_update)
check("Recovery fraction matches", abs(cl.d7_recovery_fraction - 0.75) < 0.01)
check("n_channels_derived = 1", cl.n_channels_derived == 1)
check("n_channels_approximate = 1", cl.n_channels_approximate == 1)

# ---- Section 9: D7 Consistency (5 checks) ----
print("\n--- Section 9: D7 Consistency (5 checks) ---")
grav_entry = [e for e in cr.entries if e.d7_channel_name == "gravitational_penalty"][0]
amp_entry = [e for e in cr.entries if e.d7_channel_name == "source_amplification"][0]
check("Grav penalty is action_derived", grav_entry.recovery_status == "action_derived")
check("Source amp is derived_after_approximation", amp_entry.recovery_status == "derived_after_approximation")
check("Grav penalty quality is exact", grav_entry.recovery_quality == "exact")
check("Source amp quality is structural", amp_entry.recovery_quality == "structural")
check("Source amp requires approximations", len(amp_entry.approximations_required) >= 2)

# ---- Section 10: Nonclaims & Serialization (4 checks) ----
print("\n--- Section 10: Nonclaims & Serialization (4 checks) ---")
check("10 nonclaims", len(result.nonclaims) == 10)
check("10 assumptions", len(result.assumptions) == 10)
d = coupled_action_result_to_dict(result)
check("Serialization valid JSON", json.dumps(d) is not None)
check("Serialization has classification", "classification" in d)

# ---- Section 11: Structural Consistency (5 checks) ----
print("\n--- Section 11: Structural Consistency (5 checks) ---")
check("Portal term targets source amplification",
      any(t.target_d7_channel.startswith("source_amplification") for t in interactions))
check("Grav coupling targets gravitational penalty",
      any(t.target_d7_channel.startswith("gravitational_penalty") for t in interactions))
check("Portal sign is constructive",
      any(t.name == "scalar_triplet_portal" and t.sign_effect == "constructive" for t in interactions))
check("Grav sign is destructive",
      any(t.name == "stress_energy_gravitational_coupling" and t.sign_effect == "destructive" for t in interactions))
macro_el = [el for el in els if el.field_name == "macro_scalar"][0]
check("Macro EL identifies source amplification pathway",
      "source_amplification_pathway" in macro_el.terms_identified)

# ---- Summary ----
print("\n" + "=" * 60)
total = _passed + _failed
print(f"TOTAL: {_passed}/{total} checks passed, {_failed} failed")
print("=" * 60)

# Key findings
print("\n--- Key Findings ---")
print(f"Classification: {cl.classification}")
print(f"Phase status: {cl.phase_status}")
print(f"D7 recovery fraction: {cr.d7_recovery_fraction:.2f}")
print()
print("Channel recovery map:")
for e in cr.entries:
    print(f"  {e.d7_channel_name} ({e.d7_parameter}): {e.recovery_status}")
    print(f"    Quality: {e.recovery_quality}")
    print(f"    Source: {e.source_term_in_action}")
    if e.approximations_required:
        print(f"    Approximations: {len(e.approximations_required)}")
print()
print("Closure inventory:")
print(f"  Action-derived: {ci.n_action_derived}/{ci.n_total}")
print(f"  Effective-but-disciplined: {ci.n_effective}/{ci.n_total}")
print(f"  Still open: {ci.n_open}/{ci.n_total}")
print()
print(f"Summary: {cl.summary}")

if _failed > 0:
    sys.exit(1)
