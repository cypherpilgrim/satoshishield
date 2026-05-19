# Changelog

All notable changes to SatoshiShield are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project loosely follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html), with the convention that the major version reflects breaking changes to the blocklist schema, the minor version reflects new domains or features, and the patch version reflects documentation or non-functional fixes.

---

## [1.4.4] — 2026-05-19

### Fixed

- **Regression from v1.4.3: White Paper subsections 8.1 through 8.8 were not renumbered.** The v1.4.3 patch renumbered the H1 heading "8. Adversarial Considerations" to "9. Adversarial Considerations" but missed the eight H2 subsections beneath it. Readers saw Section 9 with subsections labelled 8.1, 8.2, etc. All eight subsections now correctly read 9.1 through 9.8.
- **README TOC missing Project Identity.** The Project Identity section at the end of the README was not listed in the Table of Contents. Now added.

### Notes

- No changes to blocklist content, CSV evidence, or monitor script. All fixes are documentation.
- This release exists because a regression was introduced in v1.4.3. The audit pipeline caught it before it sat unfixed in the public repo for long.

---

## [1.4.3] — 2026-05-19

### Fixed

- **White Paper duplicate Section 8 numbering.** The white paper had two H1 headings numbered "8": Section 8 (Frequently Asked Questions) and Section 8 (Adversarial Considerations). This was a numbering bug from the original v1.0 release. Adversarial Considerations is now Section 9, About is Section 10, and License is Section 11. No internal cross-references to "Section 8" existed, so no other content needed updating.
- **Stale Document Version tables in three legacy docx files.** The White Paper, Contributor Guide, and Quarterly Checklist all had Document Version tables that listed only v1.0, despite the cover pages saying v1.4. All three now have v1.4 rows documenting what changed in v1.4 (GitHub handle migration, cover/header/footer version updates, section renumbering where applicable). The Monitor Deployment Guide already had a v1.4 row because it was rebuilt from scratch in v1.4.
- **Quarterly Checklist cover page missing version stamp.** The other three legacy docx files have versions on their covers; the Quarterly Checklist did not. The subtitle line now reads "Run every 90 days  |  Estimated time: 2–4 hours  |  v1.4  |  May 2026".
- **CHANGELOG cross-reference to White Paper Section 9.** The v1.4 entry referenced "Section 9" for the About section, which becomes Section 10 after the renumbering above. The reference now just says "the About section" to avoid section-number fragility.

### Notes

- No changes to blocklist content, CSV evidence, or monitor script. All fixes are docx-internal and one CHANGELOG line.
- Round 6 audit also flagged the White Paper roadmap (Section 7) as historically inaccurate, since the project shipped v1.1 through v1.4.2 in days rather than across the projected months. The roadmap content is still useful as a description of future goals, so it's left in place. A future v2.0 white paper revision can refresh the roadmap entirely.

---

## [1.4.2] — 2026-05-19

### Fixed

- **OPSEC: Sanitized CHANGELOG entries that re-leaked the information being removed.** The v1.4 and v1.4.1 entries previously quoted the exact name and geographic identifier that were being removed from the docx files, undoing the OPSEC fixes. The descriptions have been rewritten to explain what was sanitized without quoting the values.
- **Firm count corrected.** The README, Privacy Short, and Privacy Deep Dive each described "14 firms" in the Tier 1 list when the actual count is 12 distinct organizations across 14 root domain patterns. Chainalysis owns Transpose; Crystal Blockchain owns BitRank. The wording now reads "12 firms across 14 root domains" or "14 root domain patterns" depending on context.
- **README "What Gets Blocked" table row grouping made consistent.** Chainalysis was previously split into two rows (one for `chainalysis.com`, one for `transpose.io`) while Crystal Blockchain was already grouped into a single row with both its domains. The Chainalysis row now matches the Crystal Blockchain pattern, giving the table exactly 12 rows that each represent one organization.

### Notes

- No changes to blocklist content, CSV evidence, or monitor script. All fixes are documentation and metadata.
- An audit also flagged the TOC anchor `#two-tiers--start-with-tier-1` (double dash) as potentially broken on GitHub, but the original anchor was confirmed correct after testing GitHub's actual slugger algorithm against the heading. No change needed.

---

## [1.4.1] — 2026-05-19

### Fixed

- **OPSEC: Removed maintainer's real name from docx metadata.** One docx file had the maintainer's real name in its `last_modified_by` core property field, set automatically when the file was opened in a desktop word processor during review. The file has been regenerated with clean metadata (`Un-named` for both `author` and `last_modified_by`), matching all other docx files in the repository.
- **Broken links in CONTRIBUTING.md.** Two references to `SatoshiShield_Contributor_Guide_v1_0.docx` updated to `_v1_4` since the file was renamed in commit `83930dd`.
- **Broken links in CHANGELOG.md v1.0 entry.** Four file references (White Paper, Contributor Guide, Monitor Deployment Guide, Quarterly Checklist) updated from `_v1_0` to `_v1_4`. The descriptive prose still mentions what was added at v1.0; the links now point to the current filenames.

### Added

- **README "Files in This Repository" table** now lists `hosts-tier2.txt` and `satoshishield-tier2.abp` (both added in v1.2 but missing from the table).
- **README "Documentation" table** now lists `CHANGELOG.md` and `SECURITY.md`.
- **README Quick Install section** now includes Tier 2 install URLs for AdGuard Home (`satoshishield-tier2.abp`) and a Tier 2 mention in the hosts file section (`hosts-tier2.txt`). Previously these formats had no install instructions in the README.
- **`.env.example`** template file showing the required environment keys for the monitor script. Helps new operators understand the configuration without reading the deployment guide first.

### Changed

- **SECURITY.md URLs** converted from backtick-wrapped plain text to proper Markdown links. Users clicking the links now navigate to GitHub directly instead of needing to copy-paste a URL with stray backticks.

### Notes

- No changes to blocklist content, CSV evidence, or monitor script behavior. All fixes are documentation and metadata.

---

## [1.4.0] — 2026-05-19

### Fixed

- **OPSEC: Monitor Deployment Guide sanitized.** The original `SatoshiShield_Monitor_Deployment_v1_0.docx` contained the maintainer's real email addresses, internal IP addresses, SSH usernames, and container IDs. These have been replaced with placeholders (`<proxmox-host>`, `<proxmox-user>`, `<report-email>`, `<smtp-user>`, etc.) consistent with the Monitor Report Reading Guide style. The new file is `SatoshiShield_Monitor_Deployment_v1_4.docx`.
- **GitHub handle updated in all legacy docx files.** The White Paper, Contributor Guide, and Monitor Deployment Guide all referenced the old `sawdustpilgrim` GitHub handle, which no longer exists. All references now correctly point to `github.com/cypherpilgrim/satoshishield`. Affected files now ship as v1.4.
- **LICENSE copyright notice updated.** Changed `Copyright (c) 2026 sawdustpilgrim` to `Copyright (c) 2026 cypherpilgrim` to match the active GitHub identity.
- **White Paper Table 5 updated.** Glassnode and Nansen entries now note their promotion to Tier 1 in v1.1, rather than implying they are still Tier 2 as in the original v1.0 white paper.
- **White Paper Section 4.4 clarified.** The phrase "Version 1.0 of SatoshiShield includes the following domain categories" has been rewritten to make clear that the listing describes the initial release state, with a pointer to the CHANGELOG for current state.
- **White Paper About section.** A geographic reference in the About section has been genericized to remove potentially identifying information about the maintainer's region.

### Changed

- **Document versioning.** The four legacy docx files are now versioned at v1.4 in their filenames, cover pages, and headers to reflect the current state of the project rather than the long-stale "v1_0" stamp.

### Notes

- This release does not change the blocklist files, the CSV evidence, or the monitor script. All five fixes are documentation and metadata changes.

---

## [1.3.0] — 2026-05-19

### Fixed

- **`blocklist-tier2.txt` no longer lists Glassnode and Nansen.** These were promoted to Tier 1 in v1.1, but the regenerated Tier 2 blocklist file was missed at the time. The four orphan entries (`*.glassnode.com`, `glassnode.com`, `*.nansen.ai`, `nansen.ai`) have been removed. Users installing both Tier 1 and Tier 2 will no longer see duplicate entries.
- **`blocklist-all.txt` rebuilt** from the corrected Tier 1 and Tier 2 sources, with clear section headers separating the tiers and consistent alphabetical ordering within each category.
- **Version and date headers updated across all blocklist files** to reflect the current release. All format files (`blocklist.txt`, `blocklist-tier2.txt`, `blocklist-all.txt`, `hosts.txt`, `hosts-tier2.txt`, `satoshishield.abp`, `satoshishield-tier2.abp`, `regex.txt`) now show `Version: 1.3` and `Updated: 2026-05-19`.

### Changed

- **Monitor script extended to detect Tier 2 domains.** The `SURVEILLANCE_PATTERNS` dictionary in `monitor/satoshishield_monitor.py` now includes CryptoQuant, Bitquery, Mixpanel, Amplitude, and Segment. These are not in `ALREADY_BLOCKED`, so any DNS query matching one of them surfaces in the monthly report as a candidate for community research, which is the documented intent.

---

## [1.2.0] — 2026-05-19

### Added

- **Optional monitor script** (`monitor/satoshishield_monitor.py`) that runs monthly on a Proxmox host, queries the Pi-hole FTL database for surveillance-domain hits, and emails a report. All SMTP configuration reads from a gitignored `.env` file; no credentials are hardcoded.
- **Monitor Report Reading Guide** (`monitor/SatoshiShield_Monitor_Report_Reading_Guide_v1_0.docx`) explaining how to read and act on the monthly reports.
- **Why Bitcoin Privacy Matters** (`docs/Why_Bitcoin_Privacy_Matters_v1_0.docx`), a short public-facing guide explaining the Bitcoin surveillance industry and what it means for ordinary users.
- **Why Bitcoin Privacy Matters: Deep Dive Edition** (`docs/Why_Bitcoin_Privacy_Matters_Deep_Dive_v1_0.docx`), a long-form companion covering the same material in significantly more depth.
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

### Known issue (resolved in v1.3)

- The promotion of Glassnode and Nansen updated `domains.csv` and `domains-tier2.csv` but did not regenerate the `blocklist-tier2.txt` file. The four orphan entries remained in the Tier 2 file until v1.3.

---

## [1.0.0] — 2026-05-17

Initial public release.

### Added

- **Tier 1 blocklist** covering 12 confirmed surveillance firms (before the v1.1 promotions): Chainalysis, Transpose, Elliptic, TRM Labs, CipherTrace, Crystal Blockchain, BitRank, Scorechain, Merkle Science, Arkham Intelligence, MetaSleuth, and Breadcrumbs.
- **Tier 2 blocklist** covering 7 organizations needing verification: CryptoQuant, Bitquery, Mixpanel, Amplitude, Segment, Glassnode, and Nansen. (Glassnode and Nansen promoted to Tier 1 in v1.1.)
- **Multiple blocklist formats** for Tier 1: `blocklist.txt` (Pi-hole v5+, AdGuard Home), `hosts.txt` (Pi-hole v4, Unix/Windows hosts file), and `satoshishield.abp` (Adblock Plus syntax).
- **Tier 2 blocklist** in `blocklist-tier2.txt` format.
- **Combined `blocklist-all.txt`** for users who want all tiers in one list.
- **Pi-hole regex deny rules** (`regex.txt`) providing true wildcard coverage that the URL-fetched blocklists cannot deliver alone.
- **Evidence CSVs** (`domains.csv` and `domains-tier2.csv`) documenting the organization, category, harm, and source for every domain in each tier.
- **White Paper** (`docs/SatoshiShield_WhitePaper_v1_4.docx`) covering the project rationale, architecture, methodology, and adversarial analysis.
- **Contributor Guide** (`docs/SatoshiShield_Contributor_Guide_v1_4.docx`) covering the full research methodology, tools reference, and quarterly research protocol.
- **Monitor Deployment Guide** (`docs/SatoshiShield_Monitor_Deployment_v1_4.docx`) covering installation and configuration of the optional monthly monitoring tool.
- **Quarterly Checklist** (`docs/SatoshiShield_Quarterly_Checklist_v1_4.docx`), a structured research protocol for contribution cycles.
- **CONTRIBUTING.md** quick-reference guide for submitting domains.
- **MIT License.**

---

## Versioning Convention

- **Major version** (X.0.0): breaking changes to the CSV schema or blocklist file formats.
- **Minor version** (1.X.0): new domains added, existing domains promoted between tiers, new file formats, new tooling.
- **Patch version** (1.0.X): documentation fixes, typo corrections, non-functional improvements.

The blocklist files (`blocklist.txt`, `hosts.txt`, etc.) carry their own version headers that match the current repository version.
