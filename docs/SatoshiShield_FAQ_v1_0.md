# Frequently Asked Questions

Short answers to the questions that come up most. For the full rationale, methodology, and adversarial analysis, see the [white paper](SatoshiShield_WhitePaper_v1_4.md).

## Will blocking these domains break my Bitcoin wallet?

No, if your wallet is configured for privacy. A wallet that connects to your own node or a trusted Electrum server never needs to reach a surveillance domain. A wallet that leans on public infrastructure operated by an analytics firm may lose some functionality — which is the point. The fix is to point that wallet at privacy-respecting infrastructure, not to unblock the surveillance firm.

## I run my own node. Do I need SatoshiShield?

Running your own node is the single most important privacy step you can take, and SatoshiShield does not replace it. It covers a different surface. Your node handles your wallet's traffic; it does nothing about the other apps on your network — browser-based address lookups, price trackers, a family member's mobile wallet phoning home, a block explorer's analytics calls. SatoshiShield blocks those at the DNS layer. The two tools protect different things.

## Does this work on mobile devices?

On your home network, yes — every phone and tablet that resolves DNS through your Pi-hole or AdGuard Home is covered, with no setup on the device itself. But that protection is a property of the network, not the device. The moment a phone leaves the house and drops to cellular data, it resolves DNS through its carrier and the blocklist no longer applies. To carry the protection with you, route the phone's DNS back to your home Pi-hole over Tailscale, or run an on-device filter such as the AdGuard app pointed at the SatoshiShield list. The [install guide](SatoshiShield_Install_Guide_v1_0.md) and the [Take it with you](index.html#mobile) section on the home page cover both.

## Can I use this with a VPN?

Yes. SatoshiShield works at the DNS layer and is independent of your VPN. If your Pi-hole sits inside your VPN, devices on the VPN benefit from it; if it sits outside, it protects your local network. Both are valid — which one fits depends on your threat model.

## Do I need to be technical to set this up?

No. If you can follow a short set of steps, you can stand up Pi-hole or AdGuard Home and load the list, and an AI assistant can walk you through the parts you are unsure about. The [install guide](SatoshiShield_Install_Guide_v1_0.md) has the exact steps, including the Pi-hole regex rules and the verification checks.

## How do I know the list isn't blocking something it shouldn't?

Every entry is documented and auditable. You can browse the [full list](blocked-domains.html) on this site — each domain with its category, a one-sentence privacy harm, a source, and the date it was verified — or read the raw data in `domains.csv`. If you think a domain is wrongly included, open a GitHub issue and it will be reviewed. The MIT license also means you can fork the list and adjust it for your own needs.

## What if a surveillance firm changes its domain?

Where possible the list blocks at the organization level with wildcards, so blocking `*.chainalysis.com` catches every current and future subdomain regardless of name. New domains are caught through community reports and periodic audits, and a release is issued when one is confirmed. If you run automated gravity updates, you get the change without doing anything.

## What does SatoshiShield not protect against?

It is one layer, and it is honest about its edges. It does not stop on-chain analysis of the blockchain itself, it does not help if you hand data to a KYC exchange that shares it directly, and it cannot see an app that ships its own hardcoded DNS-over-HTTPS or connects straight to a hardcoded IP address without a normal DNS lookup. DNS filtering only acts on queries that go through the system resolver. SatoshiShield closes the DNS-layer gap that almost nothing else addresses — not every gap.
