---
name: project-notes-html-deck
description: Use when reading an unfamiliar codebase, vibe-coded project, AI app, full-stack repo, or source folder to produce visual project notes, interview-grill preparation, project defense notes, architecture walkthroughs, or a single-file HTML/PPT-style note deck.
---

# Project Notes HTML Deck

## Overview

Create source-backed HTML slide notes for unfamiliar projects. The output should help the user understand what the project does, defend what is truly implemented, answer interview grilling questions, and find the source evidence behind every claim.

## Workflow

1. Read `references/source-reading.md` before scanning the repo.
2. Build a source-backed outline from local files before authoring slides.
3. Read `references/style-guide.md` before editing HTML.
4. If the user mentions interview prep, resume projects, grilling, "拷打", or vibe coding defense, also read `references/interview-grill-mode.md`.
5. In interview-grill mode, look for `resume.md` first, then resume-like files under `docs/` before choosing highlights. Treat the resume text as the question source and the codebase as evidence.
6. Copy `assets/template.html` to the requested output path and replace its sample content.
7. Keep the deck single-file unless the user asks for a project folder.
8. Run `node <skill>/scripts/validate_deck.mjs <output.html>` before claiming completion.
9. Visually check representative slides in a real browser or headless screenshot. Structural validation alone is not enough.

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

For interview-grill mode, prefer 12-18 dense but readable slides. If a concrete `resume.md` or final resume draft exists, 20-28 slides is acceptable; split crowded content rather than shrinking text below readability.

| Section | Slides |
| --- | --- |
| Defense overview | project one-liner, real pain, stack, AI-coding ownership |
| Evidence matrix | resume claims vs code facts, confidence labels, do-not-say list |
| Resume claim drill | one slide or chapter per resume bullet: likely questions, source evidence, safe answer, danger follow-up |
| Technical highlights | 3-5 defensible highlights ranked by interview value |
| Deep-dive chapters | for each highlight: pain, tradeoff, implementation flow, key data structures |
| Grill Q&A | interviewer psychology, first-person answer, follow-up traps |
| Failure playbook | what-if failures, concurrency/idempotency, degraded behavior |
| Closing route | what to study next and what to avoid volunteering |

## Template Use

Use `assets/template.html` as the starting point. Preserve:

- Left sidebar navigation with `navSections`.
- One `<section class="slide" data-title="...">` per page.
- Keyboard navigation and progress bar.
- 1720 x 900 desktop canvas with responsive stacking.
- Paper-grid visual style, 8px cards, low-saturation accents, and source-reading tone.
- Knowledge-note typography: cover title <= 68px, slide title <= 48px, body <= 18px. Do not use hero-scale type for dense notes.

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
| Grill question card | State interviewer psychology, answer strategy, and evidence path |
| Claim matrix | Compare resume/user claim, source evidence, safe wording, and risk |
| Resume question tree | For one resume bullet, list entry questions, follow-ups, edge cases, safe answer, and code anchors |
| Failure playbook | Explain what breaks, current code behavior, and honest improvement |

## Common Mistakes

- Do not copy the referenced example deck's article content. Only reuse the structural idea and visual grammar.
- Do not create a marketing landing page. The first screen is the deck.
- Do not make oversized hero slides for source notes. If content starts to crowd, lower type size or split the slide.
- Do not paste large source files into slides. Use minimal snippets and explain the call path.
- Do not overfill tables. Split crowded tables into multiple slides.
- Do not claim the app runs unless a command was actually run and verified.
- Do not hide unknowns. Unknowns are useful handoff information.
- Do not turn interview prep into generic architecture praise. Include hard follow-up questions and "do not say" boundaries.
- Do not stop at a few generic questions when a resume is present. Every resume bullet needs a question tree and at least one failure/concurrency/security/scale follow-up.

## Verification

After generating the deck:

```bash
node C:/Users/zjh/.codex/skills/project-notes-html-deck/scripts/validate_deck.mjs path/to/output.html
```

If a dev server is needed to preview the file, start one and provide the URL. If the HTML is standalone, give the local file path.
