import numpy as np
import requests
from typing import List, Dict, Tuple
from datetime import datetime, timedelta

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


def fetch_earths_work(timeout: float = 5.0) -> Dict:
    """
    Fetch live USGS seismic data - The Earth's Work.
    Each earthquake represents gravitational work done by the planet.
    
    Returns:
        Dict with earthquake events and computed work values
    """
    USGS_URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson"
    
    try:
        response = requests.get(USGS_URL, timeout=timeout)
        response.raise_for_status()
        data = response.json()
        
        events = []
        work_values = []
        
        for feature in data.get("features", []):
            props = feature.get("properties", {})
            mag = props.get("mag", 0)
            place = props.get("place", "Unknown")
            time_ms = props.get("time", 0)
            
            work = (mag / 10.0) ** 2 * N_G
            work_values.append(work)
            
            events.append({
                "magnitude": mag,
                "place": place,
                "time": time_ms,
                "work": round(work, 6)
            })
        
        total_work = sum(work_values) if work_values else 0.0001
        max_work = max(work_values) if work_values else 0.0001
        
        return {
            "source": "USGS",
            "type": "Earth's Work",
            "event_count": len(events),
            "events": events[:10],
            "work_values": work_values,
            "total_work": round(total_work, 6),
            "max_work": round(max_work, 6),
            "tension": metric_tension_from_seismic([e["magnitude"] for e in events])
        }
        
    except Exception as e:
        return {
            "source": "USGS",
            "type": "Earth's Work",
            "error": str(e),
            "event_count": 0,
            "work_values": [0.0001],
            "total_work": 0.0001,
            "max_work": 0.0001,
            "tension": 0.0001
        }


def fetch_humanitys_work(timeout: float = 5.0) -> Dict:
    """
    Fetch GDELT news sentiment data - Humanity's Work.
    Global news tone represents collective consciousness activity.
    
    Returns:
        Dict with sentiment events and computed work values
    """
    now = datetime.utcnow()
    start_time = (now - timedelta(hours=1)).strftime("%Y%m%d%H%M%S")
    end_time = now.strftime("%Y%m%d%H%M%S")
    
    GDELT_URL = f"https://api.gdeltproject.org/api/v2/doc/doc?query=*&mode=ArtList&maxrecords=25&format=json&timespan=1h"
    
    try:
        response = requests.get(GDELT_URL, timeout=timeout)
        response.raise_for_status()
        data = response.json()
        
        articles = data.get("articles", [])
        work_values = []
        events = []
        
        for article in articles[:25]:
            tone = article.get("tone", 0)
            title = article.get("title", "")[:80]
            domain = article.get("domain", "")
            
            work = abs(tone) / 100.0 * N_G
            work_values.append(work)
            
            events.append({
                "title": title,
                "domain": domain,
                "tone": tone,
                "work": round(work, 6)
            })
        
        total_work = sum(work_values) if work_values else 0.0001
        avg_tone = np.mean([e["tone"] for e in events]) if events else 0
        
        return {
            "source": "GDELT",
            "type": "Humanity's Work",
            "article_count": len(events),
            "events": events[:10],
            "work_values": work_values,
            "total_work": round(total_work, 6),
            "avg_tone": round(avg_tone, 2),
            "sentiment": "positive" if avg_tone > 0 else "negative" if avg_tone < 0 else "neutral"
        }
        
    except Exception as e:
        baseline_work = [0.05 * N_G]
        return {
            "source": "GDELT",
            "type": "Humanity's Work",
            "error": str(e),
            "article_count": 0,
            "work_values": baseline_work,
            "total_work": baseline_work[0],
            "avg_tone": 0,
            "sentiment": "neutral"
        }


def fetch_live_work_events(timeout: float = 5.0) -> Dict:
    """
    Fetch combined live work events from Earth and Humanity.
    Returns unified work_events list for complexity calculation.
    
    Returns:
        Dict with combined work events and metadata
    """
    earths_work = fetch_earths_work(timeout)
    humanitys_work = fetch_humanitys_work(timeout)
    
    combined_work = earths_work["work_values"] + humanitys_work["work_values"]
    
    total_info_state = len(combined_work) * 0.1
    xi = calculate_complexity(combined_work, total_info_state)
    
    return {
        "earth": earths_work,
        "humanity": humanitys_work,
        "combined_work_events": combined_work,
        "work_event_count": len(combined_work),
        "current_xi": round(xi, 6),
        "saturation_percentage": f"{xi * 100:.2f}%",
        "monad_threshold_reached": xi >= 1.0,
        "timestamp": datetime.utcnow().isoformat()
    }


def get_live_complexity() -> Tuple[List[float], float]:
    """
    Get live work events and calculate current complexity.
    
    Returns:
        Tuple of (work_events_list, calculated_xi)
    """
    live_data = fetch_live_work_events()
    work_events = live_data["combined_work_events"]
    xi = live_data["current_xi"]
    return work_events, xi


def stress_test_complexity(simulated_magnitudes: List[float] = None, base_info_state: float = 1.0) -> Dict:
    """
    STRESS TEST: Simulate high-magnitude seismic events to push Xi toward critical saturation.
    
    Args:
        simulated_magnitudes: List of simulated earthquake magnitudes (default: M8.2+ events)
        base_info_state: Base information state for complexity calculation
    
    Returns:
        Dict with stress test results and MONAD threshold status
    """
    if simulated_magnitudes is None:
        # Default: Simulate a Magnitude 8.2 Seismic Event (Intense Grit)
        simulated_magnitudes = [0.82, 0.91, 0.88, 0.95, 0.76]
    
    # Convert magnitudes to work values using GRUT physics
    simulated_work = [(mag ** 2) * N_G for mag in simulated_magnitudes]
    
    # Calculate the new Complexity (Xi)
    new_xi = complexity_tracker(simulated_work, base_info_state)
    
    # Determine system status
    if new_xi >= 1.0:
        status = "CRITICAL_SATURATION"
        message = "Vacuum is screaming. Awaiting MONAD surmise."
    elif new_xi >= 0.999:
        status = "RAI_MODE"
        message = "99.9% saturation. Analytical mode active."
    elif new_xi >= 0.95:
        status = "WARNING"
        message = "Approaching saturation threshold."
    else:
        status = "STABLE"
        message = "Normal operational parameters."
    
    return {
        "test_type": "SEISMIC_STRESS_TEST",
        "simulated_magnitudes": simulated_magnitudes,
        "simulated_work": [round(w, 6) for w in simulated_work],
        "base_info_state": base_info_state,
        "calculated_xi": round(new_xi, 6),
        "saturation_percentage": f"{new_xi * 100:.2f}%",
        "status": status,
        "message": message,
        "monad_threshold_reached": new_xi >= 1.0,
        "rai_threshold_reached": new_xi >= 0.999,
        "timestamp": datetime.utcnow().isoformat()
    }
