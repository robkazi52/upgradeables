[CmdletBinding()]
param(
    [string]$Ref = "v0.3-project-harness",
    [int]$PullRequest = 1,
    [switch]$SkipPrChecks,
    [switch]$SkipInstall,
    [switch]$UseSource,
    [switch]$KeepTemp
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$Repository = "https://github.com/robkazi52/upgradeables.git"
$RepoRoot = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot ".."))
$OriginalPythonPath = $env:PYTHONPATH
$SmokeRoot = Join-Path ([System.IO.Path]::GetTempPath()) ("upgradeables-v03-smoke-" + [guid]::NewGuid().ToString("N"))
$Utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$script:HarnessExecutable = $null

function Assert-True {
    param([bool]$Condition, [string]$Message)
    if (-not $Condition) {
        throw $Message
    }
}

function Invoke-External {
    param(
        [string]$Label,
        [scriptblock]$Command,
        [switch]$Capture
    )
    Write-Host "[RUN] $Label"
    $Output = & $Command
    $ExitCode = $LASTEXITCODE
    if ($null -ne $ExitCode -and $ExitCode -ne 0) {
        throw "$Label failed with exit code $ExitCode"
    }
    if ($Capture) {
        return ,$Output
    }
    if ($null -ne $Output) {
        $Output | ForEach-Object { Write-Host $_ }
    }
}

function Invoke-Upgradeables {
    param([string[]]$CommandArgs, [switch]$Capture)
    if ($UseSource) {
        return Invoke-External "upgradeables $($CommandArgs -join ' ')" {
            & python -m upgradeables_harness @CommandArgs
        } -Capture:$Capture
    }
    return Invoke-External "upgradeables $($CommandArgs -join ' ')" {
        & $script:HarnessExecutable @CommandArgs
    } -Capture:$Capture
}

function Invoke-UpgradeablesJson {
    param([string[]]$CommandArgs)
    $Output = Invoke-Upgradeables -CommandArgs $CommandArgs -Capture
    $Text = $Output -join [Environment]::NewLine
    try {
        return $Text | ConvertFrom-Json
    }
    catch {
        throw "Command did not return valid JSON: upgradeables $($CommandArgs -join ' ')"
    }
}

function Get-TreeFingerprint {
    param([string]$Path)
    $Root = [System.IO.Path]::GetFullPath($Path).TrimEnd('\')
    $Rows = Get-ChildItem -LiteralPath $Root -File -Recurse | Sort-Object FullName | ForEach-Object {
        $Relative = $_.FullName.Substring($Root.Length).TrimStart('\').Replace('\', '/')
        $Hash = (Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash
        "$Relative`t$Hash"
    }
    return $Rows -join "`n"
}

try {
    [System.IO.Directory]::CreateDirectory($SmokeRoot) | Out-Null

    if (-not $SkipPrChecks) {
        Assert-True ($null -ne (Get-Command gh -ErrorAction SilentlyContinue)) "GitHub CLI (gh) is required."
        Invoke-External "wait for PR #$PullRequest checks" {
            & gh pr checks $PullRequest --repo robkazi52/upgradeables --watch
        }
    }

    if ($UseSource) {
        $SourcePath = Join-Path $RepoRoot "src"
        $env:PYTHONPATH = if ([string]::IsNullOrWhiteSpace($OriginalPythonPath)) {
            $SourcePath
        }
        else {
            "$SourcePath$([System.IO.Path]::PathSeparator)$OriginalPythonPath"
        }
    }
    elseif (-not $SkipInstall) {
        $Spec = "git+$Repository@$Ref"
        $Pipx = Get-Command pipx -ErrorAction SilentlyContinue
        if ($null -ne $Pipx) {
            Invoke-External "install $Spec with pipx" { & $Pipx.Source install --force $Spec }
            $InstalledCommand = Get-Command upgradeables -ErrorAction SilentlyContinue
            Assert-True ($null -ne $InstalledCommand) "pipx installed the package, but the upgradeables command is not on PATH."
            $script:HarnessExecutable = $InstalledCommand.Source
        }
        else {
            $Python = Get-Command python -ErrorAction SilentlyContinue
            Assert-True ($null -ne $Python) "Python is required for the disposable virtual-environment fallback."
            $VenvRoot = Join-Path $SmokeRoot ".install-venv"
            Invoke-External "create disposable installation environment" { & $Python.Source -m venv $VenvRoot }
            $VenvPython = Join-Path $VenvRoot "Scripts/python.exe"
            $script:HarnessExecutable = Join-Path $VenvRoot "Scripts/upgradeables.exe"
            Invoke-External "install $Spec in disposable environment" {
                & $VenvPython -m pip install --disable-pip-version-check $Spec
            }
            Assert-True (Test-Path -LiteralPath $script:HarnessExecutable) "The disposable installation did not create the upgradeables command."
        }
    }
    else {
        $InstalledCommand = Get-Command upgradeables -ErrorAction SilentlyContinue
        if ($null -eq $InstalledCommand) {
            throw "upgradeables is not on PATH. Remove -SkipInstall or use -UseSource."
        }
        $script:HarnessExecutable = $InstalledCommand.Source
    }

    Invoke-Upgradeables -CommandArgs @("version")
    Invoke-Upgradeables -CommandArgs @("--help") | Out-Null

    [System.IO.Directory]::CreateDirectory((Join-Path $SmokeRoot "tests")) | Out-Null
    [System.IO.Directory]::CreateDirectory((Join-Path $SmokeRoot "docs")) | Out-Null
    [System.IO.File]::WriteAllText((Join-Path $SmokeRoot "pyproject.toml"), "[project]`nname = `"v03-smoke`"`nversion = `"0.0.0`"`n", $Utf8NoBom)
    [System.IO.File]::WriteAllText((Join-Path $SmokeRoot "tests/test_smoke.py"), "def test_smoke():`n    assert True`n", $Utf8NoBom)
    [System.IO.File]::WriteAllText((Join-Path $SmokeRoot "docs/README.md"), "# Smoke project`n", $Utf8NoBom)
    $OriginalAgentText = "# Existing project instructions`n`nKeep this text unchanged.`n"
    [System.IO.File]::WriteAllText((Join-Path $SmokeRoot "AGENTS.md"), $OriginalAgentText, $Utf8NoBom)

    $Inspection = Invoke-UpgradeablesJson -CommandArgs @("inspect", "--project", $SmokeRoot, "--json")
    Assert-True ($Inspection.languages -contains "python") "Inspection did not detect Python."
    Assert-True ($Inspection.features.tests) "Inspection did not detect tests."

    $FirstInit = Invoke-UpgradeablesJson -CommandArgs @("init", $SmokeRoot, "--json")
    Assert-True ($FirstInit.depth -eq "standard") "Default initialization was not standard depth."
    Assert-True (([System.IO.File]::ReadAllText((Join-Path $SmokeRoot "AGENTS.md"))) -eq $OriginalAgentText) "init modified AGENTS.md."
    $FirstFingerprint = Get-TreeFingerprint (Join-Path $SmokeRoot ".upgradeables")

    $SecondInit = Invoke-UpgradeablesJson -CommandArgs @("init", $SmokeRoot, "--json")
    $SecondFingerprint = Get-TreeFingerprint (Join-Path $SmokeRoot ".upgradeables")
    Assert-True ($FirstFingerprint -eq $SecondFingerprint) "Repeated init was not byte-idempotent."

    $Recommendation = Invoke-UpgradeablesJson -CommandArgs @("recommend", "--project", $SmokeRoot, "--json")
    Assert-True ($Recommendation.selection_only) "Project recommendation crossed the selection/activation boundary."

    $Review = Invoke-UpgradeablesJson -CommandArgs @("task", "review this pull request for bugs and regressions", "--project", $SmokeRoot, "--json")
    Assert-True ($Review.best_recipe.slug -eq "code-review") "PR review did not resolve to code-review."

    $Rename = Invoke-UpgradeablesJson -CommandArgs @("task", "rename this heading from Foo to Bar", "--project", $SmokeRoot, "--json")
    Assert-True ($Rename.complexity.ceiling -eq "L1") "Simple rename exceeded the L1 complexity ceiling."
    Assert-True ($null -eq $Rename.best_recipe) "Simple rename incorrectly forced a recipe."

    Invoke-Upgradeables -CommandArgs @("integrate", "codex", "--project", $SmokeRoot) | Out-Null
    Assert-True (([System.IO.File]::ReadAllText((Join-Path $SmokeRoot "AGENTS.md"))) -eq $OriginalAgentText) "Integration preview modified AGENTS.md."

    Invoke-Upgradeables -CommandArgs @("integrate", "codex", "--project", $SmokeRoot, "--write") | Out-Null
    $ManagedHash = (Get-FileHash -LiteralPath (Join-Path $SmokeRoot "AGENTS.md") -Algorithm SHA256).Hash
    Invoke-Upgradeables -CommandArgs @("integrate", "codex", "--project", $SmokeRoot, "--write") | Out-Null
    $RepeatedManagedHash = (Get-FileHash -LiteralPath (Join-Path $SmokeRoot "AGENTS.md") -Algorithm SHA256).Hash
    Assert-True ($ManagedHash -eq $RepeatedManagedHash) "Repeated managed-block integration was not idempotent."

    Invoke-Upgradeables -CommandArgs @("integrate", "codex", "--project", $SmokeRoot, "--remove") | Out-Null
    $RestoredAgentText = [System.IO.File]::ReadAllText((Join-Path $SmokeRoot "AGENTS.md"))
    Assert-True ($RestoredAgentText.TrimEnd("`r", "`n") -eq $OriginalAgentText.TrimEnd("`r", "`n")) "Managed-block removal changed user text."
    Assert-True (-not $RestoredAgentText.Contains("upgradeables-harness:start")) "Managed-block removal left a start marker."
    Assert-True (-not $RestoredAgentText.Contains("upgradeables-harness:end")) "Managed-block removal left an end marker."

    $Brief = Invoke-UpgradeablesJson -CommandArgs @("skill", "brief", "review API changes for backwards compatibility", "--project", $SmokeRoot, "--json")
    Assert-True ($Brief.primary_recipe -eq "code-review") "Skill brief did not use the code-review recipe."

    Invoke-Upgradeables -CommandArgs @("skill", "scaffold", "api-breaking-change-review", "--task", "review API changes for backwards compatibility", "--project", $SmokeRoot) | Out-Null
    $SkillPath = Join-Path $SmokeRoot ".upgradeables/skills/api-breaking-change-review"
    Invoke-Upgradeables -CommandArgs @("skill", "validate", $SkillPath, "--draft") | Out-Null
    $Skills = Invoke-UpgradeablesJson -CommandArgs @("skill", "list", "--project", $SmokeRoot, "--json")
    Assert-True ($Skills.skills.Count -eq 1) "Scaffolded Skill is missing from the Skill map."

    $Doctor = Invoke-UpgradeablesJson -CommandArgs @("doctor", "--project", $SmokeRoot, "--json")
    Assert-True ($Doctor.status -eq "PASS") "doctor did not report PASS."

    Write-Host ""
    Write-Host "V0.3 RELEASE-CANDIDATE SMOKE TEST: PASS" -ForegroundColor Green
    Write-Host "Ref: $Ref"
    Write-Host "Temporary project: $SmokeRoot"
}
finally {
    $env:PYTHONPATH = $OriginalPythonPath
    if ((Test-Path -LiteralPath $SmokeRoot) -and -not $KeepTemp) {
        $TempBase = [System.IO.Path]::GetFullPath([System.IO.Path]::GetTempPath()).TrimEnd('\') + '\'
        $ResolvedSmoke = [System.IO.Path]::GetFullPath($SmokeRoot)
        if (-not $ResolvedSmoke.StartsWith($TempBase, [System.StringComparison]::OrdinalIgnoreCase)) {
            throw "Refusing to remove a path outside the system temp directory: $ResolvedSmoke"
        }
        Remove-Item -LiteralPath $ResolvedSmoke -Recurse -Force -ErrorAction SilentlyContinue
    }
}
