# ₿ SatoshiShield — Bitcoin Privacy DNS Blocklist

**Block blockchain analytics firms, surveillance platforms, and wallet telemetry at the DNS layer.**

SatoshiShield is a curated, community-maintained DNS blocklist that prevents organizations that surveil Bitcoin users from receiving your IP address. Compatible with Pi-hole, AdGuard Home, and any DNS-based ad blocker.

---

## Table of Contents

- [Why This Exists](#why-this-exists)
- [Two Tiers — Start with Tier 1](#two-tiers--start-with-tier-1)
- [Quick Install](#quick-install)
- [Pi-hole Regex Deny Rules (Important)](#pi-hole-regex-deny-rules-important)
- [Verify It Is Working](#verify-it-is-working)
- [What Gets Blocked (Tier 1)](#what-gets-blocked-tier-1)
- [What Does Not Get Blocked](#what-does-not-get-blocked)
- [Does This Work If You Run Your Own Node?](#does-this-work-if-you-run-your-own-node)
- [Optional Monitoring Tool](#optional-monitoring-tool)
- [Files in This Repository](#files-in-this-repository)
- [Documentation](#documentation)
- [Known Limitations](#known-limitations)
- [Contributing](#contributing)
- [License](#license)

---

## Why This Exists

When your Bitcoin wallet checks a balance, fetches fee estimates, or broadcasts a transaction, it makes DNS queries. Those queries reveal your IP address to whoever receives them. For many wallets, that receiver is infrastructure operated by companies whose business is correlating your IP address with your Bitcoin activity.

Chainalysis, Elliptic, TRM Labs, Arkham Intelligence, and others log your IP address against every address you query, every transaction you look up, and every price check you make. They sell this intelligence to exchanges, financial institutions, and law enforcement.

**SatoshiShield drops those DNS queries before they leave your network.**

No connection is established. No data is transmitted. The surveillance firm never sees your IP.

> SatoshiShield addresses the DNS layer, the earliest point at which Bitcoin surveillance can be interrupted. It complements your node and wallet privacy practices. It does not replace them.

For a full explanation of why Bitcoin privacy matters and what surveillance firms do with the data they collect, see [Why Bitcoin Privacy Matters](docs/Why_Bitcoin_Privacy_Matters_v1_0.docx) (short guide) or the [Deep Dive Edition](docs/Why_Bitcoin_Privacy_Matters_Deep_Dive_v1_0.docx) for more detail.

---

## Two Tiers — Start with Tier 1

SatoshiShield uses a two-tier system to distinguish high-confidence entries from entries that need further community verification.

| Tier | Description | Use When |
|---|---|---|
| **Tier 1** | High confidence. Organizations whose primary business is Bitcoin surveillance. Well documented. Low false positive risk. | Start here. Recommended for all users. |
| **Tier 2** | Needs verification. Dual-use domains or organizations where surveillance harm needs individual confirmation before blocking. | Advanced users. Review domains-tier2.csv before enabling. |

Promotion from Tier 2 to Tier 1 happens when community research confirms that a domain meets the inclusion criteria documented in [CONTRIBUTING.md](CONTRIBUTING.md). New submissions always start in Tier 1 with full evidence, or in Tier 2 if the harm pattern is suspected but not yet confirmed.

---

## Quick Install

### Pi-hole (v5 and v6) — Tier 1 (Recommended)

1. Go to **Settings > Blocklists > Add**
2. Add this URL:

```
https://raw.githubusercontent.com/cypherpilgrim/satoshishield/main/blocklist.txt
```

3. Run gravity update:

```bash
pihole -g
```

**Important:** After completing the steps above, also apply the [regex deny rules](#pi-hole-regex-deny-rules-important). Without them, Pi-hole will silently ignore the wildcard entries (`*.foo.com`) in the blocklist, and many subdomains will not be blocked.

### Pi-hole — Tier 2 (Needs Verification)

```
https://raw.githubusercontent.com/cypherpilgrim/satoshishield/main/blocklist-tier2.txt
```

Review [domains-tier2.csv](domains-tier2.csv) before enabling.

### Pi-hole — All Tiers Combined

```
https://raw.githubusercontent.com/cypherpilgrim/satoshishield/main/blocklist-all.txt
```

### AdGuard Home — Tier 1

1. Go to **Filters > DNS Blocklists > Add blocklist > Add a custom list**
2. Add:

```
https://raw.githubusercontent.com/cypherpilgrim/satoshishield/main/satoshishield.abp
```

### Hosts File (manual, no Pi-hole or AdGuard required)

For users without a DNS-level blocker, the [hosts.txt](hosts.txt) file can be appended to the system hosts file.

| OS | Hosts file location | Requirements |
|---|---|---|
| Linux | `/etc/hosts` | root / sudo |
| macOS | `/etc/hosts` | root / sudo |
| Windows | `C:\Windows\System32\drivers\etc\hosts` | Administrator |

After editing, flush the DNS cache:

| OS | Command |
|---|---|
| Linux | `sudo systemctl restart systemd-resolved` (varies by distro) |
| macOS | `sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder` |
| Windows | `ipconfig /flushdns` (in elevated cmd) |

**Hosts file limitations:** Browsers that use DNS-over-HTTPS (DoH) bypass the system hosts file entirely. Pi-hole or AdGuard Home is strongly recommended over the hosts file approach.

---

## Pi-hole Regex Deny Rules (Important)

Pi-hole's URL-fetched blocklists silently ignore wildcard entries like `*.chainalysis.com`. To block all subdomains of a surveillance firm (not just the root domain), Pi-hole regex deny rules must be applied separately. The rules in [regex.txt](regex.txt) provide true wildcard coverage for all 14 Tier 1 firms.

### Option A — Pi-hole Admin UI (Recommended for most users)

1. Open the Pi-hole admin interface
2. Go to **Domains > Add domain**
3. Select **Regex Filter** as the type
4. Choose **Deny**
5. Paste each line from [regex.txt](regex.txt) one at a time and click **Add**

Repeat for all 14 patterns. No gravity update is required after adding regex rules.

### Option B — SQL (Advanced)

For users comfortable with sqlite3, the regex rules can be applied directly to `gravity.db`. SSH into the Pi-hole host and run:

```bash
sqlite3 /etc/pihole/gravity.db <<'SQL'
INSERT OR IGNORE INTO domainlist (type, domain, enabled, comment) VALUES
  (3, '(\.|^)chainalysis\.com$',     1, 'SatoshiShield regex'),
  (3, '(\.|^)transpose\.io$',        1, 'SatoshiShield regex'),
  (3, '(\.|^)elliptic\.co$',         1, 'SatoshiShield regex'),
  (3, '(\.|^)trmlabs\.com$',         1, 'SatoshiShield regex'),
  (3, '(\.|^)ciphertrace\.com$',     1, 'SatoshiShield regex'),
  (3, '(\.|^)arkm\.com$',            1, 'SatoshiShield regex'),
  (3, '(\.|^)crystalblockchain\.com$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)bitrank\.com$',         1, 'SatoshiShield regex'),
  (3, '(\.|^)scorechain\.com$',      1, 'SatoshiShield regex'),
  (3, '(\.|^)merkle\.science$',      1, 'SatoshiShield regex'),
  (3, '(\.|^)metasleuth\.io$',       1, 'SatoshiShield regex'),
  (3, '(\.|^)breadcrumbs\.app$',     1, 'SatoshiShield regex'),
  (3, '(\.|^)nansen\.ai$',           1, 'SatoshiShield regex'),
  (3, '(\.|^)glassnode\.com$',       1, 'SatoshiShield regex');
SQL
```

Then restart Pi-hole's DNS resolver:

```bash
pihole restartdns
```

### AdGuard Home users

AdGuard Home processes the `*.foo.com` syntax in [satoshishield.abp](satoshishield.abp) natively. No separate regex setup is required.

---

## Verify It Is Working

After installation, confirm the blocklist is active by running these commands from any device on the network using Pi-hole (or AdGuard Home) for DNS.

### Test a Tier 1 domain (should be blocked)

```bash
dig api.chainalysis.com +short
```

**Expected:** `0.0.0.0` (or no result, depending on Pi-hole's blocking mode). If the command returns a real IP address, the blocklist is not active on this device.

### Test a few more domains

```bash
dig intel.arkm.com +short
dig api.trmlabs.com +short
dig api.elliptic.co +short
```

All should return `0.0.0.0` or no result.

### Test that legitimate Bitcoin infrastructure is not blocked

```bash
dig mempool.space +short
dig blockstream.info +short
```

These should return real IP addresses. If they do not, something other than SatoshiShield is interfering with DNS.

### Pi-hole admin UI

In the Pi-hole admin UI, go to **Tools > Query Log** and filter by one of the surveillance domains. Recent queries should appear with the action **Blocked (regex deny)** or **Blocked (gravity)**.

---

## What Gets Blocked (Tier 1)

| Organization | Domain | Category | Why |
|---|---|---|---|
| Chainalysis | *.chainalysis.com | Blockchain Analytics | Primary surveillance firm. Sells IP-address correlation intelligence to law enforcement and exchanges. |
| Chainalysis | *.transpose.io | Blockchain Analytics | Chainalysis subsidiary, on-chain data API. |
| Elliptic | *.elliptic.co | Blockchain Analytics | Blockchain analytics and compliance. Address screening APIs reveal queried addresses. |
| TRM Labs | *.trmlabs.com | Blockchain Analytics | AI-driven blockchain intelligence. BLOCKINT API correlates queries with IP addresses. |
| CipherTrace | *.ciphertrace.com | Blockchain Analytics | Mastercard acquisition. Government and financial institution clients. |
| Crystal Blockchain | *.crystalblockchain.com, *.bitrank.com | Blockchain Analytics | Transaction monitoring and risk scoring. |
| Scorechain | *.scorechain.com | KYC/AML Compliance | Flags CoinJoin transactions as high risk. |
| Merkle Science | *.merkle.science | Blockchain Analytics | Predictive risk platform logs address queries against IP. |
| Arkham Intelligence | *.arkm.com, intel.arkm.com | Deanonymization | **CRITICAL** — publicly markets real-world identity linking. |
| MetaSleuth | *.metasleuth.io | Deanonymization | Crypto tracking and investigation platform. |
| Breadcrumbs | *.breadcrumbs.app | Blockchain Analytics | Free analytics tool, IP logged against every address query. |
| Glassnode | *.glassnode.com | Blockchain Analytics | On-chain analytics. IP logged against address and metric queries. |
| Nansen | *.nansen.ai | Surveillance Analytics | Wallet labeling and identity profiling. |

**Full domain list with rationale:** [domains.csv](domains.csv) (Tier 1) | [domains-tier2.csv](domains-tier2.csv) (Tier 2)

---

## What Does Not Get Blocked

SatoshiShield is precise. It does not block:

- Bitcoin network peers or mempool propagation
- Privacy-respecting blockchain explorers (mempool.space, blockstream.info)
- Exchange websites or trading platforms
- Bitcoin wallet software download domains
- Lightning Network nodes or routing infrastructure
- Self-hosted node software update domains

Every domain inclusion is documented with the specific privacy harm.

---

## Does This Work If You Run Your Own Node?

Yes, and it adds complementary protection your node does not cover.

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

## Optional Monitoring Tool

The `monitor/` directory contains an optional Python script (`satoshishield_monitor.py`) that runs monthly on a Proxmox host, queries the Pi-hole FTL database for DNS queries matching known surveillance patterns, and emails a report.

The monitor distinguishes two cases:

- **New surveillance domains detected** — domains that matched a surveillance pattern but are not yet in the blocklist. These are candidates for community research and pull requests.
- **Known blocked domains still being queried** — domains that are already blocked but were still attempted by clients on the network. These indicate which devices and apps are calling home to surveillance infrastructure.

The monitor uses only Python's standard library and reads all SMTP credentials from a gitignored `.env` file. It does not transmit query data outside the user's network.

For deployment instructions, see the [Monitor Deployment Guide](docs/SatoshiShield_Monitor_Deployment_v1_0.docx). For instructions on reading the monthly reports, see the [Monitor Report Reading Guide](monitor/SatoshiShield_Monitor_Report_Reading_Guide_v1_0.docx).

---

## Files in This Repository

| File | Tier | Format | Use With |
|---|---|---|---|
| [blocklist.txt](blocklist.txt) | 1 | Domain-only | Pi-hole v5+, Pi-hole v6, AdGuard Home |
| [hosts.txt](hosts.txt) | 1 | Hosts file | Pi-hole v4, Unix/Windows hosts file |
| [satoshishield.abp](satoshishield.abp) | 1 | ABP syntax | AdGuard (browser), uBlock Origin |
| [regex.txt](regex.txt) | 1 | Pi-hole regex | Pi-hole wildcard coverage (see [install section](#pi-hole-regex-deny-rules-important)) |
| [blocklist-tier2.txt](blocklist-tier2.txt) | 2 | Domain-only | Pi-hole, verify entries before use |
| [blocklist-all.txt](blocklist-all.txt) | 1+2 | Domain-only | All tiers combined |
| [domains.csv](domains.csv) | 1 | CSV | Source data, Tier 1 entries with rationale |
| [domains-tier2.csv](domains-tier2.csv) | 2 | CSV | Source data, Tier 2 entries needing verification |
| [monitor/satoshishield_monitor.py](monitor/satoshishield_monitor.py) | — | Python | Optional monthly monitoring script |

---

## Documentation

Full documentation lives in the `docs/` directory:

| Document | For | What It Covers |
|---|---|---|
| [Why Bitcoin Privacy Matters](docs/Why_Bitcoin_Privacy_Matters_v1_0.docx) | All readers | Short guide explaining the Bitcoin surveillance industry and what it means for users |
| [Why Bitcoin Privacy Matters: Deep Dive](docs/Why_Bitcoin_Privacy_Matters_Deep_Dive_v1_0.docx) | Readers wanting more depth | Same topics, longer treatment with sources and case studies |
| [White Paper](docs/SatoshiShield_WhitePaper_v1_0.docx) | Technical readers | Full project rationale, architecture, methodology, and adversarial analysis |
| [Contributor Guide](docs/SatoshiShield_Contributor_Guide_v1_0.docx) | Contributors | Full research methodology, tools reference, and submission process |
| [Monitor Deployment Guide](docs/SatoshiShield_Monitor_Deployment_v1_0.docx) | Operators | How to install and configure the optional monitoring script |
| [Monitor Report Reading Guide](monitor/SatoshiShield_Monitor_Report_Reading_Guide_v1_0.docx) | Operators | How to read and interpret the monthly monitor reports |
| [Quarterly Checklist](docs/SatoshiShield_Quarterly_Checklist_v1_0.docx) | Contributors | Structured research protocol for quarterly contribution cycles |

---

## Known Limitations

- **Hardcoded IP addresses** — DNS blocking cannot intercept connections using hardcoded IPs. A companion firewall blocklist (SatoshiShield-Firewall) is planned.
- **Domain rotation** — Surveillance firms can change domain names. Monthly releases address this. Wildcard blocking via regex deny rules reduces the impact.
- **Browser DNS-over-HTTPS** — Browsers configured to use DNS-over-HTTPS (DoH) bypass the system resolver and therefore bypass Pi-hole and AdGuard Home. DoH should be disabled or configured to use Pi-hole as its upstream.
- **Tier 2 entries** — Domains in Tier 2 need further community verification before being promoted to Tier 1. Review before enabling.

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

> Privacy is not a crime. Blocking surveillance infrastructure is not concealment; it is self-defense.

---

*Not affiliated with Bitcoin Core, the Bitcoin Foundation, or any wallet software project.*
