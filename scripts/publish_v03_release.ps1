[CmdletBinding()]
param(
    [switch]$Publish,
    [int]$TimeoutMinutes = 15
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$Tag = "v0.3.0"
$Repository = "robkazi52/upgradeables"
$ExpectedWorkflows = @("Validate", "Harness package")
$ReleaseDirectory = Join-Path $PSScriptRoot "../build/release-v0.3.0"
$ReleaseAssets = @(
    "upgradeables_registry-0.3.0-py3-none-any.whl",
    "upgradeables_registry-0.3.0.tar.gz",
    "ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md",
    "registry.json",
    "registry.yaml",
    "upgradeable_task_priors.json",
    "SELECTION_ONTOLOGY_REVIEW_v0.3.md",
    "SHA256SUMS_v0.3.0.txt"
) | ForEach-Object { Join-Path $ReleaseDirectory $_ }

function Invoke-Checked {
    param([string]$Label, [scriptblock]$Command)
    Write-Host "[RUN] $Label"
    $Output = & $Command
    if ($LASTEXITCODE -ne 0) {
        throw "$Label failed with exit code $LASTEXITCODE"
    }
    if ($null -ne $Output) {
        $Output | ForEach-Object { Write-Host $_ }
    }
}

if ((& git branch --show-current) -ne "main") {
    throw "Release publication must run from main."
}
if (@(& git status --porcelain).Count -ne 0) {
    throw "Release publication requires a clean working tree."
}
if ((& python -c "import tomllib; print(tomllib.load(open('pyproject.toml','rb'))['project']['version'])") -ne "0.3.0") {
    throw "pyproject.toml does not declare version 0.3.0."
}

Invoke-Checked "verify staged release assets" { & python scripts/prepare_v03_release_assets.py --check }
foreach ($Asset in $ReleaseAssets) {
    if (-not (Test-Path -LiteralPath $Asset -PathType Leaf)) {
        throw "Missing release asset: $Asset"
    }
}

$Head = (& git rev-parse HEAD).Trim()
Write-Host "Release commit: $Head"
Write-Host "Release tag: $Tag"

if (-not $Publish) {
    Write-Host "Release is prepared. Re-run with -Publish to push main, wait for CI, tag, and publish."
    exit 0
}

Invoke-Checked "verify GitHub authentication" { & gh auth status }
Invoke-Checked "push main" { & git push origin main }

$Deadline = [DateTime]::UtcNow.AddMinutes($TimeoutMinutes)
do {
    $RunJson = & gh run list --repo $Repository --branch main --commit $Head --limit 20 --json databaseId,name,status,conclusion,url
    if ($LASTEXITCODE -ne 0) {
        throw "Could not query GitHub Actions runs."
    }
    $Runs = @($RunJson | ConvertFrom-Json)
    $Selected = @{}
    foreach ($Workflow in $ExpectedWorkflows) {
        $Selected[$Workflow] = $Runs | Where-Object { $_.name -eq $Workflow } | Select-Object -First 1
    }
    $Missing = @($ExpectedWorkflows | Where-Object { $null -eq $Selected[$_] })
    $Pending = @($ExpectedWorkflows | Where-Object { $null -ne $Selected[$_] -and $Selected[$_].status -ne "completed" })
    if ($Missing.Count -eq 0 -and $Pending.Count -eq 0) {
        $Failed = @($ExpectedWorkflows | Where-Object { $Selected[$_].conclusion -ne "success" })
        if ($Failed.Count -gt 0) {
            foreach ($Workflow in $Failed) {
                Write-Host "$Workflow failed: $($Selected[$Workflow].url)"
            }
            throw "Required GitHub Actions checks did not pass."
        }
        break
    }
    if ([DateTime]::UtcNow -ge $Deadline) {
        throw "Timed out waiting for main-branch GitHub Actions checks."
    }
    $WaitingFor = @($Missing + $Pending) -join ", "
    Write-Host "Waiting for: $WaitingFor"
    Start-Sleep -Seconds 10
} while ($true)

Write-Host "Required GitHub Actions checks passed."

$ExistingTag = & git rev-parse -q --verify "refs/tags/$Tag" 2>$null
if ($LASTEXITCODE -eq 0) {
    if ($ExistingTag.Trim() -ne $Head) {
        throw "$Tag already exists at a different commit."
    }
}
else {
    Invoke-Checked "create annotated $Tag tag" { & git tag -a $Tag -m "Upgradeables v0.3.0" $Head }
}

Invoke-Checked "push $Tag" { & git push origin $Tag }

& gh release view $Tag --repo $Repository *> $null
if ($LASTEXITCODE -eq 0) {
    throw "GitHub release $Tag already exists; refusing to overwrite it."
}

Write-Host "[RUN] publish GitHub release $Tag"
& gh release create $Tag `
    --repo $Repository `
    --verify-tag `
    --title "Upgradeables v0.3.0 - Project Harness and Skill Factory" `
    --notes-file RELEASE_NOTES_v0.3.0.md `
    @ReleaseAssets
if ($LASTEXITCODE -ne 0) {
    throw "GitHub release publication failed with exit code $LASTEXITCODE"
}

Write-Host "V0.3.0 RELEASE: PUBLISHED" -ForegroundColor Green
