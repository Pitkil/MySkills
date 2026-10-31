# Workflow

| Stage | Goal | Inputs | Outputs | Checkpoint |
|---|---|---|---|---|
| 0 Initialization | Reproducible project | Data locations, protocol, venue when known | Project folders, README, dictionary, analysis plan | Raw/derived separation, environment, seeds, replay commands |
| 1 Positioning | Claim, contributions, gap | Research question, protocol/results and nearest papers as later supplied | One-sentence claim, up to three supported contributions, evidence map | Venue fit; objections; claim no stronger than evidence |
| 2 Literature | 20-30 relevant papers | Research question, authorized Zotero exports/PDFs | Literature matrix, supported gap | DOI/source verification; no fabricated records |
| 3 Statistics | Freeze reproducible results | Raw data, dictionary, design, analysis plan | Cleaning/analysis scripts, tables, plots, sensitivity analyses | Unit of analysis, dependence, assumptions, missingness, multiplicity, effect sizes and CIs |
| 4 Figures | Figure-driven story | Verified results | Figure 1-5 messages, panels, result sentences, source mapping | One message per figure; actual count may vary with venue/evidence |
| 5 Outline | Logical story | Figures and literature | Section outline, claim-evidence links | Alternatives and limitations; no unsupported links |
| 6 Writing | Evidence-based sections | Protocol, figures, tables, outline, verified references | Methods -> Results -> Discussion -> Introduction -> Abstract -> Title | Results separate from interpretation; ethics/sample details sourced |
| 7 Review | Three review perspectives | Full manuscript and evidence | Methodology/domain/statistics major/minor comments and response table | Resolve or explicitly acknowledge objections; simulations not independent proof |
| 8 Submission | Verified submission package | Revised manuscript, venue rules | Language/format/citation edits, disclosure, cover letter and required extras | Current venue AI policy; traceability; similarity screening only if a real service is available |
| 9 Presentation/tracking | Faithful dissemination | Final paper, confirmed tracking preferences | HTML slides; scheduled literature updates when requested | No new data; unchanged monitor state stays quiet |

Stage 0 is pending during initial stage 1 intake. Reconcile its completion with the user before substantive analysis; never mark it complete because the skill was installed.

Project layout, created during stage 0 after choosing a project root:
`manuscript/ literature/ data/raw/ data/processed/ scripts/ figures/ tables/ refs/ prompts/ logs/`.
Record protocol, variable definitions, ethics details, software versions, statistical plan, raw-file hashes, and commands without exposing sensitive identifiers. Do not impose normality/variance tests indiscriminately: diagnostics must match the model, design, and estimand. Distinguish planned analyses from exploratory analyses since data already exist.
