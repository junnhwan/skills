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
<aside class="note pip-clear animate" style="--i: 7; margin-top: 28px">
  <span class="label">关键设计</span>
  <p>这条链路里最值得注意的点：事务边界收敛在 Service 层。</p>
</aside>
```

- `label`：等宽小字标签（绿色）。
- `pip-clear`：让 note 不受画中画布局约束、占满宽度。**笔记框都加上它**。

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

贴源码片段 / 命令 / 配置佐证。

```html
<div class="code-block animate" style="--i: 3"><span class="c-comment">// 事务边界收敛在 Service</span>
func (s *OrderService) Create(ctx, cmd) (*Order, error) {
    return s.tx.Do(ctx, func(tx) error {
        ...
    })
}</div>
```

- `c-comment`：注释高亮（淡色）。
- 代码里若有 `<` `>` `&`，记得转义成 `&lt;` `&gt;` `&amp;`。
- 行内代码用 `<code class="inline-code">…</code>`（表格里常用）。

---

## Cover 页专用组件

Cover 用 `.title`（不是 slide-title）、`.lead.hero-lead`、`.hero-meta`、`.chips`。完整结构见 `templates.md` 的 Cover 模板。
