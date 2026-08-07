
const fs = require('fs');
const path = require('path');

function pad(num) {
    return num < 10 ? '0' + num : num;
}

const historyDir = 'allure-history';
// Workflows that haven't produced a run in this long are treated as retired/dead
// and dropped from the portal table (e.g. renamed or deleted workflows whose old
// report folders otherwise linger on gh-pages forever, since nothing triggers
// their per-run cleanup once the workflow itself is gone).
const STALE_AFTER_DAYS = 45;
const staleCutoff = Date.now() - STALE_AFTER_DAYS * 24 * 60 * 60 * 1000;

const scopes = fs.readdirSync(historyDir).filter(scope => fs.statSync(path.join(historyDir, scope)).isDirectory());

let reportsData = [];

for (const scope of scopes) {
    const scopeDir = path.join(historyDir, scope);
    const reports = fs.readdirSync(scopeDir).filter(report => fs.statSync(path.join(scopeDir, report)).isDirectory());

    for (const report of reports) {
        const summaryPath = path.join(scopeDir, report, 'latest', 'widgets', 'summary.json');
        if (fs.existsSync(summaryPath)) {
            const fileStats = fs.statSync(summaryPath);
            const summary = JSON.parse(fs.readFileSync(summaryPath));
            let reportTimestamp;

            if (summary.time && typeof summary.time.stop === 'number') {
                reportTimestamp = new Date(summary.time.stop);
            } else {
                // Fallback to file modification time if 'time.stop' is not available or not a number
                reportTimestamp = new Date(fileStats.mtime);
            }

            const sofiaTime = new Date(reportTimestamp.getTime() + (3 * 60 * 60 * 1000));

            const day = pad(sofiaTime.getUTCDate());
            const month = pad(sofiaTime.getUTCMonth() + 1);
            const year = sofiaTime.getUTCFullYear().toString().slice(-2);
            const hours = pad(sofiaTime.getUTCHours());
            const minutes = pad(sofiaTime.getUTCMinutes());

            const formattedLastRun = `${day}.${month}.${year} ${hours}:${minutes}`;

            const stats = summary.statistic;
            const passed = stats.passed || 0;
            const failed = (stats.failed || 0) + (stats.broken || 0);
            const reportUrl = `./${scope}/${report}/`;

            reportsData.push({
                name: report,
                passed: passed,
                failed: failed,
                lastRun: reportTimestamp,
                formattedLastRun: formattedLastRun,
                reportUrl: reportUrl
            });
        }
    }
}

reportsData.sort((a, b) => b.lastRun - a.lastRun);

const activeReports = reportsData.filter(data => data.lastRun.getTime() >= staleCutoff);

let tableRows = '';
for (const data of activeReports) {
    tableRows += `
        <tr>
            <td>${data.name}</td>
            <td class="passed">${data.passed}</td>
            <td class="failed">${data.failed}</td>
            <td>${data.formattedLastRun}</td>
            <td><a href="${data.reportUrl}">View Report</a></td>
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
        table { border-collapse: collapse; width: 80%; margin: 20px auto; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        .passed { color: green; }
        .failed { color: red; }
    </style>
</head>
<body>
    <h1 style="text-align: center;">Test Automation Report Portal</h1>
    <table>
        <thead>
            <tr>
                <th>Workflow Name</th>
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
