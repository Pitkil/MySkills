#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
force="${1:-}"

python3 - "$repo_root" "$force" <<'PY'
import json
import os
import shutil
import sys
from pathlib import Path

repo_root = Path(sys.argv[1])
force = sys.argv[2] in {"--force", "-f"}
manifest = json.loads((repo_root / "skills-manifest.json").read_text(encoding="utf-8"))
home = Path.home()

for skill in manifest["skills"]:
    source = repo_root / skill["path"]
    base = home / (".codex/skills" if skill["target"] == "codex" else ".agents/skills")
    destination = base / skill["name"]

    if not source.exists():
        print(f"Missing source: {source}", file=sys.stderr)
        continue

    base.mkdir(parents=True, exist_ok=True)

    if destination.exists():
        if not force:
            print(f"Skip existing skill: {skill['name']}. Re-run with --force to overwrite.")
            continue
        shutil.rmtree(destination)

    shutil.copytree(source, destination)
    print(f"Installed {skill['name']} -> {destination}")

print("Done. Restart Codex if the new skills do not appear immediately.")
PY
