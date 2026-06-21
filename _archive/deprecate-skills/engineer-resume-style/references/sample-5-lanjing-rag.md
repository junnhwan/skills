# 样本 5：蓝鲸校园 RAG 知识库系统

> 来源：用户提供的简历截图（D:\Download\5.png）
> 时间段：2025.12 - 2026.03

## 项目简介

面向校园政策公告检索、学生学习答疑与学习小组知识管理场景，基于 RAG 搭建校园知识库系统，支持大文件上传、文档向量化、混合检索与多轮对话。

## 技术栈

SpringBoot + Spring Security + JWT + MySQL + Redis + Kafka + Elasticsearch + MinIO + WebSocket + MyBatisPlus 等

## 核心亮点

- **权限与文件处理优化**：利用 Spring Security + JWT 实现基于组织标签的 RBAC 多级权限系统，通过用户角色、组织归属和文件属性的权限过滤，实现精细化的文档访问控制，确保敏感数据安全；使用 Redis Bitmap + MinIO 实现分片上传与断点续传，1GB 文件上传耗时由 15s 降至 3s。

- **异步流水线与混合检索**：基于 Kafka 构建上传、解析、向量化异步流水线，文档处理效率提升 3 倍；集成 Elasticsearch + IK + Embedding 构建 KNN + BM25 混合检索并结合 RRF 重排序提升召回效果。

- **流式对话与降级容灾**：基于 WebSocket + LLM Stream API 实现流式响应，使用 Redis 管理会话记忆，并在 Embedding 调用失败时自动降级到关键词检索保障可用性。

---

## 这份样本好在哪（也是和我们要做的项目最像的对照）

- **项目简介一句话讲清"做什么 + 给谁用 + 支持什么"**：场景（校园政策 / 学生答疑 / 学习小组）+ 技术（RAG）+ 能力（大文件、混合检索、多轮对话）。三者打包成一句话，没有"现代化 / 工程化 / 智能化"修辞。

- **3 个亮点恰好覆盖 3 个不同维度**：
  - 权限 + 文件处理（前置层）
  - 异步管线 + 检索（核心层）
  - 对话 + 降级（应用层）

  覆盖全栈但不重复。每条都自成一段、不互相依赖。

- **每条亮点的写法骨架最稳**：
  ```
  主题：基于 X 实现 Y，[具体方案]，[可量化结果或兜底策略]
  ```
  - "基于 Kafka 构建上传/解析/向量化异步流水线，文档处理效率提升 3 倍"
  - "Redis Bitmap + MinIO 实现分片上传与断点续传，1GB 文件上传耗时由 15s 降至 3s"
  - "Embedding 调用失败时自动降级到关键词检索保障可用性"

  数字（3 倍、15s→3s）+ 兜底（自动降级）混合搭配，硬数字和工程素养都有。

- **同一条亮点里把"主路径"和"边角"一并讲完**：第 1 条同时讲了权限（主）和文件分片上传（边）；第 2 条同时讲了异步管线（主）和检索（边）；第 3 条同时讲了流式对话（主）和降级容灾（边）。**主路径 + 兜底/优化** 是最经济的信息密度。

---

## 给类似项目（zhitu-agent-java 阶段 3）的写作迁移启示

我们的阶段 3 跟这份蓝鲸 RAG 高度相似（都是 Kafka + ES + MinIO + RAG 异步管线）。可以直接套这份的骨架：

```
- 异步入库管线：基于 Kafka KRaft 构建上传/解析/向量化异步流水线，HTTP 上传立即返回 202 + uploadId，[TBD：消费 latency 平均 X 秒]；producer 事务 + idempotent + DLT 兜底，consumer 用 ES 主键 chunkId 幂等吃掉 at-least-once 重投递。

- 混合检索：集成 Elasticsearch + IK 分词 + Embedding 构建 KNN + BM25 混合检索并用 RRF 重排序，单次 ES 调用完成召回 + 重排，[TBD：v3 hybrid 比 v2 dense-only 在 holdout 集上 Recall@5 提升 X]。

- 文件处理与权限兜底：MinIO + Tika 实现文档抽取，Redis bitmap 同步入库进度，1GB 文件上传 [TBD：耗时 X 秒]；ES 写失败时降级到 InMemoryKnowledgeStore 保障读路径可用。
```
