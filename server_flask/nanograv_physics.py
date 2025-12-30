"""
GRUT NANOGrav PTA Integration Module - Gravitational Wave Correlation

Integrates NANOGrav Pulsar Timing Array data with GRUT physics for
gravitational wave background correlation analysis.

The NANOGrav 15-year data release detected a stochastic gravitational wave
background. GRUT interprets this as evidence of the Retarded Potential
operating at cosmological scales.

Key correlations:
- Common Red Noise: Interpreted as τ₀ = 41.9 Myr memory signature
- Hellings-Downs curve: Spatial correlation from n_g = 1.1547 boost
- Strain amplitude: h_c ~ 2.4 × 10⁻¹⁵ at f = 1/yr
"""

import numpy as np
from typing import Dict, List, Tuple, Optional
from datetime import datetime

from grut_physics import (
    TAU_ZERO,
    ALPHA,
    N_G,
    retarded_potential_kernel,
    complexity_tracker
)

NANOGRAV_STRAIN = 2.4e-15
NANOGRAV_FREQ = 1.0 / (365.25 * 24 * 3600)
NANOGRAV_SPECTRAL_INDEX = -2/3
CORRELATION_THRESHOLD_LOW = 0.1
CORRELATION_THRESHOLD_HIGH = 10.0


class NANOGravCorrelator:
    """
    Correlates GRUT physics predictions with NANOGrav PTA observations.
    
    The Common Red Noise detected by NANOGrav is interpreted as the
    gravitational memory signature of the Retarded Potential Kernel.
    """
    
    def __init__(self):
        self.pta_amplitude = NANOGRAV_STRAIN
        self.reference_freq = NANOGRAV_FREQ
        self.spectral_index = NANOGRAV_SPECTRAL_INDEX
        self.correlation_history: List[Dict] = []
        
    def calculate_hellings_downs(self, angle_degrees: float) -> float:
        """
        Calculate the Hellings-Downs correlation coefficient.
        
        For GW background, the correlation between pulsar pairs depends
        on their angular separation following the HD curve.
        
        HD(θ) = (1/2) - (1/4)(1 - cos(θ))/2 + (3/2)((1-cos(θ))/2)ln((1-cos(θ))/2)
        
        GRUT modification: Boost by n_g for gravitational index effect.
        
        Args:
            angle_degrees: Angular separation between pulsar pair
            
        Returns:
            Hellings-Downs correlation coefficient
        """
        theta = np.radians(angle_degrees)
        x = (1 - np.cos(theta)) / 2
        
        if x < 1e-10:
            hd = 0.5
        else:
            hd = 0.5 - 0.25 * x + 1.5 * x * np.log(x)
        
        grut_hd = hd * N_G
        
        return float(np.clip(grut_hd, -1, 1))
    
    def calculate_strain_spectrum(self, frequencies: List[float]) -> List[Dict]:
        """
        Calculate the GW strain power spectrum.
        
        h_c(f) = A × (f/f_ref)^α
        
        Where A = 2.4×10⁻¹⁵ and α = -2/3 (from NANOGrav 15-year)
        
        Args:
            frequencies: List of frequencies in Hz
            
        Returns:
            List of strain values at each frequency
        """
        spectrum = []
        
        for f in frequencies:
            strain = self.pta_amplitude * (f / self.reference_freq) ** self.spectral_index
            
            kernel_boost = 1 + abs(retarded_potential_kernel(1 / f)) * 1e10
            grut_strain = strain * kernel_boost
            
            spectrum.append({
                "frequency_hz": f,
                "period_years": 1 / (f * 365.25 * 24 * 3600),
                "strain_nanograv": strain,
                "strain_grut": grut_strain,
                "kernel_boost": kernel_boost
            })
        
        return spectrum
    
    def cross_correlate_event(
        self,
        event_strain: float,
        event_frequency: float,
        event_duration_days: float
    ) -> Dict:
        """
        Cross-correlate a single GW event with NANOGrav background.
        
        Compares individual event drift against the Common Red Noise.
        If correlation index is within [0.1, 10], patterns unify.
        
        Args:
            event_strain: Detected strain amplitude
            event_frequency: Event frequency in Hz
            event_duration_days: Duration of the event
            
        Returns:
            Correlation analysis result
        """
        expected_strain = self.pta_amplitude * (event_frequency / self.reference_freq) ** self.spectral_index
        
        if expected_strain > 0:
            correlation_index = event_strain / expected_strain
        else:
            correlation_index = 0
        
        patterns_unified = CORRELATION_THRESHOLD_LOW <= correlation_index <= CORRELATION_THRESHOLD_HIGH
        
        if patterns_unified:
            complexity_drop = 0.05
            status = "PATTERNS_UNIFIED"
            message = "Event correlates with NANOGrav background. Complexity reduced."
        elif correlation_index < CORRELATION_THRESHOLD_LOW:
            complexity_drop = 0
            status = "BELOW_THRESHOLD"
            message = "Event strain below NANOGrav correlation threshold."
        else:
            complexity_drop = 0
            status = "ABOVE_THRESHOLD"
            message = "Event strain exceeds NANOGrav correlation range."
        
        result = {
            "event_strain": event_strain,
            "event_frequency_hz": event_frequency,
            "event_duration_days": event_duration_days,
            "expected_strain": expected_strain,
            "correlation_index": round(correlation_index, 6),
            "correlation_range": [CORRELATION_THRESHOLD_LOW, CORRELATION_THRESHOLD_HIGH],
            "patterns_unified": patterns_unified,
            "complexity_drop": complexity_drop,
            "status": status,
            "message": message,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        self.correlation_history.append(result)
        return result
    
    def analyze_pulsar_timing_residuals(
        self,
        residuals_ns: List[float],
        observation_times_mjd: List[float]
    ) -> Dict:
        """
        Analyze pulsar timing residuals for GW signature.
        
        The residuals encode the integrated effect of passing GWs.
        GRUT interprets periodic residuals as Retarded Potential memory.
        
        Args:
            residuals_ns: Timing residuals in nanoseconds
            observation_times_mjd: Modified Julian Dates of observations
            
        Returns:
            Residual analysis with GW signature detection
        """
        residuals = np.array(residuals_ns)
        times = np.array(observation_times_mjd)
        
        rms_residual = np.sqrt(np.mean(residuals ** 2))
        
        time_span_days = times[-1] - times[0] if len(times) > 1 else 0
        time_span_years = time_span_days / 365.25
        
        if len(residuals) > 10:
            fft_residuals = np.fft.fft(residuals)
            power_spectrum = np.abs(fft_residuals) ** 2
            dominant_freq_idx = np.argmax(power_spectrum[1:len(power_spectrum)//2]) + 1
            
            sample_rate = len(residuals) / time_span_days if time_span_days > 0 else 1
            dominant_period_days = len(residuals) / (dominant_freq_idx * sample_rate) if dominant_freq_idx > 0 else 0
        else:
            dominant_period_days = 0
            power_spectrum = []
        
        tau_0_days = TAU_ZERO * 365.25 * 1e6
        if dominant_period_days > 0:
            tau_ratio = tau_0_days / dominant_period_days
            memory_signature = abs(1 - (tau_ratio % 1))
        else:
            memory_signature = 0
        
        induced_strain = rms_residual * 1e-9 / (3e8 * time_span_years * 3.15e7) if time_span_years > 0 else 0
        
        work_events = [abs(r) / 1000 for r in residuals[-20:]]
        info_state = len(work_events) * 0.1 + 0.1
        complexity_xi = complexity_tracker(work_events, info_state)
        
        return {
            "analysis_type": "PULSAR_TIMING_RESIDUALS",
            "observation_count": len(residuals),
            "time_span_years": round(time_span_years, 2),
            "rms_residual_ns": round(rms_residual, 2),
            "dominant_period_days": round(dominant_period_days, 2),
            "induced_strain_estimate": induced_strain,
            "memory_signature_strength": round(memory_signature, 4),
            "complexity_xi": round(complexity_xi, 6),
            "gw_detection": rms_residual > 100 and memory_signature > 0.1,
            "timestamp": datetime.utcnow().isoformat()
        }
    
    def get_nanograv_15yr_summary(self) -> Dict:
        """
        Return summary of NANOGrav 15-year data release key findings.
        
        Returns:
            Dict with key observational parameters
        """
        return {
            "dataset": "NANOGrav 15-year",
            "publication_year": 2023,
            "pulsars_observed": 67,
            "observation_span_years": 15,
            "key_findings": {
                "stochastic_background_detected": True,
                "strain_amplitude_1yr": "2.4 × 10⁻¹⁵",
                "spectral_index": "-2/3",
                "hellings_downs_evidence": "3.5σ",
                "interpretation": "Supermassive black hole binary population"
            },
            "grut_interpretation": {
                "common_red_noise": "τ₀ = 41.9 Myr memory signature",
                "hellings_downs_boost": f"n_g = {N_G} gravitational index",
                "strain_correlation": "Retarded Potential Kernel at cosmological scale",
                "complexity_link": "Ξ fluctuations correlate with GW strain variations"
            },
            "constants": {
                "tau_0_myr": TAU_ZERO / 1e6,
                "alpha": ALPHA,
                "n_g": N_G
            }
        }


def create_correlator() -> NANOGravCorrelator:
    """Factory function to create a NANOGrav correlator instance."""
    return NANOGravCorrelator()


def quick_gw_correlation(
    event_strain: float,
    event_frequency: float = 3.17e-8
) -> Dict:
    """
    Quick correlation check for a GW event against NANOGrav background.
    
    Args:
        event_strain: Detected strain amplitude
        event_frequency: Event frequency (default: 1/year in Hz)
        
    Returns:
        Correlation result
    """
    correlator = NANOGravCorrelator()
    return correlator.cross_correlate_event(event_strain, event_frequency, 365.25)


def generate_hellings_downs_curve(num_points: int = 36) -> List[Dict]:
    """
    Generate the Hellings-Downs correlation curve.
    
    Args:
        num_points: Number of angular points to calculate
        
    Returns:
        List of (angle, correlation) pairs
    """
    correlator = NANOGravCorrelator()
    curve = []
    
    for i in range(num_points + 1):
        angle = i * 180 / num_points
        hd_value = correlator.calculate_hellings_downs(angle)
        curve.append({
            "angle_degrees": angle,
            "hellings_downs_standard": hd_value / N_G,
            "hellings_downs_grut": hd_value,
            "n_g_boost": N_G
        })
    
    return curve


def analyze_pta_frequencies(
    min_freq_hz: float = 1e-9,
    max_freq_hz: float = 1e-7,
    num_points: int = 20
) -> Dict:
    """
    Analyze the PTA frequency band for GW strain.
    
    Args:
        min_freq_hz: Minimum frequency
        max_freq_hz: Maximum frequency
        num_points: Number of frequency points
        
    Returns:
        Frequency band analysis
    """
    correlator = NANOGravCorrelator()
    
    frequencies = np.logspace(np.log10(min_freq_hz), np.log10(max_freq_hz), num_points)
    spectrum = correlator.calculate_strain_spectrum(frequencies.tolist())
    
    peak_strain = max(s["strain_grut"] for s in spectrum)
    peak_freq = [s for s in spectrum if s["strain_grut"] == peak_strain][0]["frequency_hz"]
    
    return {
        "analysis_type": "PTA_FREQUENCY_BAND",
        "frequency_range_hz": [min_freq_hz, max_freq_hz],
        "num_points": num_points,
        "spectrum": spectrum,
        "peak_strain": peak_strain,
        "peak_frequency_hz": peak_freq,
        "nanograv_reference": {
            "amplitude": NANOGRAV_STRAIN,
            "reference_freq_hz": NANOGRAV_FREQ,
            "spectral_index": NANOGRAV_SPECTRAL_INDEX
        },
        "timestamp": datetime.utcnow().isoformat()
    }
