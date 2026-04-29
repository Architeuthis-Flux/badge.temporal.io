# Initial Plan: badge.temporal.io scaffold

**Plan name:** initial-plan
**Date:** 2026-04-28
**Owner:** alex.tideman@temporal.io
**Status:** Draft (awaiting user confirmation)

---

## Context

Stand up a GitHub Pages site at `badge.temporal.io` for the electronic conference badge handed out at **Replay** (Temporal's annual conference). The repo is currently empty except for `.omc/`. The site is inspired by [badger.github.io](https://badger.github.io/) (Pimoroni Badger 2350 community site) — same shape (top nav, hero with stat counters, apps gallery, hacks tutorials, footer), but Temporal-branded and structured so real Replay-badge content can be filled in later.

Key constraint: we do **not** know the actual badge hardware/firmware yet. Every section that depends on hardware specifics must ship as **visible placeholder text** with `<!-- TODO -->` markers so gaps are obvious in browser preview.

---

## Stack Decision

**Plain HTML / CSS / vanilla JS, no build step. Deploy from `main` branch root with a `.nojekyll` file.**

Rationale (3 sentences): A small marketing/docs site for one event does not justify a build pipeline, dependency lockfile, or framework upgrade burden. Plain HTML keeps the contributor barrier low — anyone at Temporal who knows HTML can edit a page without installing Node/Ruby. Dropping a `.nojekyll` file disables Jekyll processing on GitHub Pages so files like `_drafts.html` or future underscore-prefixed assets ship as-is.

If badge content later grows past ~10 pages or requires templating, migrating to Eleventy is a one-day swap because the HTML is already static.

---

## Work Objectives

1. Create a static-site directory tree and committable scaffold.
2. Mirror the Badger IA (Home, Get Started, Badge Info, Apps, Hacks, Contribute) with Temporal/Replay branding tokens.
3. Wire the site for GitHub Pages deployment at `badge.temporal.io` via CNAME.
4. Make every hardware-specific section a visible, marked placeholder.
5. Document local-preview and deploy steps in `README.md`.

---

## Guardrails

**Must Have**
- Every page renders standalone via `python3 -m http.server 8000` with no console errors and no missing-asset 404s.
- Top nav and footer are identical across all pages (copy-paste partials — acceptable for a 6-page site).
- Color, spacing, and type tokens live in CSS custom properties at `:root` so the Replay palette can be swapped in one file.
- `CNAME` file contains exactly `badge.temporal.io` (no trailing newline issues, no scheme).
- `.nojekyll` exists at repo root.
- Every TODO is both an HTML comment AND visible placeholder text.

**Must NOT Have**
- No Tailwind, React, Astro, Jekyll, npm scripts, or any build step.
- No invented Replay-badge hardware specs, firmware claims, app names, or photos. Use `placeholder.svg` and `Lorem ipsum`-style filler with `[REPLACE: ...]` markers.
- No analytics, search, CMS, or backend.
- No LICENSE file (defer to user — see Open Questions).
- No DNS configuration — only the CNAME file.

---

## Directory Tree to Create

```
badge.temporal.io/
├── .nojekyll
├── .gitignore
├── CNAME
├── README.md
├── index.html
├── get-started/
│   └── index.html
├── badge/
│   └── index.html
├── apps/
│   └── index.html
├── hacks/
│   └── index.html
├── contribute/
│   └── index.html
├── 404.html
└── assets/
    ├── css/
    │   ├── tokens.css
    │   ├── base.css
    │   └── components.css
    ├── js/
    │   └── main.js
    └── img/
        ├── placeholder.svg
        └── favicon.svg
```

Total: 17 files, 8 directories.

---

## Task Flow

```
Setup (T1-T3)
   ↓
Asset & token foundation (T4-T7)
   ↓
Shared components: nav + footer (T8-T9)
   ↓
Page scaffolds (T10-T15)
   ↓
404 + repo hygiene (T16-T18)
   ↓
Local-preview verification (T19)
```

---

## Detailed TODOs

### Setup

**T1. Create `.nojekyll`** — empty file at repo root. *Acceptance:* `ls -la` shows `.nojekyll` (0 bytes).

**T2. Create `.gitignore`** — ignore `.DS_Store`, `*.log`, `node_modules/`, `.idea/`, `.vscode/`, but keep `.omc/plans/` tracked. *Acceptance:* `git status` after a `touch .DS_Store` does not list it.

**T3. Create `CNAME`** — single line: `badge.temporal.io`, no newline at end is OK, no `https://`, no path. *Acceptance:* `wc -c CNAME` returns 18 or 19.

### Asset Foundation

**T4. Create `assets/css/tokens.css`** — `:root` CSS custom properties for: color (primary, primary-dark, accent, bg, surface, text, text-muted, border), spacing scale (`--sp-1` through `--sp-8`), type scale (`--fs-100` through `--fs-700`), radius (`--r-sm`, `--r-md`, `--r-lg`), and shadow tokens. Default to a placeholder Temporal-ish palette (purple `#7C3AED` family on near-black). *Acceptance:* changing `--color-primary` updates buttons and link accents site-wide.

**T5. Create `assets/css/base.css`** — CSS reset, body typography, link styles, container max-width (1100px), focus-visible outline. Imports `tokens.css`. *Acceptance:* loading any HTML page shows readable typography with no horizontal scroll on mobile widths down to 360px.

**T6. Create `assets/css/components.css`** — `.nav`, `.footer`, `.hero`, `.stat-card`, `.app-card`, `.hack-card`, `.btn`, `.btn--primary`, `.section`, `.grid`, `.tag`. Mobile-first; one breakpoint at 720px. *Acceptance:* every component class referenced in HTML has a definition here.

**T7. Create `assets/img/placeholder.svg`** — 600x400 SVG with `Replay Badge Photo` text on a token-colored background. Also create `assets/img/favicon.svg` (simple 32x32 mark, e.g. a stylized "R"). *Acceptance:* both files render in a browser as standalone URLs.

### Shared Components

**T8. Create `assets/js/main.js`** — small vanilla JS for: mobile nav toggle, current-year injection in footer (`<span data-year>`), and active-link highlighting based on `location.pathname`. No dependencies. *Acceptance:* clicking the hamburger toggles `aria-expanded` and a `.is-open` class on `.nav`.

**T9. Define nav + footer markup** — write the canonical nav (links: Home, Get Started, Badge Info, Apps, Hacks, Contribute, GitHub icon link) and footer (3 columns: Learn / Community / Resources) HTML. This markup will be copy-pasted into every page in T10–T15. Document the canonical block at the top of `README.md` so future contributors know to update all 6 pages when the nav changes. *Acceptance:* nav and footer markup exist as a documented snippet ready to paste.

### Page Scaffolds

Each page below includes `<head>` with title, meta description, viewport, favicon link, and the three CSS files; `<body>` with shared nav, page-specific main, shared footer, and `main.js`. Every hardware-specific value uses `[REPLACE: ...]` text plus a matching `<!-- TODO -->` comment.

**T10. `index.html` (Home)** — hero (`[REPLACE: tagline]`, badge photo using `placeholder.svg`, primary CTA → `/get-started/`), three stat cards (`[REPLACE: app count]`, `[REPLACE: hack count]`, `[REPLACE: idea count]`), short "What is the Replay Badge?" intro paragraph, featured apps strip (3 cards linking to `/apps/`), footer. *Acceptance:* page renders, all internal links resolve, no broken images.

**T11. `get-started/index.html`** — "Unbox → Power on → First app" three-step section, prerequisites list (`[REPLACE: USB cable type]`, `[REPLACE: driver install]`), troubleshooting placeholder. *Acceptance:* page renders with three numbered steps and visible TODO markers.

**T12. `badge/index.html` (Badge Info)** — hardware specs table with rows for SoC, display, buttons, battery, connectivity — every cell is `[REPLACE: spec]`, plus a "Pinout" placeholder figure using `placeholder.svg`. *Acceptance:* spec table renders with at least 6 rows of placeholders.

**T13. `apps/index.html`** — grid of 6 placeholder app cards (icon = `placeholder.svg`, title = `[REPLACE: App Name]`, 1-line description, `tag` chips for category). Intro paragraph explains "Preloaded apps ship with the badge." *Acceptance:* grid is responsive — 1 col on mobile, 2 on tablet, 3 on desktop.

**T14. `hacks/index.html`** — list of 3 placeholder beginner tutorials, each with title, time-estimate badge (`[REPLACE: ~15 min]`), difficulty tag, 1-line summary. *Acceptance:* tutorials render as cards with visible time/difficulty metadata.

**T15. `contribute/index.html`** — "How to contribute" with sections for: submitting an app, submitting a hack, reporting issues. Link to GitHub repo (`[REPLACE: repo URL]`) and code of conduct (`[REPLACE: link]`). *Acceptance:* page renders with three contribution paths and visible TODO markers for repo/CoC URLs.

### Hygiene

**T16. `404.html`** — branded 404 with link back to home. GitHub Pages serves this automatically. *Acceptance:* visiting a non-existent path locally with a server that respects 404.html shows the branded page.

**T17. `README.md`** — sections: Overview, Local Preview (`python3 -m http.server 8000`), Editing (where tokens live, how to add a page, the canonical nav/footer rule from T9), Deploying (push to `main`, GitHub Pages auto-deploys, CNAME explained), TODO Conventions (explain `[REPLACE: ...]` and `<!-- TODO -->`). *Acceptance:* a contributor with no prior context can clone, preview locally, and edit the home page tagline within 5 minutes of reading.

**T18. Final TODO sweep** — `grep -rn "REPLACE\|TODO" .` to produce a single inventory of every placeholder. Paste the inventory at the bottom of `README.md` under `## Outstanding Placeholders` so the user has a checklist. *Acceptance:* the inventory in `README.md` matches the live grep output.

### Verification

**T19. Local preview smoke test** — run `python3 -m http.server 8000` from repo root, visit each of the 6 pages plus `/nonexistent` (404), confirm: (a) no console errors, (b) no 404s in network tab for assets, (c) nav highlights the active page, (d) footer year is current, (e) hamburger works on a 375px viewport. *Acceptance:* all 5 checks pass and screenshots are attached to the PR (or evidence noted in the executor's verification report).

---

## Success Criteria

- All 17 files exist at the paths in the directory tree above.
- `python3 -m http.server 8000` serves all 6 pages with zero console errors and zero asset 404s.
- `CNAME` and `.nojekyll` are present at repo root.
- Every hardware-specific value is a `[REPLACE: ...]` placeholder, inventoried at the bottom of `README.md`.
- Color/spacing/type tokens are isolated in `assets/css/tokens.css` so a Replay-brand swap touches only one file.
- A new contributor can clone the repo and preview locally in under 5 minutes following `README.md`.

---

## Out of Scope (explicit)

- Real badge hardware specs, firmware code, or app source.
- Backend, search, analytics, CMS.
- Custom domain DNS configuration (zone file, A/AAAA records). Only the in-repo CNAME file is included.
- Choosing or adding a `LICENSE` (see Open Questions).
- Visual design polish beyond the token-driven scaffold (no custom illustrations, no motion design, no dark-mode toggle).

---

## Open Questions for the User

1. **Badge tagline.** Badger uses "Hack. Tinker. Repeat." — what's the Replay equivalent? (Used on the home hero.)
2. **Color palette.** Default scaffold uses a purple/dark Temporal-ish palette. Does Replay 2026 have its own brand colors and if so, what are the hex values for primary, accent, and surface?
3. **Repo URL / org.** Confirm: is the repo `github.com/temporalio/badge.temporal.io` or somewhere else? This URL is referenced from the nav GitHub link and the contribute page.
4. **License.** What license should the repo ship with? (MIT and Apache-2.0 are the most common for Temporal repos — defer to legal/standard policy.)
5. **Favicon mark.** OK with a simple "R" placeholder until a real Replay/badge mark is provided?
6. **Stat counter source.** On the home page, are the app/hack/idea counts hand-edited in HTML for now, or is there an expectation of a manifest file that `main.js` reads? (Default plan: hand-edited HTML for the scaffold.)
7. **Analytics.** Confirm none for now — really nothing, not even a privacy-friendly counter? (Default: none.)
8. **GitHub Pages source.** Confirm: deploy from `main` branch root (default in this plan), not `/docs` and not a `gh-pages` branch via Actions?

---

## Plan Summary

**Plan saved to:** `/Users/alex.tideman/Temporal/badge.temporal.io/.omc/plans/initial-plan.md`

**Scope:**
- 19 atomic tasks across 17 files / 8 directories
- Estimated complexity: **LOW**
- Single executor, ~2–4 hours of work

**Key Deliverables:**
1. Scaffolded GitHub Pages site (6 content pages + 404 + assets) at the repo root.
2. Token-driven CSS so Replay branding can be applied in one file.
3. CNAME + `.nojekyll` wired for `badge.temporal.io` deploy from `main`.
4. `README.md` with local-preview, editing, and TODO conventions plus a placeholder inventory.

**Stack:** Plain HTML / CSS / vanilla JS, no build step, deployed from `main` branch root.
