#!/usr/bin/env python3
"""
SatoshiShield verification-record sanitizer.

Transforms internal verification notes into public-safe Markdown:
  - redacts private lab IPs (192.168/10/172.16-31) and CT### container IDs
  - strips Obsidian [[wikilink]] brackets, keeping the inner text
  - rewrites internal vault path references (verifications/*.md, companies/*.md)
  - removes internal-only sections (vault/workflow housekeeping)
  - prepends a public banner

Usage:
    python3 sanitize_verifications.py <input_dir> <output_dir>

Reusable for any future verification record dropped into <input_dir>.
"""

import os
import re
import sys

# --- internal-only H2 sections to drop entirely -----------------------------
DROP_SECTIONS = (
    "File preservation policy",
    "Where the research lives",
    "PR and release reference",
    "Pull request",
)

BANNER = (
    "> **Public sanitized verification record.** A research artifact from the "
    "SatoshiShield project, published to show the verification methodology "
    "applied to each candidate domain. Internal lab infrastructure has been "
    "redacted. Not legal or financial advice.\n"
)

# --- regex passes ------------------------------------------------------------
PRIV_IP = re.compile(
    r"(?:192\.168|10|172\.(?:1[6-9]|2[0-9]|3[01]))\.\d{1,3}\.\d{1,3}"
)
RESOLVER_FLAG = re.compile(r"@(?:192\.168|10|172\.(?:1[6-9]|2[0-9]|3[01]))\.\d{1,3}\.\d{1,3}")
CT_ID = re.compile(r"\bCT\d+\b")
WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")
VAULT_VERIF = re.compile(r"`?verifications/[0-9A-Za-z._-]+\.md`?")
VAULT_COMPANY = re.compile(r"`?companies/[0-9A-Za-z._-]+\.md`?")
GIT_ARCH = re.compile(r"^.*git log .*-S .*$", re.MULTILINE)


def scrub_text(text: str) -> str:
    text = RESOLVER_FLAG.sub("@<your-resolver>", text)
    text = PRIV_IP.sub("<internal-ip>", text)
    text = CT_ID.sub("the test resolver", text)
    text = WIKILINK.sub(r"\1", text)
    text = VAULT_VERIF.sub("the related verification record", text)
    text = VAULT_COMPANY.sub("the company profile", text)
    text = GIT_ARCH.sub("", text)
    return text


def split_frontmatter(text: str):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            nl = text.find("\n", end + 1)
            return text[: nl + 1], text[nl + 1 :]
    return "", text


def drop_internal_sections(body: str) -> str:
    out, skip = [], False
    for line in body.splitlines(keepends=True):
        if line.startswith("## "):
            head = line[3:].strip()
            skip = any(head.startswith(s) for s in DROP_SECTIONS)
            if skip:
                continue
        elif line.startswith("# ") or line.rstrip() == "---":
            skip = False
        if not skip:
            out.append(line)
    # collapse 3+ blank lines left behind
    return re.sub(r"\n{3,}", "\n\n", "".join(out))


def sanitize(text: str) -> str:
    fm, body = split_frontmatter(text)
    fm = scrub_text(fm)
    body = drop_internal_sections(scrub_text(body))
    parts = [p for p in (fm.rstrip("\n"), BANNER, body.strip()) if p.strip()]
    return "\n\n".join(parts) + "\n"


def main():
    src, dst = sys.argv[1], sys.argv[2]
    os.makedirs(dst, exist_ok=True)
    files = sorted(f for f in os.listdir(src) if f.endswith(".md"))
    for f in files:
        with open(os.path.join(src, f), encoding="utf-8") as fh:
            raw = fh.read()
        with open(os.path.join(dst, f), "w", encoding="utf-8") as fh:
            fh.write(sanitize(raw))
    print(f"Sanitized {len(files)} files -> {dst}")


if __name__ == "__main__":
    main()
