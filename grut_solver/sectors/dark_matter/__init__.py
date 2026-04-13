"""
Sector 9 — Dark Matter

Status: Computed (toy model — solitonic DM from fixed-point landscape)

The constitutive potential with multiple minima produces topologically
stable domain wall solitons with:
  - Exact BPS bound (energy matches analytical to 0.0%)
  - Topological charge Q=1 (cannot decay)
  - Survives constitutive evolution with noise
  - Mass range: 10^6 - 10^13 GeV (superheavy / WIMPzilla)
  - Stabilized by anomaly-induced vacuum splitting (C_FINAL)
"""
SECTOR_STATUS = "Closed (gauged extension)"
SECTOR_NAME = "Dark Matter"

COMPUTED_RESULTS = [
    "Double-well potential: 2 stable + 1 unstable fixed points",
    "Domain wall soliton: BPS bound matched to 0.0%",
    "Topological stability: charge Q=1, protected against decay",
    "Constitutive evolution: survives 3000 steps with noise",
    "Mass range: 10^6 - 10^13 GeV (superheavy DM)",
    "Self-interaction: tiny at these masses (Bullet Cluster OK)",
]

NONCLAIMS = [
    "No WIMP-mass candidate (solitons are superheavy)",
    "No relic density calculation",
    "No direct detection prediction",
    "No rotation curve fit",
]

MODULE_MAP = {
    "Soliton DM toy model": "grut_solver.sectors.dark_matter.soliton_dark_matter",
    "Candidate criteria": "grut_solver.sectors.dark_matter.candidate_criteria",
    "Stability checks": "grut_solver.sectors.dark_matter.stability_checks",
}
