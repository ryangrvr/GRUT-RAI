// GRUT RAI v2 — Full Dashboard Application

const API = '/api';
let charts = {};
let dashboardLoaded = false;

// ══════════════════════════════════════════════════════
// TAB NAVIGATION
// ══════════════════════════════════════════════════════

function switchTab(tab) {
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.tab-content').forEach(t => { t.style.display = 'none'; t.classList.remove('active'); });
    document.querySelector(`[data-tab="${tab}"]`).classList.add('active');
    const el = document.getElementById('tab-' + tab);
    el.style.display = 'block';
    el.classList.add('active');
    if (tab === 'dashboard' && !dashboardLoaded) { loadDashboard(); dashboardLoaded = true; }
    if (tab === 'grutipedia') showArticle('ctp');
}

// ══════════════════════════════════════════════════════
// HELPERS
// ══════════════════════════════════════════════════════

function fmt(x, digits=4) {
    if (x === null || x === undefined) return '—';
    if (Math.abs(x) < 0.001 || Math.abs(x) > 1e6) return x.toExponential(digits);
    return x.toPrecision(digits);
}
async function get(path) { return (await fetch(API + path)).json(); }

// ══════════════════════════════════════════════════════
// DASHBOARD
// ══════════════════════════════════════════════════════

async function loadHealth() {
    const d = await get('/health');
    const el = document.getElementById('status-grid');
    const ind = document.getElementById('health-indicator');
    if (!el) return;
    el.innerHTML = '';
    let allPass = true;
    for (const [mod, checks] of Object.entries(d.modules)) {
        for (const [name, ok] of Object.entries(checks)) {
            if (!ok) allPass = false;
            el.innerHTML += `<div class="status-item"><div class="dot ${ok?'pass':'fail'}"></div>${mod}.${name}</div>`;
        }
    }
    ind.innerHTML = allPass ? '<span style="color:var(--green)">● All systems nominal</span>'
                            : '<span style="color:var(--red)">● Degraded</span>';
}

async function calcDecoherence() {
    const m=document.getElementById('dec-m').value, l=document.getElementById('dec-l').value, R=document.getElementById('dec-R').value;
    const d = await get(`/decoherence?m=${m}&l=${l}&R=${R}`);
    document.getElementById('dec-result').innerHTML = `${fmt(d.Lambda_grav_Hz)} <span class="result-unit">Hz</span>`;
    document.getElementById('dec-detail').innerHTML = `t<sub>coh</sub> = ${fmt(d.t_coh_s*1000,2)} ms | S(l/R) = ${fmt(d.S_l_R,3)}`;
}

async function loadSeparationChart() {
    const d = await get('/decoherence/sweep_separation?m=80.8e-15&R=1e-6&l_min=1e-8&l_max=1e-4&n=120');
    const ctx = document.getElementById('chart-separation');
    if (!ctx) return;
    if (charts.sep) charts.sep.destroy();
    charts.sep = new Chart(ctx, {
        type:'scatter', data:{datasets:[
            {label:'Lambda_grav', data:d.data.map(p=>({x:Math.log10(p.l),y:Math.log10(p.Lambda)})), borderColor:'#4fc3f7', backgroundColor:'rgba(79,195,247,0.3)', pointRadius:1.5, showLine:true, borderWidth:2},
            {label:'Kink at l=1.8R', data:[{x:Math.log10(d.kink_at),y:-10},{x:Math.log10(d.kink_at),y:20}], borderColor:'#ffd54f', borderWidth:1, borderDash:[4,4], pointRadius:0, showLine:true}
        ]}, options:{plugins:{legend:{labels:{color:'#6b7a90',font:{size:10}}}}, scales:{x:{title:{display:true,text:'log10(l) [m]',color:'#6b7a90'},ticks:{color:'#6b7a90'},grid:{color:'#1e2a3a'}},y:{title:{display:true,text:'log10(Λ) [Hz]',color:'#6b7a90'},ticks:{color:'#6b7a90'},grid:{color:'#1e2a3a'}}}}
    });
}

async function loadMassChart() {
    const d = await get('/decoherence/sweep_mass?l=1e-6&m_min=1e-24&m_max=1e-10&n=80');
    const ctx = document.getElementById('chart-mass');
    if (!ctx) return;
    if (charts.mass) charts.mass.destroy();
    charts.mass = new Chart(ctx, {
        type:'scatter', data:{datasets:[{label:'Lambda_grav ~ m^2', data:d.data.map(p=>({x:Math.log10(p.m),y:Math.log10(p.Lambda)})), borderColor:'#66bb6a', backgroundColor:'rgba(102,187,106,0.3)', pointRadius:1.5, showLine:true, borderWidth:2}]},
        options:{plugins:{legend:{labels:{color:'#6b7a90',font:{size:10}}}}, scales:{x:{title:{display:true,text:'log10(m) [kg]',color:'#6b7a90'},ticks:{color:'#6b7a90'},grid:{color:'#1e2a3a'}},y:{title:{display:true,text:'log10(Λ) [Hz]',color:'#6b7a90'},ticks:{color:'#6b7a90'},grid:{color:'#1e2a3a'}}}}
    });
}

async function calcBridge() {
    const L=document.getElementById('br-lambda').value;
    const d = await get(`/bridge?lambda_grav=${L}`);
    document.getElementById('br-omega').innerHTML = `Ω<sub>Λ</sub> = ${fmt(d.Omega_Lambda,4)}`;
    document.getElementById('br-detail').innerHTML = `τ<sub>0</sub> = ${fmt(d.tau_0_Myr,1)} Myr | H<sub>∞</sub> = ${fmt(d.H_inf_Hz)} Hz | Planck: 0.689 | ${fmt(d.deviation_pct,1)}%`;
}

async function calcEvolve() {
    const z0=document.getElementById('ev-z0').value, zt=document.getElementById('ev-zt').value, tau=document.getElementById('ev-tau').value;
    const d = await get(`/constitutive/evolve?z0=${z0}&z_target=${zt}&tau=${tau}&dt=0.05&n_steps=200`);
    const ctx = document.getElementById('chart-evolve');
    if (!ctx) return;
    if (charts.evolve) charts.evolve.destroy();
    charts.evolve = new Chart(ctx, {
        type:'line', data:{datasets:[
            {label:'z(t)', data:d.data.map(p=>({x:p.t,y:p.z})), borderColor:'#ce93d8', borderWidth:2, pointRadius:0},
            {label:'z_target', data:[{x:0,y:parseFloat(zt)},{x:d.data[d.data.length-1].t,y:parseFloat(zt)}], borderColor:'#ffd54f', borderDash:[4,4], borderWidth:1, pointRadius:0}
        ]}, options:{plugins:{legend:{labels:{color:'#6b7a90',font:{size:10}}}}, scales:{x:{title:{display:true,text:'t',color:'#6b7a90'},ticks:{color:'#6b7a90'},grid:{color:'#1e2a3a'}},y:{title:{display:true,text:'z',color:'#6b7a90'},ticks:{color:'#6b7a90'},grid:{color:'#1e2a3a'}}}}
    });
}

async function loadConstants() {
    const d = await get('/constants');
    const tbody = document.querySelector('#constants-table tbody');
    if (!tbody) return;
    tbody.innerHTML = '';
    for (const [k,v] of Object.entries(d)) tbody.innerHTML += `<tr><td>${k}</td><td>${fmt(v)}</td></tr>`;
}

async function loadAnomaly() {
    const d = await get('/anomaly');
    const el = document.getElementById('anomaly-info');
    if (!el) return;
    el.innerHTML = `<table>
        <tr><td>C_FINAL</td><td>${fmt(d.C_FINAL)}</td><td style="color:var(--dim)">3-loop anomaly</td></tr>
        <tr><td>C_COSMO</td><td>${fmt(d.C_COSMO)}</td><td style="color:var(--dim)">Cosmological</td></tr>
        <tr><td>R_ANOMALY</td><td>${fmt(d.R_ANOMALY,5)}</td><td style="color:var(--dim)">|C_Cosmo/C_Final|</td></tr>
        <tr><td>S_CTP</td><td>${fmt(d.S_CTP,4)}</td><td style="color:var(--dim)">108π</td></tr>
        <tr><td>f(R)=2-R</td><td>${fmt(d.f_R,4)}</td><td style="color:var(--dim)">Vacuum response</td></tr></table>`;
}

async function loadDashboard() {
    await loadHealth(); loadConstants(); loadAnomaly(); loadSeparationChart(); loadMassChart();
    calcDecoherence(); calcBridge(); calcEvolve();
}

// ══════════════════════════════════════════════════════
// GRUTIPEDIA
// ══════════════════════════════════════════════════════

const articles = {
ctp: `<h2>The CTP Effective Action</h2>
<span class="status derived">AXIOM</span>
<p>The Schwinger-Keldysh closed-time-path formalism doubles the degrees of freedom into forward (+) and backward (-) branches. This is Axiom A0 — the foundational structure of GRUT.</p>
<h3>The Keldysh Basis</h3>
<div class="eq">z<sub>r</sub> = (z<sub>+</sub> + z<sub>-</sub>) / 2 &nbsp;&nbsp; (classical field)<br>z<sub>a</sub> = z<sub>+</sub> - z<sub>-</sub> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (quantum field)</div>
<h3>The CTP Action</h3>
<div class="eq">S<sub>CTP</sub>[z<sub>r</sub>, z<sub>a</sub>] = z<sub>a</sub> F[z<sub>r</sub>] + (i/2) z<sub>a</sub> N z<sub>a</sub></div>
<p>The first term generates the <strong>retarded (causal) dynamics</strong>. The second generates the <strong>noise</strong>. Together they enforce the fluctuation-dissipation theorem.</p>
<h3>Axiom A1: Retarded Variation</h3>
<div class="eq">δS<sub>CTP</sub> / δz<sub>a</sub> |<sub>z<sub>a</sub>=0</sub> = 0 → F[z<sub>r</sub>] = 0</div>
<p>This selects the causal, forward-in-time dynamics. The arrow of time IS this axiom.</p>`,

constitutive: `<h2>The Constitutive Equation</h2>
<span class="status derived">DERIVED (3 routes)</span>
<p>The central dynamical equation of GRUT, derived from three independent routes:</p>
<div class="eq">τ dz/dt + z = z<sub>target</sub>[z]</div>
<h3>Three Independent Derivations</h3>
<p><strong>Route 1 (CTP variation):</strong> Direct expansion of A1 in the NR limit.</p>
<p><strong>Route 2 (Mori-Zwanzig):</strong> Coarse-graining of the exact microscopic dynamics with finite-memory kernel.</p>
<p><strong>Route 3 (Gradient flow):</strong> Variational relaxation toward extrema of the effective action.</p>
<h3>The Target Functional</h3>
<div class="eq">z<sub>target</sub>[z] = z - (δF/δz)<sup>-1</sup> F[z]</div>
<p>This is the Newton-Raphson step toward F[z] = 0. Not postulated — algorithmically determined by S<sub>CTP</sub>.</p>`,

noise: `<h2>Noise Kernel &amp; Fluctuation-Dissipation Theorem</h2>
<span class="status derived">DERIVED</span>
<p>The second variation of S<sub>CTP</sub> gives the noise kernel:</p>
<div class="eq">δ²S<sub>CTP</sub> / δz<sub>a</sub>² = iN</div>
<p>The noise and dissipation are related by the FDT:</p>
<div class="eq">N(ω) = (2/τ) ℏω coth(ℏω / 2k<sub>B</sub>T)</div>
<p>In the gravitational sector (Newtonian limit):</p>
<div class="eq">N<sub>grav</sub>(x, x') = G / (ℏ|x - x'|)</div>
<p>This is the Diósi gravitational self-energy kernel, derived from the CTP influence functional (Anastopoulos & Hu, 2013).</p>`,

fixedpoint: `<h2>The Fixed-Point Principle</h2>
<span class="status derived">DERIVED</span>
<p>At the fixed point of the constitutive equation:</p>
<div class="eq">z* = z<sub>target</sub>[z*]</div>
<p>The time derivative vanishes. τ drops out. The fixed-point state is determined entirely by the CTP action.</p>
<h3>Stability</h3>
<p>Stable if all eigenvalues of dz<sub>target</sub>/dz at z* have |λ<sub>i</sub>| < 1. The approach timescale is τ<sub>eff</sub> = τ/(1 - λ<sub>max</sub>).</p>
<h3>The Organizing Principle</h3>
<p>Every physical regime in GRUT is a different realization of the fixed-point transition: from external-target dynamics (f<sub>self</sub> < 1) to self-referential equilibrium (f<sub>self</sub> = 1).</p>`,

decoherence: `<h2>Gravitational Decoherence</h2>
<span class="status derived">DERIVED — zero parameters</span>
<p>The flagship prediction of GRUT:</p>
<div class="eq">Λ<sub>grav</sub> = G m² S(l/R) / (ℏ l)</div>
<div class="eq">S(l/R) = min(1, (l/R)³/6)</div>
<h3>Six Scaling Laws</h3>
<p><strong>F1:</strong> Λ ~ m² (mass-squared)<br><strong>F2:</strong> Geometry dependence (gold ≠ silica at same mass)<br><strong>F3:</strong> Pressure plateau (Λ → const as P → 0)<br><strong>F4:</strong> Λ ~ l⁻¹ (far-field separation)<br><strong>F5:</strong> Entanglement protection (Bell < separable)<br><strong>F6:</strong> Geometric kink at l = 1.8R</p>
<p>No tested alternative reproduces all six simultaneously. The scaling laws, not any single number, are the prediction.</p>
<h3>Benchmark</h3>
<p>Gold microsphere R = 1 μm, m = 80.8 pg, l = 1 μm: <strong>Λ ~ 689 Hz, t<sub>coh</sub> ~ 1.5 ms</strong></p>`,

cosmological: `<h2>The Cosmological Constant</h2>
<span class="status computed">COMPUTED — 3-loop CTP on S⁴</span>
<p>The vacuum Hubble rate from the 3-loop anomaly structure:</p>
<div class="eq">H<sub>∞</sub> = (2 - R<sub>anomaly</sub>) / (S × τ<sub>0</sub>) = 1.885 × 10⁻¹⁸ Hz</div>
<p>The function f(R) = 2 - R is confirmed numerically from the CTP boundary conditions on de Sitter (S⁴), with the competing quadratic f = R(2-R) excluded by factor 70 in RMS.</p>
<h3>Result</h3>
<p><strong>Ω<sub>Λ</sub> = 0.691</strong> at H<sub>0</sub> = 70 km/s/Mpc. Planck 2018: 0.6889. Deviation: <strong>+0.3%</strong>.</p>`,

baryogenesis: `<h2>Baryon Asymmetry</h2>
<span class="status computed">COMPUTED — within 8% of observation</span>
<div class="eq">η<sub>B</sub> = J<sub>CP</sub> × K<sub>neq</sub> × (2 - R<sub>B</sub>) / S<sub>B</sub></div>
<p>All four factors determined:</p>
<p>J<sub>CP</sub> = 3.18 × 10⁻⁵ (Jarlskog, SM input) | K<sub>neq</sub> = 1.19 × 10⁻² (constitutive at EW threshold) | R<sub>B</sub> = 1.018 (Route 1 scaling) | S<sub>B</sub> = 565.5 (all SM Weyl fermions)</p>
<h3>Result</h3>
<p><strong>η = 6.56 × 10⁻¹⁰</strong>. Observed: 6.1 × 10⁻¹⁰. Deviation: <strong>+8%</strong>.</p>`,

darkmatter: `<h2>Dark Matter</h2>
<span class="status computed">CLOSED — Route 1 selected 5/5</span>
<p>U(1)<sub>dark</sub> gauge extension of the constitutive double-well potential. Route 1 (RG running from Planck) wins all five discriminator tests:</p>
<p><strong>g<sub>dark</sub> = 0.917</strong> | λ = 0.42 | M = 2.1 × 10⁹ GeV | <strong>m<sub>A</sub> = 387 MeV</strong> (dark photon) | σ/m = 0.001 cm²/g</p>
<p>Route 2 excluded: 65% self-referential shift, unstable eigenvalue (-6.66), destroys cosmology (-99% H<sub>∞</sub> shift).</p>`,

koide: `<h2>Koide Identity &amp; Three Generations</h2>
<span class="status derived">PROVEN — algebraic identity</span>
<div class="eq">K = (m<sub>e</sub> + m<sub>μ</sub> + m<sub>τ</sub>) / (√m<sub>e</sub> + √m<sub>μ</sub> + √m<sub>τ</sub>)² = 2/3</div>
<p>This is an <strong>algebraic identity</strong> of the Z₃ circulant mass operator. Verified to 2.3 × 10⁻¹⁶ for all θ.</p>
<p><strong>N = 3 is unique:</strong> For N ≠ 3, K varies with θ. Only N = 3 gives a phase-independent Koide ratio.</p>
<p>M₀ = 0.560 GeV¹ᐟ² and θ = 0.222 rad remain undetermined (two free parameters per fermion sector).</p>`,

sm: `<h2>Standard Model Emergence</h2>
<span class="status computed">COMPUTED — unique minimal EFT</span>
<p>Five CTP-native constraints collectively select SU(3)×SU(2)×U(1) with 3 generations:</p>
<p>1. Anomaly cancellation (S<sub>CTP</sub> gauge-invariant)<br>2. Asymptotic freedom (confinement FP exists)<br>3. SSB (EW fixed point)<br>4. CP violation (R ≠ 1 requires N<sub>gen</sub> ≥ 3)<br>5. Renormalizability (S<sub>CTP</sub> well-defined at all loops)</p>
<p>N = 2 fails CP. Removing SU(3) loses confinement. The SM is not imported arbitrarily — it is <strong>selected by CTP consistency</strong>.</p>`,

bridge: `<h2>The Bridge Parameter</h2>
<span class="status structural">ONE PARAMETER — experimentally determinable</span>
<div class="eq">Ω<sub>Λ</sub> = ((2-R) / (S × τ<sub>0</sub> × H<sub>0</sub>))²</div>
<p>Four inputs: (2-R) <strong>derived</strong>, S <strong>derived</strong>, H<sub>0</sub> <strong>measured</strong>, τ<sub>0</sub> <strong>the bridge</strong>.</p>
<p>τ<sub>0</sub> and Ω<sub>Λ</sub> are linked by this derived structural relation. They are not the same quantity — they live in different physical domains. The relation IS the content of the theory.</p>
<h3>The Experimental Chain</h3>
<p>Measure Λ<sub>grav</sub> → extract τ<sub>0</sub> → compute H<sub>∞</sub> → predict Ω<sub>Λ</sub></p>
<p>Before experiment: one-parameter framework. <strong>After experiment: zero-parameter prediction.</strong></p>`,

projection: `<h2>Projection-Dependence Audit</h2>
<p>Every DERIVED and COMPUTED result is projection-independent:</p>
<h3>Projection-INDEPENDENT (13 results)</h3>
<p>Schrödinger recovery, Λ<sub>grav</sub>, six scaling laws, K = 2/3, N = 3, f(R) = 2-R, Ω<sub>Λ</sub>, η<sub>B</sub>, DM Route 1, SM emergence, 40 Hz resonance, θ = 0</p>
<h3>Projection-DEPENDENT (10 results)</h3>
<p>Graviton propagator, UV 1/ω³, classical GR recovery, BH info, singularity, Bianchi, GW/QNM (dead), era map, n<sub>s</sub></p>
<p>The constitutive projection is a <strong>pedagogical organizing principle</strong>, not a load-bearing assumption.</p>`,

conjectures: `<h2>Conjectures</h2>
<p><span class="status hypothesis">F1 (Flavor Eigenvalue)</span> Fermion masses are eigenvalues of the CTP fixed-point operator M<sub>ij</sub>.</p>
<p><span class="status computed">C1 (De Sitter Linearity)</span> CONFIRMED — f(R) = 2-R from 3-loop CTP on S⁴. Promoted to computed result.</p>
<p><span class="status hypothesis">C2 (Primordial Spectrum)</span> n<sub>s</sub> = 0.9649 from constitutive dissipation at H·τ = 0.134.</p>
<p><span class="status hypothesis">Q1 (Curvature Bound)</span> Constitutive memory bounds all curvature invariants at Planck scale.</p>
<p><span class="status hypothesis">SCP (Strong CP)</span> θ = 0 from QCD fixed-point theta-independence. No axion predicted.</p>
<p><span class="status negative">H1 (Hierarchy)</span> UV softened (1/ω³) but hierarchy NOT solved. Honest negative.</p>`,

limitations: `<h2>Limitations &amp; Open Problems</h2>
<h3>Fundamental</h3>
<p>SM gauge group not derived (selected, not produced). Fermion masses open (M₀, θ free). Hierarchy unsolved. τ₀ requires measurement.</p>
<h3>Structural</h3>
<p>Constitutive projection heuristic for 2nd-order sectors. Perturbation growth FAILS (Appendix F honest negative). Singularity not regularized by KMS τ alone.</p>
<h3>What Would Kill GRUT</h3>
<p>No decoherence plateau. Wrong Ω<sub>Λ</sub> from measured τ<sub>0</sub>. Axion detected. 4th generation found. Koide violated. Graviton mass detected.</p>`
};

function showArticle(key) {
    document.querySelectorAll('.wiki-link').forEach(l => l.classList.remove('active'));
    event.target.classList.add('active');
    document.getElementById('wiki-article').innerHTML = articles[key] || '<p>Article not found.</p>';
}

// ══════════════════════════════════════════════════════
// RAI CHAT (Claude-powered with GRUT knowledge)
// ══════════════════════════════════════════════════════

let chatHistory = [];
let aiAvailable = false;

async function checkAI() {
    try {
        const d = await get('/chat/status');
        aiAvailable = d.ai_available;
        const indicator = document.querySelector('.chat-messages .msg.system');
        if (indicator && aiAvailable) {
            indicator.innerHTML += '<br><span style="color:var(--green)">● Claude AI connected</span>';
        }
    } catch(e) {}
}

async function sendChat() {
    const input = document.getElementById('chat-input');
    const msg = input.value.trim();
    if (!msg) return;
    input.value = '';
    const messages = document.getElementById('chat-messages');
    messages.innerHTML += `<div class="msg user">${escapeHtml(msg)}</div>`;
    messages.scrollTop = messages.scrollHeight;

    // Show typing indicator
    const typingId = 'typing-' + Date.now();
    messages.innerHTML += `<div class="msg assistant" id="${typingId}" style="opacity:0.5">Thinking...</div>`;
    messages.scrollTop = messages.scrollHeight;

    let response = '';
    let source = 'fallback';

    // Try Claude AI first
    try {
        const r = await fetch(API + '/chat', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({message: msg, history: chatHistory})
        });
        const d = await r.json();
        if (d.response && d.source === 'claude') {
            response = formatMarkdown(d.response);
            source = 'claude';
        }
    } catch(e) {}

    // Fallback to keyword-based if AI unavailable
    if (!response) {
        response = await keywordFallback(msg);
        source = 'fallback';
    }

    // Update history
    chatHistory.push({role: 'user', content: msg});
    chatHistory.push({role: 'assistant', content: response});
    if (chatHistory.length > 20) chatHistory = chatHistory.slice(-20);

    // Replace typing indicator with response
    const typing = document.getElementById(typingId);
    if (typing) {
        typing.id = '';
        typing.style.opacity = '1';
        typing.innerHTML = response + (source === 'claude'
            ? '<div style="font-size:10px;color:var(--dim);margin-top:4px">via Claude</div>'
            : '');
    }
    messages.scrollTop = messages.scrollHeight;
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function formatMarkdown(text) {
    // Basic markdown → HTML
    let html = text
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/\*(.*?)\*/g, '<em>$1</em>')
        .replace(/`(.*?)`/g, '<code style="background:rgba(79,195,247,0.1);padding:1px 4px;border-radius:3px">$1</code>')
        .replace(/\n\n/g, '<br><br>')
        .replace(/\n/g, '<br>')
        .replace(/•/g, '&bull;')
        .replace(/→/g, '&rarr;');

    // Convert [VIZ:name] tags to clickable visualization buttons
    const vizNames = {
        'decoherence_frontier': 'Decoherence Frontier',
        'scaling_laws': 'Scaling Laws',
        'era_map': 'Era Map',
        'bridge': 'The Bridge',
    };
    html = html.replace(/\[VIZ:(\w+)\]/g, (match, name) => {
        const label = vizNames[name] || name;
        return `<button class="viz-btn" onclick="VIZ.open('${name}')">Visualize: ${label}</button>`;
    });
    return html;
}

async function keywordFallback(msg) {
    const lower = msg.toLowerCase();
    if (lower.includes('decoherence') && (lower.includes('rate') || lower.includes('gold') || lower.includes('calculate'))) {
        const d = await get('/decoherence?m=80.8e-15&l=1e-6&R=1e-6');
        return `<strong>Gravitational Decoherence Rate</strong><br>Gold 1μm: <strong>${fmt(d.Lambda_grav_Hz)} Hz</strong>, t<sub>coh</sub> = ${fmt(d.t_coh_s*1000,2)} ms`;
    } else if (lower.includes('bridge') || lower.includes('omega')) {
        const d = await get('/bridge?lambda_grav=689');
        return `<strong>Bridge:</strong> Ω<sub>Λ</sub> = ${fmt(d.Omega_Lambda,4)} (Planck: 0.689, ${fmt(d.deviation_pct,1)}%)`;
    } else if (lower.includes('what is grut') || lower.includes('overview')) {
        return `<strong>GRUT</strong> — A unified CTP framework. Two axioms → constitutive equation → QM, decoherence, cosmology, DM, baryogenesis. One bridge parameter connects lab to universe.`;
    }
    return `Ask me about GRUT — decoherence, cosmology, dark matter, baryogenesis, the bridge parameter, or what would falsify the theory.`;
}

// ══════════════════════════════════════════════════════
// INIT
// ══════════════════════════════════════════════════════

async function init() {
    await loadHealth();
    await checkAI();
    showArticle('ctp');
}
init();
