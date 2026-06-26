# 设计系统速查（Design System）

> 改主题色、换字体、调画布、改动画节奏时查这里。所有值都在 `assets/skeleton.html` 的 `<style>` 里定义，本文是速查表。

## 配色（CSS 变量，定义在 `:root`）

**纸质米色背景层：**

| 变量 | 值 | 用途 |
|---|---|---|
| `--paper` | `#fbfaf6` | 主背景 |
| `--paper-deep` | `#f4efe6` | 次背景 / 代码块底 |
| `--ink` | `#22211d` | 正文墨色 |
| `--muted` | `#716d63` | 次要文字 |
| `--faint` | `#918b7d` | 更淡 / 注释色 |
| `--line` | `#e3dacb` | 分隔线 / 卡片边框 |
| `--line-strong` | `#cfc3b0` | 流程图箭头 / 强分隔线 |

**强调色（克制使用，别大面积铺）：**

| 变量 | 值 | 典型用途 |
|---|---|---|
| `--green` | `#3e7e74` | card 顶条 / note 渐变 / 积极语义 |
| `--blue` | `#4a6f91` | card 顶条 / 代码块左边条 / 链接 |
| `--coral` | `#c76752` | `big-number` 编号 / 警示 |
| `--lavender` | `#6f6fae` | card 顶条 |
| `--gold` | `#aa7a36` | 备用强调（CSS 未绑定 accent 类，需自补） |

> **换肤**：只改这几个变量，全局配色立刻跟着变。不要在单处写死十六进制。

## 字体

`font-family` 栈（在 `:root`）：
```
"LXGW WenKai Screen", "PingFang SC", "Hiragino Sans GB",
"Microsoft YaHei", "Noto Sans CJK SC", sans-serif
```

- **霞鹜文楷**是纸质气质的核心来源。skeleton 已加载 CDN：
  `<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/lxgw-wenkai-screen-webfont/style.css" />`
- 无网络时自动 fallback 到苹方/微软雅黑，仍可读，只是少了手写感。
- **等宽**（代码、note 的 `.label`）：`ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace`
- **衬线**（`.big-number` 编号）：`Georgia, "Times New Roman", "Songti SC", serif`

> 国内 jsdelivr 偶尔不稳，可换成 `https://unpkg.com/lxgw-wenkai-screen-webfont/style.css` 或 npm 镜像。

## 画布与缩放（最重要的机制）

- 固定**逻辑画布**：`--deck-width: 1720px` × `--deck-height: 900px`（比 16:9 略宽）。
- 整个 `.deck` 用 `transform: scale(var(--deck-scale))` 等比缩放适配窗口。JS 实时算：
  `scale = min(1, 可用宽/1720, 可用高/900)`，监听 `resize` 更新。
- **意义**：内容按固定坐标排版，任何屏幕都**不变形、不溢出**。
- **推论**：内容**别写死 `px` 宽高**，用 `cqi` / `%` / `clamp()`，否则缩放后错位。

**容器查询单位 `cqi`**：1cqi = 画布宽的 1%。字号典型写法：
`font-size: clamp(最小值, 1.4cqi, 最大值)` —— 在缩放下仍自适应。

## 动画系统（逐级入场）

- 给元素加 `class="animate"` + `style="--i: N"`。
- 元素默认 `opacity: 0` + 轻微位移；当**所在 slide 变为 `.active`** 时触发淡入。
- `--i` 控制**出场顺序**：从 0 开始递增。delay ≈ `calc(var(--i) * 步长)`（步长见 skeleton 里 `.slide.active .animate` 的 `animation-delay`，默认约 80ms/级）。
- 排版惯例：kicker/title 用 0–1，正文构件 2、3、4…，补充 note 最后。
- 缓动：`--ease: cubic-bezier(0.22, 1, 0.36, 1)`。

## slide 修饰符

| class | 作用 |
|---|---|
| `.active` | 当前可见页（同时刻仅一页）。首屏给 cover 加，其余靠 JS 切换 |
| `.dense` | 紧凑模式：缩小字号与间距，用于表格、对照等高密度页 |
| `.corner-kicker` | Part 分隔页样式：给左上角 kicker 特殊处理 |

## 其它 token

| 变量 | 值 | 用途 |
|---|---|---|
| `--radius` | `8px` | 卡片圆角 |
| `--shadow` | `0 24px 70px rgba(32,31,27,.12)` | deck 浮起阴影 |
| `--side` | `320px` | 左侧目录栏宽度 |
| `--frame-gap` | `16px` | 画布与窗口的安全间距 |

## 交互（JS 内置，无需配置）

| 操作 | 键 | 说明 |
|---|---|---|
| 翻页 | ←/→、Space、PageUp/Down | 前后翻 |
| 首末页 | Home / End | 跳到第 1 / 最后 1 页 |
| 跳页 | 1–9 | 跳到第 N 页 |
| 概览 | `o` | 网格罗列所有页，点击跳转；`Esc` 关闭 |
| 全屏 | `f` | 切换浏览器全屏 |

左侧目录每页都可点：章节首页是组头，子页是缩进子项，点击直达任意页（不再只能跳章节首页）。

## 无障碍

- `@media (prefers-reduced-motion: reduce)`：自动禁用逐级淡入与位移，直接显示终态。
- 所有可点元素（目录项、概览项、控制按钮）都是 `<button>`，支持键盘聚焦。

## 打印 / 导出 PDF

`@media print` 已配置：每页一张、隐藏侧栏与控件、动画归位。浏览器 `Ctrl/Cmd + P` → 另存为 PDF（建议横向、关闭页眉页脚）。

## 代码高亮

highlight.js（head 里 `defer` 加载）自动处理 `.code-block` 的纯文本内容，套用纸质低饱和主题（关键字 `--blue` / 字符串 `--green` / 注释 `--faint` / 数字 `--coral`）。`data-lang="go"` 指定语言；code-block 内一旦有子元素（如手动 `.c-comment`）则跳过自动高亮。无网络时降级为纯墨色等宽。

## 字体加载

霞鹜文楷走 jsdelivr 主源，`<link>` 的 `onerror` 回退到 unpkg；两端都失败则 fallback 到苹方/微软雅黑（`font-family` 栈已含）。换镜像改 head 脚本里 `primary` / `fallback` 两个 URL。
