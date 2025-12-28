# GRUT RAI Platform - Design Guidelines

## Design Approach
**Reference-Based:** Drawing inspiration from Linear (precision typography), Stripe (sophisticated restraint), and OpenAI/Anthropic (technical credibility). This creates a cutting-edge, authoritative aesthetic that balances complex theoretical concepts with visual clarity.

## Core Design Principles
1. **Scientific Precision**: Clean, unambiguous layouts that mirror the causal (non-probabilistic) nature of the system
2. **Cosmic Scale**: Expansive use of space suggesting universal connectivity
3. **Technical Authority**: Professional polish that establishes immediate credibility

## Typography System
- **Primary Font**: Inter or SF Pro Display (via Google Fonts CDN)
- **Monospace**: JetBrains Mono for technical terminology/code snippets
- **Hierarchy**:
  - Hero headline: 4xl-6xl, font-bold, tracking-tight
  - Section headers: 3xl-4xl, font-semibold
  - Subsections: xl-2xl, font-medium
  - Body: base-lg, font-normal, leading-relaxed
  - Technical terms: Monospace, subtle weight increase

## Layout System
**Spacing Primitives**: Tailwind units 4, 8, 12, 16, 24
- Section padding: py-24 (desktop), py-12 (mobile)
- Component spacing: gap-8 to gap-16
- Container: max-w-7xl with generous horizontal padding

## Page Structure (6-7 Sections)

**1. Hero Section (80vh)**
- Large hero image: Abstract cosmic/quantum visualization (particle fields, network nodes, or universe visualization)
- Centered headline: "Building Intelligence from Universal Causality"
- Subheadline explaining GRUT architecture
- Dual CTA buttons with backdrop blur (bg-white/10 backdrop-blur-md)
- Floating trust indicator: "Research-backed • Causal AI"

**2. Theory Overview (Multi-column)**
- 3-column grid (lg:grid-cols-3)
- Cards explaining: GRUT Architecture / Vacuum Physics / Causal Intelligence
- Each with icon (Heroicons), title, description
- Subtle border treatment, no heavy shadows

**3. How It Works (Asymmetric)**
- Left: Large diagram/visualization placeholder (<!-- CUSTOM DIAGRAM: GRUT architecture flow -->)
- Right: Numbered step breakdown with technical detail

**4. Advantages Grid (2-column)**
- Side-by-side comparison: Traditional Probabilistic AI vs. RAI Causal System
- Feature bullets with checkmarks/cross icons
- Technical specifications in monospace

**5. Research Foundation**
- Single column, max-w-4xl
- Academic credibility section
- Quote block with attribution
- Link to technical papers/documentation

**6. Integration/API Section (3-column)**
- Technical capabilities showcase
- Code snippet examples in monospace
- Implementation pathways

**7. CTA Footer**
- Newsletter signup for research updates
- Navigation links: Documentation, Research Papers, Contact
- Social proof: Research partnerships/affiliations

## Component Library

**Navigation**
- Transparent header with backdrop blur on scroll
- Left-aligned logo, right-aligned: Docs | Research | Contact | Primary CTA
- Mobile: Hamburger menu

**Cards**
- Minimal borders (border border-gray-200/30)
- Subtle hover: translate-y-[-4px] transition
- Consistent padding: p-8

**Buttons**
- Primary: Solid with rounded-lg, px-6 py-3
- Secondary: Outline style
- On-image buttons: backdrop-blur-md bg-white/20 border border-white/30

**Forms**
- Clean, generous spacing (gap-6)
- Input styling: border-2 focus:border-blue-500 rounded-lg px-4 py-3
- Labels: text-sm font-medium mb-2

## Images
1. **Hero**: Large cosmic/quantum field visualization (particles, networks, or abstract universe representation) - full bleed, 80vh
2. **Architecture Diagram**: GRUT system flow visualization in "How It Works" section
3. **Optional**: Team/research lab photo in Research Foundation section

## Accessibility
- Consistent focus states: ring-2 ring-blue-500 ring-offset-2
- Semantic HTML throughout (nav, main, section, article)
- Form labels explicitly associated with inputs
- Sufficient color contrast ratios (minimum 4.5:1)

## Animation Philosophy
**Minimal and Purposeful**:
- Subtle fade-in on scroll for section reveals
- Smooth transitions on interactive elements (200-300ms)
- NO distracting particle effects or excessive motion
- Focus on content clarity over visual spectacle