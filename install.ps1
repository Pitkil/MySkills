param(
  [switch]$Force
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$ManifestPath = Join-Path $RepoRoot "skills-manifest.json"
$Manifest = Get-Content -Raw -LiteralPath $ManifestPath | ConvertFrom-Json

foreach ($Skill in $Manifest.skills) {
  $Source = Join-Path $RepoRoot $Skill.path
  $Base = if ($Skill.target -eq "codex") {
    Join-Path $HOME ".codex\skills"
  } else {
    Join-Path $HOME ".agents\skills"
  }
  $Destination = Join-Path $Base $Skill.name

  if (-not (Test-Path -LiteralPath $Source)) {
    Write-Warning "Missing source: $Source"
    continue
  }

  New-Item -ItemType Directory -Force -Path $Base | Out-Null

  if (Test-Path -LiteralPath $Destination) {
    if (-not $Force) {
      Write-Host "Skip existing skill: $($Skill.name). Re-run with -Force to overwrite."
      continue
    }
    Remove-Item -LiteralPath $Destination -Recurse -Force
  }

  Copy-Item -LiteralPath $Source -Destination $Destination -Recurse -Force
  Write-Host "Installed $($Skill.name) -> $Destination"
}

Write-Host "Done. Restart Codex if the new skills do not appear immediately."
