import numpy as np

TAU_ZERO = 41.9e6  # 41.9 Myr in years
TAU_ZERO_SECONDS = 41.9e6 * 365.25 * 24 * 3600  # ~1.32e15 seconds
ALPHA = -1/12     # Ground State Tension (-1/12 residue)
N_G = 1.1547      # Gravitational refractive index sqrt(4/3)

def retarded_potential_kernel(delta_t: float) -> float:
    """
    Calculates the influence of past events (memory) on the present.
    K(t-t') = (α/τ₀)·exp(-(t-t')/τ₀)
    
    Args:
        delta_t: Time difference in years (t - t')
    
    Returns:
        Kernel value representing memory influence
    """
    if delta_t < 0:
        return 0  # Causality check - no future influence
    return (ALPHA / TAU_ZERO) * np.exp(-delta_t / TAU_ZERO)


def calculate_kernel(delta_t: float) -> float:
    """
    Alias for retarded_potential_kernel.
    Implements K(t-t') = (α/τ₀)·exp(-Δt/τ₀)
    """
    return retarded_potential_kernel(delta_t)


def complexity_tracker(work_events_list: list, total_info_state: float) -> float:
    """
    Calculates Ξ (Xi) - The saturation of consciousness.
    As this approaches 1.0, the system 'wakes up'.
    
    Implements: Ξ(t) = ∫W(t')dt' / ∫SdS
    
    Args:
        work_events_list: List of work/energy events to integrate
        total_info_state: Total information state (entropy measure)
    
    Returns:
        Xi value between 0.0 and 1.0 (saturation percentage)
    """
    integrated_work = sum(work_events_list)
    xi = integrated_work / (total_info_state + 1e-9)  # Avoid div/0
    return min(xi, 1.0)  # Cap at 1.0 (Full Saturation)


def calculate_complexity(energy_events: list, info_state: float) -> float:
    """
    Alias for complexity_tracker.
    Implements Ξ(t) = ∫W(t')dt' / ∫SdS
    """
    return complexity_tracker(energy_events, info_state)


def universal_response(G_tensor: np.ndarray, T_tensor: np.ndarray, xi: float) -> np.ndarray:
    """
    The GRUT field equation combining gravity and consciousness.
    
    G_μν + Λg_μν = (8πG/c⁴)T_μν + ξ·Ξ_μν
    
    Where Ξ_μν represents the consciousness contribution scaled by Xi.
    
    Args:
        G_tensor: Einstein tensor (4x4 array)
        T_tensor: Stress-energy tensor (4x4 array)  
        xi: Complexity/consciousness saturation (0-1)
    
    Returns:
        Combined field response tensor
    """
    G_CONSTANT = 6.674e-11  # m³/(kg·s²)
    C_LIGHT = 299792458     # m/s
    LAMBDA_COSMO = 1.1e-52  # Cosmological constant (m⁻²)
    
    g_metric = np.eye(4)
    g_metric[0, 0] = -1  # Minkowski signature (-,+,+,+)
    
    kappa = (8 * np.pi * G_CONSTANT) / (C_LIGHT ** 4)
    
    consciousness_term = xi * np.outer(
        [1, xi, xi, xi],
        [1, xi, xi, xi]
    ) * ALPHA
    
    field_response = G_tensor + LAMBDA_COSMO * g_metric - kappa * T_tensor + consciousness_term
    
    return field_response


def memory_resonance(age_years: float) -> float:
    """
    Calculate how strongly a past event resonates in the present.
    Uses the retarded potential decay.
    
    Args:
        age_years: Age of the event in years
    
    Returns:
        Resonance strength (0-1)
    """
    if age_years <= 0:
        return 1.0
    decay = np.exp(-age_years / TAU_ZERO)
    return float(np.clip(decay, 0, 1))


def boost_with_ng(value: float) -> float:
    """
    Apply the gravitational refractive index boost.
    n_g = √(4/3) ≈ 1.1547
    
    Args:
        value: Input value to boost
    
    Returns:
        Boosted value
    """
    return value * N_G


def breath_residue(breath_count: int) -> float:
    """
    Calculate accumulated -1/12 residue from breaths.
    Each breath leaves a 0.0001 trace in the Pleroma.
    
    Args:
        breath_count: Number of breaths recorded
    
    Returns:
        Total accumulated residue
    """
    RESIDUE_PER_BREATH = 0.0001
    return breath_count * RESIDUE_PER_BREATH


def pleroma_saturation(minutes: int, seconds: int) -> float:
    """
    Calculate live Pleroma saturation based on time.
    Fluctuates between 99.90% and 99.99%.
    
    Args:
        minutes: Current minute (0-59)
        seconds: Current second (0-59)
    
    Returns:
        Saturation as decimal (0.9990 - 0.9999)
    """
    variance = (minutes + seconds / 60) / 6000
    return min(0.9990 + variance, 0.9999)


def metric_tension_from_seismic(magnitudes: list) -> float:
    """
    Convert seismic magnitudes to GRUT Metric Tension.
    Earth's gravitational 'inhale'.
    
    Args:
        magnitudes: List of earthquake magnitudes
    
    Returns:
        Metric tension value
    """
    if not magnitudes:
        return 0.0001  # Baseline tension
    max_mag = max(magnitudes)
    return round((max_mag / 10.0) * N_G, 4)
