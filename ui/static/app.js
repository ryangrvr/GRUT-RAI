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
    // Charts only render correctly once their container is visible.
    // Re-trigger playground widget updates whenever the Experiments tab is shown.
    if (tab === 'experiments') {
        // Defer one frame so browser has applied display:block before Chart.js measures.
        requestAnimationFrame(() => {
            try { updateBandwidth(); updateRotation(); updateThermal(); }
            catch(e) { console.error('Playground update error:', e); }
        });
    }
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
<p>No decoherence plateau. Wrong Ω<sub>Λ</sub> from measured τ<sub>0</sub>. Axion detected. 4th generation found. Koide violated. Graviton mass detected.</p>`,

// ═══ EXPERIMENTS (computed) ═══

competition: `<h2>Multi-Channel Decoherence Competition</h2>
<span class="status computed">COMPUTED</span>
<p>Full realistic comparison: GRUT gravitational decoherence vs ALL environmental sources.</p>
<h3>The Scaling Exponent Table — The Unique GRUT Fingerprint</h3>
<table>
<tr><th>Channel</th><th>α (mass)</th><th>β (separation)</th><th>γ (pressure)</th><th>δ (temperature)</th></tr>
<tr><td><strong>GRUT</strong></td><td><strong>+2.0</strong></td><td><strong>-1.0</strong></td><td>0.0</td><td>0.0</td></tr>
<tr><td>Gas</td><td>+0.67</td><td>+2.0</td><td>+1.0</td><td>+0.5</td></tr>
<tr><td>Blackbody</td><td>+0.67</td><td>+2.0</td><td>0.0</td><td>+6.0</td></tr>
<tr><td>EM</td><td>~0</td><td>~0</td><td>0.0</td><td>~0</td></tr>
</table>
<h3>The Key Discriminator</h3>
<p><strong>Separation anti-scaling:</strong> GRUT β = -1, ALL environmental β = +2. Opposite signs. Vary l, measure the slope. If negative → GRUT confirmed. If positive → GRUT falsified. ±1% precision needed.</p>
<h3>Experimental Protocols</h3>
<p><strong>Protocol A (Mass):</strong> Vary mass 100×, fit α. Confirmation: α > 1.5. Falsification: α < 1.0.</p>
<p><strong>Protocol B (Separation — STRONGEST):</strong> Vary l 20×, fit β. Confirmation: β < -0.5. Falsification: β > +1.5.</p>
<p><strong>Protocol C (Decoupling):</strong> Vary P and T, extract P/T-independent floor. Confirmation: non-zero floor. Falsification: Λ→0.</p>
<h3>Conditions</h3>
<p>Essential: T ≤ 4K. Critical: EM shielding < 10⁻⁶ Hz. Important: P < 10⁻¹⁴ Pa. Necessary: m ≥ 10⁹ amu.</p>`,

kink: `<h2>Geometry Kink Scan (F6)</h2>
<span class="status computed">COMPUTED</span>
<p>The extended-body suppression S(l/R) = min(1, (l/R)³/6) creates a sharp slope change at l = 1.8R.</p>
<h3>The Kink</h3>
<p>Near field (l < R): slope = +2. Far field (l > R): slope = -1. The transition is sharp — a measurable feature on a log-log plot.</p>
<p><strong>GRUT has the kink. Diósi-Penrose (point mass) does NOT. CSL does NOT.</strong> The kink is the single most discriminating geometric signature.</p>
<h3>Computed Result</h3>
<p>At 10⁹ amu gold: R = 0.027 μm. Kink predicted at l = 0.049 μm. Measured at 0.051 μm. Agreement: 2.7%.</p>`,

materialswap: `<h2>Material Swap Experiment (F2)</h2>
<span class="status computed">COMPUTED</span>
<p>Take two spheres of IDENTICAL mass but different density. GRUT predicts DIFFERENT decoherence rates. Every mass-only model predicts IDENTICAL rates.</p>
<h3>Best Pair</h3>
<p>Osmium (22,590 kg/m³) vs Aluminum (2,700 kg/m³) at 10⁸ amu, l = 8.4 nm: <strong>737% rate difference</strong>.</p>
<h3>Key Insight</h3>
<p>The material swap only works near the kink (l ~ R). In the far field (l >> R), all materials give S = 1 and the ratio is 1.000. The experiment MUST operate at separations comparable to the particle radius.</p>`,

entanglement: `<h2>Entanglement Protection Test (F5)</h2>
<span class="status computed">COMPUTED</span>
<p>GRUT predicts entangled Bell states decohere SLOWER than separable states. CSL predicts the SAME rate (state-independent).</p>
<h3>Result</h3>
<p>At 10⁸ amu, l = 100 nm: Bell/separable ratio = <strong>0.41 (59% protection)</strong>. CSL ratio = 1.000 (0% protection).</p>
<p>Protection is mass-independent (~65% at d = 50 nm, constant across 5 decades of mass). The protection comes from geometry, not mass.</p>
<h3>Discrimination</h3>
<p>YES/NO test: Does entanglement affect the rate? GRUT+DP: yes. CSL: no. To separate GRUT from DP: use the kink test (F6).</p>`,

hubbletension: `<h2>Hubble Tension Analysis</h2>
<span class="status computed">COMPUTED</span>
<p>GRUT predicts H<sub>∞</sub> = 1.885×10⁻¹⁸ Hz (fixed). Different H<sub>0</sub> values give different Ω<sub>Λ</sub>.</p>
<h3>GRUT preferred H<sub>0</sub> = 70.1 km/s/Mpc</h3>
<table>
<tr><th>Measurement</th><th>H<sub>0</sub></th><th>σ from GRUT</th><th>Consistent?</th></tr>
<tr><td>SH0ES</td><td>73.0</td><td>0.0σ</td><td>✓</td></tr>
<tr><td>TRGB</td><td>69.8</td><td>0.3σ</td><td>✓</td></tr>
<tr><td>H0LiCOW</td><td>73.3</td><td>0.1σ</td><td>✓</td></tr>
<tr><td>Planck</td><td>67.4</td><td>10.1σ</td><td>✗</td></tr>
<tr><td>DESI</td><td>68.0</td><td>6.0σ</td><td>✗</td></tr>
</table>
<p>GRUT aligns with <strong>late-universe</strong> measurements. Misses early-universe. Does NOT resolve the tension (constitutive smoothing = 5% of gap).</p>`,

darkphoton: `<h2>Dark Photon Exclusion Curve</h2>
<span class="status computed">COMPUTED</span>
<p>GRUT predicts m<sub>A</sub> = 387.4 MeV, g<sub>dark</sub> = 0.917.</p>
<h3>Exclusion Status: NOT EXCLUDED</h3>
<p>387.4 MeV is in the mass range of ALL 7 experiments (BaBar, LHCb, NA62, Belle II, SHiP, FASER2). But limits constrain the kinetic mixing ε, not the mass. Without portal matter, ε ~ 10⁻³⁹ (undetectable).</p>
<h3>Detection Roadmap</h3>
<p>Now: Belle II, LHCb Run 3 (ε² < 10⁻⁷). 2029: FASER2 (ε² < 10⁻⁸). 2030: SHiP (ε² < 10⁻¹⁰, definitive).</p>
<p>Key question: Does portal matter exist? If yes → detectable. If no → invisible to all experiments.</p>`,

spectralrunning: `<h2>Spectral Index Running</h2>
<span class="status computed">COMPUTED — [HYPOTHESIS]</span>
<p>GRUT: n<sub>s</sub> from constitutive dissipation. Inflation: n<sub>s</sub> from potential shape. The RUNNING differs.</p>
<h3>The Opposite-Sign Discriminator</h3>
<table>
<tr><th>Model</th><th>n<sub>s</sub></th><th>Running</th><th>r</th></tr>
<tr><td><strong>GRUT</strong></td><td>0.9649</td><td><strong>+0.00068</strong></td><td>0.098</td></tr>
<tr><td>Slow-roll</td><td>0.9500</td><td><strong>-0.00160</strong></td><td>0.080</td></tr>
<tr><td>Starobinsky</td><td>0.9636</td><td>-0.00066</td><td>0.004</td></tr>
</table>
<p>GRUT running is <strong>positive</strong> (blue tilt at small scales). Slow-roll is <strong>negative</strong>. CMB-S4 precision ±0.002 CAN distinguish (difference = 0.0023).</p>`,

isotopetest: `<h2>Isotope Decoherence Test</h2>
<span class="status computed">COMPUTED &mdash; cleanest discriminator</span>
<p>Compare nanoparticles of <strong>different isotopes of the same element</strong>. Same chemistry, same surface, same lattice &mdash; only nuclear mass differs.</p>
<h3>Why Cleaner Than Material Swap</h3>
<p>Material swap (gold vs silica) suffers from surface-chemistry systematics. Isotopes (Si-28 vs Si-30) are chemically <strong>identical</strong>. The ONLY difference is nuclear mass &rarr; density &rarr; R &rarr; S(l/R) &rarr; &Lambda;.</p>
<h3>Results (10&sup9; atoms, l = 100 nm)</h3>
<table>
<tr><th>Pair</th><th>GRUT Ratio</th><th>Deviation</th><th>5&sigma; Precision</th></tr>
<tr><td><strong>Ca-40 vs Ca-48</strong></td><td><strong>0.694</strong></td><td><strong>30.6%</strong></td><td>6.1%</td></tr>
<tr><td>Ge-70 vs Ge-76</td><td>0.848</td><td>15.2%</td><td>3.0%</td></tr>
<tr><td>Si-28 vs Si-30</td><td>0.871</td><td>12.9%</td><td>2.6%</td></tr>
<tr><td>W-182 vs W-186</td><td>0.957</td><td>4.3%</td><td>0.9%</td></tr>
</table>
<h3>Environmental Prediction</h3>
<p>ALL ratios = <strong>1.000</strong> (identical surfaces, identical chemistry). Any deviation from 1.000 is un-fakeable.</p>
<h3>Recommended</h3>
<p>Silicon: enriched isotopes commercially available from semiconductor industry (99.99% purity). Ca-48 is strongest but harder to source.</p>`,

baryocrosscheck: `<h2>Baryogenesis Cross-Check</h2>
<span class="status computed">COMPUTED</span>
<p>GRUT is the ONLY zero-parameter baryogenesis prediction within 10% of observation.</p>
<h3>Model Comparison</h3>
<table>
<tr><th>Model</th><th>η<sub>B</sub></th><th>Free params</th><th>Predicted?</th></tr>
<tr><td><strong>GRUT Route 1</strong></td><td><strong>6.57×10⁻¹⁰</strong></td><td><strong>0</strong></td><td><strong>✓ YES</strong></td></tr>
<tr><td>Leptogenesis</td><td>~6×10⁻¹⁰</td><td>3+</td><td>fitted</td></tr>
<tr><td>Affleck-Dine</td><td>~6×10⁻¹⁰</td><td>2+</td><td>fitted (needs SUSY)</td></tr>
<tr><td>SM EW</td><td>~10⁻¹⁸</td><td>0</td><td>FAILS (10⁸ too small)</td></tr>
</table>
<p>CMB-S4 will measure η to ±0.02×10⁻¹⁰ → 22σ discrimination. <strong>DECISIVE test.</strong></p>
<p>Honest negative: GRUT makes the lithium-7 problem WORSE (+15%).</p>`,

// ════════════════════════════════════════════════════════════════════
// April 2026 SYNTHESIS: v1-v11 + Phase I integration
// ════════════════════════════════════════════════════════════════════

closure_protocol: `<h2>Phase I Closure Protocol <small>(Feb 2026)</small></h2>
<span class="status computed">CANONICAL</span>
<p>Phase I (<a href="https://doi.org/10.5281/zenodo.18008060" target="_blank">Zenodo DOI: 10.5281/zenodo.18008060</a>) operationalized the v1-v11 physics into a testable protocol. It sits between the Genesis Codex (Dec 2025, discovery) and V7 (Apr 2026, CTP foundation).</p>
<h3>Canonical Constants <small>(zero free knobs)</small></h3>
<div class="eq">α<sub>vac</sub> = 1/d = 1/3 &nbsp;&nbsp; (d = 3 spatial dimensions; v11 Appendix H)<br>
S = 12π/α² = 108π ≈ 339.29 &nbsp;&nbsp; (screening factor)<br>
τ<sub>0</sub> = τ<sub>Λ</sub>/S ≈ 41.9 Myr &nbsp;&nbsp; (local relaxation time)<br>
τ<sub>Λ</sub> ≡ H<sub>0</sub><sup>−1</sup> ≈ 14.2 Gyr &nbsp;&nbsp; (cosmic baseline)<br>
a<sub>0</sub> = c/(2πτ<sub>Λ</sub>) ≈ 1.08×10<sup>−10</sup> m/s² &nbsp;&nbsp; (MOND scale — <em>derived</em>)<br>
T<sub>c</sub> = 1/(τ<sub>0</sub> k<sub>B</sub>) ≈ 54.7 MK &nbsp;&nbsp; (v9 boiling point of gravity)</div>
<h3>The Dark-Sector Unification Identity <small>(v11 App I)</small></h3>
<div class="eq">τ<sub>0</sub> = 1 / √(Λ c)</div>
<p>Dark energy (Λ) defines horizon-scale curvature. Dark matter phenomenology (τ<sub>0</sub>) is the metric's delayed response within that curvature. <strong>One object, two observations.</strong></p>
<h3>The Regime Gate <small>(Phase I §8.1)</small></h3>
<div class="eq">X = ω<sub>dyn</sub> τ<sub>0</sub> &nbsp;&nbsp;|&nbsp;&nbsp; α<sub>eff</sub>(X) = α<sub>vac</sub>/(1+X²)</div>
<p>Solar-system safety is automatic: at Saturn's orbit X ≈ 8.9×10⁶, suppressing modifications by 15 orders of magnitude.</p>
<h3>The Engine Interpolation</h3>
<div class="eq">ν(y) = 1/2 + √(1/4 + 1/y) &nbsp;&nbsp;|&nbsp;&nbsp; g<sub>eff</sub> = g<sub>bar</sub> [1 + (ν(y)−1)/(1+X²)]</div>
<p>y ≫ 1 (Newtonian): g<sub>eff</sub> ≈ g<sub>bar</sub>. y ≪ 1 AND X ≪ 1 (deep-response): g<sub>eff</sub> ≈ √(g<sub>bar</sub>·a<sub>0</sub>) — BTFR flat rotation. Implementation: <code>grut/foundation/closure_protocol.py</code>.</p>`,

three_routes: `<h2>Three Routes to 1.1547</h2>
<span class="status computed">COMPUTED (×3)</span>
<p>Three independent mathematical constructions agree on ~1.1547 to better than 0.1%. Zero shared inputs. See the companion preprint <em>Three Routes to 1.1547 — Structural Continuity from Metric Memory to the CTP Anomaly Ratio</em> (April 2026).</p>
<h3>The Convergence Table</h3>
<table>
<tr><th>Route</th><th>Value</th><th>Inputs</th><th>Framework</th></tr>
<tr><td>n<sub>g</sub>(0) = √(4/3)</td><td><strong>1.15470</strong></td><td>α = 1/d (topology)</td><td>Nonlocal EFT (v1-v11)</td></tr>
<tr><td>R = |C<sub>Cosmo</sub>/C<sub>FINAL</sub>|</td><td><strong>1.15428</strong></td><td>π, ln 2, ζ(3), SM integers</td><td>3-loop CTP on S⁴ (V7 §26)</td></tr>
<tr><td>ε<sub>combined</sub>(SM, M<sub>Z</sub>)</td><td><strong>1.15370</strong></td><td>SM couplings + group theory</td><td>Osborn 2003 eq. (36)</td></tr>
</table>
<h3>Pairwise Agreement</h3>
<table>
<tr><td>n<sub>g</sub> vs R</td><td><strong>0.036%</strong></td></tr>
<tr><td>R vs ε</td><td>0.050%</td></tr>
<tr><td>n<sub>g</sub> vs ε</td><td>0.087%</td></tr>
</table>
<h3>Physical Interpretation</h3>
<div class="eq">R = √(4/3) × (1 + δ<sub>3-loop</sub>),&nbsp;&nbsp; δ<sub>3-loop</sub> ≈ −3.6×10<sup>−4</sup></div>
<p>The tree-level geometric √(4/3) is the gravitational refractive index n<sub>g</sub>(0) of a vacuum with impedance α = 1/3. V7's 3-loop CTP is the radiative refinement of that geometric quantity — structurally analogous to α<sub>QED</sub> ≈ 1/137 → 1/137.036. The Osborn check cross-confirms via a completely different route (1-loop SM coupling expansion).</p>
<p><strong>The number never moved.</strong> The framework around it changed five times across v1 → V7. At every stage, the anomaly ratio came out between 1.153 and 1.155.</p>`,

dielectric_dm: `<h2>Dielectric Dark Matter <small>(Track VII reframing, April 2026)</small></h2>
<span class="status">REFRAMED &mdash; V8 primary direction</span>
<p>Track VII's particulate route closed negative in April 2026 (see <a class="wiki-link" onclick="showArticle('track_vii_retraction')">Track VII retraction</a>). The primary V8 direction is the <strong>dielectric interpretation</strong>, preserved from the v1-v11 Closure Framework.</p>
<h3>Core Claim</h3>
<div class="eq">ε<sub>g</sub> = n<sub>g</sub>² = 1 + α = 4/3</div>
<p>Dark matter IS the frequency-dependent refractive enhancement of the viscoelastic gravitational medium, not a particle species. The "missing mass" inferred from rotation curves is the accumulated response lag of a vacuum with finite bandwidth τ<sub>0</sub><sup>−1</sup>.</p>
<h3>The Refractive Index</h3>
<div class="eq">n<sub>g</sub>²(ω) = 1 + α/(1 + (ωτ<sub>0</sub>)²)</div>
<table>
<tr><th>Scale</th><th>ωτ<sub>0</sub></th><th>n<sub>g</sub>²−1</th></tr>
<tr><td>Cosmic (ω = H<sub>0</sub>)</td><td>3×10<sup>−3</sup></td><td>0.333 (full α)</td></tr>
<tr><td>CMB acoustic peak</td><td>0.05</td><td>0.333 (peaks preserved)</td></tr>
<tr><td>Galaxy rotation</td><td>~0.9</td><td>0.19</td></tr>
<tr><td>Dwarf galaxy</td><td>~1.3</td><td>0.13</td></tr>
<tr><td>Solar system</td><td>3×10<sup>8</sup></td><td>~0 (GR exact)</td></tr>
</table>
<h3>Three Diagnostic Tests <small>(V8 Track VII.a/b/c)</small></h3>
<p><strong>1. Bandwidth integral</strong> (done): Ω<sub>dm,eff</sub> = 0.333 = α exactly, +27% overshoot over observed 0.263. See <a class="wiki-link" onclick="showArticle('bandwidth_integral')">Bandwidth Integral</a>.</p>
<p><strong>2. Bullet Cluster memory-kernel lensing</strong>: naive v×τ<sub>0</sub> = 128 kpc vs observed 720 kpc — full memory-kernel convolution is the falsification test.</p>
<p><strong>3. CMB Boltzmann with n<sub>g</sub>(ω)</strong> replacing ColdDM source: acoustic-peak modes at ωτ<sub>0</sub> ≈ 0.05 preserve the enhancement at face value; full Boltzmann run needed.</p>
<p>Implementation: <code>grut/derived/cosmology/dielectric_dm.py</code>.</p>`,

bandwidth_integral: `<h2>Bandwidth Integral &amp; Ω<sub>dm,eff</sub> = 0.333</h2>
<span class="status computed">COMPUTED (zero free parameters)</span>
<p>The headline V8 Track VII result. Six-step protocol: load P(k) via BBKS transfer function (Planck cosmology), compute ω(k) = k·c<sub>s</sub>, apply Lorentzian enhancement E(k), integrate over linear regime [10<sup>−4</sup>, 0.3] h/Mpc weighted by dimensionless power Δ²(k).</p>
<h3>The Formula</h3>
<div class="eq">Ω<sub>dm,eff</sub> = ∫ E(k) Δ²(k) dk / ∫ Δ²(k) dk<br>
E(k) = α / (1 + (k·c<sub>s</sub>·τ<sub>0</sub>)²)</div>
<h3>The Result</h3>
<div class="eq">Ω<sub>dm,eff</sub> = <strong>0.3333</strong> = α = 1/3 <em>exactly</em></div>
<p>Observed Ω<sub>dm</sub> = 0.263 (Planck). Ratio = <strong>1.267</strong> — GRUT overshoots ΛCDM by <strong>+26.7%</strong>.</p>
<h3>Sensitivity <small>(insensitive to c<sub>s</sub> in linear regime)</small></h3>
<table>
<tr><th>c<sub>s</sub></th><th>Ω<sub>dm,eff</sub></th></tr>
<tr><td>50 km/s</td><td>0.3333</td></tr>
<tr><td>200 km/s</td><td>0.3333</td></tr>
<tr><td>500 km/s</td><td>0.3333</td></tr>
</table>
<p>Every linear-regime mode is deep in the DC limit (ωτ<sub>0</sub> ≪ 1) where the Lorentzian saturates at α. The saturation is <em>geometric</em>, not kinematic — the +27% excess is a structural prediction, not a fit.</p>
<h3>Two Interpretations</h3>
<p><strong>(a) Dielectric overshoots:</strong> a subtractive correction (soliton annihilation, ~7% residual particle component, higher-order n<sub>g</sub>² corrections) brings 0.333 down to 0.263.</p>
<p><strong>(b) ΛCDM underestimates Ω<sub>dm</sub>:</strong> the Planck analysis assumes a slightly wrong expansion history; GRUT's constitutive evolution differs at the percent level during matter domination. The "true" dark component is closer to 0.333.</p>
<p>Either way, the interpretation lands in the right ballpark with <strong>zero free parameters</strong>. Implementation: <code>grut/derived/cosmology/bandwidth_integral.py</code>, 18 NIS-certified tests.</p>`,

track_vii_retraction: `<h2>Track VII — Correction #15 (Ω<sub>dm</sub> = 0.38 RETRACTED)</h2>
<span class="status">RETRACTED &mdash; honest correction</span>
<p>The hardest kind of correction: one that takes back a result that looked like a breakthrough. Caught in April 2026 during the brother's topology audit.</p>
<h3>What Was Claimed</h3>
<p><strong>Track VII Step 1 (April 18, 2026):</strong> Ω<sub>dm</sub> = 0.38 from Kibble-Zurek production of topological defects at the U(1)<sub>dark</sub> phase transition (T = v<sub>dark</sub> = 422 MeV), with XY critical exponents and M<sub>soliton</sub> = 2.11×10⁹ GeV as the defect mass. Appeared to be a "factor of 2" near-miss to observed 0.263 (+44%).</p>
<h3>What Was Wrong</h3>
<p>Two errors that partially canceled:</p>
<ul>
<li><strong>Wrong topology:</strong> used monopole density scaling n ~ 1/ξ³. But U(1)<sub>dark</sub> has π₂ = 0 — <em>no monopoles</em>. Only cosmic strings (π₁(U(1)) = ℤ) exist.</li>
<li><strong>Wrong mass:</strong> used M<sub>soliton</sub> as the defect mass. The natural Kibble-Zurek vorton mass is μ×2π·ξ<sub>KZ</sub> ≈ 4.7×10⁶ GeV, 450× smaller than M<sub>soliton</sub>.</li>
</ul>
<h3>The Corrected Result <small>(Track VII Step 3)</small></h3>
<p>With correct string topology and XY universality:</p>
<div class="eq">Ω<sub>dm</sub> = 0.008 &nbsp;&nbsp; (factor 33 LOW)</div>
<p>The "near-miss" was two errors canceling, not real physics. Track VII CLOSED NEGATIVE for V7's U(1)<sub>dark</sub> particulate route.</p>
<h3>The Response</h3>
<p>The correction was accepted, documented, and folded into the honesty ledger (15 corrections, 0 hallucinations). M<sub>soliton</sub>'s structural derivation from C<sub>FINAL</sub> stands; its <em>physical identification</em> as the DM particle is open. The primary V8 direction pivoted to the <a class="wiki-link" onclick="showArticle('dielectric_dm')">dielectric interpretation</a>, and the <a class="wiki-link" onclick="showArticle('bandwidth_integral')">bandwidth integral</a> now gives Ω<sub>dm,eff</sub> = 0.333 (+27% overshoot, zero free parameters) as the honest replacement.</p>
<h3>The Lesson</h3>
<p>The protocol worked. It caught a two-errors-canceling near-miss before it made it into a headline claim. <em>Documented retractions are not failures of the framework — they are its integrity.</em></p>
<p>Full audit: <code>theory/derivation/TRACK_VII_STEP_03_VORTEX.md</code>.</p>`,
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
        const msgId = 'msg-' + Date.now();
        typing.id = msgId;
        typing.innerHTML = response
            + `<div class="msg-actions">`
            + `<button class="msg-action-btn" onclick="copyResponse('${msgId}')">Copy</button>`
            + `<button class="msg-action-btn viz-btn" onclick="visualizeFromChat('${msgId}')">Visualize</button>`
            + (source === 'claude' ? `<span class="msg-via">via Claude</span>` : '')
            + `</div>`;
    }
    messages.scrollTop = messages.scrollHeight;
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function formatMarkdown(text) {
    // Strip [VIZ:...] tags (visualization is now on every response via the button)
    let html = text.replace(/\[VIZ:\w+\]/g, '');
    // Basic markdown → HTML
    html = html
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/\*(.*?)\*/g, '<em>$1</em>')
        .replace(/`(.*?)`/g, '<code style="background:rgba(79,195,247,0.1);padding:1px 4px;border-radius:3px">$1</code>')
        .replace(/\n\n/g, '<br><br>')
        .replace(/\n/g, '<br>')
        .replace(/•/g, '&bull;')
        .replace(/→/g, '&rarr;');
    return html;
}

function copyResponse(msgId) {
    const el = document.getElementById(msgId);
    if (!el) return;
    // Get text content without the action buttons
    const clone = el.cloneNode(true);
    const actions = clone.querySelector('.msg-actions');
    if (actions) actions.remove();
    const text = clone.innerText || clone.textContent;
    navigator.clipboard.writeText(text).then(() => {
        const btn = el.querySelector('.msg-action-btn');
        if (btn) { const orig = btn.textContent; btn.textContent = 'Copied!'; setTimeout(() => btn.textContent = orig, 1500); }
    });
}

function visualizeFromChat(msgId) {
    const el = document.getElementById(msgId);
    if (!el) return;
    const text = (el.innerText || '').toLowerCase();

    // Score each visualization by keyword relevance (most specific first)
    const scores = {
        bridge: 0,
        era_map: 0,
        scaling_laws: 0,
        decoherence_frontier: 0,
    };

    // Bridge: cosmology chain, Omega_Lambda, tau_0, lab-to-universe
    const bridgeWords = ['bridge', 'omega_lambda', 'cosmological constant', 'tau_0',
        'dark energy', 'h_0', 'hubble', 'planck 2018', 'lab to universe', 'lab → universe',
        'predict the universe', 'vacuum', 'chain'];
    for (const w of bridgeWords) if (text.includes(w)) scores.bridge += 3;
    if (text.includes('ω_λ') || text.includes('ω_lambda') || text.includes('τ₀')) scores.bridge += 3;
    if (text.includes('0.6904') || text.includes('0.6889')) scores.bridge += 5;

    // Era map: cosmological eras, expansion, radiation/matter/acceleration
    const eraWords = ['era map', '329 era', 'expansion history', 'radiation era',
        'matter era', 'acceleration era', 'constitutive cosmology', 'epoch'];
    for (const w of eraWords) if (text.includes(w)) scores.era_map += 3;
    if (text.includes('radiation') && text.includes('matter') && text.includes('acceleration')) scores.era_map += 5;

    // Scaling laws: geometry, kink, material swap, isotope, F1-F6, exponents
    const scalingWords = ['scaling law', 'scaling exponent', 'kink', 'material swap',
        'isotope', 'geometry dependence', 'near-field', 'far-field', 'l/r',
        'suppression factor', 'separation anti', 'protocol a', 'protocol b', 'protocol c',
        'entanglement protection', 'bell state', 'separable'];
    for (const w of scalingWords) if (text.includes(w)) scores.scaling_laws += 3;
    for (const f of ['f1', 'f2', 'f3', 'f4', 'f5', 'f6']) if (text.includes(f + ':') || text.includes(f + ' ')) scores.scaling_laws += 2;
    if (text.includes('beta = -1') || text.includes('β = -1') || text.includes('anti-scaling')) scores.scaling_laws += 5;

    // Decoherence frontier: rates, masses, coherence time, specific measurements
    const decoWords = ['lambda_grav', 'coherence time', 't_coh', 'decoherence rate',
        'gold nanoparticle', 'silica nanoparticle', '689 hz', 'snr', 'signal-to-noise',
        'detectable', 'environmental noise', 'gas scattering', 'blackbody'];
    for (const w of decoWords) if (text.includes(w)) scores.decoherence_frontier += 3;

    // Pick the highest scorer; break ties by specificity order
    const ranked = Object.entries(scores).sort((a, b) => b[1] - a[1]);
    const best = ranked[0];

    if (best[1] > 0) {
        VIZ.open(best[0]);
    } else {
        // True fallback: no keywords matched at all
        VIZ.open('decoherence_frontier');
    }
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

// ══════════════════════════════════════════════════════
// INTERACTIVE PLAYGROUND WIDGETS (April 2026 synthesis)
// Pure SVG — renders instantly, no Chart.js hidden-canvas issues
// ══════════════════════════════════════════════════════

const SVGNS = 'http://www.w3.org/2000/svg';
function svgEl(tag, attrs) {
    const e = document.createElementNS(SVGNS, tag);
    for (const k in attrs) e.setAttribute(k, attrs[k]);
    return e;
}
function clearSvg(svg) {
    while (svg.firstChild) svg.removeChild(svg.firstChild);
}
function drawAxes(svg, W, H, xlabel, ylabel, xticks, yticks) {
    const pad = { l: 48, r: 12, t: 10, b: 28 };
    const plotW = W - pad.l - pad.r, plotH = H - pad.t - pad.b;
    svg.appendChild(svgEl('rect', {x: pad.l, y: pad.t, width: plotW, height: plotH, fill: '#0a0e17', stroke: '#1e2a3a'}));
    (xticks || []).forEach(t => {
        const x = pad.l + t.pos * plotW;
        svg.appendChild(svgEl('line', {x1: x, y1: pad.t, x2: x, y2: pad.t + plotH, stroke: '#1e2a3a', 'stroke-width': 0.5}));
        const tx = svgEl('text', {x: x, y: H - 10, fill: '#6b7a90', 'font-size': 9, 'text-anchor': 'middle'});
        tx.textContent = t.label; svg.appendChild(tx);
    });
    (yticks || []).forEach(t => {
        const y = pad.t + plotH - t.pos * plotH;
        svg.appendChild(svgEl('line', {x1: pad.l, y1: y, x2: pad.l + plotW, y2: y, stroke: '#1e2a3a', 'stroke-width': 0.5}));
        const ty = svgEl('text', {x: pad.l - 4, y: y + 3, fill: '#6b7a90', 'font-size': 9, 'text-anchor': 'end'});
        ty.textContent = t.label; svg.appendChild(ty);
    });
    const xl = svgEl('text', {x: pad.l + plotW/2, y: H - 1, fill: '#6b7a90', 'font-size': 9, 'text-anchor': 'middle'});
    xl.textContent = xlabel; svg.appendChild(xl);
    const yl = svgEl('text', {x: 10, y: pad.t + plotH/2, fill: '#6b7a90', 'font-size': 9, 'text-anchor': 'middle', transform: `rotate(-90 10 ${pad.t + plotH/2})`});
    yl.textContent = ylabel; svg.appendChild(yl);
    return { pad, plotW, plotH };
}
function plotPath(svg, points, layout, xRange, yRange, color, opts={}) {
    const { pad, plotW, plotH } = layout;
    const xmap = x => pad.l + ((x - xRange[0]) / (xRange[1] - xRange[0])) * plotW;
    const ymap = y => pad.t + plotH - ((y - yRange[0]) / (yRange[1] - yRange[0])) * plotH;
    const d = points.map((p, i) => (i === 0 ? 'M' : 'L') + xmap(p[0]).toFixed(1) + ',' + ymap(p[1]).toFixed(1)).join(' ');
    svg.appendChild(svgEl('path', {
        d, fill: opts.fill || 'none', stroke: color,
        'stroke-width': opts.width || 2,
        'stroke-dasharray': opts.dash || '',
        opacity: opts.opacity != null ? opts.opacity : 1
    }));
    return { xmap, ymap };
}
function plotLegend(svg, items, x0, y0) {
    items.forEach((it, i) => {
        const y = y0 + i * 13;
        svg.appendChild(svgEl('line', {x1: x0, y1: y, x2: x0+14, y2: y, stroke: it[0], 'stroke-width': 2, 'stroke-dasharray': it[2] || ''}));
        const tx = svgEl('text', {x: x0+18, y: y+3, fill: '#b0bccf', 'font-size': 9});
        tx.textContent = it[1]; svg.appendChild(tx);
    });
}

// Fixed constants (Phase I canonical)
const ALPHA_CANONICAL = 1/3;
const TAU_0_MYR = 41.9;
const TAU_0_SEC = TAU_0_MYR * 1e6 * 3.156e7;
const OMEGA_DM_OBS = 0.263;
const A0_MS2 = 1.08e-10;
const T_C_K = 5.47e7;   // 54.7 MK
const MPC_M = 3.086e22;
const KPC_M = 3.086e19;
const MSUN_KG = 1.989e30;
const G_NEWTON = 6.6743e-11;

// ─────────────────────────────────────────────────────
// Widget 1: Bandwidth Integral
// ─────────────────────────────────────────────────────
function bbks_T(k_h_per_Mpc, Om_m=0.311, Om_b=0.0486, h=0.7) {
    const Gamma = Om_m * h * Math.exp(-Om_b * (1 + Math.sqrt(2*h)/Om_m));
    const q = k_h_per_Mpc / Gamma;
    if (q < 1e-6) return 1 - 1.17*q;
    const log_term = Math.log(1 + 2.34*q) / (2.34*q);
    const poly = 1 + 3.89*q + Math.pow(16.1*q, 2) + Math.pow(5.46*q, 3) + Math.pow(6.71*q, 4);
    return log_term * Math.pow(poly, -0.25);
}

function delta2(k_h_per_Mpc, n_s=0.965) {
    const T = bbks_T(k_h_per_Mpc);
    const P = Math.pow(k_h_per_Mpc, n_s) * T * T;
    return Math.pow(k_h_per_Mpc, 3) * P / (2 * Math.PI * Math.PI);
}

function updateBandwidth() {
    const alpha = parseFloat(document.getElementById('bw-alpha').value);
    const tauFactor = parseFloat(document.getElementById('bw-tau').value);
    const cs_km = parseFloat(document.getElementById('bw-cs').value);
    const tau0 = TAU_0_SEC * tauFactor;
    const cs = cs_km * 1000;
    const h = 0.7;

    // Display raw slider values
    document.getElementById('bw-alpha-val').textContent = alpha.toFixed(3);
    document.getElementById('bw-tau-val').textContent = (TAU_0_MYR * tauFactor).toFixed(1) + ' Myr';
    document.getElementById('bw-cs-val').textContent = cs_km + ' km/s';

    // Linear-regime integration (k = 1e-4 to 0.3 h/Mpc)
    const n = 256;
    const k_min = 1e-4, k_max = 0.3;
    const log_k_min = Math.log(k_min), log_k_max = Math.log(k_max);
    const ks = [], Es = [], D2s = [];
    for (let i = 0; i < n; i++) {
        const log_k = log_k_min + (log_k_max - log_k_min) * i / (n-1);
        const k = Math.exp(log_k);
        const k_per_m = k * h / MPC_M;
        const omega = k_per_m * cs;
        const x = omega * tau0;
        const E = alpha / (1 + x*x);
        const D2 = delta2(k);
        ks.push(k); Es.push(E); D2s.push(D2);
    }
    // Weighted average (dk integration)
    let num = 0, den = 0;
    for (let i = 0; i < n-1; i++) {
        const dk = ks[i+1] - ks[i];
        num += E_trap(Es[i], Es[i+1], D2s[i], D2s[i+1], dk);
        den += (D2s[i] + D2s[i+1]) / 2 * dk;
    }
    const omega_eff = num / den;
    const overshoot = (omega_eff / OMEGA_DM_OBS - 1) * 100;

    // Update stats
    document.getElementById('bw-omega').textContent = omega_eff.toFixed(4);
    const overshootEl = document.getElementById('bw-overshoot');
    overshootEl.textContent = (overshoot >= 0 ? '+' : '') + overshoot.toFixed(1) + '%';
    overshootEl.style.color = Math.abs(overshoot) < 5 ? 'var(--green)' : (overshoot > 0 ? '#ffd54f' : '#ff7961');

    // Update STAGE: bar width proportional to Omega_dm_eff / 0.45 scale
    const SCALE_MAX = 0.45;
    const bar = document.getElementById('stage-bar');
    const pred = document.getElementById('stage-pred');
    if (bar && pred) {
        const pct = Math.min(1, omega_eff / SCALE_MAX);
        bar.setAttribute('width', 560 * pct);
        pred.setAttribute('x', 30 + 560 * pct - 8);
        pred.textContent = `Ω_eff = ${omega_eff.toFixed(3)}`;
        pred.setAttribute('text-anchor', 'end');
    }

    // Badge logic
    const maxX = Math.max(...ks.map(k => (k * h / MPC_M) * cs * tau0));
    const badge = document.getElementById('bw-badge');
    if (maxX < 0.01) {
        badge.textContent = 'FULL ENHANCEMENT (DC REGIME)';
        badge.className = 'widget-badge badge-full';
    } else if (maxX < 1) {
        badge.textContent = 'INTERMEDIATE — PARTIAL SCREENING';
        badge.className = 'widget-badge badge-intermediate';
    } else {
        badge.textContent = 'HIGH-FREQUENCY — SUPPRESSED';
        badge.className = 'widget-badge badge-suppressed';
    }

    // SVG Plot: E(k) curve + Δ²(k) weight + α DC line
    const svg = document.getElementById('plot-bandwidth');
    if (!svg) return;
    clearSvg(svg);
    const W = 600, H = 180;
    const maxD2 = Math.max(...D2s);
    const xTicks = [
        { pos: 0,    label: '10⁻⁴' }, { pos: 0.25, label: '10⁻³' },
        { pos: 0.5,  label: '10⁻²' }, { pos: 0.75, label: '10⁻¹' },
        { pos: 1,    label: '0.3'  },
    ];
    const yTicks = [
        { pos: 0,    label: '0'   }, { pos: 0.25, label: '0.1' },
        { pos: 0.5,  label: '0.2' }, { pos: 0.75, label: '0.3' },
        { pos: 1,    label: '0.4' },
    ];
    const layout = drawAxes(svg, W, H, 'k (h/Mpc) — observable matter power spectrum', 'E(k)', xTicks, yTicks);
    const xRange = [Math.log(k_min), Math.log(k_max)];
    const yRange = [0, 0.4];
    // Δ² weight (normalized)
    const D2pts = D2s.map((d, i) => [Math.log(ks[i]), (d/maxD2) * alpha]);
    plotPath(svg, D2pts, layout, xRange, yRange, '#ce93d8', { dash: '4,3', width: 1.5, opacity: 0.7 });
    // α DC reference line
    plotPath(svg, [[xRange[0], alpha], [xRange[1], alpha]], layout, xRange, yRange, '#ffd54f', { dash: '2,2', width: 1 });
    // E(k) filled area
    const Epts = Es.map((e, i) => [Math.log(ks[i]), e]);
    const filled = [[xRange[0], 0], ...Epts, [xRange[1], 0]];
    plotPath(svg, filled, layout, xRange, yRange, 'transparent', { fill: 'rgba(79,195,247,0.2)' });
    plotPath(svg, Epts, layout, xRange, yRange, '#4fc3f7', { width: 2.5 });
    plotLegend(svg, [
        ['#4fc3f7', 'E(k) = α/(1+(ωτ₀)²)'],
        ['#ce93d8', 'Δ²(k) weight (scaled)', '4,3'],
        ['#ffd54f', 'α DC limit', '2,2'],
    ], 56, 20);
}

// ─────────────────────────────────────────────────────
// Widget 2: Rotation Curve
// ─────────────────────────────────────────────────────
function nu_interp(y) {
    if (y <= 0) return Infinity;
    return 0.5 + Math.sqrt(0.25 + 1/y);
}

function updateRotation() {
    const logM = parseFloat(document.getElementById('rc-logM').value);
    const r_max_kpc = parseFloat(document.getElementById('rc-rmax').value);
    const M_Msun = Math.pow(10, logM);
    const M_kg = M_Msun * MSUN_KG;

    // Slider display
    document.getElementById('rc-logM-val').textContent = `${(M_Msun/1e10).toFixed(1)}×10¹⁰ M☉`;
    document.getElementById('rc-rmax-val').textContent = `${r_max_kpc.toFixed(0)} kpc`;

    // v_flat from BTFR: v^4 = G M a_0
    const v_flat = Math.pow(G_NEWTON * M_kg * A0_MS2, 0.25);
    document.getElementById('rc-vflat').textContent = `${(v_flat/1000).toFixed(0)} km/s`;

    // Compute v(r) curve
    const n = 80;
    const r_arr_kpc = [];
    const v_N = [], v_G = [];
    for (let i = 0; i < n; i++) {
        const r_kpc = 0.5 + (r_max_kpc - 0.5) * i / (n-1);
        const r_m = r_kpc * KPC_M;
        const g_bar = G_NEWTON * M_kg / (r_m * r_m);
        const v_newton = Math.sqrt(g_bar * r_m);
        // Self-consistent ω from v_newton
        const omega = v_newton / r_m;
        const y = g_bar / A0_MS2;
        const nu = nu_interp(y);
        const X = omega * TAU_0_SEC;
        const g_eff = g_bar * (1 + (nu - 1) / (1 + X*X));
        const v_grut = Math.sqrt(g_eff * r_m);
        r_arr_kpc.push(r_kpc);
        v_N.push(v_newton/1000);
        v_G.push(v_grut/1000);
    }

    // Diagnostic at r = 10 kpc
    const r_diag = 10 * KPC_M;
    const g_diag = G_NEWTON * M_kg / (r_diag * r_diag);
    const v_diag = Math.sqrt(g_diag * r_diag);
    const y_diag = g_diag / A0_MS2;
    const X_diag = (v_diag / r_diag) * TAU_0_SEC;
    document.getElementById('rc-y').textContent = y_diag.toFixed(2);
    document.getElementById('rc-x').textContent = X_diag.toFixed(2);

    // Update STAGE: velocity labels at fixed radii (5, 10, 20, 50 kpc)
    [[5, 'stage-v1'], [10, 'stage-v2'], [20, 'stage-v3'], [50, 'stage-v4']].forEach(([rk, id]) => {
        const rm = rk * KPC_M;
        const g = G_NEWTON * M_kg / (rm*rm);
        const vn = Math.sqrt(g * rm);
        const yv = g / A0_MS2;
        const Xv = (vn / rm) * TAU_0_SEC;
        const nuv = nu_interp(yv);
        const g_eff_v = g * (1 + (nuv - 1) / (1 + Xv*Xv));
        const v_grut_v = Math.sqrt(g_eff_v * rm) / 1000;
        const el = document.getElementById(id);
        if (el) { el.textContent = `${v_grut_v.toFixed(0)} km/s`; }
    });
    // Bulge size scales with log(mass)
    const bulge = document.getElementById('stage-bulge');
    if (bulge) { bulge.setAttribute('r', 6 + logM); }

    // Badge
    const badge = document.getElementById('rc-badge');
    if (y_diag > 10) {
        badge.textContent = 'NEWTONIAN REGIME (INNER)';
        badge.className = 'widget-badge badge-suppressed';
    } else if (y_diag < 0.1 && X_diag < 0.1) {
        badge.textContent = 'DEEP RESPONSE (BTFR FLAT)';
        badge.className = 'widget-badge badge-full';
    } else {
        badge.textContent = 'INTERMEDIATE REGIME';
        badge.className = 'widget-badge badge-intermediate';
    }

    // SVG Plot: v_Newton (baryons only) vs v_GRUT vs v_flat (BTFR)
    const svg = document.getElementById('plot-rotation');
    if (!svg) return;
    clearSvg(svg);
    const W = 600, H = 180;
    const y_max = Math.max(v_flat/1000 * 1.3, Math.max(...v_G) * 1.1, Math.max(...v_N) * 1.1);
    const xTicks = [
        { pos: 0,    label: '0' },
        { pos: 0.25, label: (r_max_kpc*0.25).toFixed(0) },
        { pos: 0.5,  label: (r_max_kpc*0.5).toFixed(0)  },
        { pos: 0.75, label: (r_max_kpc*0.75).toFixed(0) },
        { pos: 1,    label: r_max_kpc.toFixed(0) },
    ];
    const yTicks = [];
    for (let j = 0; j <= 4; j++) yTicks.push({ pos: j/4, label: (y_max * j/4).toFixed(0) });
    const layout = drawAxes(svg, W, H, 'radius (kpc)', 'v_circ (km/s)', xTicks, yTicks);
    const xRange = [0, r_max_kpc], yRange = [0, y_max];
    // v_flat horizontal reference
    plotPath(svg, [[0, v_flat/1000], [r_max_kpc, v_flat/1000]], layout, xRange, yRange, '#66bb6a', { dash: '3,3', width: 1 });
    // v_GRUT filled area under curve
    const vG_pts = r_arr_kpc.map((r, i) => [r, v_G[i]]);
    const vG_fill = [[0, 0], ...vG_pts, [r_max_kpc, 0]];
    plotPath(svg, vG_fill, layout, xRange, yRange, 'transparent', { fill: 'rgba(79,195,247,0.18)' });
    plotPath(svg, vG_pts, layout, xRange, yRange, '#4fc3f7', { width: 2.5 });
    // v_Newton dashed red
    plotPath(svg, r_arr_kpc.map((r, i) => [r, v_N[i]]), layout, xRange, yRange, '#ff7961', { dash: '5,3', width: 2 });
    plotLegend(svg, [
        ['#4fc3f7', 'v_GRUT (ν(y) engine)'],
        ['#ff7961', 'v_Newton (baryons only)', '5,3'],
        ['#66bb6a', `v_flat = ${(v_flat/1000).toFixed(0)} km/s (BTFR)`, '3,3'],
    ], 56, 20);
}

// ─────────────────────────────────────────────────────
// Widget 3: Thermal Transition
// ─────────────────────────────────────────────────────
function memoryActivation(T_K) {
    if (T_K <= 0) return 1.0;
    const width = 0.3;
    const x = Math.log(T_C_K / T_K) / width;
    return 1.0 / (1 + Math.exp(-x));
}

function updateThermal() {
    const logT = parseFloat(document.getElementById('tt-logT').value);
    const T = Math.pow(10, logT);
    const f = memoryActivation(T);
    const ng = Math.sqrt(1 + f * ALPHA_CANONICAL);

    // Display
    let T_display;
    if (T < 1e3) T_display = T.toFixed(T < 10 ? 2 : 0) + ' K';
    else if (T < 1e6) T_display = (T/1e3).toFixed(1) + ' kK';
    else if (T < 1e9) T_display = (T/1e6).toFixed(1) + ' MK';
    else T_display = (T/1e9).toFixed(1) + ' GK';

    let era = '';
    if (T < 5) era = 'today (CMB)';
    else if (T < 1e4) era = 'recombination era';
    else if (T < 1e7) era = 'approaching T_c';
    else if (T < 1e8) era = 'crossing T_c transition';
    else if (T < 1e9) era = 'plasma era (post-BBN)';
    else era = 'BBN / early universe';

    document.getElementById('tt-T').textContent = T_display;
    document.getElementById('tt-f').textContent = f.toFixed(4);
    document.getElementById('tt-ng').textContent = ng.toFixed(4);
    document.getElementById('tt-logT-val').textContent = `T = ${T_display} (${era})`;

    // Update STAGE: move pointer along the timeline bar (logT = 0..12 → x = 20..580)
    const pointer = document.getElementById('stage-pointer');
    const ptrLabel = document.getElementById('stage-ptr-label');
    if (pointer && ptrLabel) {
        const x = 20 + (560 * logT / 12);
        pointer.setAttribute('points', `${x},40 ${x-5},30 ${x+5},30`);
        ptrLabel.setAttribute('x', x);
        ptrLabel.textContent = era.toUpperCase();
    }

    // Badge
    const badge = document.getElementById('tt-badge');
    if (f > 0.99) {
        badge.textContent = 'DEEP REFRACTIVE REGIME (T ≪ T_c)';
        badge.className = 'widget-badge badge-full';
    } else if (f > 0.1) {
        badge.textContent = 'CROSSING T_c TRANSITION';
        badge.className = 'widget-badge badge-intermediate';
    } else {
        badge.textContent = 'ABOVE BOILING POINT — NO MEMORY';
        badge.className = 'widget-badge badge-suppressed';
    }

    // Chart: activation fraction across log(T), mark current T
    const n = 120;
    const logT_min = 0, logT_max = 12;
    const logTs = [], fs = [], ng_arr = [];
    for (let i = 0; i < n; i++) {
        const lt = logT_min + (logT_max - logT_min) * i / (n-1);
        const t = Math.pow(10, lt);
        const fi = memoryActivation(t);
        logTs.push(lt);
        fs.push(fi);
        ng_arr.push(Math.sqrt(1 + fi * ALPHA_CANONICAL));
    }

    // SVG Plot: f(T) sigmoid + n_g enhancement + T_c marker + current-T marker
    const svg = document.getElementById('plot-thermal');
    if (!svg) return;
    clearSvg(svg);
    const W = 600, H = 180;
    const xTicks = [];
    for (let j = 0; j <= 6; j++) xTicks.push({ pos: j/6, label: (j*2).toFixed(0) });
    const yTicks = [
        { pos: 0, label: '0' }, { pos: 0.25, label: '0.25' },
        { pos: 0.5, label: '0.5' }, { pos: 0.75, label: '0.75' },
        { pos: 1, label: '1.0' },
    ];
    const layout = drawAxes(svg, W, H, 'log₁₀(T / K)', 'activation f(T)', xTicks, yTicks);
    const xRange = [0, 12], yRange = [0, 1.05];
    // T_c vertical marker
    const logTc = Math.log10(T_C_K);
    plotPath(svg, [[logTc, 0], [logTc, 1.05]], layout, xRange, yRange, '#ffd54f', { dash: '3,3', width: 1 });
    // n_g enhancement (rescaled so max fits)
    const ng_pts = logTs.map((lt, i) => [lt, (ng_arr[i] - 1) / 0.1547]);
    plotPath(svg, ng_pts, layout, xRange, yRange, '#ce93d8', { width: 1.5 });
    // f(T) filled
    const f_pts = logTs.map((lt, i) => [lt, fs[i]]);
    const f_fill = [[0, 0], ...f_pts, [12, 0]];
    plotPath(svg, f_fill, layout, xRange, yRange, 'transparent', { fill: 'rgba(79,195,247,0.2)' });
    plotPath(svg, f_pts, layout, xRange, yRange, '#4fc3f7', { width: 2.5 });
    // Current T marker (bold green)
    plotPath(svg, [[logT, 0], [logT, 1.05]], layout, xRange, yRange, '#66bb6a', { width: 2.5 });
    // Current-T circle on the curve
    const cur = svgEl('circle', {
        cx: layout.pad.l + (logT/12) * layout.plotW,
        cy: layout.pad.t + layout.plotH - (f / 1.05) * layout.plotH,
        r: 5, fill: '#66bb6a', stroke: '#ffffff', 'stroke-width': 1.5
    });
    svg.appendChild(cur);
    plotLegend(svg, [
        ['#4fc3f7', 'memory activation f(T)'],
        ['#ce93d8', 'n_g(T) enhancement'],
        ['#ffd54f', 'T_c = 54.7 MK', '3,3'],
        ['#66bb6a', 'current T'],
    ], 380, 20);
}

// Wire up all sliders to update functions
function initPlayground() {
    ['bw-alpha', 'bw-tau', 'bw-cs'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.addEventListener('input', updateBandwidth);
    });
    ['rc-logM', 'rc-rmax'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.addEventListener('input', updateRotation);
    });
    const ttEl = document.getElementById('tt-logT');
    if (ttEl) ttEl.addEventListener('input', updateThermal);
    // Initial render
    try { updateBandwidth(); updateRotation(); updateThermal(); } catch(e) { console.error('Playground init error:', e); }
}

async function init() {
    await loadHealth();
    await checkAI();
    showArticle('ctp');
    initPlayground();
}
init();
