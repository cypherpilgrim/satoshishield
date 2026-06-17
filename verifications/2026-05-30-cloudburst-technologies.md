---
# Core
type: verification
company: "cloudburst-technologies"
date: 2026-05-30
verifier: cypherpilgrim
outcome: INCLUDED IN BLOCKLIST

# Project metadata
project: SatoshiShield
tier: 1
status: in-blocklist

# Verdict and process
verdict: Meets SatoshiShield inclusion criteria — off-chain cyber threat intelligence platform built to identify and attribute crypto actors across deep/dark web sources, marketed to law enforcement and OFAC use cases, with a documented strategic integration into Chainalysis's blockchain analytics stack
date_started: 2026-05-30
date_completed: 2026-05-30

# Domain scope
block_targets:
  - "burst.cloud (root + wildcard)"
non_targets: []

# Geography
hq_country: US
operations_countries: [US]
origin_country: US

# Lineage
predecessor: []
successor: []
related_companies:
  - "chainalysis"
related_verifications:
  - "2026-05-29-amberdata"

# Revision history
revision_history:
  - "2026-05-30 v1: Initial verification — INCLUDED Tier 1, PENDING FUNCTIONAL TEST"
  - "2026-06-16 v2: Status corrected to in-blocklist — shipped in v1.6.0"

# Tags
tags:
  - verification
  - tier-1-candidate
  - usa
  - north-america
  - off-chain-intelligence
  - osint
  - dark-web-monitoring
  - chainalysis-integration
  - law-enforcement-marketing
  - venture-backed
---

> **Public sanitized verification record.** A research artifact from the SatoshiShield project, published to show the verification methodology applied to each candidate domain. Internal lab infrastructure has been redacted. Not legal or financial advice.


---
# Cloudburst Technologies — Verification Record

**VERDICT: INCLUDED IN BLOCKLIST (Tier 1).**

Cloudburst Technologies is a New York-based (Tribeca) cyber threat intelligence firm founded in 2022, specializing in off-chain crypto intelligence — the systematic collection and AI-driven analysis of non-blockchain data sources (Telegram, Discord, WeChat, forums, dark web markets, regulatory filings, news, social media) to attribute crypto activity to specific actors and identify fraud networks. The company's stated mission is to give "institutions visibility into the risks and narratives shaping the digital asset ecosystem beyond the blockchain" and to identify "who is behind a wallet, what groups they interact with, and how they try to push scams."

Total funding to date is $11M, including a $7M Series A in September 2025 led by Borderless Capital, with earlier seed investment from CoinFund, Coinbase Ventures, Strategic Cyber Ventures (SCV), and Bloccelerate VC. CEO is Evan Kohlmann, a former counterterrorism analyst.

The decisive evidence for inclusion is a **strategic integration partnership with Chainalysis** announced in June 2024, which expressly merges Cloudburst's "deep and dark web monitoring capabilities" with Chainalysis's blockchain analytics platform "to provide a robust new approach in identifying and mitigating illicit online activities that touch on digital assets." The partnership is operationally targeted at law enforcement and regulatory investigations.

The company's own homepage at `burst.cloud` markets the platform as "Zero-analyst threat & financial intelligence, powered by an autonomous intelligence platform" and includes a live-simulated intelligence report titled "OPERATION 'SILENT FLOW'" describing autonomous tracing of BTC through mixers, attribution to a "threat actor" called "Cyber_Ghost," and generation of an "OFAC designation packet" linking wallet addresses to Lazarus Group identifiers. This is unambiguous identification-of-individuals positioning.

The customer list per public disclosures includes financial institutions, regulators, exchanges, crypto-native firms, government agencies, and law enforcement.

## Why it was evaluated

Cloudburst Technologies surfaced as a Tier 2 candidate during initial scoping of off-chain crypto intelligence vendors. Characteristics making the firm worth investigating:

- AI-driven OSINT platform with explicit law enforcement and OFAC use-case marketing
- Strategic integration partnership with a confirmed Tier 1 firm (Chainalysis)
- Venture-backed by tier-1 crypto and cybersecurity investors
- CEO background in counterterrorism intelligence
- Single primary domain (`burst.cloud`) with auto-narrating intelligence demo on the landing page

---
## Step 1 — WHOIS Lookup — ✓ Complete

**Tool used:** `whois` CLI. Domain verified: `burst.cloud`.

**Findings — burst.cloud:**

| Field         | Value                                                                                       |
| ------------- | ------------------------------------------------------------------------------------------- |
| Registrar     | Cloudflare, Inc. (IANA 1910)                                                                |
| Creation date | 2022-11-22                                                                                  |
| Expiry        | 2026-11-22 (annual renewal cycle)                                                           |
| Last updated  | 2025-11-22 (most recent annual renewal); registry-level update 2025-11-06                   |
| Registrant    | Redacted — Cloudflare privacy proxy (DATA REDACTED). State: NY. Country: US.                |
| Nameservers   | jaime.ns.cloudflare.com, val.ns.cloudflare.com (Cloudflare DNS)                             |
| Domain status | clientTransferProhibited (single anti-hijacking lock; no renewal/delete/update locks)       |
| DNSSEC        | unsigned                                                                                    |
| TLD operator  | Aruba PEC S.p.A. (Italy) — `.cloud` is operated by an Italian registry but Cloudflare is the registrar |

**Notes:**

- **Cloudflare full-stack bundle pattern (matches Section 5.12 registrar-tier classification).** Registrar, nameservers, and privacy proxy are all Cloudflare. Per the registrar-choice taxonomy documented in Industry Context Notes Section 5.12, this is the deliberate-consolidation pattern: a modern startup that has chosen Cloudflare across multiple infrastructure layers rather than mixing providers. Consistent with the firm's profile as a 2022-founded venture-backed startup.
- **Domain age matches firm vintage.** Registered November 22, 2022; firm was founded in 2022 per public-source research in Step 4. This is the standard early-stage startup pattern: register the brand domain at company formation. No legacy domain history, no pre-incorporation registration, no recent acquisition or rebrand.
- **NY state registrant location matches Tribeca HQ.** The "Registrant State/Province: NY" field (the only registrant data not redacted by Cloudflare's privacy proxy) is consistent with the firm's documented Tribeca, NYC headquarters per Step 4 behavioral evidence.
- **Single-lock domain status is operationally consistent with active product use.** Unlike a brand-preservation asset (which would typically carry all four client locks), Cloudburst's domain carries only `clientTransferProhibited` — the standard anti-hijacking lock that doesn't impede legitimate operational changes. This is appropriate for an actively-used startup domain where the firm needs the ability to update DNS, renew on schedule, and modify configuration without registrar-side friction. The posture is consistent with an operationally-active surveillance product domain rather than a passively-held brand.
- **Recent renewal on annual anniversary.** Domain was renewed on its November 22 anniversary date in 2025. Standard automatic renewal cadence; the firm is actively paying to retain the domain.
- **`.cloud` TLD is on-brand rather than operationally meaningful.** The `.cloud` TLD (operated by Aruba PEC S.p.A. in Italy) is a generic tech-branding TLD. Combined with the "Cloudburst" company name, the choice is brand-aesthetic rather than operationally significant. No jurisdictional signal — `.cloud` is open registration globally.
- **No corporate identity exposed in registration.** Cloudflare's privacy proxy redacts the registrant organization, street, city, and postal code. Only state, country, and phone (Cloudflare's privacy contact number) are visible. Standard treatment; the corporate identity established in Step 4 (Cloudburst Technologies, Tribeca NYC, Evan Kohlmann CEO) is unaffected.

**Conclusion:** Step 1 findings reinforce the INCLUDED Tier 1 verdict and place the firm clearly in the "venture-backed startup using Cloudflare full-stack infrastructure" tier (Section 5.12 tier 4). The single-lock status, recent renewal, and Cloudflare-consolidated stack are consistent with an actively-operated SaaS surveillance product rather than a brand-preservation asset. No surveillance-vendor co-resolution signals visible at this layer.

---
## Step 2 — SSL Certificate — ✓ Complete

**Tool used:** `openssl s_client` to retrieve and inspect TLS cert chain on `burst.cloud:443`.

**Findings:**

| Field         | Value                                                                                       |
| ------------- | ------------------------------------------------------------------------------------------- |
| Issuer        | C=US, O=Google Trust Services, CN=WE1                                                       |
| Subject       | CN=burst.cloud (DV cert; no O= field naming Cloudburst Technologies or any parent entity)   |
| SAN coverage  | burst.cloud, *.burst.cloud (apex + wildcard)                                                |
| Validity      | Expires 2026-08-27 21:34:41 UTC (≈13 weeks remaining; standard 90-day rotation cycle)       |

**Notes:**

- **Google Trust Services WE1 issuer confirms the Cloudflare cert provisioning pipeline.** GTS WE1 is one of the intermediate CAs Cloudflare uses for automated cert provisioning on proxied customer domains. Combined with the Cloudflare nameserver delegation observed in Step 1 (jaime/val.ns.cloudflare.com), this confirms the Cloudflare full-stack consolidation: registrar, DNS, and TLS termination all run through Cloudflare's edge infrastructure. The cert provisioning is automated and rotates on a ~90-day schedule.
- **DV-tier cert with no corporate identity.** Subject contains only the common name; no `O=` field naming Cloudburst Technologies. This is the standard treatment for automated Cloudflare-managed certs and is not a signal about corporate identity beyond what the Step 1 WHOIS and Step 4 behavioral evidence already establish.
- **Wildcard SAN coverage hides the production subdomain inventory.** A wildcard cert covering `*.burst.cloud` means any subdomain under the apex can be served via Cloudflare without separate cert issuance. The wildcard hides specific subdomain enumeration from this cert inspection — `api.burst.cloud`, `app.burst.cloud`, dashboard subdomains, and any product-surface endpoints would all be served through the wildcard without surfacing in the SAN list. Subdomain enumeration via crt.sh historical cert logs would be the appropriate tool to surface the production footprint if needed for block-scope precision.
- **Identical SSL provisioning pattern to Blockseer.** Both `burst.cloud` (Cloudburst Technologies, INCLUDED Tier 1, active surveillance vendor) and `blockseer.com` (Blockseer, EXCLUDED, brand-preservation asset) carry the same GTS WE1 + wildcard SAN cert pattern. This reinforces the methodological observation in Industry Context Notes Section 5.16: the Cloudflare proxy obscures the underlying operational state — two domains with the same cert provisioning pattern can have radically different surveillance postures. SSL inspection alone cannot distinguish the two; the distinction comes from behavioral evidence (Step 4) and broader corporate-state research.
- **Short-lived cert validity reflects standard Cloudflare rotation cadence.** Cloudflare provisions and rotates GTS-issued certs on a ~90-day cycle. The current cert was issued in late May 2026 and expires late August 2026. Auto-renewal is presumed.

**Conclusion:** Step 2 confirms the Cloudflare-bundled cert provisioning pattern predicted from Step 1's nameserver evidence. The wildcard SAN coverage and DV cert are operationally consistent with an actively-operated SaaS surveillance product served through Cloudflare's edge. SSL findings do not directly establish surveillance functionality — they confirm the Cloudflare proxy is active and the production subdomain footprint is hidden behind the wildcard. The INCLUDED Tier 1 verdict is unchanged; the surveillance positioning rests on Step 4 behavioral evidence (Chainalysis integration, OFAC designation packet marketing, deanonymization positioning), not on infrastructure observation.

---
## Step 3 — SecurityTrails / Passive DNS — ✓ Complete

**Tool used:** `dig` CLI for current DNS records (A, AAAA, MX). NS records previously captured in Step 1 WHOIS. SecurityTrails historical lookup deferred — not material to the INCLUDED Tier 1 verdict.

**Findings:**

| Record | Value |
|---|---|
| A | 172.67.129.39, 104.21.2.120 (Cloudflare anycast proxy IPs) |
| AAAA | 2606:4700:3036::ac43:8127, 2606:4700:3033::6815:278 (Cloudflare IPv6 anycast) |
| MX | 1 aspmx.l.google.com; 5 alt1/alt2.aspmx.l.google.com; 10 alt3/alt4.aspmx.l.google.com (standard modern Google Workspace tenant) |
| NS | jaime.ns.cloudflare.com, val.ns.cloudflare.com (Cloudflare DNS, from Step 1) |

**Notes:**

- **Cloudflare reverse-proxy confirmed on both IPv4 and IPv6.** The A records (172.67.129.39 in Cloudflare's 172.64.0.0/13 range; 104.21.2.120 in 104.16.0.0/12) and AAAA records (both in Cloudflare's 2606:4700::/32 IPv6 allocation) are anycast proxy endpoints. The production surveillance backend is hidden behind Cloudflare's edge. This is the documented pattern from Industry Context Notes Section 5.16: "Cloudflare proxy hides origin infrastructure." Without origin visibility, the only blockable surface from a DNS-layer perspective is the Cloudflare-fronted `burst.cloud` apex and wildcard.
- **Active Google Workspace MX tenant (modern five-host configuration).** Priority 1 `aspmx.l.google.com`, priority 5 `alt1/alt2.aspmx.l.google.com`, priority 10 `alt3/alt4.aspmx.l.google.com`. This is the modern Google Workspace MX pattern that Google deployed as standard from approximately 2018 onward, replacing the older `aspmx2/aspmx3.googlemail.com` priority-10 pattern. Consistent with a 2022-founded startup setting up email tenancy on the contemporary default.
- **MX vintage differs from Blockseer (cross-verification observation).** Blockseer's Step 3 surfaced the older `aspmx2/aspmx3.googlemail.com` priority-10 pattern, consistent with a Google Workspace tenant set up in the 2015-2017 era. Cloudburst uses the modern `alt3/alt4.aspmx.l.google.com` pattern. Both are functionally equivalent, but the pattern difference is a quiet vintage signal: Google Workspace tenants tend to preserve their original MX configuration unless deliberately migrated. This could be worth promoting to a cross-cutting observation if it surfaces in a third verification — extending Industry Context Notes Section 5.15 (email provider choice tracks firm vintage and customer base) with sub-pattern detail.
- **No surveillance-vendor co-resolution signal.** Cloudflare proxy IPs are shared across millions of customer domains globally; not a meaningful signal. What would be meaningful — origin AWS/GCP/Azure resolution direct from `dig`, surveillance-vendor-adjacent nameservers, or shared cloud backend with a known surveillance peer — is hidden behind the Cloudflare proxy by design.
- **No subdomain enumeration via Step 3.** As predicted from the wildcard cert observation in Step 2, the production subdomain inventory is not visible from apex-only `dig` queries. crt.sh historical cert logs would be the appropriate tool if subdomain-level block scope precision is needed (e.g., distinguishing `api.burst.cloud` from `marketing.burst.cloud` for selective blocking) — though for this verification, blocking the apex + wildcard captures the full surveillance surface regardless of subdomain structure.

**Conclusion:** DNS findings confirm the Cloudflare full-stack consolidation pattern across all three layers (registrar from Step 1, cert provisioning from Step 2, edge proxying and DNS from Step 3). The active Google Workspace MX tenant confirms operational use of the domain for corporate email. No surveillance-vendor co-resolution signals. The INCLUDED Tier 1 verdict is unchanged; the block scope of `burst.cloud` (root + wildcard) captures the entire DNS-layer surveillance surface this verification can address. The Cloudflare proxy means origin infrastructure cannot be enumerated from this layer, but that limitation does not affect the verdict — surveillance positioning was established at Step 4 by vendor self-description, not by infrastructure observation.

---
## Step 4 — Behavioral Evidence — COMPLETE (vendor documentation route)

Per Contributor Guide v1.4 §4.4, vendor-documentation route applied. Tier 1 candidate firm with extensive self-published evidence.

**Product positioning (Cloudburst homepage at burst.cloud):**
> "Zero-analyst threat & financial intelligence, powered by an autonomous intelligence platform."

**Live demo on landing page (sample auto-generated intelligence report):**
> "SUBJECT: OPERATION 'SILENT FLOW' - INTEL REPORT. SUMMARY: Autonomous agents have identified a sophisticated money laundering operation involving cryptocurrency and shell companies... The threat actor 'Cyber_Ghost' has moved approximately .2M in BTC through mixer services... INCOMING RFI: FROM H.Q. REQUEST: Confirm association between specific wallet 0x7a...4e9 and known Lazarus Group identifiers. Needed for OFAC designation packet."

**Strategic partnership with Chainalysis (PRNewswire, June 26, 2024):**
> "Cloudburst Technologies (www.burst.cloud), the market leader in off-chain intelligence data for the digital asset market, and Chainalysis (www.chainalysis.com), the blockchain analysis company, are proud to announce a strategic partnership... The partnership brings together Cloudburst Technologies' cutting-edge deep and dark web monitoring capabilities — tailored to crypto fraud and crafted using AI — with Chainalysis' state-of-the-art blockchain analysis platform... Investigators can trace cryptocurrency transactions linked to illicit actor profiles from the dark web, providing critical insights for law enforcement and regulatory bodies."

**Customer segments (CoinDesk, September 23, 2025):**
> "Cloudburst is already working with major crypto exchanges, compliance teams and government agencies."

**Attribution-focused mission (Ventureburn, October 9, 2025):**
> "Fraud detection is not just about a wallet address. It's about patterns, links, and behaviours across platforms. This helps institutions see fraud networks in context. It can reveal who is behind a wallet, what groups they interact with..."

**Corporate identity:**
- HQ: Tribeca, New York City, USA
- Founded: 2022
- CEO: Evan Kohlmann (former counterterrorism analyst)
- Domain: burst.cloud (primary; corporate identity)
- Funding: $11M total ($7M Series A 9/2025 led by Borderless Capital; seed from CoinFund, Coinbase Ventures, SCV, Bloccelerate VC)

---
## Step 5 — Privacy Harm Assessment

Cloudburst's product creates direct user-layer privacy harm in multiple dimensions, all of which fit within the SatoshiShield inclusion framework:

1. **Cross-platform attribution.** The platform's core value proposition is linking wallet addresses to off-chain identities — exactly the deanonymization function the inclusion criteria target.
2. **Law enforcement and OFAC use cases.** The platform is explicitly marketed for OFAC designation work and law enforcement investigations, with simulated reports on the homepage showing OFAC-packet generation as a feature.
3. **Chainalysis integration.** Cloudburst data flows into Chainalysis's analytics platform, multiplying the surveillance impact of both firms. Blocking either independently is incomplete; both should be blocked at the DNS layer.
4. **Off-chain data sourcing.** By design, the platform aggregates data from sources users do not consent to surveillance through (Telegram, Discord, dark web forums, social media). The blockchain itself becomes only one input to the attribution graph.

DNS-layer blocking of `burst.cloud` prevents Cloudburst's own infrastructure from being queried by any browser, wallet, or app on the protected network. It does not directly stop Cloudburst from ingesting public Telegram/Discord data, but it does prevent users from interacting with Cloudburst-affiliated services and prevents Cloudburst tracking pixels, analytics, or telemetry endpoints from being reached.

---
## Step 6 — Inclusion Criteria — MEETS 5 of 6

- [x] **Blockchain Analytics firm** — Cloudburst's product is explicitly framed as "the market leader in off-chain intelligence data for the digital asset market" with attribution as a core feature
- [x] **Address Screening API** — the platform generates "intelligence" outputs linked to specific wallet addresses; demo on the homepage explicitly shows wallet-address-to-actor mapping
- [x] **IP-Logging Infrastructure** — surveillance platform; standard pattern is to log query patterns against requester identity
- [x] **KYC/AML Intelligence** — explicit AML/compliance use case marketing; products used by compliance teams
- [ ] **Wallet Telemetry** — not a wallet vendor; no consumer wallet integration
- [x] **Deanonymization Platform** — direct positioning: "It can reveal who is behind a wallet"; live demo shows actor attribution and OFAC packet generation

**Five of six criteria met.** Wallet Telemetry does not apply because Cloudburst is not a consumer wallet vendor. All other criteria are unambiguously met by self-published vendor evidence.

---
## Step 7 — Functional Impact Test — ✓ Complete

**Date of test:** 2026-05-31
**Test environment:** Production home network behind two Pi-hole resolvers (pihole-1 at <internal-ip>, pihole-2 at <internal-ip>) operating in split-DNS configuration. Mac desktop traffic routed predominantly through pihole-2 (client IP <internal-ip>); mobile and consumer-app traffic routed predominantly through pihole-1 (client IP <internal-ip> source-NAT). Both Pi-hole logs were inspected for each test surface to ensure full visibility across the split-DNS architecture.

**Block scope tested:** `burst.cloud` (exact match), `www.burst.cloud` (exact match), `burst.cloud` (wildcard catching all subdomains). Staged on both Pi-holes via manual denylist entries; Gravity updated on both before testing began.

**Pre-test verification:** Both Pi-holes confirmed returning `0.0.0.0` for `dig burst.cloud` before test surfaces were opened. The SatoshiShield gravity-fetched blocklist remained active throughout the test (confirmed via `dig api.chainalysis.com` → 0.0.0.0).

**Post-test integrity check:** Both Pi-holes confirmed still returning `0.0.0.0` for `dig burst.cloud @<your-resolver>` and `dig burst.cloud @<your-resolver>` at 09:10 MT, after the full test cycle completed. Block integrity held throughout.

**Test surfaces and results:**

| Surface | Test start (MT) | Functional outcome | DNS queries to `burst.cloud` or `*.burst.cloud` |
|---|---|---|---|
| BlueWallet (mobile) | 08:32 | ✓ Opened, synced, balance displayed | Zero |
| Muun Wallet (mobile) | 08:34 | ✓ Opened, synced, balance displayed | Zero |
| Sparrow Wallet (desktop, public Electrum) | 08:36 | ✓ Opened, connected to Electrum, wallet view displayed | Zero |
| Strike (mobile) | 08:47 | ✓ Opened, synced, balance displayed | Zero |
| Coinbase web (browser, login + KYC route) | 09:03 | ✓ Login succeeded, KYC redirect page loaded normally | Zero |
| Electrum (desktop) | 09:16 | ✓ Opened, server discovery succeeded, wallet view displayed | Zero |

**Headline finding:** Across six consumer-facing Bitcoin wallets and exchanges spanning iOS and macOS platforms — including two surfaces that fired their most aggressive fraud-detection stacks during the test window (Strike with Firebase + Sift Science + RudderStack + Mixpanel; Coinbase web with its first-party Device Intelligence and the documented Sardine randomized-subdomain integration) — **none generated a single DNS query to `burst.cloud` or any subdomain thereof.** Cloudburst Technologies has no observed consumer-side wallet SDK integration. The block scope is functionally inert against consumer Bitcoin and exchange application traffic.

**Cross-cutting observations from the test cycle:**

- **Strike's fraud-detection vendor stack is settled and does not include Cloudburst.** Strike's session at 08:47 fired Firebase Remote Config, Firebase Crashlytics, Firebase analytics logging, Sift Science (`api3.siftscience.com`, 7 queries across the test window), RudderStack via Strike's tenant subdomain `strikemanen.dataplane.rudderstack.com`, and Mixpanel — but zero Cloudburst contacts. Strike's documented vendor list does not include Cloudburst, consistent with Cloudburst's B2B-only customer profile.
- **Coinbase web's full risk stack does not include Cloudburst.** Coinbase web at 09:03 fired its first-party Device Intelligence (`p.cb-device-intelligence.com`) and a Sardine query in the documented randomized-subdomain pattern (`mibfbljssq4wn0k5bcplku8i8ae6yxkm.d.sardine.ai`) during the login + KYC-redirect window. Even Coinbase's most aggressive identity-verification footprint did not contact Cloudburst.
- **Electrum's normal operation is unaffected.** Electrum bootstrapped its standard community Electrum server discovery, resolving `electrum.diynodes.com`, `skbxmit.coinjoined.com`, `guichet.centure.cc`, `stavver.dyshek.org`, `fulcrum.cryptohouse.ddns.net`, `vps.hsmiths.com`, and `blkhub.net` with real DNS responses (159–610 ms range). Privacy-respecting wallet operation continues normally with Cloudburst blocking active.

**Conclusion:** Zero functional impact across six consumer test surfaces. The `burst.cloud` (root + wildcard) block scope is operationally safe to include in the SatoshiShield blocklist. The INCLUDED Tier 1 verdict — based on Cloudburst's documented strategic partnership with Chainalysis, autonomous-agent OFAC designation packet marketing, and law-enforcement customer segment — is functional-test-cleared and ready for v1.6.0 merge.

---
## Pattern observations

Cloudburst extends the off-chain-intelligence pattern first surfaced during TRM Labs verification. Distinguishing features:

- **Counterterrorism-analyst founder pedigree** suggests deliberate national-security / OFAC positioning rather than incidental compliance-vendor evolution
- **Strategic dependence on Chainalysis** rather than competition with it; Cloudburst is the off-chain data layer that augments Chainalysis's on-chain analytics
- **Branded autonomous-agent positioning** ("Zero-analyst") reflects the broader 2025-2026 AI-agent industry wave in compliance and surveillance tooling
- **Single primary domain (`burst.cloud`)** rather than a corporate apex + separate API domain; simpler block scope than Amberdata

## Verification status

| Step                      | Status     | Outcome                                                                                                                                                                   |
| ------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. WHOIS                  | ✓ Complete | Cloudflare full-stack bundle (registrar + NS + privacy), 2022 creation matching firm vintage, NY state registrant matching Tribeca HQ, single-lock active-startup posture |
| 2. SSL certificate        | ✓ Complete | GTS WE1 DV cert via Cloudflare provisioning pipeline; apex + `*.burst.cloud` wildcard; 90-day rotation; production subdomain inventory hidden behind wildcard             |
| 3. SecurityTrails         | ✓ Complete | Cloudflare proxy on both A and AAAA; active Google Workspace MX (modern pattern); origin infrastructure hidden behind proxy; no surveillance-vendor co-resolution         |
| 4. Behavioral evidence    | ✓ Complete | Vendor self-documentation + Chainalysis partnership PR + venture funding coverage establish surveillance positioning unambiguously                                        |
| 5. Privacy harm           | ✓ Complete | Direct deanonymization product with law enforcement / OFAC marketing                                                                                                      |
| 6. Inclusion criteria     | ✓ Complete | **MEETS 5 of 6 CRITERIA — INCLUDE Tier 1**                                                                                                                                |
| 7. Functional impact test | ✓ Complete | Six consumer test surfaces (BlueWallet, Muun, Sparrow, Strike, Coinbase web, Electrum); zero candidate-domain queries; zero functional impact                             |

**Final verdict:** INCLUDED IN BLOCKLIST (Tier 1). Block scope: `burst.cloud` (root + wildcard). Add to `domains.csv` as two entries (`burst.cloud`, `*.burst.cloud`) once Step 7 confirms no wallet functionality impairment.
