---
name: resume-architecture-coach
description: Use when the user wants to understand, explain, rehearse, or rewrite a resume/project architecture bullet by mapping it to source code, first-principles tradeoffs, interview language, or follow-up questions. Trigger on requests like “讲一下简历这一点”, “根据源码解释项目”, “从第一性原理分析这个架构点”, “这个项目点面试怎么讲”, or similar.
---

# Resume Architecture Coach

## Overview

Turn a resume bullet into a source-backed project explanation, an interview-ready answer, and a follow-up question set.

**Iron law:** Never speak as if a claim is verified unless you actually checked the code or were given the implementation details. If something is inferred rather than verified, say so plainly.

## When To Use

Use this skill when the user:

- wants to understand a project bullet from their resume
- wants to map a resume phrase to real code or system behavior
- asks how to explain a backend/system design point in an interview
- asks whether a resume bullet is accurate, too strong, or needs rewriting
- asks for a first-principles explanation of a project architecture choice

Typical prompts:

- “讲一下简历这一点在项目中的体现”
- “根据当前仓库解释我简历上的 Feed 流”
- “这个项目点面试怎么说”
- “帮我判断这条简历会不会写得太超前”
- “只有这条简历，没有源码，你帮我从第一性原理推”

Do not use this skill for generic code changes, bug fixing, or pure product brainstorming that is unrelated to a resume/project bullet.

## Default Output

Unless the user asks for a narrower output, produce these three parts:

1. `项目讲解稿`
2. `面试回答稿`
3. `高频追问清单`

If you discover a mismatch between resume wording and implementation reality, add a fourth optional part:

4. `真实性校准与改写建议`

## Modes

Choose one of two modes first.

### Mode A: Resume Bullet + Repository/Source Available

Use this when the user gives a local repo, file paths, screenshots of a resume bullet plus a codebase, or explicitly asks for a source-backed explanation.

Required behavior:

- inspect the code first
- identify the exact files, classes, configs, or data flow that support the bullet
- separate `verified` facts from `reasonable inference`
- prefer local source over memory

### Mode B: Resume Bullet Only

Use this when the user only gives the bullet text, project summary, or interview context without source code.

Required behavior:

- explain from first principles
- state assumptions clearly
- mention what would need verification if source code later becomes available
- avoid pretending the guessed architecture definitely exists

## Workflow Checklist

- [ ] Step 1: Extract the exact resume bullet or architecture point
- [ ] Step 2: Identify the hidden claim behind the bullet
- [ ] Step 3: Decide whether this is `source-backed mode` or `inference mode`
- [ ] Step 4: If source-backed, inspect code before explaining
- [ ] Step 5: Rebuild the design from the simplest possible baseline
- [ ] Step 6: Add real-world requirements one by one
- [ ] Step 7: For every introduced mechanism, compare `not adding it` vs `adding it`
- [ ] Step 8: Map the final chain back to the resume wording
- [ ] Step 9: Translate jargon into plain language
- [ ] Step 10: Produce the default output trio
- [ ] Step 11: If needed, calibrate whether the resume wording is too strong, too weak, or accurate

## Step 1: Extract The Hidden Claim

A resume bullet usually compresses several claims into one line.

For each bullet, identify:

- what core business action it is about
- what non-functional pressure is implied
- what architectural mechanism is being claimed
- what interview-level value is being promised

Example:

- `采用 Outbox + Canal + Kafka 异步更新` is not just a tool list
- the hidden claim is: “I had a cross-datasource consistency problem and used an event pipeline to avoid lost updates and reduce coupling”

## Step 2: Inspect Source First When Available

If code is available, build an evidence map before explaining.

Look for:

- controller/API entry points
- service layer orchestration
- persistence layer and schema-related code
- cache keys, MQ producers/consumers, listeners, schedulers
- config files that reveal TTLs, rate limits, topics, or retry policies
- comments that expose design intent

When reporting findings:

- cite the main files or modules that prove the claim
- do not dump file inventories
- mention only the components that matter to the architecture story

## Step 3: Rebuild From First Principles

Always start from the dumbest version of the system.

Good starting questions:

- If we used only the database, what would the implementation look like?
- If we had only one machine, what would be simplest?
- If we ignored concurrency, consistency, or latency, what would we do first?

Then add one requirement at a time:

1. traffic gets bigger
2. latency expectations get tighter
3. writes become concurrent
4. data must stay consistent across multiple stores
5. cache invalidation becomes hard
6. failures and retries become real

This keeps the explanation grounded in engineering necessity instead of tool worship.

## Step 4: For Every Mechanism, Compare “Without” And “With”

For each introduced pattern, always explain three things:

### A. If we do not add it

State the concrete pain:

- database gets hammered
- duplicate writes appear
- cache becomes stale
- updates get lost
- retries become unsafe
- one hot key drags the whole system down

### B. After we add it

State what improves:

- fewer repeated reads
- shared cache across instances
- only one request rebuilds a cache entry
- events can be retried without corrupting state
- hot data survives longer

### C. New cost introduced

Never present mechanisms as free:

- more moving parts
- harder debugging
- eventual consistency instead of immediate consistency
- more state to clean up
- more careful invalidation logic
- more operational parameters to tune

This is what makes the explanation sound like real backend experience.

## Step 5: Translate Jargon Into Human Language

Whenever you use a term, immediately make it intuitive.

Preferred pattern:

- technical name
- one-line plain explanation
- one short metaphor or scenario

Examples:

- `Outbox`:
  write business data and the “to-be-sent event” in the same database transaction, so you do not end up with “data changed but message never sent”
- `Canal`:
  a binlog watcher that acts like a courier staring at MySQL change records and forwarding them downstream
- `single-flight`:
  when the cache misses, let one request do the rebuild work and let the others wait instead of all stampeding the database
- `hotkey detection`:
  notice that a few pages or items are being hit far more than the rest, then protect those keys more aggressively

Do not stack jargon without translation.

## Step 6: Map Back To The Resume Wording

After the first-principles chain is complete, explicitly map each resume phrase to the problem it solves.

Use this pattern:

- `resume phrase`
- what problem forced it to appear
- where it shows up in code or, if no code, what implementation shape would prove it

This is the point where the bullet stops being a slogan and becomes an explainable system.

## Step 7: Produce Interview-Friendly Deliverables

### Deliverable 1: 项目讲解稿

Use a calm, teaching-style walkthrough.

Recommended structure:

1. what the feature or architecture point is solving
2. the naive baseline
3. why the baseline breaks
4. what mechanisms were added and in what order
5. what tradeoffs were accepted
6. how this corresponds to the resume line

### Deliverable 2: 面试回答稿

Default to a compact spoken answer, usually 30-90 seconds.

It should sound like:

- the speaker actually built or deeply understood the system
- not like they memorized a glossary
- concrete enough to survive one or two follow-up questions

If helpful, provide two versions:

- `简短版`
- `展开版`

### Deliverable 3: 高频追问清单

Generate likely interviewer follow-ups such as:

- Why not use a simpler design?
- What consistency model did this create?
- What breaks if the middleware is removed?
- How did you avoid stale cache or duplicate writes?
- What was the operational cost?
- Which parts are synchronous and which are asynchronous?

For each follow-up, give a brief answer direction, not just the question.

## Step 8: Authenticity Calibration

Check whether the resume bullet is:

- `fully supported`
- `supported but slightly overstated`
- `partially supported`
- `mostly inferred and should be softened`

If the wording is too strong, suggest a safer rewrite.

Examples of overstatement to watch for:

- saying `strong consistency` when the code is clearly eventual consistency
- saying `immediate revocation` when only refresh-token revocation exists
- claiming a middleware-driven architecture when the code only has simple helper usage

Be honest but constructive.

## Output Template

Use this template unless the user asks for a different format:

```markdown
**项目讲解稿**
[Source-backed or inference-marked explanation]

**面试回答稿**
[30-90 second spoken answer]

**高频追问清单**
1. [Question]
[Answer direction]
2. [Question]
[Answer direction]

**真实性校准与改写建议**
[Only include when needed]
```

## Tone Rules

- explain like you are helping a capable developer understand distributed/backend tradeoffs for the first time
- use plain language first, terms second
- do not flex by listing middleware without purpose
- do not turn simple explanations into academic essays unless the user asks for depth
- if source exists, anchor the explanation in source
- if source does not exist, label assumptions clearly

## Anti-Patterns

Avoid these mistakes:

- starting with the final architecture instead of the naive baseline
- naming tools without explaining the pressure that forced them in
- pretending inferred details were verified from source
- giving only “what it is” and skipping “why it exists”
- speaking in resume prose instead of interview prose
- ignoring tradeoffs and only describing benefits
- overwhelming the user with file-by-file recitation

## Final Check

Before finishing, verify:

- Did I clearly say whether the explanation is source-backed or partly inferred?
- Did I start from the simplest possible system?
- Did I add requirements one by one instead of jumping to the final design?
- Did I compare not adding vs adding each major mechanism?
- Did I map the logic back to the resume wording?
- Did I produce the default output trio?
- Did I flag overstated resume wording if necessary?
