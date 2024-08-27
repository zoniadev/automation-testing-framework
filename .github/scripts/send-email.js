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
  console.log('1')
  console.log(fs.readFileSync('../test-summary.txt', 'utf8'));
  testSummary = fs.readFileSync('test-summary.txt', 'utf8');
  console.log('2')
  console.log(fs.readFileSync('../test-summary.txt', 'utf8'));
  console.log('3')
  console.log(fs.readFileSync('../../test-summary.txt', 'utf8'));
} catch (err) {
  console.error('Error reading test summary:', err);
}

async function sendEmail() {
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
    from: `"Test Failure Notifier" <${smtpUser}>`,
    to: 'atanas.atanasov.dev@gmail.com',
    subject: 'Test Failure Report',
    text: `The test has failed. Please check the details below:\n\n${testSummary}`,
    html: `<b>The test has failed. Please check the details below:</b><pre>${testSummary}</pre>`,
  });

  console.log('Message sent: %s', info.messageId);
}

sendEmail().catch(console.error);
