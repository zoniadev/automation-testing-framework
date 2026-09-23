// .github/scripts/send-cleanup-failure-email.js
//
// Separate from send-email.js: that one goes to management and only fires on
// a failed scenario. This one is a personal heads-up, sent only when the
// old-user DB cleanup in features/environment.py's after_all fails - which
// today only shows up if someone opens the raw GitHub Actions log.
const fs = require('fs');
const nodemailer = require('nodemailer');

const smtpUser = process.env.SMTP_USER;
const smtpPass = process.env.SMTP_PASS;
const smtpHost = process.env.SMTP_HOST;
const smtpPort = process.env.SMTP_PORT;
const runURL = process.env.RUN_URL;
const recipient = 'nkalendzhiev@yahoo.com';

// The two ways a cleanup failure shows up in test-summary.txt:
//  - clean_automation_users_with_api() printing its own error on a non-200 response
//  - behave itself, if the cleanup call raises (network error, bad JSON, ...),
//    catches it in after_all and prints "HOOK-ERROR in after_all: ..."
const FAILURE_MARKERS = ['Error deleting user(s)!', 'HOOK-ERROR in after_all'];

if (!smtpUser || !smtpPass || !smtpHost || !smtpPort) {
  console.error('SMTP credentials not found.');
  process.exit(1);
}

let testSummary = '';
try {
  testSummary = fs.readFileSync('./test-summary.txt', 'utf8');
} catch (err) {
  console.error('Error reading test summary:', err);
  process.exit(0);
}

const failureLines = testSummary
  .split('\n')
  .filter(line => FAILURE_MARKERS.some(marker => line.includes(marker)));

if (failureLines.length === 0) {
  console.log('No cleanup failure detected.');
  process.exit(0);
}

async function sendEmail() {
  const transporter = nodemailer.createTransport({
    host: smtpHost,
    port: smtpPort,
    secure: smtpPort == 465,
    auth: {
      user: smtpUser,
      pass: smtpPass,
    },
  });

  const details = failureLines.join('\n');
  const runLine = runURL ? `\n\nRun: ${runURL}` : '';

  const info = await transporter.sendMail({
    from: `"Zonia Test Cleanup Notifier" <${smtpUser}>`,
    to: recipient,
    subject: 'Automation user cleanup failed',
    text: `The old-user DB cleanup step failed:\n\n${details}${runLine}`,
  });

  console.log('Cleanup failure email sent: %s', info.messageId);
}

sendEmail().catch(console.error);
