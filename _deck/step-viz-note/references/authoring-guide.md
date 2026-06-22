# DATA 字段详解 & 换主题示例

模板里**只改 `DATA` 这一个对象**。下面逐块讲字段，最后给两个换主题的完整例子。

---

## 1. `meta` —— 页头

| 字段 | 作用 |
|---|---|
| `eyebrow` | 标题上方那行 mono 小标签（如 `FIG · 01`） |
| `title` | 大标题 |
| `subtitle` | 副标题（灰色一行） |
| `diagramLabel` | SVG 上方那行 mono 标签（如 `while (...)`） |

---

## 2. `diagram` —— 流程图

### `layout` —— 自动布局（推荐）
```js
diagram: { layout: "auto", nodes: [...], edges: [...] }
```
设 `"auto"` 后，**节点只需 `id/label/type`，不用填坐标**。引擎按分层算法自动算位置：
DFS 找回边 → 最长路径定层（top-down）→ 层内按父节点重心排序 → 坐标化，viewBox 也自适应。

调间距可选：`layoutOpts: { nodeW, nodeH, gapX, gapY, margin }`（全有默认值）。

> 自动布局对**流程型**图（线性/分支/带回环）效果最好。复杂依赖图可能偏高；想精修某张展示图，去掉 `layout`、
> 给节点手填 `x,y` 即可（两种模式可任选）。

### `nodes[]`
```js
// auto 模式（推荐）
{ id: "check", label: "stop_reason?", type: "diamond", end: false }
// 手摆模式（去掉 layout 后）
{ id: "check", label: "stop_reason?", x: 160, y: 200, w: 140, h: 50, type: "diamond" }
```
- `id`：唯一标识，`steps.activeNodes` 用它引用。
- `label`：节点内文字。
- `x, y`：**中心点**坐标（手摆模式用；auto 模式自动算）。
- `w, h`：宽高（可选；auto 模式用 `layoutOpts` 的默认值）。
- `type`：`"rect"`（矩形）或 `"diamond"`（菱形，用于判断）。
- `end: true`：可选。该节点激活时高亮成**紫色**（表示终止/完成）。

### `edges[]`
```js
{ from: "check", to: "execute", label: "tool_use" }
```
- 路径**按源/目标相对位置自动路由**（不依赖特定节点 id）：
  - 目标在源**上方** → 走**左侧通道回环**（适合"循环回去"）。
  - 目标在源**右方** → **横到中点再折下**（适合分支/旁路）。
  - 目标在源**左下方** → **先下行再左拐**（L 形）。
  - 其余 → **垂直直线**。
  - 想要更怪的走线，改 `template.html` 里的 `edgePath()` 加分支即可。
- `label`：可选，放在边的中点。
- 在 `steps.activeEdges` 里引用边，key 是 **`"from->to"`**（与 `from`/`to` 完全一致）。

> 想要更复杂的走线？改 `template.html` 里的 `edgePath()` 函数，按 `fromId/toId` 加分支即可。

---

## 3. `steps[]` —— 时间轴（核心）

每一步**同时**驱动三件事：

```js
{
  title: "执行并追加结果",
  desc:  "执行工具，把结果写回 messages[]，再喂回模型。",
  activeNodes: ["execute", "append"],          // 本步点亮的节点 id
  activeEdges: ["execute->append"],             // 本步点亮的边 key
  messages: [                                   // 本步新增的消息（累加进消息流）
    { role: "tool_result", detail: "auth.ts 内容…" }
  ]
}
```

- **累加规则**：第 N 步显示的消息 = `steps[0..N]` 所有 `messages` 拼起来。只有"当前步新加的"
  才播放滑入动画，历史消息静止——所以看着像真实地一步步跑起来。
- `role` 决定颜色：

  | role | 颜色 | 用途 |
  |---|---|---|
  | `user` | 蓝 | 用户输入 |
  | `assistant` / `tool_call` | 灰 | 模型回复 / 工具调用 |
  | `tool_result` | 绿 | 工具返回结果 |
  | `end` | 紫 | 终止/完成 |

- **只要图、不要消息**：`messages: []`。
- **只要消息、不要图**：`activeNodes: []`, `activeEdges: []`（甚至整张 `diagram` 可以不画，
  但建议保留至少一个示意节点，否则左半边空）。

---

## 4. `content` —— 正文 markdown

极简渲染器支持：

| 语法 | 效果 |
|---|---|
| `# H1` / `## H2` / `### H3` | 标题（H1 会渲染成 H2 大小，因为页头已有大标题） |
| `**粗体**` | **粗体** |
| `` `行内代码` `` | `行内代码` |
| ` ```代码块``` ` | 代码块 |
| `- 项目` / `* 项目` | 无序列表 |
| `1. 项目` | 有序列表 |
| `> 引用` | 左边框引用块 |

不支持表格、图片、嵌套列表。需要表格就直接在 `content` 里写 HTML（渲染器会原样保留裸标签）。

---

## 换主题示例 A：HTTP 请求生命周期

```js
const DATA = {
  meta: { eyebrow: "FIG · 02", title: "一次 HTTP 请求",
          subtitle: "从 DNS 解析到响应渲染", diagramLabel: "request lifecycle" },
  diagram: {
    nodes: [
      { id: "dns",    label: "DNS 解析",   x: 150, y: 50,  w: 130, h: 40, type: "rect" },
      { id: "tcp",    label: "TCP 握手",   x: 150, y: 130, w: 130, h: 40, type: "rect" },
      { id: "tls",    label: "TLS 握手",   x: 150, y: 210, w: 130, h: 40, type: "rect" },
      { id: "send",   label: "发送请求",   x: 150, y: 290, w: 130, h: 40, type: "rect" },
      { id: "recv",   label: "接收响应",   x: 150, y: 370, w: 130, h: 40, type: "rect", end: true },
    ],
    edges: [
      { from: "dns", to: "tcp" }, { from: "tcp", to: "tls" },
      { from: "tls", to: "send" }, { from: "send", to: "recv" },
    ],
  },
  steps: [
    { title: "DNS 解析", desc: "域名 → IP", activeNodes: ["dns"], activeEdges: [], messages: [{ role: "user", detail: "GET https://example.com" }] },
    { title: "TCP 握手", desc: "三次握手建立连接", activeNodes: ["tcp"], activeEdges: ["dns->tcp"], messages: [{ role: "tool_result", detail: "SYN → SYN-ACK → ACK" }] },
    { title: "TLS 握手", desc: "协商加密参数", activeNodes: ["tls"], activeEdges: ["tcp->tls"], messages: [{ role: "assistant", detail: "协商出对称密钥" }] },
    { title: "发送请求", desc: "发出加密后的 HTTP 报文", activeNodes: ["send"], activeEdges: ["tls->send"], messages: [{ role: "tool_call", detail: "GET / HTTP/1.1" }] },
    { title: "接收响应", desc: "拿到响应体，连接可复用", activeNodes: ["recv"], activeEdges: ["send->recv"], messages: [{ role: "end", detail: "200 OK" }] },
  ],
  content: `## 概览\n一次 HTTPS 请求要经过 **DNS → TCP → TLS → 请求 → 响应** 五步。\n\n> 每一步都是一次网络往返（RTT），所以握手阶段就占了大部分延迟。\n\n\`\`\`\nGET / HTTP/1.1\nHost: example.com\n\`\`\``,
};
```

## 换主题示例 B：Git 一次提交（只要消息流、弱化图）

把 `diagram.nodes` 压成一条横线，重点靠 `steps[].messages` 演 `git add → commit → push` 的命令与输出，
`role` 用 `tool_call`（灰）表示命令、`tool_result`（绿）表示输出、`end`（紫）表示推送完成。
正文 `content` 讲暂存区/仓库/远程三层关系即可。

---

## 常见坑

1. **边的高亮 key 拼错**：必须是 `"from->to"`，中间就是字面量 `->`，前后不能有空格。
2. **节点坐标重叠**：`x` 是中心点；两个节点 `y` 相同时 `x` 至少差 `w + 40`。
3. **消息不出现**：检查是不是写在了 `messages` 里却忘了把这一步加进 `steps` 的播放序列——
   每步都独立，不会被自动合并。
4. **想换调色板**：改 `<style>` 顶部 `:root[data-theme="light"]` / `dark` 里的 CSS 变量即可，
   不用动 JS。
