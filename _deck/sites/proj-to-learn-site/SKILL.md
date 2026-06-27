---
name: proj-to-learn-site
description: Turn a codebase (usually a vibe-coded resume project the user wants to put on their CV) into a learn.shareai.run-style interactive tutorial website that deeply reads the REAL source, teaches each core mechanism chapter-by-chapter, and bakes in 3-tier interview-grilling Q&A (🟢基础 → 🟡追问 → 🔴架构权衡 + 🧩反向溯源 + ⚖️横向对比) per chapter so the user genuinely understands their own project and survives interview pressure. Use when the user wants to turn a project into an interactive tutorial / 学习网站 / 可视化网站 to understand it or prep for interviews, references learn.shareai.run or learn-claude-code style, mentions 简历项目 / 面试准备 / 面试拷打 / 项目理解, or wants a polished framework-built site (not a single HTML file).
---

# proj-to-learn-site

Turn a project into a learn.shareai.run-style interactive tutorial for **interview prep**. The output looks like learn.shareai.run because we **reuse their actual Next.js app** and swap content — we do not rebuild the UI.

## 🎯 与其他 note 类 skill 的区别

| Skill | 输出 | 适用场景 |
|---|---|---|
| note-skill / tech-deep-dive | 单文件 HTML | 快速笔记、文档阅读 |
| step-viz-note | 单文件 HTML + 步骤可视化 | 技术教程、流程图解 |
| **proj-to-learn-site** | 完整 Next.js 站点 + **3 层面试拷打** + 可视化模拟器 | **简历项目深度理解 + 面试防拷** |

核心差异：
- ✅ 强制深度读源码（不是 AI 臆测）+ 交叉验证 prep docs
- ✅ **3 层面试题**（🟢基础理解 → 🟡深入追问 → 🔴架构权衡）+ 🧩反向溯源（给现象推机制）+ ⚖️横向对比（vs 开源框架）
- ✅ 可部署的交互式站点（模拟器 + 源码 tab + 可视化）
- ✅ 项目类型自适应（Agent Runtime / CLI Tool / Web Service / Data Pipeline / Infra Kit）

## Four non-negotiables

1. **Reuse the UI, don't reinvent it.** Copy `learn-claude-code/web` (Next 16 + Tailwind v4 + framer-motion + lucide + rehype-highlight) into `<proj>/docs/site/` and swap content. This is what guarantees pixel-fidelity to learn.shareai.run.
2. **Read the REAL source first.** Every claim verified against code (file:line). If the user has stale prep docs that contradict the code, **flag the discrepancy explicitly** — the entire point is they must not memorize wrong things. Use the project's own "what's really wired in" truth source (its CLAUDE.md will name it, e.g. `bootstrap.go`).
3. **3-tier interview-grill focus.** Each chapter teaches one mechanism AND ends with 5-layer interview Q&A answered **from code understanding**:
   - 🟢 **基础理解**（必答，1-2 题）
   - 🟡 **深入追问**（连环拷，2-3 题，如 Q2a → Q2b）
   - 🔴 **架构权衡**（为什么不用 X / 为什么这样设计）
   - 🧩 **反向溯源**（给 bug 现象推代码路径）
   - ⚖️ **横向对比**（vs LangChain / vs 开源框架）
   
   Each with "⚠ 别这么说" anti-pattern.
4. **Viz must depict the project's REAL mechanism, not Claude Code's.** The viz is the site's headline feature. The shipped 20 viz components are hard-coded to Claude-Code mechanisms — **do not reuse them as-is** (remapping `index.tsx` only borrows the animation shell; nodes/steps still say Claude Code). **Author one custom data-driven viz per chapter via `MechanismFlow`** (REFERENCE.md § 4). Verify in browser that each step-through graph shows the project's own nodes/flow.

## Quick start

```
1. Scope: list the project's core mechanisms → chapters s01..sNN (from its CLAUDE.md / architecture).
2. Ensure learn-claude-code/web is available (local, or git clone shareAI-lab/learn-claude-code).
3. bash scripts/bootstrap-site.sh <learn-claude-code>/web <proj>/docs/site
   → prompts for project type (1-5), generates .project-type marker
4. Deep-read source per chapter; record real file:line + actual defaults; cross-check vs any prep docs.
5. Hand-author: constants.ts (read .project-type for layer template) · generated/versions.json · generated/docs.json (use 3-tier interview template) · scenarios/*.json
   **author custom viz via MechanismFlow per chapter** (see § 4 — do NOT reuse Claude-Code viz shells) · update i18n/messages/<locale>.json
6. npx next dev -p 3000  →  verify all tabs in browser (playwright); **check each viz actually depicts the project's mechanism, not Claude Code's**.
```

## Workflow phases

**Phase 1 — Scope & reference.** Identify mechanisms → chapter ids. Get learn-claude-code/web.

**Phase 2 — Scaffold (deterministic).** `scripts/bootstrap-site.sh` copies the app, **prompts for project type** (1=Agent Runtime, 2=CLI, 3=Web, 4=Pipeline, 5=Infra), **neuter `predev`/`prebuild`** (they run `extract-content.ts` which clobbers hand-authored data), and `npm install`. Boot with `npx next dev`.

**Phase 3 — Deep source read (do NOT skip).** Read CLAUDE.md/AGENTS.md, the wiring/bootstrap file, each mechanism package. Record real refs. Cross-check prep docs → list discrepancies.

**Phase 4 — Author content.** constants.ts (VERSION_ORDER + VERSION_META + LAYERS, **read `.project-type` for layer template**) · generated/versions.json (AgentVersion[] + diffs) · generated/docs.json (markdown per chapter, **use 3-tier interview template**) · scenarios/sNN.json (simulator flow) · **custom viz per chapter via `MechanismFlow` (REFERENCE.md § 4)** · i18n titles.

> ⚠ **Phase 4 viz note (was a silent defect):** the app ships 20 viz components whose content is hard-coded to Claude Code's mechanisms. Remapping `index.tsx` to reuse them only borrows the *animation shell* — the nodes/steps still depict Claude Code, not the user's project. **Author custom data-driven viz with `MechanismFlow`** (one small data file per chapter); reuse is acceptable only for mechanisms that genuinely match.

> 🔧 **常见可视化布局问题**（详见 REFERENCE.md § 8）：
> - **文字溢出框**：label 超过 10 中文字或 >2 行 → 精简为单行动词短语
> - **节点几乎不可见**：`appearsAt: 2+` → 改为 `appearsAt: 0 或 1`
> - **箭头混乱**：节点间距 <140px（垂直）/<200px（水平）→ 增大间距并扩大 `viewBox`
> - **Quick fix 模板**：垂直流用 `y: 80, 220, 360, 480`（140px 间距），画布用 `viewBox="0 0 1120 520"` 容纳 9 节点

**Phase 5 — Per-chapter template** (docs.json markdown):
`问题` → `解决方案(ASCII)` → `工作原理(ordered + real code w/ file:line)` → `关键不变量/设计权衡(table)` → **`面试拷打(5-layer: 🟢基础/🟡追问/🔴权衡/🧩溯源/⚖️对比)`** → `试一试/代码证据`.

**Phase 6 — Verify.** `node scripts/validate-content.mjs <site>` + playwright (learn/simulate/code tabs render, viz loads, simulator plays the scenario, no console errors).

**Phase 7 — Deploy (optional).** The app is static-export-ready out of the box. `bash scripts/deploy-pages.sh <site> <name>` builds `out/` and ships to Cloudflare Pages (wrangler). See [REFERENCE.md §9](REFERENCE.md) for multi-project hosting.

➡ Full data schemas, file-by-file edits, the viz-component catalog (+ custom viz guide), gotchas, and the BondCode worked example live in [REFERENCE.md](REFERENCE.md) and [EXAMPLES.md](EXAMPLES.md).

➡ **Optional P2 feature**: Interview simulator page with timer + random quiz — see [INTERVIEW_SIMULATOR.md](INTERVIEW_SIMULATOR.md).

## When NOT to use this skill

- User wants a quick single-file HTML note → use `note-skill` / `step-viz-note` / `tech-deep-dive` instead.
- Target is API/library reference docs, not "a project to understand for interviews".
- No learn-claude-code/web available AND user doesn't want to clone it (the fidelity comes from reusing it).
