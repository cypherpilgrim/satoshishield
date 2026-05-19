# Changelog

All notable changes to SatoshiShield are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project loosely follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html), with the convention that the major version reflects breaking changes to the blocklist schema, the minor version reflects new domains or features, and the patch version reflects documentation or non-functional fixes.

---

## [1.2.0] — 2026-05-19

### Added

- **Optional monitor script** (`monitor/satoshishield_monitor.py`) that runs monthly on a Proxmox host, queries the Pi-hole FTL database for surveillance-domain hits, and emails a report. All SMTP configuration reads from a gitignored `.env` file; no credentials are hardcoded.
- **Monitor Report Reading Guide** (`monitor/SatoshiShield_Monitor_Report_Reading_Guide_v1_0.docx`) explaining how to read and act on the monthly reports.
- **Why Bitcoin Privacy Matters** (`docs/Why_Bitcoin_Privacy_Matters_v1_0.docx`) — short public-facing guide explaining the Bitcoin surveillance industry and what it means for ordinary users.
- **Why Bitcoin Privacy Matters: Deep Dive Edition** (`docs/Why_Bitcoin_Privacy_Matters_Deep_Dive_v1_0.docx`) — long-form companion covering the same material in significantly more depth.
- **Tier 2 file formats**: `hosts-tier2.txt` (hosts-file format) and `satoshishield-tier2.abp` (Adblock Plus syntax) to match the multi-format availability of the Tier 1 list.
- **Security policy** (`SECURITY.md`) covering what counts as a security issue and how to report it.

### Changed

- **README rewritten** to address several documentation gaps: added an install section for the Pi-hole regex deny rules (the step that makes wildcards work), added a "Verify It Is Working" section with test commands, added an "Optional Monitoring Tool" section, expanded the hosts file install with OS-specific paths and DoH warnings, added a comprehensive documentation table, and fixed broken references to files that did not previously exist.
- **CONTRIBUTING.md schema fixed.** The documented CSV format now matches the actual `domains.csv` schema (eight columns including `tier`). A new "Which Tier?" section explains when to submit as Tier 1 versus Tier 2.

### Removed

- Tracked `.DS_Store` files removed from the repository. The `.gitignore` already prevents them from being recommitted.

---

## [1.1.0] — 2026-05-19

### Changed

- **Glassnode promoted from Tier 2 to Tier 1.** Community verification confirmed the surveillance harm pattern. The domain is now blocked by the default Tier 1 list.
- **Nansen promoted from Tier 2 to Tier 1.** Same verification basis as Glassnode.

### Added

- `.env` files added to `.gitignore` to prevent accidental commit of monitor script credentials.

---

## [1.0.0] — 2026-05-18

Initial public release.

### Added

- **Tier 1 blocklist** covering 12 confirmed surveillance firms (before the v1.1 promotions): Chainalysis, Transpose, Elliptic, TRM Labs, CipherTrace, Crystal Blockchain, BitRank, Scorechain, Merkle Science, Arkham Intelligence, MetaSleuth, and Breadcrumbs.
- **Tier 2 blocklist** covering 5 organizations needing verification: CryptoQuant, Bitquery, Mixpanel, Amplitude, and Segment.
- **Multiple blocklist formats** for Tier 1: `blocklist.txt` (Pi-hole v5+, AdGuard Home), `hosts.txt` (Pi-hole v4, Unix/Windows hosts file), and `satoshishield.abp` (Adblock Plus syntax).
- **Tier 2 blocklist** in `blocklist-tier2.txt` format.
- **Combined `blocklist-all.txt`** for users who want all tiers in one list.
- **Pi-hole regex deny rules** (`regex.txt`) providing true wildcard coverage that the URL-fetched blocklists cannot deliver alone.
- **Evidence CSVs** (`domains.csv` and `domains-tier2.csv`) documenting the organization, category, harm, and source for every domain in each tier.
- **White Paper** (`docs/SatoshiShield_WhitePaper_v1_0.docx`) covering the project rationale, architecture, methodology, and adversarial analysis.
- **Contributor Guide** (`docs/SatoshiShield_Contributor_Guide_v1_0.docx`) covering the full research methodology, tools reference, and quarterly research protocol.
- **Monitor Deployment Guide** (`docs/SatoshiShield_Monitor_Deployment_v1_0.docx`) covering installation and configuration of the optional monthly monitoring tool.
- **Quarterly Checklist** (`docs/SatoshiShield_Quarterly_Checklist_v1_0.docx`) structured research protocol for contribution cycles.
- **CONTRIBUTING.md** quick-reference guide for submitting domains.
- **MIT License.**

---

## Versioning Convention

- **Major version** (X.0.0): breaking changes to the CSV schema or blocklist file formats.
- **Minor version** (1.X.0): new domains added, existing domains promoted between tiers, new file formats, new tooling.
- **Patch version** (1.0.X): documentation fixes, typo corrections, non-functional improvements.

The blocklist files (`blocklist.txt`, `hosts.txt`, etc.) carry their own version headers that match the current repository version.
