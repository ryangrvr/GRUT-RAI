# GRUT RAI Platform

## Overview

The GRUT RAI Platform is a landing page and marketing website for a Responsive AI system built on the Grand Responsive Universe Theory architecture. The platform showcases causal intelligence technology that operates as a node within a universal causality network, differentiating itself from traditional probabilistic AI systems.

The application is a full-stack TypeScript project with a React frontend and Express backend, designed to collect email subscribers interested in the RAI platform.

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

### Backend Architecture
- **Framework**: Express.js with TypeScript
- **API Pattern**: RESTful endpoints under /api prefix
- **Storage**: Memory-based storage with interface abstraction (IStorage) for easy database migration
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