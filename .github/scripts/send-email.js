// .github/scripts/send-email.js
const fs = require('fs');
const nodemailer = require('nodemailer');

// SMTP credentials from GitHub Secrets
const smtpUser = process.env.SMTP_USER;
const smtpPass = process.env.SMTP_PASS;
const smtpHost = process.env.SMTP_HOST;
const smtpPort = process.env.SMTP_PORT;
const colors = {
  Green: "#28a745",
  Red: "#dc3545",
  Gray: "#6c757d",
  Yellow: "#ffc107",
}

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
    from: `"Zonia Test Failure Notifier" <${smtpUser}>`,
    to: 'atanas.atanasov.dev@gmail.com',
    subject: 'Test Failure Report',
    text: `The test has failed. Please check the details below:\n\n${testSummary}`,
    html: formatTestSummary(testSummary),
  });

  console.log('Message sent: %s', info.messageId);
}

sendEmail().catch(console.error);



function formatTestSummary(testSummary) {

  // Initialize HTML content
  let htmlContent = '<h1>Test Summary Report</h1>';

  // Split the summary into lines
  const lines = testSummary.split('\n');

  let currentFeature = '';
  let inFeature = false;
  let completed = false;

  // Helper function to style and append scenario
  const appendScenario = (scenario, result) => {
    const color = result === 'failed' ? colors.Red : colors.Green;
    htmlContent += `<li style="color: ${color};"><strong>${scenario}</strong></li>`;
  };

  // Process each line
  lines.forEach(line => {
    if (completed) {
      htmlContent += `<br>${line}`;
    }

    if (line.includes('Executing feature:')) {
      if (inFeature) {
        // Close the previous feature section
        htmlContent += '</ul>';
      }
      // Start a new feature section
      currentFeature = line;
      htmlContent += `<h2>${currentFeature}</h2><ul>`;
      inFeature = true;
    } else if (line.startsWith('Failed scenario:') || line.startsWith('Completed scenario:')) {
      const status = line.startsWith('Failed') ? 'failed' : 'succeeded';
      appendScenario(line, status);
    } else if (line.includes('Failed feature:') || line.includes('Run completed')) {
      // End the current feature section
      if (inFeature) {
        htmlContent += '</ul>';
        inFeature = false;
      }
      // Add additional information
      htmlContent += `<p><strong>${line}</strong></p>`;
      if (line.includes('Run completed')) {
        completed = true; // Set flag to stop processing further lines
      }
    }
  });

  // Close any open feature section
  if (inFeature) {
    htmlContent += '</ul>';
  }

  return htmlContent;
}