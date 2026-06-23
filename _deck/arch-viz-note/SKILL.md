---
name: 架构图解笔记
description: |
  生成"单文件 HTML + mermaid 图"风格的结构型笔记，专攻 step-viz-note 不碰的内容：架构总览、模块依赖图、
  分层图、目录树、组件关系。当用户要做架构图/依赖图/模块关系/目录地图、或结构型内容（而非流程型动效）时使用。
  与 step-viz-note 配套：流程型→step-viz，结构型→本 skill。
trigger_words:
  - 架构图
  - 依赖图
  - 模块关系
  - 目录地图
  - 分层架构
  - 组件图
  - 结构图解
  - arch viz
---

# 架构图解笔记 Skill

`step-viz-note` 的结构型伴生。专门画**架构总览、模块依赖、分层、目录树、组件关系**这类**静态/空间型**内容——
用 **mermaid**（自动布局，依赖图/架构图的事实标准）渲染，单文件 HTML 输出。

> **分工（跟 step-viz-note 的边界）**
> - 内容能"一步步演出来"（有先后、有循环/分支）→ `step-viz-note`（动效）。
> - 内容是"长什么样/谁依赖谁/怎么分层"（静态结构）→ **本 skill**（mermaid）。
> - 拿不准问一句："这东西能一步步演吗？" 能→step-viz；不能→本 skill。

---

## 为什么用 mermaid 而不是手画 SVG

结构图（尤其依赖图）节点多、关系密，**自动布局是刚需**——手摆坐标不现实。mermaid 内置 dagre 布局，
写几行文本声明就能出干净的架构/依赖图。

但"自动布局"不等于"没风格"。本 skill 把项目里手绘 SVG 的**视觉系统**（语义配色 + 增量叙事 + 图例点题）
注入 mermaid：蓝=核心、绿=新增、橙=强调、灰=保留，节点直接 `X:::new` 上色，图下方配图例条。
做法见速查第 0 节。

---

## 模板

```
assets/template.html   # 渲染引擎 + 语义主题 + DATA 示例
assets/mermaid.min.js  # 本地 mermaid（离线用，随模板一起拷贝）
```

- 数据驱动：顶部一个 `DATA` 对象，`diagrams[]` 每项是 `{title, mermaid, caption?, legend?}`；`content` 是正文 markdown。
- 一页可放**多张图**（架构总览 + 依赖图 + 目录树…），每张一个卡片。
- **语义配色**：`core/new/emph/dim/data` 五个 class 已自动注入（仅 flowchart/graph），节点写 `X:::cls` 即用。
- **图例条**：`legend: [{cls, text}]` 渲染成图下方色块条，点题"各颜色代表什么"。
- **每图可缩放**：每张图带 `+/−/重置` 按钮 + `Ctrl/⌘+滚轮`，默认 100%（上限 500%、下限 50%）。
- 图区固定浅色（对齐手绘 SVG 画布），明暗主题只切周围框架、不重渲染图。

### 离线说明（默认即离线）
模板优先加载同目录的 `mermaid.min.js`——**只要把它跟 `arch.html` 一起拷贝，就是完全离线**；若本地文件缺失，
JS 会自动回退到 CDN（`cdn.jsdelivr.net`）。所以：
- 大多数场景 → 拷两个文件，离线可看。
- 想严格单文件 → 把 `mermaid.min.js` 内容内联进 `<script>` 标签（一份约 3.3MB）。

---

## 工作流

### Step 1 · 澄清
要画什么结构？常见四类：① 架构总览（分层）、② 模块/包依赖图、③ 目录树、④ 组件/实体关系。
给项目路径就让我自己读代码摸结构。

### Step 2 · 拷贝模板（两个文件）
```bash
mkdir -p "<目标目录>"
cp "<SKILL_ROOT>/assets/template.html" "<目标目录>/arch.html"
cp "<SKILL_ROOT>/assets/mermaid.min.js" "<目标目录>/mermaid.min.js"
```

### Step 3 · 填 `DATA`
1. `meta`：标题、副标题。
2. `diagrams[]`：每张图 `{title, mermaid, caption?, legend?}`。mermaid 语法见 `references/mermaid-cheatsheet.md`。
   - 架构总览 → `flowchart TD` + subgraph 分层，关键枢纽（如唯一调度者）打 `:::emph`
   - 依赖图 → `flowchart LR`，用 `dim`/`new` 区分"沿用核心"vs"新增/可裁剪"
   - 目录树 → `flowchart TD` 或 mindmap
   - `legend`：配色说明，帮读者一眼对应"颜色↔含义"
3. `content`：正文 markdown，讲设计决策、为什么这么分层（结构型内容的主力文字区）。

### Step 4 · 自检 & 预览
- mermaid 语法错了图不渲染——浏览器控制台会报。先单独验证 mermaid 文本。
- 节点别太多（>25 个建议拆成多张图）。
- 浏览器打开预览，切深浅主题看两遍（图区固定浅色，主题只切周围框架）。

---

## 设计原则

1. **结构型才用它**：流程型去 step-viz，别混。
2. **声明式**：写 mermaid 文本，不摆坐标。
3. **一图一主题**：架构总览、依赖图、目录树分开画，别塞一张图里。
4. **语义配色**：用 `core/new/emph/dim/data` 表达轻重，颜色即信息，而非装饰性上色。
5. **增量叙事**：讲演进/对比时，用 `dim`（旧·保留）+ `new`（新增）+ `legend`，复刻手绘 SVG 的叠加手法。
6. **配 prose**：图说"是什么"，文字补"为什么这么设计"。
7. **克制节点数**：密到看不清就拆。

---

## 资源结构
```
arch-viz-note/
├── SKILL.md
├── assets/
│   ├── template.html          # 多 mermaid 图 + 语义主题 + markdown 正文，明暗主题
│   └── mermaid.min.js         # 本地 mermaid（离线）
└── references/
    └── mermaid-cheatsheet.md  # 语义配色 + 架构/依赖/树 常用写法
```
**加载顺序**：SKILL.md → 拷 template.html + mermaid.min.js → 读 mermaid-cheatsheet.md 写图 → 填 DATA → 预览。
