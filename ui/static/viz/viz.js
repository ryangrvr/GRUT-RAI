// GRUT RAI — Interactive Visualization Engine
// Each viz is a self-contained canvas with sliders and real-time computation

const VIZ = {
    active: null,
    container: null,

    open(vizName) {
        if (!this.container) {
            this.container = document.createElement('div');
            this.container.className = 'viz-overlay';
            this.container.innerHTML = '<div class="viz-modal"><div class="viz-header"><span class="viz-title"></span><button class="viz-close" onclick="VIZ.close()">&times;</button></div><div class="viz-body"></div></div>';
            document.body.appendChild(this.container);
        }
        this.container.style.display = 'flex';
        this.container.querySelector('.viz-title').textContent = VISUALIZATIONS[vizName]?.title || vizName;
        const body = this.container.querySelector('.viz-body');
        body.innerHTML = '';
        if (VISUALIZATIONS[vizName]) {
            VISUALIZATIONS[vizName].render(body);
        }
        this.active = vizName;
    },

    close() {
        if (this.container) this.container.style.display = 'none';
        this.active = null;
    }
};

// ═══════════════════════════════════════════════════════
// VIZ 1: DECOHERENCE FRONTIER
// ═══════════════════════════════════════════════════════

const VISUALIZATIONS = {

decoherence_frontier: {
    title: 'Matter-Wave Decoherence Frontier',
    render(el) {
        el.innerHTML = `
        <div class="viz-panel">
            <div class="viz-metrics">
                <div class="viz-metric"><span class="viz-metric-label">MASS</span><span class="viz-metric-value" id="vf-mass">80.8 pg</span></div>
                <div class="viz-metric"><span class="viz-metric-label">LAMBDA</span><span class="viz-metric-value" id="vf-lambda">689 Hz</span></div>
                <div class="viz-metric"><span class="viz-metric-label">REGIME</span><span class="viz-metric-value" id="vf-regime">Classical</span></div>
                <div class="viz-metric"><span class="viz-metric-label">t_coh</span><span class="viz-metric-value" id="vf-tcoh">1.5 ms</span></div>
            </div>
            <canvas id="vf-canvas" width="800" height="400"></canvas>
            <div class="viz-controls">
                <div class="viz-slider-group">
                    <label>log₁₀(mass) [amu]</label>
                    <input type="range" id="vf-mass-slider" min="1" max="15" step="0.1" value="10">
                    <span id="vf-mass-val">10</span>
                </div>
                <div class="viz-slider-group">
                    <label>Separation [m]</label>
                    <input type="range" id="vf-sep-slider" min="-9" max="-4" step="0.1" value="-6">
                    <span id="vf-sep-val">1 μm</span>
                </div>
                <div class="viz-slider-group">
                    <label>Material</label>
                    <select id="vf-material">
                        <option value="19300">Gold (19,300)</option>
                        <option value="2200">Silica (2,200)</option>
                        <option value="3510">Diamond (3,510)</option>
                        <option value="1000">Water (1,000)</option>
                        <option value="22590">Osmium (22,590)</option>
                    </select>
                </div>
            </div>
        </div>`;

        const canvas = document.getElementById('vf-canvas');
        const ctx = canvas.getContext('2d');
        const massSlider = document.getElementById('vf-mass-slider');
        const sepSlider = document.getElementById('vf-sep-slider');
        const matSelect = document.getElementById('vf-material');

        const knownExperiments = [
            {name: 'C60', mass_amu: 720, year: 1999},
            {name: 'PFNS8', mass_amu: 10123, year: 2011},
            {name: 'Fein 2019', mass_amu: 25000, year: 2019},
        ];

        function draw() {
            const logM = parseFloat(massSlider.value);
            const logL = parseFloat(sepSlider.value);
            const rho = parseFloat(matSelect.value);
            const m_amu = Math.pow(10, logM);
            const m_kg = m_amu * 1.661e-27;
            const l = Math.pow(10, logL);
            const R = Math.pow(3*m_kg/(4*Math.PI*rho), 1/3);
            const lR = l/R;
            const S = lR < 1 ? Math.pow(lR,3)/6 : 1.0;
            const G = 6.674e-11, HBAR = 1.055e-34;
            const Lambda = G*m_kg*m_kg*S/(HBAR*l);
            const t_coh = 1/Lambda;

            // Update metrics
            document.getElementById('vf-mass').textContent = m_amu >= 1e6 ? (m_amu).toExponential(1)+' amu' : Math.round(m_amu)+' amu';
            document.getElementById('vf-lambda').textContent = Lambda >= 1 ? Lambda.toFixed(0)+' Hz' : Lambda.toExponential(2)+' Hz';
            document.getElementById('vf-tcoh').textContent = t_coh < 1 ? (t_coh*1000).toFixed(1)+' ms' : t_coh < 60 ? t_coh.toFixed(1)+' s' : (t_coh/3.156e7).toExponential(1)+' yr';
            document.getElementById('vf-mass-val').textContent = logM.toFixed(1);

            const sepM = Math.pow(10, logL);
            document.getElementById('vf-sep-val').textContent = logL >= -3 ? (sepM*1e3).toFixed(1)+' mm' : logL >= -6 ? (sepM*1e6).toFixed(1)+' μm' : (sepM*1e9).toFixed(1)+' nm';

            let regime = 'Quantum';
            if (Lambda > 1e3) regime = 'Classical';
            else if (Lambda > 1e-3) regime = 'Marginal';
            document.getElementById('vf-regime').textContent = regime;
            document.getElementById('vf-regime').style.color = regime === 'Quantum' ? '#4fc3f7' : regime === 'Marginal' ? '#ffd54f' : '#ef5350';

            // Draw chart
            const W = canvas.width, H = canvas.height;
            ctx.fillStyle = '#0a0e17';
            ctx.fillRect(0, 0, W, H);

            const pad = {l:60, r:20, t:30, b:40};
            const pw = W-pad.l-pad.r, ph = H-pad.t-pad.b;

            // Axes
            ctx.strokeStyle = '#1e2a3a'; ctx.lineWidth = 1;
            ctx.beginPath(); ctx.moveTo(pad.l, pad.t); ctx.lineTo(pad.l, H-pad.b); ctx.lineTo(W-pad.r, H-pad.b); ctx.stroke();

            // Labels
            ctx.fillStyle = '#6b7a90'; ctx.font = '11px monospace'; ctx.textAlign = 'center';
            ctx.fillText('Particle Mass (amu) →', W/2, H-5);
            ctx.save(); ctx.translate(12, H/2); ctx.rotate(-Math.PI/2); ctx.fillText('↑ Fringe Drop (%)', 0, 0); ctx.restore();

            // Mass range: 10^2 to 10^15
            const mMin = 2, mMax = 15, fMin = -22, fMax = 2;

            function xPos(logMass) { return pad.l + (logMass - mMin)/(mMax - mMin) * pw; }
            function yPos(logFringe) { return pad.t + (fMax - logFringe)/(fMax - fMin) * ph; }

            // Grid
            ctx.strokeStyle = '#1e2a3a'; ctx.lineWidth = 0.5;
            for (let m = mMin; m <= mMax; m += 1) {
                const x = xPos(m);
                ctx.beginPath(); ctx.moveTo(x, pad.t); ctx.lineTo(x, H-pad.b); ctx.stroke();
                ctx.fillStyle = '#6b7a90'; ctx.font = '9px monospace'; ctx.fillText('10^'+m, x, H-pad.b+15);
            }

            // Regime zones
            ctx.fillStyle = 'rgba(79,195,247,0.05)';
            ctx.fillRect(xPos(mMin), pad.t, xPos(5)-xPos(mMin), ph);
            ctx.fillStyle = 'rgba(255,213,79,0.05)';
            ctx.fillRect(xPos(5), pad.t, xPos(10)-xPos(5), ph);
            ctx.fillStyle = 'rgba(239,83,80,0.05)';
            ctx.fillRect(xPos(10), pad.t, xPos(mMax)-xPos(10), ph);

            ctx.fillStyle = '#4fc3f7'; ctx.font = '10px monospace';
            ctx.fillText('Quantum Regime', xPos(3.5), pad.t+15);
            ctx.fillStyle = '#ffd54f';
            ctx.fillText('Marginal Transition', xPos(7.5), pad.t+15);
            ctx.fillStyle = '#ef5350';
            ctx.fillText('GRUT Regime', xPos(12.5), pad.t+15);

            // The decoherence curve
            ctx.strokeStyle = '#4fc3f7'; ctx.lineWidth = 2;
            ctx.beginPath();
            let first = true;
            for (let lm = mMin; lm <= mMax; lm += 0.1) {
                const mi = Math.pow(10, lm) * 1.661e-27;
                const Ri = Math.pow(3*mi/(4*Math.PI*rho), 1/3);
                const Si = l/Ri < 1 ? Math.pow(l/Ri,3)/6 : 1.0;
                const Li = G*mi*mi*Si/(HBAR*l);
                // Fringe drop: approx exp(-Lambda * t_flight) with t_flight ~ 1s
                const fringe = Math.min(100, Li > 0 ? Math.max(1e-22, 100*Math.exp(-Li*0.001)) : 100);
                const logF = Math.log10(fringe);
                const x = xPos(lm), y = yPos(logF);
                if (y >= pad.t && y <= H-pad.b) {
                    if (first) { ctx.moveTo(x, y); first = false; }
                    else ctx.lineTo(x, y);
                }
            }
            ctx.stroke();

            // Known experiments
            ctx.fillStyle = '#6b7a90';
            for (const exp of knownExperiments) {
                const lm = Math.log10(exp.mass_amu);
                const mi = exp.mass_amu * 1.661e-27;
                const Ri = Math.pow(3*mi/(4*Math.PI*2200), 1/3);
                const Si = l/Ri < 1 ? Math.pow(l/Ri,3)/6 : 1.0;
                const Li = G*mi*mi*Si/(HBAR*l);
                const fringe = Math.min(100, Li > 0 ? Math.max(1e-22, 100*Math.exp(-Li*0.001)) : 100);
                const x = xPos(lm), y = yPos(Math.log10(fringe));
                ctx.beginPath(); ctx.arc(x, y, 5, 0, Math.PI*2); ctx.fill();
                ctx.fillStyle = '#e0e6f0'; ctx.font = '9px monospace';
                ctx.fillText(exp.name, x, y-10);
                ctx.fillStyle = '#6b7a90';
            }

            // Target marker
            const tX = xPos(logM), tY = yPos(Math.log10(Math.min(100, Lambda > 0 ? Math.max(1e-22, 100*Math.exp(-Lambda*0.001)) : 100)));
            ctx.fillStyle = '#ce93d8';
            ctx.beginPath(); ctx.arc(tX, Math.min(Math.max(tY, pad.t), H-pad.b), 8, 0, Math.PI*2); ctx.fill();
            ctx.fillStyle = '#e0e6f0'; ctx.font = '11px monospace';
            ctx.fillText('Target: '+m_amu.toExponential(1)+' amu', tX, Math.min(Math.max(tY-15, pad.t+25), H-pad.b-5));
        }

        massSlider.oninput = draw;
        sepSlider.oninput = draw;
        matSelect.onchange = draw;
        draw();
    }
},

// ═══════════════════════════════════════════════════════
// VIZ 2: SCALING LAWS EXPLORER
// ═══════════════════════════════════════════════════════

scaling_laws: {
    title: 'Scaling Laws: The Six Signatures',
    render(el) {
        el.innerHTML = `
        <div class="viz-panel">
            <div class="viz-metrics">
                <div class="viz-metric"><span class="viz-metric-label">MASS</span><span class="viz-metric-value" id="vs-mass">80.8 pg</span></div>
                <div class="viz-metric"><span class="viz-metric-label">RADIUS</span><span class="viz-metric-value" id="vs-radius">1.0 μm</span></div>
                <div class="viz-metric"><span class="viz-metric-label">KINK AT</span><span class="viz-metric-value" id="vs-kink">1.8 μm</span></div>
                <div class="viz-metric"><span class="viz-metric-label">MATERIAL</span><span class="viz-metric-value" id="vs-mat">Gold</span></div>
            </div>
            <canvas id="vs-canvas" width="800" height="400"></canvas>
            <div class="viz-controls">
                <div class="viz-slider-group">
                    <label>Mass [pg]</label>
                    <input type="range" id="vs-mass-slider" min="1" max="200" step="1" value="81">
                    <span id="vs-mass-val">81</span>
                </div>
                <div class="viz-slider-group">
                    <label>Material</label>
                    <select id="vs-material" onchange="this.dispatchEvent(new Event('input'))">
                        <option value="19300" data-name="Gold">Gold (19,300 kg/m³)</option>
                        <option value="2200" data-name="Silica">Silica (2,200 kg/m³)</option>
                        <option value="3510" data-name="Diamond">Diamond (3,510 kg/m³)</option>
                    </select>
                </div>
                <div class="viz-slider-group">
                    <label>Show comparison</label>
                    <input type="checkbox" id="vs-compare" checked>
                    <span style="font-size:11px;color:var(--dim)">F2: Same mass, different material</span>
                </div>
            </div>
        </div>`;

        const canvas = document.getElementById('vs-canvas');
        const ctx = canvas.getContext('2d');
        const massSlider = document.getElementById('vs-mass-slider');
        const matSelect = document.getElementById('vs-material');
        const compareCheck = document.getElementById('vs-compare');
        const G = 6.674e-11, HBAR = 1.055e-34;

        function computeCurve(m_kg, rho, color, label) {
            const R = Math.pow(3*m_kg/(4*Math.PI*rho), 1/3);
            const points = [];
            for (let logL = -8.5; logL <= -3.5; logL += 0.05) {
                const l = Math.pow(10, logL);
                const lR = l/R;
                const S = lR < 1 ? Math.pow(lR,3)/6 : 1.0;
                const Lambda = G*m_kg*m_kg*S/(HBAR*l);
                points.push({logL, logLambda: Math.log10(Lambda), l, Lambda});
            }
            return {points, R, color, label};
        }

        function draw() {
            const m_pg = parseFloat(massSlider.value);
            const m_kg = m_pg * 1e-15;
            const rho = parseFloat(matSelect.value);
            const matName = matSelect.options[matSelect.selectedIndex].dataset.name;

            const curve1 = computeCurve(m_kg, rho, '#4fc3f7', matName);
            const curves = [curve1];
            if (compareCheck.checked && rho !== 2200) {
                curves.push(computeCurve(m_kg, 2200, '#ef5350', 'Silica'));
            } else if (compareCheck.checked && rho === 2200) {
                curves.push(computeCurve(m_kg, 19300, '#ffd54f', 'Gold'));
            }

            document.getElementById('vs-mass').textContent = m_pg + ' pg';
            document.getElementById('vs-radius').textContent = (curve1.R*1e6).toFixed(2) + ' μm';
            document.getElementById('vs-kink').textContent = (1.8*curve1.R*1e6).toFixed(2) + ' μm';
            document.getElementById('vs-mat').textContent = matName;
            document.getElementById('vs-mass-val').textContent = m_pg;

            const W = canvas.width, H = canvas.height;
            ctx.fillStyle = '#0a0e17'; ctx.fillRect(0, 0, W, H);
            const pad = {l:60, r:20, t:30, b:40};
            const pw = W-pad.l-pad.r, ph = H-pad.t-pad.b;

            const xMin = -8.5, xMax = -3.5, yMin = -10, yMax = 15;
            function xPos(v) { return pad.l + (v-xMin)/(xMax-xMin)*pw; }
            function yPos(v) { return pad.t + (yMax-v)/(yMax-yMin)*ph; }

            // Grid
            ctx.strokeStyle = '#1e2a3a'; ctx.lineWidth = 0.5;
            for (let x = -8; x <= -4; x++) {
                const px = xPos(x);
                ctx.beginPath(); ctx.moveTo(px, pad.t); ctx.lineTo(px, H-pad.b); ctx.stroke();
                ctx.fillStyle = '#6b7a90'; ctx.font = '9px monospace'; ctx.textAlign = 'center';
                ctx.fillText('10^'+x, px, H-pad.b+15);
            }
            ctx.fillText('log₁₀(l) [m]', W/2, H-5);
            ctx.save(); ctx.translate(12,H/2); ctx.rotate(-Math.PI/2);
            ctx.fillText('log₁₀(Λ) [Hz]', 0, 0); ctx.restore();

            // Kink line
            const kinkX = xPos(Math.log10(1.8*curve1.R));
            ctx.strokeStyle = '#ffd54f'; ctx.lineWidth = 1; ctx.setLineDash([4,4]);
            ctx.beginPath(); ctx.moveTo(kinkX, pad.t); ctx.lineTo(kinkX, H-pad.b); ctx.stroke();
            ctx.setLineDash([]);
            ctx.fillStyle = '#ffd54f'; ctx.font = '10px monospace';
            ctx.fillText('Kink: l = 1.8R', kinkX, pad.t+15);

            // Slope labels
            const nearX = xPos(-7.5), farX = xPos(-4.5);
            ctx.fillStyle = '#4fc3f7'; ctx.font = '10px monospace';
            ctx.fillText('Slope +2', nearX, pad.t+30);
            ctx.fillText('(near field)', nearX, pad.t+42);
            ctx.fillText('Slope -1', farX, pad.t+30);
            ctx.fillText('(far field)', farX, pad.t+42);

            // Draw curves
            for (const curve of curves) {
                ctx.strokeStyle = curve.color; ctx.lineWidth = 2;
                ctx.beginPath();
                let first = true;
                for (const p of curve.points) {
                    const x = xPos(p.logL), y = yPos(p.logLambda);
                    if (y >= pad.t && y <= H-pad.b) {
                        if (first) { ctx.moveTo(x, y); first = false; }
                        else ctx.lineTo(x, y);
                    }
                }
                ctx.stroke();
                // Legend
                ctx.fillStyle = curve.color; ctx.font = '11px monospace';
                const ly = pad.t + 60 + curves.indexOf(curve)*16;
                ctx.fillRect(W-pad.r-100, ly-4, 12, 3);
                ctx.fillText(curve.label, W-pad.r-82, ly);
            }
        }

        massSlider.oninput = draw;
        matSelect.oninput = draw;
        compareCheck.onchange = draw;
        draw();
    }
},

// ═══════════════════════════════════════════════════════
// VIZ 3: COSMIC ERA MAP
// ═══════════════════════════════════════════════════════

era_map: {
    title: 'Cosmic Era Map — 329 Eras of Constitutive Evolution',
    render(el) {
        el.innerHTML = `
        <div class="viz-panel">
            <div class="viz-metrics">
                <div class="viz-metric"><span class="viz-metric-label">ERA</span><span class="viz-metric-value" id="ve-era">329</span></div>
                <div class="viz-metric"><span class="viz-metric-label">AGE</span><span class="viz-metric-value" id="ve-age">13.8 Gyr</span></div>
                <div class="viz-metric"><span class="viz-metric-label">VACUUM %</span><span class="viz-metric-value" id="ve-vac">70%</span></div>
                <div class="viz-metric"><span class="viz-metric-label">PHASE</span><span class="viz-metric-value" id="ve-phase">Acceleration</span></div>
            </div>
            <canvas id="ve-canvas" width="800" height="350"></canvas>
            <div class="viz-controls">
                <div class="viz-slider-group" style="flex:1">
                    <label>Cosmic Step (Era)</label>
                    <input type="range" id="ve-slider" min="1" max="329" step="1" value="329" style="width:100%">
                </div>
            </div>
        </div>`;

        const canvas = document.getElementById('ve-canvas');
        const ctx = canvas.getContext('2d');
        const slider = document.getElementById('ve-slider');

        // Pre-compute era map
        const alpha = 1 - Math.exp(-1), gamma = 0.000982, k = 2*Math.PI/(1.5428-1), N_th = 215;
        const eras = [{era:0, x:0, target:0, memory:0}];
        let x = 0, mem = 0;
        for (let n = 1; n <= 329; n++) {
            const arg = Math.max(-500, Math.min(500, k*(n-N_th)));
            const tgt = 1/(1+Math.exp(-arg));
            mem = (1-Math.exp(-1))*(x-tgt) + Math.exp(-1)*mem;
            x = Math.max(0, Math.min(1, x + alpha*(tgt-x) + gamma*mem));
            eras.push({era:n, x, target:tgt, memory:mem});
        }

        function draw() {
            const maxEra = parseInt(slider.value);
            const current = eras[maxEra];
            document.getElementById('ve-era').textContent = maxEra;
            document.getElementById('ve-age').textContent = (maxEra*41.9/1000).toFixed(1)+' Gyr';
            document.getElementById('ve-vac').textContent = (current.x*100).toFixed(0)+'%';
            const phase = maxEra < 100 ? 'Radiation' : maxEra < 215 ? 'Matter' : 'Acceleration';
            document.getElementById('ve-phase').textContent = phase;
            document.getElementById('ve-phase').style.color = phase==='Radiation'?'#4fc3f7':phase==='Matter'?'#66bb6a':'#ffd54f';

            const W = canvas.width, H = canvas.height;
            ctx.fillStyle = '#0a0e17'; ctx.fillRect(0, 0, W, H);
            const pad = {l:50, r:20, t:20, b:35};
            const pw = W-pad.l-pad.r, ph = H-pad.t-pad.b;

            function xPos(era) { return pad.l + era/329*pw; }
            function yPos(v) { return pad.t + (1-v)*ph; }

            // Phase backgrounds
            ctx.fillStyle = 'rgba(79,195,247,0.05)'; ctx.fillRect(xPos(0), pad.t, xPos(100)-xPos(0), ph);
            ctx.fillStyle = 'rgba(102,187,106,0.05)'; ctx.fillRect(xPos(100), pad.t, xPos(215)-xPos(100), ph);
            ctx.fillStyle = 'rgba(255,213,79,0.05)'; ctx.fillRect(xPos(215), pad.t, xPos(329)-xPos(215), ph);

            ctx.fillStyle='#4fc3f7';ctx.font='10px monospace';ctx.fillText('Radiation',xPos(30),pad.t+15);
            ctx.fillStyle='#66bb6a';ctx.fillText('Matter',xPos(150),pad.t+15);
            ctx.fillStyle='#ffd54f';ctx.fillText('Acceleration',xPos(260),pad.t+15);

            // Threshold line
            ctx.strokeStyle = '#ffd54f'; ctx.lineWidth = 1; ctx.setLineDash([3,3]);
            ctx.beginPath(); ctx.moveTo(xPos(215), pad.t); ctx.lineTo(xPos(215), H-pad.b); ctx.stroke();
            ctx.setLineDash([]);

            // Target curve (sigmoid)
            ctx.strokeStyle = 'rgba(255,213,79,0.3)'; ctx.lineWidth = 1;
            ctx.beginPath();
            for (let n = 0; n <= 329; n++) {
                const x = xPos(n), y = yPos(eras[n].target);
                n === 0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y);
            }
            ctx.stroke();

            // Vacuum fraction curve (up to current era)
            ctx.strokeStyle = '#4fc3f7'; ctx.lineWidth = 2.5;
            ctx.beginPath();
            for (let n = 0; n <= maxEra; n++) {
                const x = xPos(n), y = yPos(eras[n].x);
                n === 0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y);
            }
            ctx.stroke();

            // Current position dot
            ctx.fillStyle = '#ce93d8';
            ctx.beginPath(); ctx.arc(xPos(maxEra), yPos(current.x), 6, 0, Math.PI*2); ctx.fill();

            // Axes
            ctx.fillStyle = '#6b7a90'; ctx.font = '10px monospace'; ctx.textAlign = 'center';
            ctx.fillText('Era (× 41.9 Myr)', W/2, H-5);
            for (let n = 0; n <= 329; n += 50) {
                ctx.fillText(n, xPos(n), H-pad.b+15);
            }
        }

        slider.oninput = draw;
        draw();
    }
},

// ═══════════════════════════════════════════════════════
// VIZ 4: THE BRIDGE
// ═══════════════════════════════════════════════════════

bridge: {
    title: 'The Bridge: Lab → Universe',
    render(el) {
        el.innerHTML = `
        <div class="viz-panel" style="text-align:center">
            <div class="viz-metrics">
                <div class="viz-metric"><span class="viz-metric-label">Λ_grav</span><span class="viz-metric-value" id="vb-lambda">689 Hz</span></div>
                <div class="viz-metric"><span class="viz-metric-label">τ₀</span><span class="viz-metric-value" id="vb-tau">41.9 Myr</span></div>
                <div class="viz-metric"><span class="viz-metric-label">H∞</span><span class="viz-metric-value" id="vb-hinf">1.885e-18 Hz</span></div>
                <div class="viz-metric"><span class="viz-metric-label">Ω_Λ</span><span class="viz-metric-value" id="vb-omega" style="font-size:22px">0.690</span></div>
            </div>
            <div class="bridge-chain" style="justify-content:center;margin:20px 0;font-size:16px">
                <span class="bridge-step" style="font-size:14px">🔬 Lab Measurement</span>
                <span class="bridge-arrow" style="font-size:24px">→</span>
                <span class="bridge-step" style="font-size:14px">τ₀ = ℏl/(Gm²)</span>
                <span class="bridge-arrow" style="font-size:24px">→</span>
                <span class="bridge-step" style="font-size:14px">H∞ = (2-R)/(Sτ₀)</span>
                <span class="bridge-arrow" style="font-size:24px">→</span>
                <span class="bridge-step" style="font-size:14px;background:rgba(102,187,106,0.15);border-color:rgba(102,187,106,0.3)">🌌 Ω_Λ</span>
            </div>
            <div style="margin:16px 0;color:var(--dim);font-size:12px">
                Planck 2018: Ω_Λ = 0.6889 ± 0.0056 | GRUT deviation: <span id="vb-dev" style="color:var(--green)">+0.2%</span>
            </div>
            <div class="viz-controls">
                <div class="viz-slider-group" style="flex:1">
                    <label>H₀ [km/s/Mpc]</label>
                    <input type="range" id="vb-h0" min="60" max="80" step="0.1" value="70" style="width:100%">
                    <span id="vb-h0-val">70.0</span>
                </div>
            </div>
        </div>`;

        const h0Slider = document.getElementById('vb-h0');
        const R = 1.15428, S = 108*Math.PI, tau0 = 41.9e6*3.156e7;

        function update() {
            const H0_kms = parseFloat(h0Slider.value);
            const H0 = H0_kms * 1e3 / 3.0857e22;
            const H_inf = (2-R)/(S*tau0);
            const OL = (H_inf/H0)**2;
            const dev = (OL/0.6889 - 1)*100;

            document.getElementById('vb-lambda').textContent = '689 Hz';
            document.getElementById('vb-tau').textContent = '41.9 Myr';
            document.getElementById('vb-hinf').textContent = H_inf.toExponential(3)+' Hz';
            document.getElementById('vb-omega').textContent = OL.toFixed(3);
            document.getElementById('vb-omega').style.color = Math.abs(dev) < 5 ? '#66bb6a' : '#ffd54f';
            document.getElementById('vb-dev').textContent = (dev>=0?'+':'')+dev.toFixed(1)+'%';
            document.getElementById('vb-dev').style.color = Math.abs(dev) < 5 ? '#66bb6a' : '#ffd54f';
            document.getElementById('vb-h0-val').textContent = H0_kms.toFixed(1);
        }

        h0Slider.oninput = update;
        update();
    }
}

};
