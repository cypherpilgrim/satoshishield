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

## Which Tier?

SatoshiShield uses two tiers, and new submissions should specify which one:

| Tier | When to use it |
|---|---|
| **1** | The harm is confirmed with evidence from the verification steps below, and blocking the domain has been tested against real wallet software with no negative impact. |
| **2** | The domain pattern matches surveillance behavior but the harm has not yet been confirmed, or the domain is dual-use (also serves legitimate purposes) and needs community discussion before being treated as confirmed. |

When in doubt, submit as Tier 2 and let the review process promote it. Submitting confirmed-harm domains directly to Tier 1 is appropriate when the evidence is unambiguous.

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
3. Add your entry to `domains.csv` (Tier 1) or `domains-tier2.csv` (Tier 2), see format below
4. Commit: `git commit -m "Add example.com: [one-line description]"`
5. Push and open a pull request using the template below

---

## CSV Format

Both `domains.csv` and `domains-tier2.csv` use the same column schema:

```
domain,organization,category,tier,harm,source,date_verified,notes
```

**Column definitions:**

| Column | Description |
|---|---|
| `domain` | The domain to block. Use `*.example.com` for wildcard coverage of all subdomains, or `example.com` for the root domain only. Submit both as separate rows. |
| `organization` | The company or entity operating the domain. |
| `category` | One of: `Blockchain Analytics`, `Deanonymization`, `Wallet Telemetry`, `KYC/AML Compliance`, `Address Screening`, `IP Logging`, `Surveillance Analytics`. |
| `tier` | `1` for confirmed surveillance harm, `2` for entries needing further verification. |
| `harm` | One sentence describing the specific privacy harm. |
| `source` | URL or reference supporting the inclusion. |
| `date_verified` | Date of last verification in `YYYY-MM-DD` format. |
| `notes` | Optional additional context, caveats, or related domains. Leave empty if none. |

**Tier 1 example:**

```csv
*.suspicious-analytics.com,Suspicious Analytics Inc.,Blockchain Analytics,1,Logs querying IP addresses against Bitcoin address lookup requests,https://suspicious-analytics.com/api-docs,2026-05-19,
```

**Tier 2 example:**

```csv
*.dual-use-service.com,Dual Use Service Inc.,Wallet Telemetry,2,May log Bitcoin-related queries against IP but also serves legitimate functions,https://dual-use-service.com/about,2026-05-19,NEEDS VERIFICATION - confirm specific wallet integrations before promoting to Tier 1.
```

Use `*.domain.com` to block all subdomains and `domain.com` for the root domain. Submit both rows in the same PR.

---

## Pull Request Template

```markdown
## Domain Submission

**Domain:** *.example-surveillance.com
**Organization:** Example Surveillance Inc.
**Category:** Blockchain Analytics
**Tier:** 1 (or 2 if pending verification)

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

## CSV Entry

[Paste your CSV row(s) here. Both *.domain.com and domain.com if applicable.]
```

---

## Reporting False Positives

If a domain in the blocklist is incorrectly included or breaks legitimate functionality, open an issue with:

- The domain in question
- What functionality breaks when it is blocked
- Evidence that the domain serves a legitimate purpose that outweighs the surveillance concern

---

## Code of Conduct

- Research objectively, providing evidence rather than assertions
- No personal information about individuals associated with surveillance firms (the project targets organizations, not people)
- No speculation; evidence of current harm is required
- Engage respectfully in review discussions
- Use a pseudonymous GitHub account if you prefer; the project practices what it preaches

---

## Review Timeline

Pull requests are reviewed within 21 days. All domain additions are independently verified before merging. See the [Contributor Guide](docs/SatoshiShield_Contributor_Guide_v1_0.docx) for the full verification process.
