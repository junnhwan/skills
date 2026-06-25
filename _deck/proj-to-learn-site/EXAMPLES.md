# EXAMPLES — proj-to-learn-site

## Worked example: BondCode (Go, local-first TUI Coding Agent Runtime)

Resume project the user wanted to understand + prep for interview grilling. They had stale prep docs but **hadn't read their own source**.

### Scoping → 8 chapters (expanded from initial 4)
From `CLAUDE.md` (which names `internal/app/bootstrap.go` as the wiring truth source). The first 4 chapters cover the core loop; s05-s08 cover the advanced mechanisms that make BondCode a *real* agent runtime, not just a while-loop:
- s01 Agent Loop 与不变量 (`internal/agent/loop.go`)
- s02 工具分发与 Envelope (`internal/tool/*`)
- s03 安全模型与拦截 (`internal/safety/*`)
- s04 上下文四层治理 (`internal/contextx/*`)
- s05 Subagent 与隔离执行 (`internal/subagent/*`)
- s06 Orchestrator 多 Agent 编排 (`internal/orchestrator/*`)
- s07 Hook 生命周期扩展 (`internal/hook/*`)
- s08 System Prompt 构造与 Plan Mode (`internal/agent/prompt_context.go` + `internal/app/app.go`)

> **Scoping tip**: 4 chapters = "the loop works". 8 chapters = "it's a production agent". For interview prep, the delegation/orchestration/extensibility chapters (s05-s08) are where the hardest "架构权衡" and "横向对比" questions live — don't skip them if the project has these mechanisms.

### LAYERS (5-layer sidebar, by project type = Agent Runtime)
```ts
LAYERS = [
  { id: "tools", label: "Loop · Tools · Safety", versions: ["s01","s02","s03"] },
  { id: "memory", label: "Context Governance", versions: ["s04"] },
  { id: "concurrency", label: "委托 · 编排", versions: ["s05","s06"] },
  { id: "collaboration", label: "可扩展性", versions: ["s07"] },
  { id: "planning", label: "Prompt · 规划", versions: ["s08"] },
];
```

### Viz remapping (by mechanism)
```ts
const visualizations = {
  s01: lazy(() => import("./s01-agent-loop")),      // while-loop + messages[]
  s02: lazy(() => import("./s02-tool-dispatch")),   // registry + envelope
  s03: lazy(() => import("./s03-permission")),      // policy + confirmer
  s04: lazy(() => import("./s06-context-compact")), // 4-layer pipeline
  s05: lazy(() => import("./s04-subagent")),        // subagent isolation + profile
  s06: lazy(() => import("./s09-agent-teams")),     // orchestrator DAG
  s07: lazy(() => import("./s04-hooks")),           // lifecycle mount points
  s08: lazy(() => import("./s10-system-prompt")),   // prompt builder + plan mode
};
```

### Discrepancy flagged (the whole point)
User's `bondcode-project-prep.md` said "medium 风险走确认". **Actual `policy.go`**: `low` AND `medium` both → `Allow` (auto-execute); only `high` → `ConfirmHigh`; dangerous commands hard-`Block` first. Surfaced to user, corrected in the tutorial so they don't memorize the wrong thing.

### Real values captured into content (verified from source)
- Loop: `MaxSteps=16` (bootstrap), `MaxRepeatedToolCalls=3`, `MaxToolCallsPerStep=8`; **invariant**: `executeTool`'s 6 error paths all `return` a `*tool.Result` so tool-use→tool-result pairing never breaks.
- Safety: deny rules in `command_guard.go` (sudo, rm -rf /, mkfs, dd of=/dev/, fork bomb, curl|sh, find /, chmod -R 777 /, shutdown); `--yes` = `AutoApproveConfirmer{MaxRisk:"medium"}` (can't bypass high or Block).
- Context governor defaults: `MicroCompactKeepRecent=10`, `MicroCompactMinChars=500`, `ToolResultBudget=8000`, `ToolResultPreviewChars=2000`, `ToolResultTurnBudget=16000`, `MaxTokens=100000`; 4 layers L0(pairing)→L1(micro-compact)→L2(budget/spill)→L3(snip at turn boundary) + L4(LLM summary, degrades to rules).

### Sample 面试拷打 (s01, upgraded with 3-tier structure)

#### 🟢 基础理解
**Q1: 这不就是 while True 调 API 吗？**  
答：不是；循环是骨架，难在协议不变量(6 异常路径兜底)、loop guard、每轮上下文治理、step-budget 收尾、reactive 压缩。
> ⚠ 别这么说："就是一个 while 循环调模型"（会让面试官觉得你只看到表面）

#### 🟡 深入追问
**Q2a: 工具执行抛 error 链路会断吗？**  
答：不会；`emitToolError(...StatusError...)` 包成 Result 回填（`loop.go:287`），配对完整。

**Q2b: 追问：超时的工具还会配对吗？**  
答：会；timeout 在 `executeTool` 内捕获（`tool/executor.go:156`），包成 `tool.Result{Status: Timeout}`，依然返回 Result 而非 panic。

#### 🔴 架构权衡
**Q3: 为什么不异步并发执行多个工具？**  
答：简化配对不变量（`loop.go:45` 注释："sequential execution ensures tool_use/result pairing never breaks"）；并发收益有限（大部分工具是 I/O 等待，LLM 才是瓶颈）；错误追踪成本高（并发时难以判断哪个 Result 对应哪个 Call）。
> 💡 这题拷你有没有想过"为什么不这样优化"

#### 🧩 反向溯源
**场景：用户报告"同一个 grep 命令执行了 3 次"**  
答：`loop.go:112 MaxRepeatedToolCalls=3` → 当 LLM 连续输出相同 tool_use 时触发 retry（`detectRepeatedCall` 在 `loop.go:203`）；如果 3 次都相同会 break 并返回错误。

#### ⚖️ 横向对比
**Q: 这个 loop 和 LangChain 的 AgentExecutor 有什么本质区别？**  
答：BondCode 强制 tool-use/result 配对不变量（6 个异常路径兜底），LangChain 允许 agent 自由返回 finish；BondCode 有 4 层上下文治理（micro-compact + budget + turn-boundary + LLM summary），LangChain 只有简单 memory window。

### Result
- Copied `learn-claude-code/web` → `bond-code/docs/site`, npm install, `npx next dev` boots in ~700ms.
- Hand-authored `constants.ts` (8 versions, 5 layers), `versions.json` (8 AgentVersion + 7 diffs), `docs.json` (8 markdown chapters w/ 3-tier grill), `scenarios/s01..s08.json`.
- `validate-content.mjs`: ✓ consistent (versions↔docs↔scenarios↔viz aligned).
- `next build`: ✓ 0 errors, 64 static pages.
- Playwright: 0 console errors on all chapters; learn/simulate/code tabs render; simulator plays BondCode scenarios.
- **Bug found & fixed during validation**: simulator `scenarioModules` hardcoded s01-s20 imports → 30 errors on chapter expansion. Fixed by trimming to VERSION_ORDER. (See REFERENCE.md § 7-8.)

### Lesson for future runs
1. The single highest-value step is **Phase 3 (deep read) + discrepancy flagging** — the user's prep docs are the thing most likely to be wrong, and wrong memorization is worse than not knowing.
2. **Chapter count is a first-class variable.** When you pick N chapters, N must propagate everywhere: `VERSION_ORDER`, LAYERS, `versions.json`, `docs.json`, scenarios dir, viz `index.tsx`, AND the simulator `scenarioModules` import map (easy to miss → 500 on every page).
