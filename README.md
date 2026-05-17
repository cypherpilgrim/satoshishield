# ₿ SatoshiShield — Bitcoin Privacy DNS Blocklist

**Block blockchain analytics firms, surveillance platforms, and wallet telemetry at the DNS layer.**

SatoshiShield is a curated, community-maintained DNS blocklist that prevents organizations that surveil Bitcoin users from receiving your IP address. Compatible with Pi-hole, AdGuard Home, and any DNS-based ad blocker.

---

## Why This Exists

When your Bitcoin wallet checks a balance, fetches fee estimates, or broadcasts a transaction, it makes DNS queries. Those queries reveal your IP address to whoever receives them. For many wallets, that receiver is infrastructure operated by companies whose business is correlating your IP address with your Bitcoin activity.

Chainalysis, Elliptic, TRM Labs, Arkham Intelligence, and others log your IP address against every address you query, every transaction you look up, and every price check you make. They sell this intelligence to exchanges, financial institutions, and law enforcement.

**SatoshiShield drops those DNS queries before they leave your network.**

No connection is established. No data is transmitted. The surveillance firm never sees your IP.

> SatoshiShield addresses the DNS layer — the earliest point at which Bitcoin surveillance can be interrupted. It complements your node and wallet privacy practices. It does not replace them.

---

## Two Tiers — Start with Tier 1

SatoshiShield uses a two-tier system to distinguish high-confidence entries from entries that need further community verification.

| Tier | Description | Use When |
|---|---|---|
| **Tier 1** | High confidence. Organizations whose primary business is Bitcoin surveillance. Well documented. Low false positive risk. | Start here. Recommended for all users. |
| **Tier 2** | Needs verification. Dual-use domains or organizations where surveillance harm needs individual confirmation before blocking. | Advanced users. Review domains.csv before enabling. |

---

## Quick Install

### Pi-hole (v5 and v6) — Tier 1 (Recommended)

1. Go to **Settings > Blocklists > Add**
2. Add this URL:

```
https://raw.githubusercontent.com/sawdustpilgrim/satoshishield/main/blocklist.txt
```

3. Run gravity update:

```bash
pihole -g
```

### Pi-hole — Tier 2 (Needs Verification)

```
https://raw.githubusercontent.com/sawdustpilgrim/satoshishield/main/blocklist-tier2.txt
```

### Pi-hole — All Tiers Combined

```
https://raw.githubusercontent.com/sawdustpilgrim/satoshishield/main/blocklist-all.txt
```

### AdGuard Home — Tier 1

1. Go to **Filters > DNS Blocklists > Add blocklist > Add a custom list**
2. Add:

```
https://raw.githubusercontent.com/sawdustpilgrim/satoshishield/main/satoshishield.abp
```

### Hosts File (manual)

Download [hosts.txt](hosts.txt) for Tier 1 or [hosts-tier2.txt](hosts-tier2.txt) for Tier 2.

---

## What Gets Blocked (Tier 1)

| Organization | Domain | Category | Why |
|---|---|---|---|
| Chainalysis | *.chainalysis.com | Blockchain Analytics | Primary surveillance firm. Sells IP-address correlation intelligence to law enforcement and exchanges. |
| Chainalysis | *.transpose.io | Blockchain Analytics | Chainalysis subsidiary — on-chain data API. |
| Elliptic | *.elliptic.co | Blockchain Analytics | Blockchain analytics and compliance. Address screening APIs reveal queried addresses. |
| TRM Labs | *.trmlabs.com | Blockchain Analytics | AI-driven blockchain intelligence. BLOCKINT API correlates queries with IP addresses. |
| CipherTrace | *.ciphertrace.com | Blockchain Analytics | Mastercard acquisition. Government and financial institution clients. |
| Crystal Blockchain | *.crystalblockchain.com, *.bitrank.com | Blockchain Analytics | Transaction monitoring and risk scoring. |
| Scorechain | *.scorechain.com | KYC/AML Compliance | Flags CoinJoin transactions as high risk. |
| Merkle Science | *.merkle.science | Blockchain Analytics | Predictive risk platform logs address queries against IP. |
| Arkham Intelligence | *.arkm.com, intel.arkm.com | Deanonymization | **CRITICAL** — publicly markets real-world identity linking. |
| MetaSleuth | *.metasleuth.io | Deanonymization | Crypto tracking and investigation platform. |
| Breadcrumbs | *.breadcrumbs.app | Blockchain Analytics | Free analytics tool — IP logged against every address query. |

**Full domain list with rationale:** [domains.csv](domains.csv) (Tier 1) | [domains-tier2.csv](domains-tier2.csv) (Tier 2)

---

## What Does NOT Get Blocked

SatoshiShield is precise. It does not block:

- Bitcoin network peers or mempool propagation
- Privacy-respecting blockchain explorers (mempool.space, blockstream.info)
- Exchange websites or trading platforms
- Bitcoin wallet software download domains
- Lightning Network nodes or routing infrastructure
- Self-hosted node software update domains

Every domain inclusion is documented with the specific privacy harm.

---

## Does This Work If I Run My Own Node?

Yes — and it adds complementary protection your node does not cover.

Your node protects the blockchain data layer: your wallet connects to your node and nobody sees your addresses. SatoshiShield protects the DNS layer: other applications on your network (price trackers, mobile wallets, browser extensions) can still contact surveillance infrastructure without it.

**The recommended full stack:**

| Layer | Tool | What It Protects |
|---|---|---|
| DNS layer | SatoshiShield + Pi-hole | Blocks surveillance domains before connections are established |
| Blockchain data | Your own Bitcoin node | Prevents wallet queries from leaking to third parties |
| Index layer | Fulcrum or Electrs | Fast address indexing without exposing your xpub |
| Network layer | Tor or WireGuard | Masks your IP at the transport layer |
| On-chain layer | Coin control, CoinJoin | Reduces on-chain linkability |

---

## Files in This Repository

| File | Tier | Format | Use With |
|---|---|---|---|
| [blocklist.txt](blocklist.txt) | 1 | Domain-only | Pi-hole v5+, Pi-hole v6, AdGuard Home |
| [hosts.txt](hosts.txt) | 1 | Hosts file | Pi-hole v4, Unix/Windows hosts file |
| [satoshishield.abp](satoshishield.abp) | 1 | ABP syntax | AdGuard (browser), uBlock Origin |
| [blocklist-tier2.txt](blocklist-tier2.txt) | 2 | Domain-only | Pi-hole — verify entries before use |
| [hosts-tier2.txt](hosts-tier2.txt) | 2 | Hosts file | Hosts file — verify entries before use |
| [satoshishield-tier2.abp](satoshishield-tier2.abp) | 2 | ABP syntax | AdGuard — verify entries before use |
| [blocklist-all.txt](blocklist-all.txt) | 1+2 | Domain-only | All tiers combined |
| [domains.csv](domains.csv) | 1 | CSV | Source data — Tier 1 entries with rationale |
| [domains-tier2.csv](domains-tier2.csv) | 2 | CSV | Source data — Tier 2 entries needing verification |

---

## Known Limitations

- **Hardcoded IP addresses** — DNS blocking cannot intercept connections using hardcoded IPs. A companion firewall blocklist (SatoshiShield-Firewall) is planned.
- **Domain rotation** — Surveillance firms can change domain names. Monthly releases address this. Wildcard blocking reduces the impact.
- **Tier 2 entries** — domains in Tier 2 need further community verification before being promoted to Tier 1. Review before enabling.

See the [White Paper](docs/SatoshiShield_WhitePaper_v1_0.docx) for a full adversarial analysis.

---

## Contributing

SatoshiShield grows through community research. If you discover a surveillance domain not yet in the list, or can verify a Tier 2 domain and promote it to Tier 1:

1. Verify it using the steps in [CONTRIBUTING.md](CONTRIBUTING.md)
2. Confirm blocking it does not break wallet functionality
3. Document your findings and open a pull request

**Full research methodology:** [CONTRIBUTING.md](CONTRIBUTING.md)
**Quarterly research protocol:** [Contributor Guide](docs/SatoshiShield_Contributor_Guide_v1_0.docx)

---

## License

MIT License — see [LICENSE](LICENSE)

---

## Project Identity

SatoshiShield is maintained pseudonymously. No real-world identity is attached to this project.

> Privacy is not a crime. Blocking surveillance infrastructure is not concealment — it is self-defense.

---

*Not affiliated with Bitcoin Core, the Bitcoin Foundation, or any wallet software project.*
