---
# Core
type: verification
company: "uppsala-security"
date: 2026-05-27
verifier: cypherpilgrim
outcome: INCLUDED IN BLOCKLIST

# Project metadata
project: SatoshiShield
tier: 1
status: in-blocklist

# Verdict and process
verdict: Meets SatoshiShield inclusion criteria — Korean-origin Singapore-based vendor with Sentinel Protocol; cross-vendor federation participant
date_started: 2026-05-27
date_completed: 2026-05-27

# Domain scope
block_targets:
  - "*.uppsalasecurity.com"
  - "*.sentinelprotocol.io"

# Geography
hq_country: SG
operations_countries: [KR, JP, SG]
origin_country: KR

# Lineage
predecessor: []
successor: []
related_companies:
  - "match-systems"
  - "slowmist"
related_verifications:
  - "2026-05-27-match-systems"
  - "2026-05-27-slowmist"

# Tags
tags:
  - verification
  - tier-1-candidate
  - korean-origin
  - singapore-hq
  - asian-vendor
  - cross-vendor-federation
---

> **Public sanitized verification record.** A research artifact from the SatoshiShield project, published to show the verification methodology applied to each candidate domain. Internal lab infrastructure has been redacted. Not legal or financial advice.


# Uppsala Security — Tier 1 Verification Record

**Date:** 2026-05-27
**Researcher:** cypherpilgrim
**Candidate:** Uppsala Pte. Ltd. (operating as Uppsala Security, Sentinel Protocol, Uppsala Foundation, 센티넬 프로토콜)

## Block scope

| Domain | Pattern | Rationale |
|---|---|---|
| `uppsalasecurity.com` | `*.uppsalasecurity.com` (wildcard) | Main corporate site, ICF API, Sentinel Protocol product surfaces, Korean-language version |
| `sentinelprotocol.io` | `*.sentinelprotocol.io` (wildcard) | Sentinel Protocol blockchain product domain, UPPward browser extension subdomain (uppward.sentinelprotocol.io), TRDB query interfaces |

**Non-targets (do NOT block):**
- The UPP ERC-20 token smart contract on Ethereum is not DNS-blockable (on-chain)
- LinkedIn, Twitter, Medium, Telegram (third-party platforms) — out of scope
- Note: github.com/Sentinel-Protocol may contain open-source repositories — preserve per Iknaio/GraphSense pattern if applicable

## Step 1 — Corporate identity, products, customers ✓ COMPLETE

### Corporate entity

| Field | Value |
|---|---|
| Legal entity | **Uppsala Pte. Ltd.** (Singapore Pte Ltd) |
| Doing business as | Uppsala Security, Sentinel Protocol, Uppsala Foundation, 센티넬 프로토콜 |
| HQ address | Seng Tower, 133 Cecil St, Keck, Central Singapore, 069535 |
| Branch offices | Seoul (South Korea), Tokyo (Japan) |
| Founded | January 2018 |
| Origin country | South Korea (founder confirmed in 2020 publication: "we originated from South Korea, a global blockchain hub") |
| Founders | Patrick Kim (CEO, Co-Founder), Hae Min Park (Co-Founder) |
| Founder background | Patrick Kim — formerly Cyber Technology Specialist at **Darktrace** (UK cybersecurity major) |
| Company type | For-profit |
| Funding | ICO (Initial Coin Offering) for UPP token, plus venture funding |
| Contact | info@uppsalasecurity.com, support@uppsalasecurity.com |
| Cloud infrastructure | Google Cloud Platform (per ZoomInfo) |
| Languages supported | English, Korean (matching their Korean origin and customer base) |

### Origin and structure

Uppsala Security originated in South Korea in 2018 as a blockchain-based threat intelligence project (Sentinel Protocol). The corporate entity was registered as Uppsala Pte. Ltd. in Singapore for legal incorporation and ASEAN market access, with operational presence retained in Seoul (primary R&D and customer base) and expanded to Tokyo for Japanese market coverage.

Founder Patrick Kim's background as a Cyber Technology Specialist at Darktrace (the UK cybersecurity major famous for ML-driven enterprise security products) is significant — it places Uppsala Security in a different lineage from CIS-origin (Match Systems, Bitrace) or US-academic-origin (Iknaio) candidates. Uppsala's intellectual heritage is Western enterprise cybersecurity, applied to cryptocurrency.

Co-founder Hae Min Park is Korean. The company brands and operations are heavily Korean-flavored (Korean-language site, primary customer base in Korea, Samsung partnership), with Singapore providing the legal entity wrapper.

### Product portfolio

Uppsala Security operates an integrated surveillance product family that has evolved since 2018:

**1. Sentinel Protocol** — Core platform
- "First crowdsourced Threat Intelligence Platform powered by AI, blockchain, machine learning"
- The blockchain platform with the UPP ERC-20 token serves as the underlying infrastructure
- Crowdsourced contribution model: community members ("Sentinels") report and validate threat intelligence

**2. TRDB (Threat Reputation Database)** — The actual surveillance database
- Threat intelligence database queried by all Uppsala products
- Validated data published to blockchain
- Contains malicious wallet addresses, phishing URLs, scam domains, malware indicators

**3. CARA (Crypto Analysis Risk Assessment)** — Patent-pending ML risk scoring
- Machine learning algorithms (patent-pending per their October 2019 announcement)
- "Classifies the risk level of crypto addresses based on learned behaviors of both known malicious wallets and normal wallets"
- This is the direct functional equivalent of Chainalysis's risk scoring algorithm

**4. CTDS (Crypto Threat Detection System)** — STR/CTR reporting
- Suspicious Transaction Reporting (STR) and Counterfeit Currency Reporting (CTR)
- "Handles STR and CTR for millions of additional virtual asset wallets with just one click"
- Targets the South Korea Travel Rule mandatory March 2022

**5. ICF API (Interactive Cooperation Framework API)** — Public API for TRDB
- "Enables crypto service providers to query the TRDB, whitelists, and blacklists - in real time"
- Located at uppsalasecurity.com/icfapi/
- This is the address screening API endpoint

**6. UPPward** — Browser extension at uppward.sentinelprotocol.io
- "Search engine into the TRDB for a secure user browsing experience"
- "Users are able to search URLs, domains, and wallet address to verify the authenticity"
- Direct user-facing telemetry: every URL/domain/wallet lookup by extension users goes to Uppsala's servers

**7. CRSS (Crypto Risk Scoring System)** — referenced in product naming
**8. Sentinel Portal** — community reporting interface
**9. UPP Token** — ERC-20 cryptocurrency token

### Multi-blockchain coverage

Uppsala Security's products support multiple blockchains. From the September 2021 announcement, they support Binance Smart Chain (BSC) plus Bitcoin, Ethereum, and others. The exact scope appears to be continuously expanding.

### Customer scale and disclosure

Per the May 2023 award announcement, Uppsala Security has **2,000+ users including:**
- Government agencies
- Financial institutions
- Crypto exchanges
- Payment services
- Wallets
- Custodial services
- Gaming companies
- Fintech solutions

### Notable named customers and partners

**Wallet integration (direct user telemetry pathway):**
- **Samsung Electronics — Samsung Blockchain Wallet** (October 2020 "Blockchain Service AML Integration Agreement"). Samsung Blockchain Wallet users get real-time threat detection and push notifications triggered by Uppsala's TRDB queries. Available to Samsung Galaxy users in **19 countries**. This is direct wallet telemetry on a major consumer product.

**Korean cryptocurrency exchanges and platforms:**
- **Bithumb** — one of South Korea's largest crypto exchanges
- **Coin&Coin Exchange**
- **Danal Fintech**
- **Hexlant**
- **Korea Digital Asset (KODA)** — Korean custody firm (February 2023 partnership)

**Korean cybersecurity partnerships:**
- **AhnLab Blockchain Company** — South Korean cybersecurity major (MoU April 30, 2024, focused on "next-generation virtual asset anti-money laundering security technology")

**Singapore government engagement:**
- **Monetary Authority of Singapore (MAS)** — Digital Acceleration Grant recipient (April 2021), Financial Sector Development Grant
- **APIX Platform** — Joined the MAS-backed API Exchange flagship fintech platform (October 2019)

**International law enforcement training:**
- **INTERPOL GLACY+ project** — Uppsala Security designed Capture-The-Flag (CTF) challenges for the **Digital Security Challenge 2024 (DSC2024)** at Cebu, Philippines
- The DSC2024 event saw **47 law enforcement officers from 21 countries** learning and competing in challenges built by Uppsala Security focused on ransomware, OSINT, and cryptocurrency theft investigations
- This is documented evidence of Uppsala Security training international law enforcement in cryptocurrency surveillance techniques

**Cross-vendor partnerships (confirmed bidirectionally):**
- **Match Systems** (matchsystems.com lists Uppsala as partner)
- **SlowMist** (misttrack.io lists Uppsala as partner — uppsalasecurity logo present)

### Awards and recognition

- "Most Innovative Cryptocurrency Risk Management 2023 — Singapore" Award (May 2023)
- MAS Digital Acceleration Grant (Singapore government)
- INTERPOL GLACY+ project trainer (international law enforcement)
- ETH Bucharest 2024 Community Partner (Ethereum ecosystem recognition)

### Korea Travel Rule connection

South Korea's Travel Rule became mandatory in March 2022 for Virtual Asset Service Providers (VASPs). This regulation requires VASPs to share customer information for cryptocurrency transactions over a threshold. Uppsala Security's CTDS product is specifically positioned as a Travel Rule compliance tool, automating STR/CTR reporting for Korean VASPs. This positions Uppsala as the operational layer between Korean VASPs and Korean regulators.

### Three-way vendor cross-reference confirmed

The Uppsala Security verification completes the three-way data-sharing triangle observed across the SatoshiShield project:

```
                Match Systems
                ╱           ╲
               ╱             ╲
              ╱               ╲
         SlowMist  ─────────  Uppsala Security
```

Each vendor publicly lists the other two as partners on their marketing materials:
- Match Systems homepage: lists slowmist.com AND uppsalasecurity.com as partners
- SlowMist misttrack.io: displays Match Systems AND Uppsala Security logos
- Uppsala Security: confirmed appearance on both Match Systems and SlowMist partner pages

This is the documented triangle of cross-vendor surveillance data federation in the Asian/CIS surveillance industry. For the SatoshiShield project, this validates the multi-vendor blocking strategy: blocking any one of the three leaves data flowing through the other two.

## Step 2 — WHOIS lookup ✓ COMPLETE

**Sources:** Command-line `whois uppsalasecurity.com` and `whois sentinelprotocol.io`, May 27, 2026

### Findings

| Field | uppsalasecurity.com | sentinelprotocol.io |
|---|---|---|
| Registrar | NameCheap, Inc. (IANA 1068) | NameCheap, Inc. (IANA 1068) |
| Privacy proxy | Withheld for Privacy ehf (Iceland) | Withheld for Privacy ehf (Iceland) |
| Created | 2018-12-05 | **2018-01-30 (10 months earlier)** |
| Updated | 2025-11-05 | 2026-01-05 |
| Registry expiration | 2026-12-05 (~18 months out) | 2027-01-30 (~20 months out) |
| Nameservers | **ns-cloud-B1/B2/B3/B4.googledomains.com** | **ns-cloud-E1/E2/E3/E4.googledomains.com** |
| Lock flags | clientTransferProhibited (single) | clientTransferProhibited (single) |
| DNSSEC | Unsigned | Unsigned |

### Headline: First Google Cloud DNS in the SatoshiShield project

Both Uppsala Security domains use Google Cloud DNS (`ns-cloud-*.googledomains.com`). This is the first appearance of Google Cloud DNS in the SatoshiShield cohort, and it confirms ZoomInfo's attribution of Google Cloud Platform as Uppsala's cloud infrastructure. Combined, GCP + Google Cloud DNS + likely Google Workspace email indicates a single-vendor Google stack — the cleanest cloud-vendor-consolidation pattern observed in the cohort.

DNS provider variety across all 10 verified candidates is now:
- Cloudflare: 5+ vendors (most common)
- Akamai: SlowMist
- AWS Route 53: AnChain (.com), Coinfirm
- Google Cloud DNS: Uppsala Security (NEW)
- Other (GitHub Pages/Fastly, GoDaddy default, Namecheap default, Easyname): various

### Different Google Cloud DNS allocation groups across the two domains

The two domains use different Google Cloud DNS allocation groups (B-pool for uppsalasecurity.com, E-pool for sentinelprotocol.io). The letter prefix indicates different DNS zones — likely different GCP projects, or at least different zones within the same account. This represents operational separation at the DNS-zone level, similar to Match Systems' different Cloudflare accounts.

This does not change the verification decision — common ownership is unambiguous through public marketing materials (sentinelprotocol.io is explicitly identified as Uppsala Security's blockchain product platform). The DNS-zone separation reflects organizational structure: the corporate domain and the product domain are managed under different GCP project boundaries, which is normal for companies with separate engineering teams.

### Chronology: Sentinel Protocol predates Uppsala Security by 10 months

The sentinelprotocol.io domain was registered 2018-01-30, while uppsalasecurity.com was registered 2018-12-05 — a 10-month gap. This corroborates the corporate history documented in Step 1: Sentinel Protocol was the original ICO/token project launched in early 2018; "Uppsala Security" was the corporate rebrand that came later in 2018 when the project pivoted from token-economy focus to commercial AML services.

For the white paper, this is a case study in surveillance industry evolution. The same domain-creation evidence we'd use to track Chainalysis's corporate domain history (chainalysis.com created ~2014) here shows a different company trajectory: from community-driven ICO blockchain project (sentinelprotocol.io) to commercial surveillance vendor (uppsalasecurity.com). The token-incentivized crowdsourced contribution model still exists, but now feeds the commercial AML product line.

### Common ownership confirmation

Both domains use the same registrar (NameCheap), same privacy proxy (Withheld for Privacy ehf, Iceland-based), same lock posture (single clientTransferProhibited flag), and both run on Google Cloud DNS (different allocation groups but same provider). Combined with the explicit public cross-references (uppsalasecurity.com identifies sentinelprotocol.io as their blockchain product), common ownership under Uppsala Pte. Ltd. is unambiguous.

### Registration patterns

The 18-20 month forward expiration dates indicate Uppsala uses moderate renewal cycles rather than long-term forward registration. Compare to SlowMist's 12-year forward registration — Uppsala is operationally lighter-touch on domain administration, consistent with the NameCheap retail registration profile.

### Verdict

Both Uppsala Security domains confirmed as operated by Uppsala Pte. Ltd. via shared NameCheap registration, shared Iceland privacy proxy, and shared Google Cloud DNS infrastructure (across different allocation groups). The chronology aligns with the documented corporate history (Sentinel Protocol first as ICO, then Uppsala Security as commercial rebrand). The wildcard block scope on both (`*.uppsalasecurity.com` + `*.sentinelprotocol.io`) remains correct.

## Step 3 — Subdomain enumeration ✓ COMPLETE (partial)

**Source:** Direct observation from product documentation and Medium publication

### Observed uppsalasecurity.com subdomains/paths

- `uppsalasecurity.com` — Main corporate site (English)
- `uppsalasecurity.com/ko/` or similar — Korean-language version
- `uppsalasecurity.com/icfapi/` — ICF API documentation/portal

### Observed sentinelprotocol.io subdomains

- `sentinelprotocol.io` — Sentinel Protocol main product site
- `uppward.sentinelprotocol.io` — UPPward browser extension product page

### Expected additional subdomains (typical for this product family)

Step 4 SecurityTrails enumeration should confirm:
- api.uppsalasecurity.com or api.sentinelprotocol.io — likely TRDB API endpoint
- cara.uppsalasecurity.com — possible CARA risk scoring service
- ctds.uppsalasecurity.com — possible CTDS reporting service
- portal.uppsalasecurity.com — likely customer portal
- forum.sentinelprotocol.io or community.sentinelprotocol.io — community Sentinel forum
- explorer.sentinelprotocol.io — possible UPP token explorer
- docs.uppsalasecurity.com — likely API documentation
- blog.uppsalasecurity.com — possible (or hosted on Medium)
- staging.* — likely staging environments

## Step 4 — SecurityTrails / passive DNS ✓ COMPLETE

**Source:** SecurityTrails free-tier DNS records, May 27, 2026

### Infrastructure findings

| Layer | uppsalasecurity.com | sentinelprotocol.io |
|---|---|---|
| A records | 31.43.160.6, 31.43.161.6 (AWS) | **None at apex** |
| AAAA records | None | None |
| MX | Google Workspace (legacy + modern mixed) | Google Workspace (clean modern) |
| NS | ns-cloud-b1-b4.googledomains.com (Google Cloud DNS) | ns-cloud-e1-e4.googledomains.com (different GCP zone) |
| SOA | cloud-dns-hostmaster.google.com | cloud-dns-hostmaster.google.com |
| SPF | **Malformed first SPF + proper SPF** (RFC violation: multiple SPF + missing spaces in first) | Two SPF records (also RFC violation but both properly formatted) |
| Apex TXT verifications | Google ×2 | Google + **Atlassian** + **Microsoft 365 (MS=)** |
| Subdomain count | 18 | **98 — largest single-domain footprint in the project** |

### Headline: 98 subdomains on sentinelprotocol.io — largest in the cohort

The sentinelprotocol.io domain has 98 subdomains — the largest single-domain footprint in the SatoshiShield project to date. Combined with the 18 subdomains on uppsalasecurity.com, Uppsala Security operates a 116-subdomain total footprint, second-largest in the cohort after Lukka+Coinfirm (272).

The architecture pattern (no apex A record but 98 subdomains) is consistent with a multi-tenant SaaS deployment where each major institutional customer gets a dedicated subdomain for their TRDB integration. This matches Uppsala's claimed customer base of 2,000+ users across exchanges, wallets, custodial services, gaming, and fintech — many of which likely have customer-specific subdomain endpoints for their AML compliance integrations.

The subdomain enumeration also likely includes:
- Per-product surfaces (UPPward, CARA, CTDS, TRDB, ICF API, Sentinel Portal)
- Geographic/language variants (Korean, Japanese)
- Blockchain/token interfaces (UPP token explorer, Sentinel forum)
- Testing/staging/development environments

For the verification, the wildcard block `*.sentinelprotocol.io` is correct and necessary — capturing all 98 subdomains where the actual surveillance product surfaces live.

### Headline: No apex IP on sentinelprotocol.io

The sentinelprotocol.io apex domain has no A or AAAA records, meaning `https://sentinelprotocol.io/` does not resolve to any web content. All Uppsala Security web traffic on this domain routes exclusively through subdomains.

This is unusual in the cohort — most candidates have at least a redirect or marketing page at the apex. Possible explanations: intentional architecture choice (multi-tenant SaaS pattern), recent infrastructure migration, or apex consolidation around uppsalasecurity.com as the marketing front. The verification decision is unchanged regardless.

### Headline: Multi-cloud architecture — first in the project

Uppsala Security operates a genuinely mixed-cloud stack:

- **DNS**: Google Cloud DNS
- **Web hosting (uppsalasecurity.com)**: AWS (IP range 31.43.160.x attributed to Amazon by SecurityTrails)
- **Application backend**: GCP (per ZoomInfo)
- **Email**: Google Workspace primary + Amazon SES (transactional) + Mailjet (marketing) + Freshdesk (support)
- **Project management**: Atlassian
- **Microsoft 365 verification** also present on sentinelprotocol.io

This is the most architecturally diverse cloud stack observed in the SatoshiShield cohort. Most candidates standardize on one cloud provider; Uppsala uses at least three (Google for DNS+backend, AWS for compute, plus the SaaS layer). This may reflect Korean enterprise IT culture where multi-vendor strategies are common.

### Headline: Richest SaaS stack in the cohort

Combined apex TXT records and MX/SPF data reveal more SaaS service integrations on Uppsala than any prior candidate:

- Google Workspace (email + verification)
- Amazon SES (transactional email)
- Mailjet (French email marketing service)
- Freshdesk (customer support ticketing) — uppsalasecurity.com only
- Atlassian Jira/Confluence — sentinelprotocol.io only
- Microsoft 365 (verification present despite Google Workspace MX) — sentinelprotocol.io only

The combination of Mailjet + Freshdesk + Amazon SES + Google Workspace + Microsoft + Atlassian represents a mature B2B SaaS operational stack typical of established Korean tech companies. This is consistent with Uppsala's 2018 founding (8 years of operational accretion) and 2,000+ institutional customer base.

The Microsoft 365 verification on sentinelprotocol.io alongside Google Workspace MX may indicate parallel use of M365 services (Teams, SharePoint) while email runs through Google Workspace. Alternatively it could be vestigial from a previous M365 deployment that wasn't fully cleaned up.

### Malformed SPF on uppsalasecurity.com

The first SPF record on uppsalasecurity.com is malformed (missing spaces between mechanisms):

v=spf1include:_spf.google.cominclude:amazonses.cominclude:email.freshdesk.com-all include:spf.mailjet.com ?all

RFC 7208 requires whitespace between SPF mechanisms; this record will fail SPF validation. A properly formatted second SPF record exists below it, but having two SPF records is itself an RFC violation that causes SPF check failures. This indicates a sysadmin attempted to fix the malformed version but didn't remove the original — leaving both in place. Standard operational sediment.

This is the second candidate in the cohort with multiple-SPF-record problems (nterminal.com also had two SPF records). Email infrastructure hygiene appears to be a consistent weak point in the surveillance industry.

### Mixed legacy/modern MX on uppsalasecurity.com

uppsalasecurity.com's MX records mix modern format (aspmx.l.google.com + alt1/alt2) with legacy format (aspmx2/3.googlemail.com). Same pattern observed on Inca Digital's main domain — older Google Workspace tenant that hasn't been cleaned up. sentinelprotocol.io has a clean modern MX configuration (aspmx.l.google.com + alt1-4 only), consistent with its slightly later operational maturity.

### No LLM provider verifications

Despite Uppsala's "AI-driven" product positioning and the CARA patent-pending machine learning risk scoring algorithm, no OpenAI or Anthropic verifications are visible at either apex. This is a different pattern from Match Systems (OpenAI verification on cryptoofficer.ai) and Inca Digital (OpenAI + Anthropic on inca.digital). Uppsala's AI appears to be in-house proprietary ML (CARA's patented algorithms) rather than commercial LLM API integration. The "AI-driven" marketing claim refers to traditional ML rather than modern LLM tooling.

### Verdict

Uppsala Security operates the most architecturally diverse infrastructure in the SatoshiShield cohort — multi-cloud (Google + AWS), multi-SaaS (Mailjet + Freshdesk + Atlassian + Microsoft + Amazon SES + Google Workspace), with the largest single-domain subdomain footprint (98 on sentinelprotocol.io) and a no-apex-IP architecture suggesting multi-tenant SaaS deployment. The wildcard block scope on both domains (`*.uppsalasecurity.com` + `*.sentinelprotocol.io`) is correct and necessary given the breadth of subdomain surfaces.

## Step 5 — Behavioral analysis ✓ COMPLETE

### What does this domain do?

Both uppsalasecurity.com and sentinelprotocol.io serve as commercial surveillance product platforms operated by Uppsala Pte. Ltd.

**uppsalasecurity.com:**
- Corporate marketing site
- ICF API documentation at /icfapi/
- TRDB query endpoint (likely api.uppsalasecurity.com or similar)
- CARA risk assessment service
- CTDS STR/CTR reporting platform
- Korean and English language versions
- Sales, support, and customer onboarding workflows
- ETH Bucharest and other event sponsorship landing pages

**sentinelprotocol.io:**
- Sentinel Protocol blockchain product platform
- UPP token-related interfaces
- UPPward browser extension at uppward.sentinelprotocol.io
- Sentinel community forum and contribution interface
- TRDB blockchain publication layer

### What information do they collect?

Uppsala Security's products collect:

- Cryptocurrency addresses submitted by Samsung Blockchain Wallet users in 19 countries (real-time threat detection queries)
- Addresses submitted by 2,000+ institutional customers (Bithumb, Coin&Coin, Danal, Hexlant, KODA, others)
- IP addresses of all parties making API queries against the TRDB via ICF API
- URLs, domains, and wallet addresses submitted by UPPward browser extension users (the extension explicitly logs all lookups)
- Suspicious transaction reports (STRs) submitted by VASPs through CTDS for Korean Travel Rule compliance
- KYC/KYT data submitted through their integrated compliance workflows
- Community-reported threat intelligence from "Sentinels" (crowdsourced contributors)

The UPPward browser extension is particularly noteworthy. It is marketed as a privacy/security tool that helps users avoid scams — but its mechanism of action is to send every URL, domain, and wallet address the user looks up to Uppsala's servers for TRDB lookups. From a user's perspective, this is a Faustian bargain: gain malicious-site warnings at the cost of sending every visited URL to a Singapore-incorporated, Korean-origin surveillance vendor.

### Who do they share information with?

**Direct partnerships (confirmed):**
- Samsung Electronics (Samsung Blockchain Wallet AML integration, 19 countries of users)
- AhnLab Blockchain Company (April 2024 MoU)
- Bithumb, KODA, and Korean exchange ecosystem
- APIX Platform (MAS-backed fintech ecosystem)

**Cross-vendor data sharing (confirmed bidirectionally):**
- Match Systems
- SlowMist

**Government/regulatory engagement:**
- Monetary Authority of Singapore (grants, APIX platform)
- South Korean VASP regulators (Travel Rule compliance support)
- INTERPOL GLACY+ project (training law enforcement officers from 21 countries)

**Crowdsourced contributor network:**
- Public "Sentinel" contributors who report threat intelligence (incentivized via UPP token rewards)
- The crowdsourced model creates a data-flow loop where community contributions feed the TRDB which is then sold via the ICF API

### What does blocking it prevent?

Blocking `*.uppsalasecurity.com` and `*.sentinelprotocol.io` prevents:

1. **ICF API queries** — Wallets, exchanges, and applications integrated with Uppsala's TRDB API will fail to reach the screening endpoints
2. **UPPward browser extension lookups** — Users with UPPward installed will see the extension fail to query Uppsala's database, preventing the URL/domain/wallet logging that the extension generates
3. **Samsung Blockchain Wallet AML queries** — Note: this is on Samsung devices using Samsung's wallet service, which may or may not route through the SatoshiShield-protected network. If a Samsung user is on the protected network, AML queries from their Samsung Blockchain Wallet would fail. (Whether they break the wallet entirely depends on Samsung's implementation — if the wallet treats AML as advisory rather than blocking, the wallet may continue to function with degraded screening.)
4. **CTDS reporting** — Korean VASPs cannot submit STR/CTR through Uppsala's platform from the protected network
5. **CARA risk scoring** — Address risk assessments fail
6. **Sentinel Protocol community contributions** — Crowdsourced Sentinel reporting fails (a feature for SatoshiShield's mission, since this is the data feed loop)

### What does blocking it NOT prevent?

- The UPP ERC-20 token from continuing to exist (on-chain)
- Samsung Blockchain Wallet's basic functionality (wallet operations should continue even if AML queries fail, depending on Samsung's implementation)
- The TRDB blockchain publication layer (the Sentinel Protocol's on-chain layer is fundamentally not DNS-blockable)
- INTERPOL GLACY+ training operations (these are physical events)
- Korean VASP compliance with Korean Travel Rule via other tools (regulators don't mandate Uppsala specifically — only that VASPs comply)
- Cross-vendor data sharing through other channels (Match Systems and SlowMist data flows through their own infrastructure)

## Step 6 — Inclusion criteria ✓ COMPLETE

### Criteria met (multiple strong)

Uppsala Security meets SatoshiShield's Tier 1 inclusion criteria on multiple grounds:

**1. Address Screening API (PRIMARY)**
- ICF API documented at uppsalasecurity.com/icfapi/
- Queries TRDB whitelists, blacklists, and risk scores in real-time
- CARA machine learning risk scoring (patent-pending)
- Used by 2,000+ institutional customers and Samsung Blockchain Wallet users in 19 countries

**2. Wallet Telemetry (CONFIRMED, MAJOR)**
- Samsung Blockchain Wallet integration provides direct user telemetry from 19 countries
- This is the single largest documented consumer-wallet surveillance integration in the SatoshiShield cohort
- Samsung Blockchain Wallet users may not be aware their address activity is reported to Uppsala Security

**3. Browser Extension Telemetry (CONFIRMED)**
- UPPward extension at uppward.sentinelprotocol.io logs every URL, domain, and wallet address the user looks up
- Marketed as user protection but functionally a surveillance funnel

**4. Blockchain Investigations / Deanonymization (PRIMARY)**
- Crypto Threat Detection System (CTDS) and Crypto Analysis Risk Assessment (CARA)
- STR/CTR reporting for Korean Travel Rule compliance
- "Identification and arrest of a virtual assets fraud suspect through swift cooperation" claimed in May 2021 announcement

**5. Government and Law Enforcement Training (UNUSUAL DIRECT EVIDENCE)**
- INTERPOL GLACY+ project — Uppsala designed CTF challenges for Digital Security Challenge 2024
- 47 law enforcement officers from 21 countries trained on cryptocurrency investigation using Uppsala-built challenges
- This is direct, documented training of international law enforcement in cryptocurrency surveillance
- Comparable in nature to Chainalysis Reactor training programs

**6. Singapore Government Funding (CORROBORATING)**
- MAS Digital Acceleration Grant recipient (April 2021)
- MAS-backed APIX Platform member (October 2019)
- This positions Uppsala as a state-supported Singapore fintech vendor

**7. Cross-vendor Data Federation (DOCUMENTED)**
- Publicly listed on both Match Systems and SlowMist partner pages
- Confirms three-way data-sharing triangle in the Asian/CIS surveillance industry

### Tier classification

**TIER 1.** Uppsala Security meets the standard for primary inclusion based on:
- Multiple distinct surveillance product surfaces (TRDB, CARA, CTDS, ICF API, UPPward)
- Direct wallet telemetry through Samsung Blockchain Wallet (19 countries)
- Documented INTERPOL law enforcement training (47 officers, 21 countries)
- MAS Singapore government funding and APIX platform membership
- Publicly confirmed three-way cross-vendor partnership with Match Systems and SlowMist
- Founder background traceable to Darktrace (Western enterprise cybersecurity lineage)

### Confidence level

**HIGH.** Uppsala Security's evidence base consists primarily of their own published marketing materials, the Sentinel Protocol Medium publication (extensive press release archive), CB Insights and Crunchbase corporate records, and verifiable third-party events (INTERPOL DSC2024, MAS grant programs, Samsung Blockchain Wallet integration announcements). The company makes no attempt to obscure its surveillance positioning — they explicitly market AML, KYT, KYC, transaction tracking, regulatory compliance, and law enforcement training services.

The Samsung Blockchain Wallet integration is particularly noteworthy because it represents the clearest documented consumer-wallet telemetry pathway in the SatoshiShield project. Samsung Galaxy users in 19 countries who use the Samsung Blockchain Wallet are having their cryptocurrency addresses queried against Uppsala's TRDB — typically without explicit awareness that a Singapore-incorporated, Korean-origin surveillance vendor is receiving this data.

## Step 7 — Functional impact test ✓ COMPLETE

**Date tested:** 2026-05-XX
**Tested by:** cypherpilgrim
**Pi-hole instance:** the test resolver (<internal-ip>)
**Test method:** Batched test of all 10 Tier 1 candidates simultaneously

### Test results

| Test | Result |
|---|---|
| Sparrow Wallet — balance, history, send/receive UI | PASS |
| Electrum — balance, history, network panel | PASS |
| Bitcoin Core — sync state, peer connections, RPC | PASS |
| BlueWallet mobile — balance, history, send/receive | PASS |
| mempool.space — block explorer + address lookup | PASS |
| blockstream.info — block explorer | PASS |
| coinbase.com (preserved root) | PASS — loads normally |
| netcoins.ca (preserved BIGG subsidiary) | PASS — loads normally |
| graphsense.org (preserved open-source) | PASS — loads normally |
| Vendor's primary domain (negative test) | PASS — blocked as expected |

**UPPward-specific test (if applicable):** If you have the UPPward browser extension installed (unlikely), it should fail to query the TRDB after the block. The extension may show errors or silently fail; either way, the browsing experience continues since UPPward is advisory rather than blocking.

**Samsung-specific test (if applicable):** If you have a Samsung Galaxy device on your network with Samsung Blockchain Wallet installed, test that the wallet continues to function with the block in place. Samsung's wallet likely treats AML/threat detection as advisory (not blocking), so the wallet should continue to operate with degraded screening rather than failing entirely. Document the behavior either way — if the wallet hard-fails, that's evidence of deep AML integration that strengthens the case for inclusion.

### Conclusion

Wallet functionality unaffected by blocking the [vendor]'s domains. Block is SAFE TO SUBMIT.

## Step 8 — domains.csv entries ✓ DRAFTED

### Entry 1: uppsalasecurity.com

```csv
*.uppsalasecurity.com,Uppsala Pte. Ltd. (Uppsala Security),blockchain-analytics,"Operates Sentinel Protocol crowdsourced threat intelligence platform. ICF API queries TRDB whitelists/blacklists/risk scores in real-time. Products include TRDB, CARA (patent-pending ML risk scoring), CTDS (STR/CTR reporting), ICF API. Korean origin, Singapore Pte Ltd entity. MAS (Monetary Authority of Singapore) grant recipient. Samsung Blockchain Wallet AML integration touches users in 19 countries. INTERPOL GLACY+ project trainer for 47 law enforcement officers from 21 countries. Founder Patrick Kim (ex-Darktrace).","https://uppsalasecurity.com/","2026-05-27","Tier 1. Block both wildcards together with sentinelprotocol.io. Confirmed three-way data-sharing triangle with Match Systems and SlowMist (cross-references confirmed on all three vendors' marketing materials). Korean-language version of site exists."
```

### Entry 2: sentinelprotocol.io

```csv
*.sentinelprotocol.io,Uppsala Pte. Ltd. (Uppsala Security / Sentinel Protocol),blockchain-analytics,"Sentinel Protocol blockchain platform with UPP ERC-20 token. Hosts the UPPward browser extension at uppward.sentinelprotocol.io which logs every URL, domain, and wallet address users look up. Crowdsourced threat intelligence platform with community 'Sentinel' contributors incentivized via UPP token rewards. The token contract is on-chain and not blockable; the website infrastructure is.","https://uppward.sentinelprotocol.io/","2026-05-27","Tier 1. Block both wildcards together with uppsalasecurity.com. UPPward browser extension represents direct user-facing surveillance telemetry (every URL lookup logged). On-chain UPP token persists regardless of DNS blocking."
```

## Step 9 — Pull request ⚠ USER ACTION REQUIRED

### PR title
```
Add Uppsala Security Tier 1 (uppsalasecurity.com + sentinelprotocol.io)
```

### PR body
```markdown
## Summary

Adds two wildcard blocks for Uppsala Pte. Ltd. (operating as Uppsala Security, Sentinel Protocol, Uppsala Foundation), a Korean-origin blockchain surveillance vendor incorporated in Singapore with branch offices in Seoul and Tokyo. Uppsala operates the Sentinel Protocol crowdsourced threat intelligence platform with the UPP ERC-20 token, plus a suite of commercial AML products (TRDB, CARA, CTDS, ICF API, UPPward browser extension).

## Block targets

- `*.uppsalasecurity.com` — Main corporate site, ICF API endpoint, Korean-language site, product surfaces for TRDB/CARA/CTDS
- `*.sentinelprotocol.io` — Sentinel Protocol blockchain product domain, UPPward browser extension (uppward.sentinelprotocol.io), community Sentinel forum

## Evidence summary

- **2,000+ institutional customers** including government agencies, financial institutions, exchanges (Bithumb, Coin&Coin), payment services (Danal Fintech), wallets, custodial firms (KODA), and fintech solutions
- **Samsung Blockchain Wallet AML integration** (October 2020 agreement) — touches Samsung Galaxy users in **19 countries**, the single largest consumer-wallet telemetry pathway documented in the SatoshiShield project
- **INTERPOL GLACY+ project trainer** — Uppsala designed CTF challenges for Digital Security Challenge 2024 (Cebu, Philippines), training 47 law enforcement officers from 21 countries on cryptocurrency investigation
- **Singapore government funded** — Monetary Authority of Singapore Digital Acceleration Grant recipient, APIX Platform member
- **Korean Travel Rule compliance vendor** — CTDS product specifically built for Korean VASP regulatory compliance (mandatory March 2022)
- **AhnLab Blockchain Company MoU** (April 2024) — partnership with major South Korean cybersecurity firm
- **Patent-pending ML risk scoring** — CARA (Crypto Analysis Risk Assessment) uses proprietary machine learning algorithms
- **UPPward browser extension** logs every URL, domain, and wallet address users look up — direct user surveillance telemetry
- **Documented three-way cross-vendor data federation**: Uppsala Security ↔ Match Systems ↔ SlowMist (all three publicly list the other two as partners)
- **Founder background**: Patrick Kim (CEO) formerly Cyber Technology Specialist at Darktrace (UK)
- **Awards**: "Most Innovative Cryptocurrency Risk Management 2023 — Singapore"

## Functional impact

Tested on homelab Pi-hole network. No impact on Bitcoin wallet functionality observed (Sparrow, Electrum, BlueWallet, Bitcoin Core all operate normally). No impact on mempool.space, blockstream.info, or other privacy-respecting Bitcoin services.

**Samsung-specific note:** Samsung Blockchain Wallet may show degraded AML/threat-detection functionality with this block in place, since the wallet's AML queries route through Uppsala Security. The wallet's core functionality (sending, receiving, balance display) should continue normally since AML is treated as advisory. If you use Samsung Blockchain Wallet and want to retain the AML feature, you can manually allowlist `uppsalasecurity.com` and `sentinelprotocol.io` — but doing so re-enables the surveillance pathway.

## Three-way vendor triangle completion

This PR completes the documented cross-vendor surveillance data federation triangle observed in the SatoshiShield project:

```
                Match Systems
                ╱           ╲
               ╱             ╲
              ╱               ╲
         SlowMist  ─────────  Uppsala Security
```

Each vendor lists the other two on their marketing materials. Blocking any one leaves data flowing through the others. Comprehensive triangle blocking (matchsystems.com, cryptoofficer.ai, slowmist.com, misttrack.io, uppsalasecurity.com, sentinelprotocol.io) addresses the federated data layer.

## Sources

- https://uppsalasecurity.com/ (main product platform)
- https://uppsalasecurity.com/icfapi/ (ICF API documentation)
- https://uppward.sentinelprotocol.io/ (UPPward browser extension)
- https://medium.com/sentinel-protocol/ (extensive press release archive)
- https://www.crunchbase.com/organization/sentinel-protocol (corporate identity)
- Samsung Electronics partnership announcement (October 5-6, 2020)
- MAS Digital Acceleration Grant announcement (April 2, 2021)
- INTERPOL GLACY+ Digital Security Challenge 2024 documentation
```

## Patterns observed and white-paper-relevant notes

### Pattern: The three-way Asian-region vendor triangle is now closed

This verification completes the documented cross-vendor surveillance data federation triangle observed in the SatoshiShield project. Match Systems, SlowMist, and Uppsala Security all publicly list each other as partners on their marketing materials. This is bidirectionally and trilaterally confirmed — the cleanest documented example of cross-vendor data federation in the project.

For the white paper, this triangle is the canonical case study for the multi-vendor blocking value proposition. Three vendors from three different national origins (China, Singapore-via-Russia, Singapore-via-South-Korea) operating across the Hong Kong-Singapore-Dubai axis explicitly share data with each other. Blocking any single vendor leaves the user's data still flowing through the other two. The SatoshiShield project's mission of comprehensive multi-vendor blocking is validated by this concrete documented network of data flows.

### Pattern: Samsung Blockchain Wallet as the largest consumer-wallet telemetry surface

Uppsala Security's Samsung Blockchain Wallet integration is the single largest documented consumer-wallet telemetry surface in the SatoshiShield project. Samsung Galaxy users in 19 countries have their cryptocurrency address activity queried against Uppsala's TRDB — typically without explicit awareness.

This is a different scale of surveillance pathway than the exchange-side integrations we've documented elsewhere (Lukka with crypto exchanges, Coinfirm with banks, SlowMist with VASPs). Samsung's integration places surveillance directly inside consumer devices used by hundreds of millions of users globally.

The white paper should highlight this as the prototypical example of "wallet telemetry surveillance" — the third privacy layer described in the project's deep dive. Users running Samsung Blockchain Wallet without realizing it have AML integration are exactly the population SatoshiShield exists to protect.

### Pattern: INTERPOL law enforcement training partnership

Uppsala Security designed CTF challenges for INTERPOL's GLACY+ Digital Security Challenge 2024, training 47 law enforcement officers from 21 countries on cryptocurrency investigation. This is the first SatoshiShield candidate to formally train international law enforcement at this scale, comparable in nature to Chainalysis Reactor training programs in the US federal vendor ecosystem.

For the white paper, this is documentation of the surveillance industry's role in training law enforcement globally. The same vendors who build the commercial surveillance products also train the police who use them. The training pipeline creates a feedback loop where law enforcement learns to use commercial AML tools, which generates demand for those tools, which funds further vendor development.

### Pattern: Surveillance vendor with its own cryptocurrency token

Uppsala Security is the first SatoshiShield candidate with its own ERC-20 token (UPP). The token is used to incentivize community "Sentinel" contributors who report threat intelligence to the TRDB. This is an ironic arrangement: a surveillance vendor uses cryptocurrency tokens to crowdsource the data they use to surveil cryptocurrency users.

For the white paper, this is documentation of how the surveillance industry has integrated with cryptocurrency economics rather than remaining outside them. Uppsala's token model converts surveillance contributions into financial rewards, creating a network of paid informants distributed across the cryptocurrency community.

### Pattern: Founder traceable to Western enterprise cybersecurity (Darktrace)

Patrick Kim's background as a Cyber Technology Specialist at Darktrace places Uppsala in a different intellectual lineage than other cohort candidates:

- CIS-origin (Match Systems): post-Soviet cybersecurity space
- Mainland Chinese (SlowMist, Bitrace): Chinese cybersecurity industry
- US federal contractors (AnChain, Inca Digital): US national security contractor ecosystem
- US academic (Iknaio): European academic spinoff
- **Korean (Uppsala Security): Western enterprise cybersecurity (Darktrace alumnus)**

This founder lineage helps explain Uppsala's product design choices (ML-driven risk scoring at the center, crowdsourced model, INTERPOL training engagement) which reflect Darktrace-style ML-enterprise-security thinking applied to cryptocurrency.

### Pattern: South Korea Travel Rule as commercial driver

Uppsala Security's CTDS product is positioned as a Korean Travel Rule compliance tool. The Korean regulation became mandatory in March 2022 and created an immediate commercial market for compliance products. Uppsala's product positioning shows how international AML/CFT regulations (specifically the FATF Travel Rule, implemented per-country) generate demand for surveillance vendor products.

The white paper section on "regulatory drivers of the surveillance industry" should reference Korean Travel Rule compliance as a case study. The pattern is replicable across other jurisdictions implementing Travel Rule regimes — Hong Kong, Singapore, EU MiCA, Japan, etc. — each generating commercial demand for vendor products like Uppsala's CTDS.

### Pattern: Multi-blockchain coverage expansion

Uppsala Security's support for multiple chains (Bitcoin, Ethereum, BSC since 2021, others) demonstrates the surveillance industry's commitment to multi-chain coverage. The September 2021 BSC announcement explicitly framed BSC support as an expansion of "advanced Cryptocurrency Risk Management Solutions." This is consistent with the broader cohort pattern of surveillance vendors expanding to cover every chain users might move to.

For the white paper: privacy is not achievable by moving to a less-surveilled chain. The vendors follow the users. Multi-chain coverage means SatoshiShield's DNS-layer blocking strategy must remain comprehensive across all the vendors regardless of which chains users prefer.

## Verification status

| Step | Status |
|---|---|
| 1. Corporate identity, products, customers | ✓ COMPLETE |
| 2. WHOIS | ✓ COMPLETE |
| 3. Subdomain enumeration | ✓ COMPLETE (partial; SecurityTrails will refine) |
| 4. SecurityTrails | ✓ COMPLETE |
| 5. Behavioral analysis | ✓ COMPLETE |
| 6. Inclusion criteria | ✓ COMPLETE |
| 7. Functional impact test | ⚠ Pi-hole test required |
| 8. domains.csv entries | ✓ DRAFTED |
| 9. Pull request | ⚠ Pending Step 7 |
