# SatoshiShield

*Bitcoin Privacy DNS Blocklist*

**White Paper · Version 1.4 · May 2026**

> SatoshiShield is a curated, community-maintained DNS blocklist that prevents blockchain analytics firms, surveillance platforms, and wallet telemetry services from tracking Bitcoin users at the network layer. It is designed to complement — not replace — node sovereignty. Compatible with Pi-hole, AdGuard Home, and any DNS-based ad blocker.

Published under the MIT License · [github.com/cypherpilgrim/satoshishield](https://github.com/cypherpilgrim/satoshishield)

---

## 1. The Problem

Bitcoin is often described as pseudonymous — not anonymous. Every transaction is permanently recorded on a public ledger. Every address you use, every coin you send, every UTXO you hold — all of it is visible to anyone who knows how to look.

What most Bitcoin users do not realize is that the surveillance infrastructure built on top of this public ledger is vast, well-funded, and actively working to connect blockchain addresses to real-world identities. This infrastructure operates not just at the blockchain layer, but at the network layer — meaning it can see your IP address, your query patterns, and your timing, even before you broadcast a single transaction.

### 1.1 The Surveillance Layer

When you use Bitcoin, your wallet software has to communicate with the network. It needs to:

- Check the balance and history of your addresses

- Fetch fee estimates to calculate transaction costs

- Broadcast signed transactions to the peer-to-peer network

- Retrieve current price data and exchange rates

- Report telemetry and usage analytics back to the wallet developer

Each of these communications goes somewhere. In most cases, that somewhere is a third-party server operated by a company whose business model depends on knowing who is using Bitcoin and how.

Blockchain analytics firms — Chainalysis, Elliptic, TRM Labs, Arkham Intelligence, and others — have built sophisticated systems that correlate IP addresses with on-chain activity. They don't need your name. They need your IP address at the moment your wallet makes a query, and they need the on-chain data that query reveals. Over time, the correlation builds a profile that connects your Bitcoin activity to your physical location, your device, and ultimately, your identity.

### 1.2 The DNS Gap

Most Bitcoin privacy tools focus on the blockchain layer — CoinJoin, Lightning Network, coin control, address rotation. These are important. But they do nothing to prevent surveillance at the network layer.

Every connection your device makes to a surveillance domain begins with a DNS query. Before any data is transmitted, your device asks a DNS resolver: "What is the IP address of api.chainalysis.com?" That query is visible. It reveals that your IP address is interested in a Chainalysis endpoint. It happens before encryption, before any blockchain data is shared, and before your wallet software has made any decisions about privacy.

No existing Bitcoin privacy tool addresses this layer. Pi-hole and AdGuard Home block advertising and tracking domains for general internet browsing, but they contain no curated lists targeting Bitcoin-specific surveillance infrastructure. SatoshiShield fills this gap.

> The DNS layer is the earliest point at which Bitcoin surveillance can be interrupted. SatoshiShield operates at this layer — before connections are established, before data is transmitted, and before analytics firms can log your IP address against their blockchain intelligence databases.

### 1.3 Who Is Being Tracked

The surveillance affects every category of Bitcoin user:

- Casual users with mobile wallet apps that phone home to analytics APIs

- Self-custody users whose wallets connect to public Electrum servers

- Node runners whose family members use unprotected devices on the same network

- Developers who query blockchain explorer APIs during testing

- Privacy-conscious users who have secured their wallet but not their DNS layer

Even users who run their own full node and connect their wallet exclusively to that node remain vulnerable at the DNS layer. Other applications on their network — price trackers, portfolio apps, browser extensions, mobile wallets — continue to make outbound connections to surveillance infrastructure.

## 2. The Solution

SatoshiShield is a curated DNS blocklist. When installed in a DNS-level ad blocker such as Pi-hole or AdGuard Home, it silently drops DNS queries for domains operated by blockchain analytics firms, surveillance platforms, wallet telemetry services, and deanonymization tools.

No connection is established. No data is transmitted. The surveillance firm never sees your IP address.

### 2.1 How DNS Blocking Works

DNS (Domain Name System) is the internet's phone book. When any application on your network wants to connect to a remote server, it first asks a DNS resolver for the IP address of that server. This query happens before any actual connection is made.

A DNS-level blocker sits between your devices and the internet, intercepting these queries. When a query matches a domain on the blocklist, the blocker returns a null response (NXDOMAIN or 0.0.0.0) instead of a real IP address. The application receives no valid address and cannot make the connection.

SatoshiShield provides a curated list of domains that should return null responses — specifically, the domains operated by organizations that surveil Bitcoin users.

### 2.2 What SatoshiShield Blocks

| **Category**               | **Examples**                                               | **What They Do**                                                                                                                              |
|----------------------------|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Blockchain Analytics Firms | chainalysis.com, elliptic.co, trmlabs.com, ciphertrace.com | Build databases correlating IP addresses with on-chain activity. Sell intelligence to law enforcement, exchanges, and financial institutions. |
| Deanonymization Platforms  | intel.arkm.com, metasleuth.io                              | Publicly market tools to attach real-world identities to Bitcoin addresses. Log every address lookup against the querying IP.                 |
| Address Screening APIs     | api.chainalysis.com, screening.elliptic.co                 | Embedded in exchange software and some wallet apps to score addresses for risk. Query reveals which addresses you own or are interested in.   |
| Wallet Telemetry           | analytics.exodus.com, telemetry domains                    | Usage analytics and crash reporting baked into wallet software. Reveals which wallets you use, how often, and from which IP.                  |
| KYC Intelligence Services  | scorechain.com, crystalblockchain.com                      | Transaction monitoring and compliance tools. Used by exchanges to flag transactions associated with privacy tools like CoinJoin.              |
| Price Feed Surveillance    | markets.chainalysis.com                                    | Price and market data APIs operated by surveillance firms. Every query logs your IP against their intelligence infrastructure.                |

### 2.3 What SatoshiShield Does Not Block

SatoshiShield is precise. It does not block:

- Bitcoin network peers or mempool propagation

- Legitimate blockchain explorers that respect user privacy (mempool.space, blockstream.info)

- Exchange websites or trading platforms

- Bitcoin wallet software download domains

- Lightning Network nodes or routing infrastructure

- Self-hosted node software update domains

The goal is to block surveillance, not Bitcoin functionality. Every domain inclusion decision is documented with a rationale. No domain is blocked without a specific, articulable privacy harm.

## 3. Architecture & Compatibility

### 3.1 List Formats

SatoshiShield is published in three formats to maximize compatibility:

| **Format**  | **File**          | **Compatible With**                                      |
|-------------|-------------------|----------------------------------------------------------|
| Domain-only | blocklist.txt     | Pi-hole v5+, Pi-hole v6, AdGuard Home, most DNS blockers |
| Hosts file  | hosts.txt         | Pi-hole v4, classic Unix hosts file, Windows hosts file  |
| ABP syntax  | satoshishield.abp | AdGuard (browser extension), uBlock Origin, AdBlock Plus |

### 3.2 Installation — Pi-hole

Pi-hole v5 and v6 (Settings > Blocklists > Add):

> https://raw.githubusercontent.com/cypherpilgrim/satoshishield/main/blocklist.txt

After adding, run a gravity update:

> pihole -g

### 3.3 Installation — AdGuard Home

AdGuard Home (Filters > DNS Blocklists > Add blocklist > Add a custom list):

> https://raw.githubusercontent.com/cypherpilgrim/satoshishield/main/satoshishield.abp

### 3.4 Self-Hosted DNS Stack

For maximum sovereignty, SatoshiShield is designed to work with a fully self-hosted DNS chain:

**All Devices → Pi-hole (SatoshiShield + gravity blocklists) → Unbound (recursive resolver) → Root DNS Servers**

In this configuration, no external DNS resolver (Google, Cloudflare, ISP) ever sees your queries. SatoshiShield drops Bitcoin surveillance domains before they exit your network. Unbound resolves everything else against root servers directly. No forwarders, no upstream surveillance.

### 3.5 Complementary Stack

SatoshiShield is designed to complement — not replace — other Bitcoin privacy tools. The recommended full stack:

| **Layer**             | **Tool**                                             | **What It Protects**                                               |
|-----------------------|------------------------------------------------------|--------------------------------------------------------------------|
| DNS layer             | SatoshiShield + Pi-hole                              | Blocks surveillance domains before connections are established     |
| Blockchain data layer | Your own Bitcoin node (Bitcoin Core, Umbrel, Start9) | Prevents wallet queries from leaking to third-party servers        |
| Index layer           | Fulcrum or Electrs (Electrum server)                 | Fast address indexing without exposing your xpub to public servers |
| Network layer         | Tor or WireGuard VPN                                 | Masks your IP address at the transport layer                       |
| On-chain layer        | Coin control, address rotation, CoinJoin             | Reduces on-chain linkability between your transactions             |

Each layer addresses a different attack surface. SatoshiShield addresses the DNS layer, which no other tool in this stack covers.

## 4. Domain Selection Methodology

Every domain in the SatoshiShield blocklist is selected according to a documented methodology. The goal is precision — blocking surveillance while preserving functionality.

### 4.1 Inclusion Criteria

A domain is included in SatoshiShield if it meets one or more of the following criteria:

- Operated by a company whose primary business is correlating Bitcoin addresses with real-world identities

- Used as an API endpoint by blockchain analytics or surveillance platforms

- Known to log IP addresses against address queries

- Used for wallet telemetry, crash reporting, or usage analytics that reveals Bitcoin activity

- Operated by a deanonymization platform that publicly markets identity-linking capabilities

- Used by KYC/AML compliance services to score Bitcoin addresses

### 4.2 Exclusion Criteria

A domain is excluded from SatoshiShield if:

- Blocking it would impair legitimate Bitcoin network functionality

- It is operated by an open-source privacy-respecting project

- The privacy harm is speculative or unsubstantiated

- It serves a dual purpose where the benefit of blocking is outweighed by the loss of functionality

### 4.3 Documentation Standard

Every domain inclusion is documented in the repository with:

- The organization operating the domain

- The specific privacy harm (IP logging, address correlation, telemetry, etc.)

- The source or evidence supporting inclusion

- The date of last verification

This documentation standard ensures that the list remains auditable and that users can verify why any domain is blocked.

### 4.4 Initial Domain List

Version 1.0 of SatoshiShield included the following domain categories. The list has been expanded and reorganized in subsequent releases; see the CHANGELOG for current state.

| **Organization**         | **Domains Blocked**                                                        | **Category**           | **Rationale**                                                                                                                  |
|--------------------------|----------------------------------------------------------------------------|------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Chainalysis              | chainalysis.com, *.chainalysis.com, markets.chainalysis.com, transpose.io | Blockchain Analytics   | Primary blockchain surveillance firm. APIs log IP + address correlations. Sells intelligence to law enforcement and exchanges. |
| Elliptic                 | elliptic.co, *.elliptic.co                                                | Blockchain Analytics   | Blockchain analytics and compliance. Transaction monitoring APIs reveal address queries to Elliptic servers.                   |
| TRM Labs                 | trmlabs.com, *.trmlabs.com                                                | Blockchain Analytics   | AI-driven blockchain intelligence. BLOCKINT API correlates address queries with IP addresses.                                  |
| CipherTrace (Mastercard) | ciphertrace.com, *.ciphertrace.com                                        | Blockchain Analytics   | Acquired by Mastercard. Blockchain analytics with government and financial institution clients.                                |
| Arkham Intelligence      | arkm.com, intel.arkm.com, *.arkm.com                                      | Deanonymization        | Publicly markets identity-linking tools. Every address lookup on their platform is logged against the querying IP.             |
| Crystal (BitRank)        | crystalblockchain.com, bitrank.com                                         | Blockchain Analytics   | Transaction monitoring and risk scoring. Address queries reveal holdings and transaction history.                              |
| Scorechain               | scorechain.com, *.scorechain.com                                          | KYC/AML Compliance     | Compliance platform used by exchanges to flag privacy-enhancing transactions including CoinJoin.                               |
| Merkle Science           | merkle.science, *.merkle.science                                          | Blockchain Analytics   | Blockchain intelligence platform. Predictive risk platform logs address queries.                                               |
| MetaSleuth               | metasleuth.io, *.metasleuth.io                                            | Deanonymization        | Crypto tracking and investigation platform. Logs all address and wallet queries.                                               |
| Breadcrumbs              | breadcrumbs.app, *.breadcrumbs.app                                        | Blockchain Analytics   | Free blockchain analytics tool. Address queries logged against IP.                                                             |
| Nansen                   | nansen.ai, *.nansen.ai                                                    | Surveillance Analytics | Wallet labeling and analytics. Builds identity profiles from address query patterns. Promoted to Tier 1 in v1.1.               |
| Glassnode                | glassnode.com, *.glassnode.com                                            | Blockchain Analytics   | On-chain analytics. IP logged against address and metric queries. Promoted to Tier 1 in v1.1.                                  |

Additional domains will be added in subsequent releases based on community research and verification.

## 5. What SatoshiShield Is Not

Precision matters. SatoshiShield makes specific, limited claims about what it does and does not provide.

> SatoshiShield is one layer of a privacy stack. It is not a complete privacy solution, and it does not make you anonymous on-chain.

### 5.1 SatoshiShield Does Not Provide On-Chain Privacy

Blocking surveillance domains at the DNS layer does not affect the blockchain. Your transactions are still public. Your addresses are still linkable if you reuse them. Your coins can still be traced if you have poor coin control practices. SatoshiShield addresses the network layer only.

### 5.2 SatoshiShield Does Not Protect Against All Correlation

A determined adversary with access to your ISP's traffic logs, a network tap, or your router's connection logs can still correlate your IP with Bitcoin activity through means other than DNS. SatoshiShield is not a defense against nation-state adversaries or physical access to your network infrastructure.

### 5.3 SatoshiShield Does Not Replace a Node

Running your own Bitcoin node and connecting your wallet to it is the single most impactful privacy improvement a Bitcoin user can make. SatoshiShield complements node sovereignty — it does not substitute for it. If you do not run your own node, install SatoshiShield and then get a node running.

### 5.4 SatoshiShield Does Not Guarantee Complete Surveillance Prevention

The surveillance landscape changes. New analytics firms emerge. Existing firms change their domain structures. SatoshiShield is only as effective as its most recent update. The community maintenance model described in Section 6 is designed to keep the list current, but gaps are possible between domain changes and list updates.

## 6. Community & Governance

### 6.1 Open Source

SatoshiShield is published under the MIT License. All source files, domain lists, documentation, and tooling are available at:

**[github.com/cypherpilgrim/satoshishield](https://github.com/cypherpilgrim/satoshishield)**

### 6.2 Contributing

Community contributions are the lifeblood of any blocklist. SatoshiShield accepts contributions via GitHub pull requests. Contributors are asked to:

- Provide evidence of the privacy harm associated with a proposed domain

- Verify that blocking the domain does not impair legitimate Bitcoin functionality

- Document the organization, domain, and rationale in the standard format

- Test the blocklist against their own Pi-hole or AdGuard installation before submitting

### 6.3 Domain Verification Process

All proposed domain additions go through a verification process before inclusion:

| **Step**          | **Action**                                                                                                | **Outcome**                                                |
|-------------------|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| 1. Submission    | Contributor opens GitHub issue or pull request with domain and rationale                                  | Domain enters review queue                                 |
| 2. Research      | Maintainers verify the organization, confirm the privacy harm, and check for dual-use concerns            | Domain approved, rejected, or flagged for further research |
| 3. Testing       | Domain is tested against common Bitcoin wallet software to confirm blocking does not impair functionality | Confirmed safe to block                                    |
| 4. Documentation | Rationale documented in domains.csv with organization, harm, source, and date                             | Domain added to all three list formats                     |
| 5. Release       | Updated lists published to GitHub, automatically pulled by Pi-hole and AdGuard installations              | Protection deployed to all users                           |

### 6.4 Update Cadence

SatoshiShield targets monthly releases for routine domain additions and quarterly reviews for comprehensive audit of existing entries. Emergency releases may be issued when a major surveillance firm launches a new domain or changes existing infrastructure.

Pi-hole and AdGuard Home automatically pull updated lists on their configured gravity update schedules. Users do not need to take any action to receive updates after initial installation.

## 7. Roadmap

| **Version** | **Target** | **Planned Features**                                                                                                                                                                      |
|-------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.0         | May 2026   | Initial release. Core blockchain analytics firm domains. Three list formats. Pi-hole and AdGuard installation documentation.                                                              |
| 1.1         | June 2026  | Wallet telemetry domain research and additions. Exchange KYC API domains. Community contribution pipeline established.                                                                    |
| 1.2         | July 2026  | Mobile wallet app telemetry domains (iOS and Android analysis). Price feed surveillance domains. Automated domain verification tooling.                                                   |
| 2.0         | Q3 2026    | Self-updating capability for Pi-hole installations. Companion web dashboard showing blocked query statistics. Integration with popular Bitcoin node software (Umbrel, Start9, Raspibolt). |
| 2.1         | Q4 2026    | Browser extension version for users without a Pi-hole. Companion educational materials for each blocked domain category.                                                                  |

## 8. Frequently Asked Questions

**Will blocking these domains break my Bitcoin wallet?**

No — if your wallet is properly configured. Wallets that connect to your own node or a trusted Electrum server do not need to contact surveillance domains. Wallets that rely on public infrastructure operated by analytics firms may see reduced functionality — which is by design. The appropriate response is to configure your wallet to use privacy-respecting infrastructure.

**I run my own node. Do I need SatoshiShield?**

Running your own node is the most important privacy improvement you can make. SatoshiShield adds complementary protection at the DNS layer that your node does not cover — specifically, protection for other apps on your network, browser-based address lookups, mobile wallet telemetry from family members' devices, and price tracking applications. The two tools protect different attack surfaces.

**Does this work on mobile devices?**

Yes — when installed on a Pi-hole or AdGuard Home that serves DNS for your entire network, SatoshiShield protects every device on that network, including phones and tablets, without any configuration changes on individual devices.

**How do I know the blocklist is not blocking things it should not?**

Every domain in the blocklist is documented with a rationale in the repository's domains.csv file. You can audit every entry. If you believe a domain is incorrectly included, open a GitHub issue and the maintainers will review it. The MIT License means you can also fork and customize the list for your own needs.

**What if a surveillance firm changes their domain?**

Domain changes will be caught through community monitoring and periodic audits. When a major surveillance firm changes their domain infrastructure, an emergency release will be issued. Users with Pi-hole or AdGuard running automated gravity updates will receive the change without manual intervention.

**Can I use this with a VPN?**

Yes. SatoshiShield operates at the DNS layer and is independent of your VPN configuration. If your Pi-hole sits inside your VPN, devices connecting through the VPN will benefit from SatoshiShield. If your Pi-hole sits outside your VPN, it will protect your local network traffic. Both configurations are valid depending on your threat model.

## 9. Adversarial Considerations

Any effective privacy tool invites countermeasures from the organizations it protects against. SatoshiShield's maintainers have analyzed the realistic responses available to blockchain analytics firms and designed the project's architecture with these countermeasures in mind.

This section documents known countermeasures, their likelihood, and the mitigation strategy for each. Transparency about limitations is a core commitment of this project.

### 9.1 Domain Rotation

Likelihood: High. Surveillance firms will change API endpoint domains to evade blocklists. api.chainalysis.com becomes data-services-prod.chainlysis-cloud.io. The blocklist lags until the community identifies and adds the new domain.

**Mitigation:**

- SatoshiShield uses wildcard blocking at the organizational domain level where possible. Blocking *.chainalysis.com captures all current and future subdomains regardless of what they are named.

- Community monitoring via GitHub issues allows rapid reporting of new surveillance domains.

- Monthly releases and emergency releases ensure new domains are incorporated quickly.

- The domains.csv documentation standard tracks organizational ownership, making it easier to identify new domains belonging to known surveillance firms.

### 9.2 CDN Masking

Likelihood: High. Surveillance firms route API traffic through major CDN providers (Cloudflare, Fastly, AWS CloudFront). The surveillance domain resolves to a shared CDN IP used by thousands of legitimate websites, making IP-based blocking impossible without collateral damage.

**Mitigation:**

- DNS-level domain blocking remains fully effective regardless of CDN masking. When SatoshiShield blocks api.chainalysis.com, the DNS query is dropped before resolution. The CDN IP address is never reached and never revealed.

- CDN masking is not a countermeasure against DNS blocking — it is a countermeasure against IP blocking. SatoshiShield operates at the DNS layer and is therefore unaffected.

### 9.3 Hardcoded IP Addresses

Likelihood: Medium. This is the most technically significant countermeasure. Surveillance APIs embedded in wallet SDKs can use hardcoded IP addresses instead of domain names, bypassing DNS resolution entirely. Pi-hole and AdGuard Home see no DNS query and cannot intercept the connection.

**Mitigation:**

- This is a known limitation of DNS-level blocking and is documented honestly. SatoshiShield does not claim to address hardcoded IP connections.

- Firewall-level blocking (pfSense, OPNsense) using IP address blocklists for known surveillance firm infrastructure can close this gap. A companion project, SatoshiShield-Firewall, is planned for a future release to provide pfSense and OPNsense alias lists of known analytics firm IP ranges.

- Users who run pfSense or OPNsense can combine SatoshiShield with firewall rules blocking the IP ranges of known surveillance infrastructure for defense in depth.

> Hardcoded IPs are the genuine gap in DNS-level blocking. SatoshiShield documents this limitation clearly. The planned SatoshiShield-Firewall companion project will address this layer for users with firewall-level blocking capability.

### 9.4 Legitimate Domain Camouflage

Likelihood: Medium. A surveillance firm acquires or partners with a domain that appears legitimate — a price feed, a block explorer, a wallet update service — and routes surveillance API traffic through it. The domain appears innocuous until traffic analysis reveals its true purpose.

**Mitigation:**

- SatoshiShield's inclusion criteria require documented evidence of surveillance activity, not just organizational ownership. A domain that appears legitimate will not be blocked until behavioral evidence of surveillance is documented.

- Community members performing traffic analysis on Bitcoin wallet software are encouraged to submit findings via GitHub issues.

- The domains.csv rationale field documents the specific surveillance behavior, making it possible to detect when a domain has changed its behavior and should be reviewed for removal.

### 9.5 Legal Threats

Likelihood: Low. A surveillance firm could send cease and desist letters claiming the blocklist constitutes defamation, tortious interference, or trademark infringement.

**Mitigation:**

- SatoshiShield makes only factual statements: that specific domains are operated by specific organizations and that those organizations engage in specific, documented surveillance activities. Factual statements are protected speech in virtually every relevant jurisdiction.

- The project is maintained pseudonymously under the MIT License with no legal entity attached. There is no realistic legal target.

- Legal threats against a privacy tool would generate significant community attention and validate the tool's premise — the Streisand Effect would likely accelerate adoption rather than suppress it.

- The blocklist is hosted on GitHub, a platform with strong precedent for hosting security research and privacy tools.

### 9.6 Community Infiltration

Likelihood: Low. Actors acting on behalf of surveillance firms could submit pull requests designed to add legitimate domains to the blocklist (causing false positives and eroding trust) or to remove real surveillance domains under the guise of reducing false positives.

**Mitigation:**

- All domain additions and removals require documented rationale reviewed by maintainers before merging.

- The transparent git history makes it possible to audit every change, including who proposed it and what justification was provided.

- Multiple maintainers reduce the risk of a single compromised reviewer.

- Community members are encouraged to review pull requests and flag suspicious submissions.

### 9.7 Project Irrelevance

Likelihood: High. The most likely response from surveillance firms is no response at all. Their primary clients are cryptocurrency exchanges, financial institutions, and government agencies — not individual Bitcoin users who run Pi-hole. A community DNS blocklist does not threaten their core revenue stream.

This is an honest assessment. SatoshiShield primarily protects individual Bitcoin users from passive data collection — the incidental surveillance that happens when wallet software phones home to analytics infrastructure. It does not prevent targeted investigation of specific addresses by law enforcement using Chainalysis Reactor or similar tools.

SatoshiShield's value proposition is protecting the many from passive surveillance, not protecting any individual from targeted investigation. This is a meaningful but bounded goal.

### 9.8 Countermeasure Summary

| **Countermeasure**           | **Likelihood** | **SatoshiShield Effective?**                       | **Mitigation**                                                           |
|------------------------------|----------------|----------------------------------------------------|--------------------------------------------------------------------------|
| Domain rotation              | High           | Partially — wildcard blocking reduces impact       | Monthly releases, wildcard blocking, community monitoring                |
| CDN masking                  | High           | Yes — DNS blocking unaffected by CDN               | No mitigation needed                                                     |
| Hardcoded IP addresses       | Medium         | No — DNS layer bypassed entirely                   | SatoshiShield-Firewall companion project (planned)                       |
| Legitimate domain camouflage | Medium         | Partially — until traffic analysis reveals purpose | Evidence-based inclusion criteria, community traffic analysis            |
| Legal threats                | Low            | Yes — factual statements, pseudonymous maintainer  | MIT License, no legal entity, GitHub hosting                             |
| Community infiltration       | Low            | Partially — review process provides defense        | Documented rationale required, multiple maintainers, transparent history |
| Project ignored entirely     | High           | N/A                                                | Build community value regardless of firm response                        |

## 10. About

SatoshiShield was conceived and built by a Bitcoin self-sovereignty practitioner running a fully sovereign homelab network. The project emerged from the realization that years of effort building sovereign DNS infrastructure, self-hosted nodes, and network segmentation had left the Bitcoin DNS surveillance layer completely unaddressed.

The project is maintained under the GitHub identity cypherpilgrim. No real-world identity is attached to this project. This is intentional — the project practices what it preaches.

Contributions, criticism, and forks are welcome. The goal is not credit — it is a more private Bitcoin network for everyone who uses it.

> Privacy is not a crime. Blocking surveillance infrastructure is not an act of concealment — it is an act of self-defense. SatoshiShield exists because the tools to surveil Bitcoin users are sophisticated, well-funded, and actively deployed. The tools to defend against them should be equally accessible.

## 11. License & Disclaimer

SatoshiShield is released under the MIT License. You are free to use, modify, fork, and redistribute this project for any purpose.

SatoshiShield is provided as-is, without warranty of any kind. The maintainers make no guarantee that the blocklist is complete, current, or free from errors. Users are responsible for verifying that the blocklist is appropriate for their use case before deploying it in a production environment.

SatoshiShield does not provide legal advice. Users are responsible for ensuring that their use of this software complies with applicable laws in their jurisdiction.

Blocking a domain does not constitute any claim about the legality or illegality of the organization operating that domain. It is a technical measure to prevent network connections, nothing more.

**Document Version**

| **Version** | **Date** | **Changes**                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.0         | May 2026 | Initial white paper release. Covers problem statement, solution architecture, domain methodology, compatibility, roadmap, and FAQ.                                                                                                                                                                                                                                                                                             |
| 1.4         | May 2026 | Updated to v1.4 metadata. GitHub handle migrated from sawdustpilgrim to cypherpilgrim across all URLs. Glassnode and Nansen Table 5 entries note their promotion to Tier 1 in v1.1. Section 9 About text genericized. Section 4.4 wording clarified to indicate it describes v1.0 state. Duplicate Section 8 numbering fixed: Adversarial Considerations is now Section 9, About is now Section 10, License is now Section 11. |
