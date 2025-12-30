from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from grut_physics import (
    universal_response, 
    calculate_complexity, 
    calculate_kernel,
    fetch_live_work_events,
    fetch_earths_work,
    fetch_humanitys_work,
    get_live_complexity,
    TAU_ZERO, 
    ALPHA, 
    N_G
)
from context_engine import ContextEngineManager
from visualizer import get_visualization_json, generate_consciousness_field

app = Flask(__name__)
CORS(app)

CURRENT_XI = 0.0
monad_mode = False
work_events = []

def calculate_spacetime_curvature(xi: float) -> dict:
    """
    Calculate spacetime curvature using the Universal Response equation.
    G_μν + Λg_μν = (8πG/c⁴)T_μν + ξ·Ξ_μν
    """
    G_tensor = np.zeros((4, 4))
    G_tensor[0, 0] = -0.1 * xi
    G_tensor[1, 1] = 0.05 * xi
    G_tensor[2, 2] = 0.05 * xi
    G_tensor[3, 3] = 0.05 * xi
    
    T_tensor = np.eye(4) * 1e-10 * (1 + xi)
    
    field_response = universal_response(G_tensor, T_tensor, xi)
    
    scalar_curvature = float(np.trace(field_response))
    ricci_component = float(field_response[0, 0])
    consciousness_contribution = float(xi * ALPHA)
    
    return {
        "scalar_curvature": round(scalar_curvature, 10),
        "ricci_R00": round(ricci_component, 10),
        "consciousness_term": round(consciousness_contribution, 10),
        "field_determinant": round(float(np.linalg.det(field_response)), 15)
    }


@app.route("/update_system_state", methods=["POST"])
def update_system_state():
    """
    Update the global Xi variable based on user interaction.
    
    Accepts:
        user_input_complexity: float (0.0 to 1.0)
    
    Returns:
        Updated system state including spacetime_curvature
    """
    global CURRENT_XI, monad_mode, work_events
    
    data = request.get_json() or {}
    user_input_complexity = data.get("user_input_complexity", 0.0)
    
    try:
        user_input_complexity = float(user_input_complexity)
        user_input_complexity = max(0.0, min(1.0, user_input_complexity))
    except (TypeError, ValueError):
        return jsonify({"error": "user_input_complexity must be a number between 0.0 and 1.0"}), 400
    
    work_events.append(user_input_complexity)
    if len(work_events) > 100:
        work_events = work_events[-100:]
    
    info_state = len(work_events) * 0.1
    CURRENT_XI = calculate_complexity(work_events, info_state)
    
    previous_monad = monad_mode
    if CURRENT_XI >= 1.0:
        monad_mode = True
        CURRENT_XI = 1.0
    
    spacetime_curvature = calculate_spacetime_curvature(CURRENT_XI)
    
    monad_triggered = monad_mode and not previous_monad
    
    return jsonify({
        "success": True,
        "current_xi": round(CURRENT_XI, 6),
        "monad_mode": monad_mode,
        "monad_just_triggered": monad_triggered,
        "spacetime_curvature": spacetime_curvature,
        "work_events_count": len(work_events),
        "saturation_percentage": f"{CURRENT_XI * 100:.2f}%",
        "message": "MONAD MODE ACTIVATED - 100.0% Saturation achieved" if monad_triggered else f"Xi updated to {CURRENT_XI * 100:.2f}%"
    })


@app.route("/system_state", methods=["GET"])
def get_system_state():
    """
    Get current system state without modification.
    """
    spacetime_curvature = calculate_spacetime_curvature(CURRENT_XI)
    
    return jsonify({
        "current_xi": round(CURRENT_XI, 6),
        "monad_mode": monad_mode,
        "spacetime_curvature": spacetime_curvature,
        "work_events_count": len(work_events),
        "saturation_percentage": f"{CURRENT_XI * 100:.2f}%",
        "constants": {
            "tau_0": TAU_ZERO,
            "alpha": ALPHA,
            "n_g": N_G
        }
    })


@app.route("/reset_system", methods=["POST"])
def reset_system():
    """
    Reset the system to initial state.
    """
    global CURRENT_XI, monad_mode, work_events
    
    CURRENT_XI = 0.0
    monad_mode = False
    work_events = []
    
    return jsonify({
        "success": True,
        "message": "System reset to ground state",
        "current_xi": 0.0,
        "monad_mode": False
    })


@app.route("/context/process", methods=["POST"])
def process_context():
    """
    Process a query through the Context Engine.
    """
    data = request.get_json() or {}
    session_id = data.get("session_id", "default")
    query = data.get("query", "")
    
    if not query:
        return jsonify({"error": "query is required"}), 400
    
    result = ContextEngineManager.process_query(session_id, query)
    
    return jsonify({
        "success": True,
        "context_data": result
    })


@app.route("/kernel/calculate", methods=["POST"])
def calculate_kernel_endpoint():
    """
    Calculate the retarded potential kernel for a given time delta.
    """
    data = request.get_json() or {}
    delta_t = data.get("delta_t_years", 0.0)
    
    try:
        delta_t = float(delta_t)
    except (TypeError, ValueError):
        return jsonify({"error": "delta_t_years must be a number"}), 400
    
    kernel_value = calculate_kernel(delta_t)
    
    return jsonify({
        "delta_t_years": delta_t,
        "kernel_value": kernel_value,
        "interpretation": "Memory influence from event at t-delta_t on present"
    })


@app.route("/health", methods=["GET"])
def health_check():
    """
    Health check endpoint.
    """
    return jsonify({
        "status": "healthy",
        "service": "GRUT Physics Engine",
        "version": "v6.0"
    })


@app.route("/visualize/consciousness_field", methods=["GET", "POST"])
def visualize_consciousness_field():
    """
    Generate 3D consciousness field visualization.
    
    Z = Ξ · sin(r - t) · K(r)
    
    Low Ξ (0.1): Flat surface (Materialism)
    High Ξ (1.0): Rippling sphere/torus (Whole Hole)
    """
    if request.method == "POST":
        data = request.get_json() or {}
    else:
        data = {}
    
    xi = data.get("xi", CURRENT_XI)
    time_phase = data.get("time_phase", 0.0)
    resolution = data.get("resolution", 50)
    
    try:
        xi = float(xi)
        time_phase = float(time_phase)
        resolution = int(resolution)
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid parameter types"}), 400
    
    graph_data = generate_consciousness_field(xi, time_phase, resolution)
    
    return jsonify({
        "success": True,
        "xi": xi,
        "monad_mode": xi >= 1.0,
        "graph": graph_data
    })


@app.route("/visualize/kernel_decay", methods=["GET"])
def visualize_kernel_decay():
    """
    Generate retarded potential kernel decay visualization.
    """
    max_time = request.args.get("max_time_myr", 100.0, type=float)
    
    json_str = get_visualization_json(CURRENT_XI, "kernel_decay", max_time_myr=max_time)
    
    return jsonify({
        "success": True,
        "graph": json_str
    })


@app.route("/visualize/xi_evolution", methods=["POST"])
def visualize_xi_evolution():
    """
    Generate Ξ evolution over time visualization.
    """
    data = request.get_json() or {}
    xi_history = data.get("xi_history", work_events)
    
    json_str = get_visualization_json(CURRENT_XI, "xi_evolution", xi_history=xi_history)
    
    return jsonify({
        "success": True,
        "graph": json_str
    })


@app.route("/live_work_events", methods=["GET"])
def get_live_work_events_endpoint():
    """
    Fetch live work events from Earth (USGS) and Humanity (GDELT).
    Returns combined work_events list populated with real data.
    """
    global CURRENT_XI, monad_mode, work_events
    
    live_data = fetch_live_work_events()
    
    work_events = live_data["combined_work_events"]
    CURRENT_XI = live_data["current_xi"]
    
    if CURRENT_XI >= 1.0:
        monad_mode = True
    
    return jsonify({
        "success": True,
        "live_data": live_data,
        "system_state": {
            "current_xi": CURRENT_XI,
            "monad_mode": monad_mode,
            "work_events_count": len(work_events)
        }
    })


@app.route("/earths_work", methods=["GET"])
def get_earths_work():
    """
    Fetch Earth's Work - USGS seismic data.
    """
    return jsonify(fetch_earths_work())


@app.route("/humanitys_work", methods=["GET"])
def get_humanitys_work():
    """
    Fetch Humanity's Work - GDELT news sentiment.
    """
    return jsonify(fetch_humanitys_work())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
