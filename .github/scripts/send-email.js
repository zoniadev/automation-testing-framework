// .github/scripts/send-email.js
const fs = require('fs');
const nodemailer = require('nodemailer');

// SMTP credentials from GitHub Secrets
const smtpUser = process.env.SMTP_USER;
const smtpPass = process.env.SMTP_PASS;
const smtpHost = process.env.SMTP_HOST;
const smtpPort = process.env.SMTP_PORT;

// Check if the SMTP credentials are available
if (!smtpUser || !smtpPass || !smtpHost || !smtpPort) {
  console.error('SMTP credentials not found.');
  process.exit(1);
}

// Read the test summary
let testSummary = 'Test summary not available.';
try {
  testSummary = fs.readFileSync('./test-summary.txt', 'utf8');
} catch (err) {
  console.error('Error reading test summary:', err);
}
const colors = {
  Green: "#28a745",
  Red: "#dc3545",
  Gray: "#6c757d",
  Yellow: "#ffc107",
}

async function sendEmail() {
  const lines = testSummary.split('\n');
  let emailContent = '<h1>Test Summary Report</h1>';

  emailContent += '<h2>Test Results:</h2><ul>';

  lines.forEach(line => {
    if (line.includes('Failed scenario')) {
      emailContent += `<li style="color:${colors.Red}"><strong>${line}</strong></li>`;
    } else if (line.includes('Screenshot saved')) {
      emailContent += `<li style="color:${colors.Gray};">${line}</li>`;
    } else if (line.includes('Failed feature') || line.includes('Starting run') || line.includes('Run completed')) {
      emailContent += `<li>${line}</li>`;
    } else if (line.startsWith('Failed scenario:')) {
      emailContent += `<li><strong>${line}</strong></li>`;
    } else {
      emailContent += `<li>${line}</li>`;
    }
  });

  emailContent += '</ul>';

  let transporter = nodemailer.createTransport({
    host: smtpHost,
    port: smtpPort,
    secure: smtpPort == 465, // true for 465, false for other ports
    auth: {
      user: smtpUser,
      pass: smtpPass,
    },
  });

  let info = await transporter.sendMail({
    from: `"Zonia Test Failure Notifier" <${smtpUser}>`,
    to: 'atanas.atanasov.dev@gmail.com',
    subject: 'Test Failure Report',
    text: `The test has failed. Please check the details below:\n\n${testSummary}`,
    html: `<b>The test has failed. Please check the details below:</b><pre>${testSummary}</pre>`,
  });

  console.log('Message sent: %s', info.messageId);
}

sendEmail().catch(console.error);
