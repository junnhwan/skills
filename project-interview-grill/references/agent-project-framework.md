# Agent Project Grilling Framework

Use this reference only for Agent, Coding Agent, LLM tool, MCP, memory, planning, context, or multi-agent projects.

## Core Defense Pattern

For every Agent capability, prepare:

`user request -> model stream -> tool call -> safety decision -> tool execution -> tool result envelope -> next model call -> final answer -> audit trace`

If one step is not implemented, say where the current project stops.

## Claim Boundary Checklist

### Agent Loop

Ask:

- What is one full loop iteration?
- What happens when the model emits multiple tool calls?
- What stops infinite tool use?
- What happens on invalid JSON, unknown tool, user rejection, blocked command, or tool error?

Evidence to seek:

- loop implementation
- event stream
- loop guard tests
- tool-call integration tests

### Tool Calling

Ask:

- Is the project using structured tool calls or parsing natural language?
- How are tool results returned to the model?
- Does the result include status, summary, output, error, and metadata?
- How does it preserve provider protocol rules such as tool-use/tool-result pairing?

Good resume wording:

> 基于结构化 tool call 设计统一工具执行链路，模型输出工具调用后由 registry 分发执行，并将标准化 tool result 回填给模型，降低自然语言解析工具意图的不确定性。

### Context Management

Ask:

- Is context management automatic before every model call?
- What gets protected from compaction?
- How are oversized tool outputs handled?
- Is there LLM summarization or deterministic truncation only?
- Does local full history remain, or is history permanently lost?

Boundary wording:

- "deterministic governor" is not the same as "semantic LLM memory compression".
- "tool output spill/preview" is not the same as "full retrieval over archived outputs".

### Memory

Ask:

- Where is memory stored?
- Is memory automatically extracted, explicitly saved by the model, or manually updated?
- Is memory injected into system prompt, user message, or retrieved by a tool?
- Is it long-term memory, session memory, or just current context?

Boundary wording:

- If the model must call `save_memory`, say "tool-mediated memory".
- Do not call it autonomous preference learning unless extraction is automatic and tested.

### Planning

Ask:

- Is there a separate Plan Mode UI or a todo/task tool?
- How are tasks persisted?
- Is task state injected into the prompt?
- What prevents the model from doing long work without a plan?

Boundary wording:

- Todo tools plus prompt reminders are not a full Plan Mode unless there is a distinct planning/execution mode and user-visible approval flow.

### Subagents

Ask:

- Is the subagent synchronous and returns a result, or background fire-and-forget?
- Can subagents recurse?
- Which tools are removed from child agents?
- How are child results returned to the parent conversation?
- What happens on timeout or failure?

Boundary wording:

- "task subagent" is safe when a result is returned.
- "multi-agent parallel collaboration" is risky unless parallel execution, result aggregation, cancellation, and isolation are all implemented.

### MCP

Ask:

- Is MCP enabled by default?
- Which transport is supported?
- Are tools injected into the main tool registry?
- Are resources and prompts supported?
- How are external tools namespaced and risk-classified?

Boundary wording:

- "MCP stdio MVP" is safer than "complete MCP ecosystem".
- "config-gated tool injection" is safer than "default MCP support".

### Safety

Ask:

- What are the risk levels?
- What does auto-approval actually approve?
- Which commands are blocked regardless of approval?
- How are high-risk operations confirmed?
- Is safety enforced in the Agent Loop or only the UI?

Strong answer anchor:

> Safety is part of the runtime execution path, not just a TUI prompt. The agent decides risk before executing a tool, then either allows, requests confirmation, requires high-risk confirmation, or blocks.

### Session Trace

Ask:

- What events are persisted?
- Can a session be listed and replayed?
- How does this help debug hallucinated tool calls, rejected tools, or context compaction?
- Why JSONL instead of a database?

Good answer anchor:

> JSONL fits a local-first CLI because it is append-only, readable, simple to inspect, and enough for audit/debug without adding database operations.

## Demo Checklist For Agent Projects

Prefer one sustained interactive run:

1. Start the normal TUI/chat path with the real model.
2. Check status/model/tools.
3. Ask the model to read or search a real file.
4. Ask it to save and read memory.
5. Ask it to create a todo plan.
6. Ask it to delegate a research task to a subagent.
7. Trigger a permission confirmation with a medium-risk action.
8. Inspect session trace after exit.

For each step, record expected visible signals: tool card, permission panel, session JSONL event, memory file, task file, or context update event.
