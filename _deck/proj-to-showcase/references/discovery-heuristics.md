# 发现 / 分类 / 排序 启发式

## 1. 流程型特征清单（用来"发现"候选）

一个功能命中下面任意一个模式，就是**流程型候选**，值得画 step-viz 动图：

| 模式 | 高信号代码特征 | 典型节点骨架 |
|---|---|---|
| Agent / LLM 循环 | `while`/`for` 里调模型 + 工具；`stop_reason`/`tool_use` | prompt → model → decide? → tool → append → loop |
| 请求处理链 | handler → middleware → controller → service → DB → response | request → auth → route → handle → DB → response |
| 流水线 | 分 stage 的 map/reduce、`for stage in stages` | ingest → parse → transform → enrich → emit |
| 状态机 | 状态枚举 + transition 表/switch | idle → running → paused → done |
| 编译器/解析器 | lex → parse → analyze → codegen | source → tokens → AST → IR → output |
| 构建/部署/CI | scripts、Makefile、Dockerfile、CI yaml 的步骤序列 | install → build → test → package → deploy |
| 鉴权/会话 | login → issue token → verify → refresh → logout | credentials → verify → token → session |

**发现技巧**：
- 从入口（`main`、`cmd/`、`app.go`、`index.ts`、路由注册处）顺调用链往下找"调度者"。
- 找有 **分支 + 循环 + 多步骤** 的函数，那种"纯计算一个返回值"的函数不是流程。
- README 的"功能特性"列表常直接点出流程型功能。

## 2. 分类闸：流程型 vs 结构型

| 判为**流程型**（进 step-viz） | 判为**结构型**（走 prose / 架构图，**不画动效**） |
|---|---|
| 有明确先后步骤、逐步演进 | 静态的"是什么"而非"怎么跑" |
| 有分支/循环/终止条件 | 模块依赖关系、分层架构 |
| 能画出节点 + 连线的有向图 | 目录地图、配置说明 |
| 一次"运行"能被一步步演出来 | 设计权衡、为什么这么选（ADR） |

**边界例**：
- "用了 local-first 设计" → 结构型（prose）。
- "一次工具调用怎么过安全门" → 流程型（step-viz）。
- "整体模块依赖" → 结构型（mermaid 依赖图）。
- "上下文压缩那一下发生了什么" → 流程型（step-viz）。

拿不准时问一句：**"这个东西能'一步步演出来'吗？"** 能 → 流程型。

## 3. 排序打分

### 有简历：简历匹配分
先从简历抽：
- **硬技能**（语言/框架/工具：Go、React、K8s…）
- **能力 claim**（"做了 X 系统"、"优化了 Y"、"设计了 Z"）
- **目标岗位**关键词

每个流程型候选打分（0–3）：

| 维度 | 0 分 | 3 分 |
|---|---|---|
| **技能命中** | 简历没提相关技术 | 直接命中简历核心技能 |
| **claim 佐证** | 讲清也对简历没加分 | 能直接证明简历里某条 claim |
| **岗位相关** | 跟目标岗位无关 | 正是目标岗位天天干的 |

总分高者优先。**每个挑中的必须写一句"对应简历哪条"**——写不出就降级或丢弃。

### 无简历：重要度分
| 维度 | 说明 |
|---|---|
| 项目核心度 | 是不是这个项目的招牌/主干流程 |
| 教学清晰度 | 步骤是否干净、容易讲明白 |
| 展示惊艳度 | 画出来好不好看、有没有"哇"点 |

## 4. 起草时的准确度自检

每张笔记交付前自问：
- 节点/步骤是不是都来自**真代码**？有没有为了凑数编的？
- 调用链顺序对吗？分支条件对吗？
- 代码符号名（函数/类型/常量）写对了吗？
- `content` 里的代码片段能跟仓库对上吗？

任一项存疑 → 回去读代码，读不通就**不画**。
