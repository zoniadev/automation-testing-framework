
const fs = require('fs');
const path = require('path');

function pad(num) {
  return num < 10 ? '0' + num : num;
}

const historyDirOut = 'allure-history';
const portalManifest = path.join(historyDirOut, 'portal.json');
// Prefer a directory-tree checkout for enumeration if present
const historyDirTree = fs.existsSync(path.join('gh-pages-tree', 'allure-history'))
  ? path.join('gh-pages-tree', 'allure-history')
  : (fs.existsSync(path.join('gh-pages', 'allure-history'))
      ? path.join('gh-pages', 'allure-history')
      : historyDirOut);

// Gather current run context from environment
const REPORT_SCOPE = process.env.REPORT_SCOPE;
const REPORT_NAME = process.env.REPORT_NAME;

// Helper to read summary for a given scope/name
function readSummary(scope, name) {
  // Try from workspace first, then from tree checkout to trigger lazy blob fetch if needed
  let summaryPath = path.join(historyDirOut, scope, name, 'latest', 'widgets', 'summary.json');
  if (!fs.existsSync(summaryPath)) {
    summaryPath = path.join(historyDirTree, scope, name, 'latest', 'widgets', 'summary.json');
  }
  if (!fs.existsSync(summaryPath)) return null;
  const fileStats = fs.statSync(summaryPath);
  const summary = JSON.parse(fs.readFileSync(summaryPath));
  let ts;
  if (summary.time && typeof summary.time.stop === 'number') {
    ts = new Date(summary.time.stop);
  } else {
    ts = new Date(fileStats.mtime);
  }
  const stats = summary.statistic || {};
  const passed = stats.passed || 0;
  const failed = (stats.failed || 0) + (stats.broken || 0);
  return { ts, passed, failed };
}

// Load existing manifest (if any)
let entries = [];
if (fs.existsSync(portalManifest)) {
  try {
    entries = JSON.parse(fs.readFileSync(portalManifest, 'utf8'));
    if (!Array.isArray(entries)) entries = [];
  } catch (e) {
    console.warn('Failed to parse portal.json, starting fresh.');
    entries = [];
  }
}

// Ensure entries include all scopes/names found in the directory tree
try {
  if (fs.existsSync(historyDirTree)) {
    const scopes = fs.readdirSync(historyDirTree).filter(s => fs.statSync(path.join(historyDirTree, s)).isDirectory());
    const byKey = new Map(entries.map(e => [e.key, e]));
    for (const scope of scopes) {
      const scopeDir = path.join(historyDirTree, scope);
      const names = fs.readdirSync(scopeDir).filter(n => fs.statSync(path.join(scopeDir, n)).isDirectory());
      for (const name of names) {
        const key = `${scope}__${name}`;
        if (!byKey.has(key)) {
          const s = readSummary(scope, name);
          byKey.set(key, {
            key,
            scope,
            name,
            lastRun: s ? s.ts.getTime() : 0,
            passed: s ? s.passed : 0,
            failed: s ? s.failed : 0,
            reportUrl: `./${scope}/${name}/`
          });
        }
      }
    }
    entries = Array.from(byKey.values());
  }
} catch (e) {
  console.warn('Directory enumeration failed:', e.message);
}

// Update/insert current run entry based on local summary
if (REPORT_SCOPE && REPORT_NAME) {
  const s = readSummary(REPORT_SCOPE, REPORT_NAME);
  if (s) {
    const key = `${REPORT_SCOPE}__${REPORT_NAME}`;
    const updated = {
      key,
      scope: REPORT_SCOPE,
      name: REPORT_NAME,
      lastRun: s.ts.getTime(),
      passed: s.passed,
      failed: s.failed,
      reportUrl: `./${REPORT_SCOPE}/${REPORT_NAME}/`
    };
    const idx = entries.findIndex(e => e && e.key === key);
    if (idx >= 0) entries[idx] = updated; else entries.push(updated);
  }
}

// Sort by lastRun desc
entries.sort((a, b) => (b.lastRun || 0) - (a.lastRun || 0));

// Persist manifest
try {
  fs.writeFileSync(portalManifest, JSON.stringify(entries, null, 2));
} catch (e) {
  console.error('Failed to write portal.json:', e);
}

// Build HTML
let tableRows = '';
for (const e of entries) {
  const dt = new Date(e.lastRun || 0);
  const sofiaTime = new Date(dt.getTime() + (3 * 60 * 60 * 1000));
  const day = pad(sofiaTime.getUTCDate());
  const month = pad(sofiaTime.getUTCMonth() + 1);
  const year = sofiaTime.getUTCFullYear().toString().slice(-2);
  const hours = pad(sofiaTime.getUTCHours());
  const minutes = pad(sofiaTime.getUTCMinutes());
  const formattedLastRun = `${day}.${month}.${year} ${hours}:${minutes}`;

  tableRows += `
    <tr>
      <td>${e.scope} / ${e.name}</td>
      <td class="passed">${e.passed ?? 0}</td>
      <td class="failed">${e.failed ?? 0}</td>
      <td>${formattedLastRun}</td>
      <td><a href="${e.reportUrl}">View Report</a></td>
    </tr>
  `;
}

const html = `
<!DOCTYPE html>
<html>
<head>
  <title>Test Automation Report Portal</title>
  <style>
    body { font-family: sans-serif; }
    table { border-collapse: collapse; width: 90%; margin: 20px auto; }
    th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
    th { background-color: #f2f2f2; }
    .passed { color: green; }
    .failed { color: red; }
  </style>
  <meta charset="utf-8" />
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
  <meta http-equiv="Pragma" content="no-cache" />
  <meta http-equiv="Expires" content="0" />
  </head>
  <body>
    <h1 style="text-align: center;">Test Automation Report Portal</h1>
    <table>
      <thead>
        <tr>
          <th>Scope / Name</th>
          <th>Passed</th>
          <th>Failed</th>
          <th>Last Run (Sofia Time)</th>
          <th>Link</th>
        </tr>
      </thead>
      <tbody>
        ${tableRows}
      </tbody>
    </table>
  </body>
  </html>
`;

// Ensure output directory exists
if (!fs.existsSync(historyDirOut)) fs.mkdirSync(historyDirOut, { recursive: true });
fs.writeFileSync(path.join(historyDirOut, 'index.html'), html);
console.log('Portal page generated successfully.');
