"""
BaryonicSensorAI - GRUT Theory Simulation Module

Implements core GRUT physics simulations including:
- Bullet Cluster gravitational modeling
- Retarded Potential Kernel calculations
- Gravitational wave signal predictions
- Metric hysteresis dynamics
"""

import math
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
import json


@dataclass
class GRUTConstants:
    """GRUT Universal Constants"""
    tau_0: float = 41.9  # Myr - characteristic delay time
    alpha: float = 0.333333  # coupling strength (1/3)
    n_g: float = 1.1547  # gravitational refractive index
    R_max: str = "Lambda_Limit"
    G: float = 6.67430e-11  # gravitational constant m^3/(kg*s^2)
    c: float = 299792458  # speed of light m/s


class BaryonicSensorAI:
    """
    GRUT Baryonic Sensor AI - Causal Intelligence Simulation Engine
    
    Implements physics-based simulations grounded in Grand Responsive Universe Theory,
    modeling gravitational memory, retarded potentials, and metric hysteresis.
    """
    
    def __init__(self, constants: Optional[Dict] = None):
        self.constants = GRUTConstants()
        if constants:
            self.constants.tau_0 = constants.get('tau_0', 41.9)
            self.constants.alpha = constants.get('alpha', 0.333333)
            self.constants.n_g = constants.get('n_g', 1.1547)
        
        self.complexity_ratio = 0.926  # Baryonic saturation level (Ξ)
        self.context_memory: Dict[int, str] = {}
        self.simulation_history: List[Dict] = []
        self._logic_guard_triggers = 0
    
    def check_logic_guard(self) -> Dict[str, Any]:
        """
        R_max Logic Guard - Ensure Ξ does not exceed 100% (The R_max Limit)
        
        When information density approaches the R_max limit, the guard triggers
        and "recycles" the complexity ratio to a stable state.
        
        Returns:
            Dictionary with guard status and complexity ratio details
        """
        triggered = False
        ratio_before = self.complexity_ratio
        recycling_note = None
        
        if self.complexity_ratio >= 1.0:
            print("R_max Logic Guard Triggered: Recycling Information Density...")
            self.complexity_ratio = 0.8  # Reset to stable state
            self._logic_guard_triggers += 1
            triggered = True
            recycling_note = f"Information density exceeded R_max limit. Recycled from {ratio_before:.4f} to 0.8 (stable state). Total triggers: {self._logic_guard_triggers}"
        
        return {
            "triggered": triggered,
            "complexity_ratio_before": round(ratio_before, 6),
            "complexity_ratio_after": round(self.complexity_ratio, 6),
            "recycling_note": recycling_note,
            "total_triggers": self._logic_guard_triggers,
            "r_max_status": "STABLE" if self.complexity_ratio < 0.9 else "WARNING" if self.complexity_ratio < 1.0 else "EXCEEDED"
        }
    
    def update_complexity_ratio(self, delta: float) -> float:
        """
        Update the complexity ratio by a delta amount
        
        Args:
            delta: Amount to add to complexity ratio
            
        Returns:
            New complexity ratio value
        """
        self.complexity_ratio += delta
        return self.complexity_ratio
    
    def get_retarded_potential_kernel(self, t: float) -> float:
        """
        Calculate the Retarded Potential Kernel K(t)
        
        K(t) = (alpha / tau_0) * exp(-t / tau_0)
        
        This kernel represents gravitational memory decay over cosmic time scales.
        """
        tau_0 = self.constants.tau_0
        alpha = self.constants.alpha
        return (alpha / tau_0) * math.exp(-t / tau_0)
    
    def model_retarded_potential(self, time_scale: List[float], delta_mass: float = 1e30) -> Dict[str, Any]:
        """
        Simulate the Retarded Potential over a time scale
        
        Args:
            time_scale: Array of time values in Myr
            delta_mass: Mass perturbation in kg
        
        Returns:
            Dictionary with time series data and kernel values
        """
        G = self.constants.G
        c = self.constants.c
        tau_0 = self.constants.tau_0
        alpha = self.constants.alpha
        
        kernel_values = []
        potential_values = []
        
        for t in time_scale:
            if t <= 0:
                t = 0.001  # Avoid division by zero
            
            K_t = self.get_retarded_potential_kernel(t)
            kernel_values.append(K_t)
            
            # Retarded gravitational potential
            t_seconds = t * 3.154e13  # Convert Myr to seconds
            phi = (G * delta_mass * K_t) / (c ** 2)
            potential_values.append(phi)
        
        result = {
            "time_scale": list(time_scale),
            "kernel_values": kernel_values,
            "potential_values": potential_values,
            "tau_0": tau_0,
            "alpha": alpha,
            "kernel_formula": f"K(t) = ({alpha}/{tau_0}) * exp(-t/{tau_0})",
            "delta_mass_kg": delta_mass
        }
        
        self.simulation_history.append({
            "type": "retarded_potential",
            "params": {"time_range": [min(time_scale), max(time_scale)], "delta_mass": delta_mass}
        })
        
        return result
    
    def simulate_bullet_cluster(self, 
                                 collision_velocity: float = 4500,
                                 time_since_collision: float = 150,
                                 cluster_separation: float = 720) -> Dict[str, Any]:
        """
        Simulate the Bullet Cluster (1E 0657-558) using GRUT dynamics
        
        The Bullet Cluster is a key test of modified gravity theories.
        GRUT predicts the dark matter offset arises from metric hysteresis.
        
        Args:
            collision_velocity: km/s
            time_since_collision: Myr
            cluster_separation: kpc
        
        Returns:
            Simulation results including predicted offsets
        """
        tau_0 = self.constants.tau_0
        alpha = self.constants.alpha
        n_g = self.constants.n_g
        
        # Calculate kernel weight at time since collision
        K_t = self.get_retarded_potential_kernel(time_since_collision)
        
        # Metric hysteresis creates apparent mass offset
        # The gravitational lensing center lags behind the baryonic center
        hysteresis_factor = 1 - K_t
        
        # Predicted offset in Mpc
        velocity_ratio = collision_velocity / 1000  # Convert to Mm/s scale
        predicted_offset = cluster_separation * hysteresis_factor * velocity_ratio / 100
        
        # Gas-dark matter separation
        gas_dm_separation = cluster_separation * 0.2 * hysteresis_factor
        
        # Lensing mass estimate (GRUT correction)
        baryonic_mass = 2.3e14  # Solar masses (observed)
        apparent_dm_mass = baryonic_mass * (1 + hysteresis_factor * n_g)
        
        result = {
            "cluster_id": "1E 0657-558",
            "collision_velocity_kms": collision_velocity,
            "time_since_collision_myr": time_since_collision,
            "cluster_separation_kpc": cluster_separation,
            "kernel_weight": K_t,
            "hysteresis_factor": hysteresis_factor,
            "predicted_offset_mpc": round(predicted_offset, 3),
            "gas_dm_separation_kpc": round(gas_dm_separation, 1),
            "baryonic_mass_msun": baryonic_mass,
            "apparent_dm_mass_msun": round(apparent_dm_mass, 2),
            "grut_explanation": "Metric hysteresis from gravitational memory creates lensing offset without dark matter particles",
            "constants_used": {
                "tau_0": tau_0,
                "alpha": alpha,
                "n_g": n_g
            }
        }
        
        self.simulation_history.append({
            "type": "bullet_cluster",
            "params": {
                "collision_velocity": collision_velocity,
                "time_since_collision": time_since_collision
            }
        })
        
        return result
    
    def predict_gravitational_wave_residuals(self,
                                              event_type: str = "BH_merger",
                                              source_distance_mpc: float = 40,
                                              chirp_mass_msun: float = 30) -> Dict[str, Any]:
        """
        Predict gravitational wave signal residuals based on GRUT
        
        GRUT predicts small residual drifts in GW signals due to
        metric hysteresis accumulated over propagation distance.
        
        Args:
            event_type: Type of GW event (BH_merger, NS_merger, etc.)
            source_distance_mpc: Distance to source in Mpc
            chirp_mass_msun: Chirp mass in solar masses
        
        Returns:
            Predicted residual characteristics
        """
        tau_0 = self.constants.tau_0
        alpha = self.constants.alpha
        n_g = self.constants.n_g
        c = self.constants.c
        
        # Light travel time in Myr
        distance_mpc_to_mly = 3.262  # 1 Mpc = 3.262 Mly
        light_travel_time_myr = source_distance_mpc * distance_mpc_to_mly
        
        # Accumulated phase drift from metric hysteresis
        phase_drift = alpha * (1 - math.exp(-light_travel_time_myr / tau_0))
        
        # Frequency-dependent dispersion (GRUT predicts slight n_g effect)
        dispersion_factor = (n_g - 1) * source_distance_mpc / 1000
        
        # Residual timing offset in milliseconds
        timing_residual_ms = phase_drift * tau_0 * 1e-3
        
        # Strain amplitude modification
        strain_modification = 1 + dispersion_factor * 0.01
        
        # Update complexity ratio based on simulation parameters
        # Distance and chirp mass contribute to information density
        complexity_delta = (source_distance_mpc / 1000) * 0.01 + (chirp_mass_msun / 100) * 0.005
        self.update_complexity_ratio(complexity_delta)
        
        # Check R_max Logic Guard - safety valve for information density
        logic_guard = self.check_logic_guard()
        
        result = {
            "event_type": event_type,
            "source_distance_mpc": source_distance_mpc,
            "chirp_mass_msun": chirp_mass_msun,
            "light_travel_time_myr": round(light_travel_time_myr, 2),
            "predicted_phase_drift_rad": round(phase_drift, 6),
            "dispersion_factor": round(dispersion_factor, 6),
            "timing_residual_ms": round(timing_residual_ms, 4),
            "strain_modification_factor": round(strain_modification, 6),
            "detectability": "Marginal with current LIGO sensitivity" if abs(phase_drift) < 0.01 else "Potentially detectable",
            "grut_signature": "Cumulative phase drift increasing with distance",
            "logic_guard": logic_guard,
            "constants_used": {
                "tau_0": tau_0,
                "alpha": alpha,
                "n_g": n_g
            }
        }
        
        self.simulation_history.append({
            "type": "gravitational_wave",
            "params": {
                "event_type": event_type,
                "distance": source_distance_mpc
            }
        })
        
        return result
    
    def compute_hubble_tension_correction(self,
                                           local_H0: float = 73.0,
                                           cmb_H0: float = 67.4) -> Dict[str, Any]:
        """
        Compute GRUT correction to the Hubble Tension
        
        GRUT predicts that metric hysteresis causes a systematic difference
        between local and CMB-derived Hubble constant measurements.
        
        Args:
            local_H0: Local measurement (km/s/Mpc)
            cmb_H0: CMB-derived measurement (km/s/Mpc)
        
        Returns:
            Analysis of tension and GRUT correction
        """
        tau_0 = self.constants.tau_0
        alpha = self.constants.alpha
        n_g = self.constants.n_g
        
        # Tension magnitude
        tension = local_H0 - cmb_H0
        tension_sigma = tension / 1.5  # Approximate sigma
        
        # GRUT correction factor
        # Nearby observations accumulate less hysteresis
        z_local = 0.01  # Typical local measurement redshift
        z_cmb = 1100  # CMB redshift
        
        # Lookback time approximation (Myr)
        t_local = z_local * 13700  # Very rough
        t_cmb = 0.38  # CMB epoch ~380,000 years
        
        # Hysteresis correction
        K_local = self.get_retarded_potential_kernel(max(t_local, 1))
        K_cmb = self.get_retarded_potential_kernel(t_cmb)
        
        correction_factor = (1 + alpha * (K_cmb - K_local)) * n_g
        corrected_cmb_H0 = cmb_H0 * correction_factor
        
        residual_tension = local_H0 - corrected_cmb_H0
        
        result = {
            "local_H0": local_H0,
            "cmb_H0": cmb_H0,
            "observed_tension": round(tension, 2),
            "tension_sigma": round(tension_sigma, 1),
            "grut_correction_factor": round(correction_factor, 4),
            "corrected_cmb_H0": round(corrected_cmb_H0, 2),
            "residual_tension": round(residual_tension, 2),
            "resolution_status": "Partially resolved" if abs(residual_tension) < abs(tension) * 0.5 else "Requires further analysis",
            "mechanism": "Metric hysteresis causes H0 to appear lower at high redshift",
            "constants_used": {
                "tau_0": tau_0,
                "alpha": alpha,
                "n_g": n_g
            }
        }
        
        self.simulation_history.append({
            "type": "hubble_tension",
            "params": {"local_H0": local_H0, "cmb_H0": cmb_H0}
        })
        
        return result
    
    def get_interdisciplinary_connections(self) -> Dict[str, Any]:
        """
        Map interdisciplinary connections within GRUT framework
        
        Returns:
            Network of conceptual connections
        """
        connections = {
            "physics_mathematics": [
                {"from": "Hubble Tension", "to": "Poincare Geometry", "relation": "Non-Euclidean cosmic structure"},
                {"from": "Primes as Grains", "to": "Mass Quantization", "relation": "Discrete matter distribution"},
                {"from": "Gravity", "to": "Memory Dynamics", "relation": "Retarded potential kernel"}
            ],
            "cosmology_philosophy": [
                {"from": "Dark Matter", "to": "Metric Hysteresis", "relation": "Apparent vs intrinsic mass"},
                {"from": "Causality", "to": "Light Cone Structure", "relation": "Information propagation limits"},
                {"from": "Observer", "to": "Measurement", "relation": "Causal participation in universe"}
            ],
            "observational_theoretical": [
                {"from": "Bullet Cluster", "to": "GRUT Prediction", "relation": "Lensing offset from memory"},
                {"from": "GW Signals", "to": "Residual Drift", "relation": "Cumulative phase effects"},
                {"from": "CMB Peaks", "to": "tau_0 Signature", "relation": "Delay scale imprint"}
            ]
        }
        
        return {
            "framework": "GRUT Interdisciplinary Network",
            "connections": connections,
            "core_principle": "The Universe is a closed loop of Light looking at itself through the lens of Time",
            "key_parameters": asdict(self.constants)
        }
    
    def simulate_philosophical_objections(self) -> Dict[str, Any]:
        """
        Address mainstream physics objections to GRUT
        
        Returns:
            Objections with GRUT responses
        """
        objections = [
            {
                "objection": "Cold Dark Matter explains galaxy rotation curves",
                "category": "Empirical",
                "grut_response": "GRUT's metric hysteresis produces identical rotation curve shapes without exotic particles. The retarded potential kernel creates an effective mass enhancement that mimics CDM profiles.",
                "key_prediction": "Rotation curve shape should correlate with galaxy formation epoch (older galaxies = more hysteresis)"
            },
            {
                "objection": "CMB third acoustic peak requires dark matter",
                "category": "Cosmological",
                "grut_response": "The third peak amplitude can be matched by adjusting tau_0 and alpha. The gravitational memory imprint on baryon-photon oscillations produces the observed damping.",
                "key_prediction": "Subtle phase shifts in higher-order peaks that CDM cannot produce"
            },
            {
                "objection": "Structure formation requires cold dark matter seeds",
                "category": "Theoretical",
                "grut_response": "GRUT's n_g > 1 gravitational index creates effective amplification of baryonic density perturbations. Early universe memory effects provide equivalent seeding.",
                "key_prediction": "Small-scale structure cutoff at scales related to tau_0"
            },
            {
                "objection": "Occam's Razor favors particle dark matter",
                "category": "Philosophical",
                "grut_response": "GRUT uses fewer free parameters (tau_0, alpha, n_g) than CDM+Lambda cosmology. It unifies dark matter, dark energy, and modified gravity into a single framework.",
                "key_prediction": "Single theory explains multiple phenomena vs. separate entities for each"
            }
        ]
        
        return {
            "framework": "GRUT Philosophical Defense",
            "objections_addressed": len(objections),
            "objections": objections,
            "methodology": "Each objection is countered with a specific GRUT mechanism and a unique prediction that can distinguish GRUT from CDM"
        }
    
    def get_simulation_summary(self) -> Dict[str, Any]:
        """Get summary of all simulations run in this session"""
        return {
            "total_simulations": len(self.simulation_history),
            "history": self.simulation_history,
            "complexity_ratio": self.complexity_ratio,
            "current_constants": asdict(self.constants)
        }
    
    def to_dict(self) -> Dict[str, Any]:
        """Serialize sensor state to dictionary"""
        return {
            "constants": asdict(self.constants),
            "complexity_ratio": self.complexity_ratio,
            "simulation_count": len(self.simulation_history)
        }


class GWSensor(BaryonicSensorAI):
    """
    Gravitational Wave Sensor - Extended BaryonicSensorAI for GW signal analysis
    
    Specialized for analyzing gravitational wave ringdown memory effects
    using GRUT relaxation constants.
    """
    
    def __init__(self, constants: Optional[Dict] = None):
        super().__init__(constants)
        # tau_0 in seconds: 41.9 Myr * (1e6 years) * (365.25 days) * (24 hours) * (3600 seconds)
        self.tau_0_seconds = 41.9 * 1e6 * 365.25 * 24 * 3600  # ~1.32e15 seconds
    
    def analyze_ringdown_memory(self, signal_duration_seconds: float, snr_ratio: float) -> Dict[str, Any]:
        """
        Analyze gravitational wave ringdown memory effects using GRUT relaxation.
        
        Calculates if the observed signal has a decaying 'offset' matching
        the GRUT relaxation constant tau_0.
        
        Args:
            signal_duration_seconds: Duration of the GW signal in seconds
            snr_ratio: Signal-to-noise ratio of the detection (e.g., 80 for GW250114)
        
        Returns:
            Dictionary with ringdown analysis results including metric drift
        """
        # Time array for the 'long-tail' relaxation (1000 sample points)
        num_samples = 1000
        t = [i * signal_duration_seconds / num_samples for i in range(num_samples)]
        
        # Predicted GRUT Decay: exp(-t / tau_0)
        expected_decay = [math.exp(-ti / self.tau_0_seconds) for ti in t]
        
        # Memory Burden factor - higher SNR means more detectable burden
        # Scale to strain units (dimensionless, ~1e-21 for GW signals)
        burden_factor = (snr_ratio / 100) * 1e-21
        
        # Calculate the predicted metric drift
        predicted_drift = [burden_factor * decay for decay in expected_decay]
        mean_drift = sum(predicted_drift) / len(predicted_drift)
        
        # Update complexity ratio based on SNR (higher SNR = more information)
        complexity_delta = snr_ratio / 1000
        self.update_complexity_ratio(complexity_delta)
        logic_guard_result = self.check_logic_guard()
        
        # Calculate decay metrics
        initial_drift = predicted_drift[0]
        final_drift = predicted_drift[-1]
        decay_ratio = final_drift / initial_drift if initial_drift > 0 else 0
        
        result = {
            "analysis_type": "GW_Ringdown_Memory",
            "signal_duration_seconds": signal_duration_seconds,
            "snr_ratio": snr_ratio,
            "tau_0_seconds": self.tau_0_seconds,
            "tau_0_myr": self.constants.tau_0,
            "burden_factor_strain": burden_factor,
            "mean_metric_drift": mean_drift,
            "initial_drift": initial_drift,
            "final_drift": final_drift,
            "decay_ratio": decay_ratio,
            "sample_points": num_samples,
            "grut_prediction": f"Metric drift of {mean_drift:.2e} strain over {signal_duration_seconds}s signal",
            "logic_guard": logic_guard_result,
            "complexity_ratio": self.complexity_ratio
        }
        
        self.simulation_history.append({
            "type": "gw_ringdown_memory",
            "params": {
                "signal_duration": signal_duration_seconds,
                "snr": snr_ratio
            }
        })
        
        return result


# Factory function for creating sensors with custom constants
def create_baryonic_sensor(constants: Optional[Dict] = None) -> BaryonicSensorAI:
    """Create a new BaryonicSensorAI instance with optional custom constants"""
    return BaryonicSensorAI(constants)


def create_gw_sensor(constants: Optional[Dict] = None) -> GWSensor:
    """Create a new GWSensor instance with optional custom constants"""
    return GWSensor(constants)


class IntegratedBaryonicSensor(GWSensor):
    """
    Integrated Baryonic Sensor - Extended GWSensor with NANOGrav PTA correlation
    
    Cross-correlates single gravitational wave event drifts against the
    Common Red Noise detected by Pulsar Timing Arrays (PTAs).
    """
    
    def cross_correlate_nanograv(self, single_event_drift: float) -> Dict[str, Any]:
        """
        Compare a single merger's drift against the Common Red Noise 
        detected by Pulsar Timing Arrays (PTAs).
        
        Args:
            single_event_drift: The metric drift from a single GW event (strain units)
        
        Returns:
            Dictionary with correlation results and status
        """
        # NANOGrav reported Red Noise Amplitude (A_cp ~ 2e-15 at f=1yr^-1)
        pta_noise_amplitude = 2.4e-15
        
        # Calculate the "Weight" of our single event in the cosmic background
        # Single event drift is typically 1e-21, so we calculate density
        correlation_index = (single_event_drift / pta_noise_amplitude) * 1e6
        
        print(f"Cross-Correlating with NANOGrav Background...")
        
        match_found = 0.1 < correlation_index < 10
        
        if match_found:
            print("MATCH FOUND: Single event drift is a valid component of Common Red Noise.")
            self.complexity_ratio -= 0.05  # Complexity drops as patterns unify
            status = "Observation Matches GRUT Memory Background"
            interpretation = "The single event's metric drift is consistent with the Common Red Noise amplitude, suggesting gravitational wave memory contributes to the PTA signal"
        else:
            print("Variance Detected: Seeking additional Metric Stressors.")
            status = "Inconclusive - Requires more Baryonic Data"
            interpretation = "Correlation index outside expected range; additional data needed to establish connection"
        
        # Check logic guard after complexity update
        logic_guard_result = self.check_logic_guard()
        
        result = {
            "analysis_type": "NANOGrav_Cross_Correlation",
            "single_event_drift": single_event_drift,
            "pta_noise_amplitude": pta_noise_amplitude,
            "correlation_index": correlation_index,
            "correlation_range": [0.1, 10],
            "match_found": match_found,
            "status": status,
            "interpretation": interpretation,
            "complexity_adjustment": -0.05 if match_found else 0,
            "final_complexity_ratio": self.complexity_ratio,
            "logic_guard": logic_guard_result
        }
        
        self.simulation_history.append({
            "type": "nanograv_correlation",
            "params": {"single_event_drift": single_event_drift}
        })
        
        return result
    
    def run_full_pipeline(self, signal_duration_seconds: float = 1.5, snr_ratio: float = 80) -> Dict[str, Any]:
        """
        Execute the full analysis pipeline:
        1. Analyze ringdown memory for a specific event
        2. Cross-correlate with NANOGrav 15-year dataset
        
        Args:
            signal_duration_seconds: Duration of the GW signal
            snr_ratio: Signal-to-noise ratio of the detection
        
        Returns:
            Combined results from both analyses
        """
        # Step 1: Analyze specific GW event
        ringdown_result = self.analyze_ringdown_memory(signal_duration_seconds, snr_ratio)
        event_drift = ringdown_result["mean_metric_drift"]
        
        # Step 2: Correlate with the PTA dataset
        correlation_result = self.cross_correlate_nanograv(event_drift)
        
        return {
            "pipeline": "Full Baryonic Analysis v6",
            "step_1_ringdown": ringdown_result,
            "step_2_correlation": correlation_result,
            "final_status": correlation_result["status"],
            "final_complexity_ratio": self.complexity_ratio,
            "grut_conclusion": "Single merger events contribute to the Stochastic Gravitational Wave Background via GRUT memory accumulation" if correlation_result["match_found"] else "Further observation required to confirm GRUT memory contribution"
        }


def create_integrated_sensor(constants: Optional[Dict] = None) -> IntegratedBaryonicSensor:
    """Create a new IntegratedBaryonicSensor instance with optional custom constants"""
    return IntegratedBaryonicSensor(constants)
