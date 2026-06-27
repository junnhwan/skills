# 组件库（Components）

> 组装页面时查这里：每个组件的 HTML 片段 + class + 适用场景。所有 class 都已在 `assets/skeleton.html` 的 CSS 定义，**照抄 class 名即生效**，不用自己写样式。

---

## 页面骨架（每个 slide 都是这个结构）

```html
<section class="slide [dense] [corner-kicker]" data-title="页名" [data-nav="章节名"]>
  <div class="slide-inner">
    <p class="kicker animate" style="--i: 0">Part 1 / 小标题</p>
    <h2 class="slide-title animate" style="--i: 1">页面大标题</h2>
    <!-- 下面放内容组件，--i 从 2 开始递增 -->
  </div>
</section>
```

- `data-title`：**必填**，目录计数靠它。
- `data-nav`：**仅章节起点页**加（目录分组靠它，见 templates.md）。
- `.dense`：内容多时加（表格/对照页）。

---

## 基础文字组件

**kicker** — 页面左上角小标签（章节归属 / 日期）：
```html
<p class="kicker animate" style="--i: 0">Part 2 / 设计</p>
```

**slide-title** — 普通页主标题（h2）：
```html
<h2 class="slide-title animate" style="--i: 1">三个最值得借鉴的设计决策</h2>
```

**lead** — 标题下的引导段落：
```html
<p class="lead animate" style="--i: 2; margin-top: 24px">一段承上启下的话…</p>
```

**chips** — 关键词标签药丸（技术栈 / 主题词）：
```html
<div class="chips animate" style="--i: 4">
  <span class="chip">Go</span>
  <span class="chip">Gin</span>
  <span class="chip">PostgreSQL</span>
</div>
```

---

## 编号卡片（three-col + card）

并列列举 2–4 个要点 / 特性 / 决策。**图文并茂的主力**。

```html
<div class="three-col">
  <article class="card accent-green animate" style="--i: 2">
    <span class="big-number">01</span>
    <h3>分层清晰</h3>
    <p>Handler / Service / Repository 严格分层…</p>
  </article>
  <article class="card accent-blue animate" style="--i: 3">
    <span class="big-number">02</span>
    <h3>配置外置</h3>
    <p>环境差异全部通过配置注入…</p>
  </article>
  <article class="card accent-coral animate" style="--i: 4">
    <span class="big-number">03</span>
    <h3>可观测</h3>
    <p>结构化日志 + 链路追踪…</p>
  </article>
</div>
```

- `accent-*`：`green` / `blue` / `coral` / `lavender`（卡片顶部 4px 彩色条）。轮换着用，别全同色。
- `big-number`：大号衬线编号 01/02/03。
- 两张也行（`.three-col` 会自适应）。

---

## 模块网格（agent-module-map + agent-module）

展示**项目的模块组成 / 分层架构**。每个模块一张小卡。

```html
<div class="agent-module-map">
  <div class="agent-module animate" style="--i: 2">
    <small>API 层</small>
    <strong>路由与中间件</strong>
    <span>处理 HTTP 请求、鉴权、参数校验。</span>
  </div>
  <div class="agent-module animate" style="--i: 3">
    <small>业务层</small>
    <strong>Service</strong>
    <span>核心业务逻辑编排。</span>
  </div>
  <!-- 一般 4–6 个，自动 3 列换行 -->
</div>
```

- `small`：类别/层级（淡色小字）
- `strong`：模块名
- `span`：一句话职责

---

## 流程图（path-step）★ 图文并茂核心

展示**有顺序的流程**：请求链路 / 数据流 / 调用链 / 生命周期。

```html
<div class="agent-module-map"
     style="grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 12px; margin-top: 30px;">
  <div class="path-step animate" style="--i: 2"><strong>① 接收</strong><span>Gin 路由 + 鉴权</span></div>
  <div class="path-step animate" style="--i: 3"><strong>② 校验</strong><span>DTO 绑定校验</span></div>
  <div class="path-step animate" style="--i: 4"><strong>③ 业务</strong><span>Service 编排</span></div>
  <div class="path-step animate" style="--i: 5"><strong>④ 持久化</strong><span>写库 + 缓存</span></div>
  <div class="path-step animate" style="--i: 6"><strong>⑤ 响应</strong><span>封装返回 JSON</span></div>
</div>
```

> **关键**：`path-step` 必须放在**横向多列 grid 容器**里（内联 `grid-template-columns: repeat(步数, minmax(0,1fr))`），步骤间的箭头才横向连接。最后一步的箭头会自动隐藏。步数改 `repeat()` 里的数字即可。

---

## 资料页（two-col + panel/table + diagram/node）

左右分栏：左**表格**（文件结构 / API 对照 / 资源清单），右**竖链节点**（要点递进）。

```html
<div class="two-col">
  <div class="panel animate" style="--i: 2">
    <table class="material-table">
      <thead><tr><th>路径</th><th>职责</th></tr></thead>
      <tbody>
        <tr class="animate" style="--i: 3"><td><code class="inline-code">internal/handler/</code></td><td>HTTP 入口</td></tr>
        <tr class="animate" style="--i: 4"><td><code class="inline-code">internal/service/</code></td><td>业务逻辑</td></tr>
      </tbody>
    </table>
  </div>
  <div class="diagram animate" style="--i: 3">
    <div class="node"><strong>入口很薄</strong><span>Handler 只做 IO 转换。</span></div>
    <div class="node"><strong>业务集中</strong><span>规则收敛到 Service。</span></div>
    <div class="node"><strong>依赖倒置</strong><span>依赖接口非实现。</span></div>
  </div>
</div>
```

- `material-table`：资料表格样式（斑马纹、链接按钮化）。
- `diagram` + `node`：竖向流程，节点间有竖直连接线。`node` 内 `strong`=要点、`span`=说明。
- 这种页通常加 `.dense`。

---

## 笔记框（note）

页面里的补充说明 / 边注 / 「视角变化」类提示。

```html
<aside class="note animate" style="--i: 7; margin-top: 28px">
  <span class="label">关键设计</span>
  <p>这条链路里最值得注意的点：事务边界收敛在 Service 层。</p>
</aside>
```

- `label`：等宽小字标签（绿色）。

---

## 引用（demian-quote-card）

金句 / 设计哲学 / 书摘 / 作者原话。

```html
<blockquote class="demian-quote-card animate" style="--i: 2">
  <p class="demian-quote-text">
    <span class="quote-underline">「把核心设计思想放这里。」</span>
  </p>
  <footer>—— 出处（README / 代码注释 / 作者）</footer>
</blockquote>
```

- `quote-underline`：给引文加下划线强调。
- 常配 `demian-reflection` 反思段（可选）：
```html
<div class="demian-reflection animate" style="--i: 3"><p>为什么这么设计…</p></div>
```

---

## 代码块（code-block）

贴源码片段 / 命令 / 配置佐证。**默认自动语法高亮**（highlight.js，纸质低饱和配色）。

两种写法：

**① 自动高亮（推荐）**——直接写纯文本代码，可选 `data-lang` 指定语言（不写则自动检测）：
```html
<div class="code-block animate" data-lang="go" style="--i: 3">// 事务边界收敛在 Service
func (s *OrderService) Create(ctx, cmd) (*Order, error) {
    return s.tx.Do(ctx, func(tx) error {
        // ...
    })
}</div>
```

**② 手动标记**——需要精确控制配色时，用 `<span class="c-comment">` 包注释。**一旦 code-block 内有任何子元素，自动高亮会跳过整段**，按你手写的标记渲染：
```html
<div class="code-block animate" style="--i: 3"><span class="c-comment">// 手动注释</span>
其余代码纯文本…</div>
```

- `data-lang`：语言名（go / js / python / bash / sql …），命中 highlight.js 支持的语言。
- 配色：关键字 `--blue`、字符串 `--green`、注释 `--faint`、数字 `--coral`（纸质低饱和，不刺眼）。
- 无网络加载不到 highlight.js 时，降级为纯墨色等宽，仍可读。
- 代码里的 `<` `>` `&` 仍建议转义成 `&lt;` `&gt;` `&amp;`，避免被当成 HTML 标签。
- 行内代码用 `<code class="inline-code">…</code>`（表格里常用）。

---

## 系统设计图（mermaid-block）

画时序图 / ER 图 / 类图 / 流程图 / 状态图等**真正的系统设计图**——补齐方框箭头系（path-step / arch）画不了的场景。源码纯文本写进容器，自动渲染成 SVG（纸质主题已注入，与全局配色一致）。

源码直接写在 `.mermaid-block` 里，**保持纯文本，不要加 `<span>` 之类标记**（与 code-block 自动高亮不同，mermaid 要原始文本）：

    <div class="mermaid-block animate" style="--i: 4">sequenceDiagram
      participant U as 用户
      participant S as OrderService
      participant DB as PostgreSQL
      U->>S: 下单
      S->>DB: 事务写入
      S-->>U: 成功</div>

支持的图型（换掉首行关键字与源码即可）：

- `sequenceDiagram` — 时序图，请求链路 / 多方协作（面试最常用）。
- `erDiagram` — ER 图，数据模型与关系。
- `classDiagram` — 类图，领域模型 / 依赖关系。
- `graph LR` / `graph TD` — 流程图，比 path-step 更复杂的分支拓扑。
- `stateDiagram-v2` — 状态机。

要点：

- 加载不到 mermaid（无网络）或语法错时，**降级显示源码**（珊瑚色等宽），不白屏。
- 一页一个图最清爽；图太宽自动横向滚动；大图配 `.dense` 页。
- 语法参考 mermaid 官网（mermaid.js.org）。

---

## Cover 页专用组件

Cover 用 `.title`（不是 slide-title）、`.lead.hero-lead`、`.hero-meta`、`.chips`。完整结构见 `templates.md` 的 Cover 模板。

---

## 章节分隔页（section-divider）

每个「Part」起点用的大字过渡页：拉开层次、给读者喘息。配合 `data-nav` 作为该章节的目录首页。

```html
<section class="slide section-divider" data-title="架构总览" data-nav="架构总览">
  <div class="slide-inner">
    <p class="part-label kicker animate" style="--i: 0">Part 01 / 架构</p>
    <h2 class="part-title animate" style="--i: 1">先看全貌：这个项目由什么组成</h2>
    <p class="part-sub animate" style="--i: 2">一句承上启下的导语。</p>
    <hr class="part-rule animate" style="--i: 3" />
  </div>
</section>
```

- `.section-divider`：加在 `<section class="slide">` 上，启用分隔页布局（垂直居中、更宽内容区）。
- `part-label`：左上小标签（Part 序号 + 主题）。`part-title`：超大衬线主标题。`part-sub`：导语。`part-rule`：珊瑚色短分割线。
- **分隔页通常标 `data-nav`**——它就是这一章的目录首页，后续页只标 `data-title` 成为它的子项。

---

## 面试专用组件（Q&A 卡片 / 架构图 / 深度徽章 / 要点框）

做面试笔记（对齐 `project-grill-prep` 的拷打准备）时用。CSS 已在 `skeleton.html` 内置，照抄 class 即生效。详见 `templates.md` 的「面试笔记五层模板」。

### Q&A 卡片（最核心）

```html
<div class="qa animate" style="--i: 2">
  <p class="qa-q">面试官的问题？</p>
  <span class="qa-mind">一句话写清面试官真正在考察什么，不要写"考察XX能力"这种泛话。</span>
  <p class="qa-a">第一人称话术，像在面试现场说话，不是写技术文档。</p>
</div>
```

- `qa-q`：问题（珊瑚色 `Q` 前缀）。`qa-mind`：🎯 面试官心理（淡灰小字）。`qa-a`：回答（绿色 `A` 前缀）。
- 一个 Q&A 卡片占较大空间，一页放 1–3 个。

### 架构分层图（arch）

画系统拓扑：客户端 → API → MQ → Consumer → 存储，层间带连接线。

```html
<div class="arch">
  <div class="arch-tier">
    <div class="arch-node ag animate" style="--i:2"><strong>组件名</strong><span>职责说明</span><span class="mono">备注/配置</span></div>
    <div class="arch-node ac animate" style="--i:3"><strong>组件名</strong><span>职责说明</span></div>
  </div>
  <div class="arch-arrow animate" style="--i:4"><span class="lbl">层间连接说明（投递 / 消费 / 落盘）</span></div>
  <div class="arch-tier">...更多节点...</div>
</div>
```

- `arch-node` 颜色修饰符：`ag`(绿) / `ac`(珊瑚) / `al`(紫) / `ao`(金)，控制顶部 4px 彩色条。
- `arch-arrow .lbl`：层间带标签的连接线，用于表达数据流向。

### 深度徽章（depth）

```html
<span class="depth green">🟢 深入</span>
<span class="depth yellow">🟡 基本</span>
<span class="depth red">🔴 仅会用</span>
```

标在亮点标题或 Q&A 问题后，表示该点的准备深度。**必须基于真实掌握度校准**——标 🟢 但答不上，比主动说"了解不深"扣分重。

### 要点框（takeaway）

```html
<div class="takeaway animate" style="--i: 6">
  <span class="label">要点 / 钩子</span>
  <p>强调关键结论或埋钩子提示。</p>
</div>
```

和 `note` 类似但蓝色调，用于「关键决策」「话术钩子」等强调。
