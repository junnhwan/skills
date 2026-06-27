# Interview Grill Mode

Use this reference when the deck is for project interviews, resume defense, "拷打", AI-coded projects, or unfamiliar code the user needs to explain under pressure.

## Core Goal

The deck should prepare the user to be questioned, not just impressed. Every technical highlight needs:

- A source-backed claim.
- A safe interview wording.
- A likely follow-up question.
- A failure/concurrency edge case.
- A boundary: what not to volunteer.

When `resume.md` or a final resume draft exists, the resume becomes the spine of the deck. Do not let the source-reading summary choose only the most interesting modules. Extract every resume bullet, map it to code evidence, then generate the questions an interviewer can ask from that exact wording.

## Resume-Driven Drill Workflow

1. Find resume sources in this order: root `resume.md`, `docs/resume*.md`, `docs/*resume*.md`, `docs/*interview*.md`, then README claims.
2. Identify the latest/final resume version by heading names such as `v0.3.0`, `最终`, `final`, or explicit user preference. If unclear, state which file/version was used.
3. Split every project bullet into atomic claims: technology, scenario, mechanism, data structure, failure handling, result, metric, and boundary.
4. For each atomic claim, classify it as `Verified`, `Inferred`, `Unsupported`, or `Do not volunteer`.
5. For each resume bullet, create a question tree:
   - Entry: broad explanation questions.
   - Mechanism: how the code path actually works.
   - Alternatives: why not a simpler option.
   - Failure: what if the dependency or step fails.
   - Concurrency/idempotency: duplicate click, retry, repeated MQ delivery, race conditions.
   - Data/security: ownership, privacy, keys, isolation, cleanup.
   - Scale/performance: what can be said without invented benchmarks.
   - Boundary: what not to claim and how to admit gaps.
6. Add a final "red-team pass" slide: questions meant to expose overclaiming, AI-generated-code dependence, missing tests, fake metrics, or production-readiness gaps.

## Required Slides

| Slide | Purpose |
| --- | --- |
| Project defense one-liner | Explain the project in one sentence with real business/learning pain. |
| Claim vs code matrix | Separate implemented facts, inferred facts, and unsupported resume claims. |
| Resume bullet map | List every resume bullet with evidence files, risk level, and first safe answer. |
| Resume question tree | For each resume bullet, include entry questions, deeper follow-ups, and danger zones. |
| Highlight ranking | Rank 3-5 technical points by interview value and user's likely depth. |
| AI coding ownership | Prepare an honest answer to "was this AI-written?" with concrete review/debug examples. |
| Deep-dive flow | For each main highlight, show pain -> tradeoff -> implementation -> evidence path. |
| Grill Q&A | Include interviewer psychology, first-person answer, and follow-up trap. |
| Failure playbook | Answer "what if X fails?" with current code behavior, not generic wishes. |
| Do-not-say list | Mark risky claims, missing evidence, and topics the user should not主动展开. |

## Five-Layer Slide Adaptation

For one technical highlight, compress the project-grill five-layer structure into 2-4 slides:

1. Background pain: the reasonable old/simple approach and why it fails.
2. Tradeoff: alternatives considered, why current project chose this route, and where it is weaker.
3. Implementation flow: call path, data structures, state transitions, error branches.
4. Interview Q&A: likely questions, interviewer psychology, answer, and evidence path.
5. Failure scenario: dependency failure, retry/idempotency/concurrency, user-visible result.

## Question Card Format

Use concise cards instead of long prose:

| Field | Content |
| --- | --- |
| Q | The exact interviewer question. |
| 心理 | What the interviewer is actually testing. |
| 答法 | First-person answer the user can say out loud. |
| 证据 | File/function/table that proves the answer. |
| 追问 | One harder follow-up and the safe boundary. |

## Resume Bullet Question Tree Format

Use this compact structure when the deck is based on a resume:

| Field | Content |
| --- | --- |
| 原句 | The exact resume bullet or the shortest faithful paraphrase. |
| 面试官入口 | 2-3 questions likely asked immediately from the wording. |
| 连续追问 | 4-8 deeper questions covering mechanism, tradeoff, failure, concurrency, data, and tests. |
| 安全回答 | One first-person 20-40 second answer. |
| 证据 | Files/functions/tables proving the answer. |
| 危险边界 | Claims that are tempting but unsupported. |

The user should be able to rehearse from the slide without opening another document.

## Depth Calibration

Label each highlight:

| Depth | Meaning | Deck behavior |
| --- | --- | --- |
| Green | Can explain principle and code path | Include deeper internals and tradeoffs. |
| Yellow | Can explain why/how but not internals | Keep answers at design and usage level. |
| Red | Only knows the feature exists | Mark as "know only, do not volunteer". |

If the user's depth is unknown, default to Yellow and include diagnostic questions.

## Common Interview Traps

- "Why not the simpler synchronous solution?"
- "What happens if Kafka/Redis/MinIO/Milvus/AI provider is down?"
- "How do you avoid duplicate processing?"
- "Where is the idempotency boundary?"
- "What did you personally decide instead of AI?"
- "What is implemented now vs future work?"
- "What data supports your performance claim?"
- "This bullet says X. Point me to the exact code path."
- "What would break if two users or two consumers hit this path at the same time?"
- "Which part of this bullet was actually measured, and which part is design intent?"

Never invent performance numbers. Use `[需要压测获取]` when no benchmark or report exists.
