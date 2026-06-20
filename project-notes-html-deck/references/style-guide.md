# Project Notes Deck Style Guide

Use this guide when producing a project-reading HTML deck from `assets/template.html`.

## Visual Direction

Build a readable knowledge notebook, not a marketing deck. The style is calm, paper-like, and information-dense:

- Warm paper background with a subtle 26px grid.
- Left sidebar for chapter navigation, section numbers, progress, and page count.
- Main stage for one visible slide at a time.
- Low-saturation accent colors: green for structure, blue for interfaces, coral for risk or emphasis, gold for decisions.
- Serif display headings plus readable Chinese body text. Do not use oversized hero typography outside the cover.
- Cards use 8px radius, thin borders, and light shadows. Do not nest cards inside cards.

## Layout Types

Use these recurring slide types:

| Type | Use for | Required content |
| --- | --- | --- |
| `cover` | Project name and reading context | repo path, date, stack chips |
| `three-col` | Big conceptual groups | 3 cards, each with number, title, concrete summary |
| `module-map` | Subsystems | 4-8 modules with responsibility |
| `file-table` | Key file list | file path, responsibility, why it matters |
| `flow` | Request/runtime/data path | 4-6 ordered steps with source-backed labels |
| `two-col` | Explanation plus diagram/code | one prose panel and one visual/code panel |
| `code-focus` | Small critical snippet | max 20 lines, explain upstream/downstream impact |
| `risk-notes` | Risks and next actions | risks, reading route, first low-risk tasks |
| `quote` | Final takeaway | one principle, not decorative filler |

## Content Rules

- Every technical claim must be traceable to files read in the repo.
- Prefer relationships over inventory. A deck that only lists files is not useful.
- Use short, concrete slide titles. Avoid "系统介绍" if "从上传文件到生成摘要的链路" is known.
- Keep visible bullets short. Put explanatory detail in speaker notes only if the deck supports notes.
- For code excerpts, include only the smallest snippet that proves the point.
- For AI/vibe coding projects, include model providers, prompt locations, tool definitions, memory/RAG paths, and where API keys or environment variables are read.

## Navigation Rules

Keep `navSections` synchronized with slide indexes:

- `index` is zero-based.
- Each section should represent 2-6 slides.
- Sidebar titles should summarize the reading journey: overview, source map, runtime flow, AI layer, risks.
- Update the `<title>`, sidebar brand, cover, and chips for each generated deck.

## Responsive Rules

The template is optimized for 1720 x 900 and scales down on desktop. Mobile stacks the sidebar and slide content.

- Do not rely on negative margins or absolute-positioned text.
- Keep tables to 3 columns unless the content is very short.
- Use `word-break: break-word` on paths and identifiers.
- If a slide feels crowded, split it. Dense does not mean unreadable.
