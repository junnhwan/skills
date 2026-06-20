---
name: project-notes-html-deck
description: Use when reading an unfamiliar codebase, vibe-coded project, AI app, full-stack repo, or source folder to produce visual project notes, architecture walkthroughs, source-reading summaries, handoff decks, or a single-file HTML/PPT-style note deck.
---

# Project Notes HTML Deck

## Overview

Create source-backed HTML slide notes for unfamiliar projects. The output should help the user understand what the project does, how it runs, where the important code lives, what the primary runtime flow is, and where to start changing it.

## Workflow

1. Read `references/source-reading.md` before scanning the repo.
2. Build a source-backed outline from local files before authoring slides.
3. Read `references/style-guide.md` before editing HTML.
4. Copy `assets/template.html` to the requested output path and replace its sample content.
5. Keep the deck single-file unless the user asks for a project folder.
6. Run `node <skill>/scripts/validate_deck.mjs <output.html>` before claiming completion.

## Source Reading Requirements

- Start with `rg --files`, README/docs, package/build files, route/API definitions, entry points, schemas, and AI-specific files.
- Trace at least one primary flow end to end: user action or trigger -> entry point -> state/request -> API/service/model/database -> output.
- Every slide that makes a technical claim should be traceable to repo files or command output.
- Label uncertain conclusions as inferred or unknown instead of presenting guesses as facts.
- For vibe-coded projects, look for duplicated helpers, dead files, mismatched README scripts, hard-coded config, prompt text in UI components, weak model-call error handling, and missing tests.

## Deck Shape

Prefer 10-18 slides for a normal project:

| Section | Slides |
| --- | --- |
| Project overview | cover, purpose, user flow, stack map |
| Source map | directory map, key files, module responsibilities |
| Runtime understanding | primary flow, data/request flow, AI layer if present |
| Code focus | 1-3 critical snippets with explanation |
| Risks and next steps | risks, verification gaps, reading route, first safe tasks |

For small projects, use 6-9 slides. For larger systems, split into multiple decks rather than making crowded slides.

## Template Use

Use `assets/template.html` as the starting point. Preserve:

- Left sidebar navigation with `navSections`.
- One `<section class="slide" data-title="...">` per page.
- Keyboard navigation and progress bar.
- 1720 x 900 desktop canvas with responsive stacking.
- Paper-grid visual style, 8px cards, low-saturation accents, and source-reading tone.

Update:

- `<title>`, sidebar brand, cover title, repo path, date, and chips.
- Slide content and `navSections` indexes.
- Any sample file paths, code snippets, and claims.

## Content Patterns

Use the deck to explain relationships, not just inventory.

| Pattern | Good use |
| --- | --- |
| Three cards | Summarize purpose, user path, code organization |
| Module map | Show subsystem responsibilities and boundaries |
| Key file table | Explain file path, responsibility, why it matters |
| Flow diagram | Show request/data/model chain with source-backed steps |
| Code focus | Include max 20 lines of critical code plus impact |
| Risk slide | State risks, evidence, and next action |

## Common Mistakes

- Do not copy the referenced example deck's article content. Only reuse the structural idea and visual grammar.
- Do not create a marketing landing page. The first screen is the deck.
- Do not paste large source files into slides. Use minimal snippets and explain the call path.
- Do not overfill tables. Split crowded tables into multiple slides.
- Do not claim the app runs unless a command was actually run and verified.
- Do not hide unknowns. Unknowns are useful handoff information.

## Verification

After generating the deck:

```bash
node C:/Users/zjh/.codex/skills/project-notes-html-deck/scripts/validate_deck.mjs path/to/output.html
```

If a dev server is needed to preview the file, start one and provide the URL. If the HTML is standalone, give the local file path.
