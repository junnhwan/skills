---
name: 图解动效笔记
description: |
  生成"单文件 HTML + 数据驱动步进动效图解 + 消息流模拟器"风格的学习笔记。
  复刻 learn.shareai.run 的视觉精髓：SVG 流程图按步高亮发光、messages[] 累加动画、
  播放/单步/倍速控件、明暗主题。当用户想把某个机制/流程/原理做成"像 learn.shareai.run 那样
  会动、会一步步演进"的可视化网页笔记时使用。
trigger_words:
  - 图解笔记
  - 动效笔记
  - 步进图解
  - 流程动图
  - 模拟器笔记
  - 像shareai
  - step viz
  - 交互图解
  - 做成会动的笔记
---

# 图解动效笔记 Skill

生成**单文件 HTML** 的步进式可视化学习笔记。灵感来自 [learn.shareai.run](https://learn.shareai.run/zh)：
用一条**时间轴**同时驱动三件事——SVG 流程图节点/连线高亮发光、`messages[]` 消息流逐条累加滑入、
文字注解同步切换。配播放/单步/倍速/重置控件与明暗主题。

> **定位（与兄弟 skill 的边界）**
> - `note-skill`：手写笔记本风（纸感、装饰、静态）。
> - `tech-deep-dive`：偏文档式交互 HTML。
> - **本 skill**：核心是"**会一步步演的动效图解 + 模拟器**"。三者不互斥，按用户要的视觉选。

---

## 它解决了什么

`learn.shareai.run` 做得精美的关键是两件事：① 每个概念配一张**按步高亮的 SVG 流程图**；
② 一个**逐条演出的消息流模拟器**。但原站是完整 Next.js 工程 + framer-motion + 手写 React 组件，
**无法直接复用到别的主题**。本 skill 把这两件事压缩进**一个 HTML 文件、纯 vanilla JS、零依赖、零构建**，
只靠顶部一个 `DATA` 对象就能换主题。

---

## 模板

```
assets/template.html
```

- 双击即可在浏览器打开，无需 npm / 构建。
- **唯一需要改的是 `<script>` 顶部的 `DATA` 对象**，其余渲染引擎不要动。
- `DATA` 四块：`meta`（标题等）、`diagram`（节点+连线）、`steps`（时间轴）、`content`（正文 markdown）。

---

## 工作流

### Step 1 · 澄清主题
若用户没给全，问三件：① 讲什么机制/流程？② 有几个关键步骤？③ 是否需要"消息流"（对话/调用链），
还是只要流程图？（两者可只要其一，也可都要。）

### Step 2 · 拷贝模板
```bash
mkdir -p "<目标目录>"
cp "<SKILL_ROOT>/assets/template.html" "<目标目录>/index.html"
```

### Step 3 · 填 `DATA`（核心）
按 `references/authoring-guide.md` 的字段说明与示例填：
1. `meta`：标题、副标题、流程图上方那行 mono 标签。
2. `diagram.layout`：**默认设 `"auto"`**——只给节点的 `id/label/type` 和边的 `from/to`，坐标自动算（推荐，省心）。
   想精控位置就去掉 `layout`、给每个节点手填 `x,y,w,h`（适合做精修过的展示图）。
3. `diagram.nodes`：`{id,label,type,end?}`。`type` 为 `rect` 或 `diamond`（菱形=判断）；终止节点加 `end:true`（高亮变紫色）。
4. `diagram.edges`：`{from,to,label?}`。布线按相对位置自动选路由（回环走左、右分支折线、左下 L 形、其余垂直）。
5. `steps[]`：时间轴的每一步。每步可同时指定：
   - `activeNodes` / `activeEdges`：本步点亮哪些（id 形如 `"start"`，边形如 `"from->to"`）。
   - `messages`：本步新增的消息 `{role, detail}`（role 决定颜色：`user`=蓝 / `assistant`·`tool_call`=灰 / `tool_result`=绿 / `end`=紫）。
   - `title` / `desc`：本步文字注解。
   - 想要"只高亮图、无消息"或"只演消息、无图"都行——对应字段留空数组即可。
5. `content`：正文，用极简 markdown（`# ## ###`、`**粗**`、`` `行内码` ``、` ```代码块``` `、`- 列表`、`> 引用`）。

### Step 4 · 自检
- 节点坐标别重叠；`viewBox` 默认 `0 0 500 440`，图超界就调 `diagram-scroll` 会自动出滚动条，或改 viewBox。
- 边的 `label` 会放在边中点，别和节点文字撞。
- `activeEdges` 的 key 必须和 `edges` 里的 `from->to` 完全一致。
- 移动端会自动堆叠为单列。

### Step 5 · 预览 & 迭代
浏览器直接打开。键盘：`←`/`→` 单步，`空格` 播放/暂停。

---

## 设计原则

1. **一条时间轴驱动三视图**：图高亮、消息流、注解同步，不要让三者各走各的。
2. **累加而非替换**：消息是逐步累加的（像真实 agent 跑起来的样子），不是每步全量刷新。
3. **颜色即语义**：蓝=用户/激活、灰=模型/调用、绿=工具结果、紫=终止。不要乱配色。
4. **零依赖单文件**：不引 CDN、不引字体、不引框架。拷出来就能用、能离线、能塞进任何笔记仓库。
5. **克制**：动效服务于理解，节点/步数不要堆。一般 5–8 步最佳。

---

## 资源结构
```
step-viz-note/
├── SKILL.md
├── assets/
│   └── template.html      # 唯一模板（含 DATA 示例：Agent 循环）
└── references/
    └── authoring-guide.md # DATA 字段详解 + 换主题示例
```
**加载顺序**：SKILL.md → 拷 template.html → 读 authoring-guide.md 填 DATA → 自检 → 预览。
