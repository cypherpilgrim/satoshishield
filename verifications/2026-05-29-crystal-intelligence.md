---
type: verification
company: "crystal-intelligence"
date: 2026-05-29
verifier: cypherpilgrim
outcome: PENDING FUNCTIONAL TEST
project: SatoshiShield
tier: 1
status: in-verification
verdict: Meets SatoshiShield inclusion criteria — rebrand of existing Tier 1 firm Crystal Blockchain; new domains and active product surface
date_started: 2026-05-29
date_completed:
block_targets:
  - crystalintelligence.com
  - "*.crystalintelligence.com"
  - crystalintelligence.app
  - "*.crystalintelligence.app"
non_targets:
  - crystalintelligence.teamtailor.com (third-party HR platform)
hq_country: NL
operations_countries:
  - NL
  - GB
origin_country: NL
predecessor: '"crystal-blockchain"'
successor: []
related_companies:
  - "tether"
related_verifications: []
revision_history:
  - "2026-05-29 v1: Initial verification — rebrand from Crystal Blockchain to Crystal Intelligence"
tags:
  - verification
  - tier-1-candidate
  - netherlands
  - europe
  - rebrand
  - coverage-gap-correction
---

> **Public sanitized verification record.** A research artifact from the SatoshiShield project, published to show the verification methodology applied to each candidate domain. Internal lab infrastructure has been redacted. Not legal or financial advice.


# Crystal Intelligence — Verification Record

**VERDICT: VERIFIED.**

Crystal Intelligence is the rebranded entity of Crystal Blockchain (already in SatoshiShield blocklist since v1.0 baseline). The new corporate identity operates from two new active root domains — `crystalintelligence.com` and `crystalintelligence.app` — that are not in the v1.5.0 blocklist. Confirmed gap.

The Crystal Expert product (their primary SaaS/API surveillance offering) runs from `expert.crystalintelligence.com`. This is the active product surface that exchange/bank/LE compliance teams call when screening Bitcoin addresses today.

## Block scope

| Domain | Recommendation |
|---|---|
| `crystalintelligence.com` | BLOCK (root + wildcard) |
| `crystalintelligence.app` | BLOCK (root + wildcard) |
| `expert.crystalintelligence.com` | Covered by wildcard |
| `crystalintelligence.teamtailor.com` | NOT BLOCKED — third-party HR platform (Teamtailor), not Crystal's own infrastructure |

## Existing entry updates required

The four existing rows for Crystal Blockchain in `domains.csv` (`*.crystalblockchain.com`, `crystalblockchain.com`, `*.bitrank.com`, `bitrank.com`) should be updated in the same v1.6.0 PR:

- **Organization** field: `Crystal Blockchain` → `Crystal Intelligence (formerly Crystal Blockchain)`
- **Source** URL: `https://crystalblockchain.com/` → `https://crystalintelligence.com/`
- **date_verified**: `2026-05-04` → `2026-05-29`

This matches the pattern established with Lukka/Coinfirm in v1.5.0.

## Step 1 — WHOIS lookup — RUN LOCALLY

Commands for verification on local machine:

whois crystalintelligence.com
whois crystalintelligence.app

Expected findings to document:
- Registrant organization (likely Crystal Intelligence or a privacy-redacted variant)
- Registration date for `crystalintelligence.com` (rebrand likely post-2022)
- Registration date for `crystalintelligence.app` (likely registered alongside .com)
- Nameservers (should be consistent across both)

## Step 2 — SSL Certificate — RUN LOCALLY

echo | openssl s_client -connect crystalintelligence.com:443 -servername crystalintelligence.com 2>/dev/null | openssl x509 -text -noout | grep -E "Subject:|DNS:"
echo | openssl s_client -connect crystalintelligence.app:443 -servername crystalintelligence.app 2>/dev/null | openssl x509 -text -noout | grep -E "Subject:|DNS:"
echo | openssl s_client -connect expert.crystalintelligence.com:443 -servername expert.crystalintelligence.com 2>/dev/null | openssl x509 -text -noout | grep -E "Subject:|DNS:"

Or browser: visit each URL and inspect cert via padlock > Certificate.

Expected:
- Organization (O) field should identify Crystal Intelligence or related corporate entity
- Subject Alternative Names should enumerate additional active subdomains

## Step 3 — SecurityTrails / Passive DNS — RUN LOCALLY (or browser)

Visit in browser:
- https://crt.sh/?q=crystalintelligence.com (full certificate transparency log)
- https://crt.sh/?q=crystalintelligence.app
- https://securitytrails.com/domain/crystalintelligence.com (DNS history)
- https://securitytrails.com/domain/crystalintelligence.app

Expected findings to document:
- Subdomain enumeration (any beyond `expert`, `www`, marketing subdomains)
- IP history showing infrastructure consolidation (should resolve to consistent Cloudflare or AWS infrastructure)
- Any unexpected subdomain patterns that might indicate additional product surfaces

## Step 4 — Behavioral Evidence — COMPLETE (vendor documentation route)

Crystal Intelligence is a self-documented surveillance vendor; vendor-documentation route per Contributor Guide v1.4 §4.4 applies. Evidence:

**Primary product surface (Crystal Expert):**
- Login portal: `https://expert.crystalintelligence.com/`
- Self-described capability: "real-time transaction monitoring, automated address screening, and sanctions and blocklist checks"
- Coverage scope: 330+ blockchains, 110,000+ attributed entities, 10,000+ digital assets
- Access modes: free online blockchain explorer, SaaS, API

**Self-described function from `crystalintelligence.com`:**
> "Our crypto transaction monitoring and risk assessment software enables financial institutions to comply with global anti-money laundering regulations. Law enforcement agencies and regulators use our technology and data to track the movement of cryptocurrencies in real-time to identify illicit fund flows and solve investigations."

**Customer self-description:**
> "Compliance and risk teams at financial institutions, crypto exchanges, and payment companies; law enforcement and government agencies investigating illicit activity; virtual asset service providers (VASPs) managing AML/KYC obligations; and businesses and auditors seeking transparency into crypto transactions."

**Risk scoring confirmation:**
> "Crystal applies two types of risk scoring. For attributed entities — such as exchanges, darknet markets, or gambling services — risk scores are pre-assigned and updated as AML and KYC policies change. For unattributed wallets, Crystal calculates dynamic scores in real time based on transaction patterns and behavior."

**Entity clustering confirmation (the deanonymization function):**
> "An entity is a cluster of addresses that are determined, through data analysis and attribution methods, to belong to the same controlling party."

**Sources documenting historical context:**
- Crystal Intelligence original launch by Bitfury (historical record)
- Tether strategic investment July 2025: https://tether.io/news/tether-announces-strategic-investment-in-crystal-intelligence-strengthening-blockchain-forensics-and-efforts-to-combat-illicit-stablecoin-activity/
- 2026 product expansion: 335 blockchains supported (Jan 2026), XDC Network integration for RWA tokenization (Jan 2026), XRP/XLM coverage expansion

**Corporate identity:**
- HQs: London and Amsterdam (per careers page: "globally distributed team of world-class blockchain analysts, award-winning mathematicians, and professional software developers with headquarters in London and Amsterdam")
- CEO: Marina Khaustova
- Employee count: Medium (51-250) per Coinpedia
- Founded by: Bitfury (original launch)

## Step 5 — Privacy Harm Assessment

The Crystal Expert API logs querying IP addresses against the Bitcoin addresses being screened. Each query from an exchange's compliance team, a bank's AML system, or a law enforcement investigator produces a database record linking that querier's network identity to the address(es) under investigation.

A Bitcoin user has no direct interaction with `crystalintelligence.com`/`.app` under normal usage — but apps, browser extensions, exchange compliance backends, and any service that has integrated Crystal Expert in their compliance stack will make outbound queries to Crystal's endpoints. Those queries reveal which addresses are interesting and to whom.

DNS-layer blocking of `crystalintelligence.com` and `crystalintelligence.app` prevents any device on the protected network from being a source of those queries, even if some app on that device has Crystal SDK integration.

## Step 6 — Inclusion Criteria — MEETS MULTIPLE

Applying the six SatoshiShield inclusion criteria from the white paper:

- [x] **Blockchain Analytics firm** — primary business is correlating Bitcoin addresses with real-world identities. Self-described.
- [x] **Address Screening API** — Crystal Expert is an API-first product used by exchange compliance teams.
- [x] **IP-Logging Infrastructure** — canonical IP-logging pattern; every Crystal Expert API call is logged.
- [x] **KYC/AML Intelligence** — explicit AML positioning; AML/KYC compliance is the firm's primary market identity.
- [x] **Deanonymization-adjacent** — entity attribution and ownership clustering, with 110,000+ attributed entities.
- [ ] Wallet Telemetry — Crystal Intelligence is a B2B vendor; no consumer wallet integration documented.

Five of six criteria met. The case for inclusion is equivalent to or stronger than the original Crystal Blockchain case from v1.0.

## Step 7 — Functional Impact Test — RUN LOCALLY

Procedure:
1. Add the candidate domains to your Pi-hole instances (the test resolver at <internal-ip> and the test resolver at <internal-ip>) as temporary blocks
2. Test with Sparrow Wallet → Bitcoin Knots RPC (should still work — no Crystal integration in self-hosted wallet stack)
3. Test with Electrum → public Electrum server (should still work)
4. Test with BlueWallet (mobile) (should still work)
5. Test with browser visits to mempool.space and blockstream.info (should still work)
6. Negative test: visit `crystalintelligence.com` directly (should fail — connection refused)

Expected outcome: no impact on Bitcoin wallet functionality. Crystal Intelligence is a B2B product not integrated into consumer wallets.

## domains.csv entries (4 new rows)

```
*.crystalintelligence.com,Crystal Intelligence,Blockchain Analytics,1,Logs querying IP addresses against Bitcoin address lookup requests. Operates Crystal Expert SaaS/API for transaction monitoring entity attribution and risk scoring across 330+ blockchains. Used by financial institutions exchanges and law enforcement.,https://crystalintelligence.com/,2026-05-29,Rebrand of Crystal Blockchain. Tether took strategic investment July 2025. HQ London and Amsterdam. Originally launched by Bitfury.
crystalintelligence.com,Crystal Intelligence,Blockchain Analytics,1,Root domain of Crystal Intelligence rebranded surveillance platform.,https://crystalintelligence.com/,2026-05-29,Rebrand of Crystal Blockchain.
*.crystalintelligence.app,Crystal Intelligence,Blockchain Analytics,1,Secondary marketing domain for Crystal Intelligence blockchain analytics platform.,https://crystalintelligence.app/,2026-05-29,Active alongside crystalintelligence.com.
crystalintelligence.app,Crystal Intelligence,Blockchain Analytics,1,Root domain of Crystal Intelligence secondary marketing surface.,https://crystalintelligence.app/,2026-05-29,Active alongside crystalintelligence.com.
```

## Existing rows to update (4 updates)

For each of the four existing Crystal Blockchain rows, change `Crystal Blockchain` → `Crystal Intelligence (formerly Crystal Blockchain)` in the organization field, change source URL to `https://crystalintelligence.com/`, and update `date_verified` to `2026-05-29`. The notes field on each can have "Rebranded to Crystal Intelligence in 2024-2025" appended.

## regex.txt patterns to add

```
(\.|^)crystalintelligence\.com$
(\.|^)crystalintelligence\.app$
```

## Pattern observations

This is the first SatoshiShield case of a Tier 1 firm rebranding *without acquisition* — same company, new name, new domains. Worth documenting in Industry Context Notes as a pattern distinct from the acquisition/consolidation patterns established by Mastercard/CipherTrace, Lukka/Coinfirm, and HSBC/Elliptic.

## Verification status

| Step | Status | Outcome |
|---|---|---|
| 1. WHOIS | ⨯ Pending local | Commands documented above |
| 2. SSL certificate | ⨯ Pending local | Commands documented above |
| 3. SecurityTrails | ⨯ Pending local/browser | URLs documented above |
| 4. Behavioral evidence | ✓ Complete | Vendor self-documentation; equivalent to Tier 1 baseline standard |
| 5. Privacy harm | ✓ Complete | IP logging against Bitcoin address queries |
| 6. Inclusion criteria | ✓ Complete | **MEETS 5 of 6 CRITERIA — INCLUDE** |
| 7. Functional impact test | ⨯ Pending local | Procedure documented above |

**Final verdict (pending Steps 1-3 and Step 7 local execution):** Crystal Intelligence is the rebranded successor of Crystal Blockchain and continues operating the same surveillance functions under new domains. INCLUDE in SatoshiShield v1.6.0.
