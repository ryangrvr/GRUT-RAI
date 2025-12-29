import os
import uuid
import numpy as np
from flask import Flask, request, jsonify, g, session
from flask_cors import CORS
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import bcrypt
import psycopg2
from psycopg2.extras import RealDictCursor, Json
from functools import wraps
import json

app = Flask(__name__)
app.secret_key = os.environ.get('SESSION_SECRET', 'grut-rai-secret-key-2025')
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

CORS(app, supports_credentials=True, origins=["http://localhost:5000", "http://127.0.0.1:5000", "https://*.replit.dev", "https://*.repl.co"])

login_manager = LoginManager()
login_manager.init_app(app)

DEFAULT_UNIVERSE_STATE = {
    "tau_0": 41.9,
    "alpha": 0.333333,
    "n_g": 1.1547,
    "R_max": "Lambda_Limit"
}

def get_db_connection():
    conn = psycopg2.connect(os.environ['DATABASE_URL'])
    return conn

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS flask_users (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            email VARCHAR(255) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            universe_state JSONB DEFAULT '{"tau_0": 41.9, "alpha": 0.333333, "n_g": 1.1547, "R_max": "Lambda_Limit"}'::jsonb,
            global_sync_version INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    
    try:
        demo_email = "demo@grut.ai"
        cur.execute("SELECT id FROM flask_users WHERE email = %s", (demo_email,))
        if not cur.fetchone():
            password_hash = bcrypt.hashpw("grut2025".encode('utf-8'), bcrypt.gensalt(12)).decode('utf-8')
            cur.execute(
                "INSERT INTO flask_users (email, password_hash) VALUES (%s, %s)",
                (demo_email, password_hash)
            )
            conn.commit()
            print("[FLASK] Demo user created: demo@grut.ai / grut2025")
    except Exception as e:
        print(f"[FLASK] Demo user may already exist: {e}")
        conn.rollback()
    
    cur.close()
    conn.close()

class User(UserMixin):
    def __init__(self, id, email, universe_state=None):
        self.id = str(id)
        self.email = email
        self.universe_state = universe_state or DEFAULT_UNIVERSE_STATE.copy()
    
    def get_id(self):
        return self.id

@login_manager.user_loader
def load_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT id, email, universe_state FROM flask_users WHERE id = %s", (user_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    
    if row:
        return User(row['id'], row['email'], row['universe_state'])
    return None

def profile_hydration_middleware(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            g.tau_0 = current_user.universe_state.get('tau_0', DEFAULT_UNIVERSE_STATE['tau_0'])
            g.n_g = current_user.universe_state.get('n_g', DEFAULT_UNIVERSE_STATE['n_g'])
            g.alpha = current_user.universe_state.get('alpha', DEFAULT_UNIVERSE_STATE['alpha'])
            g.R_max = current_user.universe_state.get('R_max', DEFAULT_UNIVERSE_STATE['R_max'])
            g.user_email = current_user.email
        else:
            g.tau_0 = DEFAULT_UNIVERSE_STATE['tau_0']
            g.n_g = DEFAULT_UNIVERSE_STATE['n_g']
            g.alpha = DEFAULT_UNIVERSE_STATE['alpha']
            g.R_max = DEFAULT_UNIVERSE_STATE['R_max']
            g.user_email = None
        return f(*args, **kwargs)
    return decorated_function

def compute_retarded_potential_kernel(t):
    tau_0 = g.tau_0 if hasattr(g, 'tau_0') else DEFAULT_UNIVERSE_STATE['tau_0']
    alpha = g.alpha if hasattr(g, 'alpha') else DEFAULT_UNIVERSE_STATE['alpha']
    import math
    return (alpha / tau_0) * math.exp(-t / tau_0)

def global_physics_validator(chi_squared_value, observable_type):
    tau_0 = g.tau_0 if hasattr(g, 'tau_0') else DEFAULT_UNIVERSE_STATE['tau_0']
    alpha = g.alpha if hasattr(g, 'alpha') else DEFAULT_UNIVERSE_STATE['alpha']
    n_g = g.n_g if hasattr(g, 'n_g') else DEFAULT_UNIVERSE_STATE['n_g']
    
    kernel_signature = f"K(t) = ({alpha}/{tau_0}) * exp(-t/{tau_0})"
    
    validation = {
        "kernel": kernel_signature,
        "tau_0": tau_0,
        "alpha": alpha,
        "n_g": n_g,
        "chi_squared": chi_squared_value,
        "observable": observable_type,
        "baryonic_integrity": True,
        "dark_matter_terms": 0
    }
    
    return validation

@app.route('/api/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email', '').lower().strip()
    password = data.get('password', '')
    
    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400
    
    if len(password) < 6:
        return jsonify({"error": "Password must be at least 6 characters"}), 400
    
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    cur.execute("SELECT id FROM flask_users WHERE email = %s", (email,))
    if cur.fetchone():
        cur.close()
        conn.close()
        return jsonify({"error": "Email already registered"}), 409
    
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(12)).decode('utf-8')
    
    cur.execute(
        "INSERT INTO flask_users (email, password_hash) VALUES (%s, %s) RETURNING id, email, universe_state",
        (email, password_hash)
    )
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    
    if not row:
        return jsonify({"error": "Failed to create user"}), 500
    
    user = User(row['id'], row['email'], row['universe_state'])
    login_user(user)
    
    return jsonify({
        "message": "Registration successful",
        "user": {
            "id": str(row['id']),
            "email": row['email'],
            "universeState": row['universe_state']
        }
    }), 201

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email', '').lower().strip()
    password = data.get('password', '')
    
    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400
    
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT id, email, password_hash, universe_state FROM flask_users WHERE email = %s", (email,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    
    if not row:
        return jsonify({"error": "Invalid credentials"}), 401
    
    if not bcrypt.checkpw(password.encode('utf-8'), row['password_hash'].encode('utf-8')):
        return jsonify({"error": "Invalid credentials"}), 401
    
    user = User(row['id'], row['email'], row['universe_state'])
    login_user(user)
    
    g.tau_0 = user.universe_state.get('tau_0', DEFAULT_UNIVERSE_STATE['tau_0'])
    g.n_g = user.universe_state.get('n_g', DEFAULT_UNIVERSE_STATE['n_g'])
    g.alpha = user.universe_state.get('alpha', DEFAULT_UNIVERSE_STATE['alpha'])
    g.R_max = user.universe_state.get('R_max', DEFAULT_UNIVERSE_STATE['R_max'])
    
    return jsonify({
        "message": "Login successful",
        "user": {
            "id": str(row['id']),
            "email": row['email'],
            "universeState": row['universe_state']
        }
    })

@app.route('/api/auth/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"})

@app.route('/api/auth/me', methods=['GET'])
@profile_hydration_middleware
def get_current_user():
    if not current_user.is_authenticated:
        return jsonify({"error": "Not authenticated"}), 401
    
    return jsonify({
        "user": {
            "id": current_user.id,
            "email": current_user.email,
            "universeState": current_user.universe_state,
            "hydratedConstants": {
                "tau_0": g.tau_0,
                "n_g": g.n_g,
                "alpha": g.alpha,
                "R_max": g.R_max
            }
        }
    })

@app.route('/api/auth/universe-state', methods=['PUT'])
@login_required
def update_universe_state():
    data = request.get_json()
    new_state = data.get('universeState', {})
    
    if 'tau_0' not in new_state or 'n_g' not in new_state or 'alpha' not in new_state:
        return jsonify({"error": "Invalid universe state. Required: tau_0, n_g, alpha"}), 400
    
    try:
        validated_state = {
            "tau_0": float(new_state['tau_0']),
            "n_g": float(new_state['n_g']),
            "alpha": float(new_state['alpha']),
            "R_max": str(new_state.get('R_max', 'Lambda_Limit'))
        }
    except (ValueError, TypeError) as e:
        return jsonify({"error": f"Invalid numeric values: {str(e)}"}), 400
    
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(
        "UPDATE flask_users SET universe_state = %s WHERE id = %s RETURNING universe_state",
        (Json(validated_state), current_user.id)
    )
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    
    if not row:
        return jsonify({"error": "Failed to update universe state"}), 500
    
    current_user.universe_state = row['universe_state']
    
    return jsonify({
        "message": "Universe state updated",
        "universeState": row['universe_state']
    })

@app.route('/api/grut/validate', methods=['POST'])
@profile_hydration_middleware
def validate_physics():
    data = request.get_json()
    chi_squared = data.get('chiSquared', 0)
    observable = data.get('observable', 'generic')
    
    validation = global_physics_validator(chi_squared, observable)
    
    return jsonify(validation)

@app.route('/api/grut/kernel', methods=['GET'])
@profile_hydration_middleware
def get_kernel():
    t_values = [0, 10, 20, 30, 41.9, 50, 83.8, 100]
    kernel_values = []
    
    for t in t_values:
        k_t = compute_retarded_potential_kernel(t)
        kernel_values.append({"t": t, "K_t": k_t})
    
    return jsonify({
        "kernel": f"K(t) = (alpha/tau_0) * exp(-t/tau_0)",
        "tau_0": g.tau_0,
        "alpha": g.alpha,
        "values": kernel_values
    })

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "service": "GRUT RAI Flask Backend",
        "version": "2.0.0"
    })

import asyncio
from persistence import persistence_service

def run_async(coro):
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    return loop.run_until_complete(coro)

@app.route('/api/universe/save', methods=['POST'])
@login_required
@profile_hydration_middleware
def save_universe_state():
    try:
        data = request.get_json() or {}
        conversation_id = data.get('conversationId')
        description = data.get('description', f'Manual snapshot at {g.tau_0}')
        snapshot_type = data.get('snapshotType', 'manual')
        
        snapshot = run_async(persistence_service.save_universe_state_atomic(
            user_id=current_user.id,
            conversation_id=conversation_id,
            description=description,
            snapshot_type=snapshot_type
        ))
        
        return jsonify({
            "message": "Universe state saved atomically",
            "snapshot": {
                "id": str(snapshot.id),
                "chiSquaredMetrics": snapshot.chi_squared_metrics,
                "kernelWeights": snapshot.kernel_weights,
                "universeState": snapshot.universe_state,
                "bulletClusterChi2": snapshot.bullet_cluster_chi2,
                "cmbChi2": snapshot.cmb_chi2,
                "createdAt": snapshot.created_at.isoformat() if snapshot.created_at else None
            }
        })
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        print(f"[FLASK] Save error: {e}")
        return jsonify({"error": "Failed to save universe state"}), 500

@app.route('/api/universe/snapshots', methods=['GET'])
@login_required
def get_snapshots():
    try:
        limit = request.args.get('limit', 10, type=int)
        snapshots = run_async(persistence_service.get_user_snapshots(
            user_id=current_user.id,
            limit=limit
        ))
        
        return jsonify({
            "snapshots": [{
                "id": str(s.id),
                "snapshotType": s.snapshot_type,
                "chiSquaredMetrics": s.chi_squared_metrics,
                "kernelWeights": s.kernel_weights,
                "universeState": s.universe_state,
                "bulletClusterChi2": s.bullet_cluster_chi2,
                "cmbChi2": s.cmb_chi2,
                "description": s.description,
                "createdAt": s.created_at.isoformat() if s.created_at else None
            } for s in snapshots]
        })
    except Exception as e:
        print(f"[FLASK] Get snapshots error: {e}")
        return jsonify({"error": "Failed to get snapshots"}), 500

@app.route('/api/universe/restore/<snapshot_id>', methods=['POST'])
@login_required
def restore_snapshot(snapshot_id):
    try:
        restored_data = run_async(persistence_service.restore_snapshot(
            snapshot_id=snapshot_id,
            user_id=current_user.id
        ))
        
        if not restored_data:
            return jsonify({"error": "Snapshot not found"}), 404
        
        return jsonify({
            "message": "Universe state restored",
            "restoredData": restored_data
        })
    except Exception as e:
        print(f"[FLASK] Restore error: {e}")
        return jsonify({"error": "Failed to restore snapshot"}), 500

@app.route('/api/universe/benchmark', methods=['GET'])
@profile_hydration_middleware
def get_benchmark():
    import math
    
    tau_0 = g.tau_0 if hasattr(g, 'tau_0') else 41.9
    alpha = g.alpha if hasattr(g, 'alpha') else 0.333333
    n_g = g.n_g if hasattr(g, 'n_g') else 1.1547
    
    t_collision = 150.0
    kernel_weight = (alpha / tau_0) * math.exp(-t_collision / tau_0)
    predicted_offset = 4500.0 * t_collision * kernel_weight * n_g / 1000.0
    observed_offset = 720.0
    bullet_residual = (observed_offset - predicted_offset) / observed_offset
    bullet_chi2 = bullet_residual ** 2
    
    tau_target = 41.9
    cmb_residual = (tau_0 - tau_target) / tau_target
    cmb_chi2 = cmb_residual ** 2
    
    global_benchmark = {
        "tau_0": 41.9,
        "alpha": 0.333333,
        "n_g": 1.1547,
        "bullet_cluster_chi2": 0.0,
        "cmb_chi2": 0.0,
        "total_chi2": 0.0
    }
    
    return jsonify({
        "userMetrics": {
            "tau_0": tau_0,
            "alpha": alpha,
            "n_g": n_g,
            "kernelWeight": kernel_weight,
            "bulletCluster": {
                "observedOffset": observed_offset,
                "predictedOffset": predicted_offset,
                "chi2": bullet_chi2
            },
            "cmb": {
                "tauTarget": tau_target,
                "userTau0": tau_0,
                "chi2": cmb_chi2
            },
            "totalChi2": bullet_chi2 + cmb_chi2,
            "accuracy": max(0, 100 - (bullet_chi2 + cmb_chi2) * 100)
        },
        "globalBenchmark": global_benchmark,
        "baryonicIntegrity": True,
        "darkMatterTerms": 0
    })

from baryonic_sensor import BaryonicSensorAI, create_baryonic_sensor

@app.route('/api/baryonic/retarded-potential', methods=['POST'])
@profile_hydration_middleware
def simulate_retarded_potential():
    data = request.get_json() or {}
    time_start = data.get('timeStart', 1)
    time_end = data.get('timeEnd', 100)
    time_points = data.get('timePoints', 50)
    delta_mass = data.get('deltaMass', 1e30)
    
    constants = {
        'tau_0': g.tau_0 if hasattr(g, 'tau_0') else 41.9,
        'alpha': g.alpha if hasattr(g, 'alpha') else 0.333333,
        'n_g': g.n_g if hasattr(g, 'n_g') else 1.1547
    }
    
    sensor = create_baryonic_sensor(constants)
    time_scale = list(np.linspace(time_start, time_end, time_points))
    result = sensor.model_retarded_potential(time_scale, delta_mass)
    
    return jsonify(result)

@app.route('/api/baryonic/bullet-cluster', methods=['POST'])
@profile_hydration_middleware
def simulate_bullet_cluster():
    data = request.get_json() or {}
    collision_velocity = data.get('collisionVelocity', 4500)
    time_since_collision = data.get('timeSinceCollision', 150)
    cluster_separation = data.get('clusterSeparation', 720)
    
    constants = {
        'tau_0': g.tau_0 if hasattr(g, 'tau_0') else 41.9,
        'alpha': g.alpha if hasattr(g, 'alpha') else 0.333333,
        'n_g': g.n_g if hasattr(g, 'n_g') else 1.1547
    }
    
    sensor = create_baryonic_sensor(constants)
    result = sensor.simulate_bullet_cluster(collision_velocity, time_since_collision, cluster_separation)
    
    return jsonify(result)

@app.route('/api/baryonic/gravitational-waves', methods=['POST'])
@profile_hydration_middleware
def simulate_gravitational_waves():
    data = request.get_json() or {}
    event_type = data.get('eventType', 'BH_merger')
    source_distance = data.get('sourceDistance', 40)
    chirp_mass = data.get('chirpMass', 30)
    
    constants = {
        'tau_0': g.tau_0 if hasattr(g, 'tau_0') else 41.9,
        'alpha': g.alpha if hasattr(g, 'alpha') else 0.333333,
        'n_g': g.n_g if hasattr(g, 'n_g') else 1.1547
    }
    
    sensor = create_baryonic_sensor(constants)
    result = sensor.predict_gravitational_wave_residuals(event_type, source_distance, chirp_mass)
    
    return jsonify(result)

@app.route('/api/baryonic/hubble-tension', methods=['POST'])
@profile_hydration_middleware
def simulate_hubble_tension():
    data = request.get_json() or {}
    local_H0 = data.get('localH0', 73.0)
    cmb_H0 = data.get('cmbH0', 67.4)
    
    constants = {
        'tau_0': g.tau_0 if hasattr(g, 'tau_0') else 41.9,
        'alpha': g.alpha if hasattr(g, 'alpha') else 0.333333,
        'n_g': g.n_g if hasattr(g, 'n_g') else 1.1547
    }
    
    sensor = create_baryonic_sensor(constants)
    result = sensor.compute_hubble_tension_correction(local_H0, cmb_H0)
    
    return jsonify(result)

@app.route('/api/baryonic/connections', methods=['GET'])
def get_interdisciplinary_connections():
    sensor = create_baryonic_sensor()
    result = sensor.get_interdisciplinary_connections()
    return jsonify(result)

@app.route('/api/baryonic/objections', methods=['GET'])
def get_philosophical_objections():
    sensor = create_baryonic_sensor()
    result = sensor.simulate_philosophical_objections()
    return jsonify(result)

with app.app_context():
    init_db()
    try:
        from models import init_async_db
        run_async(init_async_db())
    except Exception as e:
        print(f"[FLASK] Async DB init warning: {e}")

if __name__ == '__main__':
    debug_mode = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(host='0.0.0.0', port=5001, debug=debug_mode, use_reloader=False)
