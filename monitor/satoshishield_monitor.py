#!/usr/bin/env python3
"""
SatoshiShield Pi-hole Surveillance Domain Monitor

Runs monthly on the Proxmox host. Queries the Pi-hole FTL database for DNS
queries matching known Bitcoin surveillance infrastructure and emails a
report to the configured recipient.

Distinguishes new (unblocked) surveillance domains from already-blocked ones.

Deployment: /opt/satoshishield/satoshishield_monitor.py
Schedule:   Monthly on the 1st at 08:00 (cron)
Project:    https://github.com/cypherpilgrim/satoshishield
"""

import os
import re
import smtplib
import sqlite3
import subprocess
import sys
import tempfile
from collections import defaultdict
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# Pi-hole container
PIHOLE_CT_ID = "107"
PIHOLE_DB_PATH = "/etc/pihole/pihole-FTL.db"

# Lookback window (days)
REPORT_DAYS = 90

# SMTP — all credentials and addresses read from .env (gitignored)
# Required keys in /opt/satoshishield/.env:
#   SMTP_HOST=smtp.gmail.com
#   SMTP_PORT=587
#   SMTP_USER=your-relay-account@example.com
#   SMTP_PASSWORD=your-smtp-app-password
#   REPORT_FROM=your-relay-account@example.com
#   REPORT_TO=where-the-report-goes@example.com
ENV_FILE = "/opt/satoshishield/.env"

# ---------------------------------------------------------------------------
# Surveillance domain patterns
#
# Two categories:
#   ALREADY_BLOCKED — domains we know are in the Pi-hole blocklist (regex deny
#                     rules in gravity.db). Queries to these still appear in
#                     the FTL log but were dropped. We report them so we can
#                     identify devices bypassing Pi-hole.
#
#   SURVEILLANCE_PATTERNS — categorical patterns for matching surveillance
#                           firm domains. Includes the firms above (so they
#                           cross-match) plus speculative/Tier 2 patterns we
#                           want to flag for human review when seen.
# ---------------------------------------------------------------------------

ALREADY_BLOCKED = {
    "chainalysis.com",
    "transpose.io",
    "elliptic.co",
    "trmlabs.com",
    "ciphertrace.com",
    "arkm.com",
    "crystalblockchain.com",
    "bitrank.com",
    "scorechain.com",
    "merkle.science",
    "metasleuth.io",
    "breadcrumbs.app",
    "nansen.ai",
    "glassnode.com",
}

# Pattern -> (organization, category, description)
# Pattern is a regex that will be matched against full query domains.
# Use (?:\.|^) anchoring so api.foo.com matches but notfoo.com does not.
SURVEILLANCE_PATTERNS = {
    # Tier 1 — Blockchain Analytics (already blocked, but useful to detect
    # if a client is still trying to reach them — indicates DNS bypass)
    r"(?:\.|^)chainalysis\.com$":      ("Chainalysis",       "Blockchain Analytics", "Primary blockchain surveillance firm; sells intel to law enforcement and exchanges"),
    r"(?:\.|^)transpose\.io$":         ("Chainalysis",       "Blockchain Analytics", "Transpose API — owned by Chainalysis"),
    r"(?:\.|^)elliptic\.co$":          ("Elliptic",          "Blockchain Analytics", "Transaction monitoring and compliance APIs"),
    r"(?:\.|^)trmlabs\.com$":          ("TRM Labs",          "Blockchain Analytics", "BLOCKINT API — correlates address queries with IP"),
    r"(?:\.|^)ciphertrace\.com$":      ("CipherTrace",       "Blockchain Analytics", "Mastercard-owned blockchain analytics"),
    r"(?:\.|^)arkm\.com$":             ("Arkham",            "Deanonymization",      "Publicly markets identity-linking; logs every address lookup"),
    r"(?:\.|^)crystalblockchain\.com$":("Crystal",           "Blockchain Analytics", "Transaction monitoring and risk scoring"),
    r"(?:\.|^)bitrank\.com$":          ("Crystal (BitRank)", "Blockchain Analytics", "BitRank scoring service"),
    r"(?:\.|^)scorechain\.com$":       ("Scorechain",        "KYC/AML",              "Flags privacy-enhancing transactions including CoinJoin"),
    r"(?:\.|^)merkle\.science$":       ("Merkle Science",    "Blockchain Analytics", "Predictive risk platform; logs address queries"),
    r"(?:\.|^)metasleuth\.io$":        ("MetaSleuth",        "Deanonymization",      "Crypto tracking and investigation platform"),
    r"(?:\.|^)breadcrumbs\.app$":      ("Breadcrumbs",       "Blockchain Analytics", "Free blockchain analytics tool"),
    r"(?:\.|^)nansen\.ai$":            ("Nansen",            "Surveillance Analytics","Wallet labeling and identity profiling"),
    r"(?:\.|^)glassnode\.com$":        ("Glassnode",         "Market Surveillance",  "On-chain analytics; logs IP against queries"),
}

# ---------------------------------------------------------------------------
# Implementation
# ---------------------------------------------------------------------------

def log(msg):
    """Print timestamped log message."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {msg}", flush=True)


def load_env():
    """Load full SMTP config from /opt/satoshishield/.env.

    Returns a dict with keys: smtp_host, smtp_port, smtp_user, smtp_password,
    report_from, report_to.
    """
    env_path = Path(ENV_FILE)
    if not env_path.exists():
        log(f"FATAL: env file not found at {ENV_FILE}")
        log("Create it with the required keys (see header of this script).")
        sys.exit(1)

    env_vars = {}
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            key, _, value = line.partition("=")
            env_vars[key.strip()] = value.strip().strip('"').strip("'")

    required = ["SMTP_HOST", "SMTP_PORT", "SMTP_USER", "SMTP_PASSWORD",
                "REPORT_FROM", "REPORT_TO"]
    missing = [k for k in required if not env_vars.get(k)]
    if missing:
        log(f"FATAL: missing required keys in .env: {', '.join(missing)}")
        sys.exit(1)

    return {
        "smtp_host":     env_vars["SMTP_HOST"],
        "smtp_port":     int(env_vars["SMTP_PORT"]),
        "smtp_user":     env_vars["SMTP_USER"],
        "smtp_password": env_vars["SMTP_PASSWORD"],
        "report_from":   env_vars["REPORT_FROM"],
        "report_to":     env_vars["REPORT_TO"],
    }


def pull_pihole_db():
    """Pull pihole-FTL.db from CT107 to a temporary file."""
    log(f"Pulling Pi-hole FTL database from CT{PIHOLE_CT_ID}...")
    tmpfile = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
    tmpfile.close()
    try:
        subprocess.run(
            ["pct", "pull", PIHOLE_CT_ID, PIHOLE_DB_PATH, tmpfile.name],
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as e:
        log(f"FATAL: pct pull failed: {e.stderr}")
        os.unlink(tmpfile.name)
        sys.exit(1)
    return tmpfile.name


def query_ftl(db_path, lookback_days):
    """Query FTL database for all DNS queries in the lookback window.

    Returns list of (timestamp, client_ip, domain) tuples.
    """
    cutoff = int((datetime.now() - timedelta(days=lookback_days)).timestamp())
    log(f"Querying DNS logs for past {lookback_days} days "
        f"(from {datetime.fromtimestamp(cutoff)})...")

    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    cur = conn.cursor()
    cur.execute(
        "SELECT timestamp, client, domain FROM queries "
        "WHERE timestamp >= ? "
        "ORDER BY timestamp ASC",
        (cutoff,),
    )
    rows = cur.fetchall()
    conn.close()

    unique_domains = {row[2] for row in rows}
    log(f"Found {len(unique_domains)} unique domains, {len(rows)} total queries")
    return rows


def match_surveillance(rows):
    """Bucket queries by surveillance pattern.

    Returns dict keyed by matched root domain. Each value is a dict:
      {
        'organization': str,
        'category': str,
        'description': str,
        'already_blocked': bool,
        'query_count': int,
        'first_seen': datetime,
        'last_seen': datetime,
        'clients': set of IPs,
        'subdomains': set of full domain names that matched,
      }
    """
    # Precompile patterns
    compiled = [
        (re.compile(pat, re.IGNORECASE), root_from_pattern(pat), meta)
        for pat, meta in SURVEILLANCE_PATTERNS.items()
    ]

    matches = defaultdict(lambda: {
        "organization": "",
        "category": "",
        "description": "",
        "already_blocked": False,
        "query_count": 0,
        "first_seen": None,
        "last_seen": None,
        "clients": set(),
        "subdomains": set(),
    })

    for timestamp, client, domain in rows:
        if not domain:
            continue
        for regex, root, (org, category, desc) in compiled:
            if regex.search(domain):
                entry = matches[root]
                entry["organization"] = org
                entry["category"] = category
                entry["description"] = desc
                entry["already_blocked"] = root in ALREADY_BLOCKED
                entry["query_count"] += 1
                ts = datetime.fromtimestamp(timestamp)
                if entry["first_seen"] is None or ts < entry["first_seen"]:
                    entry["first_seen"] = ts
                if entry["last_seen"] is None or ts > entry["last_seen"]:
                    entry["last_seen"] = ts
                entry["clients"].add(client)
                entry["subdomains"].add(domain)
                break  # Only match first pattern

    return dict(matches)


def root_from_pattern(pattern):
    """Extract the root domain from a regex pattern like (?:\\.|^)foo\\.com$"""
    # Strip the anchoring and unescape dots
    cleaned = pattern.replace(r"(?:\.|^)", "").replace(r"\.", ".").rstrip("$")
    return cleaned


def build_report(matches, lookback_days):
    """Build the email report. Returns (subject, body)."""
    new_domains = {k: v for k, v in matches.items() if not v["already_blocked"]}
    known_blocked = {k: v for k, v in matches.items() if v["already_blocked"]}

    # Subject by severity
    if new_domains:
        subject = f"🚨 SatoshiShield Alert: {len(new_domains)} new surveillance domain(s) detected"
    elif known_blocked:
        subject = f"⚠️ SatoshiShield: {len(known_blocked)} known blocked domain(s) still active"
    else:
        subject = "✓ SatoshiShield: Clean — no surveillance domains detected"

    # Body
    lines = []
    lines.append("SatoshiShield Pi-hole Surveillance Domain Monitor")
    lines.append("=" * 60)
    lines.append(f"Report date:     {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"Lookback period: {lookback_days} days")
    lines.append(f"Host:            Proxmox / CT{PIHOLE_CT_ID}")
    lines.append("")

    if new_domains:
        lines.append("!! NEW SURVEILLANCE DOMAINS (NOT IN BLOCKLIST)")
        lines.append("=" * 60)
        lines.append("These domains matched surveillance patterns but are NOT yet")
        lines.append("blocked by SatoshiShield. Verify each and consider submitting")
        lines.append("a pull request: https://github.com/cypherpilgrim/satoshishield")
        lines.append("")
        for root, entry in sorted(new_domains.items()):
            lines.extend(format_match(root, entry))
            lines.append("")

    if known_blocked:
        lines.append("KNOWN BLOCKED DOMAINS — STILL BEING QUERIED")
        lines.append("=" * 60)
        lines.append("These domains ARE in the SatoshiShield blocklist but appeared")
        lines.append("in Pi-hole query logs. Pi-hole dropped the queries, but the")
        lines.append("client(s) below tried to contact surveillance infrastructure.")
        lines.append("If query counts are high, investigate whether the device is")
        lines.append("bypassing Pi-hole DNS.")
        lines.append("")
        for root, entry in sorted(known_blocked.items()):
            lines.extend(format_match(root, entry))
            lines.append("")

    if not new_domains and not known_blocked:
        lines.append("CLEAN REPORT")
        lines.append("=" * 60)
        lines.append("No surveillance domains were detected in the lookback window.")
        lines.append("Your network is clean for the period.")
        lines.append("")
        lines.append("This is the expected outcome once SatoshiShield is fully")
        lines.append("deployed and all devices use Pi-hole for DNS.")
        lines.append("")

    lines.append("=" * 60)
    lines.append("SatoshiShield — https://github.com/cypherpilgrim/satoshishield")

    return subject, "\n".join(lines)


def format_match(root, entry):
    """Format a single matched domain entry for the report body."""
    out = []
    out.append(f"  Domain (root):   {root}")
    out.append(f"  Organization:    {entry['organization']}")
    out.append(f"  Category:        {entry['category']}")
    out.append(f"  Description:     {entry['description']}")
    out.append(f"  Query count:     {entry['query_count']}")
    out.append(f"  First seen:      {entry['first_seen']}")
    out.append(f"  Last seen:       {entry['last_seen']}")
    out.append(f"  Client IPs:      {', '.join(sorted(entry['clients']))}")
    if len(entry["subdomains"]) <= 10:
        out.append(f"  Subdomains:      {', '.join(sorted(entry['subdomains']))}")
    else:
        sample = sorted(entry["subdomains"])[:10]
        out.append(f"  Subdomains:      {', '.join(sample)} ... ({len(entry['subdomains'])} total)")
    return out


def send_email(subject, body, cfg):
    """Send the report via SMTP using the loaded config."""
    log(f"Sending report to {cfg['report_to']}...")
    msg = MIMEMultipart()
    msg["From"] = cfg["report_from"]
    msg["To"] = cfg["report_to"]
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(cfg["smtp_host"], cfg["smtp_port"], timeout=30) as server:
            server.starttls()
            server.login(cfg["smtp_user"], cfg["smtp_password"])
            server.send_message(msg)
        log("Report sent successfully.")
    except Exception as e:
        log(f"FATAL: SMTP send failed: {e}")
        sys.exit(1)


def main():
    log("SatoshiShield Pi-hole monitor starting...")
    cfg = load_env()

    db_path = pull_pihole_db()
    try:
        rows = query_ftl(db_path, REPORT_DAYS)
        log("Matching against surveillance domain patterns...")
        matches = match_surveillance(rows)
        new_count = sum(1 for v in matches.values() if not v["already_blocked"])
        known_count = sum(1 for v in matches.values() if v["already_blocked"])
        log(f"Found {len(matches)} surveillance domain matches "
            f"({new_count} new, {known_count} known blocked)")

        subject, body = build_report(matches, REPORT_DAYS)
        send_email(subject, body, cfg)
        log(f"Summary: {new_count} new domains, {known_count} known blocked domains detected")
    finally:
        log("Temporary database file cleaned up.")
        os.unlink(db_path)


if __name__ == "__main__":
    main()
