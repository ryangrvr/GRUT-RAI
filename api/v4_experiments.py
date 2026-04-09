"""
GRUT v4 Experiment Endpoints — 9 new application-backed experiments.

These expose the grut_solver/applications/ modules as API endpoints.
Each returns structured JSON with zero free parameters in the gravitational sector.
"""

from __future__ import annotations
from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import List, Optional
import sys, os

# Ensure grut_solver is importable
PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT not in sys.path:
    sys.path.insert(0, PROJECT)

router = APIRouter(prefix="/experiments", tags=["experiments-v4"])


def _sanitize(obj):
    """Recursively convert numpy types and inf/nan to JSON-safe Python types."""
    import numpy as np
    import math
    if isinstance(obj, dict):
        return {k: _sanitize(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return [_sanitize(v) for v in obj]
    elif isinstance(obj, (np.bool_,)):
        return bool(obj)
    elif isinstance(obj, (np.integer,)):
        return int(obj)
    elif isinstance(obj, (np.floating,)):
        v = float(obj)
        if math.isinf(v): return None
        if math.isnan(v): return None
        return v
    elif isinstance(obj, float):
        if math.isinf(obj): return None
        if math.isnan(obj): return None
        return obj
    elif isinstance(obj, np.ndarray):
        return _sanitize(obj.tolist())
    return obj


# ================================================================
# 1. DECOHERENCE BUDGET (the flagship endpoint)
# ================================================================

class DecoherenceBudgetRequest(BaseModel):
    mass_kg: float = Field(1e-14, description="Particle mass [kg]")
    radius_m: float = Field(50e-9, description="Particle radius [m]")
    separation_m: float = Field(100e-9, description="Superposition separation [m]")
    T_env_K: float = Field(10e-3, description="Environment temperature [K]")
    P_Pa: float = Field(1e-10, description="Gas pressure [Pa]")


@router.post("/decoherence_budget")
def decoherence_budget(req: DecoherenceBudgetRequest):
    """Compute the full GRUT decoherence budget. Zero free parameters in gravitational sector."""
    from grut_solver import GRUTSolver
    solver = GRUTSolver()
    r = solver.decoherence(m=req.mass_kg, R=req.radius_m, l=req.separation_m,
                           T_env=req.T_env_K, P=req.P_Pa)
    return _sanitize({
        "lambda_grav_hz": float(r.lambda_grav),
        "lambda_total_hz": float(r.lambda_total),
        "t_coherence_s": float(r.t_coherence),
        "S_extended": float(r.S_extended),
        "suppression_x": float(r.suppression_x),
        "signal_to_noise": float(r.signal_to_noise),
        "binding_channel": str(r.binding_channel),
        "is_grav_dominated": bool(r.is_grav_dominated),
        "is_testable": bool(r.is_testable),
        "competing_models": {
            "dp_point_mass_hz": float(r.lambda_dp_point),
            "csl_grw_hz": float(r.lambda_csl_grw),
            "standard_qm_hz": 0,
        },
        "parameters": {
            "mass_kg": req.mass_kg,
            "radius_m": req.radius_m,
            "separation_m": req.separation_m,
            "T_env_K": req.T_env_K,
            "P_Pa": req.P_Pa,
        },
        "note": "Zero free parameters in the gravitational decoherence sector.",
    })


# ================================================================
# 2. INTERFEROMETRY CATALOG
# ================================================================

@router.post("/interferometry_catalog")
def interferometry_catalog():
    """GRUT predictions for 7 published + 4 proposed interferometry experiments."""
    from grut_solver.applications.double_slit import run_published_catalog, run_proposed_catalog

    published = run_published_catalog()
    proposed = run_proposed_catalog()

    def clean(r):
        return {
            "experiment": r.get("experiment", ""),
            "m_amu": r["m_amu"],
            "lambda_grav_hz": r["lambda_grav_hz"],
            "V_total": r["V_total"],
            "V_drop_from_gravity": r["V_drop_from_gravity"],
            "grav_detectable": bool(r["grav_detectable"]),
        }

    return _sanitize({
        "published": [clean(r) for r in published],
        "proposed": [clean(r) for r in proposed],
        "all_consistent": all(r.get("consistent", True) for r in published),
        "note": "GRUT survives all 7 published experiments. Signal undetectable at these masses.",
    })


# ================================================================
# 3. BULLET CLUSTER
# ================================================================

@router.post("/bullet_cluster")
def bullet_cluster():
    """Bullet Cluster lensing analysis — null result."""
    from grut_solver.applications.bullet_cluster import full_analysis
    a = full_analysis()

    decoh = {}
    for name, r in a["decoherence"].items():
        decoh[name] = {
            "m_solar": r.get("m_solar", 0),
            "lambda_grav_hz": r["lambda_grav_hz"],
            "t_decoherence_s": r["t_decoherence_s"],
        }

    return _sanitize({
        "decoherence": decoh,
        "boundary": {
            "m_boundary_kg": a["boundary"]["m_boundary_kg"],
            "m_boundary_solar": a["boundary"]["m_boundary_solar"],
        },
        "lensing_modified": a["lensing"]["lensing_modified"],
        "weak_field_correction": a["lensing"]["weak_field_correction"],
        "verdict": a["verdict"],
    })


# ================================================================
# 4. OBSERVER HIERARCHY
# ================================================================

class ObserverRequest(BaseModel):
    mass_kg: float = Field(1.0, description="Object mass [kg]")
    separation_m: float = Field(0.01, description="Superposition separation [m]")
    radius_m: float = Field(0.005, description="Object radius [m]")
    T_env_K: float = Field(300, description="Environment temperature [K]")
    P_Pa: float = Field(1e5, description="Gas pressure [Pa]")


@router.post("/observer_hierarchy")
def observer_hierarchy(req: ObserverRequest = ObserverRequest()):
    """Compute measurement timescales — which channel 'observes' first?"""
    from grut_solver.applications.observer_dynamics import measurement_timescale, observer_hierarchy as get_hierarchy

    custom = measurement_timescale(req.mass_kg, req.separation_m, req.radius_m,
                                    req.T_env_K, req.P_Pa)

    hierarchy = get_hierarchy()
    table = []
    for r in hierarchy:
        table.append({
            "name": r["name"],
            "m_kg": r["m_kg"],
            "t_grav_s": r["t_grav"],
            "t_gas_s": r["t_gas"],
            "t_total_s": r["t_total"],
            "fastest_channel": r["fastest_channel"],
        })

    return _sanitize({
        "custom_system": {
            "t_grav_s": custom["t_grav"],
            "t_gas_s": custom["t_gas"],
            "t_total_s": custom["t_total"],
            "fastest_channel": custom["fastest_channel"],
            "gravity_dominant": custom["gravity_dominant"],
        },
        "hierarchy": table,
    })


# ================================================================
# 5. EARLY UNIVERSE
# ================================================================

@router.post("/early_universe")
def early_universe():
    """Gravity vs thermal decoherence across cosmic history."""
    from grut_solver.applications.early_universe import (
        gravity_vs_thermal_history, find_gravity_crossover,
    )

    history = gravity_vs_thermal_history(1e-14, 100e-9, 50e-9)
    crossover = find_gravity_crossover(1e-14, 100e-9, 50e-9)

    table = []
    for r in history:
        table.append({
            "epoch": r["epoch"],
            "T_K": r["T_K"],
            "lambda_grav_hz": r["Lambda_grav_hz"],
            "lambda_thermal_hz": r["Lambda_thermal_hz"],
            "gravity_dominates": r["gravity_dominates"],
        })

    return _sanitize({
        "reference": "m=10pg, l=100nm, R=50nm",
        "history": table,
        "crossover_T_K": crossover.get("crossover_T_K"),
        "note": crossover.get("note", ""),
    })


# ================================================================
# 6. STRUCTURE FORMATION
# ================================================================

@router.post("/structure_formation")
def structure_formation():
    """Quantum-classical boundary across cosmic history."""
    from grut_solver.applications.structure_formation import (
        structure_formation_boundary, decoherence_history,
    )

    sf = structure_formation_boundary()
    history = decoherence_history()

    scales = []
    for r in sf["scales"]:
        scales.append({
            "name": r["name"],
            "m_kg": r["m_kg"],
            "t_decoh_s": r["t_decoh_s"],
            "classical_by_recomb": r["classical_by_recomb"],
        })

    epochs = []
    for r in history:
        epochs.append({
            "epoch": r["epoch"],
            "m_boundary_kg": r["m_boundary_kg"],
        })

    return _sanitize({
        "recombination_scales": scales,
        "boundary_history": epochs,
        "boundary_at_horizon": sf["boundary_at_horizon"],
    })


# ================================================================
# 7. SOLAR SYSTEM FORMATION
# ================================================================

@router.post("/solar_system")
def solar_system_formation():
    """Gravitational decoherence during planetary formation."""
    from grut_solver.applications.solar_system import (
        planetary_formation_hierarchy, dust_to_planet_crossover,
    )

    hierarchy = planetary_formation_hierarchy()
    crossover = dust_to_planet_crossover()

    table = []
    for r in hierarchy:
        table.append({
            "name": r["name"],
            "R_m": r["R_m"],
            "m_kg": r["m_kg"],
            "lambda_grav_hz": r["lambda_grav"],
            "lambda_gas_hz": r["lambda_gas"],
            "gravity_dominant": r["gravity_dominant"],
        })

    return _sanitize({
        "hierarchy": table,
        "crossover_R_m": crossover.get("crossover_R_m"),
        "crossover_note": crossover.get("note", ""),
    })


# ================================================================
# 8. BIOLOGY DECOHERENCE
# ================================================================

@router.post("/biology_decoherence")
def biology_decoherence():
    """Biological decoherence hierarchy — life in the classical regime."""
    from grut_solver.applications.biology import biological_hierarchy

    hierarchy = biological_hierarchy()
    table = []
    for r in hierarchy:
        table.append({
            "name": r["name"],
            "m_kg": r["m_kg"],
            "t_grav_s": r["t_grav_s"],
            "t_water_s": r["t_water_s"],
            "log10_ratio": r["log10_ratio"],
        })

    return _sanitize({
        "hierarchy": table,
        "finding": "Water beats gravity by 10^15 to 10^33 at every biological scale.",
        "note": "Life operates entirely in the thermally-decohered classical regime.",
    })


# ================================================================
# 9. CONSCIOUSNESS (CLOSING CALCULATION)
# ================================================================

@router.post("/consciousness")
def consciousness_calculation():
    """Microtubule / Orch-OR closing calculation."""
    from grut_solver.applications.consciousness import full_analysis

    a = full_analysis()
    d = a["single_dimer"]
    l = a["linear_scaling"]
    w = a["thermal_wall"]
    v = a["verdict"]

    return _sanitize({
        "single_dimer": {
            "mass_Da": d["mass_Da"],
            "lambda_grav_hz": d["lambda_grav_hz"],
            "t_grav_yr": d["t_grav_yr"],
        },
        "linear_scaling": {
            "N_dimers_needed": l["N_dimers_needed"],
            "neurons_needed": l["neurons_needed"],
            "feasible": l["feasible_count"],
        },
        "thermal_wall": {
            "t_water_s": w["t_water_s"],
            "t_grav_s": w["t_grav_s"],
            "orders_gap": w["orders_gap"],
        },
        "verdict": {
            "mathematical_coincidence": v["mathematical_coincidence"],
            "physically_viable": v["physically_viable"],
            "reason": v["reason"],
        },
    })
