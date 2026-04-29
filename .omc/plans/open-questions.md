# Open Questions

Questions and decisions deferred to the user, persisted across plans.

## initial-plan - 2026-04-28

- [ ] **Badge tagline** — Badger uses "Hack. Tinker. Repeat." What's the Replay equivalent? Used on the home hero.
- [ ] **Color palette** — Default scaffold uses a purple/dark Temporal-ish palette. Does Replay 2026 have its own brand hex values for primary, accent, surface? Drives `assets/css/tokens.css`.
- [ ] **Repo URL / org** — Confirm `github.com/temporalio/badge.temporal.io` (vs. another org/name). Referenced from nav GitHub link and contribute page.
- [ ] **License** — Which license should ship with the repo (MIT, Apache-2.0, other)? Plan intentionally does not pick one.
- [ ] **Favicon mark** — OK with placeholder "R" mark until a real Replay/badge logo lands? Affects `assets/img/favicon.svg`.
- [ ] **Stat counter source** — On home, are app/hack/idea counts hand-edited in HTML, or is there an expectation of a manifest file `main.js` reads? Default plan: hand-edited.
- [ ] **Analytics** — Confirm none for now, not even a privacy-friendly counter? Affects whether a snippet placeholder is needed in `<head>`.
- [ ] **GitHub Pages source** — Confirm deploy from `main` branch root (plan default) vs. `/docs` folder or `gh-pages` branch via Actions. Affects `.nojekyll` placement and any workflow file.
