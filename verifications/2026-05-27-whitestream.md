---
# Core
type: verification
company: "whitestream"
date: 2026-05-27
verifier: cypherpilgrim
outcome: EXCLUDED FROM BLOCKLIST

# Project metadata
project: SatoshiShield
tier: "N/A (excluded)"
status: excluded

# Verdict and process
verdict: Does not meet SatoshiShield inclusion criteria — boutique training and investigation services firm; surveillance-adjacent but not user-layer harm
date_started: 2026-05-27
date_completed: 2026-05-27

# Domain scope
block_targets: []
non_targets:
  - whitestream.io (does not meet inclusion criteria)

# Geography
hq_country: IL
operations_countries: [IL, US]
origin_country: IL

# Lineage
predecessor: []
successor: []
related_companies:
  - "bigg-digital"
  - "slowmist"
related_verifications:
  - "2026-05-26-bigg-digital"
  - "2026-05-27-slowmist"
context_file: "SatoshiShield_Industry_Context_Notes"

# Revision history
revision_history:
  - "2026-05-27 v1: Initial verification — incorrectly recommended Tier 1 inclusion on surveillance-adjacent grounds"
  - "2026-05-27 v2: Corrected — applied inclusion criteria first; concluded exclusion. Research redirected to SatoshiShield_Industry_Context_Notes.md"

# Tags
tags:
  - verification
  - tier-na
  - excluded
  - israel
  - law-enforcement
  - surveillance-adjacent
  - retrospective-research-value
---

> **Public sanitized verification record.** A research artifact from the SatoshiShield project, published to show the verification methodology applied to each candidate domain. Internal lab infrastructure has been redacted. Not legal or financial advice.


# Whitestream — Verification Record

**VERDICT: EXCLUDED FROM BLOCKLIST.**

Whitestream does not meet SatoshiShield's stated inclusion criteria. No domain is recommended for the blocklist. Research observations of white-paper value are preserved in `SatoshiShield_Industry_Context_Notes.md` (Entry 1).

This record documents the verification process that reached the exclusion conclusion, including the WHOIS and SecurityTrails findings (which remain factually valid). The corporate identity, infrastructure, and partnership observations are preserved both for project transparency and as input to white-paper drafting on the surveillance industry's structural maturation.

## Block scope: NONE

| Domain | Recommendation |
|---|---|
| `whitestream.io` | NOT BLOCKED |

## Step 1 — Corporate identity, products, customers ✓ COMPLETE

### Corporate entity

| Field | Value |
|---|---|
| Brand name | whitestream (also "Whitestream - Blockchain Intelligence") |
| HQ | Tel Aviv, Israel |
| Founded | 2018 (per Tracxn); domain registered 2016-10-28, suggesting informal pre-incorporation operations from 2016 |
| Founders | Uri Bornstein (Co-Founder), Itsik Levy (Co-Founder & CEO) |
| Employees | 2 (as of July 2024 per Tracxn) |
| Funding | Unfunded — no VC raised |
| Website builder | Wix.com (Wix.com Website Builder per page metadata) |
| Cloud backend | Google Cloud Platform (via Wix's hosting abstraction) |
| Email | Google Workspace |
| LinkedIn | linkedin.com/company/whitestream |
| Twitter | @whitestream5 |

### Product portfolio

Whitestream is a boutique training and investigation services firm. Their products fall in three categories:

**Training (primary revenue line):**
- Introduction to Blockchain and Cryptocurrency (entry-level course)
- Certified Blockchain and Cryptocurrency Investigator
- Smart Contracts and DeFi Specialist
- Regulators and Compliance Officers training
- Prosecutors training
- Tax Auditors training
- Operational Simulator for blockchain investigators (flagship interactive training, partnership with BIGG Digital Assets)
- Private lessons
- Cross-sectoral training

**Direct investigation services:**
- General blockchain investigations
- Fraud detection
- Due diligence for crypto investors

**Incident response services:**
- Ransomware attack response
- Security breach analysis

**Trusted Partners Program:** White-label distribution model for tech vendors to deliver Whitestream training under their own brands.

### Self-positioning

Explicit marketing language from whitestream.io: *"Our training is fully tool-agnostic. You'll learn investigation techniques and operational skills that can be applied using any commercial or open-source tools available to your agency."*

This positioning is significant for the exclusion decision (see Step 6) — Whitestream explicitly does not compete with the tool vendors (Chainalysis, TRM Labs, Elliptic) on the surveillance product layer. Their business is one level up: training human investigators to use whatever tools their agency already has.

### Target customers

- Financial Intelligence Units (FIUs)
- Law Enforcement Agencies (LEAs)
- Regulators and compliance departments
- Governmental agencies
- Financial institutions
- Tax authorities
- Prosecutors

### Confirmed partnerships

- **BIGG Digital Assets / Blockchain Intelligence Group** — Operational Simulator partnership (June 2024 press release). BIGG is a SatoshiShield Tier 1 blocked candidate.
- **NICE Actimize X-Sight Marketplace** — member since September 2019. Provides indirect access to global banks via NICE Actimize's financial crime compliance integration platform.

### Israeli national security context

- **NBCTF** (National Bureau of Terrorist Financing) — Whitestream publishes detailed analyses of NBCTF seizure orders within weeks of issuance. NBCTF data flows downstream into SlowMist MistTrack (which integrates NBCTF as one of three sanction list sources alongside OFAC and UK HMT).
- **US Treasury / OFAC** — Whitestream publicly supports Treasury sanctions announcements and likely contributes intelligence inputs.

### Notable investigations (publicly attributed by Whitestream)

- 2019 Hamas crypto fundraising via Coinbase exchange exposure
- 2019 ISIS Bitcoin donation tracking before Sri Lanka bombings (Globes coverage)
- Binance involvement in Hamas terror financing (October 7 context)
- Whitestream's LinkedIn publishes specific Bitcoin transaction hashes attributed to Hamas and the Izz Adin Al Qassam Brigades

## Step 2 — WHOIS lookup ✓ COMPLETE

**Source:** Command-line `whois whitestream.io`, May 27, 2026

| Field | Value |
|---|---|
| Registrar | NameCheap, Inc. (IANA 1068) |
| Registrant Organization | Redacted for Privacy Purposes (NameCheap basic redaction — no Iceland privacy proxy) |
| Registrant Country | IL (visible through redaction) |
| Creation Date | 2016-10-28 (2 years before reported 2018 founding — suggests informal pre-incorporation operations) |
| Registry Expiration | 2026-10-28 (5 months out — shortest forward registration in the cohort) |
| Nameservers | dns1/dns2.registrar-servers.com (NameCheap bundled DNS, operated by Neustar Security Services) |
| Lock flags | `Domain Status: ok` — ZERO locks |
| DNSSEC | Unsigned |

The factual findings are unchanged from the original verification — bootstrap-tier registration profile across every measurable metric (no locks, retail registrar, bundled DNS, basic redaction, short forward registration). These observations remain relevant for the white paper as documentation of the surveillance industry's operational floor, but do not constitute privacy harm to Bitcoin users in themselves.

## Step 3 — Subdomain enumeration ✓ COMPLETE

10 subdomains under whitestream.io (smallest total vendor footprint in the SatoshiShield cohort, per Step 4 confirmation). Most services are routed through paths on whitestream.io rather than discrete subdomains, consistent with Wix's single-domain architecture preferences.

## Step 4 — SecurityTrails / passive DNS ✓ COMPLETE

**Source:** SecurityTrails free-tier DNS records, May 27, 2026

| Field | Value |
|---|---|
| A records | 23.236.62.147 (Google LLC attribution — Wix.com hosting on Google Cloud) |
| AAAA records | None |
| MX | Google Workspace mixed legacy/modern (aspmx.l.google.com + alt1/alt2 + aspmx2/3.googlemail.com) |
| NS | dns1/dns2.registrar-servers.com (Neustar-operated) |
| SOA | hostmaster.registrar-servers.com, TTL 43200 (12 hours) |
| TXT | Single SPF only: `v=spf1 include:_spf.google.com ~all` (soft-fail) |
| Subdomain count | 10 (smallest total vendor footprint in cohort) |

The "Wix on Google Cloud" pattern resolves the apparent contradiction between page-metadata "Wix.com Website Builder" and ZoomInfo's "Google Cloud Web Serving" — Wix runs its customer hosting on Google Cloud Platform, so the IP attribution reads as Google but the actual hosting layer is Wix.

The minimal TXT records (single SPF only, no Microsoft/Atlassian/Mailjet/Freshdesk/Amazon SES/LLM verifications) and soft-fail SPF policy corroborate the bootstrap-tier operational profile observed in the WHOIS data.

## Step 5 — Behavioral analysis ✓ COMPLETE

### What does whitestream.io actually do in the context of normal Bitcoin user activity?

This is the critical question for the inclusion decision. The honest answer:

**whitestream.io functions as a marketing and training-portal website.** It does not receive Bitcoin-related queries from end-user devices in the normal course of Bitcoin usage.

Specifically, whitestream.io does NOT:

- Operate an address screening API that Bitcoin wallets query
- Operate a transaction risk-scoring endpoint that exchanges query
- Embed SDKs in Bitcoin wallet software that phone home
- Run a deanonymization platform that users query for address-to-identity attribution
- Provide a block explorer with backend API calls to surveillance infrastructure
- Process passive wallet telemetry from any Bitcoin wallet application
- Operate IP-logging infrastructure that records Bitcoin address lookups from end users

The only way a Bitcoin user's IP address is logged by Whitestream is if that user **deliberately browses whitestream.io** — typically to research the surveillance industry, read Whitestream's terror-financing publications, or sign up for one of their training courses (which are restricted to organized groups of FIU/LEA personnel, not individual Bitcoin users).

### Privacy harm produced by Whitestream — but NOT addressable by DNS blocking

Whitestream does produce real impact on Bitcoin user privacy. The impact is indirect:

1. **Intelligence production** — Whitestream's investigations and publications attribute specific Bitcoin transactions to designated terrorist organizations. These attributions flow into Israeli NBCTF seizure orders.

2. **Sovereign sanction list integration** — NBCTF data is integrated by SlowMist MistTrack (one of three sanction sources alongside OFAC and UK HMT) and likely other vendors.

3. **Downstream effect** — A Bitcoin user whose transaction interacts with attributed addresses may have their funds flagged when an exchange screens against MistTrack, OFAC, or NBCTF data.

4. **Law enforcement training** — Whitestream trains FIU/LEA investigators globally, improving the human layer of cryptocurrency surveillance. The training itself happens largely offline.

**Crucially, blocking whitestream.io prevents none of this.** The intelligence still gets produced. The training still happens. The NBCTF integration still occurs. The downstream flagging still happens via the tool vendors that ARE in the SatoshiShield blocklist (SlowMist MistTrack is blocked; that block prevents the user-facing surveillance API queries that operationalize Whitestream-originated intelligence).

### What does blocking whitestream.io actually accomplish?

Blocking `*.whitestream.io` would only prevent:

- A user from browsing Whitestream's marketing website
- A user from reading Whitestream's publications about Hamas/ISIS terror financing
- A user from signing up for Whitestream training (limited to FIU/LEA personnel anyway)
- A user from contacting Whitestream's investigation services

None of these are common Bitcoin user activities. SatoshiShield's mission is to prevent passive surveillance of Bitcoin users at the DNS layer — not to prevent users from browsing the marketing sites of surveillance-adjacent companies.

## Step 6 — Inclusion criteria — DOES NOT MEET CRITERIA

Applying each of the six SatoshiShield inclusion criteria from the white paper:

### Criterion 1: Blockchain Analytics firm
*"Operated by a company whose primary business is correlating Bitcoin addresses with real-world identities"*

**Does not apply.** Whitestream's primary business is training. Direct investigations are a secondary revenue line. They are not a blockchain analytics firm in the sense the white paper means (Chainalysis, Elliptic, TRM Labs).

### Criterion 2: Deanonymization Platform
*"A platform that publicly markets the ability to attach real identities to Bitcoin addresses"*

**Does not apply.** Whitestream publishes investigation results that include identified Bitcoin transaction attributions, but they do not operate a platform like Arkham Intelligence where users query for identity attribution. The publication is intelligence dissemination, not platform operation.

### Criterion 3: Address Screening API
*"An API endpoint used to score Bitcoin addresses for risk or compliance purposes"*

**Does not apply.** Whitestream does not operate an address screening API. They train investigators to use other vendors' screening APIs.

### Criterion 4: Wallet Telemetry
*"A domain receiving usage analytics, crash reports, or behavioral data from Bitcoin wallet software"*

**Does not apply.** No wallet software phones home to whitestream.io.

### Criterion 5: KYC/AML Intelligence
*"A compliance service used to flag Bitcoin transactions associated with privacy tools"*

**Does not apply directly.** Whitestream is accessible via NICE Actimize's marketplace but they do not operate a compliance flagging service themselves. The NICE Actimize relationship is a marketing distribution channel, not a compliance product Whitestream operates.

### Criterion 6: IP-Logging Infrastructure
*"Any endpoint that logs the querying IP address against Bitcoin address or transaction data"*

**Does not apply meaningfully.** whitestream.io logs visitor IPs to its marketing site like any website does, but it does not log IPs against Bitcoin address queries because no such queries exist in normal Bitcoin user activity directed at whitestream.io.

### Conclusion

**None of the six inclusion criteria cleanly applies to Whitestream.**

The original verification attempted to construct an inclusion case on the basis of:
- Surveillance industry partnerships (BIGG, NICE Actimize)
- Sovereign sanction list intelligence input (NBCTF)
- Cross-vendor ecosystem participation
- Law enforcement training in cryptocurrency surveillance

These are real activities with real impact on the surveillance industry's effectiveness, but they describe **surveillance-adjacent activity**, not the direct user-layer privacy harm that SatoshiShield's six criteria are designed to address.

Including Whitestream in the blocklist would require expanding SatoshiShield's criteria from "vendors that surveil Bitcoin users at the DNS layer" to "vendors that participate in the surveillance industry ecosystem." That expansion would:

1. Dilute the project's discipline by replacing measurable criteria (DNS-layer surveillance of Bitcoin users) with looser ones (ecosystem participation, partnerships, intelligence flows)
2. Weaken the case for blocking the vendors who DO directly surveil users — if the standard appears inflated, the strict cases become harder to defend
3. Set a precedent for further mission creep into any company adjacent to the surveillance industry

The Contributor Guide's explicit instruction applies: **"When in doubt, do not submit — ask in a GitHub issue first."** Whitestream is the canonical "when in doubt" case.

### Recommendation

- **Blocklist:** EXCLUDE
- **Context file:** Add as Entry 1 in `SatoshiShield_Industry_Context_Notes.md` (DONE)
- **White paper:** Use Whitestream as the documented example of the surveillance industry's "training tier" — useful context for the structural maturation argument without diluting the blocklist

## Step 7 — Functional impact test — N/A

No block recommended. No functional impact test required.

## Step 8 — domains.csv entry — N/A

No entry. Whitestream is not added to the SatoshiShield blocklist.

## Step 9 — Pull request — N/A

No PR submission. The Whitestream research is captured in `SatoshiShield_Industry_Context_Notes.md` for white-paper use only.

If community members propose Whitestream for inclusion in the future, this verification record and the context notes file together document the considered exclusion decision and the reasoning. A GitHub Issue (rather than a PR) would be the appropriate venue for any reconsideration.

## Lessons documented for verification discipline

This verification originally reached the wrong conclusion. The error was caught before submission, but the failure mode is worth documenting for future reference.

### The failure pattern

The original Step 6 constructed an inclusion case by introducing categories not in the white paper's criteria:
- "Surveillance Industry Training Vendor (UNIQUE PATTERN)"
- "Sovereign Sanction Body Intelligence Input (CORROBORATING)"
- "Cross-Vendor Industry Federation (DOCUMENTED)"

None of these are SatoshiShield inclusion criteria. The case was built by expanding the criteria rather than by checking the candidate against them.

The original Step 5 also contained a sentence that should have triggered immediate reconsideration:

> *"A Bitcoin user's IP address is unlikely to be logged by Whitestream simply through normal Bitcoin usage"*

This sentence directly contradicts the inclusion case. It should have been the stopping point. Instead, the verification continued and constructed alternative justifications.

### The discipline going forward

1. **Criteria first.** Apply the six inclusion criteria from the white paper BEFORE building any case. If none cleanly applies, the verification stops at "exclude — does not meet criteria."

2. **Stopping sentences.** If the verification process produces a sentence that contradicts the inclusion case (like "unlikely to be logged through normal Bitcoin usage"), that sentence is the answer. Do not write around it.

3. **No category expansion.** Categories like "surveillance-adjacent," "ecosystem participant," or "intelligence producer" are not SatoshiShield criteria. Research that produces useful observations in these categories belongs in the context notes file, not the blocklist.

4. **"When in doubt, do not submit."** This Contributor Guide rule is a rule, not a suggestion. When the case requires construction rather than being self-evident, the answer defaults to exclude + context-notes.

## Pattern observations redirected to white paper context

The research observations of white-paper value from this verification are preserved in `SatoshiShield_Industry_Context_Notes.md` Entry 1. They include:

- The surveillance industry's structural maturation into specialized tiers (tool vendors, compliance integrators, training vendors, intelligence producers)
- The bootstrap-tier operational floor that mature SaaS infrastructure has enabled
- The cross-vendor data flow chain: Whitestream investigation → LinkedIn publication → NBCTF seizure order → SlowMist MistTrack integration → MistTrack API queries → global Bitcoin address flagging
- The Israeli surveillance industry tier (boutique specialist firms with government-adjacent positioning)
- The publication-as-product pattern (intelligence dissemination as both commercial signal and marketing asset)

These observations are useful for white-paper drafting on the surveillance industry landscape. They are not justifications for blocklist inclusion.

## Verification status

| Step | Status | Outcome |
|---|---|---|
| 1. Corporate identity | ✓ COMPLETE | Documented for context |
| 2. WHOIS | ✓ COMPLETE | Documented for context |
| 3. Subdomain enumeration | ✓ COMPLETE | Documented for context |
| 4. SecurityTrails | ✓ COMPLETE | Documented for context |
| 5. Behavioral analysis | ✓ COMPLETE | whitestream.io does not log Bitcoin queries in normal user activity |
| 6. Inclusion criteria | ✓ COMPLETE | **DOES NOT MEET CRITERIA — EXCLUDE** |
| 7. Functional impact test | N/A | No block |
| 8. domains.csv entry | N/A | No entry |
| 9. Pull request | N/A | No PR — research moved to context notes |

**Final verdict: Whitestream is NOT included in the SatoshiShield blocklist. Research is preserved in `SatoshiShield_Industry_Context_Notes.md` (Entry 1) for white-paper use.**
