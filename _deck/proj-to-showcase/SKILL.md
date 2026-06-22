---
name: proj-to-showcase
description: |
  给一个代码项目（vibe coding 出来的也行），自动发现其中"流程型"的功能点，按简历相关性排序，
  批量调用 step-viz-note 生成精美动效笔记，并产出索引页。当用户说"给我的项目做笔记/做展示"、
  "按简历挑功能点做成可视化"、"把这个项目讲清楚能面试用"时使用。
trigger_words:
  - 项目笔记
  - 项目展示
  - 按简历做笔记
  - 面试展示
  - 项目图解
  - 自动做笔记
  - 发现功能点
  - showcase
---

# proj-to-showcase Skill

把一个代码项目变成一组**可讲清楚的视觉笔记**，专门挑"流程型"功能做成 step-viz 动图。
核心卖点：**可选输入简历，按"最能佐证你简历 claim"来挑要画的功能**——产出的不是文档，是面试备战材料。

> **依赖**：本 skill 是编排层，**渲染交给 `step-viz-note`**（单文件 HTML 模板）。每张笔记 = 一份填好 DATA 的 step-viz 模板。
> 两者关系：`proj-to-showcase` 负责"发现 + 挑选 + 起草"，`step-viz-note` 负责"画出来"。

---

## 它解决的真问题

"给我的项目做笔记"如果无脑全做，会得到一堆质量参差、很多根本不适合动效的烂图。本 skill 的价值在**两道闸**：
1. **流程型分类闸**——只把真正"有先后步骤、逐步演进"的功能送去画动图；架构决策/目录结构这类**结构型**的，走 prose，不强塞动效。
2. **简历相关性闸**——给简历时，按"讲清楚这个流程能佐证简历哪条 claim"来排序挑选，不画没用的。

---

## 完整 Pipeline

### Phase 0 · 摸输入
- **必填**：项目根路径。
- **可选**：简历/JD 文本或文件；目标产出数量（默认 3–5 张）。
- 没简历就走"重要性排序"分支；有简历走"简历匹配排序"分支。

### Phase 1 · 快速测绘
扫一遍项目，搞清三件事（读 README、入口文件、目录结构、主要 package）：
1. 这个项目**到底干什么**（一句话能说清）。
2. **动作发生在哪**：主循环、handler、pipeline 入口在哪几个文件。
3. **有哪些候选功能**值得讲。
用 Explore/general-purpose agent 做广扫，只要结论不要文件 dump。

### Phase 2 · 发现候选功能点
按 `references/discovery-heuristics.md` 的特征清单找"流程型"候选。高信号模式：
- Agent/LLM 循环（`while`/`for` + 工具调用）
- 请求处理链（HTTP/gRPC/CLI → 中间件 → 控制器 → DB → 响应）
- 流水线（ingest → transform → ... 分阶段）
- 状态机（状态 + 迁移）
- 编译器/解析器（lex → parse → ... → codegen）
- 构建/部署/CI 流程、鉴权/会话流

### Phase 3 · 分类闸（关键）
对每个候选判：**流程型 or 结构型**？
- 流程型 → 进 step-viz 笔记。
- 结构型（架构决策、模块依赖图、目录地图、设计权衡）→ **不画动效**，记成 prose 或架构卡片，或直接跳过。
> 强扭结构型内容进动效 = 烂图。这道闸不能省。

### Phase 4 · 排序挑选
- **有简历**：抽简历里的技能/目标岗位/项目 claim，给每个流程型候选打分：
  *讲清楚这个流程，能多直接地佐证简历里的哪条 claim？* 按分排序取 top N。每个挑中的必须能说清"对应简历哪条"。
- **无简历**：按"对项目核心的重要度 × 讲清楚的教学价值 × 展示惊艳度"打分，取 top N。

### Phase 5 · 逐个起草（每张笔记）
对每个挑中的功能：
1. **读真代码**，把流程跑通——节点、分支、循环、终止条件、真实符号名。
2. **填 step-viz 的 DATA**：`diagram` 用 `layout:"auto"`（不手填坐标）、`steps[]` 5–8 步、`messages` 演一遍真实调用、`content` 写准确 prose。
3. **渲染**：拷 `step-viz-note/assets/template.html` 到 `<项目>/docs/notes/<feature>.html`，填入 DATA。
4. 详细字段规则看 `step-viz-note/references/authoring-guide.md`。

### Phase 6 · 索引页
用 `assets/index-template.html` 生成 `<项目>/docs/notes/index.html`，把所有笔记串成画廊，
每张配标题 + 一句话摘要 +（有简历时）"对应简历 claim"标签。

---

## 硬性原则

1. **准确 > 覆盖**：绝不编造符号、流程、调用链。读不通就不画——宁可少一张，不要一张错的。
2. **流程型闸不可省**：结构型内容不进动效。
3. **简历匹配要可辩护**：挑中的每个功能必须能指到简历具体一条。
4. **每张 5–8 步**：少了单薄，多了啰嗦。
5. **用 `layout:"auto"`**：批量生产时别手摆坐标，省心且一致。
6. **诚实标注草稿**：自动产出是 70–80% 草稿；交付前提示用户过一遍关键那张。

---

## 资源结构
```
proj-to-showcase/
├── SKILL.md
├── assets/
│   └── index-template.html      # 笔记画廊索引页模板
└── references/
    └── discovery-heuristics.md  # 流程型特征清单 + 简历匹配打分表
```
**加载顺序**：SKILL.md → 摸输入 → 测绘（Phase1）→ 读 discovery-heuristics.md 做发现/分类/排序 → 逐个调 step-viz-note 起草 → 用 index-template.html 收口。
