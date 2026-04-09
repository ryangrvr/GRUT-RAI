#!/usr/bin/env python3
"""Sector 7 — Flavor / Masses: Reproducibility Notebook"""
import sys; sys.path.insert(0, ".")
print("=" * 70); print("SECTOR 7 — FLAVOR / MASSES"); print("Status: Open"); print("=" * 70)

from grut_solver.sectors.flavor.yukawa_scan import yukawa_table, hierarchy_ratio
from grut_solver.sectors.flavor.ckm_diagnostics import hierarchy_summary

print("\n1. YUKAWA TABLE (FREE — not derived)")
for f in yukawa_table():
    print(f"  {f['name']:>10s}: M={f['M_GeV']:.4f} GeV, y={f['y_f']:.2e}, log10(y)={f['log10_y']:.2f}")
print(f"  Hierarchy: y_top/y_electron = {hierarchy_ratio():.0f}x")

print("\n2. CKM HIERARCHY (INPUT — not derived)")
h = hierarchy_summary()
print(f"  V_us={h['V_us']:.3f}, V_cb={h['V_cb']:.4f}, V_ub={h['V_ub']:.5f}")
print(f"  {h['note']}")

print("\n" + "=" * 70)
print("STATUS: All data is INPUT from the SM. No flavor prediction derived from GRUT.")
print("=" * 70)
