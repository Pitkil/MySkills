# MySkills

Personal Codex skill backup, organized by category so a new environment can clone the repo and restore the same working setup.

Repository: [Pitkil/MySkills](https://github.com/Pitkil/MySkills)

## What Is Included

The current snapshot (2026-10-31) contains **46 standalone skills and 11 complete packages**, totaling **579 SKILL.md files**, collected from:

- `~/.agents/skills`
- `~/.codex/skills`

The built-in Codex system skills from `~/.codex/skills/.system` are intentionally excluded because they are managed by Codex itself.

## Categories

See [CATALOG.md](CATALOG.md) for the current categorized index and package list. [inventory.json](inventory.json) records archived file hashes and repeated skill names. Hashes normalize CRLF to LF for UTF-8 text so verification also works after a cross-platform Git clone.

### ASu-skills

Installed and archived all nine entries of [Hisn00w/ASu-skills](https://github.com/Hisn00w/ASu-skills) at upstream commit `d27fd2a3864c48472a5c8ed942410098ba9cd35f` (MIT): `contributor`, `evidence-recap`, `project-guide`, `great-resume`, `make-resume`, `job-match`, `job-apply`, `interview`, `offer`.

The complete package is stored in `collections/installed-packages/asu-skills` and restored to `~/.codex/skills/asu-skills`, including shared templates, scripts, references and license. This is a filesystem skill installation, not a registration in the app's plugin manager.

### Organization policy

- Preserve upstream package boundaries and relative resource paths.
- Reuse identical pinned packages from the existing collection instead of creating duplicate copies.
- Index the 111 repeated names by package and variant; do not silently delete or replace active local variants.
- Exclude system-managed skills, plugin caches, environment credentials, private keys, databases and runtime caches.
- Retain each upstream license; do not apply a blanket license to the collection.

## Additional Video Workflow Collection

The pinned historical collection is available at [collections/video-paper-workflow](collections/video-paper-workflow/README.md), with source commits, file hashes, and upstream licenses. The current restore manifest reuses the ten packages from that collection that are currently installed locally. Other historical entries are not automatically installed. One unlicensed source remains indexed by link only.

## Original Skill Categories

| Category | Purpose | Skills |
| --- | --- | --- |
| `academic-research` | Research, literature review, academic writing, paper review, and full research-to-paper workflows. | `academic-paper`, `academic-paper-reviewer`, `academic-pipeline`, `deep-research` |
| `writing-language` | Copywriting, Chinese humanization, README work, and complete-output controls. | `copywriting`, `full-output-enforcement`, `humanizer-zh`, `premium-readme` |
| `frontend-ui-design` | Frontend design, visual polish, design systems, web redesigns, and style-specific UI guidance. | `design-taste-frontend`, `design-taste-frontend-v1`, `frontend-design`, `gpt-taste`, `high-end-visual-design`, `industrial-brutalist-ui`, `minimalist-ui`, `redesign-existing-projects`, `stitch-design-taste`, `ui-ux-pro-max` |
| `image-brand-generation` | Brand systems, image-led design direction, mobile/web mockups, and image-to-code workflows. | `brandkit`, `image-to-code`, `imagegen-frontend-mobile`, `imagegen-frontend-web` |
| `tools-productivity` | Skill discovery, Office CLI work, and project-specific operational memory. | `echo-experiment-memory`, `find-skills`, `officecli` |

## Restore On A New Machine

Clone the repository:

```bash
git -c core.longpaths=true clone https://github.com/Pitkil/MySkills.git
cd MySkills
```

On Windows PowerShell:

The clone command enables long paths for the bundled upstream collections on Windows. If an existing clone reported `Filename too long`, enable it locally with `git config core.longpaths true`, then restore only the missing files after preserving any local edits.

```powershell
.\install.ps1
```

On macOS or Linux:

```bash
bash install.sh
```

Python 3.10 or newer is required. Preview or validate the archive before restoring:

```powershell
.\install.ps1 -DryRun
.\install.ps1 -Check
.\install.ps1 -Only asu-skills
```

```bash
bash install.sh --dry-run
bash install.sh --check
bash install.sh --only asu-skills
```

By default, existing skill folders are skipped. With `-Force` / `--force`, the previous folder is moved to a dated `~/.codex/skill-backups/` directory before restoring:

```powershell
.\install.ps1 -Force
```

```bash
bash install.sh --force
```

## Install Targets

The restore scripts use `skills-manifest.json` (standalone `skills` plus complete `packages`) to install each item to its original runtime home:

| Manifest target | Destination |
| --- | --- |
| `agents` | `~/.agents/skills/<skill-name>` |
| `codex` | `~/.codex/skills/<skill-name>` |

## Adding New Skills Later

Use the existing category layout:

```text
skills/<category>/<skill-name>/SKILL.md
```

Then add an entry to `skills-manifest.json`:

```json
{
  "name": "my-new-skill",
  "category": "tools-productivity",
  "target": "agents",
  "path": "skills/tools-productivity/my-new-skill"
}
```

Choose `target: "agents"` for skills that normally live under `~/.agents/skills`, and `target: "codex"` for personal Codex skills that normally live under `~/.codex/skills`.

## Maintenance Checklist

Before pushing updates:

1. Put each skill in the closest existing category.
2. Confirm every skill folder contains `SKILL.md`.
3. Update `skills-manifest.json`.
4. Run `git status` and review the diff.
5. Commit and push to GitHub.

## Notes

- Plugin cache skills are not copied from Codex plugin cache directories.
- System-managed skills are not copied from `.codex/skills/.system`.
- Some skills may reference local tools or external services. Restore the skill files first, then install any tool dependencies mentioned inside the individual `SKILL.md` files.
