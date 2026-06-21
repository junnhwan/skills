---
name: project-interview-grill
description: Audit and prepare resume projects for defensible interviews from a real codebase, README, project document, or resume draft. Use when the user asks whether a project can be written on a resume, wants resume bullets, wants "项目拷打"/mock grilling, wants to compare against reference resumes, wants claim boundaries, or wants interview-ready answers for architecture, tradeoffs, tests, failure handling, and evidence. For Agent/Coding Agent/LLM tool projects, also use the Agent-specific grilling framework in this skill.
---

# Project Interview Grill

Turn a project into resume-ready, interview-defensible material. The hard rule: never upgrade a roadmap, prototype, hidden path, or config-gated feature into a default shipped capability.

## Skill Routing

- Use this skill for general project resume writing, evidence audits, project grilling, and mock interview preparation.
- If the project is clearly Java/SpringBoot/backend middleware-heavy and the user wants a full Nix-style document, prefer `$java-project-interview-prep` if available; otherwise apply the same pressure-defense method here.
- If the user asks for an interactive HTML learning document, visual notes, or "技术深潜", prefer `$tech-deep-dive` if available.
- If multiple outputs are requested, do the resume/interview evidence audit first, then generate deep-dive notes only after the safe claims are known.

## Core Workflow

1. Identify the target.
   - Infer target role, resume space, project type, and preferred style from the request.
   - If missing, assume the user wants Chinese backend/AI-infrastructure interview preparation and state the assumption.
   - If reference resumes or prep docs are provided, extract their structure and tone, not their unsupported claims.

2. Build an evidence map before drafting.
   - Read README, docs, configs, tests, and runtime assembly code.
   - Prefer `rg` and `rg --files` for discovery.
   - Verify whether each capability is wired into the main runtime, config-gated, default-off, test-only, hidden, prototype-only, or roadmap-only.
   - Run relevant tests or smoke commands when practical before making positive claims.

3. Classify every possible claim.
   - `可证明`: implemented, wired into the primary path, and backed by code/tests/docs.
   - `需限定`: real but partial, config-gated, default-off, MVP, or only safe with precise wording.
   - `只作演进`: useful future direction or interview expansion, not a current headline.
   - `别写`: roadmap-only, unverifiable, shallow, misleading, or likely to be exposed by follow-up questions.

4. Choose the output mode.
   - Use **Resume Audit Mode** for "能不能写简历".
   - Use **Resume Draft Mode** for project descriptions and bullets.
   - Use **Full Grill Mode** for a preparation document.
   - Use **Mock Interview Mode** when the user wants continuous grilling.
   - Use **Demo/Test Mode** when the user asks how to verify the feature in the real product path.

5. Draft only defensible material.
   - Tie each bullet to: technical mechanism + real pain + observable outcome.
   - Use numbers only when the user or local artifacts provide a measurement source. Otherwise use precise non-numeric wording.
   - Prefer paragraph-first spoken answers for interview prep; use lists for flows, matrices, and checklists.

6. Leave a study plan.
   - End full prep with missing knowledge, risky claims, and practice priorities.
   - Separate must-learn source files, fundamentals, tests/demos, and optional expansion topics.

## Evidence Matrix

For serious resume or grilling work, create this matrix before final wording:

| 简历说法 | 代码证据 | 测试/运行证据 | 当前边界 | 面试风险 |
|---|---|---|---|---|
| Claim as the resume might say it | Files, functions, config, docs | Tests, logs, session traces, demo steps | default/config-gated/MVP/prototype | likely follow-up or weak point |

If a row has no code evidence and no user-provided evidence, do not promote it as a resume bullet.

## Output Modes

### Resume Audit Mode

Return:

1. `结论`: can this project be written, and at what positioning level.
2. `可写亮点`: defensible claims.
3. `需限定亮点`: useful but must be worded carefully.
4. `不要这样写`: overclaims and why they are risky.
5. `补证据清单`: files, commands, logs, tests, or screenshots to collect.

### Resume Draft Mode

Return:

```text
项目名 - 项目定位
技术栈：...

项目简介：...

- ...
- ...
```

Use 4-6 bullets. Each bullet should be strong enough to survive "你具体怎么实现的？失败怎么办？数据怎么来的？为什么不用 X？"

### Full Grill Mode

Return:

1. 简历写法
2. 项目概述
3. 全链路流程
4. 证据矩阵
5. 核心亮点逐条拷打
6. 技术选型与替代方案
7. 失败场景与兜底
8. 测试、数据与可观测性
9. 风险边界
10. 复习节奏

For each core highlight, use:

`简历说法 -> 背景痛点 -> 具体实现 -> 为什么这么选 -> 为什么不用替代方案 -> 失败场景 -> 兜底方案 -> 怎么验证 -> 边界`

### Mock Interview Mode

Ask one question at a time. Start with project authenticity and full-flow explanation, then move to the strongest resume bullet, then attack failure modes and alternatives. After each user answer:

- Point out vague or unsafe wording.
- Ask the next sharper follow-up.
- Keep a running list of `已稳`, `还虚`, and `别主动讲`.

### Demo/Test Mode

Separate:

- automated commands
- sustained interactive demo steps
- expected visible signals
- post-run artifacts to inspect

For TUI/Agent products, prefer the normal sustained interaction path if the user says not to use one-shot mode.

## Agent And LLM Project Add-On

When the project involves Agent Runtime, Coding Agent, LLM tools, memory, context management, MCP, planning, subagents, ReAct, function calling, or safety controls, read `references/agent-project-framework.md` and apply it to the evidence matrix and grilling questions.

Minimum topics to cover for Agent projects:

- Agent Loop lifecycle and stop conditions
- tool call parsing, execution, result envelope, and protocol continuity
- context governance and compaction boundaries
- memory storage, injection, and mutation path
- planning/todo state and whether it is a real Plan Mode
- subagent type: synchronous result, background spawn, recursion limits, and tool restrictions
- MCP scope: default off, config-gated, stdio only, resources/prompts support, namespacing
- safety model: risk classes, confirmations, auto-approve boundaries, blocked commands
- session/audit trace and how it helps debug model/tool behavior
- real-model sustained demo path and fake/test path

## Quality Bar

- Anchor risky claims to local files or command results when possible.
- Say "默认启用", "配置开启", "MVP", "原型", "隐藏调试入口", or "后续方向" explicitly.
- Trust runtime assembly and tests over README wording when they disagree.
- Keep final wording honest and high-signal. Do not invent benchmarks, users, costs, or production incidents.
- If the user wants a polished resume but evidence is weak, first report the weak evidence, then offer a conservative version.
