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
import csv
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
DOMAINS_CSV = ROOT / "domains.csv"


def domain_records():
    """All domains.csv rows that have a domain value."""
    if not DOMAINS_CSV.exists():
        return []
    out = []
    with DOMAINS_CSV.open(encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            if (r.get("domain") or "").strip():
                out.append(r)
    return out


def domain_counts(records):
    """(entry_count, distinct_org_count, sorted_category_list)."""
    orgs = {(r["organization"] or "").strip() for r in records if (r["organization"] or "").strip()}
    cats = sorted({(r["category"] or "").strip() for r in records if (r["category"] or "").strip()})
    return len(records), len(orgs), cats


CHANGELOG_MD = ROOT / "CHANGELOG.md"


def latest_release():
    """Parse the most recent version + date from CHANGELOG.md.
    Returns (version, iso_date) or (None, None)."""
    if not CHANGELOG_MD.exists():
        return None, None
    text = CHANGELOG_MD.read_text(encoding="utf-8")
    # first '## [X.Y.Z] - YYYY-MM-DD' (date separator may be -, en/em dash)
    m = re.search(
        r"^\#{2}\s*\[(\d+\.\d+\.\d+)\]\s*[-\u2013\u2014]\s*(\d{4}-\d{2}-\d{2})",
        text, re.M,
    )
    return (m.group(1), m.group(2)) if m else (None, None)

# ------------------------------------------------------------------ doc map
# order matters: drives the in-site "Documentation" nav order
DOCS = [
    ("docs/SatoshiShield_The_Background_Hum_v1_0.md",
     "The Background Hum", "Case study · Start here"),
    ("docs/SatoshiShield_Install_Guide_v1_0.md",
     "Install Guide", "Install"),
    ("docs/SatoshiShield_FAQ_v1_0.md",
     "FAQ", "FAQ"),
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
    ("CHANGELOG.md", "Releases", "Project · Release history"),
    ("SECURITY.md", "Security Policy", "Project"),
]

# Verification records — auto-discovered from verifications/*.md. Built to HTML
# and registered for link rewriting, but kept OUT of the static nav; they are
# reachable from the generated Verification Records index page. Drop a new
# sanitized record into verifications/ and it appears on the next build.
VERIF_DIR = ROOT / "verifications"


def _verif_title(stem):
    """2026-05-26-anchain-ai -> 'Anchain Ai' (display title for the page)."""
    return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", stem).replace("-", " ").title()


def verification_docs():
    if not VERIF_DIR.exists():
        return []
    out = []
    for p in sorted(VERIF_DIR.glob("*.md")):
        if p.name.lower() == "readme.md":
            continue
        out.append((f"verifications/{p.name}", _verif_title(p.stem),
                    "Verification record"))
    return out


DOCS = DOCS + verification_docs()

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
        elif path.endswith(".html"):
            target = path           # already-built site page (relative)
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
        f'<a href="CHANGELOG.html">Releases</a>'
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


def strip_frontmatter(text: str) -> str:
    """Remove a leading YAML frontmatter block (--- ... ---) so it doesn't
    render as visible junk. No-op for docs without frontmatter."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            nl = text.find("\n", end + 1)
            return text[nl + 1:] if nl != -1 else ""
    return text


def render_doc(src_rel, title, kicker):
    src = ROOT / src_rel
    text = strip_frontmatter(src.read_text(encoding="utf-8"))
    text = strip_manual_toc(text)

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


# ------------------------------------------------------------------ domain directory
def _esc(s, attr=False):
    return html.escape((s or "").strip(), quote=attr)


def blocked_page_shell(title, body_html, tail_html=""):
    nav = (
        f'<a href="SatoshiShield_The_Background_Hum_v1_0.html">Start</a>'
        f'<a href="index.html#blocked">What\'s blocked</a>'
        f'<a href="index.html#install">Install</a>'
        f'<a href="index.html#docs">Docs</a>'
        f'<a href="CHANGELOG.html">Releases</a>'
        f'<a href="{REPO_URL}">GitHub</a>'
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} — SatoshiShield</title>
<meta name="description" content="The full SatoshiShield blocklist: every blocked surveillance-firm domain with its category, privacy harm, source, and verification date.">
<meta name="referrer" content="no-referrer">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="topbar"><div class="wrap">
  <a class="brand" href="index.html"><span class="b">&#8383;</span> SatoshiShield</a>
  <nav class="topnav">{nav}</nav>
</div></header>

<main>
{body_html}
</main>

{FOOTER}
{tail_html}
</body>
</html>
"""


def render_blocked_domains():
    """Render domains.csv into a searchable, filterable on-site table."""
    if not DOMAINS_CSV.exists():
        print("  ! skip (missing): domains.csv")
        return None

    rows = domain_records()
    total, org_count, cats = domain_counts(rows)

    cat_options = '<option value="">All categories</option>' + "".join(
        f'<option value="{_esc(c, attr=True)}">{_esc(c)}</option>' for c in cats
    )

    tr = []
    for r in rows:
        domain = (r["domain"] or "").strip()
        org = (r["organization"] or "").strip()
        cat = (r["category"] or "").strip()
        harm = (r["harm"] or "").strip()
        src = (r["source"] or "").strip()
        ver = (r.get("date_verified") or "").strip()
        blob = " ".join([domain, org, cat, harm]).lower()
        src_cell = (
            f'<a href="{_esc(src, attr=True)}" target="_blank" rel="noreferrer noopener">source &#8599;</a>'
            if src else "&mdash;"
        )
        tr.append(
            f'<tr data-cat="{_esc(cat, attr=True)}" data-search="{_esc(blob, attr=True)}">'
            f'<td><code>{_esc(domain)}</code></td>'
            f'<td class="org">{_esc(org)}</td>'
            f'<td class="cat">{_esc(cat)}</td>'
            f'<td class="harm">{_esc(harm)}</td>'
            f'<td class="src">{src_cell}</td>'
            f'<td class="ver">{_esc(ver)}</td>'
            "</tr>"
        )
    rows_html = "\n".join(tr)

    body = f"""<section class="band dirsec"><div class="wrap">
  <div class="kicker">What gets blocked &middot; Tier 1</div>
  <h2>The full list</h2>
  <p class="lede">Every entry below is the live blocklist data, rendered straight from <code>domains.csv</code> &mdash; all {total} Tier 1 entries from {org_count} organizations across {len(cats)} categories of surveillance. Each carries a one-sentence privacy harm, a source you can check, and the date it was last verified. Search or filter to find a specific firm or domain.</p>

  <div class="dir-controls">
    <input id="dir-q" type="search" placeholder="Search domain, organization, or harm&hellip;" autocomplete="off" spellcheck="false">
    <select id="dir-cat" aria-label="Filter by category">{cat_options}</select>
    <span class="dir-count" id="dir-count">Showing {total} of {total}</span>
  </div>

  <div class="dirwrap">
    <table class="domtable" id="dir-table">
      <thead><tr>
        <th>Domain</th><th>Organization</th><th>Category</th>
        <th>Privacy harm</th><th>Source</th><th>Verified</th>
      </tr></thead>
      <tbody>
{rows_html}
      </tbody>
    </table>
  </div>

  <p class="dir-foot">Generated from the source data on every build. Prefer the raw file? <a href="{REPO_BLOB}domains.csv">View domains.csv on GitHub</a>.</p>
</div></section>"""

    script = """<script>
(function () {
  var q = document.getElementById('dir-q');
  var cat = document.getElementById('dir-cat');
  var count = document.getElementById('dir-count');
  var rows = Array.prototype.slice.call(
    document.querySelectorAll('#dir-table tbody tr'));
  var total = rows.length;
  function apply() {
    var term = (q.value || '').trim().toLowerCase();
    var c = cat.value || '';
    var shown = 0;
    for (var i = 0; i < rows.length; i++) {
      var r = rows[i];
      var okText = !term || r.getAttribute('data-search').indexOf(term) !== -1;
      var okCat = !c || r.getAttribute('data-cat') === c;
      if (okText && okCat) { r.style.display = ''; shown++; }
      else { r.style.display = 'none'; }
    }
    count.textContent = 'Showing ' + shown + ' of ' + total;
  }
  q.addEventListener('input', apply);
  cat.addEventListener('change', apply);
  apply();
})();
</script>"""

    out = OUT / "blocked-domains.html"
    out.write_text(blocked_page_shell("Blocked Domains", body, script), encoding="utf-8")
    return out.name


def _fm_value(text, key):
    m = re.search(rf'^{key}:\s*"?(.*?)"?\s*$', text, re.MULTILINE)
    return m.group(1).strip() if m else ""


def render_verifications_index():
    """Generate verifications.html: an index of every verification record,
    grouped by outcome, linking to each built record page."""
    if not VERIF_DIR.exists():
        return None
    recs = []
    for p in sorted(VERIF_DIR.glob("*.md")):
        if p.name.lower() == "readme.md":
            continue
        t = p.read_text(encoding="utf-8")
        recs.append({
            "html": p.stem + ".html",
            "company": _fm_value(t, "company") or _verif_title(p.stem),
            "date": _fm_value(t, "date"),
            "outcome": _fm_value(t, "outcome"),
            "tier": _fm_value(t, "tier"),
            "hq": _fm_value(t, "hq_country"),
        })

    def bucket(o):
        o = o.upper()
        if "EXCLUD" in o:
            return "Excluded"
        if "CONSOLIDAT" in o:
            return "Consolidated into parent"
        if "PENDING" in o:
            return "Verified — pending functional test"
        return "Included"

    order = ["Included", "Verified — pending functional test",
             "Consolidated into parent", "Excluded"]
    blurb = {
        "Included": "Met the inclusion criteria and shipped to the blocklist.",
        "Verified — pending functional test": "Met the criteria on the evidence; final on-network wallet-impact test still to run.",
        "Consolidated into parent": "Independent surveillance history documented; coverage ships under an acquiring parent vendor.",
        "Excluded": "Surveillance-adjacent but did not meet the criteria — no user-layer query surface DNS blocking can address.",
    }
    groups = {k: [] for k in order}
    for r in recs:
        groups[bucket(r["outcome"])].append(r)

    inc = sum(len(groups[k]) for k in order[:2])
    parts = [
        '<div class="doc-meta">Research · Verification records</div>',
        "<h1>Verification Records</h1>",
        "<p>Every candidate domain runs through the same seven-step process before it "
        "is included in or excluded from the blocklist: WHOIS/RDAP, SSL certificate "
        "inspection, passive DNS, behavioral evidence, privacy-harm assessment, "
        "inclusion-criteria scoring (six criteria), and a functional-impact test "
        "confirming no Bitcoin wallet breakage. Each record below documents that work. "
        "Internal lab infrastructure has been redacted; these are research artifacts, "
        "not legal or financial advice.</p>",
        f"<p><strong>{len(recs)} records</strong> — {inc} verified for inclusion, "
        f"{len(groups['Excluded'])} excluded, "
        f"{len(groups['Consolidated into parent'])} consolidated into a parent vendor.</p>",
    ]
    for k in order:
        if not groups[k]:
            continue
        parts.append(f"<h2>{html.escape(k)}</h2>")
        parts.append(f"<p>{html.escape(blurb[k])}</p>")
        parts.append('<div class="tablewrap"><table>')
        parts.append("<thead><tr><th>Company</th><th>Date</th><th>Region</th>"
                     "<th>Tier</th></tr></thead><tbody>")
        for r in sorted(groups[k], key=lambda x: x["company"].lower()):
            name = _esc(r["company"].replace("-", " ").title())
            tier = _esc(r["tier"]) if r["tier"] and r["tier"] != "N/A (excluded)" else "&mdash;"
            parts.append(
                f'<tr><td><a href="{_esc(r["html"], attr=True)}">{name}</a></td>'
                f'<td>{_esc(r["date"]) or "&mdash;"}</td>'
                f'<td>{_esc(r["hq"]) or "&mdash;"}</td><td>{tier}</td></tr>'
            )
        parts.append("</tbody></table></div>")

    content = "\n".join(parts)
    out = OUT / "verifications.html"
    out.write_text(page_shell("Verification Records",
                              "Research", "", content), encoding="utf-8")
    return out.name


# ------------------------------------------------------------------ main
def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    shutil.copytree(SRC / "assets", OUT / "assets")
    if (SRC / ".well-known").exists():
        shutil.copytree(SRC / ".well-known", OUT / ".well-known")
    # landing page — inject live counts from domains.csv so the homepage
    # figures stay in sync with the source data and the directory page
    records = domain_records()
    total, org_count, cats = domain_counts(records)
    ver, date = latest_release()
    landing = (SRC / "templates" / "landing.html").read_text(encoding="utf-8")
    landing = (landing
               .replace("{{ORG_COUNT}}", str(org_count))
               .replace("{{CAT_COUNT}}", str(len(cats)))
               .replace("{{DOMAIN_COUNT}}", str(total))
               .replace("{{LATEST_VERSION}}", ver or "")
               .replace("{{LATEST_DATE}}", date or ""))
    (OUT / "index.html").write_text(landing, encoding="utf-8")

    built = []
    for src_rel, title, kicker in DOCS:
        if (ROOT / src_rel).exists():
            built.append(render_doc(src_rel, title, kicker))
        else:
            print(f"  ! skip (missing): {src_rel}")

    bd = render_blocked_domains()
    if bd:
        built.append(bd)

    vi = render_verifications_index()
    if vi:
        built.append(vi)

    print(f"Built index.html + {len(built)} pages -> {OUT}")


if __name__ == "__main__":
    main()
