#!/usr/bin/env node
import { readFileSync, existsSync } from "node:fs";
import { resolve } from "node:path";

const target = process.argv[2];

if (!target) {
  console.error("Usage: node scripts/validate_deck.mjs <deck.html>");
  process.exit(2);
}

const file = resolve(target);

if (!existsSync(file)) {
  console.error(`Deck not found: ${file}`);
  process.exit(2);
}

const html = readFileSync(file, "utf8");
const failures = [];
const slideCount = (html.match(/<section\s+class="[^"]*\bslide\b/g) || []).length;
const dataTitleCount = (html.match(/data-title="/g) || []).length;

function requirePattern(pattern, label) {
  if (!pattern.test(html)) failures.push(label);
}

if (slideCount < 6) failures.push(`expected at least 6 slides, found ${slideCount}`);
if (dataTitleCount < slideCount) failures.push("each slide should have data-title");

requirePattern(/<aside\s+class="sidebar"/, "missing sidebar");
requirePattern(/id="slideNav"/, "missing slideNav");
requirePattern(/id="stage"/, "missing stage");
requirePattern(/class="progress-bar"\s+id="progressBar"/, "missing progress bar");
requirePattern(/const\s+navSections\s*=\s*\[/, "missing navSections");
requirePattern(/function\s+showSlide\s*\(/, "missing showSlide function");
requirePattern(/addEventListener\("keydown"/, "missing keyboard navigation");
requirePattern(/--deck-width:\s*1720px/, "missing 1720px deck width token");
requirePattern(/--deck-height:\s*900px/, "missing 900px deck height token");
requirePattern(/\.three-col/, "missing three-col layout");
requirePattern(/\.two-col/, "missing two-col layout");
requirePattern(/\.material-table/, "missing material table layout");
requirePattern(/\.flow/, "missing flow layout");

if (failures.length > 0) {
  console.error(`Deck validation failed for ${file}`);
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}

console.log(`Deck validation passed: ${file}`);
console.log(`Slides: ${slideCount}`);
