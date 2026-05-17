# Contributing to SatoshiShield

Thank you for helping keep this blocklist accurate and current. This document covers the quick-reference contribution process. For the full research methodology, tools reference, and quarterly research protocol, see the [Contributor Guide](docs/SatoshiShield_Contributor_Guide_v1_0.docx).

---

## Before You Submit

A domain must meet at least one of these criteria to be included:

- Operated by a company whose primary business is correlating Bitcoin addresses with real-world identities
- Used as an API endpoint by blockchain analytics or surveillance platforms
- Known to log IP addresses against address queries
- Used for wallet telemetry that reveals Bitcoin usage patterns
- Operated by a deanonymization platform that markets identity-linking capabilities
- Used by KYC/AML services to score Bitcoin addresses

**A domain must NOT be included if blocking it impairs legitimate Bitcoin wallet functionality.**

---

## Verification Steps (Required)

Before submitting, complete all six steps:

- [ ] **WHOIS lookup** — identify the domain owner (`lookup.icann.org`)
- [ ] **SSL certificate** — confirm organization name (`crt.sh`)
- [ ] **SecurityTrails / PassiveDNS** — check IP history and related domains (`securitytrails.com`)
- [ ] **URLScan.io** — analyze what the domain does (`urlscan.io`)
- [ ] **Privacy harm** — articulate the specific harm in one sentence
- [ ] **Functional test** — confirm blocking the domain does not break wallet functionality

---

## Submitting a Domain

1. Fork the repository
2. Create a branch: `git checkout -b add-domain-example-com`
3. Add your entry to `domains.csv` (see format below)
4. Commit: `git commit -m "Add example.com: [one-line description]"`
5. Push and open a pull request using the template below

---

## domains.csv Format

```
domain,organization,category,harm,source,date_verified,notes
```

**Categories:** `Blockchain Analytics` | `Deanonymization` | `Wallet Telemetry` | `KYC/AML Compliance` | `Address Screening` | `IP Logging`

**Example:**
```csv
*.suspicious-analytics.com,Suspicious Analytics Inc.,Blockchain Analytics,"Logs querying IP addresses against Bitcoin address lookup requests",https://suspicious-analytics.com/api-docs,2026-05-04,
```

Use `*.domain.com` to block all subdomains. Use `domain.com` for the root domain. Submit both in the same PR.

---

## Pull Request Template

```markdown
## Domain Submission

**Domain:** *.example-surveillance.com
**Organization:** Example Surveillance Inc.
**Category:** Blockchain Analytics

## Evidence of Privacy Harm

[Describe what you found. Include links to WHOIS results, SSL certificate 
findings, URLScan analysis, or wallet source code references.]

## Verification Checklist

- [ ] WHOIS lookup completed
- [ ] SSL certificate inspected
- [ ] SecurityTrails / PassiveDNS checked
- [ ] URLScan.io analysis completed
- [ ] Tested that blocking does not break wallet functionality

## Functional Impact Test

[Which wallet? Which functions tested? Result?]

## domains.csv Entry

[Paste your CSV row here]
```

---

## Reporting False Positives

If a domain in the blocklist is incorrectly included or breaks legitimate functionality, open an issue with:

- The domain in question
- What functionality breaks when it is blocked
- Evidence that the domain serves a legitimate purpose that outweighs the surveillance concern

---

## Code of Conduct

- Research objectively — provide evidence, not assertions
- No personal information about individuals associated with surveillance firms
- No speculation — evidence of current harm is required
- Engage respectfully in review discussions

---

## Review Timeline

Pull requests are reviewed within 21 days. All domain additions are independently verified before merging. See the [Contributor Guide](docs/SatoshiShield_Contributor_Guide_v1_0.docx) for the full verification process.
