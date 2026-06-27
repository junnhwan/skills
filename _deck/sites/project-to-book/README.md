# Project to Book Skill

Transform any vibe-coded project into an interview preparation book (VitePress website).

## When to Use

- You have a project you built with AI assistance and want to deeply understand it
- You need to prepare for technical interviews about your project
- You want to create a knowledge base from source code
- You need a documentation site for a project

## Trigger Phrases

- "把这个项目做成一本书来准备面试"
- "Create interview prep materials for this project"
- "为这个项目生成源码走读"
- "Build a VitePress site for project documentation"
- "Generate technical interview questions from source code"

## What It Does

1. **Deep Source Analysis** — Launches parallel subagent tasks to read every module
2. **Interview Questions** — Generates 6-10 questions per category with code citations
3. **Source Walkthrough** — Creates line-by-line analysis of core modules
4. **VitePress Site** — Builds a complete searchable website

## Output Structure

```
book/
├── package.json
├── .vitepress/
│   ├── config.mts
│   └── theme/index.ts
└── docs/
    ├── index.md
    ├── interview/
    │   ├── fundamentals/
    │   ├── [category-1]/
    │   └── [category-2]/
    ├── source/
    │   ├── [module-1]/
    │   └── [module-2]/
    └── practice/
```

## Example Usage

```
User: 我有一个 Go 项目，想做成一本书来准备面试
Agent: [Loads project-to-book skill]
       [Analyzes source code]
       [Creates VitePress site with interview questions and walkthroughs]
```

## Key Features

- Every answer cites specific source code with file:line references
- Parallel analysis for fast execution
- VitePress with search, dark mode, mobile responsive
- Customizable categories and structure
