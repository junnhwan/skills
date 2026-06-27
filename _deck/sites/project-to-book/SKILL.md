---
name: project-to-book
description: Transform a vibe-coded project into an interview preparation book (VitePress website). Use when user wants to create a technical documentation site for understanding a project, preparing for interviews, or building a knowledge base from source code. Triggers: "做成一本书", "interview prep", "源码走读", "面试准备", "technical book", "documentation site", "VitePress site for project".
---

# Project to Book

IRON LAW: Every answer must cite specific source code with file path and line numbers. Never write generic descriptions — always ground content in actual implementation.

## Workflow

```
Project to Book Progress:

- [ ] Step 1: Understand Project ⚠️ REQUIRED
  - [ ] 1.1 Identify project type, language, framework
  - [ ] 1.2 Find entry points (main.go, cmd/, etc.)
  - [ ] 1.3 List core modules and their responsibilities
- [ ] Step 2: Deep Source Analysis ⚠️ REQUIRED
  - [ ] 2.1 Launch parallel subagent tasks for each core module
  - [ ] 2.2 Extract: function signatures, data structures, call chains
  - [ ] 2.3 Identify design decisions and trade-offs
- [ ] Step 3: Design Book Structure
  - [ ] 3.1 Create directory skeleton (interview/, source/, practice/)
  - [ ] 3.2 Define interview question categories
  - [ ] 3.3 Map source modules to walkthrough files
- [ ] Step 4: Initialize VitePress
  - [ ] 4.1 Create package.json with vitepress dependency
  - [ ] 4.2 Create .vitepress/config.mts with nav/sidebar
  - [ ] 4.3 Create .vitepress/theme/index.ts
  - [ ] 4.4 Create docs/index.md homepage
- [ ] Step 5: Write Content ⚠️ REQUIRED
  - [ ] 5.1 Interview questions: 6-10 per category with code citations
  - [ ] 5.2 Source walkthrough: one file per core module
  - [ ] 5.3 Practice exercises (optional)
- [ ] Step 6: Build & Verify
  - [ ] 6.1 Run npm install
  - [ ] 6.2 Run npx vitepress build
  - [ ] 6.3 Fix any broken links or build errors
- [ ] Step 7: Customize
  - [ ] 7.1 Update GitHub URLs
  - [ ] 7.2 Add logo/branding (optional)
  - [ ] 7.3 Configure deployment (optional)
```

## Step 1: Understand Project

Before writing any code, understand the project structure:

1. Read README.md, AGENTS.md, CLAUDE.md if they exist
2. Find the entry point (main.go, cmd/, src/index.ts, etc.)
3. List all packages/modules and their responsibilities
4. Identify the core architecture patterns

Ask user if unclear:
- "What is this project? A CLI tool? A web server? A library?"
- "What are the most important modules I should focus on?"
- "What level of detail do you want for interview prep?"

## Step 2: Deep Source Analysis

This is the most critical step. Launch parallel subagent tasks to analyze source code.

### Analysis Template per Module

For each core module, extract:

1. **Data Structures** — struct/class definitions with all fields
2. **Function Signatures** — public API with parameters and return types
3. **Call Chains** — how functions call each other
4. **Design Decisions** — why it's built this way
5. **Edge Cases** — error handling, boundary conditions

### Example Subagent Prompt

```
深入读取 [project]/internal/[module]/ 目录下的所有源码文件。

返回以下内容：
1. 所有 struct/type 定义（带行号）
2. 所有公开函数签名（带行号）
3. 关键函数的完整实现逻辑（带代码片段）
4. 调用链关系图
5. 设计决策和权衡

要求：
- 必须包含具体代码片段，不能只是概括
- 必须包含行号引用
- 必须解释"为什么"而不仅是"是什么"
```

## Step 3: Design Book Structure

### Standard Directory Layout

```
book/
├── package.json
├── .vitepress/
│   ├── config.mts
│   └── theme/
│       └── index.ts
└── docs/
    ├── index.md                    # Homepage
    ├── interview/                  # Interview questions
    │   ├── index.md
    │   ├── fundamentals/           # Basic concepts
    │   │   └── index.md
    │   ├── [category-1]/
    │   │   └── index.md
    │   └── [category-2]/
    │       └── index.md
    ├── source/                     # Source code walkthrough
    │   ├── index.md
    │   ├── [module-1]/
    │   │   └── index.md
    │   └── [module-2]/
    │       └── index.md
    └── practice/                   # Optional exercises
        └── index.md
```

### Interview Categories (adapt to project)

- **fundamentals** — Core concepts, architecture
- **tool-system** — If project has tools/plugins
- **data-flow** — How data moves through the system
- **error-handling** — Error patterns, recovery
- **concurrency** — Threading, async patterns
- **testing** — Test strategies, mocking

## Step 4: Initialize VitePress

### package.json

```json
{
  "name": "[project-name]-book",
  "private": true,
  "scripts": {
    "dev": "vitepress dev",
    "build": "vitepress build",
    "preview": "vitepress preview"
  },
  "devDependencies": {
    "vitepress": "^1.6.3",
    "vitepress-plugin-mermaid": "^2.0.17",
    "mermaid": "^11.13.0"
  }
}
```

### .vitepress/config.mts

**CRITICAL**: If using Mermaid, you MUST wrap with `withMermaid()`:

```typescript
import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'

export default withMermaid(
  defineConfig({
    title: '[Project Name]',
    description: '[Project Description]',
    srcDir: './docs',
    ignoreDeadLinks: true,
    themeConfig: {
      nav: [
        { text: 'Home', link: '/' },
        { text: 'Interview', link: '/interview/' },
        { text: 'Source', link: '/source/' }
      ],
      sidebar: {
        '/interview/': [
          {
            text: 'Interview Questions',
            items: [
              { text: 'Fundamentals', link: '/interview/fundamentals/' },
              // ... more categories
            ]
          }
        ],
        '/source/': [
          {
            text: 'Source Walkthrough',
          items: [
            // ... modules
          ]
        }
      ]
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/[username]/[repo]' }
    ]
  }
})
)
```

### Directory Structure

```
book/
├── package.json
├── .vitepress/
│   ├── config.mts
│   └── theme/
│       ├── index.ts
│       ├── custom.css
│       └── components/    # Vue components for interactivity
└── docs/
    ├── index.md
    ├── public/
    │   └── diagrams/      # SVG architecture diagrams
    ├── interview/
    ├── source/
    └── practice/
```

### .vitepress/theme/index.ts

```typescript
import DefaultTheme from 'vitepress/theme'
import './custom.css'

export default DefaultTheme
```

## Step 5: Write Content

### Interview Question Format

Each question must follow this structure:

```markdown
## Q[N]: [Question Title]

### [Sub-topic if needed]

```[language]
// file/path.go:line-number
func FunctionName(params) ReturnType {
    // actual code from source
}
```

**Design Decision**: [Why it's built this way]

**Key Points**:
- [Point 1 with specific detail]
- [Point 2 with specific detail]

### Source Walkthrough Format

Each module walkthrough must include:

```markdown
# [Module Name] Source Walkthrough

## Architecture Overview

[Brief description with key files table]

| File | Lines | Responsibility |
|------|-------|----------------|
| file1.go | 100 | Purpose 1 |
| file2.go | 200 | Purpose 2 |

## Core Data Structures

```go
// file.go:10-20
type StructName struct {
    Field1 Type  // description
    Field2 Type  // description
}
```

## [Function/Feature Name]

```go
// file.go:50-100
func (s *StructName) MethodName(params) ReturnType {
    // implementation with comments
}
```

### Call Chain

```
FunctionA()
  └─ FunctionB()
       └─ FunctionC()
```

## Design Decisions

| Decision | Reason |
|----------|--------|
| Choice 1 | Why |
| Choice 2 | Why |
```

## Step 6: Build & Verify

```bash
cd book
npm install
npx vitepress build
```

Fix common issues:
- Dead links → update `ignoreDeadLinks: true` or fix paths
- Missing files → ensure all referenced .md files exist
- Build errors → check TypeScript syntax in config

## Step 7: Deploy to GitHub Pages

### 7.1 Configure VitePress base path

In `.vitepress/config.mts`, set `base` to your repo name:

```typescript
base: '/[repo-name]/',  // e.g., '/bond-code/'
```

### 7.2 Create GitHub Actions workflow

Create `.github/workflows/deploy-book.yml`:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: npm
          cache-dependency-path: book/package-lock.json
      - run: npm ci
        working-directory: book
      - run: npm run build
        working-directory: book
      - uses: actions/upload-pages-artifact@v3
        with:
          path: book/.vitepress/dist

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    needs: build
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

### 7.3 Add .gitignore

Create `book/.gitignore`:

```
node_modules/
.vitepress/cache/
.vitepress/dist/
```

### 7.4 Enable GitHub Pages

1. Push code to GitHub
2. Go to repo **Settings → Pages**
3. **Source** select **GitHub Actions**
4. Scroll down and click **Save** (if available)
5. Wait 2-3 minutes for first deployment
6. Site will be live at `https://[username].github.io/[repo]/`

### 7.5 Verify

Check deployment status at `https://github.com/[username]/[repo]/actions`

## Step 8: Customize Frontend Style (Optional)

VitePress default theme is functional but generic. Apply these principles to make it distinctive.

### Design Read

Before customizing, declare the style direction:

> "Reading this as: technical documentation for developers, with a clean-editorial language, leaning toward dark-mode-first with monospace accents."

### Typography

**Banned as default**: `Inter` (too generic, every AI site uses it)

**Preferred alternatives**:
- `Geist` — Vercel's font, clean and modern
- `JetBrains Mono` — for code-heavy content
- `IBM Plex` — technical but warm
- `Space Grotesk` — geometric, distinctive

**Implementation** (in `custom.css`):

```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
  --vp-font-family-base: 'Space Grotesk', sans-serif;
  --vp-font-family-mono: 'JetBrains Mono', monospace;
}
```

### Color Palette

**Banned as default**: AI-purple gradients, generic blue links

**Pick ONE accent and lock it**:

| Style | Accent | Base |
|-------|--------|------|
| Dark Tech | `#10b981` (emerald) | `#0a0a0a` → `#1a1a1a` |
| Editorial | `#f59e0b` (amber) | `#fafaf9` → `#1c1917` |
| Minimal | `#06b6d4` (cyan) | `#ffffff` → `#09090b` |
| Warm | `#ef4444` (red) | `#fef2f2` → `#1a1a1a` |

**Implementation**:

```css
:root {
  --vp-c-brand-1: #10b981;
  --vp-c-brand-2: #059669;
  --vp-c-brand-3: #047857;
  --vp-c-brand-soft: rgba(16, 185, 129, 0.14);
}
```

### Code Blocks

Make code blocks distinctive, not just syntax-highlighted:

```css
.vp-doc div[class*='language-'] {
  border-radius: 8px;
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-code-block-bg);
}

/* Add filename indicator */
.vp-doc div[class*='language-']::before {
  content: attr(data-ext);
  position: absolute;
  top: 8px;
  right: 12px;
  font-size: 12px;
  color: var(--vp-c-text-3);
  font-family: var(--vp-font-family-mono);
}
```

### Sidebar Styling

Make sidebar more structured:

```css
.VPSidebar {
  border-right: 1px solid var(--vp-c-divider);
}

.VPSidebarItem .text {
  font-size: 14px;
  line-height: 1.6;
}

/* Active item indicator */
.VPSidebarItem.is-active > .item > .indicator {
  width: 3px;
  background: var(--vp-c-brand-1);
}
```

### Hero Section

If using a custom hero, make it memorable:

```css
.VPHero .name {
  font-weight: 700;
  letter-spacing: -0.02em;
}

.VPHero .text {
  font-size: 1.1rem;
  color: var(--vp-c-text-2);
  max-width: 500px;
}
```

### Anti-Patterns for Frontend

- **DO NOT** use purple gradients (AI tell)
- **DO NOT** use Inter font (too generic)
- **DO NOT** add excessive animations (distracting for docs)
- **DO NOT** use pure black `#000000` (use off-black like `#0a0a0a`)
- **DO NOT** mix multiple accent colors (pick one, lock it)

## Step 9: Visual Enhancement — SVG & Interactive Diagrams

A book with only text and code is boring. The key to making it **visually engaging** is hand-crafted SVG diagrams and interactive components. Reference: [learn-claude-code](https://github.com/shareAI-lab/learn-claude-code).

### 9.1 SVG Architecture Diagrams (CRITICAL)

Each module needs **1-2 hand-crafted SVGs** showing architecture, flow, or data structures. Do NOT rely on Mermaid — it renders poorly and looks generic.

**SVG Template Structure:**

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5"
            markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#64748b"/>
    </marker>
    <linearGradient id="header" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#334155"/>
    </linearGradient>
  </defs>

  <rect width="800" height="500" fill="#f8fafc" rx="8"/>

  <rect x="0" y="0" width="800" height="50" fill="url(#header)" rx="8"/>
  <text x="20" y="32" fill="white" font-size="16" font-weight="bold" font-family="system-ui">
    Module Name — Core Flow
  </text>

  <g transform="translate(50, 100)">
    <rect width="160" height="60" rx="8" fill="#dbeafe" stroke="#3b82f6" stroke-width="2"/>
    <text x="80" y="25" text-anchor="middle" font-size="13" font-weight="600" fill="#1e40af">
      User Input
    </text>
    <text x="80" y="45" text-anchor="middle" font-size="11" fill="#64748b">messages[]</text>
  </g>

  <line x1="210" y1="130" x2="300" y2="130" stroke="#64748b" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="255" y="120" text-anchor="middle" font-size="10" fill="#94a3b8">submit</text>

  <g transform="translate(350, 80)">
    <polygon points="80,0 160,50 80,100 0,50" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/>
    <text x="80" y="45" text-anchor="middle" font-size="12" font-weight="600" fill="#92400e">tool_use?</text>
  </g>

  <g transform="translate(50, 420)">
    <rect width="12" height="12" rx="2" fill="#dbeafe" stroke="#3b82f6"/>
    <text x="20" y="11" font-size="11" fill="#64748b">Process</text>
    <rect x="100" width="12" height="12" rx="2" fill="#fef3c7" stroke="#f59e0b"/>
    <text x="120" y="11" font-size="11" fill="#64748b">Decision</text>
    <rect x="200" width="12" height="12" rx="2" fill="#dcfce7" stroke="#22c55e"/>
    <text x="220" y="11" font-size="11" fill="#64748b">Data Store</text>
  </g>
</svg>
```

### 9.2 Color System for Diagrams

Use a **5-color layer system** throughout all diagrams:

| Layer | Color | Hex | Use For |
|-------|-------|-----|---------|
| Core | Blue | `#3b82f6` | Main loop, entry points |
| Tools | Green | `#22c55e` | Tool calls, dispatchers |
| Memory | Purple | `#8b5cf6` | Memory, context, storage |
| Safety | Amber | `#f59e0b` | Decisions, guards, checks |
| Agent | Red | `#ef4444` | Subagents, orchestration |

### 9.3 ASCII Diagrams

For simple flows, use ASCII art in code blocks:

````markdown
```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  User Input │────▶│   Agent     │────▶│   Tool      │
│  messages[] │     │   Loop      │     │   Execute   │
└─────────────┘     └──────┬──────┘     └─────────────┘
                           │
                    ┌──────▼──────┐
                    │  tool_use?  │
                    └─────────────┘
```
````

**CSS for ASCII blocks:**

```css
.vp-doc div[class*="language-"]::before {
  content: attr(data-ext);
  position: absolute;
  top: 8px;
  right: 12px;
  font-size: 11px;
  color: #94a3b8;
  font-family: var(--vp-font-family-mono);
  text-transform: uppercase;
}

.vp-doc div[class*="language-go"]::before { content: "Go"; color: #3b82f6; }
.vp-doc div[class*="language-python"]::before { content: "Python"; color: #22c55e; }
```

### 9.4 Hero Callout (First Blockquote)

```css
.vp-doc blockquote:first-of-type {
  background: linear-gradient(135deg, #eff6ff 0%, #f0fdf4 100%);
  border-left: 4px solid;
  border-image: linear-gradient(to bottom, #3b82f6, #22c55e) 1;
  padding: 16px 20px;
  border-radius: 0 8px 8px 0;
  font-style: italic;
}

.dark .vp-doc blockquote:first-of-type {
  background: linear-gradient(135deg, #172554 0%, #052e16 100%);
}
```

### 9.5 Interactive Vue Components

Create step-by-step flow visualizations in `.vitepress/theme/components/`:

**Example: `AgentLoopFlow.vue`** — clickable steps with code snippets.

Register in `index.ts`:
```typescript
import AgentLoopFlow from './components/AgentLoopFlow.vue'
export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('AgentLoopFlow', AgentLoopFlow)
  }
}
```

Use in Markdown: `<AgentLoopFlow />`

### 9.6 Diagram Checklist per Module

| Diagram | Type | Purpose |
|---------|------|---------|
| Architecture overview | SVG | Components and relationships |
| Core flow | SVG or Vue | Step-by-step execution |
| Data structure | ASCII | Key structs with fields |
| Call chain | ASCII | Function A → B → C |
| Decision tree | SVG | Safety checks, branching |

## Common Pitfalls (踩坑记录)

### Mermaid Plugin Not Rendering

**Symptom**: `mermaid` code blocks show as plain text, not diagrams.

**Cause**: Plugin installed but not configured in `config.mts`.

**Fix**: You MUST wrap config with `withMermaid()`:

```typescript
import { withMermaid } from 'vitepress-plugin-mermaid'

export default withMermaid(
  defineConfig({
    // ... your config
  })
)
```

**Gotcha**: The closing is `})` — two closing parens: one for `defineConfig(`, one for `withMermaid(`.

### withMermaid Syntax Error

**Symptom**: `Expected ")" but found end of file` or `Expected "}" but found ")"`

**Cause**: Wrong nesting of `defineConfig` inside `withMermaid`.

**Correct syntax**:
```typescript
export default withMermaid(
  defineConfig({
    // config object
  })
)
//     ^^-- first ) closes defineConfig, second ) closes withMermaid
```

**Wrong**:
```typescript
export default withMermaid(defineConfig({ ... }))  // Missing one )
```

### SVG Images Not Showing

**Symptom**: Images show as broken links in browser.

**Cause**: SVG files in `docs/public/diagrams/` but path in markdown is wrong.

**Fix**: Use absolute path from public root:
```markdown
![Diagram](/diagrams/agent-loop.svg)
```

NOT `./diagrams/` or `../public/diagrams/`.

### Build Succeeds but Deployed Site is Old

**Symptom**: Changes not visible on GitHub Pages after push.

**Cause**: Browser cache or GitHub Actions still running.

**Fix**:
1. Check GitHub Actions status: `gh run list --limit 3`
2. Hard refresh browser: `Ctrl + Shift + R`
3. Wait for workflow to complete (usually 1-2 minutes)

### Vue Component Not Rendering

**Symptom**: `<AgentLoopFlow />` shows as plain text.

**Cause**: Component not registered in theme.

**Fix**: Register in `.vitepress/theme/index.ts`:
```typescript
import AgentLoopFlow from './components/AgentLoopFlow.vue'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('AgentLoopFlow', AgentLoopFlow)
  }
}
```

### Dev Server Won't Start

**Symptom**: `npm run dev` hangs or errors.

**Cause**: Port already in use or missing dependencies.

**Fix**:
```bash
cd book
npm install  # Ensure dependencies installed
npm run dev -- --port 5174  # Use different port
```

## Anti-Patterns

- **DO NOT** write generic descriptions without code citations
- **DO NOT** skip source analysis and copy from docs
- **DO NOT** create placeholder content (TODO, FIXME)
- **DO NOT** include all analysis in one massive file — split by module
- **DO NOT** forget line number references
- **DO NOT** build before content is written — content first, then build
- **DO NOT** rely only on Mermaid — use hand-crafted SVGs
- **DO NOT** use generic colors — pick a 5-color system and stick to it
- **DO NOT** skip visual elements — a book without diagrams is just a README
- **DO NOT** forget to wrap config with `withMermaid()` if using Mermaid
- **DO NOT** use relative paths for images in `public/` — use absolute paths like `/diagrams/xxx.svg`

## Pre-Delivery Checklist

- [ ] All interview answers cite specific source code with file:line
- [ ] All source walkthroughs include actual code snippets
- [ ] VitePress build succeeds (`npm run build`)
- [ ] No placeholder text remaining
- [ ] GitHub URLs updated (if applicable)
- [ ] Navigation and sidebar links work
- [ ] Each module has 1-2 SVG architecture diagrams
- [ ] Color system is consistent across all diagrams
- [ ] Code blocks have language labels
- [ ] First blockquote styled as hero callout
- [ ] At least one interactive Vue component for core flow
- [ ] Mermaid plugin configured with `withMermaid()` (if using Mermaid)
- [ ] GitHub Pages deployment works (`gh run list` to verify)
