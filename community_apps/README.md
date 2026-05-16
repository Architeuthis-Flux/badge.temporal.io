# Community Apps

Installable MicroPython apps live under `<app>/` in this directory. These
apps are published to a generated `community_apps.json` GitHub Release asset,
but they are not baked into the factory filesystem.

The badge installs each app into `/apps/<app>/` from the Community Apps screen.
Use this area for community contributions, larger examples, and apps that
should stay outside the default home menu.

## Current Community Contributions

| App | Contributor | Notes |
|---|---|---|
| Tardigotchi | aask42 | Hatch and care for a tiny tardigrade. |
| Durable Snake | Alexandre Roman | Snake game with three retries. |
| Starfield Nametag | Alexandre Roman | Animated starfield with a personalized nametag. |

## Adding an App

Create one folder per app. Use a lowercase slug with underscores, because the
badge installs the folder name directly under `/apps/`:

```text
my_app/
  main.py
  community.json
  README.md
  icon.py
  engine.py
```

Required files:

- `main.py`: entry point the badge runs after install.
- `community.json`: registry metadata used by the Community Apps screen.
- `README.md`: short user/reviewer notes for the app.

`community.json` must include at least:

```json
{
  "name": "My App",
  "description": "Short menu description.",
  "contributors": ["Your Name <you@example.com>"]
}
```

Keep the description brief; it appears on a small screen.
Declare the app license in `community.json` or the app README, and include
third-party asset or library notices when the app bundles anything you did not
author.

Include metadata near the top of `main.py` so the installed app displays well
in the on-badge Apps menu:

```python
__title__ = "My App"
__description__ = "Short menu description"
__icon__ = "/apps/my_app/icon.py"
```

Use the badge UI vocabulary in on-screen text: `A`, `B`, `X`, `Y`, `Menu`, and
`Select`. Avoid keyboard-centric prompts like "press enter" or platform-specific
phrases like "press x" in lowercase.

Apps should provide a clear way back to the menu, avoid writing outside their
own `/apps/<app>/` folder unless the user explicitly asks, and keep network use
predictable.

## Local Validation

From the repo root:

```sh
python3 firmware/scripts/generate_startup_files.py
python3 -m json.tool firmware/build/community_apps.json > /dev/null
python3 -m py_compile community_apps/my_app/*.py
```

If your app has subfolders, compile those Python files too.

The GitHub release workflow regenerates the registry before building firmware
and uploads it as `community_apps.json`. Do not commit generated registry
output; commit only app source, metadata, docs, and notices.

Community App pull requests also run an automated submission review. It checks
folder shape, metadata, common MicroPython risks, docs impact, licensing, and
whether changed firmware or app behavior needs matching docs updates.
