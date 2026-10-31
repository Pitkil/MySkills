param(
  [switch]$Force,
  [switch]$DryRun,
  [switch]$Check,
  [string[]]$Only = @(),
  [string]$Python = "python"
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$RestoreArgs = @((Join-Path $RepoRoot "scripts\restore-skills.py"))
if ($Force) { $RestoreArgs += "--force" }
if ($DryRun) { $RestoreArgs += "--dry-run" }
if ($Check) { $RestoreArgs += "--check" }
foreach ($Name in $Only) { $RestoreArgs += @("--only", $Name) }
& $Python @RestoreArgs
if ($LASTEXITCODE -ne 0) { throw "Restore failed with exit code $LASTEXITCODE" }
