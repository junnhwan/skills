# Project Interview Preparation Template

Use this template after inspecting project evidence. Keep unsupported claims out of resume bullets.

## 0. Evidence Ledger

| Claim | Label | Evidence | Interview Risk |
| --- | --- | --- | --- |
| Short factual claim | 已实现事实 / 合理推断 / 面试不要硬说 | File path, config, schema, test, or command | Low / Medium / High |

Label rules:

- `已实现事实`: visible in code, config, schema, docs, tests, or command output.
- `合理推断`: reasonable design intent or future direction, but not directly implemented.
- `面试不要硬说`: unsupported, contradicted, or too risky for the user to defend.

## 1. 项目概述

### 项目介绍

Explain in 3-5 sentences:

- What problem the project solves.
- Who uses it.
- What the main backend flow is.
- Why the project has backend engineering value.
- Which parts were AI-assisted and which decisions the user owns.

### 技术栈

List only detected or documented technologies. Separate confirmed dependencies from possible technologies.

### 简历描述

Write 3-6 bullets. Each bullet should follow:

`业务痛点 + 技术方案 + 可验证结果/工程收益`

Avoid fake scale. If no benchmark exists, say "designed to" or "supports" instead of inventing QPS or latency numbers.

## 2. 全链路架构流程

Break the system into stages:

1. Request entry and validation.
2. Core business processing.
3. Persistence and cache interaction.
4. Async jobs or external calls.
5. Response, polling, streaming, or notification.
6. Failure handling and retry path.

For each stage:

- What component receives input?
- What data structure or table changes?
- What happens on success?
- What happens on failure?

## 3. AI Coding 方法论

Cover:

- Requirement decomposition before coding.
- Tech option comparison and manual verification.
- Module-by-module implementation with interface constraints.
- Review, debugging, and test process.
- AI limitations encountered: hallucinated APIs, forgotten context, weak edge-case handling.

Interview stance:

- AI accelerates implementation.
- The user must own requirement judgment, architecture choices, and quality control.
- Never claim deep ownership of generated code that the user cannot explain.

## 4. 项目难点

For each difficulty:

| Difficulty | Why it matters | Current implementation | Alternatives | Interview follow-up |
| --- | --- | --- | --- | --- |

Good difficulty topics include consistency, concurrency, idempotency, long-running tasks, cache pressure, external API instability, upload reliability, rate limiting, and observability.

## 5. 核心技术点专题

For each topic:

### Topic Name

#### 背景痛点

Describe the exact project scenario.

#### 技术选型

Compare 2-4 options with trade-offs.

#### 实现流程

Use numbered steps and mention concrete keys, tables, APIs, or functions when known.

#### 面试 Q&A

Write questions in this format:

- Q: why did you choose this?
- Q: what happens if it fails?
- Q: what if concurrency increases?
- Q: how do you verify it works?
- Q: what would you improve next?

#### 兜底保障

Explain retry, idempotency, compensation, rollback, alerting, and degradation.

## 6. 技术选型对比

Use a table:

| Decision | Chosen | Alternatives | Why chosen | When it would be wrong |
| --- | --- | --- | --- | --- |

This section is where interviewers test whether the project is "for technology stack" or "for scenario".

## 7. 故障拷打

Prepare answers for:

- Redis unavailable.
- DB write fails.
- MQ send succeeds but consume fails.
- MQ duplicate consumption.
- Cache and DB inconsistent.
- Third-party API times out.
- User retries same request.
- Service restarts mid-task.
- Data migration or schema mismatch.

Always answer with:

1. Detection.
2. Immediate behavior.
3. Data correctness.
4. Recovery.
5. Long-term improvement.

## 8. 八股知识迁移

Tie general backend topics to the project:

- Redis data structures and expiration.
- Distributed locks and idempotency.
- Message queue delivery semantics.
- Cache penetration, breakdown, and avalanche.
- Token bucket or sliding-window rate limiting.
- Database indexes, transactions, and optimistic locks.
- Observability: logs, metrics, tracing, alerts.
- LLM app topics: RAG, SSE, structured output, memory, cost control.

## 9. Mock Interview Questions

Group questions by:

- Project overview.
- Architecture flow.
- AI Coding authenticity.
- Core technology.
- Failure handling.
- Scaling and evolution.
- Weak implementation areas.

## 10. 学习清单

Use:

| Priority | Topic | Why it matters for this project | How to learn | Project exercise |
| --- | --- | --- | --- | --- |

Include only topics that help the user defend or improve this project.
