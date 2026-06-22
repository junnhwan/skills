# mermaid 速查（架构/依赖/树）

只收录做结构型笔记最常用的几种。完整文档见 mermaid 官网。

## 1. 分层架构（`flowchart TD` + subgraph）

最常用。用 `subgraph` 划层，箭头表调用方向。

```
flowchart TD
  subgraph 展示层
    TUI["TUI"]
  end
  subgraph 应用层
    APP["app"]
  end
  subgraph 运行时
    LOOP["agent.Loop"]
  end
  TUI --> APP --> LOOP
  LOOP --> LLM["llm"]
  LOOP --> TOOL["tool"]
```

- `TD` = 自上而下；`LR` = 自左而右。
- `["..."]` 给节点显式文案；不带就是 id 本身。
- `-->` 实线箭头；`---` 无箭头；`-.->` 虚线。

## 2. 模块/包依赖图（`flowchart LR`）

横排更适合"谁依赖谁"。

```
flowchart LR
  agent --> llm
  agent --> tool
  agent --> safety
  tool --> safety
  subagent --> agent      %% 受限回环
```

- `%%` 行注释。
- 标注边：`agent -- 调用 --> tool` 或 `agent -->|调用| tool`。

## 3. 目录树（`flowchart TD`）

```
flowchart TD
  root["bond-code/"]
  root --> cmd["cmd/"]
  root --> internal["internal/"]
  internal --> agent["agent/"]
  internal --> tool["tool/"]
  internal --> safety["safety/"]
```

或用 `mindmap`（mermaid 支持，更像树）：
```
mindmap
  root((bond-code))
    cmd
    internal
      agent
      tool
      safety
    docs
```

## 4. 组件/实体关系（`classDiagram` 或 `erDiagram`）

类关系：
```
classDiagram
  class Loop { +Run() +Stream() }
  class Policy { +Decide() }
  Loop --> Policy : 每次工具调用前问
```

## 5. 常用样式

- 节点形状：`["矩形"]`、`("圆角")`、`{"菱形"}`、`[("圆柱(DB)")]`、`((圆形))`。
- class 样式：`classDef hit fill:#3b82f6,color:#fff;` 然后 `A:::hit`。
- 给一组节点加样式：`class A,B,C hit;`

## 常见坑

1. **特殊字符**：节点文案里有 `()` `/` 等要用引号包：`A["pkg/sub"]`。
2. **语法错图不渲染**：浏览器控制台报错行号，先单独验证文本。
3. **节点太多**：>25 个 dagre 布局会乱，拆成多张图。
4. **方向选错**：层级深用 `TD`，依赖宽用 `LR`。
