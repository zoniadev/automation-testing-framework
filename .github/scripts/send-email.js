// .github/scripts/send-email.js
const fs = require('fs');
const nodemailer = require('nodemailer');

// SMTP credentials from GitHub Secrets
const smtpUser = process.env.SMTP_USER;
const smtpPass = process.env.SMTP_PASS;
const smtpHost = process.env.SMTP_HOST;
const smtpPort = process.env.SMTP_PORT;
const targetURL = process.env.TARGET_URL;
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
  console.log('Test summary:', testSummary);
} catch (err) {
  console.error('Error reading test summary:', err);
}

if (!testSummary.includes('Failed scenario:')) {
  console.log('No failed scenarios found.');
  process.exit(0);
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
    to: ['atanas.atanasov.dev@gmail.com', 'nkalendzhiev@yahoo.com', 'healthywithstefan@gmail.com', 'skukudov.zonia@gmail.com', 'gergana.zonia@gmail.com', 'tsvetan.zonia@gmail.com'],
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
  let skipRedundantFailingList = false;

  // Helper function to style and append scenario
  const appendScenario = (scenario, result) => {
    const color = result === 'failed' ? colors.Red : colors.Green;
    htmlContent += `<li style="color: ${color};"><strong>${scenario}</strong></li>`;
  };

  // Process each line
  lines.forEach(line => {
    // 1. Explicitly ignore noisy lines
    if (
      line.includes('Screenshot saved:') ||
      line.includes('Screenshot saved to') ||
      line.includes('HOOK-ERROR') ||
      line.includes('Cleaning up the DB') ||
      line.includes('Connected to MongoDB') ||
      line.includes('Deleted') && line.includes('user(s)') ||
      line.trim() === '' // Ignore empty lines to prevent excessive spacing
    ) {
      return;
    }

    // 2. Handle the "Failing scenarios:" block to skip it, but KEEP the stats below it
    if (line.startsWith('Failing scenarios:')) {
      skipRedundantFailingList = true;
      return; // Skip this specific line
    }

    if (skipRedundantFailingList) {
      // While in the block, ignore lines that look like file paths (the redundant list)
      if (line.trim().startsWith('features/')) {
        return; // Skip the redundant path line
      } else {
        // Once we hit something that isn't a file path (like the stats block), stop skipping
        skipRedundantFailingList = false;
      }
    }

    // 3. Process normal lines
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
        htmlContent += '<hr>'
      }
    } else {
      if (inFeature) {
        // Only add list items if we are actually inside a feature block and it's not noise
        htmlContent += `<li style="padding-left:15px;">${line}</li>`;
      } else {
        // If we are outside a feature (usually at the end), color code the stats
        const coloredLine = colorCodeLineAfterCompleted(line);
        if (coloredLine !== line) {
             // Only add a break if it's one of the stats lines
             htmlContent += `<br>${coloredLine}`;
        } else {
             // Plain text outside a feature block (e.g. "Took 30m0.306s")
             htmlContent += `<br>${line}`;
        }
      }
    }
  });

  // Close any open feature section
  if (inFeature) {
    htmlContent += '</ul>';
  }

  htmlContent += `<br><p>For more details, please visit the <a href="${targetURL}">test report</a>.</p>`;

  return htmlContent;
}

function colorCodeLineAfterCompleted(line) {
  //X (features/scenarios/steps) passed, Y filed, Z skipped should be colored with colors.Green, Red, Yellow if the X, Y, Z is not 0. 0 values should be gray
  const regex = /(\d+) (features|scenarios|steps) passed, (\d+) failed, (\d+) skipped(?:, (\d+) undefined)?(?:, (\d+) untested)?/;

  return line.replace(regex, (match, passed, type, failed, skipped, undefined, untested) => {
    // Determine colors based on the values
    const passedColor = passed != 0 ? colors.Green : colors.Gray;
    const failedColor = failed != 0 ? colors.Red : colors.Gray;
    const skippedColor = skipped != 0 ? colors.Yellow : colors.Gray;
    const undefinedColor = undefined ? colors.Gray : '';
    const untestedColor = untested ? colors.Gray : '';

    let result = `<span style="color:${passedColor}">${passed} ${type} passed</span>, ` +
      `<span style="color:${failedColor}; font-weight:bold;">${failed} failed</span>, ` +
      `<span style="color:${skippedColor}">${skipped} skipped</span>`;

    if (undefined) {
        result += `, <span style="color:${undefinedColor}">${undefined} undefined</span>`;
    }
    if (untested) {
        result += `, <span style="color:${untestedColor}">${untested} untested</span>`;
    }

    return result;
  });
}