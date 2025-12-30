"""
GRUT Battery Physics Module - Dendrite Growth Simulation

Uses the derived G(t) equation to simulate lithium dendrite growth in batteries.
Connects real-time sensor data to the Complexity Tracker (Ξ) and triggers
Metric Stabilizer pulses when dendrite length exceeds safety thresholds.

The ionic memory kernel follows the same retarded potential as GRUT:
K(t) = (α/τ₀) · exp(-t/τ₀)

Where the battery's "memory" of past charging cycles influences current growth.
"""

import numpy as np
from typing import Dict, List, Tuple
from datetime import datetime

from grut_physics import (
    TAU_ZERO,
    ALPHA,
    N_G,
    retarded_potential_kernel,
    complexity_tracker,
    metric_stabilizer
)

DENDRITE_THRESHOLD = 50.0
IONIC_MEMORY_DECAY = 0.01
GROWTH_RATE_CONSTANT = 0.1
RESET_PULSE_STRENGTH = 0.5


class BatteryDendriteSimulator:
    """
    Simulates lithium dendrite growth using GRUT physics.
    
    The G(t) growth equation:
    G(t) = G₀ + ∫₀ᵗ K(t-t') · J(t') dt'
    
    Where:
    - G(t) = dendrite length at time t
    - G₀ = initial nucleation length
    - K(t-t') = retarded potential kernel (ionic memory)
    - J(t') = current density history
    """
    
    def __init__(self, initial_length: float = 0.0):
        self.dendrite_length = initial_length
        self.ionic_memory: List[float] = []
        self.current_history: List[float] = []
        self.time_steps: List[float] = []
        self.stabilizer_pulses: List[Dict] = []
        self.complexity_xi = 0.0
        self.is_critical = False
        
    def calculate_growth_rate(self, current_density: float, time_step: float) -> float:
        """
        Calculate instantaneous growth rate using the G(t) derivative.
        
        dG/dt = Σ K(Δt_i) · J(t_i) for all past current events
        """
        growth_rate = GROWTH_RATE_CONSTANT * current_density
        
        for i, (j, t) in enumerate(zip(self.current_history, self.time_steps)):
            delta_t = time_step - t
            if delta_t > 0:
                kernel_weight = retarded_potential_kernel(delta_t * 1e-6)
                growth_rate += abs(kernel_weight) * j * IONIC_MEMORY_DECAY
                
        return growth_rate * N_G
    
    def step(self, current_density: float, time_step: float) -> Dict:
        """
        Advance simulation by one time step.
        
        Args:
            current_density: Applied current density (A/m²)
            time_step: Current time in simulation
            
        Returns:
            Step result with dendrite state
        """
        self.current_history.append(current_density)
        self.time_steps.append(time_step)
        
        growth_rate = self.calculate_growth_rate(current_density, time_step)
        self.dendrite_length += growth_rate
        
        self.ionic_memory.append(current_density * np.exp(-IONIC_MEMORY_DECAY * time_step))
        
        work_events = [abs(j) / 100.0 for j in self.current_history[-10:]]
        info_state = len(work_events) * 0.1 + 0.1
        self.complexity_xi = complexity_tracker(work_events, info_state)
        
        stabilizer_triggered = False
        if self.dendrite_length >= DENDRITE_THRESHOLD:
            stabilizer_triggered = True
            self._trigger_stabilizer_pulse(time_step)
        
        self.is_critical = self.complexity_xi >= 0.999
        
        return {
            "time": time_step,
            "dendrite_length": round(self.dendrite_length, 4),
            "growth_rate": round(growth_rate, 6),
            "complexity_xi": round(self.complexity_xi, 6),
            "ionic_memory_size": len(self.ionic_memory),
            "is_critical": self.is_critical,
            "stabilizer_triggered": stabilizer_triggered,
            "threshold": DENDRITE_THRESHOLD
        }
    
    def _trigger_stabilizer_pulse(self, time_step: float):
        """
        Trigger a Metric Stabilizer pulse to reset ionic memory.
        High Grit (dendrite stress) leads to Groot (stability).
        """
        seismic_equivalent = self.dendrite_length / DENDRITE_THRESHOLD * 10
        stabilized_alpha, status = metric_stabilizer(self.complexity_xi, seismic_equivalent)
        
        reset_factor = 1.0 - RESET_PULSE_STRENGTH * abs(stabilized_alpha) / abs(ALPHA)
        
        old_length = self.dendrite_length
        self.dendrite_length *= reset_factor
        
        memory_reset_count = int(len(self.ionic_memory) * 0.5)
        self.ionic_memory = self.ionic_memory[memory_reset_count:]
        
        pulse_record = {
            "time": time_step,
            "old_length": round(old_length, 4),
            "new_length": round(self.dendrite_length, 4),
            "reset_factor": round(reset_factor, 4),
            "stabilized_alpha": round(stabilized_alpha, 8),
            "status": status,
            "memory_cleared": memory_reset_count
        }
        
        self.stabilizer_pulses.append(pulse_record)
        print(f"[BATTERY] STABILIZER PULSE: {status}")
        print(f"[BATTERY] Dendrite reset: {old_length:.2f} → {self.dendrite_length:.2f} μm")
        
    def get_state(self) -> Dict:
        """Get current simulator state."""
        return {
            "dendrite_length": round(self.dendrite_length, 4),
            "complexity_xi": round(self.complexity_xi, 6),
            "saturation_percentage": f"{self.complexity_xi * 100:.2f}%",
            "ionic_memory_depth": len(self.ionic_memory),
            "current_history_length": len(self.current_history),
            "is_critical": self.is_critical,
            "stabilizer_pulse_count": len(self.stabilizer_pulses),
            "threshold": DENDRITE_THRESHOLD,
            "last_pulse": self.stabilizer_pulses[-1] if self.stabilizer_pulses else None
        }
    
    def run_simulation(self, current_profile: List[float], dt: float = 1.0) -> Dict:
        """
        Run a full simulation with a current density profile.
        
        Args:
            current_profile: List of current density values over time
            dt: Time step between measurements
            
        Returns:
            Complete simulation results
        """
        results = []
        
        for i, current in enumerate(current_profile):
            time_step = i * dt
            step_result = self.step(current, time_step)
            results.append(step_result)
            
        return {
            "simulation_type": "DENDRITE_GROWTH",
            "total_steps": len(results),
            "final_state": self.get_state(),
            "stabilizer_pulses": self.stabilizer_pulses,
            "peak_length": max(r["dendrite_length"] for r in results),
            "peak_xi": max(r["complexity_xi"] for r in results),
            "steps": results[-10:],
            "timestamp": datetime.utcnow().isoformat()
        }


def connect_sensor_data(sensor_readings: List[Dict]) -> Tuple[List[float], float]:
    """
    Connect real-time monitoring sensor data to the Complexity Tracker.
    
    Converts sensor readings (voltage, current, temperature) into
    work events for Xi calculation.
    
    Args:
        sensor_readings: List of sensor data dicts with 'value' and 'type'
        
    Returns:
        Tuple of (work_events, calculated_xi)
    """
    work_events = []
    
    for reading in sensor_readings:
        value = reading.get("value", 0)
        sensor_type = reading.get("type", "unknown")
        
        if sensor_type == "current":
            work = abs(value) / 100.0 * N_G
        elif sensor_type == "voltage":
            work = abs(value - 3.7) / 1.0 * N_G
        elif sensor_type == "temperature":
            work = max(0, (value - 25) / 50.0) * N_G
        else:
            work = abs(value) / 100.0
            
        work_events.append(work)
    
    info_state = len(work_events) * 0.1 + 0.1
    xi = complexity_tracker(work_events, info_state)
    
    return work_events, xi


def simulate_charging_cycle(
    cycles: int = 10,
    charge_current: float = 50.0,
    discharge_current: float = -30.0
) -> Dict:
    """
    Simulate multiple charge/discharge cycles with dendrite monitoring.
    
    Args:
        cycles: Number of charge/discharge cycles
        charge_current: Charging current density (A/m²)
        discharge_current: Discharging current density (A/m²)
        
    Returns:
        Simulation results with dendrite growth and stabilizer events
    """
    simulator = BatteryDendriteSimulator()
    
    current_profile = []
    for _ in range(cycles):
        current_profile.extend([charge_current] * 10)
        current_profile.extend([discharge_current] * 8)
        current_profile.extend([0.0] * 2)
    
    return simulator.run_simulation(current_profile)


def run_stress_test(
    high_current: float = 100.0,
    duration: int = 50
) -> Dict:
    """
    Stress test: Push dendrite growth past threshold to trigger stabilizer.
    
    Args:
        high_current: High charging current for stress test
        duration: Number of time steps
        
    Returns:
        Stress test results
    """
    simulator = BatteryDendriteSimulator()
    
    current_profile = [high_current * (1 + 0.1 * np.sin(i * 0.5)) for i in range(duration)]
    
    results = simulator.run_simulation(current_profile)
    results["test_type"] = "BATTERY_STRESS_TEST"
    
    return results
