# Session Prompt and Output Contract

Use this reference when the user wants a copyable prompt or when a project-preparation session needs a stable output format.

## Copyable Prompt

```text
请使用 project-defense-coach 的方式，帮我深入学习并准备这个项目的简历和面试防守。

项目路径：<填项目路径>

我的背景：
- 我是大二升大三学生，准备后端 / Agent 开发 / AI 应用开发实习。
- 这个项目主要是 AI 辅助 vibe coding 完成的，我能运行，但还没有系统理解。
- 目标不是包装项目，而是搞清楚它真实实现了什么、为什么这样设计、哪些地方我能在面试里安全地说，哪些地方不能硬说。

请按下面流程做：

1. 先审计项目证据
   - 阅读 README、依赖文件、入口文件、核心源码、配置、数据库/缓存/消息队列/AI 调用相关代码、测试。
   - 不要先写简历话术。
   - 每个重要结论都要引用具体文件路径或代码证据。

2. 把所有项目说法分成三类
   - 已实现事实：代码、配置、测试或文档能证明。
   - 合理推断：从代码能推测设计意图，但没有完整实现。
   - 面试不要硬说：没有证据、实现很薄、容易被追问击穿。

3. 生成项目学习地图
   - 项目解决什么问题。
   - 核心业务链路是什么。
   - 请求从入口到返回经历了哪些模块。
   - 数据如何流动。
   - 用到了哪些后端 / AI / Agent 技术点。
   - 每个技术点为什么出现，不要只罗列技术栈。

4. 做技术选型和 tradeoff 拷打
   - 为什么选这个方案。
   - 替代方案有哪些。
   - 当前方案什么时候会不适合。
   - 如果并发、数据量、失败率上升，会先坏在哪里。
   - 有哪些边界兜底、重试、幂等、一致性、降级方案。

5. 补齐相关八股知识
   - 只讲和这个项目有关的八股。
   - 每个知识点都要绑定到项目场景。
   - 包括但不限于：数据库索引、事务、缓存一致性、Redis、MQ、分布式锁、幂等、限流、SSE、RAG、Agent 工具调用、LLM 结构化输出、成本控制、可观测性。

6. 生成面试材料
   - 2 分钟项目介绍。
   - 简历 bullet，必须基于已实现事实或明确标注合理推断。
   - 核心技术难点表。
   - 高频追问 Q&A。
   - 故障拷打题。
   - 学习清单：我接下来应该补哪些知识、看哪些代码、做哪些小改造。

7. 最后进行 mock interview
   - 一次只问一个问题。
   - 根据我的回答继续追问。
   - 指出我哪里概念不清、哪里没有项目证据、哪里说法风险太高。
```

## Evidence Ledger

| Claim | Label | Evidence | Interview Risk |
| --- | --- | --- | --- |
| Short factual claim | 已实现事实 / 合理推断 / 面试不要硬说 | File path, config, schema, test, or command | Low / Medium / High |

## Learning Checklist

| Priority | Topic | Why it matters for this project | How to learn | Project exercise |
| --- | --- | --- | --- | --- |
| P0/P1/P2 | Concrete concept | Project-specific reason | Resource or experiment | Small implementation task |

