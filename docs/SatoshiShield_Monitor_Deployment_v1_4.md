# SatoshiShield Pi-hole Surveillance Domain Monitor

*Deployment & Operations Guide*

Version 1.4 · May 2026
[github.com/cypherpilgrim/satoshishield](https://github.com/cypherpilgrim/satoshishield)

---

## 1. Overview

The SatoshiShield Pi-hole Monitor is a Python script that runs monthly on a Proxmox host, queries the Pi-hole FTL database for DNS queries matching known Bitcoin surveillance infrastructure, and emails a report.

It answers one question every month: did any device on the network try to contact a Bitcoin surveillance domain, and if so, is that domain already blocked by SatoshiShield or not?

> *All analysis happens locally on the Proxmox host. No DNS query data, IP addresses, or domain names leave the network. The only outbound connection is the email report sent via an SMTP relay.*

Throughout this guide, placeholders are used for values that depend on the user's environment:

- **<proxmox-host>** — the user's Proxmox host (IP address or hostname)

- **<proxmox-user>** — the SSH user with sudo access on the Proxmox host

- **<pihole-ct-id>** — the Proxmox container ID running Pi-hole (typically 100-200)

- **<report-email>** — the address that should receive the monthly report

- **<smtp-user>, <smtp-password>, <smtp-host>** — credentials for the SMTP relay (Gmail, Proton Bridge, or similar)

Quick facts:

- **Script name:** satoshishield_monitor.py

- **Runs on:** Proxmox host, accesses the Pi-hole container via pct pull

- **Schedule:** Monthly on the 1st at 08:00 by default

- **Report delivery:** <report-email> via an SMTP relay configured in .env

- **Lookback period:** 90 days by default, configurable

- **Script location:** /opt/satoshishield/satoshishield_monitor.py

## 2. What the Report Shows

### 2.1 New Surveillance Domains (alert)

Domains that matched surveillance patterns but are NOT yet in the SatoshiShield blocklist. These are the most important findings, as they may represent new surveillance infrastructure or wallet telemetry worth investigating and potentially submitting via GitHub pull request.

The report includes for each new domain:

- Organization and description of the surveillance activity

- Number of queries made in the lookback period

- First and last time the domain was queried

- Which client IP addresses made the queries

- The exact subdomain(s) that were queried

### 2.2 Known Blocked Domains Detected

Domains that ARE in the SatoshiShield blocklist but still appeared in Pi-hole query logs. This happens when:

- A device is bypassing Pi-hole DNS (using hardcoded DNS servers or DoH)

- The domain was queried before the block was applied

- A device is not covered by the Pi-hole DNS rules

If known blocked domains appear with high query counts, investigate which device is making the queries and why.

### 2.3 Clean Report

If no surveillance domains are detected, the report confirms the network is clean for the period. This is the expected outcome once SatoshiShield is fully deployed and all devices use Pi-hole for DNS.

## 3. Deployment

### 3.1 Create the Script Directory

On the Proxmox host, SSH in and create the SatoshiShield directory:

> ssh <proxmox-user>@<proxmox-host>
>
> sudo -i
>
> mkdir -p /opt/satoshishield
>
> cd /opt/satoshishield

### 3.2 Copy the Script to the Proxmox Host

Copy satoshishield_monitor.py to the Proxmox host from a local machine:

> # From the local machine:
>
> scp satoshishield_monitor.py <proxmox-user>@<proxmox-host>:/tmp/
>
> # Then on the Proxmox host:
>
> mv /tmp/satoshishield_monitor.py /opt/satoshishield/
>
> chmod +x /opt/satoshishield/satoshishield_monitor.py

### 3.3 Create the .env Configuration File

> **Never commit the .env file to git.** It contains SMTP credentials. The .gitignore in the SatoshiShield repository already excludes both /opt/satoshishield/.env and monitor/.env. Verify the .env file lives only on the Proxmox host and never in a tracked location.

On the Proxmox host, create /opt/satoshishield/.env with the following keys:

> # /opt/satoshishield/.env
>
> # chmod 600 this file after creating it
>
> SMTP_HOST=<smtp-host>
>
> SMTP_PORT=587
>
> SMTP_USER=<smtp-user>
>
> SMTP_PASSWORD=<smtp-password>
>
> REPORT_FROM=<smtp-user>
>
> REPORT_TO=<report-email>

Lock down permissions so only root can read the file:

> chmod 600 /opt/satoshishield/.env

### 3.4 Verify Python 3 is Available

> python3 --version
>
> # Expected: Python 3.x.x
>
> # If not installed:
>
> apt install python3 -y

### 3.5 Test the Script Manually

Run the script once manually to verify it works before setting up cron:

> python3 /opt/satoshishield/satoshishield_monitor.py

Expected output looks like:

> [2026-MM-DD HH:MM:SS] SatoshiShield Pi-hole monitor starting...
>
> Pulling Pi-hole FTL database from CT<pihole-ct-id>...
>
> Querying DNS logs for past 90 days...
>
> Found N unique domains, M total queries
>
> Matching against surveillance domain patterns...
>
> Found 0 surveillance domain matches
>
> Sending report to <report-email>...
>
> Report sent successfully.
>
> Summary: 0 new domains, 0 known blocked domains detected
>
> Temporary database file cleaned up.

Check the report inbox at <report-email>. If the report arrives, deployment is successful.

### 3.6 Set Up the Monthly Cron Job

Add the cron job on the Proxmox host:

> crontab -e

Add this line:

> # SatoshiShield Pi-hole surveillance domain monitor — runs monthly on 1st at 08:00
>
> 0 8 1 * * /usr/bin/python3 /opt/satoshishield/satoshishield_monitor.py >> /var/log/satoshishield.log 2>&1

Save and exit. Verify the cron job is registered:

> crontab -l

### 3.7 Verify Log File

After the first scheduled run, check the log:

> tail -50 /var/log/satoshishield.log

## 4. Configuration

### 4.1 Configuration Variables

All configuration lives at the top of satoshishield_monitor.py. Edit with:

> nano /opt/satoshishield/satoshishield_monitor.py

| **Variable**       | **Default**               | **Description**                                        |
|--------------------|---------------------------|--------------------------------------------------------|
| **PIHOLE_CT_ID**   | <pihole-ct-id>          | Proxmox CT ID for the Pi-hole container.               |
| **PIHOLE_DB_PATH** | /etc/pihole/pihole-FTL.db | Path to the FTL database inside the Pi-hole container. |
| **REPORT_DAYS**    | 90                        | Number of days to look back in query logs.             |
| **ENV_FILE**       | /opt/satoshishield/.env   | Path to the .env file containing SMTP credentials.     |

All credentials (SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, REPORT_FROM, REPORT_TO) are read from .env at runtime. None of these values are stored in the script itself.

### 4.2 Updating Surveillance Patterns

The SURVEILLANCE_PATTERNS dictionary in the script contains all monitored domain patterns. Update this whenever SatoshiShield releases a new version with new domains:

## 1. Download the latest domains.csv from [github.com/cypherpilgrim/satoshishield](https://github.com/cypherpilgrim/satoshishield)

## 2. Review new entries since the last update

## 3. Add new patterns to the relevant category in SURVEILLANCE_PATTERNS

## 4. Update the ALREADY_BLOCKED set with domains confirmed in the blocklist

## 5. Test: python3 /opt/satoshishield/satoshishield_monitor.py

## 5. Interpreting the Report

### 5.1 New Domain Found — What to Do

## 6. Note the domain, organization, query count, and client IPs from the report

## 7. Verify the domain using the Contributor Guide verification steps (WHOIS, SSL, URLScan)

## 8. Test that blocking the domain does not break wallet functionality

## 9. If confirmed surveillance, submit a pull request to [github.com/cypherpilgrim/satoshishield](https://github.com/cypherpilgrim/satoshishield)

## 10. Add the domain to ALREADY_BLOCKED in the script after the PR is merged

### 5.2 Known Domain Still Appearing — What to Do

## 11. Identify which client IP is making the queries

## 12. Check whether that device is using Pi-hole for DNS: nslookup example.com <pihole-ip>

## 13. If the device is bypassing Pi-hole, force DNS via firewall rules (pfSense, OPNsense, etc.)

## 14. If queries persist, the domain may be using hardcoded IPs, in which case a firewall block rule by IP is needed

### 5.3 Clean Report — What to Do

Nothing. A clean report means SatoshiShield is working as intended. File the report and schedule the next quarterly research cycle.

## 6. Maintenance

### 6.1 Monthly

- Review the report email when it arrives on the 1st

- Investigate any new domains found

- Submit PRs for confirmed surveillance domains

### 6.2 With Each SatoshiShield Release

- Update SURVEILLANCE_PATTERNS with new domains from domains.csv

- Update the ALREADY_BLOCKED set

- Run a manual test: python3 /opt/satoshishield/satoshishield_monitor.py

### 6.3 Check the Log File Periodically

> tail -100 /var/log/satoshishield.log

If the log shows errors, investigate before the next scheduled run.

Version Log

| **Version** | **Date** | **Summary**                                                                                                                                                                                                                                                     |
|-------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **1.0**     | May 2026 | Initial release. Monitors surveillance domain patterns across categories. Pulls Pi-hole FTL database via pct pull. Emails monthly report via SMTP relay. Distinguishes new (unblocked) domains from known blocked domains. Cron-deployed on Proxmox host.       |
| **1.4**     | May 2026 | Sanitized for public release. All operator-specific values (email addresses, IP addresses, SSH usernames, container IDs) replaced with placeholders. GitHub handle updated to cypherpilgrim. Reflects monitor script support for Tier 2 patterns added in v1.3. |

[github.com/cypherpilgrim/satoshishield](https://github.com/cypherpilgrim/satoshishield) | MIT License
