"""
GRUT Pharmacology Physics Module - Toxicity Wake & Dose Optimization

Uses the Retarded Potential Kernel to model how previous doses influence
current toxicity levels. Implements Metric Friction alerts and dose
optimization based on -1/12 vacuum tension for healing phase transitions.

The Toxicity Wake equation:
T(t) = Σ D(t') · K(t-t')

Where:
- T(t) = cumulative toxicity at time t
- D(t') = dose administered at time t'
- K(t-t') = retarded potential kernel (dose memory decay)
"""

import numpy as np
from typing import Dict, List, Tuple, Optional
from datetime import datetime

from grut_physics import (
    TAU_ZERO,
    ALPHA,
    N_G,
    retarded_potential_kernel
)

TOXICITY_THRESHOLD = 0.8
CRITICAL_TOXICITY = 0.95
HEALING_TARGET = 0.3
DOSE_HALF_LIFE = 24.0
VACUUM_TENSION = -1/12
PHASE_TRANSITION_FACTOR = 0.618


def calculate_toxicity_wake(
    dose_array: List[float],
    time_steps: List[float],
    decay_rate: float = DOSE_HALF_LIFE
) -> Dict:
    """
    Calculate cumulative toxicity using the Retarded Potential Kernel.
    Each previous dose contributes to current toxicity with decay.
    
    T(t) = Σ D(t') · K(t-t')
    
    Args:
        dose_array: List of doses administered at each time step
        time_steps: Corresponding time points (hours)
        decay_rate: Half-life for dose decay (default: 24 hours)
        
    Returns:
        Dict with toxicity timeline and alert status
    """
    if len(dose_array) != len(time_steps):
        raise ValueError("dose_array and time_steps must have same length")
    
    toxicity_timeline = []
    alerts = []
    
    for i, current_time in enumerate(time_steps):
        cumulative_toxicity = 0.0
        dose_contributions = []
        
        for j in range(i + 1):
            dose = dose_array[j]
            dose_time = time_steps[j]
            delta_t = current_time - dose_time
            
            if delta_t >= 0:
                decay_factor = np.exp(-delta_t / decay_rate)
                kernel_weight = abs(retarded_potential_kernel(delta_t * 1e-6))
                
                contribution = dose * decay_factor * (1 + kernel_weight * 1e6)
                cumulative_toxicity += contribution
                
                if contribution > 0.01:
                    dose_contributions.append({
                        "dose_index": j,
                        "dose_value": dose,
                        "delta_t_hours": delta_t,
                        "decay_factor": round(decay_factor, 4),
                        "contribution": round(contribution, 4)
                    })
        
        normalized_toxicity = min(cumulative_toxicity / (len(dose_array) + 1), 1.0)
        
        alert_level = None
        if normalized_toxicity >= CRITICAL_TOXICITY:
            alert_level = "CRITICAL"
            alerts.append({
                "time": current_time,
                "level": "CRITICAL",
                "toxicity": round(normalized_toxicity, 4),
                "message": "METRIC FRICTION EXCEEDED: Immediate intervention required"
            })
        elif normalized_toxicity >= TOXICITY_THRESHOLD:
            alert_level = "WARNING"
            alerts.append({
                "time": current_time,
                "level": "WARNING",
                "toxicity": round(normalized_toxicity, 4),
                "message": "Approaching Metric Friction threshold"
            })
        
        toxicity_timeline.append({
            "time": current_time,
            "cumulative_toxicity": round(cumulative_toxicity, 4),
            "normalized_toxicity": round(normalized_toxicity, 4),
            "alert_level": alert_level,
            "active_dose_contributions": len(dose_contributions)
        })
    
    peak_toxicity = max(t["normalized_toxicity"] for t in toxicity_timeline)
    final_toxicity = toxicity_timeline[-1]["normalized_toxicity"] if toxicity_timeline else 0
    
    return {
        "calculation_type": "TOXICITY_WAKE",
        "dose_count": len(dose_array),
        "time_span_hours": time_steps[-1] - time_steps[0] if time_steps else 0,
        "toxicity_timeline": toxicity_timeline,
        "peak_toxicity": round(peak_toxicity, 4),
        "final_toxicity": round(final_toxicity, 4),
        "threshold": TOXICITY_THRESHOLD,
        "critical_threshold": CRITICAL_TOXICITY,
        "alerts": alerts,
        "alert_count": len(alerts),
        "is_safe": peak_toxicity < TOXICITY_THRESHOLD,
        "timestamp": datetime.utcnow().isoformat()
    }


def optimize_next_dose(
    current_toxicity: float,
    target_effect: float,
    previous_doses: List[float],
    time_since_last_dose: float
) -> Dict:
    """
    Optimize the next dose using -1/12 vacuum tension for healing phase transition.
    
    The optimization uses the principle that the vacuum tension (-1/12) represents
    the ground state residue, and optimal dosing should align with this to enable
    a 'Phase Transition' toward healing.
    
    Optimal dose formula:
    D_next = D_base × φ × (1 + α × (T_target - T_current))
    
    Where:
    - φ = 0.618 (golden ratio phase transition factor)
    - α = -1/12 (vacuum tension)
    - T_target = target toxicity for healing
    - T_current = current toxicity level
    
    Args:
        current_toxicity: Current normalized toxicity level (0-1)
        target_effect: Desired therapeutic effect (0-1)
        previous_doses: List of previous dose values
        time_since_last_dose: Hours since last dose
        
    Returns:
        Dict with optimized dose recommendation
    """
    if not previous_doses:
        base_dose = target_effect * 10
    else:
        base_dose = np.mean(previous_doses)
    
    toxicity_gap = HEALING_TARGET - current_toxicity
    
    vacuum_adjustment = 1 + VACUUM_TENSION * toxicity_gap * 12
    
    time_factor = np.exp(-time_since_last_dose / DOSE_HALF_LIFE)
    residual_effect = base_dose * time_factor * 0.5
    
    optimal_dose = base_dose * PHASE_TRANSITION_FACTOR * vacuum_adjustment
    optimal_dose = max(0, optimal_dose - residual_effect * 0.3)
    
    min_dose = base_dose * 0.25
    max_dose = base_dose * 2.0
    
    if current_toxicity >= TOXICITY_THRESHOLD:
        max_dose = base_dose * 0.5
        optimal_dose = min(optimal_dose, max_dose)
    
    optimal_dose = np.clip(optimal_dose, min_dose, max_dose)
    
    phase_state = "HEALING_TRANSITION" if toxicity_gap > 0 else "TOXICITY_MANAGEMENT"
    if current_toxicity < 0.2:
        phase_state = "MAINTENANCE"
    elif current_toxicity >= CRITICAL_TOXICITY:
        phase_state = "CRITICAL_INTERVENTION"
        optimal_dose = 0
    
    projected_toxicity = current_toxicity * time_factor + (optimal_dose / (base_dose + 1)) * 0.3
    projected_toxicity = min(projected_toxicity, 1.0)
    
    return {
        "optimization_type": "VACUUM_TENSION_DOSE",
        "current_toxicity": round(current_toxicity, 4),
        "target_effect": round(target_effect, 4),
        "healing_target": HEALING_TARGET,
        "base_dose": round(base_dose, 4),
        "optimal_dose": round(optimal_dose, 4),
        "dose_range": {
            "min": round(min_dose, 4),
            "max": round(max_dose, 4)
        },
        "vacuum_tension_factor": round(VACUUM_TENSION, 6),
        "phase_transition_factor": PHASE_TRANSITION_FACTOR,
        "vacuum_adjustment": round(vacuum_adjustment, 4),
        "time_since_last_dose_hours": time_since_last_dose,
        "residual_effect": round(residual_effect, 4),
        "phase_state": phase_state,
        "projected_toxicity": round(projected_toxicity, 4),
        "is_safe_to_dose": current_toxicity < CRITICAL_TOXICITY and optimal_dose > 0,
        "recommendation": _generate_dose_recommendation(phase_state, optimal_dose, current_toxicity),
        "timestamp": datetime.utcnow().isoformat()
    }


def _generate_dose_recommendation(phase_state: str, dose: float, toxicity: float) -> str:
    """Generate human-readable dose recommendation."""
    if phase_state == "CRITICAL_INTERVENTION":
        return "HOLD ALL DOSES. Toxicity critical. Allow clearance before resuming."
    elif phase_state == "TOXICITY_MANAGEMENT":
        return f"Reduced dose of {dose:.2f} units recommended. Monitor closely."
    elif phase_state == "HEALING_TRANSITION":
        return f"Phase transition dose: {dose:.2f} units. Optimal for healing trajectory."
    else:
        return f"Maintenance dose: {dose:.2f} units. Continue current protocol."


def simulate_treatment_protocol(
    initial_dose: float,
    doses_per_day: int,
    treatment_days: int,
    dose_adjustment_factor: float = 1.0
) -> Dict:
    """
    Simulate a complete treatment protocol with toxicity tracking.
    
    Args:
        initial_dose: Starting dose amount
        doses_per_day: Number of doses per day
        treatment_days: Total days of treatment
        dose_adjustment_factor: Multiplier for dose adjustments (1.0 = no change)
        
    Returns:
        Complete treatment simulation results
    """
    hours_between_doses = 24.0 / doses_per_day
    total_doses = doses_per_day * treatment_days
    
    dose_array = []
    time_steps = []
    
    current_dose = initial_dose
    for i in range(total_doses):
        dose_array.append(current_dose)
        time_steps.append(i * hours_between_doses)
        
        current_dose *= dose_adjustment_factor
    
    toxicity_result = calculate_toxicity_wake(dose_array, time_steps)
    
    final_toxicity = toxicity_result["final_toxicity"]
    optimization = optimize_next_dose(
        current_toxicity=final_toxicity,
        target_effect=0.7,
        previous_doses=dose_array[-3:],
        time_since_last_dose=hours_between_doses
    )
    
    return {
        "simulation_type": "TREATMENT_PROTOCOL",
        "protocol": {
            "initial_dose": initial_dose,
            "doses_per_day": doses_per_day,
            "treatment_days": treatment_days,
            "total_doses": total_doses,
            "dose_adjustment_factor": dose_adjustment_factor
        },
        "toxicity_analysis": {
            "peak_toxicity": toxicity_result["peak_toxicity"],
            "final_toxicity": toxicity_result["final_toxicity"],
            "is_safe": toxicity_result["is_safe"],
            "alert_count": toxicity_result["alert_count"]
        },
        "alerts": toxicity_result["alerts"],
        "next_dose_optimization": optimization,
        "toxicity_timeline_summary": [
            toxicity_result["toxicity_timeline"][i] 
            for i in range(0, len(toxicity_result["toxicity_timeline"]), max(1, len(toxicity_result["toxicity_timeline"]) // 10))
        ],
        "timestamp": datetime.utcnow().isoformat()
    }


def check_metric_friction_alert(toxicity: float) -> Dict:
    """
    Check if current toxicity triggers a Metric Friction alert.
    
    Args:
        toxicity: Current normalized toxicity level (0-1)
        
    Returns:
        Alert status and recommended action
    """
    if toxicity >= CRITICAL_TOXICITY:
        return {
            "alert": True,
            "level": "CRITICAL",
            "message": "METRIC FRICTION EXCEEDED: System approaching failure state",
            "toxicity": round(toxicity, 4),
            "threshold": CRITICAL_TOXICITY,
            "action": "IMMEDIATE_INTERVENTION",
            "vacuum_state": "COLLAPSED"
        }
    elif toxicity >= TOXICITY_THRESHOLD:
        return {
            "alert": True,
            "level": "WARNING",
            "message": "Approaching Metric Friction threshold",
            "toxicity": round(toxicity, 4),
            "threshold": TOXICITY_THRESHOLD,
            "action": "REDUCE_DOSE",
            "vacuum_state": "STRESSED"
        }
    elif toxicity >= HEALING_TARGET:
        return {
            "alert": False,
            "level": "ELEVATED",
            "message": "Toxicity elevated but within acceptable range",
            "toxicity": round(toxicity, 4),
            "threshold": TOXICITY_THRESHOLD,
            "action": "MONITOR",
            "vacuum_state": "NOMINAL"
        }
    else:
        return {
            "alert": False,
            "level": "NORMAL",
            "message": "Toxicity within healing range",
            "toxicity": round(toxicity, 4),
            "threshold": TOXICITY_THRESHOLD,
            "action": "CONTINUE_PROTOCOL",
            "vacuum_state": "STABLE"
        }
