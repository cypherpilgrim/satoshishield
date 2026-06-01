# SatoshiShield Quarterly Research Checklist

*Run every 90 days · Estimated time: 2–4 hours*

Version 1.4 · May 2026

---

|                   |                            |                       |                            |
|-------------------|----------------------------|-----------------------|----------------------------|
| **Quarter**       | Q___ / 20___         | **Researcher**        | (GitHub handle)            |
| **Date Started**  | ___/___/______ | **Date Completed**    | ___/___/______ |
| **PRs Submitted** | ___                     | **New Domains Found** | ___                     |

**Phase 1 — Landscape Review**

Estimated time: 30 minutes. Goal: identify new surveillance firm products, domains, and community findings before beginning wallet research.

**1A — Surveillance Firm Monitoring**

Check each firm for new product announcements, API launches, or domain changes:

> □ Chainalysis — chainalysis.com — check Blog, Products, and press releases
>
> □ Elliptic — elliptic.co — check Resources and News
>
> □ TRM Labs — trmlabs.com — check Blog and press releases
>
> □ Arkham Intelligence — arkm.com — check for new features or domain changes
>
> □ Crystal Blockchain — crystalblockchain.com — check News
>
> □ Scorechain — scorechain.com — check Blog
>
> □ Merkle Science — merkle.science — check Blog
>
> □ Other firms — Search: 'blockchain analytics new product [current quarter]'

> **New products or announcements found:**

**1B — SSL Certificate Transparency**

Check for new SSL certificates issued to known surveillance firm domains:

> □ crt.sh — chainalysis.com — https://crt.sh/?q=chainalysis.com — look for new subdomains
>
> □ crt.sh — elliptic.co — https://crt.sh/?q=elliptic.co
>
> □ crt.sh — trmlabs.com — https://crt.sh/?q=trmlabs.com
>
> □ crt.sh — arkm.com — https://crt.sh/?q=arkm.com
>
> □ crt.sh — scorechain.com — https://crt.sh/?q=scorechain.com

> **New certificates / subdomains found:**

**1C — Job Posting Intelligence**

New API products appear in job postings before they appear publicly. Search LinkedIn and Indeed:

> □ Search: 'Chainalysis API engineer [current quarter]'
>
> □ Search: 'Elliptic blockchain data scientist [current quarter]'
>
> □ Search: 'TRM Labs backend engineer [current quarter]'
>
> □ Look for job descriptions mentioning new product names, API endpoints, or service categories

> **Job postings referencing new products or APIs:**

**1D — Community Intelligence**

Review findings submitted by other contributors:

> □ SatoshiShield GitHub Issues — Review open issues tagged 'domain-candidate'
>
> □ SatoshiShield GitHub Discussions — Check for community research threads
>
> □ Bitcoin privacy forums — Search for 'surveillance domain' or 'wallet tracking' discussions
>
> □ Nostr / Twitter/X — Search: #SatoshiShield #BitcoinPrivacy domain findings

> **Community-submitted candidate domains to investigate:**

**Phase 2 — Wallet Audit**

Estimated time: 60–90 minutes. Goal: capture DNS queries from active Bitcoin wallets and identify unblocked surveillance domains.

Run Wireshark on your test device. Open each wallet, let it run for 2–3 minutes, perform normal operations (check balance, view transactions), then close it. Export DNS queries to CSV after each wallet.

**2A — Desktop Wallets**

> □ Sparrow Wallet — sparrowwallet.com — open, sync, check balance, view transactions
>
> □ DNS queries captured
>
> □ Unrecognized domains noted below
>
> □ Electrum — electrum.org — open, check balance, view transactions
>
> □ DNS queries captured
>
> □ Unrecognized domains noted below
>
> □ Bitcoin Core (if installed) — Check what external connections it makes beyond peer connections
>
> □ DNS queries captured
>
> □ Unrecognized domains noted below

> **Unrecognized domains from desktop wallet audit:**

**2B — Mobile Wallets**

Use a test device or emulator. Capture traffic via a proxy (mitmproxy or Charles Proxy) or your Pi-hole logs filtered by device IP.

> □ BlueWallet — bluewallet.io — open, check balance, view transactions
>
> □ DNS queries captured
>
> □ Unrecognized domains noted below
>
> □ Muun Wallet — muun.com — open, check balance
>
> □ DNS queries captured
>
> □ Unrecognized domains noted below
>
> □ Additional wallet — Note which wallet: _______________________
>
> □ DNS queries captured
>
> □ Unrecognized domains noted below

> **Unrecognized domains from mobile wallet audit:**

**2C — Browser Extensions and Web Wallets**

> □ Check any Bitcoin browser extensions installed on your test browser
>
> □ Open browser with Wireshark running
>
> □ Visit a Bitcoin transaction or address page
>
> □ Note any unfamiliar domains queried
>
> □ Check any price tracking or portfolio extensions
>
> □ Note domains contacted when extension loads

> **Unrecognized domains from browser extension / web wallet audit:**

**2D — Pi-hole Log Review**

Review your Pi-hole query logs for the past 90 days. Filter by known Bitcoin wallet device IPs.

> □ Export Pi-hole query log for past 90 days
>
> □ Filter by Bitcoin wallet device IP addresses
>
> □ Identify domains not already in SatoshiShield blocklist
>
> □ Cross-reference unfamiliar domains against SatoshiShield domains.csv

> **Domains appearing in Pi-hole logs not already blocked:**

**Phase 3 — Domain Verification**

Estimated time: 15–20 minutes per domain. Goal: verify each candidate domain meets inclusion criteria before submitting.

Use this section for each candidate domain identified in Phases 1 and 2. Copy this section as needed for multiple domains.

**Domain Verification Record — Domain 1**

> **Domain being verified:**

**Step 1 — WHOIS Lookup**

Tool: whois.domaintools.com or lookup.icann.org

> □ WHOIS lookup completed

> **Registrant organization:**
> **Registration date:**
> **Registrar / privacy service:**

**Step 2 — SSL Certificate**

Tool: crt.sh or browser padlock > Certificate Details

> □ SSL certificate inspected

> **Organization in certificate:**
> **Subject Alternative Names (related domains):**

**Step 3 — SecurityTrails / PassiveDNS**

Tool: securitytrails.com or passivedns.mnemonic.no

> □ Historical DNS checked

> **IPs this domain has resolved to:**
> **Other domains on same IP infrastructure:**

**Step 4 — Behavioral Evidence (URLScan.io or vendor documentation)**

Tool: urlscan.io

> □ Behavioral evidence gathered — URLScan.io scan (suspected / dual-use) or vendor documentation (self-documented / Tier 1)

> **URLScan.io scan URL (or vendor documentation URL):**
> **External connections made by this domain:**
> **JavaScript references to analytics / tracking / blockchain:**

**Step 5 — Privacy Harm Assessment**

> □ Inclusion criteria identified (check all that apply):
>
> □ Blockchain Analytics firm domain
>
> □ Deanonymization platform
>
> □ Address Screening API
>
> □ Wallet Telemetry
>
> □ KYC/AML Intelligence
>
> □ IP-Logging Infrastructure

> **Specific privacy harm (one sentence):**
> **Source / evidence URL:**

**Step 6 — Functional Impact Test**

> □ Added domain to Pi-hole temporarily
>
> □ Opened Bitcoin wallet with domain blocked
>
> □ Tested: balance check
>
> □ Tested: transaction history
>
> □ Tested: send / receive flow (if safe to test)

|                                                                      |                                                                      |
|----------------------------------------------------------------------|----------------------------------------------------------------------|
| **□ Wallet functions normally with domain blocked — SAFE TO SUBMIT** | **□ Wallet breaks with domain blocked — DO NOT SUBMIT (open issue)** |

**domains.csv Entry**

Complete this entry for the pull request:

> **domain:**
> **organization:**
> **category:**
> **harm:**
> **source:**
> **date_verified:**
> **notes:**

Add additional Domain Verification Records as needed for each candidate domain found in Phases 1 and 2.

**Phase 4 — Existing Entry Audit**

Estimated time: 30 minutes. Goal: verify that existing blocklist entries are still current and accurate.

Select 10–15 entries from domains.csv at random, or prioritize entries with the oldest date_verified field. For each entry, run a quick verification pass.

**4A — Entry Verification**

> □ Downloaded current domains.csv from repository
>
> □ Selected 10–15 entries to audit (prioritize oldest date_verified)

| **Domain** | **Organization** | **date_verified** | **Still Valid?** | **Action Needed** |
|------------|------------------|-------------------|------------------|-------------------|
|            |                  |                   | Yes / No         |                   |
|            |                  |                   | Yes / No         |                   |
|            |                  |                   | Yes / No         |                   |
|            |                  |                   | Yes / No         |                   |
|            |                  |                   | Yes / No         |                   |
|            |                  |                   | Yes / No         |                   |
|            |                  |                   | Yes / No         |                   |
|            |                  |                   | Yes / No         |                   |
|            |                  |                   | Yes / No         |                   |
|            |                  |                   | Yes / No         |                   |
|            |                  |                   | Yes / No         |                   |
|            |                  |                   | Yes / No         |                   |
|            |                  |                   | Yes / No         |                   |
|            |                  |                   | Yes / No         |                   |
|            |                  |                   | Yes / No         |                   |

**4B — Entry Audit Checks**

For any entry marked No above, investigate:

> □ Does the domain still resolve? — nslookup [domain] or dig [domain]
>
> □ Does it still belong to the same organization? — WHOIS + SSL certificate check
>
> □ Has the organization changed its business model? — Check current website
>
> □ Is there a new domain that should be added instead? — Check crt.sh for related new domains

> **Entries requiring updates or removal:**

**Phase 5 — Submission**

Estimated time: 30 minutes. Goal: submit all verified findings to the SatoshiShield repository.

**5A — New Domain Submissions**

> □ Created a new Git branch for this quarter's submissions
>
> □ Added all new verified domains to domains.csv
>
> □ Verified CSV formatting is correct (no extra commas, quotes where needed)
>
> □ Opened pull request for new domain additions
>
> □ Pull request title: 'Q[X] [Year]: Add [N] new surveillance domains'
>
> □ Pull request description includes evidence summary for each domain
>
> □ PR checklist in template completed

> **Pull request URL:**

**5B — Entry Update Submissions**

> □ Created a separate Git branch for entry updates
>
> □ Updated date_verified for all audited entries in domains.csv
>
> □ Marked any stale entries for removal with justification
>
> □ Opened pull request for entry updates
>
> □ PR title: 'Q[X] [Year]: Quarterly entry audit updates'

> **Pull request URL:**

**5C — Checklist Completion**

> □ This completed checklist saved to local records
>
> □ Checklist findings summarized in GitHub Discussion for the quarter
>
> □ Next quarter's research date scheduled: — Target: 90 days from today

> **Next quarterly research target date:**

**Quarter Summary**

| **Metric**                     | **Count** | **Notes**                  |
|--------------------------------|-----------|----------------------------|
| Wallets audited                |           |                            |
| Candidate domains identified   |           |                            |
| Domains verified and submitted |           |                            |
| Domains verified and rejected  |           | Reason documented in notes |
| Existing entries audited       |           |                            |
| Existing entries updated       |           |                            |
| Existing entries removed       |           |                            |
| Pull requests opened           |           |                            |
| Total time spent (hours)       |           |                            |

> **Notable findings this quarter:**
> **Recommended focus areas for next quarter:**

**Document Version**

| **Version** | **Date** | **Changes**                                                                                                                                                                                                                                   |
|-------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.0         | May 2026 | Initial quarterly research checklist. Five phases: landscape review, wallet audit, domain verification, existing entry audit, and submission. Includes session metadata, domain verification records, entry audit table, and quarter summary. |
| 1.4         | May 2026 | Updated to v1.4 metadata. GitHub handle migrated from sawdustpilgrim to cypherpilgrim. Cover page version stamp added. Header and footer version stamps updated.                                                                              |
