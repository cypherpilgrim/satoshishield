# Security Policy

SatoshiShield is a privacy tool, so security issues for this project look a little different from a typical software repository. This document covers what to report, how to report it, and what to expect.

---

## What Counts as a Security Issue

For SatoshiShield, the following are treated as security issues:

- **A surveillance firm domain that should be blocked but is not.** Either the domain is missing from the blocklist entirely, or the regex/wildcard pattern fails to catch a known subdomain pattern.
- **A legitimate domain that is incorrectly blocked.** Either the domain belongs to a non-surveillance organization, or blocking it breaks legitimate Bitcoin wallet or infrastructure functionality.
- **A vulnerability in the monitor script** (`monitor/satoshishield_monitor.py`) that could expose user data, leak credentials, or allow unauthorized access to the Pi-hole FTL database.
- **A supply chain issue** affecting how users fetch the blocklist (for example, a way to inject malicious entries into the published lists).
- **Documentation that misleads users about what protection SatoshiShield provides**, in a way that could cause them to underestimate their actual exposure.

The first two categories are the most common and the most important. SatoshiShield is only useful if it accurately reflects the surveillance landscape, so corrections to the blocklist itself are treated with the same urgency as code vulnerabilities.

---

## How to Report

### Public reports (preferred for most issues)

For missing surveillance domains, incorrectly blocked legitimate domains, and documentation issues, open a GitHub issue at:

`https://github.com/cypherpilgrim/satoshishield/issues`

Public reporting is preferred because it lets the community verify the finding and contribute additional evidence. Include the same verification steps documented in [CONTRIBUTING.md](CONTRIBUTING.md) if you are reporting a missing or incorrect domain.

### Private reports (for sensitive issues)

For vulnerabilities in the monitor script, supply chain concerns, or any issue that could be exploited before a fix is released, open a private security advisory at:

`https://github.com/cypherpilgrim/satoshishield/security/advisories/new`

Private security advisories are visible only to repository maintainers until disclosed.

---

## What to Expect

| Stage | Timeframe | What Happens |
|---|---|---|
| Initial response | Within 7 days | A maintainer acknowledges the report and confirms whether it is being treated as a security issue. |
| Investigation | Within 14 days | The maintainer investigates, reproduces if possible, and determines the appropriate fix. |
| Fix and disclosure | Within 30 days for most issues | The fix is published in a release. Reporters who requested credit are acknowledged in the release notes. |
| Coordinated disclosure | Negotiated case-by-case | For issues that affect downstream users (Pi-hole installations, monitor deployments), public disclosure may be timed to coincide with a fixed release. |

---

## What Does NOT Get Treated as a Security Issue

- **Domain choices that are working as designed.** If a domain is in the blocklist because the documented criteria are met, disagreement about whether the domain *should* be blocked is a normal contribution discussion, not a security issue. Open a regular GitHub issue or pull request.
- **Tier 2 entries flagged as NEEDS VERIFICATION.** These are explicitly marked as pending verification. The risk is documented and accepted by users who enable Tier 2.
- **Issues in upstream tools.** Bugs in Pi-hole, AdGuard Home, or any other tool that consumes the SatoshiShield blocklist should be reported to those projects directly.
- **Performance or usability concerns.** These are regular issues, not security issues.

---

## Responsible Disclosure

SatoshiShield is a privacy tool. Disclosing a vulnerability that lets surveillance firms evade the blocklist before a fix is released would harm the users this project is trying to protect.

Reporters are asked to coordinate disclosure timing with maintainers. The default policy is 30 days from initial report to public disclosure, with extensions negotiable for complex fixes.

Reporters who follow responsible disclosure will be credited in release notes (with pseudonyms accepted) unless they prefer to remain anonymous.

---

## Contact

All security communication happens through the GitHub interfaces above. SatoshiShield is maintained pseudonymously and does not have an out-of-band email channel.
