# SatoshiShield Contributor Guide

*How to Research, Verify, and Submit Domains*

Version 1.4 · May 2026
[github.com/cypherpilgrim/satoshishield](https://github.com/cypherpilgrim/satoshishield)

---

> This guide teaches you everything you need to research, verify, and submit domains to the SatoshiShield Bitcoin Privacy DNS Blocklist. No prior security research experience is required. Every skill in this guide can be learned in an afternoon and applied in minutes per domain.

## 1. Introduction

SatoshiShield is a community-maintained project. Its quality depends entirely on the people who contribute to it. The maintainers cannot monitor every Bitcoin wallet, every analytics firm, and every new surveillance API that appears. The community can.

This guide teaches you one core skill: how to determine whether a domain belongs on the SatoshiShield blocklist. That skill has three components:

- Finding domains — discovering candidates through wallet traffic analysis, source code inspection, and community intelligence

- Verifying domains — confirming who owns a domain and what privacy harm it causes

- Submitting domains — documenting your findings and opening a pull request on GitHub

You do not need to be a security researcher. You do not need to be a developer. You need to be curious, methodical, and willing to follow a process. This guide provides that process.

## 2. The Inclusion Standard

Before you research any domain, understand the standard it must meet to be included in SatoshiShield. Every domain in the blocklist must satisfy at least one of the following criteria:

| **Criteria**              | **Description**                                                                                          | **Example**                                                                  |
|---------------------------|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| Blockchain Analytics      | Operated by a company whose primary business is correlating Bitcoin addresses with real-world identities | chainalysis.com — Chainalysis builds IP-to-address correlation databases     |
| Deanonymization Platform  | A platform that publicly markets the ability to attach real identities to Bitcoin addresses              | intel.arkm.com — Arkham Intelligence markets identity linking as a feature   |
| Address Screening API     | An API endpoint used to score Bitcoin addresses for risk or compliance purposes                          | api.elliptic.co — Elliptic's screening API reveals which addresses you query |
| Wallet Telemetry          | A domain receiving usage analytics, crash reports, or behavioral data from Bitcoin wallet software       | analytics.walletapp.com — logs which features you use and how often          |
| KYC/AML Intelligence      | A compliance service used to flag Bitcoin transactions associated with privacy tools                     | scorechain.com — flags CoinJoin transactions as high risk                    |
| IP-Logging Infrastructure | Any endpoint that logs the querying IP address against Bitcoin address or transaction data               | markets.chainalysis.com — price API that logs IP against query timing        |

> A domain must NOT be included if blocking it would impair legitimate Bitcoin network functionality, wallet software operation, or access to open-source privacy-respecting services. When in doubt, do not submit — ask in a GitHub issue first.

## 3. Finding Candidate Domains

There are four primary methods for discovering domains that may belong on the SatoshiShield blocklist. Use whichever methods match your skills and tools.

### 3.1 Method A — Pi-hole Query Log Review

If you run Pi-hole on your home network, your query logs are a gold mine. Every DNS query made by every device on your network is recorded. Bitcoin wallet apps, mobile wallets, browser extensions, and price trackers all leave traces here.

**Step 1 — Access Pi-hole query logs**

Log into your Pi-hole admin UI and navigate to Query Log. Filter by a device you know runs Bitcoin wallet software.

**Step 2 — Identify unfamiliar domains**

Look for domains you do not recognize, particularly those with patterns like:

- api.*, data.*, analytics.*, tracking.*, metrics.*, telemetry.*

- Domains that appear shortly after you open your Bitcoin wallet

- Domains with naming patterns similar to known analytics firms

- Domains you have never visited directly in a browser

**Step 3 — Note the domain for verification**

Write down any suspicious domains. Do not submit them yet — verification comes in Section 4.

> Tip: Pi-hole's query log can be filtered by time. Open your Bitcoin wallet, wait 60 seconds, then check what domains were queried in that window. Anything you do not recognize is worth investigating.

### 3.2 Method B — Wallet Traffic Capture with Wireshark

Wireshark captures all network traffic from a device or network interface. This reveals every connection your Bitcoin wallet makes — not just DNS queries but full connection details.

**Step 1 — Install Wireshark**

Download from wireshark.org. Available for macOS, Windows, and Linux.

**Step 2 — Start a capture**

Open Wireshark and select your active network interface. Click the blue shark fin to start capturing.

**Step 3 — Open your Bitcoin wallet**

With Wireshark capturing, open your Bitcoin wallet app. Let it run for 2-3 minutes. Close it.

**Step 4 — Filter DNS queries**

In Wireshark's filter bar, type:

> dns

This shows only DNS queries. Look for domains that appear after the wallet opened that you do not recognize.

**Step 5 — Filter by wallet process (advanced)**

To isolate only traffic from the wallet process, use display filters:

```
dns.qry.name contains "analytics"
dns.qry.name contains "chainalysis"
dns.qry.name contains "tracking"
```

**Step 6 — Export results**

Go to File > Export Packet Dissections > As CSV. This gives you a searchable list of all DNS queries for later analysis.

### 3.3 Method C — Wallet Source Code Inspection

Many Bitcoin wallets are open source. Reading the source code reveals API endpoints that may not be visible in network traffic (especially if they use certificate pinning or hardcoded IPs).

**Step 1 — Find the repository**

Most popular wallets have public GitHub repositories. Search for the wallet name on github.com.

**Step 2 — Search for API endpoints**

Use GitHub's code search within the repository. Search for:

```
https://api
analytics
telemetry
tracking
mixpanel
amplitude
segment
```

**Step 3 — Review network configuration files**

Look for files named: config.js, constants.js, api.js, endpoints.js, network.js, services.js. These often contain hardcoded API URLs.

**Step 4 — Check package dependencies**

Look at package.json (JavaScript wallets) or requirements.txt / Podfile (mobile wallets). Third-party analytics packages like Mixpanel, Amplitude, or Segment indicate telemetry.

> Tip: GitHub's search syntax supports repository-scoped searches. Use 'repo:username/wallet-name analytics' to search only within that repository.

### 3.4 Method D — Community Intelligence

The Bitcoin privacy community actively researches and discusses surveillance infrastructure. Stay connected to find new domains:

- Monitor the SatoshiShield GitHub Issues tab — other contributors post findings there

- Follow Bitcoin privacy researchers on Nostr and Twitter/X

- Read privacy-focused Bitcoin forums and subreddits

- Watch for announcements from Chainalysis, Elliptic, and TRM Labs — new product launches mean new domains

- Monitor job postings from analytics firms — new API products appear in job descriptions before launch

## 4. Verifying a Domain

Finding a suspicious domain is only the first step. Before submitting, you must verify three things:

- **Who owns this domain?**

- **What specific privacy harm does it cause?**

- **Does blocking it harm legitimate Bitcoin functionality?**

This section walks through each verification step using free tools available to anyone.

### 4.1 Step 1 — WHOIS Lookup

WHOIS reveals the registered owner of a domain, when it was registered, and who hosts it.

**How to run a WHOIS lookup**

Option A — Browser: Go to whois.domaintools.com or lookup.icann.org and enter the domain.

Option B — Command line:

> whois example-suspicious-domain.com

**What to look for**

| **Field**               | **What It Tells You**                  | **Red Flag**                                                                       |
|-------------------------|----------------------------------------|------------------------------------------------------------------------------------|
| Registrant Organization | The company that registered the domain | Matches a known surveillance firm name or subsidiary                               |
| Registrant Email        | Contact email for the domain owner     | Corporate email domain matching known analytics firm                               |
| Creation Date           | When the domain was registered         | Recently registered domains may indicate infrastructure rotation                   |
| Name Servers            | DNS provider                           | Same name servers as known surveillance firm domains suggest shared infrastructure |
| Registrar               | Domain registrar                       | Less informative but can confirm corporate registration patterns                   |

> Many surveillance firms use privacy protection services that hide registrant details. If WHOIS returns a privacy service, proceed to SSL certificate inspection and SecurityTrails lookup.

### 4.2 Step 2 — SSL Certificate Inspection

SSL certificates reveal the organization name and sometimes list related domains (Subject Alternative Names). This is often more revealing than WHOIS.

**How to inspect an SSL certificate**

Option A — Browser: Navigate to https://[domain] and click the padlock icon > Certificate > Details.

Option B — crt.sh (certificate transparency logs):

> Go to: https://crt.sh/?q=suspicious-domain.com

This shows every SSL certificate ever issued for the domain and all related subdomains.

Option C — Command line:

|                                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------|
| echo | openssl s_client -connect suspicious-domain.com:443 2>/dev/null | openssl x509 -text -noout | grep -A2 'Subject:\\DNS:' |

**What to look for**

- Organization (O) field in the certificate — often shows the real company name

- Subject Alternative Names — lists all domains on the same certificate, revealing related infrastructure

- Issuer — certificates issued by the same CA as known surveillance firm domains suggest shared infrastructure

### 4.3 Step 3 — SecurityTrails or PassiveDNS

These services show the historical DNS records for a domain — what IPs it has pointed to, what other domains have pointed to the same IPs, and how the domain's infrastructure has changed over time.

**SecurityTrails**

Go to: securitytrails.com/domain/[suspicious-domain.com]/dns

Free tier available. Shows current and historical DNS records, related domains, and IP history.

**PassiveDNS**

Go to: passivedns.mnemonic.no or use VirusTotal's passive DNS feature.

Search the suspicious domain to see what IPs it has resolved to over time. Search known surveillance firm IPs to see what other domains have pointed to the same infrastructure.

**What to look for**

- The suspicious domain and a known surveillance firm domain resolving to the same IP — strong evidence of shared infrastructure

- The suspicious domain appearing in subdomain lists of known analytics firms

- Recent changes in DNS records suggesting the domain is being prepared for a new use

### 4.4 Step 4 — Behavioral Evidence

Step 4 requires behavioral evidence confirming the specific surveillance function named in the harm field. The appropriate method depends on the domain type. For domains whose surveillance behavior is not self-evident — suspected, dual-use, or camouflaged domains, typically Tier 2 — observe the behavior directly with URLScan.io. For domains operated by firms that openly document their surveillance functions, typically Tier 1, and especially for authentication-gated API endpoints that an unauthenticated sandbox visit cannot reach, the vendor's own published documentation is the appropriate evidence (see "Vendor documentation as behavioral evidence" below). URLScan.io visits a URL in a sandboxed browser and records every connection made — DNS queries, HTTP requests, JavaScript calls, and cookies. It is the most useful tool for revealing what a domain does when that behavior must be observed rather than read from the vendor.

**How to use URLScan.io**

## 1. Go to urlscan.io

## 2. Enter the suspicious domain URL and click Scan

## 3. Wait 30-60 seconds for the scan to complete

## 4. Review the results

**What to look for in URLScan results**

| **Tab**  | **What It Shows**                            | **Look For**                                                    |
|----------|----------------------------------------------|-----------------------------------------------------------------|
| Summary  | High-level overview of what the page does    | References to analytics, tracking, or blockchain data           |
| HTTP     | All HTTP requests made by the page           | API calls to known surveillance domains or unfamiliar endpoints |
| Contacts | Domains and IPs contacted during page load   | Known surveillance firm domains appearing as dependencies       |
| DOM      | JavaScript variables and objects in the page | Variable names like 'analytics', 'tracker', 'chainalysis'       |
| Links    | All links found on the page                  | Links to known surveillance firm documentation or dashboards    |

**Vendor documentation as behavioral evidence**

When a domain is operated by a firm that openly documents its surveillance functions, the vendor’s own published API or product documentation is acceptable as Step 4 behavioral evidence in place of a URLScan.io scan. This is the appropriate method for most Tier 1 firms, and the only workable method for authentication-gated endpoints, which an unauthenticated sandbox visit cannot reach. The documentation must be published by the vendor, must explicitly confirm the specific behavior cited in the harm field — for example, logging the querying IP against the queried address, risk scoring, or attribution — and must be linked as the source. For domains that do not openly document surveillance behavior (suspected, dual-use, or camouflaged domains), vendor documentation does not suffice and a URLScan.io scan or traffic capture is required.

### 4.5 Step 5 — Confirm the Privacy Harm

At this point you should have enough information to articulate the specific privacy harm. Ask yourself:

- Does this domain receive Bitcoin address queries that it correlates with IP addresses?

- Does this domain receive telemetry from wallet software that reveals Bitcoin usage patterns?

- Does this domain belong to an organization that sells blockchain intelligence to third parties?

- Does blocking this domain prevent a connection that reveals information about the user's Bitcoin activity?

If you can answer yes to any of these questions with supporting evidence, the domain meets the inclusion criteria.

### 4.6 Step 6 — Confirm Blocking Does Not Break Bitcoin Functionality

This is the most important safety check. Before submitting, verify that blocking the domain does not impair legitimate Bitcoin wallet operation.

**How to test**

## 5. Add the domain to your Pi-hole blocklist temporarily

## 6. Open your Bitcoin wallet and test all normal functions: checking balance, sending a test transaction, receiving, checking transaction history

## 7. If everything works normally, blocking the domain is safe

## 8. If wallet functions break, investigate further — the domain may serve a dual purpose

> If the wallet works normally with the domain blocked, the domain is safe to submit. A surveillance API failing silently is by design — it should not break wallet functionality.
> If blocking the domain breaks wallet functionality, do NOT submit it. Open a GitHub issue instead to discuss the dual-use concern with maintainers.

## 5. Documenting Your Finding

Every domain submission requires documentation. This is not bureaucracy — it is what allows future contributors to verify your work, update entries when things change, and remove entries if they become incorrect.

### 5.1 The domains.csv Format

All domain documentation is stored in domains.csv in the repository root. Each row represents one domain entry. The category field takes one of the canonical values listed below; the inclusion criteria named in Section 2 are descriptive, and they map to these category values (for example, the “Deanonymization Platform” criterion corresponds to the Deanonymization category, and “IP-Logging Infrastructure” to IP Logging).

The CSV columns are:

| **Column**    | **Description**                                                                                                                            | **Example**                                                        |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| domain        | The exact domain to block (use wildcard prefix for all subdomains)                                                                         | *.chainalysis.com                                                 |
| organization  | The company or entity operating the domain                                                                                                 | Chainalysis Inc.                                                   |
| category      | One of: Blockchain Analytics, Deanonymization, Wallet Telemetry, KYC/AML Compliance, Address Screening, IP Logging, Surveillance Analytics | Blockchain Analytics                                               |
| tier          | 1 for confirmed surveillance harm; 2 for entries needing further community verification                                                    | 1                                                                  |
| harm          | One sentence describing the specific privacy harm                                                                                          | Logs querying IP addresses against Bitcoin address lookup requests |
| source        | URL or reference supporting the inclusion                                                                                                  | https://www.chainalysis.com/reactor/                               |
| date_verified | Date you last verified this entry is current                                                                                               | 2026-05-04                                                         |
| notes         | Any additional context, caveats, or related domains                                                                                        | Also operates transpose.io (acquired 2022)                         |

**Example entry**

```
domain,organization,category,tier,harm,source,date_verified,notes
*.chainalysis.com,Chainalysis Inc.,Blockchain Analytics,1,"Logs querying IP addresses against
Bitcoin address lookup requests. Sells intelligence to law enforcement and
exchanges.",https://www.chainalysis.com/reactor/,2026-05-04,"Also operates
transpose.io (acquired 2022)"
```

### 5.2 Wildcard vs Exact Domain

Use wildcards when you want to block all subdomains of an organization's domain:

| **Format**          | **What It Blocks**                                              | **When to Use**                                                                                            |
|---------------------|-----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| *.chainalysis.com  | All subdomains: api.chainalysis.com, data.chainalysis.com, etc. | When the entire organizational domain should be blocked                                                    |
| api.chainalysis.com | Only that specific subdomain                                    | When only one specific endpoint is the surveillance concern and other subdomains serve legitimate purposes |
| chainalysis.com     | The root domain only (not subdomains)                           | Rarely used alone — combine with wildcard entry                                                            |

> When in doubt, use the wildcard. If an organization's primary business is Bitcoin surveillance, all of their infrastructure should be blocked. They can change subdomain names but they cannot change their root domain without losing their existing customers.

## 6. Submitting to GitHub

All submissions go through GitHub pull requests. This section walks through the process step by step.

### 6.1 Prerequisites

- A GitHub account (free). Use a pseudonymous account if you prefer — this is encouraged.

- Basic familiarity with Git. If you have never used Git, see the Git Primer in Appendix A.

### 6.2 Fork the Repository

## 9. Go to [github.com/cypherpilgrim/satoshishield](https://github.com/cypherpilgrim/satoshishield)

## 10. Click the Fork button in the top right

## 11. Select your account as the destination

## 12. You now have your own copy of the repository

### 6.3 Clone Your Fork

```
git clone https://github.com/YOUR-USERNAME/satoshishield.git
cd satoshishield
```

### 6.4 Create a Branch

Always create a new branch for your submission. Use a descriptive name:

> git checkout -b add-domain-suspicious-analytics-com

### 6.5 Add Your Domain

Edit domains.csv and add your entry. Follow the format exactly — CSV is whitespace-sensitive.

```
# Open in any text editor
nano domains.csv
```

Add your row at the bottom of the file. Save.

The three blocklist files (blocklist.txt, hosts.txt, satoshishield.abp) are generated automatically from domains.csv when a new release is cut. You do not need to edit these manually.

### 6.6 Commit and Push

```
git add domains.csv
git commit -m "Add [domain]: [one-line description of harm]"
git push origin add-domain-suspicious-analytics-com
```

### 6.7 Open a Pull Request

## 13. Go to your fork on GitHub

## 14. Click Compare & pull request

## 15. Fill in the pull request template (see Section 6.8)

## 16. Click Create pull request

### 6.8 Pull Request Template

Every pull request should include the following information:

```
## Domain Submission
**Domain:** *.suspicious-analytics.com
**Organization:** Suspicious Analytics Inc.
**Category:** Blockchain Analytics
## Evidence of Privacy Harm
[Describe what you found and how you found it. Include links to
sources, screenshots of WHOIS/SSL certificate results, URLScan
analysis, or wallet source code references.]
## Verification Steps Completed
- [ ] WHOIS lookup performed
- [ ] SSL certificate inspected
- [ ] SecurityTrails / PassiveDNS checked
- [ ] Behavioral evidence gathered — URLScan.io scan (suspected / dual-use domains) or vendor documentation (self-documented / Tier 1 firms)
- [ ] Tested that blocking does not break wallet functionality
## Functional Impact Test
[Describe how you tested that blocking the domain does not impair
Bitcoin wallet functionality. Which wallet? What functions tested?]
## domains.csv Entry
[Paste your CSV row here for review]
```

## 7. What Happens After You Submit

After you open a pull request, the maintainers will review your submission. Here is what to expect:

| **Stage**             | **Timeframe**        | **What Happens**                                                                                      |
|-----------------------|----------------------|-------------------------------------------------------------------------------------------------------|
| Initial review        | Within 7 days        | A maintainer reviews your pull request, checks the documentation, and may ask clarifying questions    |
| Research verification | Within 14 days       | Maintainers independently verify the organization, harm, and functional impact                        |
| Discussion            | Ongoing              | Community members may comment with additional findings or concerns. Engage constructively.            |
| Decision              | Within 21 days       | Pull request is merged, rejected with explanation, or flagged for further research                    |
| Release               | Next monthly release | Merged domains appear in the next scheduled release and are automatically pulled by all installations |

If your submission is rejected, the maintainers will explain why. Common reasons include insufficient evidence of harm, dual-use concerns, or functional impact on wallet operation. A rejection is not permanent — you can gather more evidence and resubmit.

## 8. Quarterly Research Protocol

For contributors who want to do systematic research rather than ad hoc submissions, this quarterly protocol provides a structured approach to discovering new surveillance domains.

Time required: 2-4 hours per quarter. No special tools beyond those described in Section 3 and 4.

### 8.1 Quarter Start — Landscape Review (30 minutes)

## 17. Check Chainalysis, Elliptic, TRM Labs, and Arkham Intelligence websites for new product announcements

## 18. Search LinkedIn for new job postings at these firms mentioning specific API products or services

## 19. Check crt.sh for new SSL certificates issued to known surveillance firm domains

## 20. Review the SatoshiShield GitHub Issues tab for community-submitted candidate domains

### 8.2 Wallet Audit (60-90 minutes)

Select 3-5 popular Bitcoin wallets. For each:

## 21. Run a Wireshark capture while opening the wallet and performing normal operations

## 22. Export DNS queries to CSV

## 23. Identify any domains not already in the SatoshiShield blocklist

## 24. Run verification steps (Section 4) on any unrecognized domains

Recommended wallets to audit each quarter:

- Sparrow Wallet (desktop)

- Electrum (desktop)

- BlueWallet (mobile)

- Muun Wallet (mobile)

- Any new wallet that has gained community attention since last quarter

### 8.3 Existing Entry Audit (30 minutes)

## 25. Review 10-15 existing entries in domains.csv

## 26. Verify each domain still resolves and still belongs to the same organization

## 27. Check if the organization has changed its domain infrastructure

## 28. Submit a pull request updating the date_verified field and noting any changes

### 8.4 Submit Findings

Submit all new domains found via pull request (Section 6). Submit any corrections to existing entries via a separate pull request. Document everything you checked, even if you found nothing new — this confirms entries are still current.

## 9. Tools Reference

| **Tool**              | **URL**                | **Cost**       | **Purpose**                                                                       |
|-----------------------|------------------------|----------------|-----------------------------------------------------------------------------------|
| Pi-hole               | pi-hole.net            | Free           | DNS query logging — reveals all domains your wallet contacts                      |
| Wireshark             | wireshark.org          | Free           | Full network traffic capture — reveals all connections including hardcoded IPs    |
| WHOIS (ICANN)         | lookup.icann.org       | Free           | Domain registration lookup — reveals domain owner                                 |
| crt.sh                | crt.sh                 | Free           | SSL certificate transparency logs — reveals organization name and related domains |
| URLScan.io            | urlscan.io             | Free (limited) | Sandboxed URL analysis — shows all connections a domain makes                     |
| SecurityTrails        | securitytrails.com     | Free tier      | Historical DNS — reveals IP history and related domains                           |
| VirusTotal            | virustotal.com         | Free           | Multi-engine analysis including passive DNS and domain relationships              |
| Shodan                | shodan.io              | Free tier      | IP address lookup — reveals services running on surveillance firm servers         |
| PassiveDNS (Mnemonic) | passivedns.mnemonic.no | Free           | Historical DNS resolution data                                                    |
| DomainTools WHOIS     | whois.domaintools.com  | Free           | Enhanced WHOIS with related domain suggestions                                    |
| GitHub Code Search    | github.com/search      | Free           | Search wallet source code for API endpoints and tracking libraries                |

## 10. Code of Conduct

SatoshiShield is a technical project with a clear mission: protecting Bitcoin users from network-layer surveillance. The following principles govern contributor interactions:

- Research and document objectively. The goal is accurate information, not activism.

- Provide evidence. Assertions without evidence will not be accepted regardless of how certain you are.

- Engage respectfully. Disagreements about inclusion decisions should be resolved through evidence, not argument.

- Protect your own privacy. Use a pseudonymous GitHub account if you prefer. The project practices what it preaches.

- No doxxing. Never include personal information about individuals associated with surveillance firms — domain research targets organizations, not people.

- No speculation. Do not submit domains based on speculation about future surveillance use. Evidence of current harm is required.

> The strongest argument in any inclusion discussion is evidence. If you have evidence, present it clearly. If you lack evidence, gather it. The process exists to ensure the blocklist remains accurate and trustworthy.

**Appendix A — Git Primer for Non-Developers**

Git is a version control system that tracks changes to files. GitHub is a website that hosts Git repositories and facilitates collaboration. You need both to contribute to SatoshiShield.

**A.1 Install Git**

macOS: Git comes pre-installed. Open Terminal and type git --version to confirm.

Windows: Download from git-scm.com and install.

Linux: sudo apt install git

**A.2 Essential Git Commands**

| **Command**                     | **What It Does**                                     |
|---------------------------------|------------------------------------------------------|
| git clone [url]               | Downloads a copy of a repository to your computer    |
| git checkout -b [branch-name] | Creates a new branch and switches to it              |
| git add [filename]            | Stages a file for commit (marks it as ready to save) |
| git commit -m "[message]"     | Saves staged changes with a description              |
| git push origin [branch-name] | Uploads your branch to GitHub                        |
| git pull                        | Downloads the latest changes from GitHub             |
| git status                      | Shows which files have been changed                  |

**A.3 The Contribution Workflow in Plain English**

## 29. Fork the repository — make your own copy on GitHub

## 30. Clone your fork — download your copy to your computer

## 31. Create a branch — create a named workspace for your changes

## 32. Edit domains.csv — add your domain entry

## 33. Commit — save your changes with a description

## 34. Push — upload your changes to GitHub

## 35. Pull request — ask the maintainers to review and merge your changes

If you get stuck, open a GitHub Issue on the SatoshiShield repository with the label 'help wanted' and describe what you are trying to do. The maintainers will help.

**Appendix B — Domain Verification Checklist**

Use this checklist for every domain you verify. Check off each step before submitting.

| **Step** | **Action**                                                                     | **Completed** |
|----------|--------------------------------------------------------------------------------|---------------|
| 1        | WHOIS lookup — identified domain owner                                         | [ ]         |
| 2        | SSL certificate inspected — confirmed organization                             | [ ]         |
| 3        | SecurityTrails / PassiveDNS — checked IP history and related domains           | [ ]         |
| 4        | Behavioral evidence — URLScan.io scan or vendor documentation, per domain type | [ ]         |
| 5        | Privacy harm articulated — one sentence describing the specific harm           | [ ]         |
| 6        | Inclusion criteria met — confirmed domain meets at least one criterion         | [ ]         |
| 7        | Functional test — confirmed blocking does not break wallet functionality       | [ ]         |
| 8        | domains.csv entry prepared — all columns completed                             | [ ]         |
| 9        | Pull request template completed — all sections filled                          | [ ]         |

**Document Version**

| **Version** | **Date** | **Changes**                                                                                                                                                                  |
|-------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.0         | May 2026 | Initial contributor guide. Covers finding, verifying, and submitting domains. Includes quarterly research protocol, tools reference, Git primer, and verification checklist. |
| 1.4         | May 2026 | Updated to v1.4 metadata. GitHub handle migrated from sawdustpilgrim to cypherpilgrim across all URLs. Cover, header, and footer version stamps updated.                     |
