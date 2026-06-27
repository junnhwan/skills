# Source Reading Workflow

Use this workflow before authoring the HTML deck.

## 1. Map The Repository

Run fast inventory commands from the project root:

```bash
rg --files
```

Then read only high-signal files first:

- README, docs, examples, env samples.
- Package/build files: `package.json`, `pnpm-lock.yaml`, `vite.config.*`, `next.config.*`, `pyproject.toml`, `requirements.txt`, `Cargo.toml`, `go.mod`, Docker files.
- Entry points: `src/main.*`, `src/App.*`, `app/layout.*`, `pages/*`, `server.*`, `index.*`, CLI entrypoints.
- Route/API definitions, database schema, model/prompt/tool/RAG files.

## 2. Identify Project Type

Classify the project by behavior, not by framework name:

- Frontend app: route tree, state management, API clients, UI component boundaries.
- Backend/API: endpoints, middleware, services, persistence, external integrations.
- Full-stack app: browser-to-server flow, shared types, auth/session boundaries.
- AI app: model calls, prompt construction, tools/functions, memory, RAG, evals.
- CLI/automation: command parser, task graph, filesystem/network side effects.

## 3. Trace One Primary Flow

Pick the user-visible flow that best explains the project. Trace it end to end:

1. User action or external trigger.
2. Entry component/route/command.
3. State or request construction.
4. API/service/model/database call.
5. Output rendering or side effect.

Record file paths and function/class names for each step. If the trace is uncertain, say what is inferred and what remains unverified.

## 4. Extract Deck Content

Create a source-backed outline before editing HTML:

- Project purpose in one sentence.
- Stack map with each technology's role.
- Directory map with important and ignorable areas.
- 6-12 key files with responsibilities.
- Primary runtime/data/request flow.
- AI-specific layer if present.
- Risks, unclear areas, and missing tests.
- Recommended reading order and first safe tasks.

For interview-grill use, also extract:

- Resume/user claims if present, starting with root `resume.md`. If multiple versions exist, identify the version used and why.
- Every resume bullet as a claim tree, not just a generic highlight list. Split technology names, mechanisms, data structures, results, and metrics into separately verifiable claims.
- Whether each claim is verified, inferred, unsupported, or a do-not-volunteer overclaim.
- 3-5 defensible technical highlights, ranked by interview value.
- Diagnostic questions that expose whether the user understands each highlight deeply.
- Failure scenarios and current code behavior for each highlight.
- "Do not say" items: tempting claims that the code does not fully support.
- Code anchors for rehearsal: file path, function/type/table name, and the reason that file proves the claim.

For each resume bullet, prepare at least these question categories:

| Category | Example pressure |
| --- | --- |
| Entry | "Explain this bullet without listing technologies." |
| Mechanism | "Walk me through the exact code path." |
| Alternative | "Why not synchronous/goroutine/local disk/MySQL LIKE?" |
| Failure | "What happens if Kafka/Redis/MinIO/Milvus/AI provider fails?" |
| Concurrency | "What if the request is duplicated or two consumers handle the same task?" |
| Data/security | "How do you isolate user data, keys, files, and RAG chunks?" |
| Measurement | "Do you have benchmark data, or is this a design claim?" |
| Boundary | "What is not implemented yet?" |

## 5. Vibe Coding Project Heuristics

Vibe-coded projects often contain working UI with uneven architecture. Look for:

- Dead components, duplicated helpers, unused API routes, and inconsistent naming.
- Hard-coded API keys, prompt text in components, or environment variables read in multiple places.
- Missing loading/error/empty states.
- Thin wrappers around model calls with no timeout, retry, or structured output validation.
- Generated-looking files that are large and mixed-responsibility.
- README instructions that no longer match package scripts.

Do not shame the code. The deck should help the owner understand what exists and where to intervene.

## 6. Evidence Standard

Use one of these confidence labels in notes or risk slides when needed:

| Label | Meaning |
| --- | --- |
| Verified | Directly confirmed in source or by running a command. |
| Inferred | Strongly suggested by file names or call paths, not fully executed. |
| Unknown | Not enough local evidence. State what would confirm it. |

If running the app or tests would take setup, still produce a useful source-reading deck, but report verification gaps plainly.
