# Monitor Report — Reading Guide

### How to read, interpret, and act on the monthly surveillance domain report

**Version 1.0  ·  May 2026**

Published by SatoshiShield  ·  [github.com/cypherpilgrim/satoshishield](https://github.com/cypherpilgrim/satoshishield)

---

## Table of Contents

- [About This Guide](#about-this-guide)
- [1. What This Report Is](#1-what-this-report-is)
- [2. How the Monitor Works](#2-how-the-monitor-works)
- [3. Reading the Subject Line](#3-reading-the-subject-line)
- [4. Report Body Structure](#4-report-body-structure)
  - [4.1 Header Block](#41-header-block)
  - [4.2 New Surveillance Domains](#42-new-surveillance-domains-when-present)
  - [4.3 Known Blocked Domains](#43-known-blocked-domains-when-present)
  - [4.4 Clean Report](#44-clean-report-when-nothing-was-found)
- [5. The Fields in Each Domain Entry](#5-the-fields-in-each-domain-entry)
- [6. Interpreting the Counts](#6-interpreting-the-counts)
  - [6.1 Was this me testing — or real activity?](#61-was-this-me-testing--or-real-activity)
  - [6.2 What's a normal count?](#62-whats-a-normal-count)
- [7. What to Do With Each Finding](#7-what-to-do-with-each-finding)
  - [7.1 New domain found](#71-new-domain-found)
  - [7.2 Known domain still being queried](#72-known-domain-still-being-queried)
  - [7.3 Clean report](#73-clean-report)
- [8. Identifying Client IPs on Your Network](#8-identifying-client-ips-on-your-network)
- [9. Troubleshooting the Report Itself](#9-troubleshooting-the-report-itself)
- [10. Walking Through a Sample Entry](#10-walking-through-a-sample-entry)
- [11. Recap — How to Read Any Report in 60 Seconds](#11-recap--how-to-read-any-report-in-60-seconds)
- [Document Version](#document-version)

---

## About This Guide

This guide explains how to read, interpret, and act on the monthly SatoshiShield Monitor Report. It is written as a companion to the Monitor Deployment Guide, which covers installation and configuration.

Throughout this document, placeholders like `<your-pihole-ip>`, `<your-proxmox-host>`, and `<your-email>` stand in for values specific to your network. Replace them with your own when applying the examples.

> This guide is generic by design. The report format and interpretation logic are the same for everyone, but the specific IPs, devices, and apps that appear in your reports will be unique to your network.

---

## 1. What This Report Is

The SatoshiShield Monitor Report is a monthly email summary of all DNS queries on your network that matched known Bitcoin surveillance infrastructure patterns. It tells you, in one glance, whether any device on your network is talking to a blockchain analytics firm — or trying to.

It answers two questions:

- Are there any new surveillance domains being queried that are NOT yet in the SatoshiShield blocklist?
- Are any already-blocked surveillance domains still being attempted — and if so, which devices are trying?

---

## 2. How the Monitor Works

The script runs on the Proxmox host at 08:00 on the first of each month via cron. It performs five steps:

1. Pulls Pi-hole's FTL database from the Pi-hole container using `pct pull` to a temporary file on the host.
2. Queries 90 days of DNS logs from the FTL database — every domain queried, by which client, when.
3. Matches against 14 surveillance patterns covering Chainalysis, Elliptic, TRM Labs, and the rest of the SatoshiShield Tier 1 list.
4. Builds a report sorted into two buckets: new (unblocked) surveillance domains and known-blocked domains.
5. Emails the report via your configured SMTP relay to your configured recipient address.

No DNS query data, IP addresses, or domain names leave your network. The only outbound connection is the SMTP submission to your relay.

> Pi-hole drops blocked queries before they leave your network — but the attempt is still logged. The monitor uses those logs to show you what would have leaked without SatoshiShield.

---

## 3. Reading the Subject Line

The subject line tells you the severity of the report at a glance. There are three possible subjects:

| Subject | Meaning |
|---|---|
| 🚨 SatoshiShield Alert: N new surveillance domain(s) detected | Urgent. A domain matched a surveillance pattern but is NOT in the blocklist. Investigate and submit a pull request. |
| ⚠️ SatoshiShield: N known blocked domain(s) still active | Informational. Domains in the blocklist were attempted by clients on your network. Pi-hole dropped them. Look at which clients and why. |
| ✓ SatoshiShield: Clean — no surveillance domains detected | All-clear. No surveillance domains were queried in the 90-day window. Expected outcome on a healthy, well-protected network. |

---

## 4. Report Body Structure

The body has three sections that appear conditionally based on what was found:

### 4.1  Header Block

Always present. Identifies the report run:

```
Report date:     <run timestamp>
Lookback period: 90 days
Host:            <your-proxmox-host> / <pihole-container>
```

### 4.2  New Surveillance Domains (when present)

Lists every domain that matched a surveillance pattern but is NOT in the blocklist. These need attention.

Each entry shows: organization name, category, description of the harm, query count, first/last seen timestamps, the client IPs that queried it, and the specific subdomains involved.

### 4.3  Known Blocked Domains (when present)

Lists domains that ARE in the SatoshiShield blocklist but still appeared in Pi-hole query logs. These were dropped — but the attempt happened.

This bucket is the most useful for understanding which apps and devices on your network are calling home to surveillance infrastructure. The domain didn't resolve, but you now know something tried.

### 4.4  Clean Report (when nothing was found)

Confirms your network is clean for the period. This is the expected outcome once SatoshiShield is fully deployed and every device routes DNS through Pi-hole.

---

## 5. The Fields in Each Domain Entry

Every matched domain in the report shows the same nine fields. Here's what each one means and how to use it:

| Field | What it shows | How to use it |
|---|---|---|
| **Domain (root)** | The root domain that matched, e.g. `chainalysis.com` | Identifies the organization. Cross-reference with `domains.csv` in the SatoshiShield repo. |
| **Organization** | The company operating this domain | Tells you who you'd have been correlated with if the query had succeeded. |
| **Category** | Blockchain Analytics, Deanonymization, KYC/AML, Market Surveillance, etc. | Helps you assess the privacy harm. Deanonymization is the most direct identity link. |
| **Description** | One-line summary of what this organization does and how they harm privacy | Decide whether this is something you'd ever want allowed (almost never) or blocked permanently. |
| **Query count** | Total number of queries in the 90-day window | Single digits = probably testing or one-off. Hundreds = a device is making sustained attempts. |
| **First seen** | Earliest timestamp of any matching query | Recent = new behavior. Long ago = sustained over time. Compare to when you installed an app. |
| **Last seen** | Most recent timestamp of any matching query | If last seen is days ago, the source may have stopped. Recent = ongoing. |
| **Client IPs** | Source IP(s) of devices that issued the queries | The most actionable field. Tells you exactly which devices on your network are calling home. |
| **Subdomains** | The full hostnames that matched (e.g. `api.chainalysis.com`) | Reveals what API or endpoint was contacted. Useful for figuring out which app made the call. |

---

## 6. Interpreting the Counts

The numbers tell a story. Here's how to read them:

### 6.1  Was this me testing — or real activity?

After a session of testing SatoshiShield, the first report can show inflated counts. Distinguishing test traffic from real surveillance attempts:

| Signal | Interpretation |
|---|---|
| Subdomains contain `fresh-test-`, `claude-test-`, or `this-is-a-test-` | Your testing. Filter these out mentally — they'll age out of the 90-day window. |
| Client IP is `127.0.0.1` | Queries made by Pi-hole itself (the CT querying its own resolver). Likely from manual testing. |
| First seen is within the last 24-48 hours and you were testing | Likely test traffic. Will age out of the 90-day window over time. |
| Client IP is a workstation, laptop, or your firewall itself | Could be testing OR a real app on those devices. Check the subdomains to tell which. |
| Client IP is your Bitcoin node, hardware wallet host, or a less-frequently-used device | Real activity. Worth investigating what app made the call. |
| Subdomains are real (`api.`, `markets.`, `intel.`, `data.`) and counts are in dozens or hundreds | Real surveillance attempt. Identify the source app and consider whether to keep using it. |
| Same domain queried steadily across many days, not in a single burst | Background telemetry from a long-running app. Most concerning category. |

### 6.2  What's a normal count?

On a well-protected network with all devices using Pi-hole DNS, most months will show single-digit or zero counts for known-blocked domains. Brief bursts are normal (an app updates, a wallet checks a quote). Sustained traffic is not.

Specific thresholds, rough guidance:

- **1-20 queries over 90 days** — Likely incidental. App startup checks, occasional pings.
- **20-100 queries over 90 days** — Active telemetry. An app is regularly checking in. Worth knowing which app.
- **100+ queries over 90 days** — Sustained surveillance attempt. Find the source. Consider whether the app is worth running.

---

## 7. What to Do With Each Finding

### 7.1  New domain found

A domain matched a surveillance pattern but isn't in your blocklist. This means the pattern was broad enough to catch a new subdomain or related infrastructure. Steps:

1. Read the domain, organization, query count, and client IPs from the report.
2. Verify the domain using the Contributor Guide steps: WHOIS, SSL certificate, SecurityTrails, URLScan.io.
3. Test that blocking the domain does not break legitimate wallet functionality.
4. If confirmed surveillance, submit a pull request to [github.com/cypherpilgrim/satoshishield](https://github.com/cypherpilgrim/satoshishield) adding the domain to `domains.csv`.
5. After the PR is merged, add the new domain to the `ALREADY_BLOCKED` set in `satoshishield_monitor.py` so it shows up in the right bucket next month.

### 7.2  Known domain still being queried

Pi-hole blocked it, but the attempt happened. The action is on the client side, not the blocklist:

1. Identify the client IP from the report.
2. Check if that device is using Pi-hole for DNS: `nslookup example.com <device-ip>` from another device.
3. If the device is bypassing Pi-hole, force DNS through it via a firewall rule on port 53.
4. If the device IS using Pi-hole but the queries persist, an app on that device is repeatedly trying. Use your operating system's process monitor or `netstat` to find the process.
5. Decide: uninstall the app, sandbox it, or accept the residual risk.

### 7.3  Clean report

Nothing to do. File the report and schedule the next quarterly research cycle. A clean report means SatoshiShield is working as designed.

---

## 8. Identifying Client IPs on Your Network

The Client IPs field is the most actionable part of every entry. Mapping IPs to specific devices on your network is essential for follow-up. Here are the most useful sources to consult:

| Source | What it tells you |
|---|---|
| **Firewall DHCP leases** | Most direct mapping. Look for the IP in your firewall's lease table to see the device hostname and MAC address. |
| **Pi-hole client list** | Pi-hole's admin UI shows recent clients with the hostnames it resolved from your local DNS. |
| **Local DNS / hosts file** | If you've configured custom hostnames for homelab services, search there first for known infrastructure IPs. |
| **Your homelab inventory** | Keep a personal table mapping IP ranges to roles (workstations, infrastructure, IoT, guest devices). |
| **`127.0.0.1` (loopback)** | Queries originating from Pi-hole itself — usually means manual testing from inside the Pi-hole container, or Pi-hole querying its own resolver. |

Common patterns to expect:

- **Workstation / laptop IPs** — most surveillance attempts come from browser tabs, IDE telemetry, or crypto app integrations.
- **Mobile device IPs** — wallet apps, exchange apps, and price trackers are common offenders.
- **Smart TV / IoT IPs** — usually not relevant to Bitcoin surveillance, but worth noting if they appear.
- **Bitcoin node / wallet host IPs** — should almost never appear. If they do, investigate immediately.

> Build your own mental map of which IPs belong to which devices. The monitor report becomes far more useful once you can read a client IP and immediately know which device on your network produced it.

---

## 9. Troubleshooting the Report Itself

If a monthly report doesn't arrive on the 1st, check these in order:

| Symptom | Likely cause | Fix |
|---|---|---|
| No email arrived | Cron didn't fire, or script failed silently | Check the monitor log file (default: `/var/log/satoshishield.log`) on the Proxmox host |
| Email says `SMTP send failed` | SMTP credentials rotated or revoked | Update the password in your `.env` file |
| Email says `pct pull failed` | Pi-hole container is stopped or the FTL database moved | Verify with `pct list` and check Pi-hole is running |
| Email says `Network is unreachable` | Firewall rule for outbound SMTP missing | Verify the Proxmox host has a pass rule for TCP/587 outbound to your SMTP relay |
| Report shows zero queries total | FTL database lookback window wiped, or Pi-hole reinstalled | Check Pi-hole's data retention settings; first report after reinstall will be short |

To trigger an out-of-cycle run manually, SSH to your Proxmox host as root and run:

```bash
python3 /opt/satoshishield/satoshishield_monitor.py
```

---

## 10. Walking Through a Sample Entry

Below is a representative entry from a monitor run, annotated to make the format concrete. Values have been generalized to placeholders:

```
Domain (root):   chainalysis.com
Organization:    Chainalysis
Category:        Blockchain Analytics
Description:     Primary blockchain surveillance firm; sells
                 intel to law enforcement and exchanges
Query count:     37
First seen:      <recent timestamp>
Last seen:       <recent timestamp>
Client IPs:      127.0.0.1, <firewall-ip>, <vm-ip>, <workstation-ip>
Subdomains:      api.chainalysis.com, markets.chainalysis.com,
                 this-is-a-test-1234567890.chainalysis.com
```

What this tells you, decoded:

- **37 queries over a short window** — high density. The first seen and last seen are within the same period, suggesting bursty activity.
- **Multiple client IPs** — different devices each produced some queries:
  - `127.0.0.1`: Pi-hole self-tests
  - Firewall IP: queries forwarded by the firewall when it acts as a DNS proxy
  - VM IP: a service on your homelab making queries (e.g. via tailnet DNS)
  - Workstation IP: a real client device — worth identifying
- **Subdomains** — two real (`api.chainalysis.com`, `markets.chainalysis.com`) and one synthetic (`this-is-a-test-...`). The synthetic one confirms at least some of this entry came from manual testing.
- **Pi-hole blocked all 37** — zero leaked. SatoshiShield did its job. The remaining work is identifying which app on the workstation produced the real subdomain queries.

> Your first monitor report will likely contain echoes of your initial testing. Subsequent monthly reports show what happens during normal use — compare them to identify which devices and apps are genuinely calling surveillance infrastructure on their own.

---

## 11. Recap — How to Read Any Report in 60 Seconds

1. Read the subject line. It tells you whether anything needs attention.
2. Skim the 'new domains' section if present. New entries are the only items that require updating the blocklist.
3. Look at query counts in the 'known blocked' section. Single digits — ignore. Dozens or hundreds — investigate the client IP.
4. Match Client IPs to devices using your firewall's DHCP leases and your own inventory.
5. Decide whether to act. Either uninstall the offending app, sandbox it, or accept that Pi-hole is already protecting you.

> A clean report is the goal, not an event. Most months should be unremarkable. The reports that contain real findings are the ones that matter — and the 60-second skim above is enough to handle them.

---

## Document Version

| Version | Date | Changes |
|---|---|---|
| 1.0 | May 2026 | Initial reading guide. Covers report structure, fields, count interpretation, client IP identification, troubleshooting, and a walkthrough of a sample entry. |

---

*[github.com/cypherpilgrim/satoshishield](https://github.com/cypherpilgrim/satoshishield)  ·  Companion to Monitor Deployment Guide v1.4*
