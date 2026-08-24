# MySkills

Personal Codex skill backup, organized by category so a new environment can clone the repo and restore the same working setup.

Repository: [Pitkil/MySkills](https://github.com/Pitkil/MySkills)

## What Is Included

This repo contains 25 non-system skills collected from:

- `~/.agents/skills`
- `~/.codex/skills`

The built-in Codex system skills from `~/.codex/skills/.system` are intentionally excluded because they are managed by Codex itself.

## Categories

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
git clone https://github.com/Pitkil/MySkills.git
cd MySkills
```

On Windows PowerShell:

```powershell
.\install.ps1
```

On macOS or Linux:

```bash
bash install.sh
```

By default, existing skill folders are skipped. To overwrite them:

```powershell
.\install.ps1 -Force
```

```bash
bash install.sh --force
```

## Install Targets

The restore scripts use `skills-manifest.json` to install each skill to its original runtime home:

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
