#!/usr/bin/env python3
"""Sector 8 — Neutrinos: Reproducibility Notebook"""
import sys; sys.path.insert(0, ".")
print("=" * 70); print("SECTOR 8 — NEUTRINOS"); print("Status: Open"); print("=" * 70)

from grut_solver.sectors.neutrinos.neutrino_mass_models import mass_scale_scan, MODEL_STATUS
from grut_solver.sectors.neutrinos.pmns_diagnostics import angle_summary
from grut_solver.sectors.neutrinos.oscillation_observables import (
    mass_splitting_summary, oscillation_probability_2flavor)

print("\n1. MASS MODEL ENTRY POINTS")
for m in mass_scale_scan():
    print(f"  {m['model']:>20s}: {m['note']}")
print(f"\n  GRUT-native mechanism: {MODEL_STATUS['GRUT-native mechanism']}")

print("\n2. PMNS MIXING ANGLES (INPUT — not derived)")
a = angle_summary()
for k, v in a.items():
    if k != "note": print(f"  {k:>15s} = {v}")
print(f"  {a['note']}")

print("\n3. MASS SPLITTINGS (INPUT — not derived)")
s = mass_splitting_summary()
print(f"  dm^2_21 = {s['dm2_21_eV2']:.2e} eV^2")
print(f"  dm^2_32 = {s['dm2_32_eV2']:.2e} eV^2")
print(f"  Ordering: {s['ordering']}")

print("\n4. OSCILLATION EXAMPLE (T2K-like)")
P = oscillation_probability_2flavor(dm2=2.5e-3, L_km=295, E_GeV=0.6)
print(f"  P(nu_mu -> nu_e) ~ {P:.4f}")

print("\n" + "=" * 70)
print("STATUS: All data is INPUT. No neutrino mass mechanism derived from GRUT.")
print("=" * 70)
