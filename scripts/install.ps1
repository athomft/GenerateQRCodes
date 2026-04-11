$ErrorActionPreference = "Stop"

# Wait briefly in case this was called from the app's --update command to release file locks
Start-Sleep -Seconds 2

$Repo = "athomft/GenerateQRCodes"
$BinName = "genqr.exe"

$InstallDir = "$env:USERPROFILE\.local\bin"
if (-not (Test-Path $InstallDir)) {
    New-Item -ItemType Directory -Force -Path $InstallDir | Out-Null
}

$ApiPath = "https://api.github.com/repos/$Repo/releases/latest"
Write-Host "Looking for the latest release..."
$Release = Invoke-RestMethod -Uri $ApiPath

$Asset = $Release.assets | Where-Object { $_.name -match "Windows" }

if (-not $Asset) {
    Write-Host "Could not find a Windows release."
    exit 1
}

$DownloadUrl = $Asset.browser_download_url
$DestPath = "$InstallDir\$BinName"

Write-Host "Downloading $BinName from $DownloadUrl..."
Invoke-WebRequest -Uri $DownloadUrl -OutFile $DestPath

Write-Host ""
Write-Host "✓ genqr installed successfully to $DestPath"

$UserPath = [Environment]::GetEnvironmentVariable("PATH", "User")
if ($UserPath -notmatch [regex]::Escape($InstallDir)) {
    Write-Host "Adding $InstallDir to your User PATH..."
    [Environment]::SetEnvironmentVariable("PATH", "$UserPath;$InstallDir", "User")
    Write-Host "ℹ️  Please restart your terminal to use the 'genqr' command."
}
