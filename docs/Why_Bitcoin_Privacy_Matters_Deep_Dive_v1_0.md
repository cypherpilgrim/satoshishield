# Why Bitcoin Privacy Matters

*Understanding the Surveillance You Do Not See*

**Deep Dive Edition**

Published by SatoshiShield · Version 1.0 · May 2026
[github.com/cypherpilgrim/satoshishield](https://github.com/cypherpilgrim/satoshishield)

---

## 1. The Promise and the Reality

Most people think Bitcoin is anonymous, but it is not. Bitcoin is pseudonymous, and that one word difference is where the trouble starts.

The Bitcoin whitepaper, published in 2008, addressed privacy directly. The traditional banking model achieves privacy by limiting who can see the records, while Bitcoin would achieve privacy by keeping the public keys anonymous. The system was never designed to be anonymous, but rather pseudonymous, which is a different and weaker thing.

The distinction matters because a Bitcoin address is a pseudonym, like a pen name, and it is not connected to the real-world identity of the person who uses it by any built-in cryptographic property. The address is also permanent, public, and globally readable, because every transaction every address makes is recorded on the blockchain, in plain text, forever.

A useful way to think about it is to imagine that every transaction in a personal bank account were published in the newspaper, attributed only to the person's initials. As long as nobody connects the initials to the name, the privacy holds, but the moment somebody makes the connection, by knowing one purchase made publicly, by seeing an ID at a counter, or by finding the initials on a social media post, the entire transaction history becomes readable. That is pseudonymity, and that is Bitcoin's actual privacy model.

### 1.1 Why this matters more than people think

The permanence of the blockchain creates an asymmetry that does not exist in the rest of the financial system. A person only needs to be identified once, ever, for their entire transaction history to become readable, and that history does not expire. A transaction made in 2014 can be analyzed in 2026 using techniques that did not exist when the transaction was made, and future techniques may reveal more still.

Cash leaves no permanent record, because a cash payment made ten years ago is gone unless someone happened to be watching at the moment of the transaction. Credit card records exist, but they are held privately by the bank and the network, accessible to a limited number of parties under defined circumstances. Bitcoin is different: the record is public, global, and accessible to anyone with an internet connection. That permanence is what makes the surveillance industry possible.

## 2. Who Is Watching

The blockchain surveillance industry is small in headcount but large in influence. It has reshaped how governments, exchanges, and financial institutions interact with cryptocurrency, and the companies involved are well-funded, growing, and have already made their data central to compliance and law enforcement operations around the world.

### 2.1 The major players

A few firms dominate the industry, each with slightly different product focus but the same core business model of collecting data and selling access to the database.

| **Company**            | **Founded** | **Specialty**                                                                                                                                                                                                                                                                 |
|------------------------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Chainalysis**        | 2014        | The market leader, selling Reactor for graph visualization, KYT for real-time transaction monitoring, and Rapid for AI-assisted investigations. Projecting 250 million dollars in annual revenue for end of 2024, with government contracts now the majority of that revenue. |
| **Elliptic**           | 2013        | Transaction monitoring and compliance APIs, with heavy use by exchanges and banks for sanctions screening.                                                                                                                                                                    |
| **TRM Labs**           | 2018        | Best known for BLOCKINT, an API that correlates address queries with the IP addresses making the queries.                                                                                                                                                                     |
| **CipherTrace**        | 2015        | Acquired by Mastercard in 2021 and now part of Mastercard's broader compliance infrastructure.                                                                                                                                                                                |
| **Arkham**             | 2020        | Publicly markets itself as a deanonymization platform, operating a website where users can attach real-world identities to Bitcoin addresses.                                                                                                                                 |
| **Crystal Blockchain** | 2017        | Transaction monitoring and risk scoring, with a separate scoring product called BitRank.                                                                                                                                                                                      |
| **Scorechain**         | 2015        | Compliance platform that explicitly flags CoinJoin and other privacy-enhancing transactions as high risk.                                                                                                                                                                     |
| **Merkle Science**     | 2018        | Predictive risk platform that logs address queries against IP addresses.                                                                                                                                                                                                      |

### 2.2 The scale of the industry

Chainalysis alone is projected to do 250 million dollars in annual recurring revenue by the end of 2024, representing roughly thirty percent year-over-year growth. The company was valued at 8.6 billion dollars at its peak in 2022, and recent secondary share purchases imply a current valuation around 2.5 billion dollars, which is lower than the peak but still substantial.

The funding behind these firms is significant. Chainalysis has raised over 536 million dollars across multiple rounds, with major investors including Accel, Benchmark, and Blackstone Alternative Asset Management. This is not a fringe industry but rather venture-backed mainstream financial infrastructure with institutional credibility.

### 2.3 Who pays the surveillance firms

Their customers fall into four major groups, each using the data differently.

#### Government agencies

The single largest revenue source for the major firms is government contracts. Chainalysis has publicly named the Department of Defense, the FBI, and the IRS as customers, and the same firms typically serve equivalent agencies in the United Kingdom, the European Union, Canada, Australia, and increasingly across South America and Asia.

Specific examples of what governments do with the data follow.

**Tax enforcement.** The IRS uses Chainalysis to identify taxpayers it believes have underreported crypto income, and the agency operates a dedicated task force called Operation Hidden Treasure within the Office of Fraud Enforcement. The IRS has also partnered with Palantir to combine blockchain analytics with the broader data fusion that Palantir is known for. The combination is significantly more powerful than either tool alone, and it works against non-custodial wallets as well as exchange accounts.

**Criminal investigations.** Chainalysis Reactor is used to map flows of funds in investigations ranging from ransomware to drug trafficking, and the output is admissible in court. Chainalysis analysts testify as expert witnesses, and their credibility with judges and prosecutors is something an independent researcher would have to build over years.

**Sanctions enforcement.** The US Treasury's Office of Foreign Assets Control maintains sanctions on specific Bitcoin addresses, and surveillance firms make it possible to identify funds that touched those addresses, even after multiple transaction hops. This is how the practical enforcement of OFAC sanctions against Bitcoin addresses actually happens.

**Privacy coin and Lightning Network attacks.** In 2020, the IRS awarded Chainalysis and a forensic data firm called Integra FEC a combined contract worth 1.25 million dollars, and the purpose of the contract was to develop tools that break the privacy of Monero and Bitcoin transactions sent over the Lightning Network. The contract is a matter of public record, verifiable on [USAspending.gov](https://www.usaspending.gov) under contract record CONT_AWD_2032H820C00041. The taxpayer-funded effort to break privacy-protecting features of Bitcoin is not speculation; it is documented and ongoing.

#### Exchanges and financial institutions

Every major cryptocurrency exchange integrates with at least one blockchain analytics firm, including Coinbase, Binance, Kraken, OKX, and the rest. Banks dealing with crypto do the same, and the integrations are used for the following purposes.

- **Real-time transaction monitoring,** where every deposit and withdrawal is screened against the database the moment it happens, with products like Chainalysis KYT operating continuously.

- **Sanctions screening,** confirming that deposits do not trace back to addresses on the OFAC sanctions list.

- **High-risk flagging,** including addresses that have used CoinJoin or other privacy tools, even though those tools are legal in most jurisdictions.

- **Automated account closure and asset freeze decisions,** based on the firm's proprietary risk scoring.

#### Insurance, lending, and employment

Less talked about but growing, crypto activity is starting to factor into insurance underwriting for life, health, and property; lending decisions for mortgages, auto loans, and personal credit; employer background checks, especially in financial services; and even tenant screening. The data flows are opaque, and most affected people will never see the report containing their crypto profile or know to contest it.

#### Private investigators and lawyers

Divorce cases, asset recovery, and civil litigation all create demand for Bitcoin surveillance data. Anyone with a budget who needs to find or characterize someone's Bitcoin activity can hire access to these databases through professional channels, and the threshold for getting the data is much lower than the threshold for getting equivalent data from a bank.

## 3. How the Watching Happens

The surveillance firms do not rely on a single technique. They use four major data sources, layered together, and each source has limits on its own. Combined, however, they build a database that can identify most active Bitcoin users with reasonable confidence.

### 3.1 On-chain analysis

The simplest source is the blockchain itself, which is public and available for anyone to download and analyze. Surveillance firms have invested heavily in the techniques required to extract identity from purely on-chain data, and the key techniques include the following.

**Common-input clustering.** If a Bitcoin transaction spends from multiple addresses at once, those addresses almost certainly belong to the same wallet, and this single observation links millions of addresses into clusters.

**Change address identification.** When Bitcoin is sent, most wallets create a change address to receive the leftover funds, and reliable heuristics exist for identifying which output of a transaction is the change, which links the change address back to the sender.

**Timing analysis.** Transaction timestamps reveal time zones, daily routines, and behavioral patterns. A wallet that consistently transacts during business hours in a specific time zone has narrowed itself geographically before the analyst has done any other work.

**Amount analysis.** Specific transaction amounts can correlate with known purchases or services, and a round number in USD value, converted to Bitcoin at the exchange rate of a particular day, often points back to a specific commercial transaction.

### 3.2 IP address correlation

The blockchain alone gives the firms clusters of addresses, but to attach those clusters to real-world identities they need a different data source. The most important one is the IP address captured when a wallet, browser, or app talks to a surveillance firm's server, and this happens more often than most users realize.

Many wallet apps embed third-party SDKs for analytics, price feeds, or address validation, and these SDKs make calls to servers operated by surveillance firms or by firms that share data with them. Every call logs the IP address and the Bitcoin-related query. Browser extensions for crypto, including price trackers, wallet integrations, and transaction explorers, do the same thing. Websites that show Bitcoin address details often make backend calls to analytics firm APIs, so when a user visits a block explorer to check a balance, the user's IP address may be logged against that address by the surveillance firm whose API powered the lookup.

This is the network-layer leak that almost no Bitcoin privacy tool addresses. A VPN hides the user's IP from the ISP and from the destination server, but the analytics firm still sees the query, just coming from the VPN exit node instead of the user's home connection. A Tor connection hides the IP more thoroughly, but only if every request goes through Tor, and a Bitcoin node prevents the user's wallet from leaking but does not help when the same network also has browser tabs open to portfolio sites. The only complete defense at this layer is to never make the query at all, which is what DNS-level blocking does.

### 3.3 Exchange and KYC data

Every Know Your Customer exchange has its customers' names, addresses, government ID documents, and records of every Bitcoin address those customers have ever deposited from or withdrawn to. This data flows to surveillance firms through several channels.

**Direct commercial partnerships.** Chainalysis and others have explicit data-sharing agreements with major exchanges, and the exchange's customer data flows into the firm's identity database in exchange for risk-scoring services that the exchange uses for compliance.

**Government subpoenas.** Law enforcement can compel exchanges to hand over customer data, and that data then informs the surveillance firm's analysis, often through informal information flow between investigators and the firms they work with.

**Data breaches.** Exchange breaches have leaked KYC data multiple times, and once leaked, the data may be acquired by analysts, sold on underground markets, or used as training input for identification systems.

### 3.4 Deanonymization platforms

A more recent development is the rise of explicit deanonymization platforms that invite the public to do the linking work, and Arkham Intelligence is the most prominent example. Its product is essentially a website where users can attach real-world identities to Bitcoin addresses and then publish those attributions for everyone to see.

The company markets the platform as a tool for transparency in financial markets, while critics describe it as a public bounty system for stripping privacy from strangers. Whatever the framing, the result is the same: a growing public-facing database of address-to-identity mappings that anyone, including the major analytics firms, can incorporate into their own analysis.

### 3.5 How the layers combine

Individually, each technique has limitations. On-chain analysis produces clusters but not identities; KYC data produces identities for specific addresses; IP correlation produces networks of interest but not always identities; deanonymization platforms add manual attributions. Combined, however, the four sources create a database where tens of millions of Bitcoin addresses are clustered into known wallets, a substantial fraction of those clusters are linked to specific real-world identities, many of those identities are enriched with location data and behavioral patterns and risk scores, and the data is stored permanently and grows continuously. The total is much more than the sum of the parts.

## 4. What They Do With What They See

Once the data is collected and identities are attached, the database becomes a product, and the surveillance firms sell access in several forms.

### 4.1 The search interface

Chainalysis Reactor, Elliptic Navigator, and similar tools are graphical search engines for the surveillance database. A user enters a Bitcoin address, and the interface returns the wallet cluster the address belongs to (often containing hundreds or thousands of related addresses), the known attribution if any exists, a graph of transaction flows in and out going back to the address's creation, connections to flagged entities such as sanctioned addresses or mixers or ransomware operators, and a risk score from zero to one hundred. An investigator can follow the graph forward and backward, examine counterparties, and build a narrative around any address in minutes.

### 4.2 Real-time monitoring

Chainalysis Know-Your-Transaction (KYT) and equivalent products at the other firms operate continuously rather than on demand. Every deposit and withdrawal at a participating exchange is screened in real time, and if the transaction matches a high-risk profile, the exchange is alerted immediately. The exchange typically responds by freezing the account, blocking the withdrawal, or requesting additional documentation.

From the user's perspective, the action is automatic and often unexplained. The exchange does not typically reveal which firm flagged the transaction or why; the customer is told only that the account has been restricted pending review.

### 4.3 Risk scoring

Every address in the database gets a numerical risk score, and while the scoring algorithm is proprietary, publicly known factors include the following.

**Direct interaction with flagged addresses,** including wallets connected to ransomware operations, sanctioned entities, darknet markets, or known thefts.

**Indirect interaction with the above,** through any number of intermediary hops, with some firms flagging funds even after dozens of transactions of separation between the user and the original flagged address.

**Use of privacy tools,** where CoinJoin, mixers, and even Lightning Network usage frequently raise the score, despite all of these tools being legal.

**Geographic and behavioral patterns,** where transactions originating from certain countries, times of day, or matching certain signatures can also raise the score.

The score determines what exchanges, banks, and other counterparties will do when they encounter the user's transactions. There is no published scoring rubric and no formal appeal process. The firm calculates the score, the institution acts on it, and the user lives with the consequences.

## 5. The Real-World Consequences

The abstract dangers become concrete when looking at what actually happens to people whose transactions get flagged or whose identities get linked. The consequences range from inconvenient to life-threatening.

### 5.1 Frozen accounts and seized deposits

This is the most common outcome, and it happens to people every day. A user deposits Bitcoin to an exchange, the exchange's compliance system checks the deposit against the surveillance database, and something in the transaction's history triggers the risk threshold. The account gets frozen, and the user receives a vague email saying the funds are under review.

The user may then be asked to provide proof of source of funds, identification documents, full transaction history from any prior wallets, and written explanations for specific addresses in their history. Sometimes the documentation satisfies the exchange and the account is unfrozen weeks or months later. Sometimes it does not, and if the funds touched anything the analytics firm flagged (a CoinJoin, an address that was later sanctioned, a counterparty who is themselves under suspicion) the user may never get the funds back. The exchange's terms of service typically give the exchange broad authority to seize what it considers high-risk deposits.

The user has not been charged with a crime and has not been convicted of anything. The user used legal tools in a legal way, but the funds are gone and practical legal recourse is limited.

### 5.2 Tax enforcement and audits

The IRS has invested heavily in crypto tax enforcement, and several specific developments are worth knowing about.

**Operation Hidden Treasure** is a task force within the Office of Fraud Enforcement that exists specifically to target taxpayers believed to have underreported crypto income. The task force is staffed and active, and it uses blockchain analytics as its primary investigative tool.

**Letters 6173, 6174, and 6174-A** are IRS enforcement letters sent to crypto users the agency believes have underreported. Receiving one creates immediate compliance obligations and signals that the agency has data the recipient may not know it has.

**Form 1099-DA** is the new IRS form crypto brokers must use to report customer activity, and reporting begins with the 2025 tax year. The form requires brokers to report gross proceeds for transactions occurring on or after January 1, 2025, and basis reporting beginning January 1, 2026, with the information flowing directly to the IRS without the taxpayer's involvement.

**The Palantir partnership** is less discussed but significant. The IRS works with Palantir alongside Chainalysis to analyze blockchain data and match wallet activity to specific taxpayers, and the combination of Palantir's broader data fusion capabilities with Chainalysis's chain analysis creates an investigative tool that works against non-custodial wallets as well as exchange accounts. The reach is substantial.

An audit driven by blockchain analytics shifts the burden of proof to the taxpayer in a way that traditional audits do not. The IRS arrives with a narrative constructed from years of on-chain data, and the taxpayer must either accept the narrative or disprove it, often years after the transactions in question, with whatever records they have happened to keep.

### 5.3 Sanctions exposure

The Treasury Department's Office of Foreign Assets Control maintains a list of specific Bitcoin addresses that are sanctioned, and funds that touch those addresses become a compliance problem for any US-connected institution that handles them. This works retroactively in a way that surprises people: a user can transact today with a counterparty who is clean today, and then learn years later that the counterparty has been sanctioned. If the user's funds passed through the counterparty's address, even through legitimate commerce, the funds may be treated as tainted. Banks and exchanges will refuse to handle them, and recovery is slow, expensive, and not always possible.

### 5.4 Insurance, lending, and employment

Less visible than the categories above but growing, crypto activity data is increasingly factored into insurance underwriting decisions covering life, health, and property; lending decisions for mortgages, auto loans, and personal credit; employer background checks, especially in financial services and government contracting; and tenant screening in some markets.

The data flows are opaque. Most affected people will never see the report containing their crypto profile, and most will not know to contest it. The decisions made on the basis of the data appear to the affected person as ordinary outcomes of ordinary processes, with no visible connection to the underlying surveillance.

### 5.5 Physical safety

> **This is the consequence people do not want to think about, and the one that has led to actual deaths.**

A confirmed Bitcoin holder is a high-value target for ordinary criminals, and the pattern, sometimes called the five dollar wrench attack, is straightforward: identify someone with significant holdings, find the physical address, and threaten or harm the holder until they hand over the keys.

Documented cases of this pattern exist in multiple countries, and the victims were not high-profile personalities. They were ordinary people whose holdings had become publicly knowable, sometimes through deanonymization platforms, sometimes through data breaches, and sometimes through their own posts on social media that connected their identity to their wallet activity.

Surveillance firm data leaks, customer databases get breached, and internal employees go rogue and exfiltrate data. Once a person's identity is attached to their Bitcoin holdings in a commercial database, the person has lost direct control over who knows. The harm here is not theoretical: it is documented, recurring, and serious.

## 6. Who Is Most Exposed

Bitcoin surveillance affects everyone who uses Bitcoin, but some categories of people face amplified risk, either because they have more to lose or because they are more likely to be specifically targeted.

### 6.1 Holders of significant Bitcoin

The relationship between holdings and risk is direct. Smaller holdings rarely attract targeted attack, but larger holdings identify the holder as worth the effort. The threshold at which a holder becomes interesting to a determined adversary is lower than most people assume, especially outside the United States, where local economic conditions make smaller absolute amounts more significant in real purchasing power.

### 6.2 Journalists, activists, and political donors

Anyone whose donations or payments could attract retaliation faces elevated exposure, including journalists working on sensitive stories who pay sources, activists in authoritarian environments, donors to causes that are legal but politically charged, and anyone supporting individuals who are themselves targets of government action. For these people, public visibility of transactions is not an abstract privacy issue but a direct safety issue for themselves and the people they support.

### 6.3 Domestic violence survivors and stalking victims

Personal adversaries can be harder to defeat than institutional ones, because a permanent searchable financial trail is a tracking device. Bitcoin held under a former name, paid to a domestic violence shelter, or sent to family in another country can all be visible to someone who knows where to look.

### 6.4 People in unstable political environments

Where political conditions change quickly, a permanent record of financial behavior is a long-term liability. The legal donation made today can become evidence in a prosecution five years from now if the regime changes, and the blockchain does not forget while laws do change.

### 6.5 Self-custody users

Counterintuitively, people doing the right thing (running their own nodes, holding their own keys, avoiding custodial services) are sometimes flagged as suspicious by surveillance firm models that treat self-custody behavior as anomalous. The protection a person builds can itself become a flag. This is not a reason to use custodial services, but rather a reason to understand that the surveillance industry is not neutral about Bitcoin self-custody.

### 6.6 Everyone else

Even users who do not fit any of the above categories pay the baseline cost. Every payment becomes part of a permanent, searchable record about that person, available to anyone who can pay for access. There is no deletion, no control over future use, and no consent given for the database to exist in the first place.

## 7. What Surveillance Does Not Need

The reassuring beliefs people use to avoid thinking about Bitcoin surveillance often do not hold up. Each of the following is widely held and substantially wrong.

"They do not have my name."

They may not need it, because an IP address, a device fingerprint, a behavioral pattern, or a single transaction visible elsewhere can identify a person across services. The name is an output of the analysis rather than a precondition for it, and even if they do not have a name today, they may have it tomorrow. The data is permanent, new linkage techniques are applied retroactively to old records, and identifications that were impossible in 2015 are routine in 2025. Identifications that are impossible today will be routine in 2030.

"I have not done anything wrong."

This is the most common misconception and the most dangerous, and three things are worth saying about it.

First, surveillance harms exist independent of wrongdoing. Account freezes, tax audits, tainted funds, and physical safety risks affect people who have committed no offense, and no wrongdoing is required for any of these outcomes to occur.

Second, the definition of wrong changes. Transactions that are legal today may be illegal tomorrow, and because the data is permanent, the records exist if laws change. A person who relied on the legality of an action at the time it was taken has no protection against retroactive reinterpretation.

Third, the risk score is not about wrongdoing. Using CoinJoin is legal, holding self-custody is legal, and sending Bitcoin to family abroad is legal, but all of these can raise a risk score and trigger real-world consequences. The score does not reflect a judgment about whether the user did something wrong; it reflects a judgment about how interesting the user is to the firm and its customers.

"They would need a court order."

Most data collection happens through commercial agreements. The exchange shares data because it is in the exchange's interest, the wallet app phones home because the SDK was installed willingly, and the browser extension makes the query because that is what it was designed to do. No court order is needed for any of this.

Court orders are used for the final mile, compelling specific records for a specific investigation, but by the time a court order is involved, the surveillance has already happened. The court order documents what is already in the database rather than gating the database's existence.

"I am a small fish."

Software changed the economics. The marginal cost of analyzing one more address is now near zero, and the marginal cost of identifying one more person, given the database infrastructure, is also near zero. Small fish are surveilled at scale, automatically, by default, and the cost of being noticed is paid by the small fish rather than by the firm doing the noticing. Being a small fish is not a defense but a description of the typical user, who is exactly who the system is designed to process.

> *A person does not need to do anything wrong to be harmed by surveillance. They just need to be visible to it.*

## 8. Defending Against Surveillance

Strong Bitcoin privacy is not a single tool installed once and forgotten, but rather a stack of practices and tools, each addressing a different layer of leakage. No single tool is a complete solution, and the combination of all four layers is what makes a user significantly harder to surveil at scale than the average Bitcoin user.

### 8.1 The four layers

Bitcoin privacy works in four distinct layers, each with its own set of tools, leaking different information and requiring different defenses.

| **Layer**            | **What leaks here**                                                                                                                                                                         | **Defenses**                                                                                                |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| **Node sovereignty** | The wallet talks to third-party servers such as public Electrum servers, exchange APIs, and block explorers, and each contact reveals the user's IP and the addresses the user cares about. | Run a Bitcoin full node (Start9, Umbrel, RaspiBlitz, MyNode) and connect the wallet only to that node.      |
| **Blockchain layer** | Transactions on the public blockchain can be clustered, traced, and linked through on-chain analysis.                                                                                       | CoinJoin (Whirlpool, JoinMarket, others); coin control; single-use addresses; avoiding KYC exchanges.       |
| **Transport layer**  | Network connections reveal the user's IP to everyone the user contacts, including surveillance firms.                                                                                       | Tor for wallet connections; privacy-respecting VPN (Mullvad, IVPN); Tailscale for trusted internal traffic. |
| **DNS layer**        | Apps and browser extensions make background queries to surveillance firm servers, and every query logs the user's IP against the user's activity.                                           | DNS-level blocking: Pi-hole, AdGuard Home, with the SatoshiShield blocklist or equivalent.                  |

### 8.2 Why the DNS layer is special

Most Bitcoin privacy guidance covers the first three layers, while the DNS layer is almost never mentioned. This is strange, because the DNS layer has a unique property that makes it both important and powerful.

The other three layers protect specific tools: the node protects the wallet, CoinJoin protects specific transactions, and a VPN protects specific connections. Each layer requires the user to use the right tool, the right way, every time, and mistakes are individual and recoverable but frequent.

DNS-level blocking works differently. It protects every device on the network, automatically, for every app, in the background, without the user doing anything, and once installed, it works without further involvement. The wallet app that quietly makes calls to a Chainalysis API, the browser extension that fetches data from Arkham, the price tracker that talks to TRM Labs: none of these require the user to investigate them, because the DNS resolver simply prevents the connection from succeeding.

### 8.3 The layered model in practice

A realistic strong-privacy setup combines all four layers.

**Hardware.** A dedicated home server such as Start9 or Umbrel runs a Bitcoin full node and Electrum server, handling the wallet layer.

**Network.** Pi-hole on the home network with the SatoshiShield blocklist installed blocks DNS queries to surveillance firm domains for every device, handling the DNS layer.

**Transport.** A privacy-respecting VPN such as Mullvad or IVPN, configured to route through the home network's DNS, handles the transport layer, with Tor for wallet connections that warrant it.

**Wallet practice.** Coin control, single-use addresses for receiving, CoinJoin for amounts that warrant the on-chain privacy improvement, and never mixing KYC and non-KYC funds in the same transaction together handle the blockchain layer.

**Operational hygiene.** Holdings should not be announced publicly, pseudonymous identities should be used for crypto-related communications, and devices should be compartmentalized where possible.

Each piece adds value, but no piece is sufficient alone. The combination makes the user substantially harder to surveil than the average Bitcoin user, and that difference is what privacy actually buys.

## 9. A Note on SatoshiShield

SatoshiShield is a free, open-source DNS blocklist that addresses the fourth layer. It is the network-layer defense that most other Bitcoin privacy tools do not cover, and it is published transparently and maintained as a community resource.

### 9.1 What it is

SatoshiShield is a list of domain names operated by Bitcoin surveillance firms, organized in two tiers. Tier 1 covers confirmed surveillance infrastructure: firms whose primary business model is identifying Bitcoin users. Tier 2 covers domains that may also be involved but that warrant additional verification before being treated as confirmed surveillance.

Tier 1 currently covers twelve firms across fourteen root domains:

- Chainalysis and its subsidiary Transpose

- Elliptic

- TRM Labs

- CipherTrace, owned by Mastercard

- Crystal Blockchain and its BitRank alias

- Scorechain

- Merkle Science

- Arkham Intelligence

- MetaSleuth

- Breadcrumbs

- Glassnode

- Nansen

Each domain in the blocklist is documented with evidence: the firm operating it, the category of surveillance it conducts, the specific harm to privacy, and a source link. Every entry is auditable.

### 9.2 How it works

The blocklist is installed on a home network's DNS resolver, most commonly Pi-hole, though AdGuard Home and other resolvers also work. From the moment it is installed, every device on the network is blocked from reaching the listed surveillance firm servers.

When an app on the user's phone, laptop, or any other device tries to query a Chainalysis API, the DNS request returns no result, the connection never gets made, and the query never leaves the network. There is nothing for the surveillance firm to log.

Installation takes under an hour for someone comfortable with home network setup, the blocklist is free, the tools required to use it (Pi-hole, AdGuard Home) are free, and the ongoing cost is zero.

### 9.3 What SatoshiShield is not

Honest scoping matters, and SatoshiShield is not a complete privacy solution. It is one specific defense against one specific category of leakage, and it does NOT do the following.

**Stop on-chain analysis.** Surveillance firms can still download and analyze the public blockchain, and defenses at this layer require CoinJoin and similar tools.

**Protect against KYC exchanges.** If the user uses an exchange that knows who they are, the exchange will share data with surveillance firms through channels that do not require any DNS lookup.

**Replace running a Bitcoin node.** If the user's wallet talks to public Electrum servers, those servers see the address activity directly, and DNS blocking does not help in this case.

**Hide the user's IP from the ISP or VPN.** The ISP still sees that the user connected to the internet, and the VPN provider, if any, still sees the user's traffic in encrypted form.

SatoshiShield complements the other layers rather than replacing them. The correct way to think about it is as the layer that is almost always missing, and that, once installed, requires no further attention.

### 9.4 How to verify it

SatoshiShield is published openly at [github.com/cypherpilgrim/satoshishield](https://github.com/cypherpilgrim/satoshishield), where anyone can review the full list of blocked domains, the evidence supporting each entry, and the rationale for the categorization. The project includes the blocklists in multiple formats (Pi-hole, AdGuard Home, hosts file), regex patterns for wildcard coverage, a CSV file documenting evidence for every domain, a white paper explaining the methodology, a contributor guide for submitting additions or corrections, and a monitoring tool that detects new surveillance domains queried on the user's network. The transparency is the point, because a privacy tool that cannot be audited is itself a risk.

## 10. What to Do Now

Practical steps, ordered by impact relative to effort. The user should pick the level that matches their situation and available time.

### 10.1 The minimum (under an hour)

Install Pi-hole on the home network and apply the SatoshiShield blocklist. This single action protects every device on the network, including phones, laptops, tablets, and smart TVs, from DNS-layer surveillance leakage, and the cost is zero with minimal maintenance. If Pi-hole is too technical, AdGuard Home offers a similar capability with a friendlier interface, and the SatoshiShield repository includes deployment documentation for both. Pi-hole runs on a Raspberry Pi or any spare computer, with total hardware cost under fifty dollars.

### 10.2 Solid baseline (a weekend project)

Building on the minimum, add the following.

- A privacy-respecting VPN such as Mullvad or IVPN, configured to route DNS through the Pi-hole

- A password manager for exchange and wallet credentials

- Hardware wallets for any significant holdings

- Backups of seed phrases stored physically and securely, in more than one location

### 10.3 Strong privacy (an ongoing commitment)

For users with significant holdings, elevated risk, or who simply want to do this properly:

- Run a Bitcoin full node and Electrum server

- Use CoinJoin for amounts where on-chain privacy matters

- Practice coin control by keeping KYC and non-KYC funds in separate UTXOs that never mix in a single transaction

- Route wallet connections through Tor

- Use pseudonymous identities for crypto-related accounts and communications

- Compartmentalize devices, using a dedicated machine for high-value operations

### 10.4 Elevated risk (full operational security)

For users facing threats like targeted surveillance, physical danger, or operations in hostile political environments, all of the above applies, plus the following.

- Air-gapped signing devices for the wallets that matter most

- Multi-signature setups distributing trust across multiple keys

- Geographic diversity in key storage

- Consultation with security professionals familiar with the specific threat model

The investment scales with the threat, and most readers will be at the first or second level, which is enough for meaningful improvement. The fourth level is for users who genuinely need it, and they usually know that they need it.

## 11. References and Further Reading

### 11.1 Cited in this document

Chainalysis financial data, government contracts, and product details: Sacra company research, Chainalysis official communications, [USAspending.gov](https://www.usaspending.gov).

IRS Monero contract (2020): [USAspending.gov](https://www.usaspending.gov) contract record CONT_AWD_2032H820C00041, and coverage by multiple crypto news outlets at the time of award.

IRS Operation Hidden Treasure and Form 1099-DA: IRS official announcements and Treasury Department regulations effective tax year 2025.

IRS partnership with Palantir and Chainalysis: Public statements by the IRS regarding blockchain analysis partnerships.

### 11.2 Further reading on Bitcoin privacy

- Bitcoin Optech: bitcoinops.org (newsletter and topics on privacy techniques)

- Bitcoin Privacy Guide: bitcoin.org/en/protect-your-privacy

- Wasabi Wallet documentation on CoinJoin: wasabiwallet.io/docs

- Samourai Wallet documentation: samouraiwallet.com (Whirlpool, coin control)

### 11.3 Tools mentioned

- Pi-hole: pi-hole.net

- AdGuard Home: adguard.com/adguard-home

- Mullvad VPN: mullvad.net

- Tor: torproject.org

- Start9: start9.com

- Umbrel: umbrel.com

- SatoshiShield: [github.com/cypherpilgrim/satoshishield](https://github.com/cypherpilgrim/satoshishield)

Published by SatoshiShield • Free to share with attribution • May 2026

[github.com/cypherpilgrim/satoshishield](https://github.com/cypherpilgrim/satoshishield)
