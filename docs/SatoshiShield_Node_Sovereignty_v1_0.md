# Node Sovereignty

*Why Running Your Own Bitcoin Node Is the Foundation of Privacy*

**A SatoshiShield Paper**

Version 1.0 · May 2026 · Published by SatoshiShield
[github.com/cypherpilgrim/satoshishield](https://github.com/cypherpilgrim/satoshishield)

*Free to share with attribution*

---

## Abstract

Most Bitcoin privacy guidance focuses on the on-chain layer — CoinJoin, coin control, address rotation. These tools matter. But none of them address the fact that the moment your wallet asks the network a question, the entity answering that question knows who you are, what you have, and what you're about to do. The single most consequential privacy improvement a Bitcoin user can make is to never ask third parties what they should be asking themselves. That is what running your own Bitcoin node provides.

This paper explains why. It walks through what a Bitcoin node actually does, what specific information leaks when you don't run one, and how each leak feeds the surveillance industry described in the companion SatoshiShield documentation. It then covers what node sovereignty does not solve, and how it fits with the other three layers of a complete privacy stack. The intended reader is someone who has heard *run your own node* repeated as a slogan and wants the technical reasoning behind the slogan.

## 1. The Privacy Stack and Where the Node Sits

Bitcoin privacy is not a single property. It is a stack of four layers, each leaking different information and each requiring its own defense. The companion document *Why Bitcoin Privacy Matters* describes the layers in detail; the table below recaps them for context.

| **Layer**        | **What leaks here**                                                                  | **Primary defense**                          |
|------------------|--------------------------------------------------------------------------------------|----------------------------------------------|
| Node sovereignty | Wallet talks to a third party to read the blockchain, revealing every address and IP | Run your own Bitcoin full node               |
| On-chain layer   | Public blockchain analysis links addresses and clusters wallets                      | CoinJoin, coin control, single-use addresses |
| Transport layer  | IP address visible to anyone you connect to                                          | Tor, privacy-respecting VPN                  |
| DNS layer        | Apps quietly query surveillance firm servers in the background                       | Pi-hole / AdGuard Home with SatoshiShield    |

The node sovereignty layer sits at the top of this list for a reason. The other three layers protect specific operations once a connection is happening — they make the connection harder to attribute, make the data inside it less revealing, or block the connection entirely when it goes to a known surveillance domain. The node layer is upstream of all of that. It governs *what your wallet asks for in the first place*, and *who it asks*. A wallet that asks a third party for its balance has already lost the privacy game before any of the other layers get a chance to engage.

The other layers exist because node sovereignty does not cover everything. Running a Bitcoin node does not stop on-chain analysis of transactions you have already made. It does not block surveillance firm domains being queried by unrelated apps on your network. It does not hide your IP from your ISP. Each layer has a job, and the job of the node layer is specific: prevent your wallet from broadcasting your identity and your holdings to third parties through routine queries.

## 2. What a Bitcoin Node Actually Is

Before discussing what a node prevents, it is worth being precise about what one is. A Bitcoin node is software that downloads, validates, and stores the entire Bitcoin blockchain, then connects to other nodes on the network to relay new transactions and blocks. Bitcoin Core is the reference implementation; alternatives like Knots and btcd exist but the function is the same.

A node does four things on behalf of its operator. First, it **validates**. Every block, every transaction, every signature is checked against the consensus rules. The node refuses to accept anything invalid. This is what gives Bitcoin its trustless property — you are not asking anyone whether a block is real, you are confirming it yourself. Second, it **stores**. The full blockchain, currently around 700 gigabytes for a pruned node and over a terabyte for an unpruned archival node, is held locally. Third, it **relays**. New transactions and blocks received from peers are forwarded to other peers, which is what propagates them across the network. Fourth, it **serves** — when a wallet asks the node for an address balance, a transaction history, or a fee estimate, the node answers from its local data.

The fourth function is the one that matters for privacy. A wallet without a node has no choice but to ask someone else those questions. A wallet with a node asks itself.

## 3. The Communication Problem

Bitcoin wallets perform a small set of operations that all require information from the blockchain. The operations are simple to describe but each one is a privacy event.

| **Wallet operation**              | **Information needed**                      | **Who has it**                       |
|-----------------------------------|---------------------------------------------|--------------------------------------|
| Display balance                   | UTXO set for each of the wallet's addresses | Whoever indexes the blockchain       |
| Show transaction history          | All transactions touching each address      | Whoever indexes the blockchain       |
| Calculate fee for new transaction | Current mempool fee distribution            | Whoever is connected to the mempool  |
| Broadcast transaction             | A connection to the peer-to-peer network    | Any full node                        |
| Check for new transactions        | Subscribe to address-related events         | An indexer with subscription support |
| Sync after offline period         | Blocks since last sync                      | Any full node or block explorer      |

In a node-less setup, all of these queries go to a third party. The third party might be a public Electrum server, a wallet vendor's API backend, a block explorer, or a price-and-data aggregator. Whoever it is, that entity now knows: this IP address operates this Bitcoin wallet, owns these addresses, holds these amounts, transacts on this schedule, and will broadcast this specific transaction at this specific time. Across a population of users, the entity assembles a database of identity-to-wallet correlations that would be invaluable to anyone working in the surveillance industry, and in many cases the entity *is* someone working in the surveillance industry.

This is not a hypothetical attack model. Many of the most popular public Electrum servers are operated by entities of unknown allegiance, and the dominant default configurations in popular wallets connect to them automatically on first launch. The privacy posture of the average Bitcoin user is determined more by where their wallet decides to look for data than by any decision the user has consciously made.

## 4. The Five Major Leaks Without Your Own Node

The communication problem manifests as a small number of specific, well-understood data leaks. Each one is a fingerprint that ties an identity to a wallet.

### 4.1 The xpub Leak

This is the worst of them. Modern Bitcoin wallets use hierarchical deterministic (HD) key derivation, defined in BIP32. A single master seed produces an extended public key, the **xpub**, from which the wallet derives every receiving and change address it will ever use. The xpub itself contains no private key material, but it is enough to derive the entire address sequence.

When a wallet connects to an Electrum server, it needs to tell the server which addresses to monitor. There are two ways this happens. The naive approach is for the wallet to send the xpub directly so the server can derive addresses on the wallet's behalf. The more careful approach is for the wallet to derive a batch of addresses locally and subscribe to each one individually. Both leak the same information, just packaged differently. The server learns: this connection cares about these addresses. Over time, the connection refreshes, requests history for additional derived addresses, and the server accumulates a complete picture of the wallet's address universe.

Combine this with the connecting IP address and the server now has: a home IP, the complete set of addresses ever used by a specific wallet, every balance change, every counterparty. This is a categorically worse leak than what an analytics firm gets from on-chain analysis alone. On-chain analysis produces probabilistic clusters; the xpub leak produces a verified, complete wallet labeling.

> *The xpub leak is the single worst privacy failure available in Bitcoin. A wallet connected to a hostile public Electrum server has effectively published its entire history to that server's operator.*

### 4.2 The Transaction Broadcast Leak

Broadcasting a transaction means sending it to the peer-to-peer network so it can propagate to miners. The transaction has to enter the network somewhere. The node that first receives a transaction is statistically the most likely candidate for being the originating node, because the transaction has to start somewhere and propagation is approximately concentric outward from there. Researchers have demonstrated that a well-connected adversarial observer running a high-degree node can identify the origin of new transactions with reasonable probability, especially when the transaction has not yet propagated widely.

A wallet without its own node broadcasts through a third party. The third party knows *for certain* which IP just submitted this transaction, because the transaction came in through an authenticated API call rather than peer-to-peer propagation. No statistical analysis is required. The third party may also delay propagation slightly to confirm the correlation, or to run additional analysis before relay.

When you broadcast through your own node, the transaction enters the public peer-to-peer network through your node's outbound peers. Your node looks like one of tens of thousands of nodes relaying transactions. An observer can still infer that you might be the source, but only probabilistically and only if they happen to be one of your peers or running an adversarial well-connected node. The natural privacy of the relay graph is restored.

### 4.3 The Fee Estimation Leak

Every wallet that lets the user choose a custom fee or recommends a fee level needs current mempool data. The fee depends on what miners are currently accepting, which depends on what other transactions are queued. Most wallets without a local node fetch this data from a third-party API — sometimes a generic Bitcoin data provider, sometimes the wallet vendor's own backend, sometimes a block explorer.

The privacy implication is timing. A wallet that queries fee estimates is almost always about to broadcast a transaction. The provider sees: this IP just asked for fees at this exact time, with this level of priority preference. If the provider also has access to mempool data, they can match the broadcast to the query within seconds and correlate the IP to the specific transaction. A wallet that fetches fees right before broadcasting is announcing its intention to broadcast.

### 4.4 The Bloom Filter Leak (BIP37)

Historically, simplified payment verification (SPV) wallets connected directly to Bitcoin full nodes and used bloom filters to request only the transactions relevant to them. The wallet would compute a bloom filter that matched its own addresses plus a configurable amount of noise, send the filter to the node, and receive back only the matching transactions. In theory, the noise made it hard for the node to know exactly which addresses belonged to the wallet.

In practice, bloom filters as deployed turned out to be devastatingly bad for privacy. Papers from 2014 and 2015 demonstrated that an adversarial node could deanonymize bloom filters reliably through statistical analysis, especially when the wallet reconnected and used slightly different filters across sessions. The Bitcoin Core developers effectively deprecated BIP37 for privacy reasons; default settings disabled bloom filter serving years ago. Modern light wallets have moved on to other approaches, none of which solve the underlying problem: if a wallet does not have its own data, it must ask someone who does, and that someone will know what was asked.

### 4.5 The Server Selection Leak

The choice of which third party to ask is itself a leak. The user who configures their wallet to connect to a specific Electrum server, block explorer, or wallet backend is making a sustained commitment of trust to that entity. Over months or years, that entity sees not just individual transactions but the user's entire pattern of Bitcoin engagement: when they check balances, what their average transaction size is, who they transact with, how active they are, when they go quiet. A relationship that begins as a convenient default can become a longitudinal surveillance record.

The risk is amplified by the fact that operating a public Electrum server is exactly the kind of investment a surveillance firm would make. The cost of running such a server is modest. The value of the data passing through it, for an entity in the address-attribution business, is substantial. Several public Electrum servers in widespread use have operators of unclear allegiance, and at least some have been credibly suspected of being run by surveillance-adjacent entities. The default behavior of most wallets — connect to whoever is fastest — selects for exactly these adversarial servers when they are well-resourced.

## 5. How Your Own Node Eliminates These Leaks

Running your own Bitcoin node addresses every one of the leaks in Section 4, because each leak is fundamentally the same problem: needing to ask a third party a question that should not require a third party. When the wallet talks to a node operated by the same person who controls the wallet, the question and the answer never leave the user's possession.

### 5.1 Bitcoin Core RPC and the Native Interface

Bitcoin Core exposes a JSON-RPC interface through which a wallet can ask for any information the node has indexed. Some wallets — including Bitcoin Core's own integrated wallet, and others like Sparrow with the appropriate configuration — can connect directly to this RPC interface. No external data source is involved. Balance queries, transaction history, fee estimates, and transaction broadcast all happen between the wallet process and the node process. If they run on the same machine, the data never leaves localhost. If they run on different machines on the same trusted network, the data crosses the local network only.

### 5.2 The Electrum Server Overlay (Electrs, Fulcrum)

Bitcoin Core's RPC interface is not optimized for the kinds of queries Electrum-protocol wallets make. To bridge this gap, open-source projects have built Electrum-protocol-compatible server implementations that run on top of Bitcoin Core. **Electrs** (written in Rust) and **Fulcrum** (written in C++) are the two main implementations. Both index Bitcoin Core's blockchain data into a structure optimized for address-based queries, and both expose an Electrum protocol endpoint on the local network.

The wallet sees the familiar Electrum protocol interface. The user gets fast queries and full feature compatibility. The privacy property is that the Electrum protocol now terminates inside the user's own infrastructure rather than at a public server run by an unknown party. The xpub leak, the transaction history leak, and the server selection leak all disappear because the server is yours.

### 5.3 Local Broadcast and Relay Graph Privacy

When a transaction is broadcast through Bitcoin Core, it enters the peer-to-peer network through Bitcoin Core's outbound peer connections — typically eight peers chosen from across the network. The transaction then propagates outward through normal mempool relay. To an adversarial observer, the transaction appears to originate *somewhere* in the relay graph, but the originating node is one of tens of thousands and cannot be deterministically identified without privileged network access.

The privacy here is probabilistic, not absolute. A well-connected adversary running many nodes can still gain statistical information about transaction origins. The defense against this is to combine local broadcast with peer connections over Tor — covered in Section 6 — which makes the originating IP unobservable even to direct peers.

### 5.4 Local Fee Estimation

A node sees the entire mempool. Bitcoin Core's **estimatesmartfee** RPC produces fee recommendations based on the local mempool plus recent block data, no external API required. The timing leak disappears because no query leaves the local network. The wallet asks for fees, the node answers from local data, the wallet builds the transaction, the wallet broadcasts it through the node — and a third-party fee provider never knows any of it happened.

## 6. The Node-to-Network Layer

Running your own node solves the wallet-to-node problem. It does not by itself solve the node-to-network problem. Your node still has to connect to other nodes to participate in the Bitcoin peer-to-peer network. Those other nodes see your node's IP address and the transactions your node relays.

For most users this is acceptable in itself — a Bitcoin node is one of many on the network, and being a node operator is not by itself revealing. The risk surfaces when transactions originate from your node, because well-connected adversarial peers can perform statistical analysis on transaction origin times to make probabilistic guesses about which node first broadcast a given transaction. The defense is to run your node's peer connections over Tor.

Bitcoin Core has supported Tor connectivity for years and the configuration is well-documented. When configured for Tor-only outbound connections, your node still participates in the network, still relays transactions, still validates blocks — but the peers it connects to see only a Tor exit address rather than your home IP. Your node operates as an anonymous participant in the relay graph, and any transaction it originates inherits that anonymity at the IP layer. This is a significant additional defense and does not require any change to the wallet or to the node's other functions.

There is a tradeoff. Tor adds latency and occasionally peer connectivity issues, especially for newer nodes. The recommended configuration for most users is to allow both clearnet and Tor outbound connections, with Tor preferred — this gives the best balance of connectivity and privacy. Users with stronger threat models can configure Tor-only.

## 7. What Running a Node Does Not Fix

Node sovereignty is necessary for Bitcoin privacy. It is not sufficient. Three categories of privacy failure are unaffected by whether you run a node, and conflating them with the node-layer defense is a common mistake.

### 7.1 On-Chain Linkability

Every Bitcoin transaction is permanently recorded on the public blockchain. A surveillance firm analyzing the blockchain can cluster addresses, follow transaction flows, and link your transactions through common-input heuristics and change-address detection regardless of how you broadcast them. Running your own node prevents new privacy leaks; it does not undo old ones. Defending against on-chain linkability requires the second layer of the privacy stack: CoinJoin, coin control, single-use addresses, and avoiding the practices (address reuse, naive coin merging) that make clustering easy.

### 7.2 KYC Exchange Data Sharing

If you deposit Bitcoin to or withdraw it from a know-your-customer exchange, the exchange knows your identity and the addresses you used. The exchange shares this information with surveillance firms through commercial partnerships, subpoenas, and other data flows that have nothing to do with your wallet's choice of node. Running your own node does not affect this. The relevant defenses are at the on-chain layer (separating KYC and non-KYC funds, coin control to prevent them mixing in transactions) and at the lifestyle layer (minimizing KYC exchange use).

### 7.3 DNS-Layer Surveillance From Other Devices

A Bitcoin node serves one specific application — Bitcoin wallet queries. It does not affect the dozens of other apps on your network that may be quietly querying surveillance firm domains. Price trackers, portfolio apps, browser extensions, mobile wallet apps used by family members on the same network — all of these continue to make outbound connections to surveillance infrastructure regardless of how your Bitcoin node is configured. This is the gap that the DNS layer (Pi-hole or AdGuard Home with SatoshiShield) covers. The two layers are independent and complementary.

> *Run your node. Then install SatoshiShield. Each layer addresses a different attack surface, and neither one substitutes for the other.*

## 8. Practical Implementation

Running a Bitcoin node is more accessible now than at any time in Bitcoin's history. The practical paths fall into three categories of decreasing technical effort and increasing convenience.

### 8.1 Bitcoin Core on a General-Purpose Computer

The most direct path. Download Bitcoin Core from bitcoincore.org, run the installer, wait for the initial block download (typically a few days on a residential connection), and configure your wallet to connect to it. This works on Windows, macOS, and Linux. The disadvantages are that the computer needs to stay on (or be on whenever you want to use the wallet), and the initial download consumes significant disk space and bandwidth. The advantages are zero additional cost and full control over the configuration.

### 8.2 Dedicated Home Server Distributions

Several open-source projects bundle Bitcoin Core, an Electrum server, Tor configuration, and a friendly web interface into a turnkey distribution that runs on a Raspberry Pi or small dedicated computer.

| **Distribution** | **Focus**                                | **Notes**                                                         |
|------------------|------------------------------------------|-------------------------------------------------------------------|
| Umbrel           | Easiest setup, app marketplace           | Most popular; broad ecosystem of optional apps beyond Bitcoin     |
| Start9 (StartOS) | Privacy-first defaults, Tor-only         | Strong defaults including SSO over Tor; pricier hardware          |
| RaspiBlitz       | Raspberry Pi-native, Lightning-focused   | More configuration-forward; popular with Lightning node operators |
| MyNode           | Bitcoin and Lightning, paid premium tier | Free community edition exists; premium adds features              |

These distributions handle the operational complexity — disk management, automatic updates, Tor configuration, wallet connection endpoints — and let the user focus on using the node rather than maintaining it. The hardware is modest: a Raspberry Pi 4 or 5 with a 2 terabyte SSD is sufficient for any of them. Total hardware cost is typically two to four hundred dollars.

### 8.3 Connecting Wallets to Your Node

Once the node is running, the wallet needs to be configured to use it. Each wallet has its own configuration path.

| **Wallet**              | **Connection method**                                                                       |
|-------------------------|---------------------------------------------------------------------------------------------|
| Bitcoin Core (built-in) | Native; no configuration needed                                                             |
| Sparrow Wallet          | Server settings → connect to your Electrs/Fulcrum endpoint, or directly to Bitcoin Core RPC |
| Electrum (desktop)      | Servers menu → add your own Electrum server, remove public ones                             |
| BlueWallet (mobile)     | Settings → Network → Electrum → enter your server (typically over Tor)                      |
| Specter Desktop         | Connect directly to Bitcoin Core RPC; supports hardware wallet integration                  |
| Nunchuk                 | Connect to your own Electrum server via Tor                                                 |

Mobile wallets need special attention. Connecting a mobile wallet to a home node requires the home node to be reachable from the mobile device, which usually means running the home node's Electrum endpoint as a Tor hidden service and configuring the mobile wallet to connect over Tor. Most of the home server distributions in the previous section handle this automatically and provide a connection string or QR code that the mobile wallet can scan.

### 8.4 Wallet Behavior to Watch For

Even after configuring a wallet to use your own node, some wallets still make supplementary requests to third-party APIs — for price data, for exchange rates, for software update checks, for analytics. These calls are independent of the node configuration and need to be addressed separately. The general defenses are: prefer open-source wallets that document their network behavior; review the wallet's source code or audit reports for non-essential phone-home behavior; run the wallet on a network that has SatoshiShield installed to block known surveillance domains regardless of which app makes the call; and check the wallet's traffic with a tool like Wireshark or Pi-hole's query log to verify it is doing what it claims.

## 9. Threat Models

Different users face different adversaries. The privacy properties of running a node are valuable to all of them, but the specific benefits and the level of additional hardening required vary.

### 9.1 The Average User

The baseline threat is passive commercial surveillance — surveillance firms collecting data because their business model rewards it, exchanges screening deposits because regulators require it, data brokers ingesting whatever they can buy. The average user is not a targeted investigation subject; they are part of a population being processed at scale. For this threat model, running a node addresses the largest single privacy leak (wallet-to-server queries) and is sufficient combined with the rest of the SatoshiShield privacy stack. Tor for node peers is recommended but not essential.

### 9.2 The Significant Holder

A user with significant Bitcoin holdings becomes a higher-value target. Adversaries here include not just surveillance firms but also criminals who might use surveillance data to identify physical targets, divorcing spouses, civil litigants, and lifestyle creep where insurance, lending, and employment decisions start factoring in the user's documented holdings. For this threat model, a node alone is insufficient — the user needs the full four-layer stack, Tor-routed node peers, CoinJoin practices for amounts where on-chain privacy matters, careful operational separation of identities, and minimal use of KYC exchanges going forward.

### 9.3 The Journalist, Activist, or Donor at Risk

Users whose transactions could attract retaliation — journalists paying sources, activists in authoritarian environments, donors to causes that attract legal or political consequences — face adversaries with non-commercial motivations and potentially with state resources. Node sovereignty is essential here, and so are Tor for both node and wallet, CoinJoin, careful identity compartmentalization, and physical opsec around the node itself. The threat model also includes future regime change, which means the user must assume that data that is safe today may be evidence later. The combination of running your own node and following strict operational hygiene is the only credible defense against well-resourced adversaries operating across long time horizons.

### 9.4 The Self-Custody Practitioner

A user who runs their own node, holds their own keys, and avoids custodial services is doing the right thing — and in the perverse logic of surveillance firm risk-scoring, this profile sometimes itself attracts elevated risk scores. Some compliance systems treat self-custody behavior as anomalous and elevate the user's risk score accordingly. This is not a reason to use custodial services; it is a reason to understand that the surveillance industry's incentives are not aligned with the principles of self-sovereignty, and that visible self-custody alone is not protection. The full stack is required.

## 10. Implementation Roadmap

For readers ready to deploy a node, the practical sequence is approximately this. Each step builds on the last; the gates between them are willingness to invest more time and effort rather than technical prerequisites.

**Step 1 — Get Bitcoin Core running, even imperfectly**

Install Bitcoin Core on a computer you already own, let it do the initial block download in the background, and verify it works. This step is the largest psychological barrier — once a node is running locally, the operational confidence required for everything else is much easier to build.

**Step 2 — Connect a wallet to it**

Configure Sparrow, Specter, or Electrum to use your local node. Verify that the wallet works end-to-end: check balances, receive a small test transaction, broadcast a small test transaction. This step makes the privacy benefit concrete; you have moved from theoretical sovereignty to operational sovereignty.

**Step 3 — Add the Electrum server overlay**

If your wallet of choice prefers the Electrum protocol, install Electrs or Fulcrum on top of your Bitcoin Core. Reconfigure the wallet to point at your local Electrum endpoint. Verify everything still works. You now have a complete sovereign indexer.

**Step 4 — Enable Tor for peer connections**

Add Tor to your node's configuration and let it use Tor for outbound peer connections. This is a one-time configuration change to bitcoin.conf. After this step, your node participates in the relay graph without revealing your IP address to peers.

**Step 5 — Move to a dedicated home server**

If your initial setup runs on a general-purpose computer that you also use for other things, consider migrating to a dedicated home server distribution like Umbrel, Start9, RaspiBlitz, or MyNode. This decouples your Bitcoin infrastructure from your daily-use machine and lets the node run continuously without competing for resources. It also makes mobile wallet connections via Tor hidden services much easier to configure.

**Step 6 — Install SatoshiShield on the same network**

Run Pi-hole or AdGuard Home with the SatoshiShield blocklist on the same home network as your node. This addresses the DNS-layer surveillance gap that your node does not cover, protecting every device on the network from the background surveillance described in the companion documentation.

At this point you have all four layers of the privacy stack deployed: node sovereignty (this paper), DNS-layer protection (SatoshiShield), transport-layer privacy (Tor for node peers), and the foundation for on-chain privacy practices (CoinJoin, coin control) that you can apply transaction by transaction. Each subsequent improvement is an enhancement on a complete baseline rather than a band-aid on a fundamentally leaky setup.

## 11. Conclusion

The slogan *run your own node* has been repeated so often in Bitcoin culture that its specific meaning has eroded. The slogan exists for a reason. A wallet without a node is a wallet that asks a third party where its money is, what its money has done, and where its money is going next. The third party answers, and in doing so it learns those things itself. The third party's incentive structure determines what happens with that knowledge — and the third parties most likely to be answering are precisely those most incentivized to collect, correlate, and sell it.

Running your own node breaks this loop. The questions stay inside your own infrastructure. The answers come from data you have validated yourself. The wallet becomes self-contained in the way Bitcoin was originally designed to allow. None of the other privacy layers — DNS blocking, Tor, CoinJoin, coin control — substitute for this. They all address adjacent problems, and they all assume that the foundational problem of wallet-to-server data leakage has been solved upstream.

The investment is modest. A few hundred dollars of hardware, a weekend of setup, and the ongoing cost is essentially zero. The benefit is the foundation that everything else in the privacy stack assumes. If you are going to do one thing for your Bitcoin privacy, run your own node. Then build the other three layers around it.

> *Self-sovereignty starts at the layer where the questions are asked. Without your own node, the questions go to someone else, and someone else gets the answers.*

**References and Further Reading**

SatoshiShield project documentation:

· *Why Bitcoin Privacy Matters* (plain language guide) — companion document covering the four-layer privacy model in accessible terms.

· *Why Bitcoin Privacy Matters: Deep Dive* — extended treatment of the surveillance industry, its techniques, and its real-world consequences.

· *SatoshiShield White Paper* — methodology and architecture of the DNS-layer blocklist that addresses the fourth privacy layer.

Technical references for node implementation:

· Bitcoin Core — bitcoincore.org

· Electrs — github.com/romanz/electrs (Rust Electrum server)

· Fulcrum — github.com/cculianu/Fulcrum (C++ Electrum server)

· Umbrel — umbrel.com

· Start9 — start9.com

· RaspiBlitz — raspiblitz.org

· MyNode — mynodebtc.com

Academic and historical context:

· Gervais et al., *On the Privacy Provisions of Bloom Filters in Lightweight Bitcoin Clients* (2014) — the foundational analysis of BIP37 privacy failures.

· Koshy, Koshy, McDaniel, *An Analysis of Anonymity in Bitcoin Using P2P Network Traffic* (2014) — origin attribution from transaction propagation patterns.

· Bitcoin Optech — bitcoinops.org — ongoing newsletter coverage of privacy-relevant Bitcoin protocol developments.

**Document Version**

| **Version** | **Date** | **Changes**                                                                                                                                                                                                                                                                                                                         |
|-------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.0         | May 2026 | Initial paper. Covers node sovereignty as the foundational layer of the SatoshiShield privacy model. Sections on the communication problem, the five major leaks, how a self-hosted node addresses each, threat models, and a step-by-step implementation roadmap. Companion to the existing Why Bitcoin Privacy Matters documents. |
