# _deck Skills 优化建议

基于对三个 `_deck` skill 的审查，对比参考教学网站 `learn-claude-code` 的风格，总结以下优化建议。

---

## 📊 整体评价

三个 skill 设计得很好，分工清晰：
- `step-viz-note`：流程型动效笔记（SVG 动效）
- `arch-viz-note`：结构型架构图（mermaid）
- `proj-to-showcase`：编排层，批量调用 step-viz-note

**优点**：
1. 三个 skill 的边界划分清楚（流程型 vs 结构型）
2. 有完整的 references 和 assets 结构
3. 工作流步骤详细，有自检环节

---

## 🔧 优化建议

### 1. Frontmatter 的 description 结构化

对比教学网站的写法，当前的 description 偏长且是纯文本块。建议改成编号列表 + 关键词。

**当前写法**（step-viz-note）：
```yaml
description: |
  生成"单文件 HTML + 数据驱动步进动效图解 + 消息流模拟器"风格的学习笔记。
  复刻 learn.shareai.run 的视觉精髓：SVG 流程图按步高亮发光、messages[] 累加动画、
  播放/单步/倍速控件、明暗主题。当用户想把某个机制/流程/原理做成"像 learn.shareai.run 那样
  会动、会一步步演进"的可视化网页笔记时使用。
```

**建议改成**：
```yaml
description: |
  Generate single-file HTML visual notes with step-by-step animations and message flow simulator.
  Use when users:
  (1) want to visualize a mechanism/process/principle with animated diagrams
  (2) ask for "step viz", "interactive notes", or "notes like learn.shareai.run"
  (3) need to explain a flow with SVG highlighting + message accumulation
  (4) want zero-dependency, offline-capable HTML notes
  Keywords: step-viz, animation, interactive, flow diagram, simulator, shareai
```

**好处**：更容易被 skill loading 系统匹配，也更清晰地说明了使用场景。

**适用文件**：
- `_deck/viz/step-viz-note/SKILL.md`
- `_deck/viz/arch-viz-note/SKILL.md`
- `_deck/proj-to-showcase/SKILL.md`

---

### 2. 添加 Anti-Patterns 部分

教学网站的 agent-builder 有一个很好的 Anti-Patterns 表格，建议在每个 skill 中加上。

**step-viz-note 建议添加**：
```markdown
## Anti-Patterns

| 模式 | 问题 | 解决方案 |
|------|------|----------|
| 强扭结构型内容 | 架构图/目录树塞进动效，效果差 | 用 arch-viz-note 画 mermaid |
| 步骤太多 | 超过 8 步用户看晕 | 拆成多张笔记 |
| 编造符号名 | 调用链不真实，面试露馅 | 读真代码，读不通不画 |
| 手摆坐标 | 批量生产效率低 | 用 layout:"auto" |
```

**arch-viz-note 建议添加**：
```markdown
## Anti-Patterns

| 模式 | 问题 | 解决方案 |
|------|------|----------|
| 流程型内容用 mermaid | 没有动效，无法演进 | 改用 step-viz-note |
| 节点太多 | 超过 25 个看不清 | 拆成多张图 |
| 强制离线 | mermaid 依赖 CDN | 预渲染 SVG 或接受联网 |
```

**proj-to-showcase 建议添加**：
```markdown
## Anti-Patterns

| 模式 | 问题 | 解决方案 |
|------|------|----------|
| 无脑全做 | 质量参差，很多不适合动效 | 用分类闸过滤 |
| 跳过简历匹配 | 产出对面试没用 | 必须按简历 claim 挑选 |
| 不读真代码 | 调用链编造，面试露馅 | Phase 5 必须读真代码 |
```

---

### 3. 精简核心哲学部分

教学网站的风格是用一句话概括核心哲学，然后展开。当前写得比较详细，可以更精炼。

**step-viz-note 建议加在开头**：
```markdown
## 核心哲学

> **一条时间轴驱动三视图：图高亮、消息流、注解同步。**

动效服务于理解，不是炫技。节点/步数要克制，5-8 步最佳。
```

**arch-viz-note 建议加在开头**：
```markdown
## 核心哲学

> **声明式画图，自动布局。写 mermaid 文本，不摆坐标。**

结构图节点多、关系密，自动布局是刚需。
```

**proj-to-showcase 建议加在开头**：
```markdown
## 核心哲学

> **两道闸：流程型分类闸 + 简历相关性闸。**

无脑全做 = 质量参差的烂图。只挑真正能佐证简历 claim 的流程型功能。
```

---

### 4. 简化 Phase 描述（proj-to-showcase）

当前的 Phase 描述有点冗长，建议精简。

**当前写法**（Phase 1）：
```markdown
### Phase 1 · 快速测绘
扫一遍项目，搞清三件事（读 README、入口文件、目录结构、主要 package）：
1. 这个项目**到底干什么**（一句话能说清）。
2. **动作发生在哪**：主循环、handler、pipeline 入口在哪几个文件。
3. **有哪些候选功能**值得讲。
用 Explore/general-purpose agent 做广扫，只要结论不要文件 dump。
```

**建议改成**：
```markdown
### Phase 1 · 快速测绘
用 Explore agent 扫项目，回答三个问题：
1. 项目干什么（一句话）
2. 动作发生在哪（主循环/handler/pipeline 入口文件）
3. 哪些功能值得讲

**输出**：结论清单，不要文件 dump。
```

---

### 5. 添加"什么时候不用它"部分

参考教学网站的渐进式复杂度表格，明确边界。

**arch-viz-note 建议添加**：
```markdown
## 什么时候不用它

| 场景 | 为什么不用 | 用什么 |
|------|-----------|--------|
| 流程能一步步演 | 结构型不适合动效 | step-viz-note |
| 只有 2-3 个节点 | mermaid 太重 | 直接写文字 |
| 需要离线 | mermaid 依赖 CDN | 预渲染 SVG |
```

**step-viz-note 建议添加**：
```markdown
## 什么时候不用它

| 场景 | 为什么不用 | 用什么 |
|------|-----------|--------|
| 静态架构图 | 动效无法表达结构关系 | arch-viz-note |
| 目录树/依赖图 | 不是流程型 | arch-viz-note |
| 只有 2-3 步 | 动效收益低 | 直接写文字 |
```

---

### 6. 统一资源结构格式

三个 skill 的资源结构部分格式略有不同，建议统一成：

```markdown
## 资源结构

```
skill-name/
├── SKILL.md                    # 主文档
├── assets/
│   └── template.html           # 模板文件
└── references/
    └── xxx.md                  # 参考文档
```

**加载顺序**：SKILL.md → 拷 template → 读 references → 填 DATA → 自检 → 预览。
```

---

### 7. 添加 Quick Start 部分

教学网站的 skill 通常有 Quick Start，让用户快速上手。

**step-viz-note 建议添加**：
```markdown
## Quick Start

最简单的用法：
1. 告诉我你想讲什么机制/流程
2. 我会生成一个 HTML 文件
3. 双击打开，用 ←/→ 单步，空格播放

示例提示词：
> "帮我做一个 Agent 循环的图解笔记，像 learn.shareai.run 那样会动的"
```

**arch-viz-note 建议添加**：
```markdown
## Quick Start

最简单的用法：
1. 告诉我你想画什么结构（架构图/依赖图/目录树）
2. 或者给我项目路径，让我自己摸结构
3. 我会生成一个 HTML 文件，双击打开

示例提示词：
> "帮我画一下这个项目的模块依赖图"
> "做一个分层架构图，展示前后端分离"
```

**proj-to-showcase 建议添加**：
```markdown
## Quick Start

最简单的用法：
1. 给我项目路径
2. 可选：给一份简历/JD
3. 我会自动发现功能点，生成 3-5 张动效笔记 + 索引页

示例提示词：
> "给我的项目做笔记，按简历挑功能点做成可视化"
> "把这个项目讲清楚，能面试用的那种"
```

---

## 📋 总结清单

| 优化项 | 影响 | 优先级 | 适用文件 |
|--------|------|--------|----------|
| description 结构化 | 提高 skill 匹配准确度 | ⭐⭐⭐ | 全部三个 |
| 添加 Anti-Patterns | 避免常见错误 | ⭐⭐⭐ | 全部三个 |
| 精简核心哲学 | 更快理解设计意图 | ⭐⭐ | 全部三个 |
| 简化 Phase 描述 | 提高可读性 | ⭐⭐ | proj-to-showcase |
| 添加"不用场景" | 明确边界 | ⭐⭐ | step-viz-note, arch-viz-note |
| 统一资源结构格式 | 一致性 | ⭐ | 全部三个 |
| 添加 Quick Start | 降低上手门槛 | ⭐ | 全部三个 |

---

## 🎯 快速行动清单

如果时间有限，建议按以下顺序优化：

1. **第一步**：给三个 skill 的 description 加上结构化的 Use when 列表
2. **第二步**：给每个 skill 加上 Anti-Patterns 部分
3. **第三步**：在开头加一句核心哲学

这三步能显著提升 skill 的可用性和匹配准确度。
