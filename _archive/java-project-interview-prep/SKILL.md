---
name: java-project-interview-prep
description: Turn a Java backend project, resume project section, README, source tree, or rough idea into a Nix-style interview preparation document with paragraph-first Chinese talking points. Use when the user wants to prepare a Java/SpringBoot project for big-tech interviews, extract resume bullets, imitate the Xiaohongshu Nix Java preparation style, generate project grilling questions, rewrite AI-looking bullet lists into spoken interview answers, identify claim boundaries, or avoid being exposed by follow-up questions.
---

# Java Project Interview Prep

## Core Rule

Prepare the project like an interview defense, not like a generic summary.

The output must make the user able to explain the project under pressure: what real problem it solves, how the system flows, why each technology was chosen, what simpler alternatives were rejected, what can fail, how the system falls back, what data supports the claim, and which claims are safe to say.

Final interview answers must be paragraph-first. Use lists to think, sort, and check coverage; then rewrite the actual answers into small spoken paragraphs.

For full preparation documents, style-sensitive answers, or any request mentioning Nix/Xiaohongshu style, read `references/prep-framework.md`.

## Mode Selection

Choose the smallest useful mode:

- `完整准备文档`: create the full resume + overview + Q&A + grilling + risk-boundary document.
- `简历项目打磨`: only rewrite project intro and resume bullets, but still mark evidence and weak claims.
- `项目拷打`: generate high-pressure questions and paragraph answers for existing bullets.
- `话术重写`: convert an AI-looking outline into natural interview paragraphs.
- `风险体检`: audit claims and split them into safe, cautious, future-only, and do-not-say.
- `速通计划`: produce a focused study plan around the claims the user wants to defend.

If the user does not specify a mode, use `完整准备文档` for broad requests and `话术重写` for requests about answer style.

## Workflow

1. Select the mode and collect inputs.
   Read the user's resume bullets, README, architecture docs, database schema, API docs, source tree, test data, logs, and any existing interview notes. If local files exist, inspect them before drafting. If evidence is missing, mark it as missing rather than inventing it.

2. Identify the project spine.
   Extract the project scenario, target users, main pain point, core workflow, and strongest technical conflict. A strong Java interview project usually has a spine like "long-running work blocks requests", "high-frequency writes need idempotency", "cache and database consistency", "costly AI calls must be protected", or "large files fail under weak networks".

3. Classify each possible highlight.
   Put every highlight into one of four buckets: main selling point, supporting detail, future evolution, or do-not-mainline risk. Do not encourage the user to lead with anything they cannot explain at the implementation and failure-mode level.

4. Build an evidence map.
   For each candidate claim, record the supporting source: code path, doc, test, log, benchmark, user statement, or "no evidence yet". Claims without evidence can still be prepared, but they must not be phrased as measured results.

5. Build the resume-facing version.
   Produce a project intro and 4-6 bullets. Each bullet should follow: action + mechanism + business pain + measurable or observable outcome. If a number is not evidenced, use "planned measurement" or ask for how it was measured.

6. Build the interview-facing version.
   For each main highlight, write:
   - Background pain
   - Concrete flow
   - Selection trade-off
   - Follow-up questions
   - Failure fallback
   - Data or experiment source
   - Boundaries and Plan B

7. Convert lists into spoken paragraphs.
   Treat lists as scaffolding only. The final answer should read like the user can say it directly in an interview: scenario first, pain second, decision third, concrete flow or fallback fourth. Use numbering only for naturally sequential flows.

8. Create the grilling layer.
   Generate questions from interviewer angles: authenticity, scale, data consistency, idempotency, failure recovery, cost, observability, testing, why-not alternatives, and "did AI write this for you?" For each question, answer in a paragraph that starts from the user's actual project facts.

9. Create the study plan.
   End with the missing knowledge the user must learn before using each claim in an interview. Separate must-learn fundamentals from optional expansion topics.

## Style Requirements

Write final talking points in Chinese by default when the user writes in Chinese.

Prefer paragraph answers that sound口述化: first set the context, then name the pain, then explain the decision, then describe the flow or fallback. Avoid "首先/其次/最后" chains unless the answer is a real ordered process.

Do not over-polish into corporate slogans. Keep some practical judgment: "这个方案不是最优解，但在当前阶段是成本最低、风险可控的选择" is better than pretending every decision is perfect.

Do not output final interview answers as dense bullet lists. If a section naturally starts as bullets, add a `可直接口述版本` paragraph after it.

Prefer concrete connective language: "我一开始...", "后来我发现...", "所以这里我没有直接...", "这个方案的边界是...". This is closer to the reference document than generic AI prose.

Explicitly label risky claims:

- `可以主打`: implemented or strongly evidenced.
- `谨慎使用`: understood but not deeply implemented.
- `只作演进`: future plan or interview expansion.
- `不要主动讲`: likely to be asked through.

## Output Shapes

For a full prep document, produce these sections:

1. 简历项目写法
2. 项目概述
3. 项目真实性准备
4. 核心亮点逐条拷打
5. 技术选型与替代方案
6. 失败场景与兜底
7. 八股与项目结合
8. 数据、测试与监控
9. 风险边界与不要主动讲的点
10. 一周到一月复习节奏

For a quick answer, produce only the requested section, but preserve the same preparation logic.

For `话术重写`, output:

1. `原答案问题`: why the current answer sounds AI-generated or unsafe.
2. `可直接口述版本`: 1-3 paragraphs.
3. `可能被追问`: 3-6 questions.
4. `别主动说`: risky wording to avoid.

## Guardrails

Do not fabricate implementation details, benchmark numbers, stars, users, costs, or incidents.

Do not turn every middleware into a highlight. A technology is worth highlighting only when it answers a real project conflict.

Do not let the user memorize someone else's project. Adapt the method to their own facts, vocabulary, and code.

Do not hide weak points. Convert weak points into honest boundaries and future evolution only when the user can explain the trade-off.

Do not promote middleware for its own sake. If the real reason is learning or resume differentiation, turn that into a boundary instead of pretending it was production necessity.

Do not let "AI helped me build it" become a defensive answer. Reframe it as: AI expanded the solution space and accelerated implementation; requirement judgment, trade-off choice, verification, and risk control stayed with the user.
