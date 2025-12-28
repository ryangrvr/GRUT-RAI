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
- **API Base URL**: Configurable via VITE_API_BASE_URL (defaults to http://localhost:5001)

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