# Project Notes Deck Style Guide

Use this guide when producing a project-reading HTML deck from `assets/template.html`.

## Visual Direction

Build a readable knowledge notebook, not a marketing deck. The style is calm, paper-like, and information-dense:

- Warm paper background with a subtle 26px grid.
- Left sidebar for chapter navigation, section numbers, progress, and page count.
- Main stage for one visible slide at a time.
- Low-saturation accent colors: green for structure, blue for interfaces, coral for risk or emphasis, gold for decisions.
- Serif display headings plus readable Chinese body text. Do not use oversized hero typography for source notes or interview prep.
- Cards use 8px radius, thin borders, and light shadows. Do not nest cards inside cards.

## Typography Hard Limits

This deck is a knowledge notebook, not a keynote hero page. Oversized text causes the exact failure mode this skill must avoid: content looks impressive but cannot be read or defended.

| Element | Desktop target | Hard max |
| --- | --- | --- |
| Cover title | 52-64px | 68px |
| Normal slide title | 34-44px | 48px |
| Lead paragraph | 17-20px | 22px |
| Card/table body | 13-16px | 18px |
| Card heading | 18-22px | 24px |
| Quote/callout | 22-30px | 34px |

Do not use viewport-width typography. Use fixed/clamped sizes that stay inside the 1720 x 900 canvas.

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
| `grill-card` | Interview questions | Q, interviewer psychology, answer strategy, evidence path |
| `claim-matrix` | Resume/project defense | claim, code evidence, safe wording, risk |
| `resume-drill` | Resume bullet grilling | exact bullet, likely entry questions, follow-ups, safe answer, code anchors, dangerous overclaims |

## Content Rules

- Every technical claim must be traceable to files read in the repo.
- Prefer relationships over inventory. A deck that only lists files is not useful.
- Use short, concrete slide titles. Avoid "系统介绍" if "从上传文件到生成摘要的链路" is known.
- Keep visible bullets short. Put explanatory detail in speaker notes only if the deck supports notes.
- For code excerpts, include only the smallest snippet that proves the point.
- For AI/vibe coding projects, include model providers, prompt locations, tool definitions, memory/RAG paths, and where API keys or environment variables are read.
- For interview prep, include first-person answer cards, likely follow-up questions, and do-not-say boundaries.
- For resume-driven interview prep, cover every resume bullet. Prefer more slides over crowded "all questions on one page" tables.
- Keep each dense slide under roughly 120 Chinese characters of prose per major panel, or split it.

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

## Visual Verification

The structure validator does not prove layout quality. Before completion:

- Open or screenshot the cover, one table-heavy slide, one flow slide, and one Q&A/risk slide.
- Check for clipped text, overlapping content, oversized headings, and unreadable table rows.
- If any representative slide is crowded, revise typography or split slides before reporting completion.
