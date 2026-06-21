---
name: learn-vibe-coded-project
description: Systematically guide the user through understanding a codebase they did not write themselves — typically AI vibe-coded projects where they need to learn the code for interviews, handoff, or production maintenance. Use this skill whenever the user says "带我学这个项目", "我没读过这个代码", "vibe coded 的项目要面试", "help me understand this codebase", "walk me through this repo", "I need to understand this for an interview", "考考我这个项目", or similar requests to study an existing codebase. Use this even when the user does not explicitly say "vibe coded" — any time they want guided learning of unfamiliar code, this skill applies. Do NOT use for designing new features, writing new code, or general coding help.
---

# Learn vibe-coded project

Guide the user through systematic understanding of a codebase they did not write themselves. Vibe-coded projects (built end-to-end by AI with no human code review) are common, and users often need to truly understand them for interviews, handoff, or production maintenance. This skill enforces a 3-phase walkthrough that respects the user's pace and prevents over-claiming.

## Why this skill exists

A user who tries to interview on or maintain code they have not read will get caught the first time someone asks "what does this project actually do?", "why did you choose this approach?", or "what happens when this fails?". The fix is not to read the whole repo end-to-end — it is to build a working mental model section by section, with concrete file references, explicit gap acknowledgment, and pre-built answers for the 6 axes interviewers actually probe: **business context, tech selection, code implementation, edge handling, fallback strategy, and the canonical knowledge ("八股") interviewers pivot to from your project.** This skill imposes that discipline so the user is never over-promised on what they "know".

## Three-phase workflow

Use the phases in order. Phase 1 runs once per project (or restarts on demand). Phase 2 runs in a loop (one file per turn). Phase 3 runs only when the user explicitly asks.

### Phase 1 — Project inventory + business overview (no source code yet)

**First, check for an existing progress file** (see "Progress persistence" below). If `<project-root>/.claude/learn-vibe-coded-progress.md` exists, read it and ask the user:

> 上次读到 **X 段** 的 `Y 文件`,接着读还是重来一遍 inventory?

If they choose to resume, skip the rest of Phase 1 and jump into Phase 2 at the next file. Otherwise, do a fresh inventory.

For a fresh inventory, read project-level documentation only. Do NOT open source files in this phase. Look for:

- `CLAUDE.md`, `AGENTS.md`, `README.md`, `README.zh.md` at the repo root
- A `docs/` directory and its index if present
- Project descriptor with intent: `pom.xml` (`<description>`), `package.json` (`description`), `pyproject.toml` (`description`), `Cargo.toml` (`description`), `go.mod` comments, etc.
- Progress / roadmap / plan documents — common names include `progress.md`, `STATUS.md`, `roadmap.md`, `plan.md`, `optimize-progress.md`, but the actual filename varies per project. **Use Glob to discover the real filename. Do not assume.**
- The user's per-project Claude Code auto-memory if present — the path is provided in the session's system prompt under an "auto memory" section. Read its `MEMORY.md` index and any files it points to.

**If you find zero project documentation** (no CLAUDE.md, no README, no docs/, no progress file, no auto-memory): say so plainly — "这个项目没有任何 doc,我会从源码结构推断"。Then switch to **structural inventory mode**: read top-level package layout (e.g., `src/main/java/<root>/` subdirs for Java, `src/` top-level for TS/JS, package layout for Python), look at the entry-point file (main / `Application.java` / `index.ts` / `app.py`), and infer capability sections from package names. Mark every entry in the capability map as ⚠️ "inferred from layout, no documentation confirmation" so the user knows the map is a guess.

#### Step A — 项目背景速览

Before drawing the capability map, summarize the project's business context in 3 short blocks. Pull from the documents you just read (README intro, CLAUDE.md TL;DR, project descriptor `description` field).

- **业务场景**: who uses this, what problem it solves, when / where / why it is used. 2-3 sentences. If docs only say "an X system" without naming users or use cases, say so plainly — "文档没写具体业务场景,只说是 X 系统,这点面试前要自己补一句合理的虚构 / 真实场景"。
- **技术栈一览**: language + version, primary framework + version, top 3-5 key dependencies (DB, vector store, LLM provider, frontend framework, message queue, etc.). One line per item.
- **架构形态**: monolith / microservices / agent system / library / CLI / hybrid + the major external integrations (databases, APIs, message queues, cron jobs, third-party services). 2-3 sentences.

Persist this overview to the progress file under a "Project overview" section so future sessions can re-display it without re-reading docs. When the user says "提醒一下这项目干啥的" / "what does this project do again" later, re-display this section verbatim, do not re-derive.

#### Step B — Capability map

From the same documents, build a **capability map** in this exact shape:

| 板块 | 完成度 | 核心文件路径 | 量化数字 |
|---|---|---|---|
| RAG 链路 | ✅ 完成 | `src/.../RagRetriever.java` | p90 -25%, Recall@5 = 0.94 |
| Multi-Agent | ⚠️ 进行中 | `src/.../agent/` (2/11 步) | — |
| 长期记忆 | ❌ 未做 | — | — |

Rules for the table:

- Use ✅ / ⚠️ / ❌ only — no other states.
- Only list capabilities the project documentation actually claims. Do not invent.
- If a doc claims a capability but you cannot find the implementation file, mark it ⚠️ and say so explicitly under the table.
- Order rows by interview value: strongest sections first, weakest or missing sections last.

After the table, ask the user which section to start with. **Stop and wait.** Do not start reading source files until the user picks one.

After the user picks, write the initial progress file (project overview + capability map + chosen section + empty file checklist).

### Phase 2 — Section walkthrough loop

When the user picks a section:

1. Use Glob/Grep to identify 3-7 core files for that section.
2. Decide a reading order: **entry point / orchestrator first, then drill into components, then helpers / config last.** Tell the user the planned file order so they know what is coming. Update the progress file with the file checklist.
3. Read **exactly one file per turn**. Output in this exact format:

```
## 文件 N/M:`<file path>`(<line count> 行)— <one-line role>

### 流水线全景
Where this file sits in the system. 1-3 lines. Name the entry points / call sites it connects to.

### 技术选型与设计决策(3-5 条)
**1. <Decision name>(line A-B)**
What the code does + why it is non-obvious / interview-worthy.
> 简历:"<one-sentence resume bullet — capability + quantification only, no narrative arc>"
**为什么选这个,不选 X / Y:** <对照其他方案的取舍 — 必须列至少一个被否决的备选 + 否决理由>

(repeat 2-5 times)

### 边界与兜底
- **边界**: <什么输入 / 状态会击穿这文件 — 空 / null / 超长 / 并发 / 超时 / 编码问题 / 重复请求>
- **兜底**: <降级路径 — fall back to X / retry policy / circuit break / 抛异常 with code>
- **监控点**: <metric 名称 或 log key,用户可以 grep / dashboard 找到的具体字符串>

### 八股延伸(interviewer 可能从这文件跳到的通用知识)
- **<Topic 1 — 一行话题名>**
  *骨架*: <1-2 句完整答案,面试现场可直接说出口,涵盖必提的关键词 + 一个 trade-off>
  *补课*: <具体资源 — 书的章节 / 论文标题 / 经典博客 URL,不要写 "google it">
- **<Topic 2>**
  *骨架*: <...>
  *补课*: <...>
- **<Topic 3>**
  *骨架*: <...>
  *补课*: <...>

### 模拟面试题(3 道,由浅入深)
**Q1:** <surface — 这文件是干啥的 / 算法是什么>
答:<answer hint with the key concept>

**Q2:** <intermediate — 设计权衡,为什么这样不那样>
答:<answer hint>

**Q3:** <deeper — failure mode / scaling 极限 / "如果 X 挂了">
答:<answer hint>

### ⚠️ 诚实警惕点
- <gap 1: where the code does NOT match what naming or docs imply>
- <gap 2: known hack / workaround / TODO an interviewer could spot>
- <gap 3: what the user should NOT claim if asked>
```

The 6 blocks map directly to the 6 interview prep axes:

| 块 | 对应面试维度 |
|---|---|
| 流水线全景 | 代码实现 |
| 技术选型与设计决策 | 技术选型(强制对比备选) |
| 边界与兜底 | 边界处理 + 兜底策略 |
| 八股延伸 | 引申八股(interviewer 从项目跳到通用知识) |
| 模拟面试题 | 综合演练 |
| ⚠️ 诚实警惕点 | 诚信底线 / 防穿底线 |

After the file, **stop and wait**. Do not auto-advance to the next file.

After each file, also update the progress file: mark the file done, set the next file in queue. Do this in the same turn as the response so the user can see the persistence happen.

Resume signals from the user: "继续" / "下一个" / "ok next" / a specific follow-up question on the current file. Anything else (including silence) means stop. If the user goes off-topic (e.g., asks an unrelated question), answer that question first and then ask whether to resume the walkthrough.

**Section completion behavior**: when the last file in a section is read and the user signals advance, do NOT silently jump into a new section. Instead output:

> ✅ <section name> 段读完了(N/N 文件)。回 capability map 看下一段,还是先停在这?

Then re-display the capability map with the just-completed section marked ✅. Wait for the user to pick the next section or stop. Update the progress file accordingly.

### Phase 3 — Mock interview (only when user explicitly asks)

Triggered by user phrases: "测一下" / "模拟面试" / "mock interview" / "考考我" / "interview me" / "quiz me" or equivalent.

Play a senior engineer interviewer. **Default to scenario-based questions** — they map most closely to mid-senior interview rounds at large tech companies, where interviewers want to see how the candidate makes architectural decisions under realistic constraints. Pure recall questions ("what is RRF?") are weak signal; scenarios force the candidate to reason from first principles and tie back to the code they actually read.

**Scenario question shapes** — pick one per question, vary across the session:

- **Scale extension**: "用户量从 1k QPS 涨到 10k QPS,你这个 RAG 链路要怎么改?"
- **Constraint flip**: "如果你们的 KB 不能用 pgvector,只能纯关系型 DB,Self-RAG 这套还能怎么落地?"
- **Failure storytelling**: "假设 rerank 服务今天挂了 30 分钟,你的告警 / 降级 / 复盘流程是什么?"
- **Trade-off forcing**: "RRF vs linear fusion vs Borda count,生产你会选哪个,为什么?"
- **Migration / refactor**: "现在 PM 要把这个项目从 Java 21 迁到 Go,你会保留哪些设计、推翻哪些?"
- **Knowledge pivot**: "够了,撇开你项目讲讲 cosine similarity 和 dot product 的本质区别,什么时候用哪个" — 模拟 interviewer 从项目跳到通用 CS / 系统设计 / 算法八股,verify 用户不是死记硬背。pivot 主题应当从 Phase 2 走过的"八股延伸"块里抽。
- **Business context probe**: "你这个项目最早是为谁做的?他们之前怎么解决这个问题?你的方案比他们好在哪?" — 测试 Phase 1 的项目背景速览到底吃透没。

For each scenario:

- Drop the user into the scenario in 2-3 sentences. Do **not** give them a structure ("first answer A, then B") — let them organize their own answer. The structure they pick is itself signal.
- Wait for the full answer. Do not coach mid-answer.
- Score on 4 axes: **(1) clarity of reasoning**, **(2) trade-off awareness**, **(3) reference to the actual code they read in Phase 2**, **(4) honesty about gaps**. Tell them which axes they nailed and which they whiffed.
- This is the right place for STAR-format narratives (Situation, Task, Action, Result) and root-cause debug stories. Coach the user to weave them in here, not on the resume.

**Fallback to direct questions** if the user explicitly asks ("just quiz me on what RRF is" / "考点知识"): then escalate surface → trade-off → failure-mode. Default is scenario-first.

End the mock when the user signals they are done.

## Progress persistence

The skill spans multiple sessions — a real project takes days to walk through. To avoid re-doing Phase 1 every session, persist progress to a markdown file.

**Location** — always project-local: `<project-root>/.claude/learn-vibe-coded-progress.md`. Create the `.claude/` directory under the project root if it does not exist. The first time the file is created, tell the user once: "建议把 `.claude/learn-vibe-coded-progress.md` 加到 `.gitignore`,这是个人学习进度不要 commit"。

**Do NOT write progress to the user-global `~/.claude/` directory** (i.e., `C:\Users\<user>\.claude\` on Windows or `/Users/<user>/.claude/` on macOS / Linux). That tree is reserved for user-level configuration, memory, and installed skills — not per-project state. Per-project learning progress belongs alongside the project code, in the project's own `.claude/`. Even when the session system prompt advertises an "auto memory" path under `~/.claude/projects/<hash>/memory/`, that is for cross-conversation user-style memory (preferences, role, feedback), not for tracking which file you read last in this project. Keep the two namespaces separate.

**File format** — strict markdown so both AI and human can scan it:

```markdown
# learn-vibe-coded-project — progress

Last updated: 2026-05-02T14:30
Project: <project-name>

## Project overview (snapshot from Phase 1 Step A)

**业务场景**: ...
**技术栈一览**: ...
**架构形态**: ...

## Capability map (snapshot from Phase 1 Step B)

| 板块 | 完成度 | 核心文件路径 | 量化数字 |
|---|---|---|---|
| RAG 链路 | ✅ 完成 | `src/.../RagRetriever.java` | p90 -25% |
| ...

## Section progress

- [x] RAG 链路 (5/5)
  - [x] RagRetriever.java
  - [x] RrfFusionMerger.java
  - ...
- [ ] Tool Use (0/4)
  - [ ] ToolRegistry.java
  - ...

## Current position

Section: Tool Use
Next file: ToolRegistry.java
Last finished: RrfFusionMerger.java (RAG 链路)
```

**When to read it**: at the start of every Phase 1, before reading any other doc.

**When to write it**:

- After Phase 1 completes (initial creation with project overview + capability map + chosen section).
- After every file walkthrough in Phase 2 (mark file done, set next file).
- After a section completes (mark section ✅ in the snapshot, ask user for next section).

**When NOT to write it**:

- During Phase 3 mock interviews — these do not change reading progress.
- If the user explicitly opts out ("don't track progress for this run").

## Hard constraints (apply across all phases)

1. **One file per turn in Phase 2.** Never read or summarize multiple files in a single response. The point is digestion, not coverage. If the user asks "just walk through the whole RAG section in one go", push back: explain that one-at-a-time is the only way they will actually retain it for an interview.

2. **Separate resume from interview.** Resume mode is triggered by user phrases like "写简历" / "for resume" / "resume bullets" / "简历怎么写" / "做简历" — switch to **bullet-only output**: capability statements and quantified metrics only, no narrative arcs like "we found a bug → fixed it → -25%". Save those root-cause stories for Phase 3 (mock interview), where they fit as STAR-format answers. Default mode (no resume trigger) is full walkthrough. The user already knows the stories exist; do not repeatedly re-pitch them across turns.

3. **Acknowledge gaps directly.** If a capability is missing, shallow, or in-progress, write it plainly — "this is not implemented", "Phase 1 in progress, 2/11 steps done", "lexical retrieval is ILIKE, not real BM25". The user is preparing for interviews where being caught lying is far worse than admitting a gap.

4. **User drives pace, AI drives explanation.** The user picks sections, picks when to advance, picks what to drill into. The AI delivers dense, file-grounded explanation on demand — it does not plan the curriculum unilaterally or auto-pick the next file.

5. **No hardcoded project-specific paths.** Different projects use different progress doc names, source layouts, and language conventions. Discover the real paths via Glob and the project's CLAUDE.md / README each time. Never carry assumptions across projects.

6. **Cite line numbers for every claim.** When highlighting a design decision, cite ranges (`line 188-206`). The user must be able to verify each claim against the file. If you cannot point to specific lines, you cannot make the claim.

7. **Use honest tech terms, not marketing words.** If lexical retrieval uses ILIKE, say ILIKE — not "BM25-style hybrid". If "memory" is just per-session history with no persistence, say "session-scoped chat history". Interviewers ask follow-ups, and the user needs ground truth, not a pitch.

8. **Tech selection always names a rejected alternative.** Every entry in the "技术选型与设计决策" block must name at least one alternative that was considered and the reason it was rejected. "We chose X" without "instead of Y because Z" is half an answer — interviewers ask "why not Y" every time. If the code does not reveal the rejected alternative, infer the obvious industry alternative (e.g., RRF → linear fusion / Borda count; pgvector → Pinecone / Weaviate / FAISS) and frame it as "the obvious alternative would have been Y; this codebase chose X, likely because ...".

9. **八股 skeleton answers are full sentences, not keyword lists.** A skeleton like "BM25, IDF, length normalization" is useless — the user cannot read it aloud in an interview. Write "BM25 在 TF-IDF 基础上加了文档长度归一化(b 参数控制)和词频饱和度(k1 参数控制),适合关键词匹配类查询;不适合语义相近但词不同的场景" — a complete spoken sentence that hits the must-mention keywords and one trade-off.

## Common failure modes to avoid

- **Reading too much code in one turn.** Tempting because "let me show you the whole RAG pipeline" feels efficient — but the user cannot absorb 5 files at once. One file. Stop. Wait.
- **Skipping Phase 1.** Diving into source files before reading docs leaves the user without the map. Always do the inventory first, even if the user is impatient — unless the progress file says they already did it.
- **Skipping the project overview (Step A).** Going straight to the capability map without summarizing what the project does means the user cannot answer "tell me about your project" in an interview. Step A is not optional.
- **Forgetting to write progress.** New session starts → user expects to resume from where they stopped → progress file is missing → frustration. Always write after each file.
- **Listing alternatives without rejection reason.** "We considered X and Y" is not an answer; "we chose X over Y because Y has problem Z" is. Every tech selection must name the reject + reason.
- **八股 skeleton written as keyword list.** See hard constraint #9 — must be full speakable sentences.
- **Resume bullets that read like interview stories.** "Caught a silent bug via eval and shipped a fix" is a story, not a bullet. The bullet form is "Built end-to-end eval harness with Recall@K / MRR / nDCG metrics; identified and resolved fusion-score scaling defect; p90 latency reduced 25%".
- **Hiding the gaps.** If multi-agent is "Phase 1, 2/11 steps done", say that. Do not write "designed multi-agent system" as if it shipped.
- **Re-pitching the same narrative.** Once the user has acknowledged they know about a story (a debug arc, an A/B comparison, etc.), do not keep recommending it as resume material in subsequent turns. They know. Move on.
- **Mocking the interview without being asked.** Phase 3 is opt-in only. Do not surprise the user with "let me quiz you" — wait for an explicit trigger.
- **Auto-advancing across sections.** When a section finishes, stop and ask. Don't silently start the next section's first file.
