#!/usr/bin/env node
// validate-content.mjs <site-dir>
// Consistency checks for hand-authored content. Run after authoring (Phase 6).
import fs from "node:fs";
import path from "node:path";

const site = process.argv[2];
if (!site) {
  console.error("usage: validate-content.mjs <site-dir>");
  process.exit(2);
}

const SIM_TYPES = new Set([
  "user_message",
  "assistant_text",
  "tool_call",
  "tool_result",
  "system_event",
]);
const LAYERS = new Set([
  "tools",
  "planning",
  "memory",
  "concurrency",
  "collaboration",
]);
const problems = [];
const readJSON = (rel) =>
  JSON.parse(fs.readFileSync(path.join(site, rel), "utf8"));

// 1. constants.ts VERSION_ORDER vs versions.json
let order = [];
try {
  const cst = fs.readFileSync(path.join(site, "src/lib/constants.ts"), "utf8");
  const m = cst.match(/VERSION_ORDER\s*=\s*\[([^\]]*)\]/);
  if (m) {
    order = [...m[1].matchAll(/"([^"]+)"/g)].map((x) => x[1]);
  } else {
    problems.push("constants.ts: could not find VERSION_ORDER array");
  }
} catch (e) {
  problems.push("cannot read constants.ts: " + e.message);
}

// 2. versions.json
let versions = [];
try {
  const v = readJSON("src/data/generated/versions.json");
  versions = (v.versions || []).map((x) => x.id);
  if (!Array.isArray(v.diffs)) problems.push("versions.json: missing diffs[]");
  (v.versions || []).forEach((ver) => {
    ["id", "filename", "title", "source", "layer", "tools"].forEach((k) => {
      if (ver[k] === undefined) problems.push(`version ${ver.id}: missing field ${k}`);
    });
    if (ver.layer && !LAYERS.has(ver.layer))
      problems.push(`version ${ver.id}: bad layer '${ver.layer}'`);
  });
} catch (e) {
  problems.push("versions.json read/parse error: " + e.message);
}

// 3. VERSION_ORDER ids exist in versions.json
order.forEach((id) => {
  if (!versions.includes(id))
    problems.push(`VERSION_ORDER has '${id}' but versions.json does not`);
});

// 4. docs.json covers every version
try {
  const docs = readJSON("src/data/generated/docs.json");
  const docVers = new Set(docs.map((d) => d.version));
  versions.forEach((id) => {
    if (!docVers.has(id)) problems.push(`docs.json missing version ${id}`);
  });
} catch (e) {
  problems.push("docs.json read/parse error: " + e.message);
}

// 5. scenarios/<id>.json for every version + valid step types
versions.forEach((id) => {
  const sp = path.join(site, "src/data/scenarios", `${id}.json`);
  if (!fs.existsSync(sp)) {
    problems.push(`scenarios/${id}.json missing`);
    return;
  }
  try {
    const sc = JSON.parse(fs.readFileSync(sp, "utf8"));
    (sc.steps || []).forEach((s, i) => {
      if (!SIM_TYPES.has(s.type))
        problems.push(`${id} step ${i}: bad type '${s.type}'`);
      if (!s.annotation) problems.push(`${id} step ${i}: missing annotation`);
    });
  } catch (e) {
    problems.push(`scenarios/${id}.json parse error: ${e.message}`);
  }
});

// 6. visualizations/index.tsx maps every VERSION_ORDER id
try {
  const viz = fs.readFileSync(
    path.join(site, "src/components/visualizations/index.tsx"),
    "utf8"
  );
  order.forEach((id) => {
    const re = new RegExp(`${id}\\s*:\\s*lazy`);
    if (!re.test(viz)) problems.push(`visualizations/index.tsx: no mapping for ${id}`);
  });
} catch (e) {
  problems.push("cannot read visualizations/index.tsx: " + e.message);
}

if (problems.length) {
  console.error(`✗ ${problems.length} problem(s):`);
  problems.forEach((p) => console.error("  - " + p));
  process.exit(1);
}
console.log(
  `✓ content consistent: ${versions.length} chapters, VERSION_ORDER ↔ versions ↔ docs ↔ scenarios ↔ viz all aligned.`
);
