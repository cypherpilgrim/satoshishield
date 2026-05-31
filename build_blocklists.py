#!/usr/bin/env python3
"""
SatoshiShield blocklist artifact builder.

Reads domains.csv (Tier 1) and domains-tier2.csv (Tier 2) and emits all seven
generated blocklist artifacts in the formats currently used by the repo:

  - blocklist.txt              (Tier 1, domain-only, wildcards preserved)
  - hosts.txt                  (Tier 1, hosts file format, apex only)
  - satoshishield.abp          (Tier 1, Adblock Plus syntax, apex only)
  - blocklist-tier2.txt        (Tier 2, domain-only, wildcards preserved)
  - hosts-tier2.txt            (Tier 2, hosts file format, apex only)
  - satoshishield-tier2.abp    (Tier 2, Adblock Plus syntax, apex only)
  - blocklist-all.txt          (Combined Tier 1 + Tier 2, domain-only)

Usage (from the repo root):
  python3 build_blocklists.py

The script does NOT modify domains.csv, domains-tier2.csv, regex.txt, or
CHANGELOG.md. regex.txt is maintained by hand; this script prints the
regex lines you need to add manually for any apex domains not already
present in regex.txt.
"""

import csv
import sys
from pathlib import Path
from collections import defaultdict

REPO_ROOT = Path(__file__).resolve().parent

# Bump these for each release
VERSION = "1.6.0"
DATE_ISO = "2026-05-31"
REPO_URL = "https://github.com/cypherpilgrim/satoshishield"

# Map domains.csv category → section header in blocklist files.
# Most categories map 1:1 verbatim; explicit overrides go here.
CATEGORY_TO_SECTION_HEADER = {
    "Wallet Telemetry": "Wallet Telemetry (dual-use, high false positive risk)",
}


def read_csv(path):
    """Read a domains CSV; return list of (domain, category) tuples."""
    if not path.exists():
        sys.exit(f"ERROR: {path} not found")
    rows = []
    with open(path, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        if not header or header[0] != "domain":
            sys.exit(f"ERROR: unexpected header in {path}: {header}")
        for row_num, row in enumerate(reader, start=2):
            if not row or not row[0].strip():
                continue
            domain = row[0].strip()
            category = row[2].strip() if len(row) > 2 else "Uncategorized"
            rows.append((domain, category))
    return rows


def group_by_category(rows):
    """Group entries by category and sort within each category.

    Sort order within a category:
      1. Wildcards first (entries starting with '*.')
      2. Apex/exact entries next
      3. Alphabetical within each sub-group
    """
    grouped = defaultdict(list)
    for domain, category in rows:
        grouped[category].append(domain)
    for category in grouped:
        grouped[category].sort(
            key=lambda d: (not d.startswith("*."), d.lower())
        )
    return dict(grouped)


def get_section_header(category):
    """Return the section header text for a given category."""
    return CATEGORY_TO_SECTION_HEADER.get(category, category)


def apex_only_set(domains):
    """Convert a list of domains (possibly including *.foo.com wildcards)
    into a set of apex/exact domains. Strips leading '*.' from wildcards.
    Used by hosts.txt and .abp formats which can't represent wildcards."""
    result = set()
    for d in domains:
        if d.startswith("*."):
            result.add(d[2:])
        else:
            result.add(d)
    return result


# ---------------------------------------------------------------------------
# Writers
# ---------------------------------------------------------------------------

def write_blocklist_txt(grouped, path, tier_label, install_filename, is_all_tiers=False):
    """Write Pi-hole / AdGuard Home domain-only blocklist."""
    lines = [
        "# SatoshiShield — Bitcoin Privacy DNS Blocklist",
        "# Domain-only format — compatible with Pi-hole v5+, Pi-hole v6, AdGuard Home",
        f"# {tier_label}",
        f"# {REPO_URL}",
        f"# Version: {VERSION} | Updated: {DATE_ISO}",
        "#",
        "# Installation (Pi-hole): Settings > Blocklists > Add",
        f"# https://raw.githubusercontent.com/cypherpilgrim/satoshishield/main/{install_filename}",
        "#",
    ]
    if "TIER 2" in tier_label:
        lines.extend([
            "# WARNING: Tier 2 entries are flagged NEEDS VERIFICATION. Review domains-tier2.csv",
            "# before enabling. Some entries (Mixpanel, Amplitude, Segment) are dual-use SDKs",
            "# that may impact non-Bitcoin applications.",
            "#",
        ])
    else:
        lines.extend([
            "# NOTE: Pi-hole's URL-fetched lists ignore *.foo.com wildcards.",
            "# For true wildcard coverage of all subdomains, also apply regex.txt",
            "# as Pi-hole regex deny rules. See README for instructions.",
            "#",
        ])
    lines.append("")

    for category in sorted(grouped):
        lines.append(f"# --- {get_section_header(category)} ---")
        for d in grouped[category]:
            lines.append(d)
        lines.append("")

    while lines and lines[-1] == "":
        lines.pop()
    lines.append("")  # trailing newline

    path.write_text("\n".join(lines), encoding="utf-8")


def write_hosts_txt(grouped, path, tier_label):
    """Write hosts file format. Strips wildcards; uses apex domains only."""
    lines = [
        "# SatoshiShield — Bitcoin Privacy DNS Blocklist",
        "# Hosts file format — compatible with Pi-hole v4, Unix/Windows hosts file",
        f"# {tier_label}",
        f"# {REPO_URL}",
        f"# Version: {VERSION} | Updated: {DATE_ISO}",
        "#",
        "# NOTE: Hosts file format does not support wildcards.",
        "# For subdomain coverage, apply regex.txt as Pi-hole regex deny rules.",
        "#",
        "",
    ]

    for category in sorted(grouped):
        apexes = apex_only_set(grouped[category])
        if not apexes:
            continue
        lines.append(f"# --- {get_section_header(category)} ---")
        for d in sorted(apexes):
            lines.append(f"0.0.0.0 {d}")
        lines.append("")

    while lines and lines[-1] == "":
        lines.pop()
    lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")


def write_abp_file(grouped, path, tier_label):
    """Write Adblock Plus 2.0 syntax. Uses ||domain^ for apex (covers subdomains)."""
    lines = [
        "[Adblock Plus 2.0]",
        f"! Title: SatoshiShield — Bitcoin Privacy DNS Blocklist ({tier_label})",
        "! Description: Blocks blockchain analytics firms and Bitcoin surveillance infrastructure",
        f"! Homepage: {REPO_URL}",
        f"! Version: {VERSION}",
        f"! Last modified: {DATE_ISO}",
        "! License: MIT",
        "!",
        "! ABP/AdGuard syntax: || matches the domain and all subdomains",
        "!",
    ]

    for category in sorted(grouped):
        apexes = apex_only_set(grouped[category])
        if not apexes:
            continue
        lines.append(f"! --- {get_section_header(category)} ---")
        for d in sorted(apexes):
            lines.append(f"||{d}^")

    lines.append("")  # trailing newline
    path.write_text("\n".join(lines), encoding="utf-8")


def write_blocklist_all(t1_grouped, t2_grouped, path):
    """Write combined Tier 1 + Tier 2 blocklist with major tier markers."""
    lines = [
        "# SatoshiShield — Bitcoin Privacy DNS Blocklist",
        "# Domain-only format — compatible with Pi-hole v5+, Pi-hole v6, AdGuard Home",
        "# ALL TIERS COMBINED — Tier 1 (high confidence) + Tier 2 (needs verification).",
        f"# {REPO_URL}",
        f"# Version: {VERSION} | Updated: {DATE_ISO}",
        "#",
        "# Installation (Pi-hole): Settings > Blocklists > Add",
        "# https://raw.githubusercontent.com/cypherpilgrim/satoshishield/main/blocklist-all.txt",
        "#",
        "# NOTE: Pi-hole's URL-fetched lists ignore *.foo.com wildcards.",
        "# For true wildcard coverage of all subdomains, also apply regex.txt",
        "# as Pi-hole regex deny rules. See README for instructions.",
        "#",
        "# WARNING: Tier 2 entries are flagged NEEDS VERIFICATION. Review domains-tier2.csv",
        "# before enabling Tier 2. Some entries (Mixpanel, Amplitude, Segment) are dual-use",
        "# SDKs that may impact non-Bitcoin applications.",
        "#",
        "",
        "# ===== TIER 1 — High confidence =====",
        "",
    ]
    for category in sorted(t1_grouped):
        lines.append(f"# --- {get_section_header(category)} ---")
        for d in t1_grouped[category]:
            lines.append(d)
        lines.append("")

    lines.append("# ===== TIER 2 — Needs verification =====")
    lines.append("")
    for category in sorted(t2_grouped):
        lines.append(f"# --- {get_section_header(category)} ---")
        for d in t2_grouped[category]:
            lines.append(d)
        lines.append("")

    while lines and lines[-1] == "":
        lines.pop()
    lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")


# ---------------------------------------------------------------------------
# regex.txt helper (prints lines to add manually)
# ---------------------------------------------------------------------------

def report_regex_diff(grouped, regex_path):
    """Compare apexes derived from domains.csv against regex.txt entries.
    Prints any missing entries the user needs to add manually."""
    all_apexes = set()
    for category, domains in grouped.items():
        all_apexes |= apex_only_set(domains)

    existing = set()
    if regex_path.exists():
        for line in regex_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("(\\.|^)") and line.endswith("$"):
                domain = line[len("(\\.|^)"):-1].replace("\\.", ".")
                existing.add(domain)

    missing = sorted(all_apexes - existing)
    if not missing:
        print("regex.txt is in sync with domains.csv (Tier 1). No manual additions needed.")
    else:
        print()
        print("regex.txt is missing the following Tier 1 apex entries.")
        print("Add these lines to regex.txt (insertion order preserved by hand):")
        print()
        for d in missing:
            escaped = d.replace(".", "\\.")
            print(f"  (\\.|^){escaped}$")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    t1_path = REPO_ROOT / "domains.csv"
    t2_path = REPO_ROOT / "domains-tier2.csv"

    t1_rows = read_csv(t1_path)
    t2_rows = read_csv(t2_path)

    t1_grouped = group_by_category(t1_rows)
    t2_grouped = group_by_category(t2_rows)

    write_blocklist_txt(
        t1_grouped,
        REPO_ROOT / "blocklist.txt",
        "TIER 1 — High confidence. Organizations whose primary business is Bitcoin surveillance.",
        "blocklist.txt",
    )
    write_hosts_txt(
        t1_grouped,
        REPO_ROOT / "hosts.txt",
        "TIER 1 — High confidence entries only.",
    )
    write_abp_file(
        t1_grouped,
        REPO_ROOT / "satoshishield.abp",
        "Tier 1",
    )

    write_blocklist_txt(
        t2_grouped,
        REPO_ROOT / "blocklist-tier2.txt",
        "TIER 2 — Needs verification. Use with caution. May have higher false positive rate.",
        "blocklist-tier2.txt",
    )
    write_hosts_txt(
        t2_grouped,
        REPO_ROOT / "hosts-tier2.txt",
        "TIER 2 — Needs verification entries.",
    )
    write_abp_file(
        t2_grouped,
        REPO_ROOT / "satoshishield-tier2.abp",
        "Tier 2",
    )

    write_blocklist_all(t1_grouped, t2_grouped, REPO_ROOT / "blocklist-all.txt")

    t1_count = sum(len(v) for v in t1_grouped.values())
    t2_count = sum(len(v) for v in t2_grouped.values())
    print(f"Built v{VERSION} artifacts ({DATE_ISO}):")
    print(f"  Tier 1: {t1_count} entries across {len(t1_grouped)} categories")
    print(f"  Tier 2: {t2_count} entries across {len(t2_grouped)} categories")
    print(f"")
    print(f"Files written:")
    for f in ["blocklist.txt", "hosts.txt", "satoshishield.abp",
              "blocklist-tier2.txt", "hosts-tier2.txt", "satoshishield-tier2.abp",
              "blocklist-all.txt"]:
        print(f"  - {f}")

    report_regex_diff(t1_grouped, REPO_ROOT / "regex.txt")


if __name__ == "__main__":
    main()
