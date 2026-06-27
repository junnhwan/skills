# Design Guide · 5 种替代主题 + 高级图示组件

> **按需查阅。** 默认 Midnight Neon 主题已在 `template.html` 内。用户要求换主题时，只需替换生成文件的 `:root` CSS 变量（和字体 `@import`）。高级组件（seq / arch-box / layer-pierce / metric compare）不在模板内，需要时复制进生成的 HTML。

---

## 主题 1: Paper Scholar

> 米白底 + 衬线标题 + 纸张质感。像精装技术教科书。

```css
@import url('https://fonts.googleapis.com/css2?family=Crimson+Pro:wght@400;500;600;700;800&family=Source+Code+Pro:wght@400;500;600&family=Noto+Serif+SC:wght@400;500;600;700;900&display=swap');

:root {
  --c-bg:#faf6f0; --c-surface:#f5f0e8; --c-card:#ffffff; --c-card-h:#faf8f4;
  --c-border:rgba(60,50,30,0.1); --c-border-h:rgba(139,92,246,0.25);
  --c-text:#2c2416; --c-text2:#6b5e4f; --c-text3:#a09482;
  --c-accent:#6d28d9; --c-cyan:#0891b2; --c-green:#059669; --c-amber:#d97706;
  --c-rose:#dc2626; --c-blue:#2563eb;
  --grad:linear-gradient(135deg,#6d28d9 0%,#2563eb 100%);
  --radius:8px; --radius-sm:6px;
  --font-ui:'Crimson Pro','Noto Serif SC',Georgia,serif;
  --font-mono:'Source Code Pro',monospace;
}
```

特点：暖白底 + 衬线字体 + 淡边框 + 无发光 + 书页感。Hero 用大号衬线标题。代码块用浅灰底。

---

## 主题 2: Gradient Flow

> 深色渐变背景 + 毛玻璃卡片。像 Linear / Stripe 的高级感。

```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fira+Code:wght@400;500;600&family=Noto+Sans+SC:wght@400;500;700&display=swap');

:root {
  --c-bg:#0c0a1a; --c-surface:rgba(20,18,40,0.7); --c-card:rgba(30,28,55,0.5);
  --c-card-h:rgba(40,38,70,0.6);
  --c-border:rgba(255,255,255,0.08); --c-border-h:rgba(255,255,255,0.15);
  --c-text:#f0f0f5; --c-text2:#a0a0b8; --c-text3:#606078;
  --c-accent:#818cf8; --c-cyan:#38bdf8; --c-green:#34d399; --c-amber:#fbbf24;
  --c-rose:#f472b6; --c-blue:#60a5fa;
  --grad:linear-gradient(135deg,#6366f1 0%,#ec4899 50%,#f59e0b 100%);
  --radius:20px; --radius-sm:12px;
  --font-ui:'Inter','Noto Sans SC',system-ui,sans-serif;
  --font-mono:'Fira Code',monospace;
}
```

特点：`backdrop-filter:blur(20px)` 毛玻璃卡片 + 渐变背景 + 更大圆角 + 无发光。Hero 有大面积渐变。需要在 body 加 `background-image: radial-gradient(ellipse at 30% 20%, rgba(99,102,241,.15), transparent 50%), radial-gradient(ellipse at 70% 80%, rgba(236,72,153,.1), transparent 50%);`。

---

## 主题 3: Terminal Green

> 纯黑底 + 绿色终端字体 + 扫描线效果。像 vim 主题。

```css
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700;800&family=Noto+Sans+SC:wght@400;500;700&display=swap');

:root {
  --c-bg:#0a0a0a; --c-surface:#111111; --c-card:#151515; --c-card-h:#1a1a1a;
  --c-border:rgba(0,255,65,0.1); --c-border-h:rgba(0,255,65,0.3);
  --c-text:#00ff41; --c-text2:#00cc33; --c-text3:#006620;
  --c-accent:#00ff41; --c-cyan:#00e5ff; --c-green:#00ff41; --c-amber:#f0e000;
  --c-rose:#ff3366; --c-blue:#4488ff;
  --grad:linear-gradient(135deg,#00ff41 0%,#00e5ff 100%);
  --radius:4px; --radius-sm:2px;
  --font-ui:'JetBrains Mono','Noto Sans SC',monospace;
  --font-mono:'JetBrains Mono',monospace;
}
```

特点：**所有文字用等宽字体** + 极小圆角 + 绿色系为主。Hero 标题像终端 prompt：`$ video-feed --deep-dive`。

扫描线效果（可选，加在 body::after）：
```css
body::after{content:'';position:fixed;inset:0;pointer-events:none;
  background:repeating-linear-gradient(0deg,transparent,transparent 2px,rgba(0,0,0,.03) 2px,rgba(0,0,0,.03) 4px);z-index:9999}
```

---

## 主题 4: Sakura Mist

> 柔粉白底 + 渐变粉紫 + 圆润卡片。日式清新风。

```css
@import url('https://fonts.googleapis.com/css2?family=M+PLUS+Rounded+1c:wght@400;500;700;900&family=Zen+Kaku+Gothic+New:wght@400;500;700&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
  --c-bg:#fef7f9; --c-surface:#fff0f4; --c-card:#ffffff; --c-card-h:#fff8fa;
  --c-border:rgba(219,112,147,0.12); --c-border-h:rgba(219,112,147,0.25);
  --c-text:#3d2c35; --c-text2:#7a5e6b; --c-text3:#b89aaa;
  --c-accent:#c026d3; --c-cyan:#06b6d4; --c-green:#10b981; --c-amber:#f59e0b;
  --c-rose:#ec4899; --c-blue:#6366f1;
  --grad:linear-gradient(135deg,#ec4899 0%,#a855f7 50%,#6366f1 100%);
  --radius:24px; --radius-sm:16px;
  --font-ui:'Zen Kaku Gothic New','M PLUS Rounded 1c','Noto Sans SC',sans-serif;
  --font-mono:'JetBrains Mono',monospace;
}
```

特点：**超大圆角** + 柔粉色系 + 白色卡片 + 粉紫渐变标题。卡片 hover 用 `box-shadow: 0 8px 30px rgba(236,72,153,.12)` 粉色阴影。

---

## 主题 5: Blueprint Grid

> 浅蓝网格底 + 工程蓝图风格。像技术图纸。

```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&family=Noto+Sans+SC:wght@400;500;700&display=swap');

:root {
  --c-bg:#f0f5fa; --c-surface:#e8f0f8; --c-card:#ffffff; --c-card-h:#f5f9ff;
  --c-border:rgba(37,99,235,0.12); --c-border-h:rgba(37,99,235,0.3);
  --c-text:#1a2744; --c-text2:#4a5e7a; --c-text3:#8a9ab5;
  --c-accent:#2563eb; --c-cyan:#0891b2; --c-green:#059669; --c-amber:#d97706;
  --c-rose:#dc2626; --c-blue:#2563eb;
  --grad:linear-gradient(135deg,#2563eb 0%,#0891b2 100%);
  --radius:4px; --radius-sm:2px;
  --font-ui:'Space Grotesk','Noto Sans SC',sans-serif;
  --font-mono:'IBM Plex Mono',monospace;
}
```

特点：**极小圆角** + 蓝色系 + 蓝色虚线边框卡片。背景加网格：
```css
body{background-image:linear-gradient(rgba(37,99,235,.05) 1px,transparent 1px),
  linear-gradient(90deg,rgba(37,99,235,.05) 1px,transparent 1px);background-size:20px 20px}
```

---

## 高级图示组件（不在 template.html 内，需复制进生成的 HTML）

以下组件需要连同 CSS 一起复制进生成的 HTML 文件的 `<style>` 块中。

### 时序流程图（编号步骤）

适合展示有顺序的流程（如初始化链、请求生命周期）。

```html
<div class="seq">
  <div class="seq-step">
    <div class="seq-num">1</div>
    <div class="seq-card">
      <div class="seq-title">步骤标题</div>
      <div class="seq-detail">描述</div>
      <div class="seq-file">文件路径</div>
    </div>
  </div>
  <div class="seq-line"></div>
  <div class="seq-step">
    <div class="seq-num">2</div>
    <div class="seq-card">
      <div class="seq-title">步骤标题</div>
      <div class="seq-detail">描述</div>
    </div>
  </div>
</div>
```

```css
.seq{padding:4px 0 4px 20px}
.seq-step{display:flex;gap:16px;align-items:flex-start}
.seq-num{width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:800;background:rgba(139,92,246,.15);color:var(--c-accent);flex-shrink:0}
.seq-card{flex:1;padding:16px 20px;background:var(--c-card);border:1px solid var(--c-border);border-radius:var(--radius-sm)}
.seq-title{font-weight:700;font-size:14px;margin-bottom:4px}
.seq-detail{font-size:13px;color:var(--c-text2);margin-bottom:6px}
.seq-file{font-family:var(--font-mono);font-size:11px;color:var(--c-text3);padding:2px 8px;background:var(--c-bg);border-radius:4px;display:inline-block}
.seq-line{width:2px;height:20px;background:var(--c-border);margin-left:17px}
```

---

### 层级架构图（arch-box）

适合展示系统架构或模块依赖。

```html
<div class="arch-box">
  <div class="arch-row">
    <div class="arch-node nc"><div class="name">组件</div><div class="desc">说明</div></div>
    <span class="arch-arrow">&rarr;</span>
    <div class="arch-node np"><div class="name">组件</div></div>
  </div>
  <div class="arch-sep">▼ 下层</div>
  <div class="arch-row">
    <div class="arch-node ng"><div class="name">组件</div></div>
  </div>
</div>
```

```css
.arch-box{padding:28px;background:var(--c-card);border:1px solid var(--c-border);border-radius:var(--radius);margin:24px 0}
.arch-row{display:flex;align-items:center;gap:12px;justify-content:center;flex-wrap:wrap;padding:8px 0}
.arch-node{display:flex;flex-direction:column;align-items:center;justify-content:center;padding:14px 20px;background:var(--c-bg);border:1.5px solid;border-radius:var(--radius-sm);min-width:100px;text-align:center;transition:all .3s}
.arch-node .name{font-weight:700;font-size:14px}.arch-node .desc{font-size:11px;color:var(--c-text3);margin-top:2px}
.nc{border-color:rgba(34,211,238,.4)}.np{border-color:rgba(139,92,246,.4)}
.ng{border-color:rgba(74,222,128,.4)}.na{border-color:rgba(251,191,36,.4)}
.nr{border-color:rgba(251,113,133,.4)}
.arch-arrow{color:var(--c-text3);font-size:18px}
.arch-sep{text-align:center;padding:6px 0;font-size:12px;color:var(--c-text3);font-family:var(--font-mono)}
```

---

### 层级穿透图（缓存穿透示意）

适合展示多级缓存、网络协议栈等嵌套结构。

```html
<div class="layer-pierce">
  <div class="layer-ring l1">
    <div class="layer-label">L1 本地缓存 3s</div>
    <div class="layer-ring l2">
      <div class="layer-label">L2 Redis 5min</div>
      <div class="layer-ring l3">
        <div class="layer-label">MySQL</div>
        <div class="layer-core">数据源</div>
      </div>
    </div>
  </div>
</div>
```

```css
.layer-pierce{padding:24px;display:flex;align-items:center;justify-content:center}
.layer-ring{padding:24px;border-radius:var(--radius);border:2px dashed;position:relative}
.l1{border-color:rgba(34,211,238,.3);background:rgba(34,211,238,.03)}
.l2{border-color:rgba(139,92,246,.3);background:rgba(139,92,246,.03)}
.l3{border-color:rgba(74,222,128,.3);background:rgba(74,222,128,.03)}
.layer-label{position:absolute;top:-10px;left:20px;font-size:12px;background:var(--c-card);padding:0 8px;color:var(--c-text2)}
.layer-core{padding:16px 24px;text-align:center;font-weight:700;font-size:14px;color:var(--c-text2);background:var(--c-card);border-radius:var(--radius-sm)}
```

---

### 性能对比图（带指标条）

适合展示优化前后的性能对比。

```html
<div class="compare-metric">
  <div class="cm-col bad">
    <div class="cm-label">优化前</div>
    <div class="cm-row">
      <span class="cm-metric-label">P99</span>
      <div class="cm-bar" style="width:100%"><span>320ms</span></div>
    </div>
    <div class="cm-row">
      <span class="cm-metric-label">QPS</span>
      <div class="cm-bar" style="width:30%"><span>1.2k</span></div>
    </div>
  </div>
  <div class="cm-col good">
    <div class="cm-label">优化后</div>
    <div class="cm-row">
      <span class="cm-metric-label">P99</span>
      <div class="cm-bar" style="width:15%"><span>48ms</span></div>
    </div>
    <div class="cm-row">
      <span class="cm-metric-label">QPS</span>
      <div class="cm-bar" style="width:90%"><span>8.5k</span></div>
    </div>
  </div>
</div>
```

```css
.compare-metric{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:24px 0}
.cm-col{padding:20px;border-radius:var(--radius);border:1px solid}
.cm-col.bad{background:rgba(251,113,133,.04);border-color:rgba(251,113,133,.15)}
.cm-col.good{background:rgba(74,222,128,.04);border-color:rgba(74,222,128,.15)}
.cm-label{font-weight:700;font-size:14px;margin-bottom:12px}
.cm-col.bad .cm-label{color:#fb7185}.cm-col.good .cm-label{color:#4ade80}
.cm-row{display:flex;align-items:center;gap:8px;margin-bottom:8px}
.cm-metric-label{font-size:11px;color:var(--c-text3);font-family:var(--font-mono);min-width:32px}
.cm-bar{height:24px;border-radius:4px;display:flex;align-items:center;padding:0 10px;font-size:12px;font-weight:600}
.cm-col.bad .cm-bar{background:rgba(251,113,133,.15);color:#fda4af}
.cm-col.good .cm-bar{background:rgba(74,222,128,.15);color:#86efac}
@media(max-width:768px){.compare-metric{grid-template-columns:1fr}}
```
