# GRUT RAI Platform

## Overview

The GRUT RAI Platform is a landing page and marketing website for a Responsive AI system built on the Grand Responsive Universe Theory architecture. The platform showcases causal intelligence technology that operates as a node within a universal causality network, differentiating itself from traditional probabilistic AI systems.

The application is a full-stack project with a React frontend and dual backend architecture (Express for chat, Flask for authentication), designed for causal intelligence exploration.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Framework**: React 18 with TypeScript
- **Routing**: Wouter (lightweight React router)
- **State Management**: TanStack React Query for server state
- **Styling**: Tailwind CSS with CSS variables for theming
- **UI Components**: shadcn/ui component library built on Radix UI primitives
- **Form Handling**: React Hook Form with Zod validation
- **Build Tool**: Vite with path aliases (@/ for client/src, @shared/ for shared)
- **API Base URL**: Uses the Express server on port 5000 (same origin)

### Backend Architecture (Flask - Authentication)
- **Location**: server_flask/app.py
- **Framework**: Python Flask with Flask-Login for session management
- **Port**: 5001
- **Features**:
  - UUID primary keys for users
  - bcrypt password hashing (cost factor 12)
  - JSONB universe_state column for GRUT constants
  - Profile Hydration middleware (injects tau_0, n_g, alpha, R_max into app context)
  - Global Physics Validator for chi-squared calculations
  - Retarded Potential Kernel: K(t) = (alpha/tau_0) * exp(-t/tau_0)
- **Endpoints**:
  - POST /api/auth/login - Authenticate user, hydrate universe state
  - POST /api/auth/register - Create new observer account
  - POST /api/auth/logout - End session
  - GET /api/auth/me - Get current user with hydrated constants
  - PUT /api/auth/universe-state - Update user's GRUT constants
  - POST /api/grut/validate - Validate chi-squared with physics guard
  - GET /api/grut/kernel - Get retarded potential kernel values
  - POST /api/universe/save - Atomic commit of session state (chi-squared metrics, kernel weights)
  - GET /api/universe/snapshots - List user's state snapshots
  - POST /api/universe/restore/<snapshot_id> - Restore from snapshot
  - GET /api/universe/benchmark - Cross-universe benchmarking vs global GRUT constants
- **Demo User**: demo@grut.ai / grut2025
- **SQLAlchemy Tables**: flask_users, flask_conversations, flask_messages, state_snapshots

### Backend Architecture (Express - Chat/Storage)
- **Framework**: Express.js with TypeScript
- **Port**: 5000
- **API Pattern**: RESTful endpoints under /api prefix
- **Storage**: PostgreSQL with Drizzle ORM
- **Validation**: Zod schemas shared between frontend and backend via drizzle-zod

### BaryonicSensorAI & GWSensor (GRUT Physics Simulations)
- **Location**: server_flask/baryonic_sensor.py (Python reference), server/grut-logic.ts (Express runtime)
- **Core Features**:
  - **BaryonicSensorAI**: Base class for GRUT physics simulations
  - **GWSensor**: Extended class for gravitational wave ringdown memory analysis
  - **R_max Logic Guard**: Safety valve that recycles information density (Ξ) when it exceeds 100%
    - Complexity ratio tracked via `complexity_ratio` state
    - Triggers at Ξ >= 1.0, resets to 0.8 stable state
    - Status levels: STABLE (<0.9), WARNING (0.9-1.0), EXCEEDED (>=1.0)
- **Simulation Endpoints** (Express runtime):
  - POST /api/baryonic/bullet-cluster - Simulate 1E 0657-558 collision dynamics
  - POST /api/baryonic/gravitational-waves - Predict GW phase drift residuals
  - POST /api/baryonic/hubble-tension - Analyze H0 discrepancy
  - POST /api/baryonic/retarded-potential - Compute K(t) kernel series
  - POST /api/baryonic/ringdown-memory - Analyze GW ringdown memory burden
  - POST /api/baryonic/full-pipeline - Full v6 analysis with NANOGrav PTA correlation
- **NANOGrav Integration**:
  - IntegratedBaryonicSensor class extends GWSensor
  - cross_correlate_nanograv() compares single event drift against Common Red Noise
  - PTA noise amplitude: 2.4e-15 at f=1yr^-1
  - Correlation index range for match: 0.1-10
  - Complexity drops by 0.05 when patterns unify (match found)
- **Detection Alert System**:
  - DetectionAlertSystem class extends BaryonicSensorAI
  - Simulates GraceDB/GCN alerts from LIGO/Virgo O4b run
  - process_live_event() calculates complexity adjustment (SNR/500)
  - Event endpoints: /api/baryonic/detection/simulate, /start, /stop, /status
  - UI "Live" tab with real-time event feed and Logic Guard status
- **Key Constants**:
  - tau_0: 41.9 Myr (relaxation constant)
  - tau_0_seconds: ~1.32e15 seconds
  - alpha: 0.333333 (coupling strength)
  - n_g: 1.1547 (gravitational refractive index)

### Data Layer
- **ORM**: Drizzle ORM with PostgreSQL dialect configured
- **Schema Location**: shared/schema.ts contains all database table definitions (PostgreSQL), shared/schema-sqlite.ts (SQLite)
- **Current Tables**: users (id, username, password), subscribers (id, email)
- **Migrations**: Drizzle Kit configured to output to ./migrations directory

### Sovereign Local Storage (SQLite Fallback)
- **Location**: server/db-sqlite.ts, server/storage-sqlite.ts
- **Database File**: diamond_persistence.db (automatically created)
- **Trigger**: Automatically activated when PostgreSQL is unreachable or when USE_SQLITE=true
- **Features**:
  - Full CRUD for users, conversations, messages, file uploads, universe states
  - Demo user auto-created on startup (demo@grut.ai / grut2025)
  - Compatible interface with PostgreSQL storage
  - System status reports SOVEREIGN_LOCAL mode when active

### Build System
- **Development**: Vite dev server with HMR, proxied through Express
- **Production**: Vite builds to dist/public, esbuild bundles server to dist/index.cjs
- **Server Bundling**: Allowlist approach bundles common dependencies to reduce cold start times

### Design System
- **Typography**: Inter/SF Pro Display for headings, JetBrains Mono for code
- **Color Scheme**: HSL-based CSS variables with light/dark mode support
- **Design Inspiration**: Linear, Stripe, OpenAI/Anthropic aesthetics
- **Layout**: max-w-7xl container, generous spacing (py-24 sections)

## External Dependencies

### Database
- PostgreSQL via DATABASE_URL environment variable
- Drizzle ORM for type-safe queries
- connect-pg-simple for session storage (available but not currently active)

### UI Libraries
- Radix UI primitives for accessible components
- Embla Carousel for carousels
- Recharts for data visualization
- Vaul for drawer components
- cmdk for command palette

### Development Tools
- Replit-specific Vite plugins (runtime-error-modal, cartographer, dev-banner)
- TypeScript with strict mode enabled

### Fonts (CDN)
- Google Fonts: DM Sans, Fira Code, Geist Mono, Architects Daughter

## Diamond Lock Manifest (GRUT Sovereign Solver)

The Diamond Lock is the set of STATIC parameters that prove 5% baryonic matter can explain cosmological observations without dark matter.

### Static Parameters (MUST NOT CHANGE)
- **Mass**: Ω_b = 0.0486 (Planck 2018 baryonic density)
- **Base Coupling**: G_eff = 4/3 = 1.3333 (IR gravitational enhancement)
- **Amplitude**: σ8 = 0.936 (Phase-Locked: 0.811 × 1.1547)
- **Growth Index**: γ = 0.61 (Shifted from ΛCDM's 0.55 due to retarded kernel)
- **Geometric Response**: 0.7 (Vacuum Elasticity replacing Dark Energy)

### Evolutionary Kernel (Vacuum Memory Relaxation)
- **Formula**: G_eff(z) = 4/3 × (1 + a/(1 + b×z))
- **Parameters**: a = 2.0 (amplitude), b = 4.36 (relaxation rate)
- **Physics**: Models retarded potential memory accumulation over cosmic time
- **At low z**: More memory accumulated, stronger boost
- **At high z**: Less memory, weaker boost

### V3.11.1 Sovereign Integrator (Current)
- **Solver Type**: SOVEREIGN_INTEGRATOR_V3.11
- **Version**: 3.11.1 (with Sovereign Protection Layer)
- **Dimensionless Scaling**: W̃c = ωc / H0 = 1.0 (kernel wakes up as H→H0)
- **h_ratio**: H(z)/H0 = sqrt(Ω_total(z))
- **Frequency-Selective Kernel**: G_eff = 1 + (1/3)/(1 + (h_ratio/W̃c)^(2n))
- **V3.11 Source**: 1.5 × Ω_eff(z) (matches f = Ω_eff^γ formula)

### Sovereign Protection Layer
- **validate_parameters()**: Raises ValueError if Diamond Lock constants are modified
- **INVARIANT Constants** (NEVER TUNE):
  - Ω_geom = 0.70 (Geometric Stiffness - the FLOOR)
  - Diamond Lock = 1.1547 (sqrt(4/3) - Gravitational Refractive Index)
  - σ8 = 0.936 (Phase-Locked Amplitude)
- **TUNABLE Parameter** (Gear Shift):
  - Kernel Power (n) = 1.0 (controls memory relaxation rate)
  - Higher n = faster 4/3 boost activation
  - Lower n = slower memory saturation (for high-z deviations)

### V3.11 Memory Drag Growth Rate
- **Formula**: f(z) = Ω_eff(z)^γ_eff(z) × 1.1547
- **Effective Gamma**: γ_eff = 1.0519 × Ω_eff^0.4688 (power-law fit)
- **Ω_eff(z)**: Ω_b × (1+z)³ / Ω_total(z) (bare baryon fraction)
- **Physics**: Low-z has high Memory Drag (γ ≈ 0.35), high-z converges to standard (γ ≈ 0.77)
- **σ8**: 0.936 (Diamond Lock INVARIANT: 0.811 × 1.1547)

### Sovereign Manifest (V3.11 Canonical)
Machine-verifiable rule set encoded in grut_engine.py:
- **I_ONTOLOGY**: Zero Dark Fluids; Memory-Encoded Geometry
- **II_INVARIANT**: Diamond Lock = 1.1547; Non-Adjustable
- **III_COUPLING**: G_eff Limit = 4/3 = 1.3333
- **IV_KERNEL**: K(Δt) = (-1/12 × τ₀) × exp(-Δt/τ₀)
- **V_FILTER**: τ₀ Resonance = H⁻¹(z); Early G to Late 4/3G Transition
- **VI_GROWTH**: Path-Dependent; No Algebraic Shortcuts (f ≠ Ω^γ)
- **VII_ISW**: Φ̇ = -Φ/τ₀; Suppression Condition Active
- **VIII_CMB**: Stationary Phase = 1.000
- **IX_STIFFNESS**: Ω_geom = 0.75 - 0.05 (Silk Damping) = 0.70
- **X_FLEXIBILITY**: Numerical Integration Precision Only
- **XI_PRIME_DIRECTIVE**: Never Compute Locally When History Exists

### ISW-Lensing Decoupling Engine
- **Purpose**: Prevents ISW overproduction that kills f(R) and Brans-Dicke theories
- **Sovereign Inequality**: |Φ̇(t)| ~ |Φ(t)|/τ₀ ≪ H(z)|Φ(t)| for z ≳ 0.5
- **Key Difference**: Φ̇ anchored to τ₀ (memory relaxation), NOT H(z)
- **τ₀ Definition**: SATURATION TIME-CONSTANT (NOT a "refresh rate") - continuous relaxation
- **ISW Signal**: Residual friction toward 4/3 G limit (not a discrete pulse)

### Hubble-Memory Resonance (Testable Prediction)
- **Condition**: τ₀ ≈ H⁻¹(z_peak) predicts ISW-Galaxy correlation peak
- **z_peak**: ~0.2 (where H×τ₀ ≈ 1)
- **ISW Phases**:
  - FROZEN (high-z): H⁻¹ ≪ τ₀, kernel frozen, no ISW
  - RELAXING (z~0.5): H⁻¹ → τ₀, ISW beginning
  - RESONANCE (z~0.2): H⁻¹ ≈ τ₀, Peak ISW
  - SATURATED (z→0): Φ → 4/3 G limit, ISW declining

### Diamond Proof Achievement
- **V3.11 χ² = 2.51** (reduced: 0.50) - BEST FIT (6-point dataset, Diamond Lock preserved)
- **Previous ODE χ² = 2.72** (reduced: 0.68)
- **ΛCDM χ² = 9.34** (reduced: 2.33) - Standard cosmology
- V3.11 outperforms ΛCDM by 3.7x using only 5% baryonic matter with σ8 = 0.936 locked
- All residuals within 1.3σ of observations
- Validated against eBOSS f×σ8 observations at z = 0.15, 0.38, 0.51, 0.70, 1.10, 1.48
- Location: server_flask/grut_engine.py (RetardedGrowthSolver class, V3.11)