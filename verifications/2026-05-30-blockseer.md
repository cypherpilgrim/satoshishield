---
# Core
type: verification
company: "blockseer"
date: 2026-05-30
verifier: cypherpilgrim
outcome: EXCLUDED FROM BLOCKLIST

# Project metadata
project: SatoshiShield
tier: "N/A (excluded)"
status: excluded

# Verdict and process
verdict: Does not meet SatoshiShield inclusion criteria — current Blockseer-branded product is a free public Bitcoin block explorer positioned for operator self-service, similar to mempool.space; historical forensics positioning (2015-2019, IRS/FBI/Secret Service) has been retired and parent company DMG Blockchain Solutions has pivoted to mining and AI data centers
date_started: 2026-05-30
date_completed: 2026-05-30

# Domain scope
block_targets: []
non_targets:
  - "blockseer.com (currently a GoDaddy-hosted parking / 'coming soon' page per ZoomInfo; no active surveillance API surface)"

# Geography
hq_country: US
operations_countries: [US, CA]
origin_country: US

# Lineage
predecessor:
  - "Blockseer Inc. (independent, founded 2015 by Danny Yang, Palo Alto CA)"
successor:
  - "DMG Blockchain Solutions Inc. (acquirer, March 2018, ~C$2.6M cash + 7.7M shares)"
parent: "dmg-blockchain-solutions"
related_companies: []
related_verifications:
  - "2026-05-29-21-analytics"
  - "2026-05-27-whitestream"

# Revision history
revision_history:
  - "2026-05-30 v1: Initial verification — EXCLUDED under the legacy-surveillance-brand-now-block-explorer pattern"

# Tags
tags:
  - verification
  - tier-na
  - usa
  - canada
  - north-america
  - excluded
  - surveillance-adjacent
  - legacy-brand
  - block-explorer
  - retrospective-research-value
---

> **Public sanitized verification record.** A research artifact from the SatoshiShield project, published to show the verification methodology applied to each candidate domain. Internal lab infrastructure has been redacted. Not legal or financial advice.


---
# Blockseer — Verification Record

**VERDICT: EXCLUDED FROM BLOCKLIST.**

Blockseer was an independent blockchain analytics and forensics firm founded in 2015 by Danny Yang (Stanford CS PhD, founder of the Stanford Bitcoin Meetup) and headquartered in Palo Alto. Its original product was a graphical Bitcoin transaction explorer with forensic analysis features marketed to law enforcement (IRS, FBI, Secret Service per CBInsights and historical company profiles) and financial institutions. DMG Blockchain Solutions (TSX-V: DMGI), a Canadian publicly-traded Bitcoin mining and data center company, acquired Blockseer in March 2018 for approximately C$2.6 million in cash and 7.7 million DMG shares. Danny Yang became DMG's CTO.

Through 2019-2020, DMG continued to market Blockseer and a companion product called Walletscore commercially as forensic software to "law enforcement, regulators, legal firms and auditors" (per a 2019 GlobeNewswire press release). DMG also used Blockseer technology to launch a North America-based Bitcoin mining pool from its Blockseer subsidiary in October 2020.

In **August 2025**, DMG announced the **relaunch of Blockseer Explorer** as a *freely available* Bitcoin blockchain explorer targeted at "Bitcoin-native operators such as miners and self-custody treasuries." The relaunched product is explicitly positioned for operator self-service:

> "Explorer helps users track wallet activity, set alerts and export concise, spreadsheet-ready transaction data — with no coding, API setup or SQL required."

The product is free, GUI-only, has no API, and is targeted at operators monitoring their own treasury wallets — not at third-party surveillance of arbitrary users. DMG's most recent quarterly reports (Q1 2026, February 2026) confirm Blockseer Explorer remains free and continues to be invested in as part of DMG's "Digital Asset Software and Services" line, but the company's primary business is now Bitcoin mining and AI infrastructure (Christina Lake data center conversion), not blockchain surveillance.

The original `blockseer.com` domain is actively maintained as a Cloudflare-proxied brand asset rather than left as a passive parking page. WHOIS (Step 1) shows the domain was renewed in December 2025 and carries full four-lock domain status (clientDelete/Renew/Transfer/UpdateProhibited), indicating deliberate brand preservation. SSL inspection (Step 2) shows a Google Trust Services wildcard cert (apex + `*.blockseer.com` SANs), consistent with Cloudflare's customer cert provisioning pipeline given the Cloudflare nameserver delegation. DNS (Step 3) shows active Cloudflare proxying on both IPv4 and IPv6, plus an active Google Workspace email tenant. ZoomInfo's "currently teasing upcoming products and services... powered by GoDaddy. The exact nature of their offerings remains undisclosed" is best read as observational rather than diagnostic: the infrastructure is in place to serve whatever DMG chooses to put there. The Blockseer Facebook page's last activity was in December 2023, with no posts referencing forensic products.

This is a new pattern: a brand with a documented surveillance history that has been operationally retired or pivoted, with the surviving product reduced to a block explorer that is functionally indistinguishable from mempool.space or blockstream.info — both of which SatoshiShield explicitly does NOT block.

## Why it was evaluated

Blockseer surfaced as a Tier 2 candidate during initial scoping of historic blockchain analytics firms. Characteristics making the firm worth investigating:

- Documented surveillance history: IRS, FBI, Secret Service customers
- Active brand still owned and invested in by a publicly-traded blockchain company (DMG)
- Two U.S. provisional patents related to blockchain-based data provenance and access control
- Companion forensic product (Walletscore) marketed alongside Blockseer in 2019

The current operational state, however, indicates retirement of the surveillance positioning.

---
## Step 1 — WHOIS Lookup — ✓ Complete

**Tool used:** `whois` CLI. Domain verified: `blockseer.com`.

**Findings — blockseer.com:**

| Field         | Value                                                                                  |
| ------------- | -------------------------------------------------------------------------------------- |
| Registrar     | GoDaddy.com, LLC (IANA 146)                                                            |
| Creation date | 2014-12-06                                                                             |
| Expiry        | 2026-12-06                                                                             |
| Last updated  | 2025-12-07 (renewed within the past six months)                                        |
| Registrant    | Redacted — Privacy proxy via Domains By Proxy, LLC (GoDaddy's default privacy service) |
| Nameservers   | NOOR.NS.CLOUDFLARE.COM, OLOF.NS.CLOUDFLARE.COM (Cloudflare DNS, not GoDaddy bundled)   |
| Domain status | clientDeleteProhibited, clientRenewProhibited, clientTransferProhibited, clientUpdateProhibited (full four-lock) |
| DNSSEC        | unsigned                                                                               |

**Notes:**

- **Domain age and pre-incorporation registration.** The domain was registered on 2014-12-06, approximately one month before Blockseer Inc. was founded in early 2015. Consistent with Danny Yang reserving the brand domain at the end of 2014 in preparation for founding the company. 11.5-year domain age.
- **Recent renewal contradicts a pure abandonment hypothesis.** The 2025-12-07 update reflects a renewal extending the domain through December 2026. DMG (the current registrant via the 2018 Blockseer acquisition) is actively paying to retain the domain. Whatever ZoomInfo describes as a "currently teasing upcoming products" state, it is not a domain being passively allowed to lapse.
- **DNS delegated to Cloudflare, not GoDaddy bundled DNS.** The domain is registered at GoDaddy but the DNS service is delegated to Cloudflare (NOOR/OLOF nameservers). This is more deliberate infrastructure than a true parking page would use — passively parked GoDaddy domains typically remain on GoDaddy's `*.domaincontrol.com` nameservers. The Cloudflare delegation means there is active DNS configuration in place, likely with the domain either proxied behind Cloudflare or with deliberately-managed DNS records pointing elsewhere. Step 2 and Step 3 will resolve which.
- **Full four-lock domain status is unusual and operationally significant.** All four client-side locks are set: `clientDeleteProhibited`, `clientRenewProhibited`, `clientTransferProhibited`, and `clientUpdateProhibited`. The transfer and update locks are common (basic security hygiene). The `clientDeleteProhibited` and `clientRenewProhibited` locks together require an explicit registrar unlock procedure even to renew or delete the domain — a configuration typically reserved for high-value brand assets being deliberately preserved against accidental loss. This is more consistent with DMG holding the domain as a brand-protection asset than with active surveillance API operation, but is also stronger evidence than passive parking.
- **Privacy proxy on registration.** Domains By Proxy is GoDaddy's default proxy service. Not material to the verdict but consistent with the established pattern of corporate-owned domains shielding registrant details from public WHOIS.
- **DNSSEC unsigned.** Consistent with the general infrastructure-security-culture pattern observed across the verification cycle — most crypto-surveillance vendors and adjacent firms have not deployed DNSSEC. Not a meaningful signal.

**Conclusion:** Step 1 findings reinforce the EXCLUDED verdict but refine the operational state framing. The domain is not a true parking page — it is an actively-managed, actively-renewed, four-lock-protected brand asset under Cloudflare DNS delegation. DMG is preserving the asset rather than abandoning it. This is consistent with the August 2025 Blockseer Explorer relaunch being part of a longer-term brand strategy. The revisit trigger documented in the verification record (paid forensic product relaunch under the Blockseer brand or active surveillance API at `blockseer.com`) remains the right escalation condition.

---
## Step 2 — SSL Certificate — ✓ Complete

**Tool used:** `openssl s_client` to retrieve and inspect TLS cert chain on `blockseer.com:443`.

**Findings:**

| Field         | Value                                                                                       |
| ------------- | ------------------------------------------------------------------------------------------- |
| Issuer        | C=US, O=Google Trust Services, CN=WE1                                                       |
| Subject       | CN=blockseer.com (DV cert; no O= field naming DMG or any successor entity)                  |
| SAN coverage  | blockseer.com, *.blockseer.com (apex + wildcard)                                            |
| Validity      | Expires 2026-07-17 22:54:20 UTC (≈7 weeks remaining; standard short-lived rotation)         |

**Notes:**

- **Google Trust Services WE1 issuer is the Cloudflare cert signal.** GTS WE1 is one of the intermediate CAs Cloudflare uses for automated cert provisioning on proxied customer domains. Combined with the Cloudflare nameserver delegation observed in Step 1, this strongly indicates the domain is configured behind Cloudflare's reverse proxy, with Cloudflare automatically provisioning and rotating the cert through GTS. Step 3 DNS A records will confirm whether the apex resolves to Cloudflare's edge IP ranges.
- **DV-tier cert with no corporate identity.** Subject contains only the common name; no `O=` field naming DMG Blockchain Solutions or any other entity. This is standard for automated DV cert provisioning and consistent with Cloudflare's free / Pro tier customer cert tooling. Not a meaningful signal beyond confirming the automation pathway.
- **Wildcard SAN covering `*.blockseer.com` is operationally significant.** A wildcard cert is provisioned only when subdomain serving is intended or anticipated. A true parking page typically only requires apex coverage. The wildcard tells us the configuration anticipates serving content from arbitrary subdomains — either deliberately set up that way during the August 2025 Blockseer Explorer relaunch, or as Cloudflare's default wildcard provisioning behavior on proxied plans. Either way, the infrastructure is configured for more than a static apex placeholder.
- **Short-lived cert validity reflects standard Cloudflare rotation cadence.** Cloudflare provisions and rotates GTS-issued certs on a ~90-day cycle. The current cert was issued in mid-April 2026 and expires mid-July 2026. Auto-renewal is presumably configured. Not a signal about the domain's operational state beyond confirming the cert pipeline is actively running.
- **No surveillance-product subdomain enumeration visible in the cert.** Wildcard SANs by design hide the specific subdomain inventory. Subdomain enumeration via crt.sh historical cert logs would be needed to surface what was previously certificated — useful if Step 7 functional testing is ever performed against the current state of the domain, but not material to the EXCLUDED verdict.

**Conclusion:** Step 2 reinforces the Step 1 observation that `blockseer.com` is an actively-managed, Cloudflare-proxied domain rather than a true parking page. The wildcard cert coverage points to infrastructure prepared for subdomain serving. Combined with the recent renewal and four-lock domain status, the overall picture is one of deliberate brand asset preservation with active infrastructure plumbing in place — consistent with the August 2025 Blockseer Explorer relaunch being a real product strategy rather than a brand-archive footnote. The EXCLUDED verdict still holds because nothing in the cert evidence indicates an active surveillance API surface; the current configuration is compatible with serving a free public block explorer at `blockseer.com` or subdomains, which is not in SatoshiShield's inclusion criteria.

---
## Step 3 — SecurityTrails / Passive DNS — ✓ Complete

**Tool used:** `dig` CLI for current DNS records (A, AAAA, MX). NS records previously captured in Step 1 WHOIS. SecurityTrails historical lookup deferred — not material to the EXCLUDED verdict, but could be useful in a future revisit cycle if the domain's serving state changes.

**Findings:**

| Record | Value |
|---|---|
| A | 172.67.130.94, 104.21.8.49 (Cloudflare anycast proxy IPs) |
| AAAA | 2606:4700:3032::ac43:825e, 2606:4700:3036::6815:831 (Cloudflare IPv6 anycast) |
| MX | 1 aspmx.l.google.com; 5 alt1/alt2.aspmx.l.google.com; 10 aspmx2/aspmx3.googlemail.com (standard Google Workspace tenant) |
| NS | noor.ns.cloudflare.com, olof.ns.cloudflare.com (Cloudflare DNS, from Step 1) |

**Notes:**

- **Cloudflare reverse-proxy active on both IPv4 and IPv6.** The A records (172.67.130.94 in Cloudflare's 172.64.0.0/13 range; 104.21.8.49 in 104.16.0.0/12) and the AAAA records (both in Cloudflare's 2606:4700::/32 IPv6 allocation) are anycast proxy endpoints. Whatever content `blockseer.com` is serving passes through Cloudflare's edge rather than connecting directly to an origin server. This confirms the Step 2 cert observation (GTS WE1 wildcard cert) as Cloudflare-managed automation: Cloudflare terminates TLS at the edge, presents the GTS-issued cert, and proxies to a hidden origin.
- **Dual-stack proxying is consistent with Cloudflare default behavior, not bespoke configuration.** Cloudflare enables IPv6 proxying by default for free and paid plans; the dual-stack record set is not itself a meaningful signal beyond confirming the Cloudflare proxy pattern.
- **Active Google Workspace MX tenant is a meaningful operational signal.** Standard five-host Google Workspace configuration (priority 1 `aspmx.l.google.com`, priority 5 `alt1/alt2.aspmx.l.google.com`, priority 10 `aspmx2/aspmx3.googlemail.com`). This is the same MX pattern documented in the Hudson Intelligence verification record. Email at `@blockseer.com` is actively routed and presumably read by someone at DMG — abandoned or pure-parking domains do not maintain Google Workspace tenants (which carry a monthly per-seat cost). Combined with the December 2025 domain renewal observed in Step 1, the picture is one of active corporate stewardship rather than passive brand-archive holding.
- **No surveillance-vendor co-resolution signal.** The Cloudflare proxy IPs are shared across millions of customer domains globally; not meaningful signals. What would be meaningful — surveillance-vendor nameservers, surveillance-vendor IP co-residency, or a direct AWS/Azure backend pointing at a forensics product — is absent.
- **No subdomain enumeration via Step 3.** The wildcard cert observed in Step 2 hides the actual subdomain inventory, and a `dig` query against the apex only returns the apex resolution. If a future revisit cycle is triggered, crt.sh historical cert log enumeration would surface any subdomains that have been certificated under `*.blockseer.com`, which would reveal whether DMG has deployed (or is preparing to deploy) operationally-meaningful subdomains beyond the apex.

**Conclusion:** DNS findings complete the operational portrait. `blockseer.com` is an actively-Cloudflare-proxied domain with an active Google Workspace email tenant, full four-lock domain status (Step 1), and a wildcard cert provisioned through Cloudflare's GTS pipeline (Step 2). This is not a parking page. It is a deliberately-maintained brand asset with the full corporate infrastructure plumbing required to deploy content quickly. The EXCLUDED verdict remains correct because nothing in the infrastructure indicates a surveillance API surface — the configuration is fully compatible with serving a free public block explorer or a "coming soon" page, neither of which meets SatoshiShield's inclusion criteria. The revisit trigger discipline documented in the verification record is operationally appropriate: if DMG ever deploys a paid forensic product behind this Cloudflare infrastructure, the operational state could flip within days, and the verification should be re-opened.

---
## Step 4 — Behavioral Evidence — COMPLETE (vendor documentation route)

Per Contributor Guide v1.4 §4.4, vendor-documentation route applied.

**Current product positioning (DMG press release, August 6, 2025):**
> "DMG announces it has relaunched Blockseer Explorer, which is part of DMG Blockchain's digital asset software suite and is a product tailored to a specific and underserved segment of the market: Bitcoin-native operators such as miners and self-custody treasuries. Explorer helps users track wallet activity, set alerts and export concise, spreadsheet-ready transaction data — with no coding, API setup or SQL required."

**Current domain state (ZoomInfo company profile, as of 2026):**
> "Blockseer is a company that is currently teasing upcoming products and services aimed at enhancing user experience. They are known for leveraging advanced technology and are powered by GoDaddy. The exact nature of their offerings remains undisclosed..."

**Historical positioning (DMG press release, August 20, 2019) — included for context, not as current evidence:**
> "DMG's COO Sheldon Bennett, a Certified Fraud Examiner (CFE) himself, leads audit efforts and uses DMG's proprietary software, Blockseer and Walletscore, to review crypto wallet activities, blockchain transactions and analyze crypto revenues... DMG is in a unique position to help law enforcement, regulators, legal firms and auditors navigate the blockchain ecosystem."

**Parent company business profile (DMG Q1 2026 financial results):**
> "DMG is a publicly traded and vertically integrated blockchain and data center technology company that manages, operates and develops end-to-end digital solutions to monetize the digital asset and artificial intelligence compute ecosystems."

DMG's stated strategic focus through 2025-2026 is on Bitcoin mining hashrate growth and converting facilities (Christina Lake) into AI data centers, not blockchain forensics. The forensics positioning is no longer prominent in the company's investor communications.

---
## Step 5 — Privacy Harm Assessment

The current operational footprint of `blockseer.com` does not create user-layer privacy harm that DNS-level blocking would meaningfully mitigate:

1. The domain appears to host a minimal placeholder rather than an active surveillance API
2. The relaunched Blockseer Explorer product is positioned for operator self-service, with no API surface and no marketing language indicating third-party surveillance use
3. The original forensic products (Blockseer/Walletscore enterprise) appear to have been wound down or are no longer the active product line
4. DMG's current business model derives revenue from Bitcoin mining and AI infrastructure, not from blockchain surveillance subscriptions

This is functionally analogous to mempool.space and blockstream.info: a public block explorer that incidentally logs HTTP requests in the standard web-server sense but does not operate an IP-to-address surveillance correlation business.

## Step 6 — Inclusion Criteria — DOES NOT MEET

Applying the six SatoshiShield inclusion criteria to the *current* operational footprint:

- [ ] **Blockchain Analytics firm** — parent (DMG) primary business is mining and AI data centers; Blockseer Explorer product is a free block explorer
- [ ] **Address Screening API** — no API; product is explicitly GUI-only ("no coding, API setup or SQL required")
- [ ] **IP-Logging Infrastructure** — no documented IP-to-address correlation business; current marketing makes no reference to risk scoring or attribution
- [ ] **KYC/AML Intelligence** — historical Walletscore product appears wound down; no current public marketing of compliance intelligence
- [ ] **Wallet Telemetry** — not a wallet vendor
- [ ] **Deanonymization Platform** — historical Blockseer (2015-2019) had this positioning; current product does not

**Zero of six criteria met under current operational state.** The historical surveillance positioning is documented and real but no longer reflects the active product or the parent company's strategic direction.

## Step 7 — Functional Impact Test — NOT REQUIRED

The conclusion is reached at Step 6 without functional testing.

If Step 7 were performed, it would test whether blocking `blockseer.com` impairs any legitimate Bitcoin wallet or operator workflow. Given the domain's current minimal state, the test would likely confirm zero impact in either direction (no surveillance to block, no functionality to break).

## Pattern observations

Blockseer establishes a **third exclusion pattern** distinct from the two already documented:

- **Whitestream pattern (training vendor):** firm operates in the surveillance ecosystem but their product is training and methodology dissemination, not surveillance infrastructure
- **21 Analytics pattern (on-premises software):** firm operates surveillance-adjacent software but delivers it as on-premises product with zero telemetry, removing any direct user-layer query surface
- **Blockseer pattern (legacy-surveillance-brand-now-block-explorer):** firm had a documented surveillance history that has been operationally retired; the surviving product is a public block explorer functionally indistinguishable from mempool.space; the domain may be in a placeholder or wind-down state

This pattern matters for future research: not every firm with a surveillance history warrants permanent inclusion. The inclusion criteria require evidence of *current* surveillance harm, not historical positioning. If a firm has pivoted and the active product no longer meets criteria, the exclusion is the correct call — even when the brand was once a clear surveillance vendor.

**Revisit trigger:** if DMG or any successor entity relaunches a paid forensic product under the Blockseer brand, or if `blockseer.com` begins serving an active surveillance API, this verification should be re-opened.

## Verification status

| Step                      | Status         | Outcome                                                                                                                       |
| ------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| 1. WHOIS                  | ✓ Complete     | GoDaddy registrar, Cloudflare NS, 2014 creation, full four-lock, renewed Dec 2025 — active brand asset                        |
| 2. SSL certificate        | ✓ Complete     | GTS WE1 DV cert via Cloudflare, wildcard `*.blockseer.com`, standard 90-day rotation                                          |
| 3. SecurityTrails         | ✓ Complete     | Cloudflare proxy on both A and AAAA; active Google Workspace MX; no surveillance-vendor co-resolution                         |
| 4. Behavioral evidence    | ✓ Complete     | Current product is free public block explorer; domain appears placeholder; parent strategic focus shifted away from forensics |
| 5. Privacy harm           | ✓ Complete     | No active user-layer query surface meeting inclusion criteria                                                                 |
| 6. Inclusion criteria     | ✓ Complete     | **MEETS 0 of 6 CRITERIA — EXCLUDE**                                                                                           |
| 7. Functional impact test | — Not required | —                                                                                                                             |

**Final verdict:** EXCLUDED FROM BLOCKLIST. Record preserved as historical research artifact under the legacy-surveillance-brand-now-block-explorer exclusion pattern. Revisit if DMG relaunches commercial forensics under the Blockseer brand or if `blockseer.com` begins serving an active surveillance API.
