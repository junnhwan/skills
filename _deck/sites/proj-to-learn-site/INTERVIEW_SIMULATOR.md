# Interview Simulator — Optional P2 Feature

A dedicated interview practice mode with timer and random question selection.

## What it does

- Random quiz: pull 3 questions from current chapter's markdown
- 30-second countdown per question
- Show reference answer + code location after time's up
- Track score (optional: save to localStorage)

## Implementation

### 1. New route: `src/app/[locale]/interview/[id]/page.tsx`

```tsx
"use client";
import { useState, useEffect } from "react";
import { useParams } from "next/navigation";
import { parseInterviewQuestions } from "@/lib/interview-parser";
import { getDocContent } from "@/lib/docs";

export default function InterviewPage() {
  const { id, locale } = useParams();
  const [questions, setQuestions] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [timeLeft, setTimeLeft] = useState(30);
  const [showAnswer, setShowAnswer] = useState(false);

  useEffect(() => {
    const doc = getDocContent(id as string, locale as string);
    if (doc) {
      const parsed = parseInterviewQuestions(doc.content); // parse "**Q:" from markdown
      const shuffled = parsed.sort(() => Math.random() - 0.5).slice(0, 3);
      setQuestions(shuffled);
    }
  }, [id, locale]);

  useEffect(() => {
    if (timeLeft > 0 && !showAnswer) {
      const timer = setTimeout(() => setTimeLeft(timeLeft - 1), 1000);
      return () => clearTimeout(timer);
    }
  }, [timeLeft, showAnswer]);

  const handleNext = () => {
    setCurrentIndex(currentIndex + 1);
    setTimeLeft(30);
    setShowAnswer(false);
  };

  if (questions.length === 0) return <div>Loading...</div>;
  if (currentIndex >= questions.length) return <div>Done! 🎉</div>;

  const q = questions[currentIndex];

  return (
    <div className="max-w-2xl mx-auto p-8">
      <div className="text-right mb-4">
        <span className={timeLeft < 10 ? "text-red-500" : ""}>
          ⏱ {timeLeft}s
        </span>
      </div>
      <h2 className="text-2xl mb-4">Q{currentIndex + 1}: {q.question}</h2>
      <textarea
        className="w-full h-32 border p-2 mb-4"
        placeholder="在这里输入你的答案..."
        disabled={showAnswer}
      />
      <button
        onClick={() => setShowAnswer(true)}
        className="bg-blue-500 text-white px-4 py-2 rounded"
        disabled={showAnswer}
      >
        显示答案
      </button>
      {showAnswer && (
        <div className="mt-4 border-t pt-4">
          <h3 className="font-bold mb-2">参考答案：</h3>
          <p className="mb-2">{q.answer}</p>
          {q.codeRef && <code className="text-sm text-gray-600">{q.codeRef}</code>}
          {q.antiPattern && (
            <div className="mt-2 bg-yellow-50 p-2 rounded">
              <strong>⚠ 别这么说：</strong> {q.antiPattern}
            </div>
          )}
          <button
            onClick={handleNext}
            className="mt-4 bg-green-500 text-white px-4 py-2 rounded"
          >
            下一题 →
          </button>
        </div>
      )}
    </div>
  );
}
```

### 2. Question parser: `src/lib/interview-parser.ts`

```ts
// Parse "## 面试拷打" section from markdown, extract Q/A pairs
export function parseInterviewQuestions(markdown: string) {
  const section = markdown.match(/## 面试拷打([\s\S]*?)(?=##|$)/)?.[1] || "";
  const questions = [];
  
  // Match patterns like:
  // **Q1: question?**
  // 答：answer
  // > ⚠ 别这么说："anti-pattern"
  const qRegex = /\*\*Q\d+[a-z]?:\s*(.+?)\?\*\*\s*\n答：(.+?)(?=\n>|[\n]{2}|\*\*Q|$)/gs;
  
  for (const match of section.matchAll(qRegex)) {
    const question = match[1].trim();
    const answer = match[2].trim();
    
    // Extract anti-pattern if present
    const antiPatternMatch = section.match(
      new RegExp(`${question}[\\s\\S]*?⚠ 别这么说[：:]\\s*"(.+?)"`, "m")
    );
    const antiPattern = antiPatternMatch?.[1];
    
    // Extract code reference (file:line pattern)
    const codeRefMatch = answer.match(/`([a-zA-Z0-9_/.-]+:\d+)`/);
    const codeRef = codeRefMatch?.[1];
    
    questions.push({ question, answer, antiPattern, codeRef });
  }
  
  return questions;
}
```

### 3. Link from chapter page

In `src/app/[locale]/[version]/page.tsx`, add a button:

```tsx
<Link href={`/${locale}/interview/${version}`}>
  <button className="bg-purple-500 text-white px-4 py-2 rounded">
    🎯 面试模拟器
  </button>
</Link>
```

## When to add

**Priority: P2** (after core content is authored). This is a **differentiation feature** — learn.shareai.run doesn't have this.

## Gotchas

- The parser regex assumes the upgraded 3-tier interview format (§ 5 in REFERENCE.md). If using the old flat format, adjust regex.
- Timer doesn't pause on tab blur — fine for MVP; add `document.visibilityState` listener if needed.
- Shuffle is client-side; add `"use client"` directive.

## Future enhancements

- Save scores to localStorage: `{ chapterId: { correct: 2, total: 3, timestamp } }`
- Add difficulty filter (only 🟢 / only 🔴)
- Multi-chapter quiz mode (pull from all chapters)
- Export wrong answers as Anki flashcards
