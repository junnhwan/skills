#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
from collections import defaultdict
from pathlib import Path
from typing import Iterable


IGNORE_DIRS = {
    ".git",
    ".idea",
    ".vscode",
    ".next",
    ".nuxt",
    ".run",
    ".venv",
    "bench",
    "bin",
    "bower_components",
    "coverage",
    "frontend",
    "htmlcov",
    "logs",
    "node_modules",
    "out",
    "results",
    "tmp",
    ".gradle",
    ".mypy_cache",
    ".pytest_cache",
    "__pycache__",
    "build",
    "dist",
    "target",
    "vendor",
    "venv",
}

BINARY_EXTENSIONS = {
    ".7z",
    ".bin",
    ".class",
    ".dll",
    ".exe",
    ".gif",
    ".gz",
    ".ico",
    ".jar",
    ".jpeg",
    ".jpg",
    ".mp4",
    ".pdf",
    ".png",
    ".tar",
    ".webp",
    ".zip",
}

LANGUAGE_EXTENSIONS = {
    ".java": "Java",
    ".go": "Go",
    ".py": "Python",
    ".kt": "Kotlin",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".tsx": "TypeScript",
    ".jsx": "JavaScript",
    ".sql": "SQL",
}

DEPENDENCY_FILES = {
    "pom.xml",
    "build.gradle",
    "build.gradle.kts",
    "go.mod",
    "requirements.txt",
    "pyproject.toml",
    "package.json",
}

CONFIG_PATTERNS = (
    "application.yml",
    "application.yaml",
    "application.properties",
    "bootstrap.yml",
    "bootstrap.yaml",
    "docker-compose.yml",
    "docker-compose.yaml",
    ".env",
)

TECH_PATTERNS = {
    "Spring": re.compile(r"\bSpring|spring-boot|@RestController|@Service|@Configuration", re.I),
    "MyBatis": re.compile(r"mybatis|Mapper\b|MyBatis-Plus|BaseMapper", re.I),
    "Redis": re.compile(r"\bRedis|Redisson|StringRedisTemplate|RedisTemplate|RBucket|RLock", re.I),
    "RocketMQ": re.compile(r"RocketMQ|rocketmq|DefaultMQ|@RocketMQMessageListener", re.I),
    "Kafka": re.compile(r"\bKafka\b|kafka", re.I),
    "RabbitMQ": re.compile(r"RabbitMQ|amqp", re.I),
    "MySQL": re.compile(r"\bMySQL\b|jdbc:mysql|CREATE TABLE|ENGINE=InnoDB", re.I),
    "PostgreSQL": re.compile(r"PostgreSQL|postgres|jdbc:postgresql", re.I),
    "MongoDB": re.compile(r"MongoDB|mongoTemplate|mongoose", re.I),
    "MinIO": re.compile(r"MinIO|minio", re.I),
    "LLM": re.compile(r"OpenAI|LangChain|DeepSeek|LLM|大模型|embedding|RAG|SSE", re.I),
    "RateLimit": re.compile(r"rate.?limit|令牌桶|限流|RateLimiter|Bucket", re.I),
    "Auth": re.compile(r"JWT|OAuth|Spring Security|authentication|authorization|鉴权", re.I),
}

API_PATTERNS = re.compile(
    r"@(?:RestController|Controller|RequestMapping|GetMapping|PostMapping|PutMapping|DeleteMapping)|"
    r"\b(router|routes?)\.|gin\.|FastAPI|Flask|express\(",
    re.I,
)


def iter_files(root: Path, max_files: int) -> Iterable[Path]:
    yielded = 0
    for current_root, dirs, files in os.walk(root):
        dirs[:] = [name for name in dirs if name not in IGNORE_DIRS]
        for file_name in files:
            path = Path(current_root) / file_name
            if path.suffix.lower() in BINARY_EXTENSIONS:
                continue
            yield path
            yielded += 1
            if yielded >= max_files:
                return


def safe_read(path: Path, max_bytes: int = 256_000) -> str:
    try:
        data = path.read_bytes()[:max_bytes]
        return data.decode("utf-8", errors="ignore")
    except OSError:
        return ""


def relative(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root)).replace("\\", "/")
    except ValueError:
        return str(path)


def classify_files(root: Path, max_files: int) -> dict:
    languages: set[str] = set()
    dependency_files: list[str] = []
    source_files: list[str] = []
    config_files: list[str] = []
    schema_files: list[str] = []
    api_files: list[str] = []
    technology_hits: dict[str, list[str]] = defaultdict(list)

    scanned_files = 0

    for path in iter_files(root, max_files=max_files):
        scanned_files += 1
        rel = relative(path, root)
        name = path.name
        suffix = path.suffix.lower()

        if suffix in LANGUAGE_EXTENSIONS:
            languages.add(LANGUAGE_EXTENSIONS[suffix])

        if name in DEPENDENCY_FILES:
            dependency_files.append(rel)

        if suffix in {".java", ".go", ".py", ".kt", ".js", ".ts", ".tsx", ".jsx"}:
            source_files.append(rel)

        if name in CONFIG_PATTERNS or suffix in {".yml", ".yaml", ".properties", ".toml"}:
            config_files.append(rel)

        if suffix == ".sql" or "migration" in rel.lower() or "schema" in rel.lower():
            schema_files.append(rel)

        text = safe_read(path)
        if text and API_PATTERNS.search(text):
            api_files.append(rel)

        searchable = f"{rel}\n{text}"
        for tech, pattern in TECH_PATTERNS.items():
            if pattern.search(searchable):
                technology_hits[tech].append(rel)

    return {
        "scanned_files": scanned_files,
        "scan_limit": max_files,
        "languages": sorted(languages),
        "dependency_files": sorted(dependency_files),
        "source_files": sorted(source_files)[:300],
        "config_files": sorted(set(config_files))[:200],
        "schema_files": sorted(set(schema_files))[:200],
        "api_files": sorted(set(api_files))[:200],
        "technology_hits": {key: sorted(set(value))[:50] for key, value in sorted(technology_hits.items())},
    }


def detect_project(root: Path, max_files: int) -> dict:
    readmes = sorted(relative(path, root) for path in root.glob("README*") if path.is_file())
    docs = []
    if (root / "docs").exists():
        docs = sorted(relative(path, root) for path in iter_files(root / "docs", max_files=200))
    result = {
        "project_root": str(root),
        "readme_files": readmes,
        "doc_files": docs[:100],
    }
    result.update(classify_files(root, max_files=max_files))
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect a backend project for interview-prep evidence.")
    parser.add_argument("project_path", help="Path to the project root")
    parser.add_argument("--max-files", type=int, default=1500, help="Maximum non-ignored files to inspect")
    args = parser.parse_args()

    root = Path(args.project_path).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        parser.error(f"project path is not a directory: {root}")

    print(json.dumps(detect_project(root, max_files=args.max_files), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
