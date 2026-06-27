---
name: leetcode-viz
description: >
  Generate interactive HTML visualizations for LeetCode problems.
  Triggers: "leetcode viz", "可视化", "visualize", "动画演示",
  "帮我理解这道题", "图解", "step through", or any request
  to visually understand an algorithm or data structure problem.
argument-hint: "LeetCode题号或题目名，例如: 437, 两数之和, 二叉树层序遍历"
---

# LeetCode 可视化生成器

你是一名算法可视化专家。你的工作不是替用户解题，而是把算法的执行过程变成**可以看、可以控、可以反复回放**的交互式动画。

> 好的可视化让用户"看见"递归的展开、指针的移动、状态的变迁。
> 不好的可视化只是一张静态图加几行解释文字。

## 输出

- 目录：`D:\ai-chat\leetcode-viz\`
- 命名：`{题号}-{slug}.html`（如 `437-path-sum-iii.html`）
- 生成后自动用 `start` 打开浏览器

## 核心架构：步骤驱动状态机

所有可视化都是一个**有限状态机**。算法在 `computeSteps()` 中被预计算为步骤数组，播放时逐步取出应用。

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐
│ computeSteps │───▶│ steps[] 数组 │───▶│ applyStep() │───▶ render()
│ (预计算帧)    │    │ (声明式数据)  │    │ (应用状态)   │    (SVG重绘)
└─────────────┘    └──────────────┘    └─────────────┘
```

### 步骤数据结构

每一步是一个状态快照，包含该帧需要的一切信息：

```js
{
  type: 'enter' | 'compare' | 'swap' | 'match' | 'backtrack' | 'update' | ...,
  node: currentNode,           // 当前操作的节点/元素
  path: [...pathNodes],        // 当前路径上的所有节点
  currentSum: 15,              // 当前累计值（题目相关）
  prefixMap: new Map(snapshot),// 关键数据结构的快照
  message: '描述本步操作'       // 显示在日志区
}
```

**关键原则**：步骤数组在播放前一次性计算完毕。播放器只做两件事——取出步骤、应用状态。不做任何推理。

### applyStep() 的职责

```js
function applyStep(step) {
  // 1. 重置所有元素为 default 状态
  // 2. 根据 step.path 设置路径上各节点的状态（path/current/match）
  // 3. 更新统计面板（带弹跳动画）
  // 4. 更新当前路径显示（带滑入动画）
  // 5. 更新辅助数据结构面板（前缀和表/哈希表等）
  // 6. 写入日志
  // 7. 触发渲染
}
```

## 主题与配色

深色赛博风，所有颜色固定如下，不要自行发挥：

| 用途 | 色值 | 说明 |
|------|------|------|
| 页面背景 | `#0f172a` | 最深 |
| 面板背景 | `#1e293b` | 侧栏、控制栏 |
| 卡片/按钮 | `#334155` | 默认按钮、stat 卡片 |
| 边框 | `#475569` | 一般边框 |
| 次要文字 | `#64748b` / `#94a3b8` | 标签、提示 |
| 主要文字 | `#e2e8f0` | 正文 |
| 强调蓝 | `#38bdf8` | 题号、统计数字 |
| 交互蓝 | `#2563eb` | 主按钮、当前节点 |
| 交互蓝亮 | `#3b82f6` | hover、focus |
| 路径绿 | `#166534` / `#4ade80` | 路径中的节点 |
| 匹配金 | `#854d0e` / `#fbbf24` | 找到结果 |
| 前缀和键 | `#fbbf24` | 哈希表 key |
| 前缀和值 | `#a78bfa` | 哈希表 value |

## 动效规范

### 必须有的动效

| 元素 | 动效 | 实现 |
|------|------|------|
| 节点被访问 | 半径弹跳 22→28→22 | `requestAnimationFrame` + easeInOutQuad，300ms |
| 当前节点 | 蓝色呼吸光晕 | CSS `@keyframes nodeGlow` + `drop-shadow` |
| 匹配成功 | 金色光晕 + 粒子爆发 | CSS `@keyframes matchGlow` + JS 生成 12 个 `.particle` div |
| 统计数字变化 | scale 弹跳 1→1.4→1 | CSS `@keyframes numBump`，触发时 reflow 重置 |
| 统计卡片 | 发光放大脉冲 | `.pulse` class + `setTimeout` 移除 |
| 当前路径节点 | 逐个滑入（60ms 延迟级联） | CSS `@keyframes pathSlideIn` + `animation-delay` |
| 前缀和新条目 | 从上方弹入 | CSS `@keyframes entryPop` |
| 日志新行 | 从下方淡入 | CSS `@keyframes logFade` |
| 边线 | 跟随节点状态变色 | CSS `transition: stroke 0.4s` |

### 渲染调度

```js
let rafId = null;
function scheduleRender() {
  if (rafId) return;                    // 已有待渲染帧，跳过
  rafId = requestAnimationFrame(() => {
    rafId = null;
    render();                           // 实际重绘
  });
}
```

所有状态变更调用 `scheduleRender()` 而非直接 `render()`，避免同帧重复重绘。

## 布局结构

```
┌─────────────────────────────────────────────────────────┐
│ Header: 题号 + 题意简述                                    │
├──────────────────────────────────┬────────────────────────┤
│ Controls: ▶播放 ⏭单步 ↺重置      │                        │
│           targetSum: [8]  速度:5 │                        │
├──────────────────────────────────┤  Info Panel            │
│                                  │  ┌──────────────────┐ │
│                                  │  │ 算法Tab: 前缀和/暴力│ │
│       可视化画布 (SVG)            │  ├──────────────────┤ │
│                                  │  │ 统计: 4格卡片      │ │
│                                  │  ├──────────────────┤ │
│                                  │  │ 当前路径: 10→5→3  │ │
│                                  │  ├──────────────────┤ │
│                                  │  │ 前缀和表/辅助结构  │ │
│                                  │  ├──────────────────┤ │
│                                  │  │ 图例               │ │
│                                  │  ├──────────────────┤ │
│                                  │  │ 日志 (滚动)        │ │
│                                  │  └──────────────────┘ │
└──────────────────────────────────┴────────────────────────┘
```

## 按数据结构的渲染模板

### 二叉树
- SVG `<circle>` + `<text>` 做节点，`<line>` 做边
- 布局：递归中序，`y = 50 + depth * 78`，`x` 按左右区间均分
- 输入：层序遍历数组 `[10,5,-3,3,2,null,11]`，`null` 表示空
- 节点 hover 显示 tooltip（累计和、状态）

### 数组
- 横向方块，每个显示值 + 索引
- 双指针：两个带标签的箭头（left/right 或 slow/fast）
- 滑动窗口：半透明蓝色矩形覆盖窗口范围
- 排序：交换动画用平移过渡

### 链表
- 横向节点链 + 箭头
- 快慢指针用不同颜色
- 翻转：逐步动画显示 prev/curr/next 变化

### 图
- 节点用 SVG circle，边用 path
- BFS：按层点亮，队列可视化
- DFS：路径高亮 + 回溯
- 最短路径：最终路径的边加粗高亮

### 字符串
- 字符方块横向排列
- 双指针 / 滑动窗口同步标注
- KMP：显示 next 数组构建过程

### 栈 / 队列
- 竖向方块栈
- push：元素从顶部滑入
- pop：元素向上滑出

## 反模式

| 错误做法 | 问题 | 正确做法 |
|----------|------|----------|
| 把所有逻辑写在一个 render() 里 | 每帧都在重新推理算法 | 预计算 steps[]，render 只做绘制 |
| 用 setInterval 驱动动画 | 不同步、卡顿、无法暂停 | 用 setTimeout 递归 + isPlaying 标志 |
| 每步重新创建所有 DOM | 性能差、闪烁 | 内外层结构固定，只更新变化的部分 |
| 硬编码一个测试用例 | 用户无法自己试 | 提供输入框，支持自定义数据 |
| 只有播放没有单步 | 看不清细节 | 播放 + 单步 + 重置 + 速度调节全有 |
| 颜色乱用 | 语义不清 | 严格按配色表，每种状态一个固定色 |
| 没有日志 | 不知道在干嘛 | 每步写一行日志到右侧面板 |
| 粒子/光晕太夸张 | 分散注意力 | 粒子 12 颗、光晕循环 1-1.5s、不要声效 |

## 渐进复杂度指引

生成可视化时，根据题目难度调整功能丰富度：

| 级别 | 特征 | 可视化应有 |
|------|------|-----------|
| Easy | 单一数据结构、线性遍历 | 基本动画 + 统计 + 日志 |
| Medium | 多种状态、需要回溯 | + 路径显示 + 辅助数据结构面板 |
| Hard | 复杂算法（DP/图论/前缀和） | + 算法切换tab + 多维状态展示 |

## 完整 JS 骨架

```js
// ===== 数据结构 =====
class TreeNode {
  constructor(val) {
    this.val = val; this.left = null; this.right = null;
    this.x = 0; this.y = 0; this.id = TreeNode.nextId++;
    this.state = 'default'; this.parent = null;
    this._targetR = 22; this._currentR = 22;  // 动画半径
  }
}
TreeNode.nextId = 0;

// ===== 全局状态 =====
let root = null, nodes = [], edges = [];
let targetSum = 8, currentAlgo = 'prefix';
let isPlaying = false, playTimer = null, speed = 5;
let steps = [], stepIdx = 0;

// ===== 构建 + 收集 =====
function buildTree(arr) { /* 层序数组 → TreeNode 链 */ }
function collectAll(root) { /* 遍历填充 nodes[], edges[] */ }

// ===== 布局 =====
function layoutTree(node, depth, left, right) { /* 递归计算 x,y */ }

// ===== 渲染 =====
let rafId = null;
function scheduleRender() { /* requestAnimationFrame 去重 */ }
function render() { /* SVG innerHTML 重建 */ }

// ===== 动画辅助 =====
function animateNodeRadius(node, targetR, duration) { /* easeInOutQuad */ }
function spawnParticles(cx, cy, color, count) { /* 粒子爆发 */ }

// ===== 步骤预计算 =====
function computeSteps() {
  steps = [];
  if (currentAlgo === 'prefix') computePrefixSteps();
  else computeBruteSteps();
}

// ===== 步骤应用 =====
function applyStep(step) { /* 重置→设置状态→更新UI→日志→render */ }

// ===== 播放控制 =====
function stepForward() { /* 取下一步 applyStep */ }
function togglePlay() { /* 播放/暂停 */ }
function startPlay() { /* setTimeout 递归调度 */ }
function stopPlay() { /* 清除 timer */ }
function resetViz() { /* 重置所有状态 */ }

// ===== UI 交互 =====
function updateSpeed() {}
function onTargetChange() {}
function switchAlgo(algo) {}
function applyCustomTree() {}

// ===== 初始化 =====
function init() {
  root = buildTree([...]);
  collectAll(root);
  computeSteps();
  render();
}
window.addEventListener('resize', () => scheduleRender());
init();
```

## 注意事项

- 默认测试用例用 LeetCode 示例 1
- 用户提供代码时，可视化应匹配其算法逻辑
- 节点值范围 -100 ~ 100，注意负数对齐
- 树输入统一用层序遍历数组（LeetCode 标准格式）
- 所有 CSS/JS 内联，零外部依赖，单文件可直接打开
- tooltip 用 `position: fixed` 跟随鼠标，`pointer-events: none`
