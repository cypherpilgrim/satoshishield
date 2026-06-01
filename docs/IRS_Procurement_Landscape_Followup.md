# The Federal Blockchain Surveillance Procurement Stack

*A 2018–2025 Survey of U.S. Government Contracts to Trace, De-Anonymize, and Attribute Cryptocurrency Transactions*

**Case Study · Follow-Up**

---

## Executive Summary

The 2020 IRS contract to Chainalysis and Integra FEC is the most widely cited federal procurement targeting cryptocurrency privacy technology, but it is not the first, the largest, or the most recent. It sits inside a continuous arc of U.S. government acquisition that begins with a 2018 Department of Homeland Security R&D pilot and extends through *sole-source* ICE procurements posted in June 2025. Cumulative federal spending on blockchain surveillance across all vendors is now well into nine figures.

This case study maps that procurement landscape. It identifies the major contracts, the vendors that won them, the agencies funding the work, and the legal and structural significance of how the federal government has consolidated its blockchain-surveillance supply chain into a small number of effectively indispensable vendors.

## Procurement Timeline at a Glance

| **Year**  | **Agency**          | **Vendor(s)**                   | **Value**              | **Stated Scope**                                            |
|-----------|---------------------|---------------------------------|------------------------|-------------------------------------------------------------|
| **2018**  | DHS S&T             | CipherTrace                     | ~$2.4M                | Tracing Monero & Zcash                                      |
| **2019**  | FBI                 | Chainalysis                     | $377K + $3.6M option | Virtual Currency Tracing Tools                              |
| **2020**  | IRS-CI              | Chainalysis + Integra FEC       | $1.25M                | Monero & Bitcoin Lightning tracing                          |
| **2021**  | (Private)           | Mastercard acquires CipherTrace | Undisclosed            | Payment network absorbs federally-funded tracing capability |
| **2023**  | IRS-CI              | Chainalysis                     | $21.5M                | Web subscription / Reactor licenses (Award 205AE923C00010)  |
| **2023+** | IRS-CI Cyber Crimes | Chainalysis                     | $11.8M                | Casework support and training                               |
| **2025**  | ICE / HSI           | Chainalysis + TRM Labs          | Sole-source            | Two parallel notices; no competing vendor deemed available  |

## Phase 1: DHS Funds the First Generation (2018)

The first publicly documented federal contract targeting cryptocurrency privacy technology was awarded by the Department of Homeland Security Science & Technology Directorate to CipherTrace in 2018. The contract specifically named Monero (XMR) and Zcash (ZEC) — the two most prominent privacy-preserving cryptocurrencies — as targets.

CipherTrace, then led by CEO Dave Jevans, spent approximately one year on development and publicly announced the deliverable in August 2020, roughly one month before IRS-CI floated its own solicitation. Reported contract value was approximately $2.4 million, with a higher ceiling. The announced capability was limited at launch — transaction search, exploration, and visualization for Monero — and Jevans publicly characterized Monero tracing as "a probabilistic game" rather than a deterministic one.

**Structural significance:** the DHS contract established the funding model. A federal agency would pay a private vendor to develop the capability, the vendor would retain commercial rights to the resulting tool, and the same tool would then be sold back to other federal agencies and to private-sector compliance customers. The taxpayer underwrote the R&D; the vendor captured the commercial upside.

## Phase 2: The IRS Pilot (2020)

The September 2020 IRS-CI award to Chainalysis and Integra FEC — covered in detail in the companion case study — extended the DHS model to a second agency and added the Bitcoin Lightning Network to the explicit target list. Award ceiling was $625,000 per vendor; combined $1.25 million.

This phase is best understood as the seed round. The IRS spent a relatively small sum, with milestone-based payouts, to validate that the surveillance vendors could deliver against named privacy technologies. The contract structure transferred development risk to the vendor and prepared the agency for a much larger institutional commitment.

## Phase 3: The Consolidation (2021)

In 2021, Mastercard acquired CipherTrace. The acquisition is structurally important: a federally-funded blockchain surveillance capability was absorbed into a global payment network. Whatever capability CipherTrace had developed under its DHS contract — and whatever ongoing development it was conducting — became an internal Mastercard asset rather than a standalone federal vendor offering.

The acquisition narrowed the federal vendor pool. CipherTrace effectively exited the standalone federal-contractor market, leaving Chainalysis as the dominant incumbent and clearing the runway for newer entrants like TRM Labs to position themselves as the second source.

## Phase 4: The Institutional Commitment (2023)

In 2023, IRS-CI converted its relationship with Chainalysis from project-based R&D into a multi-year institutional license. The contract is documented on [USAspending.gov](https://www.usaspending.gov) as Award ID **205AE923C00010**, awardee Chainalysis Inc., total contract value **$21,515,583.20**, description: "chainalysis web subscription." Number of bidders: **one**.

The terms are reportedly extensive: hundreds of annual user licenses, API access, training, educational materials, and access to industry conferences. A separate $11.8 million IRS-CI Cyber Crimes Unit contract with Chainalysis covers casework support and training.

**Structural significance:** the IRS in 2023 was no longer buying a tool. It was buying a relationship. Chainalysis is now embedded in IRS-CI workflows the way Palantir is embedded at ICE — to the point that a federal agency credibly cannot perform its own crypto-tracing work without the vendor's software.

## Phase 5: Sole-Source as the New Default (2025)

In June 2025, U.S. Immigration and Customs Enforcement posted two simultaneous notices of intent on SAM.gov to procure additional blockchain analytics technology. The first identified Chainalysis Government Solutions as the sole vendor capable of providing forensic software and support services. The second identified TRM Labs as the sole vendor capable of providing comparable capability for the Homeland Security Investigations Cyber Crimes Center.

Sole-source acquisitions are legally available to federal agencies only when no other vendor is reasonably able to provide the capability. By certifying that Chainalysis and TRM Labs are each sole-source vendors, ICE made a formal administrative finding that the federal blockchain surveillance market has consolidated to the point of effective duopoly.

**This is the procurement equivalent of a confession.** The federal government is now telling itself, in writing, that the private market for blockchain forensics has only two providers worth contracting with for HSI-grade work.

## Vendor Profiles

## Chainalysis Inc.

The dominant federal vendor. Active contracts with at least ten federal entities including FBI, IRS, DEA, ICE, State Department, SEC, and the Department of the Air Force. Federal spending on Chainalysis grew from approximately $5 million in 2019 to a 2023 IRS contract alone exceeding $21 million. Chainalysis Government Solutions exists as a dedicated federal sales unit. The company's relationship with the U.S. government is now structurally comparable to Palantir's — embedded, recurring, and politically defended.

## TRM Labs

Founded 2018; achieved unicorn status with a reported $1 billion valuation. Positioning emphasizes AI-driven cross-chain threat intelligence and real-time screening, with explicit national-security framing. Holds contracts across DHS, FBI, IRS, DEA, and State Department. The 2025 ICE sole-source designation formally elevated TRM to second-source status alongside Chainalysis.

## Integra FEC LLC

Texas-based forensic data analysis firm, founded 2012, historically focused on traditional-finance forensics for DOJ and SEC. Won one of the two 2020 IRS Monero/Lightning contracts. No public delivery of a working tracing product has been confirmed under that award. Integra appears to have remained on the periphery of the blockchain-surveillance market after the 2020 contract.

## CipherTrace (acquired by Mastercard, 2021)

Cumulative federal contracts of approximately $6 million prior to acquisition, most of it R&D-flavored. CipherTrace was the original DHS partner on Monero and Zcash tracing. Post-acquisition, its standalone federal presence diminished sharply, though its capabilities are presumed to live on inside Mastercard's compliance stack.

## Elliptic

UK-based. Dominant in private-sector compliance — banks, exchanges, regulators — with reported coverage of more than 99% of the cryptocurrency market by data volume. Federal footprint is conspicuously small: as of the most widely cited federal-contract review, Elliptic's IRS business consisted of a single $2,450 contract. Elliptic's federal posture appears to be a deliberate strategic choice rather than a competitive failure — the company has positioned itself as the compliance-side counterparty rather than the law-enforcement-side surveillance vendor.

## Strategic Analysis

## The Privatization of Surveillance R&D

Across all five phases, the consistent pattern is that capability development is funded by federal agencies but owned by private vendors. The taxpayer pays for tools targeting privacy technology; the resulting tools become commercial products sold globally. Chainalysis sells to banks, exchanges, and foreign governments using infrastructure substantially built with U.S. federal R&D dollars.

This is the same model that produced Palantir, Anduril, and the broader defense-tech industrial base. It is now operative in financial surveillance.

## The Probabilistic Floor

Across the public record, no vendor — not Chainalysis, not CipherTrace, not TRM Labs — has publicly claimed deterministic tracing of Monero. The capability that has been publicly demonstrated is probabilistic clustering and attribution, dependent on user error (address reuse, timing correlations, exchange deposits, KYC linkage at on- and off-ramps). This is a meaningful evidentiary point: probabilistic blockchain analysis is not equivalent to a confirmed cryptographic signature, and defendants in cases built on it have legitimate grounds to contest the weight of the evidence.

Lightning Network tracing is similarly constrained. Chainalysis announced Lightning support in December 2021, but the publicly described capability is built primarily on channel-funding analysis and node-graph inference, not on visibility into in-channel payments. Users who route through private channels and well-managed nodes retain meaningful privacy properties.

## Market Concentration as Policy Statement

The ICE 2025 sole-source filings are the most candid signal in the public record about where this market sits. The federal government is now formally certifying that the blockchain surveillance industry has consolidated to a duopoly. From an antitrust perspective this would normally trigger scrutiny; from a procurement perspective it triggers nothing, because the sole-source justification is a routine federal acquisition pathway.

The effect on the broader cryptocurrency ecosystem is real. Exchanges, banks, and DeFi protocols seeking regulatory legitimacy increasingly use Chainalysis and TRM Labs not as one option among many but as the default — because federal regulators use them, and because compliance failures are evaluated against the standard the regulators themselves use.

## Implications for Bitcoin and Privacy-Preserving Users

- **The federal surveillance posture is funded, contracted, operational, and growing.** It is not theoretical. Treating it as theoretical is a planning error.

- **Probabilistic attribution is the dominant attack model.** Privacy is preserved by denying the attacker the auxiliary data — KYC linkages, address reuse, timing correlations — that elevates a low-confidence probability into a court-grade attribution. Operational discipline matters more than cryptographic perfection.

- **Layer-2 and privacy-coin users should plan for vendor-grade adversaries.** The vendors are well-resourced, federally subsidized, and continuously developing. Anyone treating Monero or Lightning as opaque to a $10 million-per-year adversary is reasoning from an outdated model.

- **Compartmentalization remains the highest-leverage defensive practice.** Most successful real-world traces in published cases turn on user error at the boundaries — exchange deposits, custodial wallets, KYC bridges — rather than on cryptographic defeats. Identity-isolation discipline protects against exactly this attack surface.

## Conclusion

The 2020 IRS contract to Chainalysis and Integra FEC was not an isolated event. It was one milestone in a continuous, expanding, multi-agency federal program to procure private capability for defeating financial-privacy technology. The program began with the 2018 DHS pilot, scaled through the 2020 IRS R&D contracts, consolidated commercially with the 2021 Mastercard acquisition of CipherTrace, transitioned to institutional licensing with the 2023 $21.5 million IRS subscription, and arrived at formal duopoly recognition with the 2025 ICE sole-source filings.

Every contract referenced in this case study is verifiable on [USAspending.gov](https://www.usaspending.gov), SAM.gov, or contemporaneous federal procurement reporting. The receipts are public. The pattern is policy.

## Sources

- [USAspending.gov](https://www.usaspending.gov) — Award IDs 2032H820C00040, 2032H820C00041, 205AE923C00010.

- SAM.gov — Solicitation 2032H820Q00076; 2025 ICE sole-source notices for Chainalysis and TRM Labs.

- CoinDesk — "Inside Chainalysis' Multimillion-Dollar Relationship With the US Government" (February 2020).

- Decrypt — Coverage of DHS/CipherTrace Monero tracing contract (August 2020) and IRS/Chainalysis/Integra award (October 2020).

- FedScoop — "ICE wants more blockchain analytics tech" (June 2025).

- MeriTalk — "ICE Buying Blockchain Tools From TRM, Chainalysis" (June 2025).

- OrangeSlices AI — IRS Chainalysis web subscription contract award detail (Award 205AE923C00010).

- Monero Research Lab — Public response to leaked IRS-CI training video on XMR tracing techniques.
