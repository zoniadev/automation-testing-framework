#!/usr/bin/env bash
# Samples runner CPU/RAM/disk/process stats on a fixed interval and appends
# them to a log file, so we can correlate a test failure's timestamp with
# what the GitHub Actions VM was doing at that moment.
#
# Usage: resource-monitor.sh <log-file> [interval-seconds]
# Intended to be started in the background (nohup ... &) and killed once the
# test step finishes; the log is then uploaded as a build artifact.

set -uo pipefail

LOG_FILE="${1:?log file path required}"
INTERVAL="${2:-5}"

{
  echo "===== Runner static info ====="
  echo "Timestamp (UTC): $(date -u +%FT%TZ)"
  echo "Runner name:     ${RUNNER_NAME:-unknown}"
  echo "Runner OS/arch:  ${RUNNER_OS:-unknown} ${RUNNER_ARCH:-unknown}"
  echo "Image OS:        ${ImageOS:-unknown}"
  echo "CPUs (nproc):    $(nproc 2>/dev/null || echo unknown)"
  echo "--- lscpu ---"
  lscpu 2>/dev/null || echo "lscpu not available"
  echo "--- meminfo (total) ---"
  grep -E 'MemTotal|SwapTotal' /proc/meminfo 2>/dev/null || echo "not available"
  echo "--- disk (initial) ---"
  df -h / /home 2>/dev/null || df -h
  echo "==============================="
} > "$LOG_FILE"

echo "Resource monitor started (PID $$), sampling every ${INTERVAL}s -> $LOG_FILE"

while true; do
  {
    echo "----- $(date -u +%FT%T.%3NZ) -----"

    echo "--- load average (1m 5m 15m / running/total procs / last pid) ---"
    cat /proc/loadavg 2>/dev/null

    echo "--- memory (MB) ---"
    free -m

    echo "--- cpu (vmstat: r b swpd free buff cache si so bi bo in cs us sy id wa st) ---"
    # 'st' (last column) is CPU steal time - time a noisy-neighbor VM stole
    # from us on the shared hypervisor. High st with low local load is the
    # classic "it's the runner, not us" signature.
    vmstat 1 2 2>/dev/null | tail -n 1

    echo "--- disk ---"
    df -h / 2>/dev/null

    echo "--- top 10 processes by RSS (look for chromium/node/python) ---"
    ps -eo pid,ppid,%cpu,%mem,rss,etimes,comm --sort=-%mem 2>/dev/null | head -n 11

    echo "--- chromium/node process count ---"
    # A leaked/zombie browser process count that climbs over the job is a
    # strong signal of the "next test fails on initial load" pattern.
    # pgrep -c already prints 0 on no match (it just exits non-zero too),
    # so no "|| echo 0" fallback needed - that would double-print the 0.
    echo "chromium-ish: $(pgrep -c -f 'chrome|chromium' 2>/dev/null)"
    echo "node:         $(pgrep -c -f node 2>/dev/null)"

  } >> "$LOG_FILE" 2>&1

  sleep "$INTERVAL"
done
