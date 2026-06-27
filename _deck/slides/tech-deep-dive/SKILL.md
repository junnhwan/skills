---
name: tech-deep-dive
description: 分析代码项目、技术书籍或网页内容，生成精美交互式 HTML 学习文档。当用户提到"技术深潜"、"代码解析"、"学习项目"、"技术笔记"、"做笔记"、"面试准备"、"复习"、"总结"、"cheatsheet"、"deep dive"、"study guide"、"解析"、"读源码"、或给出 URL 要求生成笔记时使用。
---

# Tech Deep Dive · 技术深潜

分析代码项目、技术书籍或网页内容，生成一份**精美交互式 HTML 学习文档**。基于 `template.html` 骨架填充内容，包含 TOC 目录、全文搜索、进度条、幻灯片模式、数据流逐步动画、找 Bug 挑战、深度面试 Q&A。

## 核心原则

1. **基于模板生成** — 复制 `template.html`，替换 `{{}}` 占位符和示例 section
2. **默认 Midnight Neon** — 用户不指定则默认用此主题，跳过选择环节
3. **深度优先** — 宁可少讲几个模块也要讲透
4. **CSS 原生图** — 用 `.dg-node` / `.dg-layer` 生成架构图，不用外部库
5. **项目自适应** — 自动检测输入类型，适配输出结构
6. **面试官视角** — 每个 section 开头用 `.callout.interview` 标注面试官会怎么问这个点，不是 "这个模块讲了什么"，而是 "如果面试官追问这个方向，他会怎么问、你该怎么答"
7. **面试 Q&A 为主线** — 用深度面试 Q&A 替代知识测验，每道题都要有追问链和加分点

## ⚠ 踩坑清单（必须遵守）

1. **`section:nth-of-type(2n)`** — 交替背景用 `nth-of-type`，不要用 `nth-child`
2. **JS 用 IIFE 包裹** — `(function(){ ... })()` 避免全局变量冲突
3. **翻页模式用 `classList`** — 不要用 `className = ''` 覆盖
4. **退出动画页要 `display:block`** — 否则看不到滑出动画
5. **`data-steps` 单引号包裹** — flow-anim 的 JSON 用 `data-steps='[...]'`，label 里不能有单引号（用 `&apos;` 或改写）
6. **bug-challenge 只有一个 `.bug-target`** — 只有一行是 bug，其余都是 `onclick="checkBugLine(this,false)"`
7. **`.term` 定义不要有 HTML 标签** — `data-definition` 的值是纯文本
8. **代码里 `<` 要转义 `&lt;`** — HTML 才不会把代码当标签解析

## 五种模式

| 模式 | 触发 | 输出结构 |
|------|------|---------|
| **代码项目深潜** | 本地项目目录 | 架构分析 → 模块精读 → 数据流 → 深度面试 Q&A |
| **书籍/文档学习** | 本地 .md 章节 | 章节精读 → 知识卡片 → 陷阱 → 面试 Q&A |
| **Web 源笔记** | 给出 URL | 抓取网页 → 结构化 → 知识卡片 → 面试 Q&A |
| **单文件分析** | 单个源文件 | 逐段解读 → 调用链 → 边界分析 → 面试 Q&A |
| **面试突击** | 明确说"面试" | 面试题为主 + 快速参考卡 + 答题模板 |

### 模式检测规则

- 输入是 URL → Web 源笔记
- 目录有 `go.mod` / `package.json` / `pyproject.toml` → 代码项目深潜
- 目录有 `SUMMARY.md` 且子目录全是 `.md` → 书籍/文档学习
- 指定单个文件路径 → 单文件分析
- 明确说"面试" → 面试突击

## 工作流

### Phase 1 · 内容探索

#### 代码项目模式

1. **全局扫描** — 文件树 + 依赖文件 + README
2. **入口追踪** — 主入口 → 路由 → 初始化链
3. **模块精读** — 每个核心模块读 entity/repo/service/handler，用 Agent 并行
4. **深挖细节** — 测试、错误处理、注释 TODO、配置分支、并发模式
5. **数据流追踪** — 选核心场景追踪完整调用链
6. **面试题挖掘** — ≥30 道（项目介绍 + 深度追问 + 场景拷打 + 系统设计 + 代码走读 + 权衡分析），每道题都要有追问链
7. **Bug 挖掘** — 从代码中找 ≥5 个典型的 bug/bad practice，用于找 Bug 挑战

#### 书籍/文档模式

1. 扫描 SUMMARY.md / 目录 → 章节大纲
2. 每章精读 → 核心概念 + 代码示例 + 陷阱/gotcha
3. 跨章知识串联
4. ≥20 道面试 Q&A（混合分类 + 追问链）

#### Web 源模式

1. **URL 发现**
   - 单 URL → 直接抓取生成
   - URL + "整本书/整个系列" → 先抓首页提取所有章节链接，再逐个抓取
   - URL 列表 → 逐个抓取，合并
2. **内容抓取** — 用 WebFetch 逐个抓取，可并行
   - 如果 WebFetch 返回空或 4xx，跳过该章节并在结果中标注 **[内容缺失]**
3. **结构化提取** — 核心概念、代码示例、案例、陷阱、推荐资源
4. **生成笔记** — 每章一个 section，使用 card/callout/gotcha 组件
5. **面试 Q&A** — 每章 ≥2 道，基于章节内容生成

#### 单文件模式

1. 文件职责定位
2. 逐段解读（每段 ≤30 行，标注行号）
3. 调用链追踪
4. 边界 & 错误处理分析
5. 面试角度追问（10-15 道，含追问链）

#### 面试突击模式

1. **快速扫描** — 抓取项目核心架构和关键技术点
2. **题目分类生成**：
   - 项目介绍题（3-4 道）：30 秒介绍、技术栈选择、项目规模
   - 深度追问题（10-12 道）：基于代码的具体技术问题，每题附 2-3 个追问
   - 场景拷打题（8-10 道）："如果 X 发生会怎样"，要求分析完整影响链
   - 系统设计题（4-6 道）：扩展性、架构演进、技术选型权衡
   - 代码走读题（4-6 道）：展示代码片段，分析设计意图和改进空间
3. **答题模板** — 提供标准答题结构（STAR 法则 + 技术深度展示）
4. **快速参考卡** — 一页概念 Grid 总结高频考点
5. **难度标记** — 每道题标注 easy/medium/hard + 建议复习间隔
6. **追问链** — 每道题列出面试官可能的 2-3 个 follow-up 问题

### Phase 1.5 · 大纲预览（可选）

**代码项目模式推荐**：Phase 1 完成后，简要输出规划（每个 section 标题 + 一句话描述），等用户确认后再生成。避免生成 20 个 section 后结构不理想。

其他模式默认跳过此步。

### Phase 2 · 确认（默认跳过）

直接用 Midnight Neon + 双模式（滚动+幻灯片）生成。

仅在以下情况才问用户：
- 用户明确要求选主题 → 读取 `references/design-guide.md` 获取其他 5 种主题
- 用户要求特定阅读模式
- 内容大纲不确定

### Phase 3 · 生成 HTML

1. **复制 `template.html`** 到目标目录
2. **替换占位符** — `{{TITLE}}`、`{{HERO_TITLE}}`、`{{HERO_SUBTITLE}}`、`{{FOOTER_TEXT}}`
3. **添加 Prism 语言组件** — 根据内容需要的语言添加（如 `prism-go.min.js`、`prism-c.min.js`）
4. **填充 section 内容** — 每个主题一个 `<section id="xxx">`，开头加 `.callout.interview` 标注面试官会怎么问
5. **添加面试 Q&A section** — 独立 section，按分类排列 qa-card，每张卡含难度标签 + 追问链 + 面试加分
6. **添加数据流动画** — 代码项目模式必加，用 `.flow-anim` 包裹架构图
7. **添加找 Bug 挑战** — 代码项目/单文件模式必加 ≥3 个 `.bug-challenge`
8. **标记术语** — 面试关键术语用 `.term` 包裹，`data-definition` 里写面试话术

### Phase 4 · 交付

1. 保存 HTML 文件到用户目录
2. 如果目标目录已有同名 HTML → **增量更新**：读取现有内容，只更新/新增相关 section，保留用户的阅读进度和测验记录
3. 复制到 `D:\zjh\dev\my-skills\examples\`
4. 推送到 GitHub（`github.com:junnhwan/my-skills.git`，`main` 分支）
5. 告知快捷键：`Ctrl+K` 搜索、`S` 幻灯片、`T` 目录、`←→` 翻页

## 组件速查

所有组件的完整 HTML 写法见 `template.html` 中的注释标记。

| 组件 | 用途 | 结构 |
|------|------|------|
| 卡片 | 通用内容块 | `.card > h3 + p` |
| Callout | 提示/警告 | `.callout.info/.warn/.danger/.success` |
| **面试官 Callout** | **面试官会怎么问** | **`.callout.interview > strong + p`** |
| Gotcha | 陷阱提醒 | `.gotcha > .gotcha-title + p` |
| 概念 Grid | 快速参考卡 | `.concept-grid > .concept-item > .ci-label + .ci-value` |
| 架构图 | 层级关系 | `.dg > .dg-layer > .dg-node.nc-*` |
| **数据流动画** | **逐步推进调用链** | **`.flow-anim[data-steps] > .dg + .flow-controls`** |
| 箭头 | 层间连接 | `.dg-arr` |
| 对比 | 两栏对比 | `.compare > .compare-col` |
| 代码块 | 带语言标签 | `.code-wrap > .code-header + .code-body > pre > code.language-*` |
| **找 Bug 挑战** | **点击代码行找 bug** | **`.bug-challenge[data-explain] > .bug-line`** |
| **术语提示** | **悬浮显示面试话术** | **`.term[data-definition]`** |
| **文件树** | **项目结构可视化** | **`.file-tree > .ft-folder/.ft-file`** |
| Badge | 标签 | `.badge.b-purple/.b-cyan/.b-green/.b-amber/.b-rose/.b-blue` |
| **Q&A 卡片** | **面试题折叠** | **`.qa-card[data-difficulty][data-review] > .qa-q + .qa-a`** |
| 面试加分 | 加分提示 | `.qa-tip`（在 `.qa-a-inner` 内） |
| **追问链** | **面试官 follow-up** | **`.qa-followup`（在 `.qa-a-inner` 内）** |

## 面试官 Callout

每个 section 开头标注面试官会怎么问，给读者方向感：
```html
<div class="callout interview">
<strong>🎯 面试官会问：</strong>"你们项目的认证是怎么做的？Token 过期怎么处理？"
</div>
```

## 面试 Q&A 卡片（核心交互组件）

面试 Q&A 是文档的主要交互评估方式。每道面试题都是可折叠的 Q&A 卡片，包含完整的答题要素。

### 基本结构

```html
<div class="qa-card" data-difficulty="medium" data-review="3d">
  <div class="qa-q">
    <span class="badge b-purple">深度追问</span>
    <span class="qa-text">Agent Loop 为什么限制 MaxSteps 而不是用递归？</span>
    <span class="qa-difficulty medium">Medium</span>
    <span class="qa-review">复习: 3天</span>
    <span class="qa-arrow">▼</span>
  </div>
  <div class="qa-a"><div class="qa-a-inner">
    <div class="qa-tag">参考回答</div>
    <p><strong>一句话概括：</strong>MaxSteps 限制迭代轮次，防止 LLM 陷入死循环，同时保持代码可读性和可调试性。</p>
    <p><strong>深入分析：</strong>递归会让调用栈越来越深，出错的 stack trace 不直观。for 循环 + 计数器是更朴素的方式，每轮都是一个新的迭代，状态可以打印、可以断点。这跟 Kubernetes Job 的 backoffLimit 是同一思路。</p>
    <div class="qa-followup">
      <div class="qa-followup-title">🔗 追问链</div>
      <div class="qa-followup-item">
        <span class="qa-followup-q">如果 MaxSteps 用完了任务还没完成怎么办？</span>
        <span class="qa-followup-a">→ 返回部分结果 + 明确的截断提示，用户可以基于中间状态继续</span>
      </div>
      <div class="qa-followup-item">
        <span class="qa-followup-q">MaxSteps 的值怎么定的？</span>
        <span class="qa-followup-a">→ 基于经验值（通常 20-30），太大会浪费 token，太小会截断复杂任务</span>
      </div>
    </div>
    <div class="qa-tip">💡 面试加分：可以提到这和 Kubernetes Job 的 backoffLimit、CI/CD 的 timeout 是同一个设计模式 —— 用硬性上限兜底，配合优雅降级。</div>
  </div></div>
</div>
```

### 题目分类与数量要求

| 分类 | 数量（代码项目） | Badge | 典型问题 |
|------|----------------|-------|---------|
| **项目介绍** | 3-4 道 | `b-cyan` | "用 30 秒介绍你的项目"、"为什么选 Go？" |
| **深度追问** | 10-12 道 | `b-purple` | "这个模块的实现原理？"、"为什么用 X 不用 Y？" |
| **场景拷打** | 8-10 道 | `b-rose` | "如果并发翻 10 倍会怎样？"、"这个依赖挂了怎么办？" |
| **系统设计** | 4-6 道 | `b-amber` | "怎么横向扩展？"、"如何支持多租户？" |
| **代码走读** | 4-6 道 | `b-green` | "这段代码的设计意图？"、"你会怎么改进？" |
| **权衡分析** | 3-4 道 | `b-blue` | "用 JSONL 而不是数据库的取舍？"、"同步 vs 异步确认？" |

### 难度标记规则

| 难度 | 含义 | 复习间隔 | 颜色 |
|------|------|---------|------|
| **easy** | 基本概念，看过代码就能答 | 7d | 绿色 |
| **medium** | 需要理解设计原理和权衡 | 3d | 琥珀色 |
| **hard** | 需要深入源码 + 场景推演 | 1d | 红色 |

### 答题结构规范

每道题的 `.qa-a-inner` 必须包含：

1. **`qa-tag`** — 标注 "参考回答"
2. **一句话概括** — `<p><strong>一句话概括：</strong>...</p>` 展示理解力
3. **深入分析** — `<p><strong>深入分析：</strong>...</p>` 代码层面细节
4. **设计权衡**（可选） — `<p><strong>设计权衡：</strong>...</p>` 展示深度
5. **追问链 `qa-followup`** — 面试官可能的 follow-up，每个 `qa-followup-item` 含 Q + 简答
6. **面试加分 `qa-tip`** — 高于平均水平的理解，联系其他系统/模式

### 追问链规范

每道题至少 2 个追问，hard 题至少 3 个：

```html
<div class="qa-followup">
  <div class="qa-followup-title">🔗 追问链</div>
  <div class="qa-followup-item">
    <span class="qa-followup-q">追问问题？</span>
    <span class="qa-followup-a">→ 简明回答</span>
  </div>
  <div class="qa-followup-item">
    <span class="qa-followup-q">再追问？</span>
    <span class="qa-followup-a">→ 简明回答</span>
  </div>
</div>
```

## 面试答题策略（面试突击模式专用）

### STAR 法则

| 要素 | 含义 | 面试应用 |
|------|------|---------|
| **S**ituation | 项目背景 | "我们的 Coding Agent 需要..." |
| **T**ask | 你的任务 | "我负责设计 Agent Loop 的安全层" |
| **A**ction | 具体做法 | "我设计了三级风险模型，用策略模式解耦..." |
| **R**esult | 结果/收益 | "上线后工具调用拒绝率降到 5%，无安全事故" |

### 答题模板

```
面试官问: "XXX 怎么实现的？"

Level 1 回答（及格线）:
"我们用了 XXX 来实现 YYY。"

Level 2 回答（良好）:
"我们用了 XXX 来实现 YYY。因为 ZZZ 的原因，
我们没有选择 AAA 方案。主要代码在 xxx.go 里。"

Level 3 回答（优秀）:
"我们用了 XXX 来实现 YYY。
核心原理是...（展示源码理解）。
当时在 XXX 和 AAA 之间权衡，选 XXX 是因为...。
上线后遇到了...问题，通过...解决了。
如果重来一次，我会...（展示反思能力）。"
```

### 不同题型的应对策略

| 题型 | 应对策略 | 常见陷阱 |
|------|---------|---------|
| 项目介绍 | 30 秒版本 → 2 分钟版本 → 5 分钟版本 | 不要流水账，要突出亮点 |
| 深度追问 | 先概括 → 再细节 → 最后升华 | 不要背代码，要讲设计思路 |
| 场景拷打 | 先分析影响 → 再给方案 → 最后评估 | 不要慌，先确认边界条件 |
| 系统设计 | 先理清需求 → 再画架构 → 最后说取舍 | 不要一步到位，先 MVP 再迭代 |
| 代码走读 | 先说意图 → 再说实现 → 最后说改进 | 不要只说"代码怎么写"，要说"为什么这样写" |
| 权衡分析 | 两边都说 → 比较优劣 → 结合场景选择 | 不要只说一方好，要展示辩证思维 |

## 数据流动画

在 `.dg` 架构图外包一层 `.flow-anim`，用户点 "下一步" 逐步高亮节点：

```html
<div class="flow-anim" data-steps='[
  {"highlight":"handler","label":"请求进入 HTTP Handler，解析参数"},
  {"highlight":"service","label":"Handler 调用 Service 层处理业务逻辑"},
  {"highlight":"repo","label":"Service 通过 Repository 访问数据层"},
  {"highlight":"db","label":"Repository 执行 SQL 查询并返回结果"}
]'>
  <!-- 复用现有 dg 组件，节点加 data-flow-id -->
  <div class="dg">
    <div class="dg-layer">
      <div class="dg-node nc-cyan" data-flow-id="handler">Handler<span class="sub">入口层</span></div>
    </div>
    <div class="dg-arr">↓</div>
    <div class="dg-layer">
      <div class="dg-node nc-purple" data-flow-id="service">Service<span class="sub">业务层</span></div>
    </div>
    <div class="dg-arr">↓</div>
    <div class="dg-layer">
      <div class="dg-node nc-green" data-flow-id="repo">Repository<span class="sub">数据层</span></div>
    </div>
    <div class="dg-arr">↓</div>
    <div class="dg-layer">
      <div class="dg-node nc-amber" data-flow-id="db">Database<span class="sub">存储</span></div>
    </div>
  </div>
  <div class="flow-label">点击「下一步」开始追踪</div>
  <div class="flow-controls">
    <button class="flow-btn flow-next-btn">下一步</button>
    <button class="flow-btn flow-reset-btn">重置</button>
    <span class="flow-counter">0 / 4</span>
  </div>
</div>
```

## 找 Bug 挑战

展示真实代码，用户点击有问题的那一行：

```html
<div class="bug-challenge" data-explain="这里并发写 map 会 panic，Go 的 map 不是线程安全的。应该用 sync.Mutex 或 sync.Map。">
  <div class="bug-header"><span class="bug-icon">🔍</span><span>找出这段代码的并发问题</span></div>
  <div class="bug-code">
    <div class="bug-line" onclick="checkBugLine(this,false)">
      <span class="line-num">1</span><code>var m = make(map[string]int)</code>
    </div>
    <div class="bug-line" onclick="checkBugLine(this,false)">
      <span class="line-num">2</span><code>var wg sync.WaitGroup</code>
    </div>
    <div class="bug-line bug-target" onclick="checkBugLine(this,true)">
      <span class="line-num">3</span><code>go func() { m[&quot;key&quot;] = 42 }()</code>
    </div>
    <div class="bug-line" onclick="checkBugLine(this,false)">
      <span class="line-num">4</span><code>wg.Wait()</code>
    </div>
  </div>
  <div class="bug-feedback"></div>
</div>
```

## 术语悬浮提示（面试版）

关键术语用 `.term` 包裹，悬浮显示面试话术：

```html
<p>我们用了
<span class="term" data-definition="面试话术：'我们用 sync.Pool 复用对象，减少 GC 压力。高峰期 P99 降低了 40ms。'">sync.Pool</span>
来复用对象。
</p>
```

> 不需要标基础概念（如 API、变量），只标**项目特有术语**和**面试高频概念**。

## 文件树可视化

"介绍一下你的项目结构" 面试必问题：

```html
<div class="file-tree">
  <div class="ft-folder open">
    <button class="ft-toggle" onclick="this.parentElement.classList.toggle('open')">▶</button>
    <span class="ft-name">internal/</span>
    <span class="ft-desc">核心业务逻辑</span>
    <div class="ft-children">
      <div class="ft-file">
        <span class="ft-name">handler.go</span>
        <span class="ft-desc">HTTP 入口，参数校验 + 路由</span>
      </div>
      <div class="ft-file">
        <span class="ft-name">service.go</span>
        <span class="ft-desc">业务编排层，面试重点</span>
      </div>
    </div>
  </div>
  <div class="ft-folder">
    <button class="ft-toggle" onclick="this.parentElement.classList.toggle('open')">▶</button>
    <span class="ft-name">pkg/</span>
    <span class="ft-desc">可导出的公共库</span>
    <div class="ft-children">
      <div class="ft-file">
        <span class="ft-name">logger.go</span>
        <span class="ft-desc">日志工具</span>
      </div>
    </div>
  </div>
</div>
```

> ⚠ 注意：`.ft-folder` 默认不展开，必须加 `open` class 才会显示子项。CSS 规则 `.ft-folder:not(.open) > .ft-children { display: none; }` 控制折叠。

## 文件结构

```
tech-deep-dive/
├── SKILL.md              ← 你正在读（核心工作流 + 组件指南）
├── template.html         ← HTML 骨架模板（直接复制填充）
└── references/
    └── design-guide.md   ← 5 种替代主题 + 高级图示组件（按需查阅）
```

## 快捷键

| 快捷键 | 功能 |
|--------|------|
| `S` | 切换幻灯片/滚动模式 |
| `T` | 切换 TOC 目录 |
| `Ctrl+K` | 全文搜索 |
| `ESC` | 关闭搜索 |
| `←` / `→` | 幻灯片翻页 |

## 主题切换（可选）

默认 Midnight Neon（已在 `template.html` 内）。用户要求换主题时，读取 `references/design-guide.md`，替换生成文件中的 `:root` CSS 变量即可。
