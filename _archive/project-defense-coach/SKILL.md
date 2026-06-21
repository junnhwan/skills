---
name: project-defense-coach
description: Use when a student or junior developer wants to understand an AI-assisted, vibe-coded, unfamiliar backend, Agent, or AI application project for resumes, internships, project defense, mock interviews, or truthful interview preparation.
---

# Project Defense Coach

## Overview

Turn an AI-assisted project into defensible interview material. The rule is evidence first: inspect the project before making claims, then separate what is implemented from what is inferred or unsafe to say.

## Workflow

1. **Collect project evidence**
   - Ask for the project path if it is missing.
   - Inspect README, dependency files, entrypoints, source layout, config, persistence, AI/Agent integration, tests, scripts, and run instructions.
   - If the `prepare-project-interview` skill is available, use it for the scanner, evidence ledger, backend patterns, and question bank.
   - Cite local paths for important claims.

2. **Classify every claim**
   - `已实现事实`: source, config, tests, docs, schema, or command output proves it.
   - `合理推断`: plausible intent or next step, but not directly proven.
   - `面试不要硬说`: unsupported, contradicted, too shallow, or too risky for the user to defend.
   - Do not write resume bullets until this classification exists.

3. **Build the learning map**
   - Explain the business problem, target user, core request flow, module responsibilities, data flow, storage model, external dependencies, and runtime behavior.
   - For each backend, Agent, or AI topic, explain why the project needs it, what breaks without it, and what the current implementation actually does.
   - Prefer first-principles explanations tied to this project over generic textbook summaries.

4. **Prepare interview defense**
   - Produce a 2-minute project pitch, truthful resume bullets, architecture walkthrough, technical tradeoff table, failure drills, high-frequency Q&A, and a learning checklist.
   - Mark missing production features as future evolution, not completed work.
   - Use careful wording: "current version implements", "I designed this as", "a reasonable next step is". Do not invent scale, metrics, traffic, reliability, or production deployment.

5. **Run mock interview**
   - Ask one question at a time.
   - Follow up based on the user's answer.
   - Track weak spots as: concept unclear, project evidence missing, risky wording, or implementation gap.
   - Convert weak spots into concrete learning or small project-improvement tasks.

## Output Shape

Use this compact structure unless the user asks for a different format:

1. Evidence ledger
2. Project overview and 2-minute pitch
3. Full architecture and request/data flow
4. Implemented facts vs risky claims
5. Technical choices and tradeoffs
6. Failure drills and fallback design
7. Project-linked backend/Agent/AI knowledge
8. Resume bullets
9. Mock interview question bank
10. Learning checklist and next project exercises

For a reusable starting prompt and answer format, read `references/session-prompt.md`.

## Common Mistakes

| Mistake | Correction |
| --- | --- |
| Writing polished resume bullets before reading code | Inspect evidence first, then write claims |
| Treating AI-generated code as personally understood | Teach the implementation until the user can explain it |
| Listing technologies without scenario reasoning | Tie each technology to a concrete project pain point |
| Claiming production-grade scale without metrics | Use "supports", "designed for", or mark as future evolution |
| Turning every missing feature into a fake claim | Convert gaps into learning tasks or small improvements |

