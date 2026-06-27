# Java Project Interview Prep Framework

Use this reference when producing a full Java project preparation document, imitating the Nix-style preparation method, or rewriting answers into interview-ready spoken paragraphs.

## What This Preparation Style Optimizes For

This style is not a knowledge dump. It is a defense document built around interview pressure.

The core pattern is:

`resume claim -> real business pain -> concrete project flow -> why this technology -> why not simpler alternatives -> failure case -> fallback -> measurable evidence -> boundaries`

The point is to keep the interview inside territory the user can actually defend. If a feature is shallow, label it as evolution or background knowledge instead of making it a main selling point.

## Nix-Style Paragraph Formula

The reference style is not "many small points". It is a set of short spoken paragraphs that already contain the reasoning path.

Use this formula for final answers:

`真实场景 -> 痛点暴露 -> 我的判断 -> 方案落地 -> 边界/兜底`

The answer should sound like this:

> 这个项目里我真正想解决的不是单纯把功能跑通，而是视频处理这个场景本身很容易把请求链路拖死。最开始如果同步做转码和大模型调用，用户请求会挂住几十秒甚至更久，前端看起来就是一直转圈，后端线程也会被这些重任务占住。
>
> 所以后来我把这条链路拆成了两段。请求进来之后，后端只做参数校验、任务记录和消息投递，然后立刻把任务 ID 返回给前端。真正耗时的处理交给后台消费者执行，消费者跑完之后再把任务状态和结果落到数据库里。这个方案的边界是总处理耗时没有消失，只是从 HTTP 请求链路里剥离出去了，所以前端必须配合状态查询，把处理中、成功、失败这几个终态展示清楚。

This is different from:

```text
1. 使用 MQ 异步解耦
2. 前端轮询任务状态
3. MySQL 保存结果
4. 失败走重试
```

The list is useful as scaffolding, but it is not the final interview answer.

## Drafting Layers

Use two layers when preparing content.

**Material layer**

Use bullets, tables, and checklists to collect facts:

- what code exists
- what data structure is used
- what failure case exists
- what alternative was rejected
- what evidence supports the result

**Talking layer**

Rewrite the material into paragraphs. Each paragraph should do one job:

- paragraph 1: project scenario and pain
- paragraph 2: implementation flow and technical decision
- paragraph 3: fallback, measurement, or boundary

For each major answer, include `可直接口述版本`. The user should be able to read that section aloud without converting bullet points in their head.

## Sentence Patterns To Prefer

Use natural causal transitions:

- "我一开始的方案是..."
- "后来真正暴露的问题是..."
- "这里我没有直接选 A，是因为..."
- "最终我选 B，核心原因是..."
- "这个方案不是银弹，它的边界是..."
- "如果这一步失败，我的处理不是让用户死等，而是..."
- "这个数据我会限定为接口 RT，而不是整个任务耗时..."
- "这块我不会主动作为主亮点讲，因为..."

Avoid generic AI transitions when writing final talking points:

- "首先、其次、最后" repeated mechanically
- "综上所述，本项目显著提升了系统稳定性"
- "该技术具有高性能、高可用、高扩展性"
- a long list of concepts without project flow

## Global Document Structure

Use this structure for a complete prep doc:

1. **简历项目写法**
   Start with the project name, tech stack, one-sentence intro, then 4-6 bullets. Each bullet should tie a technology to a pain and an outcome.

2. **项目概述**
   Explain why the project exists, who uses it, what the main workflow is, and what the real technical conflict is. This section should be easy to say in 60-90 seconds.

3. **项目真实性准备**
   Prepare answers for architecture flow, frontend/backend split, AI coding workflow, API choice, project difficulty, product value, actual debugging cases, and "how much of this did AI generate?"

4. **核心亮点逐条拷打**
   Each highlight gets its own section. For Java backend projects, common highlights include MQ async processing, Redis/Redisson idempotency, chunked upload, cache consistency, rate limiting, retry, object storage, RAG, SSE, delayed tasks, optimistic locking, and database design.

5. **八股与项目结合**
   Do not recite textbook definitions alone. Each concept should reconnect to the project. Example: MQ repeated consumption should lead to idempotency keys, status machines, unique indexes, and lock choices in the user's project.

6. **兜底与异常场景**
   Prepare for "what if this step fails?" questions across producer, broker, consumer, database, Redis, object storage, third-party API, frontend polling/push, and user retry.

7. **风险边界**
   Mark which claims are safe, which are shallow, and which should only be mentioned if asked.

## Highlight Template

For every resume bullet or feature, fill this template before writing final prose.

**Resume claim**
What the resume says or wants to say.

**Business pain**
What breaks without this design. Prefer concrete pain: HTTP timeout, repeated token cost, weak-network upload failure, oversold inventory, cache stampede, data inconsistency, queue backlog, or user waiting forever.

**Concrete flow**
Describe the exact request path and data movement. Include key IDs, tables, Redis keys, MQ topics, statuses, and where the final state is written.

**Why this choice**
Name the chosen technology and the business reason. The reason must be more specific than "high performance".

**Why not alternatives**
Prepare at least two alternatives and reject them in context. Good alternatives are simpler options: local thread pool vs MQ, SETNX vs Redisson, MySQL vs Redis, fixed window vs token bucket, WebSocket vs SSE/polling, full-text LIKE vs RAG.

**Failure cases**
Ask what happens if each boundary fails: request accepted but MQ send fails, API succeeds but DB write fails, Redis loses progress, chunk merge fails, consumer retries after partial success, frontend repeats a request, network returns after 99% upload.

**Fallback**
Use patterns such as idempotency key, unique index, status machine, DLQ, retry with backoff, manual compensation, local durable log, lifecycle cleanup, degraded path, rate limiting, or returning a clear failed state.

**Data source**
Say how the result was measured. If there is no measurement, say what should be measured: Postman RT, JMeter comparison, logs, retry count, upload success rate, queue lag, API failure rate, token cost, storage cost.

**Boundary**
Say what this solution does not solve and what the future plan is.

## Spoken Answer Style

Final interview answers should usually be 1-4 paragraphs. They should sound like a person explaining a decision, not a list generated by an assistant.

Good answer shape:

> 我这个项目里真正麻烦的点不是功能本身，而是这个场景会把某个资源打满。最开始我用的是同步链路，结果用户请求会被长时间挂住，接口很容易超时。后来我把这段逻辑拆成了前台快速返回和后台异步消费两段，前台只负责校验、落任务记录和投递消息，后台消费者再处理重任务。这样用户拿到的是任务 ID，后续通过状态查询拿最终结果。
>
> 这里我没有直接用本地线程池，是因为这个任务失败后需要可靠重试，而且任务本身价值比较高，丢在 JVM 内存队列里风险太大。MQ 至少能把任务落到 Broker 里，失败后也能走重试和死信队列。这个方案的边界是处理总耗时没有消失，只是从请求链路里剥离了出去，所以前端还需要明确展示处理中、成功和失败这几个终态。

Avoid this as final prose:

```text
1. 使用 RocketMQ 异步解耦
2. 使用 Redisson 保证幂等
3. 使用 MySQL 状态机
4. 使用 DLQ 兜底
```

Lists are allowed for internal scaffolding, flows, and final checklists. The answer the user would say to an interviewer should be paragraph-first.

Before returning an answer, run this conversion check:

1. If the answer starts with a technology name, add the business scene before it.
2. If the answer has more than five bullets, convert it into 2-3 paragraphs.
3. If the answer says "提升性能" or "保障稳定性", add the exact resource or failure it protects.
4. If the answer mentions a metric, add how it was measured or mark it as unverified.
5. If the answer sounds too perfect, add a boundary or Plan B.

## Common Grilling Angles

### Authenticity

Ask:

- 这个项目为什么要做？
- 用户是谁？
- 你自己遇到过什么问题？
- 这个数据是怎么测出来的？
- 代码里哪一块是你最熟的？
- AI 在里面到底帮你做了什么？

Answer pattern:

Start with a concrete scenario, then a specific bug or bottleneck, then explain how AI helped expand options but the final trade-off came from the user's project constraints.

### Architecture Flow

Ask the user to explain the full path from frontend request to final persisted result. A good answer names stages and state transitions. It should not only name technologies.

For async projects, force this distinction:

HTTP 200 only means request accepted or task submitted. It does not mean business success. The real success is the terminal state in DB/Redis and the frontend rendering that terminal result.

### Technology Choice

Good choices are relative. Always prepare "why not X".

Examples:

- MQ vs local thread pool: reliability, retry, backlog, cross-service scaling.
- Redisson vs SETNX: unknown task duration and watchdog.
- Redis vs MySQL for upload chunks: high-frequency temporary writes.
- Token bucket vs fixed window/l漏桶: average rate plus burst tolerance.
- SSE vs WebSocket: server-to-client stream only, simpler HTTP model.
- RAG vs LIKE/function calling: semantic recall and source-grounded answers.

### Failure and Compensation

Every important boundary needs a fallback answer.

Use this question repeatedly:

> 如果这一步已经成功了，但下一步失败了，会不会产生脏数据、重复扣资源、用户死等，或者任务丢失？

Map answers to:

- idempotency key
- database unique index
- status machine
- retry and DLQ
- local durable log for expensive outputs
- frontend retry or clear failed state
- lifecycle cleanup for temporary objects
- rate limit and degradation during dependency failure

### Being Asked Through

If the user only understands a topic at a concept level, do not make it a headline.

Use:

- "这个我目前没有作为主链路实现，更多是下一版的演进方向。"
- "当前阶段我用的是更简单的方案，因为数据规模和成本还不值得引入完整组件。"
- "我知道这个方案的边界，所以我没有把它作为项目最核心的亮点。"

Also prepare a fallback line for shallow features:

> 这块我了解它的标准工程做法，但我当前项目里没有完整落到生产级，所以我不会把它包装成核心亮点。更准确地说，它是我基于当前方案看到的下一步演进方向。

This kind of answer is safer than pretending the user built a production-grade subsystem.

## Resume Bullet Pattern

Use this formula:

`动词 + 技术机制 + 业务痛点 + 结果`

Examples of shape, not content to copy:

- 引入 MQ 将长耗时任务从请求链路剥离，避免接口长时间阻塞，并通过任务状态机完成前后端闭环。
- 基于 Redis/Redisson 设计幂等控制，用业务唯一标识拦截重复提交，降低重复计算和外部 API 成本。
- 采用分片上传和断点续传处理大文件弱网传输，失败时只补传缺失分片，避免从头上传。

If numbers are used, attach the measurement method:

- "接口 RT 从 60s 降到 50ms" must say which video, what environment, how measured, and that this is request response time rather than total processing time.

## Full Prep Output Template

Use this template when the user asks for a complete document.

```markdown
# 项目名--面试准备文档

## 简历写法

技术栈：...

项目简介：...

- ...

## 项目概述

### 项目介绍

用 2-4 段解释真实背景、用户、主流程和核心难点。

### 全链路流程

用阶段描述请求如何流动、状态如何变化、结果如何闭环。

### 项目真实性准备

#### Q1: 你为什么做这个项目？

段落式回答。

#### Q2: 这个项目最难的地方是什么？

段落式回答。

#### Q3: AI 在项目里起了什么作用？

段落式回答，强调 AI 提供方案空间，最终判断和质量把关由自己完成。

## 亮点一：...

### 背景痛点

段落式回答。

### 具体实现

可以用阶段或少量编号描述流程。

### 选型问题

#### Q1: 为什么用 A 不用 B？

段落式回答。

### 兜底保障

#### Q1: 如果 ... 失败怎么办？

段落式回答。

## 风险边界

### 可以主打

### 谨慎使用

### 只作演进

### 不要主动讲

## 复习清单

列出必须补齐的源码、日志、测试、八股和口述练习。
```

## One-Month Preparation Rhythm

Use this only when the user asks for a study plan or "速通" plan.

Week 1: Establish the project spine and safe resume bullets. Understand the core workflow and run or read the relevant code. Remove claims that cannot be defended.

Week 2: Deepen the 2-3 strongest highlights. For each one, prepare flow, alternatives, failure cases, and measured evidence. Practice 2-minute answers.

Week 3: Connect highlights to Java backend fundamentals: MQ delivery semantics, Redis atomicity, locks, database indexes, transactions, cache consistency, JVM/threading basics, and observability.

Week 4: Run mock grilling. Rewrite weak answers into paragraphs. Create a "do not say unless asked" list. Prepare honest AI-coding and project-authenticity answers.

## Final Quality Check

Before returning a preparation document, verify:

- Every main claim has a real project pain.
- Every technology choice has rejected alternatives.
- Every cross-system boundary has a failure answer.
- Every metric has a measurement source or is marked as unmeasured.
- Final interview answers are paragraph-first.
- Risky or shallow topics are labeled instead of promoted.
- Every bullet-heavy section has a `可直接口述版本` when it may be used in an interview.
