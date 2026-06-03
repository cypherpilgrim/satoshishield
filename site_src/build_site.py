#!/usr/bin/env python3
"""
SatoshiShield static site generator.

Renders the project's markdown documentation into a self-contained static
site under ./site/. No external/runtime dependencies for the published
site: all fonts and CSS are local, zero third-party requests.

Build deps (build time only): markdown, (optional) nothing else.
    pip install markdown

Usage:
    python3 site_src/build_site.py
Output:
    site/index.html, site/<doc>.html, site/assets/...
"""

import re
import shutil
import html
from pathlib import Path

import markdown

# ------------------------------------------------------------------ paths
ROOT = Path(__file__).resolve().parent.parent      # repo root
SRC = ROOT / "site_src"
OUT = ROOT / "site"
REPO_URL = "https://github.com/cypherpilgrim/satoshishield"
REPO_BLOB = REPO_URL + "/blob/main/"

# ------------------------------------------------------------------ doc map
# order matters: drives the in-site "Documentation" nav order
DOCS = [
    ("docs/SatoshiShield_The_Background_Hum_v1_0.md",
     "The Background Hum", "Case study · Start here"),
    ("docs/Why_Bitcoin_Privacy_Matters_v1_0.md",
     "Why Bitcoin Privacy Matters", "Primer"),
    ("docs/Why_Bitcoin_Privacy_Matters_Deep_Dive_v1_0.md",
     "Why Bitcoin Privacy Matters — Deep Dive", "Primer · Long form"),
    ("docs/IRS_Privacy_Coin_Tracing_Case_Study.md",
     "Case Study — IRS Privacy-Coin Tracing", "Evidence"),
    ("docs/IRS_Procurement_Landscape_Followup.md",
     "Case Study — Federal Procurement Stack", "Evidence"),
    ("docs/SatoshiShield_WhitePaper_v1_4.md",
     "White Paper", "Technical"),
    ("docs/SatoshiShield_Node_Sovereignty_v1_0.md",
     "Node Sovereignty", "Technical"),
    ("docs/SatoshiShield_Contributor_Guide_v1_4.md",
     "Contributor Guide", "Contribute"),
    ("docs/SatoshiShield_Monitor_Deployment_v1_4.md",
     "Monitor Deployment Guide", "Operate"),
    ("monitor/SatoshiShield_Monitor_Report_Reading_Guide_v1_0.md",
     "Monitor Report Reading Guide", "Operate"),
    ("docs/SatoshiShield_Quarterly_Checklist_v1_4.md",
     "Quarterly Checklist", "Contribute"),
    ("CONTRIBUTING.md", "Contributing", "Contribute"),
    ("CHANGELOG.md", "Changelog", "Project"),
    ("SECURITY.md", "Security Policy", "Project"),
]

# basename(.md) -> output html filename, for link rewriting
DOC_HTML = {Path(src).stem: Path(src).stem + ".html" for src, _, _ in DOCS}
DOC_HTML["README"] = "index.html"


# ------------------------------------------------------------------ slugify
def gh_slugify(value, separator="-"):
    """Approximate GitHub's heading-anchor algorithm so the docs'
    hand-written tables of contents (#1-meet-carlos etc.) resolve."""
    s = value.strip().lower()
    s = s.replace("&amp;", "").replace("&", "")
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)   # drop punctuation
    s = re.sub(r"\s+", separator, s)
    return s


# ------------------------------------------------------------------ link fix
def rewrite_links(body_html: str) -> str:
    """.md links -> .html; other in-repo files -> GitHub blob; leave the rest."""
    def repl(m):
        quote, href = m.group(1), m.group(2)
        if href.startswith(("http://", "https://", "mailto:", "#")):
            return m.group(0)
        anchor = ""
        if "#" in href:
            href, anchor = href.split("#", 1)
            anchor = "#" + anchor
        path = href.lstrip("./")
        path = re.sub(r"^(\.\./)+", "", path)
        stem = Path(path).stem
        if path.endswith(".md") and stem in DOC_HTML:
            target = DOC_HTML[stem]
        elif path.endswith(".md"):
            target = stem + ".html"
        elif path == "" and anchor:
            target = ""
        else:
            target = REPO_BLOB + path           # csv, txt, abp, py, LICENSE ...
        return f"href={quote}{target}{anchor}{quote}"

    return re.sub(r'href=(["\'])([^"\']+)\1', repl, body_html)


# ------------------------------------------------------------------ toc html
def _iter_level(tokens, level):
    """Yield all toc tokens of a given level anywhere in the nested tree
    (Python-Markdown nests H2s under a leading H1, etc.)."""
    for t in tokens:
        if t["level"] == level:
            yield t
        else:
            yield from _iter_level(t.get("children", []), level)


def build_toc(tokens) -> str:
    """Two-level TOC from markdown toc_tokens (h2 with nested h3)."""
    items = []
    for tok in _iter_level(tokens, 2):
        subs = list(_iter_level(tok.get("children", []), 3))
        sub_html = ""
        if subs:
            sub_html = "<ul>" + "".join(
                f'<li><a href="#{c["id"]}">{html.escape(c["name"])}</a></li>'
                for c in subs
            ) + "</ul>"
        items.append(
            f'<li><a href="#{tok["id"]}">{html.escape(tok["name"])}</a>{sub_html}</li>'
        )
    if not items:
        return ""
    return (
        '<nav class="toc" aria-label="On this page">'
        '<div class="h">On this page</div><ul>' + "".join(items) + "</ul></nav>"
    )


# ------------------------------------------------------------------ shell
def page_shell(title, kicker, toc_html, content_html):
    nav = (
        f'<a href="SatoshiShield_The_Background_Hum_v1_0.html">Start</a>'
        f'<a href="index.html#blocked">What\'s blocked</a>'
        f'<a href="index.html#install">Install</a>'
        f'<a href="index.html#docs">Docs</a>'
        f'<a href="{REPO_URL}">GitHub</a>'
    )
    kicker_html = f'<div class="doc-meta">{html.escape(kicker)}</div>' if kicker else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} — SatoshiShield</title>
<meta name="description" content="SatoshiShield — Bitcoin privacy DNS blocklist for Pi-hole and AdGuard Home.">
<meta name="referrer" content="no-referrer">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="topbar"><div class="wrap">
  <a class="brand" href="index.html"><span class="b">&#8383;</span> SatoshiShield</a>
  <nav class="topnav">{nav}</nav>
</div></header>

<main class="wrap doc">
  <div class="doc-shell">
    {toc_html}
    <article>
      {kicker_html}
      {content_html}
    </article>
  </div>
</main>

{FOOTER}
</body>
</html>
"""


FOOTER = f"""<footer class="site"><div class="wrap">
  <div class="privacy">
    <span class="dot">&#9679;</span> This site makes zero third-party requests.
    No trackers, no analytics, no Google Fonts, no CDNs. Fonts and styles are
    served locally. Open your browser's network tab and check — a privacy tool's
    own site should not surveil its visitors.
  </div>
  <div class="ident">
    Maintained pseudonymously. Privacy is not a crime; blocking surveillance
    infrastructure is self-defense. &middot; <a href="{REPO_URL}">Source on GitHub</a> &middot; MIT
  </div>
</div></footer>"""


# ------------------------------------------------------------------ render
def strip_manual_toc(text: str) -> str:
    """Remove a hand-written '## Table of Contents' block (heading + list);
    the site renders its own sidebar TOC instead."""
    m = re.search(r"(?im)^\#{2,3}\s+Table of Contents\s*$", text)
    if not m:
        return text
    rest = text[m.end():]
    nb = re.search(r"\n-{3,}\s*\n", rest)          # next thematic break
    nh = re.search(r"\n\#{1,3}\s+\S", rest)         # next heading
    cuts = [x for x in (nb, nh) if x]
    if not cuts:
        return text
    first = min(cuts, key=lambda x: x.start())
    end = m.end() + (first.end() if first is nb else first.start())
    return text[: m.start()] + text[end:]


def render_doc(src_rel, title, kicker):
    src = ROOT / src_rel
    text = strip_manual_toc(src.read_text(encoding="utf-8"))

    md = markdown.Markdown(
        extensions=["extra", "toc", "sane_lists", "attr_list"],
        extension_configs={"toc": {"slugify": gh_slugify, "separator": "-"}},
    )
    content = md.convert(text)
    toc_html = build_toc(md.toc_tokens)
    content = rewrite_links(content)
    # wrap tables for horizontal scroll on mobile
    content = content.replace("<table>", '<div class="tablewrap"><table>').replace(
        "</table>", "</table></div>"
    )

    out = OUT / (Path(src_rel).stem + ".html")
    out.write_text(page_shell(title, kicker, toc_html, content), encoding="utf-8")
    return out.name


# ------------------------------------------------------------------ main
def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    shutil.copytree(SRC / "assets", OUT / "assets")
    if (SRC / ".well-known").exists():
        shutil.copytree(SRC / ".well-known", OUT / ".well-known")
    # landing page
    shutil.copy(SRC / "templates" / "landing.html", OUT / "index.html")

    built = []
    for src_rel, title, kicker in DOCS:
        if (ROOT / src_rel).exists():
            built.append(render_doc(src_rel, title, kicker))
        else:
            print(f"  ! skip (missing): {src_rel}")
    print(f"Built index.html + {len(built)} doc pages -> {OUT}")


if __name__ == "__main__":
    main()
