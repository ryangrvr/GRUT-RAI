"""
Sector 10 — Baryogenesis

Status: Computed (two-route anomaly, within 1 order of observation)

The baryonic anomaly ratio R_B is computed by two independent routes:
  Route 1 (field-content scaling): R_B = 1.018, eta = 2.46e-9
  Route 2 (ABJ + sphaleron):       R_B = 5.9e-5, eta = 5.01e-9
  Observed:                         eta = 6.1e-10

Both routes land within 1 order of magnitude of observation.
The smallness of eta comes from J_CP × K_neq, not from (2-R_B).
"""
SECTOR_STATUS = "Computed (two-route anomaly)"
SECTOR_NAME = "Baryogenesis"

COMPUTED_RESULTS = [
    "ABJ anomaly coefficient: k_B = N_gen/(16π²) = 0.01900 (exact, Adler-Bardeen)",
    "Baryonic field content: 36 quark Weyl, B²-weighted effective = 4.0",
    "R_B Route 1 (scaling): 1.018, eta = 2.46e-9 (4× above observed)",
    "R_B Route 2 (ABJ+sph): 5.9e-5, eta = 5.01e-9 (8× above observed)",
    "Baryonic CTP normalization: S_B = 150.8",
    "Nonequilibrium factor: K_neq = 1.19e-2 (constitutive at EW threshold)",
    "Both routes within 1 order of magnitude of eta = 6.1e-10",
]

NONCLAIMS = [
    "No exact eta match (overestimates by 4-8×)",
    "No CP-violation derivation (J_CP = 3.18e-5 is SM input)",
    "No unique R_B (two routes give different values)",
    "S_B has structural uncertainty of factor 2-3",
]

MODULE_MAP = {
    "Sakharov conditions": "grut_solver.sectors.baryogenesis.sakharov_checks",
    "Fixed-point asymmetry": "grut_solver.sectors.baryogenesis.fixed_point_asymmetry",
    "Baryonic anomaly (R_B)": "grut_solver.sectors.baryogenesis.baryonic_anomaly",
    "Nonequilibrium toy": "grut_solver.sectors.baryogenesis.nonequilibrium_toy",
}
