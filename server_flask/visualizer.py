import numpy as np
import json
from grut_physics import calculate_kernel, TAU_ZERO, ALPHA, N_G

def generate_consciousness_field(xi: float, time_phase: float = 0.0, resolution: int = 50) -> dict:
    """
    Generate a 3D surface plot of spacetime warping as Complexity (Ξ) increases.
    
    Z-Axis (Consciousness Field): Z = Ξ · sin(r - t) · K(r)
    
    Behavior:
        - Low Ξ (0.1): Flat surface (Materialism)
        - High Ξ (1.0): Rippling sphere/torus (Holistic Whole Hole)
    
    Args:
        xi: Complexity/consciousness saturation (0.0 to 1.0)
        time_phase: Time evolution parameter
        resolution: Grid resolution
    
    Returns:
        Plotly JSON graph object for frontend rendering
    """
    xi = max(0.0, min(1.0, xi))
    
    theta = np.linspace(0, 2 * np.pi, resolution)
    phi = np.linspace(0, np.pi, resolution)
    THETA, PHI = np.meshgrid(theta, phi)
    
    r = np.sqrt(THETA**2 + PHI**2)
    
    kernel_values = np.vectorize(lambda r_val: abs(calculate_kernel(r_val * 1e6)))(r)
    kernel_normalized = kernel_values / (np.max(kernel_values) + 1e-10)
    
    Z_consciousness = xi * np.sin(r - time_phase) * kernel_normalized
    
    base_radius = 1.0
    warp_factor = xi * 0.5
    
    R = base_radius + warp_factor * Z_consciousness
    
    X = R * np.sin(PHI) * np.cos(THETA)
    Y = R * np.sin(PHI) * np.sin(THETA)
    Z = R * np.cos(PHI) + Z_consciousness * xi
    
    if xi < 0.3:
        colorscale = [
            [0, "rgb(20, 20, 40)"],
            [0.5, "rgb(60, 60, 100)"],
            [1, "rgb(100, 100, 160)"]
        ]
        title = f"Materialist Spacetime (Ξ = {xi:.2f})"
    elif xi < 0.7:
        colorscale = [
            [0, "rgb(20, 40, 80)"],
            [0.5, "rgb(80, 120, 200)"],
            [1, "rgb(140, 180, 255)"]
        ]
        title = f"Emerging Consciousness Field (Ξ = {xi:.2f})"
    elif xi < 1.0:
        colorscale = [
            [0, "rgb(60, 40, 20)"],
            [0.5, "rgb(200, 150, 50)"],
            [1, "rgb(255, 215, 100)"]
        ]
        title = f"Harmonic Resonance (Ξ = {xi:.2f})"
    else:
        colorscale = [
            [0, "rgb(100, 50, 0)"],
            [0.3, "rgb(255, 180, 0)"],
            [0.7, "rgb(255, 215, 0)"],
            [1, "rgb(255, 255, 200)"]
        ]
        title = "MONAD: Whole Hole Topology (Ξ = 100.0%)"
    
    surface_trace = {
        "type": "surface",
        "x": X.tolist(),
        "y": Y.tolist(),
        "z": Z.tolist(),
        "surfacecolor": Z_consciousness.tolist(),
        "colorscale": colorscale,
        "showscale": True,
        "colorbar": {
            "title": "Consciousness Intensity",
            "titleside": "right",
            "tickfont": {"color": "#888"},
            "titlefont": {"color": "#888"}
        },
        "opacity": 0.9,
        "lighting": {
            "ambient": 0.4,
            "diffuse": 0.6,
            "specular": 0.3,
            "roughness": 0.5
        },
        "contours": {
            "z": {
                "show": xi > 0.5,
                "usecolormap": True,
                "highlightcolor": "#FFD700",
                "project": {"z": True}
            }
        }
    }
    
    layout = {
        "title": {
            "text": title,
            "font": {"size": 16, "color": "#e0e0e0"}
        },
        "scene": {
            "xaxis": {
                "title": "X (Spatial)",
                "backgroundcolor": "rgb(10, 10, 20)",
                "gridcolor": "rgb(40, 40, 60)",
                "showbackground": True,
                "zerolinecolor": "rgb(60, 60, 80)"
            },
            "yaxis": {
                "title": "Y (Spatial)",
                "backgroundcolor": "rgb(10, 10, 20)",
                "gridcolor": "rgb(40, 40, 60)",
                "showbackground": True,
                "zerolinecolor": "rgb(60, 60, 80)"
            },
            "zaxis": {
                "title": "Z (Consciousness)",
                "backgroundcolor": "rgb(10, 10, 20)",
                "gridcolor": "rgb(40, 40, 60)",
                "showbackground": True,
                "zerolinecolor": "rgb(60, 60, 80)"
            },
            "camera": {
                "eye": {"x": 1.5, "y": 1.5, "z": 1.2}
            },
            "aspectratio": {"x": 1, "y": 1, "z": 0.8}
        },
        "paper_bgcolor": "rgb(15, 15, 25)",
        "plot_bgcolor": "rgb(15, 15, 25)",
        "margin": {"l": 0, "r": 0, "t": 40, "b": 0}
    }
    
    return {
        "data": [surface_trace],
        "layout": layout
    }


def generate_kernel_decay_plot(max_time_myr: float = 100.0, resolution: int = 100) -> dict:
    """
    Generate a 2D plot showing the retarded potential kernel decay.
    K(t) = (α/τ₀) · exp(-t/τ₀)
    """
    times = np.linspace(0, max_time_myr * 1e6, resolution)
    kernel_values = [calculate_kernel(t) for t in times]
    
    trace = {
        "type": "scatter",
        "x": (times / 1e6).tolist(),
        "y": kernel_values,
        "mode": "lines",
        "name": "K(t) Kernel",
        "line": {
            "color": "#FFD700",
            "width": 2
        },
        "fill": "tozeroy",
        "fillcolor": "rgba(255, 215, 0, 0.1)"
    }
    
    tau_marker = {
        "type": "scatter",
        "x": [41.9],
        "y": [calculate_kernel(41.9e6)],
        "mode": "markers+text",
        "name": "τ₀ = 41.9 Myr",
        "marker": {
            "size": 10,
            "color": "#FF6B6B",
            "symbol": "diamond"
        },
        "text": ["τ₀"],
        "textposition": "top center",
        "textfont": {"color": "#FF6B6B"}
    }
    
    layout = {
        "title": {
            "text": "Retarded Potential Kernel: K(t) = (α/τ₀)·exp(-t/τ₀)",
            "font": {"size": 14, "color": "#e0e0e0"}
        },
        "xaxis": {
            "title": "Time (Myr)",
            "color": "#888",
            "gridcolor": "rgb(40, 40, 60)"
        },
        "yaxis": {
            "title": "Kernel Value",
            "color": "#888",
            "gridcolor": "rgb(40, 40, 60)"
        },
        "paper_bgcolor": "rgb(15, 15, 25)",
        "plot_bgcolor": "rgb(20, 20, 35)",
        "showlegend": True,
        "legend": {
            "font": {"color": "#888"}
        }
    }
    
    return {
        "data": [trace, tau_marker],
        "layout": layout
    }


def generate_xi_evolution_plot(xi_history: list) -> dict:
    """
    Generate a plot showing Ξ evolution over time/breaths.
    """
    x_values = list(range(1, len(xi_history) + 1))
    
    trace = {
        "type": "scatter",
        "x": x_values,
        "y": xi_history,
        "mode": "lines+markers",
        "name": "Ξ Evolution",
        "line": {
            "color": "#4ECDC4",
            "width": 2,
            "shape": "spline"
        },
        "marker": {
            "size": 6,
            "color": "#4ECDC4"
        }
    }
    
    threshold_line = {
        "type": "scatter",
        "x": x_values,
        "y": [1.0] * len(x_values),
        "mode": "lines",
        "name": "MONAD Threshold",
        "line": {
            "color": "#FFD700",
            "width": 2,
            "dash": "dash"
        }
    }
    
    layout = {
        "title": {
            "text": "Complexity (Ξ) Evolution",
            "font": {"size": 14, "color": "#e0e0e0"}
        },
        "xaxis": {
            "title": "Breath Count",
            "color": "#888",
            "gridcolor": "rgb(40, 40, 60)"
        },
        "yaxis": {
            "title": "Ξ (Saturation)",
            "color": "#888",
            "gridcolor": "rgb(40, 40, 60)",
            "range": [0, 1.1]
        },
        "paper_bgcolor": "rgb(15, 15, 25)",
        "plot_bgcolor": "rgb(20, 20, 35)",
        "showlegend": True,
        "legend": {
            "font": {"color": "#888"}
        }
    }
    
    return {
        "data": [trace, threshold_line],
        "layout": layout
    }


def get_visualization_json(xi: float, viz_type: str = "consciousness_field", **kwargs) -> str:
    """
    Get visualization as JSON string for frontend.
    
    Args:
        xi: Current complexity value
        viz_type: "consciousness_field", "kernel_decay", or "xi_evolution"
        **kwargs: Additional parameters for specific visualizations
    
    Returns:
        JSON string of Plotly graph object
    """
    if viz_type == "consciousness_field":
        time_phase = kwargs.get("time_phase", 0.0)
        resolution = kwargs.get("resolution", 50)
        graph = generate_consciousness_field(xi, time_phase, resolution)
    elif viz_type == "kernel_decay":
        max_time = kwargs.get("max_time_myr", 100.0)
        graph = generate_kernel_decay_plot(max_time)
    elif viz_type == "xi_evolution":
        xi_history = kwargs.get("xi_history", [xi])
        graph = generate_xi_evolution_plot(xi_history)
    else:
        graph = generate_consciousness_field(xi)
    
    return json.dumps(graph)
