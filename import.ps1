$currentUser = $env:USERNAME
$zipUrl = "https://github.com/fivance/sublime/raw/main/Sublime Text.zip"
$zipPath = "$env:TEMP\Sublime Text.zip"
$destinationPath = "C:\Users\$currentUser\AppData\Roaming\Sublime Text"

Invoke-WebRequest -Uri $zipUrl -OutFile $zipPath

if (!(Test-Path -Path $destinationPath)) {
    Write-Host "Destination folder not found: $destinationPath"
    exit 1
}

Remove-Item -Path "$destinationPath\*" -Recurse -Force

Add-Type -AssemblyName System.IO.Compression.FileSystem
[System.IO.Compression.ZipFile]::ExtractToDirectory($zipPath, $destinationPath)

Remove-Item -Path $zipPath -Force

Read-Host "Done: Sublime Text.zip extracted and configuration applied."

