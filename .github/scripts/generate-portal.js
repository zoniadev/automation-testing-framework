
const fs = require('fs');
const path = require('path');

function pad(num) {
    return num < 10 ? '0' + num : num;
}

const historyDir = 'allure-history';
const scopes = fs.readdirSync(historyDir).filter(scope => fs.statSync(path.join(historyDir, scope)).isDirectory());

let reportsData = [];

for (const scope of scopes) {
    const scopeDir = path.join(historyDir, scope);
    const reports = fs.readdirSync(scopeDir).filter(report => fs.statSync(path.join(scopeDir, report)).isDirectory());

    for (const report of reports) {
        const summaryPath = path.join(scopeDir, report, 'latest', 'widgets', 'summary.json');
        if (fs.existsSync(summaryPath)) {
            const fileStats = fs.statSync(summaryPath);
            const mtime = new Date(fileStats.mtime);

            const sofiaTime = new Date(mtime.getTime() + (3 * 60 * 60 * 1000));

            const day = pad(sofiaTime.getUTCDate());
            const month = pad(sofiaTime.getUTCMonth() + 1);
            const year = sofiaTime.getUTCFullYear().toString().slice(-2);
            const hours = pad(sofiaTime.getUTCHours());
            const minutes = pad(sofiaTime.getUTCMinutes());

            const formattedLastRun = `${day}.${month}.${year} ${hours}:${minutes}`;

            const summary = JSON.parse(fs.readFileSync(summaryPath));
            const stats = summary.statistic;
            const passed = stats.passed || 0;
            const failed = (stats.failed || 0) + (stats.broken || 0);
            const reportUrl = `./${scope}/${report}/`;

            reportsData.push({
                name: report,
                passed: passed,
                failed: failed,
                lastRun: mtime,
                formattedLastRun: formattedLastRun,
                reportUrl: reportUrl
            });
        }
    }
}

reportsData.sort((a, b) => b.lastRun - a.lastRun);

let tableRows = '';
for (const data of reportsData) {
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
