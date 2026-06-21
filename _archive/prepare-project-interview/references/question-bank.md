# Project Interview Question Bank

Use these questions for document generation or Mock interview. Ask one question at a time in mock mode.

## Project Overview

- Explain this project in 2 minutes without listing technologies.
- What real problem does it solve?
- Which part is the core backend value?
- What did AI generate, and what decisions did you personally make?
- Which feature would fail first if traffic doubled?
- What is implemented now, and what is only a future plan?

## AI Coding

- How did you use AI without losing control of the project?
- Give one case where AI proposed multiple options and you rejected one.
- How did you verify AI-generated code?
- What hallucination or wrong API did AI produce?
- If an interviewer says "this project was all AI-written", how do you respond honestly?
- What project documents did you maintain to keep AI context stable?

## Architecture Flow

- Walk through one request from entry to final response.
- Which data is stored in memory, cache, database, and external storage?
- Where are the transaction or consistency boundaries?
- What happens when the user retries the same operation?
- Which parts are synchronous and which are asynchronous?
- How does the frontend know long-running work is complete?

## Redis

- Why use Redis instead of MySQL for this state?
- Which Redis data structures are used?
- What key format and TTL strategy did you choose?
- What happens if Redis loses data?
- How do you prevent hot keys or cache penetration?
- What would change if this moved from single instance to cluster?

## RocketMQ

- Why use RocketMQ instead of a local thread pool?
- What delivery guarantee do you rely on?
- How do you handle duplicate consumption?
- What happens if sending succeeds but consuming fails?
- How do you handle message accumulation?
- How many queues and consumers would you configure, and why?

## Cache

- How do you handle cache penetration, breakdown, and avalanche?
- What happens if DB has data but cache does not?
- What happens if cache has data but DB write failed?
- Why choose logical expiration, mutex rebuild, or null caching?
- How do you verify cache consistency?

## Locks and Idempotency

- Why use a distributed lock instead of a local lock?
- Why use Redisson instead of raw SETNX?
- What is WatchDog, and when is it actually necessary?
- What is the lock granularity?
- How do you release locks safely?
- What is the idempotency key?
- Could a unique database index be a better idempotency guard?

## Rate Limiting

- Why does this project need rate limiting?
- Token bucket vs leaky bucket vs sliding window: which fits?
- Why use Lua for Redis rate limiting?
- What does the frontend receive when limited?
- What metric tells you the limit is too strict?

## Database

- What are the main tables?
- Which indexes matter most?
- What would cause slow queries?
- Where do you need transactions?
- How do you handle concurrent updates?
- What data should not be stored in Redis long term?

## Failure Drills

- DB write fails after an expensive API call succeeds. What now?
- MQ retries three times and still fails. What now?
- Service crashes while holding a lock. What now?
- Third-party API is unstable for 30 minutes. What now?
- User uploads or submits the same data repeatedly. What now?
- Config is wrong in production. How would you detect it?

## Observability

- Which metrics would you alert on first?
- What logs prove a request's full chain?
- How would you trace one task ID across services?
- What are your P95/P99 latency bottlenecks?
- What dashboard would you build before going online?

## RAG

- Why would this project need RAG instead of keyword search?
- How do chunk size and overlap affect retrieval?
- What if retrieval returns zero results?
- What if retrieved context conflicts with model knowledge?
- How do you reduce hallucination?
- What metrics evaluate answer quality?

## SSE

- Why choose SSE instead of WebSocket?
- What HTTP headers and message format does SSE use?
- Can SSE support multi-turn LLM chat?
- What happens when the client disconnects?
- How do you handle retry or resume?

## Scaling and Evolution

- What is the simplest next improvement?
- What is the riskiest technical debt?
- Which feature would you remove or simplify?
- How would you migrate from a demo project to production?
- Which claim on the resume is most likely to be challenged?
