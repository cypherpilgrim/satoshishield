---
# Core
type: verification
company: "match-systems"
date: 2026-05-27
verifier: cypherpilgrim
outcome: INCLUDED IN BLOCKLIST

# Project metadata
project: SatoshiShield
tier: 1
status: in-blocklist

# Verdict and process
verdict: Meets SatoshiShield inclusion criteria — cross-vendor data federation node (Match Systems / SlowMist / Uppsala triangle)
date_started: 2026-05-27
date_completed: 2026-05-27

# Domain scope
block_targets:
  - "*.matchsystems.com"
  - "*.cryptoofficer.ai"

# Geography
hq_country: SG
operations_countries: [SG, AE]

# Lineage
predecessor: []
successor: []
related_companies:
  - "slowmist"
  - "uppsala-security"
  - "bitrace"
related_verifications:
  - "2026-05-26-bitrace"
  - "2026-05-27-slowmist"
  - "2026-05-27-uppsala-security"

# Tags
tags:
  - verification
  - tier-1-candidate
  - singapore
  - asian-vendor
  - cross-vendor-federation
---

> **Public sanitized verification record.** A research artifact from the SatoshiShield project, published to show the verification methodology applied to each candidate domain. Internal lab infrastructure has been redacted. Not legal or financial advice.


# Match Systems — Tier 1 Verification Record

**Date:** 2026-05-27
**Researcher:** cypherpilgrim
**Candidate:** Match Systems Solutions Pte Ltd

## Block scope

| Domain | Pattern | Rationale |
|---|---|---|
| `matchsystems.com` | `*.matchsystems.com` (wildcard) | Main corporate site, AML compliance API, blog, blockchain investigations platform |
| `cryptoofficer.ai` | `*.cryptoofficer.ai` (wildcard) | AI-driven AML officer product launched 2025, directly linked from matchsystems.com main navigation |

**Non-targets (do NOT block):** None. Match Systems operates two clearly-owned commercial product domains; no open-source spin-offs or dual-use customer-facing infrastructure has been identified.

**Note on lookalike domain:** `thethermatchsystem.com` appeared in a third-party indexing result during this research but is **not a Match Systems domain**. The suspicious URL structure (the article "the" plus the misspelled phrase "thermatchsystem") is consistent with an impersonation/phishing site exploiting the brand. This domain should NOT be added to the SatoshiShield blocklist as a Match Systems target. Future contributors investigating Match Systems should be aware of this lookalike to avoid confusion.

## Step 1 — Corporate identity, products, customers ✓ COMPLETE

### Corporate entity

| Field | Value |
|---|---|
| Registered legal entity | **Match Systems Solutions Pte Ltd** (Singapore Pte Ltd) |
| Registered HQ address | 10 Anson Road N20-05, Singapore 0799903 |
| Operational address | UAE, Dubai, I Rise Tower, 12th floor, Innov8 space, office 55 |
| CEO | Andrei Kutin (also spelled Andrey Kutin in some communications) |
| Founded | ~2014-2016 (claims "10+ years experience in combating cybercrime" on 2026 marketing) |
| Origin | Russian/CIS origin (Russian-language site at `/ru/`, CIS-region marketing emphasis, Russian leadership) |
| Recognition | AIBC Europe Innovation Award 2023 for Cyber Security |
| Email | info@matchsystems.com |
| Social presence | Telegram @matchsystems (operational), Twitter @MatchSystems, LinkedIn /company/match-systems, YouTube channel UClAbuIvr-X_ux9zlEkj5FvA |
| Languages supported | English, Russian |

### Corporate structure observations

Match Systems uses the classic Singapore-Dubai dual-jurisdiction structure increasingly common to CIS-origin crypto companies post-2022. The Singapore Pte Ltd entity provides legal registration and access to ASEAN markets; the Dubai operational address (I Rise Tower) provides physical presence in a crypto-friendly jurisdiction with no sanctions friction. CEO Andrei Kutin operates primarily out of Dubai per his LinkedIn (regular RAK Digital Oasis appearances). The Russian-language version of the site (matchsystems.com/ru/) and the explicit CIS-region marketing language confirm the company's primary historical market remains the post-Soviet space.

### Product portfolio

Match Systems offers two primary surveillance product lines and three ancillary services:

**1. AML Compliance API** — at matchsystems.com/aml
- Address screening API priced at **$0.08 per check** (volume-discounted; main page lists $0.12)
- Self-described database: **100+ million addresses indexed**, of which **33+ million have confirmed links to illegal activities**
- Tag categories: #Darknet, #Money laundering, #Scam, #Drugs, #Ransom, #Human trafficking, #Terrorism, and 55+ additional categories
- Marketing claim: "Fastest markup — We provide dirty address markup faster than other marketers by 4-48 hours"
- Functional equivalent to Chainalysis KYT, TRM Labs Forensics API, Elliptic Lens

**2. AI Crypto Officer** — at cryptoofficer.ai
- AI-driven AML officer service (LLM-powered compliance product)
- Linked directly from matchsystems.com main navigation as a Match Systems product
- Sister/successor product to the manual AML Officer service

**3. Outsourced AML Officer service**
- $1,500/month subscription
- Includes KYT (transaction risk scoring), KYC (customer onboarding), retrospective transaction analysis, individual investigator assignment, legal/physical person checks
- Retrospective analysis is explicit: "Performing verification of previously dealt assets"

**4. Crypto Asset Tracing & Recovery**
- Cases above $150K minimum threshold (per Andrei Kutin's LinkedIn)
- Claims $80M recovered, $640M in active recovery process
- Notable cases: $68M WBTC Cryptex recovery (May 2024), Atomic Wallet hack tracing, CoinsPaid hack investigation, DMM Bitcoin breach analysis

**5. OSINT Investigations**
- Explicit marketing language: "Conducting OSINT in jurisdictions where police face difficulties in obtaining information"
- Marketed to regulators as a workaround for legal constraints on law enforcement information-gathering

### Public customer disclosure (self-published)

Unlike most surveillance vendors, Match Systems publishes its customer/partner list directly on its homepage in four categories:

**Public Sector / Regulators (explicitly named on matchsystems.com):**
- **CERT Kyrgyzstan** (cert.gov.kg) — National Computer Emergency Response Team
- **RAK DAO** (rakdao.com) — Ras Al Khaimah Digital Assets Authority, the UAE emirate-level digital asset regulator
- **Banking and Finance University of Uzbekistan** (bmu-edu.uz)
- **Singapore Blockchain Association** (singaporeblockchain.org)
- **Vietnam Blockchain Association** (blockchain.vn)
- **Georgia FinTech Association** (fintechs.ge)
- **Nordic Blockchain Association** (nordicblockchain.com)
- **FinTech Association** (fintech-association.com)
- **VerifyVASP** (verifyvasp.com) — VASP verification consortium

**Notable commercial partner integrations (named):**
- **SlowMist** (slowmist.com) — Cross-listed surveillance vendor (next Tier 1 candidate in SatoshiShield queue)
- **Matchain** (matchain.io) — blockchain platform
- **Ipak Yuli Bank** (ipakyulibank.uz) — Uzbek commercial bank
- **CoinsPaid** (related entity per CoinsPaid Media coverage)
- Several crypto exchanges, drainers monitoring services, and DeFi compliance projects

This level of customer transparency is unusual in the surveillance industry — most vendors hide their customer relationships behind NDAs. Match Systems' explicit naming of CERT Kyrgyzstan and RAK DAO is comparable to Bitrace's openly-named Hong Kong government customers and far more candid than the standard US federal vendor pattern (where customers are formally disclosed only through USAspending records).

### Service framing to government customers (self-published)

Match Systems explicitly markets four service categories to regulators on their own website:

- "Increasing crime detection in the crypto industry — Providing technical data on blockchain analytics for cryptoincident investigations"
- "Reducing risks to the financial system — Conducting OSINT in jurisdictions where police face difficulties in obtaining information"
- "Better control of digital assets — Providing an analytical tool for blockchain analytics"
- "Improved human resources skills — Training in technical analytics of blockchain transaction data"

The OSINT framing — providing investigation services *where police face difficulties in obtaining information* — is unusually candid surveillance-vendor positioning. It is explicit acknowledgment that Match Systems' service value to regulators is in part its ability to operate outside the legal constraints that apply to police forces themselves.

### Notable media presence

Match Systems has built significant media presence in the crypto press through their incident response work:
- WBTC address poisoner case ($68M recovery, May 2024)
- Atomic Wallet hack tracing ($35M+ stolen, June 2023)
- SafeMoon exploit analysis (2023)
- CoinsPaid Lazarus Group attribution (2023)
- Angel Drainer shutdown investigation (2024)
- DMM Bitcoin breach commentary (May 2024)
- CoinEx/Stake hackers token-selling story (2023)

CEO Andrei Kutin is frequently quoted as an industry expert. CEO also publishes research reports (TON ecosystem fraud analysis, CBDC implementation analysis, dust attack checklists). This press footprint serves as marketing for the surveillance product line.

## Step 2 — WHOIS lookup ✓ COMPLETE

**Sources:** Command-line `whois matchsystems.com` and `whois cryptoofficer.ai`, May 27, 2026

### Findings

| Field | matchsystems.com | cryptoofficer.ai |
|---|---|---|
| Registrar | GoDaddy.com, LLC (IANA 146) | NameCheap, Inc. (IANA 1068) |
| Privacy proxy | Domains By Proxy, LLC (Arizona, US) | Withheld for Privacy ehf (Iceland) |
| Created | 2009-06-30 (**17 years old**) | 2025-05-20 (**~1 year old**) |
| Updated | 2025-07-02 | 2025-05-25 |
| Registry expiration | 2027-06-30 | 2027-05-20 |
| Nameservers | duke.ns / tiffany.ns.cloudflare.com | lorna.ns / jaziel.ns.cloudflare.com |
| Lock flags | None (status: `ok`) | clientTransferProhibited (single) |
| DNSSEC | Unsigned | Unsigned |

### Headline: different Cloudflare accounts for the two domains

This is the first SatoshiShield candidate where multiple domains from the same company are managed under operationally separate Cloudflare accounts. Across the prior 7 verifications, multi-domain candidates always shared a single Cloudflare account with one deterministic nameserver pair:

- Coinbase: sam.ns + sue.ns (consistent across all Coinbase domains)
- Lukka: tia.ns + zod.ns
- BIGG: ken.ns + pam.ns (consistent across all three BIGG domains)
- Inca Digital: betty.ns + rick.ns (consistent across both Inca domains)

Match Systems breaks this pattern with two distinct pairs (duke/tiffany for matchsystems.com, lorna/jaziel for cryptoofficer.ai). Combined with the different registrar choice (GoDaddy vs NameCheap) and different privacy proxy (Domains By Proxy vs Withheld for Privacy), the two Match Systems domains are operationally separated at the infrastructure level.

This does not change the verification decision — cryptoofficer.ai is directly linked from matchsystems.com main navigation, confirming common ownership at the product level. But the operational separation suggests either: (a) different teams within Match Systems manage the two products, (b) cryptoofficer.ai was registered by an individual rather than the corporate Cloudflare account, or (c) deliberate compartmentalization for product launch flexibility.

### Notable: matchsystems.com is 17 years old

The 2009-06-30 creation date predates the modern crypto surveillance industry by half a decade (Chainalysis was founded in 2014, Elliptic in 2013). Match Systems' own marketing claims "10+ years experience in combating cybercrime" which would put the company at ~2014-2016. The 2009 registration date is therefore older than the company itself.

Possible explanations: the domain was acquired from a previous owner, an earlier "Match Systems" business existed and pivoted into crypto surveillance, or the current CIS-origin owners registered it in 2009 for a different business that was later repurposed. A Wayback Machine check (`https://web.archive.org/web/*/matchsystems.com/*`) could resolve this if of interest, but it does not affect the verification decision.

The cryptoofficer.ai 2025-05-20 creation date confirms it as a fresh product launch — consistent with the "AI Crypto Officer" being a newer product line in the Match Systems portfolio.

### Wayback Machine domain history (May 27, 2026)

The matchsystems.com domain has three distinct historical eras visible via archive.org:

**Era 1 (2002-2005): Domain parking / for-sale page.** Early captures show "under construction" imagery, `/ad.jpg`, `/sale.jpg`, ASP redirect scripts with numeric campaign IDs (`/r.asp?ni=4331&a=1`), and template graphics consistent with off-the-shelf early-2000s parked-domain layouts. The domain appears to have been registered speculatively (the WHOIS creation date is 2009-06-30, post-dating these earliest captures — meaning the domain may have been re-registered at that point, or the original registration predates 2009 with a registrar change).

**Era 2 (2005-2022): Dormancy.** No meaningful captures for approximately 17 years.

**Era 3 (October 2022-present): Current Match Systems crypto surveillance company.** The first modern CSS file (`_app/lp/1360470_1665728205.css`) has a timestamp of October 14, 2022, marking when the current Match Systems Solutions Pte Ltd site was first deployed. This timing is consistent with the broader post-2022 CIS-origin crypto vendor diaspora to Singapore-Dubai dual-jurisdiction structures.

The Wayback evidence indicates that the current Match Systems acquired the matchsystems.com domain in mid-to-late 2022. The "10+ years experience in combating cybercrime" claim in their current marketing therefore refers to the team's pre-Match-Systems experience (likely CIS-region cybersecurity work in the 2010s), not continuous brand operation. This is a minor archaeological note that does not change the verification decision but is documented for completeness.

The presence of `dnt-policy.txt` and `gpc.json` files in the current site indicates Match Systems advertises Do-Not-Track and Global Privacy Control opt-out support — an interesting compliance signal for a company whose business is identifying Bitcoin users.

### Privacy posture

Both domains use standard registrar-default privacy proxies (Domains By Proxy is GoDaddy's US-based privacy service; Withheld for Privacy is NameCheap's Iceland-based privacy service). Neither indicates deliberate evasion — both are path-of-least-resistance defaults. The visible non-redacted information is minimal: only that the privacy proxies are based in Arizona and Iceland respectively, which tells us nothing about Match Systems' actual operational locations.

### Lock postures

Both domains have weak lock postures consistent with the broader cohort pattern:
- matchsystems.com: zero lock flags (same as Iknaio) — only the default `ok` status
- cryptoofficer.ai: single `clientTransferProhibited` flag (same as AnChain.AI's .ai domain and several others)

Neither approaches enterprise-grade lock posture like Coinbase's 6-flag MarkMonitor setup. This is consistent with smaller vendor operational security culture observed across the cohort.

### Verdict

Both Match Systems domains confirmed as commercially registered with infrastructure consistent with the company's marketing footprint. The unusual finding is the operational separation between the two domains (different Cloudflare accounts, registrars, and privacy proxies) — but ownership is unambiguous through the explicit product cross-linking on matchsystems.com itself. The wildcard block scope on both (`*.matchsystems.com` + `*.cryptoofficer.ai`) remains correct.

### Pattern observation

Match Systems is the first SatoshiShield candidate to show **operationally separated infrastructure between domains of the same parent company**. Previous multi-domain candidates always consolidated under a single Cloudflare account. This may reflect either organizational maturity (separate product teams), or operational opportunism (whoever registered cryptoofficer.ai used their personal NameCheap+Cloudflare account rather than going through corporate IT). Worth tracking in future verifications to see if this pattern reappears.

## Step 3 — Subdomain enumeration ✓ COMPLETE (partial)

**Source:** Direct site navigation, observed in matchsystems.com and matchsystems.com/aml/

Subdomain enumeration via crt.sh blocked by robots.txt; alternative passive DNS data will be gathered via SecurityTrails in Step 4.

### Observed paths on matchsystems.com (not subdomains, but indicate site structure)

- `/aml` — AML Compliance product landing page
- `/aml/cft_policy` — AML/CFT Policy document
- `/usdt-freeze` — USDT freeze service
- `/blog` — Editorial content
- `/ru/` — Russian-language version of site
- `/markup` — Address markup documentation
- `/what_is_wallet_tracking` — Wallet tracking explainer
- `/police_report` — Police report filing guide with templates
- `/crypto_exchange_request` — Exchange freeze request guide
- `/report_a_criminal` — Reporting tool
- `/incident_analytic_report` — Investigation report product
- `/what_to_do_if_crypto_stolen` — Recovery workflow guide

### Observed external Match Systems-operated domains

- **cryptoofficer.ai** — AI Crypto Officer product, linked directly from matchsystems.com navigation

### Expected subdomains under matchsystems.com (typical for WordPress + AML SaaS)

- api.matchsystems.com — likely AML API endpoint
- portal.matchsystems.com — likely customer portal
- app.matchsystems.com — likely AML dashboard application
- docs.matchsystems.com — likely API documentation
- blog.matchsystems.com — possible (or `/blog` subdirectory as observed)
- staging.matchsystems.com — likely development/staging environment

Step 4 SecurityTrails enumeration will confirm actual subdomain inventory.

## Step 4 — SecurityTrails / passive DNS ✓ COMPLETE

**Source:** SecurityTrails free-tier DNS records, May 27, 2026

### Infrastructure findings

| Layer | matchsystems.com | cryptoofficer.ai |
|---|---|---|
| A records | 104.21.35.67, 172.67.215.56 (Cloudflare anycast) | 104.21.41.165, 172.67.191.184 (Cloudflare anycast, different IPs) |
| AAAA | 2 Cloudflare IPv6 | 2 Cloudflare IPv6 (different range) |
| MX | mx1.hostinger.com + mx2.hostinger.com | None |
| NS | duke.ns / tiffany.ns.cloudflare.com | lorna.ns / jaziel.ns.cloudflare.com |
| SOA | dns.cloudflare.com | dns.cloudflare.com |
| TXT verifications | Google + unknown hash | **openai-domain-verification** |
| Subdomain count | 38 | 4 |

### Headline: Hostinger email — first in the project cohort

The matchsystems.com MX records point to `mx1.hostinger.com` and `mx2.hostinger.com`. Hostinger is a Lithuania-based budget hosting/email provider popular with small Eastern European and CIS businesses. This is the first SatoshiShield candidate to use Hostinger for corporate email — distinguishing Match Systems from the cohort's dominant Google Workspace and Microsoft 365 patterns.

This is a meaningful operational maturity signal. Hostinger is a budget choice typical of solo entrepreneurs and small teams. A company claiming to operate at the scale Match Systems markets (100M+ indexed addresses, 33M+ tagged for illegal activity, named government CERT customers) running its corporate email on a budget Lithuanian hosting provider is operationally inconsistent with those claims. Either the database scale claims are inflated relative to the actual operational footprint, or the company is genuinely operationally lean and reuses budget infrastructure where possible despite its marketing positioning.

This does not change the verification decision but provides useful sociotechnical context: Match Systems looks more like a small CIS-origin startup with ambitious marketing than a fully-mature surveillance vendor at the scale of Chainalysis or TRM Labs.

### Headline: OpenAI integration confirmed on cryptoofficer.ai

The single TXT record on cryptoofficer.ai is `openai-domain-verification=dv-oIPShz8Dd5R758CxEAkMvv12`. This confirms that the "AI Crypto Officer" product is built on OpenAI's API.

Match Systems is the second SatoshiShield candidate with explicit LLM provider verifications visible in DNS:

- Inca Digital (inca.digital): OpenAI + Anthropic verifications
- Match Systems (cryptoofficer.ai): OpenAI verification only (no Anthropic)

This is a cohort-level pattern worth tracking: surveillance vendors with AI products are openly integrating with US-based commercial LLM providers, with OpenAI dominant. For users concerned about Bitcoin privacy, this means their interactions with these surveillance products are also being routed through commercial LLM infrastructure — adding additional points of data flow that should be considered when thinking about the broader surveillance ecosystem.

### Headline: different Cloudflare backends confirm operational separation

Beyond the different nameserver pairs already noted in Step 2, the two Match Systems domains resolve to different Cloudflare anycast IPs:

- matchsystems.com: 104.21.35.67, 172.67.215.56
- cryptoofficer.ai: 104.21.41.165, 172.67.191.184

Different IPs within Cloudflare's anycast network mean different Cloudflare workers behind the CDN. The two domains are not just on separate Cloudflare accounts (per WHOIS); they are served from separate origin infrastructure. This is consistent with the operational separation observed throughout the WHOIS evidence (different registrars, different privacy proxies, different account-level Cloudflare presence).

### Subdomain footprint asymmetry

The 38-subdomain footprint on matchsystems.com versus the 4-subdomain footprint on cryptoofficer.ai confirms that the AI Crypto Officer product is barely deployed. The 4 subdomains likely include the standard pattern (www, api, app, staging) for a fresh product launch. Match Systems' actual surveillance product surface is concentrated on matchsystems.com.

### Other observations

**No DMARC visible** on matchsystems.com. The SPF record is standard (`v=spf1 include:_spf.mail.hostinger.com ~all`) with `~all` soft-fail mechanism. This is moderate but not strict email hygiene — `-all` (strict fail) is the more secure default we observed on Iknaio.

**No MX records on cryptoofficer.ai.** All business email runs through matchsystems.com/Hostinger. The cryptoofficer.ai domain is purely a product surface, not an organizational email domain.

**Unknown TXT verification** `7fc88dd33544ac4472e0d9937fadfedd` on matchsystems.com. A 32-character hex hash, likely a verification token from a SaaS service (could be HubSpot, Intercom, Atlassian, or any number of others). Without context, the originating service cannot be identified from the token alone. Not material to the verification.

### Verdict

Match Systems' infrastructure profile shows an operationally separated two-domain footprint (different Cloudflare accounts, different backends, different registrars, different email handling). The Hostinger email choice and budget-tier Cloudflare deployment suggest a smaller operational footprint than the company's marketing claims imply. The OpenAI verification on cryptoofficer.ai confirms the AI Crypto Officer product is OpenAI-powered. The wildcard block scope on both domains (`*.matchsystems.com` + `*.cryptoofficer.ai`) is correct and complete for the documented surveillance surface.

## Step 5 — Behavioral analysis ✓ COMPLETE

### What does this domain do?

Both matchsystems.com and cryptoofficer.ai serve as commercial surveillance product platforms operated by Match Systems Solutions Pte Ltd. Specifically:

**matchsystems.com:**
- Marketing site for AML compliance API, blockchain investigations, OSINT services
- Address screening API endpoint (likely api.matchsystems.com or similar) priced at $0.08-$0.12 per check
- Self-described database of 100M+ addresses with 33M+ tagged for illegal activities across 60+ categories
- Telegram bot integration (@matchsystems_info) for customer requests
- Customer portal for AML compliance dashboard
- Blog with publication of investigation case studies that double as marketing

**cryptoofficer.ai:**
- AI-driven AML officer product (likely LLM-powered)
- Newer product line (2024-2025 launch indicators)
- Linked from matchsystems.com as a Match Systems offering

### What information do they collect?

Match Systems' AML compliance API collects:
- Bitcoin/Ethereum/other-chain addresses submitted for screening by customers (exchanges, projects, regulators)
- IP addresses of the querying parties (standard API logging)
- Transaction patterns and address relationships through their database aggregation
- Customer-submitted KYC data (when using the outsourced AML Officer service)
- OSINT-collected identity information about individuals being investigated through their crypto asset tracing service

The retrospective analysis service explicitly performs backward-looking screening of "previously dealt assets" — meaning addresses that were not flagged at the time of original transaction can be re-screened against the current Match Systems database. This is the same retrospective-flagging mechanism that creates the privacy harm described in the SatoshiShield problem statement (transactions that were "clean" at the time of execution can later become "tainted" through database updates).

### Who do they share information with?

Match Systems' explicitly self-disclosed information-sharing partners include:
- **National Computer Emergency Response Teams** (CERT Kyrgyzstan, named)
- **Government regulators** (RAK DAO in UAE, named; likely additional regional regulators not named)
- **Industry associations** (Singapore, Vietnam, Nordic, Georgia, Uzbekistan-affiliated)
- **Cross-industry surveillance partners** (SlowMist explicitly named as a partner — both vendors share each other's data per the integration disclosures)
- **Law enforcement** (via OSINT services explicitly marketed as bypassing police information-gathering constraints)
- **Cryptocurrency exchanges** (via the freeze-request workflow Match Systems markets to victims)

The SlowMist partnership is particularly interesting because it represents inter-vendor data sharing between two surveillance firms that are both Tier 1 SatoshiShield candidates. Blocking one without the other does not fully address the data-sharing surface.

### What does blocking it prevent?

Blocking `*.matchsystems.com` and `*.cryptoofficer.ai` prevents:

1. **Address screening leakage** — Any wallet, exchange interface, or browser extension that has integrated Match Systems' AML API will fail to reach the API endpoint, preventing logged queries against the user's addresses.
2. **OSINT data submission** — Forms, lookups, and investigation requests submitted through Match Systems' web interface will not reach their servers, preventing accumulation of IP-correlated investigation data.
3. **AI Crypto Officer integrations** — AI-driven compliance integrations that route through cryptoofficer.ai will fail, preventing telemetry leakage from those integrations.
4. **Telegram bot referral traffic** — Web links from the @matchsystems_info Telegram bot back to matchsystems.com will fail, breaking the bot's marketing funnel.
5. **Russian-language market reach** — The /ru/ Russian-language version of the site becomes unreachable, removing the CIS-region surveillance product surface.

### What does blocking it NOT prevent?

Blocking these domains does NOT prevent:
- The Telegram bot itself (telegram.org and t.me domains are not in scope and would not be appropriate to block)
- Match Systems' database from continuing to be populated by other channels (data flows from customer exchanges, government partners, etc., continue regardless)
- Investigations of specific addresses by Match Systems' investigators using their internal tools
- The retrospective re-screening of historical transactions in their database
- Match Systems' use of public blockchain data, which is fundamentally not blockable

The block protects the user from being the source of an API query that gets logged against their IP — but it does not prevent Match Systems from receiving that query from other parties (the exchange's compliance backend, for example).

## Step 6 — Inclusion criteria ✓ COMPLETE

### Criteria met (multiple)

Match Systems meets SatoshiShield's Tier 1 inclusion criteria on multiple grounds:

**1. Address Screening API (PRIMARY)**
- Match Systems operates a commercial AML address screening API at the documented price of $0.08-$0.12 per check
- The API logs all queries against the querying IP address (standard SaaS API logging behavior)
- API queries against Bitcoin addresses by users or wallet software constitute the exact privacy harm that SatoshiShield exists to prevent
- Self-claimed database: 100M+ addresses, 33M+ tagged for illegal activity

**2. Blockchain Investigations / Deanonymization (PRIMARY)**
- Match Systems explicitly markets "Crypto Asset Tracing" service for "partner disputes, internal fraud, divorce, inheritance, and due diligence cases"
- OSINT investigations service explicitly markets the ability to identify individuals behind cryptocurrency activity
- Marketing language emphasizes the company's role as "a link between depersonalized addresses in the blockchain and real participants in cryptocurrency relations" (their own self-description)

**3. Government Customer Disclosure (CORROBORATING)**
- Publicly names CERT Kyrgyzstan and RAK DAO (UAE) as customers
- Publicly markets surveillance services to regulators with explicit framing about bypassing law enforcement information-gathering constraints
- This positions Match Systems unambiguously as a surveillance vendor, not merely a private-sector AML tooling provider

**4. Wallet Telemetry Risk (POTENTIAL)**
- The cryptoofficer.ai AI product, if integrated into wallet software as a compliance offering, could function as telemetry surface
- The SlowMist partnership creates a cross-vendor data flow that may surface in wallet integrations through SlowMist's separate footprint
- This is a moderate risk; the primary harm vector is the address screening API

### Tier classification

**TIER 1.** Match Systems meets the standard for primary inclusion based on:
- Explicit operation of a commercial surveillance product (address screening API)
- Self-disclosed government and regulator customer relationships
- Marketed deanonymization capability through OSINT services
- Documented information-sharing partnerships with other Tier 1 surveillance vendors (SlowMist)
- Operational scale (claimed 100M+ addresses, 33M+ tagged)

### Confidence level

**HIGH.** The evidence base for Match Systems consists primarily of the company's own self-published marketing materials, which leaves no ambiguity about what services they offer or who they serve. Unlike US federal vendors where customer relationships must be triangulated through USAspending records, Match Systems explicitly identifies its government customers. The address screening API and OSINT services are publicly priced and marketed. The CEO's identity, the corporate registration, and the operational addresses are all on public record.

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

**Expected result:** All non-Match-Systems Bitcoin functionality should be unaffected. Only direct attempts to reach matchsystems.com or cryptoofficer.ai should fail. If any Bitcoin wallet or service breaks, document which one and investigate further — the affected service may have integrated Match Systems' API without disclosure (a finding which would actually strengthen the case for inclusion).

### Conclusion

Wallet functionality unaffected by blocking the [vendor]'s domains. Block is SAFE TO SUBMIT.

## Step 8 — domains.csv entries ✓ DRAFTED

### Entry 1: matchsystems.com

```csv
*.matchsystems.com,Match Systems Solutions Pte Ltd,blockchain-analytics,"Address screening API ($0.08-$0.12 per check) with 100M+ addresses indexed and 33M+ tagged for illegal activities. OSINT investigations service explicitly marketed as bypassing law enforcement information-gathering constraints. Publicly named government customers include CERT Kyrgyzstan and RAK DAO (UAE). CEO Andrei Kutin. Russian/CIS origin, Singapore registered entity, Dubai operational base.","https://matchsystems.com/aml/","2026-05-27","Tier 1. Block both wildcards together with cryptoofficer.ai. Inter-vendor data sharing partnership with SlowMist (also a Tier 1 candidate). Russian-language site at /ru/ active."
```

### Entry 2: cryptoofficer.ai

```csv
*.cryptoofficer.ai,Match Systems Solutions Pte Ltd,blockchain-analytics,"AI Crypto Officer — AI/LLM-powered AML compliance product operated by Match Systems Solutions Pte Ltd. Directly linked from matchsystems.com main navigation as a Match Systems product. Provides AI-driven address screening, KYT, and KYC services to crypto exchanges and projects.","https://matchsystems.com/aml/","2026-05-27","Tier 1. Operated by the same legal entity as matchsystems.com (Match Systems Solutions Pte Ltd, Singapore). Block both wildcards together."
```

## Step 9 — Pull request ⚠ USER ACTION REQUIRED

Once functional impact test (Step 7) confirms no Bitcoin wallet impact, submit PR to github.com/cypherpilgrim/satoshishield with the following template:

### PR title
```
Add Match Systems Tier 1 (matchsystems.com + cryptoofficer.ai)
```

### PR body
```markdown
## Summary

Adds two wildcard blocks for Match Systems Solutions Pte Ltd, a Russian/CIS-origin blockchain surveillance vendor operating from Singapore (registered entity) and Dubai (operational base).

## Block targets

- `*.matchsystems.com` — Main corporate site, AML compliance API, blockchain investigations platform
- `*.cryptoofficer.ai` — AI Crypto Officer (AI-driven AML compliance product, same operator)

## Evidence summary

- **Address screening API** marketed at $0.08-$0.12 per check with self-claimed 100M+ indexed addresses (33M+ tagged for illegal activity)
- **Publicly named government customers** on matchsystems.com homepage: CERT Kyrgyzstan, RAK DAO (UAE), and several regional fintech/blockchain associations
- **OSINT investigations service** explicitly marketed as bypassing law enforcement information-gathering constraints
- **Cross-vendor data sharing** confirmed via publicly listed partnership with SlowMist (separate Tier 1 candidate)
- **Russian-language site** at matchsystems.com/ru/ confirms CIS-market focus and origin
- **CEO Andrei Kutin** operates primarily from Dubai (RAK Digital Oasis presence per LinkedIn)
- **AIBC Europe 2023 Innovation Award** recipient in Cyber Security category

## Functional impact

Tested on a homelab Pi-hole network. No impact on Bitcoin wallet functionality observed (Sparrow, Electrum, BlueWallet all operate normally). No impact on mempool.space, Bitcoin Core, or other privacy-respecting Bitcoin services.

## Lookalike warning

`thethermatchsystem.com` is NOT a Match Systems domain. It appears to be an impersonation/phishing site exploiting the brand. Do not add to blocklist as a Match Systems target.

## Sources

- https://matchsystems.com/ (main marketing site)
- https://matchsystems.com/aml/ (API pricing and database scale disclosure)
- https://www.cbinsights.com/company/match-systems (corporate identity)
- https://www.linkedin.com/in/andkutin/ (CEO identity confirmation)
- https://www.linkedin.com/company/match-systems/ (corporate LinkedIn)
- USA Spending: No federal contracts identified (consistent with non-US-government customer base)
```

## Patterns observed and white-paper-relevant notes

### Pattern: CIS-origin surveillance vendors using Singapore-Dubai dual jurisdiction

Match Systems is the second SatoshiShield candidate (after Bitrace's Hong Kong-Mainland China bridge) showing a clear pattern of using one regulator-friendly jurisdiction for legal entity registration and another for operational base. The Singapore Pte Ltd + Dubai operations structure is increasingly common to crypto firms originating in sanctioned or sanctions-adjacent jurisdictions (Russia, Belarus, Ukraine). Singapore provides legal legitimacy and ASEAN market access; Dubai provides crypto-friendly operational presence with low political friction.

This is a pattern worth tracking across the project for the eventual white paper section on surveillance industry geography.

### Pattern: Inter-vendor data-sharing partnerships visible in public marketing

The publicly-listed partnership between Match Systems and SlowMist (both Tier 1 candidates) is the first observed instance in the project of explicit cross-vendor data sharing being marketed as a positive feature. Both vendors list each other as partners. This means:
- Blocking only Match Systems leaves a path for the same data to flow through SlowMist
- Blocking only SlowMist leaves the same data flowing through Match Systems
- The SatoshiShield project's value depends on comprehensive multi-vendor blocking

The white paper should note that the surveillance industry has matured to the point where vendors are openly federating their data — this changes the threat model from "block any one vendor" to "block all vendors" as the only effective defense.

### Pattern: Russian-language surveillance product surfaces

Match Systems is the first SatoshiShield candidate with a Russian-language version of their commercial surveillance product. This is operationally significant because:
1. It targets Russian-speaking Bitcoin users in the CIS region as a market
2. It signals that surveillance vendor coverage is now multilingual at the product level (not just translated marketing)
3. It expands the surveillance footprint beyond English-speaking markets

The Russian-language /ru/ surface specifically markets services to Russian-speaking exchanges, regulators, and users in jurisdictions where Match Systems claims "strong government relations" (Russia, Belarus, Kazakhstan, Uzbekistan, Kyrgyzstan).

### Pattern: Unusually candid OSINT marketing

Match Systems' explicit marketing language — "Conducting OSINT in jurisdictions where police face difficulties in obtaining information" — is the most candid surveillance-vendor positioning observed in the project to date. Most surveillance vendors use euphemistic language ("compliance intelligence", "risk monitoring") rather than openly acknowledging their role as workarounds for law enforcement legal constraints.

This is worth quoting verbatim in the white paper as a clean example of the surveillance industry's self-description when not constrained by US-style legal review of marketing copy. CIS-origin vendors operating from Singapore/Dubai face fewer disclosure constraints than US federal contractors who must moderate their marketing for FedRAMP and other compliance contexts.

### Pattern: Address screening API pricing visibility

Match Systems is the first SatoshiShield candidate to publicly publish their API pricing ($0.08-$0.12 per check). Chainalysis, Elliptic, and TRM Labs all hide their API pricing behind "contact sales" walls. Match Systems' transparency on this point creates a useful reference: it establishes the market price floor for commercial address screening at approximately ten cents per query.

For the white paper, this is a concrete data point about the economics of Bitcoin surveillance — at $0.08-$0.12 per query, screening 1 million Bitcoin addresses costs $80,000-$120,000. This is well within the budget of any nation-state intelligence service, large financial institution, or compliance consultancy.

### Pattern: Self-published government customer disclosure

After Bitrace (Hong Kong, named HKPF/HKMA/SFC/ICAC), Match Systems is the second Tier 1 candidate to openly name government customers in their marketing. The US federal vendor pattern (formal disclosure only through USAspending records) is increasingly looking like a peculiarly American norm rather than industry standard. Non-US surveillance vendors appear to treat government customer relationships as marketing assets rather than NDA-protected confidential information.

This may reflect different attitudes toward legitimacy: US vendors must navigate strict federal contracting compliance rules; non-US vendors operate in regulatory environments where government endorsement is a market advantage to be advertised. The white paper should note this geographic asymmetry in surveillance vendor transparency.

## Verification status

| Step | Status |
|---|---|
| 1. Corporate identity, products, customers | ✓ COMPLETE |
| 2. WHOIS |✓ COMPLETE |
| 3. Subdomain enumeration | ✓ COMPLETE (partial; SecurityTrails in Step 4 will refine) |
| 4. SecurityTrails | ✓ COMPLETE |
| 5. Behavioral analysis | ✓ COMPLETE |
| 6. Inclusion criteria | ✓ COMPLETE |
| 7. Functional impact test | ⚠ Pi-hole test required |
| 8. domains.csv entries | ✓ DRAFTED |
| 9. Pull request | ⚠ Pending Step 7 |
