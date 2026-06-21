---
name: glassmorphism-style
description: Generate frontend UI code in the "Premium Glassmorphism" design style — warm cream backgrounds, translucent glass panels with blur, heavy Inter typography, azure-blue accents, generous rounded corners, and smooth Framer Motion animations. Use this skill whenever the user asks to build any frontend page, component, dashboard, landing page, UI layout, or web interface, even if they don't explicitly mention a style or design preference. Also use when the user says "build a UI", "create a frontend", "make a page", "design a dashboard", "add a panel", or similar frontend-building requests. This is a personal style preference skill — it overrides default styling choices to match a specific aesthetic.
---

# Premium Glassmorphism Style Skill

This skill captures a specific frontend design aesthetic: warm, sophisticated, and modern — with glass-effect panels, bold typography, and smooth micro-interactions. Every page, component, and layout built under this skill must adhere to the design system below.

## Why this style matters

The user personally prefers this aesthetic over generic UI frameworks. It creates a distinctive, polished feel: warm cream backgrounds feel inviting rather than cold-white; glass panels add depth without heaviness; heavy Inter weights give authority to headings; and the azure-blue accent cuts cleanly through the warm palette. The mesh gradient + noise overlay background prevents the page from feeling flat while staying subtle enough not to distract.

When you build frontend with this skill, you're not just "making it look nice" — you're reproducing a carefully calibrated design system. Follow it precisely.

## Tech stack

- **React 19** + TypeScript
- **CSS Custom Properties** (no Tailwind, no CSS-in-JS) — all design tokens go into `:root`
- **Framer Motion** for animations
- **Lucide React** for icons
- **Inter** (sans-serif) + **JetBrains Mono** (monospace) fonts via Google Fonts or CDN

If the user's project already uses a different stack (Vue, Tailwind, etc.), adapt the design system values to that stack — the colors, radii, shadows, and effects stay the same regardless of framework.

## Step 1: Inject the design tokens

Every new project or page must start with these CSS custom properties in `:root`. This is the foundation — nothing else works without it.

```css
:root {
  /* Colors */
  --bg-primary: #fdfbf7;
  --bg-secondary: #f8f9fa;
  --glass-bg: rgba(255, 255, 255, 0.7);
  --glass-border: rgba(255, 255, 255, 0.4);
  --brand-azure: #38bdf8;
  --brand-azure-deep: #0369a1;
  --brand-warm: #f59e0b;
  --brand-danger: #ef4444;
  --brand-success: #10b981;
  --text-main: #1e293b;
  --text-dim: #475569;
  --text-ghost: #94a3b8;
  --accent-glow: rgba(56, 189, 248, 0.15);

  /* Typography */
  --font-sans: 'Inter', -apple-system, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;

  /* Border Radius */
  --radius-xl: 32px;
  --radius-lg: 20px;
  --radius-md: 12px;
  --radius-sm: 8px;

  /* Shadows */
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
  --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
}
```

For font loading, include in the HTML head or CSS:
```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500&display=swap');
```

## Step 2: Apply the background effects

Every page gets two decorative layers beneath the content — they create the warm, textured foundation:

1. **Mesh gradient** — fixed, full-screen, z-index: -2:
```css
.mesh-gradient {
  position: fixed;
  inset: 0;
  z-index: -2;
  background:
    radial-gradient(at 0% 0%, rgba(56, 189, 248, 0.08) 0px, transparent 50%),
    radial-gradient(at 100% 0%, rgba(245, 158, 11, 0.05) 0px, transparent 50%),
    radial-gradient(at 100% 100%, rgba(56, 189, 248, 0.08) 0px, transparent 50%),
    radial-gradient(at 0% 100%, rgba(245, 158, 11, 0.05) 0px, transparent 50%);
}
```

2. **Noise overlay** — fixed, full-screen, z-index: -1, opacity: 0.03:
```html
<div class="noise-overlay">
  <svg width="100%" height="100%">
    <filter id="noise">
      <feTurbulence type="fractalNoise" baseFrequency="0.65" numOctaves="3" stitchTiles="stitch"/>
    </filter>
    <rect width="100%" height="100%" filter="url(#noise)"/>
  </svg>
</div>
```
```css
.noise-overlay {
  position: fixed;
  inset: 0;
  z-index: -1;
  opacity: 0.03;
  pointer-events: none;
}
```

## Step 3: Use the core component patterns

### Glass card (.premium-card)

The universal container for content sections. Glass effect is the signature of this style — use it for all card-like containers.

```css
.premium-card {
  background: var(--glass-bg);
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-lg);
  padding: 2rem;
  box-shadow: var(--shadow-md);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.premium-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-xl);
  border-color: rgba(56, 189, 248, 0.3);
}
```

### Glass header

Sticky navigation bar at top — always present on multi-page apps.

```css
.glass-header {
  height: 72px;
  background: var(--glass-bg);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--glass-border);
  padding: 0 3rem;
  position: sticky;
  top: 0;
  z-index: 50;
  display: flex;
  align-items: center;
}
```

### Glass sidebar / stats panel

For three-panel layouts (dashboard-style pages):

```css
.glass-sidebar {
  width: 320px;
  background: rgba(248, 250, 252, 0.4);
  backdrop-filter: blur(8px);
  border-right: 1px solid var(--glass-border);
  padding: 2.5rem;
}

.glass-stats-panel {
  width: 380px;
  background: rgba(255, 255, 255, 0.4);
  backdrop-filter: blur(12px);
  border-left: 1px solid var(--glass-border);
  padding: 2.5rem;
}
```

### Buttons

```css
.btn-premium {
  background: var(--text-main);
  color: white;
  border: none;
  padding: 1rem 2rem;
  border-radius: var(--radius-md);
  font-weight: 700;
  font-size: 1rem;
  box-shadow: var(--shadow-md);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-premium:hover {
  background: #000;
  transform: translateY(-1px);
  box-shadow: var(--shadow-lg);
}

.btn-premium.btn-outline {
  background: transparent;
  color: var(--text-dim);
  border: 1px solid var(--glass-border);
  box-shadow: none;
}

.btn-premium.btn-outline:hover {
  background: rgba(0, 0, 0, 0.05);
  color: var(--text-main);
}

.btn-premium.btn-ghost {
  background: transparent;
  color: var(--text-dim);
  border: none;
  box-shadow: none;
}
```

### Search / input

```css
.search-container {
  display: flex;
  gap: 0.5rem;
  background: white;
  border: 1px solid #e2e8f0;
  border-radius: 16px;
  padding: 0.6rem;
  box-shadow: var(--shadow-lg);
}

.input-premium {
  border: none;
  outline: none;
  background: transparent;
  color: var(--text-main);
  font-size: 1.1rem;
  padding: 0.5rem;
  flex: 1;
}
```

### Labels

Small uppercase labels for section markers (like "SESSION CONTEXT", "AGENT CLUSTER"):

```css
.label-xs {
  font-size: 0.7rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--text-ghost);
}
```

### Stat items

For dashboard metrics (big number + small label):

```css
.stat-item {
  background: white;
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-md);
  padding: 1.5rem;
}

.stat-value {
  font-size: 1.5rem;
  font-weight: 900;
  color: var(--text-main);
}

.stat-label {
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--text-ghost);
}
```

## Step 4: Typography rules

Apply these consistently — the heavy weight hierarchy is what gives this style its authority:

| Role | Size | Weight | Letter-spacing | Line-height |
|------|------|--------|---------------|-------------|
| Hero title | 5rem | 900 | -0.05em | 1.1 |
| Section heading | 2.5rem | 900 | -0.02em | — |
| Subtitle | 1.5rem | 600 | — | 1.5 |
| Body text | 0.95rem | 400 | — | 1.6 |
| Label-xs | 0.7rem | 800 | 0.1em | — |

Hero titles use gradient text fill:
```css
.hero-title {
  font-size: 5rem;
  font-weight: 900;
  letter-spacing: -0.05em;
  background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
```

## Step 5: Animations (Framer Motion)

Every page should feel alive with subtle entrance animations. Use Framer Motion with these patterns:

### Fade-in + slide-up (the default entrance)
```tsx
<motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.6 }}>
```

### Scroll-triggered entrance
```tsx
<motion.div initial={{ opacity: 0, y: 20 }}
  whileInView={{ opacity: 1, y: 0 }}
  viewport={{ once: true }}
  transition={{ duration: 0.5, delay: i * 0.1 }}>
```

### Tab/content transitions
```tsx
<AnimatePresence mode="wait">
  <motion.div key={activeTab}
    initial={{ opacity: 0, y: 10 }}
    animate={{ opacity: 1, y: 0 }}
    exit={{ opacity: 0, y: -10 }}
    transition={{ duration: 0.3 }}>
```

### Scale entrance for cards
```tsx
<motion.div initial={{ opacity: 0, scale: 0.95 }}
  animate={{ opacity: 1, scale: 1 }}
  transition={{ duration: 0.3 }}>
```

### Progress bar width animation
```tsx
<motion.div initial={{ width: 0 }}
  animate={{ width: `${percent}%` }}
  transition={{ duration: 0.8 }}>
```

### Thinking pulse (for loading/processing states)
```css
@keyframes pulse {
  0% { transform: scale(0.95); opacity: 0.5; box-shadow: 0 0 12px var(--brand-azure); }
  50% { transform: scale(1.2); opacity: 1; box-shadow: 0 0 20px var(--brand-azure); }
  100% { transform: scale(0.95); opacity: 0.5; box-shadow: 0 0 12px var(--brand-azure); }
}

.thinking-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--brand-azure);
  animation: pulse 1.5s infinite;
}
```

## Step 6: Layout patterns

### Three-panel dashboard
For data-heavy pages (sidebar + workspace + stats):
```
[Glass Sidebar 320px] [Workspace flex:1] [Glass Stats 380px]
```
Responsive: hide stats at 1200px, hide sidebar at 992px.

### Feature grid
For landing page feature showcases:
```css
.feature-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2rem;
}
```

### Two-column grid
For cards, findings, stats:
```css
.grid-2col {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
}
```

## Step 7: Special effects

### 3D perspective (floating decorative elements)
```css
.perspective-container {
  perspective: 1000px;
}

.floating-card {
  transform: rotateY(-10deg);
  transition: transform 0.3s;
}
```

### macOS window dots (for code display cards)
```html
<div style={{ display: 'flex', gap: '6px' }}>
  <div style={{ width: 12, height: 12, borderRadius: '50%', background: '#ff5f56' }} />
  <div style={{ width: 12, height: 12, borderRadius: '50%', background: '#ffbd2e' }} />
  <div style={{ width: 12, height: 12, borderRadius: '50%', background: '#27c93f' }} />
</div>
```

### Code display card
```css
.code-card-header { background: #1e293b; }
.code-card-content { background: #0f172a; color: #e2e8f0; font-family: var(--font-mono); font-size: 0.85rem; line-height: 1.7; }
.code-card-footer { background: rgba(56, 189, 248, 0.1); backdrop-filter: blur(4px); }
```

Syntax colors: types `#38bdf8`, keywords `#f59e0b`, strings `#10b981`, classes `#ef4444`, comments `#94a3b8`.

### Severity indicators
For status/error cards with color-coded left bars:
```css
.finding-item { position: relative; padding-left: 16px; }
.finding-item::before {
  content: '';
  position: absolute;
  left: 0; top: 0; bottom: 0;
  width: 6px;
  border-radius: 3px;
}
.finding-item.critical::before { background: #ef4444; box-shadow: 4px 0 15px rgba(239, 68, 68, 0.3); }
.finding-item.high::before { background: #f97316; }
.finding-item.medium::before { background: #f59e0b; }
```

### Custom scrollbar
```css
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(0, 0, 0, 0.05); border-radius: 10px; }
::-webkit-scrollbar-thumb:hover { background: rgba(0, 0, 0, 0.1); }
```

### Progress bar gradient
```css
.progress-bar {
  background: linear-gradient(90deg, var(--brand-azure) 0%, var(--brand-azure-deep) 100%);
  border-radius: var(--radius-sm);
}
```

### Markdown content styling
```css
.markdown-body h1 { font-size: 2.5rem; font-weight: 900; letter-spacing: -0.04em; }
.markdown-body h2 { font-size: 1.5rem; font-weight: 800; border-bottom: 2px solid var(--bg-primary); }
.markdown-body p { color: var(--text-dim); line-height: 1.8; }
.markdown-body blockquote {
  background: var(--bg-primary);
  border-left: 6px solid var(--brand-azure);
  border-radius: 12px;
  font-style: italic;
}
```

## Icons

Always use **Lucide React** icons, rendered inline with adjacent text via `display: flex; align-items: center; gap: Xpx`. Common sizes: 16px for inline, 20-28px for section headers, 48-64px for feature cards.

## Responsive breakpoints

Desktop-first, with panel hiding (not restructuring):
- **1200px**: Hide stats panel
- **992px**: Hide sidebar, reduce header padding, shrink hero title, disable 3D transforms
- **768px**: Hide nav links and tagline, shrink workspace padding, full-width search

## Summary of what makes this style distinctive

1. **Warm cream background** (#fdfbf7) — not plain white, not dark mode
2. **Glass panels everywhere** — blur + translucency + thin white borders
3. **Heavy typography** — Inter at 800-900 for headings, creating visual authority
4. **Azure blue accent** (#38bdf8) — clean, modern, cutting through warm tones
5. **Mesh gradient + noise background** — subtle depth without distraction
6. **Smooth micro-interactions** — hover lifts, staggered fade-ins, pulse indicators
7. **Generous rounded corners** — 12-32px, never sharp
8. **Multi-tier shadow system** — depth hierarchy via sm/md/lg/xl shadows

When in doubt about a design decision, ask: "does this feel warm, polished, and glass-like?" If not, adjust toward the patterns above.