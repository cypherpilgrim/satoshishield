# The Background Hum

### A Day in the Life of an Unprotected Bitcoin User

*A SatoshiShield Case Study*

**Version 1.0  ·  May 2026**

Published by SatoshiShield  ·  [github.com/cypherpilgrim/satoshishield](https://github.com/cypherpilgrim/satoshishield)

*Free to share with attribution.*

---

## Table of Contents

- [A Note Before You Begin](#a-note-before-you-begin)
- [1. Meet Carlos](#1-meet-carlos)
- [2. The Morning](#2-the-morning)
- [3. What the Surveillance Company Sees](#3-what-the-surveillance-company-sees)
- [4. How the Picture Sharpens Over Time](#4-how-the-picture-sharpens-over-time)
- [5. Every Address You Will Ever Use](#5-every-address-you-will-ever-use)
- [6. The Household Amplifier](#6-the-household-amplifier)
- [7. The Enrichment Layer](#7-the-enrichment-layer)
- [8. When This Becomes a Real-World Consequence](#8-when-this-becomes-a-real-world-consequence)
  - [8.1 The Frozen Exchange Account](#81-the-frozen-exchange-account)
  - [8.2 The Quiet Career Impact](#82-the-quiet-career-impact)
  - [8.3 The Insurance and Lending Profile](#83-the-insurance-and-lending-profile)
  - [8.4 The Physical Risk](#84-the-physical-risk)
  - [8.5 The Retroactive Risk](#85-the-retroactive-risk)
- [9. The Same Morning, Protected](#9-the-same-morning-protected)
- [10. What Carlos Should Do](#10-what-carlos-should-do)
- [11. Closing](#11-closing)
- [References and Further Reading](#references-and-further-reading)
- [Document Version](#document-version)

---

## A Note Before You Begin

Everyone who uses Bitcoin has heard that the network is public. Most people understand this in the abstract — there is a ledger, the ledger records every transaction, and the ledger does not forget. What most Bitcoin users do not understand is what that public ledger looks like in the hands of a company whose business is identifying the people behind it. They do not understand what those companies know, how they came to know it, or what they do with what they know.

This paper is an attempt to make those questions concrete. Instead of explaining surveillance in the abstract, it follows one ordinary Bitcoin user through one ordinary day, and shows what a surveillance company already knows about him by sunset. He is a fictional person, but every detail of what happens to him is drawn from how the surveillance industry actually operates. By the end of the paper, the reader should understand not just that surveillance exists, but exactly what it sees, exactly when it sees it, and exactly what it eventually does with what it has seen.

No technical knowledge is assumed. The paper does not explain protocols or algorithms. It explains what happens to a person.

---

## 1. Meet Carlos

Carlos is thirty-eight years old. He works as a marketing manager for a regional bank in Houston, a job he has held for eleven years. He lives with his wife and their fifteen-year-old daughter in a comfortable middle-class neighborhood. He drives a six-year-old SUV, pays his bills on time, and is not the kind of person any government has any interest in. He has never been arrested. He has never been audited. He has never been suspected of anything.

Carlos has also, over the last three years, quietly accumulated about half a Bitcoin. He thinks of it as his daughter's college fund. He bought most of it through Coinbase and a little through River, both of which required him to upload his driver's license when he opened the accounts. He keeps the Bitcoin in a hardware wallet at home, secured with a passphrase he memorized. His recovery phrase is stamped into a stainless steel backup plate stored in a fireproof safe — a setup designed to survive fire, flood, and the decades over which he expects to hold the coins. He uses an app on his desktop computer called Sparrow to view his Bitcoin balance and prepare transactions. He uses a different app on his phone, BlueWallet, for the smaller amounts he occasionally sends to friends or to his sister-in-law who lives in Spain.

Carlos thinks of himself as careful. He does not reuse Bitcoin addresses. He does not post about his holdings on social media. He uses a hardware wallet rather than leaving Bitcoin on an exchange. He keeps his recovery phrase offline, on stainless steel, in a safe. When he reads articles about Bitcoin privacy, he nods along and feels reassured that he is doing the right things.

By the end of this paper, a Bitcoin surveillance company will know Carlos's neighborhood, his employer, the names of his wife and daughter, the size of his Bitcoin holdings, the source of every coin he owns, the destinations of every coin he has sent, the hours he sleeps, the routes he commutes, and the schedule on which he checks his balance. None of this will require any criminal act on Carlos's part, any court order, any subpoena, any hack on the surveillance company's part, or any conscious decision by Carlos to share any of it. It will all come from data that his phone and his computer volunteer in the background while he goes about his normal life.

> Carlos has done everything right by the standard of mainstream Bitcoin advice. By the end of one month, a surveillance company knows more about him than his own bank does.

---

## 2. The Morning

It is 7:14 on a Tuesday morning. Carlos's alarm has not yet gone off. His phone is on the nightstand, plugged in, screen dark. To anyone watching the bedroom, nothing is happening. To anyone watching his home internet connection, the next ninety seconds are extraordinarily eventful.

His phone has woken up briefly, as phones do, to refresh the apps running in the background. The Bitcoin wallet app on his phone wakes up and reaches out to a series of remote servers, asking each one a small question. It asks one server whether there is a software update available. It asks another server for the current Bitcoin price. It asks a third server what the current network fee is. It asks a fourth server whether any new transactions have arrived at any of the Bitcoin addresses it is monitoring. It also, without Carlos's awareness, reports to two separate analytics services that the wallet app has been opened — which version of the app, on which type of phone, in which country, at which time.

While the wallet is doing all of this, a separate app on his phone — a portfolio tracker Carlos installed two years ago to watch his Bitcoin value in dollars — wakes up and does its own version of the same dance. It asks an external server what Carlos's Bitcoin balance is by sending it a list of the Bitcoin addresses Carlos has previously entered into the tracker. It reports its own analytics. It pings a help-desk service. It checks for updates.

All of this happens before Carlos's alarm goes off. By the time Carlos reaches for his phone at 7:17, every relevant server in the world has already been told that Carlos is awake, what apps he uses, what addresses he cares about, and what his Bitcoin balance is. He has not made a single conscious choice yet.

He spends the next ten minutes the way most people spend the first ten minutes of their day. He scrolls through messages. He reads a news article. He glances at his Bitcoin balance in the portfolio tracker. Every one of these actions generates new background requests to remote servers, each one logged. By 7:30, when he gets in the shower, his phone has made roughly two hundred background requests, of which several dozen are relevant to his Bitcoin activity.

This is the normal background hum of a modern smartphone. It happens every morning. It happens whether Carlos uses Bitcoin or not, but the Bitcoin-related apps add their own contributions to the chorus. Nothing about it is unusual. Nothing about it requires Carlos to have done anything special. The surveillance does not begin when Carlos decides to do something interesting; it is always running, in the background, while he sleeps.

---

## 3. What the Surveillance Company Sees

Across the world, in an office that Carlos has never heard of, an analyst at a Bitcoin surveillance company could, if she chose to, pull up Carlos's record. She would not know him by name yet. To her, he is a row in a database, identified by the unique address his home internet connection presents to the world. But the row is detailed, and it gets more detailed by the hour.

Here is approximately what the analyst would see if she opened Carlos's record at the end of his first Tuesday:

| Field | What the record shows |
|---|---|
| **Location** | Houston, Texas. Internet provider AT&T. Residential connection. Geographic precision: neighborhood. |
| **Devices in use** | Three devices observed: an iPhone, a Mac laptop, an iPad. Activity patterns suggest a household of three people. |
| **Bitcoin-related apps observed** | BlueWallet mobile, Sparrow desktop, a portfolio tracker, occasional use of a Bitcoin block explorer in a web browser. |
| **Activity pattern** | Morning peak between 7:10 and 8:30. Evening peak between 19:00 and 22:30. Quiet between 23:00 and 7:00, consistent with a typical sleep schedule. Pattern suggests employed adult, not a night-shift worker. |
| **Bitcoin addresses associated with this connection** | Forty-seven unique Bitcoin addresses observed over the last thirty days. Forty-one of these belong to the same wallet, identified through standard analytical techniques. |
| **Estimated Bitcoin balance** | Approximately 0.487 Bitcoin, worth approximately 28,000 US dollars at current prices. |
| **Transaction history visible from the blockchain** | First Bitcoin received in August 2023 from a Coinbase exchange wallet. Subsequent purchases from the same exchange. One large incoming transfer from an address that appears to belong to a freelance worker in Spain. Four outgoing transactions, all small, to addresses that pattern-match exchange deposit addresses. |
| **Identity correlation** | The same internet address completed identity verification at Coinbase in August 2023, and at River in early 2024. The name on those accounts is on file with both exchanges and is, through standard commercial data-sharing arrangements, on file with this surveillance company as well. |

The analyst, having opened the record out of curiosity, can now see Carlos's full name, his estimated Bitcoin balance, where he lives, where he banks, what apps he uses, what hours he keeps, who his household appears to be, and the entire history of his Bitcoin activity for the last three years. She has not subpoenaed anything. She has not hacked anything. She is looking at a routine entry in a commercial database that her employer maintains as a standard part of its business.

This database is sold to government agencies, to banks, to exchanges, to insurance companies, and to anyone else who is willing to pay for access. Carlos has no idea that the database exists, no idea that he is in it, and no way to ask for his record to be corrected, deleted, or restricted in any way.

---

## 4. How the Picture Sharpens Over Time

On its own, a single morning of background requests would not produce much. The first day Carlos's phone made these requests, the surveillance company would have seen a few queries from an unknown internet address in Texas and would not have known what to make of them. The first week would have produced a thin sketch. The first month produces the dossier described in the previous section.

The mechanism is repetition. Every morning, the same apps wake up at roughly the same time and make roughly the same requests. After two weeks, the surveillance company is no longer guessing about Carlos's schedule; it knows. After three weeks, it knows which day of the week he buys groceries and which day he goes out with friends. After a month, it can predict, within a fifteen-minute window, when Carlos will check his Bitcoin balance tomorrow morning.

The same thing happens with his Bitcoin addresses. Every time Carlos's wallet generates a new address — to receive money from a friend, to send to himself as change from a transaction — that new address has to be checked against the network to see whether it has received anything. The check is made by sending the address to a remote server. The server logs it. After a month, the surveillance company has a complete inventory of every Bitcoin address Carlos's wallet has ever used or will ever use, in the order it was generated. It does not need to guess; the wallet itself, through its routine operation, supplied the list.

This is one of the more devastating aspects of the surveillance, because it means that the picture sharpens automatically. Carlos does not need to do anything new. He just needs to continue using his wallet the way he has been using it. Each day, the company learns slightly more. Each month, the picture becomes more complete. After a year, the picture is essentially complete for any practical purpose.

> The surveillance does not require Carlos to make a mistake. It requires him to continue existing as a Bitcoin user.

---

## 5. Every Address You Will Ever Use

Modern Bitcoin wallets generate a fresh address every time the user needs one. This is a good privacy practice in principle — it prevents anyone watching the blockchain from easily connecting all of a person's transactions to a single address. The trouble is that the wallet then has to monitor all of these addresses to know when funds arrive at them, and it monitors them by asking a remote server.

From the wallet's perspective, this is just bookkeeping. From the server's perspective, it is the entire wallet, handed over in installments. The wallet asks the server about its first receiving address on the day Carlos installed it. A week later, when Carlos receives a payment, the wallet asks the server about a second address. A month later, after Carlos has made a few transactions, the wallet is asking about a dozen addresses. After a year, the server has been told about every address Carlos's wallet has ever generated.

There is a quieter detail that makes this worse than it sounds. The drip does not stop because Carlos changes his behavior — it stops only when he stops using that wallet. As long as he keeps the same recovery phrase, every new transaction adds new addresses to the file, and switching to a Pi-hole tomorrow does not unleak yesterday's queries. And there is a sharper exposure that is easy to underestimate: the addresses a wallet generates are not random. They are all derived from a single master public key, the xpub, which is supposed to live only inside the wallet. But ordinary actions can hand it over — pasting it into a block explorer's "xpub watch" field, importing it into a portfolio tracker, installing a wallet app whose backend services receive xpubs for "sync" or "discovery." Anyone holding the xpub can derive every address the wallet has ever generated and every address it ever will. Individual addresses leak one at a time. An xpub is the entire future of that wallet, handed over in a single keystroke.

This is the asymmetry at the heart of the problem. The data Carlos has already leaked cannot be unleaked. The surveillance posture he had yesterday determines what is observable about him tomorrow, even if he changes his behavior today. The only complete remedy, having leaked what he has already leaked, is to retire the compromised wallet entirely and generate a new one from a fresh recovery phrase that has never touched the surveillance network. Better DNS hygiene protects the new wallet; it cannot save the old one. Most users do not understand that they need to do this, and most never do.

---

## 6. The Household Amplifier

Carlos does not live alone. His wife and daughter use the same home internet connection. To the outside world, all of their devices appear to share the same internet address. The surveillance company cannot easily separate the three of them, and in practice does not need to — they treat the household as a single profile, attributing all activity from the shared address to whoever in the household is most identifiable.

Carlos's wife has a small Bitcoin balance of her own, kept in a Cash App account she uses to send occasional gifts to her sister in Madrid. She thinks of it as pocket money. From the surveillance company's perspective, every time she opens the app, it adds to the household's profile. The activity pattern reveals a second adult on the network. The transaction destinations reveal a family connection in Spain. The amounts reveal a level of disposable income. None of this is sensitive in isolation; aggregated, it adds context that sharpens the picture of who lives at this address and how they use money.

Carlos's daughter does not use Bitcoin. She follows the Bitcoin price out of curiosity, through a tracking app she installed because some of her friends invest. The tracking app does not require her to enter any Bitcoin addresses — she does not have any — but it still makes background requests to several price-aggregation services, and those services log the home internet address. The daughter's app does not reveal any Bitcoin holdings, because she has none, but it does add a third device fingerprint to the household profile and confirms that there is sustained interest in Bitcoin at this address.

If any one of the three household members ever logs into a service tied to their real name — a work email, a school portal, a bank login — from a device on this internet connection, the surveillance company can attach that name to the household profile. The carefulness of any individual member does not protect them from the unguarded activity of the others. Carlos can use a hardware wallet and avoid posting about Bitcoin online, but if his wife logs into her employer's email portal from a laptop that shares the internet connection, his Bitcoin activity is no longer hard to attribute.

> The privacy of one person on a network is set by the weakest privacy practice in the household. Defending Carlos alone is impossible. Defending the network protects everyone at once.

---

## 7. The Enrichment Layer

The data the surveillance company collects from Carlos's network is rich on its own, but the company's true product is not raw collection — it is the combination of that data with information bought from other sources. The broader commercial data market in most countries is large, well-funded, and almost entirely unregulated. Surveillance companies are routine customers.

Some of the additional data sources the company can buy or trade for include the following. Credit card processors sell data about where Carlos has used his cards, which establishes his neighborhood and his work commute. Mobile advertising networks sell data about which apps he uses, which fills in interests and habits. Email signup databases sell data linking his email address to his real name and to his employer. Property records, often public, confirm his home address. Voter registration databases, also often public, confirm his civic identity. Data breaches — and there are many — provide phone numbers, prior passwords, security question answers, and sometimes documents.

None of this is exotic. All of it is for sale, in many jurisdictions legally and in most jurisdictions tolerated. By the time Carlos has been observable on the surveillance company's collection systems for a few weeks, his record has been enriched with everything the open commercial data market knows about a man named Carlos who lives at his address and works at his bank. The record is no longer about an unknown internet address in Texas. It is about Carlos personally.

The same enrichment happens for his wife and daughter. By the end of the first month, the surveillance company's record of the household looks less like a technical surveillance profile and more like a family bio with a Bitcoin balance attached.

---

## 8. When This Becomes a Real-World Consequence

The record exists. Most of the time, nothing happens with it. The record sits in a database, gets queried occasionally during routine compliance checks at exchanges and banks, and otherwise does nothing visible to Carlos. He goes about his life unaware that the record exists. This is the normal state of affairs for the vast majority of people whose data is in these systems.

But the record is queryable. And when something happens to trigger a query, the consequences for Carlos can arrive without warning, without explanation, and without any meaningful recourse.

### 8.1 The Frozen Exchange Account

The most common consequence is also the most banal. Carlos sells some Bitcoin to cover a car repair. He sends the Bitcoin to his Coinbase account. Coinbase, as part of its standard compliance process, queries the surveillance database with the source addresses of the Bitcoin Carlos sent. The database returns a risk score. If the score is low, the deposit clears in minutes and Carlos sees the funds in his account. If the score is elevated, the deposit is frozen pending review.

The score can be elevated for reasons that have nothing to do with anything Carlos did. The freelancer in Spain who paid Carlos two years ago may have, in the intervening time, transacted with someone who later transacted with a sanctioned entity. The taint propagates backward. The surveillance company's automated systems detect the chain of connections and elevate the score. Carlos's deposit, which used a Bitcoin that touched the freelancer's wallet, inherits the elevation.

Carlos receives an email asking him to provide documentation of the source of the funds. He provides what he has — bank records, freelance invoices, a written explanation. Sometimes the documentation satisfies the exchange and the account is unfrozen weeks later. Sometimes it does not, and the funds are forfeited to the exchange under the broad authority granted in the terms of service Carlos agreed to without reading. He has not been charged with a crime. He has not been convicted of anything. The decision is administrative. There is no appeal that any court will hear.

### 8.2 The Quiet Career Impact

Carlos's employer is a bank. The bank, like most financial institutions, runs periodic checks on its employees for compliance reasons. Some banks include cryptocurrency holdings in these checks; others do not yet, but the practice is spreading. If Carlos's employer runs such a check, the surveillance database returns a profile showing that Carlos holds approximately twenty-eight thousand dollars in Bitcoin, transacts regularly, and has international counterparties.

None of this is illegal. None of it should be a problem in a healthy professional environment. In practice, financial institutions are conservative, and the appearance of cryptocurrency activity in an employee's profile can influence promotion decisions, transfer eligibility, and access to certain client portfolios. Carlos may never know that the check happened or what it returned. He may simply notice that the promotion he was expecting did not arrive, or that he was passed over for an international assignment he was qualified for. The connection between his Bitcoin activity and his career trajectory will never be made explicit. The data flows are quiet, and the decisions made on the basis of the data are quieter still.

### 8.3 The Insurance and Lending Profile

When Carlos applies for a mortgage to upgrade the family home, the lender runs the standard credit and risk checks. Some lenders, increasingly, include third-party data about cryptocurrency holdings in these checks. The data does not always disqualify an applicant, but it can affect the interest rate offered, the down payment required, or the willingness of the lender to approve the application at all. Carlos sees a rate quote that is slightly higher than he expected and assumes it is the market. He does not realize that his Bitcoin profile contributed to the quote.

The same dynamic plays out in life insurance, where Bitcoin holdings can influence risk classification, and in renters' background checks, where some property managers have begun screening for cryptocurrency activity as a proxy for financial volatility. None of these decisions are explained to the affected person. The data is commercial, the decisions are automated, and the affected person is rarely told what data was considered.

### 8.4 The Physical Risk

This is the consequence people do not want to think about. A confirmed Bitcoin holder is a high-value target for ordinary criminals. The pattern, sometimes called a wrench attack, is straightforward: identify someone known to hold Bitcoin, find the physical address, and use violence or the threat of violence to compel the holder to hand over their keys. Documented cases exist in many countries. The victims have rarely been high-profile figures; they have been ordinary holders whose holdings became publicly knowable through one of the channels described in this paper.

Surveillance company databases leak. Customer records get breached, employees go rogue, and the data flows from the original collector into broader underground markets where it can be purchased by people whose interest in it is not academic. Once Carlos's name, address, and Bitcoin balance are connected in a commercial database, he has lost direct control over who knows. The probability of a wrench attack on any given Bitcoin holder remains small, but it is meaningfully larger than zero, and the consequences are severe enough that the asymmetry deserves serious attention.

### 8.5 The Retroactive Risk

The data is permanent. Carlos's Bitcoin activity today is being recorded today, but the consequences of that activity may not arrive for years. A transaction that is legal today may be illegal tomorrow, in jurisdictions where regulations change frequently. A counterparty who is clean today may be sanctioned next year. A government that is accepting of Bitcoin today may turn hostile after the next election. The blockchain does not forget, and the surveillance company's database does not forget, and the data assembled today will be queryable for any future purpose that anyone with access decides to pursue.

This is the consequence with the longest tail. Most users discount it because the future is hard to imagine concretely. But the costs of accumulating a permanent surveillance profile are paid out slowly, over decades, in ways that are nearly impossible to predict and even harder to reverse once they begin to arrive.

---

## 9. The Same Morning, Protected

Imagine that, three months before the morning described in Section 2, Carlos had installed a small device on his home network — a Pi-hole, costing perhaps forty dollars in hardware — and had loaded it with a Bitcoin-aware filter list of known surveillance company domains. Imagine that he had made this single change and nothing else. He still uses the same wallet, the same portfolio tracker, the same hardware wallet, the same exchange accounts, the same network. He still does not run his own Bitcoin node. He still has all the same habits. He has changed one thing.

Now consider the same Tuesday morning.

At 7:14, his phone wakes up and the apps begin their background refresh, the same as before. The wallet app reaches out to its update server. The portfolio tracker reaches out to its analytics service. The block explorer in the browser tab he left open reaches out to its backend. Each of these requests begins the same way it did before, with the device asking a directory service for the address of the remote server. In the protected setup, the directory service is the Pi-hole.

When the request is for a known surveillance company domain, the Pi-hole returns no answer. The device cannot find the server. The connection that would have carried Carlos's data outward never opens. The surveillance company never receives the request. It is not that the request is delivered and ignored; it is that the request is never sent. The remote system does not learn that Carlos failed to reach it, because it never learns that Carlos exists.

When the request is for a legitimate, non-surveillance domain — the block explorer he uses, the wallet developer's actual servers, the price feed he trusts — the Pi-hole answers normally and the request proceeds as it always did. Everything Carlos uses still works. The applications behave normally. Carlos sees no change in his daily experience.

From the surveillance company's perspective, however, the change is enormous. The detailed profile that, in the unprotected setup, accumulates from the daily background hum simply does not accumulate. The company knows what is on the public Bitcoin blockchain — they always know that, because the blockchain is public — but they do not know which internet address is generating the queries, which apps are being used, what the household pattern looks like, when activity peaks, or who lives at the address. The on-chain analysis still works, but it produces probabilistic clusters rather than verified, attributed wallets. The data broker enrichment still happens, but the bridge between the enrichment and the Bitcoin activity is broken.

The picture, in other words, becomes the picture that the surveillance industry has of someone who does not use Bitcoin at all, plus whatever the public blockchain reveals about Carlos's transactions. The aggressive correlation between identity, behavior, and on-chain activity that turned Carlos from an unknown wallet into a named person with a balance and an address — that correlation does not happen.

> DNS-layer protection does not make on-chain analysis go away. It severs the connection between on-chain analysis and the personal data that makes the analysis dangerous.

---

## 10. What Carlos Should Do

The most consequential thing Carlos can do takes one afternoon, costs less than a hundred dollars, and protects every device in his home for as long as he keeps it running. He can install a small device on his network — a Raspberry Pi or any spare computer — load it with Pi-hole or AdGuard Home, apply the SatoshiShield filter list, and let it sit. Once installed, it requires almost no ongoing attention. It updates itself. It blocks new surveillance domains as they are added to the list. It protects every device on the network, including the devices belonging to his wife and daughter, without any of them needing to install anything or change any habits.

This is the floor. It is the single highest-leverage privacy improvement Carlos can make. If he never does anything else, this one change shifts him from the unprotected category into the protected category, against the most pervasive form of Bitcoin surveillance.

If Carlos wants to do more, the additional steps are well-understood and have been documented elsewhere by the SatoshiShield project. The next step is to run his own Bitcoin node at home, which closes the leaks that occur when his wallet has to ask a remote server about his addresses. The step after that is to route his connections through Tor or a privacy-respecting paid VPN, which adds another layer of separation between his physical location and his network activity. The step after that is to use coin control and CoinJoin to address the privacy of his Bitcoin transactions on the blockchain itself.

Each step adds protection. None of them is required to begin. The most important thing is that Carlos does not wait for a perfect setup before starting. The Pi-hole and the SatoshiShield filter list will get him the majority of the practical benefit, and he can build the rest of the stack over time.

---

## 11. Closing

Carlos is fictional. The mechanisms described in this paper are not. Everything attributed to the surveillance company is something that surveillance companies actually do, using techniques that are well-documented, with data that is routinely bought and sold in the commercial market. Carlos's profile is composite, but it is composite in the way that every Bitcoin user's profile is composite — the same patterns, the same data sources, the same enrichment, the same consequences.

Most Bitcoin users will never see their dossier. Most will never know it exists. Most will go their entire lives without experiencing a frozen exchange account, a denied mortgage, a quiet career setback, or worse. The surveillance posture is not directly visible to most people most of the time. The cost of having the dossier is paid in the background, in opportunities that did not arrive, in decisions that were made without explanation, in vulnerability to consequences that may or may not arrive.

The question is not whether the surveillance is happening — it is, and the documentation is public for anyone who wants to verify it. The question is what each person decides to do about it. Carlos's choices are everyone's choices. The defenses are available, they are free, they are well-documented, and they work. The only thing standing between the unprotected and the protected is the decision to install them.

Privacy is not a crime. Blocking surveillance is not concealment. It is the recognition that data assembled today will be queried for purposes nobody can predict, by parties whose interests are not yours.

---

## References and Further Reading

**SatoshiShield project documentation:**

- [Why Bitcoin Privacy Matters](Why_Bitcoin_Privacy_Matters_v1_0.docx) — companion document covering the four-layer privacy model in plain language.
- [Why Bitcoin Privacy Matters: Deep Dive](Why_Bitcoin_Privacy_Matters_Deep_Dive_v1_0.docx) — extended treatment of the surveillance industry, its techniques, and its real-world consequences.
- Node Sovereignty: Why Running Your Own Bitcoin Node Is the Foundation of Privacy — companion paper covering the node-sovereignty layer of the privacy stack.
- [SatoshiShield White Paper](SatoshiShield_WhitePaper_v1_4.docx) — methodology and architecture of the DNS-layer blocklist.
- [SatoshiShield Pi-hole Monitor Deployment Guide](SatoshiShield_Monitor_Deployment_v1_4.docx) — practical setup instructions for the home network defense described in Section 10.

**Public documentation of the surveillance industry:**

- [USAspending.gov](https://www.usaspending.gov) — federal procurement records showing contracts awarded to Bitcoin surveillance vendors.
- [SAM.gov](https://sam.gov) — federal solicitation records for cryptocurrency tracing capabilities.
- The Intercept, CoinDesk, Decrypt — ongoing investigative reporting on surveillance vendor contracts and capabilities.

---

## Document Version

| Version | Date | Changes |
|---|---|---|
| 1.0 | May 2026 | Initial case study. Non-technical narrative paper following one hypothetical Bitcoin user through one day of unprotected activity, then through the same day with DNS-layer protection in place. Designed as an accessible companion to the more technical project documentation. |

---

*[github.com/cypherpilgrim/satoshishield](https://github.com/cypherpilgrim/satoshishield)  ·  MIT License  ·  Free to share with attribution.*
