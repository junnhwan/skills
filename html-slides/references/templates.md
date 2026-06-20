# 页面模板（Templates）

> 7 种整页骨架，可整段复制后只换文字。所有模板都能在 `assets/skeleton.html` 里直接预览真实效果。配合 SKILL.md 的「内容→模板映射表」决定用哪种。

---

## 编排建议（先看这个）

**典型一篇代码笔记的页面顺序：**

```
① Cover（项目封面）
② module-map（整体架构 / 模块组成）          ← data-nav 标章节
③ path-step（核心数据流 / 请求流程，可多页）
④ 编号卡片（核心设计要点 / 特性，可多页）       ← data-nav 标章节
⑤ 资料页 dense（目录结构 / API 对照 / 关键文件）
⑥ 引用 + 代码（设计哲学 + 源码佐证）           ← data-nav 标章节
⑦ Closing（总结 + 探索方向）
```

**章节划分（`data-nav`）**：每个「Part」的首页加 `data-nav="章节名"`，该章后续页只加 `data-title`。目录会自动生成「00 封面 / 01 架构 / 02 设计 / 03 哲学 / 04 总结」这样的分组。

**规模**：10–25 页为宜。大项目可每个主模块独立成一个 Part（data-nav），内含 cards/dense/quote。

**图文并茂检查**：翻一遍，确保没有连续两页是纯文字——至少交替出现流程图 / 卡片 / 表格 / 代码块之一。

---

## 模板① Cover 开场页

```html
<section class="slide active" data-title="项目概览" data-nav="项目概览">
  <div class="slide-inner">
    <p class="kicker animate" style="--i: 0">2026 / 06 / 20 · v1.0</p>
    <h2 class="title animate" style="--i: 1">{{项目名}}：一句话说清它解决什么问题</h2>
    <p class="lead hero-lead animate" style="--i: 2">
      2–3 句：解决什么问题、核心能力、谁在用。
    </p>
    <div class="chips animate" style="--i: 4">
      <span class="chip">技术栈1</span>
      <span class="chip">技术栈2</span>
      <span class="chip">技术栈3</span>
    </div>
  </div>
</section>
```
注意：Cover 的首屏要带 `active`，标题用 `.title` 不是 `.slide-title`。

---

## 模板② Part 分隔 + 模块网格

```html
<section class="slide corner-kicker" data-title="整体架构" data-nav="整体架构">
  <div class="slide-inner">
    <p class="kicker animate" style="--i: 0">Part 1 / 架构总览</p>
    <h2 class="slide-title animate" style="--i: 1">项目由这几个核心模块组成</h2>
    <div class="agent-module-map">
      <div class="agent-module animate" style="--i: 2"><small>层级</small><strong>模块名</strong><span>职责说明</span></div>
      <!-- 4–6 个 -->
    </div>
  </div>
</section>
```

---

## 模板③ 流程图页（path-step）

```html
<section class="slide dense" data-title="请求处理流程">
  <div class="slide-inner">
    <p class="kicker animate" style="--i: 0">Part 1 / 数据流</p>
    <h2 class="slide-title animate" style="--i: 1">一次请求怎么跑完整条链路</h2>
    <div class="agent-module-map"
         style="grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 12px; margin-top: 30px;">
      <div class="path-step animate" style="--i: 2"><strong>① 步骤</strong><span>说明</span></div>
      <!-- 步数 = repeat() 里的数字 -->
    </div>
    <aside class="note pip-clear animate" style="--i: 7; margin-top: 28px">
      <span class="label">关键设计</span><p>这条链路最值得注意的点。</p>
    </aside>
  </div>
</section>
```

---

## 模板④ 编号卡片页

```html
<section class="slide" data-title="核心设计要点" data-nav="核心设计">
  <div class="slide-inner">
    <p class="kicker animate" style="--i: 0">Part 2 / 设计</p>
    <h2 class="slide-title animate" style="--i: 1">三个最值得借鉴的设计决策</h2>
    <div class="three-col">
      <article class="card accent-green animate" style="--i: 2"><span class="big-number">01</span><h3>标题</h3><p>说明</p></article>
      <article class="card accent-blue animate" style="--i: 3"><span class="big-number">02</span><h3>标题</h3><p>说明</p></article>
      <article class="card accent-coral animate" style="--i: 4"><span class="big-number">03</span><h3>标题</h3><p>说明</p></article>
    </div>
  </div>
</section>
```

---

## 模板⑤ 资料页（表格 + 竖链节点）

```html
<section class="slide dense" data-title="关键目录与职责">
  <div class="slide-inner">
    <p class="kicker animate" style="--i: 0">Part 2 / 目录结构</p>
    <h2 class="slide-title animate" style="--i: 1">关键目录与各自职责</h2>
    <div class="two-col">
      <div class="panel animate" style="--i: 2">
        <table class="material-table">
          <thead><tr><th>路径</th><th>职责</th></tr></thead>
          <tbody>
            <tr class="animate" style="--i: 3"><td><code class="inline-code">path/</code></td><td>说明</td></tr>
          </tbody>
        </table>
      </div>
      <div class="diagram animate" style="--i: 3">
        <div class="node"><strong>要点</strong><span>说明</span></div>
      </div>
    </div>
  </div>
</section>
```

---

## 模板⑥ 引用 + 代码页

```html
<section class="slide dense" data-title="设计哲学" data-nav="设计哲学">
  <div class="slide-inner">
    <p class="kicker animate" style="--i: 0">Part 3 / 哲学</p>
    <h2 class="slide-title animate" style="--i: 1">贯穿项目的核心思想</h2>
    <blockquote class="demian-quote-card animate" style="--i: 2">
      <p class="demian-quote-text"><span class="quote-underline">「核心设计思想。」</span></p>
      <footer>—— 出处</footer>
    </blockquote>
    <div class="code-block animate" style="--i: 3"><span class="c-comment">// 佐证代码</span>
...代码...</div>
  </div>
</section>
```

---

## 模板⑦ Closing 结尾页

```html
<section class="slide" data-title="总结" data-nav="总结">
  <div class="slide-inner">
    <p class="kicker animate" style="--i: 0">Closing</p>
    <h2 class="slide-title animate" style="--i: 1">读完源码，最值得带走的是…</h2>
    <p class="lead animate" style="--i: 2; margin-top: 24px">2–3 句总结 + 可继续探索的方向。</p>
  </div>
</section>
```

---

## 常见组合

- **讲一个模块**：module-map 概览 → path-step 讲它的处理流 → dense 讲关键文件 → quote 讲设计取舍。
- **讲一次请求**：path-step 主线 → 编号卡片讲涉及的 3 个关键设计 → code-block 贴核心实现。
- **对比两种方案**：编号卡片左右对比（两张 card）→ dense 表格列差异 → note 总结取舍。
