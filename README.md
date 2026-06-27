# Personal Skills

这是我的个人 agent skill 仓库，主要服务于三类任务：

- 学习 AI / vibe coding 生成的项目，并把它们转化成可防守的简历项目
- 准备后端、Agent 开发、AI 应用开发相关的项目面试
- 把项目源码、学习笔记或技术主题整理成可视化资料

## 目录结构

```text
skills/
├─ learn-vibe-coded-project/       # 主力：逐文件学习陌生或 vibe-coded 项目
├─ project-interview-grill/        # 主力：项目简历防守、证据审计、面试拷打
├─ _deck/
│  ├─ viz/                         # 单文件可视化笔记（arch-viz-note, step-viz-note, leetcode-viz）
│  ├─ slides/                      # 单文件 HTML 演示 deck（html-slides, tech-deep-dive, project-notes-html-deck）
│  ├─ sites/                       # 多页站点生成（proj-to-learn-site, project-to-book）
│  ├─ proj-to-showcase/            # 编排层：批量调用 viz/ 生成展示材料
│  └─ _meta/                       # 优化建议、通用参考文档
├─ _incubating/                    # 实验中或待合并的 skill
└─ _archive/                       # 旧版、被替代、暂不主动使用的 skill
```

## 主力 Skills

### `learn-vibe-coded-project`

用于真正读懂一个不是自己手写的项目，尤其是 AI 辅助完成、只运行过但没有深入理解的项目。

推荐场景：

- “带我学这个项目”
- “这个 vibe coding 项目我要放简历，帮我一边读源码一边准备面试”
- “我没读过这个 repo，帮我建立项目 mental model”

推荐用法：

```text
请使用 $learn-vibe-coded-project，带我系统学习这个项目，用于后端 / Agent / AI 应用开发实习面试准备。

项目路径：D:\dev\my_proj\go\<project-name>

要求：
1. 先做项目 inventory 和业务背景速览。
2. 不要一口气总结全项目，按模块让我选。
3. 每次只讲一个核心文件。
4. 每个文件都要讲：链路位置、技术选型、替代方案、边界兜底、八股延伸、模拟面试题、哪些点不要硬说。
5. 记录学习进度，方便下次继续。
```

### `project-interview-grill`

用于把项目转成简历和面试中可防守的材料。核心是证据审计：哪些能写，哪些要限定，哪些不能主动讲。

推荐场景：

- “这个项目能不能写进简历？”
- “帮我做项目拷打”
- “根据源码判断这些简历 bullet 有没有风险”
- “Agent / LLM 项目面试会怎么追问？”

推荐用法：

```text
请使用 $project-interview-grill，基于这个项目做简历防守和面试拷打。

项目路径：D:\dev\my_proj\java\<project-name>

重点检查：
1. 哪些亮点有代码证据。
2. 哪些说法需要限定。
3. 哪些说法不要主动讲。
4. 面试官会从架构、技术选型、失败兜底、测试证据、AI Coding 真实性几个方向怎么追问。
```

## 辅助区域

### `_deck/`

放可视化输出类 skill，按用途分组：

**`viz/`** — 单文件可视化笔记：

- `arch-viz-note`: mermaid 架构图、模块依赖图、目录树
- `step-viz-note`: SVG 步进动效流程图 + 消息流模拟器
- `leetcode-viz`: LeetCode 题目交互式可视化

**`slides/`** — 单文件 HTML 演示 deck：

- `html-slides`: 纸质杂志风格 HTML slide deck
- `tech-deep-dive`: 交互式技术深潜文档（5 种输入模式）
- `project-notes-html-deck`: 源码证据驱动的项目面试笔记 deck

**`sites/`** — 多页站点生成：

- `proj-to-learn-site`: 项目→ Next.js 交互式教程站
- `project-to-book`: 项目→ VitePress 文档/书站

**`proj-to-showcase/`** — 编排层，批量调用 `viz/` 生成展示材料。

这些 skill 不作为默认主力流程。只有当目标明确是”做 HTML/PPT/可视化笔记”时再使用。

### `_incubating/`

放仍在试验、评估或等待合并的 skill。

当前：

- `project-grill-prep`: 内容很完整，但和 `project-interview-grill` 职责重叠，先保留为实验版。

### `_archive/`

放旧版本、重复版本、被替代版本或暂时不主动使用的 skill。

注意：如果某个工具会递归扫描整个仓库里的 `SKILL.md`，`_archive` 里的旧 skill 仍可能被误触发。日常使用时应优先只暴露顶层主力 skill，或在安装/同步时排除 `_archive`。

## 推荐工作流

学习并准备一个项目时，优先按这个顺序：

1. 用 `learn-vibe-coded-project` 建立项目理解。
2. 用 `project-interview-grill` 做简历防守和面试拷打。
3. 需要展示材料时，再从 `_deck` 里选择可视化 skill。

不要一开始就直接写简历话术。先读代码证据，再决定哪些内容能写、怎么写、能不能经得住追问。

