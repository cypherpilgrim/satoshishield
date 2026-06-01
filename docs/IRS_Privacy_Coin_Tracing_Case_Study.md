# Breaking Privacy by Procurement

*The 2020 IRS Contract to Trace Monero and Bitcoin Lightning Network Transactions*

**Case Study**

---

## Executive Summary

In September 2020, the U.S. Internal Revenue Service Criminal Investigation Division (IRS-CI) awarded **Chainalysis Inc.** and **Integra FEC LLC** two parallel contracts worth up to $625,000 each — a combined ceiling of $1.25 million — to develop software capable of de-anonymizing transactions on Monero (XMR) and on Bitcoin's Lightning Network (LN). The awards are a matter of public record and are searchable on [USAspending.gov](https://www.usaspending.gov) and on the federal procurement system at SAM.gov.

The procurement is significant for three reasons. First, it represents the U.S. government openly funding the targeted defeat of two of the most widely deployed financial-privacy technologies in the cryptocurrency ecosystem. Second, it demonstrates that the U.S. tax enforcement posture toward privacy-preserving payments is operational, not theoretical. Third, the contract structure — half paid up front, half contingent on a working deliverable — establishes a market signal that financial-surveillance vendors can monetize the erosion of privacy at scale.

## Facts at a Glance

|                           |                                                                         |
|---------------------------|-------------------------------------------------------------------------|
| **Contracting Agency**    | U.S. Internal Revenue Service, Criminal Investigation Division (IRS-CI) |
| **Awardees**              | Chainalysis Inc. and Integra FEC LLC                                    |
| **Award Value**           | Up to $625,000 per firm — $1.25 million combined                      |
| **Award Date**            | September 30, 2020                                                      |
| **Performance Period**    | One year (initial), with deliverable due in approximately eight months  |
| **Solicitation Released** | September 4, 2020                                                       |
| **Targets**               | Monero (XMR) and Bitcoin Lightning Network (LN) Layer-2 transactions    |
| **Public Record**         | [USAspending.gov](https://www.usaspending.gov); SAM.gov solicitation 2032H820Q00076                    |

## Background

Monero (XMR) is a privacy-preserving cryptocurrency that uses ring signatures, stealth addresses, and confidential transactions (RingCT) to obscure sender, recipient, and amount on every transaction. By design, it does not expose the deterministic transaction graph that makes Bitcoin's base layer traceable.

The Bitcoin Lightning Network is a Layer-2 payment protocol that settles transactions through bilateral payment channels off-chain, with only channel open and close events committed to the Bitcoin blockchain. The transactions inside a channel — potentially thousands of them — are not broadcast publicly. The result is a payment substrate that is fast, cheap, and structurally opaque to conventional chain-surveillance tooling.

Both technologies pose a direct problem for forensic firms whose business models depend on clustering, attribution, and entity-resolution on transparent ledgers. The 2020 IRS solicitation was the federal government's most explicit acknowledgment to date that these privacy properties were a barrier to its enforcement objectives.

## The Solicitation

On September 4, 2020, IRS-CI published a Request for Proposals soliciting "innovative solutions for tracing and attribution of privacy coins." The document specifically named expert tools, data, source code, algorithms, and software development services as eligible deliverables.

The contract scope, drawn from the published solicitation, called on contractors to:

- Provide information and technical capabilities for CI Special Agents to trace transaction inputs and outputs to a specific user.

- Differentiate genuine senders from mixin and multisig participants in Monero ring signatures.

- Deliver tracing and attribution capability for Lightning Layer-2 transactions on Bitcoin.

- Operate with minimal involvement of external vendors after deployment — i.e., to give IRS-CI in-house capability.

The agency received 22 proposals. Two were selected.

## The Awardees

## Chainalysis Inc.

Chainalysis is the dominant commercial blockchain-analytics vendor in the United States and a longstanding IRS contractor. Its Reactor product had been in use across U.S. federal agencies for years prior to the 2020 award. Chainalysis was the only awardee that publicly delivered a tracing product within the contract window: in December 2021, three months after the contract period ended, the firm publicly announced Lightning Network support in its product suite.

## Integra FEC LLC

Integra FEC is a Texas-based forensic data analysis firm founded in 2012, historically focused on traditional financial-markets forensics. The firm has held a portfolio of federal contracts with agencies including the Department of Justice and the Securities and Exchange Commission. Its 2020 IRS award represented its public entry into the cryptocurrency-tracing market. No public delivery of a Monero or Lightning tracing product has been confirmed under the Integra contract.

## Contract Structure

Each of the two contracts was structured as a milestone-based award:

- **Phase 1 — Prototype:** $500,000 paid up front per contractor to fund development of a working tracing tool.

- **Phase 2 — Acceptance:** An additional $125,000 per contractor contingent on the IRS accepting the delivered tool as functional.

The full performance period was twelve months, with the working deliverable due in approximately eight. This pay-for-performance structure is conventional in federal R&D acquisition but is unusual in its public framing: the deliverable was, in plain language, the cryptographic and statistical defeat of a specific class of consumer privacy technology.

## Public Record and Verification

The contract is publicly verifiable. The Integra FEC award is indexed on [USAspending.gov](https://www.usaspending.gov) under contract award identifier **2032H820C00040**. The original solicitation, **2032H820Q00076**, was posted on SAM.gov (formerly beta.SAM.gov). The IRS contracting officer of record confirmed the award structure and ceiling values on the public record at the time of issuance.

This matters: the policy posture is not inferred from leaks or whistleblowers. It is documented in the federal procurement system, funded with appropriated dollars, and reported by the contracting agency itself.

## Strategic Implications

## For Privacy-Coin Users

The contract is a clear signal that Monero's privacy guarantees are an active enforcement target — not theoretically, but with paid contractors working against the protocol. The Monero Research Lab has subsequently published analyses of the statistical heuristics most likely to be deployed against ring signatures. Users relying on XMR for privacy should assume that probabilistic attribution attempts are ongoing.

## For Lightning Network Users

Chainalysis's December 2021 announcement of Lightning support — three months after the contract period closed — strongly implies that some form of Lightning tracing capability was delivered under this award. The network's privacy properties depend on routing topology, channel-funding patterns, and the absence of on-chain commitment for in-channel activity. Each of these is a surveillance surface. Operators of public Lightning nodes, in particular, should consider their attack surface against well-resourced graph-analysis adversaries.

## For the Broader Surveillance Market

The 2020 contract was followed by far larger procurement. By 2022, IRS-CI had moved into a multi-year, multi-million-dollar Chainalysis licensing arrangement reportedly worth more than $20 million, granting hundreds of yearly licenses, API access, training, and conference passes. The 2020 award functioned, in effect, as a venture-style bet that paid off into a recurring institutional revenue stream for the winning vendor.

## Analysis

Three observations are worth recording.

**First, the asymmetry.** A $1.25 million procurement is a rounding error in federal budgeting, but it is sufficient to fund focused statistical and infrastructural attacks against open-source privacy protocols developed by volunteer communities. The defender's cost is permanent and distributed; the attacker's cost is one-time and concentrated.

**Second, the legitimization effect.** By publicly procuring tracing capability against named privacy technologies, the federal government implicitly classifies those technologies as adversarial. This shapes downstream policy at exchanges, banks, and payment processors, who increasingly delist or refuse to onboard customers associated with these tools regardless of underlying conduct.

**Third, the probabilistic ceiling.** Industry voices, including CipherTrace CEO Dave Jevans at the time of the award, have acknowledged publicly that tracing Monero is not deterministic — the best a contractor can deliver is a probability score on a given hypothesis. This has implications for evidentiary standards: probabilistic chain analysis is not the same as a confirmed signature on a Bitcoin input, and defendants in cases built on such evidence have meaningful grounds to contest its weight.

## Conclusion

The 2020 IRS-CI award to Chainalysis and Integra FEC is the canonical public-record example of a federal agency directly funding the development of tools to defeat consumer financial-privacy technology. It is small in dollars and large in signal. For anyone operating in the Bitcoin and broader cryptocurrency ecosystem — whether as a developer, node operator, fund manager, or sovereign individual — it is a documented data point that the surveillance posture is funded, contracted, and operational, and that the privacy properties of any specific tool should be evaluated against the assumption that focused, paid adversaries are actively working against them.

The contract is, in short, the receipt.

## Sources and Further Reading

- [USAspending.gov](https://www.usaspending.gov) — Contract award 2032H820C00040 (Integra FEC LLC).

- SAM.gov — Solicitation 2032H820Q00076, "Pilot IRS Cryptocurrency Tracing."

- Decrypt — "IRS Dishes Out $1.25 Million for Data Firms to Crack Monero" (October 1, 2020).

- Bitcoin.com News — "Chainalysis and Integra Win $1.25 Million IRS Contract to Break Monero" (October 2, 2020).

- Modern Consensus — "IRS bets $1M Monero transactions are traceable" (October 1, 2020).

- Monero Research Lab — Public response to leaked IRS-CI training video on XMR tracing techniques.

- Chainalysis press release — Lightning Network support announcement (December 2021).

**  
**

**APPENDIX A**

**The Broader Federal Procurement Landscape**

*U.S. Government Contracts for Cryptocurrency Tracing, 2018–2025*

The 2020 IRS contract documented in the main case study is one milestone in a continuous procurement arc spanning at least seven years. This appendix summarizes the broader landscape of federal acquisitions targeting cryptocurrency privacy and traceability.

## A.1 The 2018 DHS / CipherTrace Pilot

Predating the IRS contract by approximately two years, the Department of Homeland Security Science & Technology Directorate awarded CipherTrace a contract reported at approximately $2.4 million to develop tracing capability targeting both Monero (XMR) and Zcash (ZEC). The capability was publicly announced in August 2020. This contract established the funding model the IRS would replicate: federal R&D dollars finance a private vendor's development of a capability against named privacy technologies, with the vendor retaining commercial rights to the resulting product.

## A.2 The IRS-CI Institutional Commitment (2023)

Following the 2020 pilot, IRS-CI converted its Chainalysis relationship into a multi-year institutional license. The contract is documented on [USAspending.gov](https://www.usaspending.gov) as Award ID **205AE923C00010**, total value **$21,515,583.20**, description "chainalysis web subscription," number of bidders **one**. The contract reportedly covers hundreds of annual user licenses, API access, training, and conference passes. A separate IRS-CI Cyber Crimes Unit contract worth $11.8 million covers casework and training.

## A.3 The FBI Escalation

FBI spending on Chainalysis grew from a cumulative $330,000 in 2017 to multi-million-dollar annual contracts. In December 2019 the FBI paid Chainalysis $377,500 for "Virtual Currency Tracing Tools" with options exceeding $3.6 million through 2022. The FBI is now on track to overtake the IRS as the largest federal Chainalysis customer.

## A.4 The Mastercard Acquisition of CipherTrace (2021)

In 2021, Mastercard acquired CipherTrace. A federally-funded blockchain surveillance capability was absorbed into a global payment network. The acquisition removed CipherTrace from the standalone federal-vendor market and consolidated the field around Chainalysis, with TRM Labs emerging as the second source.

## A.5 ICE Sole-Source Procurements (June 2025)

In June 2025, U.S. Immigration and Customs Enforcement posted two simultaneous notices of intent on SAM.gov to sole-source blockchain forensics tools — one from Chainalysis Government Solutions, one from TRM Labs — for the Homeland Security Investigations Cyber Crimes Center. The sole-source justification is a formal administrative finding that no other vendor is reasonably capable of providing the service. This is the federal government certifying, in writing, that the blockchain surveillance market has consolidated to a duopoly.

## A.6 Other Vendors of Note

- **TRM Labs:** Founded 2018, $1 billion valuation. AI-driven cross-chain screening with explicit national-security framing. Contracts with DHS, FBI, IRS, DEA, State Department.

- **Elliptic:** UK-based, dominant in private-sector compliance. Conspicuously small federal footprint — a widely cited federal-contract review identified a single $2,450 IRS contract. Appears to have made a deliberate strategic decision to position on the compliance-counterparty side rather than the surveillance-vendor side.

- **Integra FEC:** After the 2020 IRS award, Integra appears to have remained on the periphery of the blockchain-surveillance market with no confirmed public delivery of a working tracing product.

## A.7 Cumulative Pattern

Cumulative federal spending across all vendors and agencies on blockchain surveillance is comfortably into nine figures. The procurement pattern shows three consistent properties:

- **Privatized R&D:** Capability is funded by federal agencies but owned by private vendors, who then sell the resulting tools globally to banks, exchanges, and foreign governments.

- **Probabilistic ceiling:** No vendor publicly claims deterministic tracing of Monero. Capabilities deployed against privacy technologies are statistical and depend heavily on user error at on- and off-ramps.

- **Vendor consolidation:** The federal blockchain surveillance market has consolidated to the point where ICE in 2025 formally certified two vendors as sole-source providers.

For a full standalone treatment of the procurement landscape, see the companion case study, "The Federal Blockchain Surveillance Procurement Stack: A 2018–2025 Survey."
