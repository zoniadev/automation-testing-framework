
const fs = require('fs');
const path = require('path');

function pad(num) {
  return num < 10 ? '0' + num : num;
}

const historyDir = 'allure-history';
const portalManifest = path.join(historyDir, 'portal.json');

// Gather current run context from environment
const REPORT_SCOPE = process.env.REPORT_SCOPE;
const REPORT_NAME = process.env.REPORT_NAME;

// Helper to read summary for a given scope/name
function readSummary(scope, name) {
  const summaryPath = path.join(historyDir, scope, name, 'latest', 'widgets', 'summary.json');
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

fs.writeFileSync(path.join(historyDir, 'index.html'), html);
console.log('Portal page generated successfully.');
