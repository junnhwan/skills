# CHANGELOG — proj-to-learn-site

## 2026-06-25b: 可视化布局问题修复 🔧

### 🐛 修复的问题
1. **文字溢出节点框** — label 包含过多文字或 3 行换行导致挤压
2. **节点几乎不可见（幽灵节点）** — `appearsAt: 2+` 导致前面步骤透明度只有 16%
3. **箭头混乱/穿刺** — 节点间距过小（<140px 垂直）+ focus 数组不完整
4. **节点拥挤重叠** — 垂直间距只有 110px（应为 140px+）

### ✅ 改进内容

**代码修复（bond-agent-loop-flow.tsx 示例）：**
- viewBox 从 `760×420` 扩大到 `1120×520`（+47% 画布）
- 主流程垂直间距从 110px 增大到 140px（+27%）
- label 精简：`"LLM Stream"`（单行）替代 `"LLM\nStream"`（多行挤压）
- 异常节点 `appearsAt: 1`（早出现）替代 `appearsAt: 2`（晚出现 → 幽灵）
- 步骤 2 的 focus 数组增加 `"pair"` 节点，确保端点也高亮

**文档增强（REFERENCE.md）：**
- § 4.1：新增**节点尺寸规范**（矩形 118×42px、菱形 54×54px）+ **安全间距规则**（垂直 140px、水平 200px）
- § 4.1：新增**Label 文字限制**（≤10 中文字/行，最多 2 行）+ **appearsAt 可见性指南**
- § 8：新增**常见布局问题排查章节**（5 种症状 + 原因 + 修复 + 验证 checklist）

**SKILL.md 快速提示：**
- Phase 4 下方增加醒目的 🔧 布局问题速查框，包含 Quick fix 模板

### 📚 使用建议
- 新项目：直接参考 REFERENCE.md § 4.1 的预设布局模板（垂直流/分支流/DAG）
- 旧项目修复：运行 REFERENCE.md § 8 的"快速验证 checklist"，逐项排查

---

## 2026-06-25a: Interview-focused upgrade

### ✨ New: 3-tier interview Q&A structure

**Before**: flat 3-6 Q&A list  
**After**: 5-layer structured interview grilling

- 🟢 **基础理解** — must-answer fundamentals (1-2 questions)
- 🟡 **深入追问** — follow-up chains (Q2a → Q2b, 2-3 questions)
- 🔴 **架构权衡** — "why not X?" design tradeoffs
- 🧩 **反向溯源** — given a bug symptom, trace to code cause
- ⚖️ **横向对比** — vs open-source frameworks (LangChain, etc.)

Each layer with "⚠ 别这么说" anti-pattern.

**Files updated**:
- `REFERENCE.md § 5`: new per-chapter markdown template with all 5 layers
- `EXAMPLES.md`: BondCode s01 example rewritten with full 3-tier structure
- `SKILL.md`: updated description + "Three non-negotiables" #3

### ✨ New: Project type templates

**Before**: one-size-fits-all Agent Runtime layout  
**After**: 5 project types with custom sidebar layers

`bootstrap-site.sh` now prompts:
1. Agent Runtime (default) — by agent lifecycle
2. CLI Tool — by CLI concerns (parsing → commands → errors)
3. Web Service — by request path (routing → middleware → business → storage)
4. Data Pipeline — by data flow (ingest → transform → storage → query)
5. Infra Kit — by infra components (network → storage → scheduler)

Generates `.project-type` marker; Phase 4 reads it to preset `constants.ts` LAYERS.

**Files updated**:
- `scripts/bootstrap-site.sh`: added interactive prompt + `.project-type` generation
- `REFERENCE.md § 3.1`: new section with 5 layer templates

### ✨ New: Custom visualization guide

**Before**: only listed existing viz components  
**After**: § 4.1 with 3 custom viz blueprints

- `s00-architecture-map`: interactive project overview (reactflow/SVG)
- `sNN-timeline`: lifecycle stages (for request-response / pipeline projects)
- `sNN-state-machine`: FSM diagram (for CLI/workflow engines)

Includes implementation notes (copy which base component, how to add).

**Files updated**:
- `REFERENCE.md § 4.1`: new custom viz section

### 📄 New: Interview simulator spec (P2 feature)

Added `INTERVIEW_SIMULATOR.md` with full implementation blueprint:
- Random quiz page with 30s countdown timer
- Parse Q&A from markdown (regex for upgraded 3-tier format)
- Show reference answer + code location after timer
- Integration points (route + parser + chapter page link)

**Priority**: P2 (optional differentiation feature after core content)

### 🔄 Updated: Skill comparison table

Added comparison table to `SKILL.md` showing:
- note-skill / tech-deep-dive → single HTML
- step-viz-note → single HTML + step viz
- **proj-to-learn-site** → Next.js + **3-tier interview** + simulator

Highlights core differentiators (source verification, 3-tier Q&A, project type adaptation).

---

## Migration notes for existing users

If you already generated a site with the old flat interview format:

1. **Upgrade docs.json**: rewrite "## 面试拷打" sections using the new template (REFERENCE.md § 5)
2. **Optional**: run `bootstrap-site.sh` on a fresh copy to get `.project-type` prompt, then merge your content back
3. **Optional P2**: add interview simulator (INTERVIEW_SIMULATOR.md)

No breaking changes to file structure or data schemas.

---

## 2026-06-25 (cont. 2): Fixed core defect — viz must depict project, not Claude Code

### 🔴 The silent defect (most important fix this session)

**Symptom**: User noticed on VidLens that every chapter's step-through visualization still showed learn-claude-code's original diagrams ("Three Lanes", "skill loading", etc.), even though `index.tsx` had been remapped.

**Root cause**: The reference app ships 20 viz components (`s01-agent-loop.tsx` … `s20-comprehensive.tsx`) with content **hard-coded to Claude Code's mechanisms**. The old skill (§ 4) said "reuse them by mechanism mapping" — but remapping `index.tsx` only borrows the *animation shell*. The nodes, labels, and step descriptions inside still describe Claude Code, not the user's project. Since the viz is the site's headline feature, this made every site's headline broken.

**The fix was already in the repo, just unused.** `src/components/visualizations/shared/mechanism-flow.tsx` (`MechanismFlow`) is a **data-driven template**: you supply `{nodes, edges, steps}`, it renders an animated step-through graph. None of the 20 shipped viz components used it — they each hard-coded their own. So the supported path (custom data-driven viz) existed but the skill pointed at the wrong thing.

**Changes to skill**:
- `SKILL.md`: "Three non-negotiables" → **"Four non-negotiables"** (added #4: viz must depict the real mechanism). Phase 4 + Quick start now mandate authoring custom viz via MechanismFlow.
- `REFERENCE.md § 4`: **completely rewritten**. Old "catalog of 20 reusable components" → new "use MechanismFlow, do NOT reuse Claude-Code viz shells". Includes full data schema, node kinds/colors, coordinate layout tips, and a copy-paste template. § 4.2 lists the narrow case where reuse is acceptable.
- `REFERENCE.md § 7` (Verify): added "viz content check" step — step through each MechanismFlow and confirm node labels are the project's, not Claude Code's.

**Validated on BondCode**: authored 2 custom data-driven viz via MechanismFlow:
- `bond-subagent-flow.tsx` (s05): 父Agent → task(profile) → 并发上限闸 → 子Agent独立messages[] → profile受限工具集/excludedTools → runTaskLoop → task_result截断回填
- `bond-orchestrator-dag.tsx` (s06): orchestrate → checkpoint resume → Plan DAG → 有界并发+worktree隔离 → checkpointing(retrying(subagent))分层 → Synthesize

Both verified in browser: nodes/edges/steps depict BondCode's actual mechanisms, 0 console errors. Screenshot: `bondcode-s05-custom-viz.png`.

### 📝 Lesson

Two defects hid for the whole session because the BondCode validation only checked "viz loads, no white screen" — never "viz content matches the mechanism". **The viz is the headline; its content correctness is non-negotiable.** Always verify node labels depict the project, not the borrowed shell.

---

## 2026-06-25 (cont.): Validated end-to-end on BondCode (8 chapters)

### 🐛 Fixed: simulator import map breaks on chapter expansion

**Symptom**: expanding BondCode from 4 → 8 chapters caused 30 console errors + 500 on every page: `Module not found: @/data/scenarios/s07.json ... s20.json`.

**Root cause**: `src/components/simulator/agent-loop-simulator.tsx` hardcodes static `import()` for s01..s20. When chapter count changes (or unused scenario files are deleted), dangling imports break the build.

**Fix**: trim `scenarioModules` map to exactly `VERSION_ORDER`. Now documented as **must-fix** in REFERENCE.md § 7 (Verify) + § 8 (Known residuals).

### ✅ Validation results

- 8 chapters (s01-s08) all render with 3-tier interview structure
- 5-layer sidebar grouping (Loop·Tools·Safety / Context Governance / 委托·编排 / 可扩展性 / Prompt·规划)
- `validate-content.mjs`: ✓ consistent (versions↔docs↔scenarios↔viz all aligned)
- `next build`: ✓ 0 errors, 64 static pages
- Playwright: 0 console errors on s05/s08, viz + simulator + tabs all work
- Screenshot: `bondcode-s05-interview-3tier.png`

### 📝 Lesson: chapter count is a first-class variable

The skill's reference app assumes 20 chapters in several places (simulator imports, execution-flows, arch components). When adapting to a project with N chapters, **N must propagate to**: simulator `scenarioModules` map, `VERSION_ORDER`, LAYERS, viz `index.tsx`, scenarios dir. `validate-content.mjs` catches most, but the simulator import map slips through — now flagged.
