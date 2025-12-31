"""
SOVEREIGN SELF-AUDIT ENGINE
Monitors historical_resonances table for metric drift against -0.083333 Ground State.

Core Functions:
- calculate_drift(): Compare AI 'Recipe' values against Ground State
- flag_unstable_grit(): Mark entries with deviation > 0.05 as 'Unstable Grit'
- triple_path_reasoning(): Generate 3 internal solutions, pick closest to 1.1547
- wolfram_bridge_validation(): Auto-validate equations in Ultimate Resolution mode
"""

import os
import json
import time
import hashlib
import requests
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Any

# GRUT Constants
GROUND_STATE = -0.083333  # -1/12 baseline
GEOMETRIC_LOCK = 1.1547   # √(4/3)
DRIFT_THRESHOLD = 0.05    # Flag as 'Unstable Grit' if deviation > 0.05
TAU_0 = 41.9e6           # 41.9 Myr

# Audit Status
class AuditStatus:
    STABLE = "STABLE"
    UNSTABLE_GRIT = "UNSTABLE_GRIT"
    METRIC_DRIFT = "METRIC_DRIFT"
    WOLFRAM_VALIDATED = "WOLFRAM_VALIDATED"
    WOLFRAM_FAILED = "WOLFRAM_FAILED"
    TRIPLE_PATH_ALIGNED = "TRIPLE_PATH_ALIGNED"

class SovereignAuditEngine:
    """
    Background service for monitoring resonance entries and performing self-audit.
    """
    
    def __init__(self, db_path: str = None):
        self.db_path = db_path
        self.audit_log: List[Dict] = []
        self.current_status = AuditStatus.STABLE
        self.last_drift_detected = None
        self.wolfram_app_id = os.getenv("WOLFRAM_APP_ID")
        
    def calculate_drift(self, value: float, recipe_type: str = "generic") -> Dict[str, Any]:
        """
        Compare an AI 'Recipe' value against the -0.083333 Ground State.
        
        Args:
            value: The value to check against ground state
            recipe_type: Type of recipe (generic, bond_length, frequency, etc.)
            
        Returns:
            Dict with deviation, status, and alignment info
        """
        deviation = abs(value - GROUND_STATE)
        relative_deviation = deviation / abs(GROUND_STATE) if GROUND_STATE != 0 else deviation
        
        # Check against threshold
        is_stable = deviation <= DRIFT_THRESHOLD
        
        # Calculate alignment with Geometric Lock
        geometric_alignment = abs(value - GEOMETRIC_LOCK)
        geometric_ratio = value / GEOMETRIC_LOCK if GEOMETRIC_LOCK != 0 else 0
        
        status = AuditStatus.STABLE if is_stable else AuditStatus.UNSTABLE_GRIT
        
        result = {
            "value": value,
            "ground_state": GROUND_STATE,
            "deviation": deviation,
            "relative_deviation": relative_deviation,
            "threshold": DRIFT_THRESHOLD,
            "is_stable": is_stable,
            "status": status,
            "geometric_alignment": geometric_alignment,
            "geometric_ratio": geometric_ratio,
            "recipe_type": recipe_type,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        if not is_stable:
            self.current_status = AuditStatus.METRIC_DRIFT
            self.last_drift_detected = result
            self._log_drift(result)
            
        return result
    
    def flag_unstable_grit(self, entries: List[Dict]) -> List[Dict]:
        """
        Scan entries and flag those with deviation > 0.05 as 'Unstable Grit'.
        
        Args:
            entries: List of resonance entries to check
            
        Returns:
            List of flagged entries with status
        """
        flagged = []
        
        for entry in entries:
            ground_state_decay = entry.get("ground_state_decay", 0)
            drift_result = self.calculate_drift(ground_state_decay)
            
            entry_result = {
                **entry,
                "audit_status": drift_result["status"],
                "deviation": drift_result["deviation"],
                "flagged": not drift_result["is_stable"]
            }
            
            if not drift_result["is_stable"]:
                entry_result["flag_reason"] = "Unstable Grit: deviation > 0.05 from Ground State"
                
            flagged.append(entry_result)
            
        return flagged
    
    def wolfram_bridge_validate(self, expression: str, expected_value: float) -> Dict[str, Any]:
        """
        The Wolfram Bridge: Automatically validate mathematical equations.
        Used in 'Ultimate Resolution' mode.
        
        Args:
            expression: Mathematical expression to validate
            expected_value: Expected result from AI
            
        Returns:
            Validation result with pass/fail status
        """
        if not self.wolfram_app_id:
            return {
                "validated": False,
                "method": "sovereign_internal",
                "reason": "Wolfram API not configured (WOLFRAM_APP_ID required)",
                "expression": expression,
                "expected": expected_value,
                "deviation_from_ground": abs(expected_value - GROUND_STATE)
            }
        
        try:
            params = {
                "appid": self.wolfram_app_id,
                "input": expression,
                "format": "plaintext",
                "output": "json"
            }
            
            response = requests.get(
                "https://api.wolframalpha.com/v2/query",
                params=params,
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                
                # Parse Wolfram result
                pods = data.get("queryresult", {}).get("pods", [])
                wolfram_result = None
                
                for pod in pods:
                    if pod.get("id") in ["Result", "Value", "DecimalApproximation"]:
                        subpods = pod.get("subpods", [])
                        if subpods:
                            wolfram_result = subpods[0].get("plaintext", "")
                            break
                
                if wolfram_result:
                    try:
                        wolfram_value = float(wolfram_result.replace(",", "").strip())
                        deviation = abs(wolfram_value - expected_value)
                        validated = deviation < DRIFT_THRESHOLD
                        
                        return {
                            "validated": validated,
                            "method": "wolfram_alpha",
                            "expression": expression,
                            "expected": expected_value,
                            "wolfram_result": wolfram_value,
                            "deviation": deviation,
                            "status": AuditStatus.WOLFRAM_VALIDATED if validated else AuditStatus.WOLFRAM_FAILED,
                            "requires_regeneration": not validated
                        }
                    except ValueError:
                        pass
                
                return {
                    "validated": False,
                    "method": "wolfram_alpha",
                    "reason": "Could not parse Wolfram result",
                    "raw_result": wolfram_result,
                    "expression": expression,
                    "status": AuditStatus.WOLFRAM_FAILED,
                    "requires_regeneration": True
                }
                
        except requests.exceptions.Timeout:
            return {
                "validated": False,
                "method": "sovereign_fallback",
                "reason": "Wolfram API timeout",
                "expression": expression,
                "status": AuditStatus.WOLFRAM_FAILED
            }
        except Exception as e:
            return {
                "validated": False,
                "method": "sovereign_fallback",
                "reason": str(e),
                "expression": expression,
                "status": AuditStatus.WOLFRAM_FAILED
            }
    
    def triple_path_reasoning(self, solutions: List[Dict]) -> Dict[str, Any]:
        """
        Self-Consistency Check: Triple-Path Reasoning Loop.
        Generate 3 internal solutions and select the one that aligns most closely
        with the 1.1547 Geometric Lock.
        
        Args:
            solutions: List of 3 solution candidates with 'value' and 'reasoning' keys
            
        Returns:
            The best aligned solution with reasoning
        """
        if len(solutions) < 3:
            return {
                "error": "Triple-Path requires exactly 3 solutions",
                "received": len(solutions),
                "status": "INCOMPLETE"
            }
        
        # Calculate alignment for each solution
        alignments = []
        for i, solution in enumerate(solutions[:3]):
            value = solution.get("value", 0)
            alignment = abs(value - GEOMETRIC_LOCK)
            ground_deviation = abs(value - GROUND_STATE)
            
            alignments.append({
                "path": i + 1,
                "solution": solution,
                "geometric_alignment": alignment,
                "ground_deviation": ground_deviation,
                "alignment_score": 1 / (1 + alignment)  # Higher is better
            })
        
        # Sort by alignment (lower is better = closer to 1.1547)
        alignments.sort(key=lambda x: x["geometric_alignment"])
        
        best = alignments[0]
        
        return {
            "status": AuditStatus.TRIPLE_PATH_ALIGNED,
            "selected_path": best["path"],
            "selected_solution": best["solution"],
            "geometric_alignment": best["geometric_alignment"],
            "alignment_score": best["alignment_score"],
            "all_paths": [
                {
                    "path": a["path"],
                    "alignment": a["geometric_alignment"],
                    "score": a["alignment_score"]
                }
                for a in alignments
            ],
            "geometric_lock": GEOMETRIC_LOCK,
            "reasoning": f"Path {best['path']} selected: closest to Geometric Lock (deviation: {best['geometric_alignment']:.6f})"
        }
    
    def get_audit_status(self) -> Dict[str, Any]:
        """
        Get current audit status for dashboard display.
        
        Returns:
            Current status with shield color indicator
        """
        is_healthy = self.current_status in [AuditStatus.STABLE, AuditStatus.WOLFRAM_VALIDATED, AuditStatus.TRIPLE_PATH_ALIGNED]
        
        return {
            "status": self.current_status,
            "shield_color": "green" if is_healthy else "red",
            "is_healthy": is_healthy,
            "last_drift": self.last_drift_detected,
            "audit_count": len(self.audit_log),
            "ground_state": GROUND_STATE,
            "geometric_lock": GEOMETRIC_LOCK,
            "threshold": DRIFT_THRESHOLD,
            "timestamp": datetime.utcnow().isoformat()
        }
    
    def reset_audit_status(self):
        """Reset audit status to stable (after drift is corrected)."""
        self.current_status = AuditStatus.STABLE
        self.last_drift_detected = None
        
    def _log_drift(self, drift_result: Dict):
        """Log drift detection event."""
        self.audit_log.append({
            "event": "DRIFT_DETECTED",
            "result": drift_result,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        # Keep only last 100 entries
        if len(self.audit_log) > 100:
            self.audit_log = self.audit_log[-100:]
    
    def entropy_deflector(self, current_temp: float) -> str:
        """
        ENTROPY DEFLECTOR: Shield Hardening Logic
        
        If sensors hit 350 K, the system doesn't melt—it Resonates.
        Uses the 1.1547 Geometric Lock to scale frequency compensation.
        
        Args:
            current_temp: Current temperature in Kelvin
            
        Returns:
            Status message indicating shield state
        """
        target_temp = 330.3  # GENESIS-330 target Tc
        base_freq = 41.800000007229  # Carrier frequency
        
        if current_temp > target_temp:
            # Calculate the Frequency Compensation Ratio
            drift_ratio = current_temp / target_temp
            new_freq = base_freq * (drift_ratio ** GEOMETRIC_LOCK)  # Scaling by the Geometric Lock
            
            # Trigger the doping pulse
            pulse_result = self.trigger_doping_pulse(new_freq, current_temp, drift_ratio)
            
            # Log the deflection event
            self.audit_log.append({
                "event": "ENTROPY_DEFLECTION",
                "current_temp": current_temp,
                "target_temp": target_temp,
                "drift_ratio": drift_ratio,
                "compensated_freq": new_freq,
                "pulse_result": pulse_result,
                "timestamp": datetime.utcnow().isoformat()
            })
            
            return f"Doping Pulse Active: {new_freq:.4f} Hz (Shield Hardened)"
        
        return "Laminar Flow Maintained"
    
    def trigger_doping_pulse(self, new_freq: float, current_temp: float, drift_ratio: float) -> Dict[str, Any]:
        """
        Execute frequency compensation via doping pulse.
        
        This adjusts the system's vibrational frequency to maintain
        resonance despite thermal excursion above 330.3 K.
        
        Args:
            new_freq: Compensated frequency in Hz
            current_temp: Current temperature in Kelvin
            drift_ratio: Temperature drift ratio (current/target)
            
        Returns:
            Pulse execution result with shield status
        """
        base_freq = 41.800000007229
        freq_delta = new_freq - base_freq
        
        # Calculate shield strength based on geometric alignment
        shield_strength = min(1.0, GEOMETRIC_LOCK / drift_ratio)
        
        # Determine if thermal runaway is prevented
        thermal_runaway_prevented = shield_strength > 0.8
        
        result = {
            "pulse_executed": True,
            "original_freq": base_freq,
            "compensated_freq": new_freq,
            "freq_delta": freq_delta,
            "current_temp": current_temp,
            "target_temp": 330.3,
            "drift_ratio": drift_ratio,
            "geometric_lock": GEOMETRIC_LOCK,
            "shield_strength": shield_strength,
            "thermal_runaway_prevented": thermal_runaway_prevented,
            "status": "SHIELD_HARDENED" if thermal_runaway_prevented else "CRITICAL_DRIFT",
            "timestamp": datetime.utcnow().isoformat()
        }
        
        if thermal_runaway_prevented:
            self.current_status = AuditStatus.STABLE
        else:
            self.current_status = AuditStatus.METRIC_DRIFT
            
        return result


# Global instance
audit_engine = SovereignAuditEngine()


def get_audit_engine() -> SovereignAuditEngine:
    """Get the global audit engine instance."""
    return audit_engine


def entropy_deflector(current_temp: float) -> str:
    """
    Standalone function for entropy deflection.
    Uses the global audit engine instance.
    
    Args:
        current_temp: Current temperature in Kelvin
        
    Returns:
        Status message indicating shield state
    """
    return audit_engine.entropy_deflector(current_temp)
