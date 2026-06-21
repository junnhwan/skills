---
name: prepare-project-interview
description: Use when preparing an AI-coded, vibe-coded, or unfamiliar backend project for resumes, project interviews, mock grilling, or learning backend engineering concepts from the project. Trigger when the user asks to generate a project interview preparation document, understand their own project, prepare for backend interview questions, distinguish implemented facts from resume claims, or practice project defense.
---

# Prepare Project Interview

## Overview

Turn an unfamiliar backend project into truthful interview material and a learning plan. The core rule is **Evidence-first**: inspect project artifacts before writing claims, then separate what is implemented from what is inferred or unsafe to say.

## Workflow

1. **Collect context**
   - Ask for the project path if missing.
   - Inspect README/docs, dependency files, source folders, config, schema/migrations, tests, and recent notes.
   - Run `scripts/inspect_project.py <project-path>` when local file access is available.

2. **Classify claims**
   - `已实现事实`: supported by source code, config, schema, tests, logs, docs, or command output.
   - `合理推断`: plausible design intent or evolution path, but not directly proven.
   - `面试不要硬说`: unsupported, contradicted by code, or too weak for the user to defend.

3. **Build the project map**
   - Identify business goal, target users, core modules, data flow, persistence model, external dependencies, and runtime flow.
   - For each technical point, attach evidence paths and explain the backend concept in this project's context.

4. **Generate the preparation document**
   - Load `references/interview-doc-template.md`.
   - Prefer a document structure that starts from project overview, then architecture, AI Coding method, difficulty, technical topics, failure handling, Q&A, and learning checklist.
   - Write resume bullets only from `已实现事实` or clearly marked `合理推断`; never present future plans as completed work.

5. **Teach while preparing**
   - When Redis, MQ, locks, rate limiting, cache consistency, idempotency, database indexes, observability, RAG, SSE, or LLM features appear, load the relevant parts of `references/backend-patterns.md`.
   - Explain: why this scenario needs the pattern, what breaks without it, alternatives, failure modes, and interview cautions.

6. **Mock interview**
   - Use `references/question-bank.md`.
   - Mock interview means one question at a time, then follow-up questions based on the user's answer.
   - Track weak spots as: concept unclear, project evidence missing, wording risky, or implementation gap.

## Scanner

Run:

```bash
python path/to/prepare-project-interview/scripts/inspect_project.py <project-path>
```

Use the JSON output as evidence, not as final truth. Open important files before making strong claims.

## Output Rules

- Quote or cite local file paths for important evidence.
- Mark invented improvements as future evolution.
- If a project is too thin, say so and propose small, implementable improvements instead of inflating it.
- If the user's project is Go, Java, or Python backend, adapt terminology to that stack while keeping the same evidence-first method.
- For interview answers, prefer defensible wording: "I designed this as...", "the current version implements...", "a reasonable next step is..." rather than overstating production scale.

## Reference Navigation

- Use `references/interview-doc-template.md` for the final Markdown structure.
- Use `references/question-bank.md` for grilling questions and follow-ups.
- Use `references/backend-patterns.md` when explaining backend engineering ideas or checking if a project claim is defensible.
