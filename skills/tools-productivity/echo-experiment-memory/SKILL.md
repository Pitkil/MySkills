---
name: echo-experiment-memory
description: Maintain durable operational memory for the ECHO formal experiment runtime, deployment, data locations, and validation workflow. Use when updating AGENTS.md, preparing formal runs, deploying the three-condition app, or checking experiment-readiness.
metadata:
  short-description: ECHO experiment memory and readiness
---

# ECHO Experiment Memory

Use this skill for ECHO formal experiment operational memory: AGENTS.md updates, deployment facts, data-root conventions, and readiness checks for the three-condition participant runtime.

## Stable Context

- The formal participant runtime is `ECHO-experiment-main/experiment_runtime/`; do not use the legacy root `app.py` for formal data collection.
- The active design is one AI ethics learning module with about 10 minutes fixed reading and 40 minutes agent dialogue.
- G1, G2, and G3 use the same DeepSeek model/material/interface and differ only by tutor architecture: ordinary structured support, EULER-style Socratic inquiry support, and ECHO reflective support.
- Privacy operations such as de-identification, condition-file shuffling, and shared-coder blinding are manual data-manager procedures after export, not automatic runtime transformations.

## Memory Update Rules

When new durable facts appear, update the workspace `AGENTS.md` Memory Maintenance Log. Record stable operational decisions, validated commands, deployment paths, data locations, public endpoints, and important caveats. Do not store secrets, passwords, API keys, raw participant credentials, or identity mappings.

Prefer concise dated entries. Include enough detail for a future Codex session to avoid rediscovering the same deployment state, but do not turn one-off troubleshooting into universal rules unless it changes future operations.

## Data Location Convention

Formal runtime outputs should remain inside the project unless the user explicitly asks otherwise. The three-container Docker deployment defaults to:

```text
ECHO-experiment-main/experiment_runtime_runs/g1
ECHO-experiment-main/experiment_runtime_runs/g2
ECHO-experiment-main/experiment_runtime_runs/g3
```

Each condition directory contains the SQLite database, manifest, credentials file, and `exports/` CSV output. Treat credentials and raw exports as restricted research-manager artifacts.

## Public Three-App Deployment Checks

For public deployment, verify all three neutral endpoints, not just one:

```text
/a/ -> G1 container, localhost:18101
/b/ -> G2 container, localhost:18102
/c/ -> G3 container, localhost:18103
```

Subpath deployment requires frontend resources and API calls to respect the entry prefix. Check that CSS/JS load under `/a/static`, `/b/static`, and `/c/static`, and that browser token storage is scoped per entry so accounts do not bleed across conditions on the same host.

## Readiness Checklist

Before a pilot or formal run, verify:

- containers are healthy for all three conditions;
- Nginx routes all three public entries;
- at least one account per condition can log in, read material, start dialogue, send a message, refresh/resume, and end;
- exports produce `sessions.csv`, `messages.csv`, and `quality_report.csv` for all three groups;
- no pending/error rows remain unexplained after the test;
- material hash and manifest are frozen and identical where required;
- 18101/18102/18103 are not directly exposed if Nginx is the public entry;
- the user has a plan for ICP/domain constraints or is using public IP/temporary access only for testing.
