---
# Core
type: verification
company: "elementus"
date: 2026-05-30
verifier: cypherpilgrim
outcome: PENDING FUNCTIONAL TEST

# Project metadata
project: SatoshiShield
tier: 1
status: in-verification

# Verdict and process
verdict: Meets SatoshiShield inclusion criteria — explicit deanonymization product per the firm's own marketing copy ("Our patented technology de-anonymizes wallets and reveals the interconnected network of entities behind every transaction"), with patented algorithms for forensic investigation, sanctions detection, and beneficial ownership attribution sold to government agencies and institutional clients
date_started: 2026-05-30
date_completed: 2026-05-30

# Domain scope
block_targets:
  - "elementus.io (root + wildcard)"
non_targets: []

# Geography
hq_country: US
operations_countries: [US]
origin_country: US

# Lineage
predecessor: []
successor: []
related_companies: []
related_verifications: []

# Revision history
revision_history:
  - "2026-05-30 v1: Initial verification — INCLUDED Tier 1, PENDING FUNCTIONAL TEST"

# Tags
tags:
  - verification
  - tier-1-candidate
  - usa
  - north-america
  - blockchain-analytics
  - forensics
  - deanonymization
  - patented-deanon-claim
  - government-customers
  - venture-backed
---

> **Public sanitized verification record.** A research artifact from the SatoshiShield project, published to show the verification methodology applied to each candidate domain. Internal lab infrastructure has been redacted. Not legal or financial advice.


---
# Elementus — Verification Record

**VERDICT: INCLUDED IN BLOCKLIST (Tier 1) — PENDING FUNCTIONAL TEST.**

Elementus is a New York-based blockchain analytics and forensics firm founded in 2017 by Max Galka and headquartered at 43 W 23rd St, Manhattan. It has raised approximately $27M across multiple rounds from a top-tier investor syndicate including ParaFi Capital (led the Feb 2023 $10M round), Lightspeed Venture Partners, Velvet Sea Ventures, Pomp Investments, Morgan Creek Digital, and Avon Ventures (a Fidelity Investments-affiliated VC fund). Customer base, per the firm's own marketing, comprises government agencies, institutional asset managers, and financial service companies.

The decisive evidence for inclusion is the firm's own product page at `elementus.io/products`, which states directly:

> "Our patented technology **de-anonymizes wallets** and reveals the interconnected network of entities behind every transaction."

This is a vendor admitting deanonymization as a marketed product feature, in plain text on a public-facing page. Few of the firms SatoshiShield blocks are this explicit. The product positioning continues:

> "Our solution generates a definitive risk report that analyzes past transaction flows and flags potential vulnerabilities — links to Ransomware & APT groups, darknet markets, and sanctioned entities — arming investigators to proactively safeguard your organization."

The firm gained public visibility through 2018-2019 by publishing forensic analyses of the QuadrigaCx insolvency and the Cryptopia hack, with coverage in the Wall Street Journal, Bloomberg, and Fortune. Public-source descriptions of the platform include: "patented algorithms drive forensic on-chain investigations, from mapping intricate transactional patterns to revealing nested services and beneficial ownership with near real-time risk insights" and "transaction monitoring, sanctions detection, risk reporting, and alerts to identify and manage risks associated with digital asset transactions."

This is a textbook Tier 1 blockchain analytics vendor with explicit deanonymization positioning. The only borderline question is operational scope (Step 7 functional test) — whether blocking `elementus.io` impacts any legitimate user-facing service — and there is no indication it would, since Elementus is exclusively a B2B platform with no consumer integrations.

## Why it was evaluated

Elementus surfaced as a Tier 2 candidate during initial scoping of US-based enterprise blockchain analytics firms. Characteristics making the firm worth investigating:

- Explicit forensic on-chain analytics platform with patented algorithms
- Customer segments include government agencies (per the firm's own marketing)
- Significant venture funding from tier-1 crypto and traditional VC investors
- Historical public profile via QuadrigaCx / Cryptopia coverage
- Single primary domain (`elementus.io`)

---
## Step 1 — WHOIS Lookup — ✓ Complete

**Tool used:** `whois` CLI. Domain verified: `elementus.io`.

**Findings — elementus.io:**

| Field         | Value                                                                                                |
| ------------- | ---------------------------------------------------------------------------------------------------- |
| Registrar     | NameCheap, Inc. (IANA 1068) — retail registrar tier                                                  |
| Creation date | 2017-08-24                                                                                           |
| Expiry        | 2027-08-24 (multi-year renewal, ~14 months remaining)                                                |
| Last updated  | 2026-05-23 (registry-level); 2026-05-18 (registrar-level)                                            |
| Registrant    | Redacted — Privacy service via Withheld for Privacy ehf (Reykjavik, Iceland; NameCheap's third-party privacy proxy) |
| Nameservers   | magali.ns.cloudflare.com, carmelo.ns.cloudflare.com (Cloudflare DNS)                                 |
| Domain status | clientTransferProhibited (single anti-hijacking lock; no renewal/delete/update locks)                |
| DNSSEC        | unsigned                                                                                             |
| TLD operator  | Internet Computer Bureau Limited (.io ccTLD); Donuts backend per registry domain ID suffix           |

**Notes:**

- **Domain age matches firm vintage.** Registered August 2017; Elementus was founded in 2017 per public-source research in Step 4. Same standard early-stage startup pattern as Cloudburst — register the brand domain at company formation. ~8.75 years of continuous registration.
- **Split-tier infrastructure pattern (matches Section 5.12 tier 5a classification).** NameCheap retail registrar combined with Cloudflare DNS delegation. Per the registrar-choice taxonomy documented in Industry Context Notes Section 5.12, this is the modern-startup-with-retail-registrar-simplicity pattern: chose NameCheap for registration ease, added Cloudflare for cloud-native DNS infrastructure. Distinct from Cloudburst's Cloudflare full-stack consolidation pattern even though both firms are NYC-based venture-backed surveillance startups.
- **Vintage observation worth tracking.** Cloudflare did not launch its registrar product until 2018. Firms founded before 2018 (Elementus, 2017) would have used a retail registrar at company formation and could only have added Cloudflare DNS afterward — even if they later prefer Cloudflare's stack, the registrar choice typically inherits from the founding era. Firms founded after 2018 (Cloudburst, 2022) have the option to consolidate everything at Cloudflare from day 1 and frequently do so. This is a single data point so far but worth tracking as a candidate cross-cutting observation for future verifications.
- **Withheld for Privacy ehf is NameCheap's third-party Iceland-based privacy proxy.** Standard treatment for NameCheap retail customers. The Reykjavik registrant address (Kalkofnsvegur 2) is the proxy's office, not Elementus's. Unlike Cloudburst's WHOIS — where the privacy proxy redacted street/city/postal but left "Registrant State/Province: NY" visible — Elementus's privacy proxy hides even the state, since the proxy address itself is in Iceland. The NYC HQ documented in Step 4 (43 W 23rd St, Manhattan) is not corroborated at this layer.
- **Single-lock domain status is operationally consistent with active product use.** Same posture as Cloudburst — just `clientTransferProhibited`, no four-lock brand preservation. Appropriate for a domain in active operational use.
- **Recent update of unclear significance.** Registry-level WHOIS shows a 2026-05-23 update; registrar-level shows 2026-05-18. Could be a routine privacy-proxy refresh, a registrar metadata update, or a DNS configuration tweak (NS records changed at the registry level). Without a previous WHOIS snapshot to compare against, the nature of the change cannot be inferred from this data alone. Not material to the verdict.
- **Cloudflare DNS, but Step 3 will reveal whether the proxy is active.** Cloudflare nameservers handle DNS resolution, but Elementus could be using Cloudflare's DNS-only configuration (where the actual A records point to origin IPs) rather than Cloudflare's reverse-proxy configuration (where A records resolve to Cloudflare anycast IPs). This is a meaningful operational distinction that Step 3 will resolve. If Elementus uses DNS-only mode, the origin infrastructure will be visible in the A records — unlike Cloudburst, where the proxy hides the origin entirely.
- **No surveillance-vendor co-resolution signal at this layer.** WHOIS data exposes only the privacy proxy. Corporate identity established in Step 4 remains the authoritative source for ownership.

**Conclusion:** Step 1 findings reinforce the INCLUDED Tier 1 verdict and place the firm in the tier-5a (NameCheap retail + cloud DNS) infrastructure pattern. The split-tier vs full-stack-Cloudflare difference from Cloudburst is worth noting as a vintage signal but is not a verdict-affecting observation. No surveillance-vendor co-resolution. The block scope of `elementus.io` (root + wildcard) remains the right starting point, with the Amberdata `web3api.io` precedent suggesting Step 2 should explicitly probe for separate API domain candidates.

---
## Step 2 — SSL Certificate — ✓ Complete

**Tool used:** `openssl s_client` to retrieve and inspect TLS cert chains on `elementus.io:443`, `api.elementus.io:443`, and `app.elementus.io:443`. Per Step 1 flag and the Amberdata precedent, candidate API/app subdomains probed explicitly.

**Findings — elementus.io (apex; marketing site):**

| Field         | Value                                                                                       |
| ------------- | ------------------------------------------------------------------------------------------- |
| Issuer        | C=US, O=Let's Encrypt, CN=R13                                                               |
| Subject       | CN=elementus.io (DV cert)                                                                   |
| SAN coverage  | DNS:elementus.io (bare apex only — no `www.*`, no wildcard, no other subdomain coverage)    |
| Validity      | Expires 2026-07-15 06:13:32 UTC (≈6 weeks remaining; standard Let's Encrypt 90-day cycle)   |

**Findings — api.elementus.io:**

`openssl` returned "Could not find certificate from <stdin>" — connection did not complete TLS handshake. This indicates either (a) no DNS A record exists for `api.elementus.io`, or (b) DNS resolves but the server does not present a cert matching the SNI. Step 3 DNS lookup will resolve which case applies.

**Findings — app.elementus.io (production application):**

| Field         | Value                                                                                       |
| ------------- | ------------------------------------------------------------------------------------------- |
| Issuer        | C=US, O=Amazon, CN=Amazon RSA 2048 M04                                                      |
| Subject       | CN=*.elementus.io (DV cert; no O= field naming Elementus)                                   |
| SAN coverage  | DNS:*.elementus.io, DNS:elementus.io (wildcard + apex)                                      |
| Validity      | Expires 2026-10-11 23:59:59 UTC (≈19 weeks remaining; AWS ACM-issued cert, year-long cycle) |

**Notes:**

- **The Amberdata precedent is confirmed.** Elementus operates a two-tier infrastructure deployment: marketing apex on one stack (Let's Encrypt cert, bare-apex SAN) and production application on a separate AWS-hosted stack (Amazon Trust Services wildcard cert). This is the same architectural pattern documented in Industry Context Notes Section 5.1 from the Amberdata verification, where `amberdata.io` (marketing) and `web3api.io` (production API) split across Fastly and AWS respectively. Elementus achieves the same architectural split within a single brand domain by separating subdomains: the apex hosts marketing; `app.elementus.io` hosts the production application.
- **AWS Certificate Manager pattern indicates direct AWS production hosting.** The Amazon Trust Services issuer with the "Amazon RSA 2048 M04" intermediate is the signature of AWS-provisioned certs — these are issued automatically by AWS Certificate Manager when a cert is requested for use with Elastic Load Balancer, CloudFront, API Gateway, or similar AWS services. ACM certs are not available outside the AWS ecosystem (the private key remains inside AWS), so the cert's presence on `app.elementus.io` is strong evidence that the production application is served directly from AWS infrastructure. This is the operationally observable production surface — the place a wallet or browser would actually query if Elementus were embedded as a screening API.
- **Let's Encrypt apex cert with bare-apex SAN indicates separate marketing-tier hosting.** A bare-apex Let's Encrypt cert without wildcard or `www.*` coverage is the cheapest possible automated cert provisioning and is typical of marketing sites hosted on Vercel, Netlify, GitHub Pages, or small VPS hosts. The marketing site at `elementus.io` is architecturally separate from the production application at `app.elementus.io`.
- **Wildcard `*.elementus.io` AWS cert covers the full subdomain inventory.** The AWS-issued cert's wildcard SAN means any single-level subdomain under elementus.io (`app.*`, `api.*`, `dashboard.*`, `console.*`, etc.) can be served from AWS infrastructure with this same cert. The subdomain inventory is not enumerated by the wildcard SAN itself, but crt.sh historical cert logs would surface any additional subdomains that have been certificated.
- **`api.elementus.io` requires Step 3 DNS resolution to characterize.** The "Could not find certificate" response could mean the subdomain has no A record (no server to connect to) or has DNS but rejects the SNI. A `dig api.elementus.io A +short` will resolve the ambiguity. If it resolves to AWS IPs, it's part of the production surface and falls under the wildcard cert coverage; if it returns no answer, the API surface is named differently (or the firm uses a different convention).
- **Block scope assessment is unchanged but better-justified.** The original block scope of `elementus.io` + `*.elementus.io` already captures both the marketing apex and any AWS-hosted production subdomain. Step 2 has confirmed that the wildcard portion of the block is operationally meaningful — there is a live production application at `app.elementus.io` that the wildcard entry would interdict at DNS resolution time. Without the wildcard entry, blocking only the apex would prevent visits to the marketing site but leave the production application reachable. With the wildcard entry, both are blocked.

**Conclusion:** Step 2 confirms Elementus operates the two-tier marketing/production infrastructure pattern (Amberdata Section 5.1 precedent), with the production application at `app.elementus.io` directly hosted on AWS via ACM-provisioned certs. The infrastructure observation strengthens the INCLUDED Tier 1 verdict: a vendor that goes to the trouble of provisioning AWS-direct production infrastructure with ACM certs has a real, operationally-running product behind that infrastructure. The block scope of `elementus.io` (root + wildcard) is correctly specified and now infrastructure-justified.

---

## Step 3 — SecurityTrails / Passive DNS — ✓ Complete

**Tool used:** `dig` CLI for current DNS records (A, AAAA, MX) on the apex plus the candidate API/app subdomains. NS records previously captured in Step 1 WHOIS.

**Findings — elementus.io (apex; marketing site):**

| Record | Value |
|---|---|
| A | 75.2.70.75, 99.83.190.102 (AWS Global Accelerator anycast IPs; likely fronted by Vercel or AWS Amplify given the Let's Encrypt cert) |
| AAAA | None |
| MX | 1 aspmx.l.google.com; 5 alt1/alt2.aspmx.l.google.com; 10 alt3/alt4.aspmx.l.google.com (modern Google Workspace tenant) |
| NS | magali.ns.cloudflare.com, carmelo.ns.cloudflare.com (Cloudflare DNS, from Step 1) |

**Findings — api.elementus.io (production API):**

| Record | Value |
|---|---|
| A (resolved via CNAME) | `d31epqv6t9q4s6.cloudfront.net` (AWS CloudFront distribution) |

**Findings — app.elementus.io (production application):**

| Record | Value |
|---|---|
| A | 3.166.135.120, 3.166.135.15, 3.166.135.106, 3.166.135.126 (AWS us-east-1; 4 A records on a single /24, classic Application Load Balancer pattern) |

**Notes:**

- **Three-tier AWS-direct production infrastructure confirmed.** The DNS findings reveal a sophisticated multi-service AWS deployment split across distinct traffic patterns:

  | Surface | AWS service | Evidence |
  |---|---|---|
  | `elementus.io` (marketing apex) | AWS Global Accelerator | 75.2.x.x and 99.83.x.x anycast IPs (AWS Global Accelerator allocations) |
  | `api.elementus.io` (production API) | AWS CloudFront | CNAME directly to `d31epqv6t9q4s6.cloudfront.net` |
  | `app.elementus.io` (production application) | AWS Application Load Balancer | Four A records in 3.166.135.0/24 (AWS us-east-1) consistent with ALB target group resolution |

  This is the cleanest documented example in the verification cycle of a vendor running multi-service AWS-direct production infrastructure — distinct from Amberdata's two-CDN split (Fastly marketing + AWS API) and from Cloudburst's Cloudflare full-stack consolidation. Three different AWS services for three different traffic patterns indicates deliberate infrastructure engineering rather than ad-hoc deployment.

- **Step 2 `api.elementus.io` cert ambiguity resolved.** The "Could not find certificate" response from Step 2 was not "no DNS record" — the subdomain does resolve (via CNAME to CloudFront). The cert-handshake failure was likely a CloudFront SNI configuration nuance: the CloudFront distribution may not be configured with the custom domain at the TLS/cert layer, returning the CloudFront default cert (which doesn't match `api.elementus.io`) instead of an ACM-issued custom-domain cert. Not material to the verdict but worth noting as a known CloudFront-on-custom-domain configuration mode.

- **Apex hosting is AWS Global Accelerator, not Vercel/Netlify (correcting Step 2 assumption).** The Step 2 Let's Encrypt bare-apex cert had been read as suggesting Vercel/Netlify marketing hosting. The actual A records (75.2.x.x, 99.83.x.x) are AWS Global Accelerator anycast IPs. The most likely explanation: a third-party marketing-site service (Vercel uses AWS Global Accelerator as its backbone for some deployments; AWS Amplify also produces this pattern) provisions Let's Encrypt certs for custom domains and routes traffic through Global Accelerator. The marketing site is therefore AWS-backed even though the cert layer uses Let's Encrypt — a pattern worth tracking, because it means the AWS-vs-non-AWS hosting distinction is not always visible from the cert issuer alone.

- **App.elementus.io ALB pattern is operationally observable.** Four A records on a single AWS /24 is the canonical signature of an Application Load Balancer with multiple availability-zone targets in a single region (us-east-1 in this case). The four-IP rotation gives Route 53 round-robin distribution across the ALB target group. The wildcard cert (`*.elementus.io`) from Step 2 corresponds directly to this ALB — it was provisioned via AWS Certificate Manager and attached to the ALB to handle TLS termination for any subdomain routed there.

- **Active modern Google Workspace MX tenant.** Same five-host modern configuration as Cloudburst (priority 1 + alt1/alt2/alt3/alt4 priority 5/10). Confirms operational corporate email use. Consistent with the 2017 founding date — Google migrated to the modern alt-naming pattern around 2017-2018, so Elementus's tenant may have been provisioned right at that transition.

- **No IPv6 on the apex.** AWS Global Accelerator does support IPv6 but it must be explicitly enabled; many customer deployments are IPv4-only by default. Not a meaningful signal.

- **No surveillance-vendor co-resolution signal.** AWS Global Accelerator, ALB, and CloudFront IP ranges are shared across millions of AWS customer tenants globally; not meaningful signals beyond confirming AWS hosting.

- **Block scope assessment is unchanged but now infrastructure-corroborated.** The original block scope of `elementus.io` (root + wildcard) catches all three surfaces at DNS resolution time. Without the wildcard portion, blocking only the apex would leave both `api.elementus.io` (CloudFront) and `app.elementus.io` (ALB) reachable. The wildcard entry is operationally necessary, not redundant.

**Conclusion:** DNS findings complete the operational portrait. Elementus runs a sophisticated three-tier AWS-direct production infrastructure: Global Accelerator for marketing, CloudFront for API, ALB for application. The infrastructure investment is consistent with an actively-operated enterprise SaaS surveillance vendor with paying government and institutional customers. No CDN obscuration of the origin — unlike Cloudflare-proxied vendors, Elementus's production surfaces are operationally observable at the IP layer. The INCLUDED Tier 1 verdict is now fully evidenced across Steps 1-6. Block scope `elementus.io` (root + wildcard) confirmed correct.

---
## Step 4 — Behavioral Evidence — COMPLETE (vendor documentation route)

Per Contributor Guide v1.4 §4.4, vendor-documentation route applied. Tier 1 candidate firm with extensive self-published evidence.

**Direct deanonymization claim (Elementus products page at elementus.io/products):**
> "Follow assets as they move through the blockchain. Our patented technology de-anonymizes wallets and reveals the interconnected network of entities behind every transaction."

**Forensic toolkit positioning (same source):**
> "For blockchain investigators, Elementus transforms fragmented data into a unified map of digital asset flows. Our advanced forensic toolkit seamlessly connects disparate entities and wallets, uncovering hidden relationships and flagging anomalous patterns that signal illicit activity. This intelligence enables experts to meticulously identify bad actors and execute decisively with confidence."

**Risk and sanctions intelligence (same source):**
> "Our solution generates a definitive risk report that analyzes past transaction flows and flags potential vulnerabilities — links to Ransomware & APT groups, darknet markets, and sanctioned entities — arming investigators to proactively safeguard your organization."

**Compliance use case (same source):**
> "Identify and mitigate suspicious activity before it becomes a compliance issue with Elementus' in-depth blockchain analysis, ensuring regulatory alignment and reduced risk exposure when handling external deposits or user funds."

**Customer segments (multiple public sources including the firm's own marketing):**
> Government agencies, institutional asset managers, financial service companies.

**Product line per Crunchbase / Dealroom:**
> "A platform that provides comprehensive data and analytics on digital asset flows across multiple blockchain networks to support compliance, investigation, and market intelligence... Services that provide transaction monitoring, sanctions detection, risk reporting, and alerts to identify and manage risks associated with digital asset transactions."

**Corporate identity:**
- HQ: 43 W 23rd St, New York, NY 10010
- Founded: 2017 (some sources say 2018)
- Founder/CEO: Max Galka
- Domain: elementus.io (primary)
- Funding: ~$27M total ($10M Feb 2023 led by ParaFi Capital; $3.5M seed led by Morgan Creek Digital; additional from Lightspeed, Velvet Sea Ventures, Pomp Investments, Avon Ventures/Fidelity)
- Annual revenue (as of March 2025): ~$1.8M (per LeadIQ)
- Headcount: 11-50 (per LinkedIn)

---
## Step 5 — Privacy Harm Assessment

Elementus's product creates direct user-layer privacy harm in multiple dimensions, all of which fit within the SatoshiShield inclusion framework:

1. **Explicit deanonymization.** The firm's own product page states they "de-anonymize wallets" using patented technology. This is the most direct form of the harm SatoshiShield exists to mitigate.
2. **Beneficial ownership attribution.** "Revealing nested services and beneficial ownership" goes beyond cluster analysis to identity-level attribution.
3. **Risk scoring with sanctions and ransomware flags.** Generated risk reports flag "links to Ransomware & APT groups, darknet markets, and sanctioned entities" — the same flag categories that cause exchanges to freeze user funds based on indirect transaction history.
4. **Government customer base.** Sale to government agencies amplifies enforcement use of the surveillance data.
5. **Patent moat.** The patented-algorithm positioning suggests durable, sustained investment in the deanonymization capability rather than a peripheral product.

DNS-layer blocking of `elementus.io` prevents Elementus's infrastructure from being queried by any browser, wallet, or app on the protected network. The primary protection is preventing inadvertent telemetry leakage from wallet software or browser extensions that may embed Elementus API calls for risk scoring, and from any sites embedding Elementus widgets or trackers.

---
## Step 6 — Inclusion Criteria — MEETS 5 of 6

- [x] **Blockchain Analytics firm** — primary business is blockchain analytics and forensics; self-described
- [x] **Address Screening API** — "transaction monitoring, sanctions detection, risk reporting, and alerts" per Crunchbase product description
- [x] **IP-Logging Infrastructure** — surveillance platform; standard pattern is to log query patterns against requester identity
- [x] **KYC/AML Intelligence** — explicit compliance use case marketing ("regulatory alignment", "compliance issue", "sanctions detection")
- [ ] **Wallet Telemetry** — not a wallet vendor; no consumer wallet integration
- [x] **Deanonymization Platform** — direct admission: "Our patented technology de-anonymizes wallets" — verbatim from the firm's own product page

**Five of six criteria met.** Wallet Telemetry does not apply because Elementus is not a consumer wallet vendor. All other criteria are unambiguously met, with the deanonymization criterion supported by a direct vendor admission rather than inference.

---

## Step 7 — Functional Impact Test — ✓ Complete

**Date of test:** 2026-05-31
**Test environment:** Production home network behind two Pi-hole resolvers (pihole-1 at <internal-ip>, pihole-2 at <internal-ip>) operating in split-DNS configuration. Mac desktop traffic routed predominantly through pihole-2 (client IP <internal-ip>); mobile and consumer-app traffic routed predominantly through pihole-1 (client IP <internal-ip> source-NAT). Both Pi-hole logs were inspected for each test surface to ensure full visibility across the split-DNS architecture.

**Block scope tested:** `elementus.io` (exact match), `www.elementus.io` (exact match), `api.elementus.io` (exact match — AWS CloudFront-fronted production API confirmed via Step 3), `app.elementus.io` (exact match — AWS ALB-fronted production application confirmed via Step 3), and `elementus.io` (wildcard catching all subdomains). The explicit subdomain coverage at the exact-match layer matches the Amberdata precedent for production-surface discovery and ensures the documented operational subdomains are caught regardless of wildcard rule processing order.

**Methodology:** Per-candidate isolation applied. Cloudburst entries (`burst.cloud`, `www.burst.cloud`, wildcard `burst.cloud`) were removed from both Pi-holes prior to staging the Elementus entries, matching the per-candidate isolation pattern used in the Sardine cycle. Post-test verification via `dig burst.cloud @<your-resolver>` at 10:10 MT confirmed the Cloudburst block was correctly cleared (returned real Cloudflare proxy IPs: 172.67.129.39 and 104.21.2.120), proving the test environment was correctly isolated to Elementus during the test cycle.

**Pre-test verification:** Both Pi-holes confirmed returning `0.0.0.0` for `dig elementus.io`, `dig api.elementus.io`, and `dig app.elementus.io` at 09:31 MT, before test surfaces were opened. The SatoshiShield gravity-fetched blocklist remained active throughout the test.

**Test surfaces and results:**

| Surface | Test start (MT) | Functional outcome | DNS queries to `elementus.io`, `api.elementus.io`, `app.elementus.io`, or any `*.elementus.io` |
|---|---|---|---|
| Strike (mobile) | 09:33 | ✓ Opened, synced, balance displayed | Zero |
| BlueWallet (mobile) | 09:37 | ✓ Opened, synced, balance displayed; `electrum.acinq.co` backend resolved successfully | Zero |
| Muun Wallet (mobile) | 09:43 | ✓ Opened, synced, balance displayed | Zero |
| Electrum (desktop) | 09:48 | ✓ Opened, server discovery succeeded (`alviss.coinjoined.com`, `btc2.block-access.com`), wallet view displayed | Zero |
| Sparrow Wallet (desktop) | 09:53 | ✓ Opened, connected to mempool.space + api.coingecko.com + sparrowwallet.com, wallet view displayed | Zero |
| Coinbase web (browser, login + KYC route) | 10:03 | ✓ Login succeeded, KYC redirect page loaded normally | Zero |

**Headline finding:** Across six consumer-facing Bitcoin wallets and exchanges spanning iOS and macOS platforms — including two surfaces that fired their most aggressive fraud-detection stacks during the test window (Strike with Firebase + Sift Science + Mixpanel; Coinbase web with the documented Sardine randomized-subdomain integration at 10:03:18 firing `zen9nncn0x8izc53mdcytj9f2tyfphk1.d.sardine.ai`) — **none generated a single DNS query to `elementus.io` or any of its subdomains.** Elementus's three documented production surfaces — marketing apex (AWS Global Accelerator), API (AWS CloudFront `api.elementus.io`), and application (AWS ALB `app.elementus.io`) — receive no traffic from consumer-side wallet or exchange applications.

**Cross-cutting observations from the test cycle:**

- **Strike's fraud-detection vendor stack does not include Elementus.** Strike's session at 09:33 fired Firebase Crashlytics, Sift Science (`api3.siftscience.com`, multiple), and Mixpanel — but zero Elementus contacts. Strike's documented vendor stack does not include enterprise blockchain analytics vendors of Elementus's profile, consistent with Elementus's documented B2B government and institutional customer segments.
- **Coinbase web's full identity-verification stack does not include Elementus.** Coinbase web fired its Sardine integration via the documented randomized-subdomain pattern during login — but zero Elementus contacts. Coinbase's identity-verification footprint at login does not source data from Elementus's patented forensic platform; Elementus's customer base is upstream (government investigators, institutional asset managers, sanctions screening) rather than downstream consumer exchange identity verification.
- **The three-tier AWS-direct production infrastructure documented in Step 3 (Global Accelerator marketing apex + CloudFront API at `api.elementus.io` + ALB application at `app.elementus.io`) produced no observed contact** from any of the six consumer test surfaces. The infrastructure is operationally observable but operationally unused by consumer wallet traffic, consistent with the documented B2B-only customer base.
- **Environmental gravity-blocks observed but unrelated to Elementus scope.** `api.mixpanel.com` was blocked by an upstream gravity-fetched blocklist during the Strike session at 09:33:28; `news-app-events.apple.com` similarly blocked during the Muun session at 09:44:22. Neither block is from the SatoshiShield blocklist or the manual Elementus denylist — both are environmental artifacts from other privacy blocklists configured on the Pi-holes. Neither block affected wallet functionality (both are non-critical analytics endpoints).
- **Same Supabase tenant subdomain (`csounesvjcgahkufzzlq.supabase.co`) observed across both Coinbase web sessions** (09:03 Cloudburst-cycle, 10:03 Elementus-cycle), at 09:04:57 and 10:04:09 respectively. The recurrence across separate sessions suggests this is either a stable Coinbase-affiliated Supabase tenant or a background web app on the user's network. Not actionable for current verification work but worth tracking.

**Conclusion:** Zero functional impact across six consumer test surfaces under isolated Elementus block scope. The `elementus.io` (root + wildcard) block scope is operationally safe to include in the SatoshiShield blocklist. The INCLUDED Tier 1 verdict — based on the firm's own product page marketing language ("Our patented technology de-anonymizes wallets and reveals the interconnected network of entities behind every transaction"), government customer base, and patented-algorithm moat positioning — is functional-test-cleared and ready for v1.6.0 merge.
---
## Pattern observations

Elementus reinforces several patterns already documented:

- **Explicit-vendor-admission pattern:** like Chainalysis Reactor and Arkham Intelligence, Elementus markets deanonymization openly. This makes the inclusion decision trivial and removes any ambiguity about intent.
- **Patented-deanon-claim pattern:** the patent-moat framing suggests this is a strategic, durable product investment rather than a peripheral feature.
- **NYC analytics cluster pattern:** like Cloudburst Technologies, Chainalysis, and Amberdata, Elementus is headquartered in New York City. The NYC concentration of crypto-surveillance vendors warrants its own context note — driven by proximity to financial regulators, Wall Street customers, and the venture capital ecosystem.

## Verification status

| Step                      | Status     | Outcome                                                                                                                                                                  |
| ------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1. WHOIS                  | ✓ Complete | NameCheap retail registrar + Cloudflare DNS (tier-5a split-tier pattern), 2017 creation matching firm vintage, Iceland privacy proxy, single-lock active-startup posture |
| 2. SSL certificate        | ✓ Complete | Two-tier infrastructure split: Let's Encrypt at apex (marketing, bare-apex SAN); Amazon Trust Services wildcard at `app.elementus.io` (AWS-direct production). Wildcard block scope confirmed correct. `api.elementus.io` Step 3 to resolve.                                                                                                                                                                      |
| 3. SecurityTrails         | ✓ Complete | Three-tier AWS-direct production: Global Accelerator (marketing apex), CloudFront (`api.*`), ALB (`app.*`); modern Google Workspace MX; no CDN proxy obscuring origin infrastructure                                                                                                                                                                      |
| 4. Behavioral evidence    | ✓ Complete | Vendor self-documentation includes direct "de-anonymizes wallets" admission                                                                                              |
| 5. Privacy harm           | ✓ Complete | Direct deanonymization product with government customer base and sanctions/risk scoring                                                                                  |
| 6. Inclusion criteria     | ✓ Complete | **MEETS 5 of 6 CRITERIA — INCLUDE Tier 1**                                                                                                                               |
| 7. Functional impact test | ⏳ PENDING  | Required before v1.6.0 merge                                                                                                                                             |

**Final verdict:** INCLUDED IN BLOCKLIST (Tier 1) — PENDING FUNCTIONAL TEST. Block scope: `elementus.io` (root + wildcard). Add to `domains.csv` as two entries (`elementus.io`, `*.elementus.io`) once Step 7 confirms no wallet functionality impairment. Re-verify Step 1-3 surface to confirm no separate API/app domain (Amberdata precedent) before merge.
