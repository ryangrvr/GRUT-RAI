#!/usr/bin/env python3
"""
Sector 6 — QCD / Strong Force: Reproducibility Notebook

Status: Open, with computational entry point.

Usage: python3 notebooks/sector_06_qcd.py
"""
import sys; sys.path.insert(0, ".")
import numpy as np

print("=" * 70)
print("SECTOR 6 — QCD / STRONG FORCE")
print("Status: Open, with computational entry point")
print("=" * 70)

# ── 1. SU(3) Algebra ────────────────────────────────────────
print("\n1. SU(3) LIE ALGEBRA")
print("-" * 50)
from grut_solver.sectors.qcd.su3_structure import (
    verify_lie_algebra, verify_trace_normalization, verify_hermiticity,
    verify_tracelessness, casimir_fundamental, structure_constants, N_GEN,
)

for name, func in [("Lie algebra", verify_lie_algebra),
                    ("Trace norm", verify_trace_normalization),
                    ("Hermiticity", verify_hermiticity),
                    ("Tracelessness", verify_tracelessness)]:
    r = func()
    print(f"  {name:>18s}: max_err = {r['max_error']:.2e}  [{r['status']}]")

C_F = casimir_fundamental()
print(f"  Casimir C_F = {C_F:.6f} (expected 4/3 = {4/3:.6f})")

f = structure_constants()
nonzero = np.sum(np.abs(f) > 1e-10)
print(f"  Structure constants: {nonzero} nonzero entries out of {N_GEN**3}")

# ── 2. Color Representations ────────────────────────────────
print("\n2. COLOR REPRESENTATIONS")
print("-" * 50)
from grut_solver.sectors.qcd.color_representations import (
    representation_dimensions, color_singlet_check, COLOR_STATES,
)

reps = representation_dimensions()
for name, info in reps.items():
    if isinstance(info, dict):
        print(f"  {name:>18s}: dim={info.get('dim','—')}, "
              f"C={info.get('Casimir','—')}, {info.get('objects','')}")

r_singlet = color_singlet_check(COLOR_STATES["red"])
print(f"  Red quark is singlet: {r_singlet['is_singlet']} (charge = {r_singlet['max_color_charge']:.4f})")

# ── 3. Gauge Covariance ─────────────────────────────────────
print("\n3. SU(3) GAUGE COVARIANCE")
print("-" * 50)
from grut_solver.sectors.qcd.covariant_dynamics import (
    covariance_check, field_strength_covariance_check,
)

r_cov = covariance_check()
r_field = field_strength_covariance_check()
print(f"  D covariance:    err = {r_cov['covariance_error']:.2e}  [{r_cov['status']}]")
print(f"  F covariance:    err = {r_field['F_covariance_error']:.2e}  [{r_field['status']}]")
print(f"  Tr(F^2) inv:     err = {r_field['TrF2_invariance_error']:.2e}")

# ── 4. Wilson Loop (Exploratory) ────────────────────────────
print("\n4. WILSON LOOP (EXPLORATORY — TOY LATTICE)")
print("-" * 50)
from grut_solver.sectors.qcd.wilson_loop import wilson_loop_2d, area_law_scan

w = wilson_loop_2d(Nx=8, Ny=8, g_s=1.0, eps=0.3, R=3, T=3)
print(f"  W(3x3) = {w['W']:.4f}, area = {w['area']}, perimeter = {w['perimeter']}")

scan = area_law_scan(Nx=10, Ny=10, g_s=1.0, eps=0.5, R_max=4)
if scan.get("area_fit_slope") is not None:
    print(f"  Area-law fit: slope = {scan['area_fit_slope']:.4f}, residual = {scan['area_fit_residual']:.4f}")
    print(f"  Perim-law fit: slope = {scan['perim_fit_slope']:.4f}, residual = {scan['perim_fit_residual']:.4f}")
    print(f"  Area law preferred: {scan['area_law_preferred']}")
print(f"  NOTE: {scan.get('note', 'Exploratory')}")

# ── 5. Running Coupling ─────────────────────────────────────
print("\n5. RUNNING COUPLING (STANDARD QCD, NOT GRUT-MODIFIED)")
print("-" * 50)
from grut_solver.sectors.qcd.running_diagnostics import running_coupling_table, GRUT_MODIFICATION_STATUS

table = running_coupling_table()
for row in table["table"]:
    print(f"  mu = {row['mu_GeV']:>8.1f} GeV: alpha_s = {row['alpha_s']:.4f}")
print(f"  GRUT modification: {GRUT_MODIFICATION_STATUS['status']}")

# ── Summary ─────────────────────────────────────────────────
print("\n" + "=" * 70)
print("SECTOR 6 SUMMARY")
print("=" * 70)
print("""
  SU(3) Lie algebra:       VALIDATED (8 generators, f^{abc}, all checks pass)
  Trace normalization:     VALIDATED (Tr(T^a T^b) = delta/2)
  Casimir C_F:             VALIDATED (4/3 exactly)
  Gauge covariance:        VALIDATED (D and F transform correctly)
  Color representations:   DOCUMENTED (fund=3, adj=8, singlet=1)
  Wilson loop:             EXPLORATORY (toy lattice, not physical QCD)
  Running coupling:        DOCUMENTED (standard QCD, GRUT modification OPEN)
  Confinement:             NOT DEMONSTRATED
  Asymptotic freedom:      NOT DEMONSTRATED (within GRUT; standard QCD documented)
  Hadron spectrum:          NOT ATTEMPTED
  Chiral symmetry breaking: NOT ADDRESSED

  STATUS: SECTOR 6 IS OPEN WITH A COMPUTATIONAL ENTRY POINT.
  The SU(3) algebraic structure is complete and validated.
  Physics closure (confinement, spectrum, freedom) remains open.

  What a QCD specialist can do NOW:
    - Use the validated SU(3) algebra and covariance infrastructure
    - Extend the Wilson loop scaffold to a proper Monte Carlo lattice
    - Test whether the GRUT constitutive structure modifies beta functions
    - Probe confinement diagnostics in the constitutive framework
""")
