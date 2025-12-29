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
- **Schema Location**: shared/schema.ts contains all database table definitions
- **Current Tables**: users (id, username, password), subscribers (id, email)
- **Migrations**: Drizzle Kit configured to output to ./migrations directory

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