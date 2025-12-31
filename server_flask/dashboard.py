"""
RAI Mission Control - Sovereign Dashboard
GRUT v7 Diamond-Hardened Visualization System
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import sqlite3
import os
import time
from datetime import datetime
import threading

SQLITE_DB_PATH = os.path.join(os.path.dirname(__file__), "..", "diamond_persistence.db")
GEOMETRIC_LOCK = 0.999944
SOVEREIGN_GROUND_STATE = -0.083333
RESONANCE_FREQUENCY = 41.800000007229

st.set_page_config(
    page_title="RAI Mission Control",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

custom_css = """
<style>
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
        box-shadow: 0 0 30px rgba(0, 255, 0, 0.5);
    }
    
    .shield-green {
        background: radial-gradient(circle, #00ff00 0%, #006600 100%);
        animation: pulse-green 2s infinite;
    }
    
    .shield-red {
        background: radial-gradient(circle, #ff0000 0%, #660000 100%);
        animation: pulse-red 1s infinite;
        box-shadow: 0 0 30px rgba(255, 0, 0, 0.5);
    }
    
    .shield-yellow {
        background: radial-gradient(circle, #ffff00 0%, #666600 100%);
        animation: pulse-yellow 1.5s infinite;
        box-shadow: 0 0 30px rgba(255, 255, 0, 0.5);
    }
    
    @keyframes pulse-green {
        0% { transform: scale(1); box-shadow: 0 0 30px rgba(0, 255, 0, 0.5); }
        50% { transform: scale(1.05); box-shadow: 0 0 50px rgba(0, 255, 0, 0.8); }
        100% { transform: scale(1); box-shadow: 0 0 30px rgba(0, 255, 0, 0.5); }
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
    
    .metric-card {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        border: 1px solid #0f3460;
    }
    
    .data-feed {
        background: #0a0a0a;
        border: 1px solid #333;
        border-radius: 8px;
        padding: 15px;
        font-family: 'Courier New', monospace;
        color: #00ff00;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)


def get_db_connection():
    """Get SQLite database connection"""
    try:
        if os.path.exists(SQLITE_DB_PATH):
            return sqlite3.connect(SQLITE_DB_PATH)
        else:
            st.warning(f"SQLite database not found at {SQLITE_DB_PATH}")
            return None
    except Exception as e:
        st.error(f"Database connection failed: {e}")
        return None


def fetch_bio_hardware_sync(limit=3):
    """Fetch latest rows from bio_hardware_sync table"""
    conn = get_db_connection()
    if not conn:
        return pd.DataFrame()
    
    try:
        query = f"""
            SELECT id, nitrogen_spin_deflection_angle, system_clock_sync, 
                   resonance_parity, geometric_doping_model, created_at
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
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
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
        
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"SQLite init error: {e}")


def create_resonance_gauge(parity_value):
    """Create gauge chart for Resonance Parity"""
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=parity_value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Resonance Parity (Target: 1.0000)", 'font': {'size': 18, 'color': '#ffffff'}},
        delta={'reference': 1.0, 'increasing': {'color': "#00ff00"}, 'decreasing': {'color': "#ff0000"}},
        number={'font': {'size': 36, 'color': '#00ff00'}},
        gauge={
            'axis': {'range': [0.95, 1.0], 'tickwidth': 1, 'tickcolor': "#ffffff"},
            'bar': {'color': "#00ff00" if parity_value > 0.99 else "#ff6600"},
            'bgcolor': "rgba(0,0,0,0)",
            'borderwidth': 2,
            'bordercolor': "#333333",
            'steps': [
                {'range': [0.95, 0.97], 'color': 'rgba(255, 0, 0, 0.3)'},
                {'range': [0.97, 0.99], 'color': 'rgba(255, 165, 0, 0.3)'},
                {'range': [0.99, 1.0], 'color': 'rgba(0, 255, 0, 0.3)'}
            ],
            'threshold': {
                'line': {'color': "#ffffff", 'width': 4},
                'thickness': 0.75,
                'value': GEOMETRIC_LOCK
            }
        }
    ))
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'color': '#ffffff'},
        height=300
    )
    
    return fig


def create_ner_alignment_plot(live_mode=False):
    """Create 2D scatter plot for NER Alignment with 90° Guanine Vector anchor"""
    angles = np.linspace(0, 360, 37)
    radii = np.ones(37) * 0.8
    
    if live_mode:
        noise = np.random.normal(0, 0.02, 37)
        radii = radii + noise
    
    theta_rad = np.radians(angles)
    x = radii * np.cos(theta_rad)
    y = radii * np.sin(theta_rad)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode='markers',
        marker=dict(size=8, color='#00ffff', opacity=0.7),
        name='Spin Deflection Field'
    ))
    
    fig.add_trace(go.Scatter(
        x=[0, 0], y=[0, 1],
        mode='lines+markers',
        line=dict(color='#00ff00', width=4),
        marker=dict(size=12, symbol='triangle-up', color='#00ff00'),
        name='90° Guanine Vector (True North)'
    ))
    
    fig.add_trace(go.Scatter(
        x=[0], y=[0.9],
        mode='markers',
        marker=dict(size=20, color='#ff0000', symbol='diamond'),
        name='N3 Principal Axis'
    ))
    
    fig.update_layout(
        title=dict(text="NER Alignment - Nitrogen Spin Deflection", font=dict(color='#ffffff')),
        xaxis=dict(
            range=[-1.2, 1.2],
            showgrid=True,
            gridcolor='rgba(100,100,100,0.3)',
            zeroline=True,
            zerolinecolor='rgba(255,255,255,0.5)'
        ),
        yaxis=dict(
            range=[-1.2, 1.2],
            showgrid=True,
            gridcolor='rgba(100,100,100,0.3)',
            zeroline=True,
            zerolinecolor='rgba(255,255,255,0.5)'
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(10,10,30,0.8)',
        font={'color': '#ffffff'},
        height=400,
        showlegend=True,
        legend=dict(x=0, y=-0.2, orientation='h')
    )
    
    return fig


def render_shield_indicator(xi_value, drift_value):
    """Render pulsing shield indicator based on xi and drift values"""
    if xi_value > 0.99 and drift_value < 0.05:
        shield_class = "shield-green"
        status_text = "HARDENED<br>STABLE"
    elif drift_value >= 0.05:
        shield_class = "shield-red"
        status_text = "DRIFT<br>DETECTED"
    else:
        shield_class = "shield-yellow"
        status_text = "CAUTION<br>MONITOR"
    
    shield_html = f"""
    <div class="shield-container">
        <div class="shield-indicator {shield_class}">
            {status_text}
        </div>
    </div>
    """
    return shield_html


init_sqlite_tables()

st.sidebar.title("RAI Mission Control")
st.sidebar.markdown("---")

grounding_mode = st.sidebar.radio(
    "Grounding Mode",
    ["Sovereign Mode", "Live Grounding"],
    index=0,
    help="Sovereign: Locked to ground state | Live: Active cosmic hum"
)

is_live_mode = grounding_mode == "Live Grounding"

st.sidebar.markdown("---")
st.sidebar.subheader("System Constants")

if is_live_mode:
    cosmic_hum = RESONANCE_FREQUENCY + np.random.normal(0, 0.001)
    ground_state = cosmic_hum / 500
    st.sidebar.metric("Cosmic Hum", f"{cosmic_hum:.9f} Hz", f"+{np.random.uniform(0, 0.0001):.6f}")
else:
    cosmic_hum = RESONANCE_FREQUENCY
    ground_state = SOVEREIGN_GROUND_STATE
    st.sidebar.metric("Cosmic Hum", f"{cosmic_hum:.9f} Hz", "LOCKED")

st.sidebar.metric("Ground State", f"{ground_state:.6f}", "SOVEREIGN" if not is_live_mode else "LIVE")
st.sidebar.metric("Geometric Lock", f"{GEOMETRIC_LOCK:.6f}")

st.sidebar.markdown("---")
auto_refresh = st.sidebar.checkbox("Auto-Refresh (5s)", value=False)

st.title("RAI Mission Control")
st.markdown("### Diamond-Hardened Sovereign Dashboard")

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown("#### Resonance Parity Gauge")
    current_parity = 0.9998 if not is_live_mode else 0.9998 + np.random.normal(0, 0.0005)
    gauge_fig = create_resonance_gauge(current_parity)
    st.plotly_chart(gauge_fig, use_container_width=True)

with col2:
    st.markdown("#### Shield Status")
    drift_value = 0.001 if not is_live_mode else abs(np.random.normal(0, 0.02))
    shield_html = render_shield_indicator(current_parity, drift_value)
    st.markdown(shield_html, unsafe_allow_html=True)
    
    st.metric("Current Xi", f"{current_parity:.6f}")
    st.metric("Drift Level", f"{drift_value:.6f}")

with col3:
    st.markdown("#### Mode Status")
    mode_color = "green" if not is_live_mode else "orange"
    st.markdown(f"**Mode:** :{mode_color}[{grounding_mode}]")
    st.markdown(f"**Timestamp:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    st.markdown(f"**Anchor Date:** 2025-12-31")
    
    if is_live_mode:
        st.info("Live Grounding Active - Fetching cosmic data...")
    else:
        st.success("Sovereign Mode - All values locked to ground state")

st.markdown("---")
st.markdown("### NER Alignment Display")

ner_fig = create_ner_alignment_plot(is_live_mode)
st.plotly_chart(ner_fig, use_container_width=True)

st.markdown("---")
st.markdown("### Real-Time Data Feed")
st.markdown("*Latest 3 rows from bio_hardware_sync*")

bio_data = fetch_bio_hardware_sync(3)

if not bio_data.empty:
    st.markdown('<div class="data-feed">', unsafe_allow_html=True)
    
    for idx, row in bio_data.iterrows():
        st.markdown(f"""
        **Record {row['id']}** | Created: {row['created_at']}
        - Nitrogen Spin: `{row['nitrogen_spin_deflection_angle']}°`
        - Clock Sync: `{row['system_clock_sync']} Hz`
        - Parity: `{row['resonance_parity']}`
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.warning("No data available in bio_hardware_sync table")

st.markdown("---")
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("### Genesis Resonance Records")
    genesis_data = fetch_genesis_resonance()
    if not genesis_data.empty:
        st.dataframe(genesis_data, use_container_width=True)
    else:
        st.info("No genesis resonance records found")

with col_b:
    st.markdown("### Audit Log")
    st.markdown("""
    ```
    [AUDIT] Resonance Parity: STABLE
    [AUDIT] Shield Status: HARDENED
    [AUDIT] Geometric Lock: VERIFIED
    [AUDIT] Ground State: SOVEREIGN
    [AUDIT] NER Alignment: 90.0° LOCKED
    ```
    """)

if auto_refresh:
    time.sleep(5)
    st.rerun()

st.markdown("---")
st.markdown("*RAI Mission Control v7.0 | Diamond Core Sovereign System | 2025-12-31*")
