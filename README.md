# Strongpoint Advisory

**Target: https://advisors.strongpointops.com** — *no DNS record yet; the
custom domain is not attached, so siblings route Advisory references to the
firm page instead of reinstating a dead link.*

**Independent project consulting — not construction-specific.** Feasibility,
estimates and risk work for anyone weighing a project: a homeowner costing a
remodel, landscape or custom build; a manufacturer sizing regulatory, capital
and efficiency exposure; a buyer pricing a property on what it will actually
take.

The hook is the independence, and it is the whole positioning: **an estimate
from someone who is not bidding on the work.** The fee is the same whether the
client builds with Strongpoint Build, builds with somebody else, or decides not
to build. "Your project does not pencil" is a legitimate deliverable.

Three honest endings are stated on the page — shop the scope to three
contractors, sit on it, or hand it to Build to manage. Do not add a clause that
steers people back to Build; the absence of one is the product.

Plain HTML/CSS/JS. **No build step, no framework, no npm dependencies.** Every
page is self-contained.

```
wrangler.jsonc   Cloudflare config — static assets only, no Worker script
site/
  index.html     the six practice areas, the white-paper deliverable,
                 engagement and fees, the group, Market Notes
  contact.html   intake by need, stage and scale; composes a mailto
  404.html       lists every real destination including the sibling companies
tools/build.py   keeps the shared <style> block in sync across pages
```

## Why this is a separate company

Advising an owner on whether to build is not a job for the people who would be
paid to build it. Strongpoint Build is the GC; this company is deliberately not
the same entity. The engagement section says so on the page and commits to
disclosing any overlap in writing before an engagement starts. **Do not soften
that copy** — it is the difference between a disclosure and a liability.

The split with Build is by phase:

| | Advisory | Build |
| --- | --- | --- |
| when | before and around a commitment | once the project is real |
| work | feasibility, capital planning, entitlement strategy, diligence, white papers | owner's-rep PM and construction management under one GC |
| fees | retainer, or fixed fee per deliverable | cost-plus; flat retainer over $2.5M |

## Theme

Fifth property in the group. Ground `#0e1316`, accent `#7fa968`, Archivo Narrow
/ IBM Plex Sans / IBM Plex Mono.

The accent clears all three gates from the Brand Playbook, measured:

- **6.92:1** against its own ground (needs ≥ 4.5:1)
- **65°** minimum hue separation from every sibling accent — parent 210°,
  principal 34°, build 23°, dashboard 186°; this is hue 99° (needs ≥ 60°)
- not the family colour `#6f8fa8`, which is reserved for links that leave the
  property

## Placeholders

`[surname]`, `info@strongpointops.com`, `[PHONE]`. The contact form has no backend — it
composes a mailto. Market Notes has no list backend; the form carries the four
qualifying answers into a mailto rather than dropping them.

## Local

```bash
cd site && python3 -m http.server 8899
```
