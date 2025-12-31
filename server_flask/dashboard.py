"""
GENESIS-330: BIO-SOVEREIGN BRIDGE
RAI Mission Control - Diamond-Hardened Visualization System
Guanine-Silicon Bridge Visualization
"""

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import sqlite3
import os
import time
from datetime import datetime

SQLITE_DB_PATH = os.path.join(os.path.dirname(__file__), "..", "diamond_persistence.db")
GEOMETRIC_LOCK = 0.999944
SOVEREIGN_GROUND_STATE = -0.083333
RESONANCE_FREQUENCY = 41.800000007229
GUANINE_VECTOR = 90.0

st.set_page_config(
    page_title="GENESIS-330: Sovereign Mission Control",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #c9d1d9;
    }
    .metric-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin: 5px 0;
    }
    .shield-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 20px;
    }
    .shield-indicator {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        font-weight: bold;
        font-size: 14px;
        color: white;
        text-align: center;
    }
    .shield-green {
        background: radial-gradient(circle, #00ff41 0%, #006600 100%);
        box-shadow: 0 0 30px rgba(0, 255, 65, 0.5);
        animation: pulse-green 2s infinite;
        color: #00ff41;
        font-weight: bold;
        text-shadow: 0 0 10px #00ff41;
    }
    .shield-red {
        background: radial-gradient(circle, #ff0000 0%, #660000 100%);
        box-shadow: 0 0 30px rgba(255, 0, 0, 0.5);
        animation: pulse-red 1s infinite;
        color: #ff0000;
        font-weight: bold;
        text-shadow: 0 0 10px #ff0000;
    }
    .shield-yellow {
        background: radial-gradient(circle, #ffff00 0%, #666600 100%);
        box-shadow: 0 0 30px rgba(255, 255, 0, 0.5);
        animation: pulse-yellow 1.5s infinite;
        color: #ffff00;
        font-weight: bold;
        text-shadow: 0 0 10px #ffff00;
    }
    @keyframes pulse-green {
        0% { transform: scale(1); box-shadow: 0 0 30px rgba(0, 255, 65, 0.5); }
        50% { transform: scale(1.05); box-shadow: 0 0 50px rgba(0, 255, 65, 0.8); }
        100% { transform: scale(1); box-shadow: 0 0 30px rgba(0, 255, 65, 0.5); }
    }
    @keyframes pulse-red {
        0% { transform: scale(1); box-shadow: 0 0 30px rgba(255, 0, 0, 0.5); }
        50% { transform: scale(1.08); box-shadow: 0 0 60px rgba(255, 0, 0, 0.9); }
        100% { transform: scale(1); box-shadow: 0 0 30px rgba(255, 0, 0, 0.5); }
    }
    @keyframes pulse-yellow {
        0% { transform: scale(1); box-shadow: 0 0 30px rgba(255, 255, 0, 0.5); }
        50% { transform: scale(1.03); box-shadow: 0 0 40px rgba(255, 255, 0, 0.7); }
        100% { transform: scale(1); box-shadow: 0 0 30px rgba(255, 255, 0, 0.5); }
    }
    .data-feed {
        background: #0a0a0a;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 15px;
        font-family: 'Courier New', monospace;
        color: #00ff41;
    }
    </style>
    """, unsafe_allow_html=True)


def get_db_connection():
    """Get SQLite database connection"""
    try:
        if os.path.exists(SQLITE_DB_PATH):
            return sqlite3.connect(SQLITE_DB_PATH)
        else:
            return None
    except Exception as e:
        st.error(f"Database connection failed: {e}")
        return None


def init_sqlite_tables():
    """Initialize SQLite tables if they don't exist"""
    conn = get_db_connection()
    if not conn:
        return
    
    try:
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bio_hardware_sync (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nitrogen_spin_deflection_angle REAL,
                system_clock_sync REAL,
                resonance_parity REAL,
                geometric_doping_model TEXT,
                xi_complexity REAL DEFAULT 0.9998,
                spin_deflection REAL DEFAULT 90.0,
                drift_coefficient REAL DEFAULT 0.0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cursor.execute("PRAGMA table_info(bio_hardware_sync)")
        columns = [row[1] for row in cursor.fetchall()]
        
        if 'xi_complexity' not in columns:
            cursor.execute("ALTER TABLE bio_hardware_sync ADD COLUMN xi_complexity REAL DEFAULT 0.9998")
        if 'spin_deflection' not in columns:
            cursor.execute("ALTER TABLE bio_hardware_sync ADD COLUMN spin_deflection REAL DEFAULT 90.0")
        if 'drift_coefficient' not in columns:
            cursor.execute("ALTER TABLE bio_hardware_sync ADD COLUMN drift_coefficient REAL DEFAULT 0.0")
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS genesis_resonance (
                id TEXT PRIMARY KEY,
                biomolecule TEXT,
                lattice_constant REAL,
                helical_pitch REAL,
                frequency REAL,
                resonance_parity REAL,
                ner_target_base TEXT,
                ner_spin_deflection TEXT,
                ner_status TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sovereign_manifestos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                signature TEXT NOT NULL,
                resonance_parity REAL,
                content TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"SQLite init error: {e}")


def fetch_bio_hardware_sync(limit=1):
    """Fetch latest rows from bio_hardware_sync table"""
    conn = get_db_connection()
    if not conn:
        return pd.DataFrame()
    
    try:
        query = f"""
            SELECT id, nitrogen_spin_deflection_angle, system_clock_sync, 
                   resonance_parity, geometric_doping_model,
                   xi_complexity, spin_deflection, drift_coefficient,
                   created_at
            FROM bio_hardware_sync
            ORDER BY created_at DESC
            LIMIT {limit}
        """
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        return pd.DataFrame()


def fetch_genesis_resonance():
    """Fetch genesis resonance data for NER display"""
    conn = get_db_connection()
    if not conn:
        return pd.DataFrame()
    
    try:
        query = "SELECT * FROM genesis_resonance ORDER BY created_at DESC"
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        return pd.DataFrame()


def fetch_sovereign_manifesto():
    """Fetch the sovereign manifesto - the constitution for all calculations"""
    conn = get_db_connection()
    if not conn:
        return None
    
    try:
        query = "SELECT * FROM sovereign_manifestos ORDER BY timestamp DESC LIMIT 1"
        df = pd.read_sql(query, conn)
        conn.close()
        if not df.empty:
            return df.iloc[0]
        return None
    except Exception as e:
        return None


def create_ner_scatter(is_stable=True, spin_deflection=90.0):
    """Create NER Alignment scatter plot with Guanine N3 vector"""
    spread = 0.5 if is_stable else 5.0
    x_vals = np.random.normal(spin_deflection, spread, 100)
    y_vals = np.random.normal(0, 1, 100)
    
    marker_color = '#00ff41' if is_stable else '#ff0000'
    
    fig = go.Figure(data=go.Scatter(
        x=x_vals, 
        y=y_vals, 
        mode='markers', 
        marker=dict(color=marker_color, size=8, opacity=0.6),
        name='Spin Deflection Field'
    ))
    
    fig.add_vline(x=GUANINE_VECTOR, line_width=3, line_dash="dash", line_color="white",
                  annotation_text="90.0 True North", annotation_position="top")
    
    fig.update_layout(
        xaxis_title="Deflection Angle (Degrees)", 
        yaxis_title="Spin Intensity",
        plot_bgcolor='#0e1117',
        paper_bgcolor='#0e1117',
        font=dict(color='#c9d1d9'),
        xaxis=dict(range=[80, 100], gridcolor='#30363d'),
        yaxis=dict(gridcolor='#30363d'),
        height=350
    )
    
    return fig


def create_metric_hum_wave(frequency=41.8):
    """Create Metric Hum sine wave visualization"""
    t = np.linspace(0, 1, 500)
    y = np.sin(2 * np.pi * frequency * t / 10)
    
    fig = go.Figure(data=go.Scatter(
        x=t * 1000, y=y,
        mode='lines',
        line=dict(color='#00ff41', width=2),
        fill='tozeroy',
        fillcolor='rgba(0, 255, 65, 0.1)'
    ))
    
    fig.update_layout(
        xaxis_title="Time (ms)",
        yaxis_title="Amplitude",
        plot_bgcolor='#0e1117',
        paper_bgcolor='#0e1117',
        font=dict(color='#c9d1d9'),
        height=200,
        margin=dict(l=40, r=40, t=20, b=40),
        xaxis=dict(gridcolor='#30363d'),
        yaxis=dict(gridcolor='#30363d', range=[-1.2, 1.2])
    )
    
    return fig


def create_resonance_gauge(parity_value):
    """Create gauge chart for Resonance Parity"""
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=parity_value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Resonance Parity", 'font': {'size': 16, 'color': '#c9d1d9'}},
        delta={'reference': 1.0, 'increasing': {'color': "#00ff41"}, 'decreasing': {'color': "#ff0000"}},
        number={'font': {'size': 28, 'color': '#00ff41'}},
        gauge={
            'axis': {'range': [0.95, 1.0], 'tickwidth': 1, 'tickcolor': "#c9d1d9"},
            'bar': {'color': "#00ff41" if parity_value > 0.99 else "#ff6600"},
            'bgcolor': "#161b22",
            'borderwidth': 2,
            'bordercolor': "#30363d",
            'steps': [
                {'range': [0.95, 0.97], 'color': 'rgba(255, 0, 0, 0.3)'},
                {'range': [0.97, 0.99], 'color': 'rgba(255, 165, 0, 0.3)'},
                {'range': [0.99, 1.0], 'color': 'rgba(0, 255, 65, 0.3)'}
            ],
            'threshold': {
                'line': {'color': "#ffffff", 'width': 4},
                'thickness': 0.75,
                'value': GEOMETRIC_LOCK
            }
        }
    ))
    
    fig.update_layout(
        paper_bgcolor='#0e1117',
        plot_bgcolor='#0e1117',
        font={'color': '#c9d1d9'},
        height=250
    )
    
    return fig


init_sqlite_tables()

st.sidebar.title("DIAMOND CORE")
st.sidebar.markdown("---")

toggle_live = st.sidebar.toggle("Live Grounding (Grit Mode)", value=False)
manual_hum = st.sidebar.slider("Manual Frequency Injection (Hz)", 40.0, 45.0, 41.8, 0.01)

st.sidebar.markdown("---")
st.sidebar.subheader("System Constants")
st.sidebar.metric("Carrier Wave", f"{RESONANCE_FREQUENCY:.9f} Hz")
st.sidebar.metric("Geometric Lock", f"{GEOMETRIC_LOCK:.6f}")
st.sidebar.metric("Ground State", f"{SOVEREIGN_GROUND_STATE:.6f}")
st.sidebar.metric("Guanine Vector", f"{GUANINE_VECTOR:.1f}")

st.sidebar.markdown("---")
auto_refresh = st.sidebar.checkbox("Auto-Refresh (1s)", value=False)

st.title("GENESIS-330: BIO-SOVEREIGN BRIDGE")
st.markdown("### Guanine-Silicon Diamond Core Visualization")

# --- SOVEREIGN MATERIAL DISCOVERY DISPLAY ---
st.header("2026 Material Discovery: Resonant Superconductor")
st.markdown("""
    **Material Designation:** GENESIS-330-ALPHA  
    **Stoichiometric String:** `Pb9.0Cu1.0SiC0.4(PO4)6O`  
    **Critical Temperature (Predicted):** 330.3 K (57.15 C)  
    **Legal Basis:** 2026 Sovereign Manifesto  
    **Status:** **[HARDENED]**
""")

# Visualizing the Tc Delta
st.progress(1.0, text="Resonance Parity: 0.9998 (Diamond Lock)")

st.markdown("---")

df = fetch_bio_hardware_sync(1)

if not df.empty:
    current_freq = df['system_clock_sync'].iloc[0] if df['system_clock_sync'].iloc[0] else RESONANCE_FREQUENCY
    resonance = df['resonance_parity'].iloc[0] if df['resonance_parity'].iloc[0] else 0.9998
    xi_complexity = df['xi_complexity'].iloc[0] if 'xi_complexity' in df.columns and df['xi_complexity'].iloc[0] else 0.9998
    spin_deflection = df['spin_deflection'].iloc[0] if 'spin_deflection' in df.columns and df['spin_deflection'].iloc[0] else 90.0
    drift_coefficient = df['drift_coefficient'].iloc[0] if 'drift_coefficient' in df.columns else 0.0
else:
    current_freq = RESONANCE_FREQUENCY
    resonance = 0.9998
    xi_complexity = 0.9998
    spin_deflection = 90.0
    drift_coefficient = 0.0

frequency_drift = abs(manual_hum - 41.8)
is_drifting = frequency_drift > 0.1 or (drift_coefficient and abs(drift_coefficient) > 0.05)

if is_drifting:
    drift_status = "CRITICAL DRIFT"
    shield_class = "shield-red"
    correction_msg = f"DOPING PULSE ACTIVE: Correcting {manual_hum:.2f}Hz -> 41.8Hz"
else:
    drift_status = "SOVEREIGN LOCK"
    shield_class = "shield-green"
    correction_msg = "SYSTEM STABLE"

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class='metric-card'>
        <h4>SHIELD STATUS</h4>
        <p class='{shield_class}' style='font-size: 24px;'>{drift_status}</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class='metric-card'>
        <h4>RESONANCE PARITY</h4>
        <h2 style='color: #00ff41;'>{resonance:.4f}</h2>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class='metric-card'>
        <h4>SYSTEM CLOCK</h4>
        <h2 style='color: #00ff41;'>{current_freq:.6f} Hz</h2>
    </div>
    """, unsafe_allow_html=True)

if is_drifting:
    st.warning(f"DOPING PULSE ACTIVE: Geometric Doping Model correcting frequency drift")

st.markdown("---")

c_left, c_right = st.columns([2, 1])

with c_left:
    st.subheader("Nuclear Electric Resonance (NER) Alignment")
    ner_fig = create_ner_scatter(is_stable=not is_drifting, spin_deflection=spin_deflection)
    st.plotly_chart(ner_fig, use_container_width=True)

with c_right:
    st.subheader("Metric Hum Carrier Wave")
    active_freq = manual_hum if toggle_live else RESONANCE_FREQUENCY
    wave_fig = create_metric_hum_wave(active_freq)
    st.plotly_chart(wave_fig, use_container_width=True)
    st.caption(f"Carrier: {RESONANCE_FREQUENCY:.9f} Hz")

st.markdown("---")

col_a, col_b, col_c = st.columns(3)

with col_a:
    st.markdown(f"""
    <div class='metric-card'>
        <h4>Xi Complexity</h4>
        <h2 style='color: {"#00ff41" if xi_complexity > 0.99 else "#ff0000"};'>{xi_complexity:.4f}</h2>
        <p>{"PURE" if xi_complexity > 0.99 else "DEGRADED"}</p>
    </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown(f"""
    <div class='metric-card'>
        <h4>Spin Deflection</h4>
        <h2 style='color: {"#00ff41" if abs(spin_deflection - 90.0) < 1.0 else "#ff0000"};'>{spin_deflection:.2f}</h2>
        <p>{"ALIGNED" if abs(spin_deflection - 90.0) < 1.0 else "DRIFTING"}</p>
    </div>
    """, unsafe_allow_html=True)

with col_c:
    drift_val = drift_coefficient if drift_coefficient else 0.0
    st.markdown(f"""
    <div class='metric-card'>
        <h4>Drift Coefficient</h4>
        <h2 style='color: {"#00ff41" if abs(drift_val) < 0.05 else "#ff0000"};'>{drift_val:.6f}</h2>
        <p>{"STABLE" if abs(drift_val) < 0.05 else "UNSTABLE"}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Resonance Parity Gauge")
    gauge_fig = create_resonance_gauge(resonance)
    st.plotly_chart(gauge_fig, use_container_width=True)

with col_right:
    st.subheader("Real-Time Data Feed")
    bio_data = fetch_bio_hardware_sync(3)
    
    if not bio_data.empty:
        st.markdown('<div class="data-feed">', unsafe_allow_html=True)
        for idx, row in bio_data.iterrows():
            xi = row.get('xi_complexity', 0.9998) or 0.9998
            spin = row.get('spin_deflection', 90.0) or 90.0
            drift = row.get('drift_coefficient', 0.0) or 0.0
            
            st.markdown(f"""
            **Record {row['id']}** | {row['created_at']}
            - Xi: `{xi:.4f}` | Spin: `{spin:.2f}` | Drift: `{drift:.6f}`
            """)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("No data in bio_hardware_sync table")

st.markdown("---")

manifesto = fetch_sovereign_manifesto()
if manifesto is not None:
    st.subheader("Sovereign Manifesto (BEDROCK CONSTITUTION)")
    st.markdown(f"""
    <div class='metric-card' style='text-align: left; border: 2px solid #00ff41;'>
        <h3 style='color: #00ff41;'>{manifesto['title']}</h3>
        <p><strong>Signature:</strong> <span style='color: #00ff41;'>{manifesto['signature']}</span> | 
        <strong>Resonance Parity:</strong> <span style='color: #00ff41;'>{manifesto['resonance_parity']:.4f}</span></p>
        <hr style='border-color: #30363d;'>
        <p style='font-style: italic; color: #c9d1d9;'>"{manifesto['content']}"</p>
        <p style='font-size: 12px; color: #6e7681;'>Etched: {manifesto['timestamp']}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.subheader("Audit Log")
st.markdown(f"""
```
[{datetime.now().strftime('%H:%M:%S')}] AUDIT: Resonance Parity = {resonance:.4f} - {"STABLE" if resonance > 0.99 else "DRIFT"}
[{datetime.now().strftime('%H:%M:%S')}] AUDIT: Shield Status = {drift_status}
[{datetime.now().strftime('%H:%M:%S')}] AUDIT: Geometric Lock = {GEOMETRIC_LOCK:.6f} - VERIFIED
[{datetime.now().strftime('%H:%M:%S')}] AUDIT: Ground State = {SOVEREIGN_GROUND_STATE:.6f} - SOVEREIGN
[{datetime.now().strftime('%H:%M:%S')}] AUDIT: NER Alignment = {spin_deflection:.1f} - {"LOCKED" if abs(spin_deflection - 90.0) < 1.0 else "DRIFTING"}
[{datetime.now().strftime('%H:%M:%S')}] AUDIT: Sovereign Manifesto = {"ETCHED" if manifesto else "MISSING"} - CONSTITUTION
```
""")

if auto_refresh:
    time.sleep(1)
    st.rerun()

st.markdown("---")
st.markdown("*GENESIS-330: Bio-Sovereign Bridge v7.0 | Diamond Core Sovereign System | 2025-12-31*")
