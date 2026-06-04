# SatoshiShield Install Guide

This is the complete setup, end to end: add the list, apply the Pi-hole regex deny rules that the URL list cannot carry on its own, and verify the result. The quick-install block on the home page is enough to get the list loaded; this page is for getting it loaded *correctly*, including the step most people skip.

The recommended setup for everyone is **Tier 1 plus the regex deny rules**. Tier 2 is optional and for advanced users.

---

## Before you start: confirm your devices actually use Pi-hole

The single most common reason SatoshiShield appears not to work is that the device is not using Pi-hole for DNS in the first place. A phone or laptop can be sitting on the same network and still be sending its DNS queries somewhere else — to the router, to a hardcoded `8.8.8.8`, or to a DNS-over-HTTPS resolver baked into the browser. If the query never reaches Pi-hole, no blocklist can act on it.

The reliable way to confirm is the verification test at the bottom of this page: ask a device to resolve a blocked domain and see whether it comes back empty. Do that test on each device you care about, not just the one you set Pi-hole up from.

To cover every device at once, set your **router's DHCP DNS server** to the Pi-hole's address, so the whole network is handed Pi-hole as its resolver. Setting DNS on a single device works too, but it only protects that one device.

---

## Step 1 — Add the blocklist (Pi-hole)

1. Open the Pi-hole admin interface.
2. Go to **Settings > Blocklists > Add**.
3. Add this URL:

```
https://raw.githubusercontent.com/cypherpilgrim/satoshishield/main/blocklist.txt
```

4. Run a gravity update so Pi-hole pulls the list in:

```bash
pihole -g
```

That loads the root domains. It does **not** yet cover subdomains — that is what Step 2 fixes.

---

## Step 2 — Apply the regex deny rules (the part people miss)

Pi-hole's URL-fetched blocklists silently ignore wildcard entries like `*.chainalysis.com`. So even with the list loaded, a query to `api.chainalysis.com` or any other subdomain can still resolve. The regex deny rules in [regex.txt](regex.txt) close that gap by matching any subdomain of each organization, now and in the future.

There are two ways to add them. Use whichever you are comfortable with — the result is identical.

### Option A — Pi-hole admin UI (recommended for most people)

1. Go to **Domains > Add domain**.
2. Set the type to **Regex Filter**.
3. Set the action to **Deny**.
4. Paste one line from [regex.txt](regex.txt), click **Add**, and repeat for each line.

It is tedious — there are 34 patterns as of v1.6.0 — but it requires no command line, and Pi-hole applies regex rules immediately, with no gravity update needed.

### Option B — SQL (faster, advanced)

If you are comfortable with the command line, you can insert every pattern at once. Access the Pi-hole host (on a Pi-hole v6 LXC, that is `pct exec`, not SSH) and run:

```bash
sqlite3 /etc/pihole/gravity.db <<'SQL'
INSERT OR IGNORE INTO domainlist (type, domain, enabled, comment) VALUES
  (3, '(\.|^)chainalysis\.com$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)transpose\.io$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)elliptic\.co$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)trmlabs\.com$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)ciphertrace\.com$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)arkm\.com$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)crystalblockchain\.com$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)bitrank\.com$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)scorechain\.com$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)merkle\.science$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)metasleuth\.io$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)breadcrumbs\.app$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)nansen\.ai$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)glassnode\.com$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)anchain\.ai$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)anchainai\.com$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)blockchaingroup\.io$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)bitrankverified\.com$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)biggdigitalassets\.com$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)bitrace\.io$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)iknaio\.com$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)inca\.digital$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)nterminal\.com$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)lukka\.tech$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)coinfirm\.com$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)matchsystems\.com$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)cryptoofficer\.ai$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)slowmist\.com$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)misttrack\.io$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)uppsalasecurity\.com$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)sentinelprotocol\.io$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)analytics\.coinbase\.com$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)burst\.cloud$', 1, 'SatoshiShield regex'),
  (3, '(\.|^)elementus\.io$', 1, 'SatoshiShield regex');
SQL
```

Then reload the resolver so the new rules take effect:

```bash
pihole reloaddns
```

On Pi-hole v6, use `pihole reloaddns` — it reloads the lists and regex without dropping the resolver. (`pihole restartdns` also works but is heavier.)

[regex.txt](regex.txt) is the canonical source. If the list grows in a later release, re-pull it and add any new lines; the `INSERT OR IGNORE` above is safe to re-run and will skip patterns you already have.

---

## AdGuard Home

AdGuard Home handles the `*.foo.com` wildcard syntax natively, so there is no separate regex step. Add the list and you are done:

1. Go to **Filters > DNS Blocklists > Add blocklist > Add a custom list**.
2. Add:

```
https://raw.githubusercontent.com/cypherpilgrim/satoshishield/main/satoshishield.abp
```

---

## No Pi-hole or AdGuard? Hosts file

For a single machine with no DNS-level blocker, append [hosts.txt](hosts.txt) to the system hosts file (`/etc/hosts` on Linux and macOS, `C:\Windows\System32\drivers\etc\hosts` on Windows), then flush the DNS cache. This is the weakest option — it covers only that one machine, and any browser using DNS-over-HTTPS bypasses it entirely. Pi-hole or AdGuard Home is strongly preferred.

---

## Verify it is working

Run these from a device that uses Pi-hole or AdGuard Home for DNS. This is also the test from the top of the page — the truth check for whether a given device is actually protected.

**A blocked domain should come back empty:**

```bash
dig api.chainalysis.com +short
```

Expected: `0.0.0.0`, or no result at all, depending on your blocking mode. If it returns a real IP address, this device is not protected — either it is not using Pi-hole for DNS, or the regex rules from Step 2 were not applied.

**A few more, to confirm the wildcards are catching subdomains:**

```bash
dig intel.arkm.com +short
dig api.trmlabs.com +short
dig api.elliptic.co +short
```

All should be empty.

**Legitimate Bitcoin infrastructure should still resolve normally:**

```bash
dig mempool.space +short
dig blockstream.info +short
```

These should return real IP addresses. If they do not, something other than SatoshiShield is interfering with your DNS.

**In the admin UI:** open **Tools > Query Log** and filter for one of the surveillance domains. Recent lookups should show as **Blocked (regex deny)** or **Blocked (gravity)**.

---

## When it still does not work

A short checklist for the usual causes, in the order worth checking:

- **The device is not using Pi-hole.** The most frequent one. The `dig` test above returns a real IP. Fix the device's DNS, or set the router's DHCP DNS to the Pi-hole so every device inherits it.
- **The regex rules were not applied.** Root domains block but subdomains like `api.chainalysis.com` still resolve. Re-check Step 2; if you used SQL, confirm you ran `pihole reloaddns` afterward.
- **A browser is using DNS-over-HTTPS.** Some browsers resolve names through their own encrypted resolver and skip your system DNS. Turn off "Secure DNS" / DoH in the browser, or point it at your Pi-hole, so its queries are subject to the blocklist.
- **The router is overriding DNS.** Some ISP routers force their own resolver and ignore the one you set. If so, set DNS on the devices directly, or replace the router's DNS handling.

---

## Beyond your home network

Everything above protects devices while they are on your network. A phone on cellular data resolves through its carrier and is not covered. To carry the protection with you — over Tailscale back to your home Pi-hole, or with an on-device filter — see [Take it with you](README.md#mobile) on the home page.

---

## Tier 2 (optional, advanced)

Tier 2 covers dual-use domains where the surveillance harm needs individual confirmation before blocking. Review [domains-tier2.csv](domains-tier2.csv) first, then add the Tier 2 list the same way: `blocklist-tier2.txt` for Pi-hole, or `satoshishield-tier2.abp` for AdGuard Home. A combined Tier 1 + Tier 2 list is available at `blocklist-all.txt`.
