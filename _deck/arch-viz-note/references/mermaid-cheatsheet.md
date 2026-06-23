# mermaid 速查（架构/依赖/树）

只收录做结构型笔记最常用的几种。完整文档见 mermaid 官网。

## 0. 语义配色（对齐项目手绘 SVG 风格）

模板已为每张 **flowchart / graph** 图**自动注入**下面的 classDef，节点直接写 `X:::cls` 就能上色，无需自己声明：

| class | 色系 | 含义 | 何时用 |
|---|---|---|---|
| `core` | 蓝 | 核心模块 | 系统主力能力 |
| `emph` | 橙 | 重点 / 唯一 | 唯一调度者、关键枢纽、想强调的节点 |
| `new` | 绿 | 新增 / 扩展 | 新引入、可裁剪、对比中的"新"侧 |
| `dim` | 灰 | 沿用 / 保留 | 旧结构、最小闭环、弱化 |
| `data` | 灰虚 | 持久化 / 数据 | 存储、审计、JSONL、外部依赖 |

这套配色直接取自项目里手绘 SVG 的语义体系（蓝主 / 绿新增 / 橙强调 / 灰保留），让自动布局的 mermaid 图也有同样的"一眼看懂轻重"。

**增量叙事**（项目手绘 SVG 最该学的手法）：一张图里混用 `dim`（旧的、保留）+ `new`（新增的），再配 `legend` 字段，就是"灰=保留 / 绿=新增"的叠加叙事——讲架构演进、最小闭环 vs 扩展层时特别好用。

节点上色：
```
flowchart TD
  LOOP["agent.Loop"]:::emph
  TOOL["tool"]:::core
  SESS["session"]:::data
```

图例（`DATA.diagrams[].legend`，可选，渲染成图下方色块条）：
```js
legend: [
  { cls:"emph", text:"唯一调度者 agent.Loop" },
  { cls:"new",  text:"扩展能力（可裁剪）" },
]
```

> classDef 只对 **flowchart / graph** 生效。`classDiagram` / `mindmap` / `erDiagram` 不注入（语法不同），用各自原生样式。

---

## 1. 分层架构（`flowchart TD` + subgraph）

最常用。用 `subgraph` 划层，箭头表调用方向。subgraph 用 `id["标题"]` 形式，避免中文标题当 id 出问题。

```
flowchart TD
  subgraph L1["展示层"]
    TUI["TUI"]
  end
  subgraph L2["应用层"]
    APP["app"]
  end
  TUI --> APP
  APP --> LOOP["agent.Loop"]:::emph
```

- `TD` = 自上而下；`LR` = 自左而右。
- `["..."]` 给节点显式文案；不带就是 id 本身。
- `-->` 实线箭头；`---` 无箭头；`-.->` 虚线；`A -. 文字 .-> B` 虚线带标签。

## 2. 模块/包依赖图（`flowchart LR`）

横排更适合"谁依赖谁"。配合 `dim`/`new` 区分"沿用核心"与"新增能力"。

```
flowchart LR
  agent:::dim --> llm:::dim
  agent --> tool:::dim
  tool --> safety:::dim
  subagent:::new
  agent --> subagent
  subagent -. 受限回环 .-> agent
```

- `%%` 行注释。
- 标注边：`agent -- 调用 --> tool` 或 `agent -->|调用| tool`。

## 3. 目录树（`flowchart TD` 或 `mindmap`）

```
flowchart TD
  root["bond-code/"] --> cmd["cmd/"]
  root --> internal["internal/"]
  internal --> agent["agent/"]
  internal --> tool["tool/"]
```

mindmap 更像树（注意：不支持 classDef）：
```
mindmap
  root((bond-code))
    cmd
    internal
      agent
      tool
```

## 4. 组件/实体关系（`classDiagram` 或 `erDiagram`）

```
classDiagram
  class Loop { +Run() +Stream() }
  class Policy { +Decide() }
  Loop --> Policy : 每次工具调用前问
```

> classDiagram 不注入语义 classDef，用其原生样式。

## 5. 常见坑

1. **特殊字符**：节点文案含 `()` `/` 等要用引号包：`A["pkg/sub"]`。
2. **语法错图不渲染**：浏览器控制台报错行号，先单独验证文本。
3. **节点太多**：>25 个 dagre 布局会乱，拆成多张图。
4. **方向选错**：层级深用 `TD`，依赖宽用 `LR`。
5. **classDef 只认 flowchart/graph**：给 `classDiagram`/`mindmap` 加 `:::` 会语法报错。
