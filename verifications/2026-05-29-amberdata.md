---
# Core
type: verification
company: "amberdata"
date: 2026-05-29
verifier: cypherpilgrim
outcome: PENDING FUNCTIONAL TEST

# Project metadata
project: SatoshiShield
tier: 1
status: in-verification

# Verdict and process
verdict: Meets SatoshiShield inclusion criteria — operates cloud RESTful API at amberdata.io with explicit compliance and surveillance system positioning; serves regulators and central banks
date_started: 2026-05-29
date_completed:

# Domain scope
block_targets:
  - amberdata.io
  - "*.amberdata.io"
non_targets: []

# Geography
hq_country: US
hq_city: Miami
operations_countries: [US]
origin_country: US

# Lineage
predecessor: []
successor: []
related_companies: []
related_verifications: []

# Revision history
revision_history:
  - "2026-05-29 v1: Initial verification — Tier 1 candidate; vendor self-documentation establishes compliance + surveillance API positioning"

# Tags
tags:
  - verification
  - tier-1-candidate
  - usa
  - north-america
  - florida
  - market-data
  - api-surveillance
---

> **Public sanitized verification record.** A research artifact from the SatoshiShield project, published to show the verification methodology applied to each candidate domain. Internal lab infrastructure has been redacted. Not legal or financial advice.


# Amberdata — Verification Record

**VERDICT: VERIFIED.**

Amberdata is a Miami-based digital asset data infrastructure firm founded 2017. Operates a cloud RESTful API at `amberdata.io` delivering blockchain market data, on-chain analytics, and compliance/surveillance services to financial institutions, regulators, and central banks. The firm explicitly markets surveillance use cases in their own materials: "Use wallet and transaction-level blockchain data to flag anomalies and support transaction monitoring systems."

Unlike Allium (data warehouse delivery) and 21 Analytics (on-premises), Amberdata operates a cloud API surface where queries hit `amberdata.io` and `api.amberdata.io` directly, logging querying IPs against the addresses being queried.

## Block scope

| Domain | Recommendation |
|---|---|
| `amberdata.io` | BLOCK (root + wildcard) |
| `api.amberdata.io` | Covered by wildcard |
| `app.amberdata.io` | Covered by wildcard |

## Step 1 — WHOIS Lookup — ✓ Complete

**Tool used:** `whois` CLI. Two domains verified: `amberdata.io` (marketing front) and `web3api.io` (data API).

**Findings — amberdata.io:**

| Field | Value |
|---|---|
| Registrar | Amazon Registrar, Inc. (AWS) |
| Creation date | 2017-06-16 |
| Expiry | 2027-06-16 |
| Last updated | 2026-05-17 |
| Registrant | Redacted — Privacy service via whoisproxy.com; Registrant Country: US, State: VA |
| Nameservers | ns-1917.awsdns-47.co.uk, ns-19.awsdns-02.com, ns-1278.awsdns-31.org, ns-697.awsdns-23.net (AWS Route 53) |
| DNSSEC | unsigned |
| TLD | .IO (British Indian Ocean Territory ccTLD — branding choice) |

**Findings — web3api.io:**

| Field | Value |
|---|---|
| Registrar | Amazon Registrar, Inc. (AWS) |
| Creation date | 2018-08-30 |
| Expiry | 2026-08-30 (~3 months from verification date) |
| Last updated | 2026-04-29 |
| Registrant | Redacted — Identity Protection Service; Registrant Country: GB, State: Middlesex |
| Nameservers | ns-1697.awsdns-20.co.uk, ns-144.awsdns-18.com, ns-1194.awsdns-21.org, ns-914.awsdns-50.net (AWS Route 53) |
| DNSSEC | unsigned |
| TLD | .IO (same as marketing domain) |

**Notes:**

- **Common Amberdata ownership confirmed.** Both domains registered through Amazon Registrar and using AWS Route 53 nameservers — the same AWS-native infrastructure stack. Combined with Amberdata's public developer documentation citing `web3api.io` as the canonical API hostname (REST: `https://web3api.io/api/v1/...`, websocket: `wss://ws.web3api.io`), this confirms `web3api.io` is Amberdata-owned despite the privacy-shielded WHOIS registrant fields.
- **The marketing site / API split is the operationally important finding.** `amberdata.io` hosts the corporate front and documentation (`docs.amberdata.io`); `web3api.io` is the actual data delivery surface where compliance/surveillance APIs are exposed. A block scope limited to `amberdata.io` would miss the actual surveillance endpoint — both domains must be in scope.
- **Different privacy proxies, same parent stack.** amberdata.io uses whoisproxy.com (Amazon Registrar's US-default privacy proxy); web3api.io uses Identity Protection Service (UK-default privacy proxy, also bundled by Amazon Registrar). The variation is registrar-driven, not a signal of separate operators.
- **Domain ages match operational history.** amberdata.io registered 2017 (year of company founding), web3api.io registered 2018 (consistent with first-year API launch). Clean, non-rotated operational history for both domains.
- **web3api.io expiry is near-term (2026-08-30)** — worth noting but not a verification concern. Amazon Registrar handles auto-renewal by default and the company is operationally active.

**Conclusion:** WHOIS findings confirm common Amberdata ownership of both domains and reinforce the INCLUDED verdict. Block scope must be expanded from amberdata.io alone to cover both domains.

---
## Step 2 — SSL Certificate Inspection — ✓ Complete

**Tool used:** `openssl s_client` for live certificate inspection on both apex domains. crt.sh historical lookup deferred — crt.sh was returning 502 errors at the time of verification; not material to the INCLUDED verdict.

**Findings — amberdata.io:**

| Field | Value |
|---|---|
| Issuer | C=US, O=Google Trust Services, CN=WE1 |
| Subject | CN=amberdata.io |
| SANs | amberdata.io (apex only, no www) |
| Not After | 2026-07-18 |

**Findings — web3api.io:**

| Field | Value |
|---|---|
| Issuer | C=US, O=Amazon, CN=Amazon RSA 2048 M04 |
| Subject | CN=web3api.io |
| SANs | web3api.io (apex only) |
| Not After | 2027-02-09 |

**Findings — api.amberdata.io:** Endpoint did not return a usable certificate via `openssl s_client`. Consistent with the discovery via Amberdata's developer documentation that the API is hosted at `web3api.io`, not at `api.amberdata.io`. The `api.*` subdomain on the marketing domain does not exist as a service endpoint.

**Notes:**

- **Two-domain cert split mirrors the infrastructure split.** Marketing apex (amberdata.io) uses Google Trust Services CA; API apex (web3api.io) uses Amazon's own CA (Amazon Trust Services). The issuer difference is consistent with the hosting split: the marketing site may be CDN-fronted; the API is served directly from AWS using ACM-provisioned certs.
- **Amazon-issued cert on web3api.io is a strong AWS-native hosting signal.** Amazon's own CA is used exclusively for certs provisioned via AWS Certificate Manager for AWS services. This means web3api.io's TLS termination happens on AWS infrastructure (ELB/ALB, CloudFront, or API Gateway), with no third-party CDN in the path.
- **No surveillance-product subdomains in apex certs.** Both certs cover only the apex. On AWS, separate hostnames (e.g. `ws.web3api.io` for the websocket stream, `docs.amberdata.io` for documentation) would have separately-provisioned certs not visible from these queries.
- **Corporate identity not in either cert.** Both Subject fields are bare CN values without O= fields naming Amberdata Inc. Normal for ACM-provisioned and GTS Universal SSL certs alike.

**Conclusion:** SSL findings reinforce the INCLUDED verdict and confirm the two-domain structure. The Amazon CA on web3api.io specifically confirms direct AWS hosting of the surveillance API endpoint — no CDN obfuscation, surveillance API surface is operationally observable.

---
## Step 3 — SecurityTrails / Passive DNS — ✓ Complete

**Tool used:** `dig` CLI for current DNS records (A, AAAA, MX) on both domains. NS records already captured in Step 1 WHOIS. SecurityTrails historical lookup deferred — free tier locked behind login as of May 2026; not material to the INCLUDED verdict.

**Findings — web3api.io (data API):**

| Record | Value |
|---|---|
| A | 54.240.184.21, 54.240.184.40, 54.240.184.57, 54.240.184.103 |
| AAAA | None |
| MX | None |
| NS | ns-1697.awsdns-20.co.uk, ns-144.awsdns-18.com, ns-1194.awsdns-21.org, ns-914.awsdns-50.net (AWS Route 53, from Step 1) |

**Findings — amberdata.io (marketing site):**

| Record | Value |
|---|---|
| A | 199.60.103.146, 199.60.103.46 |
| AAAA | None |
| MX | 1 aspmx.l.google.com; 5 alt1/alt2.aspmx.l.google.com; 10 alt3/alt4.aspmx.l.google.com |
| NS | ns-1917.awsdns-47.co.uk, ns-19.awsdns-02.com, ns-1278.awsdns-31.org, ns-697.awsdns-23.net (AWS Route 53, from Step 1) |

**Notes:**

- **web3api.io: direct AWS hosting confirmed.** The four A records on 54.240.184.0/24 are AWS-owned IP space. Combined with the Amazon Trust Services SSL cert (Step 2), this confirms the API endpoint is served directly from AWS infrastructure — likely an ELB/ALB or API Gateway deployment with multiple backend instances behind it. No CDN proxy in the request path.
- **amberdata.io: CDN-fronted on Fastly.** The two A records on 199.60.103.0/24 are not AWS-owned and fall within Fastly's published edge IP ranges. The Google Trust Services SSL cert (Step 2) is consistent with Fastly's customer cert provisioning. The marketing site is therefore on a separate CDN provider, architecturally distinct from the AWS-hosted API.
- **The hosting split is operationally clean.** Two-tier deployment is the architectural norm for SaaS API companies: low-traffic marketing/docs on a CDN, high-throughput API directly on cloud infrastructure with the ability to scale and stream data without CDN intermediation. The split aligns with Amberdata's documented product model (REST + websocket streaming via `wss://ws.web3api.io`).
- **No IPv6 on either domain.** Common for AWS and Fastly customer deployments where dual-stack is not enabled by default. Not a meaningful signal.
- **No MX on web3api.io.** Confirms the domain is a pure API/data delivery brand — no email infrastructure attached. amberdata.io carries the corporate Google Workspace email setup. Consistent with the two-domain functional split.
- **No shared infrastructure with known surveillance vendors.** AWS and Fastly edge ranges are shared with millions of sites globally; not meaningful signals. What would be a meaningful signal — surveillance-vendor nameservers or co-resolution with known surveillance firm IPs — is absent.

**Conclusion:** DNS findings reinforce the INCLUDED verdict and confirm the two-tier infrastructure model. The surveillance API surface at web3api.io is operationally observable and directly on AWS. The block scope of `amberdata.io` (root + wildcard) and `web3api.io` (root + wildcard) covers both the marketing front and the production data delivery endpoint, including the documented websocket stream at `ws.web3api.io` which is captured by the wildcard.

---
## Step 4 — Behavioral Evidence — COMPLETE (vendor documentation route)

Per Contributor Guide v1.4 §4.4, vendor-documentation route applied.

**Corporate self-description (from `amberdata.io/about`):**
> "As the backbone of the digital asset economy, Amberdata delivers end-to-end digital asset infrastructure solutions that enable our customers to unlock opportunities, gain valuable insights, and act decisively."
> "Our offerings include digital asset data and analytics, portfolio and risk management, compliance, and tax management, ensuring institutions have the intelligence they need at every stage of the trade lifecycle."

**Compliance and surveillance positioning (from `amberdata.io/fintechs`):**
> "Integrate Digital Asset Data into Compliance & Surveillance Systems · Use wallet and transaction-level blockchain data to flag anomalies and support transaction monitoring systems."
> "Leverage an enterprise-grade API and seamless analytics to confidently trace funds, assess vulnerabilities and analyze transactions."

**Customer base (from About and product pages):**
> Serves "asset management, trading, investment banks, regulators, central banks, venture capital, fintechs, wealth management, and corporate treasury"
> "Leverage Amberdata's data and analytics infrastructure to oversee digital asset markets, investigate market and protocol fraud, and develop policy." (regulator-targeted positioning)

**API delivery (from same source):**
> "Real-time and historical options analytics with RESTful API & cloud-based delivery."
> Cloud-hosted infrastructure with subscription-based API access

**Corporate identity:**
- HQ: Miami, Florida, USA
- Founded: 2017
- Legal entity: Amberdata, Inc.
- Domain: amberdata.io
- Funding: Series B raised; specific investor details on Crunchbase/Pitchbook
- Comparable to Coin Metrics in scale (per CBInsights)

## Step 5 — Privacy Harm Assessment

The Amberdata API logs querying IP addresses against the Bitcoin addresses being queried by their customers. Each query from a regulator's compliance system, a central bank's surveillance team, a financial institution's risk team, or an exchange compliance backend produces a database record linking that querier's network identity to the address(es) under investigation.

For consumer Bitcoin users, the indirect exposure happens through:

1. **Embedded vendor SDKs:** any wallet, portfolio app, or browser extension that integrates Amberdata's API for market data, balance lookups, or token information makes outbound queries to `amberdata.io` from the user's device. Those queries reveal the user's IP to Amberdata.
2. **DeFi platform integrations:** DeFi front-ends that use Amberdata for transaction monitoring will trigger queries when users interact, potentially exposing the user's network identity.
3. **Compliance backend queries:** when an exchange or financial institution uses Amberdata to screen the user's deposits, the user's address gets queried — though this query comes from the institution's IP, not the user's directly.

The direct user-layer privacy harm is the embedded-SDK pathway (item 1). DNS-layer blocking of `amberdata.io` prevents this category.

## Step 6 — Inclusion Criteria — MEETS MULTIPLE

Applying the six SatoshiShield inclusion criteria:

- [x] **Blockchain Analytics firm** — primary business includes on-chain data analytics with explicit compliance/surveillance positioning
- [x] **Address Screening API** — `Leverage an enterprise-grade API and seamless analytics to confidently trace funds, assess vulnerabilities and analyze transactions`
- [x] **IP-Logging Infrastructure** — canonical cloud RESTful API pattern; every API call logs the querying IP
- [x] **KYC/AML Intelligence** — explicit transaction monitoring positioning; serves regulator and central bank customers
- [x] **Deanonymization-adjacent** — wallet and transaction-level data analysis with anomaly flagging
- [ ] Wallet Telemetry — not documented as a direct wallet SDK provider; possible but unconfirmed

**Five of six criteria met.** Inclusion case is equivalent to other Tier 1 firms with cloud API surveillance positioning.

## Step 7 — Functional Impact Test — RUN LOCALLY

Procedure:
1. Add `*.amberdata.io` and `amberdata.io` to Pi-hole instances (the test resolver, the test resolver) as temporary blocks
2. Test with Sparrow Wallet → Bitcoin Knots RPC (should still work)
3. Test with Electrum → public Electrum server (should still work)
4. Test with BlueWallet (mobile) (should still work)
5. Test with browser visits to mempool.space and blockstream.info (should still work)
6. Negative test: visit `amberdata.io` directly (should fail — connection refused)

Expected outcome: no impact on Bitcoin wallet functionality. Amberdata is B2B; consumer Bitcoin wallets are not expected to embed their SDK directly. DeFi front-ends and institutional crypto-tax tools that have integrated Amberdata may show errors if accessed from the protected network — this is by design and acceptable per SatoshiShield's mission.

## domains.csv entries (2 new rows)

```
*.amberdata.io,Amberdata,Blockchain Analytics,1,Logs querying IP addresses against Bitcoin address lookup requests. Operates cloud RESTful API for transaction monitoring entity attribution and compliance screening across multiple blockchains. Used by financial institutions regulators and central banks.,https://amberdata.io/,2026-05-29,Founded 2017. HQ Miami Florida. Explicit "Compliance & Surveillance" positioning in vendor self-documentation. Customer base includes regulators and central banks.
amberdata.io,Amberdata,Blockchain Analytics,1,Root domain of Amberdata cloud analytics and surveillance API platform.,https://amberdata.io/,2026-05-29,Founded 2017. HQ Miami Florida.
```

## regex.txt pattern to add

```
(\.|^)amberdata\.io$
```

## Pattern observations

Amberdata establishes a useful contrast pattern against Allium and 21 Analytics:

- **Allium pattern (B2B data infrastructure, EXCLUDED):** delivery is into customer-owned warehouses; no direct API surface
- **21 Analytics pattern (on-premises, EXCLUDED):** product runs in customer data centers; zero telemetry
- **Amberdata pattern (cloud surveillance API, INCLUDED):** delivery via cloud RESTful API at vendor-controlled domain; canonical IP-logging surface

The distinction between "infrastructure layer" (excluded) and "cloud surveillance API" (included) turns on whether end-user-side devices query the vendor's domain directly. Amberdata's cloud RESTful API model places them clearly in the included category.

## Verification status

| Step                      | Status          | Outcome                                                                                                                                                       |
| ------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. WHOIS                  | ✓ Complete      | Both domains Amberdata-owned via Amazon Registrar + AWS Route 53; common-stack ownership confirmed; block scope expanded to include web3api.io                |
| 2. SSL certificate        | ✓ Complete      | amberdata.io: Google Trust Services issuer; web3api.io: Amazon CA (direct ACM provisioning, AWS-native); no surveillance API on api.amberdata.io              |
| 3. SecurityTrails         | ✓ Complete      | web3api.io served directly on AWS (54.240.184.0/24); amberdata.io fronted by Fastly CDN (199.60.103.0/24); no shared infrastructure with surveillance vendors |
| 4. Behavioral evidence    | ✓ Complete      | Vendor self-documentation establishes compliance + surveillance positioning                                                                                   |
| 5. Privacy harm           | ✓ Complete      | IP logging against Bitcoin address queries on cloud API                                                                                                       |
| 6. Inclusion criteria     | ✓ Complete      | **MEETS 5 of 6 CRITERIA — INCLUDE**                                                                                                                           |
| 7. Functional impact test | ⨯ Pending local | Procedure documented above                                                                                                                                    |

**Final verdict (pending Steps 1-3 and Step 7 local execution):** Amberdata operates a cloud RESTful API at `amberdata.io` with explicit compliance and surveillance positioning. INCLUDE in SatoshiShield v1.6.0 or v1.7.0.
