---
name: premium-readme
description: Create or update polished, complete repository README files from the actual codebase, especially public plugins and developer tools. Use when the user asks to write, improve, beautify, or audit a README.
---

# Premium README

Use this skill when creating, rewriting, or reviewing a repository README. The goal is a README that looks credible on GitHub, helps real users understand the product quickly, and satisfies public-directory expectations such as the Obsidian plugin directory.

## Core Standard

Start from the repository, not from marketing guesses.

- Read the actual code, manifest/package metadata, screenshots, docs, release files, and tests before describing features.
- Do not invent capabilities, providers, platforms, commands, or screenshots that are not present in the project.
- Keep the README complete enough for a first-time user to install, configure, use, evaluate privacy implications, and contribute.
- Make it feel premium and intentional: clean hierarchy, strong opening, centered hero/header when appropriate, good screenshot placement, and compact but vivid feature language.
- Avoid generic AI-product filler, exaggerated claims, and long feature dumps that make the project feel unfinished.

## Public README Shape

Prefer this structure unless the repository clearly calls for something else:

- Centered title block with project name, concise one-sentence positioning, badges, and anchor links.
- A first screenshot or product visual near the top if assets exist.
- Short explanation of what the project is and who it is for.
- Feature table or scannable feature sections grounded in code behavior.
- Screenshots with meaningful captions, not tiny collage dumps.
- Installation instructions.
- Configuration or setup instructions.
- Real user workflows.
- Command/API/reference tables when the project exposes them.
- Privacy, permissions, limitations, and safety notes when user data or external services are involved.
- Development commands and project structure.
- License section.

## Obsidian Plugin Requirements

For Obsidian plugins, apply these additional checks:

- README must contain substantial English text; a Chinese section can be included after the English section.
- Include the plugin name, plugin id when useful, repository link, and Obsidian plugin link when known: `https://obsidian.md/plugins?id=<plugin-id>`.
- Installation must mention the required plugin files: `manifest.json`, `main.js`, and `styles.css` when applicable.
- Version, plugin name, author, description, and `minAppVersion` should match `manifest.json`.
- Explain model/API configuration truthfully, including local models, remote providers, API keys, and any feature limits.
- Describe vault access, clipboard use, OCR/image handling, and network behavior plainly if the plugin does those things.
- Do not imply mobile support unless `isDesktopOnly` and the implementation make that credible.

## Screenshots And Assets

Use screenshots deliberately.

- Prefer existing project screenshots from `docs/screenshots`, README references, or user-provided images.
- If screenshots are missing, tell the user exactly what to capture and where to put each file, using concrete names and paths.
- For visual-heavy products, ask for or create one strong social/hero image only when it materially improves the README.
- Keep screenshots large enough to inspect and centered where appropriate.
- Avoid referencing image files that do not exist.

Suggested screenshot set for an Obsidian AI plugin:

- `docs/screenshots/01-chat-workspace.png`: chat sidebar with model selector and context state.
- `docs/screenshots/02-selection-toolbar.png`: selected text toolbar.
- `docs/screenshots/03-translation-popover.png`: translation result panel.
- `docs/screenshots/04-settings.png`: model/provider settings.
- `docs/screenshots/05-image-context.png`: image or OCR workflow.
- `docs/screenshots/06-format-preview.png`: formatting preview or diff.

## Writing Style

Write like a strong open-source maintainer, not like a brochure.

- Lead with the product's practical value, not a list of technologies.
- Use specific nouns and verbs: "rewrite image links", "store annotations outside Markdown", "estimate context usage".
- Prefer short paragraphs, clean tables, and descriptive captions.
- Put caveats where users need them; this builds trust.
- Keep Chinese text natural when included, but make English sections substantial for international directories.

## Validation

Before finishing, check the README against observable project state.

- Confirm referenced screenshots exist.
- Confirm links are plausible and use the current repository/plugin id.
- Confirm install commands and package scripts exist.
- Confirm version badges and manifest/package versions match.
- Run build/tests when the README update depends on generated artifacts or release files.
- Mention any verification that could not be performed.
