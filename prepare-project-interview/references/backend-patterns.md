# Backend Engineering Patterns for Project Interviews

Use this as a compact explanation guide. Do not force patterns into projects where there is no evidence.

## Async Processing with MQ

**Scenario:** Long-running work, bursty traffic, expensive external calls, or work that can finish after the HTTP response.

**Why it matters:** It releases request threads, smooths traffic spikes, and gives retry/dead-letter mechanisms.

**Alternatives:** Synchronous call, local thread pool, scheduled job, workflow engine.

**Failure modes:** Message send failure, duplicate consumption, accumulation, consumer crash, poison messages.

**Interview caution:** Do not claim MQ is needed for every async task. If local thread pool is enough, explain why MQ is for durability, retry, and decoupling.

## Distributed Lock

**Scenario:** Multiple instances may process the same business key concurrently, causing duplicate work or inconsistent state.

**Why it matters:** It coordinates cross-instance concurrency when local locks are insufficient.

**Alternatives:** Database unique index, optimistic lock, idempotency table, Redis SETNX, Redisson, ZooKeeper/etcd.

**Failure modes:** Lock expiration before work finishes, forgotten unlock, process crash, lock key too coarse, lock key collision.

**Interview caution:** Redisson WatchDog is useful for uncertain long-running tasks. For short operations, a unique index or raw SETNX may be simpler.

## Idempotency

**Scenario:** Retries, duplicate MQ delivery, repeated user clicks, network timeouts, or payment/API callbacks.

**Why it matters:** At-least-once systems require business-layer duplicate defense.

**Alternatives:** Unique index, request token, business key status check, Redis SETNX, dedup table.

**Failure modes:** Key not stable, status check race, partial success, TTL expires too early.

**Interview caution:** "I used a lock" is not enough. Explain the idempotency key and the final data guard.

## Redis Cache

**Scenario:** High-read data, temporary state, distributed counters, upload chunks, sessions, rate limiter buckets.

**Why it matters:** Redis reduces database pressure and provides fast atomic operations/data structures.

**Alternatives:** MySQL, local cache, Caffeine, in-memory map, object storage metadata.

**Failure modes:** Cache penetration, breakdown, avalanche, stale data, memory pressure, hot key, Redis outage.

**Interview caution:** Explain why the data belongs in Redis and how it recovers if Redis data disappears.

## Cache Consistency

**Scenario:** The same data exists in DB and cache.

**Why it matters:** Users may observe stale or missing data if updates are not coordinated.

**Alternatives:** Update DB then delete cache, cache-aside, logical expiration, delayed double delete, MQ compensation, CDC.

**Failure modes:** Cache delete failure, DB write failure, old value written back after delete, concurrent updates.

**Interview caution:** Prefer eventual consistency language unless there is a real transaction or strong consistency mechanism.

## Rate Limiting

**Scenario:** Protect APIs, third-party token budget, expensive AI calls, upload bandwidth, login attempts, or scraping targets.

**Why it matters:** It preserves availability under abuse or spikes.

**Alternatives:** Token bucket, leaky bucket, fixed window, sliding window, gateway rate limit, per-user quota.

**Failure modes:** Non-atomic counters, unfair limits, too strict thresholds, Redis outage, no frontend feedback.

**Interview caution:** Tie the algorithm to the business goal: burst tolerance, smooth output, or strict per-window cap.

## File Upload and Resume

**Scenario:** Large files, weak network, uploads that can fail near completion.

**Why it matters:** Chunking avoids restarting from zero and reduces user pain.

**Alternatives:** Direct upload, multipart upload, object storage presigned URLs, client-side retry, server-side merge.

**Failure modes:** Duplicate chunk, missing chunk, concurrent merge, Redis state loss, object storage merge failure.

**Interview caution:** Explain who triggers merge and what prevents multiple merges.

## Database Index and Constraint

**Scenario:** Lookup-heavy services, idempotency, unique business keys, pagination, status queries.

**Why it matters:** Indexes turn repeated table scans into predictable lookups and constraints provide final correctness guards.

**Alternatives:** Redis prefilter, Bloom filter, cache, denormalization, sharding.

**Failure modes:** Missing index, low-selectivity index, write amplification, unique conflict not handled.

**Interview caution:** Mention actual table/field evidence when possible. Do not invent indexes.

## Observability

**Scenario:** Any project expected to run beyond a demo.

**Why it matters:** Logs, metrics, and traces turn "it broke" into a debuggable chain.

**Alternatives:** Structured logs, task IDs, Prometheus metrics, tracing, alerting, dead-letter listeners.

**Failure modes:** No correlation ID, noisy logs, missing failure counters, no alert on DLQ or queue lag.

**Interview caution:** If observability is not implemented, mark it as future evolution.

## RAG

**Scenario:** Users ask natural-language questions over long documents, transcripts, notes, or knowledge bases.

**Why it matters:** Retrieval narrows context and reduces hallucination compared with asking the LLM from memory.

**Alternatives:** Keyword search, MySQL LIKE, Elasticsearch, vector DB, hybrid BM25 + vector + rerank.

**Failure modes:** Bad chunking, low recall, irrelevant retrieval, context too long, embedding mismatch, hallucination.

**Interview caution:** Do not claim RAG if the project only calls an LLM. Mark it as an evolution unless implemented.

## SSE

**Scenario:** Server streams text or progress updates to browser, especially LLM token streaming.

**Why it matters:** It gives simple one-way server-to-client streaming over HTTP.

**Alternatives:** Polling, long polling, WebSocket, HTTP chunked response.

**Failure modes:** Client disconnect, proxy timeout, no retry strategy, no event IDs, server thread/resource pressure.

**Interview caution:** SSE is not full duplex. If the product needs bidirectional real-time collaboration, WebSocket is more suitable.
